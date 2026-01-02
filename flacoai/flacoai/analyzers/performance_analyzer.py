"""Performance analyzer for detecting inefficient code patterns."""

import re
from typing import List
from .base_analyzer import BaseAnalyzer, AnalysisResult, Severity, Category


class PerformanceAnalyzer(BaseAnalyzer):
    """Analyzes code for performance issues and anti-patterns."""

    def __init__(self, io=None, verbose=False):
        super().__init__(io, verbose)

        # N+1 query patterns (ORM)
        self.n_plus_one_patterns = [
            (r'for\s+\w+\s+in\s+\w+.*:\s*\n\s+.*\.get\(', "Potential N+1 query in loop"),
            (r'for\s+\w+\s+in\s+\w+.*:\s*\n\s+.*\.filter\(', "Database query in loop"),
            (r'for\s+\w+\s+in\s+\w+.*:\s*\n\s+.*\.query\(', "Query in loop"),
            (r'\.all\(\).*for.*\sin\s', "Fetching all records then looping"),
        ]

        # Inefficient algorithm patterns
        self.algorithm_patterns = [
            (r'for\s+\w+\s+in\s+.*:\s*\n\s+for\s+\w+\s+in\s+.*:\s*\n\s+for\s+\w+\s+in', "Triple nested loop (O(n³))"),
            (r'while.*:\s*\n\s+.*\.remove\(', "remove() in loop (inefficient)"),
            (r'for.*in.*:\s*\n\s+.*\.append\(.*\)\s*\n\s+.*\.sort\(', "Sorting in loop"),
            (r'\.index\(.*\).*in.*for', "Linear search in loop"),
        ]

        # Memory leak patterns
        self.memory_patterns = [
            (r'global\s+\w+\s*=\s*\[', "Global list (potential memory leak)"),
            (r'cache\s*=\s*\{[^}]*\}(?!.*clear)', "Unbounded cache"),
            (r'while\s+True:(?!.*break)(?!.*return)', "Infinite loop without break"),
        ]

        # Inefficient data structure usage
        self.data_structure_patterns = [
            (r'if\s+\w+\s+in\s+\[', "Membership test on list (use set)"),
            (r'list\(set\(', "Converting set to list (unnecessary)"),
            (r'\[\]\s*\+\s*\[', "List concatenation with +"),
        ]

        # I/O inefficiency patterns
        self.io_patterns = [
            (r'for\s+line\s+in\s+open\([^)]+\)(?!.*with)', "File not closed properly"),
            (r'\.read\(\)\.split\(', "Reading entire file into memory"),
            (r'for.*in.*:\s*\n\s+.*\.write\(', "Writing in loop without buffering"),
        ]

        # String inefficiency patterns
        self.string_patterns = [
            (r'\+=.*[\'""].*for\s+', "String concatenation in loop (use join)"),
            (r'"\s*\+\s*\w+\s*\+\s*"', "Multiple string concatenations"),
        ]

    def analyze_file(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Analyze a file for performance issues."""
        results = []

        if not self._is_code_file(file_path):
            return results

        results.extend(self._check_patterns(file_path, content, self.n_plus_one_patterns,
                                           "N+1 Query Problem", Severity.HIGH,
                                           "Use select_related() or prefetch_related() for ORMs, or fetch data in batch"))

        results.extend(self._check_patterns(file_path, content, self.algorithm_patterns,
                                           "Inefficient Algorithm", Severity.MEDIUM,
                                           "Consider using more efficient algorithms or data structures"))

        results.extend(self._check_patterns(file_path, content, self.memory_patterns,
                                           "Potential Memory Leak", Severity.HIGH,
                                           "Implement proper cleanup, use weak references, or bound caches"))

        results.extend(self._check_patterns(file_path, content, self.data_structure_patterns,
                                           "Inefficient Data Structure", Severity.LOW,
                                           "Use appropriate data structures (set for membership, dict for lookups)"))

        results.extend(self._check_patterns(file_path, content, self.io_patterns,
                                           "I/O Inefficiency", Severity.MEDIUM,
                                           "Use context managers, buffering, and avoid reading entire files"))

        results.extend(self._check_patterns(file_path, content, self.string_patterns,
                                           "String Inefficiency", Severity.LOW,
                                           "Use str.join() for concatenating multiple strings"))

        return results

    def _check_patterns(self, file_path: str, content: str, patterns: List[tuple],
                       title: str, severity: Severity, recommendation: str) -> List[AnalysisResult]:
        """Check content against performance patterns."""
        results = []

        for pattern, description in patterns:
            matches = self.find_pattern(content, pattern, re.MULTILINE)

            for line_num, column, matched_text in matches:
                code_snippet = self.get_lines_context(content, line_num, context_lines=3)

                result = AnalysisResult(
                    file=file_path,
                    line=line_num,
                    column=column,
                    severity=severity,
                    category=Category.PERFORMANCE,
                    title=title,
                    description=description,
                    recommendation=recommendation,
                    code_snippet=code_snippet,
                )
                results.append(result)

        return results

    def _is_code_file(self, file_path: str) -> bool:
        """Check if file is a code file."""
        ext = self.get_file_extension(file_path)
        code_extensions = {'py', 'js', 'ts', 'java', 'rb', 'go', 'php', 'cs', 'cpp', 'c', 'rs'}
        return ext.lower() in code_extensions
