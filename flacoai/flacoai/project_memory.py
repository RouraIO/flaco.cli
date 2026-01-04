"""Project memory system for FlacoAI - Swift/iOS project understanding."""

import os
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple


class ProjectScanner:
    """Scans Swift/iOS projects and generates project memory."""

    SWIFT_IOS_MARKERS = {
        'xcode_project': ['.xcodeproj', '.xcworkspace'],
        'swift_package': ['Package.swift'],
        'source_dirs': ['Sources/', 'src/', 'Source/'],
        'test_dirs': ['Tests/', 'test/', 'Test/'],
        'config_files': ['project.yml', 'Podfile', 'Cartfile', '.swiftlint.yml'],
        'build_files': ['Makefile', 'build.sh', 'fastlane/'],
    }

    MEMORY_FILE = 'FlacoAI.md'

    # Markers for manual sections that should be preserved
    MANUAL_SECTION_START = '<!-- MANUAL SECTION START -->'
    MANUAL_SECTION_END = '<!-- MANUAL SECTION END -->'

    def __init__(self, repo_root: str):
        """Initialize scanner with repository root.

        Args:
            repo_root: Path to repository root directory
        """
        self.repo_root = Path(repo_root)
        self.memory_path = self.repo_root / self.MEMORY_FILE

    def detect_project_type(self) -> Dict[str, bool]:
        """Detect what type of Swift/iOS project this is.

        Returns:
            Dictionary with detected project features
        """
        detected = {
            'is_xcode_project': False,
            'is_swift_package': False,
            'has_tests': False,
            'uses_pods': False,
            'uses_carthage': False,
            'uses_swiftlint': False,
            'uses_fastlane': False,
        }

        # Check for Xcode project/workspace
        for item in self.repo_root.rglob('*'):
            if item.suffix in ['.xcodeproj', '.xcworkspace']:
                detected['is_xcode_project'] = True
                break

        # Check for Swift Package
        if (self.repo_root / 'Package.swift').exists():
            detected['is_swift_package'] = True

        # Check for test directories
        for test_dir in ['Tests', 'test', 'Test', 'UnitTests']:
            if (self.repo_root / test_dir).exists():
                detected['has_tests'] = True
                break

        # Check for dependency managers
        detected['uses_pods'] = (self.repo_root / 'Podfile').exists()
        detected['uses_carthage'] = (self.repo_root / 'Cartfile').exists()

        # Check for tools
        detected['uses_swiftlint'] = (self.repo_root / '.swiftlint.yml').exists()
        detected['uses_fastlane'] = (self.repo_root / 'fastlane').exists()

        return detected

    def scan_directory_structure(self, max_depth: int = 3) -> List[str]:
        """Scan and return directory structure.

        Args:
            max_depth: Maximum directory depth to scan

        Returns:
            List of directory paths (relative to root)
        """
        dirs = []

        def should_skip(path: Path) -> bool:
            """Check if directory should be skipped."""
            skip_patterns = [
                '.git', '.build', 'build', 'DerivedData',
                'Pods', 'Carthage', '.swiftpm', 'node_modules',
                '__pycache__', '.pytest_cache', 'venv', '.venv'
            ]
            return any(pattern in path.parts for pattern in skip_patterns)

        for root, dirnames, _ in os.walk(self.repo_root):
            path = Path(root)
            depth = len(path.relative_to(self.repo_root).parts)

            if depth > max_depth or should_skip(path):
                dirnames.clear()  # Don't recurse
                continue

            rel_path = path.relative_to(self.repo_root)
            if rel_path != Path('.'):
                dirs.append(str(rel_path))

        return sorted(dirs)

    def detect_architecture_patterns(self) -> List[str]:
        """Detect common architecture patterns in Swift code.

        Returns:
            List of detected patterns (MVVM, MVC, VIPER, etc.)
        """
        patterns = []

        # Search for common architecture indicators
        architecture_markers = {
            'MVVM': ['ViewModel', 'ViewModeling'],
            'MVC': ['ViewController', 'Controller'],
            'VIPER': ['Interactor', 'Presenter', 'Router'],
            'Redux': ['Store', 'Reducer', 'Action'],
            'Coordinator': ['Coordinator', 'Coordinating'],
            'Clean Architecture': ['UseCase', 'Repository', 'Entity'],
        }

        for pattern_name, markers in architecture_markers.items():
            for swift_file in self.repo_root.rglob('*.swift'):
                if any(marker in swift_file.name for marker in markers):
                    if pattern_name not in patterns:
                        patterns.append(pattern_name)
                    break

        return patterns

    def extract_existing_manual_sections(self) -> Dict[str, str]:
        """Extract manually edited sections from existing FlacoAI.md.

        Returns:
            Dictionary mapping section names to their content
        """
        manual_sections = {}

        if not self.memory_path.exists():
            return manual_sections

        try:
            content = self.memory_path.read_text(encoding='utf-8')

            # Find all manual sections
            pattern = rf'{self.MANUAL_SECTION_START}\n## (.+?)\n(.*?){self.MANUAL_SECTION_END}'
            matches = re.finditer(pattern, content, re.DOTALL)

            for match in matches:
                section_name = match.group(1).strip()
                section_content = match.group(2).strip()
                manual_sections[section_name] = section_content

        except Exception as e:
            print(f"Warning: Could not parse existing {self.MEMORY_FILE}: {e}")

        return manual_sections

    def generate_memory_file(self, force: bool = False) -> Tuple[str, bool]:
        """Generate or update FlacoAI.md project memory file.

        Args:
            force: If True, regenerate all auto sections

        Returns:
            Tuple of (file_path, was_created)
        """
        was_created = not self.memory_path.exists()

        # Preserve manual sections
        manual_sections = self.extract_existing_manual_sections()

        # Detect project characteristics
        project_type = self.detect_project_type()
        dirs = self.scan_directory_structure()
        architectures = self.detect_architecture_patterns()

        # Build the memory file
        lines = []

        # Header
        lines.append("# FlacoAI Project Memory")
        lines.append("")
        lines.append(f"*Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
        lines.append("")
        lines.append("This file contains FlacoAI's understanding of your project. Auto-generated sections are updated on `/init` or `/memory refresh`. Manual sections (between markers) are preserved.")
        lines.append("")

        # Project Overview (Auto)
        lines.append("---")
        lines.append("")
        lines.append("## 📱 Project Overview")
        lines.append("")

        if project_type['is_xcode_project']:
            lines.append("**Type:** Xcode Project")
        elif project_type['is_swift_package']:
            lines.append("**Type:** Swift Package")
        else:
            lines.append("**Type:** Swift/iOS Project")

        lines.append(f"**Root:** `{self.repo_root.name}`")
        lines.append("")

        # Project Features
        features = []
        if project_type['has_tests']:
            features.append("✅ Unit Tests")
        if project_type['uses_pods']:
            features.append("📦 CocoaPods")
        if project_type['uses_carthage']:
            features.append("📦 Carthage")
        if project_type['uses_swiftlint']:
            features.append("🔍 SwiftLint")
        if project_type['uses_fastlane']:
            features.append("🚀 Fastlane")

        if features:
            lines.append("**Features:** " + " · ".join(features))
            lines.append("")

        # Architecture (Auto)
        lines.append("---")
        lines.append("")
        lines.append("## 🏗️ Architecture")
        lines.append("")

        if architectures:
            lines.append("**Detected Patterns:**")
            for arch in architectures:
                lines.append(f"- {arch}")
            lines.append("")
        else:
            lines.append("*No specific architecture pattern detected. Run `/init` after adding more code.*")
            lines.append("")

        # Directory Structure (Auto)
        lines.append("---")
        lines.append("")
        lines.append("## 📂 Directory Structure")
        lines.append("")
        lines.append("```")
        lines.append(f"{self.repo_root.name}/")
        for dir_path in dirs[:20]:  # Limit to first 20
            indent = "  " * (len(Path(dir_path).parts) - 1)
            name = Path(dir_path).name
            lines.append(f"{indent}├── {name}/")
        if len(dirs) > 20:
            lines.append(f"  ... and {len(dirs) - 20} more directories")
        lines.append("```")
        lines.append("")

        # Swift/iOS Conventions (Manual Section)
        lines.append("---")
        lines.append("")
        lines.append(self.MANUAL_SECTION_START)
        lines.append("## 🍎 Swift/iOS Conventions")
        lines.append("")

        if "Swift/iOS Conventions" in manual_sections:
            lines.append(manual_sections["Swift/iOS Conventions"])
        else:
            lines.append("*Add your project's Swift coding conventions here.*")
            lines.append("")
            lines.append("**Example:**")
            lines.append("- Use `// MARK: -` for section dividers")
            lines.append("- Prefer `struct` over `class` when possible")
            lines.append("- Always use `guard let` for optional unwrapping")
            lines.append("- SwiftUI previews required for all views")

        lines.append("")
        lines.append(self.MANUAL_SECTION_END)
        lines.append("")

        # Rules & Preferences (Manual Section)
        lines.append("---")
        lines.append("")
        lines.append(self.MANUAL_SECTION_START)
        lines.append("## 📋 Rules & Preferences")
        lines.append("")

        if "Rules & Preferences" in manual_sections:
            lines.append(manual_sections["Rules & Preferences"])
        else:
            lines.append("*Add project-specific rules and preferences here.*")
            lines.append("")
            lines.append("**Example:**")
            lines.append("- Never force-unwrap optionals in production code")
            lines.append("- All public APIs must have documentation comments")
            lines.append("- Minimum iOS deployment target: iOS 15.0")

        lines.append("")
        lines.append(self.MANUAL_SECTION_END)
        lines.append("")

        # Known Quirks (Manual Section)
        lines.append("---")
        lines.append("")
        lines.append(self.MANUAL_SECTION_START)
        lines.append("## ⚠️ Known Quirks & Gotchas")
        lines.append("")

        if "Known Quirks & Gotchas" in manual_sections:
            lines.append(manual_sections["Known Quirks & Gotchas"])
        else:
            lines.append("*Document any project-specific quirks, workarounds, or gotchas here.*")
            lines.append("")
            lines.append("**Example:**")
            lines.append("- The `NetworkManager` singleton must be initialized before any API calls")
            lines.append("- CoreData context saves must happen on the main thread")

        lines.append("")
        lines.append(self.MANUAL_SECTION_END)
        lines.append("")

        # Footer
        lines.append("---")
        lines.append("")
        lines.append("*💡 Use `/memory note <text>` to quickly add notes to this file.*")
        lines.append("")

        # Write file
        content = "\n".join(lines)
        self.memory_path.write_text(content, encoding='utf-8')

        return str(self.memory_path), was_created

    def add_note(self, note: str, section: str = "Rules & Preferences") -> bool:
        """Add a quick note to a manual section.

        Args:
            note: The note to add
            section: Which manual section to add to

        Returns:
            True if successful
        """
        if not self.memory_path.exists():
            return False

        try:
            content = self.memory_path.read_text(encoding='utf-8')

            # Find the section
            section_pattern = rf'({self.MANUAL_SECTION_START}\n## {re.escape(section)}\n)(.*?)({self.MANUAL_SECTION_END})'
            match = re.search(section_pattern, content, re.DOTALL)

            if not match:
                return False

            section_start = match.group(1)
            section_content = match.group(2)
            section_end = match.group(3)

            # Add note
            timestamp = datetime.now().strftime('%Y-%m-%d')
            new_note = f"- [{timestamp}] {note}"

            # Insert note (remove example text if present)
            if "*Add your project" in section_content or "*Add project-specific" in section_content or "*Document any" in section_content:
                # Replace example with first note
                new_content = f"\n{new_note}\n"
            else:
                # Append to existing notes
                new_content = section_content.rstrip() + f"\n{new_note}\n"

            # Replace section
            new_section = section_start + new_content + section_end
            updated_content = content[:match.start()] + new_section + content[match.end():]

            self.memory_path.write_text(updated_content, encoding='utf-8')
            return True

        except Exception as e:
            print(f"Error adding note: {e}")
            return False


def init_project_memory(repo_root: str, force: bool = False) -> Tuple[str, bool]:
    """Initialize or refresh project memory.

    Args:
        repo_root: Path to repository root
        force: If True, regenerate all sections

    Returns:
        Tuple of (file_path, was_created)
    """
    scanner = ProjectScanner(repo_root)
    return scanner.generate_memory_file(force=force)


def add_memory_note(repo_root: str, note: str, section: str = "Rules & Preferences") -> bool:
    """Add a note to project memory.

    Args:
        repo_root: Path to repository root
        note: The note text
        section: Which section to add to

    Returns:
        True if successful
    """
    scanner = ProjectScanner(repo_root)
    return scanner.add_note(note, section=section)
