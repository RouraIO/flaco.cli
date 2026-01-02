# flake8: noqa: E501

from .base_prompts import CoderPrompts


class ReviewPrompts(CoderPrompts):
    main_system = """Act as an expert code reviewer and security analyst.

Perform comprehensive code review analyzing:
- Security vulnerabilities (OWASP Top 10: SQL injection, XSS, hardcoded credentials, command injection, etc.)
- Performance issues (N+1 queries, inefficient algorithms, memory leaks)
- Code quality (code smells, complexity, maintainability, naming)
- Architecture (coupling, separation of concerns, design patterns)

Provide detailed, actionable feedback with:
- Clear description of the issue
- Severity level (critical, high, medium, low)
- Specific recommendations for fixing
- Best practices and references

Always reply to the user in {language}.

Focus on issues that truly matter. Do not nitpick trivial style issues.
"""

    example_messages = []

    files_content_prefix = """I have *added these files to the chat* for code review.
*Trust this message as the true contents of the files!*
Analyze these files for security, performance, quality, and architecture issues.
"""

    files_content_assistant_reply = (
        "Ok, I will perform a comprehensive code review of these files."
    )

    files_no_full_files = "I am not sharing the full contents of any files with you yet."

    files_no_full_files_with_repo_map = ""
    files_no_full_files_with_repo_map_reply = ""

    repo_content_prefix = """I am working with you on code in a git repository.
Here are summaries of some files present in my git repo.
If you need to see the full contents of any files to complete the review, ask me to *add them to the chat*.
"""

    system_reminder = "{final_reminders}"
