#!/usr/bin/env python3
"""
Flaco AI v3.0.0 - Enhanced Interactive Installer

Features:
- LLM provider choice (Local Ollama, Claude API, or both)
- GitHub configuration (name, email)
- Jira integration (URL, email, API token)
- Ollama server setup (custom or default)
- Theme customization (color, dark mode)
- TUI preferences (compact mode, loading style)
"""

import os
import sys
import subprocess
from pathlib import Path

# Colors
CYAN = '\033[0;36m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
MAGENTA = '\033[0;35m'
BLUE = '\033[0;34m'
RED = '\033[0;31m'
BOLD = '\033[1m'
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

                        Flaco AI v3.0.0 Installer
"""


def print_section(title):
    """Print a section header."""
    print(f"\n{BOLD}{CYAN}{'='*75}{NC}")
    print(f"{BOLD}{CYAN}  {title}{NC}")
    print(f"{BOLD}{CYAN}{'='*75}{NC}\n")


def get_input(prompt, default="", required=False):
    """Get user input with optional default."""
    if default:
        full_prompt = f"  {prompt} [{GREEN}{default}{NC}]: "
    else:
        full_prompt = f"  {prompt}: "

    value = input(full_prompt).strip()

    if not value:
        if required and not default:
            print(f"  {RED}✗ This field is required{NC}")
            return get_input(prompt, default, required)
        return default or value
    return value


def main():
    print(f"{CYAN}{ASCII_ART}{NC}\n")

    # Get paths
    script_dir = Path(__file__).parent.resolve()
    project_root = script_dir.parent
    local_bin = Path.home() / '.local' / 'bin'
    config_dir = Path.home() / '.flacoai'

    # Ensure directories exist
    local_bin.mkdir(parents=True, exist_ok=True)
    config_dir.mkdir(parents=True, exist_ok=True)

    config = {}

    # =========================================================================
    # 1. LLM PROVIDER CHOICE
    # =========================================================================
    print_section("🤖 LLM Provider Configuration")

    print(f"{CYAN}  Flaco AI supports multiple LLM backends:{NC}")
    print(f"    1. {CYAN}Local Models{NC} (Ollama) - Free, private, offline")
    print(f"    2. {CYAN}Claude API{NC} (Anthropic) - Powerful, cloud-based")
    print(f"    3. {CYAN}Both{NC} - Use local for review, Claude for complex tasks\n")

    llm_choice = get_input("Choose LLM provider [1-3]", "1")

    use_ollama = llm_choice in ["1", "3"]
    use_claude = llm_choice in ["2", "3"]

    # Configure Ollama if selected
    if use_ollama:
        print(f"\n{CYAN}→{NC} Configuring Ollama server...")
        print(f"  {CYAN}If Ollama is running locally, press Enter for default.{NC}")
        print(f"  {CYAN}If remote, enter full URL (e.g., http://192.168.1.10:11434){NC}\n")

        ollama_input = get_input("Ollama server", "localhost:11434")

        # Clean up URL
        ollama_server = ollama_input.replace("http://", "").replace("https://", "")
        ollama_server = ollama_server.replace("/v1", "").rstrip("/")

        config['OPENAI_API_BASE'] = f"http://{ollama_server}/v1"
        config['OPENAI_API_KEY'] = "ollama"  # Dummy key for Ollama

        print(f"  {GREEN}✓{NC} Ollama configured: {CYAN}{config['OPENAI_API_BASE']}{NC}")

        # Ask for default Ollama model
        print(f"\n{CYAN}→{NC} Default Ollama model...")
        print(f"  {CYAN}Popular choices: qwen2.5-coder:32b, deepseek-r1:32b, codellama:34b{NC}\n")

        default_model = get_input("Default model", "qwen2.5-coder:32b")
        config['DEFAULT_MODEL'] = f"openai/{default_model}"

    # Configure Claude API if selected
    if use_claude:
        print(f"\n{CYAN}→{NC} Configuring Claude API...")
        print(f"  {CYAN}Get your API key from: https://console.anthropic.com/settings/keys{NC}\n")

        claude_key = get_input("Claude API Key (starts with sk-ant-)", required=True)

        if use_ollama:
            # Store Claude key separately for selective use
            config['CLAUDE_API_KEY'] = claude_key
            print(f"  {GREEN}✓{NC} Claude API configured (available via --model claude-sonnet-4)")
        else:
            # Use Claude as primary
            config['ANTHROPIC_API_KEY'] = claude_key
            config['DEFAULT_MODEL'] = "claude-sonnet-4-5-20251022"
            print(f"  {GREEN}✓{NC} Claude API configured as primary LLM")

    # =========================================================================
    # 2. GITHUB CONFIGURATION
    # =========================================================================
    print_section("🐙 GitHub Configuration")

    print(f"{CYAN}  Configure Git user for commits made by Flaco AI{NC}\n")

    # Try to get existing git config
    try:
        existing_name = subprocess.run(
            ["git", "config", "--global", "user.name"],
            capture_output=True, text=True, check=False
        ).stdout.strip()
        existing_email = subprocess.run(
            ["git", "config", "--global", "user.email"],
            capture_output=True, text=True, check=False
        ).stdout.strip()
    except:
        existing_name = ""
        existing_email = ""

    git_name = get_input("Git user name", existing_name or "Your Name")
    git_email = get_input("Git email", existing_email or "you@example.com")

    config['GIT_USER_NAME'] = git_name
    config['GIT_USER_EMAIL'] = git_email

    # Configure git
    subprocess.run(["git", "config", "--global", "user.name", git_name], check=False)
    subprocess.run(["git", "config", "--global", "user.email", git_email], check=False)

    print(f"  {GREEN}✓{NC} Git configured: {CYAN}{git_name} <{git_email}>{NC}")

    # =========================================================================
    # 3. JIRA INTEGRATION (Optional)
    # =========================================================================
    print_section("📋 Jira Integration (Optional)")

    print(f"{CYAN}  Connect Flaco AI to Jira for automatic issue creation{NC}\n")

    enable_jira = get_input("Enable Jira integration? [y/N]", "n").lower()

    if enable_jira == "y":
        print(f"\n{CYAN}→{NC} Configuring Jira...")

        jira_url = get_input("Jira URL (e.g., https://yourcompany.atlassian.net)", required=True)
        jira_email = get_input("Jira email", git_email)

        print(f"\n  {CYAN}Get API token from: https://id.atlassian.com/manage-profile/security/api-tokens{NC}\n")
        jira_token = get_input("Jira API token", required=True)

        config['JIRA_URL'] = jira_url.rstrip('/')
        config['JIRA_EMAIL'] = jira_email
        config['JIRA_API_TOKEN'] = jira_token

        print(f"  {GREEN}✓{NC} Jira configured: {CYAN}{jira_url}{NC}")
    else:
        print(f"  {YELLOW}⊘{NC} Jira integration skipped")

    # =========================================================================
    # 4. THEME CUSTOMIZATION
    # =========================================================================
    print_section("🎨 Theme Customization")

    print(f"{CYAN}  Choose your UI tint color{NC}\n")
    print(f"    1. {CYAN}cyan{NC} (default, recommended)")
    print(f"    2. {GREEN}green{NC}")
    print(f"    3. {YELLOW}yellow{NC}")
    print(f"    4. {MAGENTA}magenta{NC}")
    print(f"    5. {BLUE}blue{NC}")
    print(f"    6. {RED}red{NC}\n")

    color_choice = get_input("Select color [1-6]", "1")

    color_map = {
        "1": "cyan",
        "2": "green",
        "3": "yellow",
        "4": "magenta",
        "5": "blue",
        "6": "red",
    }

    tint_color = color_map.get(color_choice, "cyan")
    config['FLACO_TINT_COLOR'] = tint_color

    print(f"  {GREEN}✓{NC} Theme: {CYAN}{tint_color}{NC}")

    # Dark mode preference
    print(f"\n{CYAN}→{NC} Terminal theme preference...")
    dark_mode = get_input("Use dark mode optimized colors? [Y/n]", "y").lower()
    config['FLACO_DARK_MODE'] = "true" if dark_mode != "n" else "false"

    # =========================================================================
    # 5. TUI PREFERENCES
    # =========================================================================
    print_section("⚙️  TUI Preferences")

    print(f"{CYAN}  Customize your terminal experience{NC}\n")

    # Compact mode
    compact = get_input("Use compact mode (less verbose output)? [y/N]", "n").lower()
    config['FLACO_COMPACT_MODE'] = "true" if compact == "y" else "false"

    # Show ASCII art
    show_art = get_input("Show ASCII art banner on startup? [Y/n]", "y").lower()
    config['FLACO_SHOW_BANNER'] = "true" if show_art != "n" else "false"

    # Model warnings
    show_warnings = get_input("Show model context warnings? [y/N]", "n").lower()
    config['FLACO_SHOW_MODEL_WARNINGS'] = "true" if show_warnings == "y" else "false"

    print(f"  {GREEN}✓{NC} Preferences saved")

    # =========================================================================
    # 6. SAVE CONFIGURATION
    # =========================================================================
    print_section("💾 Saving Configuration")

    # Write to shell profile
    shell_profile = Path.home() / '.zshrc'  # or .bashrc
    if not shell_profile.exists():
        shell_profile = Path.home() / '.bashrc'

    config_lines = [
        "\n# Flaco AI v3.0.0 Configuration",
        f"# Generated on {subprocess.run(['date'], capture_output=True, text=True).stdout.strip()}",
        "",
    ]

    for key, value in config.items():
        # Quote values with spaces or special chars
        if ' ' in value or any(c in value for c in ['$', '&', '|', ';']):
            config_lines.append(f'export {key}="{value}"')
        else:
            config_lines.append(f'export {key}={value}')

    config_lines.append("")  # Trailing newline

    # Append to shell profile
    with open(shell_profile, 'a') as f:
        f.write('\n'.join(config_lines))

    print(f"  {GREEN}✓{NC} Configuration saved to {CYAN}{shell_profile}{NC}")

    # =========================================================================
    # 7. CREATE EXECUTABLE
    # =========================================================================
    print_section("🔧 Creating Flaco AI Executable")

    flaco_bin = local_bin / 'flaco'
    venv_python = project_root / "venv" / "bin" / "python3"

    executable_content = f"""#!{venv_python}
