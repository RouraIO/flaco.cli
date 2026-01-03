"""GitHub issues exporter for code review findings."""

import subprocess
import json
from typing import List


class GitHubExporter:
    """Export code review findings to GitHub Issues."""

    def __init__(self, io=None):
        """Initialize GitHub exporter.

        Args:
            io: IO object for output
        """
        self.io = io

    def check_gh_cli(self) -> bool:
        """Check if GitHub CLI is installed.

        Returns:
            True if gh CLI is available
        """
        try:
            result = subprocess.run(
                ["gh", "--version"],
                capture_output=True,
                text=True,
                check=False
            )
            return result.returncode == 0
        except FileNotFoundError:
            return False

    def ensure_labels_exist(self):
        """Create common Flaco AI labels if they don't exist.

        Creates labels for:
        - Severity levels (severity:critical, severity:high, etc.)
        - Categories (security, performance, quality, etc.)
        """
        labels_to_create = [
            # Severity labels
            ("severity:critical", "d73a4a", "Critical severity issues"),
            ("severity:high", "e99695", "High severity issues"),
            ("severity:medium", "fbca04", "Medium severity issues"),
            ("severity:low", "0e8a16", "Low severity issues"),
            # Category labels
            ("security", "b60205", "Security vulnerabilities"),
            ("performance", "d93f0b", "Performance issues"),
            ("code-quality", "fbca04", "Code quality improvements"),
            ("architecture", "0052cc", "Architecture and design"),
            ("ios", "1d76db", "iOS-specific issues"),
            ("swiftui", "5319e7", "SwiftUI-specific issues"),
            ("documentation", "d4c5f9", "Documentation improvements"),
            ("code-review", "ededed", "Automated code review findings"),
        ]

        for label_name, color, description in labels_to_create:
            try:
                # Try to create label (will fail silently if exists)
                subprocess.run(
                    [
                        "gh", "label", "create", label_name,
                        "--color", color,
                        "--description", description,
                        "--force"  # Update if exists
                    ],
                    capture_output=True,
                    check=False
                )
            except Exception:
                pass  # Silently continue if label creation fails

    def export_findings(self, results: List, severity_threshold: str = "high") -> List[str]:
        """Export findings as GitHub issues.

        Args:
            results: List of AnalysisResult objects
            severity_threshold: Minimum severity to export (low, medium, high, critical)

        Returns:
            List of created issue URLs
        """
        if not self.check_gh_cli():
            if self.io:
                self.io.tool_error("GitHub CLI (gh) not found. Install from: https://cli.github.com/")
            return []

        # Ensure labels exist before creating issues
        self.ensure_labels_exist()

        from flacoai.analyzers import Severity

        # Map severity threshold
        severity_map = {
            "low": [Severity.LOW, Severity.MEDIUM, Severity.HIGH, Severity.CRITICAL],
            "medium": [Severity.MEDIUM, Severity.HIGH, Severity.CRITICAL],
            "high": [Severity.HIGH, Severity.CRITICAL],
            "critical": [Severity.CRITICAL],
        }

        allowed_severities = severity_map.get(severity_threshold.lower(), severity_map["high"])

        # Filter results by severity
        findings_to_export = [
            r for r in results
            if r.severity in allowed_severities
        ]

        if not findings_to_export:
            if self.io:
                self.io.tool_output("No findings match the severity threshold")
            return []

        # Create issues
        created_issues = []
        for finding in findings_to_export:
            try:
                # Map category to label
                label = self._get_label(finding.category.value)

                title = f"{finding.title} in {finding.file}:{finding.line}"
                body = self._format_issue_body(finding)

                # Create issue using gh CLI
                result = subprocess.run(
                    [
                        "gh", "issue", "create",
                        "--title", title[:256],  # GitHub title limit
                        "--body", body,
                        "--label", label,
                        "--label", f"severity:{finding.severity.value}"
                    ],
                    capture_output=True,
                    text=True,
                    check=False
                )

                if result.returncode == 0:
                    issue_url = result.stdout.strip()
                    created_issues.append(issue_url)

                    if self.io:
                        short_title = title[:50] + "..." if len(title) > 50 else title
                        self.io.tool_output(f"✓ Created: {short_title}")
                        self.io.tool_output(f"  {issue_url}")
                else:
                    if self.io:
                        self.io.tool_error(f"Failed to create issue: {result.stderr}")

            except Exception as e:
                if self.io:
                    self.io.tool_error(f"Failed to create issue: {e}")

        return created_issues

    def _get_label(self, category: str) -> str:
        """Map category to GitHub label.

        Args:
            category: Category name

        Returns:
            GitHub label name
        """
        label_map = {
            "security": "security",
            "performance": "performance",
            "quality": "code-quality",
            "architecture": "architecture",
            "ios": "ios",
            "swiftui": "swiftui",
            "documentation": "documentation",
        }

        return label_map.get(category.lower(), "code-review")

    def _format_issue_body(self, finding) -> str:
        """Format finding as GitHub issue body.

        Args:
            finding: AnalysisResult object

        Returns:
            Formatted markdown body
        """
        severity_emoji = {
            "critical": "🔴",
            "high": "🟠",
            "medium": "🟡",
            "low": "🟢",
        }

        emoji = severity_emoji.get(finding.severity.value, "⚪")

        body = f"""## {emoji} {finding.severity.value.upper()} - {finding.category.value.title()}

**File**: `{finding.file}:{finding.line}`

### Description
{finding.description}

### Recommendation
{finding.recommendation}
"""

        if finding.code_snippet:
            body += f"""
### Code Snippet
```swift
{finding.code_snippet}
```
"""

        body += """
---
🤖 Generated by [Flaco AI Code Review](https://github.com/RouraIO/flaco.cli)
"""

        return body
