// Window Manager for High-Tech Linux Desktop Shell
class WindowManager {
  constructor() {
    this.container = document.getElementById('windows-container');
    this.windows = new Map();
    this.topZ = 100;
    this.activeWindowId = null;
    this.dragTarget = null;
    this.resizeTarget = null;
    this.dragOffset = { x: 0, y: 0 };
    this.initialRect = { x: 0, y: 0, w: 0, h: 0 };
    this.resizeDirection = '';

    this.bindGlobalEvents();
  }

  createWindow({ id, title, icon, width = 640, height = 440, x, y, contentHtml, onInit }) {
    if (this.windows.has(id)) {
      this.restoreWindow(id);
      this.bringToFront(id);
      return this.windows.get(id);
    }

    const defaultX = x !== undefined ? x : Math.max(40, (window.innerWidth - width) / 2 + (this.windows.size * 25));
    const defaultY = y !== undefined ? y : Math.max(40, (window.innerHeight - 48 - height) / 2 + (this.windows.size * 25));

    const winEl = document.createElement('div');
    winEl.className = 'os-window';
    winEl.id = `win-${id}`;
    winEl.style.width = `${width}px`;
    winEl.style.height = `${height}px`;
    winEl.style.left = `${defaultX}px`;
    winEl.style.top = `${defaultY}px`;
    winEl.style.zIndex = ++this.topZ;

    winEl.innerHTML = `
      <div class="window-titlebar" data-win-id="${id}">
        <div class="window-title-left">
          <div class="window-title-icon">${icon || ''}</div>
          <span class="window-title-text">${title}</span>
        </div>
        <div class="window-controls">
          <button class="win-control-btn btn-min" title="Minimize" data-action="min">
            <svg viewBox="0 0 16 16" fill="currentColor"><path d="M14 8v1H2V8h12z"/></svg>
          </button>
          <button class="win-control-btn btn-max" title="Maximize" data-action="max">
            <svg viewBox="0 0 16 16" fill="currentColor"><path d="M3 3v10h10V3H3zm9 9H4V4h8v8z"/></svg>
          </button>
          <button class="win-control-btn btn-close" title="Close" data-action="close">
            <svg viewBox="0 0 16 16" fill="currentColor"><path d="M13.854 2.146a.5.5 0 0 1 0 .708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8 2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708 0z"/></svg>
          </button>
        </div>
      </div>
      <div class="window-content" id="win-body-${id}">
        ${contentHtml || ''}
      </div>
      <div class="win-resize-handle win-resize-n" data-dir="n"></div>
      <div class="win-resize-handle win-resize-s" data-dir="s"></div>
      <div class="win-resize-handle win-resize-w" data-dir="w"></div>
      <div class="win-resize-handle win-resize-e" data-dir="e"></div>
      <div class="win-resize-handle win-resize-nw" data-dir="nw"></div>
      <div class="win-resize-handle win-resize-ne" data-dir="ne"></div>
      <div class="win-resize-handle win-resize-sw" data-dir="sw"></div>
      <div class="win-resize-handle win-resize-se" data-dir="se"></div>
    `;

    this.container.appendChild(winEl);

    const winObj = {
      id,
      el: winEl,
      isMaximized: false,
      isMinimized: false,
      prevRect: null
    };

    this.windows.set(id, winObj);
    this.bringToFront(id);

    if (window.soundFX) window.soundFX.playWindowOpen();

    if (window.taskbar) {
      window.taskbar.onWindowCreated(id);
    }

    if (onInit) {
      onInit(winEl.querySelector(`#win-body-${id}`));
    }

    return winObj;
  }

  bringToFront(id) {
    const win = this.windows.get(id);
    if (!win) return;

    this.windows.forEach(w => w.el.classList.remove('active'));
    win.el.style.zIndex = ++this.topZ;
    win.el.classList.add('active');
    this.activeWindowId = id;

    if (window.taskbar) {
      window.taskbar.setActiveWindow(id);
    }
  }

  minimizeWindow(id) {
    const win = this.windows.get(id);
    if (!win) return;
    win.isMinimized = true;
    win.el.classList.add('minimized');
    win.el.classList.remove('active');

    if (this.activeWindowId === id) {
      this.activeWindowId = null;
    }
    if (window.taskbar) {
      window.taskbar.onWindowMinimized(id);
    }
    if (window.soundFX) window.soundFX.playClick();
  }

  restoreWindow(id) {
    const win = this.windows.get(id);
    if (!win) return;
    win.isMinimized = false;
    win.el.classList.remove('minimized');
    this.bringToFront(id);
    if (window.soundFX) window.soundFX.playClick();
  }

  toggleWindow(id) {
    const win = this.windows.get(id);
    if (!win) return;
    if (win.isMinimized) {
      this.restoreWindow(id);
    } else if (this.activeWindowId === id) {
      this.minimizeWindow(id);
    } else {
      this.bringToFront(id);
    }
  }

