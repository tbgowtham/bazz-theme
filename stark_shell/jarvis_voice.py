#!/usr/bin/env python3
"""
Jarvis Voice Assistant: High-tech native voice dialog for Stark Shell.
"""

import subprocess
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class JarvisVoiceDialog(Gtk.Window):
    def __init__(self):
        super().__init__(type=Gtk.WindowType.TOPLEVEL)
        self.set_title("J.A.R.V.I.S. Core Assistant")
        self.set_default_size(500, 320)
        self.set_decorated(False)
        self.set_skip_taskbar_hint(True)
        self.set_keep_above(True)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.get_style_context().add_class("stark-start-menu")
        self.build_ui()
        self.connect("focus-out-event", lambda w, e: self.hide())
        self.connect("key-press-event", self.on_key)

    def build_ui(self):
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_margin_top(16)
        vbox.set_margin_bottom(16)
        vbox.set_margin_start(16)
        vbox.set_margin_end(16)
        self.add(vbox)

        # Header
        top_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        lbl = Gtk.Label()
        lbl.set_markup("<span weight='bold' foreground='#00E5FF' font='12'>J.A.R.V.I.S. // TACTICAL ASSISTANT</span>")
        top_hbox.pack_start(lbl, False, False, 0)
        vbox.pack_start(top_hbox, False, False, 0)

        # Response display area
        self.output_lbl = Gtk.Label()
        self.output_lbl.set_markup("<span font='10' foreground='#CBD5E1'>At your service, sir. Mark LXXXV nanotech systems, Linux telemetry, and Windows 11 shell integration are fully operational.</span>")
        self.output_lbl.set_line_wrap(True)
        self.output_lbl.set_max_width_chars(50)
        vbox.pack_start(self.output_lbl, True, True, 0)

        # Input
        self.entry = Gtk.Entry()
        self.entry.set_placeholder_text("Speak or type a command (e.g. status, scan, lock, terminal)...")
        self.entry.get_style_context().add_class("start-search-entry")
        self.entry.connect("activate", self.on_command)
        vbox.pack_start(self.entry, False, False, 0)

    def on_command(self, entry):
        text = entry.get_text().strip()
        if not text:
            return
        entry.set_text("")
        self.process_command(text)

    def process_command(self, query):
        q = query.lower()
        response = ""

        if "status" in q:
            response = "All systems operating at peak efficiency. Arc reactor output is steady at 3.42 Gigawatts with 99.9% core stability."
        elif "scan" in q:
            response = "Perimeter sensor scan complete. Zero anomalous kinetic signatures detected."
        elif "lock" in q:
            response = "Locking desktop security perimeter."
            subprocess.run("loginctl lock-session || xdg-screensaver lock", shell=True)
        elif "terminal" in q:
            response = "Launching tactical terminal shell."
            subprocess.Popen(["x-terminal-emulator"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif "cinnamon" in q or "compare" in q:
            response = "This native shell combines Cinnamon dock stability with Windows 11 centered aesthetics and Tony Stark telemetry."
        else:
            response = f"Command '{query}' executed, sir. System parameters nominal."

        self.output_lbl.set_markup(f"<span font='10' foreground='#00E5FF'><b>Jarvis:</b></span> <span font='10' foreground='#F0F6FC'>{response}</span>")
        self.speak(response)

    def speak(self, text):
        try:
            subprocess.Popen(["spd-say", "-r", "10", text], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            try:
                subprocess.Popen(["espeak-ng", text], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except Exception:
                pass

    def on_key(self, w, event):
        if event.keyval == Gdk.KEY_Escape:
            self.hide()
            return True
        return False
