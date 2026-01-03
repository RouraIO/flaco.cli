"""Custom rules analyzer for team-specific code standards."""

import re
import yaml
from pathlib import Path
from typing import List, Dict, Optional

from .base_analyzer import BaseAnalyzer, AnalysisResult, Severity, Category


class CustomRulesAnalyzer(BaseAnalyzer):
    """Analyzer for custom team-defined rules."""

    def __init__(self, rules_file: Optional[str] = None, **kwargs):
        """Initialize custom rules analyzer.

        Args:
            rules_file: Path to custom rules YAML file
            **kwargs: Additional arguments for BaseAnalyzer
        """
        super().__init__(**kwargs)
        self.rules_file = rules_file
        self.rules = []

        if rules_file and Path(rules_file).exists():
            self._load_rules(rules_file)

    def _load_rules(self, rules_file: str):
        """Load rules from YAML file.

        Args:
            rules_file: Path to YAML file
        """
        try:
            with open(rules_file, 'r') as f:
                data = yaml.safe_load(f)

            if data and 'rules' in data:
                self.rules = data['rules']

                if self.io:
                    self.io.tool_output(f"Loaded {len(self.rules)} custom rules from {rules_file}")

        except Exception as e:
            if self.io:
                self.io.tool_error(f"Failed to load custom rules: {e}")

    def analyze_file(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Analyze file with custom rules.

        Args:
            file_path: Path to file
            content: File content

        Returns:
            List of analysis results
        """
        if not self.rules:
            return []

        results = []

        for rule in self.rules:
            # Check if rule applies to this file
            if not self._rule_applies_to_file(rule, file_path):
                continue

            # Apply rule
            rule_results = self._apply_rule(rule, file_path, content)
            results.extend(rule_results)

        return results

    def _rule_applies_to_file(self, rule: Dict, file_path: str) -> bool:
        """Check if rule applies to this file.

        Args:
            rule: Rule dict
            file_path: Path to file

        Returns:
            True if rule should be applied
        """
        # Check file_pattern filter
        if 'file_pattern' in rule:
            pattern = rule['file_pattern']
            if not re.search(pattern, file_path):
                return False

        # Check file_extension filter
        if 'file_extension' in rule:
            ext = Path(file_path).suffix.lstrip('.')
            allowed_exts = rule['file_extension']

            if isinstance(allowed_exts, str):
                allowed_exts = [allowed_exts]

            if ext not in allowed_exts:
                return False

        return True

    def _apply_rule(self, rule: Dict, file_path: str, content: str) -> List[AnalysisResult]:
        """Apply a single rule to file content.

        Args:
            rule: Rule dict
            file_path: Path to file
            content: File content

        Returns:
            List of analysis results
        """
        results = []

        # Get rule parameters
        pattern = rule.get('pattern', '')
        name = rule.get('name', 'Custom Rule')
        message = rule.get('message', 'Custom rule violation')
        severity = self._parse_severity(rule.get('severity', 'medium'))
        category = self._parse_category(rule.get('category', 'quality'))
        recommendation = rule.get('recommendation', 'Fix this issue')
        mode = rule.get('mode', 'regex')  # regex or contains

        # Apply based on mode
        if mode == 'regex':
            results = self._apply_regex_rule(
                pattern, name, message, severity, category, recommendation,
                file_path, content
            )

        elif mode == 'contains':
            results = self._apply_contains_rule(
                pattern, name, message, severity, category, recommendation,
                file_path, content
            )

        elif mode == 'not_contains':
            results = self._apply_not_contains_rule(
                pattern, name, message, severity, category, recommendation,
                file_path, content
            )

        return results

    def _apply_regex_rule(
        self,
        pattern: str,
        name: str,
        message: str,
        severity: Severity,
        category: Category,
        recommendation: str,
        file_path: str,
        content: str
    ) -> List[AnalysisResult]:
        """Apply regex-based rule.

        Args:
            pattern: Regex pattern
            name: Rule name
            message: Error message
            severity: Severity level
            category: Category
            recommendation: Fix recommendation
            file_path: Path to file
            content: File content

        Returns:
            List of results
        """
        results = []

        try:
            for match in re.finditer(pattern, content, re.MULTILINE):
                line_num = content[:match.start()].count('\n') + 1

                # Extract code snippet
                lines = content.splitlines()
                if 0 < line_num <= len(lines):
                    snippet = lines[line_num - 1]
                else:
                    snippet = match.group(0)

                results.append(AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=severity,
                    category=category,
                    title=name,
                    description=message,
                    recommendation=recommendation,
                    code_snippet=snippet,
                ))

        except re.error as e:
            if self.io:
                self.io.tool_error(f"Invalid regex pattern '{pattern}': {e}")

        return results

    def _apply_contains_rule(
        self,
        pattern: str,
        name: str,
        message: str,
        severity: Severity,
        category: Category,
        recommendation: str,
        file_path: str,
        content: str
    ) -> List[AnalysisResult]:
        """Apply contains-based rule (simple string matching).

        Args:
            pattern: String to search for
            name: Rule name
            message: Error message
            severity: Severity level
            category: Category
            recommendation: Fix recommendation
            file_path: Path to file
            content: File content

        Returns:
            List of results
        """
        results = []

        lines = content.splitlines()

        for line_num, line in enumerate(lines, start=1):
            if pattern in line:
                results.append(AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=severity,
                    category=category,
                    title=name,
                    description=message,
                    recommendation=recommendation,
                    code_snippet=line.strip(),
                ))

        return results

    def _apply_not_contains_rule(
        self,
        pattern: str,
        name: str,
        message: str,
        severity: Severity,
        category: Category,
        recommendation: str,
        file_path: str,
        content: str
    ) -> List[AnalysisResult]:
        """Apply not-contains rule (ensure pattern is present).

        For file-level checks (e.g., "file must contain copyright header").

        Args:
            pattern: String that should be present
            name: Rule name
            message: Error message
            severity: Severity level
            category: Category
            recommendation: Fix recommendation
            file_path: Path to file
            content: File content

        Returns:
            List of results (empty if pattern found, one result if missing)
        """
        results = []

        if pattern not in content:
            results.append(AnalysisResult(
                file=file_path,
                line=1,
                severity=severity,
                category=category,
                title=name,
                description=message,
                recommendation=recommendation,
                code_snippet="(entire file)",
            ))

        return results

    def _parse_severity(self, severity_str: str) -> Severity:
        """Parse severity string to enum.

        Args:
            severity_str: Severity string

        Returns:
            Severity enum value
        """
        severity_map = {
            'critical': Severity.CRITICAL,
            'high': Severity.HIGH,
            'medium': Severity.MEDIUM,
            'low': Severity.LOW,
        }

        return severity_map.get(severity_str.lower(), Severity.MEDIUM)

    def _parse_category(self, category_str: str) -> Category:
        """Parse category string to enum.

        Args:
            category_str: Category string

        Returns:
            Category enum value
        """
        category_map = {
            'security': Category.SECURITY,
            'performance': Category.PERFORMANCE,
            'quality': Category.QUALITY,
            'architecture': Category.ARCHITECTURE,
            'ios': Category.IOS,
        }

        return category_map.get(category_str.lower(), Category.QUALITY)


def create_sample_rules_file(output_path: str):
    """Create a sample custom rules file.

    Args:
        output_path: Where to write the sample file
    """
    sample_rules = {
        "rules": [
            {
                "name": "No force unwrapping in ViewModels",
                "pattern": r"class\s+\w*ViewModel[\s\S]*!",
                "severity": "high",
                "category": "quality",
                "message": "Force unwrapping (!) found in ViewModel - can crash the app",
                "recommendation": "Use optional binding or nil coalescing (??) instead",
                "file_extension": "swift",
                "mode": "regex",
            },
            {
                "name": "TODO comments without ticket reference",
                "pattern": r"//\s*TODO:(?!\s*[A-Z]+-\d+)",
                "severity": "low",
                "category": "quality",
                "message": "TODO comment without ticket reference (e.g., TODO: PROJ-123)",
                "recommendation": "Add ticket reference to TODO comment for tracking",
                "mode": "regex",
            },
            {
                "name": "Copyright header required",
                "pattern": "Copyright",
                "severity": "low",
                "category": "quality",
                "message": "File missing copyright header",
                "recommendation": "Add copyright header at the top of the file",
                "file_extension": ["swift", "m", "h"],
                "mode": "not_contains",
            },
            {
                "name": "Hardcoded API endpoint",
                "pattern": r"https?://(?!.*localhost)[^/]+\.com",
                "severity": "high",
                "category": "architecture",
                "message": "Hardcoded API endpoint found - should use config",
                "recommendation": "Move API endpoint to configuration file or environment variable",
                "mode": "regex",
            },
        ]
    }

    with open(output_path, 'w') as f:
        yaml.dump(sample_rules, f, default_flow_style=False, sort_keys=False)
