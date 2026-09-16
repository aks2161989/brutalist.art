import React from 'react';
import {AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import {CLAUDE as C, CLAUDE_FONT as F} from '../tokens/claude';

/** Source-backed Godot developer teaching views: readable Script excerpts with
 * line highlights, Local/Remote scene anatomy, actual asset/engine previews,
 * and Inspector/resource evidence. This is explicitly reconstructed editor
 * chrome, not an invented live session. Portrait stacks the docks natively.
 * Supply every source line/property/result; no fictional project defaults.
 */
export const godotDevWorkbenchSchema=z.object({
  mode:z.enum(['code','tree','asset','trace']),
  title:z.string(), project:z.string(), path:z.string().default(''),
  source:z.string(), code:z.string().default(''), startLine:z.number().int().positive().default(1),
  codeFontSize:z.number().min(23).max(40).optional(),
  treeLabel:z.string().default('Scene'), tree:z.array(z.string()).default([]),
  inspectorLabel:z.string().default('Source notes — not Inspector values'),
  notes:z.array(z.object({label:z.string(),value:z.string()})).default([]),
  cues:z.array(z.object({at:z.number().nonnegative(),line:z.number().int().positive(),label:z.string()})).default([]),
  image:z.string().default(''),imageLabel:z.string().default(''),
  output:z.array(z.string()).default([]), durationSeconds:z.number().positive().default(15),
});
export type GodotDevWorkbenchProps=z.infer<typeof godotDevWorkbenchSchema>;

const colors={bg:'#202531',dock:'#2b3240',bar:'#343d4d',text:'#edf1f7',muted:'#bec8d7',blue:'#8bc7f3',line:'#354052',mark:'#455a71'};
function syntax(line:string){
  const bits=line.split(/("[^"\n]*"|'[^'\n]*'|#[^\n]*|\b(?:func|var|const|if|elif|else|return|for|in|extends|enum|true|false|and|or|not|await|class_name)\b|@export|\b\d+(?:\.\d+)?\b)/g);
  return bits.map((s,i)=><span key={i} style={{color:s.startsWith('#')?'#bac5bc':/^['"]/.test(s)?'#ece0a1':/^\d/.test(s)?'#aee7d1':/^(func|var|const|if|elif|else|return|for|in|extends|enum|true|false|and|or|not|await|@export)$/.test(s)?'#f39bce':colors.text}}>{s}</span>);
}

export const GodotDevWorkbench:React.FC<GodotDevWorkbenchProps>=(p)=>{
 const {width,height,fps}=useVideoConfig(),frame=useCurrentFrame(),t=frame/fps,portrait=height>width;
 const pad=width*.055,bodyTop=height*.16,bodyBottom=height*.12;
 const current=[...p.cues].reverse().find(c=>t>=c.at);
 const panel={background:colors.bg,border:`2px solid ${colors.line}`,minWidth:0};
 const heading={fontFamily:F.ui,fontSize:24,padding:'15px 20px',background:colors.bar,color:colors.text};
 const notes=<div style={{...panel,overflow:'hidden'}}>
  <div style={{...heading,fontSize:23}}>{p.inspectorLabel}</div>
  <div style={{padding:20,display:'flex',flexDirection:'column',gap:18}}>{p.notes.map(n=><div key={n.label} style={{padding:16,background:colors.dock,borderLeft:`4px solid ${colors.line}`}}>
    <div style={{fontSize:23,color:colors.muted,lineHeight:1.25}}>{n.label}</div>
    <div style={{fontSize:portrait?28:27,lineHeight:1.35,marginTop:10,color:colors.text,whiteSpace:'pre-wrap',overflowWrap:'anywhere'}}>{n.value}</div>
  </div>)}</div>
 </div>;
 const tree=<div style={{...panel,paddingBottom:20}}><div style={heading}>{p.treeLabel}</div><div style={{padding:'15px 20px'}}>{p.tree.map((n,i)=><div key={i} style={{fontSize:portrait?27:25,lineHeight:1.65,whiteSpace:'pre-wrap',overflowWrap:'anywhere',padding:'3px 10px',color:colors.text,background:current?.line===i+1?colors.mark:'transparent'}}>{n}</div>)}</div></div>;
 const code=<div style={{...panel,overflow:'hidden'}}><div style={{...heading,fontFamily:F.mono,fontSize:23,overflowWrap:'anywhere'}}>{p.path}</div>
   <div style={{padding:'18px 16px',fontFamily:F.mono,fontSize:portrait?Math.max(24,p.codeFontSize||23):p.codeFontSize||23,lineHeight:1.3}}>{p.code.split('\n').map((line,i)=>{
    const selected=current?.line===p.startLine+i;
    return <div key={i} data-code-line={p.startLine+i} style={{display:'grid',gridTemplateColumns:'58px 1fr',padding:'2px 6px',background:selected?colors.mark:'transparent',borderLeft:`4px solid ${selected?colors.blue:'transparent'}`}}>
     <span style={{color:colors.muted,userSelect:'none',fontSize:22}}>{p.startLine+i}</span><span style={{whiteSpace:'pre-wrap',overflowWrap:'anywhere',tabSize:2}}>{syntax(line.replace(/\t/g,'  '))}</span>
    </div>;
   })}</div>
 </div>;
 const image=<div style={{...panel,display:'flex',flexDirection:'column',minHeight:0}}><div style={heading}>{p.imageLabel}</div><div style={{position:'relative',flex:1,background:'#f6f3ec',padding:18,display:'flex',alignItems:'center',justifyContent:'center'}}>
  {p.image&&<Img src={p.image.startsWith('data:')?p.image:staticFile(p.image)} style={{position:'absolute',inset:18,width:'calc(100% - 36px)',height:'calc(100% - 36px)',objectFit:'contain'}}/>}
 </div></div>;
 const columns=p.mode==='tree'?'1fr 1fr':p.mode==='asset'?'1.08fr .92fr':'minmax(0,1fr) 390px';
 const lower=interpolate(t,[0,.35],[.45,1],{extrapolateLeft:'clamp',extrapolateRight:'clamp'});
 return <AbsoluteFill style={{background:C.PAGE,color:colors.text,fontFamily:F.ui}}>
  <div style={{position:'absolute',left:pad,right:pad,top:height*.045,fontFamily:F.serif,fontSize:portrait?62:60,lineHeight:1.1,color:C.INK}}>{p.title}</div>
  <div style={{position:'absolute',left:pad,right:pad,top:bodyTop,bottom:bodyBottom,background:colors.bg,borderRadius:14,overflow:'hidden',border:`2px solid ${colors.line}`}}>
   <div style={{height:52,background:colors.bar,display:'flex',alignItems:'center',justifyContent:'space-between',padding:'0 24px',fontSize:24}}><strong>Godot · {p.project}</strong><span>{portrait?'2D · Script':'Scene   Project   Debug   Editor     |     2D   3D   Script'}</span></div>
   <div style={{height:48,padding:'10px 24px',boxSizing:'border-box',background:colors.dock,fontSize:23,color:colors.blue}}>Godot editor reconstruction · source-backed teaching view</div>
   <div style={{position:'absolute',top:100,bottom:90,left:0,right:0,display:'grid',gridTemplateColumns:portrait?'1fr':columns,gridTemplateRows:portrait?'1fr .85fr':'1fr',gap:10,padding:12}}>
    {p.mode==='tree'?<>{tree}{notes}</>:p.mode==='asset'?<>{code}{image}</>:p.mode==='trace'?<>{tree}{notes}</>:<>{code}{notes}</>}
   </div>
   <div style={{position:'absolute',left:16,right:16,bottom:10,height:68,background:colors.dock,padding:'10px 18px',boxSizing:'border-box',fontSize:23,lineHeight:1.2,opacity:lower}}>
    <div style={{color:colors.blue,marginBottom:7}}>{current?.label||'Read the source, then follow the result.'}</div>
    <div style={{color:colors.muted,fontSize:21}}>{p.output.join(' · ')}</div>
   </div>
  </div>
  <div style={{position:'absolute',left:pad,bottom:portrait?height*.048+60:height*.048,maxWidth:portrait?width*.88:width*.72,fontSize:23,lineHeight:1.25,color:C.INK_SOFT,overflowWrap:'anywhere'}}>{p.source}</div>
  <div style={{position:'absolute',right:pad,bottom:portrait?height*.035:height*.048,fontFamily:F.serif,fontSize:28,color:C.INK}}>@NikBearBrown</div>
 </AbsoluteFill>;
};
