#!/usr/bin/env python3
"""
Start Menu: Native floating GTK Start Menu for Stark Shell.
"""

import os
import subprocess
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib
from .app_scanner import get_installed_apps

class StartMenu(Gtk.Window):
    def __init__(self, on_close_callback=None):
        super().__init__(type=Gtk.WindowType.TOPLEVEL)
        self.set_title("Stark Start Menu")
        self.set_default_size(560, 500)
        self.set_decorated(False)
        self.set_skip_taskbar_hint(True)
        self.set_skip_pager_hint(True)
        self.set_keep_above(True)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.get_style_context().add_class("stark-start-menu")
        self.on_close_callback = on_close_callback

        self.apps = get_installed_apps()
        self.filtered_apps = list(self.apps)

        self.build_ui()
        self.connect("focus-out-event", self.on_focus_out)
        self.connect("key-press-event", self.on_key_press)

    def build_ui(self):
        main_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=14)
        main_vbox.set_margin_top(16)
        main_vbox.set_margin_bottom(16)
        main_vbox.set_margin_start(16)
        main_vbox.set_margin_end(16)
        self.add(main_vbox)

        # Header / Brand
        header_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        brand_lbl = Gtk.Label()
        brand_lbl.set_markup("<span weight='bold' foreground='#00E5FF' font='11'>STARK INDUSTRIES // MARK LXXXV OS</span>")
        header_hbox.pack_start(brand_lbl, False, False, 0)
        main_vbox.pack_start(header_hbox, False, False, 0)

        # Search Entry
        self.search_entry = Gtk.Entry()
        self.search_entry.set_placeholder_text("Type to search applications or commands...")
        self.search_entry.get_style_context().add_class("start-search-entry")
        self.search_entry.connect("changed", self.on_search_changed)
        self.search_entry.connect("activate", self.on_search_activate)
        main_vbox.pack_start(self.search_entry, False, False, 0)

        # Applications Scroll Window
        scroll = Gtk.ScrolledWindow()
        scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scroll.set_min_content_height(320)

        self.apps_listbox = Gtk.ListBox()
        self.apps_listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        scroll.add(self.apps_listbox)
        main_vbox.pack_start(scroll, True, True, 0)

        self.populate_apps()

        # Footer User Profile & Power Controls
        footer_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        footer_box.get_style_context().add_class("start-footer")

        user_lbl = Gtk.Label()
        user_lbl.set_markup("<span weight='bold'>Tony Stark</span> <span foreground='#00E5FF' font='9'>[MR_Gray]</span>")
        footer_box.pack_start(user_lbl, False, False, 0)

        # Power actions
        power_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        
        lock_btn = Gtk.Button(label="🔒 Lock")
        lock_btn.get_style_context().add_class("stark-btn")
        lock_btn.connect("clicked", lambda b: self.exec_power("lock"))
        power_box.pack_start(lock_btn, False, False, 0)

        reboot_btn = Gtk.Button(label="🔄 Reboot")
        reboot_btn.get_style_context().add_class("stark-btn")
        reboot_btn.connect("clicked", lambda b: self.exec_power("reboot"))
        power_box.pack_start(reboot_btn, False, False, 0)

        power_btn = Gtk.Button(label="⏻ Shutdown")
        power_btn.get_style_context().add_class("stark-btn")
        power_btn.connect("clicked", lambda b: self.exec_power("poweroff"))
        power_box.pack_start(power_btn, False, False, 0)

        footer_box.pack_end(power_box, False, False, 0)
        main_vbox.pack_start(footer_box, False, False, 0)

    def populate_apps(self):
        # Clear existing
        for child in self.apps_listbox.get_children():
            child.destroy()

        for app in self.filtered_apps[:25]:
            row = Gtk.ListBoxRow()
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
            hbox.get_style_context().add_class("start-app-item")
            hbox.set_margin_top(2)
            hbox.set_margin_bottom(2)

            # Icon
            icon_img = Gtk.Image.new_from_icon_name(app.icon or "application-x-executable", Gtk.IconSize.LARGE_TOOLBAR)
            hbox.pack_start(icon_img, False, False, 0)

            # Labels
            vbox_text = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
            name_lbl = Gtk.Label(xalign=0)
            name_lbl.set_markup(f"<span weight='600'>{app.name}</span>")
            vbox_text.pack_start(name_lbl, False, False, 0)

            if app.comment:
                comment_lbl = Gtk.Label(xalign=0)
                comment_lbl.set_markup(f"<span font='9' foreground='#94A3B8'>{app.comment[:45]}</span>")
                vbox_text.pack_start(comment_lbl, False, False, 0)

            hbox.pack_start(vbox_text, True, True, 0)

            # Launch button
            btn = Gtk.Button(label="Open")
            btn.get_style_context().add_class("stark-btn")
            btn.connect("clicked", lambda b, a=app: self.launch_and_close(a))
            hbox.pack_end(btn, False, False, 0)

            row.add(hbox)
            self.apps_listbox.add(row)

        self.apps_listbox.show_all()

    def on_search_changed(self, entry):
        q = entry.get_text().strip().lower()
        if not q:
            self.filtered_apps = list(self.apps)
        else:
            self.filtered_apps = [a for a in self.apps if q in a.name.lower() or q in a.comment.lower() or q in a.exec_cmd.lower()]
        self.populate_apps()

    def on_search_activate(self, entry):
        if self.filtered_apps:
            self.launch_and_close(self.filtered_apps[0])

    def launch_and_close(self, app):
        app.launch()
        self.close_menu()

    def exec_power(self, action):
        self.close_menu()
        if action == "lock":
            subprocess.run("loginctl lock-session || xdg-screensaver lock", shell=True)
        elif action == "reboot":
            subprocess.run("systemctl reboot", shell=True)
        elif action == "poweroff":
            subprocess.run("systemctl poweroff", shell=True)

    def on_focus_out(self, widget, event):
        self.close_menu()
        return True

    def on_key_press(self, widget, event):
        if event.keyval == Gdk.KEY_Escape:
            self.close_menu()
            return True
        return False

    def close_menu(self):
        self.hide()
        if self.on_close_callback:
            self.on_close_callback()
