#!/usr/bin/env python3
"""
App Scanner: Discovers installed Linux desktop applications from .desktop files.
"""

import os
import glob
import subprocess

class DesktopApp:
    def __init__(self, name, exec_cmd, icon, comment="", path=""):
        self.name = name
        self.exec_cmd = exec_cmd
        self.icon = icon
        self.comment = comment
        self.path = path

    def launch(self):
        try:
            # Clean exec command (remove %u, %F, etc.)
            cmd = self.exec_cmd.split()
            clean_cmd = [arg for arg in cmd if not arg.startswith('%')]
            subprocess.Popen(clean_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return True
        except Exception as e:
            print(f"[STARK SHELL]: Failed to launch {self.name}: {e}")
            return False

def get_installed_apps():
    apps = []
    seen = set()
    dirs = [
        "/usr/share/applications",
        os.path.expanduser("~/.local/share/applications")
    ]

    for d in dirs:
        if not os.path.exists(d):
            continue
        for f in glob.glob(os.path.join(d, "*.desktop")):
            try:
                name, exec_cmd, icon, comment = "", "", "", ""
                nodisplay = False
                in_desktop_entry = False

                with open(f, "r", encoding="utf-8", errors="ignore") as fp:
                    for line in fp:
                        line = line.strip()
                        if line == "[Desktop Entry]":
                            in_desktop_entry = True
                            continue
                        elif line.startswith("[") and line.endswith("]"):
                            in_desktop_entry = False
                            continue

                        if in_desktop_entry:
                            if line.startswith("Name=") and not name:
                                name = line.split("=", 1)[1]
                            elif line.startswith("Exec=") and not exec_cmd:
                                exec_cmd = line.split("=", 1)[1]
                            elif line.startswith("Icon=") and not icon:
                                icon = line.split("=", 1)[1]
                            elif line.startswith("Comment=") and not comment:
                                comment = line.split("=", 1)[1]
                            elif line.startswith("NoDisplay=true"):
                                nodisplay = True

                if name and exec_cmd and not nodisplay and name not in seen:
                    seen.add(name)
                    apps.append(DesktopApp(name, exec_cmd, icon, comment, f))
            except Exception:
                pass

    return sorted(apps, key=lambda a: a.name.lower())
