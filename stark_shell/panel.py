#!/usr/bin/env python3
"""
Stark Shell Panel: The master native Linux desktop taskbar dock.
Anchors to the bottom of the screen via GtkLayerShell (Wayland) or X11 dock struts.
"""

import os
import sys
import time
import subprocess
import psutil
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
try:
    gi.require_version('GtkLayerShell', '0.1')
    from gi.repository import GtkLayerShell
    HAS_LAYER_SHELL = True
except Exception:
    HAS_LAYER_SHELL = False

from gi.repository import Gtk, Gdk, GLib
from .start_menu import StartMenu
from .quick_settings import QuickSettings

class StarkPanel(Gtk.Window):
    def __init__(self):
        super().__init__(type=Gtk.WindowType.TOPLEVEL)
        self.set_title("macOS Dock & Menubar")
        self.set_default_size(1366, 48)
        self.set_decorated(False)
        self.set_skip_taskbar_hint(True)
        self.set_skip_pager_hint(True)

        self.get_style_context().add_class("stark-panel")

        # LayerShell / Wayland anchoring
        if HAS_LAYER_SHELL:
            GtkLayerShell.init_for_window(self)
            GtkLayerShell.set_layer(self, GtkLayerShell.Layer.TOP)
            GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.BOTTOM, True)
            GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.LEFT, True)
            GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.RIGHT, True)
            GtkLayerShell.set_exclusive_zone(self, 48)
            GtkLayerShell.set_namespace(self, "macos-shell-panel")
        else:
            self.set_type_hint(Gdk.WindowTypeHint.DOCK)

        # Flyout Windows
        self.start_menu = StartMenu()
        self.quick_settings = QuickSettings()

        self.build_ui()
        self.start_timers()

    def build_ui(self):
        # Master Horizontal Container with 3 Sections: Left, Center, Right
        master_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        master_box.set_hexpand(True)
        self.add(master_box)

        # -------------------------------------------------------------
        # 1. Left Section: macOS Apple Menu & Status
        # -------------------------------------------------------------
        left_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        left_box.set_size_request(220, 48)

        hud_btn = Gtk.Button()
        hud_btn.get_style_context().add_class("stark-btn")
        hud_lbl = Gtk.Label()
        hud_lbl.set_markup("<span font='11' weight='bold' foreground='#cdd6f4'></span> <span font='10' weight='medium' foreground='#f5f5f7'>Finder</span>")
        hud_btn.add(hud_lbl)
        hud_btn.connect("clicked", lambda b: self.start_menu.present())
        left_box.pack_start(hud_btn, False, False, 6)

        master_box.pack_start(left_box, False, False, 0)

        # -------------------------------------------------------------
        # 2. Center Section: Windows 11 Centered Dock
        # -------------------------------------------------------------
        center_align = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        center_align.set_hexpand(True)
        center_align.set_halign(Gtk.Align.CENTER)

        center_dock = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        center_dock.set_valign(Gtk.Align.CENTER)

        # Start Button (Arc Reactor Logo)
        start_btn = Gtk.Button(label="⚛")
        start_btn.get_style_context().add_class("stark-start-btn")
        start_btn.set_tooltip_text("Start Menu (Super / Windows Key)")
        start_btn.connect("clicked", self.toggle_start_menu)
        center_dock.pack_start(start_btn, False, False, 0)

        # Search Button
        search_btn = Gtk.Button(label="🔍")
        search_btn.get_style_context().add_class("stark-btn")
        search_btn.set_tooltip_text("Search Apps & Commands")
        search_btn.connect("clicked", self.toggle_start_menu)
        center_dock.pack_start(search_btn, False, False, 0)

        # Pinned Core Apps
        pinned = [
            ("terminal", "Tactical Terminal", "x-terminal-emulator || konsole || kitty"),
            ("system-file-manager", "File Explorer", "nemo || dolphin || nautilus"),
            ("web-browser", "Web Browser", "firefox || google-chrome"),
            ("preferences-system", "System Settings", "systemsettings || cinnamon-settings"),
            ("utilities-system-monitor", "Diagnostics", "plasma-systemmonitor || gnome-system-monitor")
        ]

        for icon_name, tooltip, cmd in pinned:
            btn = Gtk.Button()
            btn.get_style_context().add_class("stark-btn")
            btn.set_tooltip_text(tooltip)
            img = Gtk.Image.new_from_icon_name(icon_name, Gtk.IconSize.LARGE_TOOLBAR)
            btn.add(img)
            btn.connect("clicked", lambda b, c=cmd: subprocess.Popen(c, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL))
            center_dock.pack_start(btn, False, False, 0)

        # macOS Spotlight Button
        spotlight_btn = Gtk.Button(label="🔍")
        spotlight_btn.get_style_context().add_class("stark-btn")
        spotlight_btn.set_tooltip_text("Spotlight Search")
        spotlight_btn.connect("clicked", lambda b: self.start_menu.present())
        center_dock.pack_start(spotlight_btn, False, False, 0)

        center_align.pack_start(center_dock, False, False, 0)
        master_box.pack_start(center_align, True, True, 0)

        # -------------------------------------------------------------
        # 3. Right Section: System Tray & Clock
        # -------------------------------------------------------------
        right_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        right_box.set_size_request(280, 48)
        right_box.set_halign(Gtk.Align.END)

        # Real CPU Meter Badge
        self.cpu_badge = Gtk.Label()
        self.cpu_badge.get_style_context().add_class("tray-badge")
        self.cpu_badge.set_markup("<span font='9'>CPU <b>--%</b></span>")
        right_box.pack_start(self.cpu_badge, False, False, 0)

        # Real RAM Meter Badge
        self.mem_badge = Gtk.Label()
        self.mem_badge.get_style_context().add_class("tray-badge")
        self.mem_badge.set_markup("<span font='9'>RAM <b>--%</b></span>")
        right_box.pack_start(self.mem_badge, False, False, 0)

        # Quick Settings Trigger (Volume, Wi-Fi)
        tray_btn = Gtk.Button()
        tray_btn.get_style_context().add_class("stark-btn")
        tray_btn.set_tooltip_text("Quick Settings & Action Center")
        self.vol_lbl = Gtk.Label()
        self.vol_lbl.set_markup("<span font='9'>🔊 📶</span>")
        tray_btn.add(self.vol_lbl)
        tray_btn.connect("clicked", lambda b: self.quick_settings.present())
        right_box.pack_start(tray_btn, False, False, 0)

        # Windows 11 Two-Line Clock & Date
        clock_box = Gtk.Button()
        clock_box.get_style_context().add_class("clock-btn")
        clock_box.set_relief(Gtk.ReliefStyle.NONE)
        clock_box.set_tooltip_text("Calendar & Notifications")

        vbox_clock = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        vbox_clock.set_valign(Gtk.Align.CENTER)
        self.clock_time = Gtk.Label(xalign=1)
        self.clock_date = Gtk.Label(xalign=1)
        vbox_clock.pack_start(self.clock_time, False, False, 0)
        vbox_clock.pack_start(self.clock_date, False, False, 0)
        clock_box.add(vbox_clock)
        right_box.pack_start(clock_box, False, False, 0)

        # Show Desktop Slice (Far right edge)
        slice_btn = Gtk.Button()
        slice_btn.set_size_request(8, 32)
        slice_btn.get_style_context().add_class("stark-btn")
        slice_btn.set_tooltip_text("Show Desktop")
        slice_btn.connect("clicked", lambda b: subprocess.run("qdbus-qt6 org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.setDashboardShown true 2>/dev/null || xdotool key super+d 2>/dev/null", shell=True))
        right_box.pack_start(slice_btn, False, False, 2)

        master_box.pack_end(right_box, False, False, 6)

    def toggle_start_menu(self, btn=None):
        if self.start_menu.get_visible():
            self.start_menu.hide()
        else:
            self.start_menu.present()

    def start_timers(self):
        # Update clock every 1 second
        self.update_clock()
        GLib.timeout_add_seconds(1, self.update_clock)

        # Update telemetry badges every 1.5 seconds
        self.update_telemetry()
        GLib.timeout_add(1500, self.update_telemetry)

    def update_clock(self):
        now = time.localtime()
        t_str = time.strftime("%H:%M", now)
        d_str = time.strftime("%d/%m/%Y", now)
        self.clock_time.set_markup(f"<span font='10' weight='bold'>{t_str}</span>")
        self.clock_date.set_markup(f"<span font='8' foreground='#94A3B8'>{d_str}</span>")
        return True

    def update_telemetry(self):
        try:
            cpu = psutil.cpu_percent(interval=None)
            mem = psutil.virtual_memory().percent
            c_color = "#00E5FF" if cpu < 70 else "#FF2A5F"
            m_color = "#00FF88" if mem < 80 else "#FFB703"

            self.cpu_badge.set_markup(f"<span font='9'>CPU <span foreground='{c_color}'><b>{int(cpu)}%</b></span></span>")
            self.mem_badge.set_markup(f"<span font='9'>RAM <span foreground='{m_color}'><b>{int(mem)}%</b></span></span>")
        except Exception:
            pass
        return True
