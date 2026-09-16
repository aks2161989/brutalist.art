import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { ANIMATIONS, AnimationName, computeAnimation, MascotSVG } from './ClaudeMascotScene';
import { claudeTitleOutroSchema, ClaudeTitleOutroProps } from './ClaudeTitleOutro';

/**
 * ClaudeTitleOutroHAI — @HumanitariansAI channel adaptation of ClaudeTitleOutro.
 *
 * BUILD-PROMPT.md ("Keep the Claude visual tokens but use that handle, not the
 * hardcoded @NikBearBrown channel of some stock NBB components"): this playlist
 * belongs to @HumanitariansAI, not @NikBearBrown. OUTRO-LOCK.md scopes the
 * hardcoded @NikBearBrown to `claude-liam-*` reels ONLY; other channels get
 * their own outro components. This is the HAI-channel outro for this batch;
 * it lives in the isolated toolkit only (do not alter the live library).
 *
 * Same schema, same visual grammar (title restate, terracotta terminal punct,
 * slug-seeded polarity + mascot). Only the handle changes.
 */

const HANDLE = '@HumanitariansAI';

function seedHash(s: string): number {
  return Array.from(s || 'default').reduce((acc, c) => acc + c.charCodeAt(0), 0);
}

export const claudeTitleOutroHAISchema = claudeTitleOutroSchema;
export type ClaudeTitleOutroHAIProps = ClaudeTitleOutroProps;

const SERIF = CLAUDE_FONT.serif;
const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));

export const ClaudeTitleOutroHAI: React.FC<ClaudeTitleOutroHAIProps> = ({ title, slug, mascotAnimation }) => {
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

  const anim: AnimationName = (mascotAnimation as AnimationName | undefined) ?? ANIMATIONS[seed % ANIMATIONS.length];
  const mascotState = computeAnimation(anim, frame, fps);
  const mascotH = 120;
  const mascotW = Math.round((136 / 86) * mascotH);

  return (
    <AbsoluteFill style={{
      background: bg,
      alignItems: 'center',
      justifyContent: 'center',
      flexDirection: 'column',
      gap: 0,
      opacity: o,
    }}>
      <div style={{ position: 'absolute', left: 96, top: 54, width: 3, height: 3, background: '#D4D4D4' }} />
      <div style={{ position: 'absolute', right: 96, bottom: 123, width: 3, height: 3, background: '#D4D4D4' }} />

      <div style={{
        fontFamily: SERIF,
        fontWeight: 700,
        fontSize: 72,
        color: fg,
        letterSpacing: '-0.02em',
        textAlign: 'center',
        lineHeight: 1.08,
        maxWidth: 1080,
        padding: '0 60px',
      }}>
        {titleBody}
        <span style={{ color: fgSend }}>{titlePunct}</span>
      </div>

      <div style={{
        fontFamily: SERIF,
        fontSize: 52,
        color: fg,
        marginTop: 28,
        opacity: 0.9,
      }}>
        {HANDLE}
      </div>

      <div style={{
        width: mascotW,
        height: mascotH,
        marginTop: 28,
        overflow: 'visible',
      }}>
        <MascotSVG s={mascotState} scale={1} />
      </div>
    </AbsoluteFill>
  );
};
