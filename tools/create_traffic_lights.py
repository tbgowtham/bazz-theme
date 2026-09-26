import os

def create_macos_traffic_lights():
    dirs = [
        "Ubuntu-Cinnamon-White/gtk-3.0/assets",
        "Ubuntu-Cinnamon-White/gtk-4.0/assets",
        "Ubuntu-Cinnamon-White/metacity-1"
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)

    # 1. Close Button (macOS Red/Coral with subtle border, hover cross)
    btn_close = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width="0.5"/>
</svg>'''

    btn_close_hover = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width="0.5"/>
  <path d="M5.5 5.5 L10.5 10.5 M10.5 5.5 L5.5 10.5" stroke="#4C0000" stroke-width="1.2" stroke-linecap="round"/>
</svg>'''

    btn_close_backdrop = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="6" fill="#CDC8C0" stroke="#B8B2AA" stroke-width="0.5"/>
</svg>'''

    # 2. Minimize Button (macOS Amber Yellow)
    btn_min = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="6" fill="#FEBC2E" stroke="#D89E24" stroke-width="0.5"/>
</svg>'''

    btn_min_hover = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="6" fill="#FEBC2E" stroke="#D89E24" stroke-width="0.5"/>
  <line x1="4.5" y1="8" x2="11.5" y2="8" stroke="#5A3A00" stroke-width="1.3" stroke-linecap="round"/>
</svg>'''

    btn_min_backdrop = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="6" fill="#CDC8C0" stroke="#B8B2AA" stroke-width="0.5"/>
</svg>'''

    # 3. Maximize Button (macOS Emerald Green)
    btn_max = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="6" fill="#28C840" stroke="#1AAB29" stroke-width="0.5"/>
</svg>'''

    btn_max_hover = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="6" fill="#28C840" stroke="#1AAB29" stroke-width="0.5"/>
  <path d="M5.5 6 L10.5 10 M10.5 6 L5.5 10" stroke="#003E0B" stroke-width="1.2" stroke-linecap="round"/>
</svg>'''

    btn_max_backdrop = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="6" fill="#CDC8C0" stroke="#B8B2AA" stroke-width="0.5"/>
</svg>'''

    # Metacity icons
    metacity_close = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="6" fill="#FF5F56" stroke="#E0443E" stroke-width="0.5"/>
  <path d="M5.5 5.5 L10.5 10.5 M10.5 5.5 L5.5 10.5" stroke="#4C0000" stroke-width="1.2" stroke-linecap="round"/>
</svg>'''

    metacity_min = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="6" fill="#FEBC2E" stroke="#D89E24" stroke-width="0.5"/>
  <line x1="4.5" y1="8" x2="11.5" y2="8" stroke="#5A3A00" stroke-width="1.3" stroke-linecap="round"/>
</svg>'''

    metacity_max = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="6" fill="#28C840" stroke="#1AAB29" stroke-width="0.5"/>
  <path d="M5 8 L11 8 M8 5 L8 11" stroke="#003E0B" stroke-width="1.2" stroke-linecap="round"/>
</svg>'''

    files = {
        "titlebutton-close.svg": btn_close,
        "titlebutton-close-hover.svg": btn_close_hover,
        "titlebutton-close-backdrop.svg": btn_close_backdrop,
        "titlebutton-min.svg": btn_min,
        "titlebutton-min-hover.svg": btn_min_hover,
        "titlebutton-min-backdrop.svg": btn_min_backdrop,
        "titlebutton-max.svg": btn_max,
        "titlebutton-max-hover.svg": btn_max_hover,
        "titlebutton-max-backdrop.svg": btn_max_backdrop,
    }

    for d in dirs:
        for fname, content in files.items():
            with open(os.path.join(d, fname), "w") as f:
                f.write(content)

    # Specific metacity icons
    with open("Ubuntu-Cinnamon-White/metacity-1/close-icon.svg", "w") as f:
        f.write(metacity_close)
    with open("Ubuntu-Cinnamon-White/metacity-1/min-icon.svg", "w") as f:
        f.write(metacity_min)
    with open("Ubuntu-Cinnamon-White/metacity-1/max-icon.svg", "w") as f:
        f.write(metacity_max)

    print("macOS-style traffic light assets created successfully")

create_macos_traffic_lights()
