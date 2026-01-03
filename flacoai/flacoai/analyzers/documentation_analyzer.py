"""Documentation coverage and quality analyzer."""

import re
from typing import List, Dict, Set
from .base_analyzer import BaseAnalyzer, AnalysisResult, Severity, Category


class DocumentationAnalyzer(BaseAnalyzer):
    """Analyzes code for documentation coverage and quality."""

    def __init__(self, io=None, verbose=False):
        super().__init__(io, verbose)

        # Documentation patterns for different languages
        self.doc_patterns = {
            'swift': {
                'single': r'///',
                'multi_start': r'/\*\*',
                'multi_end': r'\*/',
            },
            'python': {
                'single': r'#',
                'docstring': r'"""',
            },
            'js': {
                'single': r'//',
                'multi_start': r'/\*\*',
                'multi_end': r'\*/',
            },
        }

    def analyze_file(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Analyze file for documentation coverage."""
        results = []

        ext = self.get_file_extension(file_path)

        if ext == 'swift':
            results.extend(self._analyze_swift_docs(file_path, content))
        elif ext == 'py':
            results.extend(self._analyze_python_docs(file_path, content))
        elif ext in ('js', 'ts'):
            results.extend(self._analyze_js_docs(file_path, content))

        return results

    def _analyze_swift_docs(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Analyze Swift documentation."""
        results = []

        # Find public/open declarations
        public_declarations = [
            (r'(public|open)\s+class\s+(\w+)', 'class'),
            (r'(public|open)\s+struct\s+(\w+)', 'struct'),
            (r'(public|open)\s+enum\s+(\w+)', 'enum'),
            (r'(public|open)\s+protocol\s+(\w+)', 'protocol'),
            (r'(public|open)\s+func\s+(\w+)', 'function'),
            (r'(public|open)\s+var\s+(\w+)', 'property'),
            (r'(public|open)\s+let\s+(\w+)', 'constant'),
        ]

        for pattern, decl_type in public_declarations:
            matches = list(re.finditer(pattern, content))

            for match in matches:
                name = match.group(2)
                line_num = content[:match.start()].count('\n') + 1

                # Check if documented
                has_doc = self._has_swift_documentation(content, match.start())

                if not has_doc:
                    code_snippet = self.get_lines_context(content, line_num, context_lines=2)

                    result = AnalysisResult(
                        file=file_path,
                        line=line_num,
                        severity=Severity.MEDIUM,
                        category=Category.QUALITY,
                        title=f"Missing Documentation for Public {decl_type.title()}",
                        description=f"Public {decl_type} '{name}' lacks documentation comments",
                        recommendation=f"Add /// documentation comment describing the {decl_type}'s purpose and usage",
                        code_snippet=code_snippet,
                        references=[
                            "https://developer.apple.com/documentation/xcode/writing-symbol-documentation-in-your-source-files",
                        ],
                    )
                    results.append(result)

        # Check for TODO/FIXME without description
        results.extend(self._check_todos(file_path, content))

        # Check documentation quality
        results.extend(self._check_doc_quality_swift(file_path, content))

        return results

    def _has_swift_documentation(self, content: str, declaration_pos: int) -> bool:
        """Check if Swift declaration has documentation."""
        # Look backwards for /// comments or /** */ blocks
        lines_before = content[:declaration_pos].split('\n')

        # Check last few lines
        for line in reversed(lines_before[-5:]):
            stripped = line.strip()
            if stripped.startswith('///'):
                return True
            if '/**' in stripped:
                return True
            # Stop if we hit code
            if stripped and not stripped.startswith('//') and not stripped.startswith('@'):
                break

        return False

    def _analyze_python_docs(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Analyze Python documentation."""
        results = []

        # Find function/class definitions
        patterns = [
            (r'def\s+(\w+)\s*\(', 'function'),
            (r'class\s+(\w+)', 'class'),
        ]

        for pattern, decl_type in patterns:
            matches = list(re.finditer(pattern, content))

            for match in matches:
                name = match.group(1)

                # Skip private (starting with _)
                if name.startswith('_') and not name.startswith('__'):
                    continue

                line_num = content[:match.start()].count('\n') + 1

                # Check for docstring
                has_doc = self._has_python_docstring(content, match.end())

                if not has_doc:
                    code_snippet = self.get_lines_context(content, line_num, context_lines=2)

                    result = AnalysisResult(
                        file=file_path,
                        line=line_num,
                        severity=Severity.LOW,
                        category=Category.QUALITY,
                        title=f"Missing Docstring for {decl_type.title()}",
                        description=f"{decl_type.title()} '{name}' lacks docstring",
                        recommendation=f"Add docstring explaining the {decl_type}'s purpose, parameters, and return value",
                        code_snippet=code_snippet,
                    )
                    results.append(result)

        results.extend(self._check_todos(file_path, content))

        return results

    def _has_python_docstring(self, content: str, after_pos: int) -> bool:
        """Check if Python declaration has docstring."""
        # Find the next non-whitespace content after declaration
        remaining = content[after_pos:after_pos+200]  # Check next 200 chars

        # Look for """ or '''
        if '"""' in remaining or "'''" in remaining:
            return True

        return False

    def _analyze_js_docs(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Analyze JavaScript/TypeScript documentation."""
        results = []

        # Find exported functions/classes
        patterns = [
            (r'export\s+function\s+(\w+)', 'function'),
            (r'export\s+class\s+(\w+)', 'class'),
            (r'export\s+const\s+(\w+)\s*=', 'constant'),
        ]

        for pattern, decl_type in patterns:
            matches = list(re.finditer(pattern, content))

            for match in matches:
                name = match.group(1)
                line_num = content[:match.start()].count('\n') + 1

                # Check for JSDoc
                has_doc = self._has_jsdoc(content, match.start())

                if not has_doc:
                    code_snippet = self.get_lines_context(content, line_num, context_lines=2)

                    result = AnalysisResult(
                        file=file_path,
                        line=line_num,
                        severity=Severity.LOW,
                        category=Category.QUALITY,
                        title=f"Missing JSDoc for Exported {decl_type.title()}",
                        description=f"Exported {decl_type} '{name}' lacks JSDoc comment",
                        recommendation=f"Add JSDoc comment with @param and @returns tags",
                        code_snippet=code_snippet,
                    )
                    results.append(result)

        results.extend(self._check_todos(file_path, content))

        return results

    def _has_jsdoc(self, content: str, declaration_pos: int) -> bool:
        """Check if declaration has JSDoc."""
        lines_before = content[:declaration_pos].split('\n')

        for line in reversed(lines_before[-5:]):
            stripped = line.strip()
            if '/**' in stripped:
                return True
            if stripped and not stripped.startswith('//') and not stripped.startswith('*'):
                break

        return False

    def _check_todos(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for TODO/FIXME comments."""
        results = []

        todo_patterns = [
            (r'//\s*TODO:', 'TODO'),
            (r'//\s*FIXME:', 'FIXME'),
            (r'//\s*HACK:', 'HACK'),
            (r'//\s*XXX:', 'XXX'),
            (r'#\s*TODO:', 'TODO'),
            (r'#\s*FIXME:', 'FIXME'),
        ]

        for pattern, marker_type in todo_patterns:
            matches = list(re.finditer(pattern, content, re.IGNORECASE))

            for match in matches:
                line_num = content[:match.start()].count('\n') + 1
                line = content.split('\n')[line_num - 1]

                # Check if it has a description after the marker
                after_marker = line[match.end():].strip()

                if not after_marker or len(after_marker) < 10:
                    code_snippet = self.get_lines_context(content, line_num, context_lines=1)

                    result = AnalysisResult(
                        file=file_path,
                        line=line_num,
                        severity=Severity.LOW,
                        category=Category.QUALITY,
                        title=f"Incomplete {marker_type} Comment",
                        description=f"{marker_type} comment lacks detailed description",
                        recommendation=f"Add description explaining what needs to be done and why",
                        code_snippet=code_snippet,
                    )
                    results.append(result)

        return results

    def _check_doc_quality_swift(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check quality of existing Swift documentation."""
        results = []

        # Find documentation comments
        doc_pattern = r'///\s*(.+?)$'
        matches = list(re.finditer(doc_pattern, content, re.MULTILINE))

        for match in matches:
            doc_text = match.group(1).strip()
            line_num = content[:match.start()].count('\n') + 1

            # Check for too short docs
            if len(doc_text) < 15 and not doc_text.startswith('-'):
                code_snippet = self.get_lines_context(content, line_num, context_lines=1)

                result = AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=Severity.LOW,
                    category=Category.QUALITY,
                    title="Brief Documentation Comment",
                    description="Documentation comment is very brief",
                    recommendation="Expand documentation with more details about purpose, parameters, and usage",
                    code_snippet=code_snippet,
                )
                results.append(result)

            # Check for generic docs
            generic_phrases = ['this', 'returns a', 'gets the', 'sets the']
            if any(phrase in doc_text.lower() for phrase in generic_phrases):
                if len(doc_text) < 30:
                    code_snippet = self.get_lines_context(content, line_num, context_lines=1)

                    result = AnalysisResult(
                        file=file_path,
                        line=line_num,
                        severity=Severity.LOW,
                        category=Category.QUALITY,
                        title="Generic Documentation",
                        description="Documentation is generic and uninformative",
                        recommendation="Add specific details about behavior, edge cases, and usage examples",
                        code_snippet=code_snippet,
                    )
                    results.append(result)

        return results

    def is_supported_file(self, file_path: str) -> bool:
        """Documentation analyzer supports code files."""
        ext = self.get_file_extension(file_path)
        return ext in ('swift', 'py', 'js', 'ts', 'jsx', 'tsx', 'm', 'mm', 'h')
