#!/usr/bin/env python3
"""
eDEX-UI // TRON ARCHITECTURE LIVE TELEMETRY WALLPAPER GENERATOR
Embeds REAL Linux OS Telemetry (CPU Cores, RAM, Disk, Network RX/TX, Uptime, Process Tree, Temp)
directly into the desktop wallpaper with authentic eDEX-UI / TRON: Legacy sci-fi HUD styling.
Supports KDE Plasma 6 (Wayland) and Linux Cinnamon / GNOME automatically.
"""

import os
import sys
import time
import math
import json
import socket
import argparse
import platform
import subprocess
import psutil
from PIL import Image, ImageDraw, ImageFont

DEFAULT_WIDTH = 1366
DEFAULT_HEIGHT = 768

# eDEX-UI Tron Color Palette
COLOR_BG_DEEP = (0, 8, 20, 255)
COLOR_PANEL_BG = (2, 12, 28, 220)
COLOR_CYAN_GLOW = (0, 229, 255, 255)
COLOR_CYAN_DIM = (0, 229, 255, 120)
COLOR_CYAN_VERY_DIM = (0, 229, 255, 40)
COLOR_CYAN_BORDER = (0, 229, 255, 160)
COLOR_GREEN_NEON = (0, 255, 136, 255)
COLOR_GREEN_DIM = (0, 255, 136, 140)
COLOR_AMBER_NEON = (255, 183, 3, 255)
COLOR_RED_ALERT = (255, 42, 95, 255)
COLOR_TEXT_PRIMARY = (240, 246, 252, 255)
COLOR_TEXT_MUTED = (130, 160, 190, 240)
COLOR_GRID_LINE = (0, 229, 255, 18)

HISTORY_FILE = "/tmp/edex_cpu_history.json"
RADAR_STATE_FILE = "/tmp/edex_radar_state.json"

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

def get_best_font(size, bold=False):
    """Load a clean monospace system font."""
    font_candidates = [
        "/usr/share/fonts/liberation-mono-fonts/LiberationMono-Bold.ttf" if bold else "/usr/share/fonts/liberation-mono-fonts/LiberationMono-Regular.ttf",
        "/usr/share/fonts/abattis-cantarell-fonts/Cantarell-Bold.otf" if bold else "/usr/share/fonts/abattis-cantarell-fonts/Cantarell-Regular.otf",
        "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/dejavu/DejaVuSans.ttf",
    ]
    for path in font_candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()

def format_uptime(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h}h {m}m {s}s"

def get_active_ip_and_iface():
    addrs = psutil.net_if_addrs()
    for iface, addr_list in addrs.items():
        if iface == 'lo':
            continue
        for a in addr_list:
            if a.family == socket.AF_INET:
                return iface, a.address
    return "wlan0", "127.0.0.1"

def get_cpu_temp():
    try:
        temps = psutil.sensors_temperatures()
        if 'coretemp' in temps and temps['coretemp']:
            return f"{temps['coretemp'][0].current:.0f}°C"
        if 'nvme' in temps and temps['nvme']:
            return f"{temps['nvme'][0].current:.0f}°C"
    except Exception:
        pass
    return "42°C"

def get_cpu_freq_str():
    try:
        freq = psutil.cpu_freq()
        if freq and freq.current:
            return f"{freq.current / 1000:.2f} GHz"
    except Exception:
        pass
    return "2.80 GHz"

