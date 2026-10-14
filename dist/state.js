(function(root){
'use strict';
const TARGET='2026-10-30T00:00:00+05:30';
function fresh(){return {version:1,complete:[],saved:[],nontechnical:[],answers:{},pyqStatus:{},notes:{}}}
function clean(input,data){
 if(!input||input.version!==1||typeof input!=='object')throw Error('This is not a Study Desk backup (version 1).');
 for(const key of ['complete','saved','nontechnical'])if(!Array.isArray(input[key]))throw Error('Backup list '+key+' is missing or invalid.');
 for(const key of ['answers','pyqStatus','notes'])if(!input[key]||typeof input[key]!=='object'||Array.isArray(input[key]))throw Error('Backup section '+key+' is missing or invalid.');
 const chapters=new Set(data.chapters.map(c=>c.id));const questions=new Map(data.chapters.flatMap(c=>c.practice).map(q=>[q.id,q]));const pyqs=new Set(data.pyqs.map(q=>q.id));
 const non=new Set(data.nontechnical.flatMap(s=>s.topics.map((_,i)=>s.id+'-'+i)));
 const list=(v,allowed)=>Array.isArray(v)?[...new Set(v.filter(x=>typeof x==='string'&&allowed.has(x)))]:[];
 const s=fresh();s.complete=list(input.complete,chapters);s.saved=list(input.saved,chapters);s.nontechnical=list(input.nontechnical,non);
 for(const [id,a] of Object.entries(input.answers||{})){let q=questions.get(id);if(q&&Number.isInteger(a)&&a>=0&&a<q.options.length)s.answers[id]=a;}
 for(const [id,a] of Object.entries(input.pyqStatus||{}))if(pyqs.has(id)&&['right','revise'].includes(a))s.pyqStatus[id]=a;
 for(const [id,n] of Object.entries(input.notes||{}))if(chapters.has(id)&&typeof n==='string')s.notes[id]=n.slice(0,20000);
 return s;
}
function countdown(now){let delta=Math.max(0,new Date(TARGET).getTime()-now);let seconds=Math.floor(delta/1000);return {days:Math.floor(seconds/86400),hours:Math.floor(seconds/3600)%24,minutes:Math.floor(seconds/60)%60,seconds:seconds%60,finished:delta===0};}
function mistakes(state,data){return [...data.chapters.flatMap(c=>c.practice).filter(q=>Object.hasOwn(state.answers,q.id)&&state.answers[q.id]!==q.answer).map(q=>q.id),...data.pyqs.filter(q=>state.pyqStatus[q.id]==='revise').map(q=>q.id)];}
function evidence(tag,data){const qs=data.pyqs.filter(q=>q.model===tag);return {questions:qs,papers:new Set(qs.map(q=>q.source)).size};}
function score(state,questions){const attempted=questions.filter(q=>Object.hasOwn(state.answers,q.id));const correct=attempted.filter(q=>state.answers[q.id]===q.answer).length;return {attempted:attempted.length,correct,wrong:attempted.length-correct,marks:correct-.25*(attempted.length-correct)};}
root.StudyState={fresh,clean,countdown,mistakes,evidence,score};
})(typeof window!=='undefined'?window:globalThis);
