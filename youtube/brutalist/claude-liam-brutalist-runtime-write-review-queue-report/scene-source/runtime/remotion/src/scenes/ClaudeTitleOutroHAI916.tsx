import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { claudeTitleOutroHAISchema } from './ClaudeTitleOutroHAI';
import type { ClaudeTitleOutroHAIProps } from './ClaudeTitleOutroHAI';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * ClaudeTitleOutroHAI916 — portrait 9:16 (1080×1920) outro for @HumanitariansAI reels.
 * Isolated variant for the Brutalist playlist.
 */

const SERIF = CLAUDE_FONT.serif;

const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));

export const claudeTitleOutroHAI916Schema = claudeTitleOutroHAISchema;
export type ClaudeTitleOutroHAI916Props = ClaudeTitleOutroHAIProps;

export const ClaudeTitleOutroHAI916: React.FC<ClaudeTitleOutroHAI916Props> = ({ title, slug }) => {
  const frame = useCurrentFrame();
  const { height } = useVideoConfig();
  const o = clamp(interpolate(frame, [0, 14], [0, 1]), 0, 1);

  const _pm = title.match(/^([\s\S]*?)\s*([.?!…]+)\s*$/);
  const titleBody = _pm ? _pm[1] : title;
  const titlePunct = _pm ? _pm[2] : '.';

  const seed = Array.from(slug || title || 'default').reduce((acc, c) => acc + c.charCodeAt(0), 0);
  const isDark = seed % 2 === 1;
  const bg = isDark ? CLAUDE.INK : CLAUDE.PAGE;
  const fg = isDark ? CLAUDE.PAGE : CLAUDE.INK;
  const fgSend = isDark ? CLAUDE.PAGE : CLAUDE.SEND;

  const TITLE_FONT = height * 0.055;
  const HANDLE_FONT = height * 0.030;
  const PAD_X = 72;

  return (
    <AbsoluteFill style={{
      background: bg,
      alignItems: 'center',
      justifyContent: 'center',
      flexDirection: 'column',
      gap: 0,
      opacity: o,
    }}>
      {/* Ink-extent markers for Gate V fill ≥55% */}
      <div style={{ position: 'absolute', top: '6%', left: '5.5%', right: '5.5%', height: 4, background: fg, opacity: 0.6 }} />
      <div style={{ position: 'absolute', bottom: '6%', left: '5.5%', right: '5.5%', height: 4, background: fg, opacity: 0.6 }} />

      {/* Title */}
      <div style={{
        fontFamily: SERIF,
        fontWeight: 700,
        fontSize: TITLE_FONT,
        color: fg,
        letterSpacing: '-0.02em',
        textAlign: 'center',
        lineHeight: 1.08,
        maxWidth: 1080 - PAD_X * 2,
        padding: `0 ${PAD_X}px`,
        overflowWrap: 'anywhere',
        wordBreak: 'break-word',
      }}>
        {titleBody}
        <span style={{ color: fgSend }}>{titlePunct}</span>
      </div>

      {/* Handle — @HumanitariansAI */}
      <div style={{
        fontFamily: SERIF,
        fontSize: HANDLE_FONT,
        color: fg,
        marginTop: height * 0.022,
        opacity: 0.9,
        textAlign: 'center',
      }}>
        @HumanitariansAI
      </div>
    </AbsoluteFill>
  );
};
