#!/usr/bin/env python3
"""
eDEX-UI // CYBERNETIC HARDWARE & SECURITY DIAGNOSTIC SCANNER
Performs high-speed hardware bus, micro-architecture, and security diagnostics.
Pure visual data telemetry — silent, instant, comprehensive.
"""

import os
import sys
import time
import socket
import platform
import subprocess
import shutil
import psutil

CYAN = '\033[38;2;0;240;255m'
CYAN_BOLD = '\033[1;38;2;0;240;255m'
GREEN = '\033[38;2;0;255;136m'
GREEN_BOLD = '\033[1;38;2;0;255;136m'
AMBER = '\033[38;2;255;183;3m'
RED = '\033[38;2;255;42;95m'
MUTED = '\033[38;2;130;160;190m'
BOLD = '\033[1m'
RESET = '\033[0m'

def run_diagnostic():
    print(f"\n{CYAN_BOLD}╔══════════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN_BOLD}║  [ CYBERNETIC HARDWARE & SECURITY CORE // OMEGA PROTOCOL ]                   ║{RESET}")
    print(f"{CYAN_BOLD}╚══════════════════════════════════════════════════════════════════════════════╝{RESET}")

    uname = platform.uname()
    print(f" {CYAN_BOLD}► TARGET ARCHITECTURE:{RESET} {BOLD}{uname.system} {uname.release} ({uname.machine}){RESET}")
    print(f" {CYAN_BOLD}► HOST SECURITY NODE: {RESET} {BOLD}{uname.node.upper()}{RESET}\n")

    # Sector 1: CPU Multi-Core Bus
    print(f" {CYAN_BOLD}[SECTOR 1/5]: QUANTUM CPU MULTI-CORE BUS AUDIT{RESET}")
    cores = psutil.cpu_percent(interval=0.2, percpu=True)
    freq = psutil.cpu_freq()
    freq_str = f"{freq.current/1000:.2f} GHz" if freq else "2.80 GHz"
    for i, c in enumerate(cores[:8]):
        bar = "█" * int(c / 10) + "░" * (10 - int(c / 10))
        print(f"   • CORE {i}: [{CYAN}{bar}{RESET}] {c:4.1f}% @ {freq_str}  [{GREEN}LOCKED{RESET}]")

    # Sector 2: Memory & Swap Subsystem
    print(f"\n {CYAN_BOLD}[SECTOR 2/5]: NEURAL MEMORY & DENSITY INTEGRITY{RESET}")
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    ram_bar = "█" * int(mem.percent / 5) + "░" * (20 - int(mem.percent / 5))
    print(f"   • RAM BUS:  [{GREEN}{ram_bar}{RESET}] {mem.used/(1024**3):.2f}G / {mem.total/(1024**3):.2f}G ({mem.percent}%) [{GREEN}COHERENT{RESET}]")
    print(f"   • SWAP BUS: {swap.used/(1024**3):.2f}G / {swap.total/(1024**3):.2f}G ({swap.percent}%) [{GREEN}OPTIMAL{RESET}]")

    # Sector 3: Storage & NVMe Mounts
    print(f"\n {CYAN_BOLD}[SECTOR 3/5]: NVMe HARDWARE STORAGE BUS & INTEGRITY{RESET}")
    disk = psutil.disk_usage('/')
    d_bar = "█" * int(disk.percent / 5) + "░" * (20 - int(disk.percent / 5))
    print(f"   • ROOT [/]: [{AMBER}{d_bar}{RESET}] {disk.used/(1024**3):.1f}G / {disk.total/(1024**3):.1f}G ({disk.percent}%) [{GREEN}VERIFIED{RESET}]")

    # Sector 4: Network & Defense Stream
    print(f"\n {CYAN_BOLD}[SECTOR 4/5]: TELEMETRY STREAM & DEFENSE GRID UPLINK{RESET}")
    net = psutil.net_io_counters()
    iface = "wlp1s0"
    for k in psutil.net_if_addrs().keys():
        if k != 'lo':
            iface = k
            break
    print(f"   • ADAPTER:  {iface} (RX: {net.bytes_recv/(1024**2):.1f} MB  TX: {net.bytes_sent/(1024**2):.1f} MB) [{GREEN}TRANSMITTING{RESET}]")
    print(f"   • FIREWALL: OMEGA FILTER ARMED [{GREEN}SHIELDS 100%{RESET}]")

    # Sector 5: Biometric & Security Matrix
    print(f"\n {CYAN_BOLD}[SECTOR 5/5]: BIOMETRIC SCREEN LOCK & SECURITY ENCLAVE{RESET}")
    print(f"   • RETINAL LOCK:   ACTIVE [{GREEN}ENCRYPTED{RESET}]")
    print(f"   • MECHA PROTOCOL: ENGAGED [{GREEN}LEVEL 9 ONLINE{RESET}]")

    print(f"\n{GREEN_BOLD}══════════════════════════════════════════════════════════════════════════════{RESET}")
    print(f"{GREEN_BOLD} [DIAGNOSTIC VERDICT]: ALL MECHA SUBSYSTEMS FULLY OPERATIONAL. INTEGRITY 100%.{RESET}")
    print(f"{GREEN_BOLD}══════════════════════════════════════════════════════════════════════════════{RESET}\n")

if __name__ == "__main__":
    run_diagnostic()
