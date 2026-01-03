"""Interactive fix applicator for code review findings."""

import re
from typing import List, Optional
from pathlib import Path


class FixApplicator:
    """Apply fixes for code review findings interactively."""

    def __init__(self, io=None):
        """Initialize fix applicator.

        Args:
            io: IO object for output and input
        """
        self.io = io
        self.fixes_applied = 0
        self.fixes_skipped = 0

    def apply_fixes(self, results: List, auto_fix_safe: bool = False) -> dict:
        """Apply fixes interactively.

        Args:
            results: List of AnalysisResult objects
            auto_fix_safe: Auto-apply safe fixes without prompting

        Returns:
            Dict with stats on fixes applied
        """
        # Group fixes by file
        fixes_by_file = {}
        for result in results:
            if not hasattr(result, 'auto_fix') or not result.auto_fix:
                continue  # Skip if no auto-fix available

            if result.file not in fixes_by_file:
                fixes_by_file[result.file] = []
            fixes_by_file[result.file].append(result)

        if not fixes_by_file:
            if self.io:
                self.io.tool_output("No auto-fixable issues found")
            return {"applied": 0, "skipped": 0}

        # Apply fixes file by file
        for file_path, file_fixes in fixes_by_file.items():
            self._apply_fixes_to_file(file_path, file_fixes, auto_fix_safe)

        return {
            "applied": self.fixes_applied,
            "skipped": self.fixes_skipped,
        }

    def _apply_fixes_to_file(self, file_path: str, fixes: List, auto_fix_safe: bool):
        """Apply fixes to a single file.

        Args:
            file_path: Path to file
            fixes: List of fixes for this file
            auto_fix_safe: Auto-apply safe fixes
        """
        try:
            with open(file_path, 'r') as f:
                content = f.read()
                lines = content.splitlines(keepends=True)

        except Exception as e:
            if self.io:
                self.io.tool_error(f"Failed to read {file_path}: {e}")
            return

        # Sort fixes by line number (descending) to avoid line number shifts
        fixes_sorted = sorted(fixes, key=lambda x: x.line, reverse=True)

        modified = False

        for fix in fixes_sorted:
            if auto_fix_safe and not self._is_safe_fix(fix):
                self.fixes_skipped += 1
                continue

            # Show fix to user
            if self.io:
                self.io.tool_output(f"\n{'='*60}")
                self.io.tool_output(f"File: {file_path}:{fix.line}")
                self.io.tool_output(f"Issue: {fix.title} [{fix.severity.value.upper()}]")
                self.io.tool_output(f"Fix: {fix.recommendation}")

                # Show before/after
                if fix.code_snippet:
                    self.io.tool_output(f"\nBefore:")
                    self.io.tool_output(fix.code_snippet)

                if hasattr(fix, 'fixed_code') and fix.fixed_code:
                    self.io.tool_output(f"\nAfter:")
                    self.io.tool_output(fix.fixed_code)

            # Prompt user (unless auto-fix mode)
            if auto_fix_safe:
                apply = True
            else:
                if self.io:
                    response = self.io.prompt_ask("Apply this fix? [y/n/q] ")
                    apply = response.lower() in ['y', 'yes']
                    if response.lower() in ['q', 'quit']:
                        break
                else:
                    apply = False

            if apply:
                # Apply the fix
                if hasattr(fix, 'fixed_code') and fix.fixed_code:
                    # Line-based replacement
                    line_idx = fix.line - 1
                    if 0 <= line_idx < len(lines):
                        lines[line_idx] = fix.fixed_code + '\n'
                        modified = True
                        self.fixes_applied += 1

                        if self.io:
                            self.io.tool_output("✓ Fix applied")
                    else:
                        if self.io:
                            self.io.tool_error(f"Invalid line number: {fix.line}")
                        self.fixes_skipped += 1
                else:
                    if self.io:
                        self.io.tool_error("No fix code available")
                    self.fixes_skipped += 1
            else:
                self.fixes_skipped += 1
                if self.io:
                    self.io.tool_output("⊘ Fix skipped")

        # Write modified file
        if modified:
            try:
                with open(file_path, 'w') as f:
                    f.writelines(lines)

                if self.io:
                    self.io.tool_output(f"\n✓ Updated {file_path}")

            except Exception as e:
                if self.io:
                    self.io.tool_error(f"Failed to write {file_path}: {e}")

    def _is_safe_fix(self, fix) -> bool:
        """Check if a fix is safe to auto-apply.

        Args:
            fix: AnalysisResult object

        Returns:
            True if fix is considered safe
        """
        # Safe fixes are low-risk changes
        safe_categories = ["documentation", "style", "formatting"]
        safe_severities = ["low"]

        return (
            fix.category.value.lower() in safe_categories or
            fix.severity.value.lower() in safe_severities
        )

    def generate_auto_fixes(self, results: List) -> List:
        """Generate automatic fixes for common issues.

        Args:
            results: List of AnalysisResult objects

        Returns:
            Results with auto_fix and fixed_code fields added
        """
        for result in results:
            # Add auto-fix logic for common patterns
            if "force unwrap" in result.title.lower():
                result.auto_fix = True
                result.fixed_code = self._fix_force_unwrap(result)

            elif "weak self" in result.title.lower():
                result.auto_fix = True
                result.fixed_code = self._fix_weak_self(result)

            elif "deprecated" in result.title.lower():
                result.auto_fix = self._can_fix_deprecated(result)
                if result.auto_fix:
                    result.fixed_code = self._fix_deprecated(result)

            else:
                result.auto_fix = False

        return results

    def _fix_force_unwrap(self, result) -> Optional[str]:
        """Generate fix for force unwrapping.

        Args:
            result: AnalysisResult

        Returns:
            Fixed code or None
        """
        if not result.code_snippet:
            return None

        # Replace ! with ?? or optional binding suggestion
        code = result.code_snippet.strip()

        # Simple replacement: ! -> ?
        fixed = code.replace('!', '?')

        return fixed

    def _fix_weak_self(self, result) -> Optional[str]:
        """Generate fix for missing [weak self].

        Args:
            result: AnalysisResult

        Returns:
            Fixed code or None
        """
        if not result.code_snippet:
            return None

        code = result.code_snippet.strip()

        # Find closure pattern and add [weak self]
        if '{' in code and 'in' in code:
            # Insert [weak self] after {
            fixed = re.sub(r'\{(\s*)', r'{ [weak self] \1', code, count=1)
            return fixed

        return None

    def _can_fix_deprecated(self, result) -> bool:
        """Check if deprecated API can be auto-fixed.

        Args:
            result: AnalysisResult

        Returns:
            True if can be auto-fixed
        """
        # Check if recommendation contains a simple replacement
        if result.recommendation and "Use " in result.recommendation:
            return True
        return False

    def _fix_deprecated(self, result) -> Optional[str]:
        """Generate fix for deprecated API.

        Args:
            result: AnalysisResult

        Returns:
            Fixed code or None
        """
        if not result.code_snippet or not result.recommendation:
            return None

        # Extract replacement from recommendation
        # "Use UIAlertController instead" -> UIAlertController
        match = re.search(r'Use (\w+)', result.recommendation)
        if match:
            replacement = match.group(1)
            code = result.code_snippet.strip()

            # Find deprecated term in code and replace
            for word in code.split():
                if word.replace('(', '').replace(')', '') in result.title:
                    fixed = code.replace(word, replacement)
                    return fixed

        return None
