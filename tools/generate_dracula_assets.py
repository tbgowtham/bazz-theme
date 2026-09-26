#!/usr/bin/env python3
"""
Generate window controls, checkboxes, radios, switches, and assets
for Dracula-Slim and Ubuntu-Cinnamon-White matching the reference image.
"""

import os

THEMES = [
    "/home/MR_Gray/muteX/theme/Dracula-Slim",
    "/home/MR_Gray/muteX/theme/Ubuntu-Cinnamon-White"
]

def make_circle_svg(color, hover=False, backdrop=False, symbol=None):
    opacity = "0.45" if backdrop else "1.0"
    sym_html = ""
    if hover and symbol == "close":
        sym_html = '<path d="M 5 5 L 11 11 M 11 5 L 5 11" stroke="#4C0000" stroke-width="1.3" stroke-linecap="round"/>'
    elif hover and symbol == "min":
        sym_html = '<path d="M 4 8 L 12 8" stroke="#5E4E00" stroke-width="1.3" stroke-linecap="round"/>'
    elif hover and symbol == "max":
        sym_html = '<path d="M 5 5 L 11 5 L 11 11 M 11 5 L 5 11" stroke="#004D1A" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>'
    
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="6" fill="{color}" opacity="{opacity}"/>
  {sym_html}
</svg>"""

buttons = {
    "titlebutton-close.svg": make_circle_svg("#FF5555", False, False, "close"),
    "titlebutton-close-hover.svg": make_circle_svg("#FF6E6E", True, False, "close"),
    "titlebutton-close-backdrop.svg": make_circle_svg("#6272A4", False, True, "close"),
    
    "titlebutton-min.svg": make_circle_svg("#F1FA8C", False, False, "min"),
    "titlebutton-min-hover.svg": make_circle_svg("#FFFFA5", True, False, "min"),
    "titlebutton-min-backdrop.svg": make_circle_svg("#6272A4", False, True, "min"),
    
    "titlebutton-max.svg": make_circle_svg("#50FA7B", False, False, "max"),
    "titlebutton-max-hover.svg": make_circle_svg("#69FF94", True, False, "max"),
    "titlebutton-max-backdrop.svg": make_circle_svg("#6272A4", False, True, "max"),
}

# Switches, checkboxes, radios
checkbox_checked = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <rect x="1" y="1" width="14" height="14" rx="3" fill="#BD93F9" stroke="#BD93F9" stroke-width="1"/>
  <path d="M 4 8 L 7 11 L 12 5" fill="none" stroke="#282A36" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

checkbox_unchecked = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <rect x="1" y="1" width="14" height="14" rx="3" fill="#282A36" stroke="#6272A4" stroke-width="1.5"/>
</svg>"""

checkbox_checked_hover = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <rect x="1" y="1" width="14" height="14" rx="3" fill="#FF79C6" stroke="#FF79C6" stroke-width="1"/>
  <path d="M 4 8 L 7 11 L 12 5" fill="none" stroke="#282A36" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

checkbox_unchecked_hover = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <rect x="1" y="1" width="14" height="14" rx="3" fill="#343746" stroke="#8BE9FD" stroke-width="1.5"/>
</svg>"""

radio_checked = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="7" fill="#282A36" stroke="#BD93F9" stroke-width="1.5"/>
  <circle cx="8" cy="8" r="3.5" fill="#BD93F9"/>
</svg>"""

radio_unchecked = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="7" fill="#282A36" stroke="#6272A4" stroke-width="1.5"/>
</svg>"""

radio_checked_hover = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="7" fill="#343746" stroke="#FF79C6" stroke-width="1.5"/>
  <circle cx="8" cy="8" r="3.5" fill="#FF79C6"/>
</svg>"""

radio_unchecked_hover = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="7" fill="#343746" stroke="#8BE9FD" stroke-width="1.5"/>
</svg>"""

switch_on = """<svg xmlns="http://www.w3.org/2000/svg" width="36" height="20" viewBox="0 0 36 20">
  <rect x="1" y="1" width="34" height="18" rx="9" fill="#50FA7B" />
  <circle cx="26" cy="10" r="7" fill="#282A36" />
</svg>"""

switch_off = """<svg xmlns="http://www.w3.org/2000/svg" width="36" height="20" viewBox="0 0 36 20">
  <rect x="1" y="1" width="34" height="18" rx="9" fill="#44475A" />
  <circle cx="10" cy="10" r="7" fill="#F8F8F2" />
</svg>"""

widgets = {
    "checkbox-checked.svg": checkbox_checked,
    "checkbox-unchecked.svg": checkbox_unchecked,
    "checkbox-checked-hover.svg": checkbox_checked_hover,
    "checkbox-unchecked-hover.svg": checkbox_unchecked_hover,
    "radio-checked.svg": radio_checked,
    "radio-unchecked.svg": radio_unchecked,
    "radio-checked-hover.svg": radio_checked_hover,
    "radio-unchecked-hover.svg": radio_unchecked_hover,
    "switch-on.svg": switch_on,
    "switch-off.svg": switch_off,
}

for theme_path in THEMES:
    # Metacity
    meta_dir = os.path.join(theme_path, "metacity-1")
    os.makedirs(meta_dir, exist_ok=True)
    for name, content in buttons.items():
        with open(os.path.join(meta_dir, name), "w") as f:
            f.write(content)
            
    # GTK 3.0 assets
    gtk3_dir = os.path.join(theme_path, "gtk-3.0/assets")
    os.makedirs(gtk3_dir, exist_ok=True)
    for name, content in buttons.items():
        with open(os.path.join(gtk3_dir, name), "w") as f:
            f.write(content)
    for name, content in widgets.items():
        with open(os.path.join(gtk3_dir, name), "w") as f:
            f.write(content)

    # GTK 4.0 assets
    gtk4_dir = os.path.join(theme_path, "gtk-4.0/assets")
    os.makedirs(gtk4_dir, exist_ok=True)
    for name, content in buttons.items():
        with open(os.path.join(gtk4_dir, name), "w") as f:
            f.write(content)
    for name, content in widgets.items():
        with open(os.path.join(gtk4_dir, name), "w") as f:
            f.write(content)

    # Cinnamon assets
    cin_dir = os.path.join(theme_path, "cinnamon/assets")
    os.makedirs(cin_dir, exist_ok=True)
    for name, content in widgets.items():
        with open(os.path.join(cin_dir, name), "w") as f:
            f.write(content)

print("Dracula theme assets generated successfully!")
