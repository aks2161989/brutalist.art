import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import {CLAUDE_FONT} from '../tokens/claude';

/** DesignPipelineClaim: structural mechanisms for the Figma extraction lectures.
 * Diagrams are conceptual, never mock Figma interfaces. Nodes persist while a
 * decision propagates, is rejected at a gate, branches, or drifts out of sync.
 * Every label and event comes from the authored source coverage map.
 */
export const designPipelineClaimSchema = z.object({
  title: z.string(),
  mode: z.enum(['flow', 'drift', 'tree', 'gate', 'mapping']),
  labels: z.array(z.string()).min(2).max(6),
  details: z.array(z.string()).default([]),
  note: z.string().default('Conceptual model'),
  durationSeconds: z.number().default(12),
  gateLabel: z.string().default('Reject mismatch'),
  driftLabel: z.string().default('No automatic notification'),
  cues: z.array(z.number()).default([0.12, 0.3, 0.6, 0.78]),
  diagramStyle: z.enum(['flat', 'show-tell-isometric']).default('flat'),
  objectKinds: z.array(z.enum(['document','adapter','monitor','phone','package','token','scanner'])).default([]),
});
type Props = z.infer<typeof designPipelineClaimSchema>;
const ink='#3D3929', accent='#A64A24', paper='#F2F0E9';
const clamp=(x:number)=>Math.min(1,Math.max(0,x));

export const DesignPipelineClaim: React.FC<Props> = ({title,mode,labels,details,note,cues,gateLabel,driftLabel,diagramStyle,objectKinds=[]}) => {
  const frame=useCurrentFrame();
  const {durationInFrames,width,height}=useVideoConfig();
  const t=frame/durationInFrames;
  const progress=(i:number)=>clamp((t-(cues[i] ?? 0.12+i*0.18))/0.14);
  const portrait=height>width;
  const W=1920,H=1080;
  const positions=labels.map((_,i)=> {
    if(mode==='tree') return i===0 ? [960,295] : [280+(i-1)*1360/Math.max(1,labels.length-2),690];
    if(mode==='mapping') return [i%2 ? 1430:490,(labels.length>4?310:380)+Math.floor(i/2)*(labels.length>4?235:280)];
    if(mode==='drift') return [550+i*820,505];
    return [280+i*1360/Math.max(1,labels.length-1),520];
  });
  const box=(i:number)=> {
    const [x,y]=positions[i];
    const active=mode==='drift'? (i===0&&progress(0)>0.8):mode==='gate'&&i===labels.length-1?false:progress(Math.max(0,i-1))>0.85;
    const sub=details[i] || '';
    const bw=mode==='mapping'?450:300;
    return <g key={i} transform={`translate(${x},${y})`}>
      <rect x={-bw/2} y={-100} width={bw} height={200} rx={18} fill={paper} stroke={active?accent:ink} strokeWidth={2}/>
      <foreignObject x={-bw/2+12} y={-83} width={bw-24} height={166}>
        <div style={{height:'100%',display:'flex',flexDirection:'column',justifyContent:'center',textAlign:'center',fontSize:54,lineHeight:1.08}}>
          <div>{labels[i]}</div>{sub?<div style={{fontSize:54,marginTop:12}}>{sub}</div>:null}
        </div>
      </foreignObject>
      {mode==='drift'?<rect x={-105} y={132} width={210} height={80} rx={12}
        fill={i===0&&progress(0)>0.8?accent:ink}/>:null}
    </g>;
  };
  const edge=(from:number,to:number,k:number)=>{
    const a=positions[from],b=positions[to];
    const vert=mode==='tree';
    const offset=mode==='mapping'?229:154;
    const x1=a[0]+(vert?0:offset), y1=a[1]+(vert?104:0);
    const x2=b[0]-(vert?0:offset), y2=b[1]-(vert?104:0);
    const q=mode==='drift'||(mode==='gate'&&to===labels.length-1)?0:progress(k);
    return <g key={`${from}-${to}`}>
      <path d={`M ${x1} ${y1} L ${x2} ${y2}`} stroke={ink} strokeWidth={4} fill="none"/>
      {q>0&&q<1?<circle cx={interpolate(q,[0,1],[x1,x2])} cy={interpolate(q,[0,1],[y1,y2])} r={15} fill={accent}/>:null}
      {q===1?<path d={`M ${x2-12} ${y2-12} l 12 12 l -12 12`} stroke={accent} strokeWidth={5} fill="none"/>:null}
    </g>;
  };
  const edges=mode==='tree'?labels.slice(1).map((_,i)=>edge(0,i+1,i)):
    mode==='mapping'?labels.map((_,i)=>i%2===0&&i+1<labels.length?edge(i,i+1,i/2):null):
    labels.slice(1).map((_,i)=>edge(i,i+1,i));
  if(diagramStyle==='show-tell-isometric') return <ShowTellProcess {...{title,mode,labels,details,note,cues,gateLabel,driftLabel,objectKinds,t}}/>;
  return <AbsoluteFill style={{background:paper,fontFamily:CLAUDE_FONT.serif,color:ink}}>
    <svg viewBox={`0 0 ${W} ${H}`} width="100%" height="100%" preserveAspectRatio="xMidYMid meet">
      <text x={960} y={155} textAnchor="middle" fontSize={68}>{title}</text>
      {edges}{labels.map((_,i)=>box(i))}
      {mode==='gate'?<g opacity={progress(1)>0?1:0}>
        <path d="M 970 665 L 1050 745 M 1050 665 L 970 745" stroke={accent} strokeWidth={10}/>
        <text x={1010} y={810} textAnchor="middle" fontSize={54}>{gateLabel}</text>
      </g>:null}
      {mode==='drift'?<text x={960} y={810} textAnchor="middle" fontSize={54} fill={accent}>
        {driftLabel}
      </text>:null}
      <foreignObject x={120} y={900} width={1680} height={118}><div style={{fontSize:54,lineHeight:1.08}}>{note}</div></foreignObject>
      <text x={1800} y={1020} textAnchor="end" fontSize={54}>@NikBearBrown</text>
    </svg>
  </AbsoluteFill>;
};

