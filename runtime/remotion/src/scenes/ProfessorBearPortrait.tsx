import React from 'react';
import { AbsoluteFill, Img, useCurrentFrame, useVideoConfig, spring } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { pickProfessorBear, PROFESSOR_BEAR_ASPECT } from '../lib/professorBear';

/**
 * ProfessorBearPortrait — a Professor Bear portrait on the cream stage, framed in ink with a kraft
 * drop shadow, a one-to-three-word label beside it and an optional caption. The portrait is chosen at
 * random within the aspect ratio, stable per `seed` (use the beat id).
 *
 * PROFESSOR BEAR LAW: use this wherever a beat would otherwise show a person icon or a person token,
 * and always when the beat is about Professor Bear. Other components reuse `<ProfessorBear>` below.
 */

export const professorBearPortraitSchema = z.object({
  ratio: z.enum(['1x1', '2x3', '16x9']).default('2x3'),
  /** The beat id: the same seed always gives the same portrait. */
  seed: z.string().default('B00'),
  /** 1–3 words beside the portrait (e.g. "Professor Bear"). */
  label: z.string().default('Professor Bear'),
  sub: z.string().default(''),
  caption: z.string().default(''),
  /** Portrait height in design px (1920×1080 reference). */
  heightPx: z.number().default(720),
  /** Where the portrait sits. */
  side: z.enum(['left', 'center', 'right']).default('left'),
  /** Crop: a framed rectangle, or a circle (cropping is fine; use a 1x1 portrait for the circle). */
  shape: z.enum(['rect', 'circle']).default('rect'),
  durationSeconds: z.number().default(6),
});
export type ProfessorBearPortraitProps = z.infer<typeof professorBearPortraitSchema>;

const clamp = (v: number, a = 0, b = 1) => Math.min(b, Math.max(a, v));

/** Reusable element: the framed portrait at (x, y) with the given height. */
export const ProfessorBear: React.FC<{ratio: '1x1' | '2x3' | '16x9'; seed: string; x: number; y: number; h: number; o?: number; shape?: 'rect' | 'circle'}> =
  ({ ratio, seed, x, y, h, o = 1, shape = 'rect' }) => {
  // a circle is always a square crop (objectFit: cover centres the face area well enough for the 1x1 set)
  const w = shape === 'circle' ? h : h * PROFESSOR_BEAR_ASPECT[ratio];
  const r = shape === 'circle' ? '50%' : 8;
  return (
    <div style={{ position: 'absolute', left: x, top: y, width: w, height: h, opacity: o }}>
      <div style={{ position: 'absolute', left: 14, top: 14, width: w, height: h, background: '#DCC9AA', borderRadius: r }} />
      <Img src={pickProfessorBear(ratio, seed)} style={{ position: 'absolute', left: 0, top: 0, width: w, height: h, objectFit: 'cover',
            border: `4px solid ${CLAUDE.INK}`, borderRadius: r, boxSizing: 'border-box', display: 'block' }} />
    </div>
  );
};

export const ProfessorBearPortrait: React.FC<ProfessorBearPortraitProps> = ({ ratio, seed, label, sub, caption, heightPx, side, shape }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const inn = clamp(spring({ frame, fps, config: { damping: 26, stiffness: 150, mass: 0.8 } }), 0, 1);
  const lab = clamp(spring({ frame: frame - Math.round(fps * 0.35), fps, config: { damping: 26, stiffness: 150, mass: 0.8 } }), 0, 1);
  const w = shape === 'circle' ? heightPx : heightPx * PROFESSOR_BEAR_ASPECT[ratio];
  const y = 540 - heightPx / 2 - (caption ? 20 : 0);
  const x = side === 'left' ? 260 : side === 'right' ? 1660 - w : 960 - w / 2;
  const labelX = side === 'left' ? x + w + 90 : side === 'right' ? 260 : 0;
  return (
    <AbsoluteFill style={{ backgroundColor: CLAUDE.PAGE }}>
      <ProfessorBear ratio={ratio} seed={seed} x={x} y={y + (1 - inn) * 18} h={heightPx} o={inn} shape={shape} />
      {label && side !== 'center' ? (
        <div style={{ position: 'absolute', left: labelX, top: 540 - 60, opacity: lab, transform: `translateY(${(1 - lab) * 10}px)` }}>
          <div style={{ fontFamily: CLAUDE_FONT.serif, fontSize: 76, fontWeight: 600, color: CLAUDE.INK, lineHeight: 1.05 }}>{label}</div>
          {sub ? <div style={{ fontFamily: CLAUDE_FONT.serif, fontSize: 40, color: CLAUDE.INK_SOFT, marginTop: 14 }}>{sub}</div> : null}
        </div>
      ) : null}
      {label && side === 'center' ? (
        <div style={{ position: 'absolute', left: 0, right: 0, top: y + heightPx + 36, textAlign: 'center', opacity: lab,
                      fontFamily: CLAUDE_FONT.serif, fontSize: 56, fontWeight: 600, color: CLAUDE.INK }}>{label}</div>
      ) : null}
      {caption ? (
        <div style={{ position: 'absolute', left: 0, right: 0, bottom: 64, textAlign: 'center', opacity: lab,
                      fontFamily: CLAUDE_FONT.serif, fontSize: 38, color: CLAUDE.INK }}>{caption}</div>
      ) : null}
    </AbsoluteFill>
  );
};

export const professorBearPortraitDefaultProps: ProfessorBearPortraitProps = professorBearPortraitSchema.parse({});
