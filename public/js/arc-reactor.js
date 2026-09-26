// Interactive Stark Industries Arc-Reactor Canvas Renderer
class ArcReactor {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.angle1 = 0;
    this.angle2 = 0;
    this.pulse = 0;
    this.particles = [];
    this.intensity = 1.0;
    this.colorCyan = '#00e5ff';
    this.colorBlue = '#0088ff';

    this.resize();
    window.addEventListener('resize', () => this.resize());
    this.initParticles();
    this.animate();
  }

  resize() {
    if (!this.canvas) return;
    this.width = this.canvas.width = 600;
    this.height = this.canvas.height = 600;
    this.cx = this.width / 2;
    this.cy = this.height / 2;
  }

  setTheme(isFriday, isTitanium) {
    if (isFriday) {
      this.colorCyan = '#ff2a5f';
      this.colorBlue = '#ff758f';
    } else if (isTitanium) {
      this.colorCyan = '#ffb703';
      this.colorBlue = '#fb8500';
    } else {
      this.colorCyan = '#00e5ff';
      this.colorBlue = '#0088ff';
    }
  }

  initParticles() {
    this.particles = [];
    for (let i = 0; i < 40; i++) {
      this.particles.push({
        angle: Math.random() * Math.PI * 2,
        radius: 30 + Math.random() * 90,
        speed: 0.5 + Math.random() * 1.5,
        size: 1 + Math.random() * 2,
        alpha: Math.random() * 0.8
      });
    }
  }

  draw() {
    if (!this.ctx) return;
    this.ctx.clearRect(0, 0, this.width, this.height);

    const cx = this.cx;
    const cy = this.cy;
    const p = Math.sin(this.pulse) * 0.15 + 1; // Pulsing factor

    // 1. Outer Ring with Ticks
    this.ctx.save();
    this.ctx.translate(cx, cy);
    this.ctx.rotate(this.angle1);
    this.ctx.strokeStyle = this.colorCyan;
    this.ctx.lineWidth = 2;
    this.ctx.globalAlpha = 0.5;

    this.ctx.beginPath();
    this.ctx.arc(0, 0, 160, 0, Math.PI * 2);
    this.ctx.stroke();

    // Radial tick markers
    for (let i = 0; i < 36; i++) {
      const a = (i * Math.PI) / 18;
      const r1 = i % 3 === 0 ? 150 : 155;
      const r2 = 165;
      this.ctx.beginPath();
      this.ctx.moveTo(Math.cos(a) * r1, Math.sin(a) * r1);
      this.ctx.lineTo(Math.cos(a) * r2, Math.sin(a) * r2);
      this.ctx.stroke();
    }
    this.ctx.restore();

    // 2. Middle segmented ring (counter-rotating)
    this.ctx.save();
    this.ctx.translate(cx, cy);
    this.ctx.rotate(-this.angle2);
    this.ctx.strokeStyle = this.colorBlue;
    this.ctx.lineWidth = 4;
    this.ctx.globalAlpha = 0.7;

    for (let i = 0; i < 8; i++) {
      const start = (i * Math.PI) / 4 + 0.1;
      const end = start + (Math.PI / 4) - 0.2;
      this.ctx.beginPath();
      this.ctx.arc(0, 0, 125, start, end);
      this.ctx.stroke();
    }
    this.ctx.restore();

    // 3. Inner mechanical runic circle
    this.ctx.save();
    this.ctx.translate(cx, cy);
    this.ctx.rotate(this.angle1 * 1.5);
    this.ctx.strokeStyle = this.colorCyan;
    this.ctx.lineWidth = 2;
    this.ctx.globalAlpha = 0.85;

    this.ctx.beginPath();
    this.ctx.arc(0, 0, 95, 0, Math.PI * 2);
    this.ctx.stroke();

    for (let i = 0; i < 12; i++) {
      const a = (i * Math.PI) / 6;
      this.ctx.beginPath();
      this.ctx.arc(Math.cos(a) * 95, Math.sin(a) * 95, 4, 0, Math.PI * 2);
      this.ctx.fillStyle = this.colorCyan;
      this.ctx.fill();
    }
    this.ctx.restore();

    // 4. Center Glowing Arc Core
    const grad = this.ctx.createRadialGradient(cx, cy, 10, cx, cy, 70 * p);
    grad.addColorStop(0, '#ffffff');
    grad.addColorStop(0.3, this.colorCyan);
    grad.addColorStop(0.7, this.colorBlue);
    grad.addColorStop(1, 'transparent');

    this.ctx.save();
    this.ctx.fillStyle = grad;
    this.ctx.beginPath();
    this.ctx.arc(cx, cy, 70 * p, 0, Math.PI * 2);
    this.ctx.fill();
    this.ctx.restore();

    // 5. Plasma particles
    this.ctx.save();
    this.ctx.fillStyle = this.colorCyan;
    this.particles.forEach(pt => {
      pt.radius += pt.speed;
      if (pt.radius > 170) {
        pt.radius = 20;
        pt.angle = Math.random() * Math.PI * 2;
      }
      this.ctx.globalAlpha = (1 - (pt.radius / 170)) * pt.alpha;
      const px = cx + Math.cos(pt.angle) * pt.radius;
      const py = cy + Math.sin(pt.angle) * pt.radius;
      this.ctx.beginPath();
      this.ctx.arc(px, py, pt.size, 0, Math.PI * 2);
      this.ctx.fill();
    });
    this.ctx.restore();
  }

  animate() {
    this.angle1 += 0.008;
    this.angle2 += 0.012;
    this.pulse += 0.04;
    this.draw();
    requestAnimationFrame(() => this.animate());
  }
}

window.ArcReactor = ArcReactor;
