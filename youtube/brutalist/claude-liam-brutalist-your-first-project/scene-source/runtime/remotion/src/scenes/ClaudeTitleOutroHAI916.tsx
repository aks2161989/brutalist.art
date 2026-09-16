import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { claudeTitleOutroHaiSchema } from './ClaudeTitleOutroHAI';
import type { ClaudeTitleOutroHAIProps } from './ClaudeTitleOutroHAI';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * ClaudeTitleOutroHAI916 — portrait 9:16 version of ClaudeTitleOutroHAI.
 * Same schema; type sizes derived from height so it fills a 1080×1920 stage.
 */

export const claudeTitleOutroHai916Schema = claudeTitleOutroHaiSchema;
export type ClaudeTitleOutroHAI916Props = ClaudeTitleOutroHAIProps;

const SERIF = CLAUDE_FONT.serif;
const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));

export const ClaudeTitleOutroHAI916: React.FC<ClaudeTitleOutroHAI916Props> = ({ title, handle, slug }) => {
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

  const TITLE_FONT = height * 0.058;
  const HANDLE_FONT = height * 0.032;
  const SUB_FONT = height * 0.018;
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
      <div style={{ position: 'absolute', top: '6%', left: '5.5%', right: '5.5%', height: 4, background: fg, opacity: 0.5 }} />
      <div style={{ position: 'absolute', bottom: '6%', left: '5.5%', right: '5.5%', height: 4, background: fg, opacity: 0.5 }} />

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
      }}>
        {titleBody}
        <span style={{ color: fgSend }}>{titlePunct}</span>
      </div>

      <div style={{
        fontFamily: SERIF,
        fontSize: HANDLE_FONT,
        color: fg,
        marginTop: height * 0.026,
        opacity: 0.92,
        textAlign: 'center',
      }}>
        {handle}
      </div>

      <div style={{
        fontFamily: SERIF,
        fontSize: SUB_FONT,
        color: fg,
        marginTop: height * 0.018,
        opacity: 0.62,
        letterSpacing: '0.14em',
        textTransform: 'uppercase',
        textAlign: 'center',
      }}>
        Brutalist — 03
      </div>
    </AbsoluteFill>
  );
};
