"""Swift Package Manager (SPM) dependency analyzer."""

import re
from typing import List, Dict, Set
from .base_analyzer import BaseAnalyzer, AnalysisResult, Severity, Category


class SPMAnalyzer(BaseAnalyzer):
    """Analyzes Swift Package Manager dependencies and configuration."""

    def __init__(self, io=None, verbose=False):
        super().__init__(io, verbose)

        # Known vulnerable/deprecated packages
        self.deprecated_packages = {
            'Alamofire/AlamofireImage': 'Consider using native AsyncImage (iOS 15+)',
            'onevcat/Kingfisher': 'Consider using native AsyncImage (iOS 15+) for simple cases',
            'SwiftyJSON/SwiftyJSON': 'Use native Codable instead',
            'Hearst-DD/ObjectMapper': 'Use native Codable instead',
        }

        # Packages with known security issues (examples)
        self.security_issues = {
            # This would be populated from a vulnerability database
            # Format: 'owner/repo': ('affected_versions', 'issue', 'fix_version')
        }

    def analyze_file(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Analyze Package.swift for dependency issues."""
        results = []

        # Only analyze Package.swift files
        if not file_path.endswith('Package.swift'):
            return results

        results.extend(self._check_package_structure(file_path, content))
        results.extend(self._check_dependencies(file_path, content))
        results.extend(self._check_version_pinning(file_path, content))
        results.extend(self._check_platform_requirements(file_path, content))
        results.extend(self._check_deprecated_packages(file_path, content))

        return results

    def _check_package_structure(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for proper Package.swift structure."""
        results = []

        # Check for swift-tools-version
        if not re.search(r'// swift-tools-version:', content):
            result = AnalysisResult(
                file=file_path,
                line=1,
                severity=Severity.MEDIUM,
                category=Category.QUALITY,
                title="Missing Swift Tools Version",
                description="Package.swift missing // swift-tools-version comment",
                recommendation="Add // swift-tools-version:5.9 (or appropriate version) at the top",
                code_snippet="",
                references=[
                    "https://docs.swift.org/package-manager/PackageDescription/PackageDescription.html",
                ],
            )
            results.append(result)

        # Check for Package name
        if not re.search(r'name:\s*"[^"]+\"', content):
            result = AnalysisResult(
                file=file_path,
                line=1,
                severity=Severity.HIGH,
                category=Category.QUALITY,
                title="Missing Package Name",
                description="Package missing name property",
                recommendation="Add name: \"YourPackageName\" to Package initializer",
                code_snippet="",
            )
            results.append(result)

        return results

    def _check_dependencies(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check dependency declarations."""
        results = []

        # Find dependency declarations
        dep_pattern = r'\.package\s*\(\s*url:\s*"([^"]+)"'
        matches = list(re.finditer(dep_pattern, content))

        # Check for too many dependencies
        if len(matches) > 15:
            result = AnalysisResult(
                file=file_path,
                line=1,
                severity=Severity.LOW,
                category=Category.ARCHITECTURE,
                title="Many Dependencies",
                description=f"Package has {len(matches)} dependencies",
                recommendation="Review if all dependencies are necessary, consider reducing dependency count",
                code_snippet="",
            )
            results.append(result)

        # Check each dependency
        for match in matches:
            url = match.group(1)
            line_num = content[:match.start()].count('\n') + 1

            # Check for HTTP (insecure) URLs
            if url.startswith('http://'):
                code_snippet = self.get_lines_context(content, line_num, context_lines=1)

                result = AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=Severity.HIGH,
                    category=Category.SECURITY,
                    title="Insecure Dependency URL",
                    description="Dependency URL uses HTTP instead of HTTPS",
                    recommendation="Use HTTPS URL for dependency",
                    code_snippet=code_snippet,
                )
                results.append(result)

            # Check for dependencies by exact commit (good) vs branch (risky)
            line_content = content.split('\n')[line_num - 1]
            next_few_lines = '\n'.join(content.split('\n')[line_num:line_num+5])

            # Look for branch-based dependency
            if '.branch(' in next_few_lines:
                code_snippet = self.get_lines_context(content, line_num, context_lines=3)

                result = AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=Severity.MEDIUM,
                    category=Category.QUALITY,
                    title="Branch-Based Dependency",
                    description="Dependency pinned to branch instead of version",
                    recommendation="Use semantic version or exact revision for reproducible builds",
                    code_snippet=code_snippet,
                )
                results.append(result)

        return results

    def _check_version_pinning(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check version pinning strategies."""
        results = []

        # Find version specifications
        version_patterns = [
            (r'\.upToNextMajor\(', "upToNextMajor"),
            (r'\.upToNextMinor\(', "upToNextMinor"),
            (r'from:\s*"([^"]+)"', "from"),
            (r'\.exact\(', "exact"),
        ]

        version_strategies = {}
        for pattern, strategy in version_patterns:
            matches = list(re.finditer(pattern, content))
            if matches:
                version_strategies[strategy] = len(matches)

        # Warn about .from which allows any version >= specified
        if 'from' in version_strategies and version_strategies['from'] > 0:
            result = AnalysisResult(
                file=file_path,
                line=1,
                severity=Severity.LOW,
                category=Category.QUALITY,
                title="Loose Version Constraint",
                description=f"{version_strategies['from']} dependencies use 'from:' (allows major version updates)",
                recommendation="Consider using .upToNextMajor or .upToNextMinor for more controlled updates",
                code_snippet="",
            )
            results.append(result)

        # Suggest exact versions for production
        if 'exact' not in version_strategies or version_strategies.get('exact', 0) == 0:
            # Only suggest if there are dependencies
            if any(version_strategies.values()):
                result = AnalysisResult(
                    file=file_path,
                    line=1,
                    severity=Severity.LOW,
                    category=Category.QUALITY,
                    title="No Exact Version Pinning",
                    description="No dependencies use exact version pinning",
                    recommendation="Consider .exact() for critical dependencies in production apps",
                    code_snippet="",
                )
                results.append(result)

        return results

    def _check_platform_requirements(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check platform version requirements."""
        results = []

        # Find platform declarations
        platform_pattern = r'\.iOS\(\.v(\d+)\)'
        matches = list(re.finditer(platform_pattern, content))

        for match in matches:
            version = int(match.group(1))
            line_num = content[:match.start()].count('\n') + 1

            # Warn if iOS version is very old
            if version < 14:
                code_snippet = self.get_lines_context(content, line_num, context_lines=1)

                result = AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=Severity.MEDIUM,
                    category=Category.QUALITY,
                    title="Old iOS Platform Requirement",
                    description=f"Package targets iOS {version}",
                    recommendation=f"Consider updating to iOS 14+ to drop legacy code",
                    code_snippet=code_snippet,
                )
                results.append(result)

            # Suggest iOS 15+ for modern features
            if version < 15:
                result = AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=Severity.LOW,
                    category=Category.QUALITY,
                    title="Consider iOS 15+",
                    description=f"Package targets iOS {version}",
                    recommendation="iOS 15+ enables modern Swift Concurrency and SwiftUI features",
                    code_snippet=code_snippet,
                )
                results.append(result)

        return results

    def _check_deprecated_packages(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for deprecated or unnecessary packages."""
        results = []

        for package_name, suggestion in self.deprecated_packages.items():
            if package_name in content:
                # Find the line
                pattern = re.escape(package_name)
                matches = self.find_pattern(content, pattern)

                for line_num, column, matched_text in matches:
                    code_snippet = self.get_lines_context(content, line_num, context_lines=2)

                    result = AnalysisResult(
                        file=file_path,
                        line=line_num,
                        severity=Severity.LOW,
                        category=Category.ARCHITECTURE,
                        title="Consider Native Alternative",
                        description=f"Package '{package_name}' has native alternatives",
                        recommendation=suggestion,
                        code_snippet=code_snippet,
                    )
                    results.append(result)

        return results

    def is_supported_file(self, file_path: str) -> bool:
        """SPM analyzer only supports Package.swift files."""
        return file_path.endswith('Package.swift')
