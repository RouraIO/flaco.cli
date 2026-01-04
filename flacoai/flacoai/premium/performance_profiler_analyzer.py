"""
PROPRIETARY - Performance Profiler Analyzer

Copyright (c) 2026 Roura.IO
All Rights Reserved.

Requires: Flaco AI Pro or Enterprise license
"""

import re
from typing import List, Dict, Tuple
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from analyzers.base_analyzer import BaseAnalyzer, AnalysisResult, Severity, Category


class PerformanceProfilerAnalyzer(BaseAnalyzer):
    """
    Premium analyzer that predicts performance bottlenecks and UI lag.

    This analyzer uses pattern matching and heuristic analysis to identify:
    - Main thread blocking operations
    - FPS drop triggers (layout complexity, image processing)
    - Memory allocation patterns
    - Inefficient database queries
    - Network request batching issues
    - Auto Layout complexity scoring
    """

    # Performance thresholds
    AUTOLAYOUT_COMPLEXITY_THRESHOLD = 5  # Nested constraints
    ARRAY_OPERATION_SIZE_THRESHOLD = 1000  # Large array operations
    IMAGE_SIZE_THRESHOLD = 2048  # Image dimensions

    def analyze_file(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Analyze file for performance issues.

        Args:
            file_path: Path to file
            content: File content

        Returns:
            List of performance issues with impact scores
        """
        results = []

        # Only analyze Swift files
        if not file_path.endswith('.swift'):
            return results

        results.extend(self._check_main_thread_blocking(file_path, content))
        results.extend(self._check_heavy_view_hierarchy(file_path, content))
        results.extend(self._check_image_processing(file_path, content))
        results.extend(self._check_core_data_inefficiency(file_path, content))
        results.extend(self._check_autolayout_complexity(file_path, content))
        results.extend(self._check_collection_operations(file_path, content))
        results.extend(self._check_network_batching(file_path, content))

        return results

    def _check_main_thread_blocking(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect operations that block the main thread."""
        results = []

        # Patterns that indicate main thread work
        blocking_patterns = [
            (r'DispatchQueue\.main\.sync\s*\{', 'DispatchQueue.main.sync', 'CRITICAL', 90),
            (r'\.wait\(\)', '.wait() call', 'HIGH', 75),
            (r'sleep\(', 'sleep() on main thread', 'HIGH', 80),
            (r'Data\(contentsOf:\s*URL', 'Synchronous network request', 'CRITICAL', 95),
            (r'JSONDecoder\(\)\.decode.*Data\([^)]{100,}\)', 'Large JSON decode on main thread', 'HIGH', 70),
        ]

        for pattern, description, severity_str, lag_likelihood in blocking_patterns:
            for match in re.finditer(pattern, content, re.MULTILINE | re.DOTALL):
                line_num = content[:match.start()].count('\n') + 1

                # Check if we're in a background queue context
                context_start = max(0, match.start() - 200)
                context = content[context_start:match.start()]

                is_background = any([
                    'DispatchQueue.global' in context,
                    'DispatchQueue(label:' in context,
                    '.async' in context and 'DispatchQueue.main' not in context,
                ])

                if not is_background:
                    severity = Severity.CRITICAL if severity_str == 'CRITICAL' else Severity.HIGH

                    results.append(AnalysisResult(
                        file=file_path,
                        line=line_num,
                        severity=severity,
                        category=Category.PERFORMANCE,
                        title=f"Main thread blocking: {description} - {lag_likelihood}% UI lag risk",
                        description=f"This operation blocks the main thread, causing UI freezes and poor UX. "
                                   f"Users will experience {lag_likelihood}% likelihood of noticeable lag (>16ms frame time).",
                        recommendation=f"Move to background queue:\n"
                                      f"DispatchQueue.global(qos: .userInitiated).async {{\n"
                                      f"    // {description}\n"
                                      f"    DispatchQueue.main.async {{\n"
                                      f"        // Update UI here\n"
                                      f"    }}\n"
                                      f"}}",
                        code_snippet=self._get_line(content, line_num),
                    ))

        return results

    def _check_heavy_view_hierarchy(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect complex view hierarchies that cause FPS drops."""
        results = []

        # Look for deeply nested view builders
        pattern = r'(var\s+body:\s+some\s+View\s*\{[^}]*(?:\{[^}]*){5,})'

        for match in re.finditer(pattern, content, re.DOTALL):
            body = match.group(0)
            nesting_depth = body.count('{')
            line_num = content[:match.start()].count('\n') + 1

            if nesting_depth >= 7:
                fps_impact = min(95, 50 + (nesting_depth - 7) * 10)

                results.append(AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=Severity.HIGH if nesting_depth >= 10 else Severity.MEDIUM,
                    category=Category.PERFORMANCE,
                    title=f"Deep view hierarchy ({nesting_depth} levels) - {fps_impact}% FPS drop risk",
                    description=f"SwiftUI view body has {nesting_depth} nesting levels. "
                               f"This causes expensive layout passes and can drop FPS from 60 to <30.",
                    recommendation=f"Extract nested views into separate computed properties or custom views:\n"
                                  f"private var sectionView: some View {{\n"
                                  f"    // Extract nested content here\n"
                                  f"}}\n"
                                  f"Or use @ViewBuilder helpers to break up complexity.",
                    code_snippet=f"View body with {nesting_depth} nesting levels",
                ))

        return results

    def _check_image_processing(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect inefficient image processing."""
        results = []

        # Image processing patterns
        patterns = [
            (r'UIImage\(named:\s*["\'][^"\']+["\']\)\??\.jpegData',
             'JPEG compression on main thread', 70),
            (r'\.resizableImage\(',
             'Image resizing without async', 60),
            (r'CIFilter\(',
             'Core Image filter without async', 75),
            (r'UIGraphicsBeginImageContext',
             'Graphics context on main thread', 80),
        ]

        for pattern, description, perf_impact in patterns:
            for match in re.finditer(pattern, content):
                line_num = content[:match.start()].count('\n') + 1

                # Check for background queue
                context_start = max(0, match.start() - 150)
                context = content[context_start:match.start()]

                if 'DispatchQueue.global' not in context and '.async' not in context:
                    results.append(AnalysisResult(
                        file=file_path,
                        line=line_num,
                        severity=Severity.HIGH,
                        category=Category.PERFORMANCE,
                        title=f"Image processing bottleneck - {perf_impact}% lag risk",
                        description=f"{description}. Heavy image operations cause UI freezes, "
                                   f"especially on older devices or large images.",
                        recommendation=f"Process images asynchronously:\n"
                                      f"DispatchQueue.global(qos: .userInitiated).async {{\n"
                                      f"    let processedImage = // process image\n"
                                      f"    DispatchQueue.main.async {{\n"
                                      f"        imageView.image = processedImage\n"
                                      f"    }}\n"
                                      f"}}",
                        code_snippet=self._get_line(content, line_num),
                    ))

        return results

    def _check_core_data_inefficiency(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect inefficient Core Data queries."""
        results = []

        lines = content.splitlines()

        for line_num, line in enumerate(lines, start=1):
            # Missing fetchBatchSize
            if 'NSFetchRequest' in line or 'fetchRequest()' in line:
                # Check next 10 lines for fetchBatchSize
                context_lines = lines[line_num:min(line_num + 10, len(lines))]
                context = '\n'.join(context_lines)

                if 'fetchBatchSize' not in context and 'fetchLimit' not in context:
                    results.append(AnalysisResult(
                        file=file_path,
                        line=line_num,
                        severity=Severity.MEDIUM,
                        category=Category.PERFORMANCE,
                        title="Core Data fetch without batch size - memory spike risk",
                        description="Fetching without batch size loads all results into memory. "
                                   "For large datasets, this causes memory warnings and slowdowns.",
                        recommendation="Add fetchBatchSize to limit memory usage:\n"
                                      "request.fetchBatchSize = 20\n"
                                      "Or use fetchLimit for finite result sets.",
                        code_snippet=line.strip(),
                    ))

            # N+1 query pattern
            if re.search(r'for\s+\w+\s+in.*\{', line):
                # Look for fetch/query in loop body
                loop_start = line_num
                brace_count = 1
                loop_end = loop_start

                for i in range(loop_start, min(loop_start + 50, len(lines))):
                    brace_count += lines[i].count('{') - lines[i].count('}')
                    if brace_count == 0:
                        loop_end = i
                        break

                loop_body = '\n'.join(lines[loop_start:loop_end])

                if any(keyword in loop_body for keyword in ['fetch(', 'performFetch', 'execute(']):
                    results.append(AnalysisResult(
                        file=file_path,
                        line=line_num,
                        severity=Severity.HIGH,
                        category=Category.PERFORMANCE,
                        title="N+1 query pattern detected - 85% slowdown risk",
                        description="Fetching data inside a loop causes N+1 queries, "
                                   "multiplying database overhead. This is a major performance killer.",
                        recommendation="Batch fetch with relationships:\n"
                                      "request.relationshipKeyPathsForPrefetching = [\"relationship\"]\n"
                                      "Or use a single fetch with predicates instead of loop.",
                        code_snippet=line.strip(),
                    ))

        return results

    def _check_autolayout_complexity(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect Auto Layout complexity that causes layout thrashing."""
        results = []

        # Count constraints in a single function/view
        constraint_pattern = r'\.constraint\(|NSLayoutConstraint\('

        lines = content.splitlines()

        for line_num, line in enumerate(lines, start=1):
            if 'func' in line or 'var' in line:
                # Analyze function/property for constraint complexity
                func_start = line_num
                brace_count = 0
                func_body_start = False
                constraint_count = 0
                func_end = func_start

                for i in range(func_start - 1, min(func_start + 100, len(lines))):
                    current_line = lines[i]

                    if '{' in current_line:
                        func_body_start = True
                        brace_count += current_line.count('{')

                    if func_body_start:
                        brace_count -= current_line.count('}')
                        constraint_count += len(re.findall(constraint_pattern, current_line))

                    if brace_count == 0 and func_body_start:
                        func_end = i + 1
                        break

                if constraint_count >= 8:
                    layout_impact = min(90, 40 + constraint_count * 5)

                    results.append(AnalysisResult(
                        file=file_path,
                        line=line_num,
                        severity=Severity.MEDIUM,
                        category=Category.PERFORMANCE,
                        title=f"Auto Layout complexity ({constraint_count} constraints) - {layout_impact}% layout lag",
                        description=f"Function has {constraint_count} constraints. High constraint count causes "
                                   f"expensive layout calculations, especially when views update frequently.",
                        recommendation=f"Optimize constraints:\n"
                                      f"1. Use UIStackView to reduce manual constraints\n"
                                      f"2. Consider constraint priorities to reduce conflicts\n"
                                      f"3. Cache constraint references instead of recreating\n"
                                      f"4. Use frame-based layout for static views",
                        code_snippet=lines[line_num - 1].strip(),
                    ))

        return results

    def _check_collection_operations(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect expensive collection operations."""
        results = []

        # Patterns that indicate expensive operations
        expensive_patterns = [
            (r'\.map\s*\{[^}]*\.filter', 'Chained map + filter',
             'Use lazy or single pass', 60),
            (r'\.sorted\(\)\.sorted\(\)', 'Multiple sorts',
             'Sort once with custom comparator', 75),
            (r'for\s+\w+\s+in.*\.sorted\(\)', 'Sorting in loop',
             'Sort outside loop or avoid sorting', 70),
            (r'\[.*\]\s*\+\s*\[.*\]', 'Array concatenation',
             'Use append(contentsOf:) for better performance', 50),
        ]

        for pattern, description, recommendation, perf_impact in expensive_patterns:
            for match in re.finditer(pattern, content, re.DOTALL):
                line_num = content[:match.start()].count('\n') + 1

                results.append(AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=Severity.MEDIUM,
                    category=Category.PERFORMANCE,
                    title=f"Expensive collection operation - {perf_impact}% overhead",
                    description=f"{description} creates unnecessary iterations and allocations. "
                               f"For large collections, this multiplies CPU time.",
                    recommendation=recommendation,
                    code_snippet=self._get_line(content, line_num),
                ))

        return results

    def _check_network_batching(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect network requests that should be batched."""
        results = []

        # Look for network requests in loops
        lines = content.splitlines()

        for line_num, line in enumerate(lines, start=1):
            if re.search(r'for\s+\w+\s+in', line):
                # Check loop body for network calls
                loop_start = line_num
                brace_count = 1

                for i in range(loop_start, min(loop_start + 30, len(lines))):
                    brace_count += lines[i].count('{') - lines[i].count('}')

                    network_patterns = [
                        'URLSession', 'dataTask', 'fetch(',
                        'Alamofire', 'AF.request'
                    ]

                    if any(pattern in lines[i] for pattern in network_patterns):
                        results.append(AnalysisResult(
                            file=file_path,
                            line=line_num,
                            severity=Severity.HIGH,
                            category=Category.PERFORMANCE,
                            title="Network requests in loop - 80% latency multiplier",
                            description="Making individual network requests in a loop causes sequential delays. "
                                       "Each request waits for the previous, multiplying latency.",
                            recommendation="Batch network requests:\n"
                                          "1. Collect IDs/params in array\n"
                                          "2. Make single API call with batch endpoint\n"
                                          "3. Or use DispatchGroup to parallelize:\n"
                                          "   let group = DispatchGroup()\n"
                                          "   items.forEach { group.enter(); fetch($0) { group.leave() } }\n"
                                          "   group.notify { /* all done */ }",
                            code_snippet=line.strip(),
                        ))
                        break

                    if brace_count == 0:
                        break

        return results

    def _get_line(self, content: str, line_num: int) -> str:
        """Get specific line from content."""
        lines = content.splitlines()
        if 0 < line_num <= len(lines):
            return lines[line_num - 1].strip()
        return ""
