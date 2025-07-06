#!/usr/bin/env bash
# Simple installation script for jarvik-devlab
set -euo pipefail

# Determine available Python command
if command -v python3 >/dev/null 2>&1; then
    PYTHON_CMD="$(command -v python3)"
elif command -v python >/dev/null 2>&1; then
    PYTHON_CMD="$(command -v python)"
else
    echo "Error: Python interpreter not found in PATH. Please install Python." >&2
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Create local virtual environment if not present
VENV_DIR=".venv"
if [ ! -d "$VENV_DIR" ]; then
    "$PYTHON_CMD" -m venv "$VENV_DIR"
fi

# Resolve pip binary inside the venv
PIP="$VENV_DIR/bin/pip"
if [ ! -x "$PIP" ]; then
    PIP="$VENV_DIR/Scripts/pip.exe"
fi

# Upgrade pip to ensure latest features
"$PIP" install --upgrade pip

# Install the package from source
"$PIP" install .

ACTIVATE_PATH="$VENV_DIR/bin/activate"
if [ ! -f "$ACTIVATE_PATH" ]; then
    ACTIVATE_PATH="$VENV_DIR/Scripts/activate"
fi

echo "jarvik-devlab installed successfully"
echo "Activate the virtual environment with: source $ACTIVATE_PATH"
