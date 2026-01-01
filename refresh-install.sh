#!/bin/bash

# FlacoAI Refresh Installation Script
# Run this after making code changes to see them in action

set -e

echo "╔═══════════════════════════════════════════════════════════════════════════╗"
echo "║                    FlacoAI Refresh Installation                           ║"
echo "╚═══════════════════════════════════════════════════════════════════════════╝"
echo ""

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
else
    echo "✅ Virtual environment found"
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Uninstall old version if exists
echo "🗑️  Removing old installation..."
pip uninstall -y aider-chat 2>/dev/null || true

# Install in editable mode
echo "📥 Installing FlacoAI in development mode..."
cd flacoai
pip install -e . --quiet

echo ""
echo "✅ Installation complete!"
echo ""
echo "🚀 To run FlacoAI, use one of these commands:"
echo "   1. python -m aider"
echo "   2. aider (if in PATH)"
echo ""
echo "💡 Quick test:"
echo "   python -m aider --help"
echo ""
echo "🎯 For full startup experience with branding:"
echo "   cd ~/test-project && python -m aider"
echo ""
