import math
import os
from PIL import Image

def generate_slate_wallpaper_svg(width=3840, height=2160):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <!-- Rich Slate / Aubergine Deep Warm Background (Gentle on the eyes, zero glare) -->
    <linearGradient id="slate-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2F282B" />
      <stop offset="50%" stop-color="#262124" />
      <stop offset="100%" stop-color="#1E1A1C" />
    </linearGradient>

    <radialGradient id="warm-glow" cx="80%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#5A3528" stop-opacity="0.40" />
      <stop offset="50%" stop-color="#3D2625" stop-opacity="0.20" />
      <stop offset="100%" stop-color="#1E1A1C" stop-opacity="0" />
    </radialGradient>

    <!-- Ubuntu Orange Accent Gradients -->
    <linearGradient id="orange-primary" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF6836" />
      <stop offset="60%" stop-color="#E95420" />
      <stop offset="100%" stop-color="#BF3B0B" />
    </linearGradient>

    <linearGradient id="orange-deep" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#C74010" />
      <stop offset="100%" stop-color="#8F2A06" />
    </linearGradient>

    <linearGradient id="orange-translucent" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E95420" stop-opacity="0.22" />
      <stop offset="100%" stop-color="#E95420" stop-opacity="0.04" />
    </linearGradient>

    <linearGradient id="dark-facet" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#44393D" stop-opacity="0.5" />
      <stop offset="100%" stop-color="#2B2326" stop-opacity="0.8" />
    </linearGradient>

    <!-- Elegant Soft Shadow -->
    <filter id="hero-shadow" x="-10%" y="-10%" width="125%" height="125%">
      <feDropShadow dx="0" dy="12" stdDeviation="18" flood-color="#000000" flood-opacity="0.45"/>
    </filter>
  </defs>

  <!-- Base Background -->
  <rect width="{width}" height="{height}" fill="url(#slate-bg)" />
  <rect width="{width}" height="{height}" fill="url(#warm-glow)" />

  <!-- Subtle Minimal Coordinate Lines (Left area pristine for desktop icons) -->
  <g stroke="#483F43" stroke-width="1" opacity="0.4">
    <line x1="{width*0.08}" y1="0" x2="{width*0.08}" y2="{height}" stroke-dasharray="2,16" />
    <line x1="{width*0.22}" y1="0" x2="{width*0.22}" y2="{height}" stroke-dasharray="2,24" />
    <line x1="0" y1="{height*0.86}" x2="{width}" y2="{height*0.86}" stroke-dasharray="2,20" />
    <circle cx="{width*0.08}" cy="{height*0.86}" r="3" fill="#6A5E64" />
    <circle cx="{width*0.22}" cy="{height*0.86}" r="2" fill="#6A5E64" />
  </g>

  <!-- Right Geometric Compositions -->
  <!-- Layer 1: Translucent background geometry -->
  <path d="M {width*0.52} 0 L {width} 0 L {width} {height*0.80} L {width*0.68} {height*0.58} Z" 
        fill="url(#orange-translucent)" />

  <!-- Layer 2: Faceted architectural planes -->
  <polygon points="{width*0.64},{height*0.14} {width*0.94},{height*0.08} {width*0.86},{height*0.68} {width*0.56},{height*0.48}"
           fill="url(#dark-facet)" stroke="#5A4E53" stroke-width="1" />

  <polygon points="{width*0.70},{height*0.22} {width*0.96},{height*0.26} {width*0.86},{height*0.74} {width*0.64},{height*0.60}"
           fill="#382F33" fill-opacity="0.85" stroke="#50454A" stroke-width="1.5" />

  <!-- Layer 3: Ubuntu Orange Hero Ribbon & Facets -->
  <polygon points="{width*0.68},{height*0.34} {width*0.86},{height*0.22} {width*0.80},{height*0.64}"
           fill="url(#orange-primary)" filter="url(#hero-shadow)" />

  <polygon points="{width*0.68},{height*0.34} {width*0.80},{height*0.64} {width*0.63},{height*0.58}"
           fill="url(#orange-deep)" />

  <polygon points="{width*0.80},{height*0.64} {width*0.88},{height*0.74} {width*0.73},{height*0.80} {width*0.71},{height*0.68}"
           fill="#E95420" fill-opacity="0.85" />

  <!-- Layer 4: Modernized Minimal Ubuntu Emblem Motif -->
  <g transform="translate({width*0.76}, {height*0.48})">
    <!-- Outer ring with dash gaps -->
    <circle cx="0" cy="0" r="115" fill="none" stroke="#251F22" stroke-width="14"/>
    <circle cx="0" cy="0" r="115" fill="none" stroke="#E95420" stroke-width="10" stroke-dasharray="170 35 170 35 170 35" stroke-linecap="round"/>

    <!-- Three focal modern geometric nodes -->
    <circle cx="-115" cy="0" r="16" fill="#E95420" stroke="#251F22" stroke-width="4" />
    <circle cx="58" cy="-99" r="16" fill="#E95420" stroke="#251F22" stroke-width="4" />
    <circle cx="58" cy="99" r="16" fill="#E95420" stroke="#251F22" stroke-width="4" />

    <!-- Center node -->
    <circle cx="0" cy="0" r="44" fill="#251F22"/>
    <circle cx="0" cy="0" r="28" fill="#E95420" />
  </g>

  <!-- Delicate accent highlight lines -->
  <line x1="{width*0.63}" y1="{height*0.58}" x2="{width*0.96}" y2="{height*0.26}" stroke="#FFA07A" stroke-width="1.8" stroke-linecap="round" opacity="0.6" />
  <line x1="{width*0.68}" y1="{height*0.34}" x2="{width*0.58}" y2="{height*0.78}" stroke="#E95420" stroke-width="1.5" stroke-dasharray="4,10" opacity="0.4" />

  <!-- Subtle Brand Signature at Bottom Right -->
  <g transform="translate({width*0.87}, {height*0.94})" font-family="'Ubuntu', 'Ubuntu Sans', 'Noto Sans', sans-serif">
    <text x="0" y="0" font-size="20" font-weight="700" fill="#E0DCD8" opacity="0.45" letter-spacing="3">UBUNTU</text>
    <text x="110" y="0" font-size="20" font-weight="300" fill="#E95420" opacity="0.80" letter-spacing="3">CINNAMON</text>
    <text x="0" y="24" font-size="11" font-weight="400" fill="#A8A09A" opacity="0.35" letter-spacing="1.5">PROFESSIONAL EDITION</text>
  </g>

