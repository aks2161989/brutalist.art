import React from 'react';
import {AbsoluteFill, Img, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import {CLAUDE as C, CLAUDE_FONT as F} from '../tokens/claude';

/** GDD teaching view: exact source excerpt beside explicitly labeled design
 * diagrams, status comparisons or real engine evidence. No invented defaults.
 * Diagram geometry is explanatory, not a screenshot or playable level. */
export const godotDesignBoardSchema=z.object({
 title:z.string(),section:z.string(),excerpt:z.string(),source:z.string(),
 status:z.string(),visualLabel:z.string(),
 layout:z.enum(['cards','flow','zones','jump','image']).default('cards'),
 cards:z.array(z.object({label:z.string(),text:z.string()})).min(1).max(4),
 cues:z.array(z.object({at:z.number().nonnegative(),card:z.number().int().nonnegative()})).default([]),
 image:z.string().default(''),
 jump:z.object({speed:z.number().positive(),launch:z.number().positive(),gravity:z.number().positive()}).optional(),
 durationSeconds:z.number().positive().default(20),
});
export const GodotDesignBoard:React.FC<z.infer<typeof godotDesignBoardSchema>>=(p)=>{
 const {width,height,fps}=useVideoConfig(),frame=useCurrentFrame(),portrait=height>width;
 const current=[...p.cues].reverse().find(c=>frame/fps>=c.at)?.card ?? -1;
 const pad=width*.055;
 const card=(v:typeof p.cards[number],i:number)=><div key={i} style={{padding:20,border:`2px solid ${i===current?'#985039':'#ccc6ba'}`,borderLeft:`7px solid ${i===current?'#985039':'#ccc6ba'}`,background:i===current?'#f2e5d8':'#fffdf8',borderRadius:12,minWidth:0}}>
   <div style={{fontSize:portrait?30:29,fontWeight:700,color:'#663725',lineHeight:1.2}}>{v.label}</div>
   <div style={{fontSize:portrait?29:28,lineHeight:1.3,marginTop:10,whiteSpace:'pre-wrap'}}>{v.text}</div>
 </div>;
 let visual:React.ReactNode;
 if(p.layout==='jump'&&p.jump){
  const {speed,launch,gravity}=p.jump,flight=2*launch/gravity,range=speed*flight,apex=launch*launch/(2*gravity);
  const points=Array.from({length:61},(_,i)=>{const t=flight*i/60;return `${55+660*i/60},${290-(launch*t-.5*gravity*t*t)/apex*210}`}).join(' ');
  visual=<svg viewBox="0 0 800 380" style={{width:'100%',height:portrait?380:330}} aria-label="Continuous same-height jump model">
   <path d="M55 40V290H750" fill="none" stroke="#5d655c" strokeWidth="3"/>
   <path d="M55 80H715" fill="none" stroke="#aaa394" strokeWidth="2" strokeDasharray="8 8"/>
   <polyline points={points} fill="none" stroke="#8f452d" strokeWidth="6"/>
   <text x="385" y="55" textAnchor="middle" fontSize="29" fill="#342d24">apex {apex.toFixed(1)} px</text>
   <text x="385" y="335" textAnchor="middle" fontSize="29" fill="#342d24">range {range.toFixed(1)} px · full-speed model</text>
   <text x="55" y="365" fontSize="24" fill="#342d24">Horizontal distance → · height above launch ↑</text>
  </svg>;
 }else if(p.layout==='image'){
  visual=<div style={{position:'relative',height:portrait?430:370,background:'#e7e6dc',borderRadius:12}}><Img src={p.image.startsWith('data:')?p.image:staticFile(p.image)} style={{width:'100%',height:'100%',objectFit:'contain'}}/></div>;
 }else if(p.layout==='zones'){
  visual=<div style={{display:'grid',gridTemplateColumns:portrait?'1fr':'repeat(3,1fr)',gap:10,margin:'25px 0'}}>{p.cards.map((v,i)=><div key={i} style={{minHeight:portrait?85:170,background:['#dce6d6','#f0dfbe','#e8d7ce'][i%3],padding:20,border:'2px solid #a99c87',display:'flex',alignItems:'center',fontSize:29,lineHeight:1.3}}>{i+1}. {v.label}</div>)}</div>;
 }
 const cards=<div style={{display:'flex',flexDirection:'column',gap:p.layout==='flow'?7:14}}>{p.cards.map((v,i)=><React.Fragment key={i}>{card(v,i)}{p.layout==='flow'&&i<p.cards.length-1&&<div style={{textAlign:'center',fontSize:28,lineHeight:1,color:'#663725'}}>↓</div>}</React.Fragment>)}</div>;
 return <AbsoluteFill style={{background:C.PAGE,color:C.INK,fontFamily:F.ui}}>
  <div style={{position:'absolute',top:portrait?height*.055:height*.045,left:pad,right:pad,fontFamily:F.serif,fontSize:portrait?60:59,lineHeight:1.12}}>{p.title}</div>
  <div style={{position:'absolute',left:pad,right:pad,top:height*.14,bottom:height*.12,display:'grid',gridTemplateColumns:portrait?'1fr':'0.84fr 1.16fr',gridTemplateRows:portrait?'auto 1fr':'1fr',gap:25}}>
   <div style={{background:'#fffdf8',border:'2px solid #cfc6b5',borderRadius:15,padding:32,display:'flex',flexDirection:'column',minWidth:0}}>
    <div style={{fontSize:24,fontWeight:700,color:'#665546',marginBottom:22}}>GDD · DOCUMENT EXCERPT</div>
    <div style={{fontFamily:F.serif,fontSize:portrait?36:40,lineHeight:1.15,marginBottom:25}}>{p.section}</div>
    <div style={{borderLeft:'5px solid #985039',paddingLeft:22,fontSize:portrait?29:31,lineHeight:1.4,whiteSpace:'pre-wrap',overflowWrap:'anywhere'}}>{p.excerpt}</div>
    <div style={{marginTop:'auto',paddingTop:24,fontSize:24,lineHeight:1.35,color:'#564739'}}>Reconstructed reading view.<br/>Exact excerpt; interpretation at right.</div>
   </div>
   <div style={{minWidth:0,display:'flex',flexDirection:'column',gap:16}}>
    <div style={{background:'#303d34',color:'#fffdf8',padding:'14px 22px',borderRadius:10,fontSize:25,lineHeight:1.25,fontWeight:700}}>{p.status}</div>
    <div style={{fontSize:24,color:'#564739',lineHeight:1.25}}>{p.visualLabel}</div>
    {visual}{cards}
   </div>
  </div>
  <div style={{position:'absolute',left:pad,bottom:height*.045+(portrait?45:0),maxWidth:portrait?width*.88:width*.74,fontSize:23,color:'#564739',lineHeight:1.25}}>{p.source}</div>
  <div style={{position:'absolute',right:pad,bottom:portrait?height*.055:height*.04,fontSize:28,fontFamily:F.serif}}>@NikBearBrown</div>
 </AbsoluteFill>;
};
