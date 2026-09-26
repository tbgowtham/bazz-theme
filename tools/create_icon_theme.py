import os

def create_icons():
    base_dir = "icons/Ubuntu-Cinnamon-Orange-Icons"
    places_dir = os.path.join(base_dir, "scalable/places")
    status_dir = os.path.join(base_dir, "scalable/status")
    actions_dir = os.path.join(base_dir, "scalable/actions")
    apps_dir = os.path.join(base_dir, "scalable/apps")
    
    for d in [places_dir, status_dir, actions_dir, apps_dir]:
        os.makedirs(d, exist_ok=True)

    # 1. Base Folder Template
    def make_folder(glyph_svg=""):
        return f'''<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">
  <defs>
    <linearGradient id="folder-front" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FF6332"/>
      <stop offset="100%" stop-color="#E95420"/>
    </linearGradient>
  </defs>
  <!-- Back flap -->
  <path d="M 6 10 C 4.9 10 4 10.9 4 12 L 4 36 C 4 37.1 4.9 38 6 38 L 42 38 C 43.1 38 44 37.1 44 36 L 44 16 C 44 14.9 43.1 14 42 14 L 23 14 L 19 10 Z" fill="#C74010"/>
  <!-- Paper / tab layer -->
  <rect x="7" y="13" width="34" height="20" rx="2" fill="#FAFAFB" opacity="0.95"/>
  <!-- Front flap (Ubuntu Orange) -->
  <path d="M 4 17 C 4 15.9 4.9 15 6 15 L 42 15 C 43.1 15 44 15.9 44 17 L 44 37 C 44 38.1 43.1 39 42 39 L 6 39 C 4.9 39 4 38.1 4 37 Z" fill="url(#folder-front)"/>
  <!-- Top lip highlight -->
  <path d="M 6 15 L 42 15" stroke="#FFA07A" stroke-width="1" stroke-linecap="round"/>
  {glyph_svg}
</svg>'''

    # Glyphs for folders
    doc_glyph = '<path d="M 21 21 L 27 21 L 31 25 L 31 33 L 21 33 Z M 27 21 L 27 25 L 31 25" fill="none" stroke="#FFFFFF" stroke-width="1.6" stroke-linejoin="round"/>'
    dl_glyph = '<path d="M 24 21 L 24 31 M 20 27 L 24 31 L 28 27 M 18 33 L 30 33" fill="none" stroke="#FFFFFF" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
    music_glyph = '<path d="M 22 30 C 20.9 30 20 30.9 20 32 C 20 33.1 20.9 34 22 34 C 23.1 34 24 33.1 24 32 L 24 23 L 30 21 L 30 28 C 28.9 28 28 28.9 28 30 C 28 31.1 28.9 32 30 32 C 31.1 32 32 31.1 32 30 L 32 19 L 24 21 L 24 30 Z" fill="#FFFFFF"/>'
    pic_glyph = '<rect x="18" y="21" width="12" height="10" rx="1.5" fill="none" stroke="#FFFFFF" stroke-width="1.6"/><circle cx="21.5" cy="24.5" r="1.2" fill="#FFFFFF"/><path d="M 18 29 L 22 25 L 25 28 L 27 26 L 30 29" fill="none" stroke="#FFFFFF" stroke-width="1.4"/>'
    vid_glyph = '<rect x="18" y="22" width="10" height="9" rx="1" fill="none" stroke="#FFFFFF" stroke-width="1.6"/><polygon points="28,24 33,21 33,31 28,28" fill="#FFFFFF"/>'
    home_glyph = '<path d="M 19 33 L 19 26 L 29 26 L 29 33 Z M 16 26 L 24 19 L 32 26" fill="none" stroke="#FFFFFF" stroke-width="1.8" stroke-linejoin="round"/>'
    desktop_glyph = '<rect x="18" y="21" width="12" height="9" rx="1" fill="none" stroke="#FFFFFF" stroke-width="1.6"/><line x1="22" y1="32" x2="26" y2="32" stroke="#FFFFFF" stroke-width="1.6"/><line x1="24" y1="30" x2="24" y2="32" stroke="#FFFFFF" stroke-width="1.6"/>'
    trash_glyph = '<path d="M 20 22 L 28 22 M 24 20 L 24 22 M 21 24 L 22 33 L 26 33 L 27 24" fill="none" stroke="#FFFFFF" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>'

    folders = {
        "folder.svg": make_folder(""),
        "folder-documents.svg": make_folder(doc_glyph),
        "folder-download.svg": make_folder(dl_glyph),
        "folder-music.svg": make_folder(music_glyph),
        "folder-pictures.svg": make_folder(pic_glyph),
        "folder-videos.svg": make_folder(vid_glyph),
        "folder-remote.svg": make_folder(""),
        "user-home.svg": make_folder(home_glyph),
        "user-desktop.svg": make_folder(desktop_glyph),
        "user-trash.svg": make_folder(trash_glyph),
        "user-trash-full.svg": make_folder(trash_glyph),
        "inode-directory.svg": make_folder(""),
    }

    for fname, svg in folders.items():
        with open(os.path.join(places_dir, fname), "w") as f:
            f.write(svg)

    # Status Icons (Panel Indicators in Dark Charcoal #2C2C2C)
    vol_high = '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  <path d="M 5 9 L 9 9 L 14 5 L 14 19 L 9 15 L 5 15 Z" fill="#2C2C2C"/>
  <path d="M 16.5 8.5 C 17.5 9.5 18 10.7 18 12 C 18 13.3 17.5 14.5 16.5 15.5" fill="none" stroke="#2C2C2C" stroke-width="1.8" stroke-linecap="round"/>
  <path d="M 19 6 C 20.5 7.5 21.5 9.7 21.5 12 C 21.5 14.3 20.5 16.5 19 18" fill="none" stroke="#2C2C2C" stroke-width="1.8" stroke-linecap="round"/>
