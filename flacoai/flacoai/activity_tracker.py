"""Activity tracker for FlacoAI sessions."""

import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional


class ActivityTracker:
    """Track user activity across FlacoAI sessions."""

    def __init__(self, cache_dir: Optional[Path] = None):
        """Initialize activity tracker.

        Args:
            cache_dir: Directory for cache files (defaults to ~/.flacoai/cache)
        """
        if cache_dir is None:
            cache_dir = Path.home() / ".flacoai" / "cache"

        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.activity_file = self.cache_dir / "flaco_activity.json"

    def record_session(
        self,
        repo_path: Optional[str] = None,
        files_edited: Optional[List[str]] = None,
        commands_used: Optional[List[str]] = None,
        duration_seconds: Optional[float] = None,
    ):
        """Record a session's activity.

        Args:
            repo_path: Path to repository (optional)
            files_edited: List of files that were edited (optional)
            commands_used: List of commands that were used (optional)
            duration_seconds: Session duration in seconds (optional)
        """
        activity = self.load_activity()

        session = {
            "timestamp": datetime.now().isoformat(),
            "repo": str(repo_path) if repo_path else None,
            "files_edited": files_edited or [],
            "commands_used": commands_used or [],
            "duration_seconds": duration_seconds,
        }

        activity["sessions"].append(session)

        # Keep only last 30 days
        cutoff = datetime.now() - timedelta(days=30)
        activity["sessions"] = [
            s
            for s in activity["sessions"]
            if datetime.fromisoformat(s["timestamp"]) > cutoff
        ]

        self.save_activity(activity)

    def load_activity(self) -> Dict:
        """Load activity history from file.

        Returns:
            Activity dictionary with sessions list
        """
        if not self.activity_file.exists():
            return {"sessions": [], "version": "1.0"}

        try:
            with open(self.activity_file, "r") as f:
                return json.load(f)
        except Exception:
            return {"sessions": [], "version": "1.0"}

    def save_activity(self, activity: Dict):
        """Save activity history to file.

        Args:
            activity: Activity dictionary to save
        """
        try:
            with open(self.activity_file, "w") as f:
                json.dump(activity, f, indent=2)
        except Exception:
            pass  # Silently fail if we can't write

    def get_recent_activity_summary(self, days: int = 7) -> Optional[Dict]:
        """Get summary of recent activity.

        Args:
            days: Number of days to look back

        Returns:
            Summary dictionary or None if no recent activity
        """
        activity = self.load_activity()
        cutoff = datetime.now() - timedelta(days=days)

        recent_sessions = [
            s
            for s in activity["sessions"]
            if datetime.fromisoformat(s["timestamp"]) > cutoff
        ]

        if not recent_sessions:
            return None

        # Aggregate data
        total_files = set()
        total_commands = []
        repos = set()
        total_duration = 0

        for session in recent_sessions:
            total_files.update(session.get("files_edited", []))
            total_commands.extend(session.get("commands_used", []))

            if session.get("repo"):
                repos.add(session["repo"])

            if session.get("duration_seconds"):
                total_duration += session["duration_seconds"]

        # Count command frequency
        command_counts = {}
        for cmd in total_commands:
            command_counts[cmd] = command_counts.get(cmd, 0) + 1

        # Get top 5 commands
        top_commands = sorted(command_counts.items(), key=lambda x: x[1], reverse=True)[
            :5
        ]

        return {
            "session_count": len(recent_sessions),
            "files_edited": len(total_files),
            "commands_used": [cmd for cmd, _ in top_commands],
            "command_counts": dict(top_commands),
            "repos": len(repos),
            "total_duration_seconds": total_duration,
        }

    def get_lifetime_stats(self) -> Dict:
        """Get lifetime statistics.

        Returns:
            Lifetime stats dictionary
        """
        activity = self.load_activity()
        sessions = activity["sessions"]

        if not sessions:
            return {
                "total_sessions": 0,
                "total_files": 0,
                "total_repos": 0,
                "first_session": None,
                "last_session": None,
            }

        all_files = set()
        all_repos = set()
        all_commands = []

        for session in sessions:
            all_files.update(session.get("files_edited", []))
            all_commands.extend(session.get("commands_used", []))

            if session.get("repo"):
                all_repos.add(session["repo"])

        # Sort by timestamp
        sorted_sessions = sorted(sessions, key=lambda x: x["timestamp"])

        return {
            "total_sessions": len(sessions),
            "total_files": len(all_files),
            "total_repos": len(all_repos),
            "total_commands": len(all_commands),
            "first_session": sorted_sessions[0]["timestamp"],
            "last_session": sorted_sessions[-1]["timestamp"],
        }
