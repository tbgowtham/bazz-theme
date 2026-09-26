// Stark Mark LXXXV Interactive Terminal Emulator
class StarkTerminal {
  constructor(containerEl) {
    this.container = containerEl;
    this.render();
  }

  render() {
    this.container.innerHTML = `
      <div class="terminal-window-body">
        <div class="terminal-history" id="term-history">
          <div class="terminal-banner">
================================================================
STARK INDUSTRIES // MARK LXXXV COMBAT SHELL v8.5.2
OPERATING SYSTEM: LINUX [FEDORA / WAYLAND COMPATIBLE]
J.A.R.V.I.S. PROTOCOL: ONLINE // DEFENSE GRID: LEVEL 5
TYPE 'help' FOR COMMANDS, 'diagnostics' OR 'status' FOR TELEMETRY
================================================================</div>
          <div class="terminal-line success">[STARK SECURE LINK ESTABLISHED]: Terminal initialized.</div>
        </div>
        <div class="terminal-input-row">
          <span class="terminal-prompt">stark@mark-85:~$</span>
          <input type="text" class="terminal-input" id="term-input" autofocus autocomplete="off" spellcheck="false" />
        </div>
      </div>
    `;

    this.input = this.container.querySelector('#term-input');
    this.history = this.container.querySelector('#term-history');

    this.input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        const cmd = this.input.value.trim();
        this.input.value = '';
        if (cmd) {
          this.executeCommand(cmd);
        }
      }
    });

    // Auto focus input when clicking anywhere in terminal
    this.container.addEventListener('click', () => {
      this.input.focus();
    });
  }

  printLine(text, type = 'out') {
    const line = document.createElement('div');
    line.className = `terminal-line ${type}`;
    line.textContent = text;
    this.history.appendChild(line);
    this.history.scrollTop = this.history.scrollHeight;
  }

  async executeCommand(cmd) {
    this.printLine(`stark@mark-85:~$ ${cmd}`, 'cmd');
    if (window.soundFX) window.soundFX.playClick();

    const parts = cmd.split(' ');
    const root = parts[0].toLowerCase();

    switch (root) {
      case 'help':
        this.printLine('Available Stark Protocols & Commands:', 'success');
        this.printLine('  status         - Display full armor & system status readout');
        this.printLine('  diagnostics    - Real-time CPU, RAM, and reactor core analysis');
        this.printLine('  scan           - Scan local network and perimeter sensors');
        this.printLine('  cinnamon       - Display Cinnamon desktop integration report');
        this.printLine('  plasma         - Display KDE Plasma 6 compatibility layer');
        this.printLine('  gnome          - Shell architecture comparison');
        this.printLine('  friday         - Switch AI vocal protocol to F.R.I.D.A.Y.');
        this.printLine('  jarvis         - Switch AI vocal protocol to J.A.R.V.I.S.');
        this.printLine('  theme [cyan|crimson|gold] - Switch desktop color matrix');
        this.printLine('  override       - Grant level 9 administrative clearance');
        this.printLine('  clear          - Clear terminal display buffer');
        this.printLine('  uname -a, date, uptime, free, whoami - Live Linux commands');
        break;

      case 'clear':
        this.history.innerHTML = '';
        break;

      case 'status':
        this.printLine('>>> MARK LXXXV TACTICAL READOUT <<<', 'success');
        this.printLine('• Armor Integrity:    100% [Nanotech Lattice Stable]');
        this.printLine('• Arc Reactor Output: 3.42 GW [Optimal]');
        this.printLine('• Repulsors:          100% Armed & Calibrated');
        this.printLine('• Unibeam:            Ready for Discharge');
        this.printLine('• Threat Level:       GREEN // Peacekeeping Protocol');
        this.printLine('• Defense Grid:       ACTIVE OMNI-DIRECTIONAL SHIELD');
        break;

      case 'diagnostics':
        try {
          const res = await fetch('/api/telemetry');
          const data = await res.json();
          this.printLine(`Host: ${data.system.hostname} (${data.system.platform} ${data.system.release})`, 'warn');
          this.printLine(`CPU:  ${data.cpu.model} [${data.cpu.cores} Cores] - Load: ${data.cpu.usagePercent}%`);
          this.printLine(`RAM:  ${data.memory.usedGB} GB used / ${data.memory.totalGB} GB total (${data.memory.usedPercent}%)`);
          this.printLine(`Uptime: ${data.system.uptimeFormatted}`);
          this.printLine(`Stark Core: ${data.starkCore.reactorOutput} | ${data.starkCore.coreStability}`);
        } catch {
          this.printLine('CPU Load: 12% | RAM: 4.1GB/7.5GB | Arc Stability: 99.9%', 'warn');
        }
        break;

      case 'scan':
        this.printLine('[STARK SENSOR ARRAY]: Initiating 360-degree quantum sweep...', 'warn');
        setTimeout(() => {
          this.printLine('• 1 local gateway detected: 192.168.1.1 (Secure)', 'out');
          this.printLine('• Zero anomalous kinetic signatures in perimeter.', 'success');
          this.printLine('• Satellite link: STARK-SAT-04 online.', 'out');
        }, 400);
        break;

      case 'cinnamon':
        this.printLine('>>> LINUX CINNAMON SHELL SPECIFICATION <<<', 'success');
        this.printLine('• Shell Type: Cinnamon Desktop Environment Shell');
        this.printLine('• Layout: Windows 11 Bottom Dock + Frosted Start Menu');
        this.printLine('• Assets: cinnamon/cinnamon.css (included in project)');
        this.printLine('• Installer: ./apply.sh (deploys to ~/.themes/Jarvis-Windows11-Shell)');
        break;

      case 'plasma':
        this.printLine('>>> KDE PLASMA 6 ENVIRONMENT DETECTED <<<', 'success');
        this.printLine('• Host Running: plasmashell 6.7.5 on Fedora Wayland');
        this.printLine('• Compatibility: Native Wayland window decorations & blur');
        break;

      case 'friday':
        document.body.className = 'theme-friday';
        if (window.arcReactor) window.arcReactor.setTheme(true, false);
        this.printLine('[VOICE AI]: F.R.I.D.A.Y. online. "Boss, protocol changed to crimson/gold."', 'error');
        if (window.jarvisAssistant) window.jarvisAssistant.speak('Friday online. Welcome back, boss.');
        break;

      case 'jarvis':
        document.body.className = '';
        if (window.arcReactor) window.arcReactor.setTheme(false, false);
        this.printLine('[VOICE AI]: J.A.R.V.I.S. online. "At your service, sir."', 'success');
        if (window.jarvisAssistant) window.jarvisAssistant.speak('Jarvis online. Always a pleasure, sir.');
        break;

      case 'override':
        this.printLine('[SECURITY OVERRIDE]: Clearance Level 9 CONFIRMED.', 'warn');
        this.printLine('Protocol "House Party" authorized. All nanotech sub-routines unlocked.', 'success');
        if (window.soundFX) window.soundFX.playStartup();
        break;

      default:
        // Try executing via live backend API
        try {
          const response = await fetch('/api/exec', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ command: cmd })
          });
          const resData = await response.json();
          this.printLine(resData.output || 'Executed.');
        } catch {
          this.printLine(`Command not found: ${cmd}. Type 'help' for instructions.`, 'error');
        }
    }
  }
}

window.StarkTerminal = StarkTerminal;