/** Vector port of Show Tell's Iso.p / box / page / mcp geometry.
 * Conceptual documents, ports, adapters and review barriers; never fake app UI.
 * Existing cue fractions are measured against the unchanged narration.
 */
const ShowTellProcess: React.FC<Omit<Props,'durationSeconds'|'diagramStyle'> & {t:number}> =
({title,mode,labels,details,note,cues,gateLabel,driftLabel,objectKinds,t}) => {
  const lines=(text:string,limit:number)=>text.split(' ').reduce<string[]>((rows,word)=>{
    if(!rows.length||rows[rows.length-1].length+word.length+1>limit) rows.push(word);
    else rows[rows.length-1]+=' '+word;
    return rows;
  },[]);
  const curated=objectKinds.length>0;
  const p=(x:number,y:number,z:number=0)=>[(x-y)*.8660254*64,-(x+y)*.5*64-z*64];
  const pt=(v:number[])=>p(v[0],v[1],v[2]).join(',');
  const box=(x:number,y:number,z:number,w:number,d:number,h:number,dark=false)=> {
    const a=x+w,b=y+d,c=z+h;
    return <g stroke="#3D3929" strokeWidth={2.4} strokeLinejoin="round">
      <polygon points={[[x,y,z],[x,b,z],[x,b,c],[x,y,c]].map(pt).join(' ')} fill={dark?'#26221F':'#DCC9AA'}/>
      <polygon points={[[x,y,z],[a,y,z],[a,y,c],[x,y,c]].map(pt).join(' ')} fill={dark?'#1E1B18':'#C7AE86'}/>
      <polygon points={[[x,y,c],[a,y,c],[a,b,c],[x,b,c]].map(pt).join(' ')} fill={dark?'#3A3530':'#F3E9D8'}/>
    </g>;
  };
  const page=(x:number,y:number,z:number)=> <g>
    {box(x,y,z,1.8,2.2,.08)}
    <polygon points={[[x,y,z+.09],[x+1.8,y,z+.09],[x+1.8,y+2.2,z+.09],[x,y+2.2,z+.09]].map(pt).join(' ')} fill="#FAF9F5" stroke="#8B8F96" strokeWidth={2}/>
    {[.5,.9,1.3].map(k=>{const a=p(x+.3,y+k,z+.1),b=p(x+1.5,y+k,z+.1);return <line key={k} x1={a[0]} y1={a[1]} x2={b[0]} y2={b[1]} stroke="#8B8F96" strokeWidth={4}/>;})}
    <circle cx={p(x+.35,y+1.8,z+.1)[0]} cy={p(x+.35,y+1.8,z+.1)[1]} r={5} fill="#D97757"/>
  </g>;
  const q=(k:number)=>clamp((t-(cues[k]??(.12+k*.18)))/.10);
  const pos=labels.map((_,i)=>mode==='tree'?i===0?[960,380]:[300+(i-1)*1320/Math.max(1,labels.length-2),725]:mode==='drift'?[520+i*880,590]:[275+i*1370/Math.max(1,labels.length-1),590]);
  const pairs=mode==='tree'?labels.slice(1).map((_,i)=>[0,i+1,i]):labels.slice(1).map((_,i)=>[i,i+1,i]);
  const transfer=pairs.map(([a,b,k])=>{
    const [ax,ay]=pos[a],[bx,by]=pos[b];
    const start=[ax+(mode==='tree'?0:115),ay+(mode==='tree'?160:-35)],end=[bx-(mode==='tree'?0:115),by-55];
    const blocked=mode==='gate'&&b===1;
    const disallowed=mode==='gate'&&a===1;
    const f=mode==='drift'||disallowed?0:q(k), travel=blocked?Math.min(.82,f):f;
    const path=`M ${start[0]} ${start[1]} C ${start[0]+(bx-ax)*.35} ${start[1]+75}, ${end[0]-(bx-ax)*.35} ${end[1]+75}, ${end[0]} ${end[1]}`;
    const u=1-travel, cx=u*u*u*start[0]+3*u*u*travel*(start[0]+(bx-ax)*.35)+3*u*travel*travel*(end[0]-(bx-ax)*.35)+travel*travel*travel*end[0];
    const cy=u*u*u*start[1]+3*u*u*travel*(start[1]+75)+3*u*travel*travel*(end[1]+75)+travel*travel*travel*end[1];
    return <g key={k}><path d={path} fill="none" stroke="#8B8F96" strokeWidth={4} strokeDasharray={mode==='drift'?'12 12':undefined}/>
      {f>0&&(f<1||blocked)?<g transform={`translate(${cx},${cy}) scale(.28)`}>{page(-.9,-1.1,0)}</g>:null}
      {!blocked&&f===1?<circle cx={end[0]} cy={end[1]} r={7} fill="#D97757"/>:null}
    </g>;
  });
  const objects=labels.map((label,i)=>{
    const [x,y]=pos[i], isGate=mode==='gate'&&i===1;
    const kind=objectKinds[i];
    const machine=kind?kind==='adapter':/adapter|adapt|read|rebuild|build|host|context|extract/i.test(label);
    const review=/check|verify|compare|review|approve/i.test(label);
    const phone=kind?kind==='phone':/mobile/i.test(label), printed=/print/i.test(label), web=kind?kind==='monitor':/web|css/i.test(label);
    const active=curated&&mode==='gate'&&i>1?false:i===0||mode==='tree'?i===0||q(i-1)===1:q(i-1)===1;
    return <g key={i} transform={`translate(${x},${y})`}>
      {isGate?<g>{box(-1.5,-.3,0,.35,.6,2.8)}{box(1.15,-.3,0,.35,.6,2.8)}{box(-1.5,-.3,2.8,3,.6,.35)}
        <g transform="translate(0,-80)"><rect x={-75} y={-12} width={150} height={24} fill="#DCC9AA" stroke="#3D3929" strokeWidth={3}/><circle r={8} fill="#D97757"/></g></g>:
       kind==='package'?<g>{box(-1,-1,0,2,2,1.7)}<path d="M 0 -173 V -70" stroke="#8B8F96" strokeWidth={5}/>{active?<circle cx={45} cy={-50} r={7} fill="#D97757"/>:null}</g>:
       kind==='token'?<g>{box(-.9,-.9,0,1.8,1.8,.32)}<circle cx={0} cy={-30} r={24} fill="#8B8F96" stroke="#3D3929" strokeWidth={3}/>{active?<circle cx={42} cy={-30} r={7} fill="#D97757"/>:null}</g>:
       kind==='scanner'?<g>{page(-.9,-1.1,0)}<g transform={`translate(${active?40:-35},-55)`}><circle r={36} fill="#F2F0E9" fillOpacity={.72} stroke="#3D3929" strokeWidth={5}/><path d="M 25 25 L 53 53" stroke="#3D3929" strokeWidth={8}/></g></g>:
       machine?<g>{box(-1.15,-1.15,0,2.3,2.3,1.2,true)}{box(-.65,-1.4,.35,.38,.3,.3)}{box(.25,-1.4,.35,.38,.3,.3)}
        {active?<circle cx={57} cy={-22} r={7} fill="#D97757"/>:null}</g>:
       phone?<g transform="translate(0,-45) skewY(-12)"><rect x={-53} y={-105} width={106} height={205} rx={17} fill="#DCC9AA" stroke="#3D3929" strokeWidth={4}/><rect x={-43} y={-86} width={86} height={161} rx={6} fill="#FAF9F5"/><circle cy={88} r={5} fill="#3D3929"/>{active?<circle cy={-30} r={9} fill="#D97757"/>:null}</g>:
       web?<g transform="translate(0,-60) skewY(-12)"><rect x={-113} y={-80} width={226} height={150} rx={8} fill="#FAF9F5" stroke="#3D3929" strokeWidth={3}/><path d="M -113 -50 H 113 M -85 -20 H 30 M -85 5 H 60 M -85 30 H -15" stroke="#8B8F96" strokeWidth={4}/><path d="M 0 70 V 95 M -45 95 H 45" stroke="#3D3929" strokeWidth={5}/>{active?<circle cx={80} cy={-20} r={7} fill="#D97757"/>:null}</g>:
       <g>{page(-.9,-1.1,0)}
        {review&&active?<path d="M -30 -50 l 20 18 l 42 -45" stroke="#3D3929" strokeWidth={7} fill="none"/>:null}
        {printed?<path d="M -70 -30 h 140" stroke="#8B8F96" strokeWidth={3}/>:null}</g>}
      <text y={135} textAnchor="middle" fontSize={48} fill="#3D3929">{curated?lines(label,16).map((line,j)=><tspan key={j} x={0} dy={j?52:0}>{line}</tspan>):label}</text>
      {details[i]?<text y={curated?135+lines(label,16).length*52:187} textAnchor="middle" fontSize={40} fill="#3D3929">{details[i]}</text>:null}
      {mode==='drift'?<circle cx={80} cy={-95} r={14} fill={i===0&&q(0)===1?'#D97757':'#8B8F96'}/>:null}
    </g>;
  });
  return <AbsoluteFill style={{background:paper,fontFamily:CLAUDE_FONT.serif,color:ink}}><svg viewBox="0 0 1920 1080" width="100%" height="100%">
    <text x={960} y={curated&&title.length>50?120:145} textAnchor="middle" fontSize={66}>{curated?lines(title,50).map((line,j)=><tspan key={j} x={960} dy={j?72:0}>{line}</tspan>):title}</text>
    {transfer}{objects}
    {mode==='gate'&&q(1)>0?<text x={960} y={840} textAnchor="middle" fontSize={48}>{gateLabel}</text>:null}
    {mode==='drift'?<text x={960} y={840} textAnchor="middle" fontSize={48}>{driftLabel}</text>:null}
    <text x={120} y={950} fontSize={40}>{note}</text><text x={1800} y={1020} textAnchor="end" fontSize={40}>@NikBearBrown</text>
  </svg></AbsoluteFill>;
};
