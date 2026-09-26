import os

def generate_macos_ubuntu_wave_svg(width=3840, height=2160):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <!-- Deep Velvety Slate / Aubergine Backdrop -->
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#241E22" />
      <stop offset="50%" stop-color="#1B161A" />
      <stop offset="100%" stop-color="#131012" />
    </linearGradient>

    <!-- Warm Atmospheric Glow behind waves -->
    <radialGradient id="glow-ambient" cx="75%" cy="55%" r="65%">
      <stop offset="0%" stop-color="#5E2B25" stop-opacity="0.45" />
      <stop offset="45%" stop-color="#3A1D28" stop-opacity="0.25" />
      <stop offset="100%" stop-color="#131012" stop-opacity="0" />
    </radialGradient>

    <!-- macOS Wave Ribbon Gradients -->
    <!-- Ribbon 1: Deep Aubergine / Wine -->
    <linearGradient id="wave-wine" x1="10%" y1="10%" x2="90%" y2="90%">
      <stop offset="0%" stop-color="#6E2842" />
      <stop offset="50%" stop-color="#4E1A30" />
      <stop offset="100%" stop-color="#2A0F1B" />
    </linearGradient>

    <!-- Ribbon 2: Glowing Ubuntu Orange Primary Wave -->
    <linearGradient id="wave-orange-main" x1="0%" y1="20%" x2="100%" y2="80%">
      <stop offset="0%" stop-color="#FF7544" />
      <stop offset="45%" stop-color="#E95420" />
      <stop offset="85%" stop-color="#BA3A0A" />
      <stop offset="100%" stop-color="#732004" />
    </linearGradient>

    <!-- Ribbon 3: Amber / Warm Peach Accent Wave -->
    <linearGradient id="wave-amber" x1="20%" y1="0%" x2="80%" y2="100%">
      <stop offset="0%" stop-color="#FFA87D" />
      <stop offset="50%" stop-color="#FF6A38" />
      <stop offset="100%" stop-color="#C74010" />
    </linearGradient>

    <!-- Ribbon 4: Translucent Dark Glass Wave -->
    <linearGradient id="wave-dark-glass" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#463740" stop-opacity="0.6" />
      <stop offset="60%" stop-color="#261E23" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#191316" stop-opacity="0.9" />
    </linearGradient>

    <!-- macOS Specular Edge Highlights -->
    <linearGradient id="specular-line" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.8" />
      <stop offset="40%" stop-color="#FFB394" stop-opacity="0.5" />
      <stop offset="100%" stop-color="#E95420" stop-opacity="0" />
    </linearGradient>

    <!-- Dimensional Drop Shadows -->
    <filter id="shadow-deep" x="-15%" y="-15%" width="130%" height="130%">
      <feDropShadow dx="-10" dy="25" stdDeviation="30" flood-color="#000000" flood-opacity="0.65"/>
    </filter>
    <filter id="shadow-medium" x="-15%" y="-15%" width="130%" height="130%">
      <feDropShadow dx="-5" dy="18" stdDeviation="20" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <!-- Base Smooth Background -->
  <rect width="{width}" height="{height}" fill="url(#bg-grad)" />
  <rect width="{width}" height="{height}" fill="url(#glow-ambient)" />

  <!-- macOS Sweeping Waves (Layered Organic Bezier Ribbons) -->
  
  <!-- Wave Layer 1: Back Deep Wine Wave -->
  <path d="M {width*0.42} {height} 
           C {width*0.50} {height*0.65}, {width*0.62} {height*0.35}, {width*0.82} {height*0.18}
           C {width*0.92} {height*0.08}, {width*0.98} {height*0.05}, {width} 0
           L {width} {height} Z" 
        fill="url(#wave-wine)" />

  <!-- Wave Layer 2: Translucent Glass Contour Wave -->
  <path d="M {width*0.48} {height} 
           C {width*0.54} {height*0.72}, {width*0.65} {height*0.48}, {width*0.80} {height*0.28}
           C {width*0.90} {height*0.16}, {width*0.96} {height*0.12}, {width} {height*0.08}
           L {width} {height} Z" 
        fill="url(#wave-dark-glass)" filter="url(#shadow-deep)" />

  <!-- Wave Layer 3: Ubuntu Orange Hero Wave (Curved, silky, majestic) -->
  <path d="M {width*0.55} {height} 
           C {width*0.60} {height*0.78}, {width*0.68} {height*0.54}, {width*0.82} {height*0.36}
           C {width*0.92} {height*0.22}, {width*0.97} {height*0.18}, {width} {height*0.15}
           L {width} {height*0.82}
           C {width*0.92} {height*0.84}, {width*0.80} {height*0.88}, {width*0.70} {height} Z" 
        fill="url(#wave-orange-main)" filter="url(#shadow-deep)" />

  <!-- Wave Layer 4: Upper Amber Wave Crest -->
  <path d="M {width*0.62} {height} 
           C {width*0.68} {height*0.82}, {width*0.76} {height*0.64}, {width*0.86} {height*0.46}
           C {width*0.94} {height*0.32}, {width*0.98} {height*0.26}, {width} {height*0.24}
           L {width} {height*0.45}
           C {width*0.92} {height*0.52}, {width*0.82} {height*0.66}, {width*0.74} {height*0.82} Z" 
        fill="url(#wave-amber)" filter="url(#shadow-medium)" />

  <!-- Specular Light Lines (macOS Glass Edge Detail) -->
  <path d="M {width*0.55} {height} 
           C {width*0.60} {height*0.78}, {width*0.68} {height*0.54}, {width*0.82} {height*0.36}
           C {width*0.92} {height*0.22}, {width*0.97} {height*0.18}, {width} {height*0.15}"
        fill="none" stroke="url(#specular-line)" stroke-width="2.5" stroke-linecap="round" />

  <path d="M {width*0.62} {height} 
           C {width*0.68} {height*0.82}, {width*0.76} {height*0.64}, {width*0.86} {height*0.46}
           C {width*0.94} {height*0.32}, {width*0.98} {height*0.26}, {width} {height*0.24}"
        fill="none" stroke="#FFFFFF" stroke-opacity="0.7" stroke-width="1.8" stroke-linecap="round" />

  <!-- Minimal Elegant Brand Typography (Bottom Right) -->
  <g transform="translate({width*0.88}, {height*0.95})" font-family="-apple-system, BlinkMacSystemFont, 'Ubuntu', 'SF Pro Display', sans-serif">
    <text x="0" y="0" font-size="18" font-weight="600" fill="#E8E4DF" opacity="0.6" letter-spacing="4">UBUNTU</text>
    <text x="105" y="0" font-size="18" font-weight="300" fill="#E95420" opacity="0.9" letter-spacing="4">CINNAMON</text>
    <text x="0" y="22" font-size="10" font-weight="400" fill="#9C958F" opacity="0.4" letter-spacing="2">MACOS ELEGANCE EDITION</text>
  </g>

</svg>
"""
    return svg

with open("wallpapers/ubuntu-cinnamon-macos-wave.svg", "w") as f:
    f.write(generate_macos_ubuntu_wave_svg(3840, 2160))

# Also set as default wallpapers
with open("wallpapers/ubuntu-cinnamon-minimal-light.svg", "w") as f:
    f.write(generate_macos_ubuntu_wave_svg(3840, 2160))

print("Created macOS Ubuntu Wave wallpaper SVG successfully")
