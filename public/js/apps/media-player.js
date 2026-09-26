// Holographic Arc Waveform Media Player
class MediaPlayer {
  constructor(containerEl) {
    this.container = containerEl;
    this.isPlaying = false;
    this.currentTrack = 0;
    this.tracks = [
      { title: 'Shoot to Thrill (Quantum Mix)', artist: 'AC/DC // Stark Edition' },
      { title: 'Back In Black (Nanotech Synth)', artist: 'AC/DC // Mark LXXXV Remix' },
      { title: 'Avengers Theme (Arc Overdrive)', artist: 'Alan Silvestri // Jarvis Suite' }
    ];

    this.render();
  }

  render() {
    const track = this.tracks[this.currentTrack];
    this.container.innerHTML = `
      <div class="player-body">
        <div class="player-artwork" id="player-disc"></div>
        <div style="text-align: center;">
          <div style="font-size: 14px; font-weight: 700; color: #f8fafc;" id="track-title">${track.title}</div>
          <div style="font-size: 11px; color: var(--accent-cyan); font-family: var(--font-mono); margin-top: 2px;" id="track-artist">${track.artist}</div>
        </div>

        <canvas class="player-waveform-canvas" id="player-wave" width="300" height="50"></canvas>

        <div class="player-controls">
          <button class="player-btn" id="prev-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><polygon points="19 20 9 12 19 4 19 20"/><line x1="5" y1="19" x2="5" y2="5" stroke="currentColor" stroke-width="2"/></svg>
          </button>
          <button class="player-btn play-pause" id="play-btn">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" id="play-icon"><polygon points="5 3 19 12 5 21 5 3"/></svg>
          </button>
          <button class="player-btn" id="next-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 4 15 12 5 20 5 4"/><line x1="19" y1="5" x2="19" y2="19" stroke="currentColor" stroke-width="2"/></svg>
          </button>
        </div>
      </div>
    `;

    this.bindEvents();
    this.drawWaveform();
  }

  bindEvents() {
    const playBtn = this.container.querySelector('#play-btn');
    const playIcon = this.container.querySelector('#play-icon');
    const disc = this.container.querySelector('#player-disc');

    playBtn.addEventListener('click', () => {
      if (window.soundFX) {
        this.isPlaying = window.soundFX.toggleMusic((step) => {
          this.drawActiveWave(step);
        });

        if (this.isPlaying) {
          playIcon.innerHTML = `<rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/>`;
          disc.style.animationPlayState = 'running';
        } else {
          playIcon.innerHTML = `<polygon points="5 3 19 12 5 21 5 3"/>`;
          disc.style.animationPlayState = 'paused';
          this.drawWaveform();
        }
      }
    });

    const nextBtn = this.container.querySelector('#next-btn');
    nextBtn.addEventListener('click', () => {
      this.currentTrack = (this.currentTrack + 1) % this.tracks.length;
      this.updateTrackInfo();
      if (window.soundFX) window.soundFX.playClick();
    });

    const prevBtn = this.container.querySelector('#prev-btn');
    prevBtn.addEventListener('click', () => {
      this.currentTrack = (this.currentTrack - 1 + this.tracks.length) % this.tracks.length;
      this.updateTrackInfo();
      if (window.soundFX) window.soundFX.playClick();
    });
  }

  updateTrackInfo() {
    const track = this.tracks[this.currentTrack];
    this.container.querySelector('#track-title').textContent = track.title;
    this.container.querySelector('#track-artist').textContent = track.artist;
  }

  drawWaveform() {
    const canvas = this.container.querySelector('#player-wave');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.strokeStyle = 'rgba(0, 229, 255, 0.4)';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(0, h / 2);

    for (let x = 0; x < w; x += 6) {
      const y = h / 2 + Math.sin(x * 0.08) * 6;
      ctx.lineTo(x, y);
    }
    ctx.stroke();
  }

  drawActiveWave(step) {
    const canvas = this.container.querySelector('#player-wave');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);
    ctx.strokeStyle = '#00e5ff';
    ctx.shadowColor = '#00e5ff';
    ctx.shadowBlur = 8;
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(0, h / 2);

    for (let x = 0; x < w; x += 4) {
      const amp = Math.sin((x + step * 10) * 0.1) * 16 * Math.sin(x * 0.02);
      ctx.lineTo(x, h / 2 + amp);
    }
    ctx.stroke();
    ctx.shadowBlur = 0;
  }
}

window.MediaPlayer = MediaPlayer;
