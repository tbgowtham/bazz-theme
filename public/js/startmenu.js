// Windows 11 Floating Start Menu Controller
class StartMenuController {
  constructor() {
    this.menuEl = document.getElementById('start-menu');
    this.powerMenu = document.getElementById('power-options-menu');
    this.searchInput = document.getElementById('start-search-input');
    this.isOpen = false;

    this.init();
  }

  init() {
    this.bindEvents();
  }

  toggle() {
    if (this.isOpen) {
      this.close();
    } else {
      this.open();
    }
  }

  open() {
    this.isOpen = true;
    this.menuEl.classList.add('open');
    if (this.searchInput) {
      this.searchInput.value = '';
      setTimeout(() => this.searchInput.focus(), 50);
    }
    this.filterApps('');
    // Close other panels
    if (window.quickSettings) {
      window.quickSettings.closeAll();
    }
  }

  close() {
    this.isOpen = false;
    this.menuEl.classList.remove('open');
    if (this.powerMenu) this.powerMenu.classList.remove('open');
  }

  bindEvents() {
    // Search filter
    if (this.searchInput) {
      this.searchInput.addEventListener('input', (e) => {
        this.filterApps(e.target.value.toLowerCase().trim());
      });

      this.searchInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          const firstApp = this.menuEl.querySelector('.pinned-app-item:not([style*="display: none"])');
          if (firstApp) {
            firstApp.click();
          }
        }
      });
    }

    // Pinned App click
    this.menuEl.addEventListener('click', (e) => {
      const appItem = e.target.closest('.pinned-app-item');
      if (appItem) {
        const appId = appItem.dataset.appId;
        window.app.launchApp(appId);
        this.close();
        if (window.soundFX) window.soundFX.playClick();
        return;
      }

      const recItem = e.target.closest('.recommended-item');
      if (recItem) {
        const appId = recItem.dataset.appId || 'terminal';
        window.app.launchApp(appId);
        this.close();
        if (window.soundFX) window.soundFX.playClick();
        return;
      }

      const powerBtn = e.target.closest('#start-power-btn');
      if (powerBtn) {
        if (this.powerMenu) this.powerMenu.classList.toggle('open');
        if (window.soundFX) window.soundFX.playClick();
        return;
      }

      const powerOpt = e.target.closest('.power-option-item');
      if (powerOpt) {
        const action = powerOpt.dataset.powerAction;
        this.handlePower(action);
        return;
      }
    });

    // Close on outside click
    document.addEventListener('click', (e) => {
      if (this.isOpen && !e.target.closest('#start-menu') && !e.target.closest('#start-btn')) {
        this.close();
      }
    });

    // Close on ESC
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && this.isOpen) {
        this.close();
      }
    });
  }

  filterApps(query) {
    const items = this.menuEl.querySelectorAll('.pinned-app-item');
    items.forEach(item => {
      const name = item.dataset.appName.toLowerCase();
      if (!query || name.includes(query)) {
        item.style.display = 'flex';
      } else {
        item.style.display = 'none';
      }
    });
  }

  handlePower(action) {
    this.close();
    if (action === 'lock') {
      if (window.lockScreen) window.lockScreen.lock();
    } else if (action === 'restart') {
      alert('[STARK OS]: Re-calibrating Mark LXXXV armor thrusters and rebooting shell...');
      setTimeout(() => location.reload(), 800);
    } else if (action === 'shutdown') {
      alert('[STARK OS]: Powering down Arc Reactor to standby mode.');
      if (window.lockScreen) window.lockScreen.lock();
    } else if (action === 'sleep') {
      alert('[STARK OS]: Entering low-power nanotech sleep state.');
    }
  }
}

window.StartMenuController = StartMenuController;
