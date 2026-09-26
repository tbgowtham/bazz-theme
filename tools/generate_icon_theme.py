#!/usr/bin/env python3
"""
Generate Jarvis-White Icon Theme:
Minimalist, clean, crisp white and cyan line-art icons for Linux Cinnamon, GNOME, and KDE.
"""

import os

THEME_DIR = "/home/MR_Gray/muteX/theme/icons/Jarvis-White"
os.makedirs(os.path.join(THEME_DIR, "scalable/places"), exist_ok=True)
os.makedirs(os.path.join(THEME_DIR, "scalable/apps"), exist_ok=True)
os.makedirs(os.path.join(THEME_DIR, "scalable/status"), exist_ok=True)
os.makedirs(os.path.join(THEME_DIR, "scalable/actions"), exist_ok=True)
os.makedirs(os.path.join(THEME_DIR, "48x48/places"), exist_ok=True)
os.makedirs(os.path.join(THEME_DIR, "48x48/apps"), exist_ok=True)

# 1. index.theme
index_theme = """[Icon Theme]
Name=Jarvis-White
Comment=High-Tech Minimalist White and Cyan Line-Art Icon Theme for Stark OS and Cinnamon
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

# 2. Places Icons (Minimalist Frosted White Folders with Stark Cyan Accent)
def make_folder_svg(badge_path=""):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48">
  <defs>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#00e5ff" flood-opacity="0.3"/>
    </filter>
  </defs>
  <!-- Folder Back Tab -->
  <path d="M 6,12 C 6,10 7,9 9,9 L 18,9 L 22,13 L 39,13 C 41,13 42,14 42,16 L 42,20 L 6,20 Z" fill="#202b3c" stroke="#00e5ff" stroke-width="1.2" stroke-linejoin="round"/>
  <!-- Folder Front Sheet -->
  <path d="M 5,17 C 5,15.5 6,14.5 8,14.5 L 40,14.5 C 42,14.5 43,15.5 43,17 L 43,38 C 43,39.5 42,40.5 40,40.5 L 8,40.5 C 6,40.5 5,39.5 5,38 Z" fill="#0d1829" stroke="#f0f6fc" stroke-width="1.5" stroke-linejoin="round" filter="url(#glow)"/>
  <!-- Holographic accent line -->
  <line x1="10" y1="20" x2="38" y2="20" stroke="#00e5ff" stroke-width="1" opacity="0.6"/>
  {badge_path}
</svg>"""

places = {
    "folder.svg": "",
    "inode-directory.svg": "",
    "user-home.svg": '<path d="M 19,33 L 19,26 L 29,26 L 29,33 M 16,27 L 24,19 L 32,27" fill="none" stroke="#00e5ff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>',
    "user-desktop.svg": '<rect x="18" y="24" width="12" height="8" rx="1" fill="none" stroke="#00e5ff" stroke-width="1.4"/><line x1="22" y1="34" x2="26" y2="34" stroke="#00e5ff" stroke-width="1.4"/><line x1="24" y1="32" x2="24" y2="34" stroke="#00e5ff" stroke-width="1.4"/>',
    "folder-documents.svg": '<line x1="19" y1="24" x2="29" y2="24" stroke="#00e5ff" stroke-width="1.4" stroke-linecap="round"/><line x1="19" y1="28" x2="29" y2="28" stroke="#00e5ff" stroke-width="1.4" stroke-linecap="round"/><line x1="19" y1="32" x2="25" y2="32" stroke="#00e5ff" stroke-width="1.4" stroke-linecap="round"/>',
    "folder-download.svg": '<path d="M 24,22 L 24,31 M 20,28 L 24,32 L 28,28" fill="none" stroke="#00e5ff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>',
    "folder-music.svg": '<circle cx="21" cy="31" r="2.5" fill="#00e5ff"/><circle cx="29" cy="29" r="2.5" fill="#00e5ff"/><path d="M 23.5,31 L 23.5,23 L 31.5,21 L 31.5,29" fill="none" stroke="#00e5ff" stroke-width="1.4" stroke-linecap="round"/>',
    "folder-pictures.svg": '<circle cx="21" cy="24" r="1.5" fill="#00e5ff"/><path d="M 18,33 L 23,27 L 26,30 L 28,28 L 31,33 Z" fill="none" stroke="#00e5ff" stroke-width="1.3" stroke-linejoin="round"/>',
    "folder-videos.svg": '<rect x="18" y="24" width="12" height="8" rx="1" fill="none" stroke="#00e5ff" stroke-width="1.4"/><polygon points="23,26 27,28 23,30" fill="#00e5ff"/>',
    "folder-remote.svg": '<circle cx="24" cy="28" r="5" fill="none" stroke="#00e5ff" stroke-width="1.4"/><line x1="19" y1="28" x2="29" y2="28" stroke="#00e5ff" stroke-width="1.2"/>'
}

for fname, badge in places.items():
    content = make_folder_svg(badge)
    with open(os.path.join(THEME_DIR, "scalable/places", fname), "w") as f:
        f.write(content)
    with open(os.path.join(THEME_DIR, "48x48/places", fname), "w") as f:
        f.write(content)

# Trash icons
trash_empty = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48">
  <path d="M 14,14 L 34,14 L 32,38 C 32,40 30,41 29,41 L 19,41 C 18,41 16,40 16,38 Z" fill="#0d1829" stroke="#f0f6fc" stroke-width="1.5" stroke-linejoin="round"/>
  <line x1="11" y1="14" x2="37" y2="14" stroke="#00e5ff" stroke-width="1.8" stroke-linecap="round"/>
  <path d="M 20,14 L 20,10 C 20,9 21,8 22,8 L 26,8 C 27,8 28,9 28,10 L 28,14" fill="none" stroke="#00e5ff" stroke-width="1.4"/>