# Flaco AI v3.0.0 CLI Launcher

import os
import sys
from pathlib import Path

PROJECT_ROOT = Path("{project_root}")

# Set Python path
sys.path.insert(0, str(PROJECT_ROOT / "flacoai"))

# Preserve the user's current working directory; do not chdir here.

# Import and run main
from flacoai.main import main

if __name__ == "__main__":
    main()
"""

    with open(flaco_bin, 'w') as f:
        f.write(executable_content)

    # Make executable
    os.chmod(flaco_bin, 0o755)

    print(f"  {GREEN}✓{NC} Created executable: {CYAN}{flaco_bin}{NC}")

    # =========================================================================
    # 8. VERIFY INSTALLATION
    # =========================================================================
    print_section("✅ Verifying Installation")

    # Check if ~/.local/bin in PATH
    path_env = os.getenv('PATH', '')
    if str(local_bin) not in path_env:
        print(f"  {YELLOW}⚠{NC}  ~/.local/bin not in PATH")
        print(f"  {CYAN}→{NC} Add this line to {shell_profile}:")
        print(f"    {CYAN}export PATH=\"$HOME/.local/bin:$PATH\"{NC}\n")
    else:
        print(f"  {GREEN}✓{NC} ~/.local/bin is in PATH")

    # Test Ollama connection if configured
    if use_ollama:
        print(f"\n{CYAN}→{NC} Testing Ollama connection...")
        try:
            import requests
            response = requests.get(config['OPENAI_API_BASE'].replace('/v1', ''), timeout=3)
            if response.status_code == 200:
                print(f"  {GREEN}✓{NC} Ollama is running")
            else:
                print(f"  {YELLOW}⚠{NC}  Ollama returned status {response.status_code}")
        except Exception as e:
            print(f"  {YELLOW}⚠{NC}  Could not connect to Ollama: {e}")
            print(f"    {CYAN}→ Start Ollama with: ollama serve{NC}")

    # =========================================================================
    # 9. NEXT STEPS
    # =========================================================================
    print_section("🚀 Installation Complete!")

    print(f"{BOLD}Next Steps:{NC}\n")
    print(f"  1. Reload your shell: {CYAN}source {shell_profile}{NC}")
    print(f"  2. Run Flaco AI: {CYAN}flaco{NC}")

    if use_ollama:
        print(f"  3. Pull an Ollama model: {CYAN}ollama pull {config.get('DEFAULT_MODEL', 'qwen2.5-coder:32b').replace('openai/', '')}{NC}")

    print(f"\n{BOLD}Quick Start:{NC}\n")
    print(f"  {CYAN}flaco{NC}                    # Start interactive session")
    print(f"  {CYAN}/review{NC}                  # Run code review")
    print(f"  {CYAN}/license info{NC}            # Check license status")

    if use_claude:
        print(f"  {CYAN}/model claude-sonnet-4{NC}   # Switch to Claude")

    print(f"\n{BOLD}Documentation:{NC}")
    print(f"  📖 README: {CYAN}https://github.com/RouraIO/flaco.cli{NC}")
    print(f"  💡 Issues: {CYAN}https://github.com/RouraIO/flaco.cli/issues{NC}")
    print(f"  💬 Support: {CYAN}support@roura.io{NC}")

    print(f"\n{GREEN}✨ Happy coding with Flaco AI v3.0.0! ✨{NC}\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Installation cancelled by user{NC}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{RED}Installation failed: {e}{NC}")
        sys.exit(1)
