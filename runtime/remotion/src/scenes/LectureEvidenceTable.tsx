import React from 'react';
import {AbsoluteFill,interpolate,useCurrentFrame,useVideoConfig} from 'remotion';
import {z} from 'zod';
import {CLAUDE_FONT} from '../tokens/claude';

/** LectureEvidenceTable: source-grounded comparison rows, revealed and ringed on
 * spoken cues. Not narration as typography: every cell is an artifact value or
 * concise classification, with an explicit source/constructed-data note. */
export const lectureEvidenceTableSchema=z.object({
  title:z.string(),headers:z.array(z.string()).min(2).max(4),
  rows:z.array(z.array(z.string())).min(1).max(4),
  note:z.string(),durationSeconds:z.number().default(12),
  cues:z.array(z.number()).default([.1,.3,.6,.78]),
  instantReveal:z.boolean().optional(),
});
type P=z.infer<typeof lectureEvidenceTableSchema>;
export const LectureEvidenceTable:React.FC<P>=({title,headers,rows,note,cues,instantReveal})=>{
  const f=useCurrentFrame(),{durationInFrames}=useVideoConfig(),t=f/durationInFrames;
  const active=rows.reduce((last,_,i)=>t>=(cues[i]??.1+i*.2)?i:last,-1);
  return <AbsoluteFill style={{background:'#F2F0E9',color:'#3D3929',fontFamily:CLAUDE_FONT.serif,padding:'80px 130px'}}>
    <div style={{fontSize:68,textAlign:'center',marginBottom:70}}>{title}</div>
    <div style={{display:'grid',gridTemplateColumns:`repeat(${headers.length},1fr)`,gap:20,fontSize:40,padding:'20px 28px',borderBottom:'3px solid #3D3929'}}>
      {headers.map((x,i)=><div key={i}>{x}</div>)}
    </div>
    {rows.map((row,i)=>{
      const p=instantReveal ? (t>=(cues[i]??.1+i*.2)?1:0) : interpolate(t,[cues[i]??.1+i*.2,(cues[i]??.1+i*.2)+.06],[0,1],{extrapolateLeft:'clamp',extrapolateRight:'clamp'});
      return <div key={i} style={{display:'grid',gridTemplateColumns:`repeat(${headers.length},1fr)`,gap:20,
        fontSize:48,padding:'28px',marginTop:14,minHeight:106,boxSizing:'border-box',
        border:`4px solid ${active===i?'#A64A24':'transparent'}`,borderRadius:16,
        opacity:p,transform:`translateY(${(1-p)*16}px)`}}>{row.map((v,j)=><div key={j}>{v}</div>)}</div>;
    })}
    <div style={{position:'absolute',bottom:118,left:130,right:130,fontSize:40,lineHeight:1.1}}>{note}</div>
    <div style={{position:'absolute',bottom:65,right:130,fontSize:40}}>@NikBearBrown</div>
  </AbsoluteFill>;
};
