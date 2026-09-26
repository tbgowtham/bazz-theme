#!/usr/bin/env bash
# ==============================================================================
# eDEX-UI // LIQUID-GAS FLUID SHELL ENVIRONMENT
# ==============================================================================

if [[ $- == *i* ]]; then
    # Set default liquid cyan palette
    printf '\e]10;#00f0ff\a' 2>/dev/null || true
    printf '\e]11;#000c1e\a' 2>/dev/null || true
    printf '\e]12;#00f0ff\a' 2>/dev/null || true

    # Liquid-Gas Interactive Shell Prompt
    export PS1="\[\033[38;2;0;240;255m\][≋ LIQUID-GAS ≋] \[\033[38;2;0;255;136m\]\u@\h\[\033[0m\]:\[\033[38;2;0;180;255m\]\w\[\033[0m\]\$ "
fi

alias edex="edex-theme"
alias fluid="edex-theme --fluid"
alias condense="edex-theme --condense"
alias phase="edex-theme --phase"
