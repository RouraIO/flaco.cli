# Code Review Report

## Summary

- **Files Analyzed:** 100
- **Total Issues:** 1437
- **Duration:** 0.00s

### By Severity
- 🔴 **Critical:** 16
- 🟠 **High:** 24
- 🟡 **Medium:** 494
- 🟢 **Low:** 903


## 🔴 CRITICAL Severity (16 issues)

### 1. 🔴 Command Injection Risk

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:47`
**Severity:** CRITICAL
**Category:** security

**Description:** subprocess with shell=True: shell=True...

**Recommendation:** Avoid shell=True and use parameterized commands

**Code:**
```
            (r'(os\.system|subprocess\.call|exec|eval)\s*\([^)]*\+', "Command execution with concatenation"),
            (r'(os\.system|subprocess\.call)\s*\(f["\']', "Command execution with f-string"),
            (r'shell\s*=\s*True', "subprocess with shell=True"),
            (r'eval\s*\(', "eval() usage"),
            (r'exec\s*\(', "exec() usage"),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 2. 🔴 Command Injection Risk

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:173`
**Severity:** CRITICAL
**Category:** security

**Description:** subprocess with shell=True: shell=True...

**Recommendation:** Avoid shell=True and use parameterized commands

**Code:**
```
        results.extend(self._check_patterns(file_path, content, self.command_injection_patterns,
                                           "Command Injection Risk", Severity.CRITICAL,
                                           "Avoid shell=True and use parameterized commands"))

        results.extend(self._check_patterns(file_path, content, self.path_traversal_patterns,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 3. 🔴 Command Injection Risk

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:48`
**Severity:** CRITICAL
**Category:** security

**Description:** eval() usage: eval(...

**Recommendation:** Avoid shell=True and use parameterized commands

**Code:**
```
            (r'(os\.system|subprocess\.call)\s*\(f["\']', "Command execution with f-string"),
            (r'shell\s*=\s*True', "subprocess with shell=True"),
            (r'eval\s*\(', "eval() usage"),
            (r'exec\s*\(', "exec() usage"),
        ]
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 4. 🔴 Command Injection Risk

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:49`
**Severity:** CRITICAL
**Category:** security

**Description:** exec() usage: exec(...

**Recommendation:** Avoid shell=True and use parameterized commands

**Code:**
```
            (r'shell\s*=\s*True', "subprocess with shell=True"),
            (r'eval\s*\(', "eval() usage"),
            (r'exec\s*\(', "exec() usage"),
        ]

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 5. 🔴 Hardcoded Credentials

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_aws_credentials.py:24`
**Severity:** CRITICAL
**Category:** security

**Description:** AWS access key: AWS_ACCESS_KEY...

**Recommendation:** Use environment variables or secure credential storage

**Code:**
```
                # Mock the litellm validate_environment to return missing AWS keys
                mock_validate.return_value = {
                    "missing_keys": ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"],
                    "keys_in_environment": False,
                }
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 6. 🔴 Hardcoded Credentials

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_aws_credentials.py:32`
**Severity:** CRITICAL
**Category:** security

**Description:** AWS access key: AWS_ACCESS_KEY...

**Recommendation:** Use environment variables or secure credential storage

**Code:**
```

                # Check that the AWS keys were removed from missing_keys
                assert "AWS_ACCESS_KEY_ID" not in model.missing_keys
                assert "AWS_SECRET_ACCESS_KEY" not in model.missing_keys
                # With no missing keys, validation should pass
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 7. 🔴 Hardcoded Credentials

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_aws_credentials.py:56`
**Severity:** CRITICAL
**Category:** security

**Description:** AWS access key: AWS_ACCESS_KEY...

**Recommendation:** Use environment variables or secure credential storage

**Code:**
```
                # Mock the litellm validate_environment to return missing AWS keys
                mock_validate.return_value = {
                    "missing_keys": ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"],
                    "keys_in_environment": False,
                }
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 8. 🔴 Hardcoded Credentials

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_aws_credentials.py:64`
**Severity:** CRITICAL
**Category:** security

**Description:** AWS access key: AWS_ACCESS_KEY...

**Recommendation:** Use environment variables or secure credential storage

**Code:**
```

                # Check that the AWS keys were removed from missing_keys
                assert "AWS_ACCESS_KEY_ID" not in model.missing_keys
                assert "AWS_SECRET_ACCESS_KEY" not in model.missing_keys
                # With no missing keys, validation should pass
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 9. 🔴 Hardcoded Credentials

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_aws_credentials.py:88`
**Severity:** CRITICAL
**Category:** security

**Description:** AWS access key: AWS_ACCESS_KEY...

**Recommendation:** Use environment variables or secure credential storage

**Code:**
```
                # Mock the litellm validate_environment to return missing AWS keys
                mock_validate.return_value = {
                    "missing_keys": ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"],
                    "keys_in_environment": False,
                }
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 10. 🔴 Hardcoded Credentials

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_aws_credentials.py:96`
**Severity:** CRITICAL
**Category:** security

**Description:** AWS access key: AWS_ACCESS_KEY...

**Recommendation:** Use environment variables or secure credential storage

**Code:**
```

                # For non-Bedrock models, AWS credential keys should remain in missing_keys
                assert "AWS_ACCESS_KEY_ID" in model.missing_keys
                assert "AWS_SECRET_ACCESS_KEY" in model.missing_keys
                # With missing keys, validation should fail
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 11. 🔴 Hardcoded Credentials

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_aws_credentials.py:119`
**Severity:** CRITICAL
**Category:** security

**Description:** AWS access key: AWS_ACCESS_KEY...

**Recommendation:** Use environment variables or secure credential storage

**Code:**
```
                # Mock the litellm validate_environment to return missing AWS keys
                mock_validate.return_value = {
                    "missing_keys": ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"],
                    "keys_in_environment": False,
                }
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 12. 🔴 Hardcoded Credentials

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_aws_credentials.py:127`
**Severity:** CRITICAL
**Category:** security

**Description:** AWS access key: AWS_ACCESS_KEY...

**Recommendation:** Use environment variables or secure credential storage

**Code:**
```

                # Without AWS_PROFILE, AWS credential keys should remain in missing_keys
                assert "AWS_ACCESS_KEY_ID" in model.missing_keys
                assert "AWS_SECRET_ACCESS_KEY" in model.missing_keys
                # With missing keys, validation should fail
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 13. 🔴 Hardcoded Credentials

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_aws_credentials.py:151`
**Severity:** CRITICAL
**Category:** security

**Description:** AWS access key: AWS_ACCESS_KEY...

**Recommendation:** Use environment variables or secure credential storage

**Code:**
```
                # Mock the litellm validate_environment to return missing AWS keys and another key
                mock_validate.return_value = {
                    "missing_keys": ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "ANOTHER_KEY"],
                    "keys_in_environment": False,
                }
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 14. 🔴 Hardcoded Credentials

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_aws_credentials.py:159`
**Severity:** CRITICAL
**Category:** security

**Description:** AWS access key: AWS_ACCESS_KEY...

**Recommendation:** Use environment variables or secure credential storage

**Code:**
```

                # AWS credential keys should be removed from missing_keys
                assert "AWS_ACCESS_KEY_ID" not in model.missing_keys
                assert "AWS_SECRET_ACCESS_KEY" not in model.missing_keys
                # But other keys should remain
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 15. 🔴 Command Injection Risk

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:1095`
**Severity:** CRITICAL
**Category:** security

**Description:** subprocess with shell=True: shell=True...

**Recommendation:** Avoid shell=True and use parameterized commands

**Code:**
```
                try:
                    result = subprocess.run(
                        self.notifications_command, shell=True, capture_output=True
                    )
                    if result.returncode != 0 and result.stderr:
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 16. 🔴 Command Injection Risk

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:978`
**Severity:** CRITICAL
**Category:** security

**Description:** subprocess with shell=True: shell=True...

**Recommendation:** Avoid shell=True and use parameterized commands

**Code:**
```
                text=True,
                env=env,
                shell=True,
                encoding=self.io.encoding,
                errors="replace",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

## 🟠 HIGH Severity (24 issues)

### 1. 🟠 SQL Injection Risk

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:19`
**Severity:** HIGH
**Category:** security

**Description:** SQL statement with concatenation: SELECT|INSERT|UPDATE|DELETE).*\+.*FROM...

**Recommendation:** Use parameterized queries or prepared statements

**Code:**
```
            (r'(execute|query|exec)\s*\(\s*["\'].*\+.*["\']', "SQL query with string concatenation"),
            (r'(execute|query|exec)\s*\(\s*f["\'].*\{.*\}', "SQL query with f-string interpolation"),
            (r'(SELECT|INSERT|UPDATE|DELETE).*\+.*FROM', "SQL statement with concatenation"),
            (r'\.format\(.*\)\s*\)\s*#.*SQL', "SQL query using .format()"),
            (r'%s.*%(FROM|WHERE|INSERT)', "SQL query with % formatting"),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 2. 🟠 Cross-Site Scripting (XSS) Risk

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:29`
**Severity:** HIGH
**Category:** security

**Description:** React dangerouslySetInnerHTML usage: dangerouslySetInnerHTML...

**Recommendation:** Sanitize user input and use safe DOM manipulation methods

**Code:**
```
            (r'document\.write\(.*\+', "document.write with concatenation"),
            (r'\.html\(.*\+', "jQuery .html() with concatenation"),
            (r'dangerouslySetInnerHTML', "React dangerouslySetInnerHTML usage"),
            (r'v-html\s*=', "Vue v-html directive"),
        ]
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 3. 🟠 Cross-Site Scripting (XSS) Risk

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:29`
**Severity:** HIGH
**Category:** security

**Description:** React dangerouslySetInnerHTML usage: dangerouslySetInnerHTML...

**Recommendation:** Sanitize user input and use safe DOM manipulation methods

**Code:**
```
            (r'document\.write\(.*\+', "document.write with concatenation"),
            (r'\.html\(.*\+', "jQuery .html() with concatenation"),
            (r'dangerouslySetInnerHTML', "React dangerouslySetInnerHTML usage"),
            (r'v-html\s*=', "Vue v-html directive"),
        ]
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 4. 🟠 Path Traversal Risk

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:57`
**Severity:** HIGH
**Category:** security

**Description:** File operation with user input: read|write).*user.*input', "File operation with us...

**Recommendation:** Validate and sanitize file paths, use os.path.normpath()

**Code:**
```
            (r'\.\./', "Relative path traversal"),
            (r'\.\.\\', "Relative path traversal (Windows)"),
            (r'(read|write).*user.*input', "File operation with user input"),
        ]

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 5. 🟠 Authentication/Authorization Issue

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:88`
**Severity:** HIGH
**Category:** security

**Description:** Authentication disabled: disable.*auth', "Auth...

**Recommendation:** Use secure authentication frameworks and proper access control

**Code:**
```
            (r'admin\s*=\s*True', "Hardcoded admin flag"),
            (r'is_authenticated\s*=\s*True', "Hardcoded authentication bypass"),
            (r'disable.*auth', "Authentication disabled"),
        ]

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 6. 🟠 Path Traversal Risk

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/report_generator.py:306`
**Severity:** HIGH
**Category:** security

**Description:** Relative path traversal: ../...

**Recommendation:** Validate and sanitize file paths, use os.path.normpath()

**Code:**
```

        # Show first and last parts with ...
        return f"{parts[0]}/.../{'/'.join(parts[-2:])}"

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 7. 🟠 Path Traversal Risk

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/tsl_pack_langs.py:44`
**Severity:** HIGH
**Category:** security

**Description:** Relative path traversal: ../...

**Recommendation:** Validate and sanitize file paths, use os.path.normpath()

**Code:**
```
def main():
    # Path to the language definitions file
    lang_def_path = "../../tmp/tree-sitter-language-pack/sources/language_definitions.json"

    # Path to store the tags.scm files
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 8. 🟠 Path Traversal Risk

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/tsl_pack_langs.py:44`
**Severity:** HIGH
**Category:** security

**Description:** Relative path traversal: ../...

**Recommendation:** Validate and sanitize file paths, use os.path.normpath()

**Code:**
```
def main():
    # Path to the language definitions file
    lang_def_path = "../../tmp/tree-sitter-language-pack/sources/language_definitions.json"

    # Path to store the tags.scm files
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 9. 🟠 Path Traversal Risk

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2428`
**Severity:** HIGH
**Category:** security

**Description:** Relative path traversal (Windows): ..\...

**Recommendation:** Validate and sanitize file paths, use os.path.normpath()

**Code:**
```
        formatter.display_issue_details(issue)

        self.io.tool_output("\n🔍 Generating implementation plan...\n")

        # Build prompt from issue details
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 10. 🟠 Path Traversal Risk

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2828`
**Severity:** HIGH
**Category:** security

**Description:** Relative path traversal (Windows): ..\...

**Recommendation:** Validate and sanitize file paths, use os.path.normpath()

**Code:**
```
                return

            self.io.tool_output("🔍 Reviewing changes...\n")

            # Build prompt for LLM
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 11. 🟠 Path Traversal Risk

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2996`
**Severity:** HIGH
**Category:** security

**Description:** Relative path traversal (Windows): ..\...

**Recommendation:** Validate and sanitize file paths, use os.path.normpath()

**Code:**
```
            commit_log = "\n".join([f"- {c.split('|')[3]} ({c.split('|')[0]})" for c in commits])

            self.io.tool_output("🔍 Analyzing recent work...\n")

            # Build prompt for LLM
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 12. 🟠 Path Traversal Risk

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3097`
**Severity:** HIGH
**Category:** security

**Description:** Relative path traversal (Windows): ..\...

**Recommendation:** Validate and sanitize file paths, use os.path.normpath()

**Code:**
```

        try:
            self.io.tool_output("🔍 Planning implementation...\n")

            # Build context from FlacoAI.md if available
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 13. 🟠 Path Traversal Risk

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3147`
**Severity:** HIGH
**Category:** security

**Description:** Relative path traversal (Windows): ..\...

**Recommendation:** Validate and sanitize file paths, use os.path.normpath()

**Code:**
```
            from pathlib import Path

            self.io.tool_output("🔍 Analyzing codebase structure...\n")

            # Get project structure
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 14. 🟠 Path Traversal Risk

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/doc_generators/changelog_generator.py:253`
**Severity:** HIGH
**Category:** security

**Description:** Relative path traversal: ../...

**Recommendation:** Validate and sanitize file paths, use os.path.normpath()

**Code:**
```
                    # Add to list
                    short_hash = commit['hash'][:7]
                    lines.append(f"- {message} ([`{short_hash}`](../../commit/{commit['hash']}))")

                lines.append("")
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 15. 🟠 Path Traversal Risk

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/doc_generators/changelog_generator.py:253`
**Severity:** HIGH
**Category:** security

**Description:** Relative path traversal: ../...

**Recommendation:** Validate and sanitize file paths, use os.path.normpath()

**Code:**
```
                    # Add to list
                    short_hash = commit['hash'][:7]
                    lines.append(f"- {message} ([`{short_hash}`](../../commit/{commit['hash']}))")

                lines.append("")
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 16. 🟠 Potential Memory Leak

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/copypaste.py:64`
**Severity:** HIGH
**Category:** performance

**Description:** Infinite loop without break

**Recommendation:** Implement proper cleanup, use weak references, or bound caches

**Code:**
```

    try:
        watcher.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped watching clipboard")
```

---

### 17. 🟠 Potential Memory Leak

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:636`
**Severity:** HIGH
**Category:** performance

**Description:** Infinite loop without break

**Recommendation:** Implement proper cleanup, use weak references, or bound caches

**Code:**
```
                # In normal mode, Alt+Enter adds a newline
                event.current_buffer.insert_text("\n")

        while True:
            if multiline_input:
                show = self.prompt_prefix

```

---

### 18. 🟠 Potential Memory Leak

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:874`
**Severity:** HIGH
**Category:** performance

**Description:** Infinite loop without break

**Recommendation:** Implement proper cleanup, use weak references, or bound caches

**Code:**
```
            res = group.preference
            self.user_input(f"{question}{res}", log_only=False)
        else:
            while True:
                try:
                    if self.prompt_session:
                        res = self.prompt_session.prompt(
```

---

### 19. 🟠 Potential Memory Leak

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:393`
**Severity:** HIGH
**Category:** performance

**Description:** Unbounded cache

**Recommendation:** Implement proper cleanup, use weak references, or bound caches

**Code:**
```
        self.commit_before_message = []
        self.flacoai_commit_hashes = set()
        self.rejected_urls = set()
        self.abs_root_path_cache = {}

        self.auto_copy_context = auto_copy_context
        self.auto_accept_architect = auto_accept_architect
```

---

### 20. 🟠 Potential Memory Leak

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:950`
**Severity:** HIGH
**Category:** performance

**Description:** Infinite loop without break

**Recommendation:** Implement proper cleanup, use weak references, or bound caches

**Code:**
```
                self.io.user_input(with_message)
                self.run_one(with_message, preproc)
                return self.partial_response_content
            while True:
                try:
                    if not self.io.placeholder:
                        self.copy_context()
```

---

### 21. 🟠 Potential Memory Leak

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1525`
**Severity:** HIGH
**Category:** performance

**Description:** Infinite loop without break

**Recommendation:** Implement proper cleanup, use weak references, or bound caches

**Code:**
```
        exhausted = False
        interrupted = False
        try:
            while True:
                try:
                    yield from self.send(messages, functions=self.functions)
                    break
```

---

### 22. 🟠 Potential Memory Leak

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:1197`
**Severity:** HIGH
**Category:** performance

**Description:** Infinite loop without break

**Recommendation:** Implement proper cleanup, use weak references, or bound caches

**Code:**
```

    analytics.event("cli session", main_model=main_model, edit_format=main_model.edit_format)

    while True:
        try:
            coder.ok_to_warm_cache = bool(args.cache_keepalive_pings)
            coder.run()
```

---

### 23. 🟠 Potential Memory Leak

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:88`
**Severity:** HIGH
**Category:** performance

**Description:** Infinite loop without break

**Recommendation:** Implement proper cleanup, use weak references, or bound caches

**Code:**
```
    total_pages = (total_count + per_page - 1) // per_page

    with tqdm(total=total_pages, desc="Collecting issues", unit="page") as pbar:
        while True:
            response = requests.get(
                f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/issues",
                headers=headers,
```

---

### 24. 🟠 Potential Memory Leak

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:235`
**Severity:** HIGH
**Category:** performance

**Description:** Infinite loop without break

**Recommendation:** Implement proper cleanup, use weak references, or bound caches

**Code:**
```
        )
        spinner = Spinner("Installing...")

        while True:
            char = process.stdout.read(1)
            if not char:
                break
```

---

## 🟡 MEDIUM Severity (494 issues)

### 1. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/rsync.sh:10`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): DES...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
fi

DEST="$1"
REPO_ROOT="$(git rev-parse --show-toplevel)"

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 2. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/rsync.sh:20`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): DES...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

# Create remote directory if needed
ssh "$DEST" "mkdir -p ~/flacoai"

sync_repo() {
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 3. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/rsync.sh:27`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): DES...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
          --exclude-from="$EXCLUDE_FILE" \
          "$REPO_ROOT/" \
          "$DEST:~/flacoai/" || sleep 0.1
    
    rsync -av .env .gitignore .flacoai.model.settings.yml "$DEST:~/flacoai/." || sleep 0.1
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 4. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/rsync.sh:29`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): DES...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
          "$DEST:~/flacoai/" || sleep 0.1
    
    rsync -av .env .gitignore .flacoai.model.settings.yml "$DEST:~/flacoai/." || sleep 0.1

    echo Done syncing, waiting.
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 5. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/mdstream.py:26`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
electronic typesetting, remaining essentially unchanged. It was popularised in
the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
and more recently with desktop publishing software like Aldus PageMaker
including versions of Lorem Ipsum.

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 6. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/base_analyzer.py:35`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
    category: Category
    title: str
    description: str
    recommendation: str
    code_snippet: Optional[str] = None
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 7. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/base_analyzer.py:59`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            "category": self.category.value,
            "title": self.title,
            "description": self.description,
            "recommendation": self.recommendation,
            "code_snippet": self.code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 8. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/base_analyzer.py:59`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            "category": self.category.value,
            "title": self.title,
            "description": self.description,
            "recommendation": self.recommendation,
            "code_snippet": self.code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 9. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:246`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            del repo_map

    def test_get_repo_map_excludes_added_files(self):
        # Create a temporary directory with sample files for testing
        test_files = [
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 10. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/premium/crash_prediction_analyzer.py:96`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.QUALITY,
                title=f"Chained force unwraps detected ({unwrap_count} levels) - {likelihood}% crash risk",
                description=f"Multiple chained force unwraps create a compound crash risk. "
                           f"Each ! can fail independently, making this {likelihood}% likely to crash "
                           f"if any value in the chain is nil.",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 11. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/premium/crash_prediction_analyzer.py:151`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title="Unchecked array access - 60% crash risk",
                        description=f"Array subscript access '{match.group(0)}' without bounds checking. "
                                   f"Will crash with 'Index out of range' if index is invalid.",
                        recommendation=f"Add bounds checking:\n"
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 12. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/premium/crash_prediction_analyzer.py:184`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.QUALITY,
                    title=f"Deep optional chain ({depth} levels) - crash masking risk",
                    description=f"Optional chain with {depth} levels may mask underlying nil issues. "
                               f"While it won't crash, it silently fails and returns nil, "
                               f"which could cause crashes downstream.",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 13. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/premium/crash_prediction_analyzer.py:215`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.QUALITY,
                title="Force cast detected - 70% crash risk",
                description=f"Force cast 'as! {target_type}' will crash if the cast fails. "
                           f"This is a common source of runtime crashes.",
                recommendation=f"Use conditional cast with guard:\n"
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 14. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/premium/crash_prediction_analyzer.py:245`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.QUALITY,
                    title="Unhandled async throwing call - 55% crash risk",
                    description="Using 'await' without 'try' on a throwing function. "
                               "This will crash if the function throws an error.",
                    recommendation="Add try-catch:\ntry await function()\n"
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 15. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/premium/crash_prediction_analyzer.py:284`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                            category=Category.QUALITY,
                            title="Collection mutation during iteration - 90% crash risk",
                            description=f"Modifying collection '{collection_name}' while iterating over it. "
                                       f"This causes 'Collection was mutated while being enumerated' crash.",
                            recommendation=f"Iterate over a copy:\nfor item in {collection_name}.map({{ $0 }}) {{\n"
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 16. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/premium/crash_prediction_analyzer.py:319`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.PERFORMANCE,
                    title="Missing [weak self] in escaping closure - retain cycle risk",
                    description="Closure captures self strongly, creating a retain cycle risk. "
                               "While not an immediate crash, this causes memory leaks that "
                               "eventually lead to app termination.",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 17. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:62`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak hash algorithm (MD5): MD5...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        # Insecure crypto patterns
        self.crypto_patterns = [
            (r'MD5|md5', "Weak hash algorithm (MD5)"),
            (r'SHA1|sha1(?!\.)', "Weak hash algorithm (SHA1)"),
            (r'DES|des_', "Weak encryption (DES)"),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 18. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:62`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak hash algorithm (MD5): md5...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        # Insecure crypto patterns
        self.crypto_patterns = [
            (r'MD5|md5', "Weak hash algorithm (MD5)"),
            (r'SHA1|sha1(?!\.)', "Weak hash algorithm (SHA1)"),
            (r'DES|des_', "Weak encryption (DES)"),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 19. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:62`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak hash algorithm (MD5): MD5...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        # Insecure crypto patterns
        self.crypto_patterns = [
            (r'MD5|md5', "Weak hash algorithm (MD5)"),
            (r'SHA1|sha1(?!\.)', "Weak hash algorithm (SHA1)"),
            (r'DES|des_', "Weak encryption (DES)"),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 20. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:112`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak hash algorithm (MD5): MD5...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            (r'kCCAlgorithm3DES', "Weak encryption algorithm (3DES)"),
            (r'kCCAlgorithmRC4', "Weak encryption algorithm (RC4)"),
            (r'CC_MD5', "Weak hash algorithm (MD5)"),
            (r'CC_SHA1', "Weak hash algorithm (SHA1)"),
            (r'Insecure\.SHA1', "Weak hash algorithm (SHA1)"),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 21. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:112`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak hash algorithm (MD5): MD5...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            (r'kCCAlgorithm3DES', "Weak encryption algorithm (3DES)"),
            (r'kCCAlgorithmRC4', "Weak encryption algorithm (RC4)"),
            (r'CC_MD5', "Weak hash algorithm (MD5)"),
            (r'CC_SHA1', "Weak hash algorithm (SHA1)"),
            (r'Insecure\.SHA1', "Weak hash algorithm (SHA1)"),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 22. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:63`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak hash algorithm (SHA1): SHA1...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        self.crypto_patterns = [
            (r'MD5|md5', "Weak hash algorithm (MD5)"),
            (r'SHA1|sha1(?!\.)', "Weak hash algorithm (SHA1)"),
            (r'DES|des_', "Weak encryption (DES)"),
            (r'ECB', "Insecure cipher mode (ECB)"),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 23. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:63`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak hash algorithm (SHA1): sha1...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        self.crypto_patterns = [
            (r'MD5|md5', "Weak hash algorithm (MD5)"),
            (r'SHA1|sha1(?!\.)', "Weak hash algorithm (SHA1)"),
            (r'DES|des_', "Weak encryption (DES)"),
            (r'ECB', "Insecure cipher mode (ECB)"),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 24. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:63`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak hash algorithm (SHA1): SHA1...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        self.crypto_patterns = [
            (r'MD5|md5', "Weak hash algorithm (MD5)"),
            (r'SHA1|sha1(?!\.)', "Weak hash algorithm (SHA1)"),
            (r'DES|des_', "Weak encryption (DES)"),
            (r'ECB', "Insecure cipher mode (ECB)"),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 25. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:113`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak hash algorithm (SHA1): SHA1...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            (r'kCCAlgorithmRC4', "Weak encryption algorithm (RC4)"),
            (r'CC_MD5', "Weak hash algorithm (MD5)"),
            (r'CC_SHA1', "Weak hash algorithm (SHA1)"),
            (r'Insecure\.SHA1', "Weak hash algorithm (SHA1)"),
        ]
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 26. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:113`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak hash algorithm (SHA1): SHA1...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            (r'kCCAlgorithmRC4', "Weak encryption algorithm (RC4)"),
            (r'CC_MD5', "Weak hash algorithm (MD5)"),
            (r'CC_SHA1', "Weak hash algorithm (SHA1)"),
            (r'Insecure\.SHA1', "Weak hash algorithm (SHA1)"),
        ]
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 27. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:114`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak hash algorithm (SHA1): SHA1...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            (r'CC_MD5', "Weak hash algorithm (MD5)"),
            (r'CC_SHA1', "Weak hash algorithm (SHA1)"),
            (r'Insecure\.SHA1', "Weak hash algorithm (SHA1)"),
        ]

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 28. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:114`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak hash algorithm (SHA1): SHA1...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            (r'CC_MD5', "Weak hash algorithm (MD5)"),
            (r'CC_SHA1', "Weak hash algorithm (SHA1)"),
            (r'Insecure\.SHA1', "Weak hash algorithm (SHA1)"),
        ]

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 29. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:64`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): DES...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            (r'MD5|md5', "Weak hash algorithm (MD5)"),
            (r'SHA1|sha1(?!\.)', "Weak hash algorithm (SHA1)"),
            (r'DES|des_', "Weak encryption (DES)"),
            (r'ECB', "Insecure cipher mode (ECB)"),
            (r'Random\(\)', "Insecure random number generator"),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 30. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:64`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            (r'MD5|md5', "Weak hash algorithm (MD5)"),
            (r'SHA1|sha1(?!\.)', "Weak hash algorithm (SHA1)"),
            (r'DES|des_', "Weak encryption (DES)"),
            (r'ECB', "Insecure cipher mode (ECB)"),
            (r'Random\(\)', "Insecure random number generator"),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 31. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:64`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): DES...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            (r'MD5|md5', "Weak hash algorithm (MD5)"),
            (r'SHA1|sha1(?!\.)', "Weak hash algorithm (SHA1)"),
            (r'DES|des_', "Weak encryption (DES)"),
            (r'ECB', "Insecure cipher mode (ECB)"),
            (r'Random\(\)', "Insecure random number generator"),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 32. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:76`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        # Insecure deserialization patterns
        self.deserialization_patterns = [
            (r'pickle\.loads?\(', "Unsafe pickle deserialization"),
            (r'yaml\.load\((?!.*Loader=)', "Unsafe YAML deserialization"),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 33. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:77`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        # Insecure deserialization patterns
        self.deserialization_patterns = [
            (r'pickle\.loads?\(', "Unsafe pickle deserialization"),
            (r'yaml\.load\((?!.*Loader=)', "Unsafe YAML deserialization"),
            (r'jsonpickle\.decode', "Potentially unsafe jsonpickle"),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 34. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:78`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        self.deserialization_patterns = [
            (r'pickle\.loads?\(', "Unsafe pickle deserialization"),
            (r'yaml\.load\((?!.*Loader=)', "Unsafe YAML deserialization"),
            (r'jsonpickle\.decode', "Potentially unsafe jsonpickle"),
            (r'marshal\.loads', "Unsafe marshal deserialization"),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 35. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:80`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            (r'yaml\.load\((?!.*Loader=)', "Unsafe YAML deserialization"),
            (r'jsonpickle\.decode', "Potentially unsafe jsonpickle"),
            (r'marshal\.loads', "Unsafe marshal deserialization"),
        ]

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 36. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:109`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): DES...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        self.ios_weak_crypto_patterns = [
            (r'kCCAlgorithmDES', "Weak encryption algorithm (DES)"),
            (r'kCCAlgorithm3DES', "Weak encryption algorithm (3DES)"),
            (r'kCCAlgorithmRC4', "Weak encryption algorithm (RC4)"),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 37. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:109`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): DES...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        self.ios_weak_crypto_patterns = [
            (r'kCCAlgorithmDES', "Weak encryption algorithm (DES)"),
            (r'kCCAlgorithm3DES', "Weak encryption algorithm (3DES)"),
            (r'kCCAlgorithmRC4', "Weak encryption algorithm (RC4)"),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 38. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:110`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): DES...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        self.ios_weak_crypto_patterns = [
            (r'kCCAlgorithmDES', "Weak encryption algorithm (DES)"),
            (r'kCCAlgorithm3DES', "Weak encryption algorithm (3DES)"),
            (r'kCCAlgorithmRC4', "Weak encryption algorithm (RC4)"),
            (r'CC_MD5', "Weak hash algorithm (MD5)"),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 39. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:110`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): DES...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        self.ios_weak_crypto_patterns = [
            (r'kCCAlgorithmDES', "Weak encryption algorithm (DES)"),
            (r'kCCAlgorithm3DES', "Weak encryption algorithm (3DES)"),
            (r'kCCAlgorithmRC4', "Weak encryption algorithm (RC4)"),
            (r'CC_MD5', "Weak hash algorithm (MD5)"),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 40. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:181`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        results.extend(self._check_patterns(file_path, content, self.crypto_patterns,
                                           "Weak Cryptography", Severity.MEDIUM,
                                           "Use SHA-256 or better, AES with secure modes"))

        results.extend(self._check_patterns(file_path, content, self.csrf_patterns,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 41. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:187`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                                           "Add CSRF tokens to forms and validate on submission"))

        results.extend(self._check_patterns(file_path, content, self.deserialization_patterns,
                                           "Insecure Deserialization", Severity.HIGH,
                                           "Use safe serialization or validate deserialized data"))
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 42. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:188`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        results.extend(self._check_patterns(file_path, content, self.deserialization_patterns,
                                           "Insecure Deserialization", Severity.HIGH,
                                           "Use safe serialization or validate deserialized data"))

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 43. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:189`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        results.extend(self._check_patterns(file_path, content, self.deserialization_patterns,
                                           "Insecure Deserialization", Severity.HIGH,
                                           "Use safe serialization or validate deserialized data"))

        results.extend(self._check_patterns(file_path, content, self.auth_patterns,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 44. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:241`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        results = []

        for pattern, description in patterns:
            matches = self.find_pattern(content, pattern, re.IGNORECASE)

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 45. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:258`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.SECURITY,
                    title=title,
                    description=f"{description}: {matched_text[:50]}...",
                    recommendation=recommendation,
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 46. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:258`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.SECURITY,
                    title=title,
                    description=f"{description}: {matched_text[:50]}...",
                    recommendation=recommendation,
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 47. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:65`
**Severity:** MEDIUM
**Category:** security

**Description:** Insecure cipher mode (ECB): ECB...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            (r'SHA1|sha1(?!\.)', "Weak hash algorithm (SHA1)"),
            (r'DES|des_', "Weak encryption (DES)"),
            (r'ECB', "Insecure cipher mode (ECB)"),
            (r'Random\(\)', "Insecure random number generator"),
        ]
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 48. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:65`
**Severity:** MEDIUM
**Category:** security

**Description:** Insecure cipher mode (ECB): ECB...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            (r'SHA1|sha1(?!\.)', "Weak hash algorithm (SHA1)"),
            (r'DES|des_', "Weak encryption (DES)"),
            (r'ECB', "Insecure cipher mode (ECB)"),
            (r'Random\(\)', "Insecure random number generator"),
        ]
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 49. 🟡 Sensitive Data in Logs

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:93`
**Severity:** MEDIUM
**Category:** security

**Description:** Password in logs: log|print|console\.log).*password', "Password...

**Recommendation:** Remove sensitive data from log statements

**Code:**
```
        # Logging sensitive data patterns
        self.logging_patterns = [
            (r'(log|print|console\.log).*password', "Password in logs"),
            (r'(log|print|console\.log).*token', "Token in logs"),
            (r'(log|print|console\.log).*secret', "Secret in logs"),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 50. 🟡 Sensitive Data in Logs

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:94`
**Severity:** MEDIUM
**Category:** security

**Description:** Token in logs: log|print|console\.log).*token', "Token...

**Recommendation:** Remove sensitive data from log statements

**Code:**
```
        self.logging_patterns = [
            (r'(log|print|console\.log).*password', "Password in logs"),
            (r'(log|print|console\.log).*token', "Token in logs"),
            (r'(log|print|console\.log).*secret', "Secret in logs"),
            (r'(log|print|console\.log).*api[_-]?key', "API key in logs"),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 51. 🟡 Sensitive Data in Logs

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:95`
**Severity:** MEDIUM
**Category:** security

**Description:** Secret in logs: log|print|console\.log).*secret', "Secret...

**Recommendation:** Remove sensitive data from log statements

**Code:**
```
            (r'(log|print|console\.log).*password', "Password in logs"),
            (r'(log|print|console\.log).*token', "Token in logs"),
            (r'(log|print|console\.log).*secret', "Secret in logs"),
            (r'(log|print|console\.log).*api[_-]?key', "API key in logs"),
        ]
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 52. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_prompts.py:13`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

    lazy_prompt = """You are diligent and tireless!
You NEVER leave comments describing code without implementing it!
You always COMPLETELY IMPLEMENT the needed code!
"""
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 53. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:209`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a celebration SVG for flacoai's 30K GitHub stars"
    )
    parser.add_argument(
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 54. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/integrations/jira_client.py:60`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        project: str,
        summary: str,
        description: str,
        issue_type: str = "Task",
        priority: Optional[str] = None,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 55. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/integrations/jira_client.py:71`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            project: Project key (e.g., "PROJ")
            summary: Issue summary/title
            description: Issue description
            issue_type: Issue type (Task, Bug, Story, etc.)
            priority: Priority level (optional)
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 56. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/integrations/jira_client.py:71`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            project: Project key (e.g., "PROJ")
            summary: Issue summary/title
            description: Issue description
            issue_type: Issue type (Task, Bug, Story, etc.)
            priority: Priority level (optional)
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 57. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/integrations/jira_client.py:83`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            "project": {"key": project},
            "summary": summary,
            "description": description,
            "issuetype": {"name": issue_type},
        }
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 58. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/integrations/jira_client.py:83`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            "project": {"key": project},
            "summary": summary,
            "description": description,
            "issuetype": {"name": issue_type},
        }
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 59. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/integrations/jira_client.py:279`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): DES...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            jql += f' AND status = "{status}"'

        jql += " ORDER BY updated DESC"

        return self.search_issues(jql)
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 60. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:91`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
    """
    # No API keys found - Offer OpenRouter OAuth
    io.tool_output("OpenRouter provides free and paid access to many LLMs.")
    # Use confirm_ask which handles non-interactive cases
    if io.confirm_ask(
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 61. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:166`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

# PKCE code generation
def generate_pkce_codes():
    code_verifier = secrets.token_urlsafe(64)
    hasher = hashlib.sha256()
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 62. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:187`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            timeout=30,  # Add a timeout
        )
        response.raise_for_status()  # Raise exception for bad status codes (4xx or 5xx)
        data = response.json()
        api_key = data.get("key")
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 63. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:302`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

    # Generate codes and URL
    code_verifier, code_challenge = generate_pkce_codes()
    auth_url_base = "https://openrouter.ai/auth"
    auth_params = {
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 64. 🟡 Sensitive Data in Logs

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:412`
**Severity:** MEDIUM
**Category:** security

**Description:** API key in logs: print("Warning: OPENROUTER_API_KEY...

**Recommendation:** Remove sensitive data from log statements

**Code:**
```
    # (though start_openrouter_oauth_flow doesn't check this itself)
    if "OPENROUTER_API_KEY" in os.environ:
        print("Warning: OPENROUTER_API_KEY is already set in environment.")
        # del os.environ["OPENROUTER_API_KEY"] # Optionally unset it for testing

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 65. 🟡 Sensitive Data in Logs

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:419`
**Severity:** MEDIUM
**Category:** security

**Description:** API key in logs: print(f"Obtained API Key (first 5 chars): {api_key...

**Recommendation:** Remove sensitive data from log statements

**Code:**
```
    if api_key:
        print("\nOAuth flow completed successfully!")
        print(f"Obtained API Key (first 5 chars): {api_key[:5]}...")
        # Be careful printing the key, even partially
    else:
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 66. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/screenshot_prompts.py:9`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
    """Prompts for converting UI screenshots to SwiftUI code."""

    main_system = """You are an expert SwiftUI developer specializing in converting UI designs to code.