</svg>
"""
    return svg

def generate_warm_stone_wallpaper_svg(width=3840, height=2160):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <!-- Soft Warm Stone / Silk Background (Muted, warm, gentle on the eyes) -->
    <linearGradient id="stone-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#DCD7D1" />
      <stop offset="50%" stop-color="#D2CCC5" />
      <stop offset="100%" stop-color="#C5BFB7" />
    </linearGradient>

    <radialGradient id="warm-stone-glow" cx="80%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#F2EDE7" stop-opacity="0.5" />
      <stop offset="60%" stop-color="#D8D2CA" stop-opacity="0.2" />
      <stop offset="100%" stop-color="#C5BFB7" stop-opacity="0" />
    </radialGradient>

    <linearGradient id="stone-orange" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF6836" />
      <stop offset="100%" stop-color="#C74010" />
    </linearGradient>
  </defs>

  <!-- Base Warm Stone Background -->
  <rect width="{width}" height="{height}" fill="url(#stone-bg)" />
  <rect width="{width}" height="{height}" fill="url(#warm-stone-glow)" />

  <!-- Subtle Coordinate Lines -->
  <g stroke="#BAB3AA" stroke-width="1" opacity="0.5">
    <line x1="{width*0.08}" y1="0" x2="{width*0.08}" y2="{height}" stroke-dasharray="2,16" />
    <line x1="{width*0.22}" y1="0" x2="{width*0.22}" y2="{height}" stroke-dasharray="2,24" />
    <line x1="0" y1="{height*0.86}" x2="{width}" y2="{height*0.86}" stroke-dasharray="2,20" />
  </g>

  <!-- Right Geometric Compositions -->
  <polygon points="{width*0.64},{height*0.14} {width*0.94},{height*0.08} {width*0.86},{height*0.68} {width*0.56},{height*0.48}"
           fill="#BBB4AB" fill-opacity="0.6" stroke="#AAA298" stroke-width="1" />

  <polygon points="{width*0.70},{height*0.22} {width*0.96},{height*0.26} {width*0.86},{height*0.74} {width*0.64},{height*0.60}"
           fill="#E8E3DD" fill-opacity="0.8" stroke="#CBC4BC" stroke-width="1.5" />

  <!-- Orange Ribbon -->
  <polygon points="{width*0.68},{height*0.34} {width*0.86},{height*0.22} {width*0.80},{height*0.64}"
           fill="url(#stone-orange)" />

  <polygon points="{width*0.68},{height*0.34} {width*0.80},{height*0.64} {width*0.63},{height*0.58}"
           fill="#A8350A" />

  <!-- Minimal Ubuntu Emblem -->
  <g transform="translate({width*0.76}, {height*0.48})">
    <circle cx="0" cy="0" r="115" fill="none" stroke="#EAE5DF" stroke-width="14"/>
    <circle cx="0" cy="0" r="115" fill="none" stroke="#E95420" stroke-width="10" stroke-dasharray="170 35 170 35 170 35" stroke-linecap="round"/>
    <circle cx="-115" cy="0" r="16" fill="#E95420" stroke="#EAE5DF" stroke-width="4" />
    <circle cx="58" cy="-99" r="16" fill="#E95420" stroke="#EAE5DF" stroke-width="4" />
    <circle cx="58" cy="99" r="16" fill="#E95420" stroke="#EAE5DF" stroke-width="4" />
    <circle cx="0" cy="0" r="44" fill="#EAE5DF"/>
    <circle cx="0" cy="0" r="28" fill="#E95420" />
  </g>

  <!-- Typography -->
  <g transform="translate({width*0.87}, {height*0.94})" font-family="'Ubuntu', 'Ubuntu Sans', 'Noto Sans', sans-serif">
    <text x="0" y="0" font-size="20" font-weight="700" fill="#2E282A" opacity="0.65" letter-spacing="3">UBUNTU</text>
    <text x="110" y="0" font-size="20" font-weight="300" fill="#E95420" opacity="0.9" letter-spacing="3">CINNAMON</text>
    <text x="0" y="24" font-size="11" font-weight="400" fill="#58514C" opacity="0.5" letter-spacing="1.5">WARM STONE EDITION</text>
  </g>

</svg>
"""
    return svg

# Write SVGs
os.makedirs("wallpapers", exist_ok=True)
with open("wallpapers/ubuntu-cinnamon-elegant-slate.svg", "w") as f:
    f.write(generate_slate_wallpaper_svg(3840, 2160))

with open("wallpapers/ubuntu-cinnamon-warm-stone.svg", "w") as f:
    f.write(generate_warm_stone_wallpaper_svg(3840, 2160))

# Also update the default SVG
with open("wallpapers/ubuntu-cinnamon-minimal-light.svg", "w") as f:
    f.write(generate_slate_wallpaper_svg(3840, 2160))

print("Created wallpaper SVGs successfully")
