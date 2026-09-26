# eDEX-UI // TRON SYSTEM-WIDE THEME & TERMINAL CONTROLLER 🌐⚡

> An authentic, futuristic **eDEX-UI / TRON: Legacy** interface suite for Linux. Transform your entire system with a single terminal command into a high-tech sci-fi command deck with **KDE Plasma 6 TRON color themes, Konsole terminal profile, active terminal OSC palette shifting, custom shell prompt, GTK 3/4 neon cyan styling, and an interactive live terminal dashboard application**.

---

## 🚀 The Terminal Command: `edex`

Transform everything in your system using the dedicated terminal command:

```bash
# Run from anywhere in your terminal
edex
```

*(Also available as `edex-theme` or `./apply.sh`)*

### What happens when you run `edex`:
1. **Terminal & Konsole Colors**: Installs the `eDEX-TRON` profile & color scheme, and dynamically shifts your current terminal window to Neon Cyan (`#00e5ff`) on deep cyber-navy (`#000b1e`) using OSC escape sequences.
2. **KDE Plasma 6**: Installs and applies the `eDEX-TRON` color scheme across all desktop windows, titlebars, panels, and widgets.
3. **Shell Prompt**: Configures `[eDEX-UI // TRON]` prompt in `~/.bashrc.d/edex-theme.sh`.
4. **Desktop Theme & Icons**: Configures GTK 3/4 themes, Metacity glowing cyan borders, and the Jarvis-White minimalist vector icon theme.
5. **Audio Feedback**: Plays an authentic electronic Tron startup chime.

---

## 🖥️ Interactive Terminal Dashboard Mode (`edex --app`)

In addition to transforming your desktop theme, `edex` can run as a live, interactive terminal application:

```bash
edex --app
# or
edex --tui
```

### Features inside the terminal dashboard:
- **Fullscreen alternate screen buffer** (does not clutter your terminal history).
- **Live animated ASCII Geo-Radar scanner** with sweeping beam.
- **Real-time CPU core utilization gauges** (`C0` - `C7`).
- **Live RAM, Swap, and Storage consumption meters**.
- **Active process list**.
- **Interactive controls**: Press `[Q]` or `Ctrl+C` to exit.

---

## 🛠️ Command Options

| Command | Action |
| :--- | :--- |
| `edex` | Apply full eDEX-UI theme across entire system (terminal, KDE, GTK, icons, prompt) |
| `edex --app` (or `--tui`) | Launch interactive live terminal monitor dashboard |
| `edex --status` | Check system telemetry and theme status |
| `edex --restore` | Restore default desktop theme & settings |

---

## 📁 Repository Structure

```text
theme/
├── edex-theme                           # Master terminal command (executable)
├── edex                                 # Symlink to edex-theme
├── apply.sh                             # Convenience wrapper script
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
