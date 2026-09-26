#!/usr/bin/env bash
# ==============================================================================
# eDEX-UI // TRON SYSTEM-WIDE THEME & SHELL CONTROLLER
# ==============================================================================
# Applies the full eDEX-UI Tron desktop theme:
# - Live OS Telemetry Wallpaper (CPU cores, RAM, storage, network, radar, cyber-deck)
# - Real-time Background Daemon
# - KDE Plasma 6 eDEX-TRON Color Scheme
# - Konsole Terminal Profile & Colorscheme
# - Active Terminal OSC Palette Shift
# - Shell Prompt ([eDEX-UI // TRON])
# - Optional Interactive Live TUI Monitor (`./apply.sh --app`)
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EDEX_BIN="${SCRIPT_DIR}/edex-theme"

# Forward execution to the master edex-theme CLI engine
exec "${EDEX_BIN}" "$@"
