"""
PROPRIETARY - Technical Debt Analyzer

Copyright (c) 2026 Roura.IO
All Rights Reserved.

Requires: Flaco AI Pro or Enterprise license
"""

import re
from typing import List, Dict, Set, Tuple
from collections import defaultdict
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from analyzers.base_analyzer import BaseAnalyzer, AnalysisResult, Severity, Category


class TechnicalDebtAnalyzer(BaseAnalyzer):
    """
    Premium analyzer quantifying technical debt and code maintainability.

    Provides quantitative metrics:
    - Maintainability Index (0-100)
    - Cyclomatic complexity scores
    - Code duplication detection
    - File size and line count warnings
    - Dependency coupling analysis
    - Test coverage gaps
    - Documentation debt
    """

    # Thresholds
    MAX_FUNCTION_LINES = 50
    MAX_FILE_LINES = 500
    MAX_CYCLOMATIC_COMPLEXITY = 10
    MAX_PARAMETERS = 5
    MAX_CLASS_PROPERTIES = 15

    def analyze_file(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Analyze file for technical debt.

        Args:
            file_path: Path to file
            content: File content

        Returns:
            List of technical debt findings
        """
        results = []

        # Only analyze Swift files
        if not file_path.endswith('.swift'):
            return results

        results.extend(self._check_file_size(file_path, content))
        results.extend(self._check_function_complexity(file_path, content))
        results.extend(self._check_code_duplication(file_path, content))
        results.extend(self._check_class_complexity(file_path, content))
        results.extend(self._check_documentation_debt(file_path, content))
        results.extend(self._check_dependency_coupling(file_path, content))
        results.extend(self._check_test_coverage_gaps(file_path, content))

        return results

    def calculate_maintainability_index(self, file_path: str, content: str) -> Dict:
        """Calculate maintainability index for a file.

        Based on Microsoft's Maintainability Index formula:
        MI = MAX(0, (171 - 5.2 * ln(HV) - 0.23 * CC - 16.2 * ln(LOC)) * 100 / 171)

        Where:
        - HV = Halstead Volume (approximated)
        - CC = Cyclomatic Complexity
        - LOC = Lines of Code

        Returns:
            Dict with score, grade, and metrics
        """
        lines = [l for l in content.splitlines() if l.strip() and not l.strip().startswith('//')]
        loc = len(lines)

        # Approximate cyclomatic complexity
        cc = self._calculate_cyclomatic_complexity(content)

        # Simplified Halstead Volume (unique operators + operands)
        operators = len(re.findall(r'[+\-*/=<>!&|^~%]', content))
        operands = len(re.findall(r'\b[a-zA-Z_]\w*\b', content))
        halstead_volume = operators + operands

        # Calculate MI (simplified version)
        import math
        try:
            mi = max(0, (171 - 5.2 * math.log(max(1, halstead_volume)) -
                        0.23 * cc - 16.2 * math.log(max(1, loc))) * 100 / 171)
        except:
            mi = 50  # Fallback

        # Assign grade
        if mi >= 85:
            grade = 'A'
            assessment = 'Excellent'
        elif mi >= 70:
            grade = 'B'
            assessment = 'Good'
        elif mi >= 50:
            grade = 'C'
            assessment = 'Fair'
        elif mi >= 25:
            grade = 'D'
            assessment = 'Poor'
        else:
            grade = 'F'
            assessment = 'Critical'

        return {
            'score': round(mi, 1),
            'grade': grade,
            'assessment': assessment,
            'metrics': {
                'lines_of_code': loc,
                'cyclomatic_complexity': cc,
                'halstead_volume': halstead_volume,
            }
        }

    def _check_file_size(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for oversized files."""
        results = []

        lines = content.splitlines()
        code_lines = [l for l in lines if l.strip() and not l.strip().startswith('//')]
        line_count = len(code_lines)

        if line_count > self.MAX_FILE_LINES:
            debt_score = min(100, (line_count - self.MAX_FILE_LINES) // 10)

            results.append(AnalysisResult(
                file=file_path,
                line=1,
                severity=Severity.MEDIUM if line_count > 1000 else Severity.LOW,
                category=Category.QUALITY,
                title=f"Large file - {line_count} lines (debt score: {debt_score})",
                description=f"File has {line_count} lines of code. Large files are harder to understand, "
                           f"test, and maintain. Recommended max: {self.MAX_FILE_LINES} lines.",
                recommendation=f"Refactor into smaller files:\n"
                              f"1. Extract related types into separate files\n"
                              f"2. Split by feature or responsibility\n"
                              f"3. Move private nested types to extensions\n"
                              f"Target: <{self.MAX_FILE_LINES} lines per file",
                code_snippet=f"{line_count} lines of code",
            ))

        return results

    def _check_function_complexity(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for overly complex functions."""
        results = []

        # Find function definitions
        func_pattern = r'func\s+(\w+)\s*\([^)]*\)(?:\s*(?:async|throws|rethrows))?\s*(?:->\s*\w+(?:<[^>]+>)?)?\s*\{'

        lines = content.splitlines()

        for match in re.finditer(func_pattern, content):
            func_name = match.group(1)
            func_start_line = content[:match.start()].count('\n') + 1
            func_start_char = match.start()

            # Find function end
            brace_count = 1
            pos = match.end()
            while pos < len(content) and brace_count > 0:
                if content[pos] == '{':
                    brace_count += 1
                elif content[pos] == '}':
                    brace_count -= 1
                pos += 1

            func_body = content[match.end():pos]
            func_lines = [l for l in func_body.splitlines() if l.strip() and not l.strip().startswith('//')]
            func_line_count = len(func_lines)

            # Calculate cyclomatic complexity for this function
            complexity = self._calculate_cyclomatic_complexity(func_body)

            # Check function size
            if func_line_count > self.MAX_FUNCTION_LINES:
                debt_score = (func_line_count - self.MAX_FUNCTION_LINES) // 5

                results.append(AnalysisResult(
                    file=file_path,
                    line=func_start_line,
                    severity=Severity.MEDIUM if func_line_count > 100 else Severity.LOW,
                    category=Category.QUALITY,
                    title=f"Long function '{func_name}' - {func_line_count} lines (debt: {debt_score})",
                    description=f"Function has {func_line_count} lines. Long functions are hard to understand "
                               f"and test. Recommended max: {self.MAX_FUNCTION_LINES} lines.",
                    recommendation=f"Extract helper methods:\n"
                                  f"1. Identify logical blocks\n"
                                  f"2. Extract to private helper functions\n"
                                  f"3. Use meaningful names for helpers\n"
                                  f"Target: <{self.MAX_FUNCTION_LINES} lines",
                    code_snippet=f"func {func_name}() {{ ... {func_line_count} lines ... }}",
                ))

            # Check cyclomatic complexity
            if complexity > self.MAX_CYCLOMATIC_COMPLEXITY:
                debt_score = (complexity - self.MAX_CYCLOMATIC_COMPLEXITY) * 5

                results.append(AnalysisResult(
                    file=file_path,
                    line=func_start_line,
                    severity=Severity.HIGH if complexity > 20 else Severity.MEDIUM,
                    category=Category.QUALITY,
                    title=f"High complexity '{func_name}' - CC={complexity} (debt: {debt_score})",
                    description=f"Cyclomatic complexity of {complexity} (threshold: {self.MAX_CYCLOMATIC_COMPLEXITY}). "
                               f"High complexity indicates many execution paths, making testing difficult.",
                    recommendation=f"Reduce complexity:\n"
                                  f"1. Extract nested conditionals to functions\n"
                                  f"2. Replace complex conditions with guard statements\n"
                                  f"3. Use early returns to reduce nesting\n"
                                  f"4. Consider strategy pattern for multiple branches",
                    code_snippet=f"func {func_name}() - cyclomatic complexity: {complexity}",
                ))

        return results

    def _check_code_duplication(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect code duplication within file."""
        results = []

        lines = [l.strip() for l in content.splitlines() if l.strip() and not l.strip().startswith('//')]

        # Look for repeated code blocks (5+ consecutive similar lines)
        block_size = 5
        seen_blocks = defaultdict(list)

        for i in range(len(lines) - block_size + 1):
            block = tuple(lines[i:i + block_size])
            block_str = ''.join(block)

            # Skip very short blocks
            if len(block_str) < 50:
                continue

            seen_blocks[block].append(i + 1)

        # Report duplicates
        for block, occurrences in seen_blocks.items():
            if len(occurrences) > 1:
                debt_score = len(occurrences) * 10

                results.append(AnalysisResult(
                    file=file_path,
                    line=occurrences[0],
                    severity=Severity.MEDIUM,
                    category=Category.QUALITY,
                    title=f"Code duplication - {len(occurrences)} instances (debt: {debt_score})",
                    description=f"Found {len(occurrences)} duplicated code blocks. "
                               f"Duplication increases maintenance burden - bugs must be fixed in multiple places.",
                    recommendation=f"Extract to shared function or method:\n"
                                  f"1. Create private helper function\n"
                                  f"2. Parameterize differences\n"
                                  f"3. Replace all duplicates with calls\n"
                                  f"DRY principle: Don't Repeat Yourself",
                    code_snippet=f"Duplicated block at lines: {', '.join(map(str, occurrences))}",
                ))

        return results

    def _check_class_complexity(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for overly complex classes."""
        results = []

        # Find class/struct definitions
        class_pattern = r'(class|struct|actor)\s+(\w+)'

        for match in re.finditer(class_pattern, content):
            class_type = match.group(1)
            class_name = match.group(2)
            class_start = match.start()
            line_num = content[:class_start].count('\n') + 1

            # Find class body
            brace_start = content.find('{', class_start)
            if brace_start == -1:
                continue

            brace_count = 1
            pos = brace_start + 1
            while pos < len(content) and brace_count > 0:
                if content[pos] == '{':
                    brace_count += 1
                elif content[pos] == '}':
                    brace_count -= 1
                pos += 1

            class_body = content[brace_start:pos]

            # Count properties
            property_count = len(re.findall(r'(var|let)\s+\w+\s*:', class_body))

            # Count methods
            method_count = len(re.findall(r'func\s+\w+', class_body))

            # Check property count
            if property_count > self.MAX_CLASS_PROPERTIES:
                debt_score = (property_count - self.MAX_CLASS_PROPERTIES) * 3

                results.append(AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=Severity.MEDIUM,
                    category=Category.QUALITY,
                    title=f"{class_type} '{class_name}' has {property_count} properties (debt: {debt_score})",
                    description=f"Class has {property_count} properties (threshold: {self.MAX_CLASS_PROPERTIES}). "
                               f"Large classes violate Single Responsibility Principle.",
                    recommendation=f"Split into smaller classes:\n"
                                  f"1. Group related properties\n"
                                  f"2. Extract to separate types\n"
                                  f"3. Use composition over inheritance\n"
                                  f"4. Consider protocol-oriented design",
                    code_snippet=f"{class_type} {class_name} - {property_count} properties, {method_count} methods",
                ))

            # Check method count
            if method_count > 20:
                debt_score = (method_count - 20) * 2

                results.append(AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=Severity.LOW,
                    category=Category.QUALITY,
                    title=f"{class_type} '{class_name}' has {method_count} methods (debt: {debt_score})",
                    description=f"Class has {method_count} methods. High method count suggests "
                               f"class is doing too much (violates SRP).",
                    recommendation=f"Refactor to smaller classes with focused responsibilities",
                    code_snippet=f"{class_type} {class_name} - {method_count} methods",
                ))

        return results

    def _check_documentation_debt(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for missing documentation."""
        results = []

        # Find public functions without doc comments
        lines = content.splitlines()

        for line_num, line in enumerate(lines, start=1):
            if re.match(r'\s*(public|open)\s+func\s+\w+', line):
                # Check previous lines for doc comment
                has_doc = False
                for i in range(max(0, line_num - 5), line_num):
                    if i < len(lines) and '///' in lines[i]:
                        has_doc = True
                        break

                if not has_doc:
                    results.append(AnalysisResult(
                        file=file_path,
                        line=line_num,
                        severity=Severity.LOW,
                        category=Category.QUALITY,
                        title="Public API missing documentation",
                        description="Public function lacks documentation comment. "
                                   "Public APIs should have clear documentation for consumers.",
                        recommendation="Add doc comment:\n"
                                      "/// Brief description\n"
                                      "///\n"
                                      "/// - Parameters:\n"
                                      "///   - param: Description\n"
                                      "/// - Returns: Description",
                        code_snippet=line.strip(),
                    ))

        # Check for TODO/FIXME comments
        for line_num, line in enumerate(lines, start=1):
            if 'TODO' in line or 'FIXME' in line:
                marker = 'TODO' if 'TODO' in line else 'FIXME'

                results.append(AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=Severity.LOW,
                    category=Category.QUALITY,
                    title=f"{marker} comment - unfinished work",
                    description=f"{marker} indicates incomplete or temporary code. "
                               f"These accumulate as technical debt if not addressed.",
                    recommendation=f"Address {marker} item:\n"
                                  f"1. Create ticket to track work\n"
                                  f"2. Schedule time to resolve\n"
                                  f"3. Remove comment when done",
                    code_snippet=line.strip(),
                ))

        return results

    def _check_dependency_coupling(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for tight coupling via import count."""
        results = []

        # Count imports
        import_count = len(re.findall(r'^import\s+\w+', content, re.MULTILINE))

        if import_count > 15:
            debt_score = (import_count - 15) * 2

            results.append(AnalysisResult(
                file=file_path,
                line=1,
                severity=Severity.LOW,
                category=Category.QUALITY,
                title=f"High coupling - {import_count} imports (debt: {debt_score})",
                description=f"File imports {import_count} modules. High import count indicates "
                           f"tight coupling, making file harder to test and reuse.",
                recommendation=f"Reduce dependencies:\n"
                              f"1. Use dependency injection\n"
                              f"2. Define protocols for abstractions\n"
                              f"3. Remove unused imports\n"
                              f"4. Group related functionality",
                code_snippet=f"{import_count} imports",
            ))

        return results

    def _check_test_coverage_gaps(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Identify potential test coverage gaps."""
        results = []

        # Skip test files themselves
        if 'Test' in file_path or 'Spec' in file_path:
            return results

        # Look for complex logic without corresponding test
        has_complex_logic = any([
            re.search(r'\bif\b', content),
            re.search(r'\bguard\b', content),
            re.search(r'\bswitch\b', content),
            re.search(r'\bfor\b', content),
            re.search(r'\bwhile\b', content),
        ])

        # Check if corresponding test file likely exists
        test_file_might_exist = any([
            'Tests' in file_path,
            file_path.replace('.swift', 'Tests.swift'),
            file_path.replace('.swift', 'Spec.swift'),
        ])

        if has_complex_logic and not test_file_might_exist:
            results.append(AnalysisResult(
                file=file_path,
                line=1,
                severity=Severity.LOW,
                category=Category.QUALITY,
                title="Potential test coverage gap",
                description="File contains complex logic but no obvious corresponding test file. "
                           "Untested code accumulates technical debt.",
                recommendation="Add unit tests:\n"
                              "1. Create [FileName]Tests.swift\n"
                              "2. Test happy paths and edge cases\n"
                              "3. Aim for >80% coverage on business logic\n"
                              "4. Use XCTest or Quick/Nimble",
                code_snippet="Complex logic detected without tests",
            ))

        return results

    def _calculate_cyclomatic_complexity(self, code: str) -> int:
        """Calculate cyclomatic complexity.

        CC = Number of decision points + 1

        Decision points: if, else if, for, while, switch, case, catch, ?, &&, ||
        """
        complexity = 1  # Base complexity

        # Count decision keywords
        complexity += len(re.findall(r'\bif\b', code))
        complexity += len(re.findall(r'\belse\s+if\b', code))
        complexity += len(re.findall(r'\bfor\b', code))
        complexity += len(re.findall(r'\bwhile\b', code))
        complexity += len(re.findall(r'\bcase\b', code))
        complexity += len(re.findall(r'\bcatch\b', code))
        complexity += len(re.findall(r'\bguard\b', code))

        # Count logical operators
        complexity += len(re.findall(r'\&\&', code))
        complexity += len(re.findall(r'\|\|', code))

        # Count ternary operators
        complexity += len(re.findall(r'\?[^?]', code))  # Exclude ?? operator

        return complexity

    def _get_line(self, content: str, line_num: int) -> str:
        """Get specific line from content."""
        lines = content.splitlines()
        if 0 < line_num <= len(lines):
            return lines[line_num - 1].strip()
        return ""
