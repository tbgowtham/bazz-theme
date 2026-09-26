# Dracula-Slim: Cyberpunk Cockpit Cinnamon Edition 🌌🎮

> A complete, professional dark cyberpunk desktop theme suite built natively for **Linux Cinnamon** (Linux Mint, Debian, Ubuntu Cinnamon, and Arch Linux), faithfully recreated from the reference setup featuring the **Dracula-slim** GTK theme, **Dessert-white** minimalist icons, and the iconic futuristic cyberpunk mecha cockpit aesthetic.

---

## 📸 Reference Setup Replicated 1:1

This theme suite faithfully reproduces the aesthetic from the reference screenshot:
- **Base Style**: `Dracula-slim [GTK2/3/4]` — sleek dark frosted acrylic glass (`#1E1F29` / `#282A36`).
- **Icons**: `Dessert-white [GTK2/3]` — clean, minimalist frosted white line-art and glyphs.
- **Window Decorations**: Translucent dark headers with right-aligned circular traffic light controls:
  - 🟡 **Minimize**: Dracula Yellow (`#F1FA8C`)
  - 🟢 **Maximize**: Dracula Green (`#50FA7B`)
  - 🔴 **Close**: Dracula Red (`#FF5555`)
- **Shell / Panel**: Minimalist translucent slim top bar (`rgba(30, 31, 41, 0.90)`) with glowing cyan/pink status indicators.
- **Wallpaper Artwork**: The cyberpunk anime pilot with short pink hair and glowing headphones inside a high-tech mecha cockpit with neon cyan/magenta holographic circular HUD displays and a panoramic city skyline at night.

---

## 🎨 Color System (Dracula Cyberpunk Spec)

| Element | Hex / RGBA | Role |
| :--- | :--- | :--- |
| **Window Background** | `#1E1F29` / `rgba(30, 31, 41, 0.92)` | Window base, translucent glass, terminal background |
| **Cards & Surfaces** | `#282A36` | Sidebar, menu boxes, content views, headerbars |
| **Hover & Focus Surfaces** | `#343746` / `#44475A` | Hover states, active buttons, selection rows |
| **Primary Accent (Cyan)** | `#8BE9FD` | Focus rings, text highlights, active links, HUD radar |
| **Secondary Accent (Pink)** | `#FF79C6` | Notification badges, hair highlights, special indicators |
| **Selection Accent (Purple)** | `#BD93F9` | Active buttons, category selections, slider bars |
| **Traffic Lights (Close)** | `#FF5555` | Window close circular button |
| **Traffic Lights (Min)** | `#F1FA8C` | Window minimize circular button |
| **Traffic Lights (Max)** | `#50FA7B` | Window maximize circular button |
| **Primary Text** | `#F8F8F2` | Crisp high-contrast white text |
| **Comment / Muted Text** | `#6272A4` | Subtitles, pathbars, inactive status text |
| **Borders & Dividers** | `#44475A` / `rgba(255, 255, 255, 0.08)` | 1px subtle clean dividers |

---

## 📁 Repository Structure

```text
theme/
├── Dracula-Slim/                     # Primary theme folder (Reference GTK/Cinnamon theme)
│   ├── cinnamon/                    # Cinnamon Desktop Shell (Panel, Menus, Applets)
│   ├── gtk-2.0/                     # GTK 2.0 configuration (gtkrc)
│   ├── gtk-3.0/                     # GTK 3.0 CSS & traffic light vector assets
│   ├── gtk-4.0/                     # GTK 4.0 CSS & traffic light vector assets
│   ├── metacity-1/                  # Window manager decorations (metacity-theme-3.xml)
│   └── index.theme                  # Theme descriptor
├── Ubuntu-Cinnamon-White/           # Updated matching theme alias for compatibility
├── icons/
│   ├── Dessert-white/               # Minimalist white icon theme matching reference
│   └── Ubuntu-Cinnamon-Orange-Icons # Legacy icon pack
├── wallpapers/
│   ├── dracula-cyberpunk-cockpit.png        # Master 1080p Cockpit Wallpaper
│   ├── dracula-cyberpunk-cockpit-4k.png     # Master 4K Ultra-HD Cockpit Wallpaper
│   ├── dracula-cyberpunk-cockpit-1366x768.png # Laptop resolution
│   ├── dracula-cockpit-replica.png          # Exact 1:1 Instagram post replica
│   ├── dracula-avatar-hd.png                # Avatar crop for kitty/fastfetch
│   └── dracula-avatar-replica.png           # 1:1 avatar crop from reference
├── grub/
│   └── ubuntu-cinnamon/             # Matching GRUB bootloader theme
├── login-lockscreen/
│   └── slick-greeter.conf           # LightDM Slick-Greeter login configuration
├── tools/                           # Asset generation utilities
├── reference_desktop.jpg            # Original Instagram reference screenshot
└── apply.sh                         # Self-contained installer script for target machines
```

---

## 🛠️ Usage & Installation

*(Note: Theme files are self-contained in this directory and are not automatically applied to the host development environment.)*

When you wish to apply the theme to a target Linux machine running Cinnamon:

```bash
cd /path/to/theme
./apply.sh
```

### Script Flags:
- **Default (Right-aligned traffic lights `:minimize,maximize,close`)**:
  ```bash
  ./apply.sh
  ```
- **macOS Left-aligned traffic lights (`close,minimize,maximize:`)**:
  ```bash
  ./apply.sh --macos-layout
  ```
- **Full System Installation (Desktop + GRUB + Login screen)**:
  ```bash
  ./apply.sh --all
  ```
- **Restore Default Linux Mint Settings (`Mint-Y`)**:
  ```bash
  ./apply.sh --restore
  ```

---

## 💻 Terminal / Fastfetch Setup (Kitty & Neofetch)

To replicate the exact terminal presentation seen in the reference screenshot:
1. Use `kitty` or your preferred terminal with Dracula color palette.
2. Set terminal background opacity to `0.85` (`background_opacity 0.85`).
3. For fastfetch/neofetch, use the provided avatar:
   ```bash
   fastfetch --logo ~/path/to/theme/wallpapers/dracula-avatar-hd.png --logo-type kitty
   ```
