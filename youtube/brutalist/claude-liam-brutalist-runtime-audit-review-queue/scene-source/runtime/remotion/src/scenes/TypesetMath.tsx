/** TypesetMath — structured outlined SVG equations, fractions, powers and indices.
 * Local typeset_math.py creates the SVG rows; no raw-text math fallback.
 * Reveal times in seconds follow measured narration. Portrait stacks independently.
 */
import React from 'react';
import {AbsoluteFill, Img, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';

export const typesetMathSchema = z.object({
  title: z.string().default(''),
  rows: z.array(z.object({
    src: z.string().startsWith('data:image/svg+xml;base64,'),
    aspect: z.number().positive(),
    expression: z.string(),
    at: z.number().nonnegative().default(0),
  })).max(3).default([]),
  note: z.string().default(''),
  conditions: z.string().default(''),
});

export const TypesetMath: React.FC<z.infer<typeof typesetMathSchema>> =
({title, rows, note, conditions}) => {
  const frame = useCurrentFrame();
  const {width, height, fps} = useVideoConfig();
  const portrait = height > width;
  const unit = portrait ? width / 1080 : height / 1080;
  return <AbsoluteFill style={{background: CLAUDE.PAGE, color: CLAUDE.INK,
    fontFamily: CLAUDE_FONT.serif, padding: `${height * .07}px ${width * .08}px`,
    alignItems: 'center', justifyContent: 'space-between', textAlign: 'center'}}>
    <div style={{fontSize: 64 * unit, maxWidth: '100%', lineHeight: 1.12}}>{title}</div>
    <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center',
      gap: 45 * unit, width: '100%'}}>
      {rows.map((row, i) => {
        const rowWidth = Math.min(width * .84, 168 * unit * row.aspect);
        return <Img key={i} src={row.src} alt={row.expression} style={{
          width: rowWidth, height: rowWidth / row.aspect,
          opacity: frame / fps >= row.at ? 1 : 0}} />;
      })}
    </div>
    <div style={{maxWidth: '100%'}}>
      <div style={{fontSize: 44 * unit, lineHeight: 1.2}}>{note}</div>
      <div style={{fontSize: 32 * unit, marginTop: 24 * unit}}>{conditions}</div>
    </div>
  </AbsoluteFill>;
};
