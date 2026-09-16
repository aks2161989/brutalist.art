import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import {CLAUDE as C, CLAUDE_FONT as F} from '../tokens/claude';

/** Godot setup teaching surfaces: source-labeled download and project-manager
 * reconstructions, recorded terminal receipts, source diffs, and artifact flows.
 * Every displayed result is supplied by the reel, never an invented default.
 * Portrait reflows the content; neither aspect uses captured website artwork.
 */
export const walkerGodotSetupSchema = z.object({
  mode: z.enum(['download','manager','terminal','flow','diff','editor','comparison']),
  title: z.string(),
  sparkLine: z.string().default(''),
  source: z.string().default(''),
  command: z.string().default(''),
  lines: z.array(z.string()).default([]),
  labels: z.array(z.string()).default([]),
  details: z.array(z.string()).default([]),
  cueSeconds: z.array(z.number()).default([]),
  selected: z.number().default(0),
  version: z.string().default(''),
  durationSeconds: z.number().positive().default(12),
});
export type WalkerGodotSetupProps = z.infer<typeof walkerGodotSetupSchema>;

export const WalkerGodotSetup: React.FC<WalkerGodotSetupProps> = (p) => {
  const frame=useCurrentFrame(); const {fps,width,height}=useVideoConfig();
  const t=frame/fps, portrait=height>width;
  const pad=width*.065;
  const reveal=(i:number)=>interpolate(t,[(p.cueSeconds[i]??(.6+i*1.1)),(p.cueSeconds[i]??(.6+i*1.1))+.32],[.44,1],{extrapolateLeft:'clamp',extrapolateRight:'clamp'});
  const active=Math.max(0,p.cueSeconds.reduce((n,c,i)=>t>=c?i:n,0));
  const shell={position:'absolute' as const,left:pad,right:pad,top:height*.18,bottom:height*.15};
  const panel={background:C.CARD,border:`2px solid ${C.BORDER}`,borderRadius:18};
  const mono=portrait?30:32;
  const source=<div data-audit="source" style={{position:'absolute',left:pad,bottom:height*.065,fontFamily:F.ui,fontSize:24,color:C.INK_SOFT,maxWidth:width*.68,lineHeight:1.3}}>{p.source}</div>;
  const footer=<div data-audit="brand" style={{position:'absolute',right:pad,bottom:height*.065,fontFamily:F.serif,fontSize:28,color:C.INK,opacity:.65}}>@NikBearBrown</div>;
  const title=<div data-audit="title" style={{position:'absolute',left:pad,right:pad,top:height*.065,fontFamily:F.serif,fontSize:portrait?64:60,lineHeight:1.1,color:C.INK}}>{p.title}</div>;
  const spark=<div data-audit="spark" style={{position:'absolute',left:pad,top:height*.855,fontFamily:F.serif,fontSize:32,color:C.INK}}>{p.sparkLine}</div>;

  let content:React.ReactNode;
  if(p.mode==='download'){
    const chosen=p.selected;
    content=<div style={{...shell,top:height*.17,bottom:height*.15,background:'#252b46',borderRadius:18,overflow:'hidden',color:'white',fontFamily:F.ui}}>
      <svg width="100%" height="100%" viewBox="0 0 1700 740" preserveAspectRatio="none" style={{position:'absolute',opacity:.3}} aria-hidden="true">
        <path d="M0 650 L260 120 500 650 750 80 980 640 1280 160 1700 670V740H0Z" fill="#45686d"/>
        <path d="M0 740 L170 390 380 740 660 300 930 740 1270 330 1500 740Z" fill="#37564c"/>
      </svg>
      <div style={{position:'relative',display:'flex',justifyContent:'space-between',padding:'26px 36px',background:'#ffffff12',fontSize:26}}>
        <strong style={{fontSize:32}}>GODOT</strong><span>{portrait?'Download · Docs':'Features · Showcase · Community'}</span><span>Download</span>
      </div>
      <div style={{position:'relative',textAlign:'center',padding:portrait?'80px 25px':'35px 40px'}}>
        <div data-audit="download-heading" style={{fontSize:portrait?56:58,fontWeight:750,lineHeight:1.12,marginBottom:portrait?64:28}}>Download Godot 4<br/>for macOS</div>
        {[['Godot Engine','GDScript · regular build'],['Godot Engine – .NET','C# support · .NET SDK']].map(([name,note],i)=><div key={name} style={{margin:'0 auto 24px',maxWidth:850,opacity:reveal(i)}}>
          <div style={{display:'flex',borderRadius:12,overflow:'hidden',outline:chosen===i&&t>1?'4px solid #c6dff2':'4px solid transparent',background:i===0?'#478cbd':'#ffffff18',height:85,alignItems:'center',justifyContent:'space-between'}}>
            <strong data-audit={'download-button-'+i} style={{padding:'0 32px',fontSize:portrait?34:36}}>{name}</strong><span style={{background:'white',color:'#26334d',alignSelf:'stretch',display:'flex',alignItems:'center',padding:'0 26px',fontWeight:750,fontSize:32}}>{p.version}</span>
          </div>
          <div style={{fontSize:26,marginTop:12,color:'#e5e9f1'}}>Apple Silicon · Intel</div>
          {chosen===1&&<div style={{fontSize:28,marginTop:10}}>{note}</div>}
        </div>)}
      </div>
    </div>;
  } else if(p.mode==='manager') {
    content=<div style={{...shell,background:'#252525',borderRadius:18,color:'#ededed',fontFamily:F.ui,padding:portrait?'32px 36px':'25px 42px'}}>
      <div style={{fontSize:34,fontWeight:650,marginBottom:22}}>Create New Project</div>
      <div style={{display:'grid',gridTemplateColumns:portrait?'1fr':'1.25fr 1fr',gap:35}}>
        <div>
          <div style={{fontSize:28,marginBottom:12}}>Project Name</div>
          <div data-audit="project-name" style={{background:'#181818',border:'2px solid #529adb',padding:16,fontSize:36,borderRadius:7}}>walker-jumpman</div>
          <div style={{fontSize:28,margin:'24px 0 12px'}}>Project Path <span style={{float:'right',fontSize:25}}>Create Folder {p.selected===2?'OFF':'ON'}</span></div>
          <div data-audit="project-path" style={{background:'#181818',padding:18,fontSize:28,lineHeight:1.45,fontFamily:F.mono,borderRadius:7,overflowWrap:'anywhere'}}>{p.lines.map((x,i)=><div key={i}>{x}</div>)}</div>
          <div style={{fontSize:25,marginTop:18,color:'#bcdbc6'}}>Inspect the final path before creating.</div>
        </div>
        <div style={{paddingLeft:portrait?0:25}}>
          <div style={{fontSize:28,marginBottom:14}}>Renderer</div>
          {['Forward+','Mobile','Compatibility'].map((x,i)=><div key={x} style={{fontSize:34,padding:'15px 12px',background:i===(p.selected===1?2:0)?'#386589':'transparent',borderRadius:8,opacity:reveal(i)}}>{i===(p.selected===1?2:0)?'◉':'○'} {x}</div>)}
          <div style={{fontSize:28,marginTop:20}}>Version Control Metadata: Git</div>
          <div style={{fontSize:28,marginTop:24}}>☑ Edit Now</div>
        </div>
      </div>
      <div style={{display:'flex',justifyContent:'flex-end',marginTop:portrait?50:24}}><div style={{padding:'15px 70px',borderRadius:8,background:'#456b88',fontSize:30}}>Create</div></div>
    </div>;
  } else if(p.mode==='terminal') {
    content=<div style={{...shell,...panel,background:'#20242c',color:'#f2efe7',fontFamily:F.mono,overflow:'hidden'}}>
      <div style={{background:'#303641',padding:'23px 36px',fontFamily:F.ui,fontSize:26,display:'flex',gap:15,alignItems:'center'}}><span style={{color:'#e89c88'}}>●</span><span>Terminal · recorded output</span></div>
      <div style={{padding:'32px 40px'}}>
        <pre data-audit="command" style={{margin:'0 0 25px',fontFamily:'inherit',fontSize:mono,lineHeight:1.45,whiteSpace:'pre-wrap',overflowWrap:'anywhere',color:'#efd2bf'}}>{p.command}</pre>
        {p.lines.map((line,i)=><div data-audit={'output-'+i} key={i} style={{fontSize:mono,lineHeight:1.6,whiteSpace:'pre-wrap',overflowWrap:'anywhere',opacity:reveal(i),background:i===p.selected?'#3b454e':'transparent',padding:'3px 10px',borderRadius:4}}>{line}</div>)}
      </div>
    </div>;
  } else if(p.mode==='diff') {
    content=<div style={{...shell,...panel,fontFamily:F.mono,padding:32}}>
      <div style={{fontFamily:F.ui,fontSize:28,marginBottom:25}}>project.godot · actual revision</div>
      {p.lines.map((line,i)=><div data-audit={'diff-'+i} key={i} style={{fontSize:mono,lineHeight:1.7,opacity:reveal(i),whiteSpace:'pre-wrap',overflowWrap:'anywhere',padding:'8px 18px',marginBottom:6,background:line.startsWith('+')?'#eeece3':line.startsWith('-')?'#f8e4dc':'transparent',color:C.INK}}>{line}</div>)}
    </div>;
  } else if(p.mode==='editor') {
    content=<div style={{...shell,background:'#252a34',borderRadius:14,color:'#edf0f5',fontFamily:F.ui,overflow:'hidden'}}>
      <div style={{padding:'22px 32px',background:'#353d4c',fontSize:28}}>walker-jumpman <span style={{float:'right'}}>2D · Compatibility</span></div>
      <div style={{display:'grid',gridTemplateColumns:portrait?'1fr':'330px 1fr',height:'84%'}}>
        <div style={{borderRight:'2px solid #49515d',padding:25,fontSize:28,lineHeight:1.7}}><strong>FileSystem</strong><div>res://</div><div style={{paddingLeft:20}}>project.godot</div><div style={{marginTop:30,fontSize:25}}>No game scenes<br/>No game scripts</div></div>
        <div style={{position:'relative',backgroundImage:'linear-gradient(#ffffff09 1px,transparent 1px),linear-gradient(90deg,#ffffff09 1px,transparent 1px)',backgroundSize:'48px 48px',padding:35}}>
          <div style={{fontSize:40}}>Empty project</div><div style={{fontSize:29,marginTop:15,color:'#d0d6e1'}}>No main scene assigned</div>
          <div style={{position:'absolute',left:35,right:35,bottom:25,background:'#1c2028',borderRadius:9,padding:22,fontFamily:F.mono,fontSize:portrait?26:28,lineHeight:1.5}}>{p.lines.map((x,i)=><div key={i} style={{opacity:reveal(i)}}>{x}</div>)}</div>
        </div>
      </div>
    </div>;
  } else if(p.mode==='comparison') {
    content=<div style={{...shell,display:'grid',gridTemplateColumns:portrait?'1fr':'1fr 1fr',gap:35}}>{p.labels.map((label,i)=><div key={label} style={{...panel,padding:45,opacity:reveal(i),display:'flex',flexDirection:'column',justifyContent:'center',borderTop:`7px solid ${i===p.selected?C.SEND:C.INK}`}}>
      <div data-audit={'comparison-'+i} style={{fontFamily:F.serif,fontSize:portrait?50:58,lineHeight:1.12}}>{label}</div><div style={{fontFamily:F.ui,fontSize:34,lineHeight:1.5,whiteSpace:'pre-line',marginTop:35}}>{p.details[i]}</div>
    </div>)}</div>;
  } else {
    content=<div style={{...shell,overflow:'hidden',display:'flex',flexDirection:portrait?'column':'row',alignItems:'stretch',gap:portrait?22:20}}>
      {p.labels.map((label,i)=><React.Fragment key={label}><div style={{...panel,flex:1,minWidth:0,padding:portrait?'25px 35px':p.labels.length>=5?'35px 12px':'35px 25px',display:'flex',flexDirection:'column',justifyContent:'center',opacity:reveal(i),outline:i===Math.min(active,p.labels.length-1)?`3px solid ${C.SEND}`:'none'}}>
        <div style={{fontFamily:F.ui,fontSize:26,color:C.INK_SOFT,marginBottom:24}}>{String(i+1).padStart(2,'0')}</div>
        <div data-audit={'flow-'+i} style={{fontFamily:F.serif,fontSize:portrait?52:46,lineHeight:1.12,overflowWrap:'anywhere'}}>{label}</div>
        <div style={{fontFamily:F.mono,fontSize:portrait?29:28,lineHeight:1.55,marginTop:28,whiteSpace:'pre-line',overflowWrap:'anywhere'}}>{p.details[i]}</div>
      </div>{i<p.labels.length-1&&<div style={{alignSelf:'center',fontSize:38,color:C.INK,opacity:reveal(i+1)}}>{portrait?'↓':'→'}</div>}</React.Fragment>)}
    </div>;
  }
  return <AbsoluteFill style={{background:C.PAGE,color:C.INK}}>{title}{content}{spark}{source}{footer}</AbsoluteFill>;
};
