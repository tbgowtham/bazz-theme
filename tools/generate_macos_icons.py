#!/usr/bin/env python3
"""
==============================================================================
macOS-Cupertino // LUXURY SQUIRCLE ICON THEME GENERATOR
==============================================================================
Generates an authentic macOS (Sonoma / Sequoia) & Catppuccin squircle icon
theme with smooth continuous curvature, elegant gradients, realistic depth,
and macOS-inspired system glyphs.
==============================================================================
"""

import os
import shutil

THEME_DIR = "/home/MR_Gray/muteX/theme/icons/macOS-Cupertino"
os.makedirs(os.path.join(THEME_DIR, "scalable/places"), exist_ok=True)
os.makedirs(os.path.join(THEME_DIR, "scalable/apps"), exist_ok=True)
os.makedirs(os.path.join(THEME_DIR, "scalable/status"), exist_ok=True)
os.makedirs(os.path.join(THEME_DIR, "scalable/actions"), exist_ok=True)
os.makedirs(os.path.join(THEME_DIR, "scalable/categories"), exist_ok=True)

# 1. index.theme
index_theme = """[Icon Theme]
Name=macOS-Cupertino
Comment=Authentic macOS Sonoma & Sequoia Luxury Squircle Icon Theme with Catppuccin Accents
Inherits=breeze-dark,Adwaita,hicolor
Directories=scalable/places,scalable/apps,scalable/status,scalable/actions,scalable/categories

[scalable/places]
Size=64
Type=Scalable
MinSize=16
MaxSize=512
Context=Places

[scalable/apps]
Size=64
Type=Scalable
MinSize=16
MaxSize=512
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

[scalable/categories]
Size=32
Type=Scalable
MinSize=16
MaxSize=64
Context=Categories
"""

with open(os.path.join(THEME_DIR, "index.theme"), "w") as f:
    f.write(index_theme)

# 2. Authentic macOS Folder SVG Generator
def make_macos_folder(badge_svg=""):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <linearGradient id="folderBack" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#4aa5ff"/>
      <stop offset="100%" stop-color="#1976d2"/>
    </linearGradient>
    <linearGradient id="folderFront" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#64b5f6"/>
      <stop offset="40%" stop-color="#42a5f5"/>
      <stop offset="100%" stop-color="#1e88e5"/>
    </linearGradient>
    <linearGradient id="tabGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#55adff"/>
      <stop offset="100%" stop-color="#2a82e4"/>
    </linearGradient>
    <filter id="softShadow" x="-10%" y="-10%" width="120%" height="130%">
      <feDropShadow dx="0" dy="3" stdDeviation="2.5" flood-color="#001830" flood-opacity="0.35"/>
    </filter>
    <filter id="innerDepth" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="1" stdDeviation="1" flood-color="#0d47a1" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Back Tab & Folder Body -->
  <path d="M 8,17 C 8,14.5 10,12.5 12.5,12.5 L 24,12.5 C 26.5,12.5 28.5,14 30.5,16.5 L 33,19.5 L 51.5,19.5 C 54,19.5 56,21.5 56,24 L 56,48 C 56,51 53.5,53.5 50.5,53.5 L 13.5,53.5 C 10.5,53.5 8,51 8,48 Z" fill="url(#folderBack)"/>

  <!-- Interior Sheet Outline -->
  <rect x="12" y="20" width="40" height="20" rx="3" fill="#ffffff" opacity="0.85"/>

  <!-- Front Flap with Rounded Curves and Drop Shadow -->
  <path d="M 6,24.5 C 6,22 8,20 10.5,20 L 53.5,20 C 56,20 58,22 58,24.5 L 58,49 C 58,52 55.5,54.5 52.5,54.5 L 11.5,54.5 C 8.5,54.5 6,52 6,49 Z" fill="url(#folderFront)" filter="url(#softShadow)"/>

  <!-- Top Lip Highlight -->
  <path d="M 8.5,21 L 55.5,21" stroke="#a4d4ff" stroke-width="1.2" stroke-linecap="round" opacity="0.75"/>

  <!-- Embossed Badge / Glyph -->
  <g opacity="0.9" filter="url(#innerDepth)">
    {badge_svg}
  </g>
