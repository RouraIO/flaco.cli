#!/usr/bin/env python3
"""Flaco AI Complete Setup - Configures GitHub, Jira, Ollama, and Theme"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError

# Colors
CYAN = '\033[0;36m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
RED = '\033[0;31m'
MAGENTA = '\033[0;35m'
BLUE = '\033[0;34m'
NC = '\033[0m'  # No Color

ASCII_ART = """╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║      ███████╗ ██╗      █████╗   ██████╗  ██████╗       █████╗  ██╗        ║
║      ██╔════╝ ██║     ██╔══██╗ ██╔════╝ ██╔═══██╗     ██╔══██╗ ██║        ║
║      █████╗   ██║     ███████║ ██║      ██║   ██║     ███████║ ██║        ║
║      ██╔══╝   ██║     ██╔══██║ ██║      ██║   ██║     ██╔══██║ ██║        ║
║      ██║      ███████╗██║  ██║ ╚██████╗ ╚██████╔╝     ██║  ██║ ██║        ║
║      ╚═╝      ╚══════╝╚═╝  ╚═╝  ╚═════╝  ╚═════╝      ╚═╝  ╚═╝ ╚═╝        ║
║                                                                           ║
║        🚀 The Ultimate Local-First Swift & iOS Development Assistant      ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

                   Flaco AI Complete Setup Wizard