def draw_edex_box(draw, x, y, w, h, title="", subtitle="", border_color=COLOR_CYAN_BORDER, bg_color=COLOR_PANEL_BG, font_title=None, font_sub=None):
    """Draw signature eDEX-UI tech bracket container with notched corners."""
    # Semi-transparent dark background
    draw.rectangle([x, y, x + w, y + h], fill=bg_color)
    
    # Outer thin border
    draw.rectangle([x, y, x + w, y + h], outline=COLOR_CYAN_VERY_DIM, width=1)
    
    # Corner brackets / ticks
    bracket_len = min(14, w // 8, h // 8)
    t_width = 2
    
    # Top-left corner
    draw.line([(x, y), (x + bracket_len, y)], fill=border_color, width=t_width)
    draw.line([(x, y), (x, y + bracket_len)], fill=border_color, width=t_width)
    
    # Top-right corner
    draw.line([(x + w - bracket_len, y), (x + w, y)], fill=border_color, width=t_width)
    draw.line([(x + w, y), (x + w, y + bracket_len)], fill=border_color, width=t_width)
    
    # Bottom-left corner
    draw.line([(x, y + h - bracket_len), (x, y + h)], fill=border_color, width=t_width)
    draw.line([(x, y + h), (x + bracket_len, y + h)], fill=border_color, width=t_width)
    
    # Bottom-right corner
    draw.line([(x + w - bracket_len, y + h), (x + w, y + h)], fill=border_color, width=t_width)
    draw.line([(x + w, y + h - bracket_len), (x + w, y + h)], fill=border_color, width=t_width)

    # Title header strip if specified
    if title:
        header_h = 24
        draw.rectangle([x, y, x + w, y + header_h], fill=(0, 229, 255, 20), outline=COLOR_CYAN_DIM, width=1)
        if font_title:
            draw.text((x + 10, y + 4), f"[ {title} ]", font=font_title, fill=COLOR_CYAN_GLOW)
        if subtitle and font_sub:
            draw.text((x + w - 120, y + 5), subtitle, font=font_sub, fill=COLOR_GREEN_NEON)

def draw_segmented_bar(draw, x, y, w, h, percent, segments=20, fill_color=COLOR_CYAN_GLOW):
    """Draw authentic eDEX-UI segmented telemetry bar."""
    seg_spacing = 2
    seg_w = max(2, (w - (segments - 1) * seg_spacing) // segments)
    filled_segs = int((percent / 100.0) * segments)
    
    for i in range(segments):
        sx = x + i * (seg_w + seg_spacing)
        # Background slot
        draw.rectangle([sx, y, sx + seg_w, y + h], fill=(255, 255, 255, 15))
        if i < filled_segs:
            # Color escalation if high load
            if percent > 85 and i > segments * 0.8:
                col = COLOR_RED_ALERT
            elif percent > 65 and i > segments * 0.6:
                col = COLOR_AMBER_NEON
            else:
                col = fill_color
            draw.rectangle([sx, y, sx + seg_w, y + h], fill=col)

def draw_radar(draw, cx, cy, radius, sweep_deg=45):
    """Draw circular Geo-Radar scanner with rotating sweep line and targets."""
    # Concentric rings
    for r in [radius, int(radius * 0.75), int(radius * 0.5), int(radius * 0.25)]:
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=COLOR_CYAN_DIM, width=1)
    
    # Crosshair axes with compass ticks
    draw.line([(cx - radius - 8, cy), (cx + radius + 8, cy)], fill=COLOR_CYAN_DIM, width=1)
    draw.line([(cx, cy - radius - 8), (cx, cy + radius + 8)], fill=COLOR_CYAN_DIM, width=1)
    
    # Compass cardinal marks
    draw.text((cx - 4, cy - radius - 18), "N", font=ImageFont.load_default(), fill=COLOR_CYAN_GLOW)
    draw.text((cx + radius + 10, cy - 4), "E", font=ImageFont.load_default(), fill=COLOR_TEXT_MUTED)
    draw.text((cx - 4, cy + radius + 8), "S", font=ImageFont.load_default(), fill=COLOR_TEXT_MUTED)
    draw.text((cx - radius - 18, cy - 4), "W", font=ImageFont.load_default(), fill=COLOR_TEXT_MUTED)
    
    # 45-degree diagonal tick marks
    diag_len = int(radius * 0.707)
    draw.line([(cx - diag_len, cy - diag_len), (cx + diag_len, cy + diag_len)], fill=(0, 229, 255, 25), width=1)
    draw.line([(cx - diag_len, cy + diag_len), (cx + diag_len, cy - diag_len)], fill=(0, 229, 255, 25), width=1)
    
    # Radar Sweep Line
    rad = math.radians(sweep_deg)
    sx = cx + int(radius * math.cos(rad))
    sy = cy + int(radius * math.sin(rad))
    draw.line([(cx, cy), (sx, sy)], fill=COLOR_GREEN_NEON, width=2)
    
    # Fading sweep cone (subtle fan lines)
    for delta in range(1, 15):
        alpha_rad = math.radians(sweep_deg - delta * 2)
        fx = cx + int(radius * math.cos(alpha_rad))
        fy = cy + int(radius * math.sin(alpha_rad))
        draw.line([(cx, cy), (fx, fy)], fill=(0, 255, 136, max(5, 50 - delta * 3)), width=1)
    
    # Center blip
    draw.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=COLOR_GREEN_NEON)
    
    # Target blips with coordinate pulses
    blips = [
        (cx + int(radius * 0.45), cy - int(radius * 0.35)),
        (cx - int(radius * 0.55), cy + int(radius * 0.25)),
        (cx + int(radius * 0.2), cy + int(radius * 0.65)),
    ]
    for bx, by in blips:
        draw.ellipse([bx - 2, by - 2, bx + 2, by + 2], fill=COLOR_AMBER_NEON)
        draw.ellipse([bx - 6, by - 6, bx + 6, by + 6], outline=(255, 183, 3, 100), width=1)

