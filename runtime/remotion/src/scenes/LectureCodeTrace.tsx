import React from 'react';
import {AbsoluteFill,useCurrentFrame,useVideoConfig} from 'remotion';
import {z} from 'zod';
import {CLAUDE_FONT} from '../tokens/claude';

/** LectureCodeTrace: a real source excerpt with paced line focus, not simulated
 * program output. Large fixed-size code and a source note remain readable at 4K. */
export const lectureCodeTraceSchema=z.object({title:z.string(),code:z.string(),note:z.string(),
  durationSeconds:z.number().default(12),cues:z.array(z.number()).default([])});
type P=z.infer<typeof lectureCodeTraceSchema>;
export const LectureCodeTrace:React.FC<P>=({title,code,note,cues})=>{
 const f=useCurrentFrame(),{durationInFrames}=useVideoConfig(),t=f/durationInFrames;
 const lines=code.split('\n');
 const active=lines.reduce((last,_,i)=>t>=(cues[i]??.08+i*.78/lines.length)?i:last,-1);
 return <AbsoluteFill style={{background:'#F2F0E9',color:'#3D3929',fontFamily:CLAUDE_FONT.serif,padding:'70px 110px'}}>
   <div style={{fontSize:62,marginBottom:32}}>{title}</div>
   <div style={{background:'#fffefb',border:'3px solid #3D3929',borderRadius:18,padding:'36px 30px',height:700,boxSizing:'border-box'}}>
    {lines.map((line,i)=><div key={i} style={{display:'flex',fontFamily:CLAUDE_FONT.mono,fontSize:42,lineHeight:1.45,
      background:active===i?'#E6D3C2':'transparent',borderLeft:`6px solid ${active===i?'#A64A24':'transparent'}`,padding:'0 12px'}}>
       <span style={{width:70,flexShrink:0,color:'#5D584F'}}>{i+1}</span><span style={{whiteSpace:'pre-wrap',overflowWrap:'anywhere'}}>{line||' '}</span>
    </div>)}
   </div>
   <div style={{fontSize:40,marginTop:25,lineHeight:1.1}}>{note}</div>
   <div style={{position:'absolute',bottom:60,right:110,fontSize:40}}>@NikBearBrown</div>
 </AbsoluteFill>;
};