"""


def print_header(text):
    """Print a section header"""
    print(f"\n{CYAN}{'═' * 80}{NC}")
    print(f"{CYAN}  {text}{NC}")
    print(f"{CYAN}{'═' * 80}{NC}\n")


def fetch_ollama_models(ollama_url):
    """Fetch available models from Ollama server"""
    try:
        req = Request(f"{ollama_url}/api/tags", headers={'Content-Type': 'application/json'})
        response = urlopen(req, timeout=5)
        data = json.loads(response.read().decode('utf-8'))
        models = [model['name'] for model in data.get('models', [])]
        return models
    except (URLError, Exception) as e:
        print(f"  {RED}✗{NC} Failed to fetch models: {e}")
        return []


def get_git_config(key):
    """Get git config value"""
    try:
        result = subprocess.run(
            ['git', 'config', '--global', key],
            capture_output=True,
            text=True,
            check=False
        )
        return result.stdout.strip() if result.returncode == 0 else None
    except Exception:
        return None


def set_git_config(key, value):
    """Set git config value"""
    try:
        subprocess.run(['git', 'config', '--global', key, value], check=True)
        return True
    except Exception:
        return False


def setup_github():
    """Setup GitHub configuration"""
    print_header("GitHub Configuration")

    print(f"{CYAN}Flaco AI uses git for commits and GitHub CLI for PRs/releases.{NC}\n")

    # Get current git config
    current_name = get_git_config('user.name')
    current_email = get_git_config('user.email')

    # Name
    if current_name:
        name_prompt = f"  Your name [{GREEN}{current_name}{NC}]: "
    else:
        name_prompt = f"  Your name: "

    name = input(name_prompt).strip()
    if not name and current_name:
        name = current_name

    # Email
    if current_email:
        email_prompt = f"  Your email [{GREEN}{current_email}{NC}]: "
    else:
        email_prompt = f"  Your email: "

    email = input(email_prompt).strip()
    if not email and current_email:
        email = current_email

    # PAT Token (optional for private repos)
    print(f"\n  {CYAN}GitHub Personal Access Token (optional, for private repos):{NC}")
    print(f"  {CYAN}Create at: https://github.com/settings/tokens{NC}")
    pat = input(f"  PAT Token [{GREEN}press Enter to skip{NC}]: ").strip()

    # Save git config
    if name:
        set_git_config('user.name', name)
        print(f"  {GREEN}✓{NC} Git user.name set to: {CYAN}{name}{NC}")

    if email:
        set_git_config('user.email', email)
        print(f"  {GREEN}✓{NC} Git user.email set to: {CYAN}{email}{NC}")

    return {
        'name': name,
        'email': email,
        'pat': pat if pat else None
    }


def setup_jira():
    """Setup Jira configuration"""
    print_header("Jira Configuration")

    print(f"{CYAN}Flaco AI can integrate with Jira for ticket management.{NC}")
    print(f"{CYAN}You can skip this and configure later.{NC}\n")

    skip = input(f"  Configure Jira now? [{GREEN}Y/n{NC}]: ").strip().lower()
    if skip in ('n', 'no'):
        print(f"  {YELLOW}⊘{NC} Skipping Jira setup")
        return None

    print(f"\n  {CYAN}Enter your Jira details:{NC}\n")

    # Jira URL
    url = input(f"  Jira URL (e.g., https://yourcompany.atlassian.net): ").strip()
    if not url.startswith('http'):
        url = f"https://{url}"

    # Jira Email
    email = input(f"  Jira email: ").strip()

    # API Token
    print(f"\n  {CYAN}Jira API Token:{NC}")
    print(f"  {CYAN}Create at: https://id.atlassian.com/manage-profile/security/api-tokens{NC}")
    api_token = input(f"  API Token: ").strip()

    if url and email and api_token:
        print(f"  {GREEN}✓{NC} Jira configured: {CYAN}{url}{NC}")
        return {
            'url': url,
            'email': email,
            'api_token': api_token
        }
    else:
        print(f"  {YELLOW}⊘{NC} Incomplete Jira configuration, skipping")
        return None


def setup_theme():
    """Setup theme configuration"""
    print_header("Theme Configuration")

    print(f"{CYAN}Choose your UI tint color:{NC}\n")
    print(f"  1. {CYAN}cyan{NC} (default)")
    print(f"  2. {GREEN}green{NC}")
    print(f"  3. {YELLOW}yellow{NC}")
    print(f"  4. {MAGENTA}magenta{NC}")
    print(f"  5. {BLUE}blue{NC}")
    print(f"  6. {RED}red{NC}\n")

    color_input = input(f"  Select color [1-6, {GREEN}default: 1{NC}]: ").strip()

    color_map = {
        "1": ("#00FFFF", "cyan"),
        "2": ("#00FF00", "green"),
        "3": ("#FFFF00", "yellow"),
        "4": ("#FF00FF", "magenta"),
        "5": ("#0088FF", "blue"),
        "6": ("#FF0000", "red"),
        "": ("#00FFFF", "cyan")
    }

    hex_color, color_name = color_map.get(color_input, ("#00FFFF", "cyan"))
    print(f"  {GREEN}✓{NC} Theme set to: {CYAN}{color_name}{NC}")

    return {
        'hex': hex_color,
        'name': color_name
    }


def setup_ollama():
    """Setup Ollama configuration"""
    print_header("Ollama Configuration")

    print(f"{CYAN}Flaco AI works with local LLMs via Ollama.{NC}")
    print(f"{CYAN}If Ollama is running on this machine, press Enter for default.{NC}")
    print(f"{CYAN}If Ollama is on another server, enter the host:port{NC}\n")

    ollama_input = input(f"  Ollama server [{GREEN}localhost:11434{NC}]: ").strip()

    if not ollama_input:
        ollama_server = "localhost:11434"
    else:
        # Clean up user input
        ollama_server = ollama_input.replace("http://", "").replace("https://", "")
        ollama_server = ollama_server.replace("/v1", "").rstrip("/")

    ollama_base_url = f"http://{ollama_server}/v1"
    ollama_api_url = f"http://{ollama_server}"

    print(f"  {GREEN}✓{NC} Using Ollama at: {CYAN}{ollama_base_url}{NC}")

    # Fetch available models
    print(f"\n  {CYAN}Fetching available models...{NC}")
    models = fetch_ollama_models(ollama_api_url)

    if not models:
        print(f"  {RED}✗{NC} No models found. Make sure Ollama is running.")
        print(f"  {YELLOW}⊘{NC} Using default model: openai/qwen2.5-coder:32b")
        return {
            'base_url': ollama_base_url,
            'model': 'openai/qwen2.5-coder:32b'
        }

    print(f"  {GREEN}✓{NC} Found {len(models)} models:\n")

    # Display models with numbers
    for i, model in enumerate(models, 1):
        print(f"    {i}. {CYAN}{model}{NC}")

    # Let user select model
    print()
    default_model = models[0] if models else 'openai/qwen2.5-coder:32b'
    model_input = input(f"  Select model [1-{len(models)}, {GREEN}default: 1{NC}]: ").strip()

    if model_input.isdigit() and 1 <= int(model_input) <= len(models):
        selected_model = models[int(model_input) - 1]
    else:
        selected_model = default_model

    # Prefix with openai/ for litellm
    if not selected_model.startswith('openai/'):
        selected_model = f"openai/{selected_model}"

    print(f"  {GREEN}✓{NC} Selected model: {CYAN}{selected_model}{NC}")

    return {
        'base_url': ollama_base_url,
        'model': selected_model
    }


def write_config(github_config, jira_config, theme_config, ollama_config):
    """Write configuration files"""
    print_header("Writing Configuration")

    home = Path.home()

    # Write ~/.flacoai.conf.yml
    config_file = home / '.flacoai.conf.yml'

    config_content = f"""# Flaco AI Configuration