Your role is to analyze UI screenshots and generate accurate SwiftUI code that recreates the design.
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 67. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/screenshot_prompts.py:11`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
    main_system = """You are an expert SwiftUI developer specializing in converting UI designs to code.

Your role is to analyze UI screenshots and generate accurate SwiftUI code that recreates the design.

When analyzing screenshots:
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 68. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/screenshot_prompts.py:54`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
When you can't determine exact values:
- Use sensible defaults based on iOS HIG
- Add comments like "// Adjust color to match design"
- Suggest using design tokens or constants
"""
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 69. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/screenshot_prompts.py:55`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
- Use sensible defaults based on iOS HIG
- Add comments like "// Adjust color to match design"
- Suggest using design tokens or constants
"""

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 70. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/screenshot_prompts.py:86`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
- Blue accent color for button
- Standard iOS spacing
- Clean, minimal design

Here's the generated SwiftUI code:
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 71. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/args.py:37`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
def get_parser(default_config_files, git_root):
    parser = configargparse.ArgumentParser(
        description="aider is AI pair programming in your terminal",
        add_config_file_help=True,
        default_config_files=default_config_files,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 72. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/args.py:174`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        "--architect",
        action="store_const",
        dest="edit_format",
        const="architect",
        help="Use architect edit format for the main chat",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 73. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/args.py:463`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        help=(
            "Attribute flacoai code changes in the git author name (default: True). If explicitly set"
            " to True, overrides --attribute-co-authored-by precedence."
        ),
    )
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 74. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/args.py:472`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        help=(
            "Attribute flacoai commits in the git committer name (default: True). If explicitly set"
            " to True, overrides --attribute-co-authored-by precedence for flacoai edits."
        ),
    )
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 75. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/args.py:643`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

    ##########
    group = parser.add_argument_group("Modes")
    group.add_argument(
        "--message",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 76. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/problem_stats.py:172`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
    exercise_stats.sort(
        key=lambda x: (-x[2], x[1])
    )  # -x[2] for descending solve rate, x[1] for ascending exercise name

    # Calculate max lengths for alignment after cleaning up paths
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 77. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/problem_stats.py:313`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        if dst_dir.exists():
            print(f"\nError: Destination directory {dst_dir} already exists")
            return

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 78. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_symbols_analyzer.py:223`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title="Potentially Invalid SF Symbol",
                        description=f"Symbol '{symbol_name}' doesn't match common SF Symbols patterns",
                        recommendation="Verify this SF Symbol exists in SF Symbols app or Apple documentation",
                        code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 79. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_symbols_analyzer.py:252`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title="Deprecated SF Symbol",
                        description=f"Symbol '{deprecated}' is deprecated or discouraged",
                        recommendation=suggestion,
                        code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 80. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_symbols_analyzer.py:288`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title="Incorrect SF Symbol Name",
                        description=f"'{name}' is not a valid SF Symbol",
                        recommendation=f"Use SF Symbol: '{self.common_mistakes[name]}'",
                        code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 81. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_symbols_analyzer.py:309`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        ]

        for pattern, description in hardcoded_patterns:
            matches = self.find_pattern(content, pattern, re.IGNORECASE)

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 82. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_symbols_analyzer.py:326`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.QUALITY,
                    title="Hardcoded Icon Asset",
                    description=description,
                    recommendation="Consider using SF Symbols for better scalability and consistency",
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 83. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_symbols_analyzer.py:326`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.QUALITY,
                    title="Hardcoded Icon Asset",
                    description=description,
                    recommendation="Consider using SF Symbols for better scalability and consistency",
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 84. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/custom_rules_analyzer.py:191`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=category,
                    title=name,
                    description=message,
                    recommendation=recommendation,
                    code_snippet=snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 85. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/custom_rules_analyzer.py:240`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=category,
                    title=name,
                    description=message,
                    recommendation=recommendation,
                    code_snippet=line.strip(),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 86. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/custom_rules_analyzer.py:284`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=category,
                title=name,
                description=message,
                recommendation=recommendation,
                code_snippet="(entire file)",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 87. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1942`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak hash algorithm (SHA1): sha1...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            content=self.partial_response_content,
        )
        resp_hash = hashlib.sha1(json.dumps(resp_hash, sort_keys=True).encode())
        self.chat_completion_response_hashes.append(resp_hash.hexdigest())

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 88. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1544`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    if not should_retry:
                        self.mdstream = None
                        self.check_and_open_urls(err, ex_info.description)
                        break

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 89. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1548`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

                    err_msg = str(err)
                    if ex_info.description:
                        self.io.tool_warning(err_msg)
                        self.io.tool_error(ex_info.description)
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 90. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1550`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    if ex_info.description:
                        self.io.tool_warning(err_msg)
                        self.io.tool_error(ex_info.description)
                    else:
                        self.io.tool_error(err_msg)
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 91. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/patch_coder.py:213`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
    """
    A coder that uses a custom patch format for code modifications,
    inspired by the format described in tmp.gpt41edits.txt.
    Applies patches using logic adapted from the reference apply_patch.py script.
    """
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 92. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/patch_coder.py:652`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        orig_lines = text.splitlines()  # Use splitlines to handle endings consistently
        dest_lines: List[str] = []
        current_orig_line_idx = 0  # Tracks index in orig_lines processed so far

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 93. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/patch_coder.py:671`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

            # Add lines from original file between the last chunk and this one
            dest_lines.extend(orig_lines[current_orig_line_idx:chunk_start_index])

            # Verify that the lines to be deleted actually match the original file content
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 94. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/patch_coder.py:694`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

            # Add the inserted lines from the chunk
            dest_lines.extend(chunk.ins_lines)

            # Advance the original line index past the lines processed (deleted lines)
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 95. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/patch_coder.py:700`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        # Add any remaining lines from the original file after the last chunk
        dest_lines.extend(orig_lines[current_orig_line_idx:])

        # Join lines and ensure a single trailing newline
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 96. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/patch_coder.py:703`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        # Join lines and ensure a single trailing newline
        result = "\n".join(dest_lines)
        if result or orig_lines:  # Add newline unless result is empty and original was empty
            result += "\n"
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 97. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:18`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

    def generic_visit(self, node):
        for child in ast.iter_child_nodes(node):
            child.parent = node
        return super(ParentNodeTransformer, self).generic_visit(node)
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 98. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:24`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

def verify_full_func_at_top_level(tree, func, func_children):
    func_nodes = [
        item for item in ast.walk(tree) if isinstance(item, ast.FunctionDef) and item.name == func
    ]
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 99. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:27`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        item for item in ast.walk(tree) if isinstance(item, ast.FunctionDef) and item.name == func
    ]
    assert func_nodes, f"Function {func} not found"

    for func_node in func_nodes:
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 100. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:29`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
    assert func_nodes, f"Function {func} not found"

    for func_node in func_nodes:
        if not isinstance(func_node.parent, ast.Module):
            continue
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 101. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:66`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        file_contents = file.read()
    tree = ast.parse(file_contents)
    ParentNodeTransformer().visit(tree)  # Set parent attribute for all nodes

    verify_full_func_at_top_level(tree, func, func_children)
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 102. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:97`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            if not self_used and not super_used:
                # Calculate the number of child nodes in the function
                num_child_nodes = sum(1 for _ in ast.walk(node))
                res = (
                    self.parent_class_name,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 103. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:102`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    node.name,
                    self.num_class_children,
                    num_child_nodes,
                )
                self.non_self_methods.append(res)
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 104. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/report_generator.py:249`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        # Description
        lines.append(f"**Description:** {finding.description}")
        lines.append("")

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 105. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/report_generator.py:249`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        # Description
        lines.append(f"**Description:** {finding.description}")
        lines.append("")

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 106. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:33`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
    """Thanks for trying flacoai and filing this issue.

This looks like a duplicate of #{oldest_issue_number}. Please see the comments there for more information, and feel free to continue the discussion within that issue.

I'm going to close this issue for now. But please let me know if you think this is actually a distinct issue and I will reopen this issue."""  # noqa
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 107. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:87`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
    total_pages = (total_count + per_page - 1) // per_page

    with tqdm(total=total_pages, desc="Collecting issues", unit="page") as pbar:
        while True:
            response = requests.get(
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 108. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:114`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```


def find_oldest_issue(subject, all_issues):
    oldest_issue = None
    oldest_date = datetime.now()
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 109. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:115`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

def find_oldest_issue(subject, all_issues):
    oldest_issue = None
    oldest_date = datetime.now()

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 110. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:116`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
def find_oldest_issue(subject, all_issues):
    oldest_issue = None
    oldest_date = datetime.now()

    for issue in all_issues:
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 111. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:121`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        if issue["title"] == subject and not has_been_reopened(issue["number"]):
            created_at = datetime.strptime(issue["created_at"], "%Y-%m-%dT%H:%M:%SZ")
            if created_at < oldest_date:
                oldest_date = created_at
                oldest_issue = issue
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 112. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:122`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            created_at = datetime.strptime(issue["created_at"], "%Y-%m-%dT%H:%M:%SZ")
            if created_at < oldest_date:
                oldest_date = created_at
                oldest_issue = issue

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 113. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:123`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            if created_at < oldest_date:
                oldest_date = created_at
                oldest_issue = issue

    return oldest_issue
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 114. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:125`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                oldest_issue = issue

    return oldest_issue


```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 115. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:128`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```


def comment_and_close_duplicate(issue, oldest_issue):
    # Skip if issue is labeled as priority
    if "priority" in [label["name"] for label in issue["labels"]]:
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 116. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:139`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
    close_url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/issues/{issue['number']}"

    comment_body = DUPLICATE_COMMENT.format(oldest_issue_number=oldest_issue["number"])

    # Post comment
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 117. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:139`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
    close_url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/issues/{issue['number']}"

    comment_body = DUPLICATE_COMMENT.format(oldest_issue_number=oldest_issue["number"])

    # Post comment
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 118. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:403`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
    print("Looking for duplicate issues (skipping reopened issues)...")
    for subject, issues in grouped_open_issues.items():
        oldest_issue = find_oldest_issue(subject, all_issues)
        if not oldest_issue:
            continue
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 119. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:403`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
    print("Looking for duplicate issues (skipping reopened issues)...")
    for subject, issues in grouped_open_issues.items():
        oldest_issue = find_oldest_issue(subject, all_issues)
        if not oldest_issue:
            continue
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 120. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:404`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
    for subject, issues in grouped_open_issues.items():
        oldest_issue = find_oldest_issue(subject, all_issues)
        if not oldest_issue:
            continue

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 121. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:408`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        related_issues = set(issue["number"] for issue in issues)
        related_issues.add(oldest_issue["number"])
        if len(related_issues) <= 1:
            continue
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 122. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:419`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        print(
            f"Oldest issue: #{oldest_issue['number']}: {oldest_issue['comments']} comments"
            f" {oldest_issue['html_url']} ({oldest_issue['state']})"
        )
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 123. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:419`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        print(
            f"Oldest issue: #{oldest_issue['number']}: {oldest_issue['comments']} comments"
            f" {oldest_issue['html_url']} ({oldest_issue['state']})"
        )
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 124. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:419`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        print(
            f"Oldest issue: #{oldest_issue['number']}: {oldest_issue['comments']} comments"
            f" {oldest_issue['html_url']} ({oldest_issue['state']})"
        )
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 125. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:420`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        print(
            f"Oldest issue: #{oldest_issue['number']}: {oldest_issue['comments']} comments"
            f" {oldest_issue['html_url']} ({oldest_issue['state']})"
        )

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 126. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:420`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        print(
            f"Oldest issue: #{oldest_issue['number']}: {oldest_issue['comments']} comments"
            f" {oldest_issue['html_url']} ({oldest_issue['state']})"
        )

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 127. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:430`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        for issue in issues:
            if issue["number"] != oldest_issue["number"]:
                comment_and_close_duplicate(issue, oldest_issue)

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 128. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:431`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        for issue in issues:
            if issue["number"] != oldest_issue["number"]:
                comment_and_close_duplicate(issue, oldest_issue)

        if oldest_issue["state"] == "open":
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 129. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:433`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                comment_and_close_duplicate(issue, oldest_issue)

        if oldest_issue["state"] == "open":
            print(f"Oldest issue #{oldest_issue['number']} left open")

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 130. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:434`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        if oldest_issue["state"] == "open":
            print(f"Oldest issue #{oldest_issue['number']} left open")


```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 131. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:434`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        if oldest_issue["state"] == "open":
            print(f"Oldest issue #{oldest_issue['number']} left open")


```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 132. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:438`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

def main():
    parser = argparse.ArgumentParser(description="Handle duplicate GitHub issues")
    parser.add_argument(
        "--yes", action="store_true", help="Automatically close duplicates without prompting"
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 133. 🟡 Sensitive Data in Logs

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:445`
**Severity:** MEDIUM
**Category:** security

**Description:** Token in logs: print("Error: Missing GITHUB_TOKEN...

**Recommendation:** Remove sensitive data from log statements

**Code:**
```

    if not TOKEN:
        print("Error: Missing GITHUB_TOKEN environment variable. Please check your .env file.")
        return

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 134. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/template_engine.py:21`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            "login": {
                "file": "login_view.swift.template",
                "description": "Login view with email/password fields",
                "required_vars": ["VIEW_NAME", "APP_NAME"],
                "optional_vars": [],
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 135. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/template_engine.py:27`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            "settings": {
                "file": "settings_view.swift.template",
                "description": "Settings view with toggles and navigation",
                "required_vars": ["VIEW_NAME", "APP_NAME"],
                "optional_vars": [],
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 136. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/template_engine.py:33`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            "list": {
                "file": "list_view.swift.template",
                "description": "List view with search and add functionality",
                "required_vars": [
                    "VIEW_NAME",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 137. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/template_engine.py:47`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            "detail": {
                "file": "detail_view.swift.template",
                "description": "Detail view for displaying item information",
                "required_vars": [
                    "VIEW_NAME",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 138. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/template_engine.py:52`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): DES...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    "ITEM_TYPE",
                    "TITLE_FIELD",
                    "DESCRIPTION_FIELD",
                    "DATE_FIELD",
                    "STATUS_FIELD",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 139. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/template_engine.py:61`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            "tabview": {
                "file": "tabview.swift.template",
                "description": "TabView with 4 tabs",
                "required_vars": [
                    "VIEW_NAME",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 140. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/template_engine.py:93`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        """
        return [
            {"name": name, "description": info["description"]}
            for name, info in self.templates.items()
        ]
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 141. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/template_engine.py:93`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        """
        return [
            {"name": name, "description": info["description"]}
            for name, info in self.templates.items()
        ]
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 142. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/template_engine.py:207`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): DES...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            variables["ITEM_TYPE"] = item_type
            variables["TITLE_FIELD"] = "title"
            variables["DESCRIPTION_FIELD"] = "description"
            variables["DATE_FIELD"] = "createdAt"
            variables["STATUS_FIELD"] = "status"
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 143. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/template_engine.py:207`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            variables["ITEM_TYPE"] = item_type
            variables["TITLE_FIELD"] = "title"
            variables["DESCRIPTION_FIELD"] = "description"
            variables["DATE_FIELD"] = "createdAt"
            variables["STATUS_FIELD"] = "status"
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 144. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/template_engine.py:322`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            template_name: Name of the template to use
            prompt: User's generation request
            custom_vars: Optional dictionary of custom variable overrides

        Returns:
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 145. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/template_engine.py:351`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
    print("Available templates:")
    for template in engine.list_templates():
        print(f"  - {template['name']}: {template['description']}")

    print("\n" + "=" * 80 + "\n")
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 146. 🟡 Sensitive Data in Logs

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/template_engine.py:21`
**Severity:** MEDIUM
**Category:** security

**Description:** Password in logs: Login view with email/password...

**Recommendation:** Remove sensitive data from log statements

**Code:**
```
            "login": {
                "file": "login_view.swift.template",
                "description": "Login view with email/password fields",
                "required_vars": ["VIEW_NAME", "APP_NAME"],
                "optional_vars": [],
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 147. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/homepage.py:537`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
    ensure_cache_dir()

    parser = argparse.ArgumentParser(description="Get total downloads and GitHub stars for flacoai")
    parser.add_argument(
        "--api-key",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 148. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:81`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                            category=Category.QUALITY,
                            title="Touch Target Too Small",
                            description=f"Interactive element has size {width}x{height}, below HIG minimum of 44x44 points",
                            recommendation=f"Increase touch target to at least 44x44 points for better accessibility",
                            code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 149. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:85`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                            code_snippet=code_snippet,
                            references=[
                                "https://developer.apple.com/design/human-interface-guidelines/layout",
                            ],
                        )
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 150. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:117`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.ARCHITECTURE,
                    title="Too Many Tab Items",
                    description=f"TabView has {tab_count} items, exceeds HIG recommendation of 5",
                    recommendation="Limit tabs to 5 items or use a different navigation pattern",
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 151. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:121`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    code_snippet=code_snippet,
                    references=[
                        "https://developer.apple.com/design/human-interface-guidelines/tab-bars",
                    ],
                )
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 152. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:144`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.QUALITY,
                title="Multiple Modal Presentations",
                description=f"File has {len(matches)} modal presentation modifiers",
                recommendation="Limit modal presentations and avoid nesting modals per HIG",
                code_snippet="",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 153. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:148`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                code_snippet="",
                references=[
                    "https://developer.apple.com/design/human-interface-guidelines/modality",
                ],
            )
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 154. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:186`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                                category=Category.QUALITY,
                                title="Non-Standard Spacing",
                                description=f"Spacing value {value} doesn't follow 8-point grid system",
                                recommendation=f"Use multiples of 4 or 8 for consistent spacing (e.g., {(value//4)*4} or {((value+3)//4)*4})",
                                code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 155. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:211`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.QUALITY,
                title="Hardcoded Colors",
                description=f"File has {len(matches)} hardcoded RGB colors",
                recommendation="Use semantic colors (Color.primary, .secondary) or asset catalog colors for Dark Mode support",
                code_snippet="",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 156. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:215`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                code_snippet="",
                references=[
                    "https://developer.apple.com/design/human-interface-guidelines/color",
                ],
            )
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 157. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:235`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.QUALITY,
                title="Non-Semantic Color",
                description=f"Using Color.{match.group(1)} instead of semantic color",
                recommendation="Use Color.primary, .secondary, or asset catalog colors for proper Dark Mode support",
                code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 158. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:269`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title="Hardcoded Font Size",
                        description=f"Using hardcoded font size {size} instead of text style",
                        recommendation=f"Use .font({suggested_style}) for Dynamic Type support",
                        code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 159. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:273`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        code_snippet=code_snippet,
                        references=[
                            "https://developer.apple.com/design/human-interface-guidelines/typography",
                        ],
                    )
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 160. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:304`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.QUALITY,
                    title="Too Many Alert Actions",
                    description=f"Alert has {action_count} actions, exceeds HIG recommendation",
                    recommendation="Limit alerts to 2-3 actions, use action sheet for more options",
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 161. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:308`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    code_snippet=code_snippet,
                    references=[
                        "https://developer.apple.com/design/human-interface-guidelines/alerts",
                    ],
                )
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 162. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/integrations/github_exporter.py:160`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

### Description
{finding.description}

### Recommendation
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 163. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:156`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                (
                    coder.edit_format,
                    coder.__doc__.strip().split("\n")[0] if coder.__doc__ else "No description",
                )
                for coder in coders.__all__
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 164. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:171`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    "architect",
                    (
                        "Work with an architect model to design code changes, and an editor to make"
                        " them."
                    ),
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 165. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:189`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

            max_format_length = max(len(format) for format in valid_formats.keys())
            for format, description in show_formats.items():
                self.io.tool_output(f"- {format:<{max_format_length}} : {description}")

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 166. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:190`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            max_format_length = max(len(format) for format in valid_formats.keys())
            for format, description in show_formats.items():
                self.io.tool_output(f"- {format:<{max_format_length}} : {description}")

            self.io.tool_output("\nOr a valid edit format:\n")
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 167. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:193`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

            self.io.tool_output("\nOr a valid edit format:\n")
            for format, description in valid_formats.items():
                if format not in show_formats:
                    self.io.tool_output(f"- {format:<{max_format_length}} : {description}")
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 168. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:195`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            for format, description in valid_formats.items():
                if format not in show_formats:
                    self.io.tool_output(f"- {format:<{max_format_length}} : {description}")

            return
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 169. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:584`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            self.io.tool_error("The last commit was not made by flacoai in this chat session.")
            self.io.tool_output(
                "You could try `/git reset --hard HEAD^` but be aware that this is a destructive"
                " command!"
            )
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 170. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1110`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            cmd = pad.format(cmd=cmd)
            if cmd_method:
                description = cmd_method.__doc__
                self.io.tool_output(f"{cmd} {description}")
            else:
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 171. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1111`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            if cmd_method:
                description = cmd_method.__doc__
                self.io.tool_output(f"{cmd} {description}")
            else:
                self.io.tool_output(f"{cmd} No description available.")
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 172. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1113`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                self.io.tool_output(f"{cmd} {description}")
            else:
                self.io.tool_output(f"{cmd} No description available.")
        self.io.tool_output()
        self.io.tool_output("Use `/help <question>` to ask questions about how to use flacoai.")
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 173. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1226`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        res = """
|Command|Description|
|:------|:----------|
"""
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 174. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1234`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            cmd_method = getattr(self, cmd_method_name, None)
            if cmd_method:
                description = cmd_method.__doc__
                res += f"| **{cmd}** | {description} |\n"
            else:
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 175. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1235`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            if cmd_method:
                description = cmd_method.__doc__
                res += f"| **{cmd}** | {description} |\n"
            else:
                res += f"| **{cmd}** | |\n"
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 176. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1460`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            self.io.tool_output("📝 Available SwiftUI templates:\n")
            for template in engine.list_templates():
                self.io.tool_output(f"  • {template['name']:12} - {template['description']}")
            self.io.tool_output("\nUsage: /generate <template> <prompt>")
            self.io.tool_output("Example: /generate login for MyWeatherApp")
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 177. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1659`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        Examples:
          /screenshot mockup.png
          /screenshot design.jpg --save LoginView.swift
          /screenshot ui_design.png --preview

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 178. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1660`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
          /screenshot mockup.png
          /screenshot design.jpg --save LoginView.swift
          /screenshot ui_design.png --preview

        Supported formats: PNG, JPG, JPEG, PDF
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 179. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1676`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            self.io.tool_output("\nExamples:")
            self.io.tool_output("  /screenshot mockup.png")
            self.io.tool_output("  /screenshot design.jpg --save LoginView.swift")
            return

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 180. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1741`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            # Create message with image
            if preview_mode:
                prompt = f"""Analyze this UI screenshot and describe:
1. Overall layout and structure
2. All UI elements (buttons, text fields, labels, etc.)
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 181. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1750`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
Provide a detailed analysis but do NOT generate SwiftUI code."""
            else:
                prompt = f"""Analyze this UI screenshot and generate SwiftUI code that recreates the design.

Include:
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 182. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1755`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
- Accurate layout structure (VStack, HStack, ZStack)
- All UI elements with proper styling
- Colors, fonts, spacing matching the design
- SF Symbols for icons where appropriate
- @State for interactive elements
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 183. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1819`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    self.io.tool_output("💡 Next steps:")
                    self.io.tool_output("  1. Review and test the generated code")
                    self.io.tool_output("  2. Adjust colors/spacing to match your design")
                    self.io.tool_output("  3. Use --save <filename> to save to file")

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 184. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2018`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        "category": r.category.value,
                        "title": r.title,
                        "description": r.description,
                        "recommendation": r.recommendation,
                    }
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 185. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2018`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        "category": r.category.value,
                        "title": r.title,
                        "description": r.description,
                        "recommendation": r.recommendation,
                    }
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 186. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2193`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        # Prompt for description
        self.io.tool_output("Enter description (or press Enter to skip):")
        description = input("> ").strip()

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 187. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2194`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        # Prompt for description
        self.io.tool_output("Enter description (or press Enter to skip):")
        description = input("> ").strip()

        # Create issue
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 188. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2200`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            project=project,
            summary=summary,
            description=description or "Created from FlacoAI"
        )

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 189. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2200`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            project=project,
            summary=summary,
            description=description or "Created from FlacoAI"
        )

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 190. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2360`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                summary = f"{finding.title} in {finding.file}:{finding.line}"[:255]

                description = f"""
*Severity:* {finding.severity.value.upper()}
*Category:* {finding.category.value}
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 191. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2366`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
*Line:* {finding.line}

h3. Description
{finding.description}

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 192. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2367`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

h3. Description
{finding.description}

h3. Recommendation
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 193. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2385`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    project=project,
                    summary=summary,
                    description=description,
                    issue_type=issue_type,
                    labels=["code-review", "flaco-ai", finding.category.value]
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 194. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2385`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    project=project,
                    summary=summary,
                    description=description,
                    issue_type=issue_type,
                    labels=["code-review", "flaco-ai", finding.category.value]
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 195. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2432`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        # Build prompt from issue details
        issue_summary = issue.get('fields', {}).get('summary', 'Unknown')
        issue_description = issue.get('fields', {}).get('description', 'No description')
        issue_type = issue.get('fields', {}).get('issuetype', {}).get('name', 'Task')

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 196. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2432`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        # Build prompt from issue details
        issue_summary = issue.get('fields', {}).get('summary', 'Unknown')
        issue_description = issue.get('fields', {}).get('description', 'No description')
        issue_type = issue.get('fields', {}).get('issuetype', {}).get('name', 'Task')

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 197. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2432`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        # Build prompt from issue details
        issue_summary = issue.get('fields', {}).get('summary', 'Unknown')
        issue_description = issue.get('fields', {}).get('description', 'No description')
        issue_type = issue.get('fields', {}).get('issuetype', {}).get('name', 'Task')

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 198. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2449`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
**Type:** {issue_type}
**Description:**
{issue_description}
{project_context}

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 199. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2660`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            ("deepseek-r1:32b", "DeepSeek R1 32B - Advanced reasoning"),
            ("llama3.1:70b", "Llama 3.1 70B - General purpose"),
            ("codestral:22b", "Codestral 22B - Code specialist"),
        ]

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 200. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2660`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            ("deepseek-r1:32b", "DeepSeek R1 32B - Advanced reasoning"),
            ("llama3.1:70b", "Llama 3.1 70B - General purpose"),
            ("codestral:22b", "Codestral 22B - Code specialist"),
        ]

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 201. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2663`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        ]

        for model_name, description in local_models:
            marker = "✓" if model_name == current_model else " "
            self.io.tool_output(f"  [{marker}] {model_name:<30} {description}")
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 202. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2665`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        for model_name, description in local_models:
            marker = "✓" if model_name == current_model else " "
            self.io.tool_output(f"  [{marker}] {model_name:<30} {description}")

        self.io.tool_output("")
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 203. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2678`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        ]

        for model_name, description in cloud_models:
            marker = "✓" if model_name == current_model else " "
            self.io.tool_output(f"  [{marker}] {model_name:<35} {description}")
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 204. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2680`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        for model_name, description in cloud_models:
            marker = "✓" if model_name == current_model else " "
            self.io.tool_output(f"  [{marker}] {model_name:<35} {description}")

        self.io.tool_output("")
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 205. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2871`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        /mode                                 - Show current mode

        Modes:
          architect  - Focus on design, architecture, and big picture
          bugfix     - Focus on finding and fixing bugs
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 206. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2872`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        Modes:
          architect  - Focus on design, architecture, and big picture
          bugfix     - Focus on finding and fixing bugs
          refactor   - Focus on code quality and refactoring
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 207. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2884`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): DES...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        mode = args.strip().lower() if args and args.strip() else None

        MODES = {
            'architect': {
                'name': 'Architect',
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 208. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2888`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                'name': 'Architect',
                'icon': '🏗️',
                'description': 'Design-focused mode for planning and architecture',
                'prompt_addition': """
Work in ARCHITECT mode:
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 209. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2888`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                'name': 'Architect',
                'icon': '🏗️',
                'description': 'Design-focused mode for planning and architecture',
                'prompt_addition': """
Work in ARCHITECT mode:
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 210. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2891`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                'prompt_addition': """
Work in ARCHITECT mode:
- Think about overall system design and architecture
- Consider scalability, maintainability, and extensibility
- Suggest patterns and best practices
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 211. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2901`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                'name': 'Bug Fix',
                'icon': '🐛',
                'description': 'Debugging-focused mode for finding and fixing issues',
                'prompt_addition': """
Work in BUGFIX mode:
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 212. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2914`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                'name': 'Refactor',
                'icon': '♻️',
                'description': 'Code quality-focused mode for improving existing code',
                'prompt_addition': """
Work in REFACTOR mode:
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 213. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2927`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                'name': 'Default',
                'icon': '⚙️',
                'description': 'Balanced mode for general development',
                'prompt_addition': ''
            }
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 214. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2934`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): DES...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        if not mode:
            # Show current mode
            current = MODES.get(self.coder.work_mode, MODES['default'])
            self.io.tool_output(f"\n{current['icon']} Current Mode: {current['name']}")
            self.io.tool_output(f"   {current['description']}\n")
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 215. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2934`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): DES...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        if not mode:
            # Show current mode
            current = MODES.get(self.coder.work_mode, MODES['default'])
            self.io.tool_output(f"\n{current['icon']} Current Mode: {current['name']}")
            self.io.tool_output(f"   {current['description']}\n")
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 216. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2936`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            current = MODES.get(self.coder.work_mode, MODES['default'])
            self.io.tool_output(f"\n{current['icon']} Current Mode: {current['name']}")
            self.io.tool_output(f"   {current['description']}\n")
            self.io.tool_output("💡 Available modes: architect, bugfix, refactor")
            self.io.tool_output("💡 Use '/mode <mode>' to switch\n")
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 217. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2937`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            self.io.tool_output(f"\n{current['icon']} Current Mode: {current['name']}")
            self.io.tool_output(f"   {current['description']}\n")
            self.io.tool_output("💡 Available modes: architect, bugfix, refactor")
            self.io.tool_output("💡 Use '/mode <mode>' to switch\n")
            return
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 218. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2941`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): DES...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            return

        if mode not in MODES or mode == 'default':
            self.io.tool_error(f"Unknown mode: {mode}")
            self.io.tool_error("Available modes: architect, bugfix, refactor")
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 219. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2943`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        if mode not in MODES or mode == 'default':
            self.io.tool_error(f"Unknown mode: {mode}")
            self.io.tool_error("Available modes: architect, bugfix, refactor")
            return

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 220. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2948`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): DES...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        # Set the mode
        self.coder.work_mode = mode
        mode_info = MODES[mode]

        # Store the prompt addition for use in future messages
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 221. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2956`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        self.io.tool_output(f"\n✅ Switched to {mode_info['icon']} {mode_info['name']} mode")
        self.io.tool_output(f"   {mode_info['description']}\n")

    def cmd_standup(self, args):
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 222. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3086`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        """Generate implementation plan for a task

        /plan <task description>    - Create step-by-step implementation plan
        """
        self._track_command("plan")
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 223. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3091`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        if not args or not args.strip():
            self.io.tool_error("Usage: /plan <task description>")
            return

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 224. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/review_coder.py:213`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            try:
                summary = f"{finding.title} in {finding.file}:{finding.line}"
                description = f"""
*Severity:* {finding.severity.value.upper()}
*Category:* {finding.category.value}
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 225. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/review_coder.py:219`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
*Line:* {finding.line}

h3. Description
{finding.description}

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 226. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/review_coder.py:220`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

h3. Description
{finding.description}

h3. Recommendation
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 227. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/review_coder.py:234`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    project=project_key,
                    summary=summary[:255],  # Jira limit
                    description=description,
                    issue_type=issue_type
                )
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 228. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/review_coder.py:234`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    project=project_key,
                    summary=summary[:255],  # Jira limit
                    description=description,
                    issue_type=issue_type
                )
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 229. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:56`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.QUALITY,
                title="Missing Swift Tools Version",
                description="Package.swift missing // swift-tools-version comment",
                recommendation="Add // swift-tools-version:5.9 (or appropriate version) at the top",
                code_snippet="",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 230. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:60`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                code_snippet="",
                references=[
                    "https://docs.swift.org/package-manager/PackageDescription/PackageDescription.html",
                ],
            )
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 231. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:60`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                code_snippet="",
                references=[
                    "https://docs.swift.org/package-manager/PackageDescription/PackageDescription.html",
                ],
            )
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 232. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:73`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.QUALITY,
                title="Missing Package Name",
                description="Package missing name property",
                recommendation="Add name: \"YourPackageName\" to Package initializer",
                code_snippet="",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 233. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:97`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.ARCHITECTURE,
                title="Many Dependencies",
                description=f"Package has {len(matches)} dependencies",
                recommendation="Review if all dependencies are necessary, consider reducing dependency count",
                code_snippet="",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 234. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:118`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.SECURITY,
                    title="Insecure Dependency URL",
                    description="Dependency URL uses HTTP instead of HTTPS",
                    recommendation="Use HTTPS URL for dependency",
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 235. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:138`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.QUALITY,
                    title="Branch-Based Dependency",
                    description="Dependency pinned to branch instead of version",
                    recommendation="Use semantic version or exact revision for reproducible builds",
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 236. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:172`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.QUALITY,
                title="Loose Version Constraint",
                description=f"{version_strategies['from']} dependencies use 'from:' (allows major version updates)",
                recommendation="Consider using .upToNextMajor or .upToNextMinor for more controlled updates",
                code_snippet="",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 237. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:188`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.QUALITY,
                    title="No Exact Version Pinning",
                    description="No dependencies use exact version pinning",
                    recommendation="Consider .exact() for critical dependencies in production apps",
                    code_snippet="",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 238. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:218`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.QUALITY,
                    title="Old iOS Platform Requirement",
                    description=f"Package targets iOS {version}",
                    recommendation=f"Consider updating to iOS 14+ to drop legacy code",
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 239. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:232`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.QUALITY,
                    title="Consider iOS 15+",
                    description=f"Package targets iOS {version}",
                    recommendation="iOS 15+ enables modern Swift Concurrency and SwiftUI features",
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 240. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:259`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.ARCHITECTURE,
                        title="Consider Native Alternative",
                        description=f"Package '{package_name}' has native alternatives",
                        recommendation=suggestion,
                        code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 241. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/baseline_manager.py:40`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    "category": r.category.value,
                    "title": r.title,
                    "description": r.description,
                    "recommendation": r.recommendation,
                    "code_snippet": r.code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 242. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/baseline_manager.py:40`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    "category": r.category.value,
                    "title": r.title,
                    "description": r.description,
                    "recommendation": r.recommendation,
                    "code_snippet": r.code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 243. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_version_analyzer.py:93`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.QUALITY,
                    title="Deprecated iOS API",
                    description=f"{api} deprecated in {deprecated_in}",
                    recommendation=replacement,
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 244. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_version_analyzer.py:111`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        apis_found: Dict[str, List[int]] = {}

        for api, (required_version, description) in self.api_versions.items():
            escaped_api = re.escape(api)
            matches = self.find_pattern(content, escaped_api)
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 245. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_version_analyzer.py:124`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

            for api, line_nums in apis_found.items():
                required_version, description = self.api_versions[api]

                for line_num in line_nums[:3]:  # Limit to 3 per API
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 246. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_version_analyzer.py:141`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                            category=Category.QUALITY,
                            title="iOS Version Requirement",
                            description=f"{description} requires {required_version}",
                            recommendation=f"Add @available(iOS {required_version.split()[1]}, *) or ensure deployment target >= {required_version}",
                            code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 247. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_version_analyzer.py:141`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                            category=Category.QUALITY,
                            title="iOS Version Requirement",
                            description=f"{description} requires {required_version}",
                            recommendation=f"Add @available(iOS {required_version.split()[1]}, *) or ensure deployment target >= {required_version}",
                            code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 248. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_version_analyzer.py:185`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.QUALITY,
                    title="Availability Annotation Issue",
                    description=", ".join(issues),
                    recommendation="Improve @available annotation with platform and deprecation details",
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 249. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_version_analyzer.py:223`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title="Old iOS Deployment Target",
                        description=f"Deployment target is iOS {version}",
                        recommendation=f"Consider updating to iOS 14.0+ to drop legacy code and reduce binary size",
                        code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 250. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_version_analyzer.py:237`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title="Consider iOS 15+ Deployment Target",
                        description=f"Deployment target is iOS {version}",
                        recommendation="iOS 15+ enables modern SwiftUI features (.refreshable, .searchable, AsyncImage)",
                        code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 251. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:87`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.QUALITY,
                    title="Large SwiftUI View Body",
                    description=f"View body has {line_count} lines",
                    recommendation="Extract subviews using @ViewBuilder or computed properties",
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 252. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:121`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.QUALITY,
                    title="@State with Reference Type",
                    description="Using @State with a class instance",
                    recommendation="Use @StateObject for classes, @State for value types only",
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 253. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:136`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.ARCHITECTURE,
                title="Many @State Properties",
                description=f"View has {state_count} @State properties",
                recommendation="Consider using @StateObject with a ViewModel for complex state",
                code_snippet="",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 254. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:185`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title="Missing @ViewBuilder",
                        description=f"Function '{func_name}' returns some View with conditionals",
                        recommendation="Add @ViewBuilder attribute for cleaner syntax",
                        code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 255. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:208`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.QUALITY,
                title="Missing SwiftUI Preview",
                description="View has no #Preview for development",
                recommendation="Add #Preview { YourView() } for faster iteration",
                code_snippet="",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 256. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:231`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.QUALITY,
                title="Old Preview Syntax",
                description="Using PreviewProvider instead of #Preview macro",
                recommendation="Use #Preview { YourView() } for cleaner syntax (iOS 17+)",
                code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 257. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:252`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.QUALITY,
                title="GeometryReader Overuse",
                description=f"File uses GeometryReader {geometry_count} times",
                recommendation="Consider using layout system (.frame, .padding) or custom layouts instead",
                code_snippet="",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 258. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:277`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.PERFORMANCE,
                title="AnyView Type Erasure",
                description="Using AnyView has performance overhead",
                recommendation="Use @ViewBuilder or Group instead of type erasure when possible",
                code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 259. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:315`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            ]

            for pattern, description in heavy_ops:
                if re.search(pattern, onappear_content):
                    line_num = content[:match.start()].count('\n') + 1
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 260. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:326`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.PERFORMANCE,
                        title="Heavy Operation in onAppear",
                        description=f"{description} in onAppear can block UI",
                        recommendation="Use .task { } modifier or move to ViewModel initialization",
                        code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 261. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:326`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.PERFORMANCE,
                        title="Heavy Operation in onAppear",
                        description=f"{description} in onAppear can block UI",
                        recommendation="Use .task { } modifier or move to ViewModel initialization",
                        code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 262. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:354`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.QUALITY,
                title="Consider @Observable Macro",
                description=f"Class '{class_name}' uses ObservableObject",
                recommendation="Consider using @Observable macro for cleaner syntax (iOS 17+)",
                code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 263. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:382`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.QUALITY,
                    title="@EnvironmentObject Without Preview",
                    description="View uses @EnvironmentObject but Preview may crash",
                    recommendation="Add .environmentObject() to #Preview to avoid crashes",
                    code_snippet="",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 264. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:415`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.QUALITY,
                    title="Constant Binding Outside Preview",
                    description="Using .constant() Binding in production code",
                    recommendation=".constant() is meant for previews, use actual Bindings in production",
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 265. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/performance_analyzer.py:169`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        results = []

        for pattern, description in patterns:
            matches = self.find_pattern(content, pattern, re.MULTILINE)

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 266. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/performance_analyzer.py:182`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.PERFORMANCE,
                    title=title,
                    description=description,
                    recommendation=recommendation,
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 267. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/performance_analyzer.py:182`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.PERFORMANCE,
                    title=title,
                    description=description,
                    recommendation=recommendation,
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 268. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/review_prompts.py:13`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak hash algorithm (MD5): MD5...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
**Security (OWASP Mobile Top 10):**
- Insecure data storage (UserDefaults, files instead of Keychain)
- Weak cryptography (DES, 3DES, MD5, SHA1)
- App Transport Security issues
- URL scheme vulnerabilities
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 269. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/review_prompts.py:13`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak hash algorithm (SHA1): SHA1...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
**Security (OWASP Mobile Top 10):**
- Insecure data storage (UserDefaults, files instead of Keychain)
- Weak cryptography (DES, 3DES, MD5, SHA1)
- App Transport Security issues
- URL scheme vulnerabilities
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 270. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/review_prompts.py:13`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): DES...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
**Security (OWASP Mobile Top 10):**
- Insecure data storage (UserDefaults, files instead of Keychain)
- Weak cryptography (DES, 3DES, MD5, SHA1)
- App Transport Security issues
- URL scheme vulnerabilities
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 271. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/review_prompts.py:13`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): DES...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
**Security (OWASP Mobile Top 10):**
- Insecure data storage (UserDefaults, files instead of Keychain)
- Weak cryptography (DES, 3DES, MD5, SHA1)
- App Transport Security issues
- URL scheme vulnerabilities
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 272. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/review_prompts.py:55`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
## 🚨 Critical Issues (Must Fix Before Shipping)
[Issues that will cause crashes, security breaches, or data loss]
- **[File:Line]** - Issue description
  - **Impact**: What will happen if not fixed
  - **Fix**: Specific code changes needed
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 273. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/review_prompts.py:61`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
## ⚠️  High-Priority Improvements
[Important issues affecting security, performance, or UX]
- **[File:Line]** - Issue description
  - **Impact**: Performance/security/UX impact
  - **Fix**: Recommended solution
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 274. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/review_prompts.py:67`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
## 💡 Medium-Priority Improvements
[Code quality, maintainability, best practices]
- **[File:Line]** - Issue description
  - **Fix**: Improvement suggestion

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 275. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/doc_generators/readme_generator.py:37`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        # Description
        sections.append(self._generate_description())

        # Features
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 276. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/doc_generators/readme_generator.py:208`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
> A beautiful iOS app built with Swift and SwiftUI"""

    def _generate_description(self) -> str:
        """Generate description section."""
        return """## 📱 Description
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 277. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/doc_generators/readme_generator.py:210`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
    def _generate_description(self) -> str:
        """Generate description section."""
        return """## 📱 Description

[Add a brief description of your app here. What problem does it solve? Who is it for?]
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 278. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/doc_generators/readme_generator.py:212`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        return """## 📱 Description

