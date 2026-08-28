// Full-page screenshot via headless Chromium over raw CDP.
// usage: node shot.js <file.html> <out.png> [dark] [width]
const { spawn } = require('child_process');
const fs = require('fs'), path = require('path'), os = require('os');
const CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome';
const [,,inFile,outFile,theme='light',width='1280']=process.argv;
const PORT=9800+(process.pid%400), userDir=fs.mkdtempSync(path.join(os.tmpdir(),'shot-'));
const chrome=spawn(CHROME,['--headless=new','--disable-gpu','--no-sandbox','--disable-dev-shm-usage',
  '--force-color-profile=srgb','--hide-scrollbars',`--user-data-dir=${userDir}`,
  `--remote-debugging-port=${PORT}`,'about:blank'],{stdio:['ignore','ignore','ignore']});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
async function getJSON(u,t=80){for(let i=0;i<t;i++){try{const r=await fetch(u);if(r.ok)return r.json();}catch(e){}await sleep(150);}throw new Error('no devtools');}
class CDP{constructor(ws){this.ws=ws;this.id=0;this.p=new Map();this.h=new Map();
  ws.addEventListener('message',e=>{const m=JSON.parse(e.data);
    if(m.id&&this.p.has(m.id)){const{res,rej}=this.p.get(m.id);this.p.delete(m.id);m.error?rej(new Error(JSON.stringify(m.error))):res(m.result);}
    else if(m.method&&this.h.has(m.method))this.h.get(m.method).forEach(f=>f(m.params));});}
  send(method,params={},sessionId){const id=++this.id;const pl={id,method,params};if(sessionId)pl.sessionId=sessionId;
    return new Promise((res,rej)=>{this.p.set(id,{res,rej});this.ws.send(JSON.stringify(pl));});}
  on(m,f){if(!this.h.has(m))this.h.set(m,[]);this.h.get(m).push(f);}}
(async()=>{
  const v=await getJSON(`http://127.0.0.1:${PORT}/json/version`);
  const ws=await new Promise((res,rej)=>{const w=new WebSocket(v.webSocketDebuggerUrl);
    w.addEventListener('open',()=>res(w));w.addEventListener('error',e=>rej(new Error('ws')));});
  const cdp=new CDP(ws);
  const {targetId}=await cdp.send('Target.createTarget',{url:'about:blank'});
  const {sessionId}=await cdp.send('Target.attachToTarget',{targetId,flatten:true});
  await cdp.send('Page.enable',{},sessionId);
  await cdp.send('Runtime.enable',{},sessionId);
  await cdp.send('Emulation.setDeviceMetricsOverride',
    {width:+width,height:1200,deviceScaleFactor:1,mobile:false},sessionId);
  if(theme==='dark'||theme==='light')
    await cdp.send('Emulation.setEmulatedMedia',{features:[{name:'prefers-color-scheme',value:theme}]},sessionId);
  const loaded=new Promise(r=>cdp.on('Page.loadEventFired',r));
  await cdp.send('Page.navigate',{url:'file://'+path.resolve(inFile)},sessionId);
  await Promise.race([loaded,sleep(20000)]);
  await cdp.send('Runtime.evaluate',{expression:'document.fonts?document.fonts.ready.then(()=>1):1',awaitPromise:true},sessionId);
  await sleep(900);
  // Scroll the whole page first: reveal animations are IntersectionObserver-driven and
  // never fire for below-the-fold content in a single beyond-viewport capture.
  await cdp.send('Runtime.evaluate',{expression:`(async()=>{
    const H=document.body.scrollHeight, step=Math.floor(innerHeight*0.7);
    for(let y=0;y<H;y+=step){ scrollTo(0,y); await new Promise(r=>setTimeout(r,90)); }
    scrollTo(0,0); await new Promise(r=>setTimeout(r,500));
  })()`,awaitPromise:true},sessionId);
  const {data}=await cdp.send('Page.captureScreenshot',{format:'png',captureBeyondViewport:true},sessionId);
  fs.writeFileSync(outFile,Buffer.from(data,'base64'));
  console.log('OK',outFile,(fs.statSync(outFile).size/1024|0)+'KB');
  ws.close();chrome.kill('SIGKILL');fs.rmSync(userDir,{recursive:true,force:true});process.exit(0);
})().catch(e=>{console.error('FAIL',e.message);try{chrome.kill('SIGKILL');}catch(_){}process.exit(1);});
