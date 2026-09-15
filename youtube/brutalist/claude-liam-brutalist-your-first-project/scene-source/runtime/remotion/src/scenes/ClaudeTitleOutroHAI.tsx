import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * ClaudeTitleOutroHAI — title-restate outro card for @HumanitariansAI variants
 * of claude-liam reels (Brutalist playlist episodes).
 *
 * Isolated toolkit variant: same visual grammar as ClaudeTitleOutro
 * (cream/ink polarity, terracotta terminal punct) but the handle is a
 * prop and defaults to @HumanitariansAI. Not a replacement for the locked
 * @NikBearBrown outro — this is a separate composition registered alongside
 * it. Sign-off ("Liam, in for Bear") is carried in the narration, not on
 * screen.
 */

export const claudeTitleOutroHaiSchema = z.object({
  title: z.string().default('⚠ SET IN BEAT SHEET'),
  handle: z.string().default('@HumanitariansAI'),
  slug: z.string().default(''),
});
export type ClaudeTitleOutroHAIProps = z.infer<typeof claudeTitleOutroHaiSchema>;

const SERIF = CLAUDE_FONT.serif;
const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));

function seedHash(s: string): number {
  return Array.from(s || 'default').reduce((acc, c) => acc + c.charCodeAt(0), 0);
}

export const ClaudeTitleOutroHAI: React.FC<ClaudeTitleOutroHAIProps> = ({ title, handle, slug }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const o = clamp(interpolate(frame, [0, 14], [0, 1]), 0, 1);

  const _pm = title.match(/^([\s\S]*?)\s*([.?!…]+)\s*$/);
  const titleBody = _pm ? _pm[1] : title;
  const titlePunct = _pm ? _pm[2] : '.';

  const seed = seedHash(slug || title);
  const isDark = seed % 2 === 1;
  const bg = isDark ? CLAUDE.INK : CLAUDE.PAGE;
  const fg = isDark ? CLAUDE.PAGE : CLAUDE.INK;
  const fgSend = isDark ? CLAUDE.PAGE : CLAUDE.SEND;

  return (
    <AbsoluteFill style={{
      background: bg,
      alignItems: 'center',
      justifyContent: 'center',
      flexDirection: 'column',
      gap: 0,
      opacity: o,
    }}>
      {/* Ink-extent anchors — 3px dots at safe corners */}
      <div style={{ position: 'absolute', left: 96, top: 54, width: 3, height: 3, background: '#D4D4D4' }} />
      <div style={{ position: 'absolute', right: 96, bottom: 123, width: 3, height: 3, background: '#D4D4D4' }} />

      {/* Ink-extent bars — pull bbox to safe edges so FILL passes */}
      <div style={{ position: 'absolute', top: '6%', left: '5.5%', right: '5.5%', height: 4, background: fg, opacity: 0.5 }} />
      <div style={{ position: 'absolute', bottom: '10%', left: '5.5%', right: '5.5%', height: 4, background: fg, opacity: 0.5 }} />

      {/* Title */}
      <div style={{
        fontFamily: SERIF,
        fontWeight: 700,
        fontSize: 108,
        color: fg,
        letterSpacing: '-0.02em',
        textAlign: 'center',
        lineHeight: 1.08,
        maxWidth: 1600,
        padding: '0 60px',
      }}>
        {titleBody}
        <span style={{ color: fgSend }}>{titlePunct}</span>
      </div>

      {/* Handle */}
      <div style={{
        fontFamily: SERIF,
        fontSize: 64,
        color: fg,
        marginTop: 44,
        opacity: 0.92,
      }}>
        {handle}
      </div>

      {/* Sub-mark: playlist */}
      <div style={{
        fontFamily: SERIF,
        fontSize: 34,
        color: fg,
        marginTop: 26,
        opacity: 0.65,
        letterSpacing: '0.14em',
        textTransform: 'uppercase',
      }}>
        Brutalist — 03 / Your First Project
      </div>
    </AbsoluteFill>
  );
};
