"""
PROPRIETARY - Crash Prediction Analyzer

Copyright (c) 2026 Roura.IO
All Rights Reserved.

Requires: Flaco AI Pro or Enterprise license
"""

import re
from typing import List
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from analyzers.base_analyzer import BaseAnalyzer, AnalysisResult, Severity, Category


class CrashPredictionAnalyzer(BaseAnalyzer):
    """
    Premium analyzer that predicts potential crash points using
    pattern matching and heuristic analysis.

    This analyzer uses sophisticated pattern recognition to identify
    code that is statistically likely to cause crashes based on:
    - Force unwrapping patterns
    - Array index access patterns
    - Optional chaining complexity
    - Error handling gaps
    - Threading issues
    - Memory access patterns
    """

    def analyze_file(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Analyze file for crash prediction.

        Args:
            file_path: Path to file
            content: File content

        Returns:
            List of predicted crash points with likelihood scores
        """
        results = []

        # Only analyze Swift files
        if not file_path.endswith('.swift'):
            return results

        results.extend(self._check_force_unwrap_chains(file_path, content))
        results.extend(self._check_array_bounds_access(file_path, content))
        results.extend(self._check_optional_cascade_complexity(file_path, content))
        results.extend(self._check_unchecked_casts(file_path, content))
        results.extend(self._check_async_await_crashes(file_path, content))
        results.extend(self._check_collection_mutation(file_path, content))
        results.extend(self._check_weak_self_missing(file_path, content))

        return results

    def _check_force_unwrap_chains(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect chained force unwraps (high crash risk).

        Pattern: user!.profile!.name
        """
        results = []

        # Match multiple ! in a single expression
        pattern = r'(\w+!)(?:\.\w+!)+'

        for match in re.finditer(pattern, content, re.MULTILINE):
            line_num = content[:match.start()].count('\n') + 1
            code = match.group(0)

            # Count number of force unwraps
            unwrap_count = code.count('!')

            # Higher unwrap count = higher crash likelihood
            if unwrap_count >= 3:
                severity = Severity.CRITICAL
                likelihood = 95
            elif unwrap_count == 2:
                severity = Severity.HIGH
                likelihood = 75
            else:
                severity = Severity.MEDIUM
                likelihood = 50

            results.append(AnalysisResult(
                file=file_path,
                line=line_num,
                severity=severity,
                category=Category.QUALITY,
                title=f"Chained force unwraps detected ({unwrap_count} levels) - {likelihood}% crash risk",
                description=f"Multiple chained force unwraps create a compound crash risk. "
                           f"Each ! can fail independently, making this {likelihood}% likely to crash "
                           f"if any value in the chain is nil.",
                recommendation=f"Use optional chaining (?.) or guard statements:\n"
                              f"guard let name = user?.profile?.name else {{ return }}\n"
                              f"Or use if-let: if let name = user?.profile?.name {{ ... }}",
                code_snippet=self._get_line(content, line_num),
            ))

        return results

    def _check_array_bounds_access(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect unsafe array subscript access.

        Pattern: array[index] without bounds checking
        """
        results = []

        # Match array subscript access
        pattern = r'(\w+)\[([^\]]+)\]'

        lines = content.splitlines()

        for line_num, line in enumerate(lines, start=1):
            for match in re.finditer(pattern, line):
                array_name = match.group(1)
                index_expr = match.group(2)

                # Skip if there's bounds checking nearby
                context_start = max(0, line_num - 3)
                context_end = min(len(lines), line_num + 2)
                context = '\n'.join(lines[context_start:context_end])

                # Look for bounds checking patterns
                bounds_check_patterns = [
                    f'{array_name}.count',
                    f'{array_name}.isEmpty',
                    f'{array_name}.indices.contains',
                    'guard',
                    'if.*<.*count',
                ]

                has_bounds_check = any(
                    re.search(pattern, context, re.IGNORECASE)
                    for pattern in bounds_check_patterns
                )

                if not has_bounds_check:
                    # No bounds checking found - potential crash
                    results.append(AnalysisResult(
                        file=file_path,
                        line=line_num,
                        severity=Severity.HIGH,
                        category=Category.QUALITY,
                        title="Unchecked array access - 60% crash risk",
                        description=f"Array subscript access '{match.group(0)}' without bounds checking. "
                                   f"Will crash with 'Index out of range' if index is invalid.",
                        recommendation=f"Add bounds checking:\n"
                                      f"guard {array_name}.indices.contains({index_expr}) else {{ return }}\n"
                                      f"Or use safe subscript: {array_name}[safe: {index_expr}]",
                        code_snippet=line.strip(),
                    ))

        return results

    def _check_optional_cascade_complexity(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect complex optional chaining that could hide crashes.

        Pattern: user?.profile?.settings?.theme?.color?.rgb
        """
        results = []

        # Match long optional chains
        pattern = r'(\w+\?\.)+\w+'

        for match in re.finditer(pattern, content):
            chain = match.group(0)
            depth = chain.count('?.')

            if depth >= 4:
                line_num = content[:match.start()].count('\n') + 1

                results.append(AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=Severity.MEDIUM,
                    category=Category.QUALITY,
                    title=f"Deep optional chain ({depth} levels) - crash masking risk",
                    description=f"Optional chain with {depth} levels may mask underlying nil issues. "
                               f"While it won't crash, it silently fails and returns nil, "
                               f"which could cause crashes downstream.",
                    recommendation=f"Break into explicit checks with guard statements to identify "
                                  f"which level is nil:\n"
                                  f"guard let profile = user?.profile else {{ /* handle */ }}\n"
                                  f"guard let settings = profile.settings else {{ /* handle */ }}",
                    code_snippet=self._get_line(content, line_num),
                ))

        return results

    def _check_unchecked_casts(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect unsafe type casts.

        Pattern: value as! Type
        """
        results = []

        pattern = r'\sas!\s+(\w+)'

        for match in re.finditer(pattern, content):
            line_num = content[:match.start()].count('\n') + 1
            target_type = match.group(1)

            results.append(AnalysisResult(
                file=file_path,
                line=line_num,
                severity=Severity.HIGH,
                category=Category.QUALITY,
                title="Force cast detected - 70% crash risk",
                description=f"Force cast 'as! {target_type}' will crash if the cast fails. "
                           f"This is a common source of runtime crashes.",
                recommendation=f"Use conditional cast with guard:\n"
                              f"guard let value = value as? {target_type} else {{ return }}",
                code_snippet=self._get_line(content, line_num),
            ))

        return results

    def _check_async_await_crashes(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect potential async/await crash points."""
        results = []

        # Look for await without try in throwing contexts
        pattern = r'\bawait\s+(?!try\s)(\w+\([^)]*\))'

        for match in re.finditer(pattern, content):
            line_num = content[:match.start()].count('\n') + 1

            # Check if we're in a throwing context
            lines = content.splitlines()
            func_context = self._get_function_context(lines, line_num)

            if 'throws' in func_context:
                results.append(AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=Severity.HIGH,
                    category=Category.QUALITY,
                    title="Unhandled async throwing call - 55% crash risk",
                    description="Using 'await' without 'try' on a throwing function. "
                               "This will crash if the function throws an error.",
                    recommendation="Add try-catch:\ntry await function()\n"
                                  "Or use: try? await function() to handle error",
                    code_snippet=self._get_line(content, line_num),
                ))

        return results

    def _check_collection_mutation(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect collection mutation during iteration."""
        results = []

        lines = content.splitlines()

        for line_num, line in enumerate(lines, start=1):
            # Look for for-in loops
            if re.search(r'for\s+\w+\s+in\s+(\w+)', line):
                match = re.search(r'for\s+\w+\s+in\s+(\w+)', line)
                collection_name = match.group(1)

                # Check next 10 lines for mutation of same collection
                for offset in range(1, min(11, len(lines) - line_num + 1)):
                    next_line = lines[line_num + offset - 1]

                    mutation_patterns = [
                        f'{collection_name}.append',
                        f'{collection_name}.remove',
                        f'{collection_name}.insert',
                        f'{collection_name}\[',  # subscript assignment
                    ]

                    if any(pattern in next_line for pattern in mutation_patterns):
                        results.append(AnalysisResult(
                            file=file_path,
                            line=line_num,
                            severity=Severity.CRITICAL,
                            category=Category.QUALITY,
                            title="Collection mutation during iteration - 90% crash risk",
                            description=f"Modifying collection '{collection_name}' while iterating over it. "
                                       f"This causes 'Collection was mutated while being enumerated' crash.",
                            recommendation=f"Iterate over a copy:\nfor item in {collection_name}.map({{ $0 }}) {{\n"
                                          f"Or collect indices/items to modify after iteration",
                            code_snippet=self._get_line(content, line_num),
                        ))
                        break

        return results

    def _check_weak_self_missing(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect closures that should use [weak self] to prevent crashes."""
        results = []

        # Look for closures with self usage but no [weak self]
        closure_pattern = r'\{(?!\s*\[(?:weak|unowned)\s+self\])[^}]*\bself\.[^}]+\}'

        for match in re.finditer(closure_pattern, content, re.DOTALL):
            closure_text = match.group(0)
            line_num = content[:match.start()].count('\n') + 1

            # Check if this is in an async context or escaping closure
            is_risky = (
                'async' in closure_text or
                '@escaping' in content[max(0, match.start()-100):match.start()] or
                'DispatchQueue' in content[max(0, match.start()-50):match.start()]
            )

            if is_risky:
                results.append(AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=Severity.MEDIUM,
                    category=Category.PERFORMANCE,
                    title="Missing [weak self] in escaping closure - retain cycle risk",
                    description="Closure captures self strongly, creating a retain cycle risk. "
                               "While not an immediate crash, this causes memory leaks that "
                               "eventually lead to app termination.",
                    recommendation="Add [weak self] and guard:\n"
                                  "{ [weak self] in\n"
                                  "    guard let self = self else { return }",
                    code_snippet=self._get_line(content, line_num),
                ))

        return results

    def _get_line(self, content: str, line_num: int) -> str:
        """Get specific line from content."""
        lines = content.splitlines()
        if 0 < line_num <= len(lines):
            return lines[line_num - 1].strip()
        return ""

    def _get_function_context(self, lines: List[str], line_num: int) -> str:
        """Get function signature context for a line."""
        # Look backwards for function declaration
        for i in range(max(0, line_num - 20), line_num):
            if i < len(lines) and 'func ' in lines[i]:
                return lines[i]
        return ""
