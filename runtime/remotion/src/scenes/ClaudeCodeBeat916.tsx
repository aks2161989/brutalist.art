import React from 'react';
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {claudeCodeBeatSchema, ClaudeCodeBeatProps} from './ClaudeCodeBeat';

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const MONO = CLAUDE_FONT.mono;
const COMMENT_CLR = '#8B8878';
const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));

/**
 * Native 9:16 layout for ClaudeCodeBeat.
 * Designed for the Kafka producer/consumer code beats.
 * Registered at 1080x1920 and intended to be rendered at scale 2 for 2160x3840 delivery.
 */
export const ClaudeCodeBeat916: React.FC<ClaudeCodeBeatProps> = ({title, code, sparkLine}) => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();

  const cardIn = spring({frame, fps, config: {damping: 28, stiffness: 140, mass: 0.8}});
  const sparkIn = spring({frame: frame - 8, fps, config: {damping: 28, stiffness: 140, mass: 0.8}});

  const lines = code.split('\n');
  const revealStart = 12;
  const lineStride = 3;
  const filename = title.includes(' — ') ? title.split(' — ')[0].trim() : title;

  // B08 has more lines than B04. Scale typography slightly to keep both
  // comfortably inside the portrait code card without horizontal clipping.
  const codeFont = lines.length >= 16 ? 24 : 27;
  const codeLineHeight = lines.length >= 16 ? 1.58 : 1.68;

  return (
    <AbsoluteFill style={{background: CLAUDE.PAGE}}>
      <div style={{
        position: 'absolute',
        left: width * 0.065,
        right: width * 0.065,
        top: height * 0.075,
        bottom: height * 0.19,
        background: CLAUDE.CARD,
        border: `1px solid ${CLAUDE.BORDER}`,
        borderRadius: 18,
        boxShadow: '0 10px 36px rgba(61,57,41,0.10)',
        overflow: 'hidden',
        transform: `translateY(${(1 - clamp(cardIn, 0, 1)) * 18}px)`,
        opacity: clamp(cardIn, 0, 1),
      }}>
        <div style={{
          height: 74,
          boxSizing: 'border-box',
          display: 'flex',
          alignItems: 'center',
          gap: 10,
          padding: '0 28px',
          background: CLAUDE.PAGE,
          borderBottom: `1px solid ${CLAUDE.BORDER}`,
        }}>
          {[CLAUDE.SPARK, CLAUDE.BORDER, CLAUDE.BORDER].map((c, i) => (
            <div key={i} style={{width: 14, height: 14, borderRadius: '50%', background: c}} />
          ))}
          <span style={{
            marginLeft: 10,
            fontFamily: MONO,
            fontSize: 22,
            color: CLAUDE.INK_SOFT,
            letterSpacing: '0.02em',
          }}>{filename}</span>
          <span style={{
            marginLeft: 'auto',
            fontFamily: SANS,
            fontSize: 17,
            fontWeight: 600,
            color: CLAUDE.SPARK,
            letterSpacing: 2,
            textTransform: 'uppercase',
          }}>python</span>
        </div>

        <pre style={{
          margin: 0,
          padding: '34px 34px',
          fontFamily: MONO,
          fontSize: codeFont,
          lineHeight: codeLineHeight,
          textAlign: 'left',
          overflow: 'hidden',
        }}>
          {lines.map((line, i) => {
            const start = revealStart + i * lineStride;
            const op = clamp(interpolate(frame, [start, start + 5], [0, 1]), 0, 1);
            const ty = interpolate(frame, [start, start + 7], [6, 0], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            });
            const color = line.trimStart().startsWith('#') ? COMMENT_CLR : CLAUDE.INK;
            return (
              <div key={i} style={{
                opacity: op,
                transform: `translateY(${ty}px)`,
                whiteSpace: 'pre',
                color,
              }}>{line || '\u200b'}</div>
            );
          })}
        </pre>
      </div>

      <div style={{
        position: 'absolute',
        left: width * 0.075,
        right: width * 0.075,
        bottom: height * 0.065,
        opacity: clamp(sparkIn, 0, 1),
        transform: `translateY(${(1 - clamp(sparkIn, 0, 1)) * 8}px)`,
      }}>
        <div style={{
          width: 72,
          height: 5,
          borderRadius: 3,
          background: CLAUDE.SPARK,
          marginBottom: 18,
        }} />
        <span style={{
          display: 'block',
          fontFamily: SERIF,
          fontSize: 34,
          lineHeight: 1.22,
          fontStyle: 'italic',
          color: CLAUDE.INK,
        }}>{sparkLine}</span>
      </div>
    </AbsoluteFill>
  );
};

export {claudeCodeBeatSchema};
