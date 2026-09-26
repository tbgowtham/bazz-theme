// Live Linux Telemetry & Stark Diagnostics Monitor
class SystemMonitor {
  constructor(containerEl) {
    this.container = containerEl;
    this.cpuHistory = new Array(30).fill(10);
    this.memHistory = new Array(30).fill(45);
    this.timer = null;

    this.render();
    this.startPolling();
  }

  render() {
    this.container.innerHTML = `
      <div class="diagnostics-body">
        <div class="metrics-overview-grid">
          <div class="metric-card">
            <span class="metric-card-title">ARC CORE OUTPUT</span>
            <span class="metric-card-val" id="diag-arc-output">3.42 GW</span>
            <span class="metric-card-sub" id="diag-arc-status">STABLE // 99.9%</span>
          </div>
          <div class="metric-card">
            <span class="metric-card-title">CPU UTILIZATION</span>
            <span class="metric-card-val" id="diag-cpu-val">--%</span>
            <span class="metric-card-sub" id="diag-cpu-cores">8 CORES</span>
          </div>
          <div class="metric-card">
            <span class="metric-card-title">MEMORY ALLOCATION</span>
            <span class="metric-card-val" id="diag-mem-val">--%</span>
            <span class="metric-card-sub" id="diag-mem-used">-- GB / -- GB</span>
          </div>
          <div class="metric-card">
            <span class="metric-card-title">ARMOR INTEGRITY</span>
            <span class="metric-card-val" style="color: var(--accent-green);">100%</span>
            <span class="metric-card-sub">NANOTECH ACTIVE</span>
          </div>
        </div>

        <div class="diagnostics-charts-grid">
          <div class="chart-panel">
            <div class="chart-panel-header">REAL-TIME CPU TELEMETRY (ROLLING 30s)</div>
            <canvas class="canvas-chart" id="cpu-chart" width="300" height="120"></canvas>
          </div>
          <div class="chart-panel">
            <div class="chart-panel-header">MEMORY CONSUMPTION MATRIX</div>
            <canvas class="canvas-chart" id="mem-chart" width="300" height="120"></canvas>
          </div>
        </div>

        <div class="chart-panel">
          <div class="chart-panel-header">STARK INDUSTRIES KINETIC & FLIGHT READOUT</div>
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-top: 8px; font-family: var(--font-mono); font-size: 11px;">
            <div style="background: rgba(255,255,255,0.03); padding: 8px; border-radius: 6px;">
              <span style="color: var(--text-muted);">FLIGHT ALTITUDE:</span>
              <div style="color: var(--accent-cyan); font-weight: 700; font-size: 14px;">12,500 FT [MACH 2.8]</div>
            </div>
            <div style="background: rgba(255,255,255,0.03); padding: 8px; border-radius: 6px;">
              <span style="color: var(--text-muted);">HOST PLATFORM:</span>
              <div style="color: var(--accent-cyan); font-weight: 700; font-size: 14px;" id="diag-host">FEDORA LINUX</div>
            </div>
            <div style="background: rgba(255,255,255,0.03); padding: 8px; border-radius: 6px;">
              <span style="color: var(--text-muted);">SYSTEM UPTIME:</span>
              <div style="color: var(--accent-cyan); font-weight: 700; font-size: 14px;" id="diag-uptime">0h 0m</div>
            </div>
          </div>
        </div>
      </div>
    `;

    this.cpuCanvas = this.container.querySelector('#cpu-chart');
    this.memCanvas = this.container.querySelector('#mem-chart');
  }

  async fetchTelemetry() {
    try {
      const res = await fetch('/api/telemetry');
      const data = await res.json();

      this.cpuHistory.shift();
      this.cpuHistory.push(data.cpu.usagePercent);

      this.memHistory.shift();
      this.memHistory.push(data.memory.usedPercent);

      this.container.querySelector('#diag-cpu-val').textContent = `${data.cpu.usagePercent}%`;
      this.container.querySelector('#diag-cpu-cores').textContent = `${data.cpu.cores} CORES (${data.cpu.speedMHz} MHz)`;

      this.container.querySelector('#diag-mem-val').textContent = `${data.memory.usedPercent}%`;
      this.container.querySelector('#diag-mem-used').textContent = `${data.memory.usedGB} GB / ${data.memory.totalGB} GB`;

      this.container.querySelector('#diag-host').textContent = `${data.system.hostname} (${data.system.arch})`;
      this.container.querySelector('#diag-uptime').textContent = data.system.uptimeFormatted;

      // Update Desktop Top-Right HUD as well
      const topCpuBar = document.querySelector('#hud-cpu-bar');
      const topCpuVal = document.querySelector('#hud-cpu-val');
      const topMemBar = document.querySelector('#hud-mem-bar');
      const topMemVal = document.querySelector('#hud-mem-val');

      if (topCpuBar) topCpuBar.style.width = `${data.cpu.usagePercent}%`;
      if (topCpuVal) topCpuVal.textContent = `${data.cpu.usagePercent}%`;
      if (topMemBar) topMemBar.style.width = `${data.memory.usedPercent}%`;
      if (topMemVal) topMemVal.textContent = `${data.memory.usedGB}G / ${data.memory.totalGB}G`;

    } catch {
      // Simulate live random fluctuation if server is detached
      const rCpu = Math.floor(10 + Math.random() * 25);
      const rMem = Math.floor(48 + Math.random() * 8);
      this.cpuHistory.shift();
      this.cpuHistory.push(rCpu);
      this.memHistory.shift();
      this.memHistory.push(rMem);

      const cpuEl = this.container.querySelector('#diag-cpu-val');
      if (cpuEl) cpuEl.textContent = `${rCpu}%`;
      const memEl = this.container.querySelector('#diag-mem-val');
      if (memEl) memEl.textContent = `${rMem}%`;
    }

    this.drawChart(this.cpuCanvas, this.cpuHistory, '#00e5ff');
    this.drawChart(this.memCanvas, this.memHistory, '#0088ff');
  }

  drawChart(canvas, history, color) {
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width = canvas.parentElement.clientWidth - 28;
    const h = canvas.height = 120;

    ctx.clearRect(0, 0, w, h);

    // Grid lines
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.06)';
    ctx.lineWidth = 1;
    for (let y = 0; y < h; y += 30) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(w, y);
      ctx.stroke();
    }

    // Graph Line
    ctx.strokeStyle = color;
    ctx.lineWidth = 2;
    ctx.shadowColor = color;
    ctx.shadowBlur = 8;
    ctx.beginPath();

    const step = w / (history.length - 1);
    for (let i = 0; i < history.length; i++) {
      const x = i * step;
      const y = h - (history[i] / 100) * (h - 10) - 5;
      if (i === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();

    // Area Fill
    ctx.lineTo(w, h);
    ctx.lineTo(0, h);
    ctx.closePath();
    const grad = ctx.createLinearGradient(0, 0, 0, h);
    grad.addColorStop(0, color.replace(')', ', 0.25)').replace('rgb', 'rgba'));
    grad.addColorStop(1, 'transparent');
    ctx.fillStyle = grad;
    ctx.shadowBlur = 0;
    ctx.fill();
  }

  startPolling() {
    this.fetchTelemetry();
    this.timer = setInterval(() => this.fetchTelemetry(), 1500);
  }

  destroy() {
    if (this.timer) clearInterval(this.timer);
  }
}

window.SystemMonitor = SystemMonitor;
