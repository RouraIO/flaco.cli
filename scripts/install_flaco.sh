#!/usr/bin/env bash
set -euo pipefail

# Flaco AI Installer
# Installs Flaco AI CLI and sets up shell aliases

CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${CYAN}"
cat << 'EOF'
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║      ███████╗ ██╗      █████╗   ██████╗  ██████╗       █████╗  ██╗       ║
║      ██╔════╝ ██║     ██╔══██╗ ██╔════╝ ██╔═══██╗     ██╔══██╗  ██║      ║
║      █████╗   ██║     ███████║ ██║      ██║   ██║     ███████║ ██║       ║
║      ██╔══╝   ██║     ██╔══██║ ██║      ██║   ██║     ██╔══██║  ██║      ║
║      ██║      ███████╗██║  ██║ ╚██████╗ ╚██████╔╝     ██║  ██║  ██║      ║
║      ╚═╝      ╚══════╝╚═╝  ╚═╝  ╚═════╝  ╚═════╝      ╚═╝  ╚═╝  ╚═╝      ║
║                                                                           ║
║        🚀 The Ultimate Local-First Swift & iOS Development Assistant      ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

                          Flaco AI Installer
EOF
echo -e "${NC}\n"

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Ensure ~/.local/bin exists
LOCAL_BIN="$HOME/.local/bin"
mkdir -p "$LOCAL_BIN"

echo -e "${CYAN}→${NC} Creating Flaco AI executable..."

# Create the main executable
FLACO_BIN="$LOCAL_BIN/flaco"
cat > "$FLACO_BIN" << 'FLACO_SCRIPT_EOF'
#!/usr/bin/env bash
# Flaco AI CLI Launcher

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$(dirname "$SCRIPT_DIR")")"

# Activate virtual environment if it exists
if [ -d "$PROJECT_ROOT/flaco/venv" ]; then
    source "$PROJECT_ROOT/flaco/venv/bin/activate"
fi

# Set Python path
export PYTHONPATH="$PROJECT_ROOT/flaco/flacoai:$PYTHONPATH"
export SETUPTOOLS_SCM_PRETEND_VERSION=0.86.1

# Run Flaco AI
cd "$PROJECT_ROOT/flaco/flacoai"
python -m aider "$@"
FLACO_SCRIPT_EOF

chmod +x "$FLACO_BIN"

echo -e "${GREEN}✓${NC} Created executable at: ${CYAN}$FLACO_BIN${NC}"

# Add PATH export and aliases to shell config
SHELL_CONFIG="$HOME/.zshrc"

# Detect shell
if [ -n "${ZSH_VERSION:-}" ]; then
    SHELL_CONFIG="$HOME/.zshrc"
elif [ -n "${BASH_VERSION:-}" ]; then
    SHELL_CONFIG="$HOME/.bashrc"
fi

echo -e "\n${CYAN}→${NC} Setting up shell aliases in ${CYAN}$SHELL_CONFIG${NC}..."

# Check if PATH export already exists
if ! grep -q 'export PATH="$HOME/.local/bin:$PATH"' "$SHELL_CONFIG" 2>/dev/null; then
    echo -e "\n# Flaco AI - Local bin PATH" >> "$SHELL_CONFIG"
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$SHELL_CONFIG"
    echo -e "${GREEN}✓${NC} Added ~/.local/bin to PATH"
else
    echo -e "${YELLOW}!${NC} PATH already configured"
fi

# Check if aliases already exist
if ! grep -q "alias flaco.ai=" "$SHELL_CONFIG" 2>/dev/null; then
    cat >> "$SHELL_CONFIG" << 'ALIAS_EOF'

# Flaco AI - Quick model aliases
alias flaco.ai="flaco"
alias flaco.ai.qwen="flaco --model qwen2.5-coder:32b"
alias flaco.ai.ds="flaco --model deepseek-coder-v2:16b"
alias flaco.ai.r1="flaco --model deepseek-r1:32b"
ALIAS_EOF
    echo -e "${GREEN}✓${NC} Added Flaco AI shell aliases"
else
    echo -e "${YELLOW}!${NC} Aliases already configured"
fi

echo -e "\n${GREEN}═══════════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}✓ Installation Complete!${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════════════${NC}\n"

echo -e "${CYAN}Available commands:${NC}"
echo -e "  ${GREEN}flaco.ai${NC}          - Default Flaco AI (uses config model)"
echo -e "  ${GREEN}flaco.ai.qwen${NC}     - Qwen 2.5 Coder 32B"
echo -e "  ${GREEN}flaco.ai.ds${NC}       - DeepSeek Coder V2 16B"
echo -e "  ${GREEN}flaco.ai.r1${NC}       - DeepSeek R1 32B (reasoning)"

echo -e "\n${YELLOW}⚠  To use these commands, run:${NC}"
echo -e "   ${CYAN}source $SHELL_CONFIG${NC}"
echo -e "   ${CYAN}# OR open a new terminal${NC}\n"

echo -e "${CYAN}Next steps:${NC}"
echo -e "  1. Run: ${GREEN}source $SHELL_CONFIG${NC}"
echo -e "  2. Navigate to your Swift project"
echo -e "  3. Run: ${GREEN}flaco.ai${NC}"
echo -e "  4. Type: ${GREEN}/init${NC} to let Flaco AI learn your project\n"

echo -e "${CYAN}═══════════════════════════════════════════════════════════════════${NC}\n"