</svg>"""

places = {
    "folder.svg": "",
    "inode-directory.svg": "",
    "user-home.svg": '<path d="M 32,27 L 22,35 L 25,35 L 25,45 L 30,45 L 30,39 L 34,39 L 34,45 L 39,45 L 39,35 L 42,35 Z" fill="#ffffff"/>',
    "user-desktop.svg": '<rect x="22" y="28" width="20" height="13" rx="2" fill="none" stroke="#ffffff" stroke-width="2"/><line x1="28" y1="44" x2="36" y2="44" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/><line x1="32" y1="41" x2="32" y2="44" stroke="#ffffff" stroke-width="2"/>',
    "folder-documents.svg": '<path d="M 25,27 L 35,27 L 39,31 L 39,45 L 25,45 Z" fill="#ffffff"/><path d="M 35,27 L 35,31 L 39,31 Z" fill="#bbdefb"/><line x1="28" y1="34" x2="36" y2="34" stroke="#1976d2" stroke-width="1.5" stroke-linecap="round"/><line x1="28" y1="38" x2="36" y2="38" stroke="#1976d2" stroke-width="1.5" stroke-linecap="round"/><line x1="28" y1="41" x2="33" y2="41" stroke="#1976d2" stroke-width="1.5" stroke-linecap="round"/>',
    "folder-download.svg": '<circle cx="32" cy="37" r="9" fill="#1565c0" opacity="0.3"/><path d="M 32,29 L 32,41 M 27,36 L 32,41 L 37,36" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>',
    "folder-music.svg": '<circle cx="27" cy="42" r="3.5" fill="#ffffff"/><circle cx="37" cy="39" r="3.5" fill="#ffffff"/><path d="M 30.5,42 L 30.5,30 L 40.5,27 L 40.5,39" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round"/>',
    "folder-pictures.svg": '<rect x="23" y="29" width="18" height="14" rx="2" fill="none" stroke="#ffffff" stroke-width="2"/><circle cx="28" cy="34" r="2" fill="#ffffff"/><path d="M 24,41 L 30,35 L 34,39 L 37,36 L 41,40" fill="none" stroke="#ffffff" stroke-width="1.8" stroke-linejoin="round"/>',
    "folder-videos.svg": '<rect x="22" y="29" width="20" height="14" rx="2" fill="none" stroke="#ffffff" stroke-width="2"/><polygon points="30,32 36,36 30,40" fill="#ffffff"/>',
    "folder-remote.svg": '<circle cx="32" cy="37" r="7" fill="none" stroke="#ffffff" stroke-width="2"/><ellipse cx="32" cy="37" rx="3.5" ry="7" fill="none" stroke="#ffffff" stroke-width="1.5"/><line x1="25" y1="37" x2="39" y2="37" stroke="#ffffff" stroke-width="1.5"/>',
    "user-trash.svg": '<path d="M 24,28 L 40,28 M 27,28 L 29,44 C 29,45 30,46 31,46 L 33,46 C 34,46 35,45 35,44 L 37,28 M 29,25 L 35,25" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
    "user-trash-full.svg": '<path d="M 24,28 L 40,28 M 27,28 L 29,44 C 29,45 30,46 31,46 L 33,46 C 34,46 35,45 35,44 L 37,28 M 29,25 L 35,25" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/><path d="M 28,26 L 31,23 L 34,26" fill="#bbdefb"/>'
}

for fname, badge in places.items():
    svg_code = make_macos_folder(badge)
    with open(os.path.join(THEME_DIR, "scalable/places", fname), "w") as f:
        f.write(svg_code)

# 3. macOS App Squircles (Finder, Terminal, Safari, Settings, Calculator, Activity Monitor, Music, TextEdit, etc.)

APPS = {
    # macOS Finder
    "system-file-manager.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <linearGradient id="finderBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#e6e8eb"/>
    </linearGradient>
    <linearGradient id="finderBlue" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#389bf2"/>
      <stop offset="100%" stop-color="#0066cc"/>
    </linearGradient>
    <filter id="appShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="3" stdDeviation="2.5" flood-color="#000000" flood-opacity="0.3"/>
    </filter>
  </defs>
  <rect x="5" y="5" width="54" height="54" rx="14" fill="url(#finderBg)" filter="url(#appShadow)"/>
  <!-- Two tone Finder face -->
  <path d="M 5,19 C 5,11.2 11.2,5 19,5 L 32,5 L 32,59 L 19,59 C 11.2,59 5,52.8 5,45 Z" fill="url(#finderBlue)"/>
  <!-- Smile line -->
  <path d="M 20,41 C 26,49 38,49 44,41" fill="none" stroke="#222224" stroke-width="3" stroke-linecap="round"/>
  <!-- Eyes -->
  <circle cx="21" cy="27" r="3" fill="#222224"/>
  <circle cx="43" cy="27" r="3" fill="#222224"/>
  <!-- Nose curve -->
  <path d="M 32,23 L 34,33 L 30,34" fill="none" stroke="#222224" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>""",

    # macOS Terminal (Sleek dark aluminum squircle with prompt and status dots)
    "utilities-terminal.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <linearGradient id="termBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#2d3038"/>
      <stop offset="100%" stop-color="#181a1f"/>
    </linearGradient>
    <filter id="appShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="3" stdDeviation="2.5" flood-color="#000000" flood-opacity="0.35"/>
    </filter>
  </defs>
  <rect x="5" y="5" width="54" height="54" rx="14" fill="url(#termBg)" filter="url(#appShadow)"/>
  <!-- Top bar subtle highlight -->
  <path d="M 5,16 L 59,16" stroke="#3e434f" stroke-width="1"/>
  <!-- Traffic dots on terminal window header -->
  <circle cx="12" cy="11" r="2" fill="#ff5f56"/>
  <circle cx="18" cy="11" r="2" fill="#ffbd2e"/>
  <circle cx="24" cy="11" r="2" fill="#27c93f"/>
  <!-- Terminal Prompt >_ -->
  <path d="M 14,26 L 24,34 L 14,42" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="28" y1="42" x2="42" y2="42" stroke="#4ade80" stroke-width="3" stroke-linecap="round"/>
