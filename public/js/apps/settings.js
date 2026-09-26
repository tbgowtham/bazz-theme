// Settings & Shell Customization Center
class ShellSettings {
  constructor(containerEl) {
    this.container = containerEl;
    this.render();
  }

  render() {
    this.container.innerHTML = `
      <div class="settings-body">
        <div class="settings-nav">
          <div class="settings-nav-item active" data-tab="appearance">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a10 10 0 0 0 0 20z"/></svg>
            <span>Appearance</span>
          </div>
          <div class="settings-nav-item" data-tab="stark">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
            <span>Stark Protocols</span>
          </div>
          <div class="settings-nav-item" data-tab="cinnamon">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18"/></svg>
            <span>Linux Cinnamon</span>
          </div>
          <div class="settings-nav-item" data-tab="about">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
            <span>About Shell</span>
          </div>
        </div>

        <div class="settings-content-pane" id="settings-tab-content">
          <!-- Appearance Tab -->
          <div class="settings-group">
            <div class="settings-group-title">THEME & COLOR MATRIX</div>
            
            <div class="settings-row">
              <div class="settings-row-info">
                <span class="settings-row-label">Stark OS Visual Profile</span>
                <span class="settings-row-desc">Switch between J.A.R.V.I.S. Cyan, F.R.I.D.A.Y. Crimson, or Titanium Gold</span>
              </div>
              <select id="theme-selector" style="background: rgba(8,14,24,0.9); color: var(--accent-cyan); border: 1px solid var(--accent-cyan); padding: 6px 12px; border-radius: 6px; outline: none;">
                <option value="jarvis">J.A.R.V.I.S. (Cyan Neon)</option>
                <option value="friday">F.R.I.D.A.Y. (Hot Rod Crimson)</option>
                <option value="titanium">Titanium Mark XXI (Gold)</option>
              </select>
            </div>

            <div class="settings-row">
              <div class="settings-row-info">
                <span class="settings-row-label">Taskbar Alignment</span>
                <span class="settings-row-desc">Windows 11 Centered Dock or Left-aligned Classic</span>
              </div>
              <button class="start-section-btn" id="taskbar-align-toggle">Centered (Win 11)</button>
            </div>

            <div class="settings-row">
              <div class="settings-row-info">
                <span class="settings-row-label">Desktop Arc Reactor Hologram</span>
                <span class="settings-row-desc">Show dynamic spinning arc-reactor core on the desktop</span>
              </div>
              <button class="start-section-btn" id="arc-toggle-btn">Enabled</button>
            </div>

            <div class="settings-row">
              <div class="settings-row-info">
                <span class="settings-row-label">Holographic HUD Telemetry</span>
                <span class="settings-row-desc">Toggle top-right armor and system metrics overlays</span>
              </div>
              <button class="start-section-btn" id="hud-toggle-btn">Enabled</button>
            </div>
          </div>

          <div class="settings-group">
            <div class="settings-group-title">AUDIO & SYNTHESIS</div>
            <div class="settings-row">
              <div class="settings-row-info">
                <span class="settings-row-label">Web Audio Sci-Fi Sound FX</span>
                <span class="settings-row-desc">Synthesized interface clicks, window opens, and chimes</span>
              </div>
              <button class="start-section-btn" id="sound-toggle-btn">Sound: ON</button>
            </div>
          </div>
        </div>
      </div>
    `;

    this.bindEvents();
  }

