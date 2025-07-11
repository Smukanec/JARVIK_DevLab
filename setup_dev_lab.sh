#!/usr/bin/env bash
# Installs prerequisites and sets up jarvik-devlab on Ubuntu 25.04
set -euo pipefail

# Update package lists and install required packages
sudo apt update
sudo apt install -y git python3 python3-venv python3-pip

# Clone the repository and run the provided installer
git clone https://github.com/your-org/jarvik-devlab.git
cd jarvik-devlab
./install.sh

echo "Setup complete. Activate the environment using:"
echo "  source .venv/bin/activate"
