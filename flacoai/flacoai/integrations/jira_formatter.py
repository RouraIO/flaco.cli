"""Jira issue formatter for terminal display."""

from typing import List, Optional
from rich.table import Table
from rich.panel import Panel
from rich.text import Text


class JiraFormatter:
    """Format Jira issues for rich console output."""

    def __init__(self, io=None):
        """Initialize formatter.

        Args:
            io: IO object with rich console (optional)
        """
        self.io = io

    def format_issue(self, issue, detailed: bool = False) -> str:
        """Format a single issue as text.

        Args:
            issue: Jira issue object
            detailed: Include full details

        Returns:
            Formatted string
        """
        lines = []

        # Header
        lines.append(f"[bold cyan]{issue.key}[/bold cyan]: {issue.fields.summary}")

        # Status and type
        status = issue.fields.status.name
        issue_type = issue.fields.issuetype.name
        lines.append(f"Status: [yellow]{status}[/yellow] | Type: {issue_type}")

        if detailed:
            # Priority
            if hasattr(issue.fields, 'priority') and issue.fields.priority:
                lines.append(f"Priority: {issue.fields.priority.name}")

            # Assignee
            if hasattr(issue.fields, 'assignee') and issue.fields.assignee:
                lines.append(f"Assignee: {issue.fields.assignee.displayName}")

            # Reporter
            if hasattr(issue.fields, 'reporter') and issue.fields.reporter:
                lines.append(f"Reporter: {issue.fields.reporter.displayName}")

            # Description
            if hasattr(issue.fields, 'description') and issue.fields.description:
                lines.append("")
                lines.append("[bold]Description:[/bold]")
                # Truncate long descriptions
                desc = str(issue.fields.description)
                if len(desc) > 500:
                    desc = desc[:500] + "..."
                lines.append(desc)

            # Labels
            if hasattr(issue.fields, 'labels') and issue.fields.labels:
                lines.append("")
                lines.append(f"Labels: {', '.join(issue.fields.labels)}")

            # Created/Updated
            if hasattr(issue.fields, 'created'):
                lines.append(f"Created: {issue.fields.created}")
            if hasattr(issue.fields, 'updated'):
                lines.append(f"Updated: {issue.fields.updated}")

        return "\n".join(lines)

    def display_issue(self, issue, detailed: bool = True):
        """Display a single issue in the console.

        Args:
            issue: Jira issue object
            detailed: Show full details
        """
        if not self.io or not self.io.console:
            # Fallback to plain text
            text = self.format_issue(issue, detailed)
            if self.io:
                self.io.tool_output(text)
            return

        # Rich panel display
        content = self.format_issue(issue, detailed)

        panel = Panel(
            content,
            title=f"[bold cyan]{issue.key}[/bold cyan]",
            border_style="cyan",
            padding=(1, 2),
        )

        self.io.console.print(panel)

    def display_issues_table(self, issues: List, title: Optional[str] = None):
        """Display multiple issues as a table.

        Args:
            issues: List of Jira issue objects
            title: Table title (optional)
        """
        if not issues:
            if self.io:
                self.io.tool_output("No issues found")
            return

        if not self.io or not self.io.console:
            # Fallback to plain text
            for issue in issues:
                text = self.format_issue(issue, detailed=False)
                if self.io:
                    self.io.tool_output(text)
                    self.io.tool_output("")
            return

        # Create rich table
        table = Table(title=title or f"Jira Issues ({len(issues)})", border_style="cyan")

        table.add_column("Key", style="cyan", no_wrap=True)
        table.add_column("Summary", style="white")
        table.add_column("Status", style="yellow")
        table.add_column("Type", style="green")
        table.add_column("Assignee", style="blue")

        for issue in issues:
            key = issue.key
            summary = issue.fields.summary

            # Truncate long summaries
            if len(summary) > 50:
                summary = summary[:47] + "..."

            status = issue.fields.status.name
            issue_type = issue.fields.issuetype.name

            # Get assignee
            assignee = "Unassigned"
            if hasattr(issue.fields, 'assignee') and issue.fields.assignee:
                assignee = issue.fields.assignee.displayName
                # Truncate long names
                if len(assignee) > 20:
                    assignee = assignee[:17] + "..."

            table.add_row(key, summary, status, issue_type, assignee)

        self.io.console.print(table)

    def display_transition_options(self, transitions: List):
        """Display available transitions.

        Args:
            transitions: List of transition objects
        """
        if not transitions:
            if self.io:
                self.io.tool_output("No transitions available")
            return

        if not self.io or not self.io.console:
            # Plain text
            if self.io:
                self.io.tool_output("Available transitions:")
                for t in transitions:
                    self.io.tool_output(f"  - {t['name']} (ID: {t['id']})")
            return

        # Rich table
        table = Table(title="Available Transitions", border_style="cyan")
        table.add_column("ID", style="cyan")
        table.add_column("Name", style="yellow")
        table.add_column("To Status", style="green")

        for t in transitions:
            transition_id = str(t['id'])
            name = t['name']
            to_status = t.get('to', {}).get('name', 'N/A')

            table.add_row(transition_id, name, to_status)

        self.io.console.print(table)

    def format_search_results_summary(self, issues: List, jql: str) -> str:
        """Format a summary of search results.

        Args:
            issues: List of issue objects
            jql: JQL query that was used

        Returns:
            Summary string
        """
        if not issues:
            return f"No issues found for query: {jql}"

        # Count by status
        status_counts = {}
        for issue in issues:
            status = issue.fields.status.name
            status_counts[status] = status_counts.get(status, 0) + 1

        summary = f"Found {len(issues)} issue(s) for query: {jql}\n"
        summary += "Status breakdown:\n"
        for status, count in sorted(status_counts.items()):
            summary += f"  {status}: {count}\n"

        return summary.strip()

    def display_created_issue(self, issue):
        """Display a newly created issue.

        Args:
            issue: Jira issue object
        """
        if not self.io:
            return

        # Get issue URL
        issue_url = f"{issue.self.rsplit('/rest/', 1)[0]}/browse/{issue.key}"

        message = f"✅ Created issue: [bold cyan]{issue.key}[/bold cyan]\n"
        message += f"Summary: {issue.fields.summary}\n"
        message += f"URL: {issue_url}"

        if self.io.console:
            self.io.console.print(Panel(message, border_style="green", padding=(1, 2)))
        else:
            self.io.tool_output(f"Created issue: {issue.key}")
            self.io.tool_output(f"Summary: {issue.fields.summary}")
            self.io.tool_output(f"URL: {issue_url}")
