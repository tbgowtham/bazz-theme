// Master Application Orchestrator for Stark Industries Linux Desktop Shell
class StarkDesktopApp {
  constructor() {
    this.init();
  }

  init() {
    // 1. Initialize Canvas Arc-Reactor
    window.arcReactor = new ArcReactor('arc-canvas');

    // 2. Initialize Window Manager
    window.windowManager = new WindowManager();

    // 3. Initialize Taskbar
    window.taskbar = new TaskbarController();

    // 4. Initialize Start Menu
    window.startMenu = new StartMenuController();

    // 5. Initialize Quick Settings & Overlays
    window.quickSettings = new QuickSettingsController();
    window.lockScreen = window.quickSettings;

    // 6. Bind Desktop Icons
    this.bindDesktopIcons();

    // 7. Bind Keyboard Shortcuts
    this.bindKeyboardShortcuts();

    // 8. Auto-launch Terminal & System Monitor on startup for high-tech HUD experience
    setTimeout(() => {
      this.launchApp('monitor', { x: window.innerWidth - 680, y: 70, width: 640, height: 420 });
      this.launchApp('chat', { x: 50, y: 70, width: 540, height: 440 });
      if (window.soundFX) window.soundFX.playStartup();
    }, 400);

    // Initial greeting chime
    console.log('[STARK OS]: Desktop Shell Initialized successfully.');
  }

  launchApp(appId, customCoords = {}) {
    if (window.windowManager.windows.has(appId)) {
      window.windowManager.toggleWindow(appId);
      return;
    }

    switch (appId) {
      case 'terminal':
        window.windowManager.createWindow({
          id: 'terminal',
          title: 'Mark LXXXV Terminal // Bash Shell',
          icon: window.taskbar.getTerminalSvg(),
          width: customCoords.width || 680,
          height: customCoords.height || 420,
          x: customCoords.x,
          y: customCoords.y,
          onInit: (bodyEl) => {
            new StarkTerminal(bodyEl);
          }
        });
        break;

      case 'monitor':
        window.windowManager.createWindow({
          id: 'monitor',
          title: 'Stark Industries Telemetry & Diagnostic Monitor',
          icon: window.taskbar.getMonitorSvg(),
          width: customCoords.width || 660,
          height: customCoords.height || 440,
          x: customCoords.x,
          y: customCoords.y,
          onInit: (bodyEl) => {
            new SystemMonitor(bodyEl);
          }
        });
        break;

      case 'chat':
        window.windowManager.createWindow({
          id: 'chat',
          title: 'J.A.R.V.I.S. Core // Voice & Tactical Assistant',
          icon: window.taskbar.getJarvisSvg(),
          width: customCoords.width || 560,
          height: customCoords.height || 460,
          x: customCoords.x,
          y: customCoords.y,
          onInit: (bodyEl) => {
            window.jarvisAssistant = new JarvisAssistant(bodyEl);
          }
        });
        break;

      case 'explorer':
        window.windowManager.createWindow({
          id: 'explorer',
          title: 'Holographic File Explorer // Quantum Drive',
          icon: window.taskbar.getExplorerSvg(),
          width: customCoords.width || 720,
          height: customCoords.height || 460,
          x: customCoords.x,
          y: customCoords.y,
          onInit: (bodyEl) => {
            new FileExplorer(bodyEl);
          }
        });
        break;

      case 'media':
        window.windowManager.createWindow({
          id: 'media',
          title: 'Stark Arc Waveform Audio Player',
          icon: window.taskbar.getMediaSvg(),
          width: customCoords.width || 420,
          height: customCoords.height || 420,
          x: customCoords.x,
          y: customCoords.y,
          onInit: (bodyEl) => {
            new MediaPlayer(bodyEl);
          }
        });
        break;

      case 'settings':
        window.windowManager.createWindow({
          id: 'settings',
          title: 'Shell Settings & Linux Cinnamon Integration',
          icon: window.taskbar.getSettingsSvg(),
          width: customCoords.width || 720,
          height: customCoords.height || 460,
          x: customCoords.x,
          y: customCoords.y,
          onInit: (bodyEl) => {
            new ShellSettings(bodyEl);
          }
        });
        break;
    }
  }

  bindDesktopIcons() {
    const icons = document.querySelectorAll('.desktop-icon');
    icons.forEach(icon => {
      icon.addEventListener('dblclick', () => {
        const appId = icon.dataset.appId;
        if (appId) {
          this.launchApp(appId);
          if (window.soundFX) window.soundFX.playClick();
        }
      });
      icon.addEventListener('click', () => {
        if (window.soundFX) window.soundFX.playClick();
      });
    });
  }

  bindKeyboardShortcuts() {
    window.addEventListener('keydown', (e) => {
      // Windows Key / Meta Key -> Toggle Start Menu
      if (e.key === 'Meta') {
        e.preventDefault();
        window.startMenu.toggle();
        if (window.soundFX) window.soundFX.playClick();
      }

      // Ctrl + Alt + T -> Terminal
      if (e.ctrlKey && e.altKey && e.key.toLowerCase() === 't') {
        e.preventDefault();
        this.launchApp('terminal');
      }

      // Alt + Tab -> Toggle Task View
      if (e.altKey && e.key === 'Tab') {
        e.preventDefault();
        window.quickSettings.toggleTaskView();
      }

      // Meta + L -> Lock Screen
      if (e.metaKey && e.key.toLowerCase() === 'l') {
        e.preventDefault();
        window.lockScreen.lock();
      }
    });
  }
}

document.addEventListener('DOMContentLoaded', () => {
  window.app = new StarkDesktopApp();
});
