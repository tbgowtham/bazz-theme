#!/usr/bin/env bash
# ==============================================================================
# eDEX-UI // ROBOTIC MECHA & LIQUID-GAS SYSTEM CONTROLLER
# ==============================================================================
# Applies the full Robotic Mecha & Liquid-Gas futuristic theme:
# - Fullscreen Biometric Robotic Screen Locker (`./apply.sh lock`)
# - Robotic AI Voice Synthesizer & Mechanical Audio Suite
# - KDE Plasma 6 Mecha Robotic Color Scheme (`eDEX-TRON-Mecha`)
# - Mecha Hardware & Security Diagnostic Scanner (`./apply.sh diag`)
# - 2D Liquid-Gas Fluid Dynamics Reactor (`./apply.sh fluid`)
# - Matter Phase Shifting (Mecha, Cryo, Plasma, Mercury, Solar)
# - Konsole Terminal Profile & Colorscheme
# - Active Terminal OSC Palette Shift (Core Cyan / Titanium Black)
# - Interactive Shell Prompt ([⚙ MECHA-ROBOTIC ⚙])
# - Fluid Mecha GTK 3/4 & Metacity Themes
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EDEX_BIN="${SCRIPT_DIR}/edex-theme"

# Forward execution to the master edex-theme CLI engine
exec "${EDEX_BIN}" "$@"
