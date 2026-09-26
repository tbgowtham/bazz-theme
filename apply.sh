#!/usr/bin/env bash
# ===================================================================
# Ubuntu Cinnamon macOS Elegance Edition Installer & Applicator
# For Linux Mint Cinnamon & Debian/Ubuntu Cinnamon Desktops
# ===================================================================

set -e

# Terminal Colors
ORANGE='\033[38;2;233;84;32m'
BOLD='\033[1m'
NC='\033[0m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
GRAY='\033[0;90m'
RED='\033[0;31m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
THEME_NAME="Ubuntu-Cinnamon-White"
ICON_THEME_NAME="Ubuntu-Cinnamon-Orange-Icons"
BUTTON_LAYOUT="close,minimize,maximize:" # macOS Traffic Lights Default

print_header() {
    echo -e "${ORANGE}${BOLD}"
    echo "  ██╗   ██╗██████╗ ██╗   ██╗███╗   ██╗████████╗██╗   ██╗"
    echo "  ██║   ██║██╔══██╗██║   ██║████╗  ██║╚══██╔══╝██║   ██║"
    echo "  ██║   ██║██████╔╝██║   ██║██╔██╗ ██║   ██║   ██║   ██║"
    echo "  ██║   ██║██╔══██╗██║   ██║██║╚██╗██║   ██║   ██║   ██║"
    echo "  ╚██████╔╝██████╔╝╚██████╔╝██║ ╚████║   ██║   ╚██████╔╝"
    echo -e "   CINNAMON MACOS ELEGANCE EDITION  ${NC}${GRAY}(Ubuntu Orange #E95420)${NC}\n"
}

log_info() {
    echo -e " ${BLUE}[i]${NC} $1"
}

log_ok() {
    echo -e " ${GREEN}[✓]${NC} $1"
}

log_warn() {
    echo -e " ${ORANGE}[!]${NC} $1"
}

log_err() {
    echo -e " ${RED}[✗]${NC} $1"
}

set_setting() {
    local schema="$1"
    local key="$2"
    local val="$3"
    local label="$4"

    if command -v gsettings >/dev/null 2>&1; then
        if gsettings list-schemas 2>/dev/null | grep -qx "$schema"; then
            if gsettings set "$schema" "$key" "$val" 2>/dev/null; then
                log_ok "$label: $val"
                return 0
            fi
        fi
    fi
    log_info "$label skipped (schema '$schema' not active in current session)"
    return 0
}

show_help() {
    print_header
    echo -e "${BOLD}Usage:${NC} ./apply.sh [OPTION]"
    echo ""
    echo -e "${BOLD}Options:${NC}"
    echo "  (no args)             Install & apply Cinnamon shell, GTK, macOS traffic lights, icons, and wallpaper"
    echo "  --traditional-layout  Apply theme with traditional right-aligned window buttons (:minimize,maximize,close)"
    echo "  --macos-layout        Apply theme with macOS traffic light buttons on left (close,minimize,maximize:)"
    echo "  --all                 Install desktop theme + prompt for system GRUB & Slick-Greeter login theme"
    echo "  --grub                Install and activate the matching GRUB theme (requires sudo)"
    echo "  --lightdm             Configure Slick Greeter (LightDM) login screen (requires sudo)"
    echo "  --restore             Restore default Linux Mint (Mint-Y) theme settings"
    echo "  --help, -h            Display this help dialog"
    echo ""
    exit 0
}

restore_defaults() {
    log_info "Restoring Linux Mint default theme settings..."
    set_setting org.cinnamon.theme name 'Mint-Y' "Cinnamon Desktop Shell"
    set_setting org.cinnamon.desktop.interface gtk-theme 'Mint-Y' "GTK Controls"
    set_setting org.cinnamon.desktop.wm.preferences theme 'Mint-Y' "Window Borders"
    set_setting org.cinnamon.desktop.wm.preferences button-layout ':minimize,maximize,close' "Window Button Layout"
    set_setting org.cinnamon.desktop.interface icon-theme 'Mint-Y' "Icons"
    set_setting org.gnome.desktop.interface gtk-theme 'Mint-Y' "GNOME GTK"
    set_setting org.gnome.desktop.interface icon-theme 'Mint-Y' "GNOME Icons"
    log_ok "Default Mint-Y settings restored."
    exit 0
}

