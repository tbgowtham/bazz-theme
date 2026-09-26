import os
from PIL import Image, ImageDraw

def create_grub_theme():
    grub_dir = "grub/ubuntu-cinnamon"
    icons_dir = os.path.join(grub_dir, "icons")
    os.makedirs(icons_dir, exist_ok=True)

    # 1. Background image (1366 x 867) - Elegant Dark Slate / Aubergine
    width, height = 1366, 867
    bg = Image.new('RGB', (width, height), color='#262124')
    draw = ImageDraw.Draw(bg)

    # Dark slate gradient (comfortable on eyes at boot time)
    for y in range(height):
        ratio = y / height
        r = int(45 - ratio * 15)
        g = int(38 - ratio * 14)
        b = int(41 - ratio * 15)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Right side geometric facets
    draw.polygon([(850, 0), (width, 0), (width, 520), (950, 360)], fill='#2F282B')
    draw.polygon([(920, 100), (1260, 60), (1160, 500), (900, 390)], fill='#382F33', outline='#50454A')
    draw.polygon([(1000, 180), (1200, 130), (1120, 420)], fill='#E95420')
    draw.polygon([(1120, 420), (1240, 480), (1050, 540)], fill='#C74010')

    # Ubuntu minimalist emblem on right
    cx, cy = 1060, 300
    draw.ellipse([cx-52, cy-52, cx+52, cy+52], outline='#251F22', width=8)
    draw.ellipse([cx-52, cy-52, cx+52, cy+52], outline='#E95420', width=5)
    draw.ellipse([cx-16, cy-16, cx+16, cy+16], fill='#E95420')

    # Top Header Logo/Text
    draw.rounded_rectangle([width//2 - 140, 90, width//2 + 140, 140], radius=8, fill='#2F282B', outline='#483F43')
    draw.rounded_rectangle([width//2 - 130, 98, width//2 - 50, 132], radius=6, fill='#E95420')

    bg.save(os.path.join(grub_dir, "background.png"))
    print("GRUB background.png updated (1366x867 dark slate)")

    # 2. Selection bar slices (3-slice or single slice)
    sel_h = 38
    im_w = Image.new('RGBA', (8, sel_h), (0, 0, 0, 0))
    d_w = ImageDraw.Draw(im_w)
    d_w.rounded_rectangle([0, 0, 16, sel_h-1], radius=6, fill='#E95420')
    im_w.save(os.path.join(grub_dir, "select_w.png"))

    im_c = Image.new('RGBA', (16, sel_h), '#E95420')
    im_c.save(os.path.join(grub_dir, "select_c.png"))

    im_e = Image.new('RGBA', (8, sel_h), (0, 0, 0, 0))
    d_e = ImageDraw.Draw(im_e)
    d_e.rounded_rectangle([-8, 0, 7, sel_h-1], radius=6, fill='#E95420')
    im_e.save(os.path.join(grub_dir, "select_e.png"))

    # 3. Boot Icons
    def make_icon(fill_color, symbol=''):
        ico = Image.new('RGBA', (24, 24), (0, 0, 0, 0))
        d = ImageDraw.Draw(ico)
        d.ellipse([2, 2, 21, 21], fill=fill_color)
        if symbol == 'ubuntu':
            d.ellipse([9, 9, 14, 14], fill='#FFFFFF')
        elif symbol == 'mint':
            d.rectangle([7, 8, 16, 15], outline='#FFFFFF', width=2)
        elif symbol == 'win':
            d.rectangle([6, 6, 11, 11], fill='#FFFFFF')
            d.rectangle([12, 6, 17, 11], fill='#FFFFFF')
            d.rectangle([6, 12, 11, 17], fill='#FFFFFF')
            d.rectangle([12, 12, 17, 17], fill='#FFFFFF')
        return ico

    make_icon('#E95420', 'ubuntu').save(os.path.join(icons_dir, "ubuntu.png"))
    make_icon('#483F43', 'ubuntu').save(os.path.join(icons_dir, "gnu-linux.png"))
    make_icon('#688F30', 'mint').save(os.path.join(icons_dir, "linuxmint.png"))
    make_icon('#0078D7', 'win').save(os.path.join(icons_dir, "windows.png"))

    # 4. theme.txt
    theme_txt = f'''# ===================================================================
# Ubuntu Cinnamon Professional Theme for GRUB (1366x867)
# Non-glaring dark slate background with Ubuntu Orange #E95420 accent
# ===================================================================

title-text: ""
desktop-image: "background.png"
desktop-color: "#262124"
terminal-font: "Unifont Regular 16"
terminal-box: "select_c.png"

# Boot Menu
+ boot_menu {{
    left = 22%
    top = 28%
    width = 56%
    height = 42%
    item_color = "#E0DCD8"
    selected_item_color = "#FFFFFF"
    item_height = 40
    item_padding = 10
    item_spacing = 8
    icon_width = 24
    icon_height = 24
    item_icon_space = 14
    selected_item_pixmap_style = "select_*.png"
}}

# Timeout Countdown Progress Bar
+ progress_bar {{
    id = "__timeout__"
    left = 22%
    top = 74%
    width = 56%
    height = 6
    show_text = false
    fg_color = "#E95420"
    bg_color = "#382F33"
    border_color = "#483F43"
}}

# Navigation Guide
+ label {{
    top = 80%
    left = 22%
    width = 56%
    align = "center"
    color = "#A8A09A"
    text = "Use the arrow keys to select an OS, then press Enter to boot."
}}

+ label {{
    top = 84%
    left = 22%
    width = 56%
    align = "center"
    color = "#7A736E"
    text = "Press 'e' to edit boot parameters or 'c' for a command-line."
}}
'''
    with open(os.path.join(grub_dir, "theme.txt"), "w") as f:
        f.write(theme_txt)

    print("GRUB theme updated successfully")

create_grub_theme()
