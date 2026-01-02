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
║      ███████╗ ██╗      █████╗   ██████╗  ██████╗       █████╗  ██╗       ║
║      ██╔════╝ ██║     ██╔══██╗ ██╔════╝ ██╔═══██╗     ██╔══██╗ ██║        ║
║      █████╗   ██║     ███████║ ██║      ██║   ██║     ███████║ ██║       ║
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

    print(f"{CYAN}→{NC} Creating Flaco AI executable...")

    # Create the executable
    flaco_bin = local_bin / 'flaco'
    executable_content = f"""#!/usr/bin/env python3
# Flaco AI CLI Launcher

import os
import sys
from pathlib import Path

PROJECT_ROOT = Path("{project_root}")

# Activate virtual environment if it exists
venv_activate = PROJECT_ROOT / "venv" / "bin" / "activate_this.py"
if venv_activate.exists():
    exec(venv_activate.read_text())

# Set Python path
sys.path.insert(0, str(PROJECT_ROOT / "flacoai"))
os.environ["PYTHONPATH"] = str(PROJECT_ROOT / "flacoai") + os.pathsep + os.environ.get("PYTHONPATH", "")
os.environ["SETUPTOOLS_SCM_PRETEND_VERSION"] = "0.86.1"

# Run Flaco AI
os.chdir(PROJECT_ROOT / "flacoai")

if __name__ == "__main__":
    from aider.main import main
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

    # Check if aliases already exist
    if "alias flaco.ai=" not in config_content:
        aliases = """
# Flaco AI - Quick model aliases
alias flaco.ai="flaco"
alias flaco.ai.qwen="flaco --model qwen2.5-coder:32b"
alias flaco.ai.ds="flaco --model deepseek-coder-v2:16b"
alias flaco.ai.r1="flaco --model deepseek-r1:32b"
"""
        config_content = shell_config.read_text()
        shell_config.write_text(config_content + aliases)
        print(f"{GREEN}✓{NC} Added Flaco AI shell aliases")
    else:
        print(f"{YELLOW}!{NC} Aliases already configured")

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

    print(f"{CYAN}Next steps:{NC}")
    print(f"  1. Run: {GREEN}source {shell_config}{NC}")
    print(f"  2. Navigate to your Swift project")
    print(f"  3. Run: {GREEN}flaco.ai{NC}")
    print(f"  4. Type: {GREEN}/init{NC} to let Flaco AI learn your project\n")

    print(f"{CYAN}{'═'*67}{NC}\n")


if __name__ == "__main__":
    main()
