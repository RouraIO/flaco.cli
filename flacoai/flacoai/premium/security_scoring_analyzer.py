"""
PROPRIETARY - Security Scoring Analyzer

Copyright (c) 2026 Roura.IO
All Rights Reserved.

Requires: Flaco AI Pro or Enterprise license
"""

import re
from typing import List, Dict, Tuple
from collections import defaultdict
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from analyzers.base_analyzer import BaseAnalyzer, AnalysisResult, Severity, Category


class SecurityScoringAnalyzer(BaseAnalyzer):
    """
    Premium analyzer providing quantitative security scoring.

    Generates an overall security score (0-100) based on:
    - OWASP Mobile Top 10 compliance
    - Data protection vulnerabilities
    - Network security issues
    - Authentication/authorization weaknesses
    - Code injection risks
    - Cryptography misuse

    Higher scores = better security
    """

    # Vulnerability weights (impact on score)
    WEIGHTS = {
        'critical': 15,  # -15 points per critical issue
        'high': 8,       # -8 points per high issue
        'medium': 3,     # -3 points per medium issue
        'low': 1,        # -1 point per low issue
    }

    def analyze_file(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Analyze file for security issues and generate score.

        Args:
            file_path: Path to file
            content: File content

        Returns:
            List of security findings with score impact
        """
        results = []

        # Only analyze Swift files
        if not file_path.endswith('.swift'):
            return results

        results.extend(self._check_hardcoded_secrets(file_path, content))
        results.extend(self._check_insecure_network(file_path, content))
        results.extend(self._check_weak_crypto(file_path, content))
        results.extend(self._check_insecure_storage(file_path, content))
        results.extend(self._check_auth_weaknesses(file_path, content))
        results.extend(self._check_code_injection(file_path, content))
        results.extend(self._check_jailbreak_detection(file_path, content))

        return results

    def calculate_security_score(self, all_results: List[AnalysisResult]) -> Dict:
        """Calculate overall security score from findings.

        Args:
            all_results: All security findings across project

        Returns:
            Dict with score, grade, and breakdown
        """
        base_score = 100

        # Count issues by severity
        issue_counts = defaultdict(int)
        for result in all_results:
            if result.category == Category.SECURITY:
                severity_key = result.severity.value
                issue_counts[severity_key] += 1

        # Calculate deductions
        total_deduction = 0
        for severity, count in issue_counts.items():
            weight = self.WEIGHTS.get(severity, 0)
            total_deduction += weight * count

        final_score = max(0, base_score - total_deduction)

        # Assign grade
        if final_score >= 90:
            grade = 'A'
            assessment = 'Excellent'
        elif final_score >= 80:
            grade = 'B'
            assessment = 'Good'
        elif final_score >= 70:
            grade = 'C'
            assessment = 'Fair'
        elif final_score >= 60:
            grade = 'D'
            assessment = 'Poor'
        else:
            grade = 'F'
            assessment = 'Critical'

        return {
            'score': final_score,
            'grade': grade,
            'assessment': assessment,
            'issue_counts': dict(issue_counts),
            'total_deduction': total_deduction,
            'recommendations': self._get_top_recommendations(issue_counts),
        }

    def _check_hardcoded_secrets(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect hardcoded secrets, API keys, passwords."""
        results = []

        # Secret patterns
        secret_patterns = [
            (r'(?:api[_-]?key|apikey)\s*=\s*["\']([A-Za-z0-9]{20,})["\']',
             'API key hardcoded', Severity.CRITICAL),
            (r'password\s*=\s*["\'](.+)["\']',
             'Password hardcoded', Severity.CRITICAL),
            (r'(?:secret|token)\s*=\s*["\']([A-Za-z0-9+/=]{20,})["\']',
             'Secret token hardcoded', Severity.CRITICAL),
            (r'(?:private[_-]?key)\s*=\s*["\'](.+)["\']',
             'Private key hardcoded', Severity.CRITICAL),
            (r'aws[_-]?(?:access[_-]?key|secret)',
             'AWS credentials hardcoded', Severity.CRITICAL),
        ]

        for pattern, description, severity in secret_patterns:
            for match in re.finditer(pattern, content, re.IGNORECASE):
                line_num = content[:match.start()].count('\n') + 1

                results.append(AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=severity,
                    category=Category.SECURITY,
                    title=f"🔴 OWASP M9: {description} - CRITICAL vulnerability",
                    description=f"{description} in source code. Attackers can extract secrets "
                               f"from app binary using tools like Hopper or class-dump. "
                               f"This violates OWASP Mobile M9 (Reverse Engineering).",
                    recommendation="Move secrets to secure storage:\n"
                                  "1. Use Keychain for sensitive data\n"
                                  "2. Fetch from backend API at runtime\n"
                                  "3. Use environment variables (excluded from git)\n"
                                  "4. Consider app config service (Firebase Remote Config)",
                    code_snippet=self._get_line(content, line_num),
                ))

        return results

    def _check_insecure_network(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect insecure network communications."""
        results = []

        # HTTP instead of HTTPS
        http_pattern = r'(?:URL|url)\s*=\s*.*http://(?!localhost|127\.0\.0\.1)'

        for match in re.finditer(http_pattern, content):
            line_num = content[:match.start()].count('\n') + 1

            results.append(AnalysisResult(
                file=file_path,
                line=line_num,
                severity=Severity.HIGH,
                category=Category.SECURITY,
                title="🟠 OWASP M3: Insecure HTTP connection - man-in-the-middle risk",
                description="Using HTTP instead of HTTPS exposes data to interception. "
                           "Attackers on same network can read/modify traffic. "
                           "This violates OWASP Mobile M3 (Insecure Communication).",
                recommendation="Use HTTPS for all network requests:\n"
                              "Replace http:// with https://\n"
                              "Enable App Transport Security (ATS) in Info.plist",
                code_snippet=self._get_line(content, line_num),
            ))

        # SSL pinning check
        lines = content.splitlines()
        has_ssl_pinning = any([
            'serverTrustPolicy' in line or
            'pinnedCertificates' in line or
            'PinnedCertificatesTrustEvaluator' in line
            for line in lines
        ])

        # If making network requests without SSL pinning
        if 'URLSession' in content and not has_ssl_pinning:
            results.append(AnalysisResult(
                file=file_path,
                line=1,
                severity=Severity.MEDIUM,
                category=Category.SECURITY,
                title="🟡 Missing SSL pinning - certificate spoofing risk",
                description="No SSL certificate pinning detected. While HTTPS is encrypted, "
                           "attackers with rogue CA certificates can intercept traffic.",
                recommendation="Implement SSL pinning:\n"
                              "Use URLSessionDelegate to validate certificates:\n"
                              "func urlSession(_ session: URLSession,\n"
                              "    didReceive challenge: URLAuthenticationChallenge,\n"
                              "    completionHandler: @escaping (URLSession.AuthChallengeDisposition, URLCredential?) -> Void)\n"
                              "Or use Alamofire with ServerTrustManager",
                code_snippet="File contains network requests without SSL pinning",
            ))

        return results

    def _check_weak_crypto(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect weak cryptography."""
        results = []

        # Weak algorithms
        weak_patterns = [
            (r'\bMD5\b', 'MD5 hash (broken)', Severity.HIGH),
            (r'\bSHA1\b', 'SHA-1 hash (deprecated)', Severity.MEDIUM),
            (r'\bDES\b', 'DES encryption (insecure)', Severity.CRITICAL),
            (r'\bRC4\b', 'RC4 cipher (broken)', Severity.CRITICAL),
            (r'CCAlgorithm\.3DES', 'Triple-DES (deprecated)', Severity.MEDIUM),
        ]

        for pattern, description, severity in weak_patterns:
            for match in re.finditer(pattern, content):
                line_num = content[:match.start()].count('\n') + 1

                results.append(AnalysisResult(
                    file=file_path,
                    line=line_num,
                    severity=severity,
                    category=Category.SECURITY,
                    title=f"🔴 OWASP M5: Weak cryptography - {description}",
                    description=f"Using {description} which is cryptographically broken or deprecated. "
                               f"Attackers can crack this encryption. "
                               f"Violates OWASP Mobile M5 (Insufficient Cryptography).",
                    recommendation="Use modern cryptography:\n"
                                  "For hashing: SHA-256 or SHA-512\n"
                                  "For encryption: AES-256-GCM\n"
                                  "For key derivation: PBKDF2, Argon2\n"
                                  "Use CryptoKit on iOS 13+ for best practices",
                    code_snippet=self._get_line(content, line_num),
                ))

        # Check for hardcoded encryption keys
        key_pattern = r'(?:let|var)\s+(?:key|iv|salt)\s*=\s*["\']([A-Za-z0-9+/=]{16,})["\']'

        for match in re.finditer(key_pattern, content):
            line_num = content[:match.start()].count('\n') + 1

            results.append(AnalysisResult(
                file=file_path,
                line=line_num,
                severity=Severity.CRITICAL,
                category=Category.SECURITY,
                title="🔴 OWASP M5: Hardcoded encryption key - CRITICAL",
                description="Encryption key is hardcoded. Attackers can extract the key from "
                           "app binary and decrypt all data encrypted with it.",
                recommendation="Generate keys at runtime and store in Keychain:\n"
                              "let key = SymmetricKey(size: .bits256)\n"
                              "// Store in Keychain\n"
                              "Or derive from user password using PBKDF2",
                code_snippet=self._get_line(content, line_num),
            ))

        return results

    def _check_insecure_storage(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect insecure data storage."""
        results = []

        # UserDefaults for sensitive data
        sensitive_keywords = ['password', 'token', 'secret', 'key', 'credential', 'auth']

        lines = content.splitlines()

        for line_num, line in enumerate(lines, start=1):
            if 'UserDefaults' in line and 'set' in line:
                # Check if storing sensitive data
                line_lower = line.lower()
                for keyword in sensitive_keywords:
                    if keyword in line_lower:
                        results.append(AnalysisResult(
                            file=file_path,
                            line=line_num,
                            severity=Severity.HIGH,
                            category=Category.SECURITY,
                            title=f"🟠 OWASP M2: Sensitive data in UserDefaults - {keyword}",
                            description=f"Storing '{keyword}' in UserDefaults. UserDefaults is NOT encrypted "
                                       f"and can be accessed by anyone with device access (jailbreak, backup). "
                                       f"Violates OWASP Mobile M2 (Insecure Data Storage).",
                            recommendation=f"Use Keychain for sensitive data:\n"
                                          f"import Security\n"
                                          f"let query: [String: Any] = [\n"
                                          f"    kSecClass as String: kSecClassGenericPassword,\n"
                                          f"    kSecAttrAccount as String: \"user_{keyword}\",\n"
                                          f"    kSecValueData as String: data\n"
                                          f"]\n"
                                          f"SecItemAdd(query as CFDictionary, nil)",
                            code_snippet=line.strip(),
                        ))
                        break

        # Writing sensitive files without encryption
        if 'write(to:' in content or 'FileManager' in content:
            for keyword in sensitive_keywords:
                if keyword in content.lower():
                    results.append(AnalysisResult(
                        file=file_path,
                        line=1,
                        severity=Severity.HIGH,
                        category=Category.SECURITY,
                        title="🟠 OWASP M2: Unencrypted file storage of sensitive data",
                        description="Writing sensitive data to disk without encryption. "
                                   "Files can be accessed via iTunes backup or jailbroken device.",
                        recommendation="Use Data Protection API:\n"
                                      "try data.write(to: url, options: .completeFileProtection)\n"
                                      "Or encrypt before writing using CryptoKit",
                        code_snippet=f"File contains: {keyword} + file writing",
                    ))
                    break

        return results

    def _check_auth_weaknesses(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect authentication and authorization weaknesses."""
        results = []

        # Weak biometric implementation
        if 'LAContext' in content and 'evaluatePolicy' in content:
            # Check for fallback handling
            if 'biometryNotEnrolled' not in content and 'biometryNotAvailable' not in content:
                results.append(AnalysisResult(
                    file=file_path,
                    line=1,
                    severity=Severity.MEDIUM,
                    category=Category.SECURITY,
                    title="🟡 OWASP M4: Incomplete biometric auth fallback",
                    description="Biometric authentication without proper fallback handling. "
                               "App may fail on devices without biometrics or lock users out.",
                    recommendation="Handle biometric errors:\n"
                                  "switch error.code {\n"
                                  "case LAError.biometryNotEnrolled:\n"
                                  "    // Prompt user to enroll\n"
                                  "case LAError.biometryNotAvailable:\n"
                                  "    // Fall back to password\n"
                                  "}",
                    code_snippet="Biometric auth detected",
                ))

        # Session management issues
        if 'token' in content.lower() and 'expire' not in content.lower():
            results.append(AnalysisResult(
                file=file_path,
                line=1,
                severity=Severity.MEDIUM,
                category=Category.SECURITY,
                title="🟡 OWASP M4: Missing token expiration check",
                description="Auth tokens should have expiration checks. Without them, "
                           "stolen tokens remain valid indefinitely.",
                recommendation="Validate token expiration:\n"
                              "if tokenExpiryDate < Date() {\n"
                              "    // Refresh token or re-authenticate\n"
                              "}\n"
                              "Store expiry with token in Keychain",
                code_snippet="Token handling detected",
            ))

        return results

    def _check_code_injection(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Detect code injection vulnerabilities."""
        results = []

        # SQL injection in raw queries
        sql_pattern = r'(?:execute|query|prepare)\s*\([^)]*".*\+.*"'

        for match in re.finditer(sql_pattern, content):
            line_num = content[:match.start()].count('\n') + 1

            results.append(AnalysisResult(
                file=file_path,
                line=line_num,
                severity=Severity.CRITICAL,
                category=Category.SECURITY,
                title="🔴 OWASP M7: SQL injection via string concatenation",
                description="Building SQL queries with string concatenation. User input can inject "
                           "malicious SQL commands to access/modify unauthorized data.",
                recommendation="Use parameterized queries:\n"
                              "let query = \"SELECT * FROM users WHERE id = ?\"\n"
                              "statement.bind(userId)\n"
                              "Or use Core Data / Realm which auto-parameterize",
                code_snippet=self._get_line(content, line_num),
            ))

        # JavaScript injection in WebView
        if 'WKWebView' in content or 'evaluateJavaScript' in content:
            results.append(AnalysisResult(
                file=file_path,
                line=1,
                severity=Severity.HIGH,
                category=Category.SECURITY,
                title="🟠 OWASP M7: WebView XSS risk if user input not sanitized",
                description="WebView with JavaScript enabled. If user input is rendered without "
                           "sanitization, attackers can inject malicious scripts (XSS).",
                recommendation="Sanitize user input before WebView:\n"
                              "let sanitized = userInput\n"
                              "    .replacingOccurrences(of: \"<\", with: \"&lt;\")\n"
                              "    .replacingOccurrences(of: \">\", with: \"&gt;\")\n"
                              "Or disable JavaScript if not needed",
                code_snippet="WebView usage detected",
            ))

        return results

    def _check_jailbreak_detection(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for jailbreak detection mechanisms."""
        results = []

        # Jailbreak detection patterns
        jailbreak_indicators = [
            'cydia://', '/Applications/Cydia.app',
            '/bin/bash', '/usr/sbin/sshd',
            'jailbreak', 'substrate'
        ]

        has_detection = any(indicator in content.lower() for indicator in jailbreak_indicators)

        if not has_detection:
            results.append(AnalysisResult(
                file=file_path,
                line=1,
                severity=Severity.LOW,
                category=Category.SECURITY,
                title="🟢 Consider adding jailbreak detection",
                description="No jailbreak detection found. Jailbroken devices have weakened security "
                           "(disabled code signing, root access). Consider detecting and warning users.",
                recommendation="Add basic jailbreak detection:\n"
                              "func isJailbroken() -> Bool {\n"
                              "    let paths = [\"/Applications/Cydia.app\", \"/bin/bash\"]\n"
                              "    return paths.contains { FileManager.default.fileExists(atPath: $0) }\n"
                              "}\n"
                              "Or use library like IOSSecuritySuite",
                code_snippet="No jailbreak detection found",
            ))

        return results

    def _get_line(self, content: str, line_num: int) -> str:
        """Get specific line from content."""
        lines = content.splitlines()
        if 0 < line_num <= len(lines):
            return lines[line_num - 1].strip()
        return ""

    def _get_top_recommendations(self, issue_counts: Dict) -> List[str]:
        """Generate top security recommendations based on issues."""
        recommendations = []

        if issue_counts.get('critical', 0) > 0:
            recommendations.append("🔴 CRITICAL: Address all critical vulnerabilities immediately - "
                                 "these can lead to complete security compromise")

        if issue_counts.get('high', 0) > 3:
            recommendations.append("🟠 HIGH: Focus on high-severity issues - "
                                 "these expose significant attack surface")

        recommendations.append("🔐 Enable App Transport Security (ATS) in Info.plist")
        recommendations.append("🔑 Move all secrets to Keychain or backend API")
        recommendations.append("🔒 Use modern cryptography (AES-256-GCM, SHA-256)")
        recommendations.append("📱 Consider implementing certificate pinning for production")

        return recommendations[:5]  # Top 5
