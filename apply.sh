#!/usr/bin/env bash
# ==============================================================================
# eDEX-UI // TRON SYSTEM-WIDE THEME & SHELL CONTROLLER
# ==============================================================================
# Applies the full eDEX-UI Tron desktop theme:
# - KDE Plasma 6 eDEX-TRON Color Scheme
# - Konsole Terminal Profile & Colorscheme
# - Active Terminal OSC Palette Shift (Neon Cyan / Deep Navy)
# - Interactive Shell Prompt ([eDEX-UI // TRON])
# - GTK 3/4 & Metacity Neon Cyan Borders
# - Jarvis-White Minimalist Vector Icon Theme
# - Audio Chime Feedback
# - Optional Interactive Live TUI Monitor (`./apply.sh --app`)
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EDEX_BIN="${SCRIPT_DIR}/edex-theme"

# Forward execution to the master edex-theme CLI engine
exec "${EDEX_BIN}" "$@"
