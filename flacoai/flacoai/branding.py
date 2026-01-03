"""FlacoAI branding and startup UI elements."""

import random
from datetime import datetime


def get_flaco_ascii_art(version="1.0.0"):
    """Generate FlacoAI ASCII art banner.

    Args:
        version: Version string (not used, kept for compatibility)

    Returns:
        ASCII art banner as string
    """
    return """╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║      ███████╗ ██╗      █████╗   ██████╗  ██████╗       █████╗  ██╗        ║
║      ██╔════╝ ██║     ██╔══██╗ ██╔════╝ ██╔═══██╗     ██╔══██╗ ██║        ║
║      █████╗   ██║     ███████║ ██║      ██║   ██║     ███████║ ██║        ║
║      ██╔══╝   ██║     ██╔══██║ ██║      ██║   ██║     ██╔══██║ ██║        ║
║      ██║      ███████╗██║  ██║ ╚██████╗ ╚██████╔╝     ██║  ██║ ██║        ║
║      ╚═╝      ╚══════╝╚═╝  ╚═╝  ╚═════╝  ╚═════╝      ╚═╝  ╚═╝ ╚═╝        ║
║                                                                           ║
║        🚀 The Ultimate Local-First Swift & iOS Development Assistant      ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝"""


# Keep old constant for backwards compatibility, but use function
FLACO_ASCII_ART = get_flaco_ascii_art()

STARTUP_TIPS = [
    "🍎 Run /init to let Flaco AI analyze your Swift/iOS project",
    "🎟️  Link a Jira ticket with /jira link KEY to work ticket-first",
    "📝 Use /commit-msg to generate clear commit messages from your changes",
    "🔍 Run /review to get comprehensive code analysis for your Swift code",
    "🗺️  Use /tour to generate a guided tour of your codebase",
    "🎯 Switch modes with /mode: architect, bugfix, or refactor",
    "💡 Run /diff to see a natural language summary of your changes",
    "🧠 Use /memory note to add project-specific context to FlacoAI.md",
    "⚡ Type /llm to switch between local and cloud models",
    "🚀 Use /jira plan to break down a ticket into implementation steps",
    "📊 Run /standup to summarize today's work for your team",
    "🎨 Use /generate login to create SwiftUI views from templates",
    "📝 Type /help to see all available Flaco AI commands",
]


def get_session_info(repo=None):
    """Get current session information.

    Args:
        repo: GitRepo object (optional)

    Returns:
        Dictionary with session info
    """
    import os
    from pathlib import Path

    info = {
        'directory': os.getcwd(),
        'session_start': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'git_branch': None,
    }

    # Try to get git branch
    if repo and hasattr(repo, 'repo'):
        try:
            info['git_branch'] = repo.repo.active_branch.name
        except Exception:
            pass

    # Shorten directory path if it's too long
    home = str(Path.home())
    if info['directory'].startswith(home):
        info['directory'] = '~' + info['directory'][len(home):]

    return info


def format_session_header(session_info):
    """Format session info for display in header.

    Args:
        session_info: Dictionary with session info

    Returns:
        Formatted string
    """
    parts = []

    # Directory
    parts.append(f"📁  {session_info['directory']}")

    # Git branch
    if session_info.get('git_branch'):
        parts.append(f"🌿  {session_info['git_branch']}")

    # Session start time
    parts.append(f"🕐  {session_info['session_start']}")

    # Join with visual separator
    separator = "  │  "
    header = separator.join(parts)

    # Add a decorative line
    border = "─" * min(len(header), 75)

    return f"{header}\n{border}"


def get_welcome_message(git_config=None):
    """Generate personalized welcome message based on time and git config.

    Args:
        git_config: Dictionary with git user info (optional)

    Returns:
        Personalized greeting string
    """
    hour = datetime.now().hour

    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    # Get name from git config
    name = None
    if git_config and isinstance(git_config, dict):
        name = git_config.get("user.name") or git_config.get("name")

    if not name or name in ["Your Name", "you@example.com"]:
        name = "Developer"

    return f"{greeting}, {name}! Welcome back."


def get_random_tip():
    """Get a random startup tip.

    Returns:
        Random tip string
    """
    return random.choice(STARTUP_TIPS)


