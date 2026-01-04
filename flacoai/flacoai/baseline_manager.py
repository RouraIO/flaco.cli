"""Baseline manager for tracking code review progress over time."""

import json
import os
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime


class BaselineManager:
    """Manages baseline snapshots of code review results."""

    def __init__(self, project_root: str):
        """Initialize baseline manager.

        Args:
            project_root: Root directory of the project
        """
        self.project_root = Path(project_root)
        self.baseline_dir = self.project_root / ".flaco" / "baselines"
        self.baseline_dir.mkdir(parents=True, exist_ok=True)
        self.baseline_file = self.baseline_dir / "current.json"

    def save_baseline(self, report) -> None:
        """Save current review results as baseline.

        Args:
            report: AnalysisReport object to save
        """
        baseline_data = {
            "timestamp": datetime.now().isoformat(),
            "files_analyzed": report.files_analyzed,
            "results": [
                {
                    "file": r.file,
                    "line": r.line,
                    "severity": r.severity.value,
                    "category": r.category.value,
                    "title": r.title,
                    "description": r.description,
                    "recommendation": r.recommendation,
                    "code_snippet": r.code_snippet,
                }
                for r in report.results
            ],
        }

        with open(self.baseline_file, "w") as f:
            json.dump(baseline_data, f, indent=2)

    def load_baseline(self) -> Optional[Dict]:
        """Load saved baseline.

        Returns:
            Baseline data dict or None if no baseline exists
        """
        if not self.baseline_file.exists():
            return None

        with open(self.baseline_file, "r") as f:
            return json.load(f)

    def compare_with_baseline(self, current_report) -> Dict:
        """Compare current results with baseline.

        Args:
            current_report: Current AnalysisReport object

        Returns:
            Dict with new, fixed, and unchanged issues
        """
        baseline = self.load_baseline()

        if not baseline:
            return {
                "new_issues": current_report.results,
                "fixed_issues": [],
                "unchanged_issues": [],
                "baseline_exists": False,
            }

        # Create fingerprints for comparison
        def fingerprint(result):
            """Create unique fingerprint for a result."""
            if isinstance(result, dict):
                return f"{result['file']}:{result['line']}:{result['title']}"
            else:
                return f"{result.file}:{result.line}:{result.title}"

        baseline_fingerprints = {
            fingerprint(r): r for r in baseline["results"]
        }
        current_fingerprints = {
            fingerprint(r): r for r in current_report.results
        }

        # Find new, fixed, and unchanged issues
        new_issues = [
            r for r in current_report.results
            if fingerprint(r) not in baseline_fingerprints
        ]

        fixed_issues = [
            baseline_fingerprints[fp]
            for fp in baseline_fingerprints
            if fp not in current_fingerprints
        ]

        unchanged_issues = [
            r for r in current_report.results
            if fingerprint(r) in baseline_fingerprints
        ]

        return {
            "new_issues": new_issues,
            "fixed_issues": fixed_issues,
            "unchanged_issues": unchanged_issues,
            "baseline_exists": True,
            "baseline_timestamp": baseline.get("timestamp"),
        }

    def get_stats(self, comparison: Dict) -> Dict:
        """Get statistics from baseline comparison.

        Args:
            comparison: Result from compare_with_baseline()

        Returns:
            Stats dict with counts by severity
        """
        from flacoai.analyzers import Severity

        stats = {
            "new_critical": 0,
            "new_high": 0,
            "new_medium": 0,
            "new_low": 0,
            "fixed_critical": 0,
            "fixed_high": 0,
            "fixed_medium": 0,
            "fixed_low": 0,
        }

        # Count new issues
        for issue in comparison["new_issues"]:
            severity = issue.severity if hasattr(issue, "severity") else Severity.LOW
            if severity == Severity.CRITICAL:
                stats["new_critical"] += 1
            elif severity == Severity.HIGH:
                stats["new_high"] += 1
            elif severity == Severity.MEDIUM:
                stats["new_medium"] += 1
            else:
                stats["new_low"] += 1

        # Count fixed issues
        for issue in comparison["fixed_issues"]:
            severity_str = issue.get("severity", "low")
            if severity_str == "critical":
                stats["fixed_critical"] += 1
            elif severity_str == "high":
                stats["fixed_high"] += 1
            elif severity_str == "medium":
                stats["fixed_medium"] += 1
            else:
                stats["fixed_low"] += 1

        return stats
