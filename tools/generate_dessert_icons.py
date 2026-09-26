#!/usr/bin/env python3
"""
Generate Dessert-white icon theme matching the reference screenshot:
Minimalist, clean, crisp white icons with subtle Dracula accents.
"""

import os

THEME_DIR = "/home/MR_Gray/muteX/theme/icons/Dessert-white"
os.makedirs(os.path.join(THEME_DIR, "scalable/places"), exist_ok=True)
os.makedirs(os.path.join(THEME_DIR, "scalable/apps"), exist_ok=True)
os.makedirs(os.path.join(THEME_DIR, "scalable/status"), exist_ok=True)
os.makedirs(os.path.join(THEME_DIR, "scalable/actions"), exist_ok=True)
os.makedirs(os.path.join(THEME_DIR, "48x48/places"), exist_ok=True)
os.makedirs(os.path.join(THEME_DIR, "48x48/apps"), exist_ok=True)

# index.theme
index_theme = """[Icon Theme]
Name=Dessert-white
Comment=Minimalist crisp white icon theme with subtle Dracula cyberpunk accents
Inherits=Adwaita,hicolor
Directories=scalable/places,scalable/apps,scalable/status,scalable/actions,48x48/places,48x48/apps

[scalable/places]
Size=64
Type=Scalable
MinSize=16
MaxSize=256
Context=Places

[scalable/apps]
Size=64
Type=Scalable
MinSize=16
MaxSize=256
Context=Applications

[scalable/status]
Size=24
Type=Scalable
MinSize=16
MaxSize=64
Context=Status

[scalable/actions]
Size=24
Type=Scalable
MinSize=16
MaxSize=64
Context=Actions

[48x48/places]
Size=48
Type=Fixed
Context=Places

[48x48/apps]
Size=48
Type=Fixed
Context=Applications
"""

with open(os.path.join(THEME_DIR, "index.theme"), "w") as f:
    f.write(index_theme)

# Base Folder SVG Template (Frosted glass / crisp white design)
def create_folder_svg(glyph_content=""):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
  <defs>
    <linearGradient id="folder-back" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#E2E8F0"/>
      <stop offset="100%" stop-color="#CBD5E1"/>
    </linearGradient>
    <linearGradient id="folder-front" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#F1F5F9"/>
    </linearGradient>
    <filter id="shadow" x="-8%" y="-8%" width="116%" height="120%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#000000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <!-- Back Tab -->
  <path d="M 8 16 C 8 13.8 9.8 12 12 12 L 26 12 C 28 12 29.5 13 30.5 14.5 L 34 19 L 52 19 C 54.2 19 56 20.8 56 23 L 56 48 C 56 50.2 54.2 52 52 52 L 12 52 C 9.8 52 8 50.2 8 48 Z" 
        fill="url(#folder-back)" />

  <!-- Sheet -->
  <rect x="13" y="18" width="38" height="24" rx="3" fill="#8BE9FD" opacity="0.30" />

  <!-- Front Pocket -->
  <rect x="6" y="23" width="52" height="30" rx="5" fill="url(#folder-front)" filter="url(#shadow)" />

  <!-- Accent Lip Line (Dracula Cyan) -->
  <path d="M 10 24 L 54 24" stroke="#8BE9FD" stroke-width="1.5" stroke-linecap="round" />

  <!-- Glyph -->
  <g transform="translate(0, 3)">
    {glyph_content}
  </g>
