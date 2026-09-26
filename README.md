# STARK OS // J.A.R.V.I.S. & F.R.I.D.A.Y. Linux Desktop Shell 🌌🦾

> A complete, professional dark cyberpunk desktop suite engineered to replicate **Tony Stark's J.A.R.V.I.S. & F.R.I.D.A.Y.** tactical interface, fused with **Windows 11 centered frosted acrylic glass aesthetics**. Features a dynamic wallpaper engine that embeds **real-time Linux OS telemetry (CPU %, RAM %, Storage, Network, Hostname, Uptime)** directly onto the desktop wallpaper, plus complete **Shell theme, Icon theme, Window decorations, and Live background daemon**.

---

## 📸 Real Linux OS Telemetry Wallpaper HUD

The wallpaper engine inspects your real system via `psutil` and renders a live high-tech tactical HUD directly onto your desktop wallpaper:

![Stark Industries J.A.R.V.I.S. Live Telemetry Wallpaper](/home/MR_Gray/.gemini/antigravity-ide/brain/b42dcd67-d1bd-4be4-ae35-a854875eef4f/stark-live-wallpaper.png)

### Live Embedded Metrics:
- **Real CPU % & Per-Core Activity**: Overall load percentage with individual `C0`-`C7` core mini-meter gauges and clock frequency.
- **Real RAM & Storage Allocation**: Exact GB used / total, percentage bar, and NVMe `/` root filesystem capacity.
- **Real Network I/O**: Live upload & download counters (`RX` / `TX` in MB).
- **Active Process Consumption**: Top resource-demanding processes running on your OS.
- **Host & Kernel Signature**: Hostname, kernel release, architecture, battery %, and system uptime.
- **Stark Defense Grid**: Dynamic timestamp and status indicators.

---

## ⚡ Direct Comparison: Stark OS vs. Other Linux Shells

| Feature / Capability | **STARK OS (Jarvis Edition)** | **Linux Cinnamon** | **KDE Plasma 6** | **GNOME 46** | **Windows 11** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Wallpaper Telemetry** | **Real-time OS CPU/RAM on Wallpaper** | Static image | Static / slideshow | Static image | Static image |
| **Live HUD Daemon** | **`./apply.sh --live` (Continuous updates)** | None | None | None | None |
| **Taskbar Layout** | **Windows 11 Centered Dock** (or Left) | Traditional Bottom Panel | Bottom Panel / Floating Dock | Top Bar + Dash to Dock | Centered Bottom Dock |
| **Start Menu Design** | **Floating Acrylic Glass (Mica blur)** | Corner Pop-up Menu | Kickoff / Application Menu | Fullscreen App Grid | Centered Floating Grid |
| **Icon Theme** | **Jarvis-White (Frosted Minimalist SVG)** | Mint-Y / Adwaita | Breeze | Adwaita | Segoe Fluent Icons |
| **Window Decoration** | **Metacity-1 + GTK3/4 Dark Glass Controls** | Metacity Mint-Y | KWin Breeze | Libadwaita | Windows Acrylic |
| **AI Assistant Core** | **Native J.A.R.V.I.S. & F.R.I.D.A.Y. Voice & Text** | None | None | None | Copilot |
| **Virtual Workspaces** | **Stark Task View (4 Quantum Desktops)** | Cinnamon Expo | Plasma Desktop Grid | GNOME Overview | Windows Task View |

---

## 📁 Repository Structure

```text
theme/
├── apply.sh                             # Master installer & live daemon controller
├── generate_wallpaper.py                # Live OS telemetry wallpaper generator
├── live_wallpaper_daemon.py             # Background daemon for continuous wallpaper updates
├── index.theme                          # Master desktop theme descriptor
├── README.md                            # Complete documentation
│
├── cinnamon/                            # Native Linux Cinnamon Desktop Shell
│   ├── cinnamon.css                     # Windows 11 centered frosted dock & start menu
│   └── metadata.json                    # Cinnamon theme descriptor
│
├── icons/                               # Complete Icon Theme
│   └── Jarvis-White/                    # Minimalist frosted white & cyan SVG line-art
│       ├── index.theme                  # Icon theme descriptor
│       ├── scalable/                    # Scalable vector icons (places, apps, status, actions)
│       └── 48x48/                       # High-DPI fixed bitmaps/SVGs
│
├── metacity-1/                          # Window Decorations
│   └── metacity-theme-3.xml             # Sleek dark frosted acrylic window titlebars & buttons
│
├── gtk-3.0/ & gtk-4.0/                  # GTK Window & Application Styling
│   ├── gtk.css                          # Dark obsidian glass headerbars & cyan accents
│   └── gtk-dark.css                     # Dark mode overrides
│
├── stark-shell                          # Native Linux Desktop Shell executable
├── stark_shell/                         # Native Desktop Shell Engine (GTK + LayerShell)
│   ├── panel.py                         # Windows 11 centered dock with live tray
│   ├── start_menu.py                    # Floating frosted Start Menu with real app search
│   ├── quick_settings.py                # Action Center with real PipeWire/Pulse volume
│   ├── jarvis_voice.py                  # J.A.R.V.I.S. voice assistant with speech synthesis
│   ├── app_scanner.py                   # Real Linux desktop app scanner
│   └── style.css                        # Native GTK CSS styling
│
├── wallpapers/                          # Base 4K wallpapers
│   └── jarvis-master.jpg                # 4K master cyberpunk cockpit & arc-reactor
│
└── tools/                               # Asset generation utilities
    ├── generate_icon_theme.py           # Icon theme builder
    └── create_window_decorations.py     # Metacity & GTK theme builder
```

---

## 🛠️ Usage & Installation

### 1. Launch the Native Stark Desktop Shell
Run the real Linux desktop shell directly on your current desktop (Wayland or X11):
```bash
cd /home/MR_Gray/muteX/theme

# Launch native shell (anchored dock, Windows 11 centered start menu, real app launcher)
./apply.sh --shell
# or directly:
./stark-shell

# Stop the native shell
./apply.sh --stop-shell
```

### 2. Install Full Desktop Suite (Themes, Icons, Window Decor, & Wallpaper)
```bash
./apply.sh --all
```
This automatically:
- Installs the **Cinnamon Shell Theme** to `~/.themes/Jarvis-Windows11-Shell/cinnamon`
- Installs **Window Decorations (Metacity & GTK 3/4)** to `~/.themes/Jarvis-Windows11-Shell/`
- Installs the **Jarvis-White Icon Theme** to `~/.icons/Jarvis-White`
- Generates and applies the **Live OS Telemetry Wallpaper** with your current CPU/RAM metrics to your active desktop session (supports Cinnamon, KDE Plasma 6 Wayland, and GNOME).

### 3. Enable Real-Time Live Wallpaper Updates
To keep the wallpaper continuously updated with your live CPU and RAM consumption in the background:
```bash
# Start the live background daemon (updates every 3 seconds)
./apply.sh --live

# Check daemon and shell status
./apply.sh --status

# Stop the daemon
./apply.sh --stop-live
```

### 4. Generate Snapshot Wallpaper Once
```bash
./apply.sh --wallpaper
```

### 5. Restore Default Settings
```bash
./apply.sh --restore
```


