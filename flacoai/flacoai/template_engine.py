"""SwiftUI template engine for code generation."""

import os
import re
from pathlib import Path
from typing import Dict, List, Optional


class TemplateEngine:
    """Engine for loading and processing SwiftUI templates."""

    def __init__(self):
        """Initialize the template engine."""
        # Get the template directory path
        self.template_dir = Path(__file__).parent / "templates" / "swiftui"

        # Template metadata
        self.templates = {
            "login": {
                "file": "login_view.swift.template",
                "description": "Login view with email/password fields",
                "required_vars": ["VIEW_NAME", "APP_NAME"],
                "optional_vars": [],
            },
            "settings": {
                "file": "settings_view.swift.template",
                "description": "Settings view with toggles and navigation",
                "required_vars": ["VIEW_NAME", "APP_NAME"],
                "optional_vars": [],
            },
            "list": {
                "file": "list_view.swift.template",
                "description": "List view with search and add functionality",
                "required_vars": [
                    "VIEW_NAME",
                    "ITEM_TYPE",
                    "ITEM_TYPE_PLURAL",
                    "SEARCH_FIELD",
                    "DETAIL_VIEW",
                    "TITLE",
                    "EMPTY_ICON",
                ],
                "optional_vars": [],
            },
            "detail": {
                "file": "detail_view.swift.template",
                "description": "Detail view for displaying item information",
                "required_vars": [
                    "VIEW_NAME",
                    "ITEM_TYPE",
                    "TITLE_FIELD",
                    "DESCRIPTION_FIELD",
                    "DATE_FIELD",
                    "STATUS_FIELD",
                    "CATEGORY_FIELD",
                ],
                "optional_vars": ["IMAGE_FIELD"],
            },
            "tabview": {
                "file": "tabview.swift.template",
                "description": "TabView with 4 tabs",
                "required_vars": [
                    "VIEW_NAME",
                    "DEFAULT_TAB",
                    "TAB1",
                    "TAB1_VIEW",
                    "TAB1_LABEL",
                    "TAB1_ICON",
                    "TAB2",
                    "TAB2_VIEW",
                    "TAB2_LABEL",
                    "TAB2_ICON",
                    "TAB3",
                    "TAB3_VIEW",
                    "TAB3_LABEL",
                    "TAB3_ICON",
                    "TAB4",
                    "TAB4_VIEW",
                    "TAB4_LABEL",
                    "TAB4_ICON",
                ],
                "optional_vars": [],
            },
        }

    def list_templates(self) -> List[Dict[str, str]]:
        """List all available templates with their descriptions.

        Returns:
            List of template info dictionaries
        """
        return [
            {"name": name, "description": info["description"]}
            for name, info in self.templates.items()
        ]

    def load_template(self, template_name: str) -> Optional[str]:
        """Load a template file by name.

        Args:
            template_name: Name of the template (e.g., 'login', 'settings')

        Returns:
            Template content as string, or None if not found
        """
        if template_name not in self.templates:
            return None

        template_file = self.template_dir / self.templates[template_name]["file"]

        if not template_file.exists():
            return None

        with open(template_file, "r", encoding="utf-8") as f:
            return f.read()

    def get_required_vars(self, template_name: str) -> List[str]:
        """Get list of required variables for a template.

        Args:
            template_name: Name of the template

        Returns:
            List of required variable names
        """
        if template_name not in self.templates:
            return []

        return self.templates[template_name]["required_vars"]

    def substitute_variables(
        self, template_content: str, variables: Dict[str, str]
    ) -> str:
        """Substitute variables in template content.

        Args:
            template_content: Template string with {VAR_NAME} placeholders
            variables: Dictionary mapping variable names to values

        Returns:
            Template content with variables substituted
        """
        result = template_content

        for var_name, var_value in variables.items():
            placeholder = f"{{{var_name}}}"
            result = result.replace(placeholder, var_value)

        return result

    def extract_variables_from_prompt(
        self, template_name: str, prompt: str
    ) -> Dict[str, str]:
        """Extract variables from user prompt.

        Args:
            template_name: Name of the template being used
            prompt: User's generation request

        Returns:
            Dictionary of extracted variables
        """
        variables = {}

        # Extract view name (capitalize first letter of each word)
        words = prompt.split()
        if words:
            # Take first 1-3 words as view name
            view_name_words = []
            for word in words[:3]:
                cleaned = re.sub(r"[^a-zA-Z0-9]", "", word)
                if cleaned and not cleaned.lower() in [
                    "view",
                    "for",
                    "with",
                    "and",
                    "the",
                    "a",
                ]:
                    view_name_words.append(cleaned.capitalize())

            if view_name_words:
                variables["VIEW_NAME"] = "".join(view_name_words) + "View"
            else:
                variables["VIEW_NAME"] = "GeneratedView"

        # Template-specific variable extraction
        if template_name == "login":
            variables["APP_NAME"] = self._extract_app_name(prompt) or "My App"

        elif template_name == "settings":
            variables["APP_NAME"] = self._extract_app_name(prompt) or "My App"

        elif template_name == "list":
            item_type = self._extract_item_type(prompt)
            variables["ITEM_TYPE"] = item_type
            variables["ITEM_TYPE_PLURAL"] = item_type + "s"  # Simple pluralization
            variables["SEARCH_FIELD"] = "name"  # Default field
            variables["DETAIL_VIEW"] = item_type + "DetailView"
            variables["TITLE"] = variables["ITEM_TYPE_PLURAL"]
            variables["EMPTY_ICON"] = "tray"

        elif template_name == "detail":
            item_type = self._extract_item_type(prompt)
            variables["ITEM_TYPE"] = item_type
            variables["TITLE_FIELD"] = "title"
            variables["DESCRIPTION_FIELD"] = "description"
            variables["DATE_FIELD"] = "createdAt"
            variables["STATUS_FIELD"] = "status"
            variables["CATEGORY_FIELD"] = "category"
            variables["IMAGE_FIELD"] = "imageURL"

        elif template_name == "tabview":
            # Extract tab names from prompt or use defaults
            tabs = self._extract_tabs(prompt)
            variables["DEFAULT_TAB"] = tabs[0]["key"]

            for i, tab in enumerate(tabs[:4], 1):
                variables[f"TAB{i}"] = tab["key"]
                variables[f"TAB{i}_VIEW"] = tab["view"]
                variables[f"TAB{i}_LABEL"] = tab["label"]
                variables[f"TAB{i}_ICON"] = tab["icon"]

        return variables

    def _extract_app_name(self, prompt: str) -> Optional[str]:
        """Extract app name from prompt.

        Args:
            prompt: User's prompt

        Returns:
            App name if found, None otherwise
        """
        # Look for patterns like "for MyApp" or "app name MyApp"
        match = re.search(r"(?:for|app name|called)\s+([A-Z][a-zA-Z0-9]+)", prompt)
        if match:
            return match.group(1)

        return None

    def _extract_item_type(self, prompt: str) -> str:
        """Extract item type from prompt.

        Args:
            prompt: User's prompt

        Returns:
            Item type name
        """
        # Look for common patterns
        patterns = [
            r"list of (\w+)",
            r"(\w+) list",
            r"show (\w+)",
            r"display (\w+)",
            r"manage (\w+)",
        ]

        for pattern in patterns:
            match = re.search(pattern, prompt, re.IGNORECASE)
            if match:
                item_type = match.group(1).capitalize()
                # Remove plural 's' if present
                if item_type.endswith("s") and len(item_type) > 3:
                    item_type = item_type[:-1]
                return item_type

        # Default
        return "Item"

    def _extract_tabs(self, prompt: str) -> List[Dict[str, str]]:
        """Extract tab configuration from prompt.

        Args:
            prompt: User's prompt

        Returns:
            List of tab configurations
        """
        # Default tabs if not specified
        default_tabs = [
            {
                "key": "home",
                "view": "HomeView",
                "label": "Home",
                "icon": "house",
            },
            {
                "key": "search",
                "view": "SearchView",
                "label": "Search",
                "icon": "magnifyingglass",
            },
            {
                "key": "favorites",
                "view": "FavoritesView",
                "label": "Favorites",
                "icon": "heart",
            },
            {
                "key": "profile",
                "view": "ProfileView",
                "label": "Profile",
                "icon": "person",
            },
        ]

        # TODO: Parse prompt for custom tab names
        # For now, return defaults

        return default_tabs

    def generate(
        self, template_name: str, prompt: str, custom_vars: Optional[Dict[str, str]] = None
    ) -> Optional[str]:
        """Generate code from template.

        Args:
            template_name: Name of the template to use
            prompt: User's generation request
            custom_vars: Optional dictionary of custom variable overrides

        Returns:
            Generated SwiftUI code, or None if template not found
        """
        # Load template
        template_content = self.load_template(template_name)
        if template_content is None:
            return None

        # Extract variables from prompt
        variables = self.extract_variables_from_prompt(template_name, prompt)

        # Override with custom variables if provided
        if custom_vars:
            variables.update(custom_vars)

        # Substitute variables
        generated_code = self.substitute_variables(template_content, variables)

        return generated_code


def main():
    """Test the template engine."""
    engine = TemplateEngine()

    print("Available templates:")
    for template in engine.list_templates():
        print(f"  - {template['name']}: {template['description']}")

    print("\n" + "=" * 80 + "\n")

    # Test login template
    print("Generating login view...")
    code = engine.generate("login", "Login view for MyApp")
    if code:
        print(code[:500] + "...")

    print("\n" + "=" * 80 + "\n")

    # Test list template
    print("Generating list view...")
    code = engine.generate("list", "List of tasks")
    if code:
        print(code[:500] + "...")


if __name__ == "__main__":
    main()
