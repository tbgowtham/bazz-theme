# eDEX-UI // TRON SYSTEM-WIDE THEME & TERMINAL CONTROLLER 🌐⚡

> An authentic, futuristic **eDEX-UI / TRON: Legacy** interface suite for Linux. Transform your entire system with a single terminal command into a high-tech sci-fi command deck with **real-time desktop wallpaper telemetry, animated rotating radar, multi-core CPU meters, RAM & storage gauges, cyber-deck keyboard, KDE Plasma 6 & Konsole Tron color themes, and an interactive terminal dashboard application**.

---

## 📸 Real Linux OS Telemetry Wallpaper HUD (eDEX-UI)

The wallpaper engine inspects your real Linux system via `psutil` and renders a live eDEX-UI Tron tactical interface directly onto your desktop wallpaper, continuously updated by a background daemon:

![eDEX-UI Live Telemetry Wallpaper](file:///home/MR_Gray/.gemini/antigravity-ide/brain/b42dcd67-d1bd-4be4-ae35-a854875eef4f/edex-live-wallpaper.png)

### Live Embedded Telemetry:
- **Real CPU Multi-Core Utilization**: Overall load percentage, CPU clock frequency, CPU temperature, sparkline load waveform, and individual `C0`-`C7` core meters with segmented cyan-to-amber progress bars.
- **System Memory Architecture**: Exact RAM used / total GB, percentage bar, and Swap allocation.
- **Top Process Threads**: Top active resource-demanding processes running on your OS.
- **Geo-Radar & Scanner**: Circular wireframe radar with rotating sweep beam, concentric range rings, degree crosshairs, target blips, and compass coordinates.
- **Network Interface & I/O**: Active network interface (`wlan0`/`eth0`), local IP address, and real-time `RX` (download) and `TX` (upload) traffic counters.
- **Storage Mounts & Disk**: NVMe `/` root filesystem capacity, used space, and disk activity.
- **Bottom Cyber-Deck Keyboard**: Full virtual futuristic Tron keyboard matrix with illuminated keycaps.
- **Center Workspace Matrix**: Holographic HUD corner brackets framing your desktop application workspace.

---

## 🚀 The Terminal Command: `edex`

You can transform everything in your system using the dedicated terminal command:

```bash
# Run from anywhere in your terminal
edex
```

*(Also available as `edex-theme` or `./apply.sh`)*

### What happens when you run `edex`:
1. **Desktop Wallpaper**: Generates and applies the eDEX-UI Tron live telemetry wallpaper to your active desktop session (KDE Plasma 6, Cinnamon, GNOME).
2. **Live Daemon**: Automatically activates the background telemetry daemon to continuously refresh wallpaper metrics every 2.5s.
3. **KDE Plasma 6**: Installs and applies the `eDEX-TRON` color scheme across all desktop windows, titlebars, panels, and widgets.
4. **Terminal & Konsole**: Installs the `eDEX-TRON` profile & color scheme, and dynamically shifts your current terminal window to Neon Cyan (`#00e5ff`) on deep cyber-navy (`#000b1e`) using OSC escape sequences.
5. **Shell Prompt**: Configures `[eDEX-UI // TRON]` prompt in `~/.bashrc.d/edex-theme.sh`.
6. **Desktop Theme & Icons**: Configures GTK 3/4 themes and minimalist neon icon theme.
7. **Audio Feedback**: Plays an authentic electronic Tron startup chime.

---

## 🖥️ Interactive Terminal Dashboard Mode (`edex --app`)

In addition to transforming your desktop, `edex` can run as a live, interactive terminal application:

```bash
edex --app
# or
edex --tui
```

Features inside the terminal dashboard:
- Fullscreen alternate screen buffer (does not clutter your terminal history).
- Live animated ASCII Geo-Radar scanner with sweeping beam.
- Real-time CPU core utilization gauges (`C0` - `C7`).
- Live RAM, Swap, and Storage consumption meters.
- Active process list.
- Interactive controls: `[Q]` to exit, `[W]` to refresh desktop wallpaper.

---

## 🛠️ Command Options

| Command | Action |
| :--- | :--- |
| `edex` | Apply full eDEX-UI theme across entire system (wallpaper, terminal, KDE, GTK, daemon) |
| `edex --app` (or `--tui`) | Launch interactive live terminal monitor dashboard |
| `edex --wallpaper` | Render and apply eDEX-UI wallpaper snapshot once |
| `edex --live` | Start background live telemetry daemon |
| `edex --stop` | Stop background live telemetry daemon |
| `edex --status` | Check live system telemetry and daemon status |
| `edex --restore` | Restore default desktop theme & settings |

---

## 📁 Repository Structure

```text
theme/
├── edex-theme                           # Master terminal command (executable)
├── edex                                 # Symlink to edex-theme
├── apply.sh                             # Convenience wrapper script
├── generate_wallpaper.py                # eDEX-UI Tron live telemetry wallpaper engine
├── live_wallpaper_daemon.py             # Background daemon for continuous wallpaper updates
│
├── tools/
│   ├── eDEX-TRON.colors                 # KDE Plasma 6 TRON color scheme
│   ├── eDEX-TRON.colorscheme            # Konsole TRON color scheme
│   ├── eDEX-TRON.profile                # Konsole TRON profile
│   └── edex-theme.sh                    # Interactive shell environment configuration
│
├── assets/
│   └── edex_chime.wav                   # Synthesized Tron power-up sound chime
│
├── gtk-3.0/ & gtk-4.0/                  # Dark neon cyan GTK themes
├── metacity-1/                          # Window decorations with glowing cyan borders
├── icons/Jarvis-White/                  # Minimalist vector icon theme
└── cinnamon/                            # Cinnamon shell theme
```
