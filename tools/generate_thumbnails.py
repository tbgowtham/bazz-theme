#!/usr/bin/env python3
"""
Generate theme preview thumbnails matching the reference screenshot:
Cyberpunk anime cockpit background, dark translucent terminal window,
right-aligned traffic lights (Yellow, Green, Red), and Dracula neon accents.
"""

import os
from PIL import Image, ImageDraw, ImageFont

def create_thumbnails():
    width, height = 280, 180
    
    # 1. Base Wallpaper
    bg_path = "/home/MR_Gray/muteX/theme/wallpapers/dracula-cyberpunk-cockpit.png"
    if os.path.exists(bg_path):
        bg = Image.open(bg_path).resize((width, height), Image.Resampling.LANCZOS)
        # Apply slight dark overlay for UI contrast
        overlay = Image.new('RGBA', (width, height), (15, 16, 24, 70))
        im = Image.alpha_composite(bg.convert('RGBA'), overlay).convert('RGB')
    else:
        im = Image.new('RGB', (width, height), color='#1E1F29')
        
    draw = ImageDraw.Draw(im)

    # 2. Slim Top Panel (Dracula Slim)
    panel_h = 16
    draw.rectangle([0, 0, width, panel_h], fill='#1E1F29')
    draw.line([(0, panel_h), (width, panel_h)], fill='#44475A', width=1)
    
    # Top bar menu / clock indicators
    draw.text((10, 2), "Cinnamon", fill='#F8F8F2')
    draw.text((width - 45, 2), "13:37", fill='#8BE9FD')
    draw.ellipse([width - 12, 5, width - 6, 11], fill='#50FA7B')

    # 3. Translucent Terminal Window (Centered, exactly like reference)
    win_x, win_y, win_w, win_h = 35, 28, 210, 135
    
    # Window Shadow
    draw.rounded_rectangle([win_x-2, win_y-2, win_x+win_w+2, win_y+win_h+2], radius=6, fill='#0D0E15')
    
    # Window Body (Dark translucent glass effect)
    draw.rounded_rectangle([win_x, win_y, win_x+win_w, win_y+win_h], radius=5, fill='#1E1F29', outline='#44475A')
    
    # Titlebar
    tb_h = 18
    draw.rectangle([win_x, win_y, win_x+win_w, win_y+tb_h], fill='#282A36')
    draw.line([(win_x, win_y+tb_h), (win_x+win_w, win_y+tb_h)], fill='#44475A', width=1)
    
    # Title text
    draw.text((win_x + 10, win_y + 3), "user@cyberpunk:~", fill='#F8F8F2')
    
    # Right-aligned Traffic Lights (Yellow, Green, Red)
    b_y = win_y + 5
    draw.ellipse([win_x + win_w - 34, b_y, win_x + win_w - 26, b_y + 8], fill='#F1FA8C') # Min (Yellow)
    draw.ellipse([win_x + win_w - 22, b_y, win_x + win_w - 14, b_y + 8], fill='#50FA7B') # Max (Green)
    draw.ellipse([win_x + win_w - 10, b_y, win_x + win_w - 2, b_y + 8], fill='#FF5555')  # Close (Red)

    # Neofetch specs in Terminal Body
    draw.text((win_x + 12, win_y + 24), "OS -> Arch Linux x86_64", fill='#50FA7B')
    draw.text((win_x + 12, win_y + 38), "Kernel -> 6.3.8-zen", fill='#8BE9FD')
    draw.text((win_x + 12, win_y + 52), "Theme -> Dracula-slim", fill='#BD93F9')
    draw.text((win_x + 12, win_y + 66), "Icons -> Dessert-white", fill='#FF79C6')

    # Color blocks bar at bottom of terminal
    palette_colors = ['#282A36', '#FF5555', '#50FA7B', '#F1FA8C', '#BD93F9', '#FF79C6', '#8BE9FD', '#F8F8F2']
    for idx, c in enumerate(palette_colors):
        px = win_x + 12 + (idx * 10)
        draw.rectangle([px, win_y + 90, px + 8, win_y + 98], fill=c)

    destinations = [
        "Dracula-Slim/cinnamon/thumbnail.png",
        "Dracula-Slim/gtk-3.0/thumbnail.png",
        "Dracula-Slim/metacity-1/thumbnail.png",
        "Ubuntu-Cinnamon-White/cinnamon/thumbnail.png",
        "Ubuntu-Cinnamon-White/gtk-3.0/thumbnail.png",
        "Ubuntu-Cinnamon-White/metacity-1/thumbnail.png"
    ]

    for dest in destinations:
        dest_path = os.path.join("/home/MR_Gray/muteX/theme", dest)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        im.save(dest_path)

    print("Updated thumbnails with Dracula-Slim aesthetic successfully!")

if __name__ == "__main__":
    create_thumbnails()
