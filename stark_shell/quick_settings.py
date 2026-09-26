#!/usr/bin/env python3
"""
Quick Settings / Action Center: Native GTK flyout with live volume and system toggles.
"""

import subprocess
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class QuickSettings(Gtk.Window):
    def __init__(self):
        super().__init__(type=Gtk.WindowType.TOPLEVEL)
        self.set_title("Stark Action Center")
        self.set_default_size(360, 320)
        self.set_decorated(False)
        self.set_skip_taskbar_hint(True)
        self.set_keep_above(True)
        self.set_position(Gtk.WindowPosition.MOUSE)

        self.get_style_context().add_class("stark-quick-settings")
        self.build_ui()
        self.connect("focus-out-event", lambda w, e: self.hide())
        self.connect("key-press-event", self.on_key)

    def build_ui(self):
        main_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=14)
        main_vbox.set_margin_top(16)
        main_vbox.set_margin_bottom(16)
        main_vbox.set_margin_start(16)
        main_vbox.set_margin_end(16)
        self.add(main_vbox)

        # Header
        lbl = Gtk.Label(xalign=0)
        lbl.set_markup("<span weight='bold' foreground='#00E5FF'>TACTICAL ACTION CENTER</span>")
        main_vbox.pack_start(lbl, False, False, 0)

        # 6 Toggles Grid
        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(10)
        grid.set_column_homogeneous(True)

        toggles = [
            ("📶 Wi-Fi", True),
            ("ᛒ Bluetooth", True),
            ("🛡️ Defense Grid", True),
            ("🌙 Night Light", False),
            ("⚡ Overdrive", True),
            ("✈️ Flight Mode", False)
        ]

        for i, (name, active) in enumerate(toggles):
            btn = Gtk.ToggleButton(label=name)
            btn.set_active(active)
            btn.get_style_context().add_class("quick-tile")
            if active:
                btn.get_style_context().add_class("active")
            btn.connect("toggled", self.on_tile_toggled)
            row = i // 3
            col = i % 3
            grid.attach(btn, col, row, 1, 1)

        main_vbox.pack_start(grid, False, False, 0)

        # Live Volume Slider (PipeWire / PulseAudio)
        vol_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        vol_lbl = Gtk.Label(label="Volume Output", xalign=0)
        vol_lbl.set_markup("<span weight='600' font='10'>AUDIO VOLUME</span>")
        vol_box.pack_start(vol_lbl, False, False, 0)

        self.vol_scale = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 100, 5)
        self.vol_scale.set_value(self.get_current_volume())
        self.vol_scale.connect("value-changed", self.on_vol_changed)
        vol_box.pack_start(self.vol_scale, False, False, 0)
        main_vbox.pack_start(vol_box, False, False, 0)

    def on_tile_toggled(self, btn):
        if btn.get_active():
            btn.get_style_context().add_class("active")
        else:
            btn.get_style_context().remove_class("active")

    def get_current_volume(self):
        try:
            out = subprocess.check_output("wpctl get-volume @DEFAULT_AUDIO_SINK@ 2>/dev/null", shell=True).decode()
            for part in out.split():
                try:
                    val = float(part)
                    return int(val * 100)
                except ValueError:
                    pass
        except Exception:
            pass
        return 75

    def on_vol_changed(self, scale):
        val = int(scale.get_value())
        frac = val / 100.0
        subprocess.run(f"wpctl set-volume @DEFAULT_AUDIO_SINK@ {frac:.2f} 2>/dev/null || pactl set-sink-volume @DEFAULT_SINK@ {val}% 2>/dev/null", shell=True)

    def on_key(self, w, event):
        if event.keyval == Gdk.KEY_Escape:
            self.hide()
            return True
        return False
