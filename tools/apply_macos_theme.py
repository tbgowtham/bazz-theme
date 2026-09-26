#!/usr/bin/env python3
"""
==============================================================================
macOS-Cupertino // LUXURY DESKTOP RECONSTRUCTION CONTROLLER
==============================================================================
Reconstructs the Linux desktop environment into an authentic, elegant macOS
(Sonoma / Sequoia) & Catppuccin Macchiato experience:
- Apple SF Pro Display & Inter Typography
- Sleek Frosted Acrylic Glassmorphism (No neon blue, no cyber lines)
- Big Elegant Action / Spotlight Menu
- Authentic macOS Traffic Light Window Controls
- FreeDesktop Squircle Icon Theme
- Native KDE Plasma 6 Wayland & GTK 3/4 Integration
==============================================================================
"""

import os
import sys
import shutil
import subprocess
import configparser

SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
TOOLS_DIR = os.path.join(SCRIPT_DIR, "tools")
HOME = os.path.expanduser("~")

THEME_NAME = "macOS-Cupertino"
ICON_NAME = "macOS-Cupertino"
COLOR_SCHEME = "macOS-Catppuccin"

# Destinations
THEMES_USER = os.path.join(HOME, ".themes", THEME_NAME)
THEMES_LOCAL = os.path.join(HOME, ".local/share/themes", THEME_NAME)
ICONS_USER = os.path.join(HOME, ".icons", ICON_NAME)
ICONS_LOCAL = os.path.join(HOME, ".local/share/icons", ICON_NAME)
KDE_SCHEMES_DIR = os.path.join(HOME, ".local/share/color-schemes")
KONSOLE_DIR = os.path.join(HOME, ".local/share/konsole")
FONTS_DIR = os.path.join(HOME, ".local/share/fonts")
BASHRC_D = os.path.join(HOME, ".bashrc.d")

# ANSI Terminal Colors
RESET = "\033[0m"
BOLD = "\033[1m"
BLUE = "\033[38;2;137;180;250m"
LAVENDER = "\033[38;2;180;190;254m"
GREEN = "\033[38;2;166;227;161m"
WHITE = "\033[38;2;245;245;247m"
DIM = "\033[38;2;166;173;200m"

def print_banner():
    print(f"""
{BLUE}╔══════════════════════════════════════════════════════════════════════════════╗
║   macOS-Cupertino // LUXURY DESKTOP SUITE RECONSTRUCTION                   ║
║  Sonoma & Sequoia Frosted Glass  •  Catppuccin Macchiato  •  SF Pro Font   ║
╚══════════════════════════════════════════════════════════════════════════════╝{RESET}
""")

