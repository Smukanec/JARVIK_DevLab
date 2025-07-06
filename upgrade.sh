#!/usr/bin/env bash
# Upgrade jarvik-devlab to the latest available version
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

VENV_DIR=".venv"
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment not found. Run ./install.sh first." >&2
    exit 1
fi

PIP="$VENV_DIR/bin/pip"
if [ ! -x "$PIP" ]; then
    PIP="$VENV_DIR/Scripts/pip.exe"
fi

# Upgrade the package via pip
"$PIP" install --upgrade jarvik-devlab

echo "jarvik-devlab upgraded successfully"
