import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const dist=path.resolve(import.meta.dirname,'../dist');
// Render-function smoke checks in a JS VM, not a browser or a visual-layout test.
const nodes=new Map();
const node=id=>{if(!nodes.has(id))nodes.set(id,{innerHTML:'',textContent:'',style:{},classList:{add(){},remove(){}},addEventListener(){},focus(){},setAttribute(){},removeAttribute(){},click(){}});return nodes.get(id)};
const ctx={window:{addEventListener(){},scrollTo(){},print(){}},document:{getElementById:node,querySelectorAll(){return []},addEventListener(){},title:''},location:{hash:''},localStorage:{getItem(){return null},setItem(){}},setInterval(){},setTimeout(){},clearTimeout(){},console};
vm.createContext(ctx);
for(const file of ['content.js','state.js','app.js'])vm.runInContext(fs.readFileSync(path.join(dist,file),'utf8'),ctx,{filename:file});
const D=ctx.window.STUDY_DATA;
const hashes=['syllabus','subjects','pyqs','models','practice','review','downloads','sources','search/flux','search/%3Cscript%3E','missing',...D.subjects.map(s=>'subject/'+s.id),...D.pyqs.map(q=>'question/'+q.id),...D.chapters.flatMap(c=>['notes','pyqs','models','practice'].map(t=>'chapter/'+c.id+'/'+t))];
for(const hash of hashes){ctx.location.hash='#'+hash;vm.runInContext('render()',ctx);const html=node('main').innerHTML;assert(html.length>100,hash);assert(!html.includes('undefined'),hash);assert(!html.includes('<script>'),hash);assert(!html.includes('NaN'),hash);}
ctx.location.hash='#syllabus';vm.runInContext('render()',ctx);assert(node('main').innerHTML.indexOf('Your electrical syllabus')<node('main').innerHTML.indexOf('30 October 2026'));assert(node('main').innerHTML.includes('Waiting for your schedule photo.'));
ctx.location.hash='#chapter/transformers/notes';vm.runInContext('render()',ctx);assert(node('main').innerHTML.includes('V/f'));assert(node('main').innerHTML.includes('equation'));
console.log(`PASS: ${hashes.length} route render functions, escaped search text, syllabus ordering and schedule placeholder. Browser layout remains unverified.`);
