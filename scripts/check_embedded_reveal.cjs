const {chromium}=require('playwright');const fs=require('fs'),path=require('path'),p=process.env.TL_EVIDENCE_DIR||path.resolve(__dirname,'../.tmp-embedded-reveal');fs.mkdirSync(p,{recursive:true});
const mode=process.argv[2]||'candidate',app=path.resolve(__dirname,'../dashboard/app.js');
(async()=>{const browser=await chromium.launch({headless:true,args:['--mute-audio','--autoplay-policy=user-gesture-required']});const records=[];let error=null;
try{for(const [name,width,height,delay]of [['phone-fast1',390,844,800],['phone-fast2',390,844,800],['phone-normal',390,844,150],['desktop-fast',1280,800,800],['desktop-normal',1280,800,150]]){
 const c=await browser.newContext({viewport:{width,height}});await c.route('**/*',r=>r.request().resourceType()==='media'?r.abort():r.continue());await c.addInitScript(()=>{const m=()=>document.querySelectorAll('video,audio').forEach(x=>{x.muted=true;x.volume=0;x.pause()});new MutationObserver(m).observe(document,{subtree:true,childList:true});document.addEventListener('play',m,true);window.__tlLastResize=performance.now();addEventListener('message',e=>{if(e.origin==='https://local-service-spotlight.github.io'&&(e.data?.btlH||e.data?.btlRevealY))window.__tlLastResize=performance.now();});});
 if(mode==='candidate')await c.route('**/task-library/app.js',r=>r.fulfill({path:app,contentType:'text/javascript'}));
 if(delay!==150)await c.route('https://local-service-spotlight.github.io/task-library/',async r=>{const x=await r.fetch();const s=await x.text();if(!s.includes('setTimeout(measure, 150)'))throw Error('height source changed');await r.fulfill({response:x,body:s.replace('setTimeout(measure, 150)',`setTimeout(measure, ${delay})`)});});
 const page=await c.newPage();await page.goto('https://blitzmetrics.com/task-library-dashboard/',{waitUntil:'domcontentloaded',timeout:30000});const frame=page.locator('#btlframe').contentFrame();await frame.locator('#btl-q').fill('upload-processed-video-to-youtube');const row=frame.locator('#task-upload-processed-video-to-youtube');
 const rec={name,delay,mediaMuted:true,checks:[]};records.push(rec);
 for(let attempt=0;attempt<2;attempt++){
  await row.getByRole('button',{name:'Open guide',exact:true}).click();await frame.locator('#btl-modal:not([hidden])').waitFor();await page.waitForTimeout(delay+500);
  const boxes={panel:await frame.locator('.btl-m-panel').boundingBox(),copy:await frame.locator('#btl-m-copy').boundingBox(),prompt:await frame.locator('#btl-m-start').boundingBox().catch(()=>null)};
  const pass=boxes.panel&&boxes.panel.y>=0&&boxes.panel.y+boxes.panel.height<=height&&boxes.copy.y>=0&&boxes.copy.y+boxes.copy.height<=height&&boxes.prompt&&boxes.prompt.y>=0&&boxes.prompt.y+boxes.prompt.height<=height;rec.checks.push({attempt,phase:'open',pass,boxes});if(!pass)throw Error(name+' open out of viewport');
  if(attempt===0)await page.screenshot({path:p+'/'+mode+'-'+name+'.png'});
  await page.waitForFunction(()=>performance.now()-window.__tlLastResize>350,{},{timeout:5000});const y=await page.evaluate(()=>scrollY);await frame.locator('#btl-m-body').evaluate(el=>{el.scrollTop=200;});await page.waitForTimeout(200);const after=await page.evaluate(()=>scrollY);if(Math.abs(y-after)>1)throw Error('Reading moved outer page: '+y+' to '+after);rec.checks.push({phase:'body-scroll',pass:true});
  await frame.locator('[data-close]').first().click();await page.waitForTimeout(delay+500);const rb=await row.getByRole('button',{name:'Open guide',exact:true}).boundingBox();const closePass=rb&&rb.y>=0&&rb.y+rb.height<=height;rec.checks.push({phase:'close',pass:closePass,row:rb});if(!closePass)throw Error(name+' return row out of viewport');
 }
 await c.close();
}}catch(e){error=String(e);console.error(error);process.exitCode=1;}finally{await browser.close();fs.writeFileSync(p+'/'+mode+'-reveal-checks.json',JSON.stringify({at:new Date().toISOString(),mode,scope:'Agent browser regression; not novice-human first-use success',records,error},null,2));}
})();
