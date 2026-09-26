from PIL import Image, ImageDraw

def create_thumbnails():
    width, height = 280, 180
    im = Image.new('RGB', (width, height), color='#1E1A1D')
    draw = ImageDraw.Draw(im)

    # Dark slate wallpaper background with macOS sweeping curves
    for y in range(height):
        ratio = y / height
        r = int(36 - ratio * 15)
        g = int(28 - ratio * 13)
        b = int(33 - ratio * 15)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # macOS Sweeping Waves on right
    draw.polygon([(140, height), (200, 90), (280, 30), (280, height)], fill='#481A2D')
    draw.polygon([(160, height), (220, 110), (280, 50), (280, height)], fill='#E95420')
    draw.polygon([(185, height), (240, 130), (280, 75), (280, height)], fill='#FFA07A')

    # Window preview (macOS Window with Traffic Lights)
    win_x, win_y, win_w, win_h = 28, 20, 175, 115
    # Window shadow
    draw.rounded_rectangle([win_x-2, win_y-2, win_x+win_w+2, win_y+win_h+2], radius=8, fill='#110E10')
    # Window body
    draw.rounded_rectangle([win_x, win_y, win_x+win_w, win_y+win_h], radius=7, fill='#F8F6F3')
    # Window titlebar (warm stone)
    draw.rectangle([win_x, win_y, win_x+win_w, win_y+22], fill='#E8E4DF')
    draw.line([(win_x, win_y+22), (win_x+win_w, win_y+22)], fill='#D2CCC4')

    # macOS Traffic Lights (Red, Yellow, Green)
    draw.ellipse([win_x+8, win_y+7, win_x+16, win_y+15], fill='#FF5F56')
    draw.ellipse([win_x+20, win_y+7, win_x+28, win_y+15], fill='#FEBC2E')
    draw.ellipse([win_x+32, win_y+7, win_x+40, win_y+15], fill='#28C840')

    # Window content (sidebar + Nemo Finder view)
    draw.rectangle([win_x, win_y+23, win_x+48, win_y+win_h-1], fill='#EAE6E1')
    draw.line([(win_x+48, win_y+23), (win_x+48, win_y+win_h-1)], fill='#D5CFC7')
    # Selected sidebar item
    draw.rounded_rectangle([win_x+4, win_y+32, win_x+44, win_y+44], radius=4, fill='#FDF2EE', outline='#FFA07A')
    
    # Selection in content (macOS folder)
    draw.rounded_rectangle([win_x+58, win_y+34, win_x+115, win_y+65], radius=4, fill='#FDF2EE', outline='#E95420')
    draw.rounded_rectangle([win_x+68, win_y+40, win_x+82, win_y+52], radius=2, fill='#E95420') # orange folder

    # Cinnamon Top/Bottom Menu Bar (macOS translucent style)
    panel_y = height - 26
    draw.rectangle([0, panel_y, width, height], fill='#E3DFD9')
    draw.line([(0, panel_y), (width, panel_y)], fill='#CCC6BE')

    # Menu button (Ubuntu orange icon)
    draw.ellipse([8, panel_y+5, 22, panel_y+19], fill='#E95420')
    draw.ellipse([12, panel_y+9, 18, panel_y+15], fill='#FFFFFF')

    # Active window list item with Ubuntu orange underline
    draw.rounded_rectangle([28, panel_y+3, 105, panel_y+23], radius=4, fill='#FAF8F5')
    draw.line([(28, panel_y+24), (105, panel_y+24)], fill='#E95420', width=2)

    # Tray applets on right
    draw.ellipse([width-55, panel_y+9, width-47, panel_y+17], fill='#48423E')
    draw.ellipse([width-40, panel_y+9, width-32, panel_y+17], fill='#48423E')
    draw.rectangle([width-24, panel_y+7, width-14, panel_y+19], fill='#D5CFC7', outline='#48423E')

    im.save("Ubuntu-Cinnamon-White/cinnamon/thumbnail.png")
    im.save("Ubuntu-Cinnamon-White/gtk-3.0/thumbnail.png")
    im.save("Ubuntu-Cinnamon-White/metacity-1/thumbnail.png")
    print("Updated thumbnails with macOS elegance successfully")

create_thumbnails()
