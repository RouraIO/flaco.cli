"""Jira API client wrapper for FlacoAI."""

import os
from typing import Optional, List, Dict, Any
from jira import JIRA
from jira.exceptions import JIRAError


class JiraClient:
    """Wrapper for Jira API operations."""

    def __init__(self, server: str, username: str, api_token: str):
        """Initialize Jira client.

        Args:
            server: Jira server URL (e.g., https://company.atlassian.net)
            username: Jira username/email
            api_token: Jira API token
        """
        self.server = server
        self.username = username
        self.jira = JIRA(server=server, basic_auth=(username, api_token))

    @classmethod
    def from_config(cls, io=None):
        """Create JiraClient from environment variables or config.

        Looks for:
        - JIRA_SERVER
        - JIRA_USERNAME
        - JIRA_API_TOKEN

        Args:
            io: IO object for error output (optional)

        Returns:
            JiraClient instance or None if credentials not found
        """
        server = os.getenv("JIRA_SERVER")
        username = os.getenv("JIRA_USERNAME")
        api_token = os.getenv("JIRA_API_TOKEN")

        if not all([server, username, api_token]):
            if io:
                io.tool_error("Jira credentials not configured")
                io.tool_error("Set JIRA_SERVER, JIRA_USERNAME, and JIRA_API_TOKEN environment variables")
            return None

        try:
            return cls(server, username, api_token)
        except Exception as e:
            if io:
                io.tool_error(f"Failed to connect to Jira: {e}")
            return None

    def create_issue(
        self,
        project: str,
        summary: str,
        description: str,
        issue_type: str = "Task",
        priority: Optional[str] = None,
        labels: Optional[List[str]] = None,
        **kwargs
    ):
        """Create a new Jira issue.

        Args:
            project: Project key (e.g., "PROJ")
            summary: Issue summary/title
            description: Issue description
            issue_type: Issue type (Task, Bug, Story, etc.)
            priority: Priority level (optional)
            labels: List of labels (optional)
            **kwargs: Additional fields

        Returns:
            Created issue object
        """
        issue_dict = {
            "project": {"key": project},
            "summary": summary,
            "description": description,
            "issuetype": {"name": issue_type},
        }

        if priority:
            issue_dict["priority"] = {"name": priority}

        if labels:
            issue_dict["labels"] = labels

        # Add any additional fields
        issue_dict.update(kwargs)

        try:
            issue = self.jira.create_issue(fields=issue_dict)
            return issue
        except JIRAError as e:
            raise Exception(f"Failed to create issue: {e.text}")

    def get_issue(self, issue_key: str):
        """Get issue details by key.

        Args:
            issue_key: Issue key (e.g., "PROJ-123")

        Returns:
            Issue object
        """
        try:
            return self.jira.issue(issue_key)
        except JIRAError as e:
            raise Exception(f"Failed to get issue {issue_key}: {e.text}")

    def search_issues(self, jql: str, max_results: int = 50, fields: Optional[List[str]] = None):
        """Search issues using JQL.

        Args:
            jql: JQL query string
            max_results: Maximum number of results
            fields: List of fields to return (optional)

        Returns:
            List of issue objects
        """
        try:
            return self.jira.search_issues(jql, maxResults=max_results, fields=fields)
        except JIRAError as e:
            raise Exception(f"Failed to search issues: {e.text}")

    def update_issue(self, issue_key: str, **fields):
        """Update an existing issue.

        Args:
            issue_key: Issue key (e.g., "PROJ-123")
            **fields: Fields to update

        Returns:
            Updated issue object
        """
        try:
            issue = self.jira.issue(issue_key)
            issue.update(fields=fields)
            return issue
        except JIRAError as e:
            raise Exception(f"Failed to update issue {issue_key}: {e.text}")

    def add_comment(self, issue_key: str, comment: str):
        """Add a comment to an issue.

        Args:
            issue_key: Issue key (e.g., "PROJ-123")
            comment: Comment text

        Returns:
            Created comment object
        """
        try:
            return self.jira.add_comment(issue_key, comment)
        except JIRAError as e:
            raise Exception(f"Failed to add comment to {issue_key}: {e.text}")

    def transition_issue(self, issue_key: str, transition: str):
        """Transition an issue to a different status.

        Args:
            issue_key: Issue key (e.g., "PROJ-123")
            transition: Transition name or ID

        Returns:
            True if successful
        """
        try:
            self.jira.transition_issue(issue_key, transition)
            return True
        except JIRAError as e:
            raise Exception(f"Failed to transition {issue_key}: {e.text}")

    def get_transitions(self, issue_key: str):
        """Get available transitions for an issue.

        Args:
            issue_key: Issue key (e.g., "PROJ-123")

        Returns:
            List of available transitions
        """
        try:
            return self.jira.transitions(issue_key)
        except JIRAError as e:
            raise Exception(f"Failed to get transitions for {issue_key}: {e.text}")

    def link_commit(self, issue_key: str, commit_hash: str, repo_url: Optional[str] = None):
        """Link a git commit to an issue via comment.

        Args:
            issue_key: Issue key (e.g., "PROJ-123")
            commit_hash: Git commit hash
            repo_url: Repository URL (optional)

        Returns:
            Created comment object
        """
        if repo_url:
            commit_link = f"{repo_url}/commit/{commit_hash}"
            comment_text = f"Commit: [{commit_hash[:7]}|{commit_link}]"
        else:
            comment_text = f"Commit: {commit_hash[:7]}"

        return self.add_comment(issue_key, comment_text)

    def get_project(self, project_key: str):
        """Get project details.

        Args:
            project_key: Project key (e.g., "PROJ")

        Returns:
            Project object
        """
        try:
            return self.jira.project(project_key)
        except JIRAError as e:
            raise Exception(f"Failed to get project {project_key}: {e.text}")

    def get_issue_types(self, project_key: str):
        """Get available issue types for a project.

        Args:
            project_key: Project key (e.g., "PROJ")

        Returns:
            List of issue type names
        """
        try:
            project = self.jira.project(project_key)
            return [it.name for it in project.issueTypes]
        except JIRAError as e:
            raise Exception(f"Failed to get issue types: {e.text}")

    def assign_issue(self, issue_key: str, assignee: str):
        """Assign an issue to a user.

        Args:
            issue_key: Issue key (e.g., "PROJ-123")
            assignee: Username or account ID

        Returns:
            Updated issue object
        """
        try:
            issue = self.jira.issue(issue_key)
            issue.update(assignee={"name": assignee})
            return issue
        except JIRAError as e:
            raise Exception(f"Failed to assign {issue_key}: {e.text}")

    def get_user_issues(self, username: Optional[str] = None, status: Optional[str] = None):
        """Get issues assigned to a user.

        Args:
            username: Username (defaults to current user)
            status: Filter by status (optional)

        Returns:
            List of issues
        """
        if username is None:
            username = "currentUser()"
        else:
            username = f'"{username}"'

        jql = f"assignee = {username}"

        if status:
            jql += f' AND status = "{status}"'

        jql += " ORDER BY updated DESC"

        return self.search_issues(jql)