</svg>""",

    # macOS System Preferences / Settings (Refined brushed metallic gear)
    "preferences-system.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <linearGradient id="gearBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#8e8e93"/>
      <stop offset="100%" stop-color="#636366"/>
    </linearGradient>
    <linearGradient id="metal" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="50%" stop-color="#d1d1d6"/>
      <stop offset="100%" stop-color="#8e8e93"/>
    </linearGradient>
    <filter id="appShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="3" stdDeviation="2.5" flood-color="#000000" flood-opacity="0.3"/>
    </filter>
  </defs>
  <rect x="5" y="5" width="54" height="54" rx="14" fill="url(#gearBg)" filter="url(#appShadow)"/>
  <!-- Precision Gear Mechanism -->
  <circle cx="32" cy="32" r="18" fill="url(#metal)"/>
  <g fill="url(#metal)">
    <rect x="30" y="10" width="4" height="6" rx="1"/>
    <rect x="30" y="48" width="4" height="6" rx="1"/>
    <rect x="10" y="30" width="6" height="4" rx="1"/>
    <rect x="48" y="30" width="6" height="4" rx="1"/>
    <rect x="16" y="16" width="5" height="5" rx="1" transform="rotate(45 18.5 18.5)"/>
    <rect x="43" y="43" width="5" height="5" rx="1" transform="rotate(45 45.5 45.5)"/>
    <rect x="43" y="16" width="5" height="5" rx="1" transform="rotate(-45 45.5 18.5)"/>
    <rect x="16" y="43" width="5" height="5" rx="1" transform="rotate(-45 18.5 45.5)"/>
  </g>
  <circle cx="32" cy="32" r="7" fill="#48484a"/>
</svg>""",

    # macOS Safari / Web Browser (Iconic Blue Compass)
    "web-browser.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <linearGradient id="safariBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#f2f2f7"/>
    </linearGradient>
    <linearGradient id="dialBlue" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#2997ff"/>
      <stop offset="100%" stop-color="#0062cc"/>
    </linearGradient>
    <filter id="appShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="3" stdDeviation="2.5" flood-color="#000000" flood-opacity="0.3"/>
    </filter>
  </defs>
  <rect x="5" y="5" width="54" height="54" rx="14" fill="url(#safariBg)" filter="url(#appShadow)"/>
  <!-- Dial circle -->
  <circle cx="32" cy="32" r="22" fill="url(#dialBlue)"/>
  <!-- Tick marks -->
  <circle cx="32" cy="32" r="20" fill="none" stroke="#ffffff" stroke-width="1" stroke-dasharray="2,5" opacity="0.6"/>
  <!-- Compass Needle -->
  <polygon points="32,14 36,32 32,30 28,32" fill="#ff3b30"/>
  <polygon points="32,50 36,32 32,34 28,32" fill="#ffffff"/>
  <circle cx="32" cy="32" r="2.5" fill="#ffffff"/>
