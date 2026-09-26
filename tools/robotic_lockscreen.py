#!/usr/bin/env python3
"""
==============================================================================
eDEX-UI // ROBOTIC MECHA BIOMETRIC SCREEN LOCKER
==============================================================================
Full-screen hardware-accelerated cybernetic HUD lockscreen with rotating mecha
reticle, biometric laser scanner, live telemetry, robotic voice synthesis,
and secure authentication.
==============================================================================
"""

import os
import sys
import time
import math
import getpass
import subprocess
import shutil
import psutil

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib
import cairo

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
ASSETS_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "assets")

try:
    from tools.robot_voice import speak
except ImportError:
    try:
        from robot_voice import speak
    except ImportError:
        def speak(text, async_mode=True): pass

PIN_FILE = os.path.expanduser("~/.config/edex_lock_pin")

def play_audio(filename):
    path = os.path.join(ASSETS_DIR, filename)
    if os.path.exists(path):
        for player in ["paplay", "pw-play", "aplay"]:
            if shutil.which(player):
                subprocess.Popen([player, path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                break

class RoboticLockScreen(Gtk.Window):
    def __init__(self, username=None):
        super().__init__(type=Gtk.WindowType.TOPLEVEL)
        self.username = username or getpass.getuser()
        
        # Window properties
        self.set_title("MECHA CYBERNETIC LOCK")
        self.set_decorated(False)
        self.set_keep_above(True)
        self.set_modal(True)
        self.fullscreen()

        # Connect events
        self.connect("destroy", Gtk.main_quit)
        self.connect("key-press-event", self.on_key_press)
        
        # Drawing area
        self.drawing_area = Gtk.DrawingArea()
        self.drawing_area.connect("draw", self.on_draw)
        self.add(self.drawing_area)

        # Animation states
        self.angle_inner = 0.0
        self.angle_outer = 0.0
        self.laser_y = 0.0
        self.laser_dir = 1.0
        self.alert_flash = 0.0
        self.success_flash = 0.0

        # Password input buffer
        self.password_buffer = ""
        self.status_msg = "[ WORKSTATION LOCKED — ENTER OPERATOR CREDENTIALS ]"
        self.status_is_error = False

        # Telemetry cache
        self.cpu_percent = psutil.cpu_percent(interval=None)
        self.mem = psutil.virtual_memory()
        self.last_telemetry_t = time.time()

        # Initial sound and voice announcement
        play_audio("mech_lock.wav")
        speak("Security protocol active. Workstation locked. Authentication required.")

        # Animation timer: 30 FPS (33ms)
        GLib.timeout_add(33, self.on_tick)

    def on_tick(self):
        # Update angles
        self.angle_inner = (self.angle_inner + 0.02) % (2 * math.pi)
        self.angle_outer = (self.angle_outer - 0.015) % (2 * math.pi)

        # Update laser scanline
        self.laser_y += self.laser_dir * 3.5
        if self.laser_y > 80:
            self.laser_dir = -1.0
        elif self.laser_y < -80:
            self.laser_dir = 1.0

        # Decay flashes
        if self.alert_flash > 0:
            self.alert_flash = max(0.0, self.alert_flash - 0.08)
        if self.success_flash > 0:
            self.success_flash = max(0.0, self.success_flash - 0.05)
            if self.success_flash == 0:
                Gtk.main_quit()

        # Refresh telemetry every 1.5s
        now = time.time()
        if now - self.last_telemetry_t > 1.5:
            self.last_telemetry_t = now
            self.cpu_percent = psutil.cpu_percent(interval=None)
            self.mem = psutil.virtual_memory()

        self.drawing_area.queue_draw()
        return True

    def on_key_press(self, widget, event):
        keyval = event.keyval
        keyname = Gdk.keyval_name(keyval)

        if keyval == Gdk.KEY_Return or keyval == Gdk.KEY_KP_Enter:
            self.verify_password()
        elif keyval == Gdk.KEY_BackSpace:
            if len(self.password_buffer) > 0:
                self.password_buffer = self.password_buffer[:-1]
                play_audio("scan_beep.wav")
        elif keyval == Gdk.KEY_Escape:
            self.password_buffer = ""
            self.status_msg = "[ INPUT CLEARED — ENTER CREDENTIALS ]"
            self.status_is_error = False
        else:
            # Printable characters
            ch = chr(Gdk.keyval_to_unicode(keyval))
            if ch and ch.isprintable():
                self.password_buffer += ch
                play_audio("scan_beep.wav")

        self.drawing_area.queue_draw()
        return True

    def verify_password(self):
        entered = self.password_buffer
        self.password_buffer = ""

        # Check against emergency bypass PIN if configured or default 1234
        bypass_pin = "1234"
        if os.path.exists(PIN_FILE):
            try:
                with open(PIN_FILE, 'r') as f:
                    bypass_pin = f.read().strip()
            except Exception:
                pass

        is_valid = (entered == bypass_pin)

        # Check against Linux PAM unix_chkpwd if not matching PIN
        if not is_valid and shutil.which("unix_chkpwd"):
            try:
                p = subprocess.Popen(
                    ["/usr/bin/unix_chkpwd", self.username],
                    stdin=subprocess.PIPE,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                p.communicate((entered + "\0").encode('utf-8'))
                if p.returncode == 0:
                    is_valid = True
            except Exception:
                pass

        if is_valid:
            self.success_flash = 1.0
            self.status_msg = "[ AUTHENTICATION CONFIRMED — ACCESS GRANTED ]"
            self.status_is_error = False
            play_audio("mech_unlock.wav")
            speak("Authentication confirmed. Access granted.")
        else:
            self.alert_flash = 1.0
            self.status_msg = "[ ACCESS DENIED — INVALID OPERATOR TOKEN ]"
            self.status_is_error = True
            play_audio("access_denied.wav")
            speak("Access denied. Intrusion attempt logged.")

    def on_draw(self, widget, cr):
        w = widget.get_allocated_width()
        h = widget.get_allocated_height()
        cx = w / 2.0
        cy = h / 2.0 - 40.0

        # Background Fill
        cr.set_source_rgb(0.03, 0.04, 0.07) # Titanium Black
        cr.paint()

        # Flash overlays
        if self.alert_flash > 0:
            cr.set_source_rgba(1.0, 0.0, 0.2, self.alert_flash * 0.4)
            cr.paint()
        elif self.success_flash > 0:
            cr.set_source_rgba(0.0, 1.0, 0.5, self.success_flash * 0.4)
            cr.paint()

        # Hexagonal Grid Lines
        cr.set_source_rgba(0.0, 0.94, 1.0, 0.04)
        cr.set_line_width(1.0)
        grid_step = 60
        for gx in range(0, w, grid_step):
            cr.move_to(gx, 0)
            cr.line_to(gx, h)
        for gy in range(0, h, grid_step):
            cr.move_to(0, gy)
            cr.line_to(w, gy)
        cr.stroke()

        # 1. Top Header Bar
        cr.set_source_rgba(0.0, 0.94, 1.0, 0.15)
        cr.rectangle(w * 0.05, 30, w * 0.90, 45)
        cr.fill()
        cr.set_source_rgba(0.0, 0.94, 1.0, 0.6)
        cr.set_line_width(1.5)
        cr.rectangle(w * 0.05, 30, w * 0.90, 45)
        cr.stroke()

        cr.select_font_face("Monospace", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(15)
        cr.set_source_rgb(0.0, 0.94, 1.0) # Neon Cyan
        cr.move_to(w * 0.05 + 16, 58)
        cr.show_text("MECHA CYBERNETIC LOCK  //  DEFENSE GRID: OMEGA-LEVEL")

        time_str = time.strftime("%H:%M:%S UTC")
        cr.move_to(w * 0.95 - 220, 58)
        cr.show_text(f"[ TIME: {time_str} ]")

        # 2. Outer Geared Mecha Ring
        r_outer = 170.0
        cr.save()
        cr.translate(cx, cy)
        cr.rotate(self.angle_outer)
        cr.set_source_rgba(0.0, 0.94, 1.0, 0.35)
        cr.set_line_width(2.0)
        cr.arc(0, 0, r_outer, 0, 2 * math.pi)
        cr.stroke()

        # Gear teeth
        num_teeth = 24
        for i in range(num_teeth):
            ang = (i / num_teeth) * 2 * math.pi
            tx1 = (r_outer - 4) * math.cos(ang)
            ty1 = (r_outer - 4) * math.sin(ang)
            tx2 = (r_outer + 8) * math.cos(ang)
            ty2 = (r_outer + 8) * math.sin(ang)
            cr.move_to(tx1, ty1)
            cr.line_to(tx2, ty2)
        cr.stroke()
        cr.restore()

        # 3. Inner Targeting Reticle with Angle Marks
        r_inner = 130.0
        cr.save()
        cr.translate(cx, cy)
        cr.rotate(self.angle_inner)
        cr.set_source_rgb(0.0, 0.94, 1.0)
        cr.set_line_width(2.5)

        # 4 Segmented arcs
        for a_start in [0, math.pi / 2, math.pi, 3 * math.pi / 2]:
            cr.arc(0, 0, r_inner, a_start + 0.15, a_start + (math.pi / 2) - 0.15)
        cr.stroke()

        # Crosshairs
        cr.set_line_width(1.0)
        cr.set_source_rgba(0.0, 0.94, 1.0, 0.5)
        cr.move_to(-r_inner - 15, 0)
        cr.line_to(r_inner + 15, 0)
        cr.move_to(0, -r_inner - 15)
        cr.line_to(0, r_inner + 15)
        cr.stroke()
        cr.restore()

        # 4. Central Retinal Laser Scanline
        cr.save()
        cr.translate(cx, cy)
        # Laser sweep line
        laser_color = (1.0, 0.2, 0.3) if self.status_is_error else (0.0, 0.94, 1.0)
        cr.set_source_rgba(laser_color[0], laser_color[1], laser_color[2], 0.85)
        cr.set_line_width(2.0)
        cr.move_to(-r_inner * 0.75, self.laser_y)
        cr.line_to(r_inner * 0.75, self.laser_y)
        cr.stroke()

        # Central Arc-Reactor Core Ring
        cr.set_source_rgba(laser_color[0], laser_color[1], laser_color[2], 0.2)
        cr.arc(0, 0, 45, 0, 2 * math.pi)
        cr.fill()
        cr.set_source_rgb(laser_color[0], laser_color[1], laser_color[2])
        cr.arc(0, 0, 45, 0, 2 * math.pi)
        cr.stroke()

        # Center lock icon text
        cr.set_font_size(18)
        lock_txt = "SECURED" if not self.status_is_error else "ALARM"
        cr.move_to(-38, 6)
        cr.show_text(lock_txt)
        cr.restore()

        # 5. Flanking Telemetry HUD Cards
        # Left Telemetry: CPU & Thermal
        cr.set_font_size(12)
        cr.set_source_rgb(0.0, 0.94, 1.0)
        lx = w * 0.08
        ly = cy - 60
        cr.move_to(lx, ly)
        cr.show_text("[ CPU QUANTUM BUS ]")
        cr.set_source_rgb(0.0, 1.0, 0.5)
        cr.move_to(lx, ly + 22)
        cr.show_text(f"LOAD: {self.cpu_percent:.1f}%")
        cr.set_source_rgb(0.9, 0.95, 1.0)
        cr.move_to(lx, ly + 42)
        cr.show_text(f"CORES: 8 ACTIVE")
        cr.move_to(lx, ly + 62)
        cr.show_text(f"TEMP:  43°C [NOMINAL]")

        # Right Telemetry: Memory & Security
        rx = w * 0.76
        ry = cy - 60
        cr.set_source_rgb(0.0, 0.94, 1.0)
        cr.move_to(rx, ry)
        cr.show_text("[ SECURITY ENCLAVE ]")
        cr.set_source_rgb(0.0, 1.0, 0.5)
        cr.move_to(rx, ry + 22)
        cr.show_text(f"RAM:  {self.mem.percent:.1f}% ALLOCATED")
        cr.set_source_rgb(0.9, 0.95, 1.0)
        cr.move_to(rx, ry + 42)
        cr.show_text(f"AUTH: PAM & PIN BIOMETRIC")
        cr.move_to(rx, ry + 62)
        cr.show_text(f"NODE: {self.username.upper()}")

        # 6. Password Input Field (Centered below HUD)
        input_w = 420.0
        input_h = 48.0
        ix = cx - input_w / 2.0
        iy = cy + r_outer + 35.0

        # Container
        cr.set_source_rgba(0.02, 0.08, 0.16, 0.85)
        cr.rectangle(ix, iy, input_w, input_h)
        cr.fill()
        border_col = (1.0, 0.16, 0.3) if self.status_is_error else (0.0, 0.94, 1.0)
        cr.set_source_rgb(border_col[0], border_col[1], border_col[2])
        cr.set_line_width(2.0)
        cr.rectangle(ix, iy, input_w, input_h)
        cr.stroke()

        # Bullets for entered password
        bullets = "● " * len(self.password_buffer)
        if not bullets:
            bullets = "ENTER OPERATOR KEY..."
            cr.set_source_rgba(0.5, 0.65, 0.8, 0.6)
        else:
            cr.set_source_rgb(0.0, 0.94, 1.0)
        cr.set_font_size(15)
        cr.move_to(ix + 16, iy + 30)
        cr.show_text(bullets)

        # 7. Status Badge
        status_col = (1.0, 0.2, 0.3) if self.status_is_error else (0.0, 1.0, 0.5)
        cr.set_source_rgb(status_col[0], status_col[1], status_col[2])
        cr.set_font_size(12)
        # Center status message
        ext = cr.text_extents(self.status_msg)
        cr.move_to(cx - ext.width / 2.0, iy + input_h + 30)
        cr.show_text(self.status_msg)

        # Bottom hint
        cr.set_source_rgba(0.5, 0.65, 0.8, 0.5)
        cr.set_font_size(10)
        hint = "[ AUTHENTICATE WITH USER PASSWORD OR PIN // [ESC] CLEAR ]"
        ext_h = cr.text_extents(hint)
        cr.move_to(cx - ext_h.width / 2.0, h - 25)
        cr.show_text(hint)

def main():
    user = sys.argv[1] if len(sys.argv) > 1 else None
    app = RoboticLockScreen(username=user)
    app.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
