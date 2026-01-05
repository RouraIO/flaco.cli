#!/usr/bin/env zsh

set -e
set -u
setopt pipefail

# Run FlacoAI directly from source (without full installation)

# Get the directory where the script is located
SCRIPT_DIR="${0:A:h}"

# Use the venv's python directly.
# This is more robust than sourcing activate, especially if the venv directory was moved.
PYTHON_BIN="$SCRIPT_DIR/venv/bin/python"
if [ ! -x "$PYTHON_BIN" ]; then
	PYTHON_BIN="$SCRIPT_DIR/venv/bin/python3"
fi
if [ ! -x "$PYTHON_BIN" ]; then
	echo "Error: Could not find a runnable python in $SCRIPT_DIR/venv/bin" >&2
	echo "Fix: recreate the venv with: python3 -m venv $SCRIPT_DIR/venv" >&2
	exit 1
fi

# Set Python path to include flacoai directory
export PYTHONPATH="$SCRIPT_DIR/flacoai:${PYTHONPATH:-}"

# Set version for setuptools-scm
export SETUPTOOLS_SCM_PRETEND_VERSION=1.5.0

# Run flacoai
"$PYTHON_BIN" -m flacoai "$@"
