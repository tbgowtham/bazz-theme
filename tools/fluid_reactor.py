#!/usr/bin/env python3
"""
==============================================================================
eDEX-UI // LIQUID-GAS FLUID DYNAMICS & VAPOR REACTOR
==============================================================================
Real-time 2D ASCII/Unicode fluid wave equation & vapor particle simulation
driven directly by Linux OS telemetry (CPU, RAM, Temp, Network).

Interactive controls:
- [SPACE] : Inject fluid droplet (creates wave ripple + sound)
- [B]     : Release vapor bubble surge
- [P]     : Cycle matter phase (Cryo -> Plasma -> Mercury -> Solar)
- [C]     : Condense & compact memory
- [Q]     : Exit reactor
==============================================================================
"""

import os
import sys
import time
import math
import random
import select
import termios
import tty
import shutil
import subprocess
import psutil

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
ASSETS_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "assets")

PHASES = {
    'cryo': {
        'name': 'CRYO-GAS [LIQUID NITROGEN]',
        'scheme': 'eDEX-TRON-Cryo',
        'c_pri': (0, 245, 212),
        'c_sec': (0, 187, 249),
        'c_vapor': (224, 251, 252),
        'c_bg': (0, 14, 30),
        'surface_char': '≋',
        'temp_offset': -15.0
    },
    'plasma': {
        'name': 'NEON-PLASMA [IONIZED VAPOR]',
        'scheme': 'eDEX-TRON-Plasma',
        'c_pri': (247, 37, 133),
        'c_sec': (157, 78, 221),
        'c_vapor': (0, 240, 255),
        'c_bg': (16, 2, 26),
        'surface_char': '∿',
        'temp_offset': 45.0
    },
    'mercury': {
        'name': 'LIQUID-MERCURY [QUICKSILVER]',
        'scheme': 'eDEX-TRON-Mercury',
        'c_pri': (224, 225, 221),
        'c_sec': (0, 229, 255),
        'c_vapor': (119, 141, 169),
        'c_bg': (10, 14, 20),
        'surface_char': '≈',
        'temp_offset': 5.0
    },
    'solar': {
        'name': 'SOLAR-FLARE [SUPERHEATED GAS]',
        'scheme': 'eDEX-TRON-Solar',
        'c_pri': (255, 183, 3),
        'c_sec': (255, 72, 0),
        'c_vapor': (255, 209, 102),
        'c_bg': (20, 5, 0),
        'surface_char': '~',
        'temp_offset': 85.0
    }
}

class VaporParticle:
    def __init__(self, x, y, c_tuple):
        self.x = float(x)
        self.y = float(y)
        self.vx = random.uniform(-0.4, 0.4)
        self.vy = random.uniform(-0.35, -0.85)
        self.life = 1.0
        self.decay = random.uniform(0.04, 0.08)
        self.c_tuple = c_tuple
        self.char = random.choice(['*', '°', '·', 'o', '¤', '~'])

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= self.decay
        return self.life > 0

