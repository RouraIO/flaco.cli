"""SF Symbols analyzer for validating iOS icon usage."""

import re
from typing import List
from .base_analyzer import BaseAnalyzer, AnalysisResult, Severity, Category


class IOSSymbolsAnalyzer(BaseAnalyzer):
    """Analyzes SF Symbols usage in iOS code."""

    def __init__(self, io=None, verbose=False):
        super().__init__(io, verbose)

        # Common deprecated SF Symbols (examples)
        self.deprecated_symbols = {
            'folder.fill.badge.plus': 'Use folder.badge.plus instead',
            'arrow.clockwise.circle': 'Use arrow.clockwise.circle.fill for better visibility',
            'doc.text.fill': 'Use doc.fill for consistency',
        }

        # Common SF Symbol naming mistakes
        self.common_mistakes = {
            'home': 'house',
            'menu': 'line.horizontal.3',
            'settings': 'gearshape',
            'trash': 'trash.fill',
            'delete': 'trash or xmark',
            'close': 'xmark',
            'back': 'chevron.left',
            'forward': 'chevron.right',
            'save': 'square.and.arrow.down',
            'share': 'square.and.arrow.up',
            'edit': 'pencil',
            'search': 'magnifyingglass',
            'filter': 'line.horizontal.3.decrease.circle',
            'sort': 'arrow.up.arrow.down',
            'calendar': 'calendar',
            'clock': 'clock',
            'alarm': 'alarm',
            'bell': 'bell',
            'message': 'message',
            'email': 'envelope',
            'phone': 'phone',
            'camera': 'camera',
            'photo': 'photo',
            'video': 'video',
            'music': 'music.note',
            'play': 'play.fill',
            'pause': 'pause.fill',
            'stop': 'stop.fill',
            'heart': 'heart',
            'star': 'star',
            'bookmark': 'bookmark',
            'tag': 'tag',
            'location': 'location',
            'map': 'map',
            'folder': 'folder',
            'document': 'doc',
            'cloud': 'cloud',
            'download': 'arrow.down.circle',
            'upload': 'arrow.up.circle',
            'refresh': 'arrow.clockwise',
            'info': 'info.circle',
            'warning': 'exclamationmark.triangle',
            'error': 'xmark.circle',
            'success': 'checkmark.circle',
            'add': 'plus',
            'remove': 'minus',
            'checkmark': 'checkmark',
            'cancel': 'xmark',
        }

        # Valid SF Symbols categories (not exhaustive, just common ones)
        self.valid_symbol_patterns = [
            r'^arrow\.',
            r'^chevron\.',
            r'^checkmark',
            r'^xmark',
            r'^circle',
            r'^square',
            r'^rectangle',
            r'^triangle',
            r'^diamond',
            r'^seal',
            r'^capsule',
            r'^plus',
            r'^minus',
            r'^multiply',
            r'^divide',
            r'^equal',
            r'^percent',
            r'^number',
            r'^character',
            r'^textformat',
            r'^bold',
            r'^italic',
            r'^underline',
            r'^strikethrough',
            r'^list',
            r'^increase\.',
            r'^decrease\.',
            r'^text\.',
            r'^line\.',
            r'^photo',
            r'^camera',
            r'^video',
            r'^music',
            r'^mic',
            r'^speaker',
            r'^phone',
            r'^envelope',
            r'^message',
            r'^bubble',
            r'^calendar',
            r'^clock',
            r'^alarm',
            r'^stopwatch',
            r'^timer',
            r'^bell',
            r'^tag',
            r'^bookmark',
            r'^heart',
            r'^star',
            r'^flag',
            r'^location',
            r'^map',
            r'^pin',
            r'^car',
            r'^bus',
            r'^tram',
            r'^airplane',
            r'^bicycle',
            r'^figure',
            r'^person',
            r'^house',
            r'^building',
            r'^wrench',
            r'^hammer',
            r'^screwdriver',
            r'^paintbrush',
            r'^pencil',
            r'^trash',
            r'^folder',
            r'^doc',
            r'^archivebox',
            r'^tray',
            r'^paperplane',
            r'^link',
            r'^paperclip',
            r'^chart',
            r'^gauge',
            r'^cloud',
            r'^wifi',
            r'^antenna',
            r'^lock',
            r'^key',
            r'^eye',
            r'^gear',
            r'^slider',
            r'^switch',
            r'^battery',
            r'^bolt',
            r'^sun',
            r'^moon',
            r'^sparkles',
            r'^flame',
            r'^drop',
            r'^snow',
            r'^leaf',
            r'^shield',
            r'^cross',
            r'^bandage',
            r'^staroflife',
        ]

    def analyze_file(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Analyze a file for SF Symbols usage."""
        results = []

        # Only analyze Swift files
        if not self.get_file_extension(file_path) == 'swift':
            return results

        # Find SF Symbol references
        results.extend(self._check_sf_symbol_usage(file_path, content))
        results.extend(self._check_deprecated_symbols(file_path, content))
        results.extend(self._check_common_mistakes(file_path, content))
        results.extend(self._check_hardcoded_icon_strings(file_path, content))

        return results

    def _check_sf_symbol_usage(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for invalid SF Symbol names."""
        results = []

        # Pattern for UIImage(systemName:) and Image(systemName:)
        patterns = [
            r'UIImage\(systemName:\s*"([^"]+)"\)',
            r'Image\(systemName:\s*"([^"]+)"\)',
            r'\.init\(systemName:\s*"([^"]+)"\)',
        ]

        for pattern in patterns:
            matches = list(re.finditer(pattern, content))

            for match in matches:
                symbol_name = match.group(1)
                line_num = content[:match.start()].count('\n') + 1

                # Check if symbol name looks valid (matches common patterns)
                is_valid = any(re.match(p, symbol_name) for p in self.valid_symbol_patterns)

                if not is_valid and not self._is_likely_variable(symbol_name):
                    code_snippet = self.get_lines_context(content, line_num, context_lines=1)

                    result = AnalysisResult(
                        file=file_path,
                        line=line_num,
                        column=match.start(),
                        severity=Severity.MEDIUM,
                        category=Category.QUALITY,
                        title="Potentially Invalid SF Symbol",
                        description=f"Symbol '{symbol_name}' doesn't match common SF Symbols patterns",
                        recommendation="Verify this SF Symbol exists in SF Symbols app or Apple documentation",
                        code_snippet=code_snippet,
                        references=[
                            "https://developer.apple.com/sf-symbols/",
                        ],
                    )
                    results.append(result)

        return results

    def _check_deprecated_symbols(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for deprecated SF Symbols."""
        results = []

        for deprecated, suggestion in self.deprecated_symbols.items():
            if deprecated in content:
                # Find exact occurrences
                for match in re.finditer(re.escape(deprecated), content):
                    line_num = content[:match.start()].count('\n') + 1
                    code_snippet = self.get_lines_context(content, line_num, context_lines=1)

                    result = AnalysisResult(
                        file=file_path,
                        line=line_num,
                        column=match.start(),
                        severity=Severity.LOW,
                        category=Category.QUALITY,
                        title="Deprecated SF Symbol",
                        description=f"Symbol '{deprecated}' is deprecated or discouraged",
                        recommendation=suggestion,
                        code_snippet=code_snippet,
                    )
                    results.append(result)

        return results

    def _check_common_mistakes(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for common SF Symbol naming mistakes."""
        results = []

        # Pattern for string literals that might be icon names
        patterns = [
            r'systemName:\s*"([^"]+)"',
            r'iconName:\s*"([^"]+)"',
        ]

        for pattern in patterns:
            matches = list(re.finditer(pattern, content))

            for match in matches:
                name = match.group(1).lower().strip()

                # Check if it's a common mistake
                if name in self.common_mistakes:
                    line_num = content[:match.start()].count('\n') + 1
                    code_snippet = self.get_lines_context(content, line_num, context_lines=1)

                    result = AnalysisResult(
                        file=file_path,
                        line=line_num,
                        column=match.start(),
                        severity=Severity.MEDIUM,
                        category=Category.QUALITY,
                        title="Incorrect SF Symbol Name",
                        description=f"'{name}' is not a valid SF Symbol",
                        recommendation=f"Use SF Symbol: '{self.common_mistakes[name]}'",
                        code_snippet=code_snippet,
                        references=[
                            "https://developer.apple.com/sf-symbols/",
                        ],
                    )
                    results.append(result)

        return results

    def _check_hardcoded_icon_strings(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for hardcoded icon strings that should use SF Symbols."""
        results = []

        # Patterns for potential hardcoded icon references
        hardcoded_patterns = [
            (r'\.png"|\.jpg"|\.jpeg"', "Image file extension in string (consider SF Symbols)"),
            (r'icon\.png|button\.png|arrow\.png', "Hardcoded icon filename (use SF Symbols)"),
        ]

        for pattern, description in hardcoded_patterns:
            matches = self.find_pattern(content, pattern, re.IGNORECASE)

            for line_num, column, matched_text in matches:
                # Skip if it's clearly not an icon (e.g., photo assets)
                if 'photo' in matched_text.lower() or 'image' in matched_text.lower():
                    continue

                code_snippet = self.get_lines_context(content, line_num, context_lines=1)

                result = AnalysisResult(
                    file=file_path,
                    line=line_num,
                    column=column,
                    severity=Severity.LOW,
                    category=Category.QUALITY,
                    title="Hardcoded Icon Asset",
                    description=description,
                    recommendation="Consider using SF Symbols for better scalability and consistency",
                    code_snippet=code_snippet,
                )
                results.append(result)

        return results

    def _is_likely_variable(self, symbol_name: str) -> bool:
        """Check if a symbol name is likely a variable rather than a literal."""
        # Variables often have camelCase or contain certain patterns
        return (
            symbol_name[0].islower() and any(c.isupper() for c in symbol_name[1:])
            or 'Name' in symbol_name
            or 'Icon' in symbol_name
            or symbol_name.startswith('k')  # Constant prefix
        )

    def is_supported_file(self, file_path: str) -> bool:
        """SF Symbols analyzer only supports Swift files."""
        return self.get_file_extension(file_path) == 'swift'
