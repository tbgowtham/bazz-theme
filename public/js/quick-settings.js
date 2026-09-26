// Quick Settings, Calendar, Task View & Lock Screen Controller
class QuickSettingsController {
  constructor() {
    this.quickSettingsPanel = document.getElementById('quick-settings-panel');
    this.calendarPanel = document.getElementById('calendar-flyout');
    this.taskViewOverlay = document.getElementById('task-view-overlay');
    this.lockScreenOverlay = document.getElementById('lock-screen-overlay');

    this.currentDate = new Date();
    this.init();
  }

  init() {
    this.bindQuickToggles();
    this.bindSliders();
    this.renderCalendar();
    this.bindCalendarEvents();
    this.bindTaskViewEvents();
    this.bindLockScreenEvents();
    this.bindOutsideClicks();
  }

  toggleQuickSettings() {
    if (this.quickSettingsPanel.classList.contains('open')) {
      this.quickSettingsPanel.classList.remove('open');
    } else {
      this.closeAll();
      this.quickSettingsPanel.classList.add('open');
    }
  }

  toggleCalendar() {
    if (this.calendarPanel.classList.contains('open')) {
      this.calendarPanel.classList.remove('open');
    } else {
      this.closeAll();
      this.calendarPanel.classList.add('open');
      this.renderCalendar();
    }
  }

  toggleTaskView() {
    this.taskViewOverlay.classList.toggle('open');
    const viewport = document.getElementById('desktop-viewport');
    if (this.taskViewOverlay.classList.contains('open')) {
      viewport.classList.add('blurred');
    } else {
      viewport.classList.remove('blurred');
    }
  }

  closeAll() {
    if (this.quickSettingsPanel) this.quickSettingsPanel.classList.remove('open');
    if (this.calendarPanel) this.calendarPanel.classList.remove('open');
    if (window.startMenu) window.startMenu.close();
  }

  bindQuickToggles() {
    const toggles = this.quickSettingsPanel.querySelectorAll('.quick-toggle-btn');
    toggles.forEach(btn => {
      btn.addEventListener('click', () => {
        btn.classList.toggle('active');
        if (window.soundFX) window.soundFX.playClick();

        const type = btn.dataset.toggle;
        if (type === 'nightlight') {
          document.body.style.filter = btn.classList.contains('active') ? 'sepia(0.25)' : 'none';
        } else if (type === 'defense') {
          const status = btn.classList.contains('active') ? 'OMNI-SHIELD ACTIVE' : 'STANDBY';
          alert(`[STARK DEFENSE GRID]: Perimeter security shifted to: ${status}`);
        }
      });
    });
  }

  bindSliders() {
    const volSlider = document.getElementById('volume-slider');
    if (volSlider) {
      volSlider.addEventListener('input', (e) => {
        const val = e.target.value;
        const pill = document.querySelector('#tray-vol-pill');
        if (pill) pill.textContent = `${val}%`;
      });
      volSlider.addEventListener('change', () => {
        if (window.soundFX) window.soundFX.playClick();
      });
    }

    const brightSlider = document.getElementById('bright-slider');
    if (brightSlider) {
      brightSlider.addEventListener('input', (e) => {
        const val = e.target.value;
        const b = 0.4 + (val / 100) * 0.6;
        document.getElementById('desktop-viewport').style.filter = `brightness(${b})`;
      });
    }
  }

  renderCalendar() {
    const monthEl = document.getElementById('cal-month-year');
    const gridEl = document.getElementById('cal-days-grid');
    if (!monthEl || !gridEl) return;

    const year = this.currentDate.getFullYear();
    const month = this.currentDate.getMonth();
    const monthNames = [
      'January', 'February', 'March', 'April', 'May', 'June',
      'July', 'August', 'September', 'October', 'November', 'December'
    ];

    monthEl.textContent = `${monthNames[month]} ${year}`;

    // Get first day and total days in month
    const firstDay = new Date(year, month, 1).getDay();
    const totalDays = new Date(year, month + 1, 0).getDate();

    const today = new Date();
    const isThisMonth = today.getFullYear() === year && today.getMonth() === month;

    let html = '';
    // Empty cells for padding
    for (let i = 0; i < firstDay; i++) {
      html += `<div class="calendar-day-cell" style="opacity: 0.2;"></div>`;
    }

    for (let day = 1; day <= totalDays; day++) {
      const isToday = isThisMonth && today.getDate() === day;
      html += `<div class="calendar-day-cell ${isToday ? 'today' : ''}">${day}</div>`;
    }

    gridEl.innerHTML = html;
  }

  bindCalendarEvents() {
    const prevBtn = document.getElementById('cal-prev');
    const nextBtn = document.getElementById('cal-next');

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        this.currentDate.setMonth(this.currentDate.getMonth() - 1);
        this.renderCalendar();
        if (window.soundFX) window.soundFX.playClick();
      });
    }
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        this.currentDate.setMonth(this.currentDate.getMonth() + 1);
        this.renderCalendar();
        if (window.soundFX) window.soundFX.playClick();
      });
    }
  }

  bindTaskViewEvents() {
    const cards = this.taskViewOverlay.querySelectorAll('.workspace-card');
    cards.forEach(card => {
      card.addEventListener('click', () => {
        cards.forEach(c => c.classList.remove('active'));
        card.classList.add('active');
        this.toggleTaskView();
        const wsId = card.dataset.workspace;
        alert(`[STARK WORKSPACE]: Shifted to Virtual Desktop: ${wsId}`);
        if (window.soundFX) window.soundFX.playClick();
      });
    });

    this.taskViewOverlay.addEventListener('click', (e) => {
      if (e.target === this.taskViewOverlay) {
        this.toggleTaskView();
      }
    });
  }

  bindLockScreenEvents() {
    const unlockBtn = document.getElementById('lock-unlock-btn');
    const pinInput = document.getElementById('lock-pin-input');

    const tryUnlock = () => {
      this.lockScreenOverlay.classList.remove('open');
      if (pinInput) pinInput.value = '';
      if (window.soundFX) window.soundFX.playStartup();
      if (window.jarvisAssistant) {
        window.jarvisAssistant.speak('Welcome back, Mr. Gray. All security perimeters disengaged.');
      }
    };

    if (unlockBtn) unlockBtn.addEventListener('click', tryUnlock);
    if (pinInput) {
      pinInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') tryUnlock();
      });
    }
  }

  lock() {
    this.closeAll();
    this.lockScreenOverlay.classList.add('open');
    if (window.soundFX) window.soundFX.playError();
    const pinInput = document.getElementById('lock-pin-input');
    if (pinInput) setTimeout(() => pinInput.focus(), 100);
  }

  bindOutsideClicks() {
    document.addEventListener('click', (e) => {
      if (
        !e.target.closest('#quick-settings-panel') &&
        !e.target.closest('#tray-quick-settings-trigger')
      ) {
        if (this.quickSettingsPanel) this.quickSettingsPanel.classList.remove('open');
      }

      if (
        !e.target.closest('#calendar-flyout') &&
        !e.target.closest('#clock-date-group') &&
        !e.target.closest('#notification-bell')
      ) {
        if (this.calendarPanel) this.calendarPanel.classList.remove('open');
      }
    });
  }
}

window.QuickSettingsController = QuickSettingsController;