[Add a brief description of your app here. What problem does it solve? Who is it for?]

### Key Highlights
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 279. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/doc_generators/readme_generator.py:228`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

{features_list if features_list else '- [List your app features here]'}
- Clean, modern UI design
- Offline support
- Dark mode support
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 280. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/doc_generators/readme_generator.py:332`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            return ""

        deps_list = '\n'.join([f'- **{dep}** - [Add description]' for dep in self.project_info['dependencies']])

        return f"""## 📚 Dependencies
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 281. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:17`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        # Required privacy descriptions
        self.privacy_keys = {
            'NSCameraUsageDescription': 'Camera',
            'NSPhotoLibraryUsageDescription': 'Photo Library',
            'NSPhotoLibraryAddUsageDescription': 'Photo Library (Add Only)',
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 282. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:18`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        self.privacy_keys = {
            'NSCameraUsageDescription': 'Camera',
            'NSPhotoLibraryUsageDescription': 'Photo Library',
            'NSPhotoLibraryAddUsageDescription': 'Photo Library (Add Only)',
            'NSLocationWhenInUseUsageDescription': 'Location (When In Use)',
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 283. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:19`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            'NSCameraUsageDescription': 'Camera',
            'NSPhotoLibraryUsageDescription': 'Photo Library',
            'NSPhotoLibraryAddUsageDescription': 'Photo Library (Add Only)',
            'NSLocationWhenInUseUsageDescription': 'Location (When In Use)',
            'NSLocationAlwaysUsageDescription': 'Location (Always)',
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 284. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:20`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            'NSPhotoLibraryUsageDescription': 'Photo Library',
            'NSPhotoLibraryAddUsageDescription': 'Photo Library (Add Only)',
            'NSLocationWhenInUseUsageDescription': 'Location (When In Use)',
            'NSLocationAlwaysUsageDescription': 'Location (Always)',
            'NSLocationAlwaysAndWhenInUseUsageDescription': 'Location (Always and When In Use)',
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 285. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:21`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            'NSPhotoLibraryAddUsageDescription': 'Photo Library (Add Only)',
            'NSLocationWhenInUseUsageDescription': 'Location (When In Use)',
            'NSLocationAlwaysUsageDescription': 'Location (Always)',
            'NSLocationAlwaysAndWhenInUseUsageDescription': 'Location (Always and When In Use)',
            'NSMicrophoneUsageDescription': 'Microphone',
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 286. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:22`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            'NSLocationWhenInUseUsageDescription': 'Location (When In Use)',
            'NSLocationAlwaysUsageDescription': 'Location (Always)',
            'NSLocationAlwaysAndWhenInUseUsageDescription': 'Location (Always and When In Use)',
            'NSMicrophoneUsageDescription': 'Microphone',
            'NSContactsUsageDescription': 'Contacts',
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 287. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:23`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            'NSLocationAlwaysUsageDescription': 'Location (Always)',
            'NSLocationAlwaysAndWhenInUseUsageDescription': 'Location (Always and When In Use)',
            'NSMicrophoneUsageDescription': 'Microphone',
            'NSContactsUsageDescription': 'Contacts',
            'NSCalendarsUsageDescription': 'Calendars',
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 288. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:24`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            'NSLocationAlwaysAndWhenInUseUsageDescription': 'Location (Always and When In Use)',
            'NSMicrophoneUsageDescription': 'Microphone',
            'NSContactsUsageDescription': 'Contacts',
            'NSCalendarsUsageDescription': 'Calendars',
            'NSRemindersUsageDescription': 'Reminders',
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 289. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:25`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            'NSMicrophoneUsageDescription': 'Microphone',
            'NSContactsUsageDescription': 'Contacts',
            'NSCalendarsUsageDescription': 'Calendars',
            'NSRemindersUsageDescription': 'Reminders',
            'NSMotionUsageDescription': 'Motion & Fitness',
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 290. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:26`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            'NSContactsUsageDescription': 'Contacts',
            'NSCalendarsUsageDescription': 'Calendars',
            'NSRemindersUsageDescription': 'Reminders',
            'NSMotionUsageDescription': 'Motion & Fitness',
            'NSHealthShareUsageDescription': 'Health (Read)',
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 291. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:27`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            'NSCalendarsUsageDescription': 'Calendars',
            'NSRemindersUsageDescription': 'Reminders',
            'NSMotionUsageDescription': 'Motion & Fitness',
            'NSHealthShareUsageDescription': 'Health (Read)',
            'NSHealthUpdateUsageDescription': 'Health (Write)',
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 292. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:28`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            'NSRemindersUsageDescription': 'Reminders',
            'NSMotionUsageDescription': 'Motion & Fitness',
            'NSHealthShareUsageDescription': 'Health (Read)',
            'NSHealthUpdateUsageDescription': 'Health (Write)',
            'NSBluetoothAlwaysUsageDescription': 'Bluetooth',
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 293. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:29`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            'NSMotionUsageDescription': 'Motion & Fitness',
            'NSHealthShareUsageDescription': 'Health (Read)',
            'NSHealthUpdateUsageDescription': 'Health (Write)',
            'NSBluetoothAlwaysUsageDescription': 'Bluetooth',
            'NSBluetoothPeripheralUsageDescription': 'Bluetooth Peripheral',
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 294. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:30`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            'NSHealthShareUsageDescription': 'Health (Read)',
            'NSHealthUpdateUsageDescription': 'Health (Write)',
            'NSBluetoothAlwaysUsageDescription': 'Bluetooth',
            'NSBluetoothPeripheralUsageDescription': 'Bluetooth Peripheral',
            'NSSpeechRecognitionUsageDescription': 'Speech Recognition',
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 295. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:31`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            'NSHealthUpdateUsageDescription': 'Health (Write)',
            'NSBluetoothAlwaysUsageDescription': 'Bluetooth',
            'NSBluetoothPeripheralUsageDescription': 'Bluetooth Peripheral',
            'NSSpeechRecognitionUsageDescription': 'Speech Recognition',
            'NSFaceIDUsageDescription': 'Face ID',
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 296. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:32`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            'NSBluetoothAlwaysUsageDescription': 'Bluetooth',
            'NSBluetoothPeripheralUsageDescription': 'Bluetooth Peripheral',
            'NSSpeechRecognitionUsageDescription': 'Speech Recognition',
            'NSFaceIDUsageDescription': 'Face ID',
            'NSAppleMusicUsageDescription': 'Apple Music',
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 297. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:33`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            'NSBluetoothPeripheralUsageDescription': 'Bluetooth Peripheral',
            'NSSpeechRecognitionUsageDescription': 'Speech Recognition',
            'NSFaceIDUsageDescription': 'Face ID',
            'NSAppleMusicUsageDescription': 'Apple Music',
            'NSLocalNetworkUsageDescription': 'Local Network',
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 298. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:34`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            'NSSpeechRecognitionUsageDescription': 'Speech Recognition',
            'NSFaceIDUsageDescription': 'Face ID',
            'NSAppleMusicUsageDescription': 'Apple Music',
            'NSLocalNetworkUsageDescription': 'Local Network',
        }
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 299. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:35`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            'NSFaceIDUsageDescription': 'Face ID',
            'NSAppleMusicUsageDescription': 'Apple Music',
            'NSLocalNetworkUsageDescription': 'Local Network',
        }

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 300. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:40`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        # Dangerous permissions that need justification
        self.dangerous_permissions = {
            'NSLocationAlwaysUsageDescription': 'Always location access',
            'NSLocationAlwaysAndWhenInUseUsageDescription': 'Always location access',
            'NSHealthUpdateUsageDescription': 'Health data write access',
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 301. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:41`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        self.dangerous_permissions = {
            'NSLocationAlwaysUsageDescription': 'Always location access',
            'NSLocationAlwaysAndWhenInUseUsageDescription': 'Always location access',
            'NSHealthUpdateUsageDescription': 'Health data write access',
        }
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 302. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:42`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            'NSLocationAlwaysUsageDescription': 'Always location access',
            'NSLocationAlwaysAndWhenInUseUsageDescription': 'Always location access',
            'NSHealthUpdateUsageDescription': 'Health data write access',
        }

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 303. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:58`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

            if plist_data:
                results.extend(self._check_privacy_descriptions(file_path, plist_data))
                results.extend(self._check_ats_configuration(file_path, plist_data))
                results.extend(self._check_url_schemes(file_path, plist_data))
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 304. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:62`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                results.extend(self._check_url_schemes(file_path, plist_data))
                results.extend(self._check_dangerous_permissions(file_path, plist_data))
                results.extend(self._check_background_modes(file_path, plist_data))
                results.extend(self._check_bundle_configuration(file_path, plist_data))
        except Exception as e:
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 305. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:116`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        return None

    def _check_privacy_descriptions(self, file_path: str, plist_data: Dict) -> List[AnalysisResult]:
        """Check for missing privacy descriptions."""
        results = []
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 306. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:121`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        # Check which privacy keys are used but missing descriptions
        for key, description in self.privacy_keys.items():
            if key in plist_data:
                value = plist_data[key]
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 307. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:132`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        severity=Severity.HIGH,
                        category=Category.QUALITY,
                        title="Insufficient Privacy Description",
                        description=f"{description} usage description is too short or missing",
                        recommendation=f"Provide a clear, detailed explanation of why your app needs {description} access",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 308. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:133`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title="Insufficient Privacy Description",
                        description=f"{description} usage description is too short or missing",
                        recommendation=f"Provide a clear, detailed explanation of why your app needs {description} access",
                        code_snippet=f"<key>{key}</key>\n<string>{value}</string>",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 309. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:133`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title="Insufficient Privacy Description",
                        description=f"{description} usage description is too short or missing",
                        recommendation=f"Provide a clear, detailed explanation of why your app needs {description} access",
                        code_snippet=f"<key>{key}</key>\n<string>{value}</string>",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 310. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:133`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title="Insufficient Privacy Description",
                        description=f"{description} usage description is too short or missing",
                        recommendation=f"Provide a clear, detailed explanation of why your app needs {description} access",
                        code_snippet=f"<key>{key}</key>\n<string>{value}</string>",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 311. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:134`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        title="Insufficient Privacy Description",
                        description=f"{description} usage description is too short or missing",
                        recommendation=f"Provide a clear, detailed explanation of why your app needs {description} access",
                        code_snippet=f"<key>{key}</key>\n<string>{value}</string>",
                        references=[
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 312. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:157`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): Des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        severity=Severity.MEDIUM,
                        category=Category.QUALITY,
                        title="Generic Privacy Description",
                        description=f"{description} description is too generic",
                        recommendation="Be specific about how and why the data will be used",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 313. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:158`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title="Generic Privacy Description",
                        description=f"{description} description is too generic",
                        recommendation="Be specific about how and why the data will be used",
                        code_snippet=f"<key>{key}</key>\n<string>{value}</string>",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 314. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:158`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title="Generic Privacy Description",
                        description=f"{description} description is too generic",
                        recommendation="Be specific about how and why the data will be used",
                        code_snippet=f"<key>{key}</key>\n<string>{value}</string>",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 315. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:158`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title="Generic Privacy Description",
                        description=f"{description} description is too generic",
                        recommendation="Be specific about how and why the data will be used",
                        code_snippet=f"<key>{key}</key>\n<string>{value}</string>",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 316. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:183`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.SECURITY,
                        title="App Transport Security Disabled",
                        description="NSAllowsArbitraryLoads is set to true, disabling ATS entirely",
                        recommendation="Remove NSAllowsArbitraryLoads and use HTTPS for all connections, or add specific exception domains",
                        code_snippet="<key>NSAllowsArbitraryLoads</key>\n<true/>",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 317. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:202`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                            category=Category.SECURITY,
                            title="Too Many ATS Exceptions",
                            description=f"Found {len(domains)} ATS exception domains",
                            recommendation="Minimize ATS exceptions, migrate to HTTPS where possible",
                            code_snippet="",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 318. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:232`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                                        category=Category.SECURITY,
                                        title="Dangerous URL Scheme",
                                        description=f"URL scheme '{scheme}' conflicts with standard schemes",
                                        recommendation="Use a unique, app-specific URL scheme",
                                        code_snippet=f"<string>{scheme}</string>",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 319. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:247`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                                        category=Category.QUALITY,
                                        title="Non-Unique URL Scheme",
                                        description=f"URL scheme '{scheme}' doesn't use bundle ID prefix",
                                        recommendation=f"Consider using a scheme like '{bundle_id.replace('.', '-')}' for uniqueness",
                                        code_snippet=f"<string>{scheme}</string>",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 320. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:259`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        results = []

        for key, description in self.dangerous_permissions.items():
            if key in plist_data:
                result = AnalysisResult(
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 321. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:267`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.SECURITY,
                    title="Sensitive Permission Requested",
                    description=f"App requests {description}",
                    recommendation="Ensure this permission is absolutely necessary and well-justified in the description",
                    code_snippet=f"<key>{key}</key>",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 322. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:267`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.SECURITY,
                    title="Sensitive Permission Requested",
                    description=f"App requests {description}",
                    recommendation="Ensure this permission is absolutely necessary and well-justified in the description",
                    code_snippet=f"<key>{key}</key>",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 323. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:268`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    title="Sensitive Permission Requested",
                    description=f"App requests {description}",
                    recommendation="Ensure this permission is absolutely necessary and well-justified in the description",
                    code_snippet=f"<key>{key}</key>",
                    references=[
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 324. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:278`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        return results

    def _check_background_modes(self, file_path: str, plist_data: Dict) -> List[AnalysisResult]:
        """Check background modes configuration."""
        results = []
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 325. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:282`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        results = []

        if 'UIBackgroundModes' in plist_data:
            modes = plist_data['UIBackgroundModes']

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 326. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:283`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        if 'UIBackgroundModes' in plist_data:
            modes = plist_data['UIBackgroundModes']

            if isinstance(modes, list):
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 327. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:283`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        if 'UIBackgroundModes' in plist_data:
            modes = plist_data['UIBackgroundModes']

            if isinstance(modes, list):
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 328. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:285`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            modes = plist_data['UIBackgroundModes']

            if isinstance(modes, list):
                # Check for potentially battery-draining modes
                draining_modes = ['location', 'audio', 'voip', 'external-accessory', 'bluetooth-central']
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 329. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:287`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
            if isinstance(modes, list):
                # Check for potentially battery-draining modes
                draining_modes = ['location', 'audio', 'voip', 'external-accessory', 'bluetooth-central']

                for mode in modes:
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 330. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:289`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                draining_modes = ['location', 'audio', 'voip', 'external-accessory', 'bluetooth-central']

                for mode in modes:
                    if mode in draining_modes:
                        result = AnalysisResult(
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 331. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:290`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

                for mode in modes:
                    if mode in draining_modes:
                        result = AnalysisResult(
                            file=file_path,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 332. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:297`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                            category=Category.PERFORMANCE,
                            title="Battery-Draining Background Mode",
                            description=f"Background mode '{mode}' can significantly impact battery life",
                            recommendation="Ensure this background mode is essential and properly managed",
                            code_snippet=f"<string>{mode}</string>",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 333. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:304`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

                # Warn if too many background modes
                if len(modes) > 3:
                    result = AnalysisResult(
                        file=file_path,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 334. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:310`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        severity=Severity.LOW,
                        category=Category.QUALITY,
                        title="Multiple Background Modes",
                        description=f"App has {len(modes)} background modes enabled",
                        recommendation="Only enable necessary background modes to conserve battery",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 335. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:311`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title="Multiple Background Modes",
                        description=f"App has {len(modes)} background modes enabled",
                        recommendation="Only enable necessary background modes to conserve battery",
                        code_snippet="",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 336. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:311`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title="Multiple Background Modes",
                        description=f"App has {len(modes)} background modes enabled",
                        recommendation="Only enable necessary background modes to conserve battery",
                        code_snippet="",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 337. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:311`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title="Multiple Background Modes",
                        description=f"App has {len(modes)} background modes enabled",
                        recommendation="Only enable necessary background modes to conserve battery",
                        code_snippet="",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 338. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:312`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        title="Multiple Background Modes",
                        description=f"App has {len(modes)} background modes enabled",
                        recommendation="Only enable necessary background modes to conserve battery",
                        code_snippet="",
                    )
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 339. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:331`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.QUALITY,
                title="Missing Bundle Display Name",
                description="CFBundleDisplayName not specified",
                recommendation="Add CFBundleDisplayName for better App Store presentation",
                code_snippet="",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 340. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:346`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.QUALITY,
                title="Debug Bundle Identifier",
                description=f"Bundle identifier '{bundle_id}' contains debug/test keywords",
                recommendation="Use production bundle identifier for release builds",
                code_snippet=f"<key>CFBundleIdentifier</key>\n<string>{bundle_id}</string>",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 341. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/branding.py:40`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
    "🔍 Run /review to get comprehensive code analysis for your Swift code",
    "🗺️  Use /tour to generate a guided tour of your codebase",
    "🎯 Switch modes with /mode: architect, bugfix, or refactor",
    "💡 Run /diff to see a natural language summary of your changes",
    "🧠 Use /memory note to add project-specific context to FlacoAI.md",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 342. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/branding.py:48`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
    "🎨 Use /generate login to create SwiftUI views from templates",
    "📱 Use /xcode add-file to add files to your Xcode project",
    "📸 Use /screenshot mockup.png to convert designs to SwiftUI code",
    "📝 Type /help to see all available Flaco AI commands",
]
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 343. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:117`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        results.extend(self._check_patterns(file_path, content, self.naming_patterns,
                                           "Poor Naming", Severity.LOW,
                                           "Use descriptive, meaningful names"))

        # Check cyclomatic complexity
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 344. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:160`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        results = []

        for pattern, description in patterns:
            matches = self.find_pattern(content, pattern, re.MULTILINE)

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 345. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:173`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.QUALITY,
                    title=title,
                    description=description,
                    recommendation=recommendation,
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 346. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:173`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.QUALITY,
                    title=title,
                    description=description,
                    recommendation=recommendation,
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 347. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:212`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.QUALITY,
                    title="Magic Number",
                    description=f"Magic number '{number}' should be a named constant",
                    recommendation="Define as a named constant with meaningful name",
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 348. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:241`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title="High Cyclomatic Complexity",
                        description=f"Function '{current_function}' has complexity of {complexity}",
                        recommendation="Simplify function by extracting methods or reducing branching",
                        code_snippet=f"Complexity: {complexity}",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 349. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:267`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.QUALITY,
                title="High Cyclomatic Complexity",
                description=f"Function '{current_function}' has complexity of {complexity}",
                recommendation="Simplify function by extracting methods or reducing branching",
                code_snippet=f"Complexity: {complexity}",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 350. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/documentation_analyzer.py:81`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title=f"Missing Documentation for Public {decl_type.title()}",
                        description=f"Public {decl_type} '{name}' lacks documentation comments",
                        recommendation=f"Add /// documentation comment describing the {decl_type}'s purpose and usage",
                        code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 351. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/documentation_analyzer.py:82`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        title=f"Missing Documentation for Public {decl_type.title()}",
                        description=f"Public {decl_type} '{name}' lacks documentation comments",
                        recommendation=f"Add /// documentation comment describing the {decl_type}'s purpose and usage",
                        code_snippet=code_snippet,
                        references=[
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 352. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/documentation_analyzer.py:150`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title=f"Missing Docstring for {decl_type.title()}",
                        description=f"{decl_type.title()} '{name}' lacks docstring",
                        recommendation=f"Add docstring explaining the {decl_type}'s purpose, parameters, and return value",
                        code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 353. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/documentation_analyzer.py:201`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title=f"Missing JSDoc for Exported {decl_type.title()}",
                        description=f"Exported {decl_type} '{name}' lacks JSDoc comment",
                        recommendation=f"Add JSDoc comment with @param and @returns tags",
                        code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 354. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/documentation_analyzer.py:256`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title=f"Incomplete {marker_type} Comment",
                        description=f"{marker_type} comment lacks detailed description",
                        recommendation=f"Add description explaining what needs to be done and why",
                        code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 355. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/documentation_analyzer.py:256`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title=f"Incomplete {marker_type} Comment",
                        description=f"{marker_type} comment lacks detailed description",
                        recommendation=f"Add description explaining what needs to be done and why",
                        code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 356. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/documentation_analyzer.py:257`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        title=f"Incomplete {marker_type} Comment",
                        description=f"{marker_type} comment lacks detailed description",
                        recommendation=f"Add description explaining what needs to be done and why",
                        code_snippet=code_snippet,
                    )
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 357. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/documentation_analyzer.py:286`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.QUALITY,
                    title="Brief Documentation Comment",
                    description="Documentation comment is very brief",
                    recommendation="Expand documentation with more details about purpose, parameters, and usage",
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 358. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/documentation_analyzer.py:304`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                        category=Category.QUALITY,
                        title="Generic Documentation",
                        description="Documentation is generic and uninformative",
                        recommendation="Add specific details about behavior, edge cases, and usage examples",
                        code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 359. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:105`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.ARCHITECTURE,
                title="Circular Dependency",
                description=f"Circular dependency with {circular_with}",
                recommendation="Refactor to remove circular dependencies, consider dependency inversion",
                code_snippet="",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 360. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:174`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.ARCHITECTURE,
                    title="God Class",
                    description=f"Class '{class_name}' has {method_count} methods and {line_count} lines",
                    recommendation="Break into smaller, focused classes following Single Responsibility Principle",
                    code_snippet=f"Class {class_name}: {method_count} methods, {line_count} lines",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 361. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:194`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.ARCHITECTURE,
                title="High Coupling",
                description=f"File imports {len(imports)} modules",
                recommendation="Reduce dependencies, consider using dependency injection or facade pattern",
                code_snippet="",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 362. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:211`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.ARCHITECTURE,
                title="Tight Coupling",
                description=f"Many direct object instantiations ({len(matches)})",
                recommendation="Consider dependency injection and programming to interfaces",
                code_snippet="",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 363. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:237`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.ARCHITECTURE,
                title="Law of Demeter Violation",
                description="Long method chain detected",
                recommendation="Consider adding facade methods or using tell-don't-ask principle",
                code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 364. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:271`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.ARCHITECTURE,
                title="Mixed Concerns",
                description=f"File mixes {', '.join(concerns)}",
                recommendation="Separate into layers (data, business, presentation)",
                code_snippet="",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 365. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:290`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        ]

        for pattern, description in hardcoded_patterns:
            matches = self.find_pattern(content, pattern, re.IGNORECASE)

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 366. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:303`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.ARCHITECTURE,
                    title="Hardcoded Dependency",
                    description=description,
                    recommendation="Use dependency injection or configuration files",
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 367. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:303`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.ARCHITECTURE,
                    title="Hardcoded Dependency",
                    description=description,
                    recommendation="Use dependency injection or configuration files",
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 368. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:376`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.ARCHITECTURE,
                    title="Massive View Controller",
                    description=f"View Controller '{vc_name}' has {line_count} lines and {method_count} methods",
                    recommendation="Refactor using MVVM, extract business logic to ViewModel, use child VCs",
                    code_snippet=f"ViewController: {line_count} lines, {method_count} methods",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 369. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:388`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        results = []

        for pattern, description in self.ios_singleton_patterns:
            matches = self.find_pattern(content, pattern)

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 370. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:399`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.ARCHITECTURE,
                    title="Singleton Overuse",
                    description=f"File has {len(matches)} singleton instances",
                    recommendation="Limit singleton usage, consider dependency injection and protocol-based design",
                    code_snippet="",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 371. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:400`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    title="Singleton Overuse",
                    description=f"File has {len(matches)} singleton instances",
                    recommendation="Limit singleton usage, consider dependency injection and protocol-based design",
                    code_snippet="",
                )
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 372. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:412`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
        results = []

        for pattern, description in self.ios_tight_coupling_patterns:
            matches = self.find_pattern(content, pattern, re.MULTILINE)

```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 373. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:425`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.ARCHITECTURE,
                    title="Tight Coupling",
                    description=description,
                    recommendation="Separate view layer from business logic, use protocols for abstraction",
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 374. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:425`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                    category=Category.ARCHITECTURE,
                    title="Tight Coupling",
                    description=description,
                    recommendation="Separate view layer from business logic, use protocols for abstraction",
                    code_snippet=code_snippet,
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 375. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:438`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        shared_usage_count = 0
        for pattern, description in self.ios_dependency_injection_patterns:
            matches = self.find_pattern(content, pattern)
            shared_usage_count += len(matches)
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 376. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:450`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.ARCHITECTURE,
                title="Missing Dependency Injection",
                description=f"File uses {shared_usage_count} shared/default instances",
                recommendation="Inject dependencies via initializers or properties for better testability",
                code_snippet="",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 377. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:463`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```

        navigation_count = 0
        for pattern, description in self.ios_coordinator_patterns:
            matches = self.find_pattern(content, pattern)
            navigation_count += len(matches)
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 378. 🟡 Weak Cryptography

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:475`
**Severity:** MEDIUM
**Category:** security

**Description:** Weak encryption (DES): des...

**Recommendation:** Use SHA-256 or better, AES with secure modes

**Code:**
```
                category=Category.ARCHITECTURE,
                title="Navigation Logic in View Controller",
                description=f"File has {navigation_count} direct navigation calls",
                recommendation="Consider using Coordinator pattern to decouple navigation logic",
                code_snippet="",
```

**References:**
- https://owasp.org/www-project-top-ten/

---

### 379. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/mdstream.py:174`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'update' has complexity of 17

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 17
```

---

### 380. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:150`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'analyze_file' has complexity of 25

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 25
```

---

### 381. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:266`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'run_server' has complexity of 33

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 33
```

---

### 382. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:148`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'get_command_completions' has complexity of 17

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 17
```

---

### 383. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:186`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'get_completions' has complexity of 16

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 16
```

---

### 384. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:237`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function '__init__' has complexity of 40

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 40
```

---

### 385. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:653`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'get_continuation' has complexity of 32

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 32
```

---

### 386. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:807`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'confirm_ask' has complexity of 17

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 17
```

---

### 387. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:861`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'is_valid_response' has complexity of 27

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 27
```

---

### 388. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:1139`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'format_files_for_input' has complexity of 19

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 19
```

---

### 389. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/args.py:35`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'get_parser' has complexity of 84

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 84
```

---

### 390. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/args.py:917`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'main' has complexity of 17

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 17
```

---

### 391. 🟡 Code Smell

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:417`
**Severity:** MEDIUM
**Category:** quality

**Description:** Complex conditional (too many conditions)

**Recommendation:** Refactor to improve readability and maintainability

**Code:**
```
    if filename.startswith(start_fence):
        candidate = filename[len(start_fence) :]
        if candidate and ("." in candidate or "/" in candidate):
            return candidate
        return
```

---

### 392. 🟡 Code Smell

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:423`
**Severity:** MEDIUM
**Category:** quality

**Description:** Complex conditional (too many conditions)

**Recommendation:** Refactor to improve readability and maintainability

**Code:**
```
    if filename.startswith(triple_backticks):
        candidate = filename[len(triple_backticks) :]
        if candidate and ("." in candidate or "/" in candidate):
            return candidate
        return
```

---

### 393. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:41`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'apply_edits' has complexity of 22

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 22
```

---

### 394. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:190`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'try_dotdotdots' has complexity of 19

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 19
```

---

### 395. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:243`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'replace_part_with_missing_leading_whitespace' has complexity of 21

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 21
```

---

### 396. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:439`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'find_original_update_blocks' has complexity of 37

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 37
```

---

### 397. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:538`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'find_filename' has complexity of 21

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 21
```

---

### 398. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/problem_stats.py:62`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'analyze_exercise_solutions' has complexity of 91

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 91
```

---

### 399. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:125`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'create' has complexity of 22

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 22
```

---

### 400. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:207`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'get_announcements' has complexity of 31

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 31
```

---

### 401. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:341`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function '__init__' has complexity of 54

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 54
```

---

### 402. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1195`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'get_platform_info' has complexity of 16

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 16
```

---

### 403. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1294`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'format_chat_chunks' has complexity of 26

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 26
```

---

### 404. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1487`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'send_message' has complexity of 55

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 55
```

---

### 405. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1782`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'get_file_mentions' has complexity of 21

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 21
```

---

### 406. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1968`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'show_send_output_stream' has complexity of 23

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 23
```

---

### 407. 🟡 Code Smell

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:474`
**Severity:** MEDIUM
**Category:** quality

**Description:** Complex conditional (too many conditions)

**Recommendation:** Refactor to improve readability and maintainability

**Code:**
```
            # Get commands used
            commands_used = []
            if hasattr(coder, 'commands') and hasattr(coder.commands, 'used_commands'):
                commands_used = coder.commands.used_commands

```

---

### 408. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:102`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'setup_git' has complexity of 17

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 17
```

---

### 409. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:156`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'check_gitignore' has complexity of 17

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 17
```

---

### 410. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:459`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'record_session' has complexity of 37

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 37
```

---

### 411. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:586`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'get_io' has complexity of 175

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 175
```

---

### 412. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:1222`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'is_first_run_of_new_version' has complexity of 16

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 16
```

---

### 413. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/patch_coder.py:96`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'peek_next_section' has complexity of 29

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 29
```

---

### 414. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/patch_coder.py:220`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'get_edits' has complexity of 24

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 24
```

---

### 415. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/patch_coder.py:290`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function '_parse_patch_text' has complexity of 42

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 42
```

---

### 416. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/patch_coder.py:412`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function '_parse_update_file_sections' has complexity of 30

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 30
```

---

### 417. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/patch_coder.py:549`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'apply_edits' has complexity of 33

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 33
```

---

### 418. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/patch_coder.py:642`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function '_apply_update' has complexity of 21

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 21
```

---

### 419. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/tsl_pack_langs.py:42`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'main' has complexity of 25

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 25
```

---

### 420. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/udiff_coder.py:337`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'process_fenced_block' has complexity of 22

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 22
```

---

### 421. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:14`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'has_been_reopened' has complexity of 17

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 17
```

---

### 422. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:204`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'handle_stale_issues' has complexity of 20

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 20
```

---

### 423. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:249`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'handle_stale_closing' has complexity of 26

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 26
```

---

### 424. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:335`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'handle_fixed_issues' has complexity of 26

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 26
```

---

### 425. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/template_engine.py:151`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'extract_variables_from_prompt' has complexity of 18

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 18
```

---

### 426. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/homepage.py:338`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'get_badges_html' has complexity of 18

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 18
```

---

### 427. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/homepage.py:413`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'get_testimonials_js' has complexity of 37

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 37
```

---

### 428. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/homepage.py:530`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'main' has complexity of 24

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 24
```

---

### 429. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/fix_applicator.py:55`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function '_apply_fixes_to_file' has complexity of 31

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 31
```

---

### 430. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/integrations/github_exporter.py:36`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'export_findings' has complexity of 16

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 16
```

---

### 431. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:146`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'cmd_chat_mode' has complexity of 17

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 17
```

---

### 432. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:364`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'cmd_lint' has complexity of 19

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 19
```

---

### 433. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:568`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'raw_cmd_undo' has complexity of 22

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 22
```

---

### 434. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:807`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'cmd_add' has complexity of 34

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 34
```

---

### 435. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:910`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'cmd_drop' has complexity of 23

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 23
```

---

### 436. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1268`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'cmd_paste' has complexity of 17

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 17
```

---

### 437. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1318`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'cmd_read_only' has complexity of 22

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 22
```

---

### 438. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1422`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'cmd_generate' has complexity of 24

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 24
```

---

### 439. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1522`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'cmd_xcode' has complexity of 33

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 33
```

---

### 440. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1650`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'cmd_screenshot' has complexity of 35

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 35
```

---

### 441. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1828`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'cmd_review' has complexity of 78

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 78
```

---

### 442. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2106`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'cmd_jira' has complexity of 21

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 21
```

---

### 443. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2322`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function '_jira_from_review' has complexity of 17

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 17
```

---

### 444. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2513`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'cmd_memory' has complexity of 18

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 18
```

---

### 445. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2589`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'cmd_llm' has complexity of 17

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 17
```

---

### 446. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2725`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'cmd_commit_msg' has complexity of 19

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 19
```

---

### 447. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2865`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'cmd_mode' has complexity of 26

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 26
```

---

### 448. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3135`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'cmd_tour' has complexity of 18

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 18
```

---

### 449. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/review_coder.py:18`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'run_static_analysis' has complexity of 22

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 22
```

---

### 450. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/performance_analyzer.py:11`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function '__init__' has complexity of 20

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 20
```

---

### 451. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/performance_analyzer.py:100`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'analyze_file' has complexity of 17

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 17
```

---

### 452. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/branding.py:240`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'format_compact_header' has complexity of 17

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 17
```

---

### 453. 🟡 Code Smell

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:18`
**Severity:** MEDIUM
**Category:** quality

**Description:** TODO in conditional

**Recommendation:** Refactor to improve readability and maintainability

**Code:**
```
            (r'def\s+\w+\([^)]{100,}\)', "Long parameter list (>100 chars)"),
            (r'if\s+.*and.*and.*and.*and', "Complex conditional (too many conditions)"),
            (r'(if|elif).*:.*#.*TODO', "TODO in conditional"),
        ]

```

---

### 454. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:220`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function '_check_cyclomatic_complexity' has complexity of 25

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 25
```

---

### 455. 🟡 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:43`
**Severity:** MEDIUM
**Category:** quality

**Description:** Function 'analyze_file' has complexity of 16

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 16
```

---

### 456. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/mdstream.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, presentation

**Recommendation:** Separate into layers (data, business, presentation)

---

### 457. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/copypaste.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, presentation

**Recommendation:** Separate into layers (data, business, presentation)

---

### 458. 🟡 God Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:282`
**Severity:** MEDIUM
**Category:** architecture

**Description:** Class 'TestRepoMapAllLanguages' has 41 methods and 227 lines

**Recommendation:** Break into smaller, focused classes following Single Responsibility Principle

**Code:**
```
Class TestRepoMapAllLanguages: 41 methods, 227 lines
```

---

### 459. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes presentation, business logic

**Recommendation:** Separate into layers (data, business, presentation)

---

### 460. 🟡 God Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repo.py:18`
**Severity:** MEDIUM
**Category:** architecture

**Description:** Class 'TestRepo' has 22 methods and 700 lines

**Recommendation:** Break into smaller, focused classes following Single Responsibility Principle

**Code:**
```
Class TestRepo: 22 methods, 700 lines
```

---

### 461. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, presentation, business logic

**Recommendation:** Separate into layers (data, business, presentation)

---

### 462. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_aws_credentials.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, business logic

**Recommendation:** Separate into layers (data, business, presentation)

---

### 463. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, presentation

**Recommendation:** Separate into layers (data, business, presentation)

---

### 464. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_reasoning.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, business logic

**Recommendation:** Separate into layers (data, business, presentation)

---

### 465. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_wholefile.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, presentation

**Recommendation:** Separate into layers (data, business, presentation)

---

### 466. 🟡 God Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:230`
**Severity:** MEDIUM
**Category:** architecture

**Description:** Class 'InputOutput' has 43 methods and 964 lines

**Recommendation:** Break into smaller, focused classes following Single Responsibility Principle

**Code:**
```
Class InputOutput: 43 methods, 964 lines
```

---

### 467. 🟡 High Coupling

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File imports 18 modules

**Recommendation:** Reduce dependencies, consider using dependency injection or facade pattern

---

### 468. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, presentation, business logic

**Recommendation:** Separate into layers (data, business, presentation)

---

### 469. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/args.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, presentation, business logic

**Recommendation:** Separate into layers (data, business, presentation)

---

### 470. 🟡 God Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:15`
**Severity:** MEDIUM
**Category:** architecture

**Description:** Class 'EditBlockCoder' has 18 methods and 644 lines

**Recommendation:** Break into smaller, focused classes following Single Responsibility Principle

**Code:**
```
Class EditBlockCoder: 18 methods, 644 lines
```

---

### 471. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, business logic

**Recommendation:** Separate into layers (data, business, presentation)

---

### 472. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/problem_stats.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes presentation, business logic

**Recommendation:** Separate into layers (data, business, presentation)

---

### 473. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_prompts.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, presentation, business logic

**Recommendation:** Separate into layers (data, business, presentation)

---

### 474. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_editor.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, presentation, business logic

**Recommendation:** Separate into layers (data, business, presentation)

---

### 475. 🟡 God Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:88`
**Severity:** MEDIUM
**Category:** architecture

**Description:** Class 'Coder' has 87 methods and 2467 lines

**Recommendation:** Break into smaller, focused classes following Single Responsibility Principle

**Code:**
```
Class Coder: 87 methods, 2467 lines
```

---

### 476. 🟡 High Coupling

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File imports 20 modules

**Recommendation:** Reduce dependencies, consider using dependency injection or facade pattern

---

### 477. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, presentation, business logic

**Recommendation:** Separate into layers (data, business, presentation)

---

### 478. 🟡 High Coupling

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File imports 16 modules

**Recommendation:** Reduce dependencies, consider using dependency injection or facade pattern

---

### 479. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, presentation, business logic

**Recommendation:** Separate into layers (data, business, presentation)

---

### 480. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/patch_coder.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, business logic

**Recommendation:** Separate into layers (data, business, presentation)

---

### 481. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, presentation, business logic

**Recommendation:** Separate into layers (data, business, presentation)

---

### 482. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/tsl_pack_langs.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes presentation, business logic

**Recommendation:** Separate into layers (data, business, presentation)

---

### 483. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/openrouter.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, presentation

**Recommendation:** Separate into layers (data, business, presentation)

---

### 484. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/udiff_coder.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, business logic

**Recommendation:** Separate into layers (data, business, presentation)

---

### 485. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, presentation

**Recommendation:** Separate into layers (data, business, presentation)

---

### 486. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, presentation, business logic

**Recommendation:** Separate into layers (data, business, presentation)

---

### 487. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/template_engine.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, presentation, business logic

**Recommendation:** Separate into layers (data, business, presentation)

---

### 488. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/homepage.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, presentation, business logic

**Recommendation:** Separate into layers (data, business, presentation)

---

### 489. 🟡 God Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:36`
**Severity:** MEDIUM
**Category:** architecture

**Description:** Class 'Commands' has 107 methods and 3457 lines

**Recommendation:** Break into smaller, focused classes following Single Responsibility Principle

**Code:**
```
Class Commands: 107 methods, 3457 lines
```

---

### 490. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, presentation, business logic

**Recommendation:** Separate into layers (data, business, presentation)

---

### 491. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, presentation

**Recommendation:** Separate into layers (data, business, presentation)

---

### 492. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/doc_generators/changelog_generator.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes presentation, business logic

**Recommendation:** Separate into layers (data, business, presentation)

---

### 493. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/smart_context.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, presentation, business logic

**Recommendation:** Separate into layers (data, business, presentation)

---

### 494. 🟡 Mixed Concerns

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:1`
**Severity:** MEDIUM
**Category:** architecture

**Description:** File mixes database, presentation, business logic

**Recommendation:** Separate into layers (data, business, presentation)

---

## 🟢 LOW Severity (903 issues)

### 1. 🟢 Inefficient Data Structure

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1026`
**Severity:** LOW
**Category:** performance

**Description:** Converting set to list (unnecessary)

**Recommendation:** Use appropriate data structures (set for membership, dict for lookups)

**Code:**
```

        # Exclude double quotes from the matched URL characters
        url_pattern = re.compile(r'(https?://[^\s/$.?#].[^\s"]*)')
        urls = list(set(url_pattern.findall(text)))  # Use set to remove duplicates
        for url in urls:
            url = url.rstrip(".',\"}")  # Added } to the characters to strip
            self.io.offer_url(url)
```

---

### 2. 🟢 Inefficient Data Structure

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1039`
**Severity:** LOW
**Category:** performance

**Description:** Converting set to list (unnecessary)

**Recommendation:** Use appropriate data structures (set for membership, dict for lookups)

**Code:**
```

        # Exclude double quotes from the matched URL characters
        url_pattern = re.compile(r'(https?://[^\s/$.?#].[^\s"]*[^\s,.])')
        urls = list(set(url_pattern.findall(inp)))  # Use set to remove duplicates
        group = ConfirmGroup(urls)
        for url in urls:
            if url not in self.rejected_urls:
```

---

### 3. 🟢 String Inefficiency

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:499`
**Severity:** LOW
**Category:** performance

**Description:** Multiple string concatenations

**Recommendation:** Use str.join() for concatenating multiple strings

**Code:**
```
                tokens = self.coder.main_model.token_count_for_image(fname)
            else:
                # approximate
                content = f"{relative_fname}\n{fence}\n" + content + "{fence}\n"
                tokens = self.coder.main_model.token_count(content)
            file_res.append((tokens, f"{relative_fname}", "/drop to remove"))

```

---

### 4. 🟢 String Inefficiency

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:509`
**Severity:** LOW
**Category:** performance

**Description:** Multiple string concatenations

**Recommendation:** Use str.join() for concatenating multiple strings

**Code:**
```
            content = self.io.read_text(fname)
            if content is not None and not is_image_file(relative_fname):
                # approximate
                content = f"{relative_fname}\n{fence}\n" + content + "{fence}\n"
                tokens = self.coder.main_model.token_count(content)
                file_res.append((tokens, f"{relative_fname} (read-only)", "/drop to remove"))

```

---

### 5. 🟢 Inefficient Data Structure

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/doc_generators/readme_generator.py:140`
**Severity:** LOW
**Category:** performance

**Description:** Converting set to list (unnecessary)

**Recommendation:** Use appropriate data structures (set for membership, dict for lookups)

**Code:**
```
            url_matches = re.findall(r'url:\s*"https://github\.com/([^"]+)"', content)
            deps.extend([url.split('/')[-1].replace('.git', '') for url in url_matches])

        return list(set(deps))[:10]  # Limit to 10

    def _detect_features(self) -> List[str]:
        """Detect key features from code."""
```

---

### 6. 🟢 Inefficient Data Structure

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/smart_context.py:208`
**Severity:** LOW
**Category:** performance

**Description:** Membership test on list (use set)

**Recommendation:** Use appropriate data structures (set for membership, dict for lookups)

**Code:**
```
            imports.extend(re.findall(r'from\s+([\w\.]+)\s+import', content))
            imports.extend(re.findall(r'import\s+([\w\.]+)', content))

        elif ext in ['.js', '.ts', '.jsx', '.tsx']:
            # JavaScript/TypeScript imports
            imports.extend(re.findall(r'from\s+[\'"]([^\'"]+)[\'"]', content))
            imports.extend(re.findall(r'require\([\'"]([^\'"]+)[\'"]\)', content))
```

---

### 7. 🟢 Inefficient Data Structure

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/smart_context.py:213`
**Severity:** LOW
**Category:** performance

**Description:** Membership test on list (use set)

**Recommendation:** Use appropriate data structures (set for membership, dict for lookups)

**Code:**
```
            imports.extend(re.findall(r'from\s+[\'"]([^\'"]+)[\'"]', content))
            imports.extend(re.findall(r'require\([\'"]([^\'"]+)[\'"]\)', content))

        elif ext in ['.m', '.mm', '.h']:
            # Objective-C imports
            imports.extend(re.findall(r'#import\s+[<"]([^>"]+)[>"]', content))

```

---

### 8. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/fixtures/languages/python/test.py:5`
**Severity:** LOW
**Category:** quality

**Description:** Lowercase class name

**Recommendation:** Use descriptive, meaningful names

**Code:**
```

class Person:
    """A class representing a person."""

    def __init__(self, name: str, age: Optional[int] = None):
```

---

### 9. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/mdstream.py:118`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '20' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    when = 0  # Timestamp of last update
    min_delay = 1.0 / 20  # Minimum time between updates (20fps)
    live_window = 2  # Number of lines to keep visible at bottom during streaming (reduced for smoother streaming)
```

---

### 10. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/mdstream.py:209`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '20' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        # Set min_delay to render time plus a small buffer
        self.min_delay = min(max(render_time * 10, 1.0 / 20), 2)

```

---

### 11. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/mdstream.py:250`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '50' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```

    def find_minimal_suffix(self, text, match_lines=50):
        """
