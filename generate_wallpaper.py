#!/usr/bin/env python3
"""
STARK INDUSTRIES // MARK LXXXV LIVE OS TELEMETRY WALLPAPER GENERATOR
Embeds REAL Linux OS Telemetry (CPU %, RAM %, Disk, Network, Uptime, Hostname)
directly into the desktop wallpaper with high-tech holographic HUD styling.
Supports KDE Plasma 6 (Wayland) and Linux Cinnamon automatically.
"""

import os
import sys
import time
import math
import argparse
import platform
import subprocess
import psutil
from PIL import Image, ImageDraw, ImageFont, ImageFilter

DEFAULT_WIDTH = 1366
DEFAULT_HEIGHT = 768

def get_screen_resolution():
    """Detect current screen resolution via xrandr or default."""
    try:
        out = subprocess.check_output("xrandr 2>/dev/null", shell=True).decode()
        for line in out.splitlines():
            if '*' in line:
                res = line.split()[0]
                w, h = map(int, res.split('x'))
                return w, h
    except Exception:
        pass
    return DEFAULT_WIDTH, DEFAULT_HEIGHT

def get_cpu_model():
    """Get CPU model name from /proc/cpuinfo."""
    try:
        with open('/proc/cpuinfo', 'r') as f:
            for line in f:
                if 'model name' in line:
                    return line.split(':', 1)[1].strip()
    except Exception:
        pass
    return "Intel/AMD Quantum Processing Unit"

def format_uptime(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h}h {m}m {s}s"

def get_best_font(size, bold=False):
    """Attempt to load a clean system TrueType/OpenType font."""
    font_candidates = [
        "/usr/share/fonts/abattis-cantarell-fonts/Cantarell-Bold.otf" if bold else "/usr/share/fonts/abattis-cantarell-fonts/Cantarell-Regular.otf",
        "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/liberation-sans/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/liberation-sans/LiberationSans-Regular.ttf",
        "/usr/share/fonts/google-noto-vf/NotoSans[wght].ttf"
    ]
    for path in font_candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()

def draw_hud_box(draw, x, y, w, h, bg_color=(8, 14, 24, 200), border_color=(0, 229, 255, 140)):
    """Draw a frosted glass HUD container with corner brackets."""
    # Box fill
    draw.rounded_rectangle([x, y, x + w, y + h], radius=8, fill=bg_color, outline=border_color, width=1)
    
    # High-tech corner tick accents
    tick = 8
    c_tick = (0, 229, 255, 230)
    # Top-left
    draw.line([(x, y), (x + tick, y)], fill=c_tick, width=2)
    draw.line([(x, y), (x, y + tick)], fill=c_tick, width=2)
    # Top-right
    draw.line([(x + w - tick, y), (x + w, y)], fill=c_tick, width=2)
    draw.line([(x + w, y), (x + w, y + tick)], fill=c_tick, width=2)
    # Bottom-left
    draw.line([(x, y + h - tick), (x, y + h)], fill=c_tick, width=2)
    draw.line([(x, y + h), (x + tick, y + h)], fill=c_tick, width=2)
    # Bottom-right
    draw.line([(x + w - tick, y + h), (x + w, y + h)], fill=c_tick, width=2)
    draw.line([(x + w, y + h - tick), (x + w, y + h)], fill=c_tick, width=2)

