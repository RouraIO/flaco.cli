"""CHANGELOG.md generator from git history."""

import re
import subprocess
from typing import List, Dict, Optional
from datetime import datetime


class ChangelogGenerator:
    """Generates CHANGELOG.md from git commit history."""

    def __init__(self, repo_dir: str, io=None):
        """Initialize CHANGELOG generator.

        Args:
            repo_dir: Path to git repository
            io: IO object for output
        """
        self.repo_dir = repo_dir
        self.io = io

    def generate(self, since_tag: Optional[str] = None) -> str:
        """Generate CHANGELOG content.

        Args:
            since_tag: Generate changelog since this tag (optional)

        Returns:
            Markdown formatted CHANGELOG content
        """
        commits = self._get_commits(since_tag)
        grouped = self._group_commits(commits)

        sections = []

        # Header
        sections.append(self._generate_header())

        # Unreleased section
        if grouped['unreleased']:
            sections.append(self._generate_version_section('Unreleased', None, grouped['unreleased']))

        # Version sections
        for version_info in grouped['versions']:
            sections.append(self._generate_version_section(
                version_info['version'],
                version_info['date'],
                version_info['commits']
            ))

        return '\n\n'.join(sections)

    def _get_commits(self, since_tag: Optional[str]) -> List[Dict]:
        """Get commits from git history.

        Args:
            since_tag: Get commits since this tag

        Returns:
            List of commit dictionaries
        """
        cmd = ['git', 'log', '--pretty=format:%H|%s|%ad|%an', '--date=short']

        if since_tag:
            cmd.append(f'{since_tag}..HEAD')

        try:
            result = subprocess.run(
                cmd,
                cwd=self.repo_dir,
                capture_output=True,
                text=True,
                check=True
            )

            commits = []
            for line in result.stdout.strip().split('\n'):
                if not line:
                    continue

                parts = line.split('|')
                if len(parts) >= 4:
                    commit_hash, message, date, author = parts[:4]
                    commits.append({
                        'hash': commit_hash,
                        'message': message,
                        'date': date,
                        'author': author,
                        'type': self._classify_commit(message),
                    })

            return commits

        except subprocess.CalledProcessError:
            return []

    def _classify_commit(self, message: str) -> str:
        """Classify commit type from message.

        Args:
            message: Commit message

        Returns:
            Commit type (feat, fix, docs, etc.)
        """
        message_lower = message.lower()

        patterns = {
            'feat': r'^(feat|feature)',
            'fix': r'^fix',
            'docs': r'^docs?',
            'style': r'^style',
            'refactor': r'^refactor',
            'perf': r'^perf',
            'test': r'^test',
            'chore': r'^chore',
            'release': r'^(release|version)',
        }

        for commit_type, pattern in patterns.items():
            if re.match(pattern, message_lower):
                return commit_type

        return 'other'

    def _group_commits(self, commits: List[Dict]) -> Dict:
        """Group commits by version and type.

        Args:
            commits: List of commits

        Returns:
            Grouped commits dictionary
        """
        versions = []
        unreleased = []
        current_version = None

        for commit in commits:
            # Check if this is a release commit
            if commit['type'] == 'release':
                version_match = re.search(r'v?(\d+\.\d+\.\d+)', commit['message'])
                if version_match:
                    if current_version:
                        versions.append(current_version)

                    current_version = {
                        'version': version_match.group(1),
                        'date': commit['date'],
                        'commits': []
                    }
                    continue

            # Add to current version or unreleased
            if current_version:
                current_version['commits'].append(commit)
            else:
                unreleased.append(commit)

        # Add last version
        if current_version:
            versions.append(current_version)

        return {
            'unreleased': unreleased,
            'versions': versions,
        }

    def _generate_header(self) -> str:
        """Generate CHANGELOG header."""
        return """# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)."""

    def _generate_version_section(
        self,
        version: str,
        date: Optional[str],
        commits: List[Dict]
    ) -> str:
        """Generate section for a version.

        Args:
            version: Version number or 'Unreleased'
            date: Release date
            commits: List of commits for this version

        Returns:
            Markdown formatted version section
        """
        if not commits:
            return ""

        # Group commits by type
        by_type = {
            'feat': [],
            'fix': [],
            'docs': [],
            'style': [],
            'refactor': [],
            'perf': [],
            'test': [],
            'chore': [],
            'other': [],
        }

        for commit in commits:
            commit_type = commit['type']
            by_type[commit_type].append(commit)

        # Build section
        lines = []

        # Header
        if version == 'Unreleased':
            lines.append(f"## [{version}]")
        else:
            date_str = f" - {date}" if date else ""
            lines.append(f"## [v{version}]{date_str}")

        lines.append("")

        # Type sections
        type_headers = {
            'feat': '### ✨ Features',
            'fix': '### 🐛 Bug Fixes',
            'docs': '### 📚 Documentation',
            'perf': '### ⚡ Performance',
            'refactor': '### ♻️ Refactoring',
            'style': '### 💄 Styling',
            'test': '### 🧪 Tests',
            'chore': '### 🔧 Chores',
            'other': '### 📝 Other Changes',
        }

        for commit_type, header in type_headers.items():
            if by_type[commit_type]:
                lines.append(header)
                lines.append("")

                for commit in by_type[commit_type]:
                    # Clean up message (remove type prefix)
                    message = re.sub(r'^(feat|fix|docs|style|refactor|perf|test|chore|release):\s*', '', commit['message'], flags=re.IGNORECASE)

                    # Capitalize first letter
                    message = message[0].upper() + message[1:] if message else message

                    # Add to list
                    short_hash = commit['hash'][:7]
                    lines.append(f"- {message} ([`{short_hash}`](../../commit/{commit['hash']}))")

                lines.append("")

        return '\n'.join(lines)

    def get_git_tags(self) -> List[str]:
        """Get list of git tags.

        Returns:
            List of tag names
        """
        try:
            result = subprocess.run(
                ['git', 'tag', '--sort=-version:refname'],
                cwd=self.repo_dir,
                capture_output=True,
                text=True,
                check=True
            )

            return [tag.strip() for tag in result.stdout.split('\n') if tag.strip()]

        except subprocess.CalledProcessError:
            return []
