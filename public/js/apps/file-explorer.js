// Windows 11 Style Holographic File Explorer
class FileExplorer {
  constructor(containerEl) {
    this.container = containerEl;
    this.currentPath = 'C:\\StarkIndustries\\Mark85';
    this.fileSystem = {
      'C:\\StarkIndustries\\Mark85': [
        { name: 'Schematics', type: 'folder', items: 4 },
        { name: 'TelemetryLogs', type: 'folder', items: 12 },
        { name: 'cinnamon-theme', type: 'folder', items: 3 },
        { name: 'arc_reactor_v8.cad', type: 'model', size: '14.2 MB' },
        { name: 'jarvis_neural_weights.bin', type: 'code', size: '840 MB' },
        { name: 'nanotech_suit_deploy.sh', type: 'sh', size: '3.4 KB' },
        { name: 'mission_log_active.txt', type: 'text', size: '1.2 KB' }
      ],
      'C:\\StarkIndustries\\Mark85\\Schematics': [
        { name: 'mark_85_flight_stabilizer.dxf', type: 'model', size: '4.8 MB' },
        { name: 'unibeam_quantum_focus.svg', type: 'image', size: '210 KB' },
        { name: 'repulsor_emitter_matrix.dxf', type: 'model', size: '6.1 MB' }
      ],
      'C:\\StarkIndustries\\Mark85\\cinnamon-theme': [
        { name: 'cinnamon.css', type: 'code', size: '18.4 KB' },
        { name: 'metadata.json', type: 'code', size: '1.1 KB' },
        { name: 'apply.sh', type: 'sh', size: '4.6 KB' }
      ],
      'C:\\StarkIndustries\\Mark85\\TelemetryLogs': [
        { name: 'flight_test_mach3.log', type: 'text', size: '48 KB' },
        { name: 'orbital_thermal_stress.log', type: 'text', size: '82 KB' },
        { name: 'reactor_harmonic_test.log', type: 'text', size: '19 KB' }
      ]
    };

    this.render();
  }

  render() {
    this.container.innerHTML = `
      <div class="explorer-body">
        <div class="explorer-toolbar">
          <button class="explorer-nav-btn" id="nav-back">◀</button>
          <button class="explorer-nav-btn" id="nav-up">▲</button>
          <div class="explorer-path-bar" id="explorer-path">${this.currentPath}</div>
        </div>
        <div class="explorer-split">
          <div class="explorer-sidebar">
            <div class="sidebar-folder-item active" data-path="C:\\StarkIndustries\\Mark85">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg>
              <span>Mark 85 Root</span>
            </div>
            <div class="sidebar-folder-item" data-path="C:\\StarkIndustries\\Mark85\\Schematics">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
              <span>Schematics</span>
            </div>
            <div class="sidebar-folder-item" data-path="C:\\StarkIndustries\\Mark85\\cinnamon-theme">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18"/></svg>
              <span>Cinnamon Theme</span>
            </div>
            <div class="sidebar-folder-item" data-path="C:\\StarkIndustries\\Mark85\\TelemetryLogs">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
              <span>Telemetry Logs</span>
            </div>
          </div>
          <div class="explorer-file-view" id="file-grid"></div>
        </div>
      </div>
    `;

    this.renderFiles();
    this.bindEvents();
  }

  renderFiles() {
    const grid = this.container.querySelector('#file-grid');
    const pathBar = this.container.querySelector('#explorer-path');
    pathBar.textContent = this.currentPath;

    const items = this.fileSystem[this.currentPath] || [];
    grid.innerHTML = items.map(item => `
      <div class="file-item-card" data-name="${item.name}" data-type="${item.type}">
        <div class="file-item-icon">
          ${this.getIcon(item.type)}
        </div>
        <div class="file-item-name">${item.name}</div>
        <div style="font-size: 9px; color: var(--text-muted); font-family: var(--font-mono);">${item.size || item.items + ' items'}</div>
      </div>
    `).join('');
  }

  getIcon(type) {
    switch (type) {
      case 'folder':
        return `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg>`;
      case 'code':
        return `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>`;
      case 'model':
        return `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="4"/></svg>`;
      case 'sh':
        return `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg>`;
      default:
        return `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>`;
    }
  }

  bindEvents() {
    this.container.addEventListener('click', (e) => {
      const sidebarItem = e.target.closest('.sidebar-folder-item');
      if (sidebarItem) {
        this.container.querySelectorAll('.sidebar-folder-item').forEach(el => el.classList.remove('active'));
        sidebarItem.classList.add('active');
        this.currentPath = sidebarItem.dataset.path;
        this.renderFiles();
        if (window.soundFX) window.soundFX.playClick();
        return;
      }

      const fileCard = e.target.closest('.file-item-card');
      if (fileCard) {
        const type = fileCard.dataset.type;
        const name = fileCard.dataset.name;
        if (type === 'folder') {
          const next = `${this.currentPath}\\${name}`;
          if (this.fileSystem[next]) {
            this.currentPath = next;
            this.renderFiles();
          }
        } else {
          // File open preview
          alert(`[STARK SECURITY PROTOCOL]\nViewing encrypted file: ${name}\nClassification: TOP SECRET // AVENGERS CLEARANCE`);
        }
        if (window.soundFX) window.soundFX.playClick();
      }

      const upBtn = e.target.closest('#nav-up');
      if (upBtn) {
        const parts = this.currentPath.split('\\');
        if (parts.length > 2) {
          parts.pop();
          this.currentPath = parts.join('\\');
          this.renderFiles();
          if (window.soundFX) window.soundFX.playClick();
        }
      }
    });
  }
}

window.FileExplorer = FileExplorer;
