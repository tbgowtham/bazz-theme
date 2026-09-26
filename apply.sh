#!/usr/bin/env bash
# ==============================================================================
# macOS-Cupertino // LUXURY DESKTOP SHELL CONTROLLER
# ==============================================================================
# Reconstructs the Linux desktop into an elegant macOS (Sonoma/Sequoia)
# & Catppuccin Macchiato environment:
# - Apple SF Pro Display & Inter Typography
# - Translucent Frosted Glass (Zero neon blue, zero dark blue HUD)
# - Big Elegant Action Menu (macOS Spotlight & Launchpad style)
# - macOS Traffic Light Window Controls (🔴 Close, 🟡 Minimize, 🟢 Maximize)
# - FreeDesktop Squircle Icon Theme
# - KDE Plasma 6, Cinnamon, GTK 3/4, & Konsole Theme Integration
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" && pwd)"
MACOS_INSTALLER="${SCRIPT_DIR}/tools/apply_macos_theme.py"

# Forward execution to the macOS luxury theme installer
exec python3 "${MACOS_INSTALLER}" "$@"