  bindEvents() {
    const themeSel = this.container.querySelector('#theme-selector');
    themeSel.addEventListener('change', (e) => {
      const val = e.target.value;
      if (val === 'friday') {
        document.body.className = 'theme-friday';
        if (window.arcReactor) window.arcReactor.setTheme(true, false);
      } else if (val === 'titanium') {
        document.body.className = 'theme-titanium';
        if (window.arcReactor) window.arcReactor.setTheme(false, true);
      } else {
        document.body.className = '';
        if (window.arcReactor) window.arcReactor.setTheme(false, false);
      }
      if (window.soundFX) window.soundFX.playClick();
    });

    const alignBtn = this.container.querySelector('#taskbar-align-toggle');
    alignBtn.addEventListener('click', () => {
      const centerBox = document.querySelector('.taskbar-center');
      if (centerBox.style.position === 'relative') {
        centerBox.style.position = 'absolute';
        centerBox.style.left = '50%';
        centerBox.style.transform = 'translateX(-50%)';
        alignBtn.textContent = 'Centered (Win 11)';
      } else {
        centerBox.style.position = 'relative';
        centerBox.style.left = '0';
        centerBox.style.transform = 'none';
        alignBtn.textContent = 'Left Aligned';
      }
      if (window.soundFX) window.soundFX.playClick();
    });

    const arcBtn = this.container.querySelector('#arc-toggle-btn');
    arcBtn.addEventListener('click', () => {
      const arcCanvas = document.getElementById('arc-canvas');
      if (arcCanvas.style.display === 'none') {
        arcCanvas.style.display = 'block';
        arcBtn.textContent = 'Enabled';
      } else {
        arcCanvas.style.display = 'none';
        arcBtn.textContent = 'Disabled';
      }
      if (window.soundFX) window.soundFX.playClick();
    });

    const hudBtn = this.container.querySelector('#hud-toggle-btn');
    hudBtn.addEventListener('click', () => {
      const hud = document.getElementById('hud-system-telemetry');
      if (hud.style.display === 'none') {
        hud.style.display = 'block';
        hudBtn.textContent = 'Enabled';
      } else {
        hud.style.display = 'none';
        hudBtn.textContent = 'Disabled';
      }
      if (window.soundFX) window.soundFX.playClick();
    });

    const soundBtn = this.container.querySelector('#sound-toggle-btn');
    soundBtn.addEventListener('click', () => {
      if (window.soundFX) {
        window.soundFX.enabled = !window.soundFX.enabled;
        soundBtn.textContent = `Sound: ${window.soundFX.enabled ? 'ON' : 'OFF'}`;
      }
    });

    // Nav Tabs
    const navItems = this.container.querySelectorAll('.settings-nav-item');
    navItems.forEach(item => {
      item.addEventListener('click', () => {
        navItems.forEach(i => i.classList.remove('active'));
        item.classList.add('active');
        const tab = item.dataset.tab;
        this.renderTab(tab);
        if (window.soundFX) window.soundFX.playClick();
      });
    });
  }

  renderTab(tab) {
    const pane = this.container.querySelector('#settings-tab-content');
    if (tab === 'appearance') {
      this.render();
    } else if (tab === 'cinnamon') {
      pane.innerHTML = `
        <div class="settings-group">
          <div class="settings-group-title">LINUX CINNAMON SHELL THEME SUITE</div>
          <div style="font-size: 13px; line-height: 1.5; color: #cbd5e1;">
            This project provides native desktop shell files for <strong>Linux Cinnamon</strong> located in <code>cinnamon/cinnamon.css</code>.
            It provides:
            <ul style="margin: 8px 0 12px 20px;">
              <li>Windows 11 Centered Panel & Floating Applet Dock</li>
              <li>Frosted Glass Acrylic Start Menu (Cinnamon Menu Applet)</li>
              <li>Stark Cyberpunk Cyan & Gold Accent styling</li>
              <li>High-resolution Cockpit & Arc Reactor wallpapers</li>
            </ul>
          </div>
          <div class="settings-row">
            <div class="settings-row-info">
              <span class="settings-row-label">Target Installation Directory</span>
              <span class="settings-row-desc">~/.themes/Jarvis-Windows11-Shell/cinnamon</span>
            </div>
            <button class="start-section-btn" onclick="alert('Run ./apply.sh in the terminal to deploy to Cinnamon!')">Deploy Script</button>
          </div>
        </div>
      `;
    } else if (tab === 'stark') {
      pane.innerHTML = `
        <div class="settings-group">
          <div class="settings-group-title">STARK INDUSTRIES COMBAT PROTOCOLS</div>
          <div class="settings-row">
            <div class="settings-row-info">
              <span class="settings-row-label">Protocol: "House Party"</span>
              <span class="settings-row-desc">Remote nanotech reserve drone assembly</span>
            </div>
            <button class="start-section-btn" onclick="alert('Protocol House Party Authorized.')">Authorize</button>
          </div>
          <div class="settings-row">
            <div class="settings-row-info">
              <span class="settings-row-label">Flight Ceiling Limiter</span>
              <span class="settings-row-desc">Currently set to 85,000 FT (Orbital threshold)</span>
            </div>
            <span style="font-family: var(--font-mono); color: var(--accent-cyan);">85,000 FT</span>
          </div>
        </div>
      `;
    } else if (tab === 'about') {
      pane.innerHTML = `
        <div class="settings-group">
          <div class="settings-group-title">ABOUT STARK OS // J.A.R.V.I.S. SHELL</div>
          <div style="font-size: 12px; line-height: 1.6; color: #94a3b8; font-family: var(--font-mono);">
            PROJECT: J.A.R.V.I.S. & F.R.I.D.A.Y. Windows 11 Desktop Shell<br>
            VERSION: 8.5.2 (Fedora 44 / Wayland & Cinnamon Edition)<br>
            CHASSIS: MARK LXXXV Nanotech Combat Chassis<br>
            ENGINEER: Tony Stark & MR_Gray<br>
            LICENSE: MIT License // Stark Open Source Initiative
          </div>
        </div>
      `;
    }
  }
}

window.ShellSettings = ShellSettings;