def get_promotional_message():
    """Get promotional/announcement message.

    Returns:
        Promotional message string or None
    """
    # You can customize this or pull from an API
    # For now, return a simple message
    return "💡 Pro tip: Use /review before committing to catch issues early!"


def format_model_info(model_name, edit_format=None):
    """Format model information for display.

    Args:
        model_name: Name of the model
        edit_format: Edit format being used (optional)

    Returns:
        Formatted model info string
    """
    info = f"Model: {model_name}"

    if edit_format:
        info += f" · Format: {edit_format}"

    return info


def format_stats(files_count=0, commits_count=0, session_duration=None):
    """Format session statistics.

    Args:
        files_count: Number of files in context
        commits_count: Number of commits in session
        session_duration: Duration of session (optional)

    Returns:
        Formatted stats string
    """
    stats = []

    if files_count > 0:
        stats.append(f"{files_count} file{'s' if files_count != 1 else ''}")

    if commits_count > 0:
        stats.append(f"{commits_count} commit{'s' if commits_count != 1 else ''}")

    if session_duration:
        stats.append(f"{session_duration}")

    if stats:
        return " · ".join(stats)

    return "No activity yet"


def format_directory_note(current_dir, git_dir):
    """Format the directory note shown below the header.

    Args:
        current_dir: Current working directory
        git_dir: Git working directory (repo root)

    Returns:
        Formatted note string with yellow triangle icon
    """
    from pathlib import Path

    # Shorten paths with ~
    home = str(Path.home())
    if current_dir.startswith(home):
        current_dir = '~' + current_dir[len(home):]
    if git_dir and git_dir.startswith(home):
        git_dir = '~' + git_dir[len(home):]

    note_lines = []
    note_lines.append("⚠️  Note: in-chat filenames are always relative to the git working dir, not the current working dir.")
    note_lines.append(f"Cur working dir: {current_dir}")
    if git_dir and git_dir != current_dir:
        note_lines.append(f"Git working dir: {git_dir}")

    return "\n".join(note_lines)


def format_compact_header(model_name, edit_format, directory, branch=None, file_count=0,
                         thinking_tokens=None, reasoning_effort=None, cache_enabled=False,
                         infinite_output=False, repo_map_tokens=None, repo_map_refresh=None):
    """Format a compact, organized header (3 labeled lines).

    Args:
        model_name: LLM model name
        edit_format: Edit format being used
        directory: Working directory path
        branch: Git branch name (optional)
        file_count: Number of files in repo
        thinking_tokens: Thinking token budget (optional)
        reasoning_effort: Reasoning effort setting (optional)
        cache_enabled: Whether prompt caching is enabled
        infinite_output: Whether infinite output is supported
        repo_map_tokens: Repo-map token count (optional)
        repo_map_refresh: Repo-map refresh setting (optional)

    Returns:
        Formatted header string (3 lines with labels)
    """
    # Strip "openai/" prefix for local models (cleaner display)
    if model_name.startswith("openai/"):
        model_name = model_name[7:]  # Remove "openai/" prefix

    # Build model info with extras
    model_info = f"{model_name}"
    extras = []

    if edit_format:
        extras.append(edit_format)
    if thinking_tokens:
        extras.append(f"{thinking_tokens} think")
    if reasoning_effort:
        extras.append(f"reasoning {reasoning_effort}")
    if cache_enabled:
        extras.append("cache")
    if infinite_output:
        extras.append("∞ output")

    if extras:
        model_info += f" ({', '.join(extras)})"

    # Build directory info
    from pathlib import Path
    home = str(Path.home())
    if directory.startswith(home):
        directory = '~' + directory[len(home):]

    # Line 1: Model
    line1 = f"🤖 Model: {model_info}"

    # Line 2: Directory
    line2 = f"📁 Directory: {directory}"

    # Line 3: Branch, files, repo-map
    line3_parts = []
    if branch:
        line3_parts.append(f"🌿 {branch}")
    if file_count > 0:
        line3_parts.append(f"📊 {file_count:,} files")
    if repo_map_tokens and repo_map_tokens > 0:
        line3_parts.append(f"🗺️  {repo_map_tokens} tokens ({repo_map_refresh})")

    line3 = " • ".join(line3_parts) if line3_parts else ""

    # Return all lines
    lines = [line1, line2]
    if line3:
        lines.append(line3)

    return "\n".join(lines)
