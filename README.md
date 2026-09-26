# eDEX-UI // ROBOTIC MECHA & LIQUID-GAS SYSTEM CONTROLLER 🤖⚡

> An ultra-futuristic **Robotic Mecha & Liquid-Gas** cybernetic desktop suite for Linux. Engineered with features standard desktop environments like Cinnamon do not possess: a **fullscreen biometric robotic screen locker, AI adaptive compute pressure monitor, mecha hardware & security diagnostic scanner, physical matter phase shifting, 2D fluid dynamics reactor, and full KDE Plasma 6 & Konsole mecha styling** — completely silent, hardware-accelerated, and built for maximum data density.

---

## ⚡ What Makes This Different (Beyond Cinnamon & Traditional Desktops)

Cinnamon and standard desktop environments provide traditional flat panels, static menus, and basic themes. This system upgrades your OS into an **autonomous cybernetic mecha environment**:

1. **Fullscreen Biometric Robotic Screen Locker (`edex lock` / `edex-lock`)**:
   - Hardware-accelerated GTK 3 & Cairo cybernetic HUD.
   - Dual-ring counter-rotating mecha gears & targeting crosshairs.
   - Vertical laser retinal/biometric scanline sweeping across the HUD.
   - Real-time CPU, RAM, battery, and defense grid telemetry displayed on the locked screen.
   - 100% silent, stealth operation without intrusive sounds or synthetic voices.
   - Secure verification via Linux user password (PAM `/usr/bin/unix_chkpwd`) or emergency bypass PIN (`1234`).
2. **AI Adaptive Compute Pressure Engine (`edex auto`)**:
   - Continuously samples CPU multi-core load and core temperatures to dynamically shift the desktop matter phase:
     - **Cryo-Gas** (< 25% load, < 48°C): Sub-zero liquid nitrogen cyan, frost mist.
     - **Robotic Mecha** (25% - 60% load): Titanium black chassis, mecha hazard gold, core cyan.
     - **Neon Plasma** (60% - 85% load): Ionized electric magenta, violet glow.
     - **Solar Flare** (> 85% load or > 75°C): Superheated solar flare orange and crimson core.
   - Can run as a one-shot evaluation (`edex auto`) or continuous background daemon (`edex auto --daemon`).
3. **Robotic Mecha System Diagnostic Scanner (`edex diag` / `edex scan`)**:
   - Live hardware bus and security audit in your terminal: Quantum CPU multi-core audit, neural memory bus test, NVMe storage integrity, and defense uplink telemetry.
4. **Physical Matter Phase Shifting (`edex phase <state>`)**:
   - Instant system-wide matter phase transitions across KDE Plasma, Konsole, GTK, and shell prompt:
     - **`mecha`** : Titanium Black (`#070a10`), Mecha Hazard Gold (`#ffb703`), Core Cyan (`#00f0ff`).
     - **`cryo`** : Sub-zero Liquid Nitrogen (`#00f5d4`), Arctic Ice Blue (`#00bbf9`), Frost Mist.
     - **`plasma`** : Ionized Neon Plasma (`#f72585`), Electric Violet (`#9d4edd`), Cyan Glow.
     - **`mercury`** : Liquid Metal Quicksilver (`#e0e1dd`), Liquid Titanium, Gallium Aqua.
     - **`solar`** : Superheated Solar Flare (`#ffb703`), Molten Orange (`#ff4800`), Crimson Core.
5. **Interactive 2D Liquid-Gas Terminal Reactor (`edex fluid`)**:
   - Real-time fluid wave equation and vapor particle physics reacting to live CPU temperature and RAM viscosity.
6. **Memory Condensation Reactor (`edex condense`)**:
   - Terminal animation of gaseous threads cooling and condensing into a pure liquid pool while compacting memory caches.

---

## 🚀 The Terminal Command: `edex`

Because it is installed in your `$PATH` (`~/.local/bin/edex`), you can run `edex` from **any terminal window**:

