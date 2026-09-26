# STARK OS // J.A.R.V.I.S. & F.R.I.D.A.Y. Linux Desktop Shell 🌌🦾

> A next-generation, high-tech Linux desktop shell engineered to replicate **Tony Stark's J.A.R.V.I.S. & F.R.I.D.A.Y.** tactical interface, fused seamlessly with **Windows 11 centered frosted acrylic glass aesthetics**. Features a fully interactive, runnable desktop environment with live Linux system telemetry, plus native **Linux Cinnamon** theme suite deployment files.

---

## ⚡ Direct Comparison: Stark OS vs. Other Linux Shells

| Feature / Capability | **STARK OS (Jarvis Edition)** | **Linux Cinnamon** | **KDE Plasma 6** | **GNOME 46** | **Windows 11** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Taskbar Layout** | **Windows 11 Centered Dock** (or Left-aligned) | Traditional Bottom Panel | Bottom Panel / Floating Dock | Top Bar + Dash to Dock | Centered Bottom Dock |
| **Start Menu Design** | **Floating Acrylic Glass (Mica blur + Glow)** | Corner Pop-up Menu | Kickoff / Application Menu | Fullscreen App Grid | Centered Floating Grid |
| **AI Assistant Core** | **Native J.A.R.V.I.S. & F.R.I.D.A.Y. Voice & Text** | None (Third-party) | None (Third-party) | None | Copilot |
| **HUD & System Visuals** | **Rotating Canvas Arc-Reactor + Telemetry** | Flat / GTK widgets | Plasma Widgets (Plasmoids) | GNOME Extensions | Desktop Widgets flyout |
| **Audio Synthesis** | **Native Web Audio Sci-Fi Clicks & Chords** | Standard system sounds | System sound theme | System sound theme | Windows default chimes |
| **Quick Settings** | **Windows 11 Action Center (6 Toggles + Sliders)** | Applet flyouts | System Tray Quick Settings | Quick Settings Pills | Action Center Grid |
| **Virtual Workspaces** | **Stark Task View (4 Quantum Desktops)** | Cinnamon Expo | Plasma Desktop Grid | GNOME Overview | Windows Task View |
| **Live Diagnostics** | **Real-time CPU/RAM/Arc Output Canvas graphs** | System Monitor app | KSysGuard / Plasma System | GNOME System Monitor | Task Manager |
| **Native Cinnamon Theme**| **Included (`cinnamon/cinnamon.css`)** | Default | N/A | N/A | N/A |

---

## 🚀 Key Features

### 1. 🪟 Windows 11 Centered Taskbar & Dock
- **Centered Application Cluster**: Start button with glowing Arc Reactor crest, Search, Task View, Widgets, and Jarvis Quick Voice button.
- **Active Window Indicators**: Subtle illuminated pills under running apps, active window glow, and minimize/restore toggle on click.
- **System Tray**:
  - Wi-Fi and Bluetooth status indicators
  - Audio volume with interactive level feedback
  - Battery charge percentage with Arc Core charging readout
  - Windows 11 compact two-line Clock & Date (`19:30` / `26/09/2026`)
  - Action Center Notification Bell with unread badge count
  - "Show Desktop" edge peek slice

### 2. 🌌 Floating Frosted Glass Start Menu
- Centered floating placement with `backdrop-filter: blur(32px) saturate(200%)`.
- Instant search bar with real-time app and Stark command filtering.
- Pinned app grid (Terminal, J.A.R.V.I.S., Diagnostics, File Explorer, Arc Player, Settings).
- Recent protocols list tracking mission logs and schematics.
- Tony Stark user profile card with Power flyout (Lock Shell, Sleep, Restart, Shutdown).

### 3. 🦾 J.A.R.V.I.S. & F.R.I.D.A.Y. Conversational Assistant
- **Voice Synthesis**: Built-in speech synthesis using the native Web Speech API.
- **Vocal Dual-Personality**:
  - **J.A.R.V.I.S.**: Refined British AI assistant mode with cyan holographic accents.
  - **F.R.I.D.A.Y.**: Tactical Irish female AI mode with hot-rod red and crimson-gold accents.
- Responds to system diagnostic queries, armor scan commands, shell comparison requests, and security lockdown.

### 4. ⚛️ Dynamic Animated Arc Reactor Canvas
- Renders directly on the desktop background with concentric rotating rings, mechanical runes, radial tick markers, pulsing core, and kinetic plasma particles.
- Dynamically responds to theme switching and system load.

