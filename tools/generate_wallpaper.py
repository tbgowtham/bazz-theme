import math

def generate_wallpaper_svg(width=3840, height=2160):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <!-- Background Gradients -->
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FCFCFD" />
      <stop offset="60%" stop-color="#F6F7FA" />
      <stop offset="100%" stop-color="#EDEFF4" />
    </linearGradient>

    <radialGradient id="subtle-glow" cx="80%" cy="45%" r="65%">
      <stop offset="0%" stop-color="#FDEEE6" stop-opacity="0.45" />
      <stop offset="50%" stop-color="#FBF2EC" stop-opacity="0.20" />
      <stop offset="100%" stop-color="#F5F6F9" stop-opacity="0" />
    </radialGradient>

    <!-- Ubuntu Orange Accent Gradients -->
    <linearGradient id="orange-primary" x1="20%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF6332" />
      <stop offset="70%" stop-color="#E95420" />
      <stop offset="100%" stop-color="#C74010" />
    </linearGradient>

    <linearGradient id="orange-soft" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFA07A" stop-opacity="0.75" />
      <stop offset="100%" stop-color="#E95420" stop-opacity="0.65" />
    </linearGradient>

    <linearGradient id="orange-translucent" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E95420" stop-opacity="0.15" />
      <stop offset="100%" stop-color="#E95420" stop-opacity="0.03" />
    </linearGradient>

    <linearGradient id="charcoal-plane" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3C3B37" stop-opacity="0.04" />
      <stop offset="100%" stop-color="#2C2C2C" stop-opacity="0.08" />
    </linearGradient>

    <!-- Subtle Drop Shadows (minimal, professional) -->
    <filter id="soft-shadow" x="-5%" y="-5%" width="115%" height="115%">
      <feDropShadow dx="3" dy="6" stdDeviation="10" flood-color="#C74010" flood-opacity="0.15"/>
    </filter>
    <filter id="subtle-card-shadow" x="-5%" y="-5%" width="115%" height="115%">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#000000" flood-opacity="0.04"/>
    </filter>
  </defs>

  <!-- Base Clean Background (White / Off-White) -->
  <rect width="{width}" height="{height}" fill="url(#bg-grad)" />
  <rect width="{width}" height="{height}" fill="url(#subtle-glow)" />

  <!-- Subtle Minimalist Coordinate Grid Lines (Left Area remains pristine for icons) -->
  <g stroke="#E2E4E8" stroke-width="1" opacity="0.6">
    <line x1="{width*0.08}" y1="0" x2="{width*0.08}" y2="{height}" stroke-dasharray="3,12" />
    <line x1="{width*0.20}" y1="0" x2="{width*0.20}" y2="{height}" stroke-dasharray="2,20" />
    <line x1="0" y1="{height*0.88}" x2="{width}" y2="{height*0.88}" stroke-dasharray="2,16" />
    <circle cx="{width*0.08}" cy="{height*0.88}" r="3" fill="#D0D3D9" />
    <circle cx="{width*0.20}" cy="{height*0.88}" r="2" fill="#D0D3D9" />
  </g>

  <!-- Right Geometric Compositions: Clean, Origami-like Facets and Ubuntu Orange Accents -->
  <!-- Layer 1: Translucent background geometry -->
  <path d="M {width*0.55} 0 L {width} 0 L {width} {height*0.75} L {width*0.70} {height*0.55} Z" 
        fill="url(#orange-translucent)" />

  <polygon points="{width*0.62},{height*0.15} {width*0.92},{height*0.08} {width*0.85},{height*0.65} {width*0.58},{height*0.50}"
           fill="url(#charcoal-plane)" />

  <!-- Layer 2: Geometric polygon facets with delicate light borders -->
  <polygon points="{width*0.72},{height*0.20} {width*0.98},{height*0.25} {width*0.88},{height*0.72} {width*0.66},{height*0.58}"
           fill="#FFFFFF" fill-opacity="0.75" stroke="#E5E7EB" stroke-width="1.5" filter="url(#subtle-card-shadow)" />

  <polygon points="{width*0.66},{height*0.58} {width*0.88},{height*0.72} {width*0.80},{height*0.95} {width*0.60},{height*0.78}"
           fill="#F9FAFC" fill-opacity="0.9" stroke="#E5E7EB" stroke-width="1.5" />

  <!-- Layer 3: Ubuntu Orange Hero Ribbon & Geometric Core (Clean #E95420) -->
  <!-- Dynamic triangular ribbon 1 -->
  <polygon points="{width*0.70},{height*0.32} {width*0.86},{height*0.22} {width*0.80},{height*0.62}"
           fill="url(#orange-primary)" filter="url(#soft-shadow)" />

  <!-- Faceted shadow plane of hero ribbon -->
  <polygon points="{width*0.70},{height*0.32} {width*0.80},{height*0.62} {width*0.65},{height*0.56}"
           fill="#C74010" fill-opacity="0.95" />

  <!-- Secondary warm ribbon accent -->
  <polygon points="{width*0.80},{height*0.62} {width*0.88},{height*0.72} {width*0.74},{height*0.78} {width*0.72},{height*0.66}"
           fill="url(#orange-soft)" />

  <!-- Layer 4: Minimal Ubuntu Motif (Circle of Friends Emblem Modernized) -->
  <g transform="translate({width*0.75}, {height*0.48})">
    <!-- Outer delicate ring -->
    <circle cx="0" cy="0" r="110" fill="none" stroke="#FFFFFF" stroke-width="12" filter="url(#subtle-card-shadow)"/>
    <circle cx="0" cy="0" r="110" fill="none" stroke="#E95420" stroke-width="10" stroke-dasharray="160 30 160 30 160 30" stroke-linecap="round"/>

    <!-- Three focal modern geometric nodes -->
    <circle cx="-110" cy="0" r="15" fill="#E95420" stroke="#FFFFFF" stroke-width="4" />
    <circle cx="55" cy="-95" r="15" fill="#E95420" stroke="#FFFFFF" stroke-width="4" />
    <circle cx="55" cy="95" r="15" fill="#E95420" stroke="#FFFFFF" stroke-width="4" />

    <!-- Core circle -->
    <circle cx="0" cy="0" r="42" fill="#FFFFFF" filter="url(#subtle-card-shadow)"/>
    <circle cx="0" cy="0" r="28" fill="#E95420" />
  </g>

  <!-- Crisp Modern Geometric Accent Lines -->
  <line x1="{width*0.65}" y1="{height*0.56}" x2="{width*0.98}" y2="{height*0.25}" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" opacity="0.8" />
  <line x1="{width*0.70}" y1="{height*0.32}" x2="{width*0.60}" y2="{height*0.78}" stroke="#E95420" stroke-width="1.5" stroke-dasharray="4,8" opacity="0.4" />

  <!-- Subtle Ubuntu / Cinnamon Typography Watermark at bottom right (Extremely subtle, 0.25 opacity) -->
  <g transform="translate({width*0.88}, {height*0.94})" font-family="'Ubuntu', 'Ubuntu Sans', 'Noto Sans', 'Segoe UI', sans-serif">
    <text x="0" y="0" font-size="20" font-weight="700" fill="#2C2C2C" opacity="0.30" letter-spacing="3">UBUNTU</text>
    <text x="110" y="0" font-size="20" font-weight="300" fill="#E95420" opacity="0.45" letter-spacing="3">CINNAMON</text>
    <text x="0" y="24" font-size="11" font-weight="400" fill="#666666" opacity="0.25" letter-spacing="1.5">LIGHT EDITION</text>
  </g>

</svg>
"""
    return svg

with open("wallpapers/ubuntu-cinnamon-minimal-light.svg", "w") as f:
    f.write(generate_wallpaper_svg(3840, 2160))

print("Created wallpapers/ubuntu-cinnamon-minimal-light.svg successfully")
