// J.A.R.V.I.S. & F.R.I.D.A.Y. Conversational Voice & AI Assistant
class JarvisAssistant {
  constructor(containerEl) {
    this.container = containerEl;
    this.mode = 'jarvis'; // 'jarvis' or 'friday'
    this.voiceSynth = window.speechSynthesis;
    this.speechEnabled = true;

    this.render();
  }

  render() {
    this.container.innerHTML = `
      <div class="jarvis-chat-body">
        <div class="jarvis-hud-bar">
          <div class="jarvis-status-tag">
            <span class="core-pulse-dot"></span>
            <span id="jarvis-ai-title">${this.mode === 'jarvis' ? 'J.A.R.V.I.S. CORE v8.5' : 'F.R.I.D.A.Y. PROTOCOL'}</span>
          </div>
          <button class="jarvis-voice-toggle-btn" id="voice-toggle-btn">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg>
            <span id="voice-toggle-text">Voice: ON</span>
          </button>
        </div>
        <div class="jarvis-messages-container" id="jarvis-msgs">
          <div class="jarvis-msg ai">
            <strong>${this.mode === 'jarvis' ? 'J.A.R.V.I.S.' : 'F.R.I.D.A.Y.'}:</strong>
            Good evening, sir. Mark LXXXV nanotech systems and Windows 11 shell integration are fully operational. How may I assist you today?
          </div>
        </div>
        <div style="padding: 6px 16px; display: flex; gap: 6px; overflow-x: auto; background: rgba(8,14,24,0.95); border-top: 1px solid rgba(255,255,255,0.05);" id="quick-chips">
          <button class="start-section-btn quick-chip" data-query="Status report">Status Report</button>
          <button class="start-section-btn quick-chip" data-query="Compare with Cinnamon and KDE">Shell Comparison</button>
          <button class="start-section-btn quick-chip" data-query="Switch to Friday">Switch to Friday</button>
          <button class="start-section-btn quick-chip" data-query="Full armor scan">Armor Scan</button>
        </div>
        <div class="jarvis-input-container">
          <input type="text" class="jarvis-input" id="jarvis-user-input" placeholder="Ask Jarvis anything or speak a command..." autocomplete="off" />
          <button class="jarvis-send-btn" id="jarvis-send-btn">Transmit</button>
        </div>
      </div>
    `;

    this.messages = this.container.querySelector('#jarvis-msgs');
    this.input = this.container.querySelector('#jarvis-user-input');
    this.sendBtn = this.container.querySelector('#jarvis-send-btn');
    this.voiceBtn = this.container.querySelector('#voice-toggle-btn');
    this.chips = this.container.querySelectorAll('.quick-chip');

    this.sendBtn.addEventListener('click', () => this.handleSend());
    this.input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') this.handleSend();
    });

    this.voiceBtn.addEventListener('click', () => {
      this.speechEnabled = !this.speechEnabled;
      this.container.querySelector('#voice-toggle-text').textContent = `Voice: ${this.speechEnabled ? 'ON' : 'OFF'}`;
      if (window.soundFX) window.soundFX.playClick();
    });

    this.chips.forEach(chip => {
      chip.addEventListener('click', () => {
        this.input.value = chip.dataset.query;
        this.handleSend();
      });
    });
  }

  handleSend() {
    const text = this.input.value.trim();
    if (!text) return;
    this.input.value = '';

    this.addMessage(text, 'user');
    if (window.soundFX) window.soundFX.playClick();

    setTimeout(() => {
      const response = this.generateResponse(text);
      this.addMessage(response, 'ai');
      this.speak(response);
    }, 300);
  }

  addMessage(text, sender) {
    const msg = document.createElement('div');
    msg.className = `jarvis-msg ${sender}`;
    const name = sender === 'user' ? 'Tony Stark' : (this.mode === 'jarvis' ? 'J.A.R.V.I.S.' : 'F.R.I.D.A.Y.');
    msg.innerHTML = `<strong>${name}:</strong> ${text}`;
    this.messages.appendChild(msg);
    this.messages.scrollTop = this.messages.scrollHeight;
  }

  speak(text) {
    if (!this.speechEnabled || !this.voiceSynth) return;
    try {
      this.voiceSynth.cancel();
      const utterance = new SpeechSynthesisUtterance(text.replace(/<[^>]*>?/gm, ''));
      const voices = this.voiceSynth.getVoices();

      if (this.mode === 'jarvis') {
        const ukVoice = voices.find(v => v.lang.includes('en-GB') || v.name.includes('George') || v.name.includes('Oliver') || v.name.includes('Male'));
        if (ukVoice) utterance.voice = ukVoice;
        utterance.pitch = 0.95;
        utterance.rate = 1.02;
      } else {
        const femaleVoice = voices.find(v => v.name.includes('Female') || v.name.includes('Victoria') || v.name.includes('Zira') || v.lang.includes('en-IE') || v.lang.includes('en-US'));
        if (femaleVoice) utterance.voice = femaleVoice;
        utterance.pitch = 1.15;
        utterance.rate = 1.05;
      }

      this.voiceSynth.speak(utterance);
    } catch {}
  }

  generateResponse(query) {
    const q = query.toLowerCase();

    if (q.includes('switch to friday') || q.includes('friday protocol')) {
      this.mode = 'friday';
      document.body.className = 'theme-friday';
      if (window.arcReactor) window.arcReactor.setTheme(true, false);
      const titleEl = this.container.querySelector('#jarvis-ai-title');
      if (titleEl) titleEl.textContent = 'F.R.I.D.A.Y. PROTOCOL';
      return "Switching to the Friday protocol. Mark LXXXV nanotech matrix shifted to crimson and titanium gold. I'm all set, boss.";
    }

    if (q.includes('switch to jarvis') || q.includes('jarvis')) {
      this.mode = 'jarvis';
      document.body.className = '';
      if (window.arcReactor) window.arcReactor.setTheme(false, false);
      const titleEl = this.container.querySelector('#jarvis-ai-title');
      if (titleEl) titleEl.textContent = 'J.A.R.V.I.S. CORE v8.5';
      return "Re-engaging the J.A.R.V.I.S. neural network. Always delightful to serve you, sir.";
    }

    if (q.includes('status') || q.includes('report')) {
      return "All Mark LXXXV systems are operating at peak efficiency. Arc reactor output is steady at 3.42 Gigawatts with 99.9% core stability. Flight thrusters, micro-repulsors, and nanotech armor integrity are at 100%.";
    }

    if (q.includes('cinnamon') || q.includes('plasma') || q.includes('gnome') || q.includes('compare') || q.includes('shell')) {
      return "Compared to standard shells like Cinnamon, KDE Plasma, and GNOME, our Stark OS integrates Windows 11's centered taskbar, frosted glass Start Menu, and Quick Settings directly with the Mark LXXXV holographic HUD and native Linux telemetry. It also includes full Cinnamon theme files in cinnamon/cinnamon.css for direct desktop installation!";
    }

    if (q.includes('armor') || q.includes('suit') || q.includes('scan')) {
      return "Nanotech lattice structure verified. Atmospheric pressurization intact. Zero micro-fractures detected. Ready for orbital engagement.";
    }

    if (q.includes('lock') || q.includes('security')) {
      if (window.lockScreen) window.lockScreen.lock();
      return "Engaging Stark Industries lockdown protocol. Biometric and security credentials required.";
    }

    if (q.includes('weather') || q.includes('temperature')) {
      return "Atmospheric sensors report optimal ambient conditions: 22°C (71.6°F), barometric pressure 1013 hPa, wind speed 4 knots. Perfect conditions for a supersonic test flight.";
    }

    if (q.includes('who are you') || q.includes('identity')) {
      return this.mode === 'jarvis' 
        ? "I am J.A.R.V.I.S. — Just A Rather Very Intelligent System, engineered by Tony Stark to manage Stark Industries facilities, the Iron Man armor, and your Linux desktop shell."
        : "I am F.R.I.D.A.Y. — Female Replacement Intelligent Digital Assistant Youth, ready to run diagnostics and back you up in any tactical scenario.";
    }

    return `Telemetry recorded for "${query}". Tactical analysis confirms optimal system parameters. Let me know if you would like me to calibrate thrusters, run a diagnostics sweep, or configure the Cinnamon shell.`;
  }
}

window.JarvisAssistant = JarvisAssistant;
