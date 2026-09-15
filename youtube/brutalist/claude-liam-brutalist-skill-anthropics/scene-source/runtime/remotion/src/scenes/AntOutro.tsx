import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate} from 'remotion';
import {z} from 'zod';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';

/**
 * AntOutro — reel-local outro card for The anthropics Skill (Ep 05).
 * Hardcodes @HumanitariansAI. The shipped ClaudeTitleOutro hardcodes
 * @NikBearBrown per OUTRO-LOCK.md; this reel is on the @HumanitariansAI
 * channel per BUILD-PROMPT, so a native custom variant is the required
 * override — the live library is not modified.
 *
 * Geometry scales off useVideoConfig() so the same component serves the
 * 3840x2160 landscape AND the 2160x3840 native portrait registrations.
 * No rotation on any element (no crisp-edges surprise); translate/scale only.
 */

export const antOutroSchema = z.object({
  title: z.string().default('The anthropics Skill'),
  subline: z.string().default('Liam, in for Bear.'),
});
export type AntOutroProps = z.infer<typeof antOutroSchema>;

const HAI_HANDLE = '@HumanitariansAI';
const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const cl = (v: number) => Math.min(1, Math.max(0, v));

export const AntOutro: React.FC<AntOutroProps> = ({title, subline}) => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();
  const portrait = height > width;

  const fadeIn = interpolate(frame, [0, 18], [0, 1], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });
  const eyebrowIn = spring({frame: frame - 6, fps, config: {damping: 24, stiffness: 100}});
  const handleIn = spring({frame: frame - 20, fps, config: {damping: 24, stiffness: 100}});
  const sublineIn = spring({frame: frame - 40, fps, config: {damping: 24, stiffness: 100}});

  // Terminal punctuation in terracotta
  const pm = title.match(/^([\s\S]*?)\s*([.?!…]+)\s*$/);
  const titleBody = pm ? pm[1] : title;
  const titlePunct = pm ? pm[2] : '.';

  const pad = 96;

  return (
    <AbsoluteFill style={{background: CLAUDE.PAGE, opacity: fadeIn}}>
      {/* Eyebrow — small tracked-caps near the top of the safe area */}
      <div style={{
        position: 'absolute',
        top: portrait ? 190 : 130,
        left: pad, right: pad,
        textAlign: 'center',
        fontFamily: SANS,
        fontSize: portrait ? 40 : 34,
        fontWeight: 700,
        letterSpacing: 10,
        textTransform: 'uppercase' as const,
        color: CLAUDE.INK_SOFT,
        opacity: cl(eyebrowIn),
      }}>
        BRUTALIST · EPISODE 05
      </div>

      {/* Terracotta rule under the eyebrow */}
      <div style={{
        position: 'absolute',
        top: portrait ? 270 : 190,
        left: '50%',
        transform: `translateX(-50%) scaleX(${cl(eyebrowIn)})`,
        transformOrigin: 'center',
        width: portrait ? 280 : 320,
        height: 5,
        background: CLAUDE.SPARK,
        opacity: cl(eyebrowIn),
      }} />

      {/* Title — poster serif, terracotta terminal punctuation */}
      <div style={{
        position: 'absolute',
        top: portrait ? 420 : 300,
        left: pad, right: pad,
        textAlign: 'center',
        fontFamily: SERIF,
        fontWeight: 700,
        fontSize: portrait ? 172 : 200,
        color: CLAUDE.INK,
        letterSpacing: '-0.02em',
        lineHeight: 1.04,
      }}>
        {titleBody}
        <span style={{color: CLAUDE.SPARK}}>{titlePunct}</span>
      </div>

      {/* Handle — HARDCODED @HumanitariansAI */}
      <div style={{
        position: 'absolute',
        top: portrait ? 1500 : 780,
        left: pad, right: pad,
        textAlign: 'center',
        fontFamily: SERIF,
        fontSize: portrait ? 110 : 112,
        color: CLAUDE.INK,
        opacity: cl(handleIn) * 0.94,
        transform: `translateY(${(1 - cl(handleIn)) * 10}px)`,
      }}>
        {HAI_HANDLE}
      </div>

      {/* Subline — near the bottom of the safe area */}
      <div style={{
        position: 'absolute',
        bottom: portrait ? 200 : 120,
        left: pad, right: pad,
        textAlign: 'center',
        fontFamily: SANS,
        fontSize: portrait ? 56 : 54,
        color: CLAUDE.INK_SOFT,
        opacity: cl(sublineIn),
        transform: `translateY(${(1 - cl(sublineIn)) * 8}px)`,
        letterSpacing: 6,
        textTransform: 'uppercase' as const,
        fontWeight: 700,
      }}>
        {subline}
      </div>
    </AbsoluteFill>
  );
};
