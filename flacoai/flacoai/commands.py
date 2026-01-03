import glob
import os
import re
import subprocess
import sys
import tempfile
from collections import OrderedDict
from os.path import expanduser
from pathlib import Path

import pyperclip
from PIL import Image, ImageGrab
from prompt_toolkit.completion import Completion, PathCompleter
from prompt_toolkit.document import Document

from flacoai import models, prompts, voice
from flacoai.editor import pipe_editor
from flacoai.format_settings import format_settings
from flacoai.help import Help, install_help_extra
from flacoai.io import CommandCompletionException
from flacoai.llm import litellm
from flacoai.repo import ANY_GIT_ERROR
from flacoai.run_cmd import run_cmd
from flacoai.scrape import Scraper, install_playwright
from flacoai.utils import is_image_file

from .dump import dump  # noqa: F401


class SwitchCoder(Exception):
    def __init__(self, placeholder=None, **kwargs):
        self.kwargs = kwargs
        self.placeholder = placeholder


class Commands:
    voice = None
    scraper = None

    def clone(self):
        return Commands(
            self.io,
            None,
            voice_language=self.voice_language,
            verify_ssl=self.verify_ssl,
            args=self.args,
            parser=self.parser,
            verbose=self.verbose,
            editor=self.editor,
            original_read_only_fnames=self.original_read_only_fnames,
        )

    def __init__(
        self,
        io,
        coder,
        voice_language=None,
        voice_input_device=None,
        voice_format=None,
        verify_ssl=True,
        args=None,
        parser=None,
        verbose=False,
        editor=None,
        original_read_only_fnames=None,
    ):
        self.io = io
        self.coder = coder
        self.parser = parser
        self.args = args
        self.verbose = verbose

        self.verify_ssl = verify_ssl
        if voice_language == "auto":
            voice_language = None

        self.voice_language = voice_language
        self.voice_format = voice_format
        self.voice_input_device = voice_input_device

        self.help = None
        self.editor = editor

        # Store the original read-only filenames provided via args.read
        self.original_read_only_fnames = set(original_read_only_fnames or [])

        # Track commands used in this session for activity tracking
        self.used_commands = []

    def _track_command(self, command_name):
        """Track command usage for activity analytics."""
        if command_name not in self.used_commands:
            self.used_commands.append(command_name)

    def cmd_model(self, args):
        "Switch the Main Model to a new LLM"

        model_name = args.strip()
        if not model_name:
            announcements = "\n".join(self.coder.get_announcements())
            self.io.tool_output(announcements)
            return

        model = models.Model(
            model_name,
            editor_model=self.coder.main_model.editor_model.name,
            weak_model=self.coder.main_model.weak_model.name,
        )
        models.sanity_check_models(self.io, model)

        # Check if the current edit format is the default for the old model
        old_model_edit_format = self.coder.main_model.edit_format
        current_edit_format = self.coder.edit_format

        new_edit_format = current_edit_format
        if current_edit_format == old_model_edit_format:
            # If the user was using the old model's default, switch to the new model's default
            new_edit_format = model.edit_format

        raise SwitchCoder(main_model=model, edit_format=new_edit_format)

    def cmd_editor_model(self, args):
        "Switch the Editor Model to a new LLM"

        model_name = args.strip()
        model = models.Model(
            self.coder.main_model.name,
            editor_model=model_name,
            weak_model=self.coder.main_model.weak_model.name,
        )
        models.sanity_check_models(self.io, model)
        raise SwitchCoder(main_model=model)

    def cmd_weak_model(self, args):
        "Switch the Weak Model to a new LLM"

        model_name = args.strip()
        model = models.Model(
            self.coder.main_model.name,
            editor_model=self.coder.main_model.editor_model.name,
            weak_model=model_name,
        )
        models.sanity_check_models(self.io, model)
        raise SwitchCoder(main_model=model)

    def cmd_chat_mode(self, args):
        "Switch to a new chat mode"

        from flacoai import coders

        ef = args.strip()
        valid_formats = OrderedDict(
            sorted(
                (
                    coder.edit_format,
                    coder.__doc__.strip().split("\n")[0] if coder.__doc__ else "No description",
                )
                for coder in coders.__all__
                if getattr(coder, "edit_format", None)
            )
        )

        show_formats = OrderedDict(
            [
                ("help", "Get help about using flacoai (usage, config, troubleshoot)."),
                ("ask", "Ask questions about your code without making any changes."),
                ("code", "Ask for changes to your code (using the best edit format)."),
                (
                    "architect",
                    (
                        "Work with an architect model to design code changes, and an editor to make"
                        " them."
                    ),
                ),
                (
                    "context",
                    "Automatically identify which files will need to be edited.",
                ),
            ]
        )

        if ef not in valid_formats and ef not in show_formats:
            if ef:
                self.io.tool_error(f'Chat mode "{ef}" should be one of these:\n')
            else:
                self.io.tool_output("Chat mode should be one of these:\n")

            max_format_length = max(len(format) for format in valid_formats.keys())
            for format, description in show_formats.items():
                self.io.tool_output(f"- {format:<{max_format_length}} : {description}")

            self.io.tool_output("\nOr a valid edit format:\n")
            for format, description in valid_formats.items():
                if format not in show_formats:
                    self.io.tool_output(f"- {format:<{max_format_length}} : {description}")

            return

        summarize_from_coder = True
        edit_format = ef

        if ef == "code":
            edit_format = self.coder.main_model.edit_format
            summarize_from_coder = False
        elif ef == "ask":
            summarize_from_coder = False

        raise SwitchCoder(
            edit_format=edit_format,
            summarize_from_coder=summarize_from_coder,
        )

    def completions_model(self):
        models = litellm.model_cost.keys()
        return models

    def cmd_models(self, args):
        "Search the list of available models"

        args = args.strip()

        if args:
            models.print_matching_models(self.io, args)
        else:
            self.io.tool_output("Please provide a partial model name to search for.")

    def cmd_web(self, args, return_content=False):
        "Scrape a webpage, convert to markdown and send in a message"

        url = args.strip()
        if not url:
            self.io.tool_error("Please provide a URL to scrape.")
            return

        self.io.tool_output(f"Scraping {url}...")
        if not self.scraper:
            disable_playwright = getattr(self.args, "disable_playwright", False)
            if disable_playwright:
                res = False
            else:
                res = install_playwright(self.io)
                if not res:
                    self.io.tool_warning("Unable to initialize playwright.")

            self.scraper = Scraper(
                print_error=self.io.tool_error,
                playwright_available=res,
                verify_ssl=self.verify_ssl,
            )

        content = self.scraper.scrape(url) or ""
        content = f"Here is the content of {url}:\n\n" + content
        if return_content:
            return content

        self.io.tool_output("... added to chat.")

        self.coder.cur_messages += [
            dict(role="user", content=content),
            dict(role="assistant", content="Ok."),
        ]

    def is_command(self, inp):
        return inp[0] in "/!"

    def get_raw_completions(self, cmd):
        assert cmd.startswith("/")
        cmd = cmd[1:]
        cmd = cmd.replace("-", "_")

        raw_completer = getattr(self, f"completions_raw_{cmd}", None)
        return raw_completer

    def get_completions(self, cmd):
        assert cmd.startswith("/")
        cmd = cmd[1:]

        cmd = cmd.replace("-", "_")
        fun = getattr(self, f"completions_{cmd}", None)
        if not fun:
            return
        return sorted(fun())

    def get_commands(self):
        commands = []
        for attr in dir(self):
            if not attr.startswith("cmd_"):
                continue
            cmd = attr[4:]
            cmd = cmd.replace("_", "-")
            commands.append("/" + cmd)

        return commands

    def do_run(self, cmd_name, args):
        cmd_name = cmd_name.replace("-", "_")
        cmd_method_name = f"cmd_{cmd_name}"
        cmd_method = getattr(self, cmd_method_name, None)
        if not cmd_method:
            self.io.tool_output(f"Error: Command {cmd_name} not found.")
            return

        try:
            return cmd_method(args)
        except ANY_GIT_ERROR as err:
            self.io.tool_error(f"Unable to complete {cmd_name}: {err}")

    def matching_commands(self, inp):
        words = inp.strip().split()
        if not words:
            return

        first_word = words[0]
        rest_inp = inp[len(words[0]) :].strip()

        all_commands = self.get_commands()
        matching_commands = [cmd for cmd in all_commands if cmd.startswith(first_word)]
        return matching_commands, first_word, rest_inp

    def run(self, inp):
        if inp.startswith("!"):
            self.coder.event("command_run")
            return self.do_run("run", inp[1:])

        res = self.matching_commands(inp)
        if res is None:
            return
        matching_commands, first_word, rest_inp = res
        if len(matching_commands) == 1:
            command = matching_commands[0][1:]
            self.coder.event(f"command_{command}")
            return self.do_run(command, rest_inp)
        elif first_word in matching_commands:
            command = first_word[1:]
            self.coder.event(f"command_{command}")
            return self.do_run(command, rest_inp)
        elif len(matching_commands) > 1:
            self.io.tool_error(f"Ambiguous command: {', '.join(matching_commands)}")
        else:
            self.io.tool_error(f"Invalid command: {first_word}")

    # any method called cmd_xxx becomes a command automatically.
    # each one must take an args param.

    def cmd_commit(self, args=None):
        "Commit edits to the repo made outside the chat (commit message optional)"
        try:
            self.raw_cmd_commit(args)
        except ANY_GIT_ERROR as err:
            self.io.tool_error(f"Unable to complete commit: {err}")

    def raw_cmd_commit(self, args=None):
        if not self.coder.repo:
            self.io.tool_error("No git repository found.")
            return

        if not self.coder.repo.is_dirty():
            self.io.tool_warning("No more changes to commit.")
            return

        commit_message = args.strip() if args else None
        self.coder.repo.commit(message=commit_message, coder=self.coder)

    def cmd_lint(self, args="", fnames=None):
        "Lint and fix in-chat files or all dirty files if none in chat"

        if not self.coder.repo:
            self.io.tool_error("No git repository found.")
            return

        if not fnames:
            fnames = self.coder.get_inchat_relative_files()

        # If still no files, get all dirty files in the repo
        if not fnames and self.coder.repo:
            fnames = self.coder.repo.get_dirty_files()

        if not fnames:
            self.io.tool_warning("No dirty files to lint.")
            return

        fnames = [self.coder.abs_root_path(fname) for fname in fnames]

        lint_coder = None
        for fname in fnames:
            try:
                errors = self.coder.linter.lint(fname)
            except FileNotFoundError as err:
                self.io.tool_error(f"Unable to lint {fname}")
                self.io.tool_output(str(err))
                continue

            if not errors:
                continue

            self.io.tool_output(errors)
            if not self.io.confirm_ask(f"Fix lint errors in {fname}?", default="y"):
                continue

            # Commit everything before we start fixing lint errors
            if self.coder.repo.is_dirty() and self.coder.dirty_commits:
                self.cmd_commit("")

            if not lint_coder:
                lint_coder = self.coder.clone(
                    # Clear the chat history, fnames
                    cur_messages=[],
                    done_messages=[],
                    fnames=None,
                )

            lint_coder.add_rel_fname(fname)
            lint_coder.run(errors)
            lint_coder.abs_fnames = set()

        if lint_coder and self.coder.repo.is_dirty() and self.coder.auto_commits:
            self.cmd_commit("")

    def cmd_clear(self, args):
        "Clear the chat history"

        self._clear_chat_history()
        self.io.tool_output("All chat history cleared.")

    def _drop_all_files(self):
        self.coder.abs_fnames = set()

        # When dropping all files, keep those that were originally provided via args.read
        if self.original_read_only_fnames:
            # Keep only the original read-only files
            to_keep = set()
            for abs_fname in self.coder.abs_read_only_fnames:
                rel_fname = self.coder.get_rel_fname(abs_fname)
                if (
                    abs_fname in self.original_read_only_fnames
                    or rel_fname in self.original_read_only_fnames
                ):
                    to_keep.add(abs_fname)
            self.coder.abs_read_only_fnames = to_keep
        else:
            self.coder.abs_read_only_fnames = set()

    def _clear_chat_history(self):
        self.coder.done_messages = []
        self.coder.cur_messages = []

    def cmd_reset(self, args):
        "Drop all files and clear the chat history"
        self._drop_all_files()
        self._clear_chat_history()
        self.io.tool_output("All files dropped and chat history cleared.")

    def cmd_tokens(self, args):
        "Report on the number of tokens used by the current chat context"

        res = []

        self.coder.choose_fence()

        # system messages
        main_sys = self.coder.fmt_system_prompt(self.coder.gpt_prompts.main_system)
        main_sys += "\n" + self.coder.fmt_system_prompt(self.coder.gpt_prompts.system_reminder)
        msgs = [
            dict(role="system", content=main_sys),
            dict(
                role="system",
                content=self.coder.fmt_system_prompt(self.coder.gpt_prompts.system_reminder),
            ),
        ]

        tokens = self.coder.main_model.token_count(msgs)
        res.append((tokens, "system messages", ""))

        # chat history
        msgs = self.coder.done_messages + self.coder.cur_messages
        if msgs:
            tokens = self.coder.main_model.token_count(msgs)
            res.append((tokens, "chat history", "use /clear to clear"))

        # repo map
        other_files = set(self.coder.get_all_abs_files()) - set(self.coder.abs_fnames)
        if self.coder.repo_map:
            repo_content = self.coder.repo_map.get_repo_map(self.coder.abs_fnames, other_files)
            if repo_content:
                tokens = self.coder.main_model.token_count(repo_content)
                res.append((tokens, "repository map", "use --map-tokens to resize"))

        fence = "`" * 3

        file_res = []
        # files
        for fname in self.coder.abs_fnames:
            relative_fname = self.coder.get_rel_fname(fname)
            content = self.io.read_text(fname)
            if is_image_file(relative_fname):
                tokens = self.coder.main_model.token_count_for_image(fname)
            else:
                # approximate
                content = f"{relative_fname}\n{fence}\n" + content + "{fence}\n"
                tokens = self.coder.main_model.token_count(content)
            file_res.append((tokens, f"{relative_fname}", "/drop to remove"))

        # read-only files
        for fname in self.coder.abs_read_only_fnames:
            relative_fname = self.coder.get_rel_fname(fname)
            content = self.io.read_text(fname)
            if content is not None and not is_image_file(relative_fname):
                # approximate
                content = f"{relative_fname}\n{fence}\n" + content + "{fence}\n"
                tokens = self.coder.main_model.token_count(content)
                file_res.append((tokens, f"{relative_fname} (read-only)", "/drop to remove"))

        file_res.sort()
        res.extend(file_res)

        self.io.tool_output(
            f"Approximate context window usage for {self.coder.main_model.name}, in tokens:"
        )
        self.io.tool_output()

        width = 8
        cost_width = 9

        def fmt(v):
            return format(int(v), ",").rjust(width)

        col_width = max(len(row[1]) for row in res)

        cost_pad = " " * cost_width
        total = 0
        total_cost = 0.0
        for tk, msg, tip in res:
            total += tk
            cost = tk * (self.coder.main_model.info.get("input_cost_per_token") or 0)
            total_cost += cost
            msg = msg.ljust(col_width)
            self.io.tool_output(f"${cost:7.4f} {fmt(tk)} {msg} {tip}")  # noqa: E231

        self.io.tool_output("=" * (width + cost_width + 1))
        self.io.tool_output(f"${total_cost:7.4f} {fmt(total)} tokens total")  # noqa: E231

        limit = self.coder.main_model.info.get("max_input_tokens") or 0
        if not limit:
            return

        remaining = limit - total
        if remaining > 1024:
            self.io.tool_output(f"{cost_pad}{fmt(remaining)} tokens remaining in context window")
        elif remaining > 0:
            self.io.tool_error(
                f"{cost_pad}{fmt(remaining)} tokens remaining in context window (use /drop or"
                " /clear to make space)"
            )
        else:
            self.io.tool_error(
                f"{cost_pad}{fmt(remaining)} tokens remaining, window exhausted (use /drop or"
                " /clear to make space)"
            )
        self.io.tool_output(f"{cost_pad}{fmt(limit)} tokens max context window size")

    def cmd_undo(self, args):
        "Undo the last git commit if it was done by flacoai"
        try:
            self.raw_cmd_undo(args)
        except ANY_GIT_ERROR as err:
            self.io.tool_error(f"Unable to complete undo: {err}")

    def raw_cmd_undo(self, args):
        if not self.coder.repo:
            self.io.tool_error("No git repository found.")
            return

        last_commit = self.coder.repo.get_head_commit()
        if not last_commit or not last_commit.parents:
            self.io.tool_error("This is the first commit in the repository. Cannot undo.")
            return

        last_commit_hash = self.coder.repo.get_head_commit_sha(short=True)
        last_commit_message = self.coder.repo.get_head_commit_message("(unknown)").strip()
        last_commit_message = (last_commit_message.splitlines() or [""])[0]
        if last_commit_hash not in self.coder.flacoai_commit_hashes:
            self.io.tool_error("The last commit was not made by flacoai in this chat session.")
            self.io.tool_output(
                "You could try `/git reset --hard HEAD^` but be aware that this is a destructive"
                " command!"
            )
            return

        if len(last_commit.parents) > 1:
            self.io.tool_error(
                f"The last commit {last_commit.hexsha} has more than 1 parent, can't undo."
            )
            return

        prev_commit = last_commit.parents[0]
        changed_files_last_commit = [item.a_path for item in last_commit.diff(prev_commit)]

        for fname in changed_files_last_commit:
            if self.coder.repo.repo.is_dirty(path=fname):
                self.io.tool_error(
                    f"The file {fname} has uncommitted changes. Please stash them before undoing."
                )
                return

            # Check if the file was in the repo in the previous commit
            try:
                prev_commit.tree[fname]
            except KeyError:
                self.io.tool_error(
                    f"The file {fname} was not in the repository in the previous commit. Cannot"
                    " undo safely."
                )
                return

        local_head = self.coder.repo.repo.git.rev_parse("HEAD")
        current_branch = self.coder.repo.repo.active_branch.name
        try:
            remote_head = self.coder.repo.repo.git.rev_parse(f"origin/{current_branch}")
            has_origin = True
        except ANY_GIT_ERROR:
            has_origin = False

        if has_origin:
            if local_head == remote_head:
                self.io.tool_error(
                    "The last commit has already been pushed to the origin. Undoing is not"
                    " possible."
                )
                return

        # Reset only the files which are part of `last_commit`
        restored = set()
        unrestored = set()
        for file_path in changed_files_last_commit:
            try:
                self.coder.repo.repo.git.checkout("HEAD~1", file_path)
                restored.add(file_path)
            except ANY_GIT_ERROR:
                unrestored.add(file_path)

        if unrestored:
            self.io.tool_error(f"Error restoring {file_path}, aborting undo.")
            self.io.tool_output("Restored files:")
            for file in restored:
                self.io.tool_output(f"  {file}")
            self.io.tool_output("Unable to restore files:")
            for file in unrestored:
                self.io.tool_output(f"  {file}")
            return

        # Move the HEAD back before the latest commit
        self.coder.repo.repo.git.reset("--soft", "HEAD~1")

        self.io.tool_output(f"Removed: {last_commit_hash} {last_commit_message}")

        # Get the current HEAD after undo
        current_head_hash = self.coder.repo.get_head_commit_sha(short=True)
        current_head_message = self.coder.repo.get_head_commit_message("(unknown)").strip()
        current_head_message = (current_head_message.splitlines() or [""])[0]
        self.io.tool_output(f"Now at:  {current_head_hash} {current_head_message}")

        if self.coder.main_model.send_undo_reply:
            return prompts.undo_command_reply

    def cmd_diff(self, args=""):
        "Display the diff of changes since the last message"
        try:
            self.raw_cmd_diff(args)
        except ANY_GIT_ERROR as err:
            self.io.tool_error(f"Unable to complete diff: {err}")

    def raw_cmd_diff(self, args=""):
        if not self.coder.repo:
            self.io.tool_error("No git repository found.")
            return

        current_head = self.coder.repo.get_head_commit_sha()
        if current_head is None:
            self.io.tool_error("Unable to get current commit. The repository might be empty.")
            return

        if len(self.coder.commit_before_message) < 2:
            commit_before_message = current_head + "^"
        else:
            commit_before_message = self.coder.commit_before_message[-2]

        if not commit_before_message or commit_before_message == current_head:
            self.io.tool_warning("No changes to display since the last message.")
            return

        self.io.tool_output(f"Diff since {commit_before_message[:7]}...")

        if self.coder.pretty:
            run_cmd(f"git diff {commit_before_message}")
            return

        diff = self.coder.repo.diff_commits(
            self.coder.pretty,
            commit_before_message,
            "HEAD",
        )

        self.io.print(diff)

    def quote_fname(self, fname):
        if " " in fname and '"' not in fname:
            fname = f'"{fname}"'
        return fname

    def completions_raw_read_only(self, document, complete_event):
        # Get the text before the cursor
        text = document.text_before_cursor

        # Skip the first word and the space after it
        after_command = text.split()[-1]

        # Create a new Document object with the text after the command
        new_document = Document(after_command, cursor_position=len(after_command))

        def get_paths():
            return [self.coder.root] if self.coder.root else None

        path_completer = PathCompleter(
            get_paths=get_paths,
            only_directories=False,
            expanduser=True,
        )

        # Adjust the start_position to replace all of 'after_command'
        adjusted_start_position = -len(after_command)

        # Collect all completions
        all_completions = []

        # Iterate over the completions and modify them
        for completion in path_completer.get_completions(new_document, complete_event):
            quoted_text = self.quote_fname(after_command + completion.text)
            all_completions.append(
                Completion(
                    text=quoted_text,
                    start_position=adjusted_start_position,
                    display=completion.display,
                    style=completion.style,
                    selected_style=completion.selected_style,
                )
            )

        # Add completions from the 'add' command
        add_completions = self.completions_add()
        for completion in add_completions:
            if after_command in completion:
                all_completions.append(
                    Completion(
                        text=completion,
                        start_position=adjusted_start_position,
                        display=completion,
                    )
                )

        # Sort all completions based on their text
        sorted_completions = sorted(all_completions, key=lambda c: c.text)

        # Yield the sorted completions
        for completion in sorted_completions:
            yield completion

    def completions_add(self):
        files = set(self.coder.get_all_relative_files())
        files = files - set(self.coder.get_inchat_relative_files())
        files = [self.quote_fname(fn) for fn in files]
        return files

    def glob_filtered_to_repo(self, pattern):
        if not pattern.strip():
            return []
        try:
            if os.path.isabs(pattern):
                # Handle absolute paths
                raw_matched_files = [Path(pattern)]
            else:
                try:
                    raw_matched_files = list(Path(self.coder.root).glob(pattern))
                except (IndexError, AttributeError):
                    raw_matched_files = []
        except ValueError as err:
            self.io.tool_error(f"Error matching {pattern}: {err}")
            raw_matched_files = []

        matched_files = []
        for fn in raw_matched_files:
            matched_files += expand_subdir(fn)

        matched_files = [
            fn.relative_to(self.coder.root)
            for fn in matched_files
            if fn.is_relative_to(self.coder.root)
        ]

        # if repo, filter against it
        if self.coder.repo:
            git_files = self.coder.repo.get_tracked_files()
            matched_files = [fn for fn in matched_files if str(fn) in git_files]

        res = list(map(str, matched_files))
        return res

    def cmd_add(self, args):
        "Add files to the chat so flacoai can edit them or review them in detail"

        all_matched_files = set()

        filenames = parse_quoted_filenames(args)
        for word in filenames:
            if Path(word).is_absolute():
                fname = Path(word)
            else:
                fname = Path(self.coder.root) / word

            if self.coder.repo and self.coder.repo.ignored_file(fname):
                self.io.tool_warning(f"Skipping {fname} due to flacoaiignore or --subtree-only.")
                continue

            if fname.exists():
                if fname.is_file():
                    all_matched_files.add(str(fname))
                    continue
                # an existing dir, escape any special chars so they won't be globs
                word = re.sub(r"([\*\?\[\]])", r"[\1]", word)

            matched_files = self.glob_filtered_to_repo(word)
            if matched_files:
                all_matched_files.update(matched_files)
                continue

            if "*" in str(fname) or "?" in str(fname):
                self.io.tool_error(
                    f"No match, and cannot create file with wildcard characters: {fname}"
                )
                continue

            if fname.exists() and fname.is_dir() and self.coder.repo:
                self.io.tool_error(f"Directory {fname} is not in git.")
                self.io.tool_output(f"You can add to git with: /git add {fname}")
                continue

            if self.io.confirm_ask(f"No files matched '{word}'. Do you want to create {fname}?"):
                try:
                    fname.parent.mkdir(parents=True, exist_ok=True)
                    fname.touch()
                    all_matched_files.add(str(fname))
                except OSError as e:
                    self.io.tool_error(f"Error creating file {fname}: {e}")

        for matched_file in sorted(all_matched_files):
            abs_file_path = self.coder.abs_root_path(matched_file)

            if not abs_file_path.startswith(self.coder.root) and not is_image_file(matched_file):
                self.io.tool_error(
                    f"Can not add {abs_file_path}, which is not within {self.coder.root}"
                )
                continue

            if (
                self.coder.repo
                and self.coder.repo.git_ignored_file(matched_file)
                and not self.coder.add_gitignore_files
            ):
                self.io.tool_error(f"Can't add {matched_file} which is in gitignore")
                continue

            if abs_file_path in self.coder.abs_fnames:
                self.io.tool_error(f"{matched_file} is already in the chat as an editable file")
                continue
            elif abs_file_path in self.coder.abs_read_only_fnames:
                if self.coder.repo and self.coder.repo.path_in_repo(matched_file):
                    self.coder.abs_read_only_fnames.remove(abs_file_path)
                    self.coder.abs_fnames.add(abs_file_path)
                    self.io.tool_output(
                        f"Moved {matched_file} from read-only to editable files in the chat"
                    )
                else:
                    self.io.tool_error(
                        f"Cannot add {matched_file} as it's not part of the repository"
                    )
            else:
                if is_image_file(matched_file) and not self.coder.main_model.info.get(
                    "supports_vision"
                ):
                    self.io.tool_error(
                        f"Cannot add image file {matched_file} as the"
                        f" {self.coder.main_model.name} does not support images."
                    )
                    continue
                content = self.io.read_text(abs_file_path)
                if content is None:
                    self.io.tool_error(f"Unable to read {matched_file}")
                else:
                    self.coder.abs_fnames.add(abs_file_path)
                    fname = self.coder.get_rel_fname(abs_file_path)
                    self.io.tool_output(f"Added {fname} to the chat")
                    self.coder.check_added_files()

    def completions_drop(self):
        files = self.coder.get_inchat_relative_files()
        read_only_files = [self.coder.get_rel_fname(fn) for fn in self.coder.abs_read_only_fnames]
        all_files = files + read_only_files
        all_files = [self.quote_fname(fn) for fn in all_files]
        return all_files

    def cmd_drop(self, args=""):
        "Remove files from the chat session to free up context space"

        if not args.strip():
            if self.original_read_only_fnames:
                self.io.tool_output(
                    "Dropping all files from the chat session except originally read-only files."
                )
            else:
                self.io.tool_output("Dropping all files from the chat session.")
            self._drop_all_files()
            return

        filenames = parse_quoted_filenames(args)
        for word in filenames:
            # Expand tilde in the path
            expanded_word = os.path.expanduser(word)

            # Handle read-only files with substring matching and samefile check
            read_only_matched = []
            for f in self.coder.abs_read_only_fnames:
                if expanded_word in f:
                    read_only_matched.append(f)
                    continue

                # Try samefile comparison for relative paths
                try:
                    abs_word = os.path.abspath(expanded_word)
                    if os.path.samefile(abs_word, f):
                        read_only_matched.append(f)
                except (FileNotFoundError, OSError):
                    continue

            for matched_file in read_only_matched:
                self.coder.abs_read_only_fnames.remove(matched_file)
                self.io.tool_output(f"Removed read-only file {matched_file} from the chat")

            # For editable files, use glob if word contains glob chars, otherwise use substring
            if any(c in expanded_word for c in "*?[]"):
                matched_files = self.glob_filtered_to_repo(expanded_word)
            else:
                # Use substring matching like we do for read-only files
                matched_files = [
                    self.coder.get_rel_fname(f) for f in self.coder.abs_fnames if expanded_word in f
                ]

            if not matched_files:
                matched_files.append(expanded_word)

            for matched_file in matched_files:
                abs_fname = self.coder.abs_root_path(matched_file)
                if abs_fname in self.coder.abs_fnames:
                    self.coder.abs_fnames.remove(abs_fname)
                    self.io.tool_output(f"Removed {matched_file} from the chat")

    def cmd_git(self, args):
        "Run a git command (output excluded from chat)"
        combined_output = None
        try:
            args = "git " + args
            env = dict(subprocess.os.environ)
            env["GIT_EDITOR"] = "true"
            result = subprocess.run(
                args,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                env=env,
                shell=True,
                encoding=self.io.encoding,
                errors="replace",
            )
            combined_output = result.stdout
        except Exception as e:
            self.io.tool_error(f"Error running /git command: {e}")

        if combined_output is None:
            return

        self.io.tool_output(combined_output)

    def cmd_test(self, args):
        "Run a shell command and add the output to the chat on non-zero exit code"
        if not args and self.coder.test_cmd:
            args = self.coder.test_cmd

        if not args:
            return

        if not callable(args):
            if type(args) is not str:
                raise ValueError(repr(args))
            return self.cmd_run(args, True)

        errors = args()
        if not errors:
            return

        self.io.tool_output(errors)
        return errors

    def cmd_run(self, args, add_on_nonzero_exit=False):
        "Run a shell command and optionally add the output to the chat (alias: !)"
        exit_status, combined_output = run_cmd(
            args, verbose=self.verbose, error_print=self.io.tool_error, cwd=self.coder.root
        )

        if combined_output is None:
            return

        # Calculate token count of output
        token_count = self.coder.main_model.token_count(combined_output)
        k_tokens = token_count / 1000

        if add_on_nonzero_exit:
            add = exit_status != 0
        else:
            add = self.io.confirm_ask(f"Add {k_tokens:.1f}k tokens of command output to the chat?")

        if add:
            num_lines = len(combined_output.strip().splitlines())
            line_plural = "line" if num_lines == 1 else "lines"
            self.io.tool_output(f"Added {num_lines} {line_plural} of output to the chat.")

            msg = prompts.run_output.format(
                command=args,
                output=combined_output,
            )

            self.coder.cur_messages += [
                dict(role="user", content=msg),
                dict(role="assistant", content="Ok."),
            ]

            if add_on_nonzero_exit and exit_status != 0:
                # Return the formatted output message for test failures
                return msg
            elif add and exit_status != 0:
                self.io.placeholder = "What's wrong? Fix"

        # Return None if output wasn't added or command succeeded
        return None

    def cmd_exit(self, args):
        "Exit the application"
        self.coder.event("exit", reason="/exit")
        sys.exit()

    def cmd_quit(self, args):
        "Exit the application"
        self.cmd_exit(args)

    def cmd_ls(self, args):
        "List all known files and indicate which are included in the chat session"

        files = self.coder.get_all_relative_files()

        other_files = []
        chat_files = []
        read_only_files = []
        for file in files:
            abs_file_path = self.coder.abs_root_path(file)
            if abs_file_path in self.coder.abs_fnames:
                chat_files.append(file)
            else:
                other_files.append(file)

        # Add read-only files
        for abs_file_path in self.coder.abs_read_only_fnames:
            rel_file_path = self.coder.get_rel_fname(abs_file_path)
            read_only_files.append(rel_file_path)

        if not chat_files and not other_files and not read_only_files:
            self.io.tool_output("\nNo files in chat, git repo, or read-only list.")
            return

        if other_files:
            self.io.tool_output("Repo files not in the chat:\n")
        for file in other_files:
            self.io.tool_output(f"  {file}")

        if read_only_files:
            self.io.tool_output("\nRead-only files:\n")
        for file in read_only_files:
            self.io.tool_output(f"  {file}")

        if chat_files:
            self.io.tool_output("\nFiles in chat:\n")
        for file in chat_files:
            self.io.tool_output(f"  {file}")

    def basic_help(self):
        commands = sorted(self.get_commands())
        pad = max(len(cmd) for cmd in commands)
        pad = "{cmd:" + str(pad) + "}"
        for cmd in commands:
            cmd_method_name = f"cmd_{cmd[1:]}".replace("-", "_")
            cmd_method = getattr(self, cmd_method_name, None)
            cmd = pad.format(cmd=cmd)
            if cmd_method:
                description = cmd_method.__doc__
                self.io.tool_output(f"{cmd} {description}")
            else:
                self.io.tool_output(f"{cmd} No description available.")
        self.io.tool_output()
        self.io.tool_output("Use `/help <question>` to ask questions about how to use flacoai.")

    def cmd_help(self, args):
        "Ask questions about flacoai"

        if not args.strip():
            self.basic_help()
            return

        self.coder.event("interactive help")
        from flacoai.coders.base_coder import Coder

        if not self.help:
            res = install_help_extra(self.io)
            if not res:
                self.io.tool_error("Unable to initialize interactive help.")
                return

            self.help = Help()

        coder = Coder.create(
            io=self.io,
            from_coder=self.coder,
            edit_format="help",
            summarize_from_coder=False,
            map_tokens=512,
            map_mul_no_files=1,
        )
        user_msg = self.help.ask(args)
        user_msg += """
# Announcement lines from when this session of flacoai was launched:

"""
        user_msg += "\n".join(self.coder.get_announcements()) + "\n"

        coder.run(user_msg, preproc=False)

        if self.coder.repo_map:
            map_tokens = self.coder.repo_map.max_map_tokens
            map_mul_no_files = self.coder.repo_map.map_mul_no_files
        else:
            map_tokens = 0
            map_mul_no_files = 1

        raise SwitchCoder(
            edit_format=self.coder.edit_format,
            summarize_from_coder=False,
            from_coder=coder,
            map_tokens=map_tokens,
            map_mul_no_files=map_mul_no_files,
            show_announcements=False,
        )

    def completions_ask(self):
        raise CommandCompletionException()

    def completions_code(self):
        raise CommandCompletionException()

    def completions_architect(self):
        raise CommandCompletionException()

    def completions_context(self):
        raise CommandCompletionException()

    def cmd_ask(self, args):
        """Ask questions about the code base without editing any files. If no prompt provided, switches to ask mode."""  # noqa
        return self._generic_chat_command(args, "ask")

    def cmd_code(self, args):
        """Ask for changes to your code. If no prompt provided, switches to code mode."""  # noqa
        return self._generic_chat_command(args, self.coder.main_model.edit_format)

    def cmd_architect(self, args):
        """Enter architect/editor mode using 2 different models. If no prompt provided, switches to architect/editor mode."""  # noqa
        return self._generic_chat_command(args, "architect")

    def cmd_context(self, args):
        """Enter context mode to see surrounding code context. If no prompt provided, switches to context mode."""  # noqa
        return self._generic_chat_command(args, "context", placeholder=args.strip() or None)

    def _generic_chat_command(self, args, edit_format, placeholder=None):
        if not args.strip():
            # Switch to the corresponding chat mode if no args provided
            return self.cmd_chat_mode(edit_format)

        from flacoai.coders.base_coder import Coder

        coder = Coder.create(
            io=self.io,
            from_coder=self.coder,
            edit_format=edit_format,
            summarize_from_coder=False,
        )

        user_msg = args
        coder.run(user_msg)

        # Use the provided placeholder if any
        raise SwitchCoder(
            edit_format=self.coder.edit_format,
            summarize_from_coder=False,
            from_coder=coder,
            show_announcements=False,
            placeholder=placeholder,
        )

    def get_help_md(self):
        "Show help about all commands in markdown"

        res = """
|Command|Description|
|:------|:----------|
"""
        commands = sorted(self.get_commands())
        for cmd in commands:
            cmd_method_name = f"cmd_{cmd[1:]}".replace("-", "_")
            cmd_method = getattr(self, cmd_method_name, None)
            if cmd_method:
                description = cmd_method.__doc__
                res += f"| **{cmd}** | {description} |\n"
            else:
                res += f"| **{cmd}** | |\n"

        res += "\n"
        return res

    def cmd_voice(self, args):
        "Record and transcribe voice input"

        if not self.voice:
            if "OPENAI_API_KEY" not in os.environ:
                self.io.tool_error("To use /voice you must provide an OpenAI API key.")
                return
            try:
                self.voice = voice.Voice(
                    audio_format=self.voice_format or "wav", device_name=self.voice_input_device
                )
            except voice.SoundDeviceError:
                self.io.tool_error(
                    "Unable to import `sounddevice` and/or `soundfile`, is portaudio installed?"
                )
                return

        try:
            text = self.voice.record_and_transcribe(None, language=self.voice_language)
        except litellm.OpenAIError as err:
            self.io.tool_error(f"Unable to use OpenAI whisper model: {err}")
            return

        if text:
            self.io.placeholder = text

    def cmd_paste(self, args):
        """Paste image/text from the clipboard into the chat.\
        Optionally provide a name for the image."""
        try:
            # Check for image first
            image = ImageGrab.grabclipboard()
            if isinstance(image, Image.Image):
                if args.strip():
                    filename = args.strip()
                    ext = os.path.splitext(filename)[1].lower()
                    if ext in (".jpg", ".jpeg", ".png"):
                        basename = filename
                    else:
                        basename = f"{filename}.png"
                else:
                    basename = "clipboard_image.png"

                temp_dir = tempfile.mkdtemp()
                temp_file_path = os.path.join(temp_dir, basename)
                image_format = "PNG" if basename.lower().endswith(".png") else "JPEG"
                image.save(temp_file_path, image_format)

                abs_file_path = Path(temp_file_path).resolve()

                # Check if a file with the same name already exists in the chat
                existing_file = next(
                    (f for f in self.coder.abs_fnames if Path(f).name == abs_file_path.name), None
                )
                if existing_file:
                    self.coder.abs_fnames.remove(existing_file)
                    self.io.tool_output(f"Replaced existing image in the chat: {existing_file}")

                self.coder.abs_fnames.add(str(abs_file_path))
                self.io.tool_output(f"Added clipboard image to the chat: {abs_file_path}")
                self.coder.check_added_files()

                return

            # If not an image, try to get text
            text = pyperclip.paste()
            if text:
                self.io.tool_output(text)
                return text

            self.io.tool_error("No image or text content found in clipboard.")
            return

        except Exception as e:
            self.io.tool_error(f"Error processing clipboard content: {e}")

    def cmd_read_only(self, args):
        "Add files to the chat that are for reference only, or turn added files to read-only"
        if not args.strip():
            # Convert all files in chat to read-only
            for fname in list(self.coder.abs_fnames):
                self.coder.abs_fnames.remove(fname)
                self.coder.abs_read_only_fnames.add(fname)
                rel_fname = self.coder.get_rel_fname(fname)
                self.io.tool_output(f"Converted {rel_fname} to read-only")
            return

        filenames = parse_quoted_filenames(args)
        all_paths = []

        # First collect all expanded paths
        for pattern in filenames:
            expanded_pattern = expanduser(pattern)
            path_obj = Path(expanded_pattern)
            is_abs = path_obj.is_absolute()
            if not is_abs:
                path_obj = Path(self.coder.root) / path_obj

            matches = []
            # Check for literal path existence first
            if path_obj.exists():
                matches = [path_obj]
            else:
                # If literal path doesn't exist, try globbing
                if is_abs:
                    # For absolute paths, glob it
                    matches = [Path(p) for p in glob.glob(expanded_pattern)]
                else:
                    # For relative paths and globs, use glob from the root directory
                    matches = list(Path(self.coder.root).glob(expanded_pattern))

            if not matches:
                self.io.tool_error(f"No matches found for: {pattern}")
            else:
                all_paths.extend(matches)

        # Then process them in sorted order
        for path in sorted(all_paths):
            abs_path = self.coder.abs_root_path(path)
            if os.path.isfile(abs_path):
                self._add_read_only_file(abs_path, path)
            elif os.path.isdir(abs_path):
                self._add_read_only_directory(abs_path, path)
            else:
                self.io.tool_error(f"Not a file or directory: {abs_path}")

    def _add_read_only_file(self, abs_path, original_name):
        if is_image_file(original_name) and not self.coder.main_model.info.get("supports_vision"):
            self.io.tool_error(
                f"Cannot add image file {original_name} as the"
                f" {self.coder.main_model.name} does not support images."
            )
            return

        if abs_path in self.coder.abs_read_only_fnames:
            self.io.tool_error(f"{original_name} is already in the chat as a read-only file")
            return
        elif abs_path in self.coder.abs_fnames:
            self.coder.abs_fnames.remove(abs_path)
            self.coder.abs_read_only_fnames.add(abs_path)
            self.io.tool_output(
                f"Moved {original_name} from editable to read-only files in the chat"
            )
        else:
            self.coder.abs_read_only_fnames.add(abs_path)
            self.io.tool_output(f"Added {original_name} to read-only files.")

    def _add_read_only_directory(self, abs_path, original_name):
        added_files = 0
        for root, _, files in os.walk(abs_path):
            for file in files:
                file_path = os.path.join(root, file)
                if (
                    file_path not in self.coder.abs_fnames
                    and file_path not in self.coder.abs_read_only_fnames
                ):
                    self.coder.abs_read_only_fnames.add(file_path)
                    added_files += 1

        if added_files > 0:
            self.io.tool_output(
                f"Added {added_files} files from directory {original_name} to read-only files."
            )
        else:
            self.io.tool_output(f"No new files added from directory {original_name}.")

    def cmd_map(self, args):
        "Print out the current repository map"
        repo_map = self.coder.get_repo_map()
        if repo_map:
            self.io.tool_output(repo_map)
        else:
            self.io.tool_output("No repository map available.")

    def cmd_map_refresh(self, args):
        "Force a refresh of the repository map"
        repo_map = self.coder.get_repo_map(force_refresh=True)
        if repo_map:
            self.io.tool_output("The repo map has been refreshed, use /map to view it.")

    def cmd_generate(self, args):
        """Generate SwiftUI code from templates

        /generate                      - Show available templates
        /generate login <prompt>       - Generate login view
        /generate settings <prompt>    - Generate settings view
        /generate list <prompt>        - Generate list view
        /generate detail <prompt>      - Generate detail view
        /generate tabview <prompt>     - Generate tab view
        /generate <template> --save <file>  - Save generated code to file

        Examples:
          /generate login for MyApp
          /generate list of tasks
          /generate settings
          /generate tabview with home search favorites profile
        """
        self._track_command("generate")

        from flacoai.template_engine import TemplateEngine

        engine = TemplateEngine()

        # Parse arguments
        args_parts = args.strip().split() if args.strip() else []

        # Extract --save flag
        save_file = None
        if "--save" in args_parts:
            save_idx = args_parts.index("--save")
            if save_idx + 1 < len(args_parts):
                save_file = args_parts[save_idx + 1]
                args_parts = [a for i, a in enumerate(args_parts) if i not in [save_idx, save_idx + 1]]

        # If no args, show available templates
        if not args_parts:
            self.io.tool_output("📝 Available SwiftUI templates:\n")
            for template in engine.list_templates():
                self.io.tool_output(f"  • {template['name']:12} - {template['description']}")
            self.io.tool_output("\nUsage: /generate <template> <prompt>")
            self.io.tool_output("Example: /generate login for MyWeatherApp")
            return

        # Extract template name
        template_name = args_parts[0].lower()

        # Validate template
        if template_name not in engine.templates:
            self.io.tool_error(f"Unknown template: {template_name}")
            self.io.tool_output("\nAvailable templates:")
            for template in engine.list_templates():
                self.io.tool_output(f"  • {template['name']}")
            return

        # Extract prompt (everything after template name)
        prompt = " ".join(args_parts[1:]) if len(args_parts) > 1 else template_name

        # Show what we're generating
        self.io.tool_output(f"🎨 Generating {template_name} view...")

        # Generate code
        try:
            generated_code = engine.generate(template_name, prompt)

            if generated_code is None:
                self.io.tool_error(f"Failed to generate code from template: {template_name}")
                return

            # Save to file if requested
            if save_file:
                try:
                    # Ensure .swift extension
                    if not save_file.endswith('.swift'):
                        save_file += '.swift'

                    # Write to file
                    with open(save_file, 'w', encoding='utf-8') as f:
                        f.write(generated_code)

                    self.io.tool_output(f"✅ Saved to: {save_file}")
                except Exception as e:
                    self.io.tool_error(f"Failed to save file: {e}")
            else:
                # Output to terminal
                self.io.tool_output("\n" + "=" * 80)
                self.io.tool_output(generated_code)
                self.io.tool_output("=" * 80 + "\n")

                # Show helpful next steps
                self.io.tool_output("💡 Next steps:")
                self.io.tool_output("  1. Copy the code above to your Xcode project")
                self.io.tool_output("  2. Customize the TODO sections for your needs")
                self.io.tool_output("  3. Or use --save <filename> to save directly to a file")

        except Exception as e:
            self.io.tool_error(f"Error generating code: {e}")
            import traceback
            if self.verbose:
                traceback.print_exc()

    def cmd_xcode(self, args):
        """Manage Xcode project files and targets

        /xcode                          - Show project info
        /xcode list-targets             - List all targets
        /xcode list-files [target]      - List files in project or target
        /xcode add-file <path> [target] - Add file to project
        /xcode remove-file <path>       - Remove file from project

        Examples:
          /xcode
          /xcode list-targets
          /xcode list-files MyApp
          /xcode add-file LoginView.swift
          /xcode add-file Sources/NewFile.swift MyApp
          /xcode remove-file OldFile.swift
        """
        self._track_command("xcode")

        from flacoai.xcode import XcodeManager
        from flacoai.xcode.xcode_manager import XcodeManagerException

        # Parse arguments
        args_parts = args.strip().split() if args.strip() else []

        try:
            # Load Xcode project
            manager = XcodeManager(io=self.io)

            # No args - show project info
            if not args_parts:
                info = manager.get_project_info()
                self.io.tool_output(f"\n📱 Xcode Project: {info['name']}")
                self.io.tool_output(f"📍 Path: {info['path']}")
                self.io.tool_output(f"\n🎯 Targets ({info['target_count']}):")
                for target in info['targets']:
                    self.io.tool_output(f"   • {target['name']} ({target['type']})")
                self.io.tool_output(f"\n💡 Use '/xcode list-targets' for more details")
                self.io.tool_output(f"💡 Use '/xcode add-file <path>' to add files")
                return

            # Extract command
            command = args_parts[0].lower()

            # list-targets command
            if command == "list-targets":
                targets = manager.list_targets()
                self.io.tool_output(f"\n🎯 Targets in {manager.project_path.stem}:\n")
                for target in targets:
                    self.io.tool_output(f"  📦 {target['name']}")
                    self.io.tool_output(f"     Type: {target['type']}")
                    self.io.tool_output(f"     Product: {target['product']}")
                    self.io.tool_output("")

            # list-files command
            elif command == "list-files":
                target_name = args_parts[1] if len(args_parts) > 1 else None
                files = manager.list_files(target_name)

                if target_name:
                    self.io.tool_output(f"\n📄 Files in target '{target_name}':\n")
                else:
                    self.io.tool_output(f"\n📄 All files in project:\n")

                for file_path in sorted(files):
                    self.io.tool_output(f"   {file_path}")

                self.io.tool_output(f"\nTotal: {len(files)} files")

            # add-file command
            elif command == "add-file":
                if len(args_parts) < 2:
                    self.io.tool_error("Usage: /xcode add-file <file_path> [target_name]")
                    return

                file_path = args_parts[1]
                target_name = args_parts[2] if len(args_parts) > 2 else None

                # Check if file exists
                if not os.path.exists(file_path):
                    self.io.tool_error(f"File not found: {file_path}")
                    return

                # Add file
                success = manager.add_file(file_path, target_name=target_name)

                if success:
                    # Save project
                    manager.save()
                    self.io.tool_output(f"\n✅ Successfully added {file_path} to Xcode project")
                    self.io.tool_output(f"💡 You can now open the project in Xcode")

            # remove-file command
            elif command == "remove-file":
                if len(args_parts) < 2:
                    self.io.tool_error("Usage: /xcode remove-file <file_path>")
                    return

                file_path = args_parts[1]

                # Remove file
                success = manager.remove_file(file_path)

                if success:
                    # Save project
                    manager.save()
                    self.io.tool_output(f"\n✅ Successfully removed {file_path} from Xcode project")
                else:
                    self.io.tool_error(f"Failed to remove file: {file_path}")

            else:
                self.io.tool_error(f"Unknown command: {command}")
                self.io.tool_output("\nAvailable commands:")
                self.io.tool_output("  list-targets")
                self.io.tool_output("  list-files [target]")
                self.io.tool_output("  add-file <path> [target]")
                self.io.tool_output("  remove-file <path>")

        except XcodeManagerException as e:
            self.io.tool_error(f"Xcode error: {e}")
            if not XcodeManager or not hasattr(XcodeManager, '__init__'):
                self.io.tool_output("\n💡 Install mod-pbxproj: pip install mod-pbxproj")
        except Exception as e:
            self.io.tool_error(f"Error: {e}")
            import traceback
            if self.verbose:
                traceback.print_exc()

    def cmd_screenshot(self, args):
        """Convert UI screenshot to SwiftUI code

        /screenshot <image_path>              - Convert screenshot to SwiftUI
        /screenshot <image_path> --save <file> - Save generated code to file
        /screenshot <image_path> --preview     - Show analysis without generating code

        Examples:
          /screenshot mockup.png
          /screenshot design.jpg --save LoginView.swift
          /screenshot ui_design.png --preview

        Supported formats: PNG, JPG, JPEG, PDF
        """
        self._track_command("screenshot")

        import base64
        from pathlib import Path

        # Parse arguments
        args_parts = args.strip().split() if args.strip() else []

        if not args_parts:
            self.io.tool_error("Usage: /screenshot <image_path> [--save <file>] [--preview]")
            self.io.tool_output("\nExamples:")
            self.io.tool_output("  /screenshot mockup.png")
            self.io.tool_output("  /screenshot design.jpg --save LoginView.swift")
            return

        # Extract image path
        image_path = args_parts[0]

        # Extract flags
        save_file = None
        preview_mode = "--preview" in args_parts

        if "--save" in args_parts:
            save_idx = args_parts.index("--save")
            if save_idx + 1 < len(args_parts):
                save_file = args_parts[save_idx + 1]

        # Validate image file exists
        image_path = Path(image_path)
        if not image_path.exists():
            self.io.tool_error(f"Image file not found: {image_path}")
            return

        # Validate file format
        supported_formats = ['.png', '.jpg', '.jpeg', '.pdf']
        if image_path.suffix.lower() not in supported_formats:
            self.io.tool_error(f"Unsupported format: {image_path.suffix}")
            self.io.tool_output(f"Supported formats: {', '.join(supported_formats)}")
            return

        # Check if current model supports vision
        from flacoai.coders.screenshot_coder import ScreenshotCoder
        from flacoai.coders.base_coder import Coder

        # Create screenshot coder
        try:
            coder = Coder.create(
                io=self.io,
                from_coder=self.coder,
                edit_format="ask",
                summarize_from_coder=False,
            )

            # Check vision support
            screenshot_coder = ScreenshotCoder(
                main_model=coder.main_model,
                io=self.io,
            )

            if not screenshot_coder.supports_vision():
                self.io.tool_error(
                    f"Current model ({coder.main_model.name}) does not support vision/images"
                )
                self.io.tool_output("\nVision-capable models:")
                self.io.tool_output("  • gpt-4-vision-preview")
                self.io.tool_output("  • gpt-4-turbo (gpt-4-turbo-2024-04-09)")
                self.io.tool_output("  • gpt-4o")
                self.io.tool_output("  • claude-3-opus")
                self.io.tool_output("  • claude-3-sonnet")
                self.io.tool_output("\nSwitch model with: /model gpt-4o")
                return

            # Read and encode image
            self.io.tool_output(f"📸 Analyzing screenshot: {image_path.name}")

            # Create message with image
            if preview_mode:
                prompt = f"""Analyze this UI screenshot and describe:
1. Overall layout and structure
2. All UI elements (buttons, text fields, labels, etc.)
3. Colors and styling
4. Spacing and alignment
5. Any recognizable iOS patterns

Provide a detailed analysis but do NOT generate SwiftUI code."""
            else:
                prompt = f"""Analyze this UI screenshot and generate SwiftUI code that recreates the design.

Include:
- Accurate layout structure (VStack, HStack, ZStack)
- All UI elements with proper styling
- Colors, fonts, spacing matching the design
- SF Symbols for icons where appropriate
- @State for interactive elements
- #Preview for testing

Make the code production-ready and compilable."""

            # Add image to the message
            # Note: The actual image handling will be done by the model/io layer
            # For now, we'll add the image path as a special marker
            full_prompt = f"[IMAGE: {image_path.absolute()}]\n\n{prompt}"

            # Send to model
            messages = [
                {"role": "user", "content": full_prompt}
            ]

            # Get response
            self.io.tool_output("🤖 Generating SwiftUI code from screenshot...")

            # Use the coder to send the message
            # The model will handle the image if it supports vision
            response_text = coder.send_with_retries(messages=messages)

            # Display response
            if preview_mode:
                self.io.tool_output("\n" + "=" * 80)
                self.io.tool_output("📊 Screenshot Analysis:\n")
                self.io.tool_output(response_text)
                self.io.tool_output("=" * 80 + "\n")
            else:
                # Save to file if requested
                if save_file:
                    # Extract code from response
                    # Look for Swift code blocks
                    import re
                    code_blocks = re.findall(r'```swift\n(.*?)\n```', response_text, re.DOTALL)

                    if code_blocks:
                        swift_code = code_blocks[0]

                        # Ensure .swift extension
                        save_path = Path(save_file)
                        if not save_path.suffix:
                            save_path = save_path.with_suffix('.swift')

                        # Write to file
                        with open(save_path, 'w', encoding='utf-8') as f:
                            f.write(swift_code)

                        self.io.tool_output(f"✅ Saved SwiftUI code to: {save_path}")
                        self.io.tool_output(f"\n💡 Add to Xcode: /xcode add-file {save_path}")
                    else:
                        self.io.tool_error("No Swift code found in response")
                        self.io.tool_output("\nFull response:")
                        self.io.tool_output(response_text)
                else:
                    # Display code
                    self.io.tool_output("\n" + "=" * 80)
                    self.io.tool_output(response_text)
                    self.io.tool_output("=" * 80 + "\n")

                    self.io.tool_output("💡 Next steps:")
                    self.io.tool_output("  1. Review and test the generated code")
                    self.io.tool_output("  2. Adjust colors/spacing to match your design")
                    self.io.tool_output("  3. Use --save <filename> to save to file")

        except Exception as e:
            self.io.tool_error(f"Error processing screenshot: {e}")
            import traceback
            if self.verbose:
                traceback.print_exc()

    def cmd_review(self, args):
        """Perform comprehensive code review

        /review                        - Review entire project automatically
        /review <filename>             - Review specific file (can omit extension)
        /review --security             - Only security analysis
        /review --performance          - Only performance analysis
        /review --quality              - Only quality analysis
        /review --architecture         - Only architecture analysis
        /review --save <file>          - Save report to file
        /review --ci                   - CI/CD mode (JSON output, exit code 1 if HIGH+ issues)
        /review --fix                  - Interactive fix application
        /review --baseline             - Save current state as baseline
        /review --compare              - Compare against saved baseline (show only new issues)
        /review --export-github        - Export HIGH+ issues to GitHub
        /review --json                 - Output results as JSON
        """
        self._track_command("review")

        from flacoai.coders.review_coder import ReviewCoder
        from flacoai.report_generator import ReviewReportGenerator
        import os
        from pathlib import Path

        # Parse arguments
        args_parts = args.strip().split() if args.strip() else []

        # Extract new v2.0.0 flags
        ci_mode = "--ci" in args_parts
        fix_mode = "--fix" in args_parts
        baseline_mode = "--baseline" in args_parts
        compare_mode = "--compare" in args_parts
        export_github = "--export-github" in args_parts
        json_output = "--json" in args_parts or ci_mode  # CI mode implies JSON

        # Extract flags
        enable_security = "--security" in args_parts or not any(
            f in args_parts for f in ["--security", "--performance", "--quality", "--architecture"]
        )
        enable_performance = "--performance" in args_parts or not any(
            f in args_parts for f in ["--security", "--performance", "--quality", "--architecture"]
        )
        enable_quality = "--quality" in args_parts or not any(
            f in args_parts for f in ["--security", "--performance", "--quality", "--architecture"]
        )
        enable_architecture = "--architecture" in args_parts or not any(
            f in args_parts for f in ["--security", "--performance", "--quality", "--architecture"]
        )

        # Extract save file
        save_file = None
        if "--save" in args_parts:
            save_idx = args_parts.index("--save")
            if save_idx + 1 < len(args_parts):
                save_file = args_parts[save_idx + 1]
                args_parts = [a for i, a in enumerate(args_parts) if i not in [save_idx, save_idx + 1]]

        # Remove flags from args to get filename
        filename_args = [a for a in args_parts if not a.startswith("--")]

        # Determine files to review
        files_to_review = set()

        if filename_args:
            # Mode 1: Review specific file(s)
            for file_arg in filename_args:
                # Try to find the file (with or without extension)
                candidates = []

                # If full path exists
                if os.path.exists(file_arg):
                    candidates.append(file_arg)
                else:
                    # Search for file with any extension
                    base_name = os.path.splitext(file_arg)[0]

                    # Search in current directory and subdirectories
                    root_path = self.coder.root if self.coder.root else os.getcwd()
                    for root, dirs, files in os.walk(root_path):
                        # Skip hidden directories and common ignore patterns
                        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__', 'venv', 'env']]

                        for f in files:
                            if f == file_arg or os.path.splitext(f)[0] == base_name:
                                full_path = os.path.join(root, f)
                                candidates.append(full_path)

                if not candidates:
                    self.io.tool_error(f"File not found: {file_arg}")
                    continue

                # Use the first candidate (or prompt if multiple)
                if len(candidates) == 1:
                    files_to_review.add(os.path.abspath(candidates[0]))
                    self.io.tool_output(f"Found: {candidates[0]}")
                else:
                    # Multiple matches - use the shortest path (most likely match)
                    shortest = min(candidates, key=len)
                    files_to_review.add(os.path.abspath(shortest))
                    self.io.tool_output(f"Found: {shortest} (multiple matches, using shortest path)")

        else:
            # Mode 2: Review entire project automatically with smart context loading (v2.0.0)
            self.io.tool_output("🔍 Smart file discovery (skipping generated code, build artifacts)...")

            from flacoai.smart_context import SmartContextLoader

            root_path = self.coder.root if self.coder.root else os.getcwd()
            context_loader = SmartContextLoader(root_path, io=self.io)

            # Use smart context loader
            files_to_review = context_loader.get_relevant_files(
                focus_files=None,
                include_tests=True,
                max_files=100  # Reasonable limit for performance
            )

            self.io.tool_output(f"📁 Found {len(files_to_review)} relevant code files to analyze")

        if not files_to_review:
            self.io.tool_error("No files to review")
            return

        # Create ReviewCoder instance (reuse existing coder's settings)
        review_coder = ReviewCoder(
            main_model=self.coder.main_model,
            io=self.io,
            repo=self.coder.repo,
            fnames=list(files_to_review),
            show_diffs=False,
            auto_commits=False,
            stream=False,
            verbose=self.verbose,
        )

        # Run static analysis
        self.io.tool_output("")
        self.io.tool_output("🔬 Running code analysis...")

        report = review_coder.run_static_analysis(
            files_to_analyze=files_to_review,
            enable_security=enable_security,
            enable_performance=enable_performance,
            enable_quality=enable_quality,
            enable_architecture=enable_architecture,
        )

        # Baseline comparison (v2.0.0 feature)
        baseline_comparison = None
        if compare_mode or baseline_mode:
            from flacoai.baseline_manager import BaselineManager

            project_root = self.coder.root if self.coder.root else os.getcwd()
            baseline_manager = BaselineManager(project_root)

            if compare_mode:
                baseline_comparison = baseline_manager.compare_with_baseline(report)

                if baseline_comparison["baseline_exists"]:
                    comp_stats = baseline_manager.get_stats(baseline_comparison)
                    self.io.tool_output("\n📊 Baseline Comparison")
                    self.io.tool_output(f"   New issues: {len(baseline_comparison['new_issues'])} (Critical: {comp_stats['new_critical']}, High: {comp_stats['new_high']}, Medium: {comp_stats['new_medium']}, Low: {comp_stats['new_low']})")
                    self.io.tool_output(f"   Fixed issues: {len(baseline_comparison['fixed_issues'])} (Critical: {comp_stats['fixed_critical']}, High: {comp_stats['fixed_high']}, Medium: {comp_stats['fixed_medium']}, Low: {comp_stats['fixed_low']})")
                    self.io.tool_output(f"   Unchanged: {len(baseline_comparison['unchanged_issues'])}")

                    # Filter report to show only new issues
                    report.results = baseline_comparison['new_issues']
                else:
                    self.io.tool_output("\n⚠️  No baseline found. Run '/review --baseline' to create one.")

            if baseline_mode:
                baseline_manager.save_baseline(report)
                self.io.tool_output("\n✓ Baseline saved to .flaco/baselines/current.json")

        # JSON output (v2.0.0 feature - for CI/CD)
        if json_output:
            import json
            import sys

            output_data = {
                "files_analyzed": report.files_analyzed,
                "total_issues": len(report.results),
                "stats": report.get_stats(),
                "issues": [
                    {
                        "file": r.file,
                        "line": r.line,
                        "severity": r.severity.value,
                        "category": r.category.value,
                        "title": r.title,
                        "description": r.description,
                        "recommendation": r.recommendation,
                    }
                    for r in report.results
                ],
            }

            if baseline_comparison:
                output_data["baseline_comparison"] = {
                    "new_issues": len(baseline_comparison['new_issues']),
                    "fixed_issues": len(baseline_comparison['fixed_issues']),
                    "unchanged_issues": len(baseline_comparison['unchanged_issues']),
                }

            print(json.dumps(output_data, indent=2))

            # CI mode: exit with code 1 if HIGH+ issues found
            if ci_mode:
                stats = report.get_stats()
                if stats['critical'] > 0 or stats['high'] > 0:
                    sys.exit(1)
                else:
                    sys.exit(0)

            return  # Don't show regular output in JSON mode

        # Generate and display report
        generator = ReviewReportGenerator(io=self.io)

        self.io.tool_output("")
        self.io.tool_output("=" * 80)

        # Display in console
        generator.display_console(report)

        # Save to file if requested
        if save_file:
            generator.save_to_file(report, save_file)

        # GitHub export (v2.0.0 feature)
        if export_github:
            from flacoai.integrations.github_exporter import GitHubExporter

            self.io.tool_output("\n📤 Exporting to GitHub Issues...")
            exporter = GitHubExporter(io=self.io)
            created_issues = exporter.export_findings(report.results, severity_threshold="high")

            if created_issues:
                self.io.tool_output(f"\n✓ Created {len(created_issues)} GitHub issues")
            else:
                self.io.tool_output("\n⚠️  No issues were created (check if gh CLI is installed)")

        # Interactive fix application (v2.0.0 feature)
        if fix_mode:
            from flacoai.fix_applicator import FixApplicator

            self.io.tool_output("\n🔧 Interactive Fix Application")
            self.io.tool_output("=" * 60)

            applicator = FixApplicator(io=self.io)

            # Generate auto-fixes for results
            report.results = applicator.generate_auto_fixes(report.results)

            # Apply fixes interactively
            fix_stats = applicator.apply_fixes(report.results, auto_fix_safe=False)

            self.io.tool_output(f"\n✓ Fixes applied: {fix_stats['applied']}")
            self.io.tool_output(f"  Fixes skipped: {fix_stats['skipped']}")

            if fix_stats['applied'] > 0:
                self.io.tool_output("\n💡 Don't forget to review the changes and test your code!")

        # Summary message
        stats = report.get_stats()
        if stats['total'] == 0:
            self.io.tool_output("\n✅ No issues found! Code looks good.")
        else:
            self.io.tool_output(f"\n📊 Review complete: {stats['total']} issues found")
            self.io.tool_output(f"   Critical: {stats['critical']} | High: {stats['high']} | Medium: {stats['medium']} | Low: {stats['low']}")

            if not save_file and not json_output:
                self.io.tool_output("\n💡 Tips:")
                self.io.tool_output("   • Use '/review --save report.md' to save the full report")
                self.io.tool_output("   • Use '/review --baseline' to track progress over time")
                self.io.tool_output("   • Use '/review --export-github' to create GitHub issues")
                self.io.tool_output("   • Use '/review --fix' to apply fixes interactively")

    def cmd_jira(self, args):
        """Interact with Jira issue tracker

        /jira create <project> <summary>     - Create new issue
        /jira search <JQL>                   - Search issues with JQL
        /jira show <KEY>                     - Display issue details
        /jira comment <KEY> <text>           - Add comment to issue
        /jira status <KEY> <status>          - Update issue status
        /jira assign <KEY> <user>            - Assign issue to user
        /jira link <KEY>                     - Link current changes to issue
        /jira plan <KEY>                     - Break down ticket into implementation steps
        /jira from-review                    - Create issues from last review
        /jira my                             - Show my assigned issues
        """
        self._track_command("jira")

        from flacoai.integrations.jira_client import JiraClient
        from flacoai.integrations.jira_formatter import JiraFormatter

        # Parse subcommand
        args_parts = args.strip().split(maxsplit=1) if args.strip() else []

        if not args_parts:
            self.io.tool_error("Usage: /jira <subcommand> [args...]")
            self.io.tool_error("Type '/help jira' for details")
            return

        subcommand = args_parts[0].lower()
        subargs = args_parts[1] if len(args_parts) > 1 else ""

        # Initialize client
        client = JiraClient.from_config(self.io)
        if not client:
            return

        formatter = JiraFormatter(io=self.io)

        try:
            if subcommand == "create":
                self._jira_create(client, formatter, subargs)

            elif subcommand == "search":
                self._jira_search(client, formatter, subargs)

            elif subcommand == "show":
                self._jira_show(client, formatter, subargs)

            elif subcommand == "comment":
                self._jira_comment(client, formatter, subargs)

            elif subcommand == "status":
                self._jira_status(client, formatter, subargs)

            elif subcommand == "assign":
                self._jira_assign(client, formatter, subargs)

            elif subcommand == "link":
                self._jira_link(client, formatter, subargs)

            elif subcommand == "from-review":
                self._jira_from_review(client, formatter, subargs)

            elif subcommand == "my":
                self._jira_my_issues(client, formatter, subargs)

            elif subcommand == "plan":
                self._jira_plan(client, formatter, subargs)

            else:
                self.io.tool_error(f"Unknown subcommand: {subcommand}")
                self.io.tool_error("Type '/help jira' for available commands")

        except Exception as e:
            self.io.tool_error(f"Jira error: {e}")

    def _jira_create(self, client, formatter, args):
        """Create a new Jira issue."""
        args_parts = args.strip().split(maxsplit=1) if args.strip() else []

        if len(args_parts) < 2:
            self.io.tool_error("Usage: /jira create <project> <summary>")
            return

        project = args_parts[0]
        summary = args_parts[1]

        # Prompt for description
        self.io.tool_output("Enter description (or press Enter to skip):")
        description = input("> ").strip()

        # Create issue
        issue = client.create_issue(
            project=project,
            summary=summary,
            description=description or "Created from FlacoAI"
        )

        formatter.display_created_issue(issue)

    def _jira_search(self, client, formatter, args):
        """Search Jira issues with JQL."""
        if not args.strip():
            self.io.tool_error("Usage: /jira search <JQL>")
            self.io.tool_error("Example: /jira search 'project = PROJ AND status = Open'")
            return

        jql = args.strip()
        issues = client.search_issues(jql)

        # Display summary
        summary = formatter.format_search_results_summary(issues, jql)
        self.io.tool_output(summary)
        self.io.tool_output("")

        # Display table
        formatter.display_issues_table(issues, title=f"Search Results: {jql[:50]}...")

    def _jira_show(self, client, formatter, args):
        """Show details of a Jira issue."""
        issue_key = args.strip().upper()

        if not issue_key:
            self.io.tool_error("Usage: /jira show <KEY>")
            self.io.tool_error("Example: /jira show PROJ-123")
            return

        issue = client.get_issue(issue_key)
        formatter.display_issue(issue, detailed=True)

    def _jira_comment(self, client, formatter, args):
        """Add a comment to a Jira issue."""
        args_parts = args.strip().split(maxsplit=1) if args.strip() else []

        if len(args_parts) < 2:
            self.io.tool_error("Usage: /jira comment <KEY> <text>")
            return

        issue_key = args_parts[0].upper()
        comment_text = args_parts[1]

        client.add_comment(issue_key, comment_text)
        self.io.tool_output(f"✅ Added comment to {issue_key}")

    def _jira_status(self, client, formatter, args):
        """Update issue status."""
        args_parts = args.strip().split(maxsplit=1) if args.strip() else []

        if not args_parts:
            self.io.tool_error("Usage: /jira status <KEY> [status]")
            self.io.tool_error("Omit status to see available transitions")
            return

        issue_key = args_parts[0].upper()

        if len(args_parts) == 1:
            # Show available transitions
            transitions = client.get_transitions(issue_key)
            formatter.display_transition_options(transitions)
            return

        status = args_parts[1]

        # Try to transition
        client.transition_issue(issue_key, status)
        self.io.tool_output(f"✅ Transitioned {issue_key} to {status}")

    def _jira_assign(self, client, formatter, args):
        """Assign an issue to a user."""
        args_parts = args.strip().split(maxsplit=1) if args.strip() else []

        if len(args_parts) < 2:
            self.io.tool_error("Usage: /jira assign <KEY> <username>")
            return

        issue_key = args_parts[0].upper()
        assignee = args_parts[1]

        client.assign_issue(issue_key, assignee)
        self.io.tool_output(f"✅ Assigned {issue_key} to {assignee}")

    def _jira_link(self, client, formatter, args):
        """Link current changes to a Jira issue."""
        issue_key = args.strip().upper()

        if not issue_key:
            self.io.tool_error("Usage: /jira link <KEY>")
            return

        # Get last commit hash if in a git repo
        if not self.coder.repo:
            self.io.tool_error("Not in a git repository")
            return

        try:
            last_commit = self.coder.repo.get_last_commit()
            commit_hash = last_commit.hexsha

            # Try to get repo URL
            repo_url = None
            try:
                origin = self.coder.repo.repo.remotes.origin.url
                # Clean up git URL to https URL
                if origin.startswith('git@'):
                    origin = origin.replace(':', '/').replace('git@', 'https://')
                if origin.endswith('.git'):
                    origin = origin[:-4]
                repo_url = origin
            except:
                pass

            client.link_commit(issue_key, commit_hash, repo_url)
            self.io.tool_output(f"✅ Linked commit {commit_hash[:7]} to {issue_key}")

        except Exception as e:
            self.io.tool_error(f"Failed to link commit: {e}")

    def _jira_from_review(self, client, formatter, args):
        """Create Jira issues from last code review."""
        # Check if there's a ReviewCoder with results
        if not hasattr(self, '_last_review_results'):
            self.io.tool_error("No review results found. Run /review first.")
            return

        # Get project key
        project = args.strip() or os.getenv("JIRA_PROJECT")

        if not project:
            self.io.tool_error("Usage: /jira from-review <project>")
            self.io.tool_error("Or set JIRA_PROJECT environment variable")
            return

        # Get review results
        results = self._last_review_results

        if not results:
            self.io.tool_output("No issues found in last review")
            return

        # Filter by severity (only high and critical)
        from flacoai.analyzers import Severity

        high_severity = [r for r in results if r.severity in [Severity.HIGH, Severity.CRITICAL]]

        if not high_severity:
            self.io.tool_output("No high-severity issues to create tickets for")
            return

        self.io.tool_output(f"Creating {len(high_severity)} Jira issues from review findings...")

        created = []
        for finding in high_severity:
            try:
                summary = f"{finding.title} in {finding.file}:{finding.line}"[:255]

                description = f"""
*Severity:* {finding.severity.value.upper()}
*Category:* {finding.category.value}
*File:* {finding.file}
*Line:* {finding.line}

h3. Description
{finding.description}

h3. Recommendation
{finding.recommendation}

h3. Code Snippet
{{code}}
{finding.code_snippet or 'N/A'}
{{code}}

_Created by FlacoAI Code Review_
"""

                issue_type = "Bug" if finding.category.value == "security" else "Task"

                issue = client.create_issue(
                    project=project,
                    summary=summary,
                    description=description,
                    issue_type=issue_type,
                    labels=["code-review", "flaco-ai", finding.category.value]
                )

                created.append(issue.key)
                self.io.tool_output(f"  ✅ Created {issue.key}")

            except Exception as e:
                self.io.tool_error(f"  ❌ Failed to create issue: {e}")

        if created:
            self.io.tool_output(f"\n✅ Created {len(created)} Jira issue(s): {', '.join(created)}")

    def _jira_my_issues(self, client, formatter, args):
        """Show issues assigned to current user."""
        status = args.strip() or None

        issues = client.get_user_issues(status=status)

        if status:
            title = f"My Issues (Status: {status})"
        else:
            title = "My Assigned Issues"

        formatter.display_issues_table(issues, title=title)

    def _jira_plan(self, client, formatter, args):
        """Generate implementation plan from Jira ticket."""
        if not args or not args.strip():
            self.io.tool_error("Usage: /jira plan <KEY>")
            return

        issue_key = args.strip()

        # Get issue details
        issue = client.get_issue(issue_key)
        if not issue:
            return

        # Display issue
        formatter.display_issue_details(issue)

        self.io.tool_output("\n🔍 Generating implementation plan...\n")

        # Build prompt from issue details
        issue_summary = issue.get('fields', {}).get('summary', 'Unknown')
        issue_description = issue.get('fields', {}).get('description', 'No description')
        issue_type = issue.get('fields', {}).get('issuetype', {}).get('name', 'Task')

        # Get project context if FlacoAI.md exists
        from pathlib import Path
        memory_file = Path(self.coder.root) / "FlacoAI.md"
        project_context = ""

        if memory_file.exists():
            memory_content = memory_file.read_text(encoding='utf-8')[:2000]
            project_context = f"\n\nProject Context:\n{memory_content}"

        prompt = f"""Create a detailed implementation plan for this Jira ticket:

**Ticket:** {issue_key} - {issue_summary}
**Type:** {issue_type}
**Description:**
{issue_description}
{project_context}

Provide a step-by-step implementation plan with:
1. **Understanding** - What problem are we solving?
2. **Approach** - High-level strategy
3. **Files to Modify/Create** - Specific files needed
4. **Implementation Steps** - Numbered steps with details
5. **Testing Strategy** - How to verify it works
6. **Acceptance Criteria** - How do we know it's done?

Focus on Swift/iOS best practices."""

        try:
            response = self.coder.send_message(prompt, system_prompt="You are a technical architect specializing in Swift/iOS. Create detailed, actionable implementation plans from Jira tickets.")

            if response:
                self.io.tool_output("="*75)
                self.io.tool_output(f"📋 Implementation Plan: {issue_key}")
                self.io.tool_output("="*75)
                self.io.tool_output(response)
                self.io.tool_output("="*75 + "\n")
                self.io.tool_output(f"💡 Tip: Use '/jira link {issue_key}' when you start working on this")
                self.io.tool_output("💡 Tip: Use '/mode architect' for architecture-focused development")

        except Exception as e:
            self.io.tool_error(f"Error generating plan: {e}")

    def cmd_init(self, args):
        """Initialize or refresh project memory

        /init [--force]    - Scan project and generate/update FlacoAI.md

        This command analyzes your Swift/iOS project structure, detects architecture
        patterns, and creates a FlacoAI.md file that helps FlacoAI understand your
        project better. Manual sections are preserved on refresh.
        """
        self._track_command("init")

        from flacoai.project_memory import init_project_memory

        force = "--force" in args if args else False

        self.io.tool_output("🔍 Scanning project...")

        try:
            file_path, was_created = init_project_memory(
                repo_root=self.coder.root,
                force=force
            )

            if was_created:
                self.io.tool_output(f"\n✅ Created {file_path}")
                self.io.tool_output("\n💡 Next steps:")
                self.io.tool_output("   1. Review and customize the manual sections in FlacoAI.md")
                self.io.tool_output("   2. Use '/memory note <text>' to add quick notes")
                self.io.tool_output("   3. Run '/memory show' to view project memory")
            else:
                self.io.tool_output(f"\n✅ Updated {file_path}")
                self.io.tool_output("\n💡 Manual sections preserved. Use '/memory show' to review.")

        except Exception as e:
            self.io.tool_error(f"Error initializing project memory: {e}")

    def cmd_memory(self, args):
        """Manage project memory (FlacoAI.md)

        /memory show              - Display current project memory
        /memory refresh           - Regenerate auto sections (preserves manual edits)
        /memory note <text>       - Add a quick note to Rules & Preferences
        """
        self._track_command("memory")

        from flacoai.project_memory import init_project_memory, add_memory_note, ProjectScanner
        from pathlib import Path

        # Parse subcommand
        args_parts = args.strip().split(maxsplit=1) if args.strip() else []

        if not args_parts:
            subcommand = "show"
            subargs = ""
        else:
            subcommand = args_parts[0].lower()
            subargs = args_parts[1] if len(args_parts) > 1 else ""

        memory_file = Path(self.coder.root) / "FlacoAI.md"

        try:
            if subcommand == "show":
                # Display current memory file
                if not memory_file.exists():
                    self.io.tool_error("FlacoAI.md not found. Run '/init' first.")
                    return

                content = memory_file.read_text(encoding='utf-8')
                self.io.tool_output("\n" + "="*75)
                self.io.tool_output(content)
                self.io.tool_output("="*75 + "\n")

            elif subcommand == "refresh":
                # Refresh auto sections
                if not memory_file.exists():
                    self.io.tool_error("FlacoAI.md not found. Run '/init' first.")
                    return

                self.io.tool_output("🔄 Refreshing project memory...")
                file_path, _ = init_project_memory(
                    repo_root=self.coder.root,
                    force=True
                )
                self.io.tool_output(f"✅ Refreshed {file_path}")

            elif subcommand == "note":
                # Add quick note
                if not subargs:
                    self.io.tool_error("Usage: /memory note <text>")
                    return

                if not memory_file.exists():
                    self.io.tool_error("FlacoAI.md not found. Run '/init' first.")
                    return

                success = add_memory_note(
                    repo_root=self.coder.root,
                    note=subargs
                )

                if success:
                    self.io.tool_output(f"✅ Added note to FlacoAI.md")
                else:
                    self.io.tool_error("Failed to add note")

            else:
                self.io.tool_error(f"Unknown subcommand: {subcommand}")
                self.io.tool_error("Available: show, refresh, note")

        except Exception as e:
            self.io.tool_error(f"Memory error: {e}")

    def cmd_llm(self, args):
        """Manage LLM models

        /llm list                 - Show available models
        /llm use <model>          - Switch to a specific model
        /llm search <term>        - Search for models by name

        Popular local models:
          - qwen2.5-coder:32b      (Qwen 2.5 Coder 32B)
          - deepseek-coder-v2:16b  (DeepSeek Coder V2 16B)
          - deepseek-r1:32b        (DeepSeek R1 32B - Reasoning)
        """
        self._track_command("llm")

        # Parse subcommand
        args_parts = args.strip().split(maxsplit=1) if args.strip() else []

        if not args_parts:
            subcommand = "list"
            subargs = ""
        else:
            subcommand = args_parts[0].lower()
            subargs = args_parts[1] if len(args_parts) > 1 else ""

        try:
            if subcommand == "list":
                self._llm_list(subargs)

            elif subcommand == "use":
                if not subargs:
                    self.io.tool_error("Usage: /llm use <model>")
                    return
                # Delegate to cmd_model
                self.cmd_model(subargs)

            elif subcommand == "search":
                if not subargs:
                    self.io.tool_error("Usage: /llm search <term>")
                    return
                self._llm_search(subargs)

            else:
                self.io.tool_error(f"Unknown subcommand: {subcommand}")
                self.io.tool_error("Available: list, use, search")

        except Exception as e:
            if "SwitchCoder" not in str(type(e).__name__):
                self.io.tool_error(f"LLM error: {e}")
            else:
                # Re-raise SwitchCoder exceptions (model switching)
                raise

    def _llm_list(self, category=None):
        """List available models."""
        from flacoai.models import MODEL_ALIASES, MODEL_SETTINGS

        self.io.tool_output("\n" + "="*75)
        self.io.tool_output("🤖 Available Models")
        self.io.tool_output("="*75 + "\n")

        # Show current model
        current_model = self.coder.main_model.name
        self.io.tool_output(f"📍 Current Model: {current_model}\n")

        # Popular local models (Ollama-compatible)
        self.io.tool_output("🏠 Popular Local Models (Ollama):")
        local_models = [
            ("qwen2.5-coder:32b", "Qwen 2.5 Coder 32B - Excellent for coding"),
            ("deepseek-coder-v2:16b", "DeepSeek Coder V2 16B - Fast and capable"),
            ("deepseek-r1:32b", "DeepSeek R1 32B - Advanced reasoning"),
            ("llama3.1:70b", "Llama 3.1 70B - General purpose"),
            ("codestral:22b", "Codestral 22B - Code specialist"),
        ]

        for model_name, description in local_models:
            marker = "✓" if model_name == current_model else " "
            self.io.tool_output(f"  [{marker}] {model_name:<30} {description}")

        self.io.tool_output("")

        # Popular cloud models
        self.io.tool_output("☁️  Popular Cloud Models:")
        cloud_models = [
            ("gpt-4o", "OpenAI GPT-4 Optimized - Latest flagship"),
            ("gpt-4-turbo", "OpenAI GPT-4 Turbo - Fast and capable"),
            ("claude-3-5-sonnet-20241022", "Claude 3.5 Sonnet - Excellent for coding"),
            ("claude-3-opus-20240229", "Claude 3 Opus - Most capable"),
        ]

        for model_name, description in cloud_models:
            marker = "✓" if model_name == current_model else " "
            self.io.tool_output(f"  [{marker}] {model_name:<35} {description}")

        self.io.tool_output("")

        # Model aliases
        self.io.tool_output("🔗 Quick Aliases:")
        popular_aliases = {
            "sonnet": "anthropic/claude-sonnet-4-20250514",
            "opus": "claude-3-opus-20240229",
            "4": "gpt-4-turbo",
            "4o": "gpt-4o",
        }

        for alias, full_name in popular_aliases.items():
            marker = "✓" if full_name == current_model or alias == current_model else " "
            self.io.tool_output(f"  [{marker}] {alias:<10} → {full_name}")

        self.io.tool_output("")
        self.io.tool_output("💡 Tip: Use '/llm use <model>' to switch models")
        self.io.tool_output("💡 Tip: Use '/llm search <term>' to find specific models")
        self.io.tool_output("="*75 + "\n")

    def _llm_search(self, search_term):
        """Search for models by name."""
        from flacoai.models import fuzzy_match_models

        matches = fuzzy_match_models(search_term)

        if not matches:
            self.io.tool_output(f"No models found matching '{search_term}'")
            return

        self.io.tool_output(f"\n🔍 Models matching '{search_term}':\n")

        current_model = self.coder.main_model.name

        for model_name in matches[:20]:  # Limit to top 20
            marker = "✓" if model_name == current_model else " "
            self.io.tool_output(f"  [{marker}] {model_name}")

        if len(matches) > 20:
            self.io.tool_output(f"\n  ... and {len(matches) - 20} more matches")

        self.io.tool_output(f"\n💡 Use '/llm use <model>' to switch\n")

    def cmd_commit_msg(self, args):
        """Generate AI-powered commit message from changes

        /commit-msg [--write]    - Analyze changes and suggest commit message
                                   Use --write to create the commit automatically
        """
        self._track_command("commit-msg")

        if not self.coder.repo:
            self.io.tool_error("No git repository found.")
            return

        write_commit = "--write" in args if args else False

        try:
            # Get current diff
            diff = self.coder.repo.diff_commits(
                self.coder.pretty,
                "HEAD",
                include_working_dir=True
            )

            if not diff or not diff.strip():
                self.io.tool_error("No changes to analyze.")
                return

            self.io.tool_output("🔍 Analyzing changes...")

            # Build prompt for LLM
            prompt = f"""Based on the following git diff, generate a clear, concise commit message.

Follow these guidelines:
- Use conventional commit format: type(scope): subject
- Types: feat, fix, refactor, docs, test, chore, style
- Keep subject under 50 characters
- Focus on the "why" not the "what"
- Be specific and actionable

Git Diff:
```diff
{diff[:3000]}  # Limit diff size
```

Generate only the commit message, nothing else."""

            # Ask LLM to generate commit message
            response = self.coder.send_message(prompt, system_prompt="You are a commit message generator. Generate clear, conventional commit messages.")

            if not response:
                self.io.tool_error("Failed to generate commit message.")
                return

            # Extract commit message from response
            commit_msg = response.strip()

            # Clean up if LLM included extra formatting
            if "```" in commit_msg:
                # Extract from code block
                parts = commit_msg.split("```")
                for part in parts:
                    if part.strip() and not part.startswith("diff"):
                        commit_msg = part.strip()
                        break

            self.io.tool_output("\n" + "="*75)
            self.io.tool_output("📝 Suggested Commit Message:")
            self.io.tool_output("="*75)
            self.io.tool_output(commit_msg)
            self.io.tool_output("="*75 + "\n")

            if write_commit:
                # Create commit with this message
                self.coder.repo.commit(message=commit_msg)
                self.io.tool_output("✅ Commit created successfully!")
            else:
                self.io.tool_output("💡 Use '/commit-msg --write' to create the commit with this message")

        except Exception as e:
            self.io.tool_error(f"Error generating commit message: {e}")

    def cmd_review_diff(self, args):
        """Review uncommitted changes with AI

        /review-diff    - Analyze current changes for potential issues
        """
        self._track_command("review-diff")

        if not self.coder.repo:
            self.io.tool_error("No git repository found.")
            return

        try:
            # Get current diff
            diff = self.coder.repo.diff_commits(
                self.coder.pretty,
                "HEAD",
                include_working_dir=True
            )

            if not diff or not diff.strip():
                self.io.tool_error("No changes to review.")
                return

            self.io.tool_output("🔍 Reviewing changes...\n")

            # Build prompt for LLM
            prompt = f"""Review the following git diff and provide feedback.

Focus on:
1. Potential bugs or issues
2. Code quality concerns
3. Swift/iOS best practices
4. Performance implications
5. Security considerations

Git Diff:
```diff
{diff[:4000]}  # Limit diff size
```

Provide a concise review with specific line-by-line feedback where relevant."""

            # Ask LLM to review
            response = self.coder.send_message(prompt, system_prompt="You are a code reviewer specializing in Swift/iOS. Provide helpful, constructive feedback.")

            if not response:
                self.io.tool_error("Failed to review changes.")
                return

            self.io.tool_output("="*75)
            self.io.tool_output("📋 Code Review:")
            self.io.tool_output("="*75)
            self.io.tool_output(response)
            self.io.tool_output("="*75 + "\n")

            self.io.tool_output("💡 Tip: Use '/commit-msg' to generate a commit message after addressing feedback")

        except Exception as e:
            self.io.tool_error(f"Error reviewing diff: {e}")

    def cmd_mode(self, args):
        """Switch work mode (architect, bugfix, refactor)

        /mode [architect|bugfix|refactor]    - Switch to a specific mode
        /mode                                 - Show current mode

        Modes:
          architect  - Focus on design, architecture, and big picture
          bugfix     - Focus on finding and fixing bugs
          refactor   - Focus on code quality and refactoring
        """
        self._track_command("mode")

        # Initialize mode if not set
        if not hasattr(self.coder, 'work_mode'):
            self.coder.work_mode = 'default'

        mode = args.strip().lower() if args and args.strip() else None

        MODES = {
            'architect': {
                'name': 'Architect',
                'icon': '🏗️',
                'description': 'Design-focused mode for planning and architecture',
                'prompt_addition': """
Work in ARCHITECT mode:
- Think about overall system design and architecture
- Consider scalability, maintainability, and extensibility
- Suggest patterns and best practices
- Focus on the big picture before diving into implementation
- Plan before coding
"""
            },
            'bugfix': {
                'name': 'Bug Fix',
                'icon': '🐛',
                'description': 'Debugging-focused mode for finding and fixing issues',
                'prompt_addition': """
Work in BUGFIX mode:
- Focus on identifying root causes
- Suggest minimal, surgical fixes
- Consider edge cases and error conditions
- Add defensive programming where needed
- Think about testing to prevent regressions
"""
            },
            'refactor': {
                'name': 'Refactor',
                'icon': '♻️',
                'description': 'Code quality-focused mode for improving existing code',
                'prompt_addition': """
Work in REFACTOR mode:
- Improve code quality without changing behavior
- Reduce complexity and improve readability
- Eliminate code smells and duplication
- Follow Swift/iOS best practices
- Maintain backward compatibility unless explicitly asked
"""
            },
            'default': {
                'name': 'Default',
                'icon': '⚙️',
                'description': 'Balanced mode for general development',
                'prompt_addition': ''
            }
        }

        if not mode:
            # Show current mode
            current = MODES.get(self.coder.work_mode, MODES['default'])
            self.io.tool_output(f"\n{current['icon']} Current Mode: {current['name']}")
            self.io.tool_output(f"   {current['description']}\n")
            self.io.tool_output("💡 Available modes: architect, bugfix, refactor")
            self.io.tool_output("💡 Use '/mode <mode>' to switch\n")
            return

        if mode not in MODES or mode == 'default':
            self.io.tool_error(f"Unknown mode: {mode}")
            self.io.tool_error("Available modes: architect, bugfix, refactor")
            return

        # Set the mode
        self.coder.work_mode = mode
        mode_info = MODES[mode]

        # Store the prompt addition for use in future messages
        if not hasattr(self.coder, 'mode_prompt_additions'):
            self.coder.mode_prompt_additions = {}
        self.coder.mode_prompt_additions['work_mode'] = mode_info['prompt_addition']

        self.io.tool_output(f"\n✅ Switched to {mode_info['icon']} {mode_info['name']} mode")
        self.io.tool_output(f"   {mode_info['description']}\n")

    def cmd_standup(self, args):
        """Generate standup summary from recent git activity

        /standup [days]    - Summarize work from last N days (default: 1)
        """
        self._track_command("standup")

        if not self.coder.repo:
            self.io.tool_error("No git repository found.")
            return

        # Parse days argument
        days = 1
        if args and args.strip().isdigit():
            days = int(args.strip())

        try:
            import subprocess
            from datetime import datetime, timedelta

            # Get commits from last N days
            since_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
            result = subprocess.run(
                ['git', 'log', f'--since={since_date}', '--pretty=format:%h|%an|%ar|%s', '--no-merges'],
                cwd=self.coder.root,
                capture_output=True,
                text=True
            )

            commits = result.stdout.strip().split('\n') if result.stdout.strip() else []

            if not commits or commits == ['']:
                self.io.tool_output(f"\n📊 No commits found in the last {days} day(s).\n")
                return

            # Format commit log
            commit_log = "\n".join([f"- {c.split('|')[3]} ({c.split('|')[0]})" for c in commits])

            self.io.tool_output("🔍 Analyzing recent work...\n")

            # Build prompt for LLM
            prompt = f"""Based on the following git commits from the last {days} day(s), generate a concise standup summary.

Format:
✅ **Completed:**
- [Brief summary of work done]

🚀 **Next:**
- [What should be worked on next]

Commits:
{commit_log}

Keep it brief and focus on the impact, not the technical details."""

            response = self.coder.send_message(prompt, system_prompt="You are a project manager generating standup summaries. Be concise and focus on outcomes.")

            if response:
                self.io.tool_output("="*75)
                self.io.tool_output(f"📊 Standup Summary ({days} day(s))")
                self.io.tool_output("="*75)
                self.io.tool_output(response)
                self.io.tool_output("="*75 + "\n")

        except Exception as e:
            self.io.tool_error(f"Error generating standup: {e}")

    def cmd_summary(self, args):
        """Generate project summary

        /summary    - Summarize project structure and current state
        """
        self._track_command("summary")

        from pathlib import Path

        memory_file = Path(self.coder.root) / "FlacoAI.md"

        try:
            # Gather project info
            info_parts = []

            # Check for FlacoAI.md
            if memory_file.exists():
                info_parts.append("📝 Project memory available (FlacoAI.md)")
                memory_content = memory_file.read_text(encoding='utf-8')[:1000]
                info_parts.append(f"\nProject Memory Preview:\n{memory_content}...")
            else:
                info_parts.append("📝 No project memory found. Run /init to create FlacoAI.md")

            # Git status
            if self.coder.repo:
                info_parts.append("\n📊 Git Status:")
                try:
                    import subprocess
                    result = subprocess.run(
                        ['git', 'status', '--short'],
                        cwd=self.coder.root,
                        capture_output=True,
                        text=True
                    )
                    status_lines = result.stdout.strip().split('\n') if result.stdout.strip() else []
                    if status_lines and status_lines != ['']:
                        info_parts.append(f"  {len(status_lines)} file(s) with changes")
                    else:
                        info_parts.append("  Working directory clean")
                except Exception:
                    pass

            # File count
            swift_files = list(Path(self.coder.root).rglob('*.swift'))
            info_parts.append(f"\n📁 Project Stats:")
            info_parts.append(f"  {len(swift_files)} Swift files")

            summary_text = "\n".join(info_parts)

            self.io.tool_output("\n" + "="*75)
            self.io.tool_output("📋 Project Summary")
            self.io.tool_output("="*75)
            self.io.tool_output(summary_text)
            self.io.tool_output("="*75 + "\n")

        except Exception as e:
            self.io.tool_error(f"Error generating summary: {e}")

    def cmd_plan(self, args):
        """Generate implementation plan for a task

        /plan <task description>    - Create step-by-step implementation plan
        """
        self._track_command("plan")

        if not args or not args.strip():
            self.io.tool_error("Usage: /plan <task description>")
            return

        task = args.strip()

        try:
            self.io.tool_output("🔍 Planning implementation...\n")

            # Build context from FlacoAI.md if available
            from pathlib import Path
            memory_file = Path(self.coder.root) / "FlacoAI.md"
            project_context = ""

            if memory_file.exists():
                memory_content = memory_file.read_text(encoding='utf-8')[:2000]
                project_context = f"\n\nProject Context:\n{memory_content}"

            prompt = f"""Create a detailed implementation plan for the following task:

**Task:** {task}
{project_context}

Provide a step-by-step plan with:
1. **Approach** - High-level strategy
2. **Files to Modify/Create** - Specific files needed
3. **Implementation Steps** - Numbered steps with details
4. **Testing Strategy** - How to verify it works
5. **Potential Challenges** - Things to watch out for

Focus on Swift/iOS best practices."""

            response = self.coder.send_message(prompt, system_prompt="You are a technical architect specializing in Swift/iOS. Create detailed, actionable implementation plans.")

            if response:
                self.io.tool_output("="*75)
                self.io.tool_output(f"📋 Implementation Plan: {task}")
                self.io.tool_output("="*75)
                self.io.tool_output(response)
                self.io.tool_output("="*75 + "\n")
                self.io.tool_output("💡 Tip: Use '/mode architect' for architecture-focused development")

        except Exception as e:
            self.io.tool_error(f"Error generating plan: {e}")

    def cmd_tour(self, args):
        """Generate guided tour of the codebase

        /tour [component]    - Generate code tour (optionally focused on component)
        """
        self._track_command("tour")

        component = args.strip() if args else None

        try:
            from pathlib import Path

            self.io.tool_output("🔍 Analyzing codebase structure...\n")

            # Get project structure
            swift_files = list(Path(self.coder.root).rglob('*.swift'))

            if not swift_files:
                self.io.tool_error("No Swift files found in project.")
                return

            # Sample key files
            key_files = []
            for pattern in ['App.swift', 'main.swift', 'ViewController.swift', 'View.swift', 'Model.swift']:
                matches = [f for f in swift_files if pattern in f.name]
                key_files.extend(matches[:3])  # Max 3 per pattern

            # Limit to 10 key files
            key_files = key_files[:10]

            # Read sample of each file
            file_samples = []
            for file_path in key_files:
                try:
                    content = file_path.read_text(encoding='utf-8')
                    # Get first 20 lines
                    lines = content.split('\n')[:20]
                    sample = '\n'.join(lines)
                    rel_path = file_path.relative_to(self.coder.root)
                    file_samples.append(f"File: {rel_path}\n{sample}\n...")
                except Exception:
                    pass

            files_overview = "\n\n".join(file_samples[:5])  # Limit to 5 files

            focus = f" focusing on {component}" if component else ""

            prompt = f"""Generate a guided tour of this Swift/iOS codebase{focus}.

Project Structure:
- {len(swift_files)} Swift files total

Key Files:
{files_overview}

Create a tour that explains:
1. **Project Overview** - What this project does
2. **Architecture** - How the code is organized
3. **Key Components** - Main files/modules and their purpose
4. **Getting Started** - Where to begin exploring
5. **Common Workflows** - Typical development tasks

Make it friendly and educational for new developers."""

            response = self.coder.send_message(prompt, system_prompt="You are a friendly technical guide. Create engaging code tours that help developers understand codebases.")

            if response:
                self.io.tool_output("="*75)
                self.io.tool_output(f"🗺️  Codebase Tour{f': {component}' if component else ''}")
                self.io.tool_output("="*75)
                self.io.tool_output(response)
                self.io.tool_output("="*75 + "\n")

        except Exception as e:
            self.io.tool_error(f"Error generating tour: {e}")

    def cmd_settings(self, args):
        "Print out the current settings"
        settings = format_settings(self.parser, self.args)
        announcements = "\n".join(self.coder.get_announcements())

        # Build metadata for the active models (main, editor, weak)
        model_sections = []
        active_models = [
            ("Main model", self.coder.main_model),
            ("Editor model", getattr(self.coder.main_model, "editor_model", None)),
            ("Weak model", getattr(self.coder.main_model, "weak_model", None)),
        ]
        for label, model in active_models:
            if not model:
                continue
            info = getattr(model, "info", {}) or {}
            if not info:
                continue
            model_sections.append(f"{label} ({model.name}):")
            for k, v in sorted(info.items()):
                model_sections.append(f"  {k}: {v}")
            model_sections.append("")  # blank line between models

        model_metadata = "\n".join(model_sections)

        output = f"{announcements}\n{settings}"
        if model_metadata:
            output += "\n" + model_metadata
        self.io.tool_output(output)

    def completions_raw_load(self, document, complete_event):
        return self.completions_raw_read_only(document, complete_event)

    def cmd_load(self, args):
        "Load and execute commands from a file"
        if not args.strip():
            self.io.tool_error("Please provide a filename containing commands to load.")
            return

        try:
            with open(args.strip(), "r", encoding=self.io.encoding, errors="replace") as f:
                commands = f.readlines()
        except FileNotFoundError:
            self.io.tool_error(f"File not found: {args}")
            return
        except Exception as e:
            self.io.tool_error(f"Error reading file: {e}")
            return

        for cmd in commands:
            cmd = cmd.strip()
            if not cmd or cmd.startswith("#"):
                continue

            self.io.tool_output(f"\nExecuting: {cmd}")
            try:
                self.run(cmd)
            except SwitchCoder:
                self.io.tool_error(
                    f"Command '{cmd}' is only supported in interactive mode, skipping."
                )

    def completions_raw_save(self, document, complete_event):
        return self.completions_raw_read_only(document, complete_event)

    def cmd_save(self, args):
        "Save commands to a file that can reconstruct the current chat session's files"
        if not args.strip():
            self.io.tool_error("Please provide a filename to save the commands to.")
            return

        try:
            with open(args.strip(), "w", encoding=self.io.encoding) as f:
                f.write("/drop\n")
                # Write commands to add editable files
                for fname in sorted(self.coder.abs_fnames):
                    rel_fname = self.coder.get_rel_fname(fname)
                    f.write(f"/add       {rel_fname}\n")

                # Write commands to add read-only files
                for fname in sorted(self.coder.abs_read_only_fnames):
                    # Use absolute path for files outside repo root, relative path for files inside
                    if Path(fname).is_relative_to(self.coder.root):
                        rel_fname = self.coder.get_rel_fname(fname)
                        f.write(f"/read-only {rel_fname}\n")
                    else:
                        f.write(f"/read-only {fname}\n")

            self.io.tool_output(f"Saved commands to {args.strip()}")
        except Exception as e:
            self.io.tool_error(f"Error saving commands to file: {e}")

    def cmd_multiline_mode(self, args):
        "Toggle multiline mode (swaps behavior of Enter and Meta+Enter)"
        self.io.toggle_multiline_mode()

    def cmd_copy(self, args):
        "Copy the last assistant message to the clipboard"
        all_messages = self.coder.done_messages + self.coder.cur_messages
        assistant_messages = [msg for msg in reversed(all_messages) if msg["role"] == "assistant"]

        if not assistant_messages:
            self.io.tool_error("No assistant messages found to copy.")
            return

        last_assistant_message = assistant_messages[0]["content"]

        try:
            pyperclip.copy(last_assistant_message)
            preview = (
                last_assistant_message[:50] + "..."
                if len(last_assistant_message) > 50
                else last_assistant_message
            )
            self.io.tool_output(f"Copied last assistant message to clipboard. Preview: {preview}")
        except pyperclip.PyperclipException as e:
            self.io.tool_error(f"Failed to copy to clipboard: {str(e)}")
            self.io.tool_output(
                "You may need to install xclip or xsel on Linux, or pbcopy on macOS."
            )
        except Exception as e:
            self.io.tool_error(f"An unexpected error occurred while copying to clipboard: {str(e)}")

    def cmd_report(self, args):
        "Report a problem by opening a GitHub Issue"
        from flacoai.report import report_github_issue

        announcements = "\n".join(self.coder.get_announcements())
        issue_text = announcements

        if args.strip():
            title = args.strip()
        else:
            title = None

        report_github_issue(issue_text, title=title, confirm=False)

    def cmd_editor(self, initial_content=""):
        "Open an editor to write a prompt"

        user_input = pipe_editor(initial_content, suffix="md", editor=self.editor)
        if user_input.strip():
            self.io.set_placeholder(user_input.rstrip())

    def cmd_edit(self, args=""):
        "Alias for /editor: Open an editor to write a prompt"
        return self.cmd_editor(args)

    def cmd_think_tokens(self, args):
        """Set the thinking token budget, eg: 8096, 8k, 10.5k, 0.5M, or 0 to disable."""
        model = self.coder.main_model

        if not args.strip():
            # Display current value if no args are provided
            formatted_budget = model.get_thinking_tokens()
            if formatted_budget is None:
                self.io.tool_output("Thinking tokens are not currently set.")
            else:
                budget = model.get_raw_thinking_tokens()
                self.io.tool_output(
                    f"Current thinking token budget: {budget:,} tokens ({formatted_budget})."
                )
            return

        value = args.strip()
        model.set_thinking_tokens(value)

        # Handle the special case of 0 to disable thinking tokens
        if value == "0":
            self.io.tool_output("Thinking tokens disabled.")
        else:
            formatted_budget = model.get_thinking_tokens()
            budget = model.get_raw_thinking_tokens()
            self.io.tool_output(
                f"Set thinking token budget to {budget:,} tokens ({formatted_budget})."
            )

        self.io.tool_output()

        # Output announcements
        announcements = "\n".join(self.coder.get_announcements())
        self.io.tool_output(announcements)

    def cmd_reasoning_effort(self, args):
        "Set the reasoning effort level (values: number or low/medium/high depending on model)"
        model = self.coder.main_model

        if not args.strip():
            # Display current value if no args are provided
            reasoning_value = model.get_reasoning_effort()
            if reasoning_value is None:
                self.io.tool_output("Reasoning effort is not currently set.")
            else:
                self.io.tool_output(f"Current reasoning effort: {reasoning_value}")
            return

        value = args.strip()
        model.set_reasoning_effort(value)
        reasoning_value = model.get_reasoning_effort()
        self.io.tool_output(f"Set reasoning effort to {reasoning_value}")
        self.io.tool_output()

        # Output announcements
        announcements = "\n".join(self.coder.get_announcements())
        self.io.tool_output(announcements)

    def cmd_copy_context(self, args=None):
        """Copy the current chat context as markdown, suitable to paste into a web UI"""

        chunks = self.coder.format_chat_chunks()

        markdown = ""

        # Only include specified chunks in order
        for messages in [chunks.repo, chunks.readonly_files, chunks.chat_files]:
            for msg in messages:
                # Only include user messages
                if msg["role"] != "user":
                    continue

                content = msg["content"]

                # Handle image/multipart content
                if isinstance(content, list):
                    for part in content:
                        if part.get("type") == "text":
                            markdown += part["text"] + "\n\n"
                else:
                    markdown += content + "\n\n"

        args = args or ""
        markdown += f"""
Just tell me how to edit the files to make the changes.
Don't give me back entire files.
Just show me the edits I need to make.

{args}
"""

        try:
            pyperclip.copy(markdown)
            self.io.tool_output("Copied code context to clipboard.")
        except pyperclip.PyperclipException as e:
            self.io.tool_error(f"Failed to copy to clipboard: {str(e)}")
            self.io.tool_output(
                "You may need to install xclip or xsel on Linux, or pbcopy on macOS."
            )
        except Exception as e:
            self.io.tool_error(f"An unexpected error occurred while copying to clipboard: {str(e)}")


def expand_subdir(file_path):
    if file_path.is_file():
        yield file_path
        return

    if file_path.is_dir():
        for file in file_path.rglob("*"):
            if file.is_file():
                yield file


def parse_quoted_filenames(args):
    filenames = re.findall(r"\"(.+?)\"|(\S+)", args)
    filenames = [name for sublist in filenames for name in sublist if name]
    return filenames


def get_help_md():
    md = Commands(None, None).get_help_md()
    return md


def main():
    md = get_help_md()
    print(md)


if __name__ == "__main__":
    status = main()
    sys.exit(status)