class FluidReactor:
    def __init__(self, phase_name='cryo'):
        self.phase_key = phase_name if phase_name in PHASES else 'cryo'
        self.term_w, self.term_h = shutil.get_terminal_size((80, 24))
        self.sim_w = max(40, self.term_w - 4)
        
        # 1D wave simulation arrays
        self.heights = [0.0] * self.sim_w
        self.velocities = [0.0] * self.sim_w
        self.c2 = 0.22      # Wave propagation speed
        self.damping = 0.025 # Fluid viscosity damping
        
        self.particles = []
        self.last_net_bytes = 0
        try:
            self.last_net_bytes = psutil.net_io_counters().bytes_recv
        except Exception:
            pass

    def play_sound(self, sound_file):
        path = os.path.join(ASSETS_DIR, sound_file)
        if os.path.exists(path):
            for player in ["paplay", "pw-play", "aplay"]:
                if shutil.which(player):
                    try:
                        subprocess.Popen([player, path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        break
                    except Exception:
                        pass

    def drop_ripple(self, x=None, strength=7.0):
        if x is None:
            x = random.randint(5, self.sim_w - 6)
        x = max(2, min(self.sim_w - 3, int(x)))
        self.heights[x] += strength
        self.heights[x - 1] += strength * 0.5
        self.heights[x + 1] += strength * 0.5
        self.play_sound("liquid_drop.wav")

    def burst_bubble(self):
        p_cfg = PHASES[self.phase_key]
        for _ in range(8):
            bx = random.randint(4, self.sim_w - 5)
            by = self.term_h - 6
            self.particles.append(VaporParticle(bx, by, p_cfg['c_vapor']))
        self.drop_ripple(strength=4.0)
        self.play_sound("vapor_hiss.wav")

    def cycle_phase(self):
        keys = list(PHASES.keys())
        idx = (keys.index(self.phase_key) + 1) % len(keys)
        self.phase_key = keys[idx]
        p_cfg = PHASES[self.phase_key]
        
        # Shift KDE & Konsole colors dynamically
        if shutil.which("plasma-apply-colorscheme"):
            subprocess.run(["plasma-apply-colorscheme", p_cfg['scheme']], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
        r, g, b = p_cfg['c_pri']
        br, bg, bb = p_cfg['c_bg']
        sys.stdout.write(f"\033]10;rgb:{r:02x}/{g:02x}/{b:02x}\a")
        sys.stdout.write(f"\033]11;rgb:{br:02x}/{bg:02x}/{bb:02x}\a")
        sys.stdout.flush()
        self.play_sound("vapor_hiss.wav")

    def condense_memory(self):
        # Memory compaction
        subprocess.run(["sync"], check=False)
        self.burst_bubble()

    def update_physics(self, cpu_p, mem_p):
        # CPU heat adds random thermal agitation / boiling
        boil_chance = min(0.9, cpu_p / 100.0)
        if random.random() < boil_chance:
            rx = random.randint(2, self.sim_w - 3)
            amp = (cpu_p / 100.0) * random.uniform(1.5, 4.0)
            self.heights[rx] += amp
            p_cfg = PHASES[self.phase_key]
            self.particles.append(VaporParticle(rx, self.term_h - 8, p_cfg['c_vapor']))

        # Update 1D wave equation
        new_v = [0.0] * self.sim_w
        new_h = [0.0] * self.sim_w
        for x in range(1, self.sim_w - 1):
            accel = self.c2 * (self.heights[x - 1] - 2 * self.heights[x] + self.heights[x + 1])
            new_v[x] = (self.velocities[x] + accel) * (1.0 - self.damping)
            new_h[x] = self.heights[x] + new_v[x]

        self.velocities = new_v
        self.heights = new_h

        # Update vapor particles
        self.particles = [p for p in self.particles if p.update()]

        # Check network I/O for splash ripples
        try:
            cur_bytes = psutil.net_io_counters().bytes_recv
            diff = cur_bytes - self.last_net_bytes
            self.last_net_bytes = cur_bytes
            if diff > 50000: # 50KB received
                self.drop_ripple(strength=min(6.0, diff / 25000))
        except Exception:
            pass

    def run(self):
        # Enter alternate buffer & hide cursor
        sys.stdout.write('\033[?1049h\033[?25l\033[H\033[2J')
        sys.stdout.flush()

        old_settings = None
        try:
            if sys.stdin.isatty():
                old_settings = termios.tcgetattr(sys.stdin)
                tty.setcbreak(sys.stdin.fileno())

            last_stats_t = 0
            cpu_p = 10.0
            mem_p = 50.0

            while True:
                # Terminal resize handling
                nw, nh = shutil.get_terminal_size((80, 24))
                if nw != self.term_w or nh != self.term_h:
                    self.term_w, self.term_h = nw, nh
                    self.sim_w = max(40, self.term_w - 4)
                    self.heights = [0.0] * self.sim_w
                    self.velocities = [0.0] * self.sim_w
                    sys.stdout.write('\033[2J')

                # User keyboard input (non-blocking)
                if sys.stdin.isatty():
                    r, _, _ = select.select([sys.stdin], [], [], 0.04)
                    if r:
                        ch = sys.stdin.read(1)
                        if ch in ['q', 'Q', '\x03', '\x1b']:
                            break
                        elif ch == ' ':
                            self.drop_ripple()
                        elif ch in ['b', 'B']:
                            self.burst_bubble()
                        elif ch in ['p', 'P']:
                            self.cycle_phase()
                        elif ch in ['c', 'C']:
                            self.condense_memory()

                # Refresh telemetry every 0.8s
                now = time.time()
                if now - last_stats_t > 0.8:
                    last_stats_t = now
                    cpu_p = psutil.cpu_percent(interval=None)
                    mem = psutil.virtual_memory()
                    mem_p = mem.percent

                self.update_physics(cpu_p, mem_p)

                # Render Frame
                p_cfg = PHASES[self.phase_key]
                pr, pg, pb = p_cfg['c_pri']
                sr, sg, sb = p_cfg['c_sec']
                vr, vg, vb = p_cfg['c_vapor']

                # Liquid base line determined by RAM %
                pool_depth = max(6, int((mem_p / 100.0) * (self.term_h - 10)))
                surface_y = self.term_h - pool_depth - 2

                # Grid buffer of characters & colors
                screen = [[' ' for _ in range(self.term_w)] for _ in range(self.term_h)]
                colors = [[None for _ in range(self.term_w)] for _ in range(self.term_h)]

                # 1. Top HUD Header
                calc_temp = 35.0 + (cpu_p * 0.65) + p_cfg['temp_offset']
                header_str = f" [≋ eDEX-UI // LIQUID-GAS FLUID REACTOR ≋]   PHASE: {p_cfg['name']}"
                for i, c in enumerate(header_str[:self.term_w - 2]):
                    screen[0][i + 1] = c
                    colors[0][i + 1] = (pr, pg, pb)

                sub_str = f" FLUID_TEMP: {calc_temp:.1f}°C   TURBULENCE: {cpu_p:.1f}%   VISCOSITY_LEVEL: {mem_p:.1f}% RAM"
                for i, c in enumerate(sub_str[:self.term_w - 2]):
                    screen[1][i + 1] = c
                    colors[1][i + 1] = (sr, sg, sb)

                # 2. Render Vapor Particles in Gas Region
                for p in self.particles:
                    px = int(p.x)
                    py = int(p.y)
                    if 2 <= py < self.term_h - 1 and 2 <= px < self.term_w - 2:
                        screen[py][px] = p.char
                        alpha = max(0.2, min(1.0, p.life))
                        colors[py][px] = (int(vr * alpha), int(vg * alpha), int(vb * alpha))

                # 3. Render Fluid Surface and Liquid Body
                for sx in range(min(self.sim_w, self.term_w - 4)):
                    wave_off = int(self.heights[sx] * 0.4)
                    cur_surf_y = max(3, min(self.term_h - 2, surface_y - wave_off))
                    tx = sx + 2

                    # Surface boundary wave
                    if 0 <= cur_surf_y < self.term_h:
                        screen[cur_surf_y][tx] = p_cfg['surface_char']
                        colors[cur_surf_y][tx] = (pr, pg, pb)

                    # Submerged liquid body
                    for ly in range(cur_surf_y + 1, self.term_h - 1):
                        depth_ratio = (ly - cur_surf_y) / max(1, (self.term_h - cur_surf_y))
                        # Subtle gradient from surface color to deep abyss
                        lr = int(pr * (1.0 - depth_ratio * 0.6))
                        lg = int(pg * (1.0 - depth_ratio * 0.6))
                        lb = int(pb * (1.0 - depth_ratio * 0.6))
                        screen[ly][tx] = '█' if depth_ratio > 0.4 else '▓'
                        colors[ly][tx] = (lr, lg, lb)

                # 4. Bottom Controls Bar
                footer_str = " [SPACE] Drop Ripple   [B] Bubble Surge   [P] Shift Phase   [C] Condense   [Q] Exit"
                for i, c in enumerate(footer_str[:self.term_w - 2]):
                    screen[self.term_h - 1][i + 1] = c
                    colors[self.term_h - 1][i + 1] = (sr, sg, sb)

                # Output buffer to terminal
                buf = ['\033[H']
                cur_c = None
                for y in range(self.term_h):
                    for x in range(self.term_w):
                        c = colors[y][x]
                        ch = screen[y][x]
                        if c != cur_c:
                            if c is None:
                                buf.append('\033[0m')
                            else:
                                buf.append(f"\033[38;2;{c[0]};{c[1]};{c[2]}m")
                            cur_c = c
                        buf.append(ch)
                    if y < self.term_h - 1:
                        buf.append('\n')

                sys.stdout.write("".join(buf))
                sys.stdout.flush()

        finally:
            if old_settings and sys.stdin.isatty():
                termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
            sys.stdout.write('\033[0m\033[?25h\033[?1049l')
            sys.stdout.flush()

if __name__ == "__main__":
    phase = sys.argv[1] if len(sys.argv) > 1 else 'cryo'
    reactor = FluidReactor(phase)
    reactor.run()
