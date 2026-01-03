"""iOS version and API availability analyzer."""

import re
from typing import List, Dict, Set
from .base_analyzer import BaseAnalyzer, AnalysisResult, Severity, Category


class IOSVersionAnalyzer(BaseAnalyzer):
    """Analyzes code for iOS version compatibility and deprecated APIs."""

    def __init__(self, io=None, verbose=False):
        super().__init__(io, verbose)

        # Deprecated iOS APIs (common ones)
        self.deprecated_apis = {
            'UIAlertView': ('iOS 9.0', 'Use UIAlertController'),
            'UIActionSheet': ('iOS 9.0', 'Use UIAlertController with actionSheet style'),
            'UIWebView': ('iOS 12.0', 'Use WKWebView'),
            'UISearchDisplayController': ('iOS 8.0', 'Use UISearchController'),
            'MPMoviePlayerController': ('iOS 9.0', 'Use AVPlayerViewController'),
            'UIPageControl.currentPageIndicatorTintColor': ('iOS 14.0', 'Use UIPageControl.currentPage'),
            'UIApplication.openURL': ('iOS 10.0', 'Use UIApplication.open(_:options:completionHandler:)'),
            'UIApplication.statusBarStyle': ('iOS 13.0', 'Use UIStatusBarStyle'),
        }

        # iOS version requirements for APIs
        self.api_versions = {
            'async': ('iOS 13.0', 'Swift Concurrency'),
            'await': ('iOS 13.0', 'Swift Concurrency'),
            '@MainActor': ('iOS 13.0', 'Swift Concurrency'),
            'AsyncStream': ('iOS 13.0', 'Swift Concurrency'),
            'Task': ('iOS 13.0', 'Swift Concurrency'),
            '.task': ('iOS 15.0', 'SwiftUI task modifier'),
            '.refreshable': ('iOS 15.0', 'SwiftUI pull-to-refresh'),
            '.searchable': ('iOS 15.0', 'SwiftUI search'),
            '.confirmationDialog': ('iOS 15.0', 'SwiftUI confirmation dialog'),
            '.badge': ('iOS 15.0', 'SwiftUI badge modifier'),
            '@Observable': ('iOS 17.0', 'Observable macro'),
            '#Preview': ('iOS 17.0', 'Preview macro'),
            '.scrollContentBackground': ('iOS 16.0', 'SwiftUI scroll background'),
            '.scrollIndicators': ('iOS 16.0', 'SwiftUI scroll indicators'),
            '.symbolEffect': ('iOS 17.0', 'SF Symbol animations'),
            '.symbolVariant': ('iOS 15.0', 'SF Symbol variants'),
            'NavigationStack': ('iOS 16.0', 'NavigationStack'),
            'NavigationSplitView': ('iOS 16.0', 'NavigationSplitView'),
            '.sheet(item:': ('iOS 13.0', 'Sheet with item'),
            '.toolbar': ('iOS 14.0', 'SwiftUI toolbar'),
            '.swipeActions': ('iOS 15.0', 'SwiftUI swipe actions'),
        }

    def analyze_file(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Analyze file for iOS version compatibility issues."""
        results = []

        # Only analyze Swift and Objective-C files
        ext = self.get_file_extension(file_path)
        if ext not in ('swift', 'm', 'mm'):
            return results

        results.extend(self._check_deprecated_apis(file_path, content))
        results.extend(self._check_version_requirements(file_path, content))
        results.extend(self._check_availability_annotations(file_path, content))
        results.extend(self._check_deployment_target(file_path, content))

        return results

    def _check_deprecated_apis(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for usage of deprecated APIs."""
        results = []

        for api, (deprecated_in, replacement) in self.deprecated_apis.items():
            # Escape special regex characters
            escaped_api = re.escape(api)
            pattern = r'\b' + escaped_api + r'\b'

            matches = self.find_pattern(content, pattern)

            for line_num, column, matched_text in matches:
                # Skip if it's in a comment
                line = content.split('\n')[line_num - 1]
                if '//' in line and line.index('//') < column:
                    continue

                code_snippet = self.get_lines_context(content, line_num, context_lines=2)

                result = AnalysisResult(
                    file=file_path,
                    line=line_num,
                    column=column,
                    severity=Severity.HIGH,
                    category=Category.QUALITY,
                    title="Deprecated iOS API",
                    description=f"{api} deprecated in {deprecated_in}",
                    recommendation=replacement,
                    code_snippet=code_snippet,
                    references=[
                        "https://developer.apple.com/documentation/",
                    ],
                )
                results.append(result)

        return results

    def _check_version_requirements(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for APIs that require specific iOS versions."""
        results = []

        # Track which APIs are used
        apis_found: Dict[str, List[int]] = {}

        for api, (required_version, description) in self.api_versions.items():
            escaped_api = re.escape(api)
            matches = self.find_pattern(content, escaped_api)

            if matches:
                apis_found[api] = [match[0] for match in matches]  # Store line numbers

        # Only report if there are version-specific APIs
        if apis_found:
            # Check if there's an @available annotation
            has_availability_check = bool(re.search(r'@available\(iOS', content))

            for api, line_nums in apis_found.items():
                required_version, description = self.api_versions[api]

                for line_num in line_nums[:3]:  # Limit to 3 per API
                    # Check if this specific usage has an availability check nearby
                    context_lines = content.split('\n')[max(0, line_num-5):line_num]
                    has_local_check = any('@available' in line or '#available' in line
                                         for line in context_lines)

                    if not has_local_check:
                        code_snippet = self.get_lines_context(content, line_num, context_lines=2)

                        result = AnalysisResult(
                            file=file_path,
                            line=line_num,
                            severity=Severity.MEDIUM,
                            category=Category.QUALITY,
                            title="iOS Version Requirement",
                            description=f"{description} requires {required_version}",
                            recommendation=f"Add @available(iOS {required_version.split()[1]}, *) or ensure deployment target >= {required_version}",
                            code_snippet=code_snippet,
                        )
                        results.append(result)

        return results

    def _check_availability_annotations(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for proper @available usage."""
        results = []

        # Find @available annotations
        available_pattern = r'@available\((.*?)\)'
        matches = list(re.finditer(available_pattern, content))

        for match in matches:
            availability_text = match.group(1)
            line_num = content[:match.start()].count('\n') + 1

            # Check for common mistakes
            issues = []

            # Missing platform
            if not any(platform in availability_text for platform in ['iOS', 'macOS', 'watchOS', 'tvOS', '*']):
                issues.append("Missing platform specifier")

            # Using 'deprecated' without message
            if 'deprecated' in availability_text and 'message' not in availability_text:
                issues.append("Deprecation without message")

            # Obsoleted without renamed
            if 'obsoleted' in availability_text and 'renamed' not in availability_text:
                issues.append("Consider adding 'renamed:' for obsoleted APIs")

            if issues:
                code_snippet = self.get_lines_context(content, line_num, context_lines=1)

                result = AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=Severity.LOW,
                    category=Category.QUALITY,
                    title="Availability Annotation Issue",
                    description=", ".join(issues),
                    recommendation="Improve @available annotation with platform and deprecation details",
                    code_snippet=code_snippet,
                )
                results.append(result)

        return results

    def _check_deployment_target(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check deployment target settings in project files."""
        results = []

        # Only check .pbxproj files
        if not file_path.endswith('.pbxproj'):
            return results

        # Find IPHONEOS_DEPLOYMENT_TARGET
        deployment_pattern = r'IPHONEOS_DEPLOYMENT_TARGET\s*=\s*([0-9.]+)'
        matches = list(re.finditer(deployment_pattern, content))

        for match in matches:
            version = match.group(1)
            line_num = content[:match.start()].count('\n') + 1

            # Parse version
            try:
                major, minor = map(int, version.split('.')[:2])

                # Warn if deployment target is very old
                if major < 14:
                    code_snippet = self.get_lines_context(content, line_num, context_lines=1)

                    result = AnalysisResult(
                        file=file_path,
                        line=line_num,
                        severity=Severity.MEDIUM,
                        category=Category.QUALITY,
                        title="Old iOS Deployment Target",
                        description=f"Deployment target is iOS {version}",
                        recommendation=f"Consider updating to iOS 14.0+ to drop legacy code and reduce binary size",
                        code_snippet=code_snippet,
                    )
                    results.append(result)

                # Suggest updating to iOS 15+ for modern SwiftUI
                if major < 15:
                    result = AnalysisResult(
                        file=file_path,
                        line=line_num,
                        severity=Severity.LOW,
                        category=Category.QUALITY,
                        title="Consider iOS 15+ Deployment Target",
                        description=f"Deployment target is iOS {version}",
                        recommendation="iOS 15+ enables modern SwiftUI features (.refreshable, .searchable, AsyncImage)",
                        code_snippet=code_snippet,
                    )
                    results.append(result)
            except ValueError:
                continue

        return results

    def is_supported_file(self, file_path: str) -> bool:
        """Version analyzer supports Swift, Objective-C, and project files."""
        ext = self.get_file_extension(file_path)
        return ext in ('swift', 'm', 'mm') or file_path.endswith('.pbxproj')