</svg>""",

    # macOS Music (Apple Music Coral Gradient with White Note)
    "multimedia-audio-player.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <linearGradient id="musicBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fa233b"/>
      <stop offset="100%" stop-color="#fb5c74"/>
    </linearGradient>
    <filter id="appShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="3" stdDeviation="2.5" flood-color="#000000" flood-opacity="0.3"/>
    </filter>
  </defs>
  <rect x="5" y="5" width="54" height="54" rx="14" fill="url(#musicBg)" filter="url(#appShadow)"/>
  <!-- White Eighth Note -->
  <circle cx="24" cy="42" r="5" fill="#ffffff"/>
  <circle cx="40" cy="37" r="5" fill="#ffffff"/>
  <path d="M 28,42 L 28,21 L 44,17 L 44,37" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
  <polygon points="28,21 44,17 44,22 28,26" fill="#ffffff"/>
</svg>""",

    # macOS TextEdit / Notes (Warm amber notepad with pen)
    "text-editor.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <linearGradient id="noteBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffd60a"/>
      <stop offset="100%" stop-color="#ff9f0a"/>
    </linearGradient>
    <filter id="appShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="3" stdDeviation="2.5" flood-color="#000000" flood-opacity="0.3"/>
    </filter>
  </defs>
  <rect x="5" y="5" width="54" height="54" rx="14" fill="url(#noteBg)" filter="url(#appShadow)"/>
  <!-- Paper lines -->
  <line x1="16" y1="20" x2="48" y2="20" stroke="#b25e00" stroke-width="2" stroke-linecap="round" opacity="0.4"/>
  <line x1="16" y1="28" x2="48" y2="28" stroke="#b25e00" stroke-width="2" stroke-linecap="round" opacity="0.4"/>
  <line x1="16" y1="36" x2="48" y2="36" stroke="#b25e00" stroke-width="2" stroke-linecap="round" opacity="0.4"/>
  <line x1="16" y1="44" x2="34" y2="44" stroke="#b25e00" stroke-width="2" stroke-linecap="round" opacity="0.4"/>
  <!-- Yellow ballpoint pen -->
  <polygon points="38,44 48,22 52,24 42,46 37,47" fill="#ffffff"/>
  <polygon points="37,47 40,45 38,44" fill="#3a3a3c"/>
