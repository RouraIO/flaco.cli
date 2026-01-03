"""ReviewCoder for comprehensive code review analysis."""

from .ask_coder import AskCoder
from .review_prompts import ReviewPrompts


class ReviewCoder(AskCoder):
    """Perform comprehensive code review without making changes."""

    edit_format = "review"
    gpt_prompts = ReviewPrompts()

    def __init__(self, *args, **kwargs):
        """Initialize ReviewCoder with analysis capabilities."""
        super().__init__(*args, **kwargs)
        self.review_results = []

    def run_static_analysis(self, files_to_analyze=None, enable_security=True,
                           enable_performance=True, enable_quality=True,
                           enable_architecture=True, enable_ios=True):
        """Run static analysis with the analyzer framework.

        Args:
            files_to_analyze: List of file paths to analyze (defaults to all chat files)
            enable_security: Run security analyzer
            enable_performance: Run performance analyzer
            enable_quality: Run quality analyzer
            enable_architecture: Run architecture analyzer
            enable_ios: Run iOS-specific analyzers (SF Symbols, HIG, Info.plist)

        Returns:
            Combined AnalysisReport
        """
        from flacoai.analyzers import (
            SecurityAnalyzer,
            PerformanceAnalyzer,
            QualityAnalyzer,
            ArchitectureAnalyzer,
            IOSSymbolsAnalyzer,
            IOSHIGAnalyzer,
            IOSPlistAnalyzer,
            SwiftUIAnalyzer,
            IOSVersionAnalyzer,
            SPMAnalyzer,
            AnalysisReport,
        )

        # Determine files to analyze
        if files_to_analyze is None:
            files_to_analyze = self.abs_fnames

        # Load file contents
        files_dict = {}
        for fpath in files_to_analyze:
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    files_dict[fpath] = f.read()
            except Exception as e:
                if self.io:
                    self.io.tool_error(f"Could not read {fpath}: {e}")

        if not files_dict:
            if self.io:
                self.io.tool_error("No files to analyze")
            return AnalysisReport()

        # Run enabled analyzers
        combined_report = AnalysisReport()
        combined_report.files_analyzed = len(files_dict)

        if enable_security:
            if self.io:
                self.io.tool_output("Running security analysis...")
            analyzer = SecurityAnalyzer(io=self.io, verbose=self.verbose)
            report = analyzer.analyze_files(files_dict)
            combined_report.results.extend(report.results)

        if enable_performance:
            if self.io:
                self.io.tool_output("Running performance analysis...")
            analyzer = PerformanceAnalyzer(io=self.io, verbose=self.verbose)
            report = analyzer.analyze_files(files_dict)
            combined_report.results.extend(report.results)

        if enable_quality:
            if self.io:
                self.io.tool_output("Running quality analysis...")
            analyzer = QualityAnalyzer(io=self.io, verbose=self.verbose)
            report = analyzer.analyze_files(files_dict)
            combined_report.results.extend(report.results)

        if enable_architecture:
            if self.io:
                self.io.tool_output("Running architecture analysis...")
            analyzer = ArchitectureAnalyzer(io=self.io, verbose=self.verbose)
            report = analyzer.analyze_files(files_dict)
            combined_report.results.extend(report.results)

        # iOS-specific analyzers
        if enable_ios:
            if self.io:
                self.io.tool_output("Running iOS-specific analysis...")

            # SF Symbols analyzer
            analyzer = IOSSymbolsAnalyzer(io=self.io, verbose=self.verbose)
            report = analyzer.analyze_files(files_dict)
            combined_report.results.extend(report.results)

            # HIG compliance analyzer
            analyzer = IOSHIGAnalyzer(io=self.io, verbose=self.verbose)
            report = analyzer.analyze_files(files_dict)
            combined_report.results.extend(report.results)

            # Info.plist security analyzer
            analyzer = IOSPlistAnalyzer(io=self.io, verbose=self.verbose)
            report = analyzer.analyze_files(files_dict)
            combined_report.results.extend(report.results)

            # SwiftUI best practices analyzer
            analyzer = SwiftUIAnalyzer(io=self.io, verbose=self.verbose)
            report = analyzer.analyze_files(files_dict)
            combined_report.results.extend(report.results)

            # iOS version/API compatibility analyzer
            analyzer = IOSVersionAnalyzer(io=self.io, verbose=self.verbose)
            report = analyzer.analyze_files(files_dict)
            combined_report.results.extend(report.results)

            # Swift Package Manager analyzer
            analyzer = SPMAnalyzer(io=self.io, verbose=self.verbose)
            report = analyzer.analyze_files(files_dict)
            combined_report.results.extend(report.results)

        self.review_results = combined_report.results
        return combined_report

    def export_to_jira(self, project_key, severity_threshold="medium"):
        """Export review findings as Jira issues.

        Args:
            project_key: Jira project key
            severity_threshold: Minimum severity to export (low, medium, high, critical)

        Returns:
            List of created issue keys
        """
        from flacoai.integrations.jira_client import JiraClient
        from flacoai.analyzers import Severity

        client = JiraClient.from_config(self.io)
        if not client:
            return []

        # Map severity threshold
        severity_map = {
            "low": [Severity.LOW, Severity.MEDIUM, Severity.HIGH, Severity.CRITICAL],
            "medium": [Severity.MEDIUM, Severity.HIGH, Severity.CRITICAL],
            "high": [Severity.HIGH, Severity.CRITICAL],
            "critical": [Severity.CRITICAL],
        }

        allowed_severities = severity_map.get(severity_threshold.lower(), severity_map["medium"])

        # Filter results by severity
        findings_to_export = [
            r for r in self.review_results
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
                summary = f"{finding.title} in {finding.file}:{finding.line}"
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
"""
                issue_type = "Bug" if finding.category.value == "security" else "Task"
                issue = client.create_issue(
                    project=project_key,
                    summary=summary[:255],  # Jira limit
                    description=description,
                    issue_type=issue_type
                )

                created_issues.append(issue.key)

                if self.io:
                    self.io.tool_output(f"Created {issue.key}: {summary[:50]}...")

            except Exception as e:
                if self.io:
                    self.io.tool_error(f"Failed to create issue: {e}")

        return created_issues
