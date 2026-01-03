"""Quality analyzer for code smells and maintainability issues."""

import re
from typing import List
from .base_analyzer import BaseAnalyzer, AnalysisResult, Severity, Category


class QualityAnalyzer(BaseAnalyzer):
    """Analyzes code quality, code smells, and maintainability."""

    def __init__(self, io=None, verbose=False):
        super().__init__(io, verbose)

        # Code smell patterns
        self.code_smell_patterns = [
            (r'def\s+\w+\([^)]{100,}\)', "Long parameter list (>100 chars)"),
            (r'if\s+.*and.*and.*and.*and', "Complex conditional (too many conditions)"),
            (r'(if|elif).*:.*#.*TODO', "TODO in conditional"),
        ]

        # Magic number patterns
        self.magic_number_patterns = [
            (r'[^a-zA-Z0-9_]([\d]{2,})[^a-zA-Z0-9_.]', "Magic number"),
        ]

        # Duplicate code patterns
        self.duplication_patterns = [
            (r'(def\s+\w+.*:.*\n(?: {4}|\t).*){5,}\n+(?=def\s+\w+.*:.*\n(?: {4}|\t).*)', "Potential code duplication"),
        ]

        # Dead code patterns
        self.dead_code_patterns = [
            (r'if\s+False:', "Dead code (if False)"),
            (r'if\s+0:', "Dead code (if 0)"),
            (r'return.*\n.*return', "Unreachable code after return"),
            (r'def\s+\w+.*:\s*\n\s+pass\s*$', "Empty function"),
        ]

        # Complexity patterns
        self.complexity_patterns = [
            (r'class\s+\w+.*:\s*\n(?:(?:.*\n){200,})', "Large class (>200 lines)"),
            (r'def\s+\w+.*:\s*\n(?:(?:.*\n){50,})(?=def\s|\nclass\s|\Z)', "Long function (>50 lines)"),
        ]

        # Poor naming patterns
        self.naming_patterns = [
            (r'\b[a-z]\b\s*=', "Single letter variable"),
            (r'def\s+[a-z]{1,2}\(', "Short function name"),
            (r'class\s+[a-z]', "Lowercase class name"),
        ]

        # iOS/Swift-specific quality patterns
        self.ios_force_unwrap_patterns = [
            (r'!\s*(?!\(|=)', "Force unwrap (!) used"),
            (r'as!\s+\w+', "Force downcast (as!) used"),
            (r'try!\s+', "Force try (try!) used"),
        ]

        self.ios_implicitly_unwrapped_patterns = [
            (r'var\s+\w+:\s*\w+!', "Implicitly unwrapped optional (!)"),
            (r'let\s+\w+:\s*\w+!', "Implicitly unwrapped optional (!)"),
        ]

        self.ios_swiftui_patterns = [
            (r'var\s+body:\s*some\s+View\s*\{(?:[^}]{500,})\}', "Large SwiftUI body (>500 chars)"),
            (r'@State\s+var\s+\w+.*=.*\n.*@State', "Multiple @State vars (consider @StateObject or view model)"),
            (r'View\s*\{[^}]*(if|switch).*\{[^}]*(if|switch)', "Deeply nested conditionals in View"),
        ]

        self.ios_accessibility_patterns = [
            (r'Button\([^)]*\)(?!.*accessibility)', "Button without accessibility label"),
            (r'Image\([^)]*\)(?!.*accessibility)', "Image without accessibility label"),
            (r'\.onTapGesture(?!.*accessibility)', "Custom gesture without accessibility"),
        ]

        self.ios_naming_patterns = [
            (r'class\s+[a-z]', "Swift class should start with uppercase"),
            (r'struct\s+[a-z]', "Swift struct should start with uppercase"),
            (r'enum\s+[a-z]', "Swift enum should start with uppercase"),
            (r'protocol\s+[a-z]', "Swift protocol should start with uppercase"),
            (r'func\s+[A-Z]', "Swift function should start with lowercase"),
        ]

        self.ios_documentation_patterns = [
            (r'public\s+(func|var|let|class|struct|enum)(?!.*///)(?!.*\*/)', "Public API without documentation"),
            (r'open\s+(func|var|let|class)(?!.*///)(?!.*\*/)', "Open declaration without documentation"),
        ]

        self.ios_error_handling_patterns = [
            (r'catch\s*\{[^}]*\}', "Empty or generic catch block"),
            (r'do\s*\{[^}]*\}\s*catch\s*\{\s*\}', "Empty catch block"),
        ]

    def analyze_file(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Analyze a file for quality issues."""
        results = []

        if not self._is_code_file(file_path):
            return results

        results.extend(self._check_patterns(file_path, content, self.code_smell_patterns,
                                           "Code Smell", Severity.MEDIUM,
                                           "Refactor to improve readability and maintainability"))

        results.extend(self._check_magic_numbers(file_path, content))

        results.extend(self._check_patterns(file_path, content, self.dead_code_patterns,
                                           "Dead Code", Severity.LOW,
                                           "Remove unused or unreachable code"))

        results.extend(self._check_patterns(file_path, content, self.complexity_patterns,
                                           "High Complexity", Severity.MEDIUM,
                                           "Consider breaking into smaller, more focused units"))

        results.extend(self._check_patterns(file_path, content, self.naming_patterns,
                                           "Poor Naming", Severity.LOW,
                                           "Use descriptive, meaningful names"))

        # Check cyclomatic complexity
        results.extend(self._check_cyclomatic_complexity(file_path, content))

        # iOS/Swift-specific checks
        ext = self.get_file_extension(file_path)
        if ext in ('swift',):
            results.extend(self._check_patterns(file_path, content, self.ios_force_unwrap_patterns,
                                               "Force Unwrap", Severity.MEDIUM,
                                               "Use optional binding (if let, guard let) or nil coalescing (??) instead"))

            results.extend(self._check_patterns(file_path, content, self.ios_implicitly_unwrapped_patterns,
                                               "Implicitly Unwrapped Optional", Severity.LOW,
                                               "Avoid implicitly unwrapped optionals, use regular optionals instead"))

            results.extend(self._check_patterns(file_path, content, self.ios_swiftui_patterns,
                                               "SwiftUI Code Quality", Severity.MEDIUM,
                                               "Break down large views, extract subviews, use @ViewBuilder"))

            results.extend(self._check_patterns(file_path, content, self.ios_accessibility_patterns,
                                               "Missing Accessibility", Severity.LOW,
                                               "Add accessibility labels/hints for better accessibility support"))

            results.extend(self._check_patterns(file_path, content, self.ios_naming_patterns,
                                               "Swift Naming Convention", Severity.LOW,
                                               "Follow Swift naming conventions: UpperCamelCase for types, lowerCamelCase for functions/vars"))

            results.extend(self._check_patterns(file_path, content, self.ios_documentation_patterns,
                                               "Missing Documentation", Severity.LOW,
                                               "Add documentation comments (///) for public APIs"))

            results.extend(self._check_patterns(file_path, content, self.ios_error_handling_patterns,
                                               "Poor Error Handling", Severity.MEDIUM,
                                               "Handle specific error cases, don't use empty catch blocks"))

        return results

    def _check_patterns(self, file_path: str, content: str, patterns: List[tuple],
                       title: str, severity: Severity, recommendation: str) -> List[AnalysisResult]:
        """Check content against quality patterns."""
        results = []

        for pattern, description in patterns:
            matches = self.find_pattern(content, pattern, re.MULTILINE)

            for line_num, column, matched_text in matches:
                code_snippet = self.get_lines_context(content, line_num, context_lines=2)

                result = AnalysisResult(
                    file=file_path,
                    line=line_num,
                    column=column,
                    severity=severity,
                    category=Category.QUALITY,
                    title=title,
                    description=description,
                    recommendation=recommendation,
                    code_snippet=code_snippet,
                )
                results.append(result)

        return results

    def _check_magic_numbers(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for magic numbers (excluding common exceptions)."""
        results = []
        lines = content.split('\n')

        for line_num, line in enumerate(lines, 1):
            # Skip comments
            if re.match(r'^\s*[#/]', line):
                continue

            # Find numbers that aren't 0, 1, -1
            for match in re.finditer(r'[^a-zA-Z0-9_]([\d]{2,})[^a-zA-Z0-9_.]', line):
                number = match.group(1)

                # Skip common non-magic numbers
                if number in ('10', '100', '1000', '0', '1', '2', '24', '60'):
                    continue

                # Skip if it looks like a year, port, or HTTP status
                if re.match(r'(19|20)\d{2}|[1-9]\d{3,4}', number):
                    continue

                code_snippet = self.get_lines_context(content, line_num, context_lines=1)

                result = AnalysisResult(
                    file=file_path,
                    line=line_num,
                    column=match.start(),
                    severity=Severity.LOW,
                    category=Category.QUALITY,
                    title="Magic Number",
                    description=f"Magic number '{number}' should be a named constant",
                    recommendation="Define as a named constant with meaningful name",
                    code_snippet=code_snippet,
                )
                results.append(result)

        return results

    def _check_cyclomatic_complexity(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check cyclomatic complexity of functions."""
        results = []
        lines = content.split('\n')

        current_function = None
        function_start = 0
        complexity = 0

        for line_num, line in enumerate(lines, 1):
            # Detect function definition
            func_match = re.match(r'^(\s*)def\s+(\w+)', line)
            if func_match:
                # Analyze previous function
                if current_function and complexity > 10:
                    result = AnalysisResult(
                        file=file_path,
                        line=function_start,
                        severity=Severity.MEDIUM if complexity > 15 else Severity.LOW,
                        category=Category.QUALITY,
                        title="High Cyclomatic Complexity",
                        description=f"Function '{current_function}' has complexity of {complexity}",
                        recommendation="Simplify function by extracting methods or reducing branching",
                        code_snippet=f"Complexity: {complexity}",
                    )
                    results.append(result)

                # Start new function
                current_function = func_match.group(2)
                function_start = line_num
                complexity = 1

            # Count complexity-adding keywords
            if current_function:
                keywords = ['if', 'elif', 'else', 'for', 'while', 'and', 'or', 'except', 'case']
                for keyword in keywords:
                    if re.search(r'\b' + keyword + r'\b', line):
                        complexity += 1

        # Check last function
        if current_function and complexity > 10:
            result = AnalysisResult(
                file=file_path,
                line=function_start,
                severity=Severity.MEDIUM if complexity > 15 else Severity.LOW,
                category=Category.QUALITY,
                title="High Cyclomatic Complexity",
                description=f"Function '{current_function}' has complexity of {complexity}",
                recommendation="Simplify function by extracting methods or reducing branching",
                code_snippet=f"Complexity: {complexity}",
            )
            results.append(result)

        return results

    def _is_code_file(self, file_path: str) -> bool:
        """Check if file is a code file."""
        ext = self.get_file_extension(file_path)
        code_extensions = {'py', 'js', 'ts', 'jsx', 'tsx', 'java', 'rb', 'go', 'php', 'cs', 'cpp', 'c', 'rs', 'kt', 'swift'}
        return ext.lower() in code_extensions
