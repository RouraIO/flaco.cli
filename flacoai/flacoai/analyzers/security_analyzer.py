"""Security analyzer for detecting vulnerabilities (OWASP Top 10)."""

import re
from typing import List, Dict
from .base_analyzer import BaseAnalyzer, AnalysisResult, Severity, Category


class SecurityAnalyzer(BaseAnalyzer):
    """Analyzes code for security vulnerabilities based on OWASP Top 10."""

    def __init__(self, io=None, verbose=False):
        super().__init__(io, verbose)

        # SQL Injection patterns
        self.sql_patterns = [
            # String concatenation in SQL queries
            (r'(execute|query|exec)\s*\(\s*["\'].*\+.*["\']', "SQL query with string concatenation"),
            (r'(execute|query|exec)\s*\(\s*f["\'].*\{.*\}', "SQL query with f-string interpolation"),
            (r'(SELECT|INSERT|UPDATE|DELETE).*\+.*FROM', "SQL statement with concatenation"),
            (r'\.format\(.*\)\s*\)\s*#.*SQL', "SQL query using .format()"),
            (r'%s.*%(FROM|WHERE|INSERT)', "SQL query with % formatting"),
        ]

        # XSS patterns
        self.xss_patterns = [
            (r'innerHTML\s*=\s*[^;]*\+', "Unsafe innerHTML assignment"),
            (r'document\.write\(.*\+', "document.write with concatenation"),
            (r'\.html\(.*\+', "jQuery .html() with concatenation"),
            (r'dangerouslySetInnerHTML', "React dangerouslySetInnerHTML usage"),
            (r'v-html\s*=', "Vue v-html directive"),
        ]

        # Hardcoded credentials patterns
        self.credential_patterns = [
            (r'password\s*=\s*["\'][^"\']{3,}["\']', "Hardcoded password"),
            (r'api[_-]?key\s*=\s*["\'][^"\']{10,}["\']', "Hardcoded API key"),
            (r'secret\s*=\s*["\'][^"\']{10,}["\']', "Hardcoded secret"),
            (r'token\s*=\s*["\'][^"\']{10,}["\']', "Hardcoded token"),
            (r'aws[_-]?access[_-]?key', "AWS access key"),
            (r'private[_-]?key\s*=\s*["\']', "Hardcoded private key"),
        ]

        # Command injection patterns
        self.command_injection_patterns = [
            (r'(os\.system|subprocess\.call|exec|eval)\s*\([^)]*\+', "Command execution with concatenation"),
            (r'(os\.system|subprocess\.call)\s*\(f["\']', "Command execution with f-string"),
            (r'shell\s*=\s*True', "subprocess with shell=True"),
            (r'eval\s*\(', "eval() usage"),
            (r'exec\s*\(', "exec() usage"),
        ]

        # Path traversal patterns
        self.path_traversal_patterns = [
            (r'open\s*\([^)]*\+', "File open with concatenation"),
            (r'\.\./', "Relative path traversal"),
            (r'\.\.\\', "Relative path traversal (Windows)"),
            (r'(read|write).*user.*input', "File operation with user input"),
        ]

        # Insecure crypto patterns
        self.crypto_patterns = [
            (r'MD5|md5', "Weak hash algorithm (MD5)"),
            (r'SHA1|sha1(?!\.)', "Weak hash algorithm (SHA1)"),
            (r'DES|des_', "Weak encryption (DES)"),
            (r'ECB', "Insecure cipher mode (ECB)"),
            (r'Random\(\)', "Insecure random number generator"),
        ]

        # CSRF patterns
        self.csrf_patterns = [
            (r'@app\.route.*methods\s*=\s*\[[^\]]*["\']POST["\'][^\]]*\](?![^@]*@csrf)', "POST route without CSRF protection"),
            (r'<form[^>]*method\s*=\s*["\']post["\'][^>]*>(?![^<]*csrf)', "Form without CSRF token"),
        ]

        # Insecure deserialization patterns
        self.deserialization_patterns = [
            (r'pickle\.loads?\(', "Unsafe pickle deserialization"),
            (r'yaml\.load\((?!.*Loader=)', "Unsafe YAML deserialization"),
            (r'jsonpickle\.decode', "Potentially unsafe jsonpickle"),
            (r'marshal\.loads', "Unsafe marshal deserialization"),
        ]

        # Authentication/Authorization patterns
        self.auth_patterns = [
            (r'if.*password\s*==\s*["\']', "Password comparison in code"),
            (r'admin\s*=\s*True', "Hardcoded admin flag"),
            (r'is_authenticated\s*=\s*True', "Hardcoded authentication bypass"),
            (r'disable.*auth', "Authentication disabled"),
        ]

        # Logging sensitive data patterns
        self.logging_patterns = [
            (r'(log|print|console\.log).*password', "Password in logs"),
            (r'(log|print|console\.log).*token', "Token in logs"),
            (r'(log|print|console\.log).*secret', "Secret in logs"),
            (r'(log|print|console\.log).*api[_-]?key', "API key in logs"),
        ]

        # iOS/Swift-specific security patterns
        self.ios_insecure_storage_patterns = [
            (r'UserDefaults\.standard\.(set|setValue).*password', "Password stored in UserDefaults (insecure)"),
            (r'UserDefaults\.standard\.(set|setValue).*token', "Token stored in UserDefaults (insecure)"),
            (r'UserDefaults\.standard\.(set|setValue).*apiKey', "API key stored in UserDefaults (insecure)"),
            (r'UserDefaults\.standard\.(set|setValue).*secret', "Secret stored in UserDefaults (insecure)"),
            (r'\.write\(to:.*password', "Password written to file (insecure)"),
        ]

        self.ios_weak_crypto_patterns = [
            (r'kCCAlgorithmDES', "Weak encryption algorithm (DES)"),
            (r'kCCAlgorithm3DES', "Weak encryption algorithm (3DES)"),
            (r'kCCAlgorithmRC4', "Weak encryption algorithm (RC4)"),
            (r'CC_MD5', "Weak hash algorithm (MD5)"),
            (r'CC_SHA1', "Weak hash algorithm (SHA1)"),
            (r'Insecure\.SHA1', "Weak hash algorithm (SHA1)"),
        ]

        self.ios_app_transport_security_patterns = [
            (r'NSAllowsArbitraryLoads.*true', "App Transport Security disabled"),
            (r'NSExceptionAllowsInsecureHTTPLoads', "Insecure HTTP loads allowed"),
            (r'NSAllowsLocalNetworking.*true', "Local networking allowed (review necessity)"),
        ]

        self.ios_url_scheme_patterns = [
            (r'canOpenURL.*without.*checking', "URL scheme without validation"),
            (r'open\(.*URL.*\).*user.*input', "Opening URL with user input (potential injection)"),
        ]

        self.ios_keychain_patterns = [
            (r'kSecAttrAccessibleAlways(?!ThisDeviceOnly)', "Keychain item accessible always (weak)"),
            (r'kSecAttrAccessibleWhenUnlocked(?!ThisDeviceOnly)', "Keychain without device-only protection"),
        ]

        self.ios_debug_patterns = [
            (r'#if\s+DEBUG\s*$(?!.*#endif)', "Debug code block without endif"),
            (r'assert\(', "Assert statement (should be DEBUG only)"),
            (r'fatalError\(["\'][^"\']*TODO', "TODO fatalError in code"),
        ]

        self.ios_webview_patterns = [
            (r'evaluateJavaScript.*user.*input', "WebView JavaScript injection risk"),
            (r'WKUserScript.*user.*input', "User script injection risk"),
            (r'loadHTMLString.*user.*input', "HTML injection in WebView"),
        ]

        self.ios_certificate_pinning_patterns = [
            (r'URLSession.*without.*pinning', "URLSession without certificate pinning"),
            (r'serverTrustPolicy.*None', "Server trust policy disabled"),
        ]

    def analyze_file(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Analyze a file for security vulnerabilities."""
        results = []

        # Skip binary files and very large files
        if not self._is_analyzable(content):
            return results

        # Check all security patterns
        results.extend(self._check_patterns(file_path, content, self.sql_patterns,
                                           "SQL Injection Risk", Severity.HIGH,
                                           "Use parameterized queries or prepared statements"))

        results.extend(self._check_patterns(file_path, content, self.xss_patterns,
                                           "Cross-Site Scripting (XSS) Risk", Severity.HIGH,
                                           "Sanitize user input and use safe DOM manipulation methods"))

        results.extend(self._check_patterns(file_path, content, self.credential_patterns,
                                           "Hardcoded Credentials", Severity.CRITICAL,
                                           "Use environment variables or secure credential storage"))

        results.extend(self._check_patterns(file_path, content, self.command_injection_patterns,
                                           "Command Injection Risk", Severity.CRITICAL,
                                           "Avoid shell=True and use parameterized commands"))

        results.extend(self._check_patterns(file_path, content, self.path_traversal_patterns,
                                           "Path Traversal Risk", Severity.HIGH,
                                           "Validate and sanitize file paths, use os.path.normpath()"))

        results.extend(self._check_patterns(file_path, content, self.crypto_patterns,
                                           "Weak Cryptography", Severity.MEDIUM,
                                           "Use SHA-256 or better, AES with secure modes"))

        results.extend(self._check_patterns(file_path, content, self.csrf_patterns,
                                           "Missing CSRF Protection", Severity.MEDIUM,
                                           "Add CSRF tokens to forms and validate on submission"))

        results.extend(self._check_patterns(file_path, content, self.deserialization_patterns,
                                           "Insecure Deserialization", Severity.HIGH,
                                           "Use safe serialization or validate deserialized data"))

        results.extend(self._check_patterns(file_path, content, self.auth_patterns,
                                           "Authentication/Authorization Issue", Severity.HIGH,
                                           "Use secure authentication frameworks and proper access control"))

        results.extend(self._check_patterns(file_path, content, self.logging_patterns,
                                           "Sensitive Data in Logs", Severity.MEDIUM,
                                           "Remove sensitive data from log statements"))

        # iOS-specific checks
        ext = self.get_file_extension(file_path)
        if ext in ('swift', 'm', 'mm', 'plist', 'xml'):
            results.extend(self._check_patterns(file_path, content, self.ios_insecure_storage_patterns,
                                               "Insecure iOS Data Storage", Severity.CRITICAL,
                                               "Use Keychain for sensitive data instead of UserDefaults or files"))

            results.extend(self._check_patterns(file_path, content, self.ios_weak_crypto_patterns,
                                               "Weak iOS Cryptography", Severity.HIGH,
                                               "Use AES-256 (kCCAlgorithmAES) and SHA-256 or better"))

            results.extend(self._check_patterns(file_path, content, self.ios_app_transport_security_patterns,
                                               "App Transport Security Issue", Severity.HIGH,
                                               "Enable ATS and use HTTPS for all network requests"))

            results.extend(self._check_patterns(file_path, content, self.ios_url_scheme_patterns,
                                               "URL Scheme Vulnerability", Severity.HIGH,
                                               "Validate and sanitize URL schemes before opening"))

            results.extend(self._check_patterns(file_path, content, self.ios_keychain_patterns,
                                               "Weak Keychain Protection", Severity.MEDIUM,
                                               "Use kSecAttrAccessibleWhenUnlockedThisDeviceOnly"))

            results.extend(self._check_patterns(file_path, content, self.ios_debug_patterns,
                                               "Debug Code in Release", Severity.MEDIUM,
                                               "Wrap debug code in #if DEBUG and remove before release"))

            results.extend(self._check_patterns(file_path, content, self.ios_webview_patterns,
                                               "WebView Injection Risk", Severity.HIGH,
                                               "Sanitize user input before using in WebView JavaScript or HTML"))

            results.extend(self._check_patterns(file_path, content, self.ios_certificate_pinning_patterns,
                                               "Missing Certificate Pinning", Severity.MEDIUM,
                                               "Implement certificate pinning for sensitive network requests"))

        return results

    def _check_patterns(self, file_path: str, content: str, patterns: List[tuple],
                       title: str, severity: Severity, recommendation: str) -> List[AnalysisResult]:
        """Check content against a list of patterns."""
        results = []

        for pattern, description in patterns:
            matches = self.find_pattern(content, pattern, re.IGNORECASE)

            for line_num, column, matched_text in matches:
                # Skip comments and strings in some cases
                if self._is_likely_false_positive(content, line_num, matched_text):
                    continue

                code_snippet = self.get_lines_context(content, line_num, context_lines=2)

                result = AnalysisResult(
                    file=file_path,
                    line=line_num,
                    column=column,
                    severity=severity,
                    category=Category.SECURITY,
                    title=title,
                    description=f"{description}: {matched_text[:50]}...",
                    recommendation=recommendation,
                    code_snippet=code_snippet,
                    references=[
                        "https://owasp.org/www-project-top-ten/",
                    ],
                )
                results.append(result)

        return results

    def _is_analyzable(self, content: str) -> bool:
        """Check if content can be analyzed (text, reasonable size)."""
        try:
            # Try to decode as text
            if isinstance(content, bytes):
                content.decode('utf-8')

            # Skip very large files (>1MB)
            if len(content) > 1024 * 1024:
                return False

            return True
        except (UnicodeDecodeError, AttributeError):
            return False

    def _is_likely_false_positive(self, content: str, line_num: int, matched_text: str) -> bool:
        """Check if a match is likely a false positive."""
        lines = content.split('\n')
        if line_num > len(lines):
            return False

        line = lines[line_num - 1]

        # Skip comment lines
        comment_patterns = [r'^\s*#', r'^\s*//', r'^\s*/\*', r'^\s*\*', r'^\s*"""', r"^\s*'''"]
        for pattern in comment_patterns:
            if re.match(pattern, line):
                return True

        # Skip lines that are clearly examples or documentation
        if 'example' in line.lower() or 'todo' in line.lower() or 'fixme' in line.lower():
            return True

        return False

    def is_supported_file(self, file_path: str) -> bool:
        """Security analyzer supports most code files."""
        ext = self.get_file_extension(file_path)

        # Supported extensions
        supported = {
            'py', 'js', 'ts', 'jsx', 'tsx', 'php', 'java', 'rb', 'go',
            'cs', 'cpp', 'c', 'h', 'hpp', 'rs', 'swift', 'kt', 'scala',
            'sql', 'pl', 'sh', 'bash', 'vue', 'html', 'htm'
        }

        return ext.lower() in supported
