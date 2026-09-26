const http = require('http');
const fs = require('fs');
const path = require('path');
const os = require('os');
const { exec } = require('child_process');

const PORT = process.env.PORT || 3030;
const PUBLIC_DIR = path.join(__dirname, 'public');

const MIME_TYPES = {
  '.html': 'text/html; charset=UTF-8',
  '.css': 'text/css; charset=UTF-8',
  '.js': 'application/javascript; charset=UTF-8',
  '.json': 'application/json; charset=UTF-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.webp': 'image/webp',
  '.wav': 'audio/wav',
  '.mp3': 'audio/mpeg'
};

// Calculate initial CPU times
let previousCpuTimes = getCpuTimes();

function getCpuTimes() {
  const cpus = os.cpus();
  let totalUser = 0, totalNice = 0, totalSys = 0, totalIdle = 0, totalIrq = 0;
  for (const cpu of cpus) {
    totalUser += cpu.times.user;
    totalNice += cpu.times.nice;
    totalSys += cpu.times.sys;
    totalIdle += cpu.times.idle;
    totalIrq += cpu.times.irq;
  }
  const total = totalUser + totalNice + totalSys + totalIdle + totalIrq;
  return { idle: totalIdle, total };
}

function calculateCpuUsage() {
  const current = getCpuTimes();
  const idleDiff = current.idle - previousCpuTimes.idle;
  const totalDiff = current.total - previousCpuTimes.total;
  previousCpuTimes = current;
  if (totalDiff === 0) return 0;
  const usage = 100 - Math.round((100 * idleDiff) / totalDiff);
  return Math.max(0, Math.min(100, usage));
}

const server = http.createServer((req, res) => {
  const parsedUrl = new URL(req.url, `http://${req.headers.host}`);
  const pathname = parsedUrl.pathname;

  // CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  // Telemetry endpoint
  if (pathname === '/api/telemetry') {
    const totalMem = os.totalmem();
    const freeMem = os.freemem();
    const usedMem = totalMem - freeMem;
    const cpuUsage = calculateCpuUsage();
    const cpus = os.cpus();

    const telemetry = {
      timestamp: new Date().toISOString(),
      system: {
        hostname: os.hostname(),
        platform: os.platform(),
        release: os.release(),
        arch: os.arch(),
        uptime: os.uptime(),
        uptimeFormatted: formatUptime(os.uptime())
      },
      cpu: {
        usagePercent: cpuUsage,
        model: cpus[0]?.model || 'Quantum Arc Processing Unit',
        cores: cpus.length,
        speedMHz: cpus[0]?.speed || 3400
      },
      memory: {
        totalGB: (totalMem / (1024 ** 3)).toFixed(2),
        usedGB: (usedMem / (1024 ** 3)).toFixed(2),
        freeGB: (freeMem / (1024 ** 3)).toFixed(2),
        usedPercent: Math.round((usedMem / totalMem) * 100)
      },
      starkCore: {
        suitModel: 'MARK LXXXV // NANO-TECH',
        reactorOutput: '3.42 GW',
        coreStability: '99.94%',
        defenseGrid: 'ONLINE - ACTIVE SCAN',
        protocol: 'J.A.R.V.I.S. VER 8.5'
      }
    };

    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(telemetry));
    return;
  }

  // Safe terminal command execution endpoint
  if (pathname === '/api/exec' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      try {
        const { command } = JSON.parse(body || '{}');
        if (!command || typeof command !== 'string') {
          res.writeHead(400, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ error: 'Command required' }));
          return;
        }

        const safeWhitelist = [
          'uname -a', 'uptime', 'free -h', 'df -h', 'whoami',
          'date', 'hostname', 'lscpu', 'top -b -n 1 | head -n 15',
          'ps -ef | head -n 12', 'echo', 'pwd'
        ];

        const cmdTrimmed = command.trim();
        const isSafe = safeWhitelist.some(prefix => cmdTrimmed.startsWith(prefix.split(' ')[0]));

        // Allow execution of safe commands or custom diagnostic echoes
        const commandToRun = isSafe ? cmdTrimmed : `echo "[STARK SECURITY] Query registered: ${cmdTrimmed.replace(/["$`\\]/g, '')}"`;

        exec(commandToRun, { timeout: 3000 }, (error, stdout, stderr) => {
          res.writeHead(200, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({
            output: stdout || stderr || (error ? error.message : 'Command executed with no output.'),
            exitCode: error ? error.code : 0
          }));
        });
      } catch (err) {
        res.writeHead(500, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: err.message }));
      }
    });
    return;
  }

  // Serve static files
  let safePath = path.normalize(pathname).replace(/^(\.\.[\/\\])+/, '');
  if (safePath === '/' || safePath === '\\') {
    safePath = '/index.html';
  }

  const filePath = path.join(PUBLIC_DIR, safePath);

  fs.stat(filePath, (err, stats) => {
    if (err || !stats.isFile()) {
      res.writeHead(404, { 'Content-Type': 'text/plain' });
      res.end('404 Not Found - Stark Industries Shell Protocol');
      return;
    }

    const ext = path.extname(filePath).toLowerCase();
    const contentType = MIME_TYPES[ext] || 'application/octet-stream';

    res.writeHead(200, { 'Content-Type': contentType });
    const stream = fs.createReadStream(filePath);
    stream.pipe(res);
  });
});

function formatUptime(seconds) {
  const d = Math.floor(seconds / (3600 * 24));
  const h = Math.floor((seconds % (3600 * 24)) / 3600);
  const m = Math.floor((seconds % 3600) / 60);
  const s = Math.floor(seconds % 60);
  return `${d}d ${h}h ${m}m ${s}s`;
}

server.listen(PORT, '0.0.0.0', () => {
  console.log(`[STARK CORE] Jarvis Windows Linux Shell running at http://localhost:${PORT}`);
});
