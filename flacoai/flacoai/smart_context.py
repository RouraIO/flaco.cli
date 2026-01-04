"""Smart context loading for automatic file detection."""

import os
import re
from pathlib import Path
from typing import Set, List, Optional


class SmartContextLoader:
    """Intelligently load relevant files for code review."""

    # Directories to always skip
    SKIP_DIRS = {
        '.git', '.svn', '.hg',
        'node_modules', 'bower_components',
        '__pycache__', '.pytest_cache', '.mypy_cache',
        'venv', 'env', '.venv', '.env',
        'dist', 'build', 'target',
        '.idea', '.vscode', '.vs',
        'Pods', 'Carthage',
        'DerivedData',
        '.build',
    }

    # Files to always skip
    SKIP_FILES = {
        '.DS_Store',
        'package-lock.json',
        'yarn.lock',
        'Podfile.lock',
        'Cartfile.resolved',
        '*.pbxproj',  # Xcode project files (binary-ish)
        '*.xcworkspacedata',
        '*.xcuserdata',
    }

    # Generated file patterns
    GENERATED_PATTERNS = [
        r'\.generated\.',
        r'\.g\.',
        r'\.pb\.',  # Protobuf
        r'\.grpc\.',  # gRPC
        r'_generated',
        r'generated_',
        r'\.bundle\.',  # Webpack bundles
        r'\.min\.',  # Minified files
    ]

    # Code file extensions (what to include)
    CODE_EXTENSIONS = {
        # iOS/Swift
        'swift', 'h', 'm', 'mm',
        # General
        'py', 'js', 'ts', 'jsx', 'tsx',
        'java', 'kt', 'kts',
        'rb', 'go', 'rs',
        'php', 'cs', 'cpp', 'c', 'hpp',
        'scala', 'clj', 'ex', 'exs',
        # Web
        'vue', 'svelte',
        'html', 'htm', 'css', 'scss', 'sass',
        # Scripts
        'sh', 'bash', 'zsh',
        'sql',
        # Config (sometimes has logic)
        'yml', 'yaml',
    }

    def __init__(self, project_root: str, io=None):
        """Initialize smart context loader.

        Args:
            project_root: Root directory of project
            io: IO object for output
        """
        self.project_root = Path(project_root)
        self.io = io

    def get_relevant_files(
        self,
        focus_files: Optional[List[str]] = None,
        include_tests: bool = True,
        max_files: int = 100
    ) -> Set[str]:
        """Get relevant files for review.

        Args:
            focus_files: Optional list of files to focus on
            include_tests: Whether to include test files
            max_files: Maximum number of files to return

        Returns:
            Set of absolute file paths
        """
        relevant_files = set()

        if focus_files:
            # Mode 1: Expand from focus files
            for file_path in focus_files:
                relevant_files.add(os.path.abspath(file_path))

                # Find related files (imports, dependencies)
                related = self._find_related_files(file_path)
                relevant_files.update(related)

        else:
            # Mode 2: Auto-discover all code files
            relevant_files = self._discover_code_files(include_tests)

        # Filter out generated files
        relevant_files = {
            f for f in relevant_files
            if not self._is_generated(f)
        }

        # Limit to max_files (prioritize by git changes if available)
        if len(relevant_files) > max_files:
            relevant_files = self._prioritize_files(relevant_files, max_files)

        return relevant_files

    def _discover_code_files(self, include_tests: bool) -> Set[str]:
        """Discover all code files in project.

        Args:
            include_tests: Whether to include test files

        Returns:
            Set of file paths
        """
        code_files = set()

        for root, dirs, files in os.walk(self.project_root):
            # Skip directories in SKIP_DIRS
            dirs[:] = [d for d in dirs if d not in self.SKIP_DIRS]

            for file in files:
                # Check extension
                ext = Path(file).suffix.lstrip('.').lower()
                if ext not in self.CODE_EXTENSIONS:
                    continue

                # Skip test files if requested
                if not include_tests and self._is_test_file(file):
                    continue

                # Skip files in SKIP_FILES
                if file in self.SKIP_FILES:
                    continue

                full_path = os.path.join(root, file)
                code_files.add(os.path.abspath(full_path))

        return code_files

    def _find_related_files(self, file_path: str) -> Set[str]:
        """Find files related to the given file through imports.

        Args:
            file_path: Path to file

        Returns:
            Set of related file paths
        """
        related = set()

        try:
            with open(file_path, 'r') as f:
                content = f.read()

            # Extract import/include statements
            imports = self._extract_imports(content, file_path)

            # Resolve imports to file paths
            for imp in imports:
                resolved = self._resolve_import(imp, file_path)
                if resolved:
                    related.add(resolved)

        except Exception as e:
            if self.io and self.io.verbose:
                self.io.tool_error(f"Error reading {file_path}: {e}")

        return related

    def _extract_imports(self, content: str, file_path: str) -> List[str]:
        """Extract import statements from file content.

        Args:
            content: File content
            file_path: Path to file (for language detection)

        Returns:
            List of import strings
        """
        imports = []
        ext = Path(file_path).suffix.lower()

        if ext == '.swift':
            # Swift imports
            imports.extend(re.findall(r'import\s+([\w\.]+)', content))

        elif ext == '.py':
            # Python imports
            imports.extend(re.findall(r'from\s+([\w\.]+)\s+import', content))
            imports.extend(re.findall(r'import\s+([\w\.]+)', content))

        elif ext in ['.js', '.ts', '.jsx', '.tsx']:
            # JavaScript/TypeScript imports
            imports.extend(re.findall(r'from\s+[\'"]([^\'"]+)[\'"]', content))
            imports.extend(re.findall(r'require\([\'"]([^\'"]+)[\'"]\)', content))

        elif ext in ['.m', '.mm', '.h']:
            # Objective-C imports
            imports.extend(re.findall(r'#import\s+[<"]([^>"]+)[>"]', content))

        return imports

    def _resolve_import(self, import_str: str, from_file: str) -> Optional[str]:
        """Resolve import string to file path.

        Args:
            import_str: Import string (e.g., "MyModule" or "./utils")
            from_file: File making the import

        Returns:
            Resolved file path or None
        """
        from_dir = Path(from_file).parent

        # Handle relative imports
        if import_str.startswith('.'):
            # Relative path import
            candidate = (from_dir / import_str).resolve()

            # Try with various extensions
            for ext in self.CODE_EXTENSIONS:
                full_path = candidate.with_suffix(f'.{ext}')
                if full_path.exists():
                    return str(full_path)

        else:
            # Absolute/module import - search project
            # Convert module name to file path (e.g., "App.Views.Login" -> "App/Views/Login.swift")
            path_parts = import_str.split('.')
            base_name = path_parts[-1]

            # Search for file with this name
            for root, dirs, files in os.walk(self.project_root):
                dirs[:] = [d for d in dirs if d not in self.SKIP_DIRS]

                for file in files:
                    if Path(file).stem == base_name:
                        return os.path.abspath(os.path.join(root, file))

        return None

    def _is_generated(self, file_path: str) -> bool:
        """Check if file is generated/auto-generated.

        Args:
            file_path: Path to file

        Returns:
            True if file appears to be generated
        """
        file_name = Path(file_path).name

        # Check against patterns
        for pattern in self.GENERATED_PATTERNS:
            if re.search(pattern, file_name, re.IGNORECASE):
                return True

        # Check file content for generation markers
        try:
            with open(file_path, 'r') as f:
                # Read first few lines
                head = ''.join([next(f) for _ in range(min(10, sum(1 for _ in f)))])

                # Common generation markers
                generation_markers = [
                    'auto-generated',
                    'autogenerated',
                    'do not edit',
                    'do not modify',
                    'generated by',
                    'code generator',
                    '@generated',
                ]

                head_lower = head.lower()
                for marker in generation_markers:
                    if marker in head_lower:
                        return True

        except Exception:
            pass

        return False

    def _is_test_file(self, file_name: str) -> bool:
        """Check if file is a test file.

        Args:
            file_name: Name of file

        Returns:
            True if file is a test
        """
        test_patterns = [
            r'test_',
            r'_test\.',
            r'\.test\.',
            r'\.spec\.',
            r'Tests\.',
            r'Spec\.',
        ]

        for pattern in test_patterns:
            if re.search(pattern, file_name, re.IGNORECASE):
                return True

        return False

    def _prioritize_files(self, files: Set[str], max_files: int) -> Set[str]:
        """Prioritize files when limiting to max_files.

        Prioritizes:
        1. Recently changed files (git)
        2. Smaller files
        3. Non-test files

        Args:
            files: Set of file paths
            max_files: Maximum number to return

        Returns:
            Prioritized subset of files
        """
        import subprocess

        # Try to get recently changed files from git
        try:
            result = subprocess.run(
                ['git', 'diff', '--name-only', 'HEAD~10..HEAD'],
                cwd=self.project_root,
                capture_output=True,
                text=True,
                check=False
            )

            if result.returncode == 0:
                changed_files = set(
                    os.path.abspath(os.path.join(self.project_root, f.strip()))
                    for f in result.stdout.splitlines()
                )

                # Prioritize changed files
                prioritized = list(files & changed_files)
                remaining = list(files - changed_files)

                # Fill up to max_files
                prioritized.extend(remaining[:max_files - len(prioritized)])

                return set(prioritized[:max_files])

        except Exception:
            pass

        # Fallback: just take first max_files
        return set(list(files)[:max_files])
