#!/usr/bin/env bash
# ==============================================================================
# J.A.R.V.I.S. // STARK INDUSTRIES WINDOWS 11 LINUX DESKTOP SHELL INSTALLER
# Version: 8.5.2
# Author: Tony Stark / MR_Gray
# Target Systems: Linux Cinnamon, Fedora, KDE Plasma 6, Ubuntu, Mint, Debian, Arch
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
THEME_NAME="Jarvis-Windows11-Shell"
ICON_THEME_NAME="Jarvis-White"
THEME_DEST="${HOME}/.themes/${THEME_NAME}"
ICON_DEST="${HOME}/.icons/${ICON_THEME_NAME}"
ICON_DEST_LOCAL="${HOME}/.local/share/icons/${ICON_THEME_NAME}"
WALLPAPER_DEST="${HOME}/.local/share/backgrounds"
WALLPAPER_LIVE="${WALLPAPER_DEST}/stark-live-wallpaper.png"

CYAN='\033[0;36m'
GREEN='\033[0;32m'
GOLD='\033[0;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${CYAN}"
echo "======================================================================"
echo "   STARK INDUSTRIES // MARK LXXXV J.A.R.V.I.S. DESKTOP SUITE        "
echo "  Shell + Icon Theme + Window Decorations + Live Telemetry Wallpaper  "
echo "======================================================================"
echo -e "${NC}"

usage() {
    echo "Usage: ./apply.sh [OPTION]"
    echo ""
    echo "Options:"
    echo "  --all, -a         Install full suite (Shell, Icons, Window Decor, & Live Wallpaper)"
    echo "  --wallpaper, -wp  Generate & apply real OS telemetry wallpaper once"
    echo "  --live            Start background daemon updating real-time CPU/RAM on wallpaper"
    echo "  --stop-live       Stop the background live telemetry wallpaper daemon"
    echo "  --status          Check status of the live wallpaper daemon"
    echo "  --icons           Install only the Jarvis-White icon theme"
    echo "  --web, -w         Launch interactive Stark OS Web Desktop Shell (localhost:3030)"
    echo "  --restore, -r     Restore default desktop and icon settings"
    echo "  --help, -h        Show this help message"
    echo ""
}

install_full_suite() {
    echo -e "${CYAN}[1/5] Installing Shell & Window Decorations to ${THEME_DEST}...${NC}"
    mkdir -p "${THEME_DEST}/cinnamon"
    mkdir -p "${THEME_DEST}/metacity-1"
    mkdir -p "${THEME_DEST}/gtk-3.0"
    mkdir -p "${THEME_DEST}/gtk-4.0"
    mkdir -p "${WALLPAPER_DEST}"

    # Copy Cinnamon Shell theme
    cp -r "${SCRIPT_DIR}/cinnamon/"* "${THEME_DEST}/cinnamon/"
    
    # Copy Metacity-1 Window Decorations
    cp -r "${SCRIPT_DIR}/metacity-1/"* "${THEME_DEST}/metacity-1/"
    
    # Copy GTK 3.0 & 4.0 themes
    cp -r "${SCRIPT_DIR}/gtk-3.0/"* "${THEME_DEST}/gtk-3.0/"
    cp -r "${SCRIPT_DIR}/gtk-4.0/"* "${THEME_DEST}/gtk-4.0/"
    
    # Copy Master index.theme
    if [ -f "${SCRIPT_DIR}/index.theme" ]; then
        cp "${SCRIPT_DIR}/index.theme" "${THEME_DEST}/index.theme"
    fi

    echo -e "${CYAN}[2/5] Installing Jarvis-White Icon Theme...${NC}"
    mkdir -p "${ICON_DEST}" "${ICON_DEST_LOCAL}"
    if [ ! -d "${SCRIPT_DIR}/icons/Jarvis-White" ]; then
        python3 "${SCRIPT_DIR}/tools/generate_icon_theme.py"
    fi
    cp -r "${SCRIPT_DIR}/icons/Jarvis-White/"* "${ICON_DEST}/"
    cp -r "${SCRIPT_DIR}/icons/Jarvis-White/"* "${ICON_DEST_LOCAL}/"

    echo -e "${CYAN}[3/5] Generating Real Linux OS Telemetry Wallpaper...${NC}"
    python3 "${SCRIPT_DIR}/generate_wallpaper.py" --output "${WALLPAPER_LIVE}" --apply

    echo -e "${CYAN}[4/5] Applying Theme Configuration to Active Desktop Session...${NC}"
    
    # Check for Cinnamon
    if command -v gsettings >/dev/null 2>&1; then
        echo -e "${GREEN}Configuring GSettings (Cinnamon / GTK / GNOME)...${NC}"
        gsettings set org.cinnamon.theme name "${THEME_NAME}" 2>/dev/null || true
        gsettings set org.cinnamon.desktop.interface gtk-theme "${THEME_NAME}" 2>/dev/null || true
        gsettings set org.cinnamon.desktop.interface icon-theme "${ICON_THEME_NAME}" 2>/dev/null || true
        gsettings set org.cinnamon.desktop.wm.preferences theme "${THEME_NAME}" 2>/dev/null || true
        gsettings set org.gnome.desktop.interface gtk-theme "${THEME_NAME}" 2>/dev/null || true
        gsettings set org.gnome.desktop.interface icon-theme "${ICON_THEME_NAME}" 2>/dev/null || true
    fi

    # Check for KDE Plasma 6
    if command -v qdbus-qt6 >/dev/null 2>&1; then
        echo -e "${GREEN}Detected KDE Plasma 6: Applying live wallpaper to all Plasma desktops...${NC}"
        qdbus-qt6 org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript "
        for (var i = 0; i < desktops().length; i++) {
            var d = desktops()[i];
            d.wallpaperPlugin = 'org.kde.image';
            d.currentConfigGroup = Array('Wallpaper', 'org.kde.image', 'General');
            d.writeConfig('Image', 'file://${WALLPAPER_LIVE}');
        }
        " 2>/dev/null || true
    fi

    echo -e "${CYAN}[5/5] Checking Live Daemon...${NC}"
    echo -e "${GREEN}✓ Full suite installed successfully!${NC}"
    echo -e "${GOLD}Tip: Run './apply.sh --live' to keep the wallpaper continuously updated with live CPU & RAM metrics!${NC}"
}

