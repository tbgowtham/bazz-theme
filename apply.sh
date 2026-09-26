#!/usr/bin/env bash
# ==============================================================================
# J.A.R.V.I.S. // STARK INDUSTRIES WINDOWS 11 LINUX DESKTOP SHELL INSTALLER
# Version: 8.5.2
# Author: Tony Stark / MR_Gray
# Target Systems: Linux Cinnamon, Fedora, Ubuntu, Mint, Debian, Arch
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
THEME_NAME="Jarvis-Windows11-Shell"
THEME_DEST="${HOME}/.themes/${THEME_NAME}"
WALLPAPER_DEST="${HOME}/.local/share/backgrounds"
WALLPAPER_SRC="${SCRIPT_DIR}/public/assets/wallpapers/jarvis-master.jpg"

CYAN='\033[0;36m'
GREEN='\033[0;32m'
GOLD='\033[0;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${CYAN}"
echo "======================================================================"
echo "   STARK INDUSTRIES // MARK LXXXV J.A.R.V.I.S. DESKTOP SHELL SUITE   "
echo "        Windows 11 Frosted Glass Architecture for Linux               "
echo "======================================================================"
echo -e "${NC}"

usage() {
    echo "Usage: ./apply.sh [OPTION]"
    echo ""
    echo "Options:"
    echo "  --install, -i     Install and apply native Cinnamon shell theme (Default)"
    echo "  --web, -w         Launch the interactive Stark OS Web Desktop Shell"
    echo "  --restore, -r     Restore default Linux Mint / Cinnamon themes"
    echo "  --help, -h        Show this help message"
    echo ""
}

install_cinnamon_theme() {
    echo -e "${CYAN}[1/4] Creating theme directory at ${THEME_DEST}...${NC}"
    mkdir -p "${THEME_DEST}/cinnamon"
    mkdir -p "${WALLPAPER_DEST}"

    echo -e "${CYAN}[2/4] Copying Cinnamon shell theme files...${NC}"
    cp -r "${SCRIPT_DIR}/cinnamon/"* "${THEME_DEST}/cinnamon/"
    
    if [ -f "${WALLPAPER_SRC}" ]; then
        echo -e "${CYAN}[3/4] Installing Mark LXXXV 4K Arc Reactor wallpaper...${NC}"
        cp "${WALLPAPER_SRC}" "${WALLPAPER_DEST}/jarvis-stark-wallpaper.jpg"
    fi

    echo -e "${CYAN}[4/4] Checking desktop environment...${NC}"
    if command -v gsettings >/dev/null 2>&1; then
        if [ "${XDG_CURRENT_DESKTOP:-}" = "X-Cinnamon" ] || [ "${DESKTOP_SESSION:-}" = "cinnamon" ]; then
            echo -e "${GREEN}Applying theme to Cinnamon...${NC}"
            gsettings set org.cinnamon.theme name "${THEME_NAME}" || true
            if [ -f "${WALLPAPER_DEST}/jarvis-stark-wallpaper.jpg" ]; then
                gsettings set org.cinnamon.desktop.background picture-uri "file://${WALLPAPER_DEST}/jarvis-stark-wallpaper.jpg" || true
            fi
            echo -e "${GREEN}✓ Theme successfully applied to Cinnamon!${NC}"
        else
            echo -e "${GOLD}Note: Current desktop session is '${XDG_CURRENT_DESKTOP:-Unknown}'.${NC}"
            echo -e "Theme files installed to ${THEME_DEST}. You can select '${THEME_NAME}' in Cinnamon System Settings."
        fi
    fi

    echo -e "${GREEN}Installation complete! Mark LXXXV J.A.R.V.I.S. suite is ready.${NC}"
}

start_web_shell() {
    echo -e "${CYAN}Starting Stark OS Interactive Desktop Shell...${NC}"
    if command -v node >/dev/null 2>&1; then
        cd "${SCRIPT_DIR}"
        echo -e "${GREEN}Serving shell at: http://localhost:3030${NC}"
        node server.js
    else
        echo -e "${RED}Error: Node.js is required to start the web shell server.${NC}"
        exit 1
    fi
}

restore_defaults() {
    echo -e "${GOLD}Restoring default theme settings...${NC}"
    if command -v gsettings >/dev/null 2>&1; then
        gsettings set org.cinnamon.theme name "Mint-Y" || true
        echo -e "${GREEN}✓ Restored default theme.${NC}"
    fi
}

ACTION="${1:-install}"
case "${ACTION}" in
    --install|-i|install)
        install_cinnamon_theme
        ;;
    --web|-w|web)
        start_web_shell
        ;;
    --restore|-r|restore)
        restore_defaults
        ;;
    --help|-h|help)
        usage
        ;;
    *)
        echo -e "${RED}Unknown argument: ${ACTION}${NC}"
        usage
        exit 1
        ;;
esac
