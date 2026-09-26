#!/usr/bin/env python3
"""
STARK SHELL: Master Native Linux Desktop Shell Entrypoint
"""

import os
import sys
import signal
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk, Gdk, GLib
from .panel import StarkPanel

def apply_gtk_styles():
    style_path = os.path.join(os.path.dirname(__file__), "style.css")
    if os.path.exists(style_path):
        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        try:
            provider.load_from_path(style_path)
            Gtk.StyleContext.add_provider_for_screen(
                screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
            )
        except Exception as e:
            print(f"[STARK SHELL]: Warning loading CSS: {e}")

def main():
    print("[STARK SHELL]: Initializing native Linux Desktop Shell...")
    apply_gtk_styles()

    panel = StarkPanel()
    panel.show_all()

    # Graceful exit on Ctrl+C or kill
    signal.signal(signal.SIGINT, lambda *args: Gtk.main_quit())
    signal.signal(signal.SIGTERM, lambda *args: Gtk.main_quit())

    # Periodic GLib pulse for signal handling
    GLib.timeout_add(500, lambda: True)

    print("[STARK SHELL]: Native desktop shell is online.")
    Gtk.main()

if __name__ == "__main__":
    main()
