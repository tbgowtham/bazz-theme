// Taskbar Controller for Windows 11 Centered Dock
class TaskbarController {
  constructor() {
    this.pinnedApps = [
      { id: 'terminal', name: 'Mark LXXXV Terminal', icon: this.getTerminalSvg() },
      { id: 'monitor', name: 'Stark Diagnostics', icon: this.getMonitorSvg() },
      { id: 'chat', name: 'J.A.R.V.I.S. Core', icon: this.getJarvisSvg() },
      { id: 'explorer', name: 'File Explorer', icon: this.getExplorerSvg() },
      { id: 'media', name: 'Arc Player', icon: this.getMediaSvg() },
      { id: 'settings', name: 'Shell Settings', icon: this.getSettingsSvg() }
    ];

    this.activeWindowId = null;
    this.runningWindows = new Set();
    this.init();
  }

  init() {
    this.renderPinnedApps();
    this.startClock();
    this.bindEvents();
  }

  renderPinnedApps() {
    const centerContainer = document.querySelector('.taskbar-center');
    if (!centerContainer) return;

    this.pinnedApps.forEach(app => {
      const btn = document.createElement('button');
      btn.className = 'taskbar-item app-icon-btn';
      btn.id = `tb-${app.id}`;
      btn.title = app.name;
      btn.dataset.appId = app.id;
      btn.innerHTML = `
        ${app.icon}
        <div class="taskbar-indicator"></div>
      `;
      btn.addEventListener('click', () => {
        window.app.launchApp(app.id);
        if (window.soundFX) window.soundFX.playClick();
      });
      centerContainer.appendChild(btn);
    });
  }

  startClock() {
    const timeEl = document.querySelector('.clock-time');
    const dateEl = document.querySelector('.clock-date');

    const update = () => {
      const now = new Date();
      const hours = String(now.getHours()).padStart(2, '0');
      const mins = String(now.getMinutes()).padStart(2, '0');
      if (timeEl) timeEl.textContent = `${hours}:${mins}`;

      const day = String(now.getDate()).padStart(2, '0');
      const month = String(now.getMonth() + 1).padStart(2, '0');
      const year = now.getFullYear();
      if (dateEl) dateEl.textContent = `${day}/${month}/${year}`;
    };

    update();
    setInterval(update, 1000);
  }

  onWindowCreated(id) {
    this.runningWindows.add(id);
    const tbBtn = document.getElementById(`tb-${id}`);
    if (tbBtn) {
      tbBtn.classList.add('running');
    }
  }

  setActiveWindow(id) {
    this.activeWindowId = id;
    document.querySelectorAll('.taskbar-item').forEach(el => el.classList.remove('active-window'));
    const tbBtn = document.getElementById(`tb-${id}`);
    if (tbBtn) {
      tbBtn.classList.add('active-window');
      tbBtn.classList.remove('minimized');
    }
  }

  onWindowMinimized(id) {
    const tbBtn = document.getElementById(`tb-${id}`);
    if (tbBtn) {
      tbBtn.classList.remove('active-window');
      tbBtn.classList.add('minimized');
    }
  }

  onWindowClosed(id) {
    this.runningWindows.delete(id);
    const tbBtn = document.getElementById(`tb-${id}`);
    if (tbBtn) {
      tbBtn.classList.remove('running', 'active-window', 'minimized');
    }
  }

  bindEvents() {
    // Start Button
    const startBtn = document.getElementById('start-btn');
    if (startBtn) {
      startBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        window.startMenu.toggle();
        if (window.soundFX) window.soundFX.playClick();
      });
    }

    // Jarvis Quick Button
    const jarvisBtn = document.getElementById('jarvis-quick-btn');
    if (jarvisBtn) {
      jarvisBtn.addEventListener('click', () => {
        window.app.launchApp('chat');
        if (window.soundFX) window.soundFX.playJarvisChime();
      });
    }

    // Task View / Workspaces Button
    const taskViewBtn = document.getElementById('task-view-btn');
    if (taskViewBtn) {
      taskViewBtn.addEventListener('click', () => {
        window.quickSettings.toggleTaskView();
        if (window.soundFX) window.soundFX.playClick();
      });
    }

    // Widgets button (Arc Reactor HUD toggle)
    const widgetsBtn = document.getElementById('widgets-btn');
    if (widgetsBtn) {
      widgetsBtn.addEventListener('click', () => {
        const hud = document.getElementById('hud-system-telemetry');
        const arc = document.getElementById('arc-canvas');
        if (hud) hud.style.display = hud.style.display === 'none' ? 'block' : 'none';
        if (arc) arc.style.display = arc.style.display === 'none' ? 'block' : 'none';
        if (window.soundFX) window.soundFX.playClick();
      });
    }

    // Quick Settings Trigger
    const trayGroup = document.getElementById('tray-quick-settings-trigger');
    if (trayGroup) {
      trayGroup.addEventListener('click', (e) => {
        e.stopPropagation();
        window.quickSettings.toggleQuickSettings();
        if (window.soundFX) window.soundFX.playClick();
      });
    }

    // Clock/Calendar Trigger
    const clockGroup = document.getElementById('clock-date-group');
    if (clockGroup) {
      clockGroup.addEventListener('click', (e) => {
        e.stopPropagation();
        window.quickSettings.toggleCalendar();
        if (window.soundFX) window.soundFX.playClick();
      });
    }

    // Notification Bell
    const bell = document.getElementById('notification-bell');
    if (bell) {
      bell.addEventListener('click', (e) => {
        e.stopPropagation();
        window.quickSettings.toggleCalendar();
        if (window.soundFX) window.soundFX.playClick();
      });
    }

    // Show Desktop Slice
    const showDesktop = document.getElementById('show-desktop-slice');
    if (showDesktop) {
      showDesktop.addEventListener('click', () => {
        if (window.windowManager) {
          const wins = Array.from(window.windowManager.windows.values());
          const allMinimized = wins.every(w => w.isMinimized);
          wins.forEach(w => {
            if (allMinimized) window.windowManager.restoreWindow(w.id);
            else window.windowManager.minimizeWindow(w.id);
          });
        }
        if (window.soundFX) window.soundFX.playClick();
      });
    }
  }

  getTerminalSvg() {
    return `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: #38bdf8;"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg>`;
  }
  getMonitorSvg() {
    return `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: #34d399;"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/><polyline points="6 10 9 7 12 12 15 9 18 10"/></svg>`;
  }
  getJarvisSvg() {
    return `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: #00e5ff;"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3"/><line x1="12" y1="3" x2="12" y2="6"/><line x1="12" y1="18" x2="12" y2="21"/><line x1="3" y1="12" x2="6" y2="12"/><line x1="18" y1="12" x2="21" y2="12"/></svg>`;
  }
  getExplorerSvg() {
    return `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: #fbbf24;"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg>`;
  }
  getMediaSvg() {
    return `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: #ec4899;"><circle cx="12" cy="12" r="10"/><polygon points="10 8 16 12 10 16 10 8"/></svg>`;
  }
  getSettingsSvg() {
    return `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: #94a3b8;"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>`;
  }
}

window.TaskbarController = TaskbarController;
