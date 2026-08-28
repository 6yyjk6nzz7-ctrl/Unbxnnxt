// Evaluate a JS expression against a local HTML file and print the result.
const { spawn } = require('child_process');
const fs=require('fs'),path=require('path'),os=require('os');
const CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome';
const [,,inFile,expr,width='390']=process.argv;
const PORT=9700+(process.pid%300), dir=fs.mkdtempSync(path.join(os.tmpdir(),'pr-'));
const ch=spawn(CHROME,['--headless=new','--disable-gpu','--no-sandbox','--disable-dev-shm-usage',
  `--user-data-dir=${dir}`,`--remote-debugging-port=${PORT}`,'about:blank'],{stdio:'ignore'});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
async function getJSON(u,t=80){for(let i=0;i<t;i++){try{const r=await fetch(u);if(r.ok)return r.json();}catch(e){}await sleep(150);}throw new Error('nope');}
class CDP{constructor(ws){this.ws=ws;this.id=0;this.p=new Map();this.h=new Map();
  ws.addEventListener('message',e=>{const m=JSON.parse(e.data);
    if(m.id&&this.p.has(m.id)){const{res,rej}=this.p.get(m.id);this.p.delete(m.id);m.error?rej(new Error(JSON.stringify(m.error))):res(m.result);}
    else if(m.method&&this.h.has(m.method))this.h.get(m.method).forEach(f=>f(m.params));});}
  send(method,params={},s){const id=++this.id;const pl={id,method,params};if(s)pl.sessionId=s;
    return new Promise((res,rej)=>{this.p.set(id,{res,rej});this.ws.send(JSON.stringify(pl));});}
  on(m,f){if(!this.h.has(m))this.h.set(m,[]);this.h.get(m).push(f);}}
(async()=>{
  const v=await getJSON(`http://127.0.0.1:${PORT}/json/version`);
  const ws=await new Promise((r,j)=>{const w=new WebSocket(v.webSocketDebuggerUrl);
    w.addEventListener('open',()=>r(w));w.addEventListener('error',()=>j(new Error('ws')));});
  const cdp=new CDP(ws);
  const {targetId}=await cdp.send('Target.createTarget',{url:'about:blank'});
  const {sessionId}=await cdp.send('Target.attachToTarget',{targetId,flatten:true});
  await cdp.send('Page.enable',{},sessionId); await cdp.send('Runtime.enable',{},sessionId);
  await cdp.send('Emulation.setDeviceMetricsOverride',{width:+width,height:900,deviceScaleFactor:1,mobile:false},sessionId);
  const loaded=new Promise(r=>cdp.on('Page.loadEventFired',r));
  await cdp.send('Page.navigate',{url:'file://'+path.resolve(inFile)},sessionId);
  await Promise.race([loaded,sleep(15000)]);
  await cdp.send('Runtime.evaluate',{expression:'document.fonts?document.fonts.ready.then(()=>1):1',awaitPromise:true},sessionId);
  await sleep(600);
  const r=await cdp.send('Runtime.evaluate',{expression:expr,returnByValue:true},sessionId);
  console.log(JSON.stringify(r.result.value,null,2));
  ws.close(); ch.kill('SIGKILL'); fs.rmSync(dir,{recursive:true,force:true}); process.exit(0);
})().catch(e=>{console.error('FAIL',e.message);try{ch.kill('SIGKILL');}catch(_){}process.exit(1);});