```

---

### 12. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/mdstream.py:266`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '01' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        pm.update(_text[:i])
        time.sleep(0.01)

```

---

### 13. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/mdstream.py:72`
**Severity:** LOW
**Category:** quality

**Description:** Lowercase class name

**Recommendation:** Use descriptive, meaningful names

**Code:**
```

class LeftHeading(Heading):
    """A heading class that renders left-justified."""

    def __rich_console__(self, console, options):
```

---

### 14. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:94`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '12' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    def create_figure(self) -> Tuple[plt.Figure, plt.Axes]:
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.grid(axis="y", zorder=0, lw=0.2)
```

---

### 15. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:119`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '120' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            # Plot points
            ax.scatter(dates, rates, c=color, alpha=0.5, s=120)

```

---

### 16. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:134`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '18' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    def set_labels_and_style(self, ax: plt.Axes):
        ax.set_xlabel("Model release date", fontsize=18, color="#555")
        ax.set_ylabel(
```

---

### 17. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:134`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '555' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    def set_labels_and_style(self, ax: plt.Axes):
        ax.set_xlabel("Model release date", fontsize=18, color="#555")
        ax.set_ylabel(
```

---

### 18. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:136`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '18' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        ax.set_ylabel(
            "aider code editing benchmark,\npercent completed correctly", fontsize=18, color="#555"
        )
```

---

### 19. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:136`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '555' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        ax.set_ylabel(
            "aider code editing benchmark,\npercent completed correctly", fontsize=18, color="#555"
        )
```

---

### 20. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:138`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '20' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        )
        ax.set_title("LLM code editing skill by model release date", fontsize=20)
        ax.set_ylim(30, 90)
```

---

### 21. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:139`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '30' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        ax.set_title("LLM code editing skill by model release date", fontsize=20)
        ax.set_ylim(30, 90)
        plt.xticks(fontsize=14, rotation=45, ha="right")
```

---

### 22. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:139`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '90' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        ax.set_title("LLM code editing skill by model release date", fontsize=20)
        ax.set_ylim(30, 90)
        plt.xticks(fontsize=14, rotation=45, ha="right")
```

---

### 23. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:140`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '14' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        ax.set_ylim(30, 90)
        plt.xticks(fontsize=14, rotation=45, ha="right")
        plt.tight_layout(pad=1.0)
```

---

### 24. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:140`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '45' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        ax.set_ylim(30, 90)
        plt.xticks(fontsize=14, rotation=45, ha="right")
        plt.tight_layout(pad=1.0)
```

---

### 25. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:116`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```

            # Plot line
            ax.plot(dates, rates, c=color, alpha=0.5, linewidth=1)

            # Plot points
```

---

### 26. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:119`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```

            # Plot points
            ax.scatter(dates, rates, c=color, alpha=0.5, s=120)

            # Add label for first point
```

---

### 27. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:119`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```

            # Plot points
            ax.scatter(dates, rates, c=color, alpha=0.5, s=120)

            # Add label for first point
```

---

### 28. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:18`
**Severity:** LOW
**Category:** quality

**Description:** Function 'color' has complexity of 11

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 11
```

---

### 29. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:41`
**Severity:** LOW
**Category:** quality

**Description:** Function 'legend_label' has complexity of 13

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 13
```

---

### 30. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/base_analyzer.py:111`
**Severity:** LOW
**Category:** quality

**Description:** Lowercase class name

**Recommendation:** Use descriptive, meaningful names

**Code:**
```

class BaseAnalyzer(ABC):
    """Abstract base class for all code analyzers."""

    def __init__(self, io=None, verbose=False):
```

---

### 31. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/premium/crash_prediction_analyzer.py:214`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '70' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                category=Category.QUALITY,
                title="Force cast detected - 70% crash risk",
                description=f"Force cast 'as! {target_type}' will crash if the cast fails. "
```

---

### 32. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/premium/crash_prediction_analyzer.py:244`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '55' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                    category=Category.QUALITY,
                    title="Unhandled async throwing call - 55% crash risk",
                    description="Using 'await' without 'try' on a throwing function. "
```

---

### 33. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/premium/crash_prediction_analyzer.py:267`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '11' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                # Check next 10 lines for mutation of same collection
                for offset in range(1, min(11, len(lines) - line_num + 1)):
                    next_line = lines[line_num + offset - 1]
```

---

### 34. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/premium/crash_prediction_analyzer.py:283`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '90' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                            category=Category.QUALITY,
                            title="Collection mutation during iteration - 90% crash risk",
                            description=f"Modifying collection '{collection_name}' while iterating over it. "
```

---

### 35. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/premium/crash_prediction_analyzer.py:309`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '50' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                '@escaping' in content[max(0, match.start()-100):match.start()] or
                'DispatchQueue' in content[max(0, match.start()-50):match.start()]
            )
```

---

### 36. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/premium/crash_prediction_analyzer.py:340`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '20' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        # Look backwards for function declaration
        for i in range(max(0, line_num - 20), line_num):
            if i < len(lines) and 'func ' in lines[i]:
```

---

### 37. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/premium/crash_prediction_analyzer.py:254`
**Severity:** LOW
**Category:** quality

**Description:** Function '_check_collection_mutation' has complexity of 12

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 12
```

---

### 38. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_analytics.py:97`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '000' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```

    analytics.user_id = "000"
    assert analytics.need_to_ask(None) is True
```

---

### 39. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_analytics.py:111`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '00000000000000000000000000000000' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    # Test basic percentage thresholds
    assert is_uuid_in_percentage("00000000000000000000000000000000", 1) is True
    assert is_uuid_in_percentage("01999000000000000000000000000000", 1) is True
```

---

### 40. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_analytics.py:112`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '01999000000000000000000000000000' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    assert is_uuid_in_percentage("00000000000000000000000000000000", 1) is True
    assert is_uuid_in_percentage("01999000000000000000000000000000", 1) is True
    assert is_uuid_in_percentage("02000000000000000000000000000000", 1) is True
```

---

### 41. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_analytics.py:113`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '02000000000000000000000000000000' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    assert is_uuid_in_percentage("01999000000000000000000000000000", 1) is True
    assert is_uuid_in_percentage("02000000000000000000000000000000", 1) is True
    assert is_uuid_in_percentage("02910000000000000000000000000001", 1) is False
```

---

### 42. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_analytics.py:114`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '02910000000000000000000000000001' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    assert is_uuid_in_percentage("02000000000000000000000000000000", 1) is True
    assert is_uuid_in_percentage("02910000000000000000000000000001", 1) is False
    assert is_uuid_in_percentage("03000000000000000000000000000000", 1) is False
```

---

### 43. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_analytics.py:115`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '03000000000000000000000000000000' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    assert is_uuid_in_percentage("02910000000000000000000000000001", 1) is False
    assert is_uuid_in_percentage("03000000000000000000000000000000", 1) is False
    assert is_uuid_in_percentage("ff000000000000000000000000000000", 1) is False
```

---

### 44. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_analytics.py:118`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '00000000000000000000000000000000' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```

    assert is_uuid_in_percentage("00000000000000000000000000000000", 10) is True
    assert is_uuid_in_percentage("19000000000000000000000000000000", 10) is True
```

---

### 45. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_analytics.py:124`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '00000000000000000000000000000000' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    # Test edge cases
    assert is_uuid_in_percentage("00000000000000000000000000000000", 0) is False
    assert is_uuid_in_percentage("00000000000000000000000000000000", 100) is True
```

---

### 46. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_analytics.py:125`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '00000000000000000000000000000000' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    assert is_uuid_in_percentage("00000000000000000000000000000000", 0) is False
    assert is_uuid_in_percentage("00000000000000000000000000000000", 100) is True
    assert is_uuid_in_percentage("ffffffffffffffffffffffffffffffff", 100) is True
```

---

### 47. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_analytics.py:130`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '00000000000000000000000000000000' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    with pytest.raises(ValueError):
        is_uuid_in_percentage("00000000000000000000000000000000", -1)
    with pytest.raises(ValueError):
```

---

### 48. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_analytics.py:132`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '00000000000000000000000000000000' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    with pytest.raises(ValueError):
        is_uuid_in_percentage("00000000000000000000000000000000", 101)

```

---

### 49. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_analytics.py:132`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '101' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    with pytest.raises(ValueError):
        is_uuid_in_percentage("00000000000000000000000000000000", 101)

```

---

### 50. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_analytics.py:135`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '50' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    # Test empty/None UUID
    assert is_uuid_in_percentage("", 50) is False
    assert is_uuid_in_percentage(None, 50) is False
```

---

### 51. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_analytics.py:136`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '50' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    assert is_uuid_in_percentage("", 50) is False
    assert is_uuid_in_percentage(None, 50) is False

```

---

### 52. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:181`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '256' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                                           "Weak Cryptography", Severity.MEDIUM,
                                           "Use SHA-256 or better, AES with secure modes"))

```

---

### 53. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:208`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '256' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                                               "Weak iOS Cryptography", Severity.HIGH,
                                               "Use AES-256 (kCCAlgorithmAES) and SHA-256 or better"))

```

---

### 54. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:208`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '256' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                                               "Weak iOS Cryptography", Severity.HIGH,
                                               "Use AES-256 (kCCAlgorithmAES) and SHA-256 or better"))

```

---

### 55. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:258`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '50' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                    title=title,
                    description=f"{description}: {matched_text[:50]}...",
                    recommendation=recommendation,
```

---

### 56. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:4`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '30' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
"""
Generate a celebratory SVG image for flacoai reaching 30,000 GitHub stars.
This creates a shareable social media graphic with confetti animation.
```

---

### 57. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:46`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '150' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```

def generate_confetti(count=150, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
    """Generate SVG confetti elements for the celebration."""
```

---

### 58. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:85`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '15' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        confetti_count += 1
        size = random.randint(5, 15)
        color = random.choice(colors)
```

---

### 59. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:87`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '360' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        color = random.choice(colors)
        rotation = random.randint(0, 360)
        delay = random.uniform(0, 2)
```

---

### 60. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:98`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '200' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                <animate attributeName="opacity" from="1" to="0" dur="{duration}s" begin="{delay}s" repeatCount="indefinite" />
                <animate attributeName="y" from="{y}" to="{y + random.randint(200, 400)}" dur="{duration}s" begin="{delay}s" repeatCount="indefinite" />
            </rect>"""
```

---

### 61. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:98`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '400' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                <animate attributeName="opacity" from="1" to="0" dur="{duration}s" begin="{delay}s" repeatCount="indefinite" />
                <animate attributeName="y" from="{y}" to="{y + random.randint(200, 400)}" dur="{duration}s" begin="{delay}s" repeatCount="indefinite" />
            </rect>"""
```

---

### 62. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:103`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '200' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                <animate attributeName="opacity" from="1" to="0" dur="{duration}s" begin="{delay}s" repeatCount="indefinite" />
                <animate attributeName="cy" from="{y}" to="{y + random.randint(200, 400)}" dur="{duration}s" begin="{delay}s" repeatCount="indefinite" />
            </circle>"""
```

---

### 63. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:103`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '400' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                <animate attributeName="opacity" from="1" to="0" dur="{duration}s" begin="{delay}s" repeatCount="indefinite" />
                <animate attributeName="cy" from="{y}" to="{y + random.randint(200, 400)}" dur="{duration}s" begin="{delay}s" repeatCount="indefinite" />
            </circle>"""
```

---

### 64. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:124`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '360' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                <animate attributeName="opacity" from="1" to="0" dur="{duration}s" begin="{delay}s" repeatCount="indefinite" />
                <animate attributeName="transform" from="rotate({rotation}, {x}, {y})" to="rotate({rotation + 360}, {x}, {y})" dur="{duration*2}s" begin="{delay}s" repeatCount="indefinite" />
                <animate attributeName="cy" from="{y}" to="{y + random.randint(200, 400)}" dur="{duration}s" begin="{delay}s" repeatCount="indefinite" />
```

---

### 65. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:125`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '200' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                <animate attributeName="transform" from="rotate({rotation}, {x}, {y})" to="rotate({rotation + 360}, {x}, {y})" dur="{duration*2}s" begin="{delay}s" repeatCount="indefinite" />
                <animate attributeName="cy" from="{y}" to="{y + random.randint(200, 400)}" dur="{duration}s" begin="{delay}s" repeatCount="indefinite" />
            </polygon>"""
```

---

### 66. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:125`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '400' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                <animate attributeName="transform" from="rotate({rotation}, {x}, {y})" to="rotate({rotation + 360}, {x}, {y})" dur="{duration*2}s" begin="{delay}s" repeatCount="indefinite" />
                <animate attributeName="cy" from="{y}" to="{y + random.randint(200, 400)}" dur="{duration}s" begin="{delay}s" repeatCount="indefinite" />
            </polygon>"""
```

---

### 67. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:148`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '150' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    # Generate confetti elements
    confetti = generate_confetti(count=150, width=width, height=height)

```

---

### 68. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:154`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '20' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
  <defs>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="10" result="blur" />
```

---

### 69. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:154`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '20' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
  <defs>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="10" result="blur" />
```

---

### 70. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:154`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '140' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
  <defs>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="10" result="blur" />
```

---

### 71. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:154`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '140' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
  <defs>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="10" result="blur" />
```

---

### 72. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:166`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '20' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    <clipPath id="rounded-rect">
      <rect x="0" y="0" width="{width}" height="{height}" rx="20" ry="20" />
    </clipPath>
```

---

### 73. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:166`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '20' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    <clipPath id="rounded-rect">
      <rect x="0" y="0" width="{width}" height="{height}" rx="20" ry="20" />
    </clipPath>
```

---

### 74. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:190`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '20' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    <text x="{width/2}" y="{height/2 - 100}" class="aider-logo">flacoai</text>
    <text x="{width/2}" y="{height/2 + 20}" class="stars-text">30,000 GitHub stars!</text>
    <text x="{width/2}" y="{height/2 + 100}" class="tagline">Thank you to our amazing community!</text>
```

---

### 75. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:190`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '30' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    <text x="{width/2}" y="{height/2 - 100}" class="aider-logo">flacoai</text>
    <text x="{width/2}" y="{height/2 + 20}" class="stars-text">30,000 GitHub stars!</text>
    <text x="{width/2}" y="{height/2 + 100}" class="tagline">Thank you to our amazing community!</text>
```

---

### 76. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:192`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '50' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    <text x="{width/2}" y="{height/2 + 100}" class="tagline">Thank you to our amazing community!</text>
    <text x="{width/2}" y="{height - 50}" class="footer">github.com/flacoai-AI/flacoai</text>

```

---

### 77. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:72`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```

        # Generate random position
        x = random.randint(0, width)
        y = random.randint(0, height)

```

---

### 78. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:73`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
        # Generate random position
        x = random.randint(0, width)
        y = random.randint(0, height)

        # Skip if the position is in either of the safe zones
```

---

### 79. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:95`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```

        if shape_type == "rect":
            shape = f"""<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="{color}"
                    transform="rotate({rotation}, {x + size/2}, {y + size/2})">
                <animate attributeName="opacity" from="1" to="0" dur="{duration}s" begin="{delay}s" repeatCount="indefinite" />
```

---

### 80. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:95`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```

        if shape_type == "rect":
            shape = f"""<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="{color}"
                    transform="rotate({rotation}, {x + size/2}, {y + size/2})">
                <animate attributeName="opacity" from="1" to="0" dur="{duration}s" begin="{delay}s" repeatCount="indefinite" />
```

---

### 81. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:101`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
            </rect>"""
        elif shape_type == "circle":
            shape = f"""<circle cx="{x}" cy="{y}" r="{size/2}" fill="{color}">
                <animate attributeName="opacity" from="1" to="0" dur="{duration}s" begin="{delay}s" repeatCount="indefinite" />
                <animate attributeName="cy" from="{y}" to="{y + random.randint(200, 400)}" dur="{duration}s" begin="{delay}s" repeatCount="indefinite" />
```

---

### 82. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:154`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="10" result="blur" />
      <feComponentTransfer in="blur" result="glow">
```

---

### 83. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:154`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="10" result="blur" />
      <feComponentTransfer in="blur" result="glow">
```

---

### 84. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:166`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
    </linearGradient>
    <clipPath id="rounded-rect">
      <rect x="0" y="0" width="{width}" height="{height}" rx="20" ry="20" />
    </clipPath>
  </defs>
```

---

### 85. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:166`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
    </linearGradient>
    <clipPath id="rounded-rect">
      <rect x="0" y="0" width="{width}" height="{height}" rx="20" ry="20" />
    </clipPath>
  </defs>
```

---

### 86. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:180`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
  <g clip-path="url(#rounded-rect)">
    <!-- Background with pattern -->
    <rect class="main-bg" x="0" y="0" width="{width}" height="{height}" />

    <!-- Pattern overlay -->
```

---

### 87. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:180`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
  <g clip-path="url(#rounded-rect)">
    <!-- Background with pattern -->
    <rect class="main-bg" x="0" y="0" width="{width}" height="{height}" />

    <!-- Pattern overlay -->
```

---

### 88. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:189`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```

    <!-- Main content -->
    <text x="{width/2}" y="{height/2 - 100}" class="aider-logo">flacoai</text>
    <text x="{width/2}" y="{height/2 + 20}" class="stars-text">30,000 GitHub stars!</text>
    <text x="{width/2}" y="{height/2 + 100}" class="tagline">Thank you to our amazing community!</text>
```

---

### 89. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:189`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```

    <!-- Main content -->
    <text x="{width/2}" y="{height/2 - 100}" class="aider-logo">flacoai</text>
    <text x="{width/2}" y="{height/2 + 20}" class="stars-text">30,000 GitHub stars!</text>
    <text x="{width/2}" y="{height/2 + 100}" class="tagline">Thank you to our amazing community!</text>
```

---

### 90. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:190`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
    <!-- Main content -->
    <text x="{width/2}" y="{height/2 - 100}" class="aider-logo">flacoai</text>
    <text x="{width/2}" y="{height/2 + 20}" class="stars-text">30,000 GitHub stars!</text>
    <text x="{width/2}" y="{height/2 + 100}" class="tagline">Thank you to our amazing community!</text>
    <text x="{width/2}" y="{height - 50}" class="footer">github.com/flacoai-AI/flacoai</text>
```

---

### 91. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:190`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
    <!-- Main content -->
    <text x="{width/2}" y="{height/2 - 100}" class="aider-logo">flacoai</text>
    <text x="{width/2}" y="{height/2 + 20}" class="stars-text">30,000 GitHub stars!</text>
    <text x="{width/2}" y="{height/2 + 100}" class="tagline">Thank you to our amazing community!</text>
    <text x="{width/2}" y="{height - 50}" class="footer">github.com/flacoai-AI/flacoai</text>
```

---

### 92. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:191`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
    <text x="{width/2}" y="{height/2 - 100}" class="aider-logo">flacoai</text>
    <text x="{width/2}" y="{height/2 + 20}" class="stars-text">30,000 GitHub stars!</text>
    <text x="{width/2}" y="{height/2 + 100}" class="tagline">Thank you to our amazing community!</text>
    <text x="{width/2}" y="{height - 50}" class="footer">github.com/flacoai-AI/flacoai</text>

```

---

### 93. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:191`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
    <text x="{width/2}" y="{height/2 - 100}" class="aider-logo">flacoai</text>
    <text x="{width/2}" y="{height/2 + 20}" class="stars-text">30,000 GitHub stars!</text>
    <text x="{width/2}" y="{height/2 + 100}" class="tagline">Thank you to our amazing community!</text>
    <text x="{width/2}" y="{height - 50}" class="footer">github.com/flacoai-AI/flacoai</text>

```

---

### 94. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:192`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
    <text x="{width/2}" y="{height/2 + 20}" class="stars-text">30,000 GitHub stars!</text>
    <text x="{width/2}" y="{height/2 + 100}" class="tagline">Thank you to our amazing community!</text>
    <text x="{width/2}" y="{height - 50}" class="footer">github.com/flacoai-AI/flacoai</text>

  </g>
```

---

### 95. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:192`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
    <text x="{width/2}" y="{height/2 + 20}" class="stars-text">30,000 GitHub stars!</text>
    <text x="{width/2}" y="{height/2 + 100}" class="tagline">Thank you to our amazing community!</text>
    <text x="{width/2}" y="{height - 50}" class="footer">github.com/flacoai-AI/flacoai</text>

  </g>
```

---

### 96. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/30k-image.py:46`
**Severity:** LOW
**Category:** quality

**Description:** Function 'generate_confetti' has complexity of 15

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 15
```

---

### 97. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/integrations/jira_client.py:106`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '123' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        Args:
            issue_key: Issue key (e.g., "PROJ-123")

```

---

### 98. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/integrations/jira_client.py:116`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '50' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```

    def search_issues(self, jql: str, max_results: int = 50, fields: Optional[List[str]] = None):
        """Search issues using JQL.
```

---

### 99. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/integrations/jira_client.py:136`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '123' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        Args:
            issue_key: Issue key (e.g., "PROJ-123")
            **fields: Fields to update
```

---

### 100. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/integrations/jira_client.py:153`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '123' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        Args:
            issue_key: Issue key (e.g., "PROJ-123")
            comment: Comment text
```

---

### 101. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/integrations/jira_client.py:168`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '123' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        Args:
            issue_key: Issue key (e.g., "PROJ-123")
            transition: Transition name or ID
```

---

### 102. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/integrations/jira_client.py:184`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '123' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        Args:
            issue_key: Issue key (e.g., "PROJ-123")

```

---

### 103. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/integrations/jira_client.py:198`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '123' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        Args:
            issue_key: Issue key (e.g., "PROJ-123")
            commit_hash: Git commit hash
```

---

### 104. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/integrations/jira_client.py:246`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '123' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        Args:
            issue_key: Issue key (e.g., "PROJ-123")
            assignee: Username or account ID
```

---

### 105. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/integrations/jira_client.py:25`
**Severity:** LOW
**Category:** quality

**Description:** Function 'from_config' has complexity of 11

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 11
```

---

### 106. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/licensing/license_manager.py:261`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '16' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```

        return f"FLACO-{signature[:8].upper()}-{signature[8:16].upper()}-{signature[16:24].upper()}"

```

---

### 107. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/licensing/license_manager.py:261`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '16' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```

        return f"FLACO-{signature[:8].upper()}-{signature[8:16].upper()}-{signature[16:24].upper()}"

```

---

### 108. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/licensing/license_manager.py:295`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '03' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        tier = "pro"  # Default to pro for now
        expires = "2027-01-03"  # 1 year from now

```

---

### 109. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/licensing/license_manager.py:202`
**Severity:** LOW
**Category:** quality

**Description:** Function 'validate_license' has complexity of 12

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 12
```

---

### 110. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:67`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '03' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        ("OPENAI_API_KEY", "gpt-4o"),
        ("GEMINI_API_KEY", "gemini/gemini-2.5-pro-exp-03-25"),
        ("VERTEXAI_PROJECT", "vertex_ai/gemini-2.5-pro-exp-03-25"),
```

---

### 111. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:68`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '03' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        ("GEMINI_API_KEY", "gemini/gemini-2.5-pro-exp-03-25"),
        ("VERTEXAI_PROJECT", "vertex_ai/gemini-2.5-pro-exp-03-25"),
    ]
```

---

### 112. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:167`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '64' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
def generate_pkce_codes():
    code_verifier = secrets.token_urlsafe(64)
    hasher = hashlib.sha256()
```

---

### 113. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:185`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '30' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            },
            timeout=30,  # Add a timeout
        )
```

---

### 114. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:237`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '200' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                    auth_code = query_params["code"][0]
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
```

---

### 115. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:250`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '302' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                    # Redirect to flacoai website if 'code' is missing (e.g., user visited manually)
                    self.send_response(302)  # Found (temporary redirect)
                    self.send_header("Location", urls.website)
```

---

### 116. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:257`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '302' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                # Redirect anything else (e.g., favicon.ico) to the main website as well
                self.send_response(302)
                self.send_header("Location", urls.website)
```

---

### 117. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:386`
**Severity:** LOW
**Category:** quality

**Description:** Lowercase class name

**Recommendation:** Use descriptive, meaningful names

**Code:**
```


# Dummy Analytics class for testing
class DummyAnalytics:
    def event(self, *args, **kwargs):
```

---

### 118. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:79`
**Severity:** LOW
**Category:** quality

**Description:** Function 'offer_openrouter_oauth' has complexity of 11

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 11
```

---

### 119. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:116`
**Severity:** LOW
**Category:** quality

**Description:** Function 'select_default_model' has complexity of 14

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 14
```

---

### 120. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/fixtures/languages/csharp/test.cs:21`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '150' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        private const string PREFIX = "Good day";
        private static readonly int MAX_AGE = 150;

```

---

### 121. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/fixtures/languages/csharp/test.cs:35`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '42' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            var greeter = new FormalGreeter();
            var person = new Person("World", 42);
            Console.WriteLine(greeter.GreetPerson(person));
```

---

### 122. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/deprecated.py:24`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '0613' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    )
    gpt_4_model = "gpt-4-0613"
    group.add_argument(
```

---

### 123. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/deprecated.py:56`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '35' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        "--35turbo",
        "--35-turbo",
        "--3",
```

---

### 124. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/deprecated.py:93`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '0613' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        "haiku": "claude-3-5-haiku-20241022",
        "4": "gpt-4-0613",
        "4o": "gpt-4o",
```

---

### 125. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/deprecated.py:1`
**Severity:** LOW
**Category:** quality

**Description:** Function 'add_deprecated_model_args' has complexity of 12

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 12
```

---

### 126. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/deprecated.py:86`
**Severity:** LOW
**Category:** quality

**Description:** Function 'handle_deprecated_model_args' has complexity of 12

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 12
```

---

### 127. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_reasoning.py:93`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' has complexity of 15

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 15
```

---

### 128. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_reasoning.py:276`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' has complexity of 15

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 15
```

---

### 129. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_reasoning.py:484`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' has complexity of 15

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 15
```

---

### 130. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/screenshot_prompts.py:22`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '15' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
When generating SwiftUI code:
1. Use modern SwiftUI best practices (iOS 15+)
2. Create proper view hierarchy matching the layout
```

---

### 131. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/screenshot_prompts.py:105`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '64' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                Image(systemName: "lock.shield.fill")
                    .font(.system(size: 64))
                    .foregroundColor(.accentColor)
```

---

### 132. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/screenshot_prompts.py:112`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '40' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            }
            .padding(.bottom, 40)

```

---

### 133. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/screenshot_prompts.py:139`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '50' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            .frame(maxWidth: .infinity)
            .frame(height: 50)
            .background(Color.accentColor)
```

---

### 134. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/screenshot_prompts.py:158`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '32' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        }
        .padding(.horizontal, 32)
    }
```

---

### 135. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_wholefile.py:92`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '20' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        # the live diff should be concise, since we haven't changed anything yet
        self.assertLess(len(lines), 20)

```

---

### 136. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:627`
**Severity:** LOW
**Category:** quality

**Description:** Function '_' has complexity of 11

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 11
```

---

### 137. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:928`
**Severity:** LOW
**Category:** quality

**Description:** Function 'prompt_ask' has complexity of 11

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 11
```

---

### 138. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:966`
**Severity:** LOW
**Category:** quality

**Description:** Function '_tool_message' has complexity of 15

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 15
```

---

### 139. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:1055`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_default_notification_command' has complexity of 11

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 11
```

---

### 140. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/args.py:718`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '639' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        default="en",
        help="Specify the language for voice using ISO 639-1 code (default: auto)",
    )
```

---

### 141. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/args.py:879`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '70' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
def get_md_help():
    os.environ["COLUMNS"] = "70"
    sys.argv = ["aider"]
```

---

### 142. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/args.py:905`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '120' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
def get_sample_dotenv():
    os.environ["COLUMNS"] = "120"
    sys.argv = ["aider"]
```

---

### 143. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:441`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
def find_original_update_blocks(content, fence=DEFAULT_FENCE, valid_fnames=None):
    lines = content.splitlines(keepends=True)
    i = 0
    current_filename = None

```

---

### 144. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:589`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
    # Perform fuzzy matching with valid_fnames
    for fname in filenames:
        close_matches = difflib.get_close_matches(fname, valid_fnames, n=1, cutoff=0.8)
        if len(close_matches) == 1:
            return close_matches[0]
```

---

### 145. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/problem_stats.py:146`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '40' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    print("\nExercise Solution Statistics:")
    print("-" * 40)

```

---

### 146. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/problem_stats.py:209`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '50' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    print("Models  Exercises  Cumulative  RevCumulative")
    print("-" * 50)
    counts = [0] * (total_models + 1)
```

---

### 147. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/problem_stats.py:264`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '12' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    print("\nUnsolved and hard set problems by language:")
    print(f"{'Language':<12} {'Unsolved':>8} {'Hard Set':>9} {'Total':>7} {'%hardUnsolved':>8}")
    print("-" * 47)
```

---

### 148. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/problem_stats.py:265`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '47' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    print(f"{'Language':<12} {'Unsolved':>8} {'Hard Set':>9} {'Total':>7} {'%hardUnsolved':>8}")
    print("-" * 47)
    for lang in sorted(lang_totals.keys()):
```

---

### 149. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/problem_stats.py:271`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '12' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        pct = (count / hard) * 100 if hard else -1
        print(f"{lang:<12} {count:>8} {hard:>9} {total:>7} {pct:>7.1f}%")
    print()
```

---

### 150. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/problem_stats.py:302`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '55' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    print("\nModel performance on hard set:")
    print(f"{'Model':<55} {'Solved':<8} {'Percent':>7}")
    print("-" * 50)
```

---

### 151. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/problem_stats.py:303`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '50' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    print(f"{'Model':<55} {'Solved':<8} {'Percent':>7}")
    print("-" * 50)
    for model, solved, pct in model_hard_stats:
```

---

### 152. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/problem_stats.py:305`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '55' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    for model, solved, pct in model_hard_stats:
        print(f"{model:<55} {solved:>6d}   {pct:>6.1f}%")

```

---

### 153. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_symbols_analyzer.py:192`
**Severity:** LOW
**Category:** quality

**Description:** Function '_check_sf_symbol_usage' has complexity of 11

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 11
```

---

### 154. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_prompts.py:62`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
    "compute factorial"

    if n == 0:
        return 1
    else:
```

---

### 155. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_prompts.py:108`
**Severity:** LOW
**Category:** quality

**Description:** Function 'hello' has complexity of 14

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 14
```

---

### 156. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/fixtures/languages/go/test.go:40`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '42' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    greeter := NewFormalGreeter()
    person := Person{Name: DefaultName, Age: 42}
    fmt.Println(greeter.Greet(person))
