// HTML -> PDF via headless Chromium over raw CDP. No npm dependencies.
// Usage: node render.js <input.html> <output.pdf> [--footer]
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const os = require('os');

const CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';
const [, , inFile, outFile, ...flags] = process.argv;
if (!inFile || !outFile) {
  console.error('usage: node render.js <input.html> <output.pdf> [--footer]');
  process.exit(1);
}
const wantFooter = flags.includes('--footer');

const PORT = 9333 + (process.pid % 500);
const userDir = fs.mkdtempSync(path.join(os.tmpdir(), 'chr-'));

const chrome = spawn(CHROME, [
  '--headless=new',
  '--disable-gpu',
  '--no-sandbox',
  '--disable-dev-shm-usage',
  '--font-render-hinting=none',
  '--force-color-profile=srgb',
  '--hide-scrollbars',
  `--user-data-dir=${userDir}`,
  `--remote-debugging-port=${PORT}`,
  'about:blank',
], { stdio: ['ignore', 'ignore', 'pipe'] });

let chromeErr = '';
chrome.stderr.on('data', (d) => { chromeErr += d.toString(); });

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function getJSON(url, tries = 60) {
  for (let i = 0; i < tries; i++) {
    try {
      const res = await fetch(url);
      if (res.ok) return await res.json();
    } catch (_) { /* not up yet */ }
    await sleep(150);
  }
  throw new Error('Chromium devtools endpoint never came up.\n' + chromeErr);
}

class CDP {
  constructor(ws) {
    this.ws = ws;
    this.id = 0;
    this.pending = new Map();
    this.handlers = new Map();
    ws.addEventListener('message', (ev) => {
      const msg = JSON.parse(ev.data);
      if (msg.id && this.pending.has(msg.id)) {
        const { resolve, reject } = this.pending.get(msg.id);
        this.pending.delete(msg.id);
        msg.error ? reject(new Error(JSON.stringify(msg.error))) : resolve(msg.result);
      } else if (msg.method && this.handlers.has(msg.method)) {
        this.handlers.get(msg.method).forEach((fn) => fn(msg.params));
      }
    });
  }
  send(method, params = {}, sessionId) {
    const id = ++this.id;
    const payload = { id, method, params };
    if (sessionId) payload.sessionId = sessionId;
    return new Promise((resolve, reject) => {
      this.pending.set(id, { resolve, reject });
      this.ws.send(JSON.stringify(payload));
    });
  }
  on(method, fn) {
    if (!this.handlers.has(method)) this.handlers.set(method, []);
    this.handlers.get(method).push(fn);
  }
}

function connect(url) {
  return new Promise((resolve, reject) => {
    const ws = new WebSocket(url);
    ws.addEventListener('open', () => resolve(ws));
    ws.addEventListener('error', (e) => reject(new Error('ws error: ' + e.message)));
  });
}

const FOOTER = `
<style>
  #f { font-family: Helvetica, Arial, sans-serif; font-size: 8px; color: #8a8f98;
       width: 100%; padding: 0 16mm; display: flex; justify-content: space-between; }
</style>
<div id="f">
  <span class="title"></span>
  <span><span class="pageNumber"></span> / <span class="totalPages"></span></span>
</div>`;

(async () => {
  const version = await getJSON(`http://127.0.0.1:${PORT}/json/version`);
  const ws = await connect(version.webSocketDebuggerUrl);
  const cdp = new CDP(ws);

  const { targetId } = await cdp.send('Target.createTarget', { url: 'about:blank' });
  const { sessionId } = await cdp.send('Target.attachToTarget', { targetId, flatten: true });

  await cdp.send('Page.enable', {}, sessionId);
  await cdp.send('Runtime.enable', {}, sessionId);

  const loaded = new Promise((resolve) => {
    cdp.on('Page.loadEventFired', resolve);
  });

  const fileUrl = 'file://' + path.resolve(inFile);
  await cdp.send('Page.navigate', { url: fileUrl }, sessionId);
  await Promise.race([loaded, sleep(30000)]);

  // Give web fonts + layout a beat to settle.
  await cdp.send('Runtime.evaluate', {
    expression: 'document.fonts ? document.fonts.ready.then(() => true) : true',
    awaitPromise: true,
  }, sessionId);
  await sleep(600);

  const opts = {
    printBackground: true,
    preferCSSPageSize: true,
    marginTop: 0, marginBottom: 0, marginLeft: 0, marginRight: 0,
    displayHeaderFooter: wantFooter,
  };
  if (wantFooter) {
    opts.headerTemplate = '<span></span>';
    opts.footerTemplate = FOOTER;
  }

  const { data } = await cdp.send('Page.printToPDF', opts, sessionId);
  fs.writeFileSync(outFile, Buffer.from(data, 'base64'));

  ws.close();
  chrome.kill('SIGKILL');
  fs.rmSync(userDir, { recursive: true, force: true });

  const kb = (fs.statSync(outFile).size / 1024).toFixed(0);
  console.log(`OK  ${outFile}  ${kb} KB`);
  process.exit(0);
})().catch((e) => {
  console.error('FAILED:', e.message);
  try { chrome.kill('SIGKILL'); } catch (_) {}
  process.exit(1);
});