# Auto-generated by setup wizard

# Model Configuration
model: {ollama_config['model']}
edit-format: diff

# Ollama Configuration
openai-api-base: {ollama_config['base_url']}
openai-api-key: ollama

# Disable model warnings for local models
show-model-warnings: false

# UI Configuration
assistant-output-color: "{theme_config['hex']}"

# Git Configuration
# user.name: {github_config['name']}
# user.email: {github_config['email']}
"""

    with open(config_file, 'w') as f:
        f.write(config_content)

    print(f"  {GREEN}✓{NC} Created: {CYAN}{config_file}{NC}")

    # Write environment variables to ~/.zshrc or ~/.bashrc
    shell_rc = None
    if (home / '.zshrc').exists():
        shell_rc = home / '.zshrc'
    elif (home / '.bashrc').exists():
        shell_rc = home / '.bashrc'

    if shell_rc:
        env_lines = [
            "\n# Flaco AI Configuration",
            f"export OPENAI_API_BASE=\"{ollama_config['base_url']}\"",
            f"export OPENAI_API_KEY=\"ollama\"",
        ]

        # Add GitHub PAT if provided
        if github_config.get('pat'):
            env_lines.append(f"export GITHUB_TOKEN=\"{github_config['pat']}\"")

        # Add Jira config if provided
        if jira_config:
            env_lines.extend([
                f"export JIRA_SERVER=\"{jira_config['url']}\"",
                f"export JIRA_USERNAME=\"{jira_config['email']}\"",
                f"export JIRA_API_TOKEN=\"{jira_config['api_token']}\"",
            ])

        env_lines.append("")  # Blank line at end

        # Check if config already exists
        with open(shell_rc, 'r') as f:
            content = f.read()

        # Remove old Flaco AI config if it exists
        if '# Flaco AI Configuration' in content:
            lines = content.split('\n')
            new_lines = []
            skip = False
            for line in lines:
                if '# Flaco AI Configuration' in line:
                    skip = True
                    continue
                if skip and (line.strip() == '' or line.startswith('export')):
                    continue
                else:
                    skip = False
                    new_lines.append(line)
            content = '\n'.join(new_lines)

        # Append new config
        with open(shell_rc, 'a') as f:
            f.write('\n'.join(env_lines))

        print(f"  {GREEN}✓{NC} Updated: {CYAN}{shell_rc}{NC}")

    return config_file, shell_rc


def main():
    print(f"{CYAN}{ASCII_ART}{NC}")

    try:
        # Run setup steps
        github_config = setup_github()
        jira_config = setup_jira()
        theme_config = setup_theme()
        ollama_config = setup_ollama()

        # Write configs
        config_file, shell_rc = write_config(github_config, jira_config, theme_config, ollama_config)

        # Summary
        print_header("Setup Complete!")

        print(f"{GREEN}✓{NC} GitHub configured with git")
        if github_config.get('pat'):
            print(f"{GREEN}✓{NC} GitHub PAT token saved")

        if jira_config:
            print(f"{GREEN}✓{NC} Jira integration configured")
        else:
            print(f"{YELLOW}⊘{NC} Jira integration skipped (can configure later)")

        print(f"{GREEN}✓{NC} Theme: {theme_config['name']}")
        print(f"{GREEN}✓{NC} Ollama: {ollama_config['model']}")

        print(f"\n{CYAN}Next steps:{NC}")
        print(f"  1. Restart your terminal or run: {CYAN}source {shell_rc}{NC}")
        print(f"  2. Run: {CYAN}flaco{NC}")
        print(f"\n{CYAN}Enjoy coding with Flaco AI! 🚀{NC}\n")

    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Setup cancelled by user{NC}\n")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n{RED}Setup failed: {e}{NC}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
