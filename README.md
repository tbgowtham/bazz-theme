# eDEX-UI // ROBOTIC MECHA & LIQUID-GAS SYSTEM CONTROLLER 🤖⚡

> An ultra-futuristic **Robotic Mecha & Liquid-Gas** cybernetic desktop suite for Linux. Engineered with features standard desktop environments like Cinnamon do not possess: a **fullscreen biometric robotic screen locker, onboard robotic AI voice synthesizer, mecha hardware diagnostic scanner, physical matter phase shifting, 2D fluid dynamics reactor, and full KDE Plasma 6 & Konsole mecha styling**.

---

## ⚡ What Makes This Different (Beyond Cinnamon & Traditional Desktops)

Cinnamon and standard desktop environments provide traditional flat panels, static menus, and basic themes. This system upgrades your OS into an **onboard combat mecha AI**:

1. **Fullscreen Biometric Robotic Screen Locker (`edex lock`)**:
   - Hardware-accelerated GTK 3 & Cairo cybernetic HUD.
   - Dual-ring counter-rotating mecha gears & targeting crosshairs.
   - Vertical laser retinal/biometric scanline sweeping across the HUD.
   - Real-time CPU, RAM, battery, and defense grid telemetry displayed on the locked screen.
   - Mechanical hydraulic lock sound (`mech_lock.wav`) and pneumatic unlock release (`mech_unlock.wav`).
   - Robotic voice announcements: *"SECURITY PROTOCOL ACTIVE. WORKSTATION LOCKED."* / *"AUTHENTICATION CONFIRMED. ACCESS GRANTED."*
   - Secure verification via Linux user password or emergency bypass PIN (`1234`).
2. **Onboard Robotic AI Voice Synthesizer**:
   - Mechanical formant-modulated speech AI that speaks system status, matter phase shifts, lock events, and diagnostic verdicts.
   - Can be toggled anytime via `edex voice on` / `edex voice off`.
3. **Robotic Mecha System Diagnostic Scanner (`edex diag`)**:
   - Live hardware bus and security audit in your terminal: Quantum CPU multi-core audit, neural memory bus test, NVMe storage integrity, and defense uplink check with cybernetic sonar beeps.
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

Because it is installed in your `$PATH`, you can run `edex` from **any terminal window**:

```bash
# Apply the master Robotic Mecha theme across entire system
edex
```

### Specialized Commands:

```bash
# 1. Lock screen with robotic biometric HUD
edex lock
# (or simply: edex-lock)

# 2. Run mecha system hardware & security diagnostic
edex diag

# 3. Switch immediately to Titanium Mecha state & voice
edex mecha

# 4. Launch interactive 2D fluid dynamics reactor
edex fluid

# 5. Shift matter state (mecha, cryo, plasma, mercury, solar)
edex phase plasma

# 6. Compact memory cache with liquid condensation animation
edex condense

# 7. Toggle robotic AI voice synthesizer
edex voice on   # or: edex voice off

# 8. Launch live telemetry terminal dashboard
edex --app
```

---

## 🔒 The Robotic Screen Locker (`edex lock` / `edex-lock`)

When you run `edex lock`:
- Takes over the display in fullscreen mode.
- Locks the workstation with rotating mecha gears and a sweeping laser reticle.
- Robotic Voice speaks: *"SECURITY PROTOCOL ACTIVE. WORKSTATION LOCKED. AUTHENTICATION REQUIRED."*
- Enter your Linux user password (or default bypass PIN `1234`) and press `Enter`:
  - **Wrong Password**: Alarm buzzer sounds, screen flashes red, and AI announces *"ACCESS DENIED. INTRUSION ATTEMPT LOGGED."*
  - **Correct Password**: Pneumatic depressurize sound, emerald green glow, and AI announces *"AUTHENTICATION CONFIRMED. ACCESS GRANTED."* Unlocks smoothly.
- You can also customize your lock PIN anytime in `~/.config/edex_lock_pin`.

---

## 🛠️ Command Summary

| Command | Action |
| :--- | :--- |
| `edex` | Apply master Robotic Mecha theme across the entire system |
| `edex lock` (or `edex-lock`) | Launch fullscreen robotic biometric screen locker |
| `edex diag` (or `scan`) | Run robotic mecha hardware & security diagnostic |
| `edex mecha` | Switch immediately to Titanium Mecha state & voice |
| `edex fluid` | Launch interactive 2D fluid wave & vapor reactor |
| `edex phase <state>` | Shift matter state (`mecha`, `cryo`, `plasma`, `mercury`, `solar`) |
| `edex condense` | Compact memory cache with liquid condensation animation |
| `edex voice <on\|off>` | Toggle mechanical robotic AI voice synthesizer |
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
│   ├── robotic_lockscreen.py            # Fullscreen robotic mecha biometric screen locker
│   ├── robot_voice.py                   # Mechanical robotic combat AI voice synthesizer
│   ├── mecha_diag.py                    # Robotic hardware & security diagnostic scanner
│   ├── fluid_reactor.py                 # Real-time 2D fluid wave & vapor particle reactor
│   ├── sound_synth.py                   # Organic liquid & mechanical sound synthesizer
│   ├── eDEX-TRON-Mecha.colors           # Titanium Mecha KDE Plasma color scheme
│   ├── eDEX-TRON-Cryo.colors            # Sub-zero Cryo-Gas KDE color scheme
│   ├── eDEX-TRON-Plasma.colors          # Neon-Plasma KDE color scheme
│   ├── eDEX-TRON-Mercury.colors         # Liquid-Mercury KDE color scheme
│   ├── eDEX-TRON-Solar.colors           # Solar-Flare KDE color scheme
│   └── edex-theme.sh                    # Interactive shell environment configuration
│
├── assets/
│   ├── mech_lock.wav                    # Hydraulic clamp closure sound
│   ├── mech_unlock.wav                  # Pneumatic depressurize & servo sound
│   ├── access_denied.wav                # High-security alarm buzzer sound
│   ├── scan_beep.wav                    # Cybernetic scanning sonar beep
│   ├── liquid_drop.wav                  # Resonant fluid droplet sound
│   ├── vapor_hiss.wav                   # Steam vapor release sound
│   ├── plasma_ignite.wav                # High-energy plasma surge sound
│   └── solar_flare.wav                  # Solar flare hiss sound
│
├── gtk-3.0/ & gtk-4.0/                  # Fluid mecha glassmorphism GTK themes
├── metacity-1/                          # Window decorations with glowing vapor borders
├── icons/Jarvis-White/                  # Minimalist vector icon theme
└── cinnamon/                            # Cinnamon shell theme
```
