"""Apple Human Interface Guidelines (HIG) compliance analyzer."""

import re
from typing import List
from .base_analyzer import BaseAnalyzer, AnalysisResult, Severity, Category


class IOSHIGAnalyzer(BaseAnalyzer):
    """Analyzes code for Apple HIG compliance."""

    def __init__(self, io=None, verbose=False):
        super().__init__(io, verbose)

        # Minimum touch target size (44x44 points)
        self.min_touch_target = 44

        # HIG-recommended spacing
        self.standard_spacing = [8, 12, 16, 20, 24, 32]

    def analyze_file(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Analyze a file for HIG compliance."""
        results = []

        # Only analyze Swift files
        if not self.get_file_extension(file_path) == 'swift':
            return results

        # Check various HIG compliance issues
        results.extend(self._check_touch_targets(file_path, content))
        results.extend(self._check_navigation_patterns(file_path, content))
        results.extend(self._check_modal_presentation(file_path, content))
        results.extend(self._check_spacing_values(file_path, content))
        results.extend(self._check_color_usage(file_path, content))
        results.extend(self._check_font_usage(file_path, content))
        results.extend(self._check_alert_patterns(file_path, content))

        return results

    def _check_touch_targets(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for touch targets that are too small."""
        results = []

        # Pattern for frame/size definitions that might be too small
        patterns = [
            r'\.frame\(width:\s*(\d+),\s*height:\s*(\d+)\)',
            r'CGSize\(width:\s*(\d+),\s*height:\s*(\d+)\)',
            r'\.frame\(.*width:\s*(\d+).*height:\s*(\d+)',
        ]

        for pattern in patterns:
            matches = list(re.finditer(pattern, content))

            for match in matches:
                try:
                    width = int(match.group(1))
                    height = int(match.group(2))

                    # Check if this is a Button or interactive element
                    line_num = content[:match.start()].count('\n') + 1
                    line_start = content.rfind('\n', 0, match.start()) + 1
                    line_end = content.find('\n', match.end())
                    if line_end == -1:
                        line_end = len(content)
                    line_context = content[line_start:line_end]

                    # Check if it's an interactive element
                    is_interactive = any(keyword in line_context for keyword in [
                        'Button', 'button', '.onTapGesture', 'UIButton', '.addTarget'
                    ])

                    if is_interactive and (width < self.min_touch_target or height < self.min_touch_target):
                        code_snippet = self.get_lines_context(content, line_num, context_lines=2)

                        result = AnalysisResult(
                            file=file_path,
                            line=line_num,
                            column=match.start(),
                            severity=Severity.MEDIUM,
                            category=Category.QUALITY,
                            title="Touch Target Too Small",
                            description=f"Interactive element has size {width}x{height}, below HIG minimum of 44x44 points",
                            recommendation=f"Increase touch target to at least 44x44 points for better accessibility",
                            code_snippet=code_snippet,
                            references=[
                                "https://developer.apple.com/design/human-interface-guidelines/layout",
                            ],
                        )
                        results.append(result)
                except (ValueError, IndexError):
                    continue

        return results

    def _check_navigation_patterns(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for HIG navigation pattern violations."""
        results = []

        # Check for tabs with more than 5 items
        tab_pattern = r'TabView\s*\{[^}]*\}'
        matches = list(re.finditer(tab_pattern, content, re.DOTALL))

        for match in matches:
            tab_content = match.group(0)
            # Count tab items (approximate)
            tab_count = tab_content.count('.tag(') or tab_content.count('TabItem')

            if tab_count > 5:
                line_num = content[:match.start()].count('\n') + 1
                code_snippet = self.get_lines_context(content, line_num, context_lines=1)

                result = AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=Severity.MEDIUM,
                    category=Category.ARCHITECTURE,
                    title="Too Many Tab Items",
                    description=f"TabView has {tab_count} items, exceeds HIG recommendation of 5",
                    recommendation="Limit tabs to 5 items or use a different navigation pattern",
                    code_snippet=code_snippet,
                    references=[
                        "https://developer.apple.com/design/human-interface-guidelines/tab-bars",
                    ],
                )
                results.append(result)

        return results

    def _check_modal_presentation(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for modal presentation best practices."""
        results = []

        # Check for multiple nested sheets/fullScreenCovers
        sheet_pattern = r'\.sheet\(|\.fullScreenCover\('
        matches = list(re.finditer(sheet_pattern, content))

        # Count modals in the same view
        if len(matches) > 2:
            result = AnalysisResult(
                file=file_path,
                line=1,
                severity=Severity.LOW,
                category=Category.QUALITY,
                title="Multiple Modal Presentations",
                description=f"File has {len(matches)} modal presentation modifiers",
                recommendation="Limit modal presentations and avoid nesting modals per HIG",
                code_snippet="",
                references=[
                    "https://developer.apple.com/design/human-interface-guidelines/modality",
                ],
            )
            results.append(result)

        return results

    def _check_spacing_values(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for non-standard spacing values."""
        results = []

        # Pattern for spacing/padding values
        patterns = [
            r'\.padding\((\d+)\)',
            r'\.spacing\((\d+)\)',
        ]

        for pattern in patterns:
            matches = list(re.finditer(pattern, content))

            for match in matches:
                try:
                    value = int(match.group(1))

                    # Check if it's a non-standard spacing value
                    if value not in self.standard_spacing and value > 0 and value < 50:
                        # Only flag if it's not a multiple of 4 (8-point grid)
                        if value % 4 != 0:
                            line_num = content[:match.start()].count('\n') + 1
                            code_snippet = self.get_lines_context(content, line_num, context_lines=1)

                            result = AnalysisResult(
                                file=file_path,
                                line=line_num,
                                column=match.start(),
                                severity=Severity.LOW,
                                category=Category.QUALITY,
                                title="Non-Standard Spacing",
                                description=f"Spacing value {value} doesn't follow 8-point grid system",
                                recommendation=f"Use multiples of 4 or 8 for consistent spacing (e.g., {(value//4)*4} or {((value+3)//4)*4})",
                                code_snippet=code_snippet,
                            )
                            results.append(result)
                except ValueError:
                    continue

        return results

    def _check_color_usage(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for hardcoded colors that should use semantic colors."""
        results = []

        # Pattern for hardcoded RGB colors
        rgb_pattern = r'Color\(red:\s*[\d.]+,\s*green:\s*[\d.]+,\s*blue:\s*[\d.]+'
        matches = list(re.finditer(rgb_pattern, content))

        if len(matches) > 3:
            result = AnalysisResult(
                file=file_path,
                line=1,
                severity=Severity.LOW,
                category=Category.QUALITY,
                title="Hardcoded Colors",
                description=f"File has {len(matches)} hardcoded RGB colors",
                recommendation="Use semantic colors (Color.primary, .secondary) or asset catalog colors for Dark Mode support",
                code_snippet="",
                references=[
                    "https://developer.apple.com/design/human-interface-guidelines/color",
                ],
            )
            results.append(result)

        # Check for .black and .white instead of semantic colors
        semantic_pattern = r'Color\.(black|white)(?!\s*\.|opacity)'
        matches = list(re.finditer(semantic_pattern, content))

        for match in matches:
            line_num = content[:match.start()].count('\n') + 1
            code_snippet = self.get_lines_context(content, line_num, context_lines=1)

            result = AnalysisResult(
                file=file_path,
                line=line_num,
                column=match.start(),
                severity=Severity.LOW,
                category=Category.QUALITY,
                title="Non-Semantic Color",
                description=f"Using Color.{match.group(1)} instead of semantic color",
                recommendation="Use Color.primary, .secondary, or asset catalog colors for proper Dark Mode support",
                code_snippet=code_snippet,
            )
            results.append(result)

        return results

    def _check_font_usage(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for font usage best practices."""
        results = []

        # Check for hardcoded font sizes
        font_pattern = r'\.font\(\.system\(size:\s*(\d+)'
        matches = list(re.finditer(font_pattern, content))

        for match in matches:
            try:
                size = int(match.group(1))
                line_num = content[:match.start()].count('\n') + 1

                # Suggest using text styles instead
                suggested_style = self._suggest_text_style(size)

                if suggested_style:
                    code_snippet = self.get_lines_context(content, line_num, context_lines=1)

                    result = AnalysisResult(
                        file=file_path,
                        line=line_num,
                        column=match.start(),
                        severity=Severity.LOW,
                        category=Category.QUALITY,
                        title="Hardcoded Font Size",
                        description=f"Using hardcoded font size {size} instead of text style",
                        recommendation=f"Use .font({suggested_style}) for Dynamic Type support",
                        code_snippet=code_snippet,
                        references=[
                            "https://developer.apple.com/design/human-interface-guidelines/typography",
                        ],
                    )
                    results.append(result)
            except ValueError:
                continue

        return results

    def _check_alert_patterns(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for alert and action sheet best practices."""
        results = []

        # Check for alerts with too many actions
        alert_pattern = r'\.alert\([^)]*\)\s*\{[^}]*\}'
        matches = list(re.finditer(alert_pattern, content, re.DOTALL))

        for match in matches:
            alert_content = match.group(0)
            action_count = alert_content.count('Button(')

            if action_count > 3:
                line_num = content[:match.start()].count('\n') + 1
                code_snippet = self.get_lines_context(content, line_num, context_lines=2)

                result = AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=Severity.MEDIUM,
                    category=Category.QUALITY,
                    title="Too Many Alert Actions",
                    description=f"Alert has {action_count} actions, exceeds HIG recommendation",
                    recommendation="Limit alerts to 2-3 actions, use action sheet for more options",
                    code_snippet=code_snippet,
                    references=[
                        "https://developer.apple.com/design/human-interface-guidelines/alerts",
                    ],
                )
                results.append(result)

        return results

    def _suggest_text_style(self, size: int) -> str:
        """Suggest a text style based on font size."""
        # Map font sizes to text styles (approximate)
        if size >= 34:
            return ".largeTitle"
        elif size >= 28:
            return ".title"
        elif size >= 22:
            return ".title2"
        elif size >= 20:
            return ".title3"
        elif size >= 17:
            return ".body"
        elif size >= 15:
            return ".callout"
        elif size >= 13:
            return ".subheadline"
        elif size >= 12:
            return ".footnote"
        elif size >= 11:
            return ".caption"
        else:
            return ".caption2"

    def is_supported_file(self, file_path: str) -> bool:
        """HIG analyzer only supports Swift files."""
        return self.get_file_extension(file_path) == 'swift'
