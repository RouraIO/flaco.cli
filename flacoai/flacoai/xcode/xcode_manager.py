"""Xcode project manager for adding/removing files and managing targets."""

import os
from pathlib import Path
from typing import List, Optional, Dict, Tuple

try:
    from pbxproj import XcodeProject
    from pbxproj.pbxextensions import FileOptions
    PBXPROJ_AVAILABLE = True
except ImportError:
    PBXPROJ_AVAILABLE = False
    XcodeProject = None
    FileOptions = None


class XcodeManagerException(Exception):
    """Exception raised by XcodeManager."""
    pass


class XcodeManager:
    """Manager for Xcode project operations."""

    def __init__(self, project_path: Optional[str] = None, io=None):
        """Initialize XcodeManager.

        Args:
            project_path: Path to .xcodeproj file (optional, will auto-discover)
            io: IO object for output messages
        """
        if not PBXPROJ_AVAILABLE:
            raise XcodeManagerException(
                "mod-pbxproj is not installed. Install with: pip install mod-pbxproj"
            )

        self.io = io
        self.project_path = None
        self.project = None

        if project_path:
            self._load_project(project_path)
        else:
            self._discover_project()

    def _discover_project(self):
        """Auto-discover Xcode project in current directory or subdirectories."""
        current_dir = Path.cwd()

        # Look in current directory
        projects = list(current_dir.glob("*.xcodeproj"))

        # If not found, look one level down
        if not projects:
            projects = list(current_dir.glob("*/*.xcodeproj"))

        if not projects:
            raise XcodeManagerException(
                "No Xcode project found. Please specify project path or run from project directory."
            )

        if len(projects) > 1:
            # Multiple projects found, use first one but warn
            if self.io:
                self.io.tool_warning(
                    f"Multiple Xcode projects found. Using: {projects[0].name}"
                )

        self._load_project(str(projects[0]))

    def _load_project(self, project_path: str):
        """Load an Xcode project.

        Args:
            project_path: Path to .xcodeproj file
        """
        project_path = Path(project_path)

        if not project_path.exists():
            raise XcodeManagerException(f"Project not found: {project_path}")

        if not project_path.suffix == ".xcodeproj":
            raise XcodeManagerException(
                f"Invalid project path. Must end with .xcodeproj: {project_path}"
            )

        # Load the project
        pbxproj_path = project_path / "project.pbxproj"
        if not pbxproj_path.exists():
            raise XcodeManagerException(
                f"project.pbxproj not found in: {project_path}"
            )

        try:
            self.project = XcodeProject.load(str(pbxproj_path))
            self.project_path = project_path
            if self.io:
                self.io.tool_output(f"✅ Loaded Xcode project: {project_path.name}")
        except Exception as e:
            raise XcodeManagerException(f"Failed to load project: {e}")

    def save(self):
        """Save changes to the Xcode project."""
        if not self.project:
            raise XcodeManagerException("No project loaded")

        try:
            self.project.save()
            if self.io:
                self.io.tool_output(f"✅ Saved changes to: {self.project_path.name}")
        except Exception as e:
            raise XcodeManagerException(f"Failed to save project: {e}")

    def add_file(
        self, file_path: str, target_name: Optional[str] = None, group: Optional[str] = None
    ) -> bool:
        """Add a file to the Xcode project.

        Args:
            file_path: Path to the file to add (relative or absolute)
            target_name: Name of target to add file to (optional, uses main target)
            group: Group to add file to (optional, uses file's directory)

        Returns:
            True if file was added successfully
        """
        if not self.project:
            raise XcodeManagerException("No project loaded")

        file_path = Path(file_path)

        # Make path relative to project directory
        if file_path.is_absolute():
            try:
                file_path = file_path.relative_to(self.project_path.parent)
            except ValueError:
                # File is outside project directory
                pass

        file_path_str = str(file_path)

        # Check if file already exists in project
        existing_files = self.project.get_files_by_name(file_path.name)
        if existing_files:
            if self.io:
                self.io.tool_warning(f"File already in project: {file_path.name}")
            return False

        # Determine target
        if target_name:
            targets = [t for t in self.project.objects.get_targets() if t.name == target_name]
            if not targets:
                raise XcodeManagerException(f"Target not found: {target_name}")
            target = targets[0]
        else:
            # Use main target (first target)
            targets = self.project.objects.get_targets()
            if not targets:
                raise XcodeManagerException("No targets found in project")
            target = targets[0]

        # Determine if file should be added to compile sources
        file_ext = file_path.suffix.lower()
        is_source_file = file_ext in ['.swift', '.m', '.mm', '.c', '.cpp', '.cc']
        is_header = file_ext in ['.h', '.hpp']

        # Add file to project
        try:
            # Create file options
            create_build_files = is_source_file

            # Add the file
            file_ref = self.project.add_file(
                file_path_str,
                parent=group,
                target_name=target.name if create_build_files else None,
                force=False
            )

            if self.io:
                self.io.tool_output(f"✅ Added file: {file_path.name}")
                if create_build_files:
                    self.io.tool_output(f"   Added to target: {target.name}")
                    self.io.tool_output(f"   Added to compile sources")

            return True

        except Exception as e:
            raise XcodeManagerException(f"Failed to add file: {e}")

    def remove_file(self, file_path: str) -> bool:
        """Remove a file from the Xcode project.

        Args:
            file_path: Path or name of file to remove

        Returns:
            True if file was removed successfully
        """
        if not self.project:
            raise XcodeManagerException("No project loaded")

        # Try to find file by name
        file_name = Path(file_path).name
        files = self.project.get_files_by_name(file_name)

        if not files:
            if self.io:
                self.io.tool_error(f"File not found in project: {file_name}")
            return False

        if len(files) > 1:
            if self.io:
                self.io.tool_warning(f"Multiple files named '{file_name}' found. Removing all.")

        # Remove all matching files
        try:
            for file_ref in files:
                self.project.remove_file(file_ref)

            if self.io:
                self.io.tool_output(f"✅ Removed file: {file_name}")

            return True

        except Exception as e:
            raise XcodeManagerException(f"Failed to remove file: {e}")

    def list_targets(self) -> List[Dict[str, str]]:
        """List all targets in the project.

        Returns:
            List of target info dictionaries
        """
        if not self.project:
            raise XcodeManagerException("No project loaded")

        targets = self.project.objects.get_targets()
        target_info = []

        for target in targets:
            info = {
                "name": target.name,
                "type": target.productType if hasattr(target, 'productType') else "Unknown",
                "product": target.productName if hasattr(target, 'productName') else target.name,
            }
            target_info.append(info)

        return target_info

    def list_files(self, target_name: Optional[str] = None) -> List[str]:
        """List all files in the project or in a specific target.

        Args:
            target_name: Name of target to list files for (optional)

        Returns:
            List of file paths
        """
        if not self.project:
            raise XcodeManagerException("No project loaded")

        if target_name:
            # Get files for specific target
            targets = [t for t in self.project.objects.get_targets() if t.name == target_name]
            if not targets:
                raise XcodeManagerException(f"Target not found: {target_name}")

            target = targets[0]
            files = self.project.get_build_files(target.name)
            return [f.fileRef.path for f in files if hasattr(f, 'fileRef') and f.fileRef.path]
        else:
            # Get all files in project
            files = []
            for obj in self.project.objects.get_objects_in_section('PBXFileReference'):
                if hasattr(obj, 'path') and obj.path:
                    files.append(obj.path)
            return files

    def get_project_info(self) -> Dict[str, any]:
        """Get project information.

        Returns:
            Dictionary with project info
        """
        if not self.project:
            raise XcodeManagerException("No project loaded")

        targets = self.list_targets()

        info = {
            "name": self.project_path.stem,
            "path": str(self.project_path),
            "targets": targets,
            "target_count": len(targets),
        }

        return info


def find_xcode_project(start_path: Optional[str] = None) -> Optional[Path]:
    """Find Xcode project in directory or parent directories.

    Args:
        start_path: Directory to start search from (defaults to current directory)

    Returns:
        Path to .xcodeproj or None if not found
    """
    if start_path:
        search_dir = Path(start_path)
    else:
        search_dir = Path.cwd()

    # Look in current directory and parent directories
    current = search_dir
    for _ in range(5):  # Look up to 5 levels
        projects = list(current.glob("*.xcodeproj"))
        if projects:
            return projects[0]

        # Try subdirectories
        projects = list(current.glob("*/*.xcodeproj"))
        if projects:
            return projects[0]

        # Move to parent
        if current.parent == current:
            break
        current = current.parent

    return None
