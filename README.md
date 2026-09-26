#  macOS-Cupertino // LUXURY DESKTOP SHELL SUITE 🍏✨

> An authentic, elegant **macOS (Sonoma & Sequoia)** and **Catppuccin Macchiato** desktop shell reconstruction for Linux. Engineered with **Apple SF Pro Display & Inter typography, translucent frosted acrylic glassmorphism, authentic traffic light window controls, a spacious macOS Spotlight-inspired Action Menu, and a luxury squircle vector icon theme**.

---

## 🎨 What Makes This Reconstruction Special

Standard desktop environments often suffer from cramped menus, harsh high-contrast borders, or generic icons. This reconstruction reimagines your desktop with pure Cupertino luxury and Catppuccin's soothing ergonomics:

1. **Apple SF Pro Display & Inter Typography**:
   - Native Apple **SF Pro Display** (11pt UI, 12pt Titles) paired with **Inter** (11pt Monospace).
   - Applied system-wide across KDE Plasma 6 (`kdeglobals`), GTK 3/4 (`settings.ini`), Cinnamon (`gsettings`), and Konsole terminal.
2. **Spacious macOS Spotlight & Launchpad Action Menu**:
   - Reconstructed with generous padding (22px), smooth 20px rounded corners, and frosted glass depth.
   - **Spotlight Search Bar**: Centered 44px pill-shaped search bar with macOS accent blue focus ring (`rgba(137, 180, 250, 0.25)`).
   - **Rounded Pill Categories**: Generously padded category tabs with smooth hover highlights.
   - **Clean Application Cards**: Spacious application entries with 32px squircle icons, high-contrast labels, and subtle pill hovers.
3. **Translucent Frosted Glass (Zero Neon Blue)**:
   - Panel and Menus feature silky background blur and frosted dark slate (`rgba(30, 32, 48, 0.85)`).
   - Hairline borders (`1px solid rgba(255, 255, 255, 0.12)`) and soft ambient shadows.
   - All harsh neon cyan, dark blue sci-fi borders, and angular mecha lines have been eliminated.
4. **Authentic macOS Traffic Light Window Controls**:
   - 🔴 **Close**: Smooth red circle (`#ff5f56`) with dark hover cross glyph.
   - 🟡 **Minimize**: Warm amber circle (`#ffbd2e`) with dark hover minus glyph.
   - 🟢 **Maximize / Zoom**: Vibrant green circle (`#27c93f`) with diagonal arrow glyph.
   - Integrated into both Metacity (`metacity-theme-3.xml`) and GTK 3/4 headerbars.
5. **Luxury Squircle Icon Theme (`macOS-Cupertino`)**:
   - Complete vector SVG icon suite with authentic macOS continuous squircle curvature.
   - Sky-Blue layered folders with 3D embossed badges for Home, Desktop, Documents, Downloads, Music, Pictures, Videos, and Trash.
   - Apple-style app icons for Finder, Terminal, Safari/Web Browser, System Settings, Notes/TextEdit, Activity Monitor, Calculator, App Store, and Music.
6. **KDE Plasma 6 & Konsole Integration**:
   - Two handcrafted KDE color schemes: `macOS-Catppuccin.colors` (Macchiato warmth) and `macOS-Cupertino.colors` (Dark slate & Apple System Blue).
   - Custom Konsole profile with Apple Terminal palette and clean prompt: ` ~/path ❯`.

---

## 🚀 How to Apply the Theme

Because it is linked into your `$PATH` (`~/.local/bin/macos`), you can apply it from **any terminal** or directly in this folder:

```bash
# Apply the complete macOS-Cupertino suite across your entire system
./apply.sh
```

Or simply run:

```bash
macos
```

### What `./apply.sh` Does Automatically:
1. Verifies and activates **SF Pro Display** and **Inter** fonts.
2. Generates and installs the **macOS-Cupertino squircle icon theme** to `~/.icons/` and `~/.local/share/icons/`.
3. Assembles and installs the **macOS-Cupertino** desktop theme to `~/.themes/` and `~/.local/share/themes/`.
4. Activates the **macOS-Catppuccin** color scheme in KDE Plasma 6 via `plasma-apply-colorscheme` and `kwriteconfig6`.
5. Sets Konsole default profile to `macOS-Cupertino` with Inter typography.
6. Configures GTK 3 & GTK 4 `settings.ini` and Cinnamon `gsettings` (theme, icons, fonts, button layout).
7. Sets up the clean macOS shell prompt (` ~/path ❯`) in `~/.bashrc.d/macos-theme.sh`.

---

## 🛠️ Color Palette Reference

| Token | Hex | Role |
| :--- | :--- | :--- |
| **Base Slate** | `#1e1e2e` | Window background & main canvas |
| **Mantle / Header** | `#181825` | Titlebars, headerbars, secondary backgrounds |
| **Frosted Glass** | `rgba(30, 32, 48, 0.85)` | Panel, Spotlight menu, and floating popovers |
| **macOS Blue Accent**| `#89b4fa` / `#0a84ff` | Primary buttons, active tabs, focus rings |
| **Text Primary** | `#f5f5f7` | Crisp high-legibility UI text |
| **Text Secondary** | `#a6adc8` | Subtitles, labels, inactive tabs |
| **Traffic Red** | `#ff5f56` | Window close button |
| **Traffic Yellow** | `#ffbd2e` | Window minimize button |
| **Traffic Green** | `#27c93f` | Window maximize / zoom button |

---

## 📁 Repository Structure

```text
theme/
├── apply.sh                             # Master execution script (./apply.sh or macos)
├── index.theme                          # XDG metatheme index (macOS-Cupertino)
│
├── tools/
│   ├── apply_macos_theme.py             # Master system installer & config engine
│   ├── generate_macos_icons.py          # SVG Squircle icon generator
│   ├── macOS-Cupertino.colors           # Apple Dark Slate KDE Plasma color scheme
│   ├── macOS-Catppuccin.colors          # Catppuccin Macchiato KDE color scheme
│   ├── macOS-Catppuccin.colorscheme     # Konsole terminal color palette
│   ├── macOS.profile                    # Konsole default profile
│   └── macos-theme.sh                   # Interactive shell prompt script ( ~/path ❯)
│
├── icons/macOS-Cupertino/               # Scalable squircle icon theme
│   ├── index.theme
│   └── scalable/ (places, apps, categories, actions, status)
│
├── cinnamon/                            # Cinnamon desktop shell theme
│   ├── metadata.json
│   └── cinnamon.css                     # Frosted panel & spacious Spotlight Action Menu
│
├── gtk-3.0/ & gtk-4.0/                  # macOS frosted GTK styles with traffic lights
│   ├── gtk.css
│   └── gtk-dark.css
│
├── metacity-1/                          # Window decorations with macOS Traffic Lights
│   └── metacity-theme-3.xml
│
└── stark_shell/                         # Standalone Python/GTK dock & Spotlight launcher
    ├── panel.py                         # macOS Dock & Menubar
    ├── start_menu.py                    # Big elegant Spotlight & Applications launcher
    └── style.css                        # Frosted glass stylesheet
```
