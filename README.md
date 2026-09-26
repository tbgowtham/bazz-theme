# Ubuntu-Cinnamon-White: macOS Elegance Edition 🍎🍊

> A complete, professional Ubuntu-inspired desktop theme crafted natively for the **Linux Cinnamon** desktop environment (Linux Mint, Debian, and Ubuntu Cinnamon) infused with **macOS-level visual refinement**. 

---

## ✨ macOS Elegance Features

1. **Traffic Light Window Controls**:
   - Signature **macOS Traffic Lights** (Coral Red Close `#FF5F56`, Amber Yellow Minimize `#FEBC2E`, Emerald Green Maximize `#28C840`) with clean vector glyphs on hover.
   - Default left-aligned window button layout (`close,minimize,maximize:`), with a switch for traditional right-aligned buttons.
   - Fully supported in both GTK 3/4 Headerbars and Metacity/Muffin Server-Side Decorations.

2. **macOS Top Menu Bar & Dock Aesthetic**:
   - Sleek, semi-translucent 36px Cinnamon panel with subtle bottom separator.
   - Window list items styled with macOS Dock-inspired active application indicators (pill/dot highlight) and smooth rounded hover states (`border-radius: 6px`).

3. **Spotlight / Launchpad Application Menu**:
   - Rounded floating card (`border-radius: 12px`).
   - macOS Spotlight-style search pill (`border-radius: 20px`) with subtle background.
   - Sidebar categories with smooth rounded selection pills (`border-radius: 8px`).

4. **Nemo (macOS Finder Elegance)**:
   - macOS Finder sidebar layout with categorized places and rounded hover/selection pills.
   - Clean breadcrumb path bar resembling Finder's bottom path pill.

5. **Notification Cards**:
   - macOS Notification Center style cards with 12px rounded corners and smooth pill action buttons.

6. **Floating Square OSD HUD**:
   - Volume and brightness popups styled like modern macOS Big Sur / Sonoma floating square cards (`border-radius: 16px`, smooth rounded level bar).

7. **macOS Wave Wallpaper**:
   - Sweeping, organic bezier ribbon waves with dimensional depth, combining velvety slate, deep aubergine, and glowing Ubuntu Orange ribbons with specular glass edges.
   - 0% glare, 100% desktop icon legibility.

---

## 🎨 Color System (Warm Silk & Slate)

| Element | Color Hex / Tone | Role |
| :--- | :--- | :--- |
| **Window Background** | `#EFECE8` (Warm Silk Stone) | Window body, dialogs, preferences |
| **Base Surface / Views** | `#FAF8F5` (Soft Warm Silk / Ivory) | Nemo file grid, text fields, cards |
| **Panel Surface** | `rgba(235, 232, 227, 0.96)` | Sleek macOS menu bar / panel |
| **Primary Accent** | `#E95420` (Ubuntu Orange) | Focused states, active tabs, buttons, highlights |
| **Window Controls** | Red `#FF5F56`, Yellow `#FEBC2E`, Green `#28C840` | macOS Traffic Light buttons |
| **Primary Text** | `#242220` (Deep Dark Charcoal) | High-contrast, sharp, comfortable readability |
| **Secondary Text** | `#635E58` (Muted Warm Slate) | Subtitles, captions, and muted labels |
| **Borders & Dividers**| `#D2CCC4` / `rgba(0, 0, 0, 0.12)` | Subtle 1px warm dividers |

---

## 🚀 One-Click Theme Application

```bash
cd /home/MR_Gray/muteX/theme
./apply.sh
```

### Options:
- **Default (macOS Left-Aligned Traffic Lights)**:
  ```bash
  ./apply.sh
  ```
- **Traditional Right-Aligned Window Buttons**:
  ```bash
  ./apply.sh --traditional-layout
  ```
- **Full System Setup (Desktop + GRUB + Login Screen)**:
  ```bash
  ./apply.sh --all
  ```
- **Apply GRUB Theme Only (1366×867)**:
  ```bash
  ./apply.sh --grub
  ```
- **Restore Default Linux Mint Settings (`Mint-Y`)**:
  ```bash
  ./apply.sh --restore
  ```