def draw_progress_bar(draw, x, y, w, h, percent, fill_color=(0, 229, 255, 230), bg_color=(255, 255, 255, 25)):
    """Draw a sleek segmented or filled progress bar."""
    draw.rounded_rectangle([x, y, x + w, y + h], radius=h//2, fill=bg_color)
    fill_w = max(2, int((w * min(100, max(0, percent))) / 100))
    draw.rounded_rectangle([x, y, x + fill_w, y + h], radius=h//2, fill=fill_color)

def generate_telemetry_wallpaper(base_path, output_path, width=None, height=None):
    """Generate high-resolution wallpaper with live OS telemetry overlaid."""
    if not width or not height:
        width, height = get_screen_resolution()

    # 1. Base Wallpaper
    if base_path and os.path.exists(base_path):
        try:
            base_img = Image.open(base_path).convert("RGBA")
            base_img = base_img.resize((width, height), Image.Resampling.LANCZOS)
        except Exception:
            base_img = Image.new("RGBA", (width, height), (7, 11, 18, 255))
    else:
        base_img = Image.new("RGBA", (width, height), (7, 11, 18, 255))

    # Create HUD Overlay Canvas with Alpha
    hud = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(hud)

    # Fonts
    font_hero = get_best_font(int(height * 0.024), bold=True)
    font_title = get_best_font(int(height * 0.017), bold=True)
    font_bold = get_best_font(int(height * 0.015), bold=True)
    font_regular = get_best_font(int(height * 0.013), bold=False)
    font_small = get_best_font(int(height * 0.011), bold=False)

    # 2. Gather Real Linux OS Telemetry
    cpu_percent = psutil.cpu_percent(interval=None)
    cpu_cores_percent = psutil.cpu_percent(interval=None, percpu=True)
    cpu_count = psutil.cpu_count(logical=True)
    cpu_model = get_cpu_model()
    
    mem = psutil.virtual_memory()
    mem_used_gb = mem.used / (1024 ** 3)
    mem_total_gb = mem.total / (1024 ** 3)
    mem_percent = mem.percent

    disk = psutil.disk_usage('/')
    disk_used_gb = disk.used / (1024 ** 3)
    disk_total_gb = disk.total / (1024 ** 3)
    disk_percent = disk.percent

    net = psutil.net_io_counters()
    net_sent_mb = net.bytes_sent / (1024 ** 2)
    net_recv_mb = net.bytes_recv / (1024 ** 2)

    uptime_sec = time.time() - psutil.boot_time()
    uptime_str = format_uptime(uptime_sec)

    uname = platform.uname()
    hostname = uname.node
    kernel = uname.release
    arch = uname.machine

    # Top memory processes
    try:
        procs = sorted(
            psutil.process_iter(['name', 'memory_percent', 'cpu_percent']),
            key=lambda p: p.info.get('memory_percent') or 0,
            reverse=True
        )[:3]
        proc_str = " | ".join([f"{p.info['name']} ({p.info['memory_percent']:.1f}%)" for p in procs if p.info.get('name')])
    except Exception:
        proc_str = "kernel_task | systemd | desktop_shell"

    # Battery
    battery = psutil.sensors_battery()
    bat_str = f"BATTERY: {battery.percent}% {'[PLUGGED]' if battery.power_plugged else '[DISCHARGING]'}" if battery else "POWER: AC GRID [100% ONLINE]"

    # 3. Draw Top Master HUD Bar
    bar_y = int(height * 0.03)
    bar_h = int(height * 0.065)
    bar_w = int(width * 0.94)
    bar_x = (width - bar_w) // 2

    draw_hud_box(draw, bar_x, bar_y, bar_w, bar_h, bg_color=(8, 14, 24, 210), border_color=(0, 229, 255, 120))
    
    # Title & Branding
    draw.text((bar_x + 16, bar_y + 8), "MARK LXXXV // STARK INDUSTRIES // LIVE OS TELEMETRY", font=font_title, fill=(0, 229, 255, 255))
    draw.text((bar_x + 16, bar_y + 26), f"HOST: {hostname}  •  KERNEL: {kernel} ({arch})  •  UPTIME: {uptime_str}  •  {bat_str}", font=font_small, fill=(203, 213, 225, 240))
    
    # Right side timestamp & stability
    time_now = time.strftime("%H:%M:%S UTC")
    draw.text((bar_x + bar_w - 220, bar_y + 8), f"SYNC: {time_now}", font=font_bold, fill=(0, 255, 136, 255))
    draw.text((bar_x + bar_w - 220, bar_y + 26), "DEFENSE GRID: LEVEL 5 ARMED", font=font_small, fill=(0, 229, 255, 200))

    # 4. Telemetry Cards Layout
    card_w = int(width * 0.28)
    card_h = int(height * 0.23)
    spacing_x = int(width * 0.03)
    start_y = int(height * 0.12)

    # -----------------------------------------------------------------
    # CARD 1: Real CPU Telemetry (Left)
    # -----------------------------------------------------------------
    c1_x = bar_x
    draw_hud_box(draw, c1_x, start_y, card_w, card_h)
    
    draw.text((c1_x + 14, start_y + 10), "CPU CORE UTILIZATION", font=font_title, fill=(0, 229, 255, 255))
    draw.text((c1_x + card_w - 70, start_y + 10), f"{cpu_percent:.1f}%", font=font_hero, fill=(0, 229, 255, 255))
    draw.text((c1_x + 14, start_y + 32), f"{cpu_model[:32]} ({cpu_count} Cores)", font=font_small, fill=(148, 163, 184, 230))

    # Main CPU Bar
    draw_progress_bar(draw, c1_x + 14, start_y + 50, card_w - 28, 8, cpu_percent, fill_color=(0, 229, 255, 240))

    # Per-Core Mini Bars (up to 8 cores)
    cores_to_show = min(8, len(cpu_cores_percent))
    core_bar_w = (card_w - 28 - (cores_to_show - 1) * 6) // cores_to_show
    core_bar_y = start_y + 70
    for i in range(cores_to_show):
        cx = c1_x + 14 + i * (core_bar_w + 6)
        cp = cpu_cores_percent[i]
        draw.text((cx, core_bar_y), f"C{i}", font=font_small, fill=(148, 163, 184, 200))
        # Vertical-ish or small horizontal bar
        draw_progress_bar(draw, cx, core_bar_y + 14, core_bar_w, 5, cp, fill_color=(0, 255, 136, 220) if cp < 70 else (255, 42, 95, 220))
        draw.text((cx, core_bar_y + 22), f"{int(cp)}%", font=font_small, fill=(203, 213, 225, 220))

    # -----------------------------------------------------------------
    # CARD 2: Memory & Storage Allocation (Middle)
    # -----------------------------------------------------------------
    c2_x = c1_x + card_w + spacing_x
    draw_hud_box(draw, c2_x, start_y, card_w, card_h)

    draw.text((c2_x + 14, start_y + 10), "SYSTEM MEMORY & STORAGE", font=font_title, fill=(0, 229, 255, 255))
    draw.text((c2_x + card_w - 70, start_y + 10), f"{mem_percent:.1f}%", font=font_hero, fill=(0, 255, 136, 255))
    draw.text((c2_x + 14, start_y + 32), f"RAM: {mem_used_gb:.2f} GB used of {mem_total_gb:.2f} GB total", font=font_small, fill=(148, 163, 184, 230))

    # RAM Bar
    draw_progress_bar(draw, c2_x + 14, start_y + 50, card_w - 28, 8, mem_percent, fill_color=(0, 255, 136, 240))

    # NVMe / Root Disk Storage
    draw.text((c2_x + 14, start_y + 70), f"STORAGE [/]: {disk_used_gb:.1f} GB / {disk_total_gb:.1f} GB ({disk_percent:.1f}%)", font=font_small, fill=(203, 213, 225, 240))
    draw_progress_bar(draw, c2_x + 14, start_y + 88, card_w - 28, 6, disk_percent, fill_color=(255, 183, 3, 240))

    draw.text((c2_x + 14, start_y + 102), f"SWAP: {psutil.swap_memory().percent}% used", font=font_small, fill=(148, 163, 184, 200))

    # -----------------------------------------------------------------
    # CARD 3: Network & Active Processes (Right)
    # -----------------------------------------------------------------
    c3_x = c2_x + card_w + spacing_x
    draw_hud_box(draw, c3_x, start_y, card_w, card_h)

    draw.text((c3_x + 14, start_y + 10), "NETWORK I/O & TOP PROCESSES", font=font_title, fill=(0, 229, 255, 255))
    draw.text((c3_x + card_w - 90, start_y + 10), "ONLINE", font=font_hero, fill=(0, 229, 255, 255))
    
    draw.text((c3_x + 14, start_y + 34), f"NET TRAFFIC: RX {net_recv_mb:.1f} MB  •  TX {net_sent_mb:.1f} MB", font=font_regular, fill=(203, 213, 225, 240))
    draw.line([(c3_x + 14, start_y + 54), (c3_x + card_w - 14, start_y + 54)], fill=(255, 255, 255, 30), width=1)

    draw.text((c3_x + 14, start_y + 62), "TOP CONSUMPTION PROCESSES:", font=font_small, fill=(0, 229, 255, 220))
    
    try:
        for idx, p in enumerate(procs[:3]):
            py = start_y + 78 + (idx * 14)
            p_name = p.info.get('name') or 'unknown'
            p_mem = p.info.get('memory_percent') or 0
            p_cpu = p.info.get('cpu_percent') or 0
            draw.text((c3_x + 14, py), f"• {p_name[:18]}", font=font_small, fill=(241, 245, 249, 230))
            draw.text((c3_x + card_w - 100, py), f"RAM: {p_mem:.1f}%", font=font_small, fill=(148, 163, 184, 200))
    except Exception:
        pass

    # 5. Composite HUD onto Base Image
    final_img = Image.alpha_composite(base_img, hud).convert("RGB")
    
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    final_img.save(output_path, "PNG", quality=95)
    return output_path

def apply_wallpaper_to_desktop(image_path):
    """Apply wallpaper to KDE Plasma 6 (Wayland) or Linux Cinnamon / GNOME."""
    abs_path = os.path.abspath(image_path)
    file_uri = f"file://{abs_path}"
    desktop_session = os.environ.get("XDG_CURRENT_DESKTOP", "").lower()

    # 1. KDE Plasma 6 (Wayland)
    if "kde" in desktop_session or subprocess.call("which qdbus-qt6 >/dev/null 2>&1", shell=True) == 0:
        plasma_js = f"""
        for (var i = 0; i < desktops().length; i++) {{
            var d = desktops()[i];
            d.wallpaperPlugin = "org.kde.image";
            d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");
            d.writeConfig("Image", "{file_uri}");
        }}
        """
        cmd = f"qdbus-qt6 org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript '{plasma_js}'"
        try:
            subprocess.run(cmd, shell=True, check=False)
        except Exception:
            pass

    # 2. Linux Cinnamon
    if subprocess.call("which gsettings >/dev/null 2>&1", shell=True) == 0:
        try:
            subprocess.run(f"gsettings set org.cinnamon.desktop.background picture-uri '{file_uri}'", shell=True, check=False)
            subprocess.run(f"gsettings set org.cinnamon.desktop.background picture-options 'zoom'", shell=True, check=False)
            # Also GNOME compatibility
            subprocess.run(f"gsettings set org.gnome.desktop.background picture-uri '{file_uri}'", shell=True, check=False)
            subprocess.run(f"gsettings set org.gnome.desktop.background picture-uri-dark '{file_uri}'", shell=True, check=False)
        except Exception:
            pass

def main():
    parser = argparse.ArgumentParser(description="Stark Industries Live OS Telemetry Wallpaper Engine")
    parser.add_argument("--base", default=None, help="Base image path")
    parser.add_argument("--output", default=os.path.expanduser("~/.local/share/backgrounds/stark-live-wallpaper.png"), help="Output PNG path")
    parser.add_argument("--apply", action="store_true", help="Apply generated wallpaper immediately to desktop")
    parser.add_argument("--live", "--daemon", action="store_true", dest="live", help="Run continuously in background updating stats")
    parser.add_argument("--interval", type=float, default=3.0, help="Live refresh interval in seconds (default: 3s)")
    args = parser.parse_args()

    # Default base resolution wallpaper
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_file = args.base
    if not base_file or not os.path.exists(base_file):
        default_candidate = os.path.join(script_dir, "public/assets/wallpapers/jarvis-master.jpg")
        user_photo = os.path.expanduser("~/Pictures/tony-stark-iron-man-2008 (1).jpeg")
        if os.path.exists(default_candidate):
            base_file = default_candidate
        elif os.path.exists(user_photo):
            base_file = user_photo

    print(f"[STARK HUD ENGINE]: Generating wallpaper with real Linux telemetry...")
    out = generate_telemetry_wallpaper(base_file, args.output)
    print(f"[STARK HUD ENGINE]: Wallpaper rendered at: {out}")

    if args.apply:
        apply_wallpaper_to_desktop(args.output)
        print(f"[STARK HUD ENGINE]: Applied to active desktop session.")

    if args.live:
        print(f"[STARK HUD ENGINE]: Starting Live Telemetry Daemon (interval: {args.interval}s)...")
        try:
            while True:
                time.sleep(args.interval)
                generate_telemetry_wallpaper(base_file, args.output)
                apply_wallpaper_to_desktop(args.output)
        except KeyboardInterrupt:
            print("\n[STARK HUD ENGINE]: Daemon stopped.")

if __name__ == "__main__":
    main()