</svg>"""

places_icons = {
    "folder.svg": "",
    "inode-directory.svg": "",
    "folder-documents.svg": """
      <path d="M 26 31 L 38 31 M 26 35 L 38 35 M 26 39 L 34 39" stroke="#6272A4" stroke-width="1.8" stroke-linecap="round" />
    """,
    "folder-download.svg": """
      <path d="M 32 30 L 32 40 M 27 35 L 32 40 L 37 35 M 25 43 L 39 43" stroke="#BD93F9" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" />
    """,
    "folder-music.svg": """
      <path d="M 28 41 A 3 3 0 1 1 25 38 L 25 31 L 37 28 L 37 38 A 3 3 0 1 1 34 35 L 34 30 L 28 32 Z" fill="#FF79C6" />
    """,
    "folder-pictures.svg": """
      <rect x="24" y="30" width="16" height="13" rx="2" fill="none" stroke="#50FA7B" stroke-width="1.8" />
      <circle cx="28" cy="34" r="1.5" fill="#50FA7B" />
      <path d="M 25 41 L 30 35 L 34 39 L 36 37 L 39 41" fill="none" stroke="#50FA7B" stroke-width="1.5" stroke-linejoin="round" />
    """,
    "folder-videos.svg": """
      <rect x="23" y="30" width="18" height="13" rx="2" fill="none" stroke="#FF5555" stroke-width="1.8" />
      <polygon points="30,33 36,36.5 30,40" fill="#FF5555" />
    """,
    "folder-remote.svg": """
      <circle cx="32" cy="37" r="7" fill="none" stroke="#8BE9FD" stroke-width="1.8" />
      <path d="M 25 37 L 39 37 M 32 30 C 34.5 33 34.5 41 32 44 C 29.5 41 29.5 33 32 30 Z" fill="none" stroke="#8BE9FD" stroke-width="1.5" />
    """,
    "user-home.svg": """
      <path d="M 24 37 L 32 30 L 40 37 L 40 44 C 40 45 39 46 38 46 L 26 46 C 25 46 24 45 24 44 Z" fill="none" stroke="#8BE9FD" stroke-width="1.8" stroke-linejoin="round" />
      <rect x="30" y="38" width="4" height="8" fill="#8BE9FD" />
    """,
    "user-desktop.svg": """
      <rect x="23" y="30" width="18" height="12" rx="2" fill="none" stroke="#6272A4" stroke-width="1.8" />
      <path d="M 29 44 L 35 44 M 32 42 L 32 44" stroke="#6272A4" stroke-width="1.8" stroke-linecap="round" />
    """,
    "user-trash.svg": """
      <path d="M 26 31 L 38 31 M 29 28 L 35 28 M 27 31 L 28 44 C 28 45.2 29 46 30.2 46 L 33.8 46 C 35 46 36 45.2 36 44 L 37 31" fill="none" stroke="#6272A4" stroke-width="1.8" stroke-linejoin="round" />
    """,
    "user-trash-full.svg": """
      <path d="M 26 31 L 38 31 M 29 28 L 35 28 M 27 31 L 28 44 C 28 45.2 29 46 30.2 46 L 33.8 46 C 35 46 36 45.2 36 44 L 37 31" fill="none" stroke="#FF5555" stroke-width="1.8" stroke-linejoin="round" />
      <line x1="30" y1="34" x2="30" y2="42" stroke="#FF5555" stroke-width="1.5" stroke-linecap="round"/>
      <line x1="34" y1="34" x2="34" y2="42" stroke="#FF5555" stroke-width="1.5" stroke-linecap="round"/>
    """
}

for filename, glyph in places_icons.items():
    content = create_folder_svg(glyph)
    with open(os.path.join(THEME_DIR, "scalable/places", filename), "w") as f:
        f.write(content)
    with open(os.path.join(THEME_DIR, "48x48/places", filename), "w") as f:
        f.write(content)

# Apps Icons (Clean white squircle with Dracula neon accents)
apps_icons = {
    "system-file-manager.svg": create_folder_svg("""
      <path d="M 24 37 L 32 30 L 40 37 L 40 44 C 40 45 39 46 38 46 L 26 46 C 25 46 24 45 24 44 Z" fill="none" stroke="#8BE9FD" stroke-width="1.8" stroke-linejoin="round" />
    """),
    "nemo.svg": create_folder_svg("""
      <path d="M 24 37 L 32 30 L 40 37 L 40 44 C 40 45 39 46 38 46 L 26 46 C 25 46 24 45 24 44 Z" fill="none" stroke="#8BE9FD" stroke-width="1.8" stroke-linejoin="round" />
    """),
    "utilities-terminal.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
  <rect x="6" y="8" width="52" height="48" rx="10" fill="#282A36" stroke="#44475A" stroke-width="1.5"/>
  <circle cx="14" cy="16" r="3" fill="#FF5555" />
  <circle cx="22" cy="16" r="3" fill="#F1FA8C" />
  <circle cx="30" cy="16" r="3" fill="#50FA7B" />
  <path d="M 16 28 L 26 36 L 16 44" fill="none" stroke="#50FA7B" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
  <line x1="28" y1="44" x2="42" y2="44" stroke="#8BE9FD" stroke-width="3" stroke-linecap="round" />
</svg>""",
    "kitty.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
  <rect x="6" y="8" width="52" height="48" rx="10" fill="#1E1F29" stroke="#BD93F9" stroke-width="1.5"/>
  <circle cx="14" cy="16" r="3" fill="#FF5555" />
  <circle cx="22" cy="16" r="3" fill="#F1FA8C" />
  <circle cx="30" cy="16" r="3" fill="#50FA7B" />
  <path d="M 16 28 L 26 36 L 16 44" fill="none" stroke="#FF79C6" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
  <line x1="28" y1="44" x2="42" y2="44" stroke="#8BE9FD" stroke-width="3" stroke-linecap="round" />
