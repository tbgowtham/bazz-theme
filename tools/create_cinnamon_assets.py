import os

def create_cinnamon_assets():
    os.makedirs("Ubuntu-Cinnamon-White/cinnamon/assets", exist_ok=True)
    
    # 1. checkbox-checked.svg (Ubuntu orange #E95420 with white checkmark)
    with open("Ubuntu-Cinnamon-White/cinnamon/assets/checkbox-checked.svg", "w") as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <rect x="0.5" y="0.5" width="15" height="15" rx="3" fill="#E95420" stroke="#C74010" stroke-width="1"/>
  <path d="M4 8.2 L6.8 11 L12 5" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>''')

    # 2. checkbox-unchecked.svg (clean off-white with subtle gray border)
    with open("Ubuntu-Cinnamon-White/cinnamon/assets/checkbox-unchecked.svg", "w") as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <rect x="0.5" y="0.5" width="15" height="15" rx="3" fill="#FFFFFF" stroke="#C5C7CC" stroke-width="1"/>
</svg>''')

    # 3. radio-checked.svg (circle with orange dot)
    with open("Ubuntu-Cinnamon-White/cinnamon/assets/radio-checked.svg", "w") as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="7.5" fill="#FFFFFF" stroke="#E95420" stroke-width="1.5"/>
  <circle cx="8" cy="8" r="4" fill="#E95420"/>
</svg>''')

    # 4. radio-unchecked.svg
    with open("Ubuntu-Cinnamon-White/cinnamon/assets/radio-unchecked.svg", "w") as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="7.5" fill="#FFFFFF" stroke="#C5C7CC" stroke-width="1"/>
</svg>''')

    # 5. switch-on.svg (Ubuntu Orange pill with white handle)
    with open("Ubuntu-Cinnamon-White/cinnamon/assets/switch-on.svg", "w") as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" width="38" height="20" viewBox="0 0 38 20">
  <rect x="1" y="1" width="36" height="18" rx="9" fill="#E95420"/>
  <circle cx="28" cy="10" r="7.5" fill="#FFFFFF" filter="drop-shadow(0 1px 2px rgba(0,0,0,0.15))"/>
</svg>''')

    # 6. switch-off.svg (Neutral gray pill with white handle)
    with open("Ubuntu-Cinnamon-White/cinnamon/assets/switch-off.svg", "w") as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" width="38" height="20" viewBox="0 0 38 20">
  <rect x="1" y="1" width="36" height="18" rx="9" fill="#E0E2E6"/>
  <circle cx="10" cy="10" r="7.5" fill="#FFFFFF" stroke="#D0D3D9" stroke-width="0.5" filter="drop-shadow(0 1px 2px rgba(0,0,0,0.12))"/>
</svg>''')

    # 7. close.svg (charcoal close icon)
    with open("Ubuntu-Cinnamon-White/cinnamon/assets/close.svg", "w") as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <line x1="4" y1="4" x2="12" y2="12" stroke="#444444" stroke-width="1.8" stroke-linecap="round"/>
  <line x1="12" y1="4" x2="4" y2="12" stroke="#444444" stroke-width="1.8" stroke-linecap="round"/>
</svg>''')

    # 8. close-hover.svg (Ubuntu orange circle with white x)
    with open("Ubuntu-Cinnamon-White/cinnamon/assets/close-hover.svg", "w") as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="7.5" fill="#E95420"/>
  <line x1="5" y1="5" x2="11" y2="11" stroke="#FFFFFF" stroke-width="1.8" stroke-linecap="round"/>
  <line x1="11" y1="5" x2="5" y2="11" stroke="#FFFFFF" stroke-width="1.8" stroke-linecap="round"/>
</svg>''')

    # 9. menu-arrow.svg
    with open("Ubuntu-Cinnamon-White/cinnamon/assets/menu-arrow.svg", "w") as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12">
  <path d="M4 2 L8 6 L4 10" fill="none" stroke="#555555" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>''')

    # 10. menu-arrow-hover.svg
    with open("Ubuntu-Cinnamon-White/cinnamon/assets/menu-arrow-hover.svg", "w") as f:
        f.write('''<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12">
  <path d="M4 2 L8 6 L4 10" fill="none" stroke="#E95420" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>''')

    print("Cinnamon assets created successfully")

create_cinnamon_assets()
