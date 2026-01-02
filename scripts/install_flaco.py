#!/usr/bin/env python3
"""Flaco AI Installer - Python version"""

import os
import sys
from pathlib import Path

# Colors
CYAN = '\033[0;36m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
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

                          Flaco AI Installer
"""


def main():
    print(f"{CYAN}{ASCII_ART}{NC}\n")

    # Get paths
    script_dir = Path(__file__).parent.resolve()
    project_root = script_dir.parent
    local_bin = Path.home() / '.local' / 'bin'

    # Ensure ~/.local/bin exists
    local_bin.mkdir(parents=True, exist_ok=True)

    # Ollama server configuration
    print(f"{CYAN}→{NC} Configuring Ollama server connection...\n")
    print(f"  {CYAN}Flaco AI works with local LLMs via Ollama.{NC}")
    print(f"  {CYAN}If Ollama is running on this machine, press Enter for default.{NC}")
    print(f"  {CYAN}If Ollama is on another server, enter the host:port{NC}\n")

    ollama_input = input(f"  Ollama server [{GREEN}localhost:11434{NC}]: ").strip()

    if not ollama_input:
        ollama_server = "localhost:11434"
    else:
        # Remove http:// if user added it
        ollama_server = ollama_input.replace("http://", "").replace("https://", "")
        # Remove /v1 if user added it
        ollama_server = ollama_server.replace("/v1", "").rstrip("/")

    ollama_base_url = f"http://{ollama_server}/v1"
    print(f"  {GREEN}✓{NC} Using Ollama at: {CYAN}{ollama_base_url}{NC}\n")

    # Tint color configuration
    print(f"{CYAN}→{NC} Choose your UI tint color...\n")
    print(f"  {CYAN}Available colors:{NC}")
    print(f"    1. {CYAN}cyan{NC} (default)")
    print(f"    2. {GREEN}green{NC}")
    print(f"    3. {YELLOW}yellow{NC}")
    print(f"    4. \033[0;35mmagenta\033[0m")
    print(f"    5. \033[0;34mblue\033[0m")
    print(f"    6. \033[0;31mred\033[0m\n")

    color_input = input(f"  Select color [1-6, {GREEN}default: cyan{NC}]: ").strip()

    color_map = {
        "1": "cyan",
        "2": "green",
        "3": "yellow",
        "4": "magenta",
        "5": "blue",
        "6": "red",
        "": "cyan"
    }

    tint_color = color_map.get(color_input, "cyan")
    print(f"  {GREEN}✓{NC} Using {CYAN}{tint_color}{NC} theme\n")

    print(f"{CYAN}→{NC} Creating Flaco AI executable...")

    # Create the executable
    flaco_bin = local_bin / 'flaco'
    venv_python = project_root / "venv" / "bin" / "python3"
    executable_content = f"""#!{venv_python}
# Flaco AI CLI Launcher

import os
import sys
from pathlib import Path

PROJECT_ROOT = Path("{project_root}")

# Set Python path
sys.path.insert(0, str(PROJECT_ROOT / "aider"))
os.environ["PYTHONPATH"] = str(PROJECT_ROOT / "aider") + os.pathsep + os.environ.get("PYTHONPATH", "")
os.environ["SETUPTOOLS_SCM_PRETEND_VERSION"] = "1.5.0"

# Run Flaco AI
os.chdir(PROJECT_ROOT / "aider")

if __name__ == "__main__":
    from flacoai.main import main
    sys.exit(main())
"""

    flaco_bin.write_text(executable_content)
    flaco_bin.chmod(0o755)

    print(f"{GREEN}✓{NC} Created executable at: {CYAN}{flaco_bin}{NC}")

    # Detect shell
    shell = os.environ.get('SHELL', '/bin/bash')
    if 'zsh' in shell:
        shell_config = Path.home() / '.zshrc'
    else:
        shell_config = Path.home() / '.bashrc'

    print(f"\n{CYAN}→{NC} Setting up shell aliases in {CYAN}{shell_config}{NC}...")

    # Ensure shell config exists
    shell_config.touch(exist_ok=True)

    config_content = shell_config.read_text()

    # Check if PATH export already exists
    path_export = 'export PATH="$HOME/.local/bin:$PATH"'
    if path_export not in config_content:
        shell_config.write_text(config_content + f"\n# Flaco AI - Local bin PATH\n{path_export}\n")
        print(f"{GREEN}✓{NC} Added ~/.local/bin to PATH")
    else:
        print(f"{YELLOW}!{NC} PATH already configured")

    # Add Ollama configuration
    config_content = shell_config.read_text()
    if "OPENAI_API_BASE" not in config_content or "flaco" not in config_content.lower():
        ollama_config = f"""
# Flaco AI - Configuration
export OPENAI_API_BASE="{ollama_base_url}"
export OPENAI_API_KEY="ollama"
export FLACO_TINT_COLOR="{tint_color}"

# Flaco AI - Quick model aliases
alias flaco.ai="flaco"
alias flaco.ai.qwen="flaco --model qwen2.5-coder:32b"
alias flaco.ai.ds="flaco --model deepseek-coder-v2:16b"
alias flaco.ai.r1="flaco --model deepseek-r1:32b"
"""
        config_content = shell_config.read_text()
        shell_config.write_text(config_content + ollama_config)
        print(f"{GREEN}✓{NC} Added Ollama configuration and shell aliases")
    else:
        print(f"{YELLOW}!{NC} Configuration already exists")

    # Success message
    print(f"\n{GREEN}{'═'*67}{NC}")
    print(f"{GREEN}✓ Installation Complete!{NC}")
    print(f"{GREEN}{'═'*67}{NC}\n")

    print(f"{CYAN}Available commands:{NC}")
    print(f"  {GREEN}flaco.ai{NC}          - Default Flaco AI (uses config model)")
    print(f"  {GREEN}flaco.ai.qwen{NC}     - Qwen 2.5 Coder 32B")
    print(f"  {GREEN}flaco.ai.ds{NC}       - DeepSeek Coder V2 16B")
    print(f"  {GREEN}flaco.ai.r1{NC}       - DeepSeek R1 32B (reasoning)")

    print(f"\n{YELLOW}⚠  To use these commands, run:{NC}")
    print(f"   {CYAN}source {shell_config}{NC}")
    print(f"   {CYAN}# OR open a new terminal{NC}\n")

    print(f"{CYAN}Configuration Summary:{NC}")
    print(f"  Ollama API: {GREEN}{ollama_base_url}{NC}")
    print(f"  Tint Color: {GREEN}{tint_color}{NC}")
    print(f"  {YELLOW}Note:{NC} Make sure Ollama is running before using Flaco AI\n")

    print(f"{CYAN}Next steps:{NC}")
    print(f"  1. Run: {GREEN}source {shell_config}{NC}")
    print(f"  2. Navigate to your Swift project")
    print(f"  3. Run: {GREEN}flaco.ai{NC}")
    print(f"  4. Type: {GREEN}/init{NC} to let Flaco AI learn your project\n")

    print(f"{CYAN}{'═'*67}{NC}\n")


if __name__ == "__main__":
    main()