</svg>"""

trash_full = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48">
  <path d="M 14,14 L 34,14 L 32,38 C 32,40 30,41 29,41 L 19,41 C 18,41 16,40 16,38 Z" fill="#0d1829" stroke="#f0f6fc" stroke-width="1.5" stroke-linejoin="round"/>
  <line x1="11" y1="14" x2="37" y2="14" stroke="#ff2a5f" stroke-width="1.8" stroke-linecap="round"/>
  <path d="M 20,14 L 20,10 C 20,9 21,8 22,8 L 26,8 C 27,8 28,9 28,10 L 28,14" fill="none" stroke="#ff2a5f" stroke-width="1.4"/>
  <line x1="21" y1="20" x2="21" y2="34" stroke="#ff2a5f" stroke-width="1.3" stroke-linecap="round"/>
  <line x1="27" y1="20" x2="27" y2="34" stroke="#ff2a5f" stroke-width="1.3" stroke-linecap="round"/>
</svg>"""

with open(os.path.join(THEME_DIR, "scalable/places/user-trash.svg"), "w") as f:
    f.write(trash_empty)
with open(os.path.join(THEME_DIR, "48x48/places/user-trash.svg"), "w") as f:
    f.write(trash_empty)
with open(os.path.join(THEME_DIR, "scalable/places/user-trash-full.svg"), "w") as f:
    f.write(trash_full)
with open(os.path.join(THEME_DIR, "48x48/places/user-trash-full.svg"), "w") as f:
    f.write(trash_full)

# 3. Application Icons
terminal_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48">
  <rect x="6" y="8" width="36" height="32" rx="4" fill="#070b14" stroke="#00e5ff" stroke-width="1.8"/>
  <path d="M 14,18 L 21,24 L 14,30" fill="none" stroke="#00e5ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="24" y1="30" x2="32" y2="30" stroke="#f0f6fc" stroke-width="2" stroke-linecap="round"/>
</svg>"""

settings_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48">
  <circle cx="24" cy="24" r="8" fill="#0d1829" stroke="#00e5ff" stroke-width="2"/>
  <circle cx="24" cy="24" r="3" fill="#00e5ff"/>
  <path d="M 24,6 L 24,10 M 24,38 L 24,42 M 6,24 L 10,24 M 38,24 L 42,24 M 11.3,11.3 L 14.1,14.1 M 33.9,33.9 L 36.7,36.7 M 11.3,36.7 L 14.1,33.9 M 33.9,14.1 L 36.7,11.3" stroke="#f0f6fc" stroke-width="2.5" stroke-linecap="round"/>
</svg>"""

apps = {
    "utilities-terminal.svg": terminal_svg,
    "kitty.svg": terminal_svg,
    "system-file-manager.svg": make_folder_svg('<path d="M 21,24 L 27,24 M 24,21 L 24,27" stroke="#00e5ff" stroke-width="1.5" stroke-linecap="round"/>'),
    "nemo.svg": make_folder_svg('<path d="M 21,24 L 27,24 M 24,21 L 24,27" stroke="#00e5ff" stroke-width="1.5" stroke-linecap="round"/>'),
    "preferences-system.svg": settings_svg
}

for fname, content in apps.items():
    with open(os.path.join(THEME_DIR, "scalable/apps", fname), "w") as f:
        f.write(content)
    with open(os.path.join(THEME_DIR, "48x48/apps", fname), "w") as f:
        f.write(content)

# 4. Status & Action Icons
audio_high = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <polygon points="4 9 8 9 13 4 13 20 8 15 4 15" fill="#0d1829" stroke="#f0f6fc" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M 16.5,7.5 C 18,9 18,15 16.5,16.5" fill="none" stroke="#00e5ff" stroke-width="1.6" stroke-linecap="round"/>
  <path d="M 19,5 C 21.5,7.5 21.5,16.5 19,19" fill="none" stroke="#00e5ff" stroke-width="1.6" stroke-linecap="round"/>
</svg>"""

battery_full = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <rect x="2" y="6" width="18" height="12" rx="2" fill="#0d1829" stroke="#f0f6fc" stroke-width="1.5"/>
  <rect x="5" y="9" width="12" height="6" rx="1" fill="#00ff88"/>
  <path d="M 21,10 L 21,14" stroke="#f0f6fc" stroke-width="2" stroke-linecap="round"/>
</svg>"""

wifi_exc = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <circle cx="12" cy="18" r="1.5" fill="#00e5ff"/>
  <path d="M 8.5,14.5 C 10.5,12.8 13.5,12.8 15.5,14.5" fill="none" stroke="#00e5ff" stroke-width="1.6" stroke-linecap="round"/>
  <path d="M 5,11 C 9,7.5 15,7.5 19,11" fill="none" stroke="#00e5ff" stroke-width="1.6" stroke-linecap="round"/>
</svg>"""

search_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
  <circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="#f0f6fc" stroke-width="1.8"/>
  <line x1="15.5" y1="15.5" x2="20" y2="20" stroke="#00e5ff" stroke-width="2" stroke-linecap="round"/>
</svg>"""

status_map = {
    "scalable/status/audio-volume-high.svg": audio_high,
    "scalable/status/battery-full.svg": battery_full,
    "scalable/status/network-wireless-signal-excellent.svg": wifi_exc,
    "scalable/actions/system-search.svg": search_svg,
    "scalable/actions/edit-find.svg": search_svg
}

for rel_path, content in status_map.items():
    with open(os.path.join(THEME_DIR, rel_path), "w") as f:
        f.write(content)

print("[JARVIS ICON ENGINE]: Successfully generated Jarvis-White icon theme.")
