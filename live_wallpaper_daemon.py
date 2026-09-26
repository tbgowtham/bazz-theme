#!/usr/bin/env python3
"""
STARK INDUSTRIES // LIVE TELEMETRY WALLPAPER BACKGROUND DAEMON
Continuously updates the desktop wallpaper with real-time Linux OS telemetry:
CPU %, RAM %, Storage, Network, and Uptime.
Supports starting, stopping, and status checking via CLI.
"""

import os
import sys
import time
import signal
import argparse
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PID_FILE = "/tmp/stark_wallpaper_daemon.pid"
OUTPUT_WALLPAPER = os.path.expanduser("~/.local/share/backgrounds/stark-live-wallpaper.png")
GEN_SCRIPT = os.path.join(SCRIPT_DIR, "generate_wallpaper.py")

def get_running_pid():
    if os.path.exists(PID_FILE):
        try:
            with open(PID_FILE, "r") as f:
                pid = int(f.read().strip())
            # Check if process is alive
            os.kill(pid, 0)
            return pid
        except Exception:
            try:
                os.remove(PID_FILE)
            except Exception:
                pass
    return None

def start_daemon(interval=3.0, base_image=None):
    pid = get_running_pid()
    if pid:
        print(f"[STARK DAEMON]: Live wallpaper daemon is already running (PID: {pid}).")
        return

    # Fork to background
    cmd = [sys.executable, GEN_SCRIPT, "--apply", "--live", "--interval", str(interval), "--output", OUTPUT_WALLPAPER]
    if base_image:
        cmd.extend(["--base", base_image])

    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        preexec_fn=os.setpgrp
    )

    with open(PID_FILE, "w") as f:
        f.write(str(proc.pid))

    print(f"[STARK DAEMON]: Started Live Telemetry Wallpaper Daemon (PID: {proc.pid}, interval: {interval}s).")
    print(f"[STARK DAEMON]: Active wallpaper: {OUTPUT_WALLPAPER}")

def stop_daemon():
    pid = get_running_pid()
    if not pid:
        print("[STARK DAEMON]: No active wallpaper daemon found.")
        return

    try:
        os.killpg(os.getpgid(pid), signal.SIGTERM)
        print(f"[STARK DAEMON]: Stopped wallpaper daemon (PID: {pid}).")
    except Exception as e:
        print(f"[STARK DAEMON]: Error stopping process: {e}")

    if os.path.exists(PID_FILE):
        try:
            os.remove(PID_FILE)
        except Exception:
            pass

def status_daemon():
    pid = get_running_pid()
    if pid:
        print(f"[STARK DAEMON]: Live wallpaper daemon is ONLINE (PID: {pid}).")
        print(f"[STARK DAEMON]: Updating {OUTPUT_WALLPAPER} with real OS metrics.")
    else:
        print("[STARK DAEMON]: Live wallpaper daemon is OFFLINE.")

def main():
    parser = argparse.ArgumentParser(description="Manage Stark Live Wallpaper Daemon")
    parser.add_argument("action", choices=["start", "stop", "status", "restart"], default="status", nargs="?")
    parser.add_argument("--interval", type=float, default=3.0, help="Refresh interval in seconds")
    parser.add_argument("--base", default=None, help="Base image path")
    args = parser.parse_args()

    if args.action == "start":
        start_daemon(args.interval, args.base)
    elif args.action == "stop":
        stop_daemon()
    elif args.action == "restart":
        stop_daemon()
        time.sleep(1)
        start_daemon(args.interval, args.base)
    elif args.action == "status":
        status_daemon()

if __name__ == "__main__":
    main()