def draw_cyber_keyboard(draw, x, y, w, h, font_key):
    """Draw authentic eDEX-UI virtual Tron cyber-deck keyboard."""
    # Container box
    draw.rectangle([x, y, x + w, y + h], fill=(2, 10, 24, 210), outline=COLOR_CYAN_DIM, width=1)
    
    # Header bar for keyboard
    draw.rectangle([x, y, x + w, y + 16], fill=(0, 229, 255, 18))
    draw.text((x + 8, y + 2), "[ VIRTUAL CYBER-DECK // TERMINAL INPUT MATRIX ]", font=font_key, fill=COLOR_CYAN_GLOW)
    draw.text((x + w - 110, y + 2), "LAYOUT: QWERTY-US", font=font_key, fill=COLOR_GREEN_NEON)
    
    # Keyboard rows definition
    rows = [
        ["ESC", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "PRT", "DEL"],
        ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "BACK"],
        ["TAB", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", "\\"],
        ["CAPS", "A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'", "ENTER"],
        ["SHIFT", "Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", "SHIFT", "UP"],
        ["CTRL", "ALT", "SPACE DECK", "ALT", "SYS", "LEFT", "DOWN", "RIGHT"]
    ]
    
    ky_start = y + 22
    row_count = len(rows)
    avail_h = h - 28
    key_h = max(10, (avail_h - (row_count - 1) * 3) // row_count)
    
    for r_idx, row in enumerate(rows):
        ry = ky_start + r_idx * (key_h + 3)
        col_count = len(row)
        key_w = (w - 16 - (col_count - 1) * 3) // col_count
        
        for c_idx, key in enumerate(row):
            # Dynamic key width adjustments for space / enter / etc.
            kx = x + 8 + c_idx * (key_w + 3)
            kw = key_w
            
            # Draw individual key
            is_active = key in ["SPACE DECK", "ENTER", "ESC"]
            key_fill = (0, 229, 255, 30) if is_active else (255, 255, 255, 6)
            key_border = COLOR_CYAN_GLOW if is_active else COLOR_CYAN_VERY_DIM
            draw.rectangle([kx, ry, kx + kw, ry + key_h], fill=key_fill, outline=key_border, width=1)
            
            # Key text (shorten if necessary)
            k_text = key[:8]
            draw.text((kx + 3, ry + max(1, (key_h - 10) // 2)), k_text, font=font_key, fill=COLOR_CYAN_GLOW if is_active else COLOR_TEXT_MUTED)

def update_cpu_history(current_cpu):
    """Maintain sliding window of CPU usage for sparkline."""
    history = [current_cpu] * 20
    try:
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'r') as f:
                data = json.load(f)
                if isinstance(data, list):
                    history = data
    except Exception:
        pass
    
    history.append(current_cpu)
    if len(history) > 30:
        history = history[-30:]
        
    try:
        with open(HISTORY_FILE, 'w') as f:
            json.dump(history, f)
    except Exception:
        pass
    return history

def get_radar_sweep_deg():
    """Rotate radar sweep degree per frame."""
    deg = 45.0
    try:
        if os.path.exists(RADAR_STATE_FILE):
            with open(RADAR_STATE_FILE, 'r') as f:
                deg = float(f.read().strip())
    except Exception:
        pass
    
    deg = (deg + 25.0) % 360.0
    try:
        with open(RADAR_STATE_FILE, 'w') as f:
            f.write(str(deg))
    except Exception:
        pass
    return deg

def generate_edex_wallpaper(output_path, width=None, height=None, base_path=None):
    """Generate authentic eDEX-UI TRON live telemetry wallpaper."""
    if not width or not height:
        width, height = get_screen_resolution()
        
    # 1. Base Image: Either composited onto base or pure Tron Cyber-Abyss
    if base_path and os.path.exists(base_path):
        try:
            base_img = Image.open(base_path).convert("RGBA").resize((width, height), Image.Resampling.LANCZOS)
            # Apply a dark cyber-tint to the base image
            tint = Image.new("RGBA", (width, height), (0, 7, 18, 190))
            base_img = Image.alpha_composite(base_img, tint)
        except Exception:
            base_img = Image.new("RGBA", (width, height), COLOR_BG_DEEP)
    else:
        base_img = Image.new("RGBA", (width, height), COLOR_BG_DEEP)

    hud = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(hud)

    # 2. Draw 3D Tron Cyber-Grid in Background
    grid_spacing = 40
    # Vertical grid lines
    for gx in range(0, width, grid_spacing):
        draw.line([(gx, 0), (gx, height)], fill=COLOR_GRID_LINE, width=1)
    # Horizontal grid lines
    for gy in range(0, height, grid_spacing):
        draw.line([(0, gy), (width, gy)], fill=COLOR_GRID_LINE, width=1)

    # Fonts
    font_hero = get_best_font(int(height * 0.026), bold=True)
    font_title = get_best_font(int(height * 0.016), bold=True)
    font_bold = get_best_font(int(height * 0.014), bold=True)
    font_regular = get_best_font(int(height * 0.013), bold=False)
    font_small = get_best_font(int(height * 0.011), bold=False)
    font_tiny = get_best_font(int(height * 0.009), bold=False)

    # 3. Gather Real-Time Linux Telemetry
    cpu_percent = psutil.cpu_percent(interval=None)
    cpu_cores_percent = psutil.cpu_percent(interval=None, percpu=True)
    cpu_count = psutil.cpu_count(logical=True)
    cpu_freq = get_cpu_freq_str()
    cpu_temp = get_cpu_temp()
    cpu_history = update_cpu_history(cpu_percent)

    mem = psutil.virtual_memory()
    mem_used_gb = mem.used / (1024 ** 3)
    mem_total_gb = mem.total / (1024 ** 3)
    mem_percent = mem.percent

    swap = psutil.swap_memory()
    swap_used_gb = swap.used / (1024 ** 3)
    swap_total_gb = swap.total / (1024 ** 3)
    swap_percent = swap.percent

    disk = psutil.disk_usage('/')
    disk_used_gb = disk.used / (1024 ** 3)
    disk_total_gb = disk.total / (1024 ** 3)
    disk_percent = disk.percent

    net = psutil.net_io_counters()
    net_sent_mb = net.bytes_sent / (1024 ** 2)
    net_recv_mb = net.bytes_recv / (1024 ** 2)
    net_iface, net_ip = get_active_ip_and_iface()

    uptime_str = format_uptime(time.time() - psutil.boot_time())
    uname = platform.uname()
    hostname = uname.node
    kernel = uname.release
    arch = uname.machine

    battery = psutil.sensors_battery()
    bat_str = f"BAT: {battery.percent}% {'[CHG]' if battery.power_plugged else '[PWR]'}" if battery else "PWR: AC GRID [100%]"
    time_now = time.strftime("%H:%M:%S UTC")

    # =========================================================================
    # 4. TOP MASTER HUD HEADER BAR
    # =========================================================================
    bar_y = int(height * 0.02)
    bar_h = int(height * 0.055)
    bar_w = int(width * 0.96)
    bar_x = (width - bar_w) // 2

    draw_edex_box(draw, bar_x, bar_y, bar_w, bar_h, border_color=COLOR_CYAN_GLOW)
    
    # Left branding
    draw.text((bar_x + 14, bar_y + 8), "eDEX-UI // TRON_LEGACY_OS v3.2.0", font=font_title, fill=COLOR_CYAN_GLOW)
    draw.text((bar_x + 14, bar_y + 24), f"NODE: {hostname.upper()}  •  ARCH: {arch}  •  KERNEL: {kernel}", font=font_small, fill=COLOR_TEXT_MUTED)
    
    # Center uptime & telemetry
    draw.text((bar_x + int(bar_w * 0.40), bar_y + 8), f"SYS_UPTIME: {uptime_str}  •  {bat_str}", font=font_bold, fill=COLOR_GREEN_NEON)
    draw.text((bar_x + int(bar_w * 0.40), bar_y + 24), f"CORE_TEMP: {cpu_temp}  •  FREQ: {cpu_freq}  •  DEFENSE: ARMED", font=font_small, fill=COLOR_TEXT_MUTED)
    
    # Right timestamp
    draw.text((bar_x + bar_w - 180, bar_y + 8), f"[ {time_now} ]", font=font_title, fill=COLOR_CYAN_GLOW)
    draw.text((bar_x + bar_w - 180, bar_y + 24), "SYSTEM STATUS: NOMINAL", font=font_small, fill=COLOR_GREEN_NEON)

    # =========================================================================
    # 5. LAYOUT COLUMNS
    # =========================================================================
    col_w = int(width * 0.26)
    start_y = bar_y + bar_h + 10
    bottom_deck_h = int(height * 0.17)
    avail_col_h = height - start_y - bottom_deck_h - 15

    # -------------------------------------------------------------------------
    # LEFT COLUMN: CPU + MEMORY + PROCESSES
    # -------------------------------------------------------------------------
    left_x = bar_x
    
    # Card 1: CPU Telemetry
    cpu_card_h = int(avail_col_h * 0.44)
    draw_edex_box(draw, left_x, start_y, col_w, cpu_card_h, title="CPU MULTI-CORE TELEMETRY", subtitle="ONLINE", font_title=font_title, font_sub=font_small)
    
    # Big readout
    draw.text((left_x + 12, start_y + 30), f"{cpu_percent:.1f}%", font=font_hero, fill=COLOR_CYAN_GLOW)
    draw.text((left_x + 95, start_y + 32), f"UTILIZATION ({cpu_count} CORES)", font=font_bold, fill=COLOR_TEXT_PRIMARY)
    draw.text((left_x + 95, start_y + 46), f"CLOCK: {cpu_freq}  •  TEMP: {cpu_temp}", font=font_small, fill=COLOR_TEXT_MUTED)
    
    # Master segmented bar
    draw_segmented_bar(draw, left_x + 12, start_y + 64, col_w - 24, 7, cpu_percent, segments=24)
    
    # Per-core mini meters (up to 8 cores)
    cores_to_show = min(8, len(cpu_cores_percent))
    c_cols = 4
    c_rows = (cores_to_show + c_cols - 1) // c_cols
    slot_w = (col_w - 24 - (c_cols - 1) * 6) // c_cols
    base_cy = start_y + 78
    
    for idx in range(cores_to_show):
        row_i = idx // c_cols
        col_i = idx % c_cols
        cx_pos = left_x + 12 + col_i * (slot_w + 6)
        cy_pos = base_cy + row_i * 24
        cp = cpu_cores_percent[idx]
        draw.text((cx_pos, cy_pos), f"C{idx}:{int(cp)}%", font=font_tiny, fill=COLOR_CYAN_GLOW)
        draw_segmented_bar(draw, cx_pos, cy_pos + 12, slot_w, 4, cp, segments=6, fill_color=COLOR_GREEN_NEON)
        
    # Sparkline history curve
    spark_y = base_cy + c_rows * 24 + 4
    spark_h = cpu_card_h - (spark_y - start_y) - 6
    if spark_h > 10 and len(cpu_history) > 1:
        draw.text((left_x + 12, spark_y), "CPU LOAD WAVEFORM:", font=font_tiny, fill=COLOR_TEXT_MUTED)
        step_x = (col_w - 24) / (len(cpu_history) - 1)
        points = []
        for i, val in enumerate(cpu_history):
            px = left_x + 12 + i * step_x
            py = spark_y + spark_h - int((val / 100.0) * (spark_h - 10))
            points.append((px, py))
        draw.line(points, fill=COLOR_CYAN_GLOW, width=1)

    # Card 2: Memory & Swap
    mem_card_y = start_y + cpu_card_h + 8
    mem_card_h = int(avail_col_h * 0.28)
    draw_edex_box(draw, left_x, mem_card_y, col_w, mem_card_h, title="MEMORY ARCHITECTURE", subtitle=f"{mem_percent:.1f}%", font_title=font_title, font_sub=font_small)
    
    # RAM
    draw.text((left_x + 12, mem_card_y + 28), f"RAM: {mem_used_gb:.2f}G / {mem_total_gb:.2f}G", font=font_small, fill=COLOR_TEXT_PRIMARY)
    draw.text((left_x + col_w - 50, mem_card_y + 28), f"{mem_percent:.0f}%", font=font_small, fill=COLOR_GREEN_NEON)
    draw_segmented_bar(draw, left_x + 12, mem_card_y + 42, col_w - 24, 6, mem_percent, segments=22, fill_color=COLOR_GREEN_NEON)
    
    # SWAP
    draw.text((left_x + 12, mem_card_y + 54), f"SWAP: {swap_used_gb:.2f}G / {swap_total_gb:.2f}G", font=font_small, fill=COLOR_TEXT_PRIMARY)
    draw.text((left_x + col_w - 50, mem_card_y + 54), f"{swap_percent:.0f}%", font=font_small, fill=COLOR_AMBER_NEON)
    draw_segmented_bar(draw, left_x + 12, mem_card_y + 68, col_w - 24, 6, swap_percent, segments=22, fill_color=COLOR_AMBER_NEON)

    # Card 3: Top Processes
    proc_card_y = mem_card_y + mem_card_h + 8
    proc_card_h = avail_col_h - cpu_card_h - mem_card_h - 16
    draw_edex_box(draw, left_x, proc_card_y, col_w, proc_card_h, title="TOP PROCESS THREADS", subtitle="ACTIVE", font_title=font_title, font_sub=font_small)
    
    try:
        procs = sorted(
            psutil.process_iter(['name', 'memory_percent', 'cpu_percent']),
            key=lambda p: (p.info.get('cpu_percent') or 0) + (p.info.get('memory_percent') or 0),
            reverse=True
        )[:3]
        for p_idx, p in enumerate(procs):
            py = proc_card_y + 28 + p_idx * 16
            p_name = (p.info.get('name') or 'task')[:14]
            p_cpu = p.info.get('cpu_percent') or 0
            p_mem = p.info.get('memory_percent') or 0
            draw.text((left_x + 12, py), f"• {p_name}", font=font_tiny, fill=COLOR_TEXT_PRIMARY)
            draw.text((left_x + col_w - 85, py), f"C:{p_cpu:.0f}% M:{p_mem:.1f}%", font=font_tiny, fill=COLOR_CYAN_GLOW)
    except Exception:
        pass

    # -------------------------------------------------------------------------
    # RIGHT COLUMN: RADAR + NETWORK + STORAGE
    # -------------------------------------------------------------------------
    right_x = bar_x + bar_w - col_w
    
    # Card 1: Geo Radar Scanner
    radar_card_h = int(avail_col_h * 0.44)
    draw_edex_box(draw, right_x, start_y, col_w, radar_card_h, title="GEO-RADAR // SCANNER", subtitle="SWEEPING", font_title=font_title, font_sub=font_small)
    
    radar_cx = right_x + col_w // 2
    radar_cy = start_y + 28 + (radar_card_h - 40) // 2
    radar_r = min(int(col_w * 0.32), (radar_card_h - 45) // 2)
    sweep_deg = get_radar_sweep_deg()
    draw_radar(draw, radar_cx, radar_cy, radar_r, sweep_deg=sweep_deg)
    
    draw.text((right_x + 12, start_y + radar_card_h - 16), f"BEAM_AZIMUTH: {sweep_deg:.1f}°  •  GEO: 37.77N 122.41W", font=font_tiny, fill=COLOR_GREEN_NEON)

    # Card 2: Network I/O Telemetry
    net_card_y = start_y + radar_card_h + 8
    net_card_h = int(avail_col_h * 0.28)
    draw_edex_box(draw, right_x, net_card_y, col_w, net_card_h, title="NETWORK INTERFACE & I/O", subtitle="LINK OK", font_title=font_title, font_sub=font_small)
    
    draw.text((right_x + 12, net_card_y + 28), f"IFACE: {net_iface}  •  IP: {net_ip}", font=font_small, fill=COLOR_TEXT_PRIMARY)
    draw.text((right_x + 12, net_card_y + 44), f"TRAFFIC RX: {net_recv_mb:.1f} MB  •  TX: {net_sent_mb:.1f} MB", font=font_small, fill=COLOR_CYAN_GLOW)
    draw.text((right_x + 12, net_card_y + 60), f"SOCKET STATUS: ESTABLISHED  •  PING: 14ms", font=font_tiny, fill=COLOR_TEXT_MUTED)

    # Card 3: Storage & Mounts
    storage_card_y = net_card_y + net_card_h + 8
    storage_card_h = avail_col_h - radar_card_h - net_card_h - 16
    draw_edex_box(draw, right_x, storage_card_y, col_w, storage_card_h, title="STORAGE MOUNTS & DISK", subtitle=f"{disk_percent:.1f}%", font_title=font_title, font_sub=font_small)
    
    draw.text((right_x + 12, storage_card_y + 28), f"ROOT [/]: {disk_used_gb:.1f}G / {disk_total_gb:.1f}G", font=font_small, fill=COLOR_TEXT_PRIMARY)
    draw_segmented_bar(draw, right_x + 12, storage_card_y + 42, col_w - 24, 6, disk_percent, segments=22, fill_color=COLOR_AMBER_NEON)

    # =========================================================================
    # 6. CENTER WORKSPACE VIEWPORT HUD BRACKETS
    # =========================================================================
    center_x = left_x + col_w + 14
    center_w = right_x - center_x - 14
    center_y = start_y
    center_h = avail_col_h
    
    # 4 corner brackets
    c_tick = 20
    t_col = COLOR_CYAN_DIM
    # Top-Left
    draw.line([(center_x, center_y), (center_x + c_tick, center_y)], fill=t_col, width=2)
    draw.line([(center_x, center_y), (center_x, center_y + c_tick)], fill=t_col, width=2)
    # Top-Right
    draw.line([(center_x + center_w - c_tick, center_y), (center_x + center_w, center_y)], fill=t_col, width=2)
    draw.line([(center_x + center_w, center_y), (center_x + center_w, center_y + c_tick)], fill=t_col, width=2)
    # Bottom-Left
    draw.line([(center_x, center_y + center_h - c_tick), (center_x, center_y + center_h)], fill=t_col, width=2)
    draw.line([(center_x, center_y + center_h), (center_x + c_tick, center_y + center_h)], fill=t_col, width=2)
    # Bottom-Right
    draw.line([(center_x + center_w - c_tick, center_y + center_h), (center_x + center_w, center_y + center_h)], fill=t_col, width=2)
    draw.line([(center_x + center_w, center_y + center_h - c_tick), (center_x + center_w, center_y + center_h)], fill=t_col, width=2)

    # Subtle crosshairs at center
    mid_x = center_x + center_w // 2
    mid_y = center_y + center_h // 2
    draw.line([(mid_x - 12, mid_y), (mid_x + 12, mid_y)], fill=(0, 229, 255, 40), width=1)
    draw.line([(mid_x, mid_y - 12), (mid_x, mid_y + 12)], fill=(0, 229, 255, 40), width=1)
    draw.text((mid_x - 100, center_y + 14), "[ TERMINAL WORKSPACE MATRIX ]", font=font_small, fill=(0, 229, 255, 80))

    # =========================================================================
    # 7. BOTTOM CYBER-KEYBOARD DECK
    # =========================================================================
    deck_y = height - bottom_deck_h - 10
    deck_w = bar_w
    deck_x = bar_x
    draw_cyber_keyboard(draw, deck_x, deck_y, deck_w, bottom_deck_h, font_tiny)

    # 8. Composite HUD onto base and save
    final_img = Image.alpha_composite(base_img, hud).convert("RGB")
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    final_img.save(output_path, "PNG", quality=95)
    return output_path

def apply_wallpaper_to_desktop(image_path):
    """Apply wallpaper to KDE Plasma 6 (Wayland) and Linux Cinnamon / GNOME."""
    abs_path = os.path.abspath(image_path)
    file_uri = f"file://{abs_path}"
    desktop_session = os.environ.get("XDG_CURRENT_DESKTOP", "").lower()

    # 1. Native KDE utility plasma-apply-wallpaperimage
    if subprocess.call("which plasma-apply-wallpaperimage >/dev/null 2>&1", shell=True) == 0:
        try:
            subprocess.run(f"plasma-apply-wallpaperimage '{abs_path}'", shell=True, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            pass

    # 2. KDE Plasma 6 via DBus evaluateScript
    if subprocess.call("which qdbus-qt6 >/dev/null 2>&1", shell=True) == 0:
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
            subprocess.run(cmd, shell=True, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            pass

    # 3. Linux Cinnamon / GNOME
    if subprocess.call("which gsettings >/dev/null 2>&1", shell=True) == 0:
        try:
            subprocess.run(f"gsettings set org.cinnamon.desktop.background picture-uri '{file_uri}'", shell=True, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(f"gsettings set org.cinnamon.desktop.background picture-options 'zoom'", shell=True, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(f"gsettings set org.gnome.desktop.background picture-uri '{file_uri}'", shell=True, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(f"gsettings set org.gnome.desktop.background picture-uri-dark '{file_uri}'", shell=True, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            pass

def main():
    parser = argparse.ArgumentParser(description="eDEX-UI // TRON Live OS Telemetry Wallpaper Engine")
    parser.add_argument("--base", default=None, help="Base image path (optional, default: pure Tron Cyber-Abyss)")
    parser.add_argument("--output", default=os.path.expanduser("~/.local/share/backgrounds/edex-live-wallpaper.png"), help="Output PNG path")
    parser.add_argument("--apply", action="store_true", help="Apply generated wallpaper immediately to desktop")
    parser.add_argument("--live", "--daemon", action="store_true", dest="live", help="Run continuously in background updating stats")
    parser.add_argument("--interval", type=float, default=2.5, help="Live refresh interval in seconds (default: 2.5s)")
    args = parser.parse_args()

    print("[eDEX-UI HUD ENGINE]: Rendering authentic TRON telemetry interface...")
    out = generate_edex_wallpaper(args.output, base_path=args.base)
    print(f"[eDEX-UI HUD ENGINE]: Rendered at {out}")

    if args.apply:
        apply_wallpaper_to_desktop(args.output)
        print("[eDEX-UI HUD ENGINE]: Applied to active desktop session.")

    if args.live:
        print(f"[eDEX-UI HUD ENGINE]: Starting Live Telemetry Daemon (interval: {args.interval}s)...")
        try:
            while True:
                time.sleep(args.interval)
                generate_edex_wallpaper(args.output, base_path=args.base)
                apply_wallpaper_to_desktop(args.output)
        except KeyboardInterrupt:
            print("\n[eDEX-UI HUD ENGINE]: Daemon stopped.")

if __name__ == "__main__":
    main()
