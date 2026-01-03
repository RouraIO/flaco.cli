"""Info.plist security and configuration analyzer."""

import re
import xml.etree.ElementTree as ET
from typing import List, Dict, Optional
from .base_analyzer import BaseAnalyzer, AnalysisResult, Severity, Category


class IOSPlistAnalyzer(BaseAnalyzer):
    """Analyzes Info.plist files for security and configuration issues."""

    def __init__(self, io=None, verbose=False):
        super().__init__(io, verbose)

        # Required privacy descriptions
        self.privacy_keys = {
            'NSCameraUsageDescription': 'Camera',
            'NSPhotoLibraryUsageDescription': 'Photo Library',
            'NSPhotoLibraryAddUsageDescription': 'Photo Library (Add Only)',
            'NSLocationWhenInUseUsageDescription': 'Location (When In Use)',
            'NSLocationAlwaysUsageDescription': 'Location (Always)',
            'NSLocationAlwaysAndWhenInUseUsageDescription': 'Location (Always and When In Use)',
            'NSMicrophoneUsageDescription': 'Microphone',
            'NSContactsUsageDescription': 'Contacts',
            'NSCalendarsUsageDescription': 'Calendars',
            'NSRemindersUsageDescription': 'Reminders',
            'NSMotionUsageDescription': 'Motion & Fitness',
            'NSHealthShareUsageDescription': 'Health (Read)',
            'NSHealthUpdateUsageDescription': 'Health (Write)',
            'NSBluetoothAlwaysUsageDescription': 'Bluetooth',
            'NSBluetoothPeripheralUsageDescription': 'Bluetooth Peripheral',
            'NSSpeechRecognitionUsageDescription': 'Speech Recognition',
            'NSFaceIDUsageDescription': 'Face ID',
            'NSAppleMusicUsageDescription': 'Apple Music',
            'NSLocalNetworkUsageDescription': 'Local Network',
        }

        # Dangerous permissions that need justification
        self.dangerous_permissions = {
            'NSLocationAlwaysUsageDescription': 'Always location access',
            'NSLocationAlwaysAndWhenInUseUsageDescription': 'Always location access',
            'NSHealthUpdateUsageDescription': 'Health data write access',
        }

    def analyze_file(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Analyze Info.plist for security and configuration issues."""
        results = []

        # Only analyze plist files
        if not file_path.endswith(('Info.plist', '.plist')):
            return results

        try:
            # Parse plist
            plist_data = self._parse_plist(content)

            if plist_data:
                results.extend(self._check_privacy_descriptions(file_path, plist_data))
                results.extend(self._check_ats_configuration(file_path, plist_data))
                results.extend(self._check_url_schemes(file_path, plist_data))
                results.extend(self._check_dangerous_permissions(file_path, plist_data))
                results.extend(self._check_background_modes(file_path, plist_data))
                results.extend(self._check_bundle_configuration(file_path, plist_data))
        except Exception as e:
            if self.verbose and self.io:
                self.io.tool_error(f"Failed to parse plist: {e}")

        return results

    def _parse_plist(self, content: str) -> Optional[Dict]:
        """Parse plist content into dictionary."""
        try:
            root = ET.fromstring(content)
            # Find the main dict element
            dict_elem = root.find('.//dict')
            if dict_elem is not None:
                return self._parse_dict(dict_elem)
        except ET.ParseError:
            pass
        return None

    def _parse_dict(self, dict_elem) -> Dict:
        """Parse plist dict element."""
        result = {}
        children = list(dict_elem)

        i = 0
        while i < len(children):
            if children[i].tag == 'key':
                key = children[i].text
                if i + 1 < len(children):
                    value_elem = children[i + 1]
                    result[key] = self._parse_value(value_elem)
                i += 2
            else:
                i += 1

        return result

    def _parse_value(self, elem):
        """Parse plist value element."""
        if elem.tag == 'string':
            return elem.text or ''
        elif elem.tag == 'true':
            return True
        elif elem.tag == 'false':
            return False
        elif elem.tag == 'dict':
            return self._parse_dict(elem)
        elif elem.tag == 'array':
            return [self._parse_value(child) for child in elem]
        elif elem.tag in ('integer', 'real'):
            return elem.text
        return None

    def _check_privacy_descriptions(self, file_path: str, plist_data: Dict) -> List[AnalysisResult]:
        """Check for missing privacy descriptions."""
        results = []

        # Check which privacy keys are used but missing descriptions
        for key, description in self.privacy_keys.items():
            if key in plist_data:
                value = plist_data[key]

                # Check if description is too short or generic
                if not value or len(value) < 20:
                    result = AnalysisResult(
                        file=file_path,
                        line=1,
                        severity=Severity.HIGH,
                        category=Category.QUALITY,
                        title="Insufficient Privacy Description",
                        description=f"{description} usage description is too short or missing",
                        recommendation=f"Provide a clear, detailed explanation of why your app needs {description} access",
                        code_snippet=f"<key>{key}</key>\n<string>{value}</string>",
                        references=[
                            "https://developer.apple.com/documentation/bundleresources/information_property_list",
                        ],
                    )
                    results.append(result)

                # Check for generic descriptions
                generic_phrases = [
                    'we need',
                    'required',
                    'necessary',
                    'app needs',
                    'to work',
                ]

                if any(phrase in value.lower() for phrase in generic_phrases):
                    result = AnalysisResult(
                        file=file_path,
                        line=1,
                        severity=Severity.MEDIUM,
                        category=Category.QUALITY,
                        title="Generic Privacy Description",
                        description=f"{description} description is too generic",
                        recommendation="Be specific about how and why the data will be used",
                        code_snippet=f"<key>{key}</key>\n<string>{value}</string>",
                    )
                    results.append(result)

        return results

    def _check_ats_configuration(self, file_path: str, plist_data: Dict) -> List[AnalysisResult]:
        """Check App Transport Security configuration."""
        results = []

        ats_key = 'NSAppTransportSecurity'
        if ats_key in plist_data:
            ats_config = plist_data[ats_key]

            if isinstance(ats_config, dict):
                # Check for NSAllowsArbitraryLoads
                if ats_config.get('NSAllowsArbitraryLoads'):
                    result = AnalysisResult(
                        file=file_path,
                        line=1,
                        severity=Severity.CRITICAL,
                        category=Category.SECURITY,
                        title="App Transport Security Disabled",
                        description="NSAllowsArbitraryLoads is set to true, disabling ATS entirely",
                        recommendation="Remove NSAllowsArbitraryLoads and use HTTPS for all connections, or add specific exception domains",
                        code_snippet="<key>NSAllowsArbitraryLoads</key>\n<true/>",
                        references=[
                            "https://developer.apple.com/documentation/security/preventing_insecure_network_connections",
                        ],
                    )
                    results.append(result)

                # Check for exception domains
                if 'NSExceptionDomains' in ats_config:
                    domains = ats_config['NSExceptionDomains']
                    if isinstance(domains, dict) and len(domains) > 5:
                        result = AnalysisResult(
                            file=file_path,
                            line=1,
                            severity=Severity.MEDIUM,
                            category=Category.SECURITY,
                            title="Too Many ATS Exceptions",
                            description=f"Found {len(domains)} ATS exception domains",
                            recommendation="Minimize ATS exceptions, migrate to HTTPS where possible",
                            code_snippet="",
                        )
                        results.append(result)

        return results

    def _check_url_schemes(self, file_path: str, plist_data: Dict) -> List[AnalysisResult]:
        """Check URL scheme configuration."""
        results = []

        if 'CFBundleURLTypes' in plist_data:
            url_types = plist_data['CFBundleURLTypes']

            if isinstance(url_types, list):
                for url_type in url_types:
                    if isinstance(url_type, dict):
                        schemes = url_type.get('CFBundleURLSchemes', [])

                        if isinstance(schemes, list):
                            for scheme in schemes:
                                # Check for common/generic schemes
                                if scheme.lower() in ['http', 'https', 'file', 'ftp']:
                                    result = AnalysisResult(
                                        file=file_path,
                                        line=1,
                                        severity=Severity.HIGH,
                                        category=Category.SECURITY,
                                        title="Dangerous URL Scheme",
                                        description=f"URL scheme '{scheme}' conflicts with standard schemes",
                                        recommendation="Use a unique, app-specific URL scheme",
                                        code_snippet=f"<string>{scheme}</string>",
                                    )
                                    results.append(result)

                                # Check for schemes without bundle ID prefix
                                bundle_id = plist_data.get('CFBundleIdentifier', '')
                                if bundle_id and not scheme.startswith(bundle_id.split('.')[0]):
                                    result = AnalysisResult(
                                        file=file_path,
                                        line=1,
                                        severity=Severity.LOW,
                                        category=Category.QUALITY,
                                        title="Non-Unique URL Scheme",
                                        description=f"URL scheme '{scheme}' doesn't use bundle ID prefix",
                                        recommendation=f"Consider using a scheme like '{bundle_id.replace('.', '-')}' for uniqueness",
                                        code_snippet=f"<string>{scheme}</string>",
                                    )
                                    results.append(result)

        return results

    def _check_dangerous_permissions(self, file_path: str, plist_data: Dict) -> List[AnalysisResult]:
        """Check for dangerous permissions that need strong justification."""
        results = []

        for key, description in self.dangerous_permissions.items():
            if key in plist_data:
                result = AnalysisResult(
                    file=file_path,
                    line=1,
                    severity=Severity.MEDIUM,
                    category=Category.SECURITY,
                    title="Sensitive Permission Requested",
                    description=f"App requests {description}",
                    recommendation="Ensure this permission is absolutely necessary and well-justified in the description",
                    code_snippet=f"<key>{key}</key>",
                    references=[
                        "https://developer.apple.com/app-store/review/guidelines/#privacy",
                    ],
                )
                results.append(result)

        return results

    def _check_background_modes(self, file_path: str, plist_data: Dict) -> List[AnalysisResult]:
        """Check background modes configuration."""
        results = []

        if 'UIBackgroundModes' in plist_data:
            modes = plist_data['UIBackgroundModes']

            if isinstance(modes, list):
                # Check for potentially battery-draining modes
                draining_modes = ['location', 'audio', 'voip', 'external-accessory', 'bluetooth-central']

                for mode in modes:
                    if mode in draining_modes:
                        result = AnalysisResult(
                            file=file_path,
                            line=1,
                            severity=Severity.MEDIUM,
                            category=Category.PERFORMANCE,
                            title="Battery-Draining Background Mode",
                            description=f"Background mode '{mode}' can significantly impact battery life",
                            recommendation="Ensure this background mode is essential and properly managed",
                            code_snippet=f"<string>{mode}</string>",
                        )
                        results.append(result)

                # Warn if too many background modes
                if len(modes) > 3:
                    result = AnalysisResult(
                        file=file_path,
                        line=1,
                        severity=Severity.LOW,
                        category=Category.QUALITY,
                        title="Multiple Background Modes",
                        description=f"App has {len(modes)} background modes enabled",
                        recommendation="Only enable necessary background modes to conserve battery",
                        code_snippet="",
                    )
                    results.append(result)

        return results

    def _check_bundle_configuration(self, file_path: str, plist_data: Dict) -> List[AnalysisResult]:
        """Check bundle configuration."""
        results = []

        # Check for missing or generic bundle display name
        if 'CFBundleDisplayName' not in plist_data:
            result = AnalysisResult(
                file=file_path,
                line=1,
                severity=Severity.LOW,
                category=Category.QUALITY,
                title="Missing Bundle Display Name",
                description="CFBundleDisplayName not specified",
                recommendation="Add CFBundleDisplayName for better App Store presentation",
                code_snippet="",
            )
            results.append(result)

        # Check for debug/test identifiers in bundle ID
        bundle_id = plist_data.get('CFBundleIdentifier', '')
        if any(keyword in bundle_id.lower() for keyword in ['test', 'debug', 'dev', 'staging']):
            result = AnalysisResult(
                file=file_path,
                line=1,
                severity=Severity.HIGH,
                category=Category.QUALITY,
                title="Debug Bundle Identifier",
                description=f"Bundle identifier '{bundle_id}' contains debug/test keywords",
                recommendation="Use production bundle identifier for release builds",
                code_snippet=f"<key>CFBundleIdentifier</key>\n<string>{bundle_id}</string>",
            )
            results.append(result)

        return results

    def is_supported_file(self, file_path: str) -> bool:
        """Plist analyzer only supports .plist files."""
        return file_path.endswith(('.plist', 'Info.plist'))
