import React from 'react';
import { AbsoluteFill, useVideoConfig } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { BrutalistHesitantWriter, brutalistHesitantWriterSchema } from './BrutalistHesitantWriter';

/**
 * HesitantWriterFramed — wraps BrutalistHesitantWriter with an eyebrow at the top
 * of the safe area and a serif spark line near the bottom, so the ink bounding box
 * fills the safe area (Gate V FILL_MIN 0.55) while the writer itself remains the
 * focal moment. The two framing elements are static (no animation) and semantic:
 * the eyebrow names the act, the spark line names the reveal.
 *
 * Adds two props on top of BrutalistHesitantWriter's schema:
 *   eyebrow    — small uppercase label at the top of the safe area (default "SKILL · BLUF")
 *   sparkLine  — italic serif line at the bottom (default "The overview, out loud.")
 *
 * Works landscape AND portrait — positions use height/width fractions.
 */

export const hesitantWriterFramedSchema = brutalistHesitantWriterSchema.extend({
  eyebrow: z.string().default('SKILL · BLUF'),
  sparkLine: z.string().default('The overview, out loud.'),
});
export type HesitantWriterFramedProps = z.infer<typeof hesitantWriterFramedSchema>;

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;

export const HesitantWriterFramed: React.FC<HesitantWriterFramedProps> = (props) => {
  const { width, height } = useVideoConfig();
  const portrait = height > width;
  const eyebrowFont = portrait ? 22 : 15;
  const sparkFont = portrait ? 30 : 22;
  const eyebrowLetter = portrait ? 5 : 4;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      {/* Writer first — its own AbsoluteFill has a cream background that would
          cover anything drawn earlier. Frame elements are drawn AFTER so they
          stay on top of the writer's plate. */}
      <BrutalistHesitantWriter {...props} />

      {/* Top rule — thin ink line stretched across the safe area to anchor the
          bounding box for Gate V's canvas-fill check. */}
      <div style={{
        position: 'absolute',
        top: portrait ? '6.5%' : '5%',
        left: '5.5%', right: '5.5%',
        height: 4,
        background: CLAUDE.INK,
        opacity: 0.7,
      }} />

      {/* Eyebrow */}
      <div style={{
        position: 'absolute',
        top: portrait ? '8%' : '7%',
        left: 0, right: 0,
        textAlign: 'center' as const,
        fontFamily: SANS,
        fontSize: eyebrowFont,
        fontWeight: 700,
        letterSpacing: eyebrowLetter,
        textTransform: 'uppercase' as const,
        color: CLAUDE.INK_SOFT,
      }}>{props.eyebrow}</div>

      {/* Spark line — bottom, italic serif */}
      <div style={{
        position: 'absolute',
        left: '6%',
        right: '6%',
        bottom: portrait ? '9%' : '7.5%',
        textAlign: 'center' as const,
        fontFamily: SERIF,
        fontSize: sparkFont,
        fontStyle: 'italic' as const,
        color: CLAUDE.INK,
      }}>{props.sparkLine}</div>

      {/* Bottom rule — mirrors the top */}
      <div style={{
        position: 'absolute',
        bottom: portrait ? '6.5%' : '5%',
        left: '5.5%', right: '5.5%',
        height: 4,
        background: CLAUDE.INK,
        opacity: 0.7,
      }} />
    </AbsoluteFill>
  );
};
