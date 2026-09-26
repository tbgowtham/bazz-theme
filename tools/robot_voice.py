#!/usr/bin/env python3
"""
eDEX-UI // ROBOTIC COMBAT AI VOICE SYNTHESIZER
Uses formant-shifted mechanical speech synthesis to voice onboard AI events.
"""

import os
import sys
import shutil
import subprocess

CONFIG_FILE = os.path.expanduser("~/.config/edex_voice.conf")

def is_voice_enabled():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                return f.read().strip() != "0"
        except Exception:
            pass
    return True

def set_voice_enabled(enabled=True):
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    with open(CONFIG_FILE, 'w') as f:
        f.write("1" if enabled else "0")

def speak(text, async_mode=True):
    """Speak text with mechanical robotic pitch and formant modulation."""
    if not is_voice_enabled():
        return False

    clean_text = text.replace('"', '').replace("'", "")
    
    # Priority 1: espeak-ng with mechanical pitch and speed
    if shutil.which("espeak-ng"):
        cmd = ["espeak-ng", "-v", "en-us", "-p", "18", "-s", "135", clean_text]
        if async_mode:
            subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True

    # Priority 2: spd-say with deep cybernetic pitch
    if shutil.which("spd-say"):
        cmd = ["spd-say", "-p", "-45", "-r", "-15", clean_text]
        if async_mode:
            subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True

    return False

if __name__ == "__main__":
    msg = sys.argv[1] if len(sys.argv) > 1 else "Mecha robotic systems fully operational."
    speak(msg, async_mode=False)
