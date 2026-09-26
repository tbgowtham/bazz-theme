import os

def create_icons():
    base_dir = "icons/Ubuntu-Cinnamon-Orange-Icons"
    places_dir = os.path.join(base_dir, "scalable/places")
    status_dir = os.path.join(base_dir, "scalable/status")
    actions_dir = os.path.join(base_dir, "scalable/actions")
    apps_dir = os.path.join(base_dir, "scalable/apps")
    
    for d in [places_dir, status_dir, actions_dir, apps_dir]:
        os.makedirs(d, exist_ok=True)

    # macOS-style Elegant Folder (Rounded geometry, soft subtle inner fold, Ubuntu Orange warmth)
    def make_macos_folder(glyph_svg=""):
        return f'''<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
  <defs>
    <linearGradient id="folder-back" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#D94818"/>
      <stop offset="100%" stop-color="#B8380E"/>
    </linearGradient>
    <linearGradient id="folder-front" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FF6B38"/>
      <stop offset="60%" stop-color="#E95420"/>
      <stop offset="100%" stop-color="#CC4010"/>
    </linearGradient>
    <linearGradient id="paper-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#EDE8E2"/>
    </linearGradient>
    <filter id="pocket-shadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#000000" flood-opacity="0.22"/>
    </filter>
  </defs>

  <!-- macOS-style Back Plate & Tab -->
  <path d="M 8 16 C 8 13.8 9.8 12 12 12 L 26 12 C 28 12 29.5 13 30.5 14.5 L 34 19 L 52 19 C 54.2 19 56 20.8 56 23 L 56 48 C 56 50.2 54.2 52 52 52 L 12 52 C 9.8 52 8 50.2 8 48 Z" 
        fill="url(#folder-back)" />

  <!-- macOS Interior Paper Sheet -->
  <rect x="13" y="18" width="38" height="24" rx="3" fill="url(#paper-grad)" opacity="0.95" />

  <!-- macOS Front Pocket / Flap (Smooth curved corners, glowing lip) -->
  <rect x="6" y="23" width="52" height="30" rx="5" fill="url(#folder-front)" filter="url(#pocket-shadow)" />

  <!-- Top Lip Specular Highlight -->
  <path d="M 11 24 L 53 24" stroke="#FFAE8C" stroke-width="1.2" stroke-linecap="round" />

  <!-- Center Embossed Glyph -->
  <g transform="translate(0, 3)">
    {glyph_svg}
  </g>
</svg>'''

    # Center Glyphs for Folders (Scaled for 64px)
    doc_glyph = '<path d="M 28 29 L 36 29 L 41 34 L 41 44 L 28 44 Z M 36 29 L 36 34 L 41 34" fill="none" stroke="#FFFFFF" stroke-width="1.8" stroke-linejoin="round"/>'
    dl_glyph = '<path d="M 32 28 L 32 40 M 27 35 L 32 40 L 37 35 M 25 43 L 39 43" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>'
    music_glyph = '<path d="M 29 39 C 27.9 39 27 39.9 27 41 C 27 42.1 27.9 43 29 43 C 30.1 43 31 42.1 31 41 L 31 30 L 38 28 L 38 37 C 36.9 37 36 37.9 36 39 C 36 40.1 36.9 41 38 41 C 39.1 41 40 40.1 40 39 L 40 26 L 31 28 L 31 39 Z" fill="#FFFFFF"/>'
    pic_glyph = '<rect x="25" y="29" width="15" height="12" rx="2" fill="none" stroke="#FFFFFF" stroke-width="1.8"/><circle cx="29" cy="33" r="1.5" fill="#FFFFFF"/><path d="M 25 39 L 30 34 L 34 38 L 36 36 L 40 40" fill="none" stroke="#FFFFFF" stroke-width="1.6"/>'
    vid_glyph = '<rect x="25" y="30" width="13" height="11" rx="2" fill="none" stroke="#FFFFFF" stroke-width="1.8"/><polygon points="38,32 44,28 44,42 38,38" fill="#FFFFFF"/>'
    home_glyph = '<path d="M 26 43 L 26 34 L 38 34 L 38 43 Z M 22 34 L 32 26 L 42 34" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linejoin="round"/>'
    desktop_glyph = '<rect x="24" y="28" width="16" height="12" rx="2" fill="none" stroke="#FFFFFF" stroke-width="1.8"/><line x1="29" y1="43" x2="35" y2="43" stroke="#FFFFFF" stroke-width="2"/><line x1="32" y1="40" x2="32" y2="43" stroke="#FFFFFF" stroke-width="2"/>'
    trash_glyph = '<path d="M 26 30 L 38 30 M 32 27 L 32 30 M 28 32 L 29 43 L 35 43 L 36 32" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'

    folders = {
        "folder.svg": make_macos_folder(""),
        "folder-documents.svg": make_macos_folder(doc_glyph),
        "folder-download.svg": make_macos_folder(dl_glyph),
        "folder-music.svg": make_macos_folder(music_glyph),
        "folder-pictures.svg": make_macos_folder(pic_glyph),
        "folder-videos.svg": make_macos_folder(vid_glyph),
        "folder-remote.svg": make_macos_folder(""),
        "user-home.svg": make_macos_folder(home_glyph),
        "user-desktop.svg": make_macos_folder(desktop_glyph),
        "user-trash.svg": make_macos_folder(trash_glyph),
        "user-trash-full.svg": make_macos_folder(trash_glyph),
        "inode-directory.svg": make_macos_folder(""),
    }

    for fname, svg in folders.items():
        with open(os.path.join(places_dir, fname), "w") as f:
            f.write(svg)

    print("macOS-style Ubuntu Orange folders created successfully")

create_icons()