</svg>'''

    vol_muted = '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  <path d="M 5 9 L 9 9 L 14 5 L 14 19 L 9 15 L 5 15 Z" fill="#2C2C2C"/>
  <line x1="17" y1="10" x2="22" y2="15" stroke="#E95420" stroke-width="2" stroke-linecap="round"/>
  <line x1="22" y1="10" x2="17" y2="15" stroke="#E95420" stroke-width="2" stroke-linecap="round"/>
</svg>'''

    wifi_full = '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  <circle cx="12" cy="18" r="1.8" fill="#2C2C2C"/>
  <path d="M 8.5 14.5 C 10.5 12.8 13.5 12.8 15.5 14.5" fill="none" stroke="#2C2C2C" stroke-width="2" stroke-linecap="round"/>
  <path d="M 5.5 11.5 C 9.2 8.5 14.8 8.5 18.5 11.5" fill="none" stroke="#2C2C2C" stroke-width="2" stroke-linecap="round"/>
  <path d="M 2.5 8.5 C 8 3.5 16 3.5 21.5 8.5" fill="none" stroke="#2C2C2C" stroke-width="2" stroke-linecap="round"/>
</svg>'''

    bat_good = '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  <rect x="4" y="6" width="14" height="12" rx="2" fill="none" stroke="#2C2C2C" stroke-width="1.8"/>
  <rect x="6" y="8" width="10" height="8" rx="1" fill="#38B44A"/>
  <path d="M 19 10 C 19.6 10 20 10.5 20 11 L 20 13 C 20 13.5 19.6 14 19 14" fill="#2C2C2C"/>
</svg>'''

    bt_active = '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  <path d="M 7 7 L 16 15 L 12 19 L 12 5 L 16 9 L 7 17" fill="none" stroke="#2C2C2C" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
</svg>'''

    statuses = {
        "audio-volume-high.svg": vol_high,
        "audio-volume-medium.svg": vol_high,
        "audio-volume-low.svg": vol_high,
        "audio-volume-muted.svg": vol_muted,
        "network-wireless-signal-excellent.svg": wifi_full,
        "network-wireless-signal-good.svg": wifi_full,
        "network-wireless-signal-ok.svg": wifi_full,
        "battery-good.svg": bat_good,
        "battery-full.svg": bat_good,
        "bluetooth-active.svg": bt_active,
    }

    for fname, svg in statuses.items():
        with open(os.path.join(status_dir, fname), "w") as f:
            f.write(svg)

    # Actions & App Icons
    search_icon = '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  <circle cx="10.5" cy="10.5" r="6" fill="none" stroke="#2C2C2C" stroke-width="2"/>
  <line x1="15" y1="15" x2="20.5" y2="20.5" stroke="#2C2C2C" stroke-width="2.2" stroke-linecap="round"/>
</svg>'''

    with open(os.path.join(actions_dir, "system-search.svg"), "w") as f:
        f.write(search_icon)
    with open(os.path.join(actions_dir, "edit-find.svg"), "w") as f:
        f.write(search_icon)

    # Nemo app icon
    with open(os.path.join(apps_dir, "system-file-manager.svg"), "w") as f:
        f.write(make_folder(doc_glyph))
    with open(os.path.join(apps_dir, "nemo.svg"), "w") as f:
        f.write(make_folder(doc_glyph))

    # Index.theme
    index_theme = '''[Icon Theme]
Name=Ubuntu-Cinnamon-Orange-Icons
Comment=Clean Ubuntu-inspired modern icon theme in Ubuntu Orange and Dark Charcoal
Inherits=Yaru,Mint-Y,Adwaita,gnome,hicolor
Directories=scalable/places,scalable/status,scalable/actions,scalable/apps

[scalable/places]
Size=48
Type=Scalable
MinSize=16
MaxSize=512
Context=Places

[scalable/status]
Size=24
Type=Scalable
MinSize=16
MaxSize=128
Context=Status

[scalable/actions]
Size=24
Type=Scalable
MinSize=16
MaxSize=128
Context=Actions

[scalable/apps]
Size=48
Type=Scalable
MinSize=16
MaxSize=256
Context=Applications
'''
    with open(os.path.join(base_dir, "index.theme"), "w") as f:
        f.write(index_theme)

    print("Icon theme created successfully")

create_icons()