install_theme_files() {
    log_info "Installing theme directories to user profile..."
    
    USER_THEMES="$HOME/.themes"
    USER_LOCAL_THEMES="$HOME/.local/share/themes"
    USER_ICONS="$HOME/.icons"
    USER_LOCAL_ICONS="$HOME/.local/share/icons"
    USER_BG="$HOME/.local/share/backgrounds"

    mkdir -p "$USER_THEMES" "$USER_LOCAL_THEMES" "$USER_ICONS" "$USER_LOCAL_ICONS" "$USER_BG"

    # Copy Theme
    rm -rf "$USER_THEMES/$THEME_NAME" "$USER_LOCAL_THEMES/$THEME_NAME"
    cp -r "$SCRIPT_DIR/$THEME_NAME" "$USER_THEMES/"
    cp -r "$SCRIPT_DIR/$THEME_NAME" "$USER_LOCAL_THEMES/"
    log_ok "Desktop Theme ($THEME_NAME) installed to ~/.themes and ~/.local/share/themes"

    # Copy Icons
    rm -rf "$USER_ICONS/$ICON_THEME_NAME" "$USER_LOCAL_ICONS/$ICON_THEME_NAME"
    cp -r "$SCRIPT_DIR/icons/$ICON_THEME_NAME" "$USER_ICONS/"
    cp -r "$SCRIPT_DIR/icons/$ICON_THEME_NAME" "$USER_LOCAL_ICONS/"
    log_ok "Icon Theme ($ICON_THEME_NAME) installed to ~/.icons and ~/.local/share/icons"

    # Copy Wallpapers
    cp "$SCRIPT_DIR/wallpapers/"*.png "$USER_BG/" 2>/dev/null || true
    cp "$SCRIPT_DIR/wallpapers/"*.svg "$USER_BG/" 2>/dev/null || true
    log_ok "macOS-Ubuntu wallpapers installed to $USER_BG."
}

apply_cinnamon_settings() {
    log_info "Applying visual settings via gsettings..."

    # 1. Cinnamon Desktop Shell Theme
    set_setting org.cinnamon.theme name "$THEME_NAME" "Cinnamon Desktop Shell"

    # 2. GTK 3 & GTK 4 Controls Theme
    set_setting org.cinnamon.desktop.interface gtk-theme "$THEME_NAME" "Cinnamon GTK Controls"
    set_setting org.gnome.desktop.interface gtk-theme "$THEME_NAME" "GNOME GTK Controls"

    # 3. Window Borders / Titlebars (Metacity / Muffin)
    set_setting org.cinnamon.desktop.wm.preferences theme "$THEME_NAME" "Cinnamon Window Decorations"
    set_setting org.gnome.desktop.wm.preferences theme "$THEME_NAME" "GNOME Window Decorations"

    # 4. macOS Traffic Lights Button Layout
    set_setting org.cinnamon.desktop.wm.preferences button-layout "$BUTTON_LAYOUT" "Window Controls Layout"
    set_setting org.gnome.desktop.wm.preferences button-layout "$BUTTON_LAYOUT" "GNOME Controls Layout"

    # 5. Icon Theme
    set_setting org.cinnamon.desktop.interface icon-theme "$ICON_THEME_NAME" "Cinnamon Icons"
    set_setting org.gnome.desktop.interface icon-theme "$ICON_THEME_NAME" "GNOME Icons"

    # 6. Desktop Wallpaper (Default: macOS-style Ubuntu Wave)
    WALLPAPER_PATH="$HOME/.local/share/backgrounds/ubuntu-cinnamon-macos-wave.png"
    if [ ! -f "$WALLPAPER_PATH" ]; then
        WALLPAPER_PATH="$SCRIPT_DIR/wallpapers/ubuntu-cinnamon-macos-wave.png"
    fi
    if [ -f "$WALLPAPER_PATH" ]; then
        set_setting org.cinnamon.desktop.background picture-uri "file://$WALLPAPER_PATH" "Cinnamon Wallpaper"
        set_setting org.cinnamon.desktop.background picture-options 'zoom' "Wallpaper Sizing"
        set_setting org.gnome.desktop.background picture-uri "file://$WALLPAPER_PATH" "GNOME Wallpaper"
        set_setting org.gnome.desktop.background picture-uri-dark "file://$WALLPAPER_PATH" "GNOME Dark Wallpaper"
    fi

    # 7. Typography (Prefer Ubuntu or SF Pro / Cantarell if installed)
    if command -v fc-list >/dev/null 2>&1 && fc-list : family | grep -iq "Ubuntu"; then
        set_setting org.cinnamon.desktop.interface font-name 'Ubuntu 10' "Interface Font"
        set_setting org.cinnamon.desktop.wm.preferences titlebar-font 'Ubuntu Bold 10' "Titlebar Font"
    fi

    # 8. Nemo File Manager consistency
    set_setting org.nemo.desktop show-desktop-icons true "Nemo Desktop Icons"
}

reload_cinnamon() {
    log_info "Reloading Cinnamon interface..."
    if pgrep -x "cinnamon" > /dev/null; then
        if command -v dbus-send >/dev/null 2>&1; then
            dbus-send --type=method_call --dest=org.Cinnamon /org/Cinnamon org.Cinnamon.Eval string:'global.reexec_self();' 2>/dev/null || true
        fi
        log_ok "Cinnamon reloaded seamlessly."
    else
        log_info "Cinnamon is not running in current session. Themes are registered and ready for Cinnamon startup."
    fi
}

