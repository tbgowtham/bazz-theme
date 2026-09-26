#!/usr/bin/env python3
"""
eDEX-UI // ORGANIC LIQUID-GAS SOUND SYNTHESIZER
Synthesizes resonant fluid droplets, steam releases, and plasma surges.
"""

import os
import wave
import math
import struct
import random

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
ASSETS_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

def generate_liquid_drop(filename="liquid_drop.wav"):
    path = os.path.join(ASSETS_DIR, filename)
    sample_rate = 44100
    duration = 0.35
    num_samples = int(sample_rate * duration)
    with wave.open(path, 'w') as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        for i in range(num_samples):
            t = i / sample_rate
            freq = 380 + 950 * (1 - math.exp(-32 * t))
            env = math.exp(-18 * t) * math.sin(math.pi * t / duration)
            sample = math.sin(2 * math.pi * freq * t)
            val = int(sample * env * 30000)
            wav.writeframes(struct.pack('<h', max(-32767, min(32767, val))))

def generate_vapor_hiss(filename="vapor_hiss.wav"):
    path = os.path.join(ASSETS_DIR, filename)
    sample_rate = 44100
    duration = 0.45
    num_samples = int(sample_rate * duration)
    with wave.open(path, 'w') as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        prev = 0.0
        for i in range(num_samples):
            t = i / sample_rate
            noise = random.uniform(-1.0, 1.0)
            filtered = 0.25 * noise + 0.75 * prev
            prev = filtered
            env = math.exp(-5.5 * t) * (math.sin(math.pi * t / duration)**0.5)
            sample = filtered * 0.75 + 0.25 * math.sin(2 * math.pi * (2800 - 900 * t) * t)
            val = int(sample * env * 26000)
            wav.writeframes(struct.pack('<h', max(-32767, min(32767, val))))

def generate_plasma_ignite(filename="plasma_ignite.wav"):
    path = os.path.join(ASSETS_DIR, filename)
    sample_rate = 44100
    duration = 0.50
    num_samples = int(sample_rate * duration)
    with wave.open(path, 'w') as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        for i in range(num_samples):
            t = i / sample_rate
            f1 = 220 + 880 * math.sin(math.pi * t / duration)
            f2 = 440 + 440 * (t / duration)**2
            env = math.exp(-3.5 * t) * math.sin(math.pi * t / duration)
            sample = 0.5 * math.sin(2 * math.pi * f1 * t) + 0.5 * math.sin(2 * math.pi * f2 * t)
            val = int(sample * env * 28000)
            wav.writeframes(struct.pack('<h', max(-32767, min(32767, val))))

def generate_solar_flare(filename="solar_flare.wav"):
    path = os.path.join(ASSETS_DIR, filename)
    sample_rate = 44100
    duration = 0.55
    num_samples = int(sample_rate * duration)
    with wave.open(path, 'w') as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        for i in range(num_samples):
            t = i / sample_rate
            noise = random.uniform(-0.5, 0.5)
            f = 160 + 640 * (1 - t / duration)
            env = math.exp(-4 * t) * math.sin(math.pi * t / duration)
            sample = 0.7 * math.sin(2 * math.pi * f * t) + 0.3 * noise
            val = int(sample * env * 28000)
            wav.writeframes(struct.pack('<h', max(-32767, min(32767, val))))

def build_all():
    generate_liquid_drop()
    generate_vapor_hiss()
    generate_plasma_ignite()
    generate_solar_flare()

if __name__ == "__main__":
    build_all()
    print("All liquid-gas organic audio synthesized successfully.")
