import React from 'react';
import {AbsoluteFill,useCurrentFrame,useVideoConfig} from 'remotion';
import {z} from 'zod';
import {CLAUDE_FONT} from '../tokens/claude';
/** LectureDocumentTree: the seven-node source traversal, with a persistent
 * parent-child tree and an advancing preorder visitor. IDs trace to fixture. */
export const lectureDocumentTreeSchema=z.object({title:z.string(),durationSeconds:z.number().default(12),
  cues:z.array(z.number()).default([]),
  note:z.string().default('Constructed fixture; parent before children'),
  labels:z.array(z.string()).length(7).default(['CANVAS','FRAME','COMPONENT_SET','Default','Label','Hover','Label'])});
type P=z.infer<typeof lectureDocumentTreeSchema>;
const positions=[[960,260],[960,395],[960,530],[510,685],[510,825],[1410,685],[1410,825]];
const edges=[[0,1],[1,2],[2,3],[3,4],[2,5],[5,6]];
export const LectureDocumentTree:React.FC<P>=({title,note,labels,cues})=>{
 const frame=useCurrentFrame(),{durationInFrames}=useVideoConfig(),t=frame/durationInFrames;
 const active=cues.length?cues.reduce((last,cue,i)=>t>=cue?i:last,-1):Math.min(6,Math.floor(Math.max(0,t-.06)/.12));
 return <AbsoluteFill style={{background:'#F2F0E9',fontFamily:CLAUDE_FONT.serif}}>
  <svg viewBox="0 0 1920 1080" width="100%" height="100%">
   <text x="960" y="135" textAnchor="middle" fontSize="66" fill="#3D3929">{title}</text>
   {edges.map(([a,b],i)=><line key={i} x1={positions[a][0]} y1={positions[a][1]+47} x2={positions[b][0]} y2={positions[b][1]-47} stroke={active>=b?'#A64A24':'#3D3929'} strokeWidth="2"/>)}
   {positions.map(([x,y],i)=><g key={i} transform={`translate(${x},${y})`}>
    <rect x="-215" y="-47" width="430" height="94" rx="14" fill={active===i?'#E6D3C2':'#F2F0E9'} stroke={active>=i?'#A64A24':'#3D3929'} strokeWidth="2"/>
    <text x="0" y="14" textAnchor="middle" fontSize="43" fill="#3D3929">{labels[i]}</text>
    {active>=i?<g><circle cx="-256" cy="0" r="30" fill="#A64A24"/><text x="-256" y="14" textAnchor="middle" fontSize="42" fill="#fff">{i+1}</text></g>:null}
   </g>)}
   <text x="120" y="955" fontSize="42" fill="#3D3929">{note}</text>
   <text x="1800" y="1010" textAnchor="end" fontSize="40" fill="#3D3929">@NikBearBrown</text>
  </svg>
 </AbsoluteFill>;
};
