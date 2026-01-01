"""Architecture analyzer for detecting design and dependency issues."""

import re
from typing import List, Dict, Set
from collections import defaultdict
from .base_analyzer import BaseAnalyzer, AnalysisResult, Severity, Category


class ArchitectureAnalyzer(BaseAnalyzer):
    """Analyzes code architecture, dependencies, and design patterns."""

    def __init__(self, io=None, verbose=False):
        super().__init__(io, verbose)
        self.import_graph: Dict[str, Set[str]] = defaultdict(set)

    def analyze_file(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Analyze a file for architecture issues."""
        results = []

        if not self._is_code_file(file_path):
            return results

        # Track imports for dependency analysis
        imports = self._extract_imports(content)
        self.import_graph[file_path] = imports

        # Check for God Class
        results.extend(self._check_god_class(file_path, content))

        # Check for tight coupling
        results.extend(self._check_tight_coupling(file_path, content, imports))

        # Check for circular dependencies (requires multiple files)
        # This is better done at the report level

        # Check for law of demeter violations
        results.extend(self._check_law_of_demeter(file_path, content))

        # Check for separation of concerns
        results.extend(self._check_separation_of_concerns(file_path, content))

        # Check for dependency injection opportunities
        results.extend(self._check_dependency_injection(file_path, content))

        return results

    def analyze_files(self, files: Dict[str, str]):
        """Override to add circular dependency detection."""
        report = super().analyze_files(files)

        # Detect circular dependencies across all files
        circular_deps = self._find_circular_dependencies()
        for file_path, circular_with in circular_deps:
            result = AnalysisResult(
                file=file_path,
                line=1,
                severity=Severity.HIGH,
                category=Category.ARCHITECTURE,
                title="Circular Dependency",
                description=f"Circular dependency with {circular_with}",
                recommendation="Refactor to remove circular dependencies, consider dependency inversion",
                code_snippet="",
            )
            report.add_result(result)

        return report

    def _extract_imports(self, content: str) -> Set[str]:
        """Extract import statements from content."""
        imports = set()

        # Python imports
        for match in re.finditer(r'^(?:from\s+([\w.]+)|import\s+([\w.]+))', content, re.MULTILINE):
            module = match.group(1) or match.group(2)
            if module:
                imports.add(module.split('.')[0])

        # JavaScript/TypeScript imports
        for match in re.finditer(r'import\s+.*?from\s+["\']([^"\']+)["\']', content):
            module = match.group(1)
            if not module.startswith('.'):
                imports.add(module.split('/')[0])

        # Java imports
        for match in re.finditer(r'import\s+([\w.]+);', content):
            package = match.group(1)
            imports.add(package.split('.')[0])

        return imports

    def _check_god_class(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for God Class anti-pattern."""
        results = []

        # Count methods and lines in classes
        class_pattern = r'class\s+(\w+).*?:'
        matches = list(re.finditer(class_pattern, content))

        for match in matches:
            class_name = match.group(1)
            class_start = match.start()

            # Find class end (next class or end of file)
            next_class = None
            for other_match in matches:
                if other_match.start() > class_start:
                    next_class = other_match.start()
                    break

            if next_class:
                class_content = content[class_start:next_class]
            else:
                class_content = content[class_start:]

            # Count methods
            method_count = len(re.findall(r'def\s+\w+\s*\(', class_content))
            line_count = len(class_content.split('\n'))

            # God class indicators
            if method_count > 20 or line_count > 500:
                line_num = content[:class_start].count('\n') + 1

                result = AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=Severity.MEDIUM,
                    category=Category.ARCHITECTURE,
                    title="God Class",
                    description=f"Class '{class_name}' has {method_count} methods and {line_count} lines",
                    recommendation="Break into smaller, focused classes following Single Responsibility Principle",
                    code_snippet=f"Class {class_name}: {method_count} methods, {line_count} lines",
                )
                results.append(result)

        return results

    def _check_tight_coupling(self, file_path: str, content: str, imports: Set[str]) -> List[AnalysisResult]:
        """Check for tight coupling."""
        results = []

        # Too many imports is a sign of tight coupling
        if len(imports) > 15:
            result = AnalysisResult(
                file=file_path,
                line=1,
                severity=Severity.MEDIUM,
                category=Category.ARCHITECTURE,
                title="High Coupling",
                description=f"File imports {len(imports)} modules",
                recommendation="Reduce dependencies, consider using dependency injection or facade pattern",
                code_snippet="",
            )
            results.append(result)

        # Direct instantiation of concrete classes
        instantiation_pattern = r'\w+\s*=\s*\w+\([^)]*\)'
        matches = self.find_pattern(content, instantiation_pattern)

        if len(matches) > 20:
            result = AnalysisResult(
                file=file_path,
                line=1,
                severity=Severity.LOW,
                category=Category.ARCHITECTURE,
                title="Tight Coupling",
                description=f"Many direct object instantiations ({len(matches)})",
                recommendation="Consider dependency injection and programming to interfaces",
                code_snippet="",
            )
            results.append(result)

        return results

    def _check_law_of_demeter(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for Law of Demeter violations."""
        results = []

        # Look for chains of method calls (object.method().method().method())
        chain_pattern = r'\w+\.(\w+\(\)\.){3,}\w+\(\)'
        matches = self.find_pattern(content, chain_pattern)

        for line_num, column, matched_text in matches:
            code_snippet = self.get_lines_context(content, line_num, context_lines=1)

            result = AnalysisResult(
                file=file_path,
                line=line_num,
                column=column,
                severity=Severity.LOW,
                category=Category.ARCHITECTURE,
                title="Law of Demeter Violation",
                description="Long method chain detected",
                recommendation="Consider adding facade methods or using tell-don't-ask principle",
                code_snippet=code_snippet,
            )
            results.append(result)

        return results

    def _check_separation_of_concerns(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for separation of concerns violations."""
        results = []

        # Check for mixing database logic with business logic
        has_db = bool(re.search(r'(SELECT|INSERT|UPDATE|DELETE|query|execute)', content, re.IGNORECASE))
        has_ui = bool(re.search(r'(render|template|html|print)', content, re.IGNORECASE))
        has_business = bool(re.search(r'(calculate|process|validate|compute)', content, re.IGNORECASE))

        violations = sum([has_db, has_ui, has_business])

        if violations >= 2:
            concerns = []
            if has_db:
                concerns.append("database")
            if has_ui:
                concerns.append("presentation")
            if has_business:
                concerns.append("business logic")

            result = AnalysisResult(
                file=file_path,
                line=1,
                severity=Severity.MEDIUM,
                category=Category.ARCHITECTURE,
                title="Mixed Concerns",
                description=f"File mixes {', '.join(concerns)}",
                recommendation="Separate into layers (data, business, presentation)",
                code_snippet="",
            )
            results.append(result)

        return results

    def _check_dependency_injection(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for hardcoded dependencies that should use DI."""
        results = []

        # Look for hardcoded configuration or service instantiation
        hardcoded_patterns = [
            (r'config\s*=\s*\{[^}]+\}', "Hardcoded configuration"),
            (r'(database|db)\s*=\s*\w+\(["\']', "Hardcoded database connection"),
            (r'api[_-]?url\s*=\s*["\']http', "Hardcoded API URL"),
        ]

        for pattern, description in hardcoded_patterns:
            matches = self.find_pattern(content, pattern, re.IGNORECASE)

            for line_num, column, matched_text in matches:
                code_snippet = self.get_lines_context(content, line_num, context_lines=1)

                result = AnalysisResult(
                    file=file_path,
                    line=line_num,
                    column=column,
                    severity=Severity.LOW,
                    category=Category.ARCHITECTURE,
                    title="Hardcoded Dependency",
                    description=description,
                    recommendation="Use dependency injection or configuration files",
                    code_snippet=code_snippet,
                )
                results.append(result)

        return results

    def _find_circular_dependencies(self) -> List[tuple]:
        """Find circular dependencies in the import graph."""
        circular = []

        def has_path(start: str, end: str, visited: Set[str]) -> bool:
            """Check if there's a path from start to end."""
            if start == end:
                return True
            if start in visited:
                return False

            visited.add(start)

            for neighbor in self.import_graph.get(start, set()):
                if has_path(neighbor, end, visited.copy()):
                    return True

            return False

        # Check each edge for circularity
        for file_a in self.import_graph:
            for file_b in self.import_graph[file_a]:
                if has_path(file_b, file_a, set()):
                    circular.append((file_a, file_b))

        return circular

    def _is_code_file(self, file_path: str) -> bool:
        """Check if file is a code file."""
        ext = self.get_file_extension(file_path)
        code_extensions = {'py', 'js', 'ts', 'jsx', 'tsx', 'java', 'rb', 'go', 'php', 'cs', 'cpp', 'c', 'rs', 'kt', 'swift'}
        return ext.lower() in code_extensions
