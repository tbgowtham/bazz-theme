#!/usr/bin/env bash
# ==============================================================================
# eDEX-UI // TRON Shell Environment Configuration
# ==============================================================================

if [[ $- == *i* ]]; then
    # Dynamically paint active terminal palette to eDEX Tron colors
    printf '\e]10;#00e5ff\a' 2>/dev/null || true
    printf '\e]11;#000b1e\a' 2>/dev/null || true
    printf '\e]12;#00e5ff\a' 2>/dev/null || true

    # Tron Interactive Shell Prompt
    export PS1="\[\033[38;2;0;229;255m\][eDEX-UI // TRON] \[\033[38;2;0;255;136m\]\u@\h\[\033[0m\]:\[\033[38;2;0;180;255m\]\w\[\033[0m\]\$ "
fi

alias edex="edex-theme"