### 5. 📊 Real Linux System Telemetry & Diagnostics
- Reads live metrics from the host operating system via Node.js `/api/telemetry` (CPU cores, model, utilization %, memory total/used/free, uptime, platform).
- Live rolling 30-second timeline charts drawn with HTML5 Canvas.

### 6. 💻 Mark LXXXV Interactive Terminal
- Stark command processor with built-in commands: `status`, `diagnostics`, `scan`, `cinnamon`, `plasma`, `friday`, `jarvis`, `override`, `help`.
- Live safe bash execution hook via backend API for native Linux commands (`uname -a`, `uptime`, `free -h`, `date`, `whoami`).

### 7. 🗂️ Holographic File Explorer
- Windows 11 style address bar, navigation buttons, and categorized sidebar.
- Virtual Stark quantum directory structure: Mark 85 root, Blueprints, Schematics, Telemetry Logs, and Cinnamon Theme assets.

### 8. 🎛️ Quick Settings & Action Center
- 6 quick toggles: Stark Wi-Fi, Quantum BT, Flight Mode, Defense Grid, Night Light, Overdrive.
- Interactive volume and display brightness sliders.
- Integrated full month calendar with active date highlight.

### 9. 🎨 Native Linux Cinnamon Theme Suite
- Located in `cinnamon/cinnamon.css`.
- Applies the exact Windows 11 centered frosted glass panel, floating start menu, and glowing cyan accents natively to any Linux distribution running Cinnamon (Linux Mint, Debian, Arch, Fedora).

---

## 🛠️ Quick Start & Installation

### Option 1: Launch the Interactive Web Desktop Shell
```bash
# Start the Stark OS Desktop Shell server (runs on port 3030)
./apply.sh --web
# or
node server.js
```
Open **`http://localhost:3030`** in any web browser.

### Option 2: Install Native Linux Cinnamon Theme
```bash
# Deploys theme to ~/.themes/Jarvis-Windows11-Shell and activates it
./apply.sh --install
```

### Option 3: Restore Default Cinnamon Settings
```bash
./apply.sh --restore
```

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
| :--- | :--- |
| `Win / Meta` | Toggle Windows 11 Start Menu |
| `Ctrl + Alt + T` | Open Mark LXXXV Terminal |
| `Alt + Tab` | Toggle Virtual Desktops (Task View) |
| `Win + L` | Lock Shell (Stark Security Screen) |
| `Esc` | Close active menu or flyout |

---

## 📁 Repository Structure

```text
theme/
├── package.json                         # Node.js manifest
├── server.js                            # Telemetry & static server
├── apply.sh                             # Self-contained installer script
├── README.md                            # Complete documentation
├── cinnamon/                            # Native Linux Cinnamon shell package
│   ├── cinnamon.css                     # Cinnamon theme styling
│   └── metadata.json                    # Cinnamon theme descriptor
└── public/                              # Interactive Desktop Shell
    ├── index.html                       # Master desktop viewport
    ├── assets/
    │   ├── wallpapers/                  # 4K Arc Reactor wallpaper
    │   └── icons/                       # Stark avatar and SVG assets
    ├── css/
    │   ├── shell.css                    # Base tokens, glassmorphism, HUD
    │   ├── taskbar.css                  # Windows 11 centered dock
    │   ├── start-menu.css               # Floating frosted glass Start Menu
    │   ├── windows.css                  # Draggable/resizable window manager
    │   ├── quick-settings.css           # Action Center, Calendar, Lock Screen
    │   └── apps.css                     # App window specific layouts
    └── js/
        ├── sound-fx.js                  # Web Audio API sound synthesizer
        ├── arc-reactor.js               # HTML5 Canvas Arc Reactor animation
        ├── window-manager.js            # Window dragging, snapping, resizing
        ├── taskbar.js                   # Taskbar, clock, tray controller
        ├── startmenu.js                 # Start menu search & power logic
        ├── quick-settings.js            # Quick toggles, sliders, calendar
        ├── app.js                       # Master app launcher & keybindings
        └── apps/
            ├── terminal.js              # Mark LXXXV Bash CLI
            ├── jarvis-chat.js           # J.A.R.V.I.S. & F.R.I.D.A.Y. Voice AI
            ├── system-monitor.js        # Live CPU/RAM/GPU canvas charts
            ├── file-explorer.js         # Holographic File Explorer
            ├── settings.js              # Personalization & Cinnamon settings
            └── media-player.js          # Waveform audio visualizer
```

---

*Engineered with nanotech precision by Tony Stark & MR_Gray.*
