import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate } from 'remotion';
import { claudeCodeBeatSchema } from './ClaudeCodeBeat';
import type { ClaudeCodeBeatProps } from './ClaudeCodeBeat';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * ClaudeCodeBeat916 — portrait 9:16 (1080×1920) version of ClaudeCodeBeat.
 * Same schema. Code card fills the portrait safe area; spark line at bottom.
 * Per REFLOW rule: stack vertically, fill the height, distribute content down.
 * ILLUSTRATE LAW: code beats only — never wallpaper.
 */

export const claudeCodeBeat916Schema = claudeCodeBeatSchema;
export type ClaudeCodeBeat916Props = ClaudeCodeBeatProps;

const SERIF = CLAUDE_FONT.serif;
const SANS  = CLAUDE_FONT.ui;
const MONO  = CLAUDE_FONT.mono;
const COMMENT_CLR = '#8B8878';
const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));

export const ClaudeCodeBeat916: React.FC<ClaudeCodeBeat916Props> = ({ title, code, sparkLine }) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();

  const cardIn  = spring({ frame,           fps, config: { damping: 28, stiffness: 140, mass: 0.8 } });
  const sparkIn = spring({ frame: frame - 8, fps, config: { damping: 28, stiffness: 140, mass: 0.8 } });

  const lines = code.split('\n');
  const REVEAL_START = 12;
  const LINE_STRIDE  = 3;

  const filename = title.includes(' — ') ? title.split(' — ')[0].trim() : title;

  // Portrait: tall card, font scaled to height
  const PAD_X = width * 0.06;
  const CARD_TOP = height * 0.06;
  const CARD_BOT = height * 0.13;
  const CODE_FONT = Math.min(height * 0.019, width * 0.038);

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>

      {/* Code card */}
      <div style={{
        position: 'absolute',
        left: PAD_X,
        right: PAD_X,
        top: CARD_TOP,
        bottom: CARD_BOT,
        background: CLAUDE.CARD,
        border: `1px solid ${CLAUDE.BORDER}`,
        borderRadius: 14,
        boxShadow: '0 8px 32px rgba(61,57,41,0.10)',
        overflow: 'hidden',
        transform: `translateY(${(1 - clamp(cardIn, 0, 1)) * 18}px)`,
        opacity: clamp(cardIn, 0, 1),
      }}>

        {/* Title bar */}
        <div style={{
          display: 'flex',
          alignItems: 'center',
          gap: 8,
          padding: '14px 20px',
          background: CLAUDE.PAGE,
          borderBottom: `1px solid ${CLAUDE.BORDER}`,
        }}>
          {[CLAUDE.SPARK, CLAUDE.BORDER, CLAUDE.BORDER].map((c, i) => (
            <div key={i} style={{
              width: 13, height: 13, borderRadius: '50%', background: c,
            }} />
          ))}
          <span style={{
            marginLeft: 10,
            fontFamily: MONO,
            fontSize: height * 0.014,
            color: CLAUDE.INK_SOFT,
            letterSpacing: '0.02em',
          }}>
            {filename}
          </span>
          <span style={{
            marginLeft: 'auto',
            fontFamily: SANS,
            fontSize: height * 0.012,
            fontWeight: 600,
            color: CLAUDE.SPARK,
            letterSpacing: 2,
            textTransform: 'uppercase' as const,
          }}>
            python
          </span>
        </div>

        {/* Code lines */}
        <pre style={{
          margin: 0,
          padding: '20px 24px',
          fontFamily: MONO,
          fontSize: CODE_FONT,
          lineHeight: 1.65,
          textAlign: 'left',
          overflow: 'hidden',
        }}>
          {lines.map((line, i) => {
            const start = REVEAL_START + i * LINE_STRIDE;
            const op = clamp(interpolate(frame, [start, start + 5], [0, 1]), 0, 1);
            const ty = interpolate(frame, [start, start + 7], [6, 0], {
              extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
            });
            const isComment = line.trimStart().startsWith('#');
            const color = isComment ? COMMENT_CLR : CLAUDE.INK;
            return (
              <div key={i} style={{
                opacity: op,
                transform: `translateY(${ty}px)`,
                whiteSpace: 'pre' as const,
                color,
              }}>
                {line || '​'}
              </div>
            );
          })}
        </pre>
      </div>

      {/* Ink-extent top/bottom anchors for Gate V — 5.5% keeps anchors inside SAFE916 (5%) boundary */}
      <div style={{ position: 'absolute', top: '5.5%', left: '5%', right: '5%', height: 3, background: CLAUDE.INK, opacity: 0.4 }} />
      <div style={{ position: 'absolute', bottom: '5.5%', left: '5%', right: '5%', height: 3, background: CLAUDE.INK, opacity: 0.4 }} />

      {/* Spark line */}
      <div style={{
        position: 'absolute',
        left: PAD_X,
        right: PAD_X,
        bottom: height * 0.045,
        display: 'flex',
        alignItems: 'center',
        gap: 10,
        opacity: clamp(sparkIn, 0, 1),
        transform: `translateY(${(1 - clamp(sparkIn, 0, 1)) * 8}px)`,
      }}>
        <span style={{
          fontFamily: SERIF,
          fontSize: height * 0.018,
          fontStyle: 'italic',
          color: CLAUDE.INK,
        }}>
          {sparkLine}
        </span>
      </div>

    </AbsoluteFill>
  );
};
