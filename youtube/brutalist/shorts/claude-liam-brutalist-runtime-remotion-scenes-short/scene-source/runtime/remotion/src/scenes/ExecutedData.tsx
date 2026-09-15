/** ExecutedData — measured rows or zero-baseline probability comparison.
 * Values are supplied from an executed evidence record; no generated screenshots.
 * Both aspects use native layout. Labels disclose constructed answer keys.
 */
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';

export const executedDataSchema = z.object({
  title: z.string(),
  mode: z.enum(['table', 'probability']),
  rows: z.array(z.object({label: z.string(), value: z.number(), at: z.number()})).min(1).max(4),
  note: z.string(),
  columnLabels: z.array(z.string()).length(2).default(['Outcome index', 'Score']),
});

export const ExecutedData: React.FC<z.infer<typeof executedDataSchema>> =
({title, mode, rows, note, columnLabels}) => {
  const frame = useCurrentFrame();
  const {width, height, fps} = useVideoConfig();
  const unit = Math.min(width / 1920, height / 1080);
  const t = frame / fps;
  return <AbsoluteFill style={{background: CLAUDE.PAGE, color: CLAUDE.INK,
    fontFamily: CLAUDE_FONT.serif, padding: `${height * .09}px ${width * .1}px`,
    justifyContent: 'space-between'}}>
    <div style={{fontSize: 66 * unit, textAlign: 'center', lineHeight: 1.12}}>{title}</div>
    <div style={{display: 'flex', flexDirection: 'column', gap: 36 * unit}}>
      {mode === 'table' && <div style={{display: 'flex', justifyContent: 'space-around',
        fontSize: 40 * unit}}>{columnLabels.map(x => <span key={x}>{x}</span>)}</div>}
      {rows.map((row, i) => <div key={i} style={{opacity: t >= row.at ? 1 : 0,
        borderBottom: mode === 'table' ? `2px solid ${CLAUDE.BORDER}` : undefined,
        padding: `${20 * unit}px 0`}}>
        <div style={{display: 'flex', justifyContent: 'space-around', fontSize: 68 * unit,
          fontFamily: mode === 'table' ? CLAUDE_FONT.mono : CLAUDE_FONT.serif}}>
          <span>{row.label}</span><span>{mode === 'probability' ? `${(row.value * 100).toFixed(1)}%` : row.value}</span>
        </div>
        {mode === 'probability' && <div style={{height: 48 * unit, background: '#E8E5DC',
          marginTop: 18 * unit}}><div style={{height: '100%', background: CLAUDE.SPARK,
          width: `${100 * row.value * Math.max(0, Math.min(1, (t - row.at) / .8))}%`}} /></div>}
      </div>)}
      {mode === 'probability' && <div style={{display: 'flex', justifyContent: 'space-between',
        fontSize: 32 * unit}}><span>0%</span><span>100%</span></div>}
    </div>
    <div style={{fontSize: 38 * unit, textAlign: 'center', lineHeight: 1.25}}>{note}</div>
  </AbsoluteFill>;
};
