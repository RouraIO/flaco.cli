"""SwiftUI best practices and pattern analyzer."""

import re
from typing import List
from .base_analyzer import BaseAnalyzer, AnalysisResult, Severity, Category


class SwiftUIAnalyzer(BaseAnalyzer):
    """Analyzes SwiftUI code for best practices and common patterns."""

    def __init__(self, io=None, verbose=False):
        super().__init__(io, verbose)

        # SwiftUI anti-patterns
        self.anti_patterns = {
            'onAppear': 'Heavy operations in onAppear',
            'GeometryReader': 'Overuse of GeometryReader',
            'AnyView': 'Type-erased AnyView (performance cost)',
            '@State.*class': 'Using @State with reference types',
            '@ObservedObject.*struct': 'Using @ObservedObject with value types',
        }

    def analyze_file(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Analyze SwiftUI code for best practices."""
        results = []

        # Only analyze Swift files
        if not self.get_file_extension(file_path) == 'swift':
            return results

        # Check if file contains SwiftUI code
        if not self._is_swiftui_file(content):
            return results

        results.extend(self._check_view_body_size(file_path, content))
        results.extend(self._check_state_management(file_path, content))
        results.extend(self._check_view_builder_usage(file_path, content))
        results.extend(self._check_preview_usage(file_path, content))
        results.extend(self._check_geometry_reader_overuse(file_path, content))
        results.extend(self._check_anyview_usage(file_path, content))
        results.extend(self._check_onappear_usage(file_path, content))
        results.extend(self._check_observable_patterns(file_path, content))
        results.extend(self._check_environment_usage(file_path, content))
        results.extend(self._check_binding_patterns(file_path, content))

        return results

    def _is_swiftui_file(self, content: str) -> bool:
        """Check if file uses SwiftUI."""
        return 'import SwiftUI' in content or ': View' in content

    def _check_view_body_size(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for overly large View body implementations."""
        results = []

        # Find View bodies
        view_pattern = r'var\s+body:\s*some\s+View\s*\{'
        matches = list(re.finditer(view_pattern, content))

        for match in matches:
            # Find the closing brace
            start = match.end()
            brace_count = 1
            pos = start

            while pos < len(content) and brace_count > 0:
                if content[pos] == '{':
                    brace_count += 1
                elif content[pos] == '}':
                    brace_count -= 1
                pos += 1

            body_content = content[start:pos-1]
            line_count = body_content.count('\n')

            # Flag if body is too large
            if line_count > 50:
                line_num = content[:match.start()].count('\n') + 1
                code_snippet = self.get_lines_context(content, line_num, context_lines=2)

                result = AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=Severity.MEDIUM,
                    category=Category.QUALITY,
                    title="Large SwiftUI View Body",
                    description=f"View body has {line_count} lines",
                    recommendation="Extract subviews using @ViewBuilder or computed properties",
                    code_snippet=code_snippet,
                    references=[
                        "https://developer.apple.com/documentation/swiftui/viewbuilder",
                    ],
                )
                results.append(result)

        return results

    def _check_state_management(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for state management issues."""
        results = []

        # Check for @State with classes
        state_class_pattern = r'@State.*(?:var|let)\s+\w+:\s*\w+(?:\?|\!)?(?:\s*=\s*\w+\()'
        matches = list(re.finditer(state_class_pattern, content))

        for match in matches:
            line_num = content[:match.start()].count('\n') + 1
            line_content = content.split('\n')[line_num - 1]

            # Check if it's likely a class (starts with uppercase)
            type_match = re.search(r':\s*([A-Z]\w+)', line_content)
            if type_match and '(' in line_content:
                code_snippet = self.get_lines_context(content, line_num, context_lines=1)

                result = AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=Severity.MEDIUM,
                    category=Category.QUALITY,
                    title="@State with Reference Type",
                    description="Using @State with a class instance",
                    recommendation="Use @StateObject for classes, @State for value types only",
                    code_snippet=code_snippet,
                )
                results.append(result)

        # Check for multiple @State properties (suggest ViewModel)
        state_count = len(re.findall(r'@State\s+(?:private\s+)?var', content))
        if state_count > 5:
            result = AnalysisResult(
                file=file_path,
                line=1,
                severity=Severity.LOW,
                category=Category.ARCHITECTURE,
                title="Many @State Properties",
                description=f"View has {state_count} @State properties",
                recommendation="Consider using @StateObject with a ViewModel for complex state",
                code_snippet="",
            )
            results.append(result)

        return results

    def _check_view_builder_usage(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for missing @ViewBuilder usage."""
        results = []

        # Find functions returning 'some View' without @ViewBuilder
        func_pattern = r'func\s+(\w+)\([^)]*\)\s*->\s*some\s+View\s*\{'
        matches = list(re.finditer(func_pattern, content))

        for match in matches:
            func_name = match.group(1)
            line_num = content[:match.start()].count('\n') + 1

            # Check if @ViewBuilder is present before the function
            preceding_lines = content[:match.start()].split('\n')[-3:]
            has_viewbuilder = any('@ViewBuilder' in line for line in preceding_lines)

            if not has_viewbuilder:
                # Check if function body has conditionals (if/switch)
                start = match.end()
                brace_count = 1
                pos = start

                while pos < len(content) and brace_count > 0:
                    if content[pos] == '{':
                        brace_count += 1
                    elif content[pos] == '}':
                        brace_count -= 1
                    pos += 1

                func_body = content[start:pos-1]

                # If it has conditionals, suggest @ViewBuilder
                if re.search(r'\bif\s+|\bswitch\s+', func_body):
                    code_snippet = self.get_lines_context(content, line_num, context_lines=2)

                    result = AnalysisResult(
                        file=file_path,
                        line=line_num,
                        severity=Severity.LOW,
                        category=Category.QUALITY,
                        title="Missing @ViewBuilder",
                        description=f"Function '{func_name}' returns some View with conditionals",
                        recommendation="Add @ViewBuilder attribute for cleaner syntax",
                        code_snippet=code_snippet,
                    )
                    results.append(result)

        return results

    def _check_preview_usage(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for missing or improper #Preview usage."""
        results = []

        # Check if file has Views but no Preview
        has_views = bool(re.search(r'struct\s+\w+:\s*View', content))
        has_preview = bool(re.search(r'#Preview|struct.*_Previews:\s*PreviewProvider', content))

        if has_views and not has_preview:
            result = AnalysisResult(
                file=file_path,
                line=1,
                severity=Severity.LOW,
                category=Category.QUALITY,
                title="Missing SwiftUI Preview",
                description="View has no #Preview for development",
                recommendation="Add #Preview { YourView() } for faster iteration",
                code_snippet="",
                references=[
                    "https://developer.apple.com/documentation/swiftui/previews-in-xcode",
                ],
            )
            results.append(result)

        # Check for old PreviewProvider syntax
        old_preview_pattern = r'struct\s+(\w+)_Previews:\s*PreviewProvider'
        matches = list(re.finditer(old_preview_pattern, content))

        for match in matches:
            line_num = content[:match.start()].count('\n') + 1
            code_snippet = self.get_lines_context(content, line_num, context_lines=1)

            result = AnalysisResult(
                file=file_path,
                line=line_num,
                severity=Severity.LOW,
                category=Category.QUALITY,
                title="Old Preview Syntax",
                description="Using PreviewProvider instead of #Preview macro",
                recommendation="Use #Preview { YourView() } for cleaner syntax (iOS 17+)",
                code_snippet=code_snippet,
            )
            results.append(result)

        return results

    def _check_geometry_reader_overuse(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for GeometryReader overuse."""
        results = []

        geometry_count = len(re.findall(r'GeometryReader', content))

        if geometry_count > 2:
            result = AnalysisResult(
                file=file_path,
                line=1,
                severity=Severity.LOW,
                category=Category.QUALITY,
                title="GeometryReader Overuse",
                description=f"File uses GeometryReader {geometry_count} times",
                recommendation="Consider using layout system (.frame, .padding) or custom layouts instead",
                code_snippet="",
            )
            results.append(result)

        return results

    def _check_anyview_usage(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for AnyView usage (type erasure has performance cost)."""
        results = []

        anyview_pattern = r'AnyView\('
        matches = list(re.finditer(anyview_pattern, content))

        for match in matches:
            line_num = content[:match.start()].count('\n') + 1
            code_snippet = self.get_lines_context(content, line_num, context_lines=1)

            result = AnalysisResult(
                file=file_path,
                line=line_num,
                severity=Severity.LOW,
                category=Category.PERFORMANCE,
                title="AnyView Type Erasure",
                description="Using AnyView has performance overhead",
                recommendation="Use @ViewBuilder or Group instead of type erasure when possible",
                code_snippet=code_snippet,
            )
            results.append(result)

        return results

    def _check_onappear_usage(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for onAppear with heavy operations."""
        results = []

        onappear_pattern = r'\.onAppear\s*\{'
        matches = list(re.finditer(onappear_pattern, content))

        for match in matches:
            # Get the onAppear block
            start = match.end()
            brace_count = 1
            pos = start

            while pos < len(content) and brace_count > 0:
                if content[pos] == '{':
                    brace_count += 1
                elif content[pos] == '}':
                    brace_count -= 1
                pos += 1

            onappear_content = content[start:pos-1]

            # Check for heavy operations
            heavy_ops = [
                ('URLSession', 'Network requests'),
                ('fetch', 'Data fetching'),
                ('try Data(contentsOf:', 'File I/O'),
                ('for.*in.*0\.\.', 'Loops'),
            ]

            for pattern, description in heavy_ops:
                if re.search(pattern, onappear_content):
                    line_num = content[:match.start()].count('\n') + 1
                    code_snippet = self.get_lines_context(content, line_num, context_lines=2)

                    result = AnalysisResult(
                        file=file_path,
                        line=line_num,
                        severity=Severity.MEDIUM,
                        category=Category.PERFORMANCE,
                        title="Heavy Operation in onAppear",
                        description=f"{description} in onAppear can block UI",
                        recommendation="Use .task { } modifier or move to ViewModel initialization",
                        code_snippet=code_snippet,
                    )
                    results.append(result)
                    break  # Only report once per onAppear

        return results

    def _check_observable_patterns(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for Observable macro usage (iOS 17+)."""
        results = []

        # Check for ObservableObject when @Observable is available
        observable_object_pattern = r'class\s+(\w+):\s*ObservableObject'
        matches = list(re.finditer(observable_object_pattern, content))

        for match in matches:
            class_name = match.group(1)
            line_num = content[:match.start()].count('\n') + 1
            code_snippet = self.get_lines_context(content, line_num, context_lines=1)

            result = AnalysisResult(
                file=file_path,
                line=line_num,
                severity=Severity.LOW,
                category=Category.QUALITY,
                title="Consider @Observable Macro",
                description=f"Class '{class_name}' uses ObservableObject",
                recommendation="Consider using @Observable macro for cleaner syntax (iOS 17+)",
                code_snippet=code_snippet,
            )
            results.append(result)

        return results

    def _check_environment_usage(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for environment object usage."""
        results = []

        # Check for @EnvironmentObject without providing it
        env_obj_pattern = r'@EnvironmentObject\s+var\s+(\w+):\s+(\w+)'
        matches = list(re.finditer(env_obj_pattern, content))

        if matches:
            # Check if .environmentObject is used in Preview
            has_env_in_preview = bool(re.search(r'\.environmentObject\(', content))

            if not has_env_in_preview:
                line_num = content[:matches[0].start()].count('\n') + 1
                result = AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=Severity.LOW,
                    category=Category.QUALITY,
                    title="@EnvironmentObject Without Preview",
                    description="View uses @EnvironmentObject but Preview may crash",
                    recommendation="Add .environmentObject() to #Preview to avoid crashes",
                    code_snippet="",
                )
                results.append(result)

        return results

    def _check_binding_patterns(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for Binding usage patterns."""
        results = []

        # Check for constant Bindings (.constant)
        constant_binding_pattern = r'\.constant\('
        matches = list(re.finditer(constant_binding_pattern, content))

        # Only flag if used outside of Previews
        for match in matches:
            line_num = content[:match.start()].count('\n') + 1

            # Check if we're in a Preview
            lines_before = content[:match.start()].split('\n')
            in_preview = any('#Preview' in line or '_Previews' in line for line in lines_before[-10:])

            if not in_preview:
                code_snippet = self.get_lines_context(content, line_num, context_lines=1)

                result = AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=Severity.LOW,
                    category=Category.QUALITY,
                    title="Constant Binding Outside Preview",
                    description="Using .constant() Binding in production code",
                    recommendation=".constant() is meant for previews, use actual Bindings in production",
                    code_snippet=code_snippet,
                )
                results.append(result)

        return results

    def is_supported_file(self, file_path: str) -> bool:
        """SwiftUI analyzer only supports Swift files."""
        return self.get_file_extension(file_path) == 'swift'
