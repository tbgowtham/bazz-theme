#!/usr/bin/env bash
# ==============================================================================
# macOS-Cupertino // LUXURY SHELL ENVIRONMENT
# Typography: Apple SF Pro & Inter
# Palette: Catppuccin Macchiato & macOS Sonoma Dark
# ==============================================================================

if [[ $- == *i* ]]; then
    # Set elegant macOS / Catppuccin dark palette
    printf '\e]10;#f5f5f7\a' 2>/dev/null || true
    printf '\e]11;#1e1e2e\a' 2>/dev/null || true
    printf '\e]12;#89b4fa\a' 2>/dev/null || true

    # Elegant Minimal macOS Terminal Prompt
    export PS1="\[\033[38;2;137;180;250m\] \[\033[38;2;205;214;244m\]\w \[\033[38;2;166;227;161m\]❯\[\033[0m\] "
fi