```

---

### 157. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_urls.py:15`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '200' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        response = requests.get(url)
        assert response.status_code == 200, f"URL {url} returned status code {response.status_code}"

```

---

### 158. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/custom_rules_analyzer.py:352`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '123' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                "category": "quality",
                "message": "TODO comment without ticket reference (e.g., TODO: PROJ-123)",
                "recommendation": "Add ticket reference to TODO comment for tracking",
```

---

### 159. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2119`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '00' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            if value == 0:
                return "0.00"
            magnitude = abs(value)
```

---

### 160. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2121`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '01' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            magnitude = abs(value)
            if magnitude >= 0.01:
                return f"{value:.2f}"
```

---

### 161. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2317`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '20' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        warn_number_of_files = 4
        warn_number_of_tokens = 20 * 1024

```

---

### 162. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:885`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_images_message' has complexity of 13

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 13
```

---

### 163. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1116`
**Severity:** LOW
**Category:** quality

**Description:** Function 'normalize_language' has complexity of 13

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 13
```

---

### 164. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1242`
**Severity:** LOW
**Category:** quality

**Description:** Function 'fmt_system_prompt' has complexity of 11

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 11
```

---

### 165. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1696`
**Severity:** LOW
**Category:** quality

**Description:** Function 'show_exhausted_error' has complexity of 13

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 13
```

---

### 166. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1851`
**Severity:** LOW
**Category:** quality

**Description:** Function 'send' has complexity of 12

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 12
```

---

### 167. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1904`
**Severity:** LOW
**Category:** quality

**Description:** Function 'show_send_output' has complexity of 14

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 14
```

---

### 168. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2062`
**Severity:** LOW
**Category:** quality

**Description:** Function 'calculate_and_show_tokens_and_cost' has complexity of 15

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 15
```

---

### 169. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2259`
**Severity:** LOW
**Category:** quality

**Description:** Function 'allowed_to_edit' has complexity of 14

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 14
```

---

### 170. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2518`
**Severity:** LOW
**Category:** quality

**Description:** Function 'handle_shell_commands' has complexity of 15

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 15
```

---

### 171. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:1265`
**Severity:** LOW
**Category:** quality

**Description:** Function 'check_and_load_imports' has complexity of 13

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 13
```

---

### 172. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/patch_coder.py:295`
**Severity:** LOW
**Category:** quality

**Description:** Lowercase class name

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
        """
        Parses patch content lines into a Patch object.
        Adapted from the Parser class in apply_patch.py.
        """
        patch = Patch()
```

---

### 173. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/patch_coder.py:59`
**Severity:** LOW
**Category:** quality

**Description:** Function 'find_context_core' has complexity of 13

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 13
```

---

### 174. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:149`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '250' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        return
    if method_children < 250:
        return
```

---

### 175. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:59`
**Severity:** LOW
**Category:** quality

**Description:** Lowercase class name

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
    assert (
        pct_diff_children < 10
    ), f"Old class had {old_class_children} children, new class has {num_children}"


```

---

### 176. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:59`
**Severity:** LOW
**Category:** quality

**Description:** Lowercase class name

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
    assert (
        pct_diff_children < 10
    ), f"Old class had {old_class_children} children, new class has {num_children}"


```

---

### 177. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:172`
**Severity:** LOW
**Category:** quality

