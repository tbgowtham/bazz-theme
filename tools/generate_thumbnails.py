from PIL import Image, ImageDraw, ImageFont
import os

def create_cinnamon_thumbnail():
    width, height = 280, 180
    im = Image.new('RGB', (width, height), color='#F5F6F9')
    draw = ImageDraw.Draw(im)

    # Wallpaper background preview with subtle geometric orange accent
    for y in range(height):
        ratio = y / height
        # off-white gradient
        r = int(250 - ratio * 8)
        g = int(251 - ratio * 7)
        b = int(253 - ratio * 6)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Geometric orange accents on right
    draw.polygon([(180, 20), (270, 10), (250, 110), (160, 90)], fill='#FFFFFF', outline='#E5E7EB')
    draw.polygon([(190, 40), (260, 30), (230, 100)], fill='#E95420')
    draw.polygon([(230, 100), (260, 115), (210, 135)], fill='#FFA07A')

    # Window preview
    win_x, win_y, win_w, win_h = 30, 25, 170, 105
    # Window shadow
    draw.rounded_rectangle([win_x-1, win_y-1, win_x+win_w+1, win_y+win_h+1], radius=6, fill='#E2E4E8')
    # Window body
    draw.rounded_rectangle([win_x, win_y, win_x+win_w, win_y+win_h], radius=5, fill='#FFFFFF')
    # Window titlebar
    draw.rectangle([win_x, win_y, win_x+win_w, win_y+20], fill='#F8F9FA')
    draw.line([(win_x, win_y+20), (win_x+win_w, win_y+20)], fill='#E5E7EB')

    # Window controls (close = orange, min/max = gray)
    draw.ellipse([win_x+6, win_y+5, win_x+16, win_y+15], fill='#E95420')
    draw.ellipse([win_x+20, win_y+5, win_x+30, win_y+15], fill='#D0D3D9')
    draw.ellipse([win_x+34, win_y+5, win_x+44, win_y+15], fill='#D0D3D9')

    # Window content (sidebar + Nemo view)
    draw.rectangle([win_x, win_y+21, win_x+45, win_y+win_h-1], fill='#F7F8FA')
    draw.line([(win_x+45, win_y+21), (win_x+45, win_y+win_h-1)], fill='#E5E7EB')
    # Selected sidebar item
    draw.rounded_rectangle([win_x+4, win_y+30, win_x+41, win_y+42], radius=3, fill='#FDF2EE', outline='#FFA07A')
    
    # Selection in content
    draw.rounded_rectangle([win_x+55, win_y+32, win_x+110, win_y+62], radius=3, fill='#FDF2EE', outline='#E95420')
    draw.rectangle([win_x+65, win_y+38, win_x+77, win_y+48], fill='#E95420') # orange folder

    # Cinnamon Bottom Panel (height 28)
    panel_y = height - 28
    draw.rectangle([0, panel_y, width, height], fill='#FAFAFB')
    draw.line([(0, panel_y), (width, panel_y)], fill='#E2E4E8')

    # Menu button (Ubuntu orange icon/circle)
    draw.ellipse([8, panel_y+6, 24, panel_y+22], fill='#E95420')
    draw.ellipse([13, panel_y+11, 19, panel_y+17], fill='#FFFFFF')

    # Active window list item with Ubuntu orange underline
    draw.rounded_rectangle([32, panel_y+3, 105, panel_y+25], radius=3, fill='#FDECE5')
    draw.line([(32, panel_y+26), (105, panel_y+26)], fill='#E95420', width=2)

    # Tray applets on right
    draw.ellipse([width-55, panel_y+10, width-47, panel_y+18], fill='#555555')
    draw.ellipse([width-40, panel_y+10, width-32, panel_y+18], fill='#555555')
    draw.rectangle([width-24, panel_y+8, width-14, panel_y+20], fill='#E5E7EB', outline='#555555')
    draw.line([(width-4, panel_y), (width-4, height)], fill='#E2E4E8')

    im.save("Ubuntu-Cinnamon-White/cinnamon/thumbnail.png")
    im.save("Ubuntu-Cinnamon-White/gtk-3.0/thumbnail.png")
    im.save("Ubuntu-Cinnamon-White/metacity-1/thumbnail.png")
    print("Thumbnails generated successfully")

create_cinnamon_thumbnail()
