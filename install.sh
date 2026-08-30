#!/bin/bash
# =============================================================
# 🌟 AiraLang Global Installer for Termux & Linux
# 👑 Creator: Adam Eehan (Aira Group of Technology)
# =============================================================

set -e

echo -e "\033[1;36m"
echo "    ___    _           __                    "
echo "   /   |  (_)________ _/ /   ____ _____  ____ _"
echo "  / /| | / / ___/ __ \`/ /   / __ \`/ __ \/ __ \`/"
echo " / ___ |/ / /  / /_/ / /___/ /_/ / / / / /_/ / "
echo "/_/  |_/_/_/   \\__,_/_____/\\__,_/_/ /_/\\__, /  "
echo "                                      /____/   "
echo -e "\033[0m"
echo -e "\033[1;32m[*] Installing AiraLang (v1.2.0 Next-Gen Engine)...\033[0m"

# Target installation directory
INSTALL_DIR="$HOME/.airalang"
BIN_DIR=""

if [ -d "/data/data/com.termux/files/usr/bin" ]; then
    BIN_DIR="/data/data/com.termux/files/usr/bin"
elif [ -d "$HOME/.local/bin" ]; then
    BIN_DIR="$HOME/.local/bin"
elif [ -d "/usr/local/bin" ] && [ -w "/usr/local/bin" ]; then
    BIN_DIR="/usr/local/bin"
else
    BIN_DIR="$HOME/bin"
    mkdir -p "$BIN_DIR"
fi

echo -e "\033[1;34m[*] Target Binary Path: $BIN_DIR/airalang\033[0m"

# Create symlink / launcher
cat << 'EOF' > "$BIN_DIR/airalang"
#!/data/data/com.termux/files/usr/bin/python3
import sys
import os

INSTALL_PATH = os.path.expanduser("~/.airalang/src")
LOCAL_PATH = "/data/data/com.termux/files/home/airalang/src"

if os.path.exists(LOCAL_PATH):
    sys.path.insert(0, LOCAL_PATH)
elif os.path.exists(INSTALL_PATH):
    sys.path.insert(0, INSTALL_PATH)

import cli

if __name__ == "__main__":
    cli.main()
EOF

chmod +x "$BIN_DIR/airalang"

echo -e "\033[1;32m[+] AiraLang Successfully Installed! 🚀\033[0m"
echo -e "\033[1;37m[*] Run \033[1;33mairalang\033[0m to start the REPL, or \033[1;33mairalang <script.aira>\033[0m to run a file.\033[0m"
