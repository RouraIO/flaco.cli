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

        # iOS/Swift-specific performance patterns
        self.ios_main_thread_patterns = [
            (r'DispatchQueue\.main\.(sync|async)\s*\{[^}]*(URLSession|fetch|request|download)', "Network request on main thread"),
            (r'DispatchQueue\.main.*\{[^}]*(try\s+Data\(contentsOf:|FileManager|\.write\()', "File I/O on main thread"),
            (r'func.*\{[^}]*(URLSession|fetch).*\}(?!.*DispatchQueue)', "Synchronous network call without dispatch"),
        ]

        self.ios_tableview_patterns = [
            (r'cellForRowAt.*\{[^}]*UITableViewCell\(\)', "Creating new cell instead of dequeuing"),
            (r'cellForRowAt.*\{[^}]*(URLSession|\.load|fetch)', "Heavy operation in cellForRowAt"),
            (r'numberOfRowsInSection.*\{[^}]*(\.count\s*>|filter|map)', "Heavy computation in numberOfRowsInSection"),
        ]

        self.ios_memory_patterns = [
            (r'\[weak\s+self\](?!.*guard)', "weak self without guard (potential retain cycle)"),
            (r'@escaping.*\{[^}]*self\.(?!weak)', "Escaping closure capturing self strongly"),
            (r'lazy\s+var.*\{[^}]*self\.', "Lazy var capturing self (potential retain cycle)"),
            (r'NotificationCenter.*addObserver.*\{[^}]*self\.', "Notification observer without weak self"),
        ]

        self.ios_core_data_patterns = [
            (r'NSFetchRequest.*\{[^}]*fetchLimit\s*=\s*0', "Core Data fetch without limit"),
            (r'NSFetchRequest.*without.*predicate', "Core Data fetch without predicate (fetching all)"),
            (r'for.*in.*NSFetchRequest', "Fetching Core Data in loop (N+1 problem)"),
        ]

        self.ios_image_patterns = [
            (r'UIImage\(named:.*\)(?!.*cache)', "UIImage without caching consideration"),
            (r'UIImage\(contentsOfFile:.*large', "Loading large image synchronously"),
            (r'imageView\.image\s*=\s*UIImage\(data:.*\)(?!.*DispatchQueue)', "Image decoding on main thread"),
        ]

        self.ios_animation_patterns = [
            (r'UIView\.animate.*duration:\s*[0-9]+\.[0-9]{3,}', "Very long animation duration"),
            (r'\.layer\.add\(.*animation.*\).*in.*for', "Adding animations in loop"),
        ]

        self.ios_view_patterns = [
            (r'layoutSubviews.*\{[^}]*(for|while)', "Heavy computation in layoutSubviews"),
            (r'draw\(_:\s*CGRect\).*\{[^}]*(for|while)', "Heavy computation in draw()"),
            (r'viewWillAppear.*\{[^}]*(fetch|request|load.*large)', "Heavy operation in viewWillAppear"),
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

        # iOS-specific checks
        ext = self.get_file_extension(file_path)
        if ext in ('swift', 'm', 'mm'):
            results.extend(self._check_patterns(file_path, content, self.ios_main_thread_patterns,
                                               "Main Thread Blocking", Severity.HIGH,
                                               "Move heavy operations to background queue using DispatchQueue.global()"))

            results.extend(self._check_patterns(file_path, content, self.ios_tableview_patterns,
                                               "Inefficient UITableView/UICollectionView", Severity.MEDIUM,
                                               "Use dequeueReusableCell and move heavy operations out of cellForRowAt"))

            results.extend(self._check_patterns(file_path, content, self.ios_memory_patterns,
                                               "Potential Retain Cycle", Severity.HIGH,
                                               "Use [weak self] in escaping closures and guard let self = self"))

            results.extend(self._check_patterns(file_path, content, self.ios_core_data_patterns,
                                               "Inefficient Core Data Usage", Severity.MEDIUM,
                                               "Use fetch limits, predicates, and batch operations"))

            results.extend(self._check_patterns(file_path, content, self.ios_image_patterns,
                                               "Inefficient Image Loading", Severity.MEDIUM,
                                               "Use image caching and decode images on background thread"))

            results.extend(self._check_patterns(file_path, content, self.ios_animation_patterns,
                                               "Inefficient Animation", Severity.LOW,
                                               "Keep animations short and avoid animating in loops"))

            results.extend(self._check_patterns(file_path, content, self.ios_view_patterns,
                                               "Heavy View Operation", Severity.MEDIUM,
                                               "Avoid heavy operations in layoutSubviews, draw(), and view lifecycle methods"))

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