</svg>""",

    # macOS Activity Monitor (Dark squircle with glowing neon green EKG pulse)
    "utilities-system-monitor.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <linearGradient id="actBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#2c2c2e"/>
      <stop offset="100%" stop-color="#1c1c1e"/>
    </linearGradient>
    <filter id="appShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="3" stdDeviation="2.5" flood-color="#000000" flood-opacity="0.3"/>
    </filter>
  </defs>
  <rect x="5" y="5" width="54" height="54" rx="14" fill="url(#actBg)" filter="url(#appShadow)"/>
  <!-- Grid lines -->
  <line x1="10" y1="32" x2="54" y2="32" stroke="#3a3a3c" stroke-width="1"/>
  <line x1="32" y1="10" x2="32" y2="54" stroke="#3a3a3c" stroke-width="1"/>
  <!-- Heartbeat Pulse Line -->
  <path d="M 8,32 L 20,32 L 24,18 L 30,46 L 36,25 L 40,36 L 44,32 L 56,32" fill="none" stroke="#30d158" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
</svg>""",

    # macOS Calculator (Dark gray grid with bright orange action buttons)
    "accessories-calculator.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <linearGradient id="calcBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#3a3a3c"/>
      <stop offset="100%" stop-color="#242426"/>
    </linearGradient>
    <filter id="appShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="3" stdDeviation="2.5" flood-color="#000000" flood-opacity="0.3"/>
    </filter>
  </defs>
  <rect x="5" y="5" width="54" height="54" rx="14" fill="url(#calcBg)" filter="url(#appShadow)"/>
  <!-- Screen Area -->
  <rect x="12" y="12" width="40" height="10" rx="3" fill="#1c1c1e"/>
  <!-- Buttons -->
  <circle cx="18" cy="30" r="4" fill="#636366"/>
  <circle cx="28" cy="30" r="4" fill="#636366"/>
  <circle cx="37" cy="30" r="4" fill="#636366"/>
  <circle cx="46" cy="30" r="4" fill="#ff9f0a"/>

  <circle cx="18" cy="40" r="4" fill="#505054"/>
  <circle cx="28" cy="40" r="4" fill="#505054"/>
  <circle cx="37" cy="40" r="4" fill="#505054"/>
  <circle cx="46" cy="40" r="4" fill="#ff9f0a"/>

  <rect x="14" y="47" width="18" height="8" rx="4" fill="#505054"/>
  <circle cx="37" cy="51" r="4" fill="#505054"/>
  <circle cx="46" cy="51" r="4" fill="#ff9f0a"/>
</svg>""",

    # macOS App Store (Cobalt blue squircle with white drafting tools 'A')
    "system-software-install.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <linearGradient id="storeBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#007aff"/>
      <stop offset="100%" stop-color="#0051ba"/>
    </linearGradient>
    <filter id="appShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="3" stdDeviation="2.5" flood-color="#000000" flood-opacity="0.3"/>
    </filter>
  </defs>
  <rect x="5" y="5" width="54" height="54" rx="14" fill="url(#storeBg)" filter="url(#appShadow)"/>
  <!-- Stylized App Store 'A' -->
  <line x1="20" y1="48" x2="32" y2="16" stroke="#ffffff" stroke-width="4.5" stroke-linecap="round"/>
  <line x1="44" y1="48" x2="32" y2="16" stroke="#ffffff" stroke-width="4.5" stroke-linecap="round"/>
  <line x1="18" y1="38" x2="46" y2="38" stroke="#ffffff" stroke-width="4.5" stroke-linecap="round"/>
</svg>""",

    # macOS Mail (Sky blue squircle with envelope)
    "internet-mail.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <linearGradient id="mailBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#38a9f8"/>
      <stop offset="100%" stop-color="#0870d8"/>
    </linearGradient>
    <filter id="appShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="3" stdDeviation="2.5" flood-color="#000000" flood-opacity="0.3"/>
    </filter>
  </defs>
  <rect x="5" y="5" width="54" height="54" rx="14" fill="url(#mailBg)" filter="url(#appShadow)"/>
  <!-- White Envelope -->
  <rect x="14" y="20" width="36" height="24" rx="3" fill="#ffffff"/>
  <path d="M 14,21 L 32,34 L 50,21" fill="none" stroke="#0870d8" stroke-width="2.5" stroke-linejoin="round"/>
</svg>""",

    # macOS Photos (Multicolor flower petals on crisp white)
    "camera-photo.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <linearGradient id="photoBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#f2f2f7"/>
    </linearGradient>
    <filter id="appShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="3" stdDeviation="2.5" flood-color="#000000" flood-opacity="0.3"/>
    </filter>
  </defs>
  <rect x="5" y="5" width="54" height="54" rx="14" fill="url(#photoBg)" filter="url(#appShadow)"/>
  <!-- Photos Petals -->
  <ellipse cx="32" cy="20" rx="4.5" ry="9" fill="#ff2d55"/>
  <ellipse cx="42" cy="24" rx="4.5" ry="9" fill="#ff9500" transform="rotate(45 42 24)"/>
  <ellipse cx="44" cy="34" rx="4.5" ry="9" fill="#ffcc00" transform="rotate(90 44 34)"/>
  <ellipse cx="40" cy="44" rx="4.5" ry="9" fill="#34c759" transform="rotate(135 40 44)"/>
  <ellipse cx="32" cy="46" rx="4.5" ry="9" fill="#007aff"/>
  <ellipse cx="22" cy="42" rx="4.5" ry="9" fill="#5856d6" transform="rotate(225 22 42)"/>
  <ellipse cx="20" cy="32" rx="4.5" ry="9" fill="#af52de" transform="rotate(270 20 32)"/>
  <ellipse cx="24" cy="22" rx="4.5" ry="9" fill="#ff2d55" transform="rotate(315 24 22)"/>
</svg>"""
}