**Description:** Lowercase class name

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
    ins_fname.write_text(f"""# Refactor {class_name}.{method_name}

Refactor the `{method_name}` method in the `{class_name}` class to be a stand alone, top level function.
Name the new function `{method_name}`, exactly the same name as the existing method.
Update any existing `self.{method_name}` calls to work with the new `{method_name}` function.
```

---

### 178. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:82`
**Severity:** LOW
**Category:** quality

**Description:** Function 'visit_FunctionDef' has complexity of 14

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 14
```

---

### 179. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/fixtures/languages/tsx/test.tsx:28`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '150' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
const DEFAULT_NAME = 'World';
const MAX_AGE = 150;

```

---

### 180. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/fixtures/languages/tsx/test.tsx:22`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
function useCounter(initial: number = 0) {
    const [count, setCount] = useState(initial);
    const increment = () => setCount(c => c + 1);
    return { count, increment };
}
```

---

### 181. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/report_generator.py:112`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '50' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                    finding.title,
                    finding.recommendation[:50] + "..." if len(finding.recommendation) > 50 else finding.recommendation
                )
```

---

### 182. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/report_generator.py:112`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '50' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                    finding.title,
                    finding.recommendation[:50] + "..." if len(finding.recommendation) > 50 else finding.recommendation
                )
```

---

### 183. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/report_generator.py:118`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '40' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```

        if stats['total'] > 40:
            self.io.console.print(f"[yellow]Showing first 40 issues. Use markdown report for full details.[/yellow]")
```

---

### 184. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/report_generator.py:119`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '40' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        if stats['total'] > 40:
            self.io.console.print(f"[yellow]Showing first 40 issues. Use markdown report for full details.[/yellow]")

```

---

### 185. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/report_generator.py:296`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '40' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```

    def _short_path(self, file_path: str, max_length: int = 40) -> str:
        """Shorten file path for display."""
```

---

### 186. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/report_generator.py:60`
**Severity:** LOW
**Category:** quality

**Description:** Function 'display_console' has complexity of 12

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 12
```

---

### 187. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/openrouter.py:117`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '200' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            response = requests.get(self.MODELS_URL, timeout=10, verify=self.verify_ssl)
            if response.status_code == 200:
                self.content = response.json()
```

---

### 188. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/openrouter.py:6`
**Severity:** LOW
**Category:** quality

**Description:** Lowercase class name

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
This module keeps a local cached copy of the OpenRouter model list
(downloaded from ``https://openrouter.ai/api/v1/models``) and exposes a
helper class that returns metadata for a given model in a format compatible
with litellm’s ``get_model_info``.
"""
```

---

### 189. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/openrouter.py:47`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_model_info' has complexity of 12

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 12
```

---

### 190. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/udiff_coder.py:234`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '66' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```

    if len(new_before) < len(before) * 0.66:
        return hunk
```

---

### 191. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/udiff_coder.py:237`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
        return hunk

    new_hunk = difflib.unified_diff(new_before, after, n=max(len(new_before), len(after)))
    new_hunk = list(new_hunk)[3:]

```

---

### 192. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/udiff_coder.py:256`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
    after = cleanup_pure_whitespace_lines(after)

    diff = difflib.unified_diff(before, after, n=max(len(before), len(after)))
    diff = list(diff)[3:]
    return diff
```

---

### 193. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:224`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '14' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        days_inactive = (datetime.now() - latest_activity).days
        if days_inactive >= 14:
            print(f"\nStale issue found: #{issue['number']}: {issue['title']}\n{issue['html_url']}")
```

---

### 194. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:371`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '21' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```

        if days_fixed >= 21:
            issue_type = "enhancement" if is_enhancement else "bug"
```

---

### 195. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:397`
**Severity:** LOW
**Category:** quality

**Description:** Function 'handle_duplicate_issues' has complexity of 15

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 15
```

---

### 196. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:112`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '50' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    if title:
        output.append(f"{title.upper()} {'*' * 50}")

```

---

### 197. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:109`
**Severity:** LOW
**Category:** quality

**Description:** Function 'format_messages' has complexity of 13

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 13
```

---

### 198. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/template_engine.py:353`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '80' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```

    print("\n" + "=" * 80 + "\n")

```

---

### 199. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/template_engine.py:359`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '500' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    if code:
        print(code[:500] + "...")

```

---

### 200. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/template_engine.py:361`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '80' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```

    print("\n" + "=" * 80 + "\n")

```

---

### 201. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/template_engine.py:367`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '500' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    if code:
        print(code[:500] + "...")

```

---

### 202. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/homepage.py:294`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '25' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
  <a href="https://flacoai.chat/HISTORY.html"><img alt="Singularity" title="{SINGULARITY_TOOLTIP}"
src="https://img.shields.io/badge/🔄%20Singularity-{flacoai_percent_rounded}%25-e74c3c?style=flat-square&labelColor=555555"/></a>"""  # noqa

```

---

### 203. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/homepage.py:403`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '20' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    <span class="badge-label">🏆 OpenRouter</span>
    <span class="badge-value">Top 20</span>
</a>
```

---

### 204. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/homepage.py:88`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_downloads_from_bigquery' has complexity of 15

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 15
```

---

### 205. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/homepage.py:208`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_latest_release_flacoai_percentage' has complexity of 12

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 12
```

---

### 206. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/homepage.py:299`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_badges_md' has complexity of 14

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 14
```

---

### 207. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:18`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '12' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        # HIG-recommended spacing
        self.standard_spacing = [8, 12, 16, 20, 24, 32]

```

---

### 208. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:18`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '16' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        # HIG-recommended spacing
        self.standard_spacing = [8, 12, 16, 20, 24, 32]

```

---

### 209. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:18`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '20' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        # HIG-recommended spacing
        self.standard_spacing = [8, 12, 16, 20, 24, 32]

```

---

### 210. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:18`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '32' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        # HIG-recommended spacing
        self.standard_spacing = [8, 12, 16, 20, 24, 32]

```

---

### 211. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:173`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '50' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                    # Check if it's a non-standard spacing value
                    if value not in self.standard_spacing and value > 0 and value < 50:
                        # Only flag if it's not a multiple of 4 (8-point grid)
```

---

### 212. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:318`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '34' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        # Map font sizes to text styles (approximate)
        if size >= 34:
            return ".largeTitle"
```

---

### 213. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:320`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '28' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            return ".largeTitle"
        elif size >= 28:
            return ".title"
```

---

### 214. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:322`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '22' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            return ".title"
        elif size >= 22:
            return ".title2"
```

---

### 215. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:324`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '20' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            return ".title2"
        elif size >= 20:
            return ".title3"
```

---

### 216. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:326`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '17' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            return ".title3"
        elif size >= 17:
            return ".body"
```

---

### 217. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:328`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '15' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            return ".body"
        elif size >= 15:
            return ".callout"
```

---

### 218. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:330`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '13' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            return ".callout"
        elif size >= 13:
            return ".subheadline"
```

---

### 219. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:332`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '12' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            return ".subheadline"
        elif size >= 12:
            return ".footnote"
```

---

### 220. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:334`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '11' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            return ".footnote"
        elif size >= 11:
            return ".caption"
```

---

### 221. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:39`
**Severity:** LOW
**Category:** quality

**Description:** Function '_check_touch_targets' has complexity of 15

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 15
```

---

### 222. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:155`
**Severity:** LOW
**Category:** quality

**Description:** Function '_check_spacing_values' has complexity of 13

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 13
```

---

### 223. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:196`
**Severity:** LOW
**Category:** quality

**Description:** Function '_check_color_usage' has complexity of 11

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 11
```

---

### 224. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:315`
**Severity:** LOW
**Category:** quality

**Description:** Function '_suggest_text_style' has complexity of 11

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 11
```

---

### 225. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/integrations/github_exporter.py:88`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '256' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                        "gh", "issue", "create",
                        "--title", title[:256],  # GitHub title limit
                        "--body", body,
```

---

### 226. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/integrations/github_exporter.py:103`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '50' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                    if self.io:
                        short_title = title[:50] + "..." if len(title) > 50 else title
                        self.io.tool_output(f"✓ Created: {short_title}")
```

---

### 227. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/integrations/github_exporter.py:103`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '50' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                    if self.io:
                        short_title = title[:50] + "..." if len(title) > 50 else title
                        self.io.tool_output(f"✓ Created: {short_title}")
```

---

### 228. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1140`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '512' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            summarize_from_coder=False,
            map_tokens=512,
            map_mul_no_files=1,
```

---

### 229. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1460`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '12' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            for template in engine.list_templates():
                self.io.tool_output(f"  • {template['name']:12} - {template['description']}")
            self.io.tool_output("\nUsage: /generate <template> <prompt>")
```

---

### 230. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1506`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '80' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                # Output to terminal
                self.io.tool_output("\n" + "=" * 80)
                self.io.tool_output(generated_code)
```

---

### 231. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1508`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '80' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                self.io.tool_output(generated_code)
                self.io.tool_output("=" * 80 + "\n")

```

---

### 232. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1729`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '09' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                self.io.tool_output("  • gpt-4-vision-preview")
                self.io.tool_output("  • gpt-4-turbo (gpt-4-turbo-2024-04-09)")
                self.io.tool_output("  • gpt-4o")
```

---

### 233. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1781`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '80' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            if preview_mode:
                self.io.tool_output("\n" + "=" * 80)
                self.io.tool_output("📊 Screenshot Analysis:\n")
```

---

### 234. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1784`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '80' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                self.io.tool_output(response_text)
                self.io.tool_output("=" * 80 + "\n")
            else:
```

---

### 235. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1813`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '80' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                    # Display code
                    self.io.tool_output("\n" + "=" * 80)
                    self.io.tool_output(response_text)
```

---

### 236. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1815`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '80' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                    self.io.tool_output(response_text)
                    self.io.tool_output("=" * 80 + "\n")

```

---

### 237. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2048`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '80' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        self.io.tool_output("")
        self.io.tool_output("=" * 80)

```

---

### 238. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2221`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '50' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        # Display table
        formatter.display_issues_table(issues, title=f"Search Results: {jql[:50]}...")

```

---

### 239. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2229`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '123' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            self.io.tool_error("Usage: /jira show <KEY>")
            self.io.tool_error("Example: /jira show PROJ-123")
            return
```

---

### 240. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2358`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '255' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            try:
                summary = f"{finding.title} in {finding.file}:{finding.line}"[:255]

```

---

### 241. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2466`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            if response:
                self.io.tool_output("="*75)
                self.io.tool_output(f"📋 Implementation Plan: {issue_key}")
```

---

### 242. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2468`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                self.io.tool_output(f"📋 Implementation Plan: {issue_key}")
                self.io.tool_output("="*75)
                self.io.tool_output(response)
```

---

### 243. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2470`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                self.io.tool_output(response)
                self.io.tool_output("="*75 + "\n")
                self.io.tool_output(f"💡 Tip: Use '/jira link {issue_key}' when you start working on this")
```

---

### 244. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2545`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                content = memory_file.read_text(encoding='utf-8')
                self.io.tool_output("\n" + "="*75)
                self.io.tool_output(content)
```

---

### 245. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2547`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                self.io.tool_output(content)
                self.io.tool_output("="*75 + "\n")

```

---

### 246. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2645`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```

        self.io.tool_output("\n" + "="*75)
        self.io.tool_output("🤖 Available Models")
```

---

### 247. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2647`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        self.io.tool_output("🤖 Available Models")
        self.io.tool_output("="*75 + "\n")

```

---

### 248. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2665`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '30' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            marker = "✓" if model_name == current_model else " "
            self.io.tool_output(f"  [{marker}] {model_name:<30} {description}")

```

---

### 249. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2680`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '35' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            marker = "✓" if model_name == current_model else " "
            self.io.tool_output(f"  [{marker}] {model_name:<35} {description}")

```

---

### 250. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2700`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        self.io.tool_output("💡 Tip: Use '/llm search <term>' to find specific models")
        self.io.tool_output("="*75 + "\n")

```

---

### 251. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2716`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '20' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```

        for model_name in matches[:20]:  # Limit to top 20
            marker = "✓" if model_name == current_model else " "
```

---

### 252. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2720`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '20' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```

        if len(matches) > 20:
            self.io.tool_output(f"\n  ... and {len(matches) - 20} more matches")
```

---

### 253. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2721`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '20' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        if len(matches) > 20:
            self.io.tool_output(f"\n  ... and {len(matches) - 20} more matches")

```

---

### 254. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2759`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '50' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
- Types: feat, fix, refactor, docs, test, chore, style
- Keep subject under 50 characters
- Focus on the "why" not the "what"
```

---

### 255. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2789`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```

            self.io.tool_output("\n" + "="*75)
            self.io.tool_output("📝 Suggested Commit Message:")
```

---

### 256. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2791`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            self.io.tool_output("📝 Suggested Commit Message:")
            self.io.tool_output("="*75)
            self.io.tool_output(commit_msg)
```

---

### 257. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2793`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            self.io.tool_output(commit_msg)
            self.io.tool_output("="*75 + "\n")

```

---

### 258. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2854`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```

            self.io.tool_output("="*75)
            self.io.tool_output("📋 Code Review:")
```

---

### 259. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2856`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            self.io.tool_output("📋 Code Review:")
            self.io.tool_output("="*75)
            self.io.tool_output(response)
```

---

### 260. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2858`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            self.io.tool_output(response)
            self.io.tool_output("="*75 + "\n")

```

---

### 261. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3016`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            if response:
                self.io.tool_output("="*75)
                self.io.tool_output(f"📊 Standup Summary ({days} day(s))")
```

---

### 262. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3018`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                self.io.tool_output(f"📊 Standup Summary ({days} day(s))")
                self.io.tool_output("="*75)
                self.io.tool_output(response)
```

---

### 263. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3020`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                self.io.tool_output(response)
                self.io.tool_output("="*75 + "\n")

```

---

### 264. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3074`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```

            self.io.tool_output("\n" + "="*75)
            self.io.tool_output("📋 Project Summary")
```

---

### 265. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3076`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            self.io.tool_output("📋 Project Summary")
            self.io.tool_output("="*75)
            self.io.tool_output(summary_text)
```

---

### 266. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3078`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            self.io.tool_output(summary_text)
            self.io.tool_output("="*75 + "\n")

```

---

### 267. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3125`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            if response:
                self.io.tool_output("="*75)
                self.io.tool_output(f"📋 Implementation Plan: {task}")
```

---

### 268. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3127`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                self.io.tool_output(f"📋 Implementation Plan: {task}")
                self.io.tool_output("="*75)
                self.io.tool_output(response)
```

---

### 269. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3129`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                self.io.tool_output(response)
                self.io.tool_output("="*75 + "\n")
                self.io.tool_output("💡 Tip: Use '/mode architect' for architecture-focused development")
```

---

### 270. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3171`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '20' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                    # Get first 20 lines
                    lines = content.split('\n')[:20]
                    sample = '\n'.join(lines)
```

---

### 271. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3202`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            if response:
                self.io.tool_output("="*75)
                self.io.tool_output(f"🗺️  Codebase Tour{f': {component}' if component else ''}")
```

---

### 272. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3204`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                self.io.tool_output(f"🗺️  Codebase Tour{f': {component}' if component else ''}")
                self.io.tool_output("="*75)
                self.io.tool_output(response)
```

---

### 273. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3206`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                self.io.tool_output(response)
                self.io.tool_output("="*75 + "\n")

```

---

### 274. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3321`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '50' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            preview = (
                last_assistant_message[:50] + "..."
                if len(last_assistant_message) > 50
```

---

### 275. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1911`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```

                        for f in files:
                            if f == file_arg or os.path.splitext(f)[0] == base_name:
                                full_path = os.path.join(root, f)
                                candidates.append(full_path)
```

---

### 276. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:453`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_tokens' has complexity of 11

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 11
```

---

### 277. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:524`
**Severity:** LOW
**Category:** quality

**Description:** Function 'fmt' has complexity of 11

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 11
```

---

### 278. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:773`
**Severity:** LOW
**Category:** quality

**Description:** Function 'glob_filtered_to_repo' has complexity of 13

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 13
```

---

### 279. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1011`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_run' has complexity of 15

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 15
```

---

### 280. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1062`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_ls' has complexity of 15

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 15
```

---

### 281. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2641`
**Severity:** LOW
**Category:** quality

**Description:** Function '_llm_list' has complexity of 15

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 15
```

---

### 282. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:2958`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_standup' has complexity of 14

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 14
```

---

### 283. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3025`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_summary' has complexity of 13

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 13
```

---

### 284. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3083`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_plan' has complexity of 11

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 11
```

---

### 285. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3417`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_copy_context' has complexity of 13

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 13
```

---

### 286. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/review_coder.py:233`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '255' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                    project=project_key,
                    summary=summary[:255],  # Jira limit
                    description=description,
```

---

### 287. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/review_coder.py:241`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '50' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                if self.io:
                    self.io.tool_output(f"Created {issue.key}: {summary[:50]}...")

```

---

### 288. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/review_coder.py:170`
**Severity:** LOW
**Category:** quality

**Description:** Function 'export_to_jira' has complexity of 13

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 13
```

---

### 289. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:16`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '15' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        self.deprecated_packages = {
            'Alamofire/AlamofireImage': 'Consider using native AsyncImage (iOS 15+)',
            'onevcat/Kingfisher': 'Consider using native AsyncImage (iOS 15+) for simple cases',
```

---

### 290. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:17`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '15' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            'Alamofire/AlamofireImage': 'Consider using native AsyncImage (iOS 15+)',
            'onevcat/Kingfisher': 'Consider using native AsyncImage (iOS 15+) for simple cases',
            'SwiftyJSON/SwiftyJSON': 'Use native Codable instead',
```

---

### 291. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:90`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '15' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        # Check for too many dependencies
        if len(matches) > 15:
            result = AnalysisResult(
```

---

### 292. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:209`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '14' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            # Warn if iOS version is very old
            if version < 14:
                code_snippet = self.get_lines_context(content, line_num, context_lines=1)
```

---

### 293. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:219`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '14' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                    description=f"Package targets iOS {version}",
                    recommendation=f"Consider updating to iOS 14+ to drop legacy code",
                    code_snippet=code_snippet,
```

---

### 294. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:225`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '15' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            # Suggest iOS 15+ for modern features
            if version < 15:
                result = AnalysisResult(
```

---

### 295. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:231`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '15' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                    category=Category.QUALITY,
                    title="Consider iOS 15+",
                    description=f"Package targets iOS {version}",
```

---

### 296. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:233`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '15' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                    description=f"Package targets iOS {version}",
                    recommendation="iOS 15+ enables modern Swift Concurrency and SwiftUI features",
                    code_snippet=code_snippet,
```

---

### 297. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:81`
**Severity:** LOW
**Category:** quality

**Description:** Function '_check_dependencies' has complexity of 13

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 13
```

---

### 298. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:146`
**Severity:** LOW
**Category:** quality

**Description:** Function '_check_version_pinning' has complexity of 13

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 13
```

---

### 299. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/baseline_manager.py:83`
**Severity:** LOW
**Category:** quality

**Description:** Function 'fingerprint' has complexity of 13

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 13
```

---

### 300. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/baseline_manager.py:122`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_stats' has complexity of 13

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 13
```

---

### 301. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_version_analyzer.py:214`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '14' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                # Warn if deployment target is very old
                if major < 14:
                    code_snippet = self.get_lines_context(content, line_num, context_lines=1)
```

---

### 302. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_version_analyzer.py:230`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '15' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                # Suggest updating to iOS 15+ for modern SwiftUI
                if major < 15:
                    result = AnalysisResult(
```

---

### 303. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_version_analyzer.py:236`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '15' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                        category=Category.QUALITY,
                        title="Consider iOS 15+ Deployment Target",
                        description=f"Deployment target is iOS {version}",
```

---

### 304. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_version_analyzer.py:238`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '15' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                        description=f"Deployment target is iOS {version}",
                        recommendation="iOS 15+ enables modern SwiftUI features (.refreshable, .searchable, AsyncImage)",
                        code_snippet=code_snippet,
```

---

### 305. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_version_analyzer.py:104`
**Severity:** LOW
**Category:** quality

**Description:** Function '_check_version_requirements' has complexity of 15

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 15
```

---

### 306. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_version_analyzer.py:149`
**Severity:** LOW
**Category:** quality

**Description:** Function '_check_availability_annotations' has complexity of 13

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 13
```

---

### 307. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:77`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '50' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            # Flag if body is too large
            if line_count > 50:
                line_num = content[:match.start()].count('\n') + 1
```

---

### 308. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:232`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '17' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                description="Using PreviewProvider instead of #Preview macro",
                recommendation="Use #Preview { YourView() } for cleaner syntax (iOS 17+)",
                code_snippet=code_snippet,
```

---

### 309. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:336`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '17' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    def _check_observable_patterns(self, file_path: str, content: str) -> List[AnalysisResult]:
        """Check for Observable macro usage (iOS 17+)."""
        results = []
```

---

### 310. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:355`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '17' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                description=f"Class '{class_name}' uses ObservableObject",
                recommendation="Consider using @Observable macro for cleaner syntax (iOS 17+)",
                code_snippet=code_snippet,
```

---

### 311. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:121`
**Severity:** LOW
**Category:** quality

**Description:** Lowercase class name

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
                    category=Category.QUALITY,
                    title="@State with Reference Type",
                    description="Using @State with a class instance",
                    recommendation="Use @StateObject for classes, @State for value types only",
                    code_snippet=code_snippet,
```

---

### 312. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:98`
**Severity:** LOW
**Category:** quality

**Description:** Function '_check_state_management' has complexity of 11

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 11
```

---

### 313. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:144`
**Severity:** LOW
**Category:** quality

**Description:** Function '_check_view_builder_usage' has complexity of 13

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 13
```

---

### 314. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:193`
**Severity:** LOW
**Category:** quality

**Description:** Function '_check_preview_usage' has complexity of 11

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 11
```

---

### 315. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:285`
**Severity:** LOW
**Category:** quality

**Description:** Function '_check_onappear_usage' has complexity of 12

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 12
```

---

### 316. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/doc_generators/changelog_generator.py:126`
**Severity:** LOW
**Category:** quality

**Description:** Function '_group_commits' has complexity of 11

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 11
```

---

### 317. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/doc_generators/changelog_generator.py:178`
**Severity:** LOW
**Category:** quality

**Description:** Function '_generate_version_section' has complexity of 15

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 15
```

---

### 318. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/review_prompts.py:32`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '500' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
- Force unwrapping (!) and implicitly unwrapped optionals
- Large SwiftUI view bodies (>500 chars)
- Missing accessibility labels
```

---

### 319. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/review_prompts.py:40`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '300' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
**Architecture:**
- Massive View Controller (>300 lines, >15 methods)
- Singleton overuse
```

---

### 320. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/review_prompts.py:40`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '15' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
**Architecture:**
- Massive View Controller (>300 lines, >15 methods)
- Singleton overuse
```

---

### 321. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:126`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '20' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                # Check if description is too short or generic
                if not value or len(value) < 20:
                    result = AnalysisResult(
```

---

### 322. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:87`
**Severity:** LOW
**Category:** quality

**Description:** Single letter variable

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
        children = list(dict_elem)

        i = 0
        while i < len(children):
            if children[i].tag == 'key':
```

---

### 323. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:116`
**Severity:** LOW
**Category:** quality

**Description:** Function '_check_privacy_descriptions' has complexity of 13

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 13
```

---

### 324. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:166`
**Severity:** LOW
**Category:** quality

**Description:** Function '_check_ats_configuration' has complexity of 12

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 12
```

---

### 325. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:210`
**Severity:** LOW
**Category:** quality

**Description:** Function '_check_url_schemes' has complexity of 13

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 13
```

---

### 326. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/branding.py:112`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '75' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
    # Add a decorative line
    border = "─" * min(len(header), 75)

```

---

### 327. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/branding.py:128`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '12' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```

    if hour < 12:
        greeting = "Good morning"
```

---

### 328. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/branding.py:130`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '18' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
```

---

### 329. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:41`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '200' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        self.complexity_patterns = [
            (r'class\s+\w+.*:\s*\n(?:(?:.*\n){200,})', "Large class (>200 lines)"),
            (r'def\s+\w+.*:\s*\n(?:(?:.*\n){50,})(?=def\s|\nclass\s|\Z)', "Long function (>50 lines)"),
```

---

### 330. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:41`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '200' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        self.complexity_patterns = [
            (r'class\s+\w+.*:\s*\n(?:(?:.*\n){200,})', "Large class (>200 lines)"),
            (r'def\s+\w+.*:\s*\n(?:(?:.*\n){50,})(?=def\s|\nclass\s|\Z)', "Long function (>50 lines)"),
```

---

### 331. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:42`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '50' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            (r'class\s+\w+.*:\s*\n(?:(?:.*\n){200,})', "Large class (>200 lines)"),
            (r'def\s+\w+.*:\s*\n(?:(?:.*\n){50,})(?=def\s|\nclass\s|\Z)', "Long function (>50 lines)"),
        ]
```

---

### 332. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:42`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '50' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            (r'class\s+\w+.*:\s*\n(?:(?:.*\n){200,})', "Large class (>200 lines)"),
            (r'def\s+\w+.*:\s*\n(?:(?:.*\n){50,})(?=def\s|\nclass\s|\Z)', "Long function (>50 lines)"),
        ]
```

---

### 333. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:65`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '500' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        self.ios_swiftui_patterns = [
            (r'var\s+body:\s*some\s+View\s*\{(?:[^}]{500,})\}', "Large SwiftUI body (>500 chars)"),
            (r'@State\s+var\s+\w+.*=.*\n.*@State', "Multiple @State vars (consider @StateObject or view model)"),
```

---

### 334. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:65`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '500' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        self.ios_swiftui_patterns = [
            (r'var\s+body:\s*some\s+View\s*\{(?:[^}]{500,})\}', "Large SwiftUI body (>500 chars)"),
            (r'@State\s+var\s+\w+.*=.*\n.*@State', "Multiple @State vars (consider @StateObject or view model)"),
```

---

### 335. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:200`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '19' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                # Skip if it looks like a year, port, or HTTP status
                if re.match(r'(19|20)\d{2}|[1-9]\d{3,4}', number):
                    continue
```

---

### 336. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:238`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '15' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                        line=function_start,
                        severity=Severity.MEDIUM if complexity > 15 else Severity.LOW,
                        category=Category.QUALITY,
```

---

### 337. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:264`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '15' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
                line=function_start,
                severity=Severity.MEDIUM if complexity > 15 else Severity.LOW,
                category=Category.QUALITY,
```

---

### 338. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:49`
**Severity:** LOW
**Category:** quality

**Description:** Lowercase class name

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
            (r'\b[a-z]\b\s*=', "Single letter variable"),
            (r'def\s+[a-z]{1,2}\(', "Short function name"),
            (r'class\s+[a-z]', "Lowercase class name"),
        ]

```

---

### 339. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:77`
**Severity:** LOW
**Category:** quality

**Description:** Lowercase class name

**Recommendation:** Use descriptive, meaningful names

**Code:**
```

        self.ios_naming_patterns = [
            (r'class\s+[a-z]', "Swift class should start with uppercase"),
            (r'struct\s+[a-z]', "Swift struct should start with uppercase"),
            (r'enum\s+[a-z]', "Swift enum should start with uppercase"),
```

---

### 340. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:94`
**Severity:** LOW
**Category:** quality

**Description:** Function 'analyze_file' has complexity of 11

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 11
```

---

### 341. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/documentation_analyzer.py:163`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '200' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        # Find the next non-whitespace content after declaration
        remaining = content[after_pos:after_pos+200]  # Check next 200 chars

```

---

### 342. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/documentation_analyzer.py:163`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '200' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        # Find the next non-whitespace content after declaration
        remaining = content[after_pos:after_pos+200]  # Check next 200 chars

```

---

### 343. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/documentation_analyzer.py:277`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '15' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            # Check for too short docs
            if len(doc_text) < 15 and not doc_text.startswith('-'):
                code_snippet = self.get_lines_context(content, line_num, context_lines=1)
```

---

### 344. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/documentation_analyzer.py:295`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '30' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            if any(phrase in doc_text.lower() for phrase in generic_phrases):
                if len(doc_text) < 30:
                    code_snippet = self.get_lines_context(content, line_num, context_lines=1)
```

---

### 345. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/documentation_analyzer.py:120`
**Severity:** LOW
**Category:** quality

**Description:** Lowercase class name

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
        results = []

        # Find function/class definitions
        patterns = [
            (r'def\s+(\w+)\s*\(', 'function'),
```

---

### 346. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/documentation_analyzer.py:264`
**Severity:** LOW
**Category:** quality

**Description:** Function '_check_doc_quality_swift' has complexity of 12

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 12
```

---

### 347. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/smart_context.py:219`
**Severity:** LOW
**Category:** quality

**Description:** Function '_resolve_import' has complexity of 13

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 13
```

---

### 348. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:165`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '20' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            # God class indicators
            if method_count > 20 or line_count > 500:
                line_num = content[:class_start].count('\n') + 1
```

---

### 349. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:165`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '500' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            # God class indicators
            if method_count > 20 or line_count > 500:
                line_num = content[:class_start].count('\n') + 1
```

---

### 350. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:187`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '15' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
        # Too many imports is a sign of tight coupling
        if len(imports) > 15:
            result = AnalysisResult(
```

---

### 351. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:204`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '20' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```

        if len(matches) > 20:
            result = AnalysisResult(
```

---

### 352. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:367`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '300' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            # Massive VC indicators
            if line_count > 300 or method_count > 15:
                line_num = content[:vc_start].count('\n') + 1
```

---

### 353. 🟢 Magic Number

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:367`
**Severity:** LOW
**Category:** quality

**Description:** Magic number '15' should be a named constant

**Recommendation:** Define as a named constant with meaningful name

**Code:**
```
            # Massive VC indicators
            if line_count > 300 or method_count > 15:
                line_num = content[:vc_start].count('\n') + 1
```

---

### 354. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:148`
**Severity:** LOW
**Category:** quality

**Description:** Lowercase class name

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
            class_start = match.start()

            # Find class end (next class or end of file)
            next_class = None
            for other_match in matches:
```

---

### 355. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:148`
**Severity:** LOW
**Category:** quality

**Description:** Lowercase class name

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
            class_start = match.start()

            # Find class end (next class or end of file)
            next_class = None
            for other_match in matches:
```

---

### 356. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:164`
**Severity:** LOW
**Category:** quality

**Description:** Lowercase class name

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
            line_count = len(class_content.split('\n'))

            # God class indicators
            if method_count > 20 or line_count > 500:
                line_num = content[:class_start].count('\n') + 1
```

---

### 357. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:350`
**Severity:** LOW
**Category:** quality

**Description:** Lowercase class name

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
            vc_start = match.start()

            # Find class end (next class or end of file)
            next_class = None
            for other_match in matches:
```

---

### 358. 🟢 Poor Naming

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:350`
**Severity:** LOW
**Category:** quality

**Description:** Lowercase class name

**Recommendation:** Use descriptive, meaningful names

**Code:**
```
            vc_start = match.start()

            # Find class end (next class or end of file)
            next_class = None
            for other_match in matches:
```

---

### 359. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:136`
**Severity:** LOW
**Category:** quality

**Description:** Function '_check_god_class' has complexity of 12

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 12
```

---

### 360. 🟢 High Cyclomatic Complexity

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:338`
**Severity:** LOW
**Category:** quality

**Description:** Function '_check_massive_view_controller' has complexity of 12

**Recommendation:** Simplify function by extracting methods or reducing branching

**Code:**
```
Complexity: 12
```

---

### 361. 🟢 Tight Coupling

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:1`
**Severity:** LOW
**Category:** architecture

**Description:** Many direct object instantiations (22)

**Recommendation:** Consider dependency injection and programming to interfaces

---

### 362. 🟢 Tight Coupling

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repo.py:1`
**Severity:** LOW
**Category:** architecture

**Description:** Many direct object instantiations (66)

**Recommendation:** Consider dependency injection and programming to interfaces

---

### 363. 🟢 Tight Coupling

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_reasoning.py:1`
**Severity:** LOW
**Category:** architecture

**Description:** Many direct object instantiations (41)

**Recommendation:** Consider dependency injection and programming to interfaces

---

### 364. 🟢 Tight Coupling

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_wholefile.py:1`
**Severity:** LOW
**Category:** architecture

**Description:** Many direct object instantiations (31)

**Recommendation:** Consider dependency injection and programming to interfaces

---

### 365. 🟢 Tight Coupling

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:1`
**Severity:** LOW
**Category:** architecture

**Description:** Many direct object instantiations (48)

**Recommendation:** Consider dependency injection and programming to interfaces

---

### 366. 🟢 Tight Coupling

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:1`
**Severity:** LOW
**Category:** architecture

**Description:** Many direct object instantiations (34)

**Recommendation:** Consider dependency injection and programming to interfaces

---

### 367. 🟢 Tight Coupling

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/problem_stats.py:1`
**Severity:** LOW
**Category:** architecture

**Description:** Many direct object instantiations (21)

**Recommendation:** Consider dependency injection and programming to interfaces

---

### 368. 🟢 Tight Coupling

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1`
**Severity:** LOW
**Category:** architecture

**Description:** Many direct object instantiations (77)

**Recommendation:** Consider dependency injection and programming to interfaces

---

### 369. 🟢 Tight Coupling

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:1`
**Severity:** LOW
**Category:** architecture

**Description:** Many direct object instantiations (48)

**Recommendation:** Consider dependency injection and programming to interfaces

---

### 370. 🟢 Tight Coupling

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/udiff_coder.py:1`
**Severity:** LOW
**Category:** architecture

**Description:** Many direct object instantiations (32)

**Recommendation:** Consider dependency injection and programming to interfaces

---

### 371. 🟢 Hardcoded Dependency

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:64`
**Severity:** LOW
**Category:** architecture

**Description:** Hardcoded API URL

**Recommendation:** Use dependency injection or configuration files

**Code:**
```
# GitHub API configuration
GITHUB_API_URL = "https://api.github.com"
REPO_OWNER = "aider-AI"
```

---

### 372. 🟢 Tight Coupling

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1`
**Severity:** LOW
**Category:** architecture

**Description:** Many direct object instantiations (69)

**Recommendation:** Consider dependency injection and programming to interfaces

---

### 373. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/help_coder.py:12`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_edits' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    gpt_prompts = HelpPrompts()

    def get_edits(self, mode="update"):
        return []

```

---

### 374. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/help_coder.py:15`
**Severity:** LOW
**Category:** quality

**Description:** Function 'apply_edits' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return []

    def apply_edits(self, edits):
        pass

```

---

### 375. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/mdstream.py:56`
**Severity:** LOW
**Category:** quality

**Description:** Function '__rich_console__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    """A code block with syntax highlighting, no padding, and dark theme."""

    def __rich_console__(self, console, options):
        code = str(self.text).rstrip()
        # Force dark theme and transparent background to avoid blinding white blocks
```

---

### 376. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/mdstream.py:74`
**Severity:** LOW
**Category:** quality

**Description:** Function '__rich_console__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    """A heading class that renders left-justified."""

    def __rich_console__(self, console, options):
        text = self.text
        text.justify = "left"  # Override justification
```

---

### 377. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:18`
**Severity:** LOW
**Category:** quality

**Description:** Function 'color' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

    @property
    def color(self) -> str:
        model = self.name.lower()
        if "gemini" in model and "pro" in model:
```

---

### 378. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:41`
**Severity:** LOW
**Category:** quality

**Description:** Function 'legend_label' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

    @property
    def legend_label(self) -> str:
        model = self.name.lower()
        if "gemini" in model and "pro" in model:
```

---

### 379. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:69`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    LABEL_FONT_SIZE = 16

    def __init__(self):
        self.setup_plot_style()

```

---

### 380. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:72`
**Severity:** LOW
**Category:** quality

**Description:** Function 'setup_plot_style' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.setup_plot_style()

    def setup_plot_style(self):
        plt.rcParams["hatch.linewidth"] = 0.5
        plt.rcParams["hatch.color"] = "#444444"
```

---

### 381. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:78`
**Severity:** LOW
**Category:** quality

**Description:** Function 'load_data' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        plt.rcParams["text.color"] = "#444444"

    def load_data(self, yaml_file: str) -> List[ModelData]:
        with open(yaml_file, "r") as file:
            data = yaml.safe_load(file)
```

---

### 382. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:93`
**Severity:** LOW
**Category:** quality

**Description:** Function 'create_figure' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return models

    def create_figure(self) -> Tuple[plt.Figure, plt.Axes]:
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.grid(axis="y", zorder=0, lw=0.2)
```

---

### 383. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:101`
**Severity:** LOW
**Category:** quality

**Description:** Function 'plot_model_series' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return fig, ax

    def plot_model_series(self, ax: plt.Axes, models: List[ModelData]):
        # Group models by color
        color_groups: Dict[str, List[ModelData]] = {}
```

---

### 384. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:133`
**Severity:** LOW
**Category:** quality

**Description:** Function 'set_labels_and_style' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            )

    def set_labels_and_style(self, ax: plt.Axes):
        ax.set_xlabel("Model release date", fontsize=18, color="#555")
        ax.set_ylabel(
```

---

### 385. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:143`
**Severity:** LOW
**Category:** quality

**Description:** Function 'save_and_display' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        plt.tight_layout(pad=1.0)

    def save_and_display(self, fig: plt.Figure):
        plt.savefig("aider/website/assets/models-over-time.png")
        plt.savefig("aider/website/assets/models-over-time.svg")
```

---

### 386. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:148`
**Severity:** LOW
**Category:** quality

**Description:** Function 'plot' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        imgcat(fig)

    def plot(self, yaml_file: str):
        models = self.load_data(yaml_file)
        fig, ax = self.create_figure()
```

---

### 387. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:156`
**Severity:** LOW
**Category:** quality

**Description:** Function 'main' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def main():
    plotter = BenchmarkPlotter()
    models = plotter.load_data("aider/website/_data/edit_leaderboard.yml")
```

---

### 388. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:1`
**Severity:** LOW
**Category:** quality

**Description:** Class 'from' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```
from dataclasses import dataclass
from datetime import date
from typing import Dict, List, Tuple
```

---

### 389. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:11`
**Severity:** LOW
**Category:** quality

**Description:** Class 'class' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


@dataclass
class ModelData:
    name: str
```

---

### 390. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/over_time.py:66`
**Severity:** LOW
**Category:** quality

**Description:** Class 'BenchmarkPlotter' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class BenchmarkPlotter:
    LABEL_FONT_SIZE = 16

```

---

### 391. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_scripting.py:12`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_basic_scripting' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
class TestScriptingAPI(unittest.TestCase):
    @patch("aider.coders.base_coder.Coder.send")
    def test_basic_scripting(self, mock_send):
        with GitTemporaryDirectory():
            # Setup
```

---

### 392. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_scripting.py:15`
**Severity:** LOW
**Category:** quality

**Description:** Function 'mock_send_side_effect' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        with GitTemporaryDirectory():
            # Setup
            def mock_send_side_effect(messages, functions=None):
                coder.partial_response_content = "Changes applied successfully."
                coder.partial_response_function_call = None
```

---

### 393. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_scripting.py:10`
**Severity:** LOW
**Category:** quality

**Description:** Class 'TestScriptingAPI' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class TestScriptingAPI(unittest.TestCase):
    @patch("aider.coders.base_coder.Coder.send")
    def test_basic_scripting(self, mock_send):
```

---

### 394. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/copypaste.py:10`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    """Watches clipboard for changes and updates IO placeholder"""

    def __init__(self, io, verbose=False):
        self.io = io
        self.verbose = verbose
```

---

### 395. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/copypaste.py:23`
**Severity:** LOW
**Category:** quality

**Description:** Function 'watch_clipboard' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.last_clipboard = pyperclip.paste()

        def watch_clipboard():
            while not self.stop_event.is_set():
                try:
```

---

### 396. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:18`
**Severity:** LOW
**Category:** quality

**Description:** Function 'setUp' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

class TestRepoMap(unittest.TestCase):
    def setUp(self):
        self.GPT35 = Model("gpt-3.5-turbo")

```

---

### 397. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:21`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_get_repo_map' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.GPT35 = Model("gpt-3.5-turbo")

    def test_get_repo_map(self):
        # Create a temporary directory with sample files for testing
        test_files = [
```

---

### 398. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:49`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_repo_map_refresh_files' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            del repo_map

    def test_repo_map_refresh_files(self):
        with GitTemporaryDirectory() as temp_dir:
            repo = git.Repo(temp_dir)
```

---

### 399. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:54`
**Severity:** LOW
**Category:** quality

**Description:** Function 'function1' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

            # Create three source files with one function each
            file1_content = "def function1():\n    return 'Hello from file1'\n"
            file2_content = "def function2():\n    return 'Hello from file2'\n"
            file3_content = "def function3():\n    return 'Hello from file3'\n"
```

---

### 400. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:55`
**Severity:** LOW
**Category:** quality

**Description:** Function 'function2' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            # Create three source files with one function each
            file1_content = "def function1():\n    return 'Hello from file1'\n"
            file2_content = "def function2():\n    return 'Hello from file2'\n"
            file3_content = "def function3():\n    return 'Hello from file3'\n"

```

---

### 401. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:56`
**Severity:** LOW
**Category:** quality

**Description:** Function 'function3' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            file1_content = "def function1():\n    return 'Hello from file1'\n"
            file2_content = "def function2():\n    return 'Hello from file2'\n"
            file3_content = "def function3():\n    return 'Hello from file3'\n"

            with open(os.path.join(temp_dir, "file1.py"), "w") as f:
```

---

### 402. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:87`
**Severity:** LOW
**Category:** quality

**Description:** Function 'functionNEW' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            # Add a new function to file1.py
            with open(os.path.join(temp_dir, "file1.py"), "a") as f:
                f.write("\ndef functionNEW():\n    return 'Hello NEW'\n")

            # Get another repo map
```

---

### 403. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:106`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_repo_map_refresh_auto' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            del repo

    def test_repo_map_refresh_auto(self):
        with GitTemporaryDirectory() as temp_dir:
            repo = git.Repo(temp_dir)
```

---

### 404. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:111`
**Severity:** LOW
**Category:** quality

**Description:** Function 'function1' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

            # Create two source files with one function each
            file1_content = "def function1():\n    return 'Hello from file1'\n"
            file2_content = "def function2():\n    return 'Hello from file2'\n"

```

---

### 405. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:112`
**Severity:** LOW
**Category:** quality

**Description:** Function 'function2' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            # Create two source files with one function each
            file1_content = "def function1():\n    return 'Hello from file1'\n"
            file2_content = "def function2():\n    return 'Hello from file2'\n"

            with open(os.path.join(temp_dir, "file1.py"), "w") as f:
```

---

### 406. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:132`
**Severity:** LOW
**Category:** quality

**Description:** Function 'slow_get_ranked_tags' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            original_get_ranked_tags = repo_map.get_ranked_tags

            def slow_get_ranked_tags(*args, **kwargs):
                time.sleep(1.1)  # Sleep for 1.1 seconds to ensure it's over 1 second
                return original_get_ranked_tags(*args, **kwargs)
```

---

### 407. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:146`
**Severity:** LOW
**Category:** quality

**Description:** Function 'functionNEW' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            # Add a new function to file1.py
            with open(os.path.join(temp_dir, "file1.py"), "a") as f:
                f.write("\ndef functionNEW():\n    return 'Hello NEW'\n")

            # Get another repo map without force_refresh
```

---

### 408. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:216`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_get_repo_map_all_files' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            del repo_map

    def test_get_repo_map_all_files(self):
        test_files = [
            "test_file0.py",
```

---

### 409. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:246`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_get_repo_map_excludes_added_files' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            del repo_map

    def test_get_repo_map_excludes_added_files(self):
        # Create a temporary directory with sample files for testing
        test_files = [
```

---

### 410. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:258`
**Severity:** LOW
**Category:** quality

**Description:** Function 'foo' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            for file in test_files:
                with open(os.path.join(temp_dir, file), "w") as f:
                    f.write("def foo(): pass\n")

            io = InputOutput()
```

---

### 411. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:278`
**Severity:** LOW
**Category:** quality

**Description:** Function 'setUp' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

class TestRepoMapTypescript(unittest.TestCase):
    def setUp(self):
        self.GPT35 = Model("gpt-3.5-turbo")

```

---

### 412. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:283`
**Severity:** LOW
**Category:** quality

**Description:** Function 'setUp' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

class TestRepoMapAllLanguages(unittest.TestCase):
    def setUp(self):
        self.GPT35 = Model("gpt-3.5-turbo")
        self.fixtures_dir = Path(__file__).parent.parent / "fixtures" / "languages"
```

---

### 413. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:287`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_c' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.fixtures_dir = Path(__file__).parent.parent / "fixtures" / "languages"

    def test_language_c(self):
        self._test_language_repo_map("c", "c", "main")

```

---

### 414. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:290`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_cpp' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("c", "c", "main")

    def test_language_cpp(self):
        self._test_language_repo_map("cpp", "cpp", "main")

```

---

### 415. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:293`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_d' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("cpp", "cpp", "main")

    def test_language_d(self):
        self._test_language_repo_map("d", "d", "main")

```

---

### 416. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:296`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_dart' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("d", "d", "main")

    def test_language_dart(self):
        self._test_language_repo_map("dart", "dart", "Person")

```

---

### 417. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:299`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_elixir' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("dart", "dart", "Person")

    def test_language_elixir(self):
        self._test_language_repo_map("elixir", "ex", "Greeter")

```

---

### 418. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:302`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_gleam' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("elixir", "ex", "Greeter")

    def test_language_gleam(self):
        self._test_language_repo_map("gleam", "gleam", "greet")

```

---

### 419. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:305`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_haskell' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("gleam", "gleam", "greet")

    def test_language_haskell(self):
        self._test_language_repo_map("haskell", "hs", "add")

```

---

### 420. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:308`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_java' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("haskell", "hs", "add")

    def test_language_java(self):
        self._test_language_repo_map("java", "java", "Greeting")

```

---

### 421. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:311`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_javascript' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("java", "java", "Greeting")

    def test_language_javascript(self):
        self._test_language_repo_map("javascript", "js", "Person")

```

---

### 422. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:314`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_kotlin' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("javascript", "js", "Person")

    def test_language_kotlin(self):
        self._test_language_repo_map("kotlin", "kt", "Greeting")

```

---

### 423. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:317`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_lua' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("kotlin", "kt", "Greeting")

    def test_language_lua(self):
        self._test_language_repo_map("lua", "lua", "greet")

```

---

### 424. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:320`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_php' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("lua", "lua", "greet")

    def test_language_php(self):
        self._test_language_repo_map("php", "php", "greet")

```

---

### 425. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:323`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_python' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("php", "php", "greet")

    def test_language_python(self):
        self._test_language_repo_map("python", "py", "Person")

```

---

### 426. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:328`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_ruby' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    # "ql": ("ql", "greet"), # not supported in tsl-pack (yet?)

    def test_language_ruby(self):
        self._test_language_repo_map("ruby", "rb", "greet")

```

---

### 427. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:331`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_rust' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("ruby", "rb", "greet")

    def test_language_rust(self):
        self._test_language_repo_map("rust", "rs", "Person")

```

---

### 428. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:334`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_typescript' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("rust", "rs", "Person")

    def test_language_typescript(self):
        self._test_language_repo_map("typescript", "ts", "greet")

```

---

### 429. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:337`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_tsx' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("typescript", "ts", "greet")

    def test_language_tsx(self):
        self._test_language_repo_map("tsx", "tsx", "UserProps")

```

---

### 430. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:340`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_zig' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("tsx", "tsx", "UserProps")

    def test_language_zig(self):
        self._test_language_repo_map("zig", "zig", "add")

```

---

### 431. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:343`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_csharp' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("zig", "zig", "add")

    def test_language_csharp(self):
        self._test_language_repo_map("csharp", "cs", "IGreeter")

```

---

### 432. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:346`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_elisp' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("csharp", "cs", "IGreeter")

    def test_language_elisp(self):
        self._test_language_repo_map("elisp", "el", "greeter")

```

---

### 433. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:349`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_elm' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("elisp", "el", "greeter")

    def test_language_elm(self):
        self._test_language_repo_map("elm", "elm", "Person")

```

---

### 434. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:352`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_go' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("elm", "elm", "Person")

    def test_language_go(self):
        self._test_language_repo_map("go", "go", "Greeter")

```

---

### 435. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:355`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_hcl' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("go", "go", "Greeter")

    def test_language_hcl(self):
        self._test_language_repo_map("hcl", "tf", "aws_vpc")

```

---

### 436. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:358`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_arduino' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("hcl", "tf", "aws_vpc")

    def test_language_arduino(self):
        self._test_language_repo_map("arduino", "ino", "setup")

```

---

### 437. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:361`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_chatito' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("arduino", "ino", "setup")

    def test_language_chatito(self):
        self._test_language_repo_map("chatito", "chatito", "intent")

```

---

### 438. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:364`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_clojure' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("chatito", "chatito", "intent")

    def test_language_clojure(self):
        self._test_language_repo_map("clojure", "clj", "greet")

```

---

### 439. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:367`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_commonlisp' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("clojure", "clj", "greet")

    def test_language_commonlisp(self):
        self._test_language_repo_map("commonlisp", "lisp", "greet")

```

---

### 440. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:370`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_pony' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("commonlisp", "lisp", "greet")

    def test_language_pony(self):
        self._test_language_repo_map("pony", "pony", "Greeter")

```

---

### 441. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:373`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_properties' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("pony", "pony", "Greeter")

    def test_language_properties(self):
        self._test_language_repo_map("properties", "properties", "database.url")

```

---

### 442. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:376`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_r' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("properties", "properties", "database.url")

    def test_language_r(self):
        self._test_language_repo_map("r", "r", "calculate")

```

---

### 443. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:379`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_racket' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("r", "r", "calculate")

    def test_language_racket(self):
        self._test_language_repo_map("racket", "rkt", "greet")

```

---

### 444. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:382`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_solidity' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("racket", "rkt", "greet")

    def test_language_solidity(self):
        self._test_language_repo_map("solidity", "sol", "SimpleStorage")

```

---

### 445. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:385`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_swift' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("solidity", "sol", "SimpleStorage")

    def test_language_swift(self):
        self._test_language_repo_map("swift", "swift", "Greeter")

```

---

### 446. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:388`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_udev' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("swift", "swift", "Greeter")

    def test_language_udev(self):
        self._test_language_repo_map("udev", "rules", "USB_DRIVER")

```

---

### 447. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:391`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_scala' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("udev", "rules", "USB_DRIVER")

    def test_language_scala(self):
        self._test_language_repo_map("scala", "scala", "Greeter")

```

---

### 448. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:394`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_ocaml' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("scala", "scala", "Greeter")

    def test_language_ocaml(self):
        self._test_language_repo_map("ocaml", "ml", "Greeter")

```

---

### 449. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:397`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_language_ocaml_interface' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._test_language_repo_map("ocaml", "ml", "Greeter")

    def test_language_ocaml_interface(self):
        self._test_language_repo_map("ocaml_interface", "mli", "Greeter")

```

---

### 450. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:442`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_repo_map_sample_code_base' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            del repo_map

    def test_repo_map_sample_code_base(self):
        # Path to the sample code base
        sample_code_base = Path(__file__).parent.parent / "fixtures" / "sample-code-base"
```

---

### 451. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:17`
**Severity:** LOW
**Category:** quality

**Description:** Class 'TestRepoMap' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class TestRepoMap(unittest.TestCase):
    def setUp(self):
        self.GPT35 = Model("gpt-3.5-turbo")
```

---

### 452. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:277`
**Severity:** LOW
**Category:** quality

**Description:** Class 'TestRepoMapTypescript' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class TestRepoMapTypescript(unittest.TestCase):
    def setUp(self):
        self.GPT35 = Model("gpt-3.5-turbo")
```

---

### 453. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repomap.py:282`
**Severity:** LOW
**Category:** quality

**Description:** Class 'TestRepoMapAllLanguages' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class TestRepoMapAllLanguages(unittest.TestCase):
    def setUp(self):
        self.GPT35 = Model("gpt-3.5-turbo")
```

---

### 454. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_sendchat.py:14`
**Severity:** LOW
**Category:** quality

**Description:** Function 'setUp' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

class TestSendChat(unittest.TestCase):
    def setUp(self):
        self.mock_messages = [{"role": "user", "content": "Hello"}]
        self.mock_model = "gpt-4"
```

---

### 455. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_sendchat.py:18`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_litellm_exceptions' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.mock_model = "gpt-4"

    def test_litellm_exceptions(self):
        litellm_ex = LiteLLMExceptions()
        litellm_ex._load(strict=True)
```

---

### 456. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_sendchat.py:24`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_simple_send_with_retries_rate_limit_error' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    @patch("litellm.completion")
    @patch("builtins.print")
    def test_simple_send_with_retries_rate_limit_error(self, mock_print, mock_completion):
        mock = MagicMock()
        mock.status_code = 500
```

---

### 457. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_sendchat.py:44`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_send_completion_basic' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

    @patch("litellm.completion")
    def test_send_completion_basic(self, mock_completion):
        # Setup mock response
        mock_response = MagicMock()
```

---

### 458. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_sendchat.py:58`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_send_completion_with_functions' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

    @patch("litellm.completion")
    def test_send_completion_with_functions(self, mock_completion):
        mock_function = {"name": "test_function", "parameters": {"type": "object"}}

```

---

### 459. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_sendchat.py:71`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_simple_send_attribute_error' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

    @patch("litellm.completion")
    def test_simple_send_attribute_error(self, mock_completion):
        # Setup mock to raise AttributeError
        mock_completion.return_value = MagicMock()
```

---

### 460. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_sendchat.py:82`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_simple_send_non_retryable_error' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    @patch("litellm.completion")
    @patch("builtins.print")
    def test_simple_send_non_retryable_error(self, mock_print, mock_completion):
        # Test with an error that shouldn't trigger retries
        mock = MagicMock()
```

---

### 461. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_sendchat.py:96`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_ensure_alternating_roles_empty' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        assert mock_print.call_count == 1

    def test_ensure_alternating_roles_empty(self):
        from flacoai.sendchat import ensure_alternating_roles

```

---

### 462. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_sendchat.py:103`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_ensure_alternating_roles_single_message' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        assert result == []

    def test_ensure_alternating_roles_single_message(self):
        from flacoai.sendchat import ensure_alternating_roles

```

---

### 463. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_sendchat.py:110`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_ensure_alternating_roles_already_alternating' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        assert result == messages

    def test_ensure_alternating_roles_already_alternating(self):
        from flacoai.sendchat import ensure_alternating_roles

```

---

### 464. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_sendchat.py:121`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_ensure_alternating_roles_consecutive_user' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        assert result == messages

    def test_ensure_alternating_roles_consecutive_user(self):
        from flacoai.sendchat import ensure_alternating_roles

```

---

### 465. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_sendchat.py:136`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_ensure_alternating_roles_consecutive_assistant' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        assert result == expected

    def test_ensure_alternating_roles_consecutive_assistant(self):
        from flacoai.sendchat import ensure_alternating_roles

```

---

### 466. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_sendchat.py:151`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_ensure_alternating_roles_mixed_sequence' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        assert result == expected

    def test_ensure_alternating_roles_mixed_sequence(self):
        from flacoai.sendchat import ensure_alternating_roles

```

---

### 467. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_sendchat.py:9`
**Severity:** LOW
**Category:** quality

**Description:** Class 'PrintCalled' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class PrintCalled(Exception):
    pass

```

---

### 468. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_sendchat.py:13`
**Severity:** LOW
**Category:** quality

**Description:** Class 'TestSendChat' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class TestSendChat(unittest.TestCase):
    def setUp(self):
        self.mock_messages = [{"role": "user", "content": "Hello"}]
```

---

### 469. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repo.py:19`
**Severity:** LOW
**Category:** quality

**Description:** Function 'setUp' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

class TestRepo(unittest.TestCase):
    def setUp(self):
        self.GPT35 = Model("gpt-3.5-turbo")

```

---

### 470. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repo.py:22`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_diffs_empty_repo' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.GPT35 = Model("gpt-3.5-turbo")

    def test_diffs_empty_repo(self):
        with GitTemporaryDirectory():
            repo = git.Repo()
```

---

### 471. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repo.py:39`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_diffs_nonempty_repo' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.assertIn("workingdir", diffs)

    def test_diffs_nonempty_repo(self):
        with GitTemporaryDirectory():
            repo = git.Repo()
```

---

### 472. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repo.py:62`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_diffs_with_single_byte_encoding' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.assertIn("workingdir", diffs)

    def test_diffs_with_single_byte_encoding(self):
        with GitTemporaryDirectory():
            encoding = "cp1251"
```

---

### 473. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repo.py:84`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_diffs_detached_head' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.assertIn("АБВ", diffs)

    def test_diffs_detached_head(self):
        with GitTemporaryDirectory():
            repo = git.Repo()
```

---

### 474. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repo.py:114`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_diffs_between_commits' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.assertIn("workingdir", diffs)

    def test_diffs_between_commits(self):
        with GitTemporaryDirectory():
            repo = git.Repo()
```

---

### 475. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repo.py:132`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_get_commit_message' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

    @patch("aider.models.Model.simple_send_with_retries")
    def test_get_commit_message(self, mock_send):
        mock_send.side_effect = ["", "a good commit message"]

```

---

### 476. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repo.py:156`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_get_commit_message_strip_quotes' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

    @patch("aider.models.Model.simple_send_with_retries")
    def test_get_commit_message_strip_quotes(self, mock_send):
        mock_send.return_value = '"a good commit message"'

```

---

### 477. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repo.py:167`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_get_commit_message_no_strip_unmatched_quotes' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

    @patch("aider.models.Model.simple_send_with_retries")
    def test_get_commit_message_no_strip_unmatched_quotes(self, mock_send):
        mock_send.return_value = 'a good "commit message"'

```

---

### 478. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repo.py:178`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_get_commit_message_with_custom_prompt' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

    @patch("aider.models.Model.simple_send_with_retries")
    def test_get_commit_message_with_custom_prompt(self, mock_send):
        mock_send.return_value = "Custom commit message"
        custom_prompt = "Generate a commit message in the style of Shakespeare"
```

---

### 479. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repo.py:192`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_commit_with_custom_committer_name' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    @unittest.skipIf(platform.system() == "Windows", "Git env var behavior differs on Windows")
    @patch("aider.repo.GitRepo.get_commit_message")
    def test_commit_with_custom_committer_name(self, mock_send):
        mock_send.return_value = '"a good commit message"'

```

---

### 480. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repo.py:267`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_commit_with_co_authored_by' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

    @unittest.skipIf(platform.system() == "Windows", "Git env var behavior differs on Windows")
    def test_commit_with_co_authored_by(self):
        with GitTemporaryDirectory():
            # new repo
```

---

### 481. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repo.py:318`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_commit_co_authored_by_with_explicit_name_modification' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

    @unittest.skipIf(platform.system() == "Windows", "Git env var behavior differs on Windows")
    def test_commit_co_authored_by_with_explicit_name_modification(self):
        # Test scenario where Co-authored-by is true AND
        # author/committer modification are explicitly True
```

---

### 482. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repo.py:375`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_commit_ai_edits_no_coauthor_explicit_false' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

    @unittest.skipIf(platform.system() == "Windows", "Git env var behavior differs on Windows")
    def test_commit_ai_edits_no_coauthor_explicit_false(self):
        # Test AI edits (flacoai_edits=True) when co-authored-by is False,
        # but author or committer attribution is explicitly disabled.
```

---

### 483. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repo.py:446`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_get_tracked_files' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            )

    def test_get_tracked_files(self):
        # Create a temporary directory
        tempdir = Path(tempfile.mkdtemp())
```

---

### 484. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repo.py:482`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_get_tracked_files_with_new_staged_file' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.assertEqual(set(tracked_files), set(created_files))

    def test_get_tracked_files_with_new_staged_file(self):
        with GitTemporaryDirectory():
            # new repo
```

---

### 485. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repo.py:513`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_get_tracked_files_with_flacoaiignore' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.assertIn(str(fname2), fnames)

    def test_get_tracked_files_with_flacoaiignore(self):
        with GitTemporaryDirectory():
            # new repo
```

---

### 486. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repo.py:563`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_get_tracked_files_from_subdir' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            # self.assertNotIn(str(fname2), fnames)

    def test_get_tracked_files_from_subdir(self):
        with GitTemporaryDirectory():
            # new repo
```

---

### 487. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repo.py:587`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_subtree_only' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.assertIn(str(fname), fnames)

    def test_subtree_only(self):
        with GitTemporaryDirectory():
            # Create a new repo
```

---

### 488. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repo.py:624`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_noop_commit' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

    @patch("aider.models.Model.simple_send_with_retries")
    def test_noop_commit(self, mock_send):
        mock_send.return_value = '"a good commit message"'

```

---

### 489. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_repo.py:18`
**Severity:** LOW
**Category:** quality

**Description:** Class 'TestRepo' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class TestRepo(unittest.TestCase):
    def setUp(self):
        self.GPT35 = Model("gpt-3.5-turbo")
```

---

### 490. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_analytics.py:13`
**Severity:** LOW
**Category:** quality

**Description:** Function 'temp_analytics_file' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

@pytest.fixture
def temp_analytics_file():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        yield f.name
```

---

### 491. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_analytics.py:20`
**Severity:** LOW
**Category:** quality

**Description:** Function 'temp_data_dir' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

@pytest.fixture
def temp_data_dir(monkeypatch):
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_dir = Path(tmpdir)
```

---

### 492. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_analytics.py:27`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_analytics_initialization' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def test_analytics_initialization(temp_data_dir):
    analytics = Analytics(permanently_disable=True)
    assert analytics.mp is None
```

---

### 493. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_analytics.py:35`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_analytics_enable_disable' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def test_analytics_enable_disable(temp_data_dir):
    analytics = Analytics()
    analytics.asked_opt_in = True
```

---

### 494. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_analytics.py:52`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_analytics_data_persistence' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def test_analytics_data_persistence(temp_data_dir):
    analytics1 = Analytics()
    user_id = analytics1.user_id
```

---

### 495. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_analytics.py:60`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_analytics_event_logging' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def test_analytics_event_logging(temp_analytics_file, temp_data_dir):
    analytics = Analytics(logfile=temp_analytics_file)
    analytics.asked_opt_in = True
```

---

### 496. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_analytics.py:82`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_system_info' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def test_system_info(temp_data_dir):
    analytics = Analytics()
    sys_info = analytics.get_system_info()
```

---

### 497. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_analytics.py:92`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_need_to_ask' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def test_need_to_ask(temp_data_dir):
    analytics = Analytics()
    assert analytics.need_to_ask(True) is True
```

---

### 498. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_analytics.py:107`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_is_uuid_in_percentage' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def test_is_uuid_in_percentage():
    from flacoai.analytics import is_uuid_in_percentage

```

---

### 499. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/security_analyzer.py:11`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    """Analyzes code for security vulnerabilities based on OWASP Top 10."""

    def __init__(self, io=None, verbose=False):
        super().__init__(io, verbose)

```

---

### 500. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/llm.py:24`
**Severity:** LOW
**Category:** quality

**Description:** Function '__getattr__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    _lazy_module = None

    def __getattr__(self, name):
        if name == "_lazy_module":
            return super()
```

---

### 501. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/llm.py:21`
**Severity:** LOW
**Category:** quality

**Description:** Class 'LazyLiteLLM' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class LazyLiteLLM:
    _lazy_module = None

```

---

### 502. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_prompts.py:1`
**Severity:** LOW
**Category:** quality

**Description:** Class 'CoderPrompts' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```
class CoderPrompts:
    system_reminder = ""

```

---

### 503. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/integrations/jira_client.py:56`
**Severity:** LOW
**Category:** quality

**Description:** Function 'create_issue' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            return None

    def create_issue(
        self,
        project: str,
```

---

### 504. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:153`
**Severity:** LOW
**Category:** quality

**Description:** Function 'find_available_port' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

# Helper function to find an available port
def find_available_port(start_port=8484, end_port=8584):
    for port in range(start_port, end_port + 1):
        try:
```

---

### 505. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:166`
**Severity:** LOW
**Category:** quality

**Description:** Function 'generate_pkce_codes' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

# PKCE code generation
def generate_pkce_codes():
    code_verifier = secrets.token_urlsafe(64)
    hasher = hashlib.sha256()
```

---

### 506. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:175`
**Severity:** LOW
**Category:** quality

**Description:** Function 'exchange_code_for_key' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

# Function to exchange the authorization code for an API key
def exchange_code_for_key(code, code_verifier, io):
    try:
        response = requests.post(
```

---

### 507. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:230`
**Severity:** LOW
**Category:** quality

**Description:** Function 'do_GET' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

    class OAuthCallbackHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            nonlocal auth_code, server_error
            parsed_path = urlparse(self.path)
```

---

### 508. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:262`
**Severity:** LOW
**Category:** quality

**Description:** Function 'log_message' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
                self.wfile.write(b"Not Found")

        def log_message(self, format, *args):
            # Suppress server logging to keep terminal clean
            pass
```

---

### 509. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:266`
**Severity:** LOW
**Category:** quality

**Description:** Function 'run_server' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            pass

    def run_server():
        nonlocal server_error
        try:
```

---

### 510. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/onboarding.py:229`
**Severity:** LOW
**Category:** quality

**Description:** Class 'OAuthCallbackHandler' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```
    shutdown_server = threading.Event()

    class OAuthCallbackHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            nonlocal auth_code, server_error
```

---

### 511. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_reasoning.py:32`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        # Mock completion response with reasoning content
        class MockCompletion:
            def __init__(self, content, reasoning_content):
                self.content = content
                # Add required attributes expected by show_send_output
```

---

### 512. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_reasoning.py:93`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        # Mock streaming response chunks
        class MockStreamingChunk:
            def __init__(
                self, content=None, reasoning_content=None, reasoning=None, finish_reason=None
            ):
```

---

### 513. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_reasoning.py:214`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        # Mock completion response with think tags in content
        class MockCompletion:
            def __init__(self, content):
                self.content = content
                # Add required attributes expected by show_send_output
```

---

### 514. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_reasoning.py:276`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        # Mock streaming response chunks
        class MockStreamingChunk:
            def __init__(
                self, content=None, reasoning_content=None, reasoning=None, finish_reason=None
            ):
```

---

### 515. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_reasoning.py:419`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        # Mock completion response with reasoning content
        class MockCompletion:
            def __init__(self, content, reasoning):
                self.content = content
                # Add required attributes expected by show_send_output
```

---

### 516. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_reasoning.py:484`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        # Mock streaming response chunks
        class MockStreamingChunk:
            def __init__(
                self, content=None, reasoning_content=None, reasoning=None, finish_reason=None
            ):
```

---

### 517. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_reasoning.py:31`
**Severity:** LOW
**Category:** quality

**Description:** Class 'MockCompletion' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```

        # Mock completion response with reasoning content
        class MockCompletion:
            def __init__(self, content, reasoning_content):
                self.content = content
```

---

### 518. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_reasoning.py:92`
**Severity:** LOW
**Category:** quality

**Description:** Class 'MockStreamingChunk' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```

        # Mock streaming response chunks
        class MockStreamingChunk:
            def __init__(
                self, content=None, reasoning_content=None, reasoning=None, finish_reason=None
```

---

### 519. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_reasoning.py:213`
**Severity:** LOW
**Category:** quality

**Description:** Class 'MockCompletion' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```

        # Mock completion response with think tags in content
        class MockCompletion:
            def __init__(self, content):
                self.content = content
```

---

### 520. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_reasoning.py:275`
**Severity:** LOW
**Category:** quality

**Description:** Class 'MockStreamingChunk' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```

        # Mock streaming response chunks
        class MockStreamingChunk:
            def __init__(
                self, content=None, reasoning_content=None, reasoning=None, finish_reason=None
```

---

### 521. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_reasoning.py:418`
**Severity:** LOW
**Category:** quality

**Description:** Class 'MockCompletion' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```

        # Mock completion response with reasoning content
        class MockCompletion:
            def __init__(self, content, reasoning):
                self.content = content
```

---

### 522. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_reasoning.py:483`
**Severity:** LOW
**Category:** quality

**Description:** Class 'MockStreamingChunk' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```

        # Mock streaming response chunks
        class MockStreamingChunk:
            def __init__(
                self, content=None, reasoning_content=None, reasoning=None, finish_reason=None
```

---

### 523. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/special.py:184`
**Severity:** LOW
**Category:** quality

**Description:** Function 'is_important' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def is_important(file_path):
    file_name = os.path.basename(file_path)
    dir_name = os.path.normpath(os.path.dirname(file_path))
```

---

### 524. 🟢 Incomplete TODO Comment

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/screenshot_prompts.py:163`
**Severity:** LOW
**Category:** quality

**Description:** TODO comment lacks detailed description

**Recommendation:** Add description explaining what needs to be done and why

**Code:**
```
        isLoading = true
        // TODO: Implement login logic
        DispatchQueue.main.asyncAfter(deadline: .now() + 1) {
```

---

### 525. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_wholefile.py:16`
**Severity:** LOW
**Category:** quality

**Description:** Function 'setUp' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

class TestWholeFileCoder(unittest.TestCase):
    def setUp(self):
        self.original_cwd = os.getcwd()
        self.tempdir = tempfile.mkdtemp()
```

---

### 526. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_wholefile.py:23`
**Severity:** LOW
**Category:** quality

**Description:** Function 'tearDown' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.GPT35 = Model("gpt-3.5-turbo")

    def tearDown(self):
        os.chdir(self.original_cwd)
        shutil.rmtree(self.tempdir, ignore_errors=True)
```

---

### 527. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_wholefile.py:27`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_no_files' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        shutil.rmtree(self.tempdir, ignore_errors=True)

    def test_no_files(self):
        # Initialize WholeFileCoder with the temporary directory
        io = InputOutput(yes=True)
```

---

### 528. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_wholefile.py:41`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_no_files_new_file_should_ask' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        coder.render_incremental_response(True)

    def test_no_files_new_file_should_ask(self):
        io = InputOutput(yes=False)  # <- yes=FALSE
        coder = WholeFileCoder(main_model=self.GPT35, io=io, fnames=[])
```

---

### 529. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_wholefile.py:52`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_update_files' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.assertFalse(Path("foo.js").exists())

    def test_update_files(self):
        # Create a sample file in the temporary directory
        sample_file = "sample.txt"
```

---

### 530. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_wholefile.py:76`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_update_files_live_diff' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.assertEqual(updated_content, "Updated content\n")

    def test_update_files_live_diff(self):
        # Create a sample file in the temporary directory
        sample_file = "sample.txt"
```

---

### 531. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_wholefile.py:130`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_update_files_bogus_path_prefix' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.assertEqual(updated_content, "Updated content\n")

    def test_update_files_bogus_path_prefix(self):
        # Create a sample file in the temporary directory
        sample_file = "sample.txt"
```

---

### 532. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_wholefile.py:155`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_update_files_not_in_chat' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.assertEqual(updated_content, "Updated content\n")

    def test_update_files_not_in_chat(self):
        # Create a sample file in the temporary directory
        sample_file = "sample.txt"
```

---

### 533. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_wholefile.py:179`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_update_files_no_filename_single_file_in_chat' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.assertEqual(updated_content, "Updated content\n")

    def test_update_files_no_filename_single_file_in_chat(self):
        sample_file = "accumulate.py"
        content = (
```

---

### 534. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_wholefile.py:182`
**Severity:** LOW
**Category:** quality

**Description:** Function 'accumulate' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        sample_file = "accumulate.py"
        content = (
            "def accumulate(collection, operation):\n    return [operation(x) for x in"
            " collection]\n"
        )
```

---

### 535. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_wholefile.py:287`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_update_named_file_but_extra_unnamed_code_block' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.assertEqual(fname_b.read_text(), "after b\n")

    def test_update_named_file_but_extra_unnamed_code_block(self):
        sample_file = "hello.py"
        new_content = "new\ncontent\ngoes\nhere\n"
```

---

### 536. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_wholefile.py:319`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_full_edit' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.assertEqual(updated_content, new_content)

    def test_full_edit(self):
        # Create a few temporary files
        _, file1 = tempfile.mkstemp()
```

---

### 537. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_wholefile.py:15`
**Severity:** LOW
**Category:** quality

**Description:** Class 'TestWholeFileCoder' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class TestWholeFileCoder(unittest.TestCase):
    def setUp(self):
        self.original_cwd = os.getcwd()
```

---

### 538. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:61`
**Severity:** LOW
**Category:** quality

**Description:** Function 'wrapper' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        orig_multiline = self.multiline_mode
        self.multiline_mode = False
```

---

### 539. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:86`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    show_group: bool = True

    def __init__(self, items=None):
        if items is not None:
            self.show_group = len(items) > 1
```

---

### 540. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:92`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

class AutoCompleter(Completer):
    def __init__(
        self, root, rel_fnames, addable_rel_fnames, commands, encoding, abs_read_only_fnames=None
    ):
```

---

### 541. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:127`
**Severity:** LOW
**Category:** quality

**Description:** Function 'tokenize' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.tokenized = False

    def tokenize(self):
        if self.tokenized:
            return
```

---

### 542. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:148`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_command_completions' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            )

    def get_command_completions(self, document, complete_event, text, words):
        if len(words) == 1 and not text[-1].isspace():
            partial = words[0].lower()
```

---

### 543. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:186`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_completions' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            yield Completion(candidate, start_position=-len(words[-1]))

    def get_completions(self, document, complete_event):
        self.tokenize()

```

---

### 544. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:237`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    notifications_command = None

    def __init__(
        self,
        pretty=True,
```

---

### 545. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:435`
**Severity:** LOW
**Category:** quality

**Description:** Function 'read_image' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return Style.from_dict(style_dict)

    def read_image(self, filename):
        try:
            with open(str(filename), "rb") as image_file:
```

---

### 546. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:453`
**Severity:** LOW
**Category:** quality

**Description:** Function 'read_text' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            return

    def read_text(self, filename, silent=False):
        if is_image_file(filename):
            return self.read_image(filename)
```

---

### 547. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:509`
**Severity:** LOW
**Category:** quality

**Description:** Function 'rule' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
                raise

    def rule(self):
        if self.pretty:
            style = dict(style=self.user_input_color) if self.user_input_color else dict()
```

---

### 548. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:516`
**Severity:** LOW
**Category:** quality

**Description:** Function 'interrupt_input' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            print()

    def interrupt_input(self):
        if self.prompt_session and self.prompt_session.app:
            # Store any partial input before interrupting
```

---

### 549. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:523`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_input' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.prompt_session.app.exit()

    def get_input(
        self,
        root,
```

---

### 550. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:653`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_continuation' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
                            self.clipboard_watcher.start()

                    def get_continuation(width, line_number, is_soft_wrap):
                        return self.prompt_prefix

```

---

### 551. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:736`
**Severity:** LOW
**Category:** quality

**Description:** Function 'add_to_input_history' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return inp

    def add_to_input_history(self, inp):
        if not self.input_history_file:
            return
```

---

### 552. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:747`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_input_history' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.tool_warning(f"Unable to write to input history file: {err}")

    def get_input_history(self):
        if not self.input_history_file:
            return []
```

---

### 553. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:754`
**Severity:** LOW
**Category:** quality

**Description:** Function 'log_llm_history' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return fh.load_history_strings()

    def log_llm_history(self, role, content):
        if not self.llm_history_file:
            return
```

---

### 554. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:767`
**Severity:** LOW
**Category:** quality

**Description:** Function 'display_user_input' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.llm_history_file = None

    def display_user_input(self, inp):
        if self.pretty and self.user_input_color:
            style = dict(style=self.user_input_color)
```

---

### 555. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:775`
**Severity:** LOW
**Category:** quality

**Description:** Function 'user_input' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.console.print(Text(inp), **style)

    def user_input(self, inp, log_only=True):
        if not log_only:
            self.display_user_input(inp)
```

---

### 556. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:807`
**Severity:** LOW
**Category:** quality

**Description:** Function 'confirm_ask' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

    @restore_multiline
    def confirm_ask(
        self,
        question,
```

---

### 557. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:861`
**Severity:** LOW
**Category:** quality

**Description:** Function 'is_valid_response' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        style = self._get_style()

        def is_valid_response(text):
            if not text:
                return True
```

---

### 558. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:928`
**Severity:** LOW
**Category:** quality

**Description:** Function 'prompt_ask' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

    @restore_multiline
    def prompt_ask(self, question, default="", subject=None):
        self.num_user_asks += 1

```

---

### 559. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:988`
**Severity:** LOW
**Category:** quality

**Description:** Function 'tool_error' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.console.print(message, **style)

    def tool_error(self, message="", strip=True):
        self.num_error_outputs += 1
        self._tool_message(message, strip, self.tool_error_color)
```

---

### 560. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:992`
**Severity:** LOW
**Category:** quality

**Description:** Function 'tool_warning' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._tool_message(message, strip, self.tool_error_color)

    def tool_warning(self, message="", strip=True):
        self._tool_message(message, strip, self.tool_warning_color)

```

---

### 561. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:995`
**Severity:** LOW
**Category:** quality

**Description:** Function 'tool_output' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self._tool_message(message, strip, self.tool_warning_color)

    def tool_output(self, *messages, log_only=False, bold=False):
        if messages:
            hist = " ".join(messages)
```

---

### 562. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:1014`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_assistant_mdstream' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.console.print(*messages, style=style)

    def get_assistant_mdstream(self):
        mdargs = dict(
            style=self.assistant_output_color,
```

---

### 563. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:1024`
**Severity:** LOW
**Category:** quality

**Description:** Function 'assistant_output' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return mdStream

    def assistant_output(self, message, pretty=None):
        if not message:
            self.tool_warning("Empty response received from LLM. Check your provider account?")
```

---

### 564. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:1118`
**Severity:** LOW
**Category:** quality

**Description:** Function 'append_chat_history' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            )

    def append_chat_history(self, text, linebreak=False, blockquote=False, strip=True):
        if blockquote:
            if strip:
```

---

### 565. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:1139`
**Severity:** LOW
**Category:** quality

**Description:** Function 'format_files_for_input' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
                self.chat_history_file = None  # Disable further attempts to write

    def format_files_for_input(self, rel_fnames, rel_read_only_fnames):
        if not self.pretty:
            read_only_files = []
```

---

### 566. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:1188`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_rel_fname' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def get_rel_fname(fname, root):
    try:
        return os.path.relpath(fname, root)
```

---

### 567. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:10`
**Severity:** LOW
**Category:** quality

**Description:** Class 'from' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```
import webbrowser
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from io import StringIO
```

---

### 568. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:81`
**Severity:** LOW
**Category:** quality

**Description:** Class 'class' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


@dataclass
class ConfirmGroup:
    preference: str = None
```

---

### 569. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:91`
**Severity:** LOW
**Category:** quality

**Description:** Class 'AutoCompleter' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class AutoCompleter(Completer):
    def __init__(
        self, root, rel_fnames, addable_rel_fnames, commands, encoding, abs_read_only_fnames=None
```

---

### 570. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/io.py:230`
**Severity:** LOW
**Category:** quality

**Description:** Class 'InputOutput' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class InputOutput:
    num_error_outputs = 0
    num_user_asks = 0
```

---

### 571. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/args.py:22`
**Severity:** LOW
**Category:** quality

**Description:** Function 'resolve_flacoaiignore_path' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def resolve_flacoaiignore_path(path_str, git_root=None):
    path = Path(path_str)
    if path.is_absolute():
```

---

### 572. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/args.py:31`
**Severity:** LOW
**Category:** quality

**Description:** Function 'default_env_file' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def default_env_file(git_root):
    return os.path.join(git_root, ".env") if git_root else ".env"

```

---

### 573. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/args.py:35`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_parser' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def get_parser(default_config_files, git_root):
    parser = configargparse.ArgumentParser(
        description="aider is AI pair programming in your terminal",
```

---

### 574. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/args.py:878`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_md_help' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def get_md_help():
    os.environ["COLUMNS"] = "70"
    sys.argv = ["aider"]
```

---

### 575. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/args.py:891`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_sample_yaml' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def get_sample_yaml():
    os.environ["COLUMNS"] = "100"
    sys.argv = ["aider"]
```

---

### 576. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/args.py:904`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_sample_dotenv' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def get_sample_dotenv():
    os.environ["COLUMNS"] = "120"
    sys.argv = ["aider"]
```

---

### 577. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/args.py:917`
**Severity:** LOW
**Category:** quality

**Description:** Function 'main' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]
```

---

### 578. 🟢 Incomplete TODO Comment

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/wholefile_func_prompts.py:24`
**Severity:** LOW
**Category:** quality

**Description:** TODO comment lacks detailed description

**Recommendation:** Add description explaining what needs to be done and why

**Code:**
```

    # TODO: should this be present for using this with gpt-4?
    repo_content_prefix = None
```

---

### 579. 🟢 Incomplete TODO Comment

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/wholefile_func_prompts.py:27`
**Severity:** LOW
**Category:** quality

**Description:** TODO comment lacks detailed description

**Recommendation:** Add description explaining what needs to be done and why

**Code:**
```

    # TODO: fix the chat history, except we can't keep the whole file

```

---

### 580. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:21`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_edits' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    gpt_prompts = EditBlockPrompts()

    def get_edits(self):
        content = self.partial_response_content

```

---

### 581. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:38`
**Severity:** LOW
**Category:** quality

**Description:** Function 'apply_edits_dry_run' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return edits

    def apply_edits_dry_run(self, edits):
        return self.apply_edits(edits, dry_run=True)

```

---

### 582. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:41`
**Severity:** LOW
**Category:** quality

**Description:** Function 'apply_edits' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return self.apply_edits(edits, dry_run=True)

    def apply_edits(self, edits, dry_run=False):
        failed = []
        passed = []
```

---

### 583. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:127`
**Severity:** LOW
**Category:** quality

**Description:** Function 'prep' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def prep(content):
    if content and not content.endswith("\n"):
        content += "\n"
```

---

### 584. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:134`
**Severity:** LOW
**Category:** quality

**Description:** Function 'perfect_or_whitespace' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def perfect_or_whitespace(whole_lines, part_lines, replace_lines):
    # Try for a perfect match
    res = perfect_replace(whole_lines, part_lines, replace_lines)
```

---

### 585. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:146`
**Severity:** LOW
**Category:** quality

**Description:** Function 'perfect_replace' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def perfect_replace(whole_lines, part_lines, replace_lines):
    part_tup = tuple(part_lines)
    part_len = len(part_lines)
```

---

### 586. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:243`
**Severity:** LOW
**Category:** quality

**Description:** Function 'replace_part_with_missing_leading_whitespace' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def replace_part_with_missing_leading_whitespace(whole_lines, part_lines, replace_lines):
    # GPT often messes up leading whitespace.
    # It usually does it uniformly across the ORIG and UPD blocks.
```

---

### 587. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:276`
**Severity:** LOW
**Category:** quality

**Description:** Function 'match_but_for_leading_whitespace' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def match_but_for_leading_whitespace(whole_lines, part_lines):
    num = len(whole_lines)

```

---

### 588. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:296`
**Severity:** LOW
**Category:** quality

**Description:** Function 'replace_closest_edit_distance' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def replace_closest_edit_distance(whole_lines, part, part_lines, replace_lines):
    similarity_thresh = 0.8

```

---

### 589. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:364`
**Severity:** LOW
**Category:** quality

**Description:** Function 'do_replace' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def do_replace(fname, content, before_text, after_text, fence=None):
    before_text = strip_quoted_wrapping(before_text, fname, fence)
    after_text = strip_quoted_wrapping(after_text, fname, fence)
```

---

### 590. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:408`
**Severity:** LOW
**Category:** quality

**Description:** Function 'strip_filename' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def strip_filename(filename, fence):
    filename = filename.strip()

```

---

### 591. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:439`
**Severity:** LOW
**Category:** quality

**Description:** Function 'find_original_update_blocks' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def find_original_update_blocks(content, fence=DEFAULT_FENCE, valid_fnames=None):
    lines = content.splitlines(keepends=True)
    i = 0
```

---

### 592. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:602`
**Severity:** LOW
**Category:** quality

**Description:** Function 'find_similar_lines' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def find_similar_lines(search_lines, content_lines, threshold=0.6):
    search_lines = search_lines.splitlines()
    content_lines = content_lines.splitlines()
```

---

### 593. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_coder.py:631`
**Severity:** LOW
**Category:** quality

**Description:** Function 'main' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def main():
    history_md = Path(sys.argv[1]).read_text()
    if not history_md:
```

---

### 594. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/problem_stats.py:16`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_dirs_from_leaderboard' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def get_dirs_from_leaderboard():
    # Load the leaderboard data
    with open("aider/website/_data/polyglot_leaderboard.yml") as f:
```

---

### 595. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/problem_stats.py:62`
**Severity:** LOW
**Category:** quality

**Description:** Function 'analyze_exercise_solutions' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def analyze_exercise_solutions(dirs=None, topn=None, copy_hard_set=False):
    PARSE_ERROR_M = 4  # Threshold for number of parse errors to DQ an exercise

```

---

### 596. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_symbols_analyzer.py:11`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    """Analyzes SF Symbols usage in iOS code."""

    def __init__(self, io=None, verbose=False):
        super().__init__(io, verbose)

```

---

### 597. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_prompts.py:59`
**Severity:** LOW
**Category:** quality

**Description:** Function 'factorial' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
{fence[0]}python
<<<<<<< SEARCH
def factorial(n):
    "compute factorial"

```

---

### 598. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editblock_prompts.py:98`
**Severity:** LOW
**Category:** quality

**Description:** Function 'hello' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
<<<<<<< SEARCH
=======
def hello():
    "print a greeting"

```

---

### 599. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_editor.py:16`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_get_environment_editor' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def test_get_environment_editor():
    # Test with no environment variables set
    with patch.dict(os.environ, {}, clear=True):
```

---

### 600. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_editor.py:30`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_discover_editor_defaults' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def test_discover_editor_defaults():
    with patch("platform.system") as mock_system:
        # Test Windows default
```

---

### 601. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_editor.py:48`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_write_temp_file' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def test_write_temp_file():
    # Test basic file creation
    content = "test content"
```

---

### 602. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_editor.py:68`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_print_status_message' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def test_print_status_message(capsys):
    # Test success message
    print_status_message(True, "Success!")
```

---

### 603. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_editor.py:80`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_discover_editor_override' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def test_discover_editor_override():
    # Test editor override
    assert discover_editor("code") == "code"
```

---

### 604. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_editor.py:86`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_pipe_editor_with_fake_editor' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def test_pipe_editor_with_fake_editor():
    # Create a temporary Python script that logs its arguments
    import sys
```

---

### 605. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_editor.py:122`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_pipe_editor' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def test_pipe_editor():
    # Test with default editor
    test_content = "Initial content"
```

---

### 606. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/dump.py:5`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cvt' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def cvt(s):
    if isinstance(s, str):
        return s
```

---

### 607. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/dump.py:14`
**Severity:** LOW
**Category:** quality

**Description:** Function 'dump' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def dump(*vals):
    # http://docs.python.org/library/traceback.html
    stack = traceback.extract_stack()
```

---

### 608. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/basic/test_urls.py:6`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_urls' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def test_urls():
    url_attributes = [
        attr
```

---

### 609. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:57`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

class UnknownEditFormat(ValueError):
    def __init__(self, edit_format, valid_formats):
        self.edit_format = edit_format
        self.valid_formats = valid_formats
```

---

### 610. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:73`
**Severity:** LOW
**Category:** quality

**Description:** Function 'wrap_fence' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def wrap_fence(name):
    return f"<{name}>", f"</{name}>"

```

---

### 611. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:125`
**Severity:** LOW
**Category:** quality

**Description:** Function 'create' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

    @classmethod
    def create(
        self,
        main_model=None,
```

---

### 612. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:203`
**Severity:** LOW
**Category:** quality

**Description:** Function 'clone' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        raise UnknownEditFormat(edit_format, valid_formats)

    def clone(self, **kwargs):
        new_coder = Coder.create(from_coder=self, **kwargs)
        return new_coder
```

---

### 613. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:207`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_announcements' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return new_coder

    def get_announcements(self):
        from flacoai.branding import (
            get_flaco_ascii_art,
```

---

### 614. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:341`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    ok_to_warm_cache = False

    def __init__(
        self,
        main_model,
```

---

### 615. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:624`
**Severity:** LOW
**Category:** quality

**Description:** Function 'add_rel_fname' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            bold = False

    def add_rel_fname(self, rel_fname):
        self.abs_fnames.add(self.abs_root_path(rel_fname))
        self.check_added_files()
```

---

### 616. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:628`
**Severity:** LOW
**Category:** quality

**Description:** Function 'drop_rel_fname' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.check_added_files()

    def drop_rel_fname(self, fname):
        abs_fname = self.abs_root_path(fname)
        if abs_fname in self.abs_fnames:
```

---

### 617. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:634`
**Severity:** LOW
**Category:** quality

**Description:** Function 'abs_root_path' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            return True

    def abs_root_path(self, path):
        key = path
        if key in self.abs_root_path_cache:
```

---

### 618. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:647`
**Severity:** LOW
**Category:** quality

**Description:** Function 'show_pretty' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    fence = fences[0]

    def show_pretty(self):
        if not self.pretty:
            return False
```

---

### 619. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:666`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_abs_fnames_content' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
                self.waiting_spinner = None

    def get_abs_fnames_content(self):
        for fname in list(self.abs_fnames):
            content = self.io.read_text(fname)
```

---

### 620. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:677`
**Severity:** LOW
**Category:** quality

**Description:** Function 'choose_fence' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
                yield fname, content

    def choose_fence(self):
        all_content = ""
        for _fname, content in self.get_abs_fnames_content():
```

---

### 621. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:705`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_files_content' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return

    def get_files_content(self, fnames=None):
        if not fnames:
            fnames = self.abs_fnames
```

---

### 622. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:727`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_read_only_files_content' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return prompt

    def get_read_only_files_content(self):
        prompt = ""
        for fname in self.abs_read_only_fnames:
```

---

### 623. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:740`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_cur_message_text' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return prompt

    def get_cur_message_text(self):
        text = ""
        for msg in self.cur_messages:
```

---

### 624. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:746`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_ident_mentions' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return text

    def get_ident_mentions(self, text):
        # Split the string on any character that is not alphanumeric
        # \W+ matches one or more non-word characters (equivalent to [^a-zA-Z0-9_]+)
```

---

### 625. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:752`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_ident_filename_matches' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return words

    def get_ident_filename_matches(self, idents):
        all_fnames = defaultdict(set)
        for fname in self.get_all_relative_files():
```

---

### 626. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:777`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_repo_map' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return matches

    def get_repo_map(self, force_refresh=False):
        if not self.repo_map:
            return
```

---

### 627. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:818`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_repo_messages' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return repo_content

    def get_repo_messages(self):
        repo_messages = []
        repo_content = self.get_repo_map()
```

---

### 628. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:831`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_readonly_files_messages' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return repo_messages

    def get_readonly_files_messages(self):
        readonly_messages = []

```

---

### 629. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:857`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_chat_files_messages' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return readonly_messages

    def get_chat_files_messages(self):
        chat_files_messages = []
        if self.abs_fnames:
```

---

### 630. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:885`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_images_message' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return chat_files_messages

    def get_images_message(self, fnames):
        supports_images = self.main_model.info.get("supports_vision")
        supports_pdfs = self.main_model.info.get("supports_pdf_input") or self.main_model.info.get(
```

---

### 631. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:927`
**Severity:** LOW
**Category:** quality

**Description:** Function 'run_stream' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return {"role": "user", "content": image_messages}

    def run_stream(self, user_message):
        self.io.user_input(user_message)
        self.init_before_message()
```

---

### 632. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:932`
**Severity:** LOW
**Category:** quality

**Description:** Function 'init_before_message' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        yield from self.send_message(user_message)

    def init_before_message(self):
        self.flacoai_edited_files = set()
        self.reflected_message = None
```

---

### 633. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:944`
**Severity:** LOW
**Category:** quality

**Description:** Function 'run' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.commit_before_message.append(self.repo.get_head_commit_sha())

    def run(self, with_message=None, preproc=True):
        try:
            if with_message:
```

---

### 634. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:962`
**Severity:** LOW
**Category:** quality

**Description:** Function 'copy_context' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            return

    def copy_context(self):
        if self.auto_copy_context:
            self.commands.cmd_copy_context()
```

---

### 635. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:966`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_input' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.commands.cmd_copy_context()

    def get_input(self):
        inchat_files = self.get_inchat_relative_files()
        read_only_files = [self.get_rel_fname(fname) for fname in self.abs_read_only_fnames]
```

---

### 636. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:980`
**Severity:** LOW
**Category:** quality

**Description:** Function 'preproc_user_input' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        )

    def preproc_user_input(self, inp):
        if not inp:
            return
```

---

### 637. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:992`
**Severity:** LOW
**Category:** quality

**Description:** Function 'run_one' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return inp

    def run_one(self, user_message, preproc):
        self.init_before_message()

```

---

### 638. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1054`
**Severity:** LOW
**Category:** quality

**Description:** Function 'keyboard_interrupt' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return inp

    def keyboard_interrupt(self):
        # Ensure cursor is visible on exit
        Console().show_cursor(True)
```

---

### 639. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1070`
**Severity:** LOW
**Category:** quality

**Description:** Function 'summarize_start' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.last_keyboard_interrupt = now

    def summarize_start(self):
        if not self.summarizer.too_big(self.done_messages):
            return
```

---

### 640. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1082`
**Severity:** LOW
**Category:** quality

**Description:** Function 'summarize_worker' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.summarizer_thread.start()

    def summarize_worker(self):
        self.summarizing_messages = list(self.done_messages)
        try:
```

---

### 641. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1092`
**Severity:** LOW
**Category:** quality

**Description:** Function 'summarize_end' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.io.tool_output("Finished summarizing chat history.")

    def summarize_end(self):
        if self.summarizer_thread is None:
            return
```

---

### 642. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1104`
**Severity:** LOW
**Category:** quality

**Description:** Function 'move_back_cur_messages' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.summarized_done_messages = []

    def move_back_cur_messages(self, message):
        self.done_messages += self.cur_messages
        self.summarize_start()
```

---

### 643. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1195`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_platform_info' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return None

    def get_platform_info(self):
        platform_text = ""
        try:
```

---

### 644. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1242`
**Severity:** LOW
**Category:** quality

**Description:** Function 'fmt_system_prompt' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return platform_text

    def fmt_system_prompt(self, prompt):
        final_reminders = []
        if self.main_model.lazy:
```

---

### 645. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1294`
**Severity:** LOW
**Category:** quality

**Description:** Function 'format_chat_chunks' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return prompt

    def format_chat_chunks(self):
        self.choose_fence()
        main_sys = self.fmt_system_prompt(self.gpt_prompts.main_system)
```

---

### 646. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1401`
**Severity:** LOW
**Category:** quality

**Description:** Function 'format_messages' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return chunks

    def format_messages(self):
        chunks = self.format_chat_chunks()
        if self.add_cache_headers:
```

---

### 647. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1408`
**Severity:** LOW
**Category:** quality

**Description:** Function 'warm_cache' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return chunks

    def warm_cache(self, chunks):
        if not self.add_cache_headers:
            return
```

---

### 648. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1425`
**Severity:** LOW
**Category:** quality

**Description:** Function 'warm_cache_worker' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            return

        def warm_cache_worker():
            while self.ok_to_warm_cache:
                time.sleep(1)
```

---

### 649. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1487`
**Severity:** LOW
**Category:** quality

**Description:** Function 'send_message' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return True

    def send_message(self, inp):
        self.event("message_send_starting")

```

---

### 650. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1693`
**Severity:** LOW
**Category:** quality

**Description:** Function 'reply_completed' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
                    return

    def reply_completed(self):
        pass

```

---

### 651. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1696`
**Severity:** LOW
**Category:** quality

**Description:** Function 'show_exhausted_error' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        pass

    def show_exhausted_error(self):
        output_tokens = 0
        if self.partial_response_content:
```

---

### 652. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1749`
**Severity:** LOW
**Category:** quality

**Description:** Function 'lint_edited' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.io.offer_url(urls.token_limits)

    def lint_edited(self, fnames):
        res = ""
        for fname in fnames:
```

---

### 653. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1770`
**Severity:** LOW
**Category:** quality

**Description:** Function 'add_assistant_reply_to_cur_messages' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.ok_to_warm_cache = False

    def add_assistant_reply_to_cur_messages(self):
        if self.partial_response_content:
            self.cur_messages += [dict(role="assistant", content=self.partial_response_content)]
```

---

### 654. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1782`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_file_mentions' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            ]

    def get_file_mentions(self, content, ignore_current=False):
        words = set(word for word in content.split())

```

---

### 655. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1829`
**Severity:** LOW
**Category:** quality

**Description:** Function 'check_for_file_mentions' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return mentioned_rel_fnames

    def check_for_file_mentions(self, content):
        mentioned_rel_fnames = self.get_file_mentions(content)

```

---

### 656. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1851`
**Severity:** LOW
**Category:** quality

**Description:** Function 'send' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            return prompts.added_files.format(fnames=", ".join(added_fnames))

    def send(self, messages, model=None, functions=None):
        self.got_reasoning_content = False
        self.ended_reasoning_content = False
```

---

### 657. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1904`
**Severity:** LOW
**Category:** quality

**Description:** Function 'show_send_output' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
                    self.io.ai_output(json.dumps(args, indent=4))

    def show_send_output(self, completion):
        # Stop spinner once we have a response
        self._stop_waiting_spinner()
```

---

### 658. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1968`
**Severity:** LOW
**Category:** quality

**Description:** Function 'show_send_output_stream' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            raise FinishReasonLength()

    def show_send_output_stream(self, completion):
        received_content = False

```

---

### 659. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2045`
**Severity:** LOW
**Category:** quality

**Description:** Function 'live_incremental_response' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.io.tool_warning("Empty response received from LLM. Check your provider account?")

    def live_incremental_response(self, final):
        show_resp = self.render_incremental_response(final)
        # Apply any reasoning tag formatting
```

---

### 660. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2062`
**Severity:** LOW
**Category:** quality

**Description:** Function 'calculate_and_show_tokens_and_cost' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        )

    def calculate_and_show_tokens_and_cost(self, messages, completion=None):
        prompt_tokens = 0
        completion_tokens = 0
```

---

### 661. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2117`
**Severity:** LOW
**Category:** quality

**Description:** Function 'format_cost' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.message_cost += cost

        def format_cost(value):
            if value == 0:
                return "0.00"
```

---

### 662. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2138`
**Severity:** LOW
**Category:** quality

**Description:** Function 'compute_costs_from_tokens' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.usage_report = tokens_report + sep + cost_report

    def compute_costs_from_tokens(
        self, prompt_tokens, completion_tokens, cache_write_tokens, cache_hit_tokens
    ):
```

---

### 663. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2170`
**Severity:** LOW
**Category:** quality

**Description:** Function 'show_usage_report' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return cost

    def show_usage_report(self):
        if not self.usage_report:
            return
```

---

### 664. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2196`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_multi_response_content_in_progress' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.message_tokens_received = 0

    def get_multi_response_content_in_progress(self, final=False):
        cur = self.multi_response_content or ""
        new = self.partial_response_content or ""
```

---

### 665. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2205`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_rel_fname' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return cur + new

    def get_rel_fname(self, fname):
        try:
            return os.path.relpath(fname, self.root)
```

---

### 666. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2211`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_inchat_relative_files' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            return fname

    def get_inchat_relative_files(self):
        files = [self.get_rel_fname(fname) for fname in self.abs_fnames]
        return sorted(set(files))
```

---

### 667. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2215`
**Severity:** LOW
**Category:** quality

**Description:** Function 'is_file_safe' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return sorted(set(files))

    def is_file_safe(self, fname):
        try:
            return Path(self.abs_root_path(fname)).is_file()
```

---

### 668. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2221`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_all_relative_files' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            return

    def get_all_relative_files(self):
        if self.repo:
            files = self.repo.get_tracked_files()
```

---

### 669. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2232`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_all_abs_files' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return sorted(set(files))

    def get_all_abs_files(self):
        files = self.get_all_relative_files()
        files = [self.abs_root_path(path) for path in files]
```

---

### 670. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2237`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_addable_relative_files' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return files

    def get_addable_relative_files(self):
        all_files = set(self.get_all_relative_files())
        inchat_files = set(self.get_inchat_relative_files())
```

---

### 671. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2243`
**Severity:** LOW
**Category:** quality

**Description:** Function 'check_for_dirty_commit' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return all_files - inchat_files - read_only_files

    def check_for_dirty_commit(self, path):
        if not self.repo:
            return
```

---

### 672. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2259`
**Severity:** LOW
**Category:** quality

**Description:** Function 'allowed_to_edit' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.need_commit_before_edits.add(path)

    def allowed_to_edit(self, path):
        full_path = self.abs_root_path(path)
        if self.repo:
```

---

### 673. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2312`
**Severity:** LOW
**Category:** quality

**Description:** Function 'check_added_files' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    warning_given = False

    def check_added_files(self):
        if self.warning_given:
            return
```

---

### 674. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2337`
**Severity:** LOW
**Category:** quality

**Description:** Function 'prepare_to_edit' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.warning_given = True

    def prepare_to_edit(self, edits):
        res = []
        seen = dict()
```

---

### 675. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2364`
**Severity:** LOW
**Category:** quality

**Description:** Function 'apply_updates' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return res

    def apply_updates(self):
        edited = set()
        try:
```

---

### 676. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2406`
**Severity:** LOW
**Category:** quality

**Description:** Function 'parse_partial_args' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return edited

    def parse_partial_args(self):
        # dump(self.partial_response_function_call)

```

---

### 677. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2435`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_context_from_history' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    # commits...

    def get_context_from_history(self, history):
        context = ""
        if history:
```

---

### 678. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2443`
**Severity:** LOW
**Category:** quality

**Description:** Function 'auto_commit' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return context

    def auto_commit(self, edited, context=None):
        if not self.repo or not self.auto_commits or self.dry_run:
            return
```

---

### 679. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2465`
**Severity:** LOW
**Category:** quality

**Description:** Function 'show_auto_commit_outcome' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            return

    def show_auto_commit_outcome(self, res):
        commit_hash, commit_message = res
        self.last_flacoai_commit_hash = commit_hash
```

---

### 680. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2473`
**Severity:** LOW
**Category:** quality

**Description:** Function 'show_undo_hint' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.commands.cmd_diff()

    def show_undo_hint(self):
        if not self.commit_before_message:
            return
```

---

### 681. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2479`
**Severity:** LOW
**Category:** quality

**Description:** Function 'dirty_commit' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.io.tool_output("You can use /undo to undo and discard each flacoai commit.")

    def dirty_commit(self):
        if not self.need_commit_before_edits:
            return
```

---

### 682. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2493`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_edits' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return True

    def get_edits(self, mode="update"):
        return []

```

---

### 683. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2496`
**Severity:** LOW
**Category:** quality

**Description:** Function 'apply_edits' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return []

    def apply_edits(self, edits):
        return

```

---

### 684. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2499`
**Severity:** LOW
**Category:** quality

**Description:** Function 'apply_edits_dry_run' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return

    def apply_edits_dry_run(self, edits):
        return edits

```

---

### 685. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2502`
**Severity:** LOW
**Category:** quality

**Description:** Function 'run_shell_commands' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return edits

    def run_shell_commands(self):
        if not self.suggest_shell_commands:
            return ""
```

---

### 686. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:2518`
**Severity:** LOW
**Category:** quality

**Description:** Function 'handle_shell_commands' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return accumulated_output

    def handle_shell_commands(self, commands_str, group):
        commands = commands_str.strip().splitlines()
        command_count = sum(
```

---

### 687. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:56`
**Severity:** LOW
**Category:** quality

**Description:** Class 'UnknownEditFormat' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class UnknownEditFormat(ValueError):
    def __init__(self, edit_format, valid_formats):
        self.edit_format = edit_format
```

---

### 688. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:65`
**Severity:** LOW
**Category:** quality

**Description:** Class 'MissingAPIKeyError' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class MissingAPIKeyError(ValueError):
    pass

```

---

### 689. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:69`
**Severity:** LOW
**Category:** quality

**Description:** Class 'FinishReasonLength' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class FinishReasonLength(Exception):
    pass

```

---

### 690. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:88`
**Severity:** LOW
**Category:** quality

**Description:** Class 'Coder' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class Coder:
    abs_fnames = None
    abs_read_only_fnames = None
```

---

### 691. 🟢 Incomplete TODO Comment

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/base_coder.py:1899`
**Severity:** LOW
**Category:** quality

**Description:** TODO comment lacks detailed description

**Recommendation:** Add description explaining what needs to be done and why

**Code:**
```
            elif self.partial_response_function_call:
                # TODO: push this into subclasses
                args = self.parse_partial_args()
```

---

### 692. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:44`
**Severity:** LOW
**Category:** quality

**Description:** Function 'check_config_files_for_yes' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def check_config_files_for_yes(config_files):
    found = False
    for config_file in config_files:
```

---

### 693. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:89`
**Severity:** LOW
**Category:** quality

**Description:** Function 'make_new_repo' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def make_new_repo(git_root, io):
    try:
        repo = git.Repo.init(git_root)
```

---

### 694. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:102`
**Severity:** LOW
**Category:** quality

**Description:** Function 'setup_git' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def setup_git(git_root, io):
    if git is None:
        return
```

---

### 695. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:156`
**Severity:** LOW
**Category:** quality

**Description:** Function 'check_gitignore' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def check_gitignore(git_root, io, ask=True):
    if not git_root:
        return
```

---

### 696. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:209`
**Severity:** LOW
**Category:** quality

**Description:** Function 'check_streamlit_install' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def check_streamlit_install(io):
    return utils.check_pip_install_extra(
        io,
```

---

### 697. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:218`
**Severity:** LOW
**Category:** quality

**Description:** Function 'write_streamlit_credentials' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def write_streamlit_credentials():
    from streamlit.file_util import get_streamlit_file_path

```

---

### 698. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:234`
**Severity:** LOW
**Category:** quality

**Description:** Function 'launch_gui' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def launch_gui(args):
    from streamlit.web import cli

```

---

### 699. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:279`
**Severity:** LOW
**Category:** quality

**Description:** Function 'parse_lint_cmds' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def parse_lint_cmds(lint_cmds, io):
    err = False
    res = dict()
```

---

### 700. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:306`
**Severity:** LOW
**Category:** quality

**Description:** Function 'generate_search_path_list' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def generate_search_path_list(default_file, git_root, command_line_file):
    files = []
    files.append(Path.home() / default_file)  # homedir
```

---

### 701. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:336`
**Severity:** LOW
**Category:** quality

**Description:** Function 'register_models' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def register_models(git_root, model_settings_fname, io, verbose=False):
    model_settings_files = generate_search_path_list(
        ".flacoai.model.settings.yml", git_root, model_settings_fname
```

---

### 702. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:362`
**Severity:** LOW
**Category:** quality

**Description:** Function 'load_dotenv_files' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def load_dotenv_files(git_root, dotenv_fname, encoding="utf-8"):
    # Standard .env file search path
    dotenv_files = generate_search_path_list(
```

---

### 703. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:391`
**Severity:** LOW
**Category:** quality

**Description:** Function 'register_litellm_models' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def register_litellm_models(git_root, model_metadata_fname, io, verbose=False):
    model_metadata_files = []

```

---

### 704. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:413`
**Severity:** LOW
**Category:** quality

**Description:** Function 'sanity_check_repo' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def sanity_check_repo(repo, io):
    if not repo:
        return True
```

---

### 705. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:452`
**Severity:** LOW
**Category:** quality

**Description:** Function 'main' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def main(argv=None, input=None, output=None, force_git_root=None, return_coder=False):
    report_uncaught_exceptions()

```

---

### 706. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:586`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_io' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    editing_mode = EditingMode.VI if args.vim else EditingMode.EMACS

    def get_io(pretty):
        return InputOutput(
            pretty,
```

---

### 707. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:1265`
**Severity:** LOW
**Category:** quality

**Description:** Function 'check_and_load_imports' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def check_and_load_imports(io, is_first_run, verbose=False):
    try:
        if is_first_run:
```

---

### 708. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/main.py:1295`
**Severity:** LOW
**Category:** quality

**Description:** Function 'load_slow_imports' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def load_slow_imports(swallow=True):
    # These imports are deferred in various ways to
    # improve startup time.
```

---

### 709. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/patch_coder.py:17`
**Severity:** LOW
**Category:** quality

**Description:** Class 'ActionType' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class ActionType(str, Enum):
    ADD = "Add"
    DELETE = "Delete"
```

---

### 710. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/patch_coder.py:23`
**Severity:** LOW
**Category:** quality

**Description:** Class 'class' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


@dataclass
class Chunk:
    orig_index: int = -1  # Line number in the *original* file block where the change starts
```

---

### 711. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/patch_coder.py:30`
**Severity:** LOW
**Category:** quality

**Description:** Class 'class' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


@dataclass
class PatchAction:
    type: ActionType
```

---

### 712. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/patch_coder.py:45`
**Severity:** LOW
**Category:** quality

**Description:** Class 'class' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


@dataclass
class Patch:
    actions: Dict[str, PatchAction] = field(default_factory=dict)
```

---

### 713. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:17`
**Severity:** LOW
**Category:** quality

**Description:** Function 'generic_visit' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    """

    def generic_visit(self, node):
        for child in ast.iter_child_nodes(node):
            child.parent = node
```

---

### 714. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:23`
**Severity:** LOW
**Category:** quality

**Description:** Function 'verify_full_func_at_top_level' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def verify_full_func_at_top_level(tree, func, func_children):
    func_nodes = [
        item for item in ast.walk(tree) if isinstance(item, ast.FunctionDef) and item.name == func
```

---

### 715. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:43`
**Severity:** LOW
**Category:** quality

**Description:** Function 'verify_old_class_children' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def verify_old_class_children(tree, old_class, old_class_children):
    node = next(
        (
```

---

### 716. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:62`
**Severity:** LOW
**Category:** quality

**Description:** Function 'verify_refactor' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def verify_refactor(fname, func, func_children, old_class, old_class_children):
    with open(fname, "r") as file:
        file_contents = file.read()
```

---

### 717. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:77`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

class SelfUsageChecker(ast.NodeVisitor):
    def __init__(self):
        self.non_self_methods = []
        self.parent_class_name = None
```

---

### 718. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:82`
**Severity:** LOW
**Category:** quality

**Description:** Function 'visit_FunctionDef' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.num_class_children = 0

    def visit_FunctionDef(self, node):
        # Check if the first argument is 'self' and if it's not used
        if node.args.args and node.args.args[0].arg == "self":
```

---

### 719. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:107`
**Severity:** LOW
**Category:** quality

**Description:** Function 'visit_ClassDef' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        self.parent_class_name = node.name
        self.num_class_children = sum(1 for _ in ast.walk(node))
```

---

### 720. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:113`
**Severity:** LOW
**Category:** quality

**Description:** Function 'find_python_files' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def find_python_files(path):
    if os.path.isfile(path) and path.endswith(".py"):
        return [path]
```

---

### 721. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:128`
**Severity:** LOW
**Category:** quality

**Description:** Function 'find_non_self_methods' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def find_non_self_methods(path):
    python_files = find_python_files(path)
    non_self_methods = []
```

---

### 722. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:145`
**Severity:** LOW
**Category:** quality

**Description:** Function 'process' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def process(entry):
    fname, class_name, method_name, class_children, method_children = entry
    if method_children > class_children / 2:
```

---

### 723. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:199`
**Severity:** LOW
**Category:** quality

**Description:** Function 'main' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def main(paths):
    for path in paths:
        methods = find_non_self_methods(path)
```

---

### 724. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:59`
**Severity:** LOW
**Category:** quality

**Description:** Class 'had' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```
    assert (
        pct_diff_children < 10
    ), f"Old class had {old_class_children} children, new class has {num_children}"


```

---

### 725. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:59`
**Severity:** LOW
**Category:** quality

**Description:** Class 'has' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```
    assert (
        pct_diff_children < 10
    ), f"Old class had {old_class_children} children, new class has {num_children}"


```

---

### 726. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:76`
**Severity:** LOW
**Category:** quality

**Description:** Class 'SelfUsageChecker' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class SelfUsageChecker(ast.NodeVisitor):
    def __init__(self):
        self.non_self_methods = []
```

---

### 727. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:172`
**Severity:** LOW
**Category:** quality

**Description:** Class 'to' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```
    ins_fname.write_text(f"""# Refactor {class_name}.{method_name}

Refactor the `{method_name}` method in the `{class_name}` class to be a stand alone, top level function.
Name the new function `{method_name}`, exactly the same name as the existing method.
Update any existing `self.{method_name}` calls to work with the new `{method_name}` function.
```

---

### 728. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/benchmark/refactor_tools.py:183`
**Severity:** LOW
**Category:** quality

**Description:** Class 'TheTest' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```
from pathlib import Path

class TheTest(unittest.TestCase):
    def test_{method_name}(self):
        fname = Path(__file__).parent / "{fname.name}"
```

---

### 729. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:5`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

class DummyIO:
    def __init__(self):
        self.outputs = []
        self.confirmed = False
```

---

### 730. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:9`
**Severity:** LOW
**Category:** quality

**Description:** Function 'tool_output' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.confirmed = False

    def tool_output(self, msg):
        self.outputs.append(msg)

```

---

### 731. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:12`
**Severity:** LOW
**Category:** quality

**Description:** Function 'confirm_ask' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.outputs.append(msg)

    def confirm_ask(self, msg, default="y"):
        self.outputs.append(f"confirm: {msg}")
        return self.confirmed
```

---

### 732. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:16`
**Severity:** LOW
**Category:** quality

**Description:** Function 'tool_error' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return self.confirmed

    def tool_error(self, msg):
        self.outputs.append(f"error: {msg}")

```

---

### 733. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:20`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_scraper_disable_playwright_flag' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def test_scraper_disable_playwright_flag(monkeypatch):
    io = DummyIO()
    # Simulate that playwright is not available
```

---

### 734. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:28`
**Severity:** LOW
**Category:** quality

**Description:** Function 'fake_httpx' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    called = {}

    def fake_httpx(url):
        called["called"] = True
        return "plain text", "text/plain"
```

---

### 735. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:38`
**Severity:** LOW
**Category:** quality

**Description:** Function 'test_scraper_enable_playwright' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def test_scraper_enable_playwright(monkeypatch):
    io = DummyIO()
    # Simulate that playwright is available and should be used
```

---

### 736. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:45`
**Severity:** LOW
**Category:** quality

**Description:** Function 'fake_playwright' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    called = {}

    def fake_playwright(url):
        called["called"] = True
        return "<html>hi</html>", "text/html"
```

---

### 737. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:63`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    # Dummy IO to capture outputs and warnings
    class DummyIO:
        def __init__(self):
            self.outputs = []
            self.warnings = []
```

---

### 738. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:68`
**Severity:** LOW
**Category:** quality

**Description:** Function 'tool_output' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.errors = []

        def tool_output(self, msg, *a, **k):
            self.outputs.append(msg)

```

---

### 739. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:71`
**Severity:** LOW
**Category:** quality

**Description:** Function 'tool_warning' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.outputs.append(msg)

        def tool_warning(self, msg, *a, **k):
            self.warnings.append(msg)

```

---

### 740. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:74`
**Severity:** LOW
**Category:** quality

**Description:** Function 'tool_error' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.warnings.append(msg)

        def tool_error(self, msg, *a, **k):
            self.errors.append(msg)

```

---

### 741. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:77`
**Severity:** LOW
**Category:** quality

**Description:** Function 'read_text' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.errors.append(msg)

        def read_text(self, filename, silent=False):
            return ""

```

---

### 742. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:80`
**Severity:** LOW
**Category:** quality

**Description:** Function 'confirm_ask' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            return ""

        def confirm_ask(self, *a, **k):
            return True

```

---

### 743. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:83`
**Severity:** LOW
**Category:** quality

**Description:** Function 'print' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            return True

        def print(self, *a, **k):
            pass

```

---

### 744. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:88`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    # Dummy coder to satisfy Commands
    class DummyCoder:
        def __init__(self):
            self.cur_messages = []
            self.main_model = type("M", (), {"edit_format": "code", "name": "dummy", "info": {}})
```

---

### 745. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:92`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_rel_fname' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.main_model = type("M", (), {"edit_format": "code", "name": "dummy", "info": {}})

        def get_rel_fname(self, fname):
            return fname

```

---

### 746. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:95`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_inchat_relative_files' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            return fname

        def get_inchat_relative_files(self):
            return []

```

---

### 747. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:98`
**Severity:** LOW
**Category:** quality

**Description:** Function 'abs_root_path' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            return []

        def abs_root_path(self, fname):
            return fname

```

---

### 748. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:101`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_all_abs_files' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            return fname

        def get_all_abs_files(self):
            return []

```

---

### 749. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:104`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_announcements' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            return []

        def get_announcements(self):
            return []

```

---

### 750. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:107`
**Severity:** LOW
**Category:** quality

**Description:** Function 'format_chat_chunks' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            return []

        def format_chat_chunks(self):
            return type("Chunks", (), {"repo": [], "readonly_files": [], "chat_files": []})()

```

---

### 751. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:110`
**Severity:** LOW
**Category:** quality

**Description:** Function 'event' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            return type("Chunks", (), {"repo": [], "readonly_files": [], "chat_files": []})()

        def event(self, *a, **k):
            pass

```

---

### 752. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:118`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    # Patch Scraper to always use scrape_with_httpx and never warn
    class DummyScraper:
        def __init__(self, **kwargs):
            self.called = False

```

---

### 753. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:121`
**Severity:** LOW
**Category:** quality

**Description:** Function 'scrape' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.called = False

        def scrape(self, url):
            self.called = True
            return "dummy content"
```

---

### 754. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:4`
**Severity:** LOW
**Category:** quality

**Description:** Class 'DummyIO' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class DummyIO:
    def __init__(self):
        self.outputs = []
```

---

### 755. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:62`
**Severity:** LOW
**Category:** quality

**Description:** Class 'DummyIO' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```

    # Dummy IO to capture outputs and warnings
    class DummyIO:
        def __init__(self):
            self.outputs = []
```

---

### 756. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:87`
**Severity:** LOW
**Category:** quality

**Description:** Class 'DummyCoder' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```

    # Dummy coder to satisfy Commands
    class DummyCoder:
        def __init__(self):
            self.cur_messages = []
```

---

### 757. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/tests/scrape/test_playwright_disable.py:117`
**Severity:** LOW
**Category:** quality

**Description:** Class 'DummyScraper' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```

    # Patch Scraper to always use scrape_with_httpx and never warn
    class DummyScraper:
        def __init__(self, **kwargs):
            self.called = False
```

---

### 758. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/tsl_pack_langs.py:42`
**Severity:** LOW
**Category:** quality

**Description:** Function 'main' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def main():
    # Path to the language definitions file
    lang_def_path = "../../tmp/tree-sitter-language-pack/sources/language_definitions.json"
```

---

### 759. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/openrouter.py:33`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    CACHE_TTL = 60 * 60 * 24  # 24 h

    def __init__(self) -> None:
        self.cache_dir = Path.home() / ".flacoai" / "caches"
        self.cache_file = self.cache_dir / "openrouter_models.json"
```

---

### 760. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/openrouter.py:29`
**Severity:** LOW
**Category:** quality

**Description:** Class 'OpenRouterModelManager' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class OpenRouterModelManager:
    MODELS_URL = "https://openrouter.ai/api/v1/models"
    CACHE_TTL = 60 * 60 * 24  # 24 h
```

---

### 761. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/udiff_coder.py:52`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_edits' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    gpt_prompts = UnifiedDiffPrompts()

    def get_edits(self):
        content = self.partial_response_content

```

---

### 762. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/udiff_coder.py:69`
**Severity:** LOW
**Category:** quality

**Description:** Function 'apply_edits' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return edits

    def apply_edits(self, edits):
        seen = set()
        uniq = []
```

---

### 763. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/udiff_coder.py:121`
**Severity:** LOW
**Category:** quality

**Description:** Function 'do_replace' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def do_replace(fname, content, hunk):
    fname = Path(fname)

```

---

### 764. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/udiff_coder.py:147`
**Severity:** LOW
**Category:** quality

**Description:** Function 'collapse_repeats' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def collapse_repeats(s):
    return "".join(k for k, g in groupby(s))

```

---

### 765. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/udiff_coder.py:151`
**Severity:** LOW
**Category:** quality

**Description:** Function 'apply_hunk' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def apply_hunk(content, hunk):
    before_text, after_text = hunk_to_before_after(hunk)

```

---

### 766. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/udiff_coder.py:201`
**Severity:** LOW
**Category:** quality

**Description:** Function 'flexi_just_search_and_replace' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def flexi_just_search_and_replace(texts):
    strategies = [
        (search_and_replace, all_preprocs),
```

---

### 767. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/udiff_coder.py:209`
**Severity:** LOW
**Category:** quality

**Description:** Function 'make_new_lines_explicit' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def make_new_lines_explicit(content, hunk):
    before, after = hunk_to_before_after(hunk)

```

---

### 768. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/udiff_coder.py:243`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cleanup_pure_whitespace_lines' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def cleanup_pure_whitespace_lines(lines):
    res = [
        line if line.strip() else line[-(len(line) - len(line.rstrip("\r\n")))] for line in lines
```

---

### 769. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/udiff_coder.py:250`
**Severity:** LOW
**Category:** quality

**Description:** Function 'normalize_hunk' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def normalize_hunk(hunk):
    before, after = hunk_to_before_after(hunk, lines=True)

```

---

### 770. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/udiff_coder.py:261`
**Severity:** LOW
**Category:** quality

**Description:** Function 'directly_apply_hunk' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def directly_apply_hunk(content, hunk):
    before, after = hunk_to_before_after(hunk)

```

---

### 771. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/udiff_coder.py:282`
**Severity:** LOW
**Category:** quality

**Description:** Function 'apply_partial_hunk' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def apply_partial_hunk(content, preceding_context, changes, following_context):
    len_prec = len(preceding_context)
    len_foll = len(following_context)
```

---

### 772. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/udiff_coder.py:312`
**Severity:** LOW
**Category:** quality

**Description:** Function 'find_diffs' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def find_diffs(content):
    # We can always fence with triple-quotes, because all the udiff content
    # is prefixed with +/-/space.
```

---

### 773. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/udiff_coder.py:337`
**Severity:** LOW
**Category:** quality

**Description:** Function 'process_fenced_block' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def process_fenced_block(lines, start_line_num):
    for line_num in range(start_line_num, len(lines)):
        line = lines[line_num]
```

---

### 774. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/udiff_coder.py:403`
**Severity:** LOW
**Category:** quality

**Description:** Function 'hunk_to_before_after' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def hunk_to_before_after(hunk, lines=False):
    before = []
    after = []
```

---

### 775. 🟢 Incomplete TODO Comment

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/udiff_coder.py:134`
**Severity:** LOW
**Category:** quality

**Description:** TODO comment lacks detailed description

**Recommendation:** Add description explaining what needs to be done and why

**Code:**
```

    # TODO: handle inserting into new file
    if not before_text.strip():
```

---

### 776. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editor_diff_fenced_prompts.py:6`
**Severity:** LOW
**Category:** quality

**Description:** Class 'EditorDiffFencedPrompts' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class EditorDiffFencedPrompts(EditBlockFencedPrompts):
    shell_cmd_prompt = ""
    no_shell_cmd_prompt = ""
```

---

### 777. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/editor_whole_coder.py:5`
**Severity:** LOW
**Category:** quality

**Description:** Class 'EditorWholeFileCoder' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class EditorWholeFileCoder(WholeFileCoder):
    "A coder that operates on entire files, focused purely on editing files."
    edit_format = "editor-whole"
```

---

### 778. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:14`
**Severity:** LOW
**Category:** quality

**Description:** Function 'has_been_reopened' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def has_been_reopened(issue_number):
    timeline_url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/issues/{issue_number}/timeline"
    response = requests.get(timeline_url, headers=headers)
```

---

### 779. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:72`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_issues' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def get_issues(state="open"):
    issues = []
    page = 1
```

---

### 780. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:104`
**Severity:** LOW
**Category:** quality

**Description:** Function 'group_issues_by_subject' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def group_issues_by_subject(issues):
    grouped_issues = defaultdict(list)
    pattern = r"Uncaught .+ in .+ line \d+"
```

---

### 781. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:114`
**Severity:** LOW
**Category:** quality

**Description:** Function 'find_oldest_issue' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def find_oldest_issue(subject, all_issues):
    oldest_issue = None
    oldest_date = datetime.now()
```

---

### 782. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:128`
**Severity:** LOW
**Category:** quality

**Description:** Function 'comment_and_close_duplicate' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def comment_and_close_duplicate(issue, oldest_issue):
    # Skip if issue is labeled as priority
    if "priority" in [label["name"] for label in issue["labels"]]:
```

---

### 783. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:152`
**Severity:** LOW
**Category:** quality

**Description:** Function 'find_unlabeled_with_paul_comments' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def find_unlabeled_with_paul_comments(issues):
    unlabeled_issues = []
    for issue in issues:
```

---

### 784. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:174`
**Severity:** LOW
**Category:** quality

**Description:** Function 'handle_unlabeled_issues' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def handle_unlabeled_issues(all_issues, auto_yes):
    print("\nFinding unlabeled issues with paul-gauthier comments...")
    unlabeled_issues = [
```

---

### 785. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:204`
**Severity:** LOW
**Category:** quality

**Description:** Function 'handle_stale_issues' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def handle_stale_issues(all_issues, auto_yes):
    print("\nChecking for stale question issues...")

```

---

### 786. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:249`
**Severity:** LOW
**Category:** quality

**Description:** Function 'handle_stale_closing' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def handle_stale_closing(all_issues, auto_yes):
    print("\nChecking for issues to close or unstale...")

```

---

### 787. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:335`
**Severity:** LOW
**Category:** quality

**Description:** Function 'handle_fixed_issues' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def handle_fixed_issues(all_issues, auto_yes):
    print("\nChecking for fixed enhancement and bug issues to close...")

```

---

### 788. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:397`
**Severity:** LOW
**Category:** quality

**Description:** Function 'handle_duplicate_issues' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def handle_duplicate_issues(all_issues, auto_yes):
    open_issues = [issue for issue in all_issues if issue["state"] == "open"]
    grouped_open_issues = group_issues_by_subject(open_issues)
```

---

### 789. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/issues.py:437`
**Severity:** LOW
**Category:** quality

**Description:** Function 'main' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def main():
    parser = argparse.ArgumentParser(description="Handle duplicate GitHub issues")
    parser.add_argument(
```

---

### 790. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:17`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

class IgnorantTemporaryDirectory:
    def __init__(self):
        if sys.version_info >= (3, 10):
            self.temp_dir = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
```

---

### 791. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:23`
**Severity:** LOW
**Category:** quality

**Description:** Function '__enter__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.temp_dir = tempfile.TemporaryDirectory()

    def __enter__(self):
        return self.temp_dir.__enter__()

```

---

### 792. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:26`
**Severity:** LOW
**Category:** quality

**Description:** Function '__exit__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return self.temp_dir.__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cleanup()

```

---

### 793. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:29`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cleanup' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.cleanup()

    def cleanup(self):
        try:
            self.temp_dir.cleanup()
```

---

### 794. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:35`
**Severity:** LOW
**Category:** quality

**Description:** Function '__getattr__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            pass  # Ignore errors (Windows and potential recursion)

    def __getattr__(self, item):
        return getattr(self.temp_dir, item)

```

---

### 795. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:40`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

class ChdirTemporaryDirectory(IgnorantTemporaryDirectory):
    def __init__(self):
        try:
            self.cwd = os.getcwd()
```

---

### 796. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:48`
**Severity:** LOW
**Category:** quality

**Description:** Function '__enter__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        super().__init__()

    def __enter__(self):
        res = super().__enter__()
        os.chdir(Path(self.temp_dir.name).resolve())
```

---

### 797. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:53`
**Severity:** LOW
**Category:** quality

**Description:** Function '__exit__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return res

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cwd:
            try:
```

---

### 798. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:63`
**Severity:** LOW
**Category:** quality

**Description:** Function '__enter__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

class GitTemporaryDirectory(ChdirTemporaryDirectory):
    def __enter__(self):
        dname = super().__enter__()
        self.repo = make_repo(dname)
```

---

### 799. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:68`
**Severity:** LOW
**Category:** quality

**Description:** Function '__exit__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return dname

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self.repo
        super().__exit__(exc_type, exc_val, exc_tb)
```

---

### 800. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:73`
**Severity:** LOW
**Category:** quality

**Description:** Function 'make_repo' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def make_repo(path=None):
    import git

```

---

### 801. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:96`
**Severity:** LOW
**Category:** quality

**Description:** Function 'safe_abs_path' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def safe_abs_path(res):
    "Gives an abs path, which safely returns a full (not 8.3) windows path"
    res = Path(res).resolve()
```

---

### 802. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:102`
**Severity:** LOW
**Category:** quality

**Description:** Function 'format_content' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def format_content(role, content):
    formatted_lines = []
    for line in content.splitlines():
```

---

### 803. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:109`
**Severity:** LOW
**Category:** quality

**Description:** Function 'format_messages' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def format_messages(messages, title=None):
    output = []
    if title:
```

---

### 804. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:137`
**Severity:** LOW
**Category:** quality

**Description:** Function 'show_messages' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def show_messages(messages, title=None, functions=None):
    formatted_output = format_messages(messages, title)
    print(formatted_output)
```

---

### 805. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:145`
**Severity:** LOW
**Category:** quality

**Description:** Function 'split_chat_history_markdown' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def split_chat_history_markdown(text, include_tool=False):
    messages = []
    user = []
```

---

### 806. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:152`
**Severity:** LOW
**Category:** quality

**Description:** Function 'append_msg' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    lines = text.splitlines(keepends=True)

    def append_msg(role, lines):
        lines = "".join(lines)
        if lines.strip():
```

---

### 807. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:196`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_pip_install' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def get_pip_install(args):
    cmd = [
        sys.executable,
```

---

### 808. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:210`
**Severity:** LOW
**Category:** quality

**Description:** Function 'run_install' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def run_install(cmd):
    print()
    print("Installing:", printable_shell_command(cmd))
```

---

### 809. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:260`
**Severity:** LOW
**Category:** quality

**Description:** Function 'find_common_root' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def find_common_root(abs_fnames):
    try:
        if len(abs_fnames) == 1:
```

---

### 810. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:276`
**Severity:** LOW
**Category:** quality

**Description:** Function 'format_tokens' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def format_tokens(count):
    if count < 1000:
        return f"{count}"
```

---

### 811. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:285`
**Severity:** LOW
**Category:** quality

**Description:** Function 'touch_file' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def touch_file(fname):
    fname = Path(fname)
    try:
```

---

### 812. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:295`
**Severity:** LOW
**Category:** quality

**Description:** Function 'check_pip_install_extra' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def check_pip_install_extra(io, module, prompt, pip_install_cmd, self_update=False):
    if module:
        try:
```

---

### 813. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:16`
**Severity:** LOW
**Category:** quality

**Description:** Class 'IgnorantTemporaryDirectory' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class IgnorantTemporaryDirectory:
    def __init__(self):
        if sys.version_info >= (3, 10):
```

---

### 814. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:39`
**Severity:** LOW
**Category:** quality

**Description:** Class 'ChdirTemporaryDirectory' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class ChdirTemporaryDirectory(IgnorantTemporaryDirectory):
    def __init__(self):
        try:
```

---

### 815. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/utils.py:62`
**Severity:** LOW
**Category:** quality

**Description:** Class 'GitTemporaryDirectory' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class GitTemporaryDirectory(ChdirTemporaryDirectory):
    def __enter__(self):
        dname = super().__enter__()
```

---

### 816. 🟢 Incomplete TODO Comment

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/template_engine.py:309`
**Severity:** LOW
**Category:** quality

**Description:** TODO comment lacks detailed description

**Recommendation:** Add description explaining what needs to be done and why

**Code:**
```

        # TODO: Parse prompt for custom tab names
        # For now, return defaults
```

---

### 817. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/scripts/homepage.py:530`
**Severity:** LOW
**Category:** quality

**Description:** Function 'main' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def main():
    # Load environment variables from .env file
    load_dotenv()
```

---

### 818. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_hig_analyzer.py:11`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    """Analyzes code for Apple HIG compliance."""

    def __init__(self, io=None, verbose=False):
        super().__init__(io, verbose)

```

---

### 819. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:31`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```

class SwitchCoder(Exception):
    def __init__(self, placeholder=None, **kwargs):
        self.kwargs = kwargs
        self.placeholder = placeholder
```

---

### 820. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:40`
**Severity:** LOW
**Category:** quality

**Description:** Function 'clone' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    scraper = None

    def clone(self):
        return Commands(
            self.io,
```

---

### 821. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:53`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        )

    def __init__(
        self,
        io,
```

---

### 822. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:95`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_model' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.used_commands.append(command_name)

    def cmd_model(self, args):
        "Switch the Main Model to a new LLM"

```

---

### 823. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:122`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_editor_model' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        raise SwitchCoder(main_model=model, edit_format=new_edit_format)

    def cmd_editor_model(self, args):
        "Switch the Editor Model to a new LLM"

```

---

### 824. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:134`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_weak_model' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        raise SwitchCoder(main_model=model)

    def cmd_weak_model(self, args):
        "Switch the Weak Model to a new LLM"

```

---

### 825. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:146`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_chat_mode' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        raise SwitchCoder(main_model=model)

    def cmd_chat_mode(self, args):
        "Switch to a new chat mode"

```

---

### 826. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:213`
**Severity:** LOW
**Category:** quality

**Description:** Function 'completions_model' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        )

    def completions_model(self):
        models = litellm.model_cost.keys()
        return models
```

---

### 827. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:217`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_models' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return models

    def cmd_models(self, args):
        "Search the list of available models"

```

---

### 828. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:227`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_web' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.io.tool_output("Please provide a partial model name to search for.")

    def cmd_web(self, args, return_content=False):
        "Scrape a webpage, convert to markdown and send in a message"

```

---

### 829. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:263`
**Severity:** LOW
**Category:** quality

**Description:** Function 'is_command' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        ]

    def is_command(self, inp):
        return inp[0] in "/!"

```

---

### 830. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:266`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_raw_completions' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return inp[0] in "/!"

    def get_raw_completions(self, cmd):
        assert cmd.startswith("/")
        cmd = cmd[1:]
```

---

### 831. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:274`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_completions' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return raw_completer

    def get_completions(self, cmd):
        assert cmd.startswith("/")
        cmd = cmd[1:]
```

---

### 832. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:284`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_commands' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return sorted(fun())

    def get_commands(self):
        commands = []
        for attr in dir(self):
```

---

### 833. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:295`
**Severity:** LOW
**Category:** quality

**Description:** Function 'do_run' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return commands

    def do_run(self, cmd_name, args):
        cmd_name = cmd_name.replace("-", "_")
        cmd_method_name = f"cmd_{cmd_name}"
```

---

### 834. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:308`
**Severity:** LOW
**Category:** quality

**Description:** Function 'matching_commands' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.io.tool_error(f"Unable to complete {cmd_name}: {err}")

    def matching_commands(self, inp):
        words = inp.strip().split()
        if not words:
```

---

### 835. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:320`
**Severity:** LOW
**Category:** quality

**Description:** Function 'run' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return matching_commands, first_word, rest_inp

    def run(self, inp):
        if inp.startswith("!"):
            self.coder.event("command_run")
```

---

### 836. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:345`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_commit' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    # each one must take an args param.

    def cmd_commit(self, args=None):
        "Commit edits to the repo made outside the chat (commit message optional)"
        try:
```

---

### 837. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:352`
**Severity:** LOW
**Category:** quality

**Description:** Function 'raw_cmd_commit' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.io.tool_error(f"Unable to complete commit: {err}")

    def raw_cmd_commit(self, args=None):
        if not self.coder.repo:
            self.io.tool_error("No git repository found.")
```

---

### 838. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:364`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_lint' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.coder.repo.commit(message=commit_message, coder=self.coder)

    def cmd_lint(self, args="", fnames=None):
        "Lint and fix in-chat files or all dirty files if none in chat"

```

---

### 839. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:419`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_clear' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.cmd_commit("")

    def cmd_clear(self, args):
        "Clear the chat history"

```

---

### 840. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:447`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_reset' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.coder.cur_messages = []

    def cmd_reset(self, args):
        "Drop all files and clear the chat history"
        self._drop_all_files()
```

---

### 841. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:453`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_tokens' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.io.tool_output("All files dropped and chat history cleared.")

    def cmd_tokens(self, args):
        "Report on the number of tokens used by the current chat context"

```

---

### 842. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:524`
**Severity:** LOW
**Category:** quality

**Description:** Function 'fmt' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        cost_width = 9

        def fmt(v):
            return format(int(v), ",").rjust(width)

```

---

### 843. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:561`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_undo' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.io.tool_output(f"{cost_pad}{fmt(limit)} tokens max context window size")

    def cmd_undo(self, args):
        "Undo the last git commit if it was done by flacoai"
        try:
```

---

### 844. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:568`
**Severity:** LOW
**Category:** quality

**Description:** Function 'raw_cmd_undo' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.io.tool_error(f"Unable to complete undo: {err}")

    def raw_cmd_undo(self, args):
        if not self.coder.repo:
            self.io.tool_error("No git repository found.")
```

---

### 845. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:665`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_diff' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            return prompts.undo_command_reply

    def cmd_diff(self, args=""):
        "Display the diff of changes since the last message"
        try:
```

---

### 846. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:672`
**Severity:** LOW
**Category:** quality

**Description:** Function 'raw_cmd_diff' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.io.tool_error(f"Unable to complete diff: {err}")

    def raw_cmd_diff(self, args=""):
        if not self.coder.repo:
            self.io.tool_error("No git repository found.")
```

---

### 847. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:705`
**Severity:** LOW
**Category:** quality

**Description:** Function 'quote_fname' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.io.print(diff)

    def quote_fname(self, fname):
        if " " in fname and '"' not in fname:
            fname = f'"{fname}"'
```

---

### 848. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:710`
**Severity:** LOW
**Category:** quality

**Description:** Function 'completions_raw_read_only' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return fname

    def completions_raw_read_only(self, document, complete_event):
        # Get the text before the cursor
        text = document.text_before_cursor
```

---

### 849. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:720`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_paths' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        new_document = Document(after_command, cursor_position=len(after_command))

        def get_paths():
            return [self.coder.root] if self.coder.root else None

```

---

### 850. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:767`
**Severity:** LOW
**Category:** quality

**Description:** Function 'completions_add' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            yield completion

    def completions_add(self):
        files = set(self.coder.get_all_relative_files())
        files = files - set(self.coder.get_inchat_relative_files())
```

---

### 851. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:773`
**Severity:** LOW
**Category:** quality

**Description:** Function 'glob_filtered_to_repo' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return files

    def glob_filtered_to_repo(self, pattern):
        if not pattern.strip():
            return []
```

---

### 852. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:807`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_add' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return res

    def cmd_add(self, args):
        "Add files to the chat so flacoai can edit them or review them in detail"

```

---

### 853. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:903`
**Severity:** LOW
**Category:** quality

**Description:** Function 'completions_drop' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
                    self.coder.check_added_files()

    def completions_drop(self):
        files = self.coder.get_inchat_relative_files()
        read_only_files = [self.coder.get_rel_fname(fn) for fn in self.coder.abs_read_only_fnames]
```

---

### 854. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:910`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_drop' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return all_files

    def cmd_drop(self, args=""):
        "Remove files from the chat session to free up context space"

```

---

### 855. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:965`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_git' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
                    self.io.tool_output(f"Removed {matched_file} from the chat")

    def cmd_git(self, args):
        "Run a git command (output excluded from chat)"
        combined_output = None
```

---

### 856. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:991`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_test' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.io.tool_output(combined_output)

    def cmd_test(self, args):
        "Run a shell command and add the output to the chat on non-zero exit code"
        if not args and self.coder.test_cmd:
```

---

### 857. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1011`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_run' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return errors

    def cmd_run(self, args, add_on_nonzero_exit=False):
        "Run a shell command and optionally add the output to the chat (alias: !)"
        exit_status, combined_output = run_cmd(
```

---

### 858. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1053`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_exit' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return None

    def cmd_exit(self, args):
        "Exit the application"
        self.coder.event("exit", reason="/exit")
```

---

### 859. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1058`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_quit' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        sys.exit()

    def cmd_quit(self, args):
        "Exit the application"
        self.cmd_exit(args)
```

---

### 860. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1062`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_ls' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.cmd_exit(args)

    def cmd_ls(self, args):
        "List all known files and indicate which are included in the chat session"

```

---

### 861. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1101`
**Severity:** LOW
**Category:** quality

**Description:** Function 'basic_help' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.io.tool_output(f"  {file}")

    def basic_help(self):
        commands = sorted(self.get_commands())
        pad = max(len(cmd) for cmd in commands)
```

---

### 862. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1117`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_help' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.io.tool_output("Use `/help <question>` to ask questions about how to use flacoai.")

    def cmd_help(self, args):
        "Ask questions about flacoai"

```

---

### 863. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1168`
**Severity:** LOW
**Category:** quality

**Description:** Function 'completions_ask' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        )

    def completions_ask(self):
        raise CommandCompletionException()

```

---

### 864. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1171`
**Severity:** LOW
**Category:** quality

**Description:** Function 'completions_code' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        raise CommandCompletionException()

    def completions_code(self):
        raise CommandCompletionException()

```

---

### 865. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1242`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_voice' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return res

    def cmd_voice(self, args):
        "Record and transcribe voice input"

```

---

### 866. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1318`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_read_only' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.io.tool_error(f"Error processing clipboard content: {e}")

    def cmd_read_only(self, args):
        "Add files to the chat that are for reference only, or turn added files to read-only"
        if not args.strip():
```

---

### 867. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1408`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_map' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.io.tool_output(f"No new files added from directory {original_name}.")

    def cmd_map(self, args):
        "Print out the current repository map"
        repo_map = self.coder.get_repo_map()
```

---

### 868. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:1416`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_map_refresh' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.io.tool_output("No repository map available.")

    def cmd_map_refresh(self, args):
        "Force a refresh of the repository map"
        repo_map = self.coder.get_repo_map(force_refresh=True)
```

---

### 869. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3211`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_settings' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.io.tool_error(f"Error generating tour: {e}")

    def cmd_settings(self, args):
        "Print out the current settings"
        settings = format_settings(self.parser, self.args)
```

---

### 870. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3241`
**Severity:** LOW
**Category:** quality

**Description:** Function 'completions_raw_load' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.io.tool_output(output)

    def completions_raw_load(self, document, complete_event):
        return self.completions_raw_read_only(document, complete_event)

```

---

### 871. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3244`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_load' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return self.completions_raw_read_only(document, complete_event)

    def cmd_load(self, args):
        "Load and execute commands from a file"
        if not args.strip():
```

---

### 872. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3273`
**Severity:** LOW
**Category:** quality

**Description:** Function 'completions_raw_save' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
                )

    def completions_raw_save(self, document, complete_event):
        return self.completions_raw_read_only(document, complete_event)

```

---

### 873. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3276`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_save' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        return self.completions_raw_read_only(document, complete_event)

    def cmd_save(self, args):
        "Save commands to a file that can reconstruct the current chat session's files"
        if not args.strip():
```

---

### 874. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3303`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_multiline_mode' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.io.tool_error(f"Error saving commands to file: {e}")

    def cmd_multiline_mode(self, args):
        "Toggle multiline mode (swaps behavior of Enter and Meta+Enter)"
        self.io.toggle_multiline_mode()
```

---

### 875. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3307`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_copy' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.io.toggle_multiline_mode()

    def cmd_copy(self, args):
        "Copy the last assistant message to the clipboard"
        all_messages = self.coder.done_messages + self.coder.cur_messages
```

---

### 876. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3334`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_report' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
            self.io.tool_error(f"An unexpected error occurred while copying to clipboard: {str(e)}")

    def cmd_report(self, args):
        "Report a problem by opening a GitHub Issue"
        from flacoai.report import report_github_issue
```

---

### 877. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3348`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_editor' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        report_github_issue(issue_text, title=title, confirm=False)

    def cmd_editor(self, initial_content=""):
        "Open an editor to write a prompt"

```

---

### 878. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3394`
**Severity:** LOW
**Category:** quality

**Description:** Function 'cmd_reasoning_effort' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.io.tool_output(announcements)

    def cmd_reasoning_effort(self, args):
        "Set the reasoning effort level (values: number or low/medium/high depending on model)"
        model = self.coder.main_model
```

---

### 879. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3462`
**Severity:** LOW
**Category:** quality

**Description:** Function 'expand_subdir' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def expand_subdir(file_path):
    if file_path.is_file():
        yield file_path
```

---

### 880. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3473`
**Severity:** LOW
**Category:** quality

**Description:** Function 'parse_quoted_filenames' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def parse_quoted_filenames(args):
    filenames = re.findall(r"\"(.+?)\"|(\S+)", args)
    filenames = [name for sublist in filenames for name in sublist if name]
```

---

### 881. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3479`
**Severity:** LOW
**Category:** quality

**Description:** Function 'get_help_md' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def get_help_md():
    md = Commands(None, None).get_help_md()
    return md
```

---

### 882. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:3484`
**Severity:** LOW
**Category:** quality

**Description:** Function 'main' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def main():
    md = get_help_md()
    print(md)
```

---

### 883. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:30`
**Severity:** LOW
**Category:** quality

**Description:** Class 'SwitchCoder' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class SwitchCoder(Exception):
    def __init__(self, placeholder=None, **kwargs):
        self.kwargs = kwargs
```

---

### 884. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/commands.py:36`
**Severity:** LOW
**Category:** quality

**Description:** Class 'Commands' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```


class Commands:
    voice = None
    scraper = None
```

---

### 885. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/coders/review_coder.py:18`
**Severity:** LOW
**Category:** quality

**Description:** Function 'run_static_analysis' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
        self.review_results = []

    def run_static_analysis(self, files_to_analyze=None, enable_security=True,
                           enable_performance=True, enable_quality=True,
                           enable_architecture=True, enable_ios=True):
```

---

### 886. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/spm_analyzer.py:11`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    """Analyzes Swift Package Manager dependencies and configuration."""

    def __init__(self, io=None, verbose=False):
        super().__init__(io, verbose)

```

---

### 887. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_version_analyzer.py:11`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    """Analyzes code for iOS version compatibility and deprecated APIs."""

    def __init__(self, io=None, verbose=False):
        super().__init__(io, verbose)

```

---

### 888. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:11`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    """Analyzes SwiftUI code for best practices and common patterns."""

    def __init__(self, io=None, verbose=False):
        super().__init__(io, verbose)

```

---

### 889. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/swiftui_analyzer.py:121`
**Severity:** LOW
**Category:** quality

**Description:** Class 'instance' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```
                    category=Category.QUALITY,
                    title="@State with Reference Type",
                    description="Using @State with a class instance",
                    recommendation="Use @StateObject for classes, @State for value types only",
                    code_snippet=code_snippet,
```

---

### 890. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/performance_analyzer.py:11`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    """Analyzes code for performance issues and anti-patterns."""

    def __init__(self, io=None, verbose=False):
        super().__init__(io, verbose)

```

---

### 891. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/ios_plist_analyzer.py:12`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    """Analyzes Info.plist files for security and configuration issues."""

    def __init__(self, io=None, verbose=False):
        super().__init__(io, verbose)

```

---

### 892. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/branding.py:240`
**Severity:** LOW
**Category:** quality

**Description:** Function 'format_compact_header' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```


def format_compact_header(model_name, edit_format, directory, branch=None, file_count=0,
                         thinking_tokens=None, reasoning_effort=None, cache_enabled=False,
                         infinite_output=False, repo_map_tokens=None, repo_map_refresh=None):
```

---

### 893. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:11`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    """Analyzes code quality, code smells, and maintainability."""

    def __init__(self, io=None, verbose=False):
        super().__init__(io, verbose)

```

---

### 894. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:49`
**Severity:** LOW
**Category:** quality

**Description:** Class 'name' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```
            (r'\b[a-z]\b\s*=', "Single letter variable"),
            (r'def\s+[a-z]{1,2}\(', "Short function name"),
            (r'class\s+[a-z]', "Lowercase class name"),
        ]

```

---

### 895. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/quality_analyzer.py:77`
**Severity:** LOW
**Category:** quality

**Description:** Class 'should' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```

        self.ios_naming_patterns = [
            (r'class\s+[a-z]', "Swift class should start with uppercase"),
            (r'struct\s+[a-z]', "Swift struct should start with uppercase"),
            (r'enum\s+[a-z]', "Swift enum should start with uppercase"),
```

---

### 896. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/documentation_analyzer.py:11`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    """Analyzes code for documentation coverage and quality."""

    def __init__(self, io=None, verbose=False):
        super().__init__(io, verbose)

```

---

### 897. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/documentation_analyzer.py:120`
**Severity:** LOW
**Category:** quality

**Description:** Class 'definitions' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```
        results = []

        # Find function/class definitions
        patterns = [
            (r'def\s+(\w+)\s*\(', 'function'),
```

---

### 898. 🟢 Missing Docstring for Function

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:12`
**Severity:** LOW
**Category:** quality

**Description:** Function '__init__' lacks docstring

**Recommendation:** Add docstring explaining the function's purpose, parameters, and return value

**Code:**
```
    """Analyzes code architecture, dependencies, and design patterns."""

    def __init__(self, io=None, verbose=False):
        super().__init__(io, verbose)
        self.import_graph: Dict[str, Set[str]] = defaultdict(set)
```

---

### 899. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:148`
**Severity:** LOW
**Category:** quality

**Description:** Class 'end' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```
            class_start = match.start()

            # Find class end (next class or end of file)
            next_class = None
            for other_match in matches:
```

---

### 900. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:148`
**Severity:** LOW
**Category:** quality

**Description:** Class 'or' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```
            class_start = match.start()

            # Find class end (next class or end of file)
            next_class = None
            for other_match in matches:
```

---

### 901. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:164`
**Severity:** LOW
**Category:** quality

**Description:** Class 'indicators' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```
            line_count = len(class_content.split('\n'))

            # God class indicators
            if method_count > 20 or line_count > 500:
                line_num = content[:class_start].count('\n') + 1
```

---

### 902. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:350`
**Severity:** LOW
**Category:** quality

**Description:** Class 'end' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```
            vc_start = match.start()

            # Find class end (next class or end of file)
            next_class = None
            for other_match in matches:
```

---

### 903. 🟢 Missing Docstring for Class

**Location:** `/Users/roura.io/Documents/dev/work/flaco/flaco.cli/flacoai/flacoai/analyzers/architecture_analyzer.py:350`
**Severity:** LOW
**Category:** quality

**Description:** Class 'or' lacks docstring

**Recommendation:** Add docstring explaining the class's purpose, parameters, and return value

**Code:**
```
            vc_start = match.start()

            # Find class end (next class or end of file)
            next_class = None
            for other_match in matches:
```

---


---
*Report generated by FlacoAI - Analyzed 100 files in 0.00s*