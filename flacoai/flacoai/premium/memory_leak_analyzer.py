"""
PROPRIETARY - Memory Leak Analyzer

Copyright (c) 2026 Roura.IO
All Rights Reserved.

Requires: Flaco AI Pro or Enterprise license
"""

import re
from typing import List, Dict, Set
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from analyzers.base_analyzer import BaseAnalyzer, AnalysisResult, Severity, Category


class MemoryLeakAnalyzer(BaseAnalyzer):
    """
    Premium analyzer that detects memory leaks and retain cycles.

    This analyzer identifies common memory leak patterns:
    - Retain cycles in closures
    - Delegate strong reference cycles
    - Timer leaks (not invalidated)
    - NotificationCenter observer leaks
    - Core Data managed object context leaks
    - Image cache unbounded growth
    - Singleton memory accumulation
    """

    def analyze_file(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Analyze file for memory leaks.

        Args:
            file_path: Path to file
            content: File content

        Returns:
            List of potential memory leaks with likelihood scores
        """
        results = []

        # Only analyze Swift files
        if not file_path.endswith('.swift'):
            return results

        results.extend(self._check_closure_retain_cycles(file_path, content))
        results.extend(self._check_delegate_cycles(file_path, content))
        results.extend(self._check_timer_leaks(file_path, content))
        results.extend(self._check_notification_leaks(file_path, content))
        results.extend(self._check_core_data_leaks(file_path, content))
        results.extend(self._check_image_cache_leaks(file_path, content))
        results.extend(self._check_singleton_growth(file_path, content))

        return results

    def _check_closure_retain_cycles(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect retain cycles in closures missing [weak self]."""
        results = []

        # Pattern: closure with self usage but no [weak/unowned self]
        closure_pattern = r'\{(?!\s*\[(?:weak|unowned)\s+self\])[^}]*\bself\.'

        for match in re.finditer(closure_pattern, content, re.DOTALL):
            closure_start = match.start()
            line_num = content[:closure_start].count('\n') + 1

            # Get closure context
            context_start = max(0, closure_start - 150)
            context = content[context_start:closure_start + 200]

            # High-risk contexts for retain cycles
            high_risk_indicators = [
                '@escaping',
                'DispatchQueue',
                'URLSession',
                'completion:',
                'Task {',
                '.sink',
                '.receive',
                'NotificationCenter',
                'Timer.scheduledTimer',
            ]

            risk_count = sum(1 for indicator in high_risk_indicators if indicator in context)

            if risk_count >= 2:
                leak_likelihood = min(95, 60 + risk_count * 10)

                results.append(AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=Severity.HIGH,
                    category=Category.PERFORMANCE,
                    title=f"Retain cycle in closure - {leak_likelihood}% memory leak risk",
                    description=f"Closure captures 'self' strongly, creating a retain cycle. "
                               f"Detected {risk_count} high-risk patterns. This prevents "
                               f"deallocation, causing memory to grow until app termination.",
                    recommendation=f"Use [weak self] and guard:\n"
                                  f"{{ [weak self] in\n"
                                  f"    guard let self = self else {{ return }}\n"
                                  f"    // Use self safely here\n"
                                  f"}}\n"
                                  f"Or use [unowned self] if you're certain self outlives the closure.",
                    code_snippet=self._get_line(content, line_num),
                ))

        return results

    def _check_delegate_cycles(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect delegate properties that should be weak."""
        results = []

        # Pattern: delegate properties without weak
        delegate_pattern = r'(var|let)\s+(\w*[Dd]elegate\w*)\s*:\s*(\w+)(?!\s*\??\s*=)'

        lines = content.splitlines()

        for line_num, line in enumerate(lines, start=1):
            match = re.search(delegate_pattern, line)

            if match and 'weak' not in line and 'protocol' not in line:
                delegate_name = match.group(2)

                # Check if it's a protocol type (common for delegates)
                is_protocol = any([
                    'Delegate' in delegate_name,
                    'DataSource' in delegate_name,
                    line.rstrip().endswith('?'),  # Optional type
                ])

                if is_protocol:
                    results.append(AnalysisResult(
                        file=file_path,
                        line=line_num,
                        severity=Severity.HIGH,
                        category=Category.PERFORMANCE,
                        title="Delegate strong reference - 75% retain cycle risk",
                        description=f"Delegate property '{delegate_name}' is not marked weak. "
                                   f"This creates a two-way strong reference (parent ↔ child), "
                                   f"preventing both objects from being deallocated.",
                        recommendation=f"Make delegate weak:\n"
                                      f"weak var {delegate_name}: [ProtocolName]?\n"
                                      f"Note: Must be 'var' (not let) and optional.",
                        code_snippet=line.strip(),
                    ))

        return results

    def _check_timer_leaks(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect Timer instances that may not be invalidated."""
        results = []

        # Find Timer creation
        timer_pattern = r'Timer\.scheduledTimer|Timer\(timeInterval:'

        lines = content.splitlines()

        for line_num, line in enumerate(lines, start=1):
            if re.search(timer_pattern, line):
                # Check for invalidate() call in class
                class_start = self._find_class_start(lines, line_num)
                class_end = min(class_start + 200, len(lines))
                class_body = '\n'.join(lines[class_start:class_end])

                # Look for deinit with timer.invalidate()
                has_deinit_invalidate = (
                    'deinit' in class_body and
                    'invalidate()' in class_body
                )

                if not has_deinit_invalidate:
                    results.append(AnalysisResult(
                        file=file_path,
                        line=line_num,
                        severity=Severity.HIGH,
                        category=Category.PERFORMANCE,
                        title="Timer not invalidated in deinit - 80% memory leak risk",
                        description="Timer creates a strong reference to its target. "
                                   "If not invalidated, the timer prevents the object from being "
                                   "deallocated, causing a memory leak.",
                        recommendation="Add deinit to invalidate timer:\n"
                                      "deinit {\n"
                                      "    timer?.invalidate()\n"
                                      "    timer = nil\n"
                                      "}\n"
                                      "Or use weak target pattern.",
                        code_snippet=line.strip(),
                    ))

        return results

    def _check_notification_leaks(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect NotificationCenter observers that may not be removed."""
        results = []

        # Find addObserver calls
        observer_pattern = r'NotificationCenter\.default\.addObserver'

        lines = content.splitlines()

        for line_num, line in enumerate(lines, start=1):
            if re.search(observer_pattern, line):
                # Check for removeObserver in deinit
                class_start = self._find_class_start(lines, line_num)
                class_end = min(class_start + 200, len(lines))
                class_body = '\n'.join(lines[class_start:class_end])

                has_deinit_remove = (
                    'deinit' in class_body and
                    'removeObserver' in class_body
                )

                if not has_deinit_remove:
                    results.append(AnalysisResult(
                        file=file_path,
                        line=line_num,
                        severity=Severity.MEDIUM,
                        category=Category.PERFORMANCE,
                        title="NotificationCenter observer not removed - 65% leak risk",
                        description="NotificationCenter keeps a strong reference to observers. "
                                   "While iOS 9+ auto-removes on dealloc, explicit removal is safer "
                                   "and prevents crashes if notifications fire during deallocation.",
                        recommendation="Remove observer in deinit:\n"
                                      "deinit {\n"
                                      "    NotificationCenter.default.removeObserver(self)\n"
                                      "}\n"
                                      "Or use notification publishers (Combine) which auto-clean.",
                        code_snippet=line.strip(),
                    ))

        return results

    def _check_core_data_leaks(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect Core Data context and object retention issues."""
        results = []

        # Strong references to NSManagedObjectContext
        context_pattern = r'(var|let)\s+(\w*context\w*)\s*:\s*NSManagedObjectContext(?!\?)'

        lines = content.splitlines()

        for line_num, line in enumerate(lines, start=1):
            match = re.search(context_pattern, line, re.IGNORECASE)

            if match and 'weak' not in line:
                context_name = match.group(2)

                results.append(AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=Severity.MEDIUM,
                    category=Category.PERFORMANCE,
                    title="Strong reference to NSManagedObjectContext - 60% leak risk",
                    description=f"Holding a strong reference to Core Data context '{context_name}' "
                               f"can create retain cycles if the context holds objects that reference "
                               f"back to this class. Contexts should typically be weak or accessed "
                               f"via a coordinator.",
                    recommendation=f"Consider making it weak or accessing via coordinator:\n"
                                  f"weak var {context_name}: NSManagedObjectContext?\n"
                                  f"Or access from AppDelegate/SceneDelegate when needed.",
                    code_snippet=line.strip(),
                ))

            # Fetched objects stored in arrays without clearing
            if 'NSFetchRequest' in line or 'fetchRequest()' in line:
                # Check if results stored in property
                context_lines = lines[max(0, line_num - 5):min(line_num + 10, len(lines))]
                context_text = '\n'.join(context_lines)

                if 'self.' in context_text and '=' in context_text:
                    results.append(AnalysisResult(
                        file=file_path,
                        line=line_num,
                        severity=Severity.LOW,
                        category=Category.PERFORMANCE,
                        title="Core Data objects retained in property - memory growth risk",
                        description="Storing fetched managed objects in properties keeps them in memory. "
                                   "For large datasets, this causes unbounded memory growth.",
                        recommendation="Only fetch when needed, or use NSFetchedResultsController:\n"
                                      "let controller = NSFetchedResultsController(...)\n"
                                      "controller.performFetch()\n"
                                      "// Accesses objects on demand, releases when not needed",
                        code_snippet=line.strip(),
                    ))

        return results

    def _check_image_cache_leaks(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect image caching without size limits."""
        results = []

        # Image cache patterns
        cache_patterns = [
            (r'var\s+imageCache\s*=\s*\[.*:\s*UIImage\]', 'Dictionary-based image cache'),
            (r'NSCache<.*UIImage>', 'NSCache for images'),
            (r'var\s+.*cache.*=.*UIImage', 'Image cache property'),
        ]

        lines = content.splitlines()

        for line_num, line in enumerate(lines, start=1):
            for pattern, description in cache_patterns:
                if re.search(pattern, line):
                    # Check for size limits
                    class_start = self._find_class_start(lines, line_num)
                    class_end = min(class_start + 100, len(lines))
                    class_body = '\n'.join(lines[class_start:class_end])

                    has_limit = any([
                        'countLimit' in class_body,
                        'totalCostLimit' in class_body,
                        'maxCacheSize' in class_body,
                        'removeAll()' in class_body,
                    ])

                    if not has_limit:
                        results.append(AnalysisResult(
                            file=file_path,
                            line=line_num,
                            severity=Severity.MEDIUM,
                            category=Category.PERFORMANCE,
                            title="Image cache without size limit - unbounded memory growth",
                            description=f"{description} has no size limit. Images are large "
                                       f"(MBs each), so unlimited caching causes memory warnings "
                                       f"and eventual app termination.",
                            recommendation="Add cache limits:\n"
                                          "For NSCache:\n"
                                          "  cache.countLimit = 50\n"
                                          "  cache.totalCostLimit = 50 * 1024 * 1024 // 50MB\n"
                                          "For Dictionary:\n"
                                          "  Use NSCache instead, or manually evict old entries.",
                            code_snippet=line.strip(),
                        ))

        return results

    def _check_singleton_growth(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect singletons accumulating data without cleanup."""
        results = []

        # Singleton pattern detection
        singleton_pattern = r'static\s+(?:let|var)\s+shared\s*=\s*\w+\('

        lines = content.splitlines()

        for line_num, line in enumerate(lines, start=1):
            if re.search(singleton_pattern, line):
                # Check if singleton has array/dict properties
                class_start = self._find_class_start(lines, line_num)
                class_end = min(class_start + 150, len(lines))
                class_body = '\n'.join(lines[class_start:class_end])

                # Look for collection properties
                has_collections = any([
                    re.search(r'var\s+\w+\s*:\s*\[', class_body),
                    re.search(r'var\s+\w+\s*=\s*\[', class_body),
                    'Dictionary' in class_body,
                    'Set<' in class_body,
                ])

                # Look for cleanup methods
                has_cleanup = any([
                    'removeAll()' in class_body,
                    'clear()' in class_body,
                    'reset()' in class_body,
                    'func cleanup' in class_body,
                ])

                if has_collections and not has_cleanup:
                    results.append(AnalysisResult(
                        file=file_path,
                        line=line_num,
                        severity=Severity.MEDIUM,
                        category=Category.PERFORMANCE,
                        title="Singleton accumulating data without cleanup - 70% memory growth",
                        description="Singleton lives for entire app lifetime. If it accumulates data "
                                   "in arrays/dictionaries without cleanup, memory grows unbounded.",
                        recommendation="Add cleanup method:\n"
                                      "func reset() {\n"
                                      "    cachedData.removeAll()\n"
                                      "    // Clear other collections\n"
                                      "}\n"
                                      "Call reset() when appropriate (logout, memory warning, etc.)",
                        code_snippet=line.strip(),
                    ))

        return results

    def _get_line(self, content: str, line_num: int) -> str:
        """Get specific line from content."""
        lines = content.splitlines()
        if 0 < line_num <= len(lines):
            return lines[line_num - 1].strip()
        return ""

    def _find_class_start(self, lines: List[str], current_line: int) -> int:
        """Find the start of the class/struct containing current line."""
        for i in range(current_line - 1, max(0, current_line - 100), -1):
            if re.match(r'^\s*(class|struct|actor|enum)\s+\w+', lines[i]):
                return i
        return max(0, current_line - 50)