```bash
# Apply the master Robotic Mecha theme across entire system
edex
```

### Specialized Commands:

```bash
# 1. Lock screen with robotic biometric HUD (silent & secure)
edex lock
# (or simply: edex-lock)

# 2. Run mecha system hardware & security diagnostic
edex diag

# 3. Run AI adaptive matter engine (auto-shifts theme by real-time compute load)
edex auto
# (or continuously monitor: edex auto --daemon)

# 4. Switch immediately to Titanium Mecha state
edex mecha

# 5. Launch interactive 2D fluid dynamics reactor
edex fluid

# 6. Shift matter state (mecha, cryo, plasma, mercury, solar)
edex phase plasma

# 7. Compact memory cache with liquid condensation animation
edex condense

# 8. Launch live telemetry terminal dashboard
edex --app
```

---

## 🔒 The Robotic Screen Locker (`edex lock` / `edex-lock`)

When you run `edex lock`:
- Takes over the display in fullscreen mode.
- Locks the workstation with rotating mecha gears and a sweeping laser reticle.
- Completely silent operation (no unwanted synthetic voice or audio effects).
- Enter your Linux user password (or default bypass PIN `1234`) and press `Enter`:
  - **Wrong Password**: Security alert border flashes red, intrusion attempt logged.
  - **Correct Password**: Emerald green confirmation glow, unlocks smoothly into your session.
- You can customize your lock PIN anytime in `~/.config/edex_lock_pin`.

---

## 🛠️ Command Summary

| Command | Action |
| :--- | :--- |
| `edex` | Apply master Robotic Mecha theme across the entire system |
| `edex lock` (or `edex-lock`) | Launch fullscreen robotic biometric screen locker (silent) |
| `edex auto` (or `--daemon`) | Run AI adaptive compute pressure engine (shifts theme by CPU/temp) |
| `edex diag` (or `scan`) | Run robotic mecha hardware & security diagnostic |
| `edex mecha` | Switch immediately to Titanium Mecha state |
| `edex fluid` | Launch interactive 2D fluid wave & vapor reactor |
| `edex phase <state>` | Shift matter state (`mecha`, `cryo`, `plasma`, `mercury`, `solar`) |
| `edex condense` | Compact memory cache with liquid condensation animation |
| `edex --app` | Launch live telemetry terminal monitor dashboard |
| `edex --status` | Check system telemetry and active matter state |
| `edex --restore` | Restore default desktop theme & settings |

---

## 📁 Repository Structure

```text
theme/
├── edex-theme                           # Master system controller (executable)
├── edex                                 # Symlink to edex-theme
├── apply.sh                             # Convenience wrapper script
│
├── tools/
│   ├── robotic_lockscreen.py            # Fullscreen robotic mecha biometric screen locker (silent)
│   ├── mecha_diag.py                    # Robotic hardware & security diagnostic scanner
│   ├── fluid_reactor.py                 # Real-time 2D fluid wave & vapor particle reactor
│   ├── eDEX-TRON-Mecha.colors           # Titanium Mecha KDE Plasma color scheme
│   ├── eDEX-TRON-Cryo.colors            # Sub-zero Cryo-Gas KDE color scheme
│   ├── eDEX-TRON-Plasma.colors          # Neon-Plasma KDE color scheme
│   ├── eDEX-TRON-Mercury.colors         # Liquid-Mercury KDE color scheme
│   ├── eDEX-TRON-Solar.colors           # Solar-Flare KDE color scheme
│   ├── eDEX-TRON.profile                # High-contrast Konsole terminal profile
│   └── edex-theme.sh                    # Interactive shell environment configuration
│
├── gtk-3.0/ & gtk-4.0/                  # Fluid mecha glassmorphism GTK themes
├── metacity-1/                          # Window decorations with glowing vapor borders
├── icons/Jarvis-White/                  # Minimalist vector icon theme
└── cinnamon/                            # Cinnamon shell theme
```