  toggleMaximize(id) {
    const win = this.windows.get(id);
    if (!win) return;

    if (!win.isMaximized) {
      win.prevRect = {
        left: win.el.style.left,
        top: win.el.style.top,
        width: win.el.style.width,
        height: win.el.style.height
      };
      win.el.classList.add('maximized');
      win.isMaximized = true;
    } else {
      win.el.classList.remove('maximized');
      if (win.prevRect) {
        win.el.style.left = win.prevRect.left;
        win.el.style.top = win.prevRect.top;
        win.el.style.width = win.prevRect.width;
        win.el.style.height = win.prevRect.height;
      }
      win.isMaximized = false;
    }
    if (window.soundFX) window.soundFX.playClick();
  }

  closeWindow(id) {
    const win = this.windows.get(id);
    if (!win) return;

    win.el.style.transform = 'scale(0.8)';
    win.el.style.opacity = '0';
    setTimeout(() => {
      win.el.remove();
      this.windows.delete(id);
      if (this.activeWindowId === id) {
        this.activeWindowId = null;
      }
      if (window.taskbar) {
        window.taskbar.onWindowClosed(id);
      }
    }, 200);

    if (window.soundFX) window.soundFX.playClick();
  }

  bindGlobalEvents() {
    this.container.addEventListener('mousedown', (e) => {
      const winEl = e.target.closest('.os-window');
      if (winEl) {
        const id = winEl.id.replace('win-', '');
        this.bringToFront(id);
      }

      // Titlebar buttons
      const btn = e.target.closest('.win-control-btn');
      if (btn) {
        const titlebar = btn.closest('.window-titlebar');
        const id = titlebar.dataset.winId;
        const action = btn.dataset.action;
        if (action === 'min') this.minimizeWindow(id);
        else if (action === 'max') this.toggleMaximize(id);
        else if (action === 'close') this.closeWindow(id);
        return;
      }

      // Titlebar drag initiation
      const titlebar = e.target.closest('.window-titlebar');
      if (titlebar && !btn) {
        const id = titlebar.dataset.winId;
        const win = this.windows.get(id);
        if (win && !win.isMaximized) {
          this.dragTarget = win;
          const rect = win.el.getBoundingClientRect();
          this.dragOffset = {
            x: e.clientX - rect.left,
            y: e.clientY - rect.top
          };
        }
        return;
      }

      // Resize handle
      const resizeHandle = e.target.closest('.win-resize-handle');
      if (resizeHandle) {
        const winEl = resizeHandle.closest('.os-window');
        const id = winEl.id.replace('win-', '');
        const win = this.windows.get(id);
        if (win && !win.isMaximized) {
          this.resizeTarget = win;
          this.resizeDirection = resizeHandle.dataset.dir;
          const rect = win.el.getBoundingClientRect();
          this.initialRect = {
            x: rect.left,
            y: rect.top,
            w: rect.width,
            h: rect.height,
            startX: e.clientX,
            startY: e.clientY
          };
        }
      }
    });

    window.addEventListener('mousemove', (e) => {
      // Dragging
      if (this.dragTarget) {
        let newX = e.clientX - this.dragOffset.x;
        let newY = e.clientY - this.dragOffset.y;

        // Desktop bounds
        newY = Math.max(0, Math.min(window.innerHeight - 80, newY));
        newX = Math.max(-200, Math.min(window.innerWidth - 100, newX));

        this.dragTarget.el.style.left = `${newX}px`;
        this.dragTarget.el.style.top = `${newY}px`;
      }

      // Resizing
      if (this.resizeTarget) {
        const dx = e.clientX - this.initialRect.startX;
        const dy = e.clientY - this.initialRect.startY;
        let newW = this.initialRect.w;
        let newH = this.initialRect.h;
        let newX = this.initialRect.x;
        let newY = this.initialRect.y;

        if (this.resizeDirection.includes('e')) newW = Math.max(340, this.initialRect.w + dx);
        if (this.resizeDirection.includes('s')) newH = Math.max(220, this.initialRect.h + dy);
        if (this.resizeDirection.includes('w')) {
          const possibleW = this.initialRect.w - dx;
          if (possibleW >= 340) {
            newW = possibleW;
            newX = this.initialRect.x + dx;
          }
        }
        if (this.resizeDirection.includes('n')) {
          const possibleH = this.initialRect.h - dy;
          if (possibleH >= 220) {
            newH = possibleH;
            newY = this.initialRect.y + dy;
          }
        }

        this.resizeTarget.el.style.width = `${newW}px`;
        this.resizeTarget.el.style.height = `${newH}px`;
        this.resizeTarget.el.style.left = `${newX}px`;
        this.resizeTarget.el.style.top = `${newY}px`;
      }
    });

    window.addEventListener('mouseup', () => {
      this.dragTarget = null;
      this.resizeTarget = null;
    });
  }
}

window.WindowManager = WindowManager;
