import os, shutil

def create_gtk_assets():
    dirs = [
        "Ubuntu-Cinnamon-White/gtk-3.0/assets",
        "Ubuntu-Cinnamon-White/gtk-4.0/assets"
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    
    # Checkboxes
    cb_checked = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <rect x="0.5" y="0.5" width="15" height="15" rx="3" fill="#E95420" stroke="#C74010" stroke-width="1"/>
  <path d="M4 8.2 L6.8 11 L12 5" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

    cb_unchecked = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <rect x="0.5" y="0.5" width="15" height="15" rx="3" fill="#FFFFFF" stroke="#C5C7CC" stroke-width="1"/>
</svg>'''

    cb_checked_hover = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <rect x="0.5" y="0.5" width="15" height="15" rx="3" fill="#FF6332" stroke="#E95420" stroke-width="1"/>
  <path d="M4 8.2 L6.8 11 L12 5" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

    cb_unchecked_hover = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <rect x="0.5" y="0.5" width="15" height="15" rx="3" fill="#FDF2EE" stroke="#E95420" stroke-width="1"/>
</svg>'''

    # Radios
    radio_checked = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="7.5" fill="#FFFFFF" stroke="#E95420" stroke-width="1.5"/>
  <circle cx="8" cy="8" r="4" fill="#E95420"/>
</svg>'''

    radio_unchecked = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="7.5" fill="#FFFFFF" stroke="#C5C7CC" stroke-width="1"/>
</svg>'''

    radio_checked_hover = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="7.5" fill="#FDF2EE" stroke="#FF6332" stroke-width="1.5"/>
  <circle cx="8" cy="8" r="4.2" fill="#FF6332"/>
</svg>'''

    radio_unchecked_hover = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="7.5" fill="#FDF2EE" stroke="#E95420" stroke-width="1"/>
</svg>'''

    # Switches
    switch_on = '''<svg xmlns="http://www.w3.org/2000/svg" width="38" height="20" viewBox="0 0 38 20">
  <rect x="1" y="1" width="36" height="18" rx="9" fill="#E95420"/>
  <circle cx="28" cy="10" r="7.5" fill="#FFFFFF"/>
</svg>'''

    switch_off = '''<svg xmlns="http://www.w3.org/2000/svg" width="38" height="20" viewBox="0 0 38 20">
  <rect x="1" y="1" width="36" height="18" rx="9" fill="#E0E2E6"/>
  <circle cx="10" cy="10" r="7.5" fill="#FFFFFF" stroke="#D0D3D9" stroke-width="0.5"/>
</svg>'''

    # Window titlebar buttons (close, min, max)
    btn_close = '''<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18">
  <circle cx="9" cy="9" r="8" fill="#E95420"/>
  <path d="M6 6 L12 12 M12 6 L6 12" stroke="#FFFFFF" stroke-width="1.6" stroke-linecap="round"/>
</svg>'''

    btn_close_backdrop = '''<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18">
  <circle cx="9" cy="9" r="8" fill="#D5D7DC"/>
  <path d="M6 6 L12 12 M12 6 L6 12" stroke="#888888" stroke-width="1.6" stroke-linecap="round"/>
</svg>'''

    btn_min = '''<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18">
  <circle cx="9" cy="9" r="8" fill="#E5E7EB"/>
  <line x1="5.5" y1="9" x2="12.5" y2="9" stroke="#444444" stroke-width="1.8" stroke-linecap="round"/>
</svg>'''

    btn_max = '''<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18">
  <circle cx="9" cy="9" r="8" fill="#E5E7EB"/>
  <rect x="5.5" y="5.5" width="7" height="7" rx="1" fill="none" stroke="#444444" stroke-width="1.6"/>
</svg>'''

    files = {
        "checkbox-checked.svg": cb_checked,
        "checkbox-unchecked.svg": cb_unchecked,
        "checkbox-checked-hover.svg": cb_checked_hover,
        "checkbox-unchecked-hover.svg": cb_unchecked_hover,
        "radio-checked.svg": radio_checked,
        "radio-unchecked.svg": radio_unchecked,
        "radio-checked-hover.svg": radio_checked_hover,
        "radio-unchecked-hover.svg": radio_unchecked_hover,
        "switch-on.svg": switch_on,
        "switch-off.svg": switch_off,
        "titlebutton-close.svg": btn_close,
        "titlebutton-close-backdrop.svg": btn_close_backdrop,
        "titlebutton-min.svg": btn_min,
        "titlebutton-max.svg": btn_max,
    }

    for d in dirs:
        for fname, content in files.items():
            with open(os.path.join(d, fname), "w") as f:
                f.write(content)

    print("GTK 3.0 & 4.0 vector assets created successfully")

create_gtk_assets()