# Write app icons
for fname, content in APPS.items():
    with open(os.path.join(THEME_DIR, "scalable/apps", fname), "w") as f:
        f.write(content)

# Common App Aliases & Symlinks
ALIASES = {
    "scalable/apps": {
        "org.kde.dolphin.svg": "system-file-manager.svg",
        "nemo.svg": "system-file-manager.svg",
        "nautilus.svg": "system-file-manager.svg",
        "finder.svg": "system-file-manager.svg",
        "org.kde.konsole.svg": "utilities-terminal.svg",
        "terminal.svg": "utilities-terminal.svg",
        "gnome-terminal.svg": "utilities-terminal.svg",
        "xterm.svg": "utilities-terminal.svg",
        "systemsettings.svg": "preferences-system.svg",
        "org.kde.systemsettings.svg": "preferences-system.svg",
        "gnome-control-center.svg": "preferences-system.svg",
        "firefox.svg": "web-browser.svg",
        "google-chrome.svg": "web-browser.svg",
        "chromium.svg": "web-browser.svg",
        "safari.svg": "web-browser.svg",
        "spotify.svg": "multimedia-audio-player.svg",
        "music.svg": "multimedia-audio-player.svg",
        "org.kde.kwrite.svg": "text-editor.svg",
        "gedit.svg": "text-editor.svg",
        "kate.svg": "text-editor.svg",
        "accessories-text-editor.svg": "text-editor.svg",
        "org.kde.kcalc.svg": "accessories-calculator.svg",
        "gnome-calculator.svg": "accessories-calculator.svg",
        "org.kde.plasma-systemmonitor.svg": "utilities-system-monitor.svg",
        "gnome-system-monitor.svg": "utilities-system-monitor.svg",
        "org.kde.discover.svg": "system-software-install.svg",
        "gnome-software.svg": "system-software-install.svg",
        "mail.svg": "internet-mail.svg"
    }
}

for folder, links in ALIASES.items():
    dest_dir = os.path.join(THEME_DIR, folder)
    for alias, target in links.items():
        src_path = os.path.join(dest_dir, target)
        alias_path = os.path.join(dest_dir, alias)
        if os.path.exists(src_path):
            shutil.copyfile(src_path, alias_path)

