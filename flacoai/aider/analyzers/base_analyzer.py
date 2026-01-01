"""Base analyzer framework for code review."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import List, Optional, Dict, Any
import re


class Severity(Enum):
    """Severity levels for analysis findings."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class Category(Enum):
    """Categories of analysis findings."""
    SECURITY = "security"
    PERFORMANCE = "performance"
    QUALITY = "quality"
    ARCHITECTURE = "architecture"


@dataclass
class AnalysisResult:
    """Represents a single finding from code analysis."""
    file: str
    line: int
    severity: Severity
    category: Category
    title: str
    description: str
    recommendation: str
    code_snippet: Optional[str] = None
    column: Optional[int] = None
    end_line: Optional[int] = None
    references: List[str] = field(default_factory=list)

    def __post_init__(self):
        """Ensure enums are properly set."""
        if isinstance(self.severity, str):
            self.severity = Severity(self.severity)
        if isinstance(self.category, str):
            self.category = Category(self.category)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "file": self.file,
            "line": self.line,
            "column": self.column,
            "end_line": self.end_line,
            "severity": self.severity.value,
            "category": self.category.value,
            "title": self.title,
            "description": self.description,
            "recommendation": self.recommendation,
            "code_snippet": self.code_snippet,
            "references": self.references,
        }


@dataclass
class AnalysisReport:
    """Aggregates multiple analysis results."""
    results: List[AnalysisResult] = field(default_factory=list)
    files_analyzed: int = 0
    duration_seconds: float = 0.0

    def add_result(self, result: AnalysisResult):
        """Add a finding to the report."""
        self.results.append(result)

    def get_by_severity(self, severity: Severity) -> List[AnalysisResult]:
        """Filter results by severity."""
        return [r for r in self.results if r.severity == severity]

    def get_by_category(self, category: Category) -> List[AnalysisResult]:
        """Filter results by category."""
        return [r for r in self.results if r.category == category]

    def get_by_file(self, file_path: str) -> List[AnalysisResult]:
        """Filter results by file."""
        return [r for r in self.results if r.file == file_path]

    def get_stats(self) -> Dict[str, int]:
        """Get summary statistics."""
        stats = {
            "total": len(self.results),
            "critical": len(self.get_by_severity(Severity.CRITICAL)),
            "high": len(self.get_by_severity(Severity.HIGH)),
            "medium": len(self.get_by_severity(Severity.MEDIUM)),
            "low": len(self.get_by_severity(Severity.LOW)),
        }
        return stats

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "results": [r.to_dict() for r in self.results],
            "files_analyzed": self.files_analyzed,
            "duration_seconds": self.duration_seconds,
            "stats": self.get_stats(),
        }


class BaseAnalyzer(ABC):
    """Abstract base class for all code analyzers."""

    def __init__(self, io=None, verbose=False):
        """Initialize the analyzer.

        Args:
            io: IO object for output (optional)
            verbose: Enable verbose logging
        """
        self.io = io
        self.verbose = verbose
        self.results: List[AnalysisResult] = []

    @abstractmethod
    def analyze_file(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Analyze a single file and return findings.

        Args:
            file_path: Path to the file being analyzed
            content: File contents as string

        Returns:
            List of AnalysisResult objects
        """
        pass

    def analyze_files(self, files: Dict[str, str]) -> AnalysisReport:
        """Analyze multiple files.

        Args:
            files: Dictionary mapping file paths to their contents

        Returns:
            AnalysisReport with all findings
        """
        import time
        start_time = time.time()

        report = AnalysisReport()
        report.files_analyzed = len(files)

        for file_path, content in files.items():
            if self.verbose and self.io:
                self.io.tool_output(f"Analyzing {file_path}...")

            try:
                results = self.analyze_file(file_path, content)
                for result in results:
                    report.add_result(result)
            except Exception as e:
                if self.io:
                    self.io.tool_error(f"Error analyzing {file_path}: {e}")

        report.duration_seconds = time.time() - start_time
        return report

    def get_lines_context(self, content: str, line_num: int, context_lines: int = 2) -> str:
        """Get lines of code around a specific line number.

        Args:
            content: File content
            line_num: Line number (1-indexed)
            context_lines: Number of lines before/after to include

        Returns:
            Code snippet as string
        """
        lines = content.split('\n')
        start = max(0, line_num - context_lines - 1)
        end = min(len(lines), line_num + context_lines)
        return '\n'.join(lines[start:end])

    def find_pattern(self, content: str, pattern: str, flags=0) -> List[tuple]:
        """Find all matches of a regex pattern in content.

        Args:
            content: File content
            pattern: Regex pattern
            flags: Regex flags

        Returns:
            List of (line_number, column, matched_text) tuples
        """
        results = []
        lines = content.split('\n')

        for line_num, line in enumerate(lines, 1):
            for match in re.finditer(pattern, line, flags):
                results.append((line_num, match.start(), match.group()))

        return results

    def is_supported_file(self, file_path: str) -> bool:
        """Check if this analyzer supports the given file type.

        Args:
            file_path: Path to the file

        Returns:
            True if supported, False otherwise
        """
        # Default: support all files
        # Subclasses can override to filter by extension
        return True

    def get_file_extension(self, file_path: str) -> str:
        """Get file extension without the dot.

        Args:
            file_path: Path to the file

        Returns:
            Extension string (e.g., 'py', 'js')
        """
        return Path(file_path).suffix.lstrip('.')
