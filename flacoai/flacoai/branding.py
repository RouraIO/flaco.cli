"""FlacoAI branding and startup UI elements."""

import random
from datetime import datetime


FLACO_ASCII_ART = r"""
╔═══════════════════════════════════════════════════════════════════════════╗
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
╚═══════════════════════════════════════════════════════════════════════════╝
"""

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


def format_compact_header(version, model_name, edit_format, directory, branch=None, file_count=0,
                         thinking_tokens=None, reasoning_effort=None, cache_enabled=False,
                         infinite_output=False):
    """Format a compact, Claude Code-inspired header (2 lines).

    Args:
        version: Flaco AI version
        model_name: LLM model name
        edit_format: Edit format being used
        directory: Working directory path
        branch: Git branch name (optional)
        file_count: Number of files in repo
        thinking_tokens: Thinking token budget (optional)
        reasoning_effort: Reasoning effort setting (optional)
        cache_enabled: Whether prompt caching is enabled
        infinite_output: Whether infinite output is supported

    Returns:
        Compact formatted header string (2 lines)
    """
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

    # Line 1: version | model | directory
    line1_parts = [
        f"v{version}",
        model_info,
        directory,
    ]
    line1 = " | ".join(line1_parts)

    # Line 2: branch | files
    line2_parts = []
    if branch:
        line2_parts.append(f"🌿 {branch}")
    if file_count > 0:
        line2_parts.append(f"{file_count:,} files")

    line2 = " | ".join(line2_parts) if line2_parts else ""

    # Return both lines
    if line2:
        return f"{line1}\n{line2}"
    else:
        return line1