# Categories (Spacious, clean icons for the Action Menu categories)
CATEGORIES = {
    "applications-all.svg": '<circle cx="16" cy="16" r="3" fill="#89b4fa"/><circle cx="26" cy="16" r="3" fill="#89b4fa"/><circle cx="16" cy="26" r="3" fill="#89b4fa"/><circle cx="26" cy="26" r="3" fill="#89b4fa"/>',
    "applications-accessories.svg": '<rect x="10" y="10" width="14" height="14" rx="3" fill="none" stroke="#89b4fa" stroke-width="2"/><line x1="14" y1="17" x2="20" y2="17" stroke="#89b4fa" stroke-width="2"/>',
    "applications-development.svg": '<path d="M 12,14 L 6,20 L 12,26 M 20,14 L 26,20 L 20,26 M 17,13 L 15,27" fill="none" stroke="#89b4fa" stroke-width="2" stroke-linecap="round"/>',
    "applications-games.svg": '<rect x="6" y="12" width="20" height="12" rx="4" fill="none" stroke="#89b4fa" stroke-width="2"/><path d="M 10,18 L 14,18 M 12,16 L 12,20" stroke="#89b4fa" stroke-width="2"/><circle cx="20" cy="16" r="1" fill="#89b4fa"/><circle cx="22" cy="19" r="1" fill="#89b4fa"/>',
    "applications-graphics.svg": '<circle cx="12" cy="14" r="2" fill="#89b4fa"/><path d="M 8,24 L 14,17 L 18,21 L 21,18 L 24,24 Z" fill="none" stroke="#89b4fa" stroke-width="2"/>',
    "applications-internet.svg": '<circle cx="16" cy="16" r="10" fill="none" stroke="#89b4fa" stroke-width="2"/><ellipse cx="16" cy="16" rx="5" ry="10" fill="none" stroke="#89b4fa" stroke-width="1.5"/><line x1="6" y1="16" x2="26" y2="16" stroke="#89b4fa" stroke-width="1.5"/>',
    "applications-multimedia.svg": '<circle cx="12" cy="21" r="3" fill="#89b4fa"/><circle cx="21" cy="18" r="3" fill="#89b4fa"/><path d="M 15,21 L 15,11 L 24,9 L 24,18" fill="none" stroke="#89b4fa" stroke-width="2"/>',
    "applications-office.svg": '<path d="M 10,6 L 20,6 L 24,10 L 24,26 L 10,26 Z" fill="none" stroke="#89b4fa" stroke-width="2"/><line x1="14" y1="14" x2="20" y2="14" stroke="#89b4fa" stroke-width="2"/><line x1="14" y1="18" x2="20" y2="18" stroke="#89b4fa" stroke-width="2"/>',
    "applications-system.svg": '<circle cx="16" cy="16" r="5" fill="none" stroke="#89b4fa" stroke-width="2"/><path d="M 16,8 L 16,11 M 16,21 L 16,24 M 8,16 L 11,16 M 21,16 L 24,16" stroke="#89b4fa" stroke-width="2"/>',
    "preferences-desktop.svg": '<line x1="8" y1="12" x2="24" y2="12" stroke="#89b4fa" stroke-width="2"/><circle cx="13" cy="12" r="2.5" fill="#89b4fa"/><line x1="8" y1="20" x2="24" y2="20" stroke="#89b4fa" stroke-width="2"/><circle cx="19" cy="20" r="2.5" fill="#89b4fa"/>'
}

for cat_name, cat_svg in CATEGORIES.items():
    code = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">{cat_svg}</svg>"""
    with open(os.path.join(THEME_DIR, "scalable/categories", cat_name), "w") as f:
        f.write(code)

# Actions & Status (Search, Close, Menu, etc.)
ACTIONS = {
    "system-search.svg": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><circle cx="10" cy="10" r="6" fill="none" stroke="#89b4fa" stroke-width="2.2"/><line x1="14.5" y1="14.5" x2="20" y2="20" stroke="#89b4fa" stroke-width="2.2" stroke-linecap="round"/></svg>',
    "edit-clear.svg": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><circle cx="12" cy="12" r="9" fill="#585b70"/><line x1="9" y1="9" x2="15" y2="15" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/><line x1="15" y1="9" x2="9" y2="15" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/></svg>',
    "system-shutdown.svg": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path d="M 12,3 L 12,12 M 7.5,6.5 C 5,8.5 4,12 5.5,15.5 C 7,19 11,21 14.5,20 C 18,19 20,15.5 19.5,12 C 19,9.5 17.5,7.5 16,6.5" fill="none" stroke="#f38ba8" stroke-width="2.2" stroke-linecap="round"/></svg>',
    "system-lock-screen.svg": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><rect x="6" y="10" width="12" height="10" rx="2" fill="none" stroke="#89b4fa" stroke-width="2"/><path d="M 9,10 L 9,7 C 9,5.3 10.3,4 12,4 C 13.7,4 15,5.3 15,7 L 15,10" fill="none" stroke="#89b4fa" stroke-width="2"/><circle cx="12" cy="15" r="1.5" fill="#89b4fa"/></svg>'
}

for act_name, act_svg in ACTIONS.items():
    with open(os.path.join(THEME_DIR, "scalable/actions", act_name), "w") as f:
        f.write(act_svg)
    with open(os.path.join(THEME_DIR, "scalable/status", act_name), "w") as f:
        f.write(act_svg)

print("✓ Generated macOS-Cupertino squircle icon theme.")