generate_wallpaper_once() {
    echo -e "${CYAN}Generating single snapshot wallpaper with real OS telemetry...${NC}"
    python3 "${SCRIPT_DIR}/generate_wallpaper.py" --output "${WALLPAPER_LIVE}" --apply
    echo -e "${GREEN}✓ Live telemetry wallpaper applied!${NC}"
}

start_live_daemon() {
    python3 "${SCRIPT_DIR}/live_wallpaper_daemon.py" start --interval 3.0
}

stop_live_daemon() {
    python3 "${SCRIPT_DIR}/live_wallpaper_daemon.py" stop
}

check_daemon_status() {
    python3 "${SCRIPT_DIR}/live_wallpaper_daemon.py" status
}

install_icons_only() {
    echo -e "${CYAN}Installing Jarvis-White Icon Theme...${NC}"
    mkdir -p "${ICON_DEST}" "${ICON_DEST_LOCAL}"
    python3 "${SCRIPT_DIR}/tools/generate_icon_theme.py"
    cp -r "${SCRIPT_DIR}/icons/Jarvis-White/"* "${ICON_DEST}/"
    cp -r "${SCRIPT_DIR}/icons/Jarvis-White/"* "${ICON_DEST_LOCAL}/"
    if command -v gsettings >/dev/null 2>&1; then
        gsettings set org.cinnamon.desktop.interface icon-theme "${ICON_THEME_NAME}" 2>/dev/null || true
    fi
    echo -e "${GREEN}✓ Jarvis-White icon theme installed!${NC}"
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
    echo -e "${GOLD}Restoring default theme and icon settings...${NC}"
    stop_live_daemon || true
    if command -v gsettings >/dev/null 2>&1; then
        gsettings set org.cinnamon.theme name "Mint-Y" 2>/dev/null || true
        gsettings set org.cinnamon.desktop.interface gtk-theme "Mint-Y" 2>/dev/null || true
        gsettings set org.cinnamon.desktop.interface icon-theme "Mint-Y" 2>/dev/null || true
        gsettings set org.cinnamon.desktop.wm.preferences theme "Mint-Y" 2>/dev/null || true
        echo -e "${GREEN}✓ Restored default Cinnamon settings.${NC}"
    fi
}

ACTION="${1:---all}"
case "${ACTION}" in
    --all|-a|all)
        install_full_suite
        ;;
    --wallpaper|-wp|wallpaper)
        generate_wallpaper_once
        ;;
    --live|live)
        start_live_daemon
        ;;
    --stop-live|stop-live)
        stop_live_daemon
        ;;
    --status|status)
        check_daemon_status
        ;;
    --icons|icons)
        install_icons_only
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
