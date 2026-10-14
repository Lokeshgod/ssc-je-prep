import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
const root=path.resolve(import.meta.dirname,'..'), dist=path.join(root,'dist');
const context={window:{}};vm.createContext(context);
vm.runInContext(fs.readFileSync(path.join(dist,'content.js'),'utf8'),context);
vm.runInContext(fs.readFileSync(path.join(dist,'state.js'),'utf8'),context);
const D=context.window.STUDY_DATA,S=context.window.StudyState;
const ids=new Set(D.chapters.map(c=>c.id));assert.equal(ids.size,D.chapters.length);
const subjectIds=new Set(D.subjects.map(s=>s.id));assert.equal(subjectIds.size,7);
const sourceIds=new Set(D.sources.map(s=>s.id));
let pcount=0,mcount=0,wordCount=0;const qids=new Set();
for(const c of D.chapters){
 assert(subjectIds.has(c.subject));assert(c.words>=300,`${c.id} too short`);wordCount+=c.words;
 assert(c.headings.length>=3);assert(c.html.includes('<h2'));
 assert(fs.existsSync(path.join(dist,'notes',c.id+'.md')));
 if(c.diagram)assert(fs.existsSync(path.join(dist,'assets',c.diagram+'.svg')));
 for(const match of c.html.matchAll(/src="([^"]+)"/g))assert(fs.existsSync(path.join(dist,match[1])),match[1]);
 for(const q of c.practice){assert(!qids.has(q.id));qids.add(q.id);assert.equal(q.options.length,4);assert(new Set(q.options).size===4);assert(Number.isInteger(q.answer)&&q.answer>=0&&q.answer<4);assert(q.explanation.length>10);pcount++;}
 for(const m of c.models){assert(m.solution.length>15);assert(m.tag);mcount++;}
}
for(const q of D.pyqs){assert(ids.has(q.chapter));assert(sourceIds.has(q.source));assert(!qids.has(q.id));qids.add(q.id);assert(q.q>0&&q.page>0);}
assert.equal(D.pyqs.length,44);assert.equal(pcount,79);assert.equal(mcount,63);
for(const s of D.sources)assert(s.url.startsWith('https://'));
const index=fs.readFileSync(path.join(dist,'index.html'),'utf8');
for(const m of index.matchAll(/(?:src|href)="([^"#]+)"/g)){if(!m[1].startsWith('http'))assert(fs.existsSync(path.join(dist,m[1])),m[1]);}
const app=fs.readFileSync(path.join(dist,'app.js'),'utf8');
for(const m of app.matchAll(/(?:href|src)="((?:materials|assets)\/[^"$]+)"/g))assert(fs.existsSync(path.join(dist,m[1])),m[1]);
assert(!app.includes('data-study-day'));
// Target boundary uses IST, never the visitor's local timezone.
const target=Date.parse('2026-10-29T18:30:00Z');
assert.equal(S.countdown(target-86400000).days,1);assert.equal(S.countdown(target-1000).seconds,1);assert(S.countdown(target).finished);assert.equal(S.countdown(target+1).days,0);
const q=D.chapters[0].practice[0];const backup={version:1,complete:['transformers','transformers','unknown'],saved:['ac'],nontechnical:['reasoning-0','bad'],answers:{[q.id]:q.answer,bad:0},pyqStatus:{[D.pyqs[0].id]:'revise',bad:'right'},notes:{transformers:'<script>note text</script>',bad:'ignored'}};
const state=S.clean(backup,D);assert.equal(state.complete.length,1);assert.equal(state.nontechnical.length,1);assert.equal(Object.keys(state.answers).length,1);assert.equal(state.notes.transformers,backup.notes.transformers);assert(!state.notes.bad);
assert.equal(S.score(state,[q]).marks,1);state.answers[q.id]=(q.answer+1)%4;assert.equal(S.score(state,[q]).marks,-.25);assert.equal(S.mistakes(state,D).length,2);
const roundtrip=S.clean(JSON.parse(JSON.stringify(state)),D);assert.equal(JSON.stringify(roundtrip),JSON.stringify(state));assert.throws(()=>S.clean({version:2},D));
assert.equal(S.evidence('coupled-coils',D).papers,2);assert.equal(S.evidence('coupled-coils',D).questions.length,4);assert.equal(S.evidence('not-a-tag',D).papers,0);
// Check the numerical results used by the worked models and sourced examples.
const near=(a,b)=>assert(Math.abs(a-b)<1e-8,`${a} != ${b}`);
near(Math.sqrt(400/1600),.5);near(Math.sqrt(1-.6**2),.8);near(120/125,.96);near(.8-.6*4,-1.6);
near(200-20*.5,190);near((1500-1440)/1500,.04);near(.04*50,2);near((1-.05)*20,19);
near(.4*Math.sqrt(8*32),6.4);near((38-12)/4,6.5);near((4-2)/4,.5);near(Math.sqrt(20*320),80);
near((2**2+3**2+5**2)/2,19);near(400/5*Math.sqrt(400/4),800);near(10*(30*2**2-5),1150);
near(2*2*3.6e6/100**2,1440);near((12-3)/.036,250);near(40/(5+15),2);near(300/5,60);
near(8*(1-(-2)/(-4))**2,2);near(100/(1+100*.09),10);near(60*1000/200,300);
near(1-24/60,.6);near(-.25/(1-.25)*12,-4);near(800/1600,.5);near(10000/(2000*.5*.8),12.5);
console.log(`PASS: ${D.chapters.length} chapters, ${wordCount} note words, ${mcount} models, ${pcount} practice questions, ${D.pyqs.length} PYQ concepts. Assets, backups, scoring, countdown and numerical checks passed.`);

await import('./check-render.mjs');