def install_fonts():
    print(f"{BLUE}[1/7] Configuring Apple SF Pro Display & Inter Typography...{RESET}")
    # Run font cache update
    subprocess.run(["fc-cache", "-f", FONTS_DIR], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Configure KDE Plasma Fonts via kwriteconfig
    kw = shutil.which("kwriteconfig6") or shutil.which("kwriteconfig5")
    if kw:
        fonts = {
            "font": "SF Pro Display,11,-1,5,50,0,0,0,0,0",
            "fixed": "Inter,11,-1,5,50,0,0,0,0,0",
            "menuFont": "SF Pro Display,11,-1,5,50,0,0,0,0,0",
            "smallestReadableFont": "SF Pro Text,9,-1,5,50,0,0,0,0,0",
            "toolBarFont": "SF Pro Display,11,-1,5,50,0,0,0,0,0",
            "windowTitleFont": "SF Pro Display,12,-1,5,60,0,0,0,0,0"
        }
        for k, v in fonts.items():
            subprocess.run([kw, "--file", "kdeglobals", "--group", "General", "--key", k, v], check=False)
    print(f" {GREEN}✓ Apple SF Pro Display (11pt UI, 12pt Titles) active in KDE Plasma{RESET}")

def install_icons():
    print(f"{BLUE}[2/7] Generating & Installing macOS Squircle Icon Theme...{RESET}")
    # Run icon generator
    gen_script = os.path.join(TOOLS_DIR, "generate_macos_icons.py")
    subprocess.run([sys.executable, gen_script], stdout=subprocess.DEVNULL, check=True)
    
    src_icons = os.path.join(SCRIPT_DIR, "icons", ICON_NAME)
    for dest in [ICONS_USER, ICONS_LOCAL]:
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        if os.path.exists(dest):
            shutil.rmtree(dest)
        shutil.copytree(src_icons, dest)
    
    subprocess.run(["gtk-update-icon-cache", "-f", "-t", ICONS_LOCAL], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f" {GREEN}✓ Installed macOS-Cupertino squircle icons into ~/.icons and ~/.local/share/icons{RESET}")

def install_desktop_theme():
    print(f"{BLUE}[3/7] Assembling macOS Frosted Glass & Traffic Lights Theme...{RESET}")
    for dest in [THEMES_USER, THEMES_LOCAL]:
        os.makedirs(dest, exist_ok=True)
        for folder in ["cinnamon", "gtk-3.0", "gtk-4.0", "metacity-1"]:
            src_f = os.path.join(SCRIPT_DIR, folder)
            dst_f = os.path.join(dest, folder)
            if os.path.exists(dst_f):
                shutil.rmtree(dst_f)
            if os.path.exists(src_f):
                shutil.copytree(src_f, dst_f)
        
        # Copy index.theme
        idx_src = os.path.join(SCRIPT_DIR, "index.theme")
        if os.path.exists(idx_src):
            shutil.copyfile(idx_src, os.path.join(dest, "index.theme"))
    print(f" {GREEN}✓ Installed macOS-Cupertino to ~/.themes/ and ~/.local/share/themes/{RESET}")

def configure_kde_plasma():
    print(f"{BLUE}[4/7] Applying KDE Plasma 6 macOS-Catppuccin Color Scheme...{RESET}")
    os.makedirs(KDE_SCHEMES_DIR, exist_ok=True)
    for scheme in ["macOS-Cupertino.colors", "macOS-Catppuccin.colors"]:
        src = os.path.join(TOOLS_DIR, scheme)
        dst = os.path.join(KDE_SCHEMES_DIR, scheme)
        if os.path.exists(src):
            shutil.copyfile(src, dst)
    
    kw = shutil.which("kwriteconfig6") or shutil.which("kwriteconfig5")
    if kw:
        try:
            subprocess.run([kw, "--file", "kdeglobals", "--group", "General", "--key", "accentColor", "137,180,250"], check=False)
            subprocess.run([kw, "--file", "kdeglobals", "--group", "Icons", "--key", "Theme", ICON_NAME], check=False)
        except Exception:
            pass

    if shutil.which("plasma-apply-colorscheme"):
        try:
            subprocess.run(["plasma-apply-colorscheme", COLOR_SCHEME], check=False)
            print(f" {GREEN}✓ Activated '{COLOR_SCHEME}' across KDE Plasma desktop{RESET}")
        except Exception:
            pass

def configure_konsole():
    print(f"{BLUE}[5/7] Configuring Konsole & Apple Terminal Colors...{RESET}")
    os.makedirs(KONSOLE_DIR, exist_ok=True)
    
    for fname in ["macOS-Catppuccin.colorscheme", "macOS.profile"]:
        src = os.path.join(TOOLS_DIR, fname)
        dst = os.path.join(KONSOLE_DIR, fname)
        if os.path.exists(src):
            shutil.copyfile(src, dst)
    
    # Configure konsolerc default profile
    konsolerc = os.path.join(HOME, ".config/konsolerc")
    if os.path.exists(konsolerc):
        cfg = configparser.ConfigParser(interpolation=None)
        cfg.read(konsolerc)
        if "Desktop Entry" not in cfg:
            cfg["Desktop Entry"] = {}
        cfg["Desktop Entry"]["DefaultProfile"] = "macOS-Cupertino.profile"
        with open(konsolerc, "w") as f:
            cfg.write(f)
    print(f" {GREEN}✓ Set Konsole profile to 'macOS-Cupertino' with Inter typography{RESET}")

def configure_gtk_and_cinnamon():
    print(f"{BLUE}[6/7] Setting GTK 3/4 & Desktop Environment Settings...{RESET}")
    # GTK 3 & GTK 4 settings.ini
    for gtk_dir in [os.path.join(HOME, ".config/gtk-3.0"), os.path.join(HOME, ".config/gtk-4.0")]:
        os.makedirs(gtk_dir, exist_ok=True)
        ini_file = os.path.join(gtk_dir, "settings.ini")
        cfg = configparser.ConfigParser(interpolation=None)
        if os.path.exists(ini_file):
            cfg.read(ini_file)
        if "Settings" not in cfg:
            cfg["Settings"] = {}
        cfg["Settings"]["gtk-theme-name"] = THEME_NAME
        cfg["Settings"]["gtk-icon-theme-name"] = ICON_NAME
        cfg["Settings"]["gtk-font-name"] = "SF Pro Display 11"
        cfg["Settings"]["gtk-application-prefer-dark-theme"] = "1"
        with open(ini_file, "w") as f:
            cfg.write(f)
    
    # Cinnamon / GNOME gsettings
    if shutil.which("gsettings"):
        cmds = [
            ["gsettings", "set", "org.cinnamon.theme", "name", THEME_NAME],
            ["gsettings", "set", "org.cinnamon.desktop.interface", "gtk-theme", THEME_NAME],
            ["gsettings", "set", "org.cinnamon.desktop.interface", "icon-theme", ICON_NAME],
            ["gsettings", "set", "org.cinnamon.desktop.interface", "font-name", "SF Pro Display 11"],
            ["gsettings", "set", "org.cinnamon.desktop.wm.preferences", "theme", THEME_NAME],
            ["gsettings", "set", "org.cinnamon.desktop.wm.preferences", "button-layout", "close,minimize,maximize:"],
            ["gsettings", "set", "org.gnome.desktop.interface", "gtk-theme", THEME_NAME],
            ["gsettings", "set", "org.gnome.desktop.interface", "icon-theme", ICON_NAME],
            ["gsettings", "set", "org.gnome.desktop.interface", "font-name", "SF Pro Display 11"],
            ["gsettings", "set", "org.gnome.desktop.interface", "color-scheme", "prefer-dark"],
        ]
        for cmd in cmds:
            try:
                subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except Exception:
                pass
    print(f" {GREEN}✓ Configured GTK 3/4, window button layout, and Cinnamon interface{RESET}")

def configure_shell_env():
    print(f"{BLUE}[7/7] Activating Clean macOS Terminal Prompt & Palette...{RESET}")
    os.makedirs(BASHRC_D, exist_ok=True)
    
    # Remove old edex-theme.sh if present
    old_sh = os.path.join(BASHRC_D, "edex-theme.sh")
    if os.path.exists(old_sh):
        os.remove(old_sh)
    
    src_sh = os.path.join(TOOLS_DIR, "macos-theme.sh")
    dst_sh = os.path.join(BASHRC_D, "macos-theme.sh")
    shutil.copyfile(src_sh, dst_sh)
    os.chmod(dst_sh, 0o755)
    
    # Shift active terminal OSC palette immediately
    # Foreground: #f5f5f7, Background: #1e1e2e, Cursor: #89b4fa
    sys.stdout.write("\033]10;#f5f5f7\007")
    sys.stdout.write("\033]11;#1e1e2e\007")
    sys.stdout.write("\033]12;#89b4fa\007")
    sys.stdout.flush()
    print(f" {GREEN}✓ Active terminal palette shifted to macOS dark slate & white{RESET}")

def main():
    print_banner()
    install_fonts()
    install_icons()
    install_desktop_theme()
    configure_kde_plasma()
    configure_konsole()
    configure_gtk_and_cinnamon()
    configure_shell_env()
    
    print(f"""
{GREEN}{BOLD}══════════════════════════════════════════════════════════════════════════════
✓ SUCCESS: macOS-Cupertino & Catppuccin Macchiato Suite Fully Reconstructed!
══════════════════════════════════════════════════════════════════════════════{RESET}

{WHITE}Aesthetics Applied:{RESET}
 • {LAVENDER}Typography{RESET}      : Apple SF Pro Display (11pt UI, 12pt Titles) & Inter (11pt Monospace)
 • {LAVENDER}Panel & Menus{RESET}   : macOS Frosted Acrylic Glass (No neon blue, no dark blue HUD)
 • {LAVENDER}Action Menu{RESET}     : Big, spacious macOS Spotlight search & rounded pill categories
 • {LAVENDER}Window Controls{RESET} : Authentic macOS Traffic Lights (🔴 Close, 🟡 Minimize, 🟢 Maximize)
 • {LAVENDER}Icons{RESET}           : macOS Sonoma & Sequoia Luxury Squircle Icons
 • {LAVENDER}Color Palette{RESET}   : Catppuccin Macchiato & macOS Cupertino Dark Slate
 • {LAVENDER}Terminal{RESET}        : Apple Terminal palette with clean prompt:  ~/path ❯
""")

if __name__ == "__main__":
    main()
