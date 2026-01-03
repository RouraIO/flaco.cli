#!/bin/bash

# Run FlacoAI directly from source (without full installation)

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Activate virtual environment
source "$SCRIPT_DIR/venv/bin/activate"

# Set Python path to include flacoai directory
export PYTHONPATH="$SCRIPT_DIR/flacoai:$PYTHONPATH"

# Set version for setuptools-scm
export SETUPTOOLS_SCM_PRETEND_VERSION=1.5.0

# Run flacoai
python -m flacoai "$@"
