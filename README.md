# Ubuntu-Cinnamon-White Theme 🍊

> A complete, professional Ubuntu-inspired desktop theme crafted natively for the **Linux Cinnamon** desktop environment (Linux Mint, Debian, and Ubuntu Cinnamon). Designed with a clean off-white foundation, dark charcoal typography, and signature **Ubuntu Orange (`#E95420`)** accents.

---

## 🎨 Design Philosophy & Color System

The theme is built around minimalism, crisp readability, and lightweight performance suitable for daily use on both modern and low-spec laptops without heavy graphical overhead or eye fatigue.

| Element | Color Hex / Style | Role |
| :--- | :--- | :--- |
| **Primary Background** | `#FFFFFF` / `#FAFAFB` | Base window, panel, and surface background |
| **Primary Accent** | `#E95420` | Ubuntu Orange accent, active indicators, highlights |
| **Primary Text** | `#2C2C2C` | High-contrast Dark Charcoal for maximum readability |
| **Secondary Text** | `#666666` | Medium Gray for subtitles, captions, and muted labels |
| **Secondary Surfaces**| `#F5F6F8` / `#F0F1F4` | Sidebars, search fields, toolbar buttons |
| **Borders & Dividers**| `#DCDFE6` / `#E2E4E8` | Subtle 1px dividers and clean widget boundaries |
| **Hover State** | `#FDF2EE` | Very soft warm orange tint for interactive elements |
| **Active / Selected** | `#E95420` | Vibrant Ubuntu Orange with crisp white text (`#FFFFFF`) |
| **Disabled State** | `#A0A0A0` | Neutral muted gray |

> **Visual Rules Strictly Followed:** No neon colors, no excessive gradients, no cyberpunk styling, no heavy blur, and no heavy drop shadows.

---

## 📦 What's Included

```
theme/
├── apply.sh                          # Automated one-step installation & apply script
├── Ubuntu-Cinnamon-White/            # Complete Desktop Theme
│   ├── cinnamon/                     # Cinnamon Desktop Shell (panel, menu, applets)
│   │   ├── cinnamon.css
│   │   ├── thumbnail.png
│   │   └── assets/                   # Checkboxes, radios, switches, close buttons
│   ├── gtk-3.0/                      # GTK 3 theme & Nemo file manager styling
│   │   ├── gtk.css
│   │   ├── gtk-dark.css
│   │   ├── thumbnail.png
│   │   └── assets/
│   ├── gtk-4.0/                      # GTK 4 & Libadwaita application styling
│   │   ├── gtk.css
│   │   └── assets/
│   ├── gtk-2.0/                      # Legacy GTK2 application styling (gtkrc)
│   ├── metacity-1/                   # Window borders & titlebars (Metacity/Muffin)
│   │   ├── metacity-theme-3.xml
│   │   └── *.svg                     # Titlebar button vectors (close, min, max)
│   └── index.theme                   # Desktop theme metadata
├── icons/
│   └── Ubuntu-Cinnamon-Orange-Icons/ # Ubuntu-Orange folder & charcoal indicator theme
│       ├── index.theme
│       └── scalable/                 # Places, status, actions, and apps
├── wallpapers/                       # Minimalist geometric wallpapers
│   ├── ubuntu-cinnamon-minimal-light.svg
│   ├── ubuntu-cinnamon-minimal-light.png       # 4K UHD (3840×2160)
│   ├── ubuntu-cinnamon-minimal-light-1080p.png # Full HD (1920×1080)
│   └── ubuntu-cinnamon-minimal-light-1366x768.png # Laptop standard
├── grub/
│   └── ubuntu-cinnamon/              # Ubuntu-inspired GRUB theme (1366×867)
│       ├── theme.txt
│       ├── background.png
│       ├── select_*.png
│       └── icons/
├── login-lockscreen/                 # Slick Greeter (LightDM) login screen config
│   └── slick-greeter.conf
└── tools/                            # Generator scripts for wallpapers, assets & icons
```

---

## 🚀 Quick Installation (`apply.sh`)

### Standard One-Click Application
To immediately install and apply the Cinnamon shell, GTK theme, window decorations, icons, and wallpaper:

```bash
./apply.sh
```

### Full System Setup (including GRUB & Login Screen)
To install the desktop theme and be guided through setting up the GRUB boot menu and Slick-Greeter login screen:

```bash
./apply.sh --all
```

### Individual Options
- **Apply GRUB Theme Only**:
  ```bash
  ./apply.sh --grub
  ```
- **Apply Slick Greeter (LightDM) Login Screen**:
  ```bash
  ./apply.sh --lightdm
  ```
- **Restore Default Linux Mint Settings (`Mint-Y`)**:
  ```bash
  ./apply.sh --restore
  ```

---

## 🛠 Manual Installation & Configuration

If you prefer configuring Cinnamon through the graphical interface:

1. **Copy Theme Files**:
   ```bash
   mkdir -p ~/.themes ~/.icons ~/.local/share/backgrounds
   cp -r Ubuntu-Cinnamon-White ~/.themes/
   cp -r icons/Ubuntu-Cinnamon-Orange-Icons ~/.icons/
   cp wallpapers/*.png ~/.local/share/backgrounds/
   ```

2. **Open Cinnamon Settings**:
   - Go to **System Settings** → **Themes**.
   - **Window borders**: Select `Ubuntu-Cinnamon-White`.
   - **Icons**: Select `Ubuntu-Cinnamon-Orange-Icons`.
   - **Controls (GTK)**: Select `Ubuntu-Cinnamon-White`.
   - **Desktop (Shell)**: Select `Ubuntu-Cinnamon-White`.

3. **Set Wallpaper**:
   - Right-click desktop → **Change Desktop Background** → Choose `ubuntu-cinnamon-minimal-light.png`.

---

## 🖥 Component Highlights

### 1. Cinnamon Desktop Shell
- **Panel**: Crisp off-white `#FAFAFB` with a subtle `1px` border separator.
- **Window List**: Underlined active window indicator in Ubuntu Orange (`#E95420`).
- **Main Menu**: Clean white container with category sidebar, search bar with orange focus ring, and soft orange hover states.
- **Calendar & Clock**: Popup calendar highlighting the current day in an orange badge.
- **Notifications**: Clean white cards with an Ubuntu Orange accent bar on the left edge.
- **Workspace Switcher & Expo**: Orange border highlight around active workspace.

### 2. Nemo File Manager
- **Sidebar**: Light neutral gray `#F6F7F9` with standard places and orange folder icons.
- **File Grid**: White background, clean charcoal text, and orange selection bounding boxes.
- **Breadcrumb Path Bar**: Subtle borders with highlighted active folder.

### 3. Window Decorations (Metacity / Muffin)
- **Titlebars**: Off-white titlebar with dark charcoal text for focused windows; muted gray for unfocused windows.
- **Window Controls**: Circular Ubuntu Orange close button (`#E95420`) with white cross; subtle neutral minimize/maximize controls.

### 4. GRUB Boot Theme
- **Resolution**: Designed specifically for `1366×867` (and scales to `1366×768` and `1920×1080`).
- **Selector**: Ubuntu Orange rounded pill indicator.
- **Typography & Elements**: Clean dark charcoal entries, subtle progress countdown bar, and official distribution icons.

---

## ⚡ Performance on Low-Spec Hardware

This theme is optimized for low CPU and GPU usage:
- No resource-heavy blur shaders or heavy translucent overlays.
- Lightweight pure CSS without unnecessary pseudo-element animations.
- Vector SVGs rendered cleanly for icons and controls without memory bloat.
- Fully compatible with Cinnamon 5.x and 6.x.