install_grub() {
    log_info "Configuring GRUB Theme (1366x867)..."
    if [ "$EUID" -ne 0 ]; then
        log_warn "GRUB installation requires administrative privileges. Running with sudo..."
        sudo bash "$SCRIPT_DIR/apply.sh" --grub-internal
        return
    fi
    install_grub_internal
}

install_grub_internal() {
    GRUB_DEST="/boot/grub/themes/ubuntu-cinnamon"
    mkdir -p "$GRUB_DEST"
    cp -r "$SCRIPT_DIR/grub/ubuntu-cinnamon/"* "$GRUB_DEST/"

    if [ -f "/etc/default/grub" ]; then
        cp /etc/default/grub "/etc/default/grub.bak.$(date +%s)"
        if grep -q "^GRUB_THEME=" /etc/default/grub; then
            sed -i 's|^GRUB_THEME=.*|GRUB_THEME="/boot/grub/themes/ubuntu-cinnamon/theme.txt"|' /etc/default/grub
        else
            echo 'GRUB_THEME="/boot/grub/themes/ubuntu-cinnamon/theme.txt"' >> /etc/default/grub
        fi

        if command -v update-grub >/dev/null 2>&1; then
            update-grub
        elif command -v grub2-mkconfig >/dev/null 2>&1; then
            grub2-mkconfig -o /boot/grub2/grub.cfg 2>/dev/null || grub2-mkconfig -o /boot/efi/EFI/fedora/grub.cfg 2>/dev/null || true
        fi
        log_ok "GRUB theme installed and activated successfully!"
    else
        log_warn "/etc/default/grub not found. Files copied to $GRUB_DEST."
    fi
}

install_lightdm() {
    log_info "Configuring Slick Greeter (LightDM) login screen..."
    if [ "$EUID" -ne 0 ]; then
        log_warn "Login screen installation requires administrative privileges. Running with sudo..."
        sudo bash "$SCRIPT_DIR/apply.sh" --lightdm-internal
        return
    fi
    install_lightdm_internal
}

install_lightdm_internal() {
    mkdir -p /usr/share/themes /usr/share/icons /usr/share/backgrounds
    cp -r "$SCRIPT_DIR/$THEME_NAME" /usr/share/themes/
    cp -r "$SCRIPT_DIR/icons/$ICON_THEME_NAME" /usr/share/icons/
    cp "$SCRIPT_DIR/wallpapers/ubuntu-cinnamon-macos-wave.png" /usr/share/backgrounds/

    if [ -d "/etc/lightdm" ]; then
        cp "$SCRIPT_DIR/login-lockscreen/slick-greeter.conf" /etc/lightdm/slick-greeter.conf
        log_ok "Slick Greeter login screen configured."
    fi
}

# --- Main Entry Point ---
case "$1" in
    -h|--help)
        show_help
        ;;
    --traditional-layout)
        BUTTON_LAYOUT=":minimize,maximize,close"
        print_header
        install_theme_files
        apply_cinnamon_settings
        reload_cinnamon
        log_ok "Theme applied with traditional right-aligned window buttons."
        ;;
    --macos-layout)
        BUTTON_LAYOUT="close,minimize,maximize:"
        print_header
        install_theme_files
        apply_cinnamon_settings
        reload_cinnamon
        log_ok "Theme applied with macOS left-aligned traffic lights."
        ;;
    --restore)
        restore_defaults
        ;;
    --grub)
        install_grub
        exit 0
        ;;
    --grub-internal)
        install_grub_internal
        exit 0
        ;;
    --lightdm)
        install_lightdm
        exit 0
        ;;
    --lightdm-internal)
        install_lightdm_internal
        exit 0
        ;;
    --all)
        print_header
        install_theme_files
        apply_cinnamon_settings
        reload_cinnamon
        echo ""
        read -p "Would you also like to install the matching GRUB theme? (y/N): " -r
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            install_grub
        fi
        read -p "Would you also like to configure the Slick-Greeter login screen? (y/N): " -r
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            install_lightdm
        fi
        ;;
    *)
        print_header
        install_theme_files
        apply_cinnamon_settings
        reload_cinnamon
        echo ""
        log_ok "${BOLD}Ubuntu Cinnamon macOS Elegance Theme successfully applied!${NC}"
        echo -e "${GRAY}Window buttons set to macOS traffic lights (${BUTTON_LAYOUT})${NC}"
        echo -e "${GRAY}To use traditional right-aligned buttons, run: ${BOLD}./apply.sh --traditional-layout${NC}"
        echo -e "${GRAY}To apply the matching GRUB theme, run: ${BOLD}./apply.sh --grub${NC}"
        echo -e "${GRAY}To restore Mint defaults, run: ${BOLD}./apply.sh --restore${NC}\n"
        ;;
esac