</svg>""",
    "preferences-system.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
  <rect x="6" y="8" width="52" height="48" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>
  <circle cx="32" cy="32" r="12" fill="none" stroke="#6272A4" stroke-width="3.5" stroke-dasharray="6,4"/>
  <circle cx="32" cy="32" r="6" fill="#BD93F9" />
</svg>"""
}

for filename, content in apps_icons.items():
    with open(os.path.join(THEME_DIR, "scalable/apps", filename), "w") as f:
        f.write(content)
    with open(os.path.join(THEME_DIR, "48x48/apps", filename), "w") as f:
        f.write(content)

# Status Icons (Crisp White Monochrome for Panel & Tray)
status_icons = {
    "audio-volume-high.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F8F8F2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5" fill="#F8F8F2"/>
  <path d="M15.54 8.46a5 5 0 0 1 0 7.07"/>
  <path d="M19.07 4.93a10 10 0 0 1 0 14.14"/>
</svg>""",
    "audio-volume-medium.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F8F8F2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5" fill="#F8F8F2"/>
  <path d="M15.54 8.46a5 5 0 0 1 0 7.07"/>
</svg>""",
    "audio-volume-low.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F8F8F2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5" fill="#F8F8F2"/>
</svg>""",
    "audio-volume-muted.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#6272A4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>
  <line x1="23" y1="9" x2="17" y2="15"/>
  <line x1="17" y1="9" x2="23" y2="15"/>
</svg>""",
    "network-wireless-signal-excellent.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F8F8F2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M5 12.55a11 11 0 0 1 14.08 0"/>
  <path d="M1.42 9a16 16 0 0 1 21.16 0"/>
  <path d="M8.53 16.11a6 6 0 0 1 6.95 0"/>
  <line x1="12" y1="20" x2="12.01" y2="20" stroke-width="3"/>
</svg>""",
    "battery-full.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#50FA7B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <rect x="2" y="7" width="16" height="10" rx="2" ry="2"/>
  <line x1="22" y1="11" x2="22" y2="13"/>
  <rect x="4" y="9" width="12" height="6" fill="#50FA7B"/>
</svg>""",
    "battery-good.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#50FA7B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <rect x="2" y="7" width="16" height="10" rx="2" ry="2"/>
  <line x1="22" y1="11" x2="22" y2="13"/>
  <rect x="4" y="9" width="9" height="6" fill="#50FA7B"/>
</svg>""",
    "bluetooth-active.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#8BE9FD" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <polyline points="6.5 6.5 17.5 17.5 12 23 12 1 17.5 6.5 6.5 17.5"/>
</svg>"""
}

for filename, content in status_icons.items():
    with open(os.path.join(THEME_DIR, "scalable/status", filename), "w") as f:
        f.write(content)

# Actions Icons
actions_icons = {
    "system-search.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F8F8F2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="11" cy="11" r="8"/>
  <line x1="21" y1="21" x2="16.65" y2="16.65"/>
</svg>""",
    "edit-find.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#8BE9FD" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="11" cy="11" r="8"/>
  <line x1="21" y1="21" x2="16.65" y2="16.65"/>
</svg>"""
}

for filename, content in actions_icons.items():
    with open(os.path.join(THEME_DIR, "scalable/actions", filename), "w") as f:
        f.write(content)

print("Dessert-white icon theme generated successfully!")
