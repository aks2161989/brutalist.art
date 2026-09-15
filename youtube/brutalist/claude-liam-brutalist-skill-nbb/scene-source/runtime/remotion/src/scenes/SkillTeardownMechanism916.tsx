import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring } from 'remotion';
import { skillTeardownMechanismSchema } from './SkillTeardownMechanism';
import type { SkillTeardownMechanismProps } from './SkillTeardownMechanism';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * SkillTeardownMechanism916 — portrait 9:16 (1080×1920) variant.
 * Same schema as landscape. Reflow: R2 (typography ramp) + narrower body,
 * stacked vertically to fill the portrait column. Positions relative to
 * useVideoConfig() height/width so the same component reads on both aspects.
 * TEXT LAW: variable-length text gets maxWidth + wrap for safety inside SAFE916.
 */

export const skillTeardownMechanism916Schema = skillTeardownMechanismSchema;
export type SkillTeardownMechanism916Props = SkillTeardownMechanismProps;

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const MONO = CLAUDE_FONT.mono;

const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));

export const SkillTeardownMechanism916: React.FC<SkillTeardownMechanism916Props> = ({
  eyebrow, heading, body, quote, cite, verdictLabel, verdictPositive, sparkLine,
}) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();

  const headerIn = spring({ frame, fps, config: { damping: 28, stiffness: 120, mass: 0.9 } });
  const bodyIn = spring({ frame: frame - 18, fps, config: { damping: 26, stiffness: 110, mass: 1.0 } });
  const quoteIn = spring({ frame: frame - 32, fps, config: { damping: 26, stiffness: 110, mass: 1.0 } });
  const verdictIn = spring({ frame: frame - 50, fps, config: { damping: 26, stiffness: 110, mass: 1.0 } });
  const sparkIn = spring({ frame: frame - 60, fps, config: { damping: 28, stiffness: 120, mass: 0.9 } });

  const hasQuote = !!quote;
  const hasVerdict = !!verdictLabel;

  const CONTENT_L = width * 0.06;
  const CONTENT_R = width * 0.06;
  const CONTENT_W = width - CONTENT_L - CONTENT_R;

  const FONT_EYEBROW = 22;
  const FONT_HEADING = 82;
  const FONT_BODY = 40;
  const FONT_QUOTE = 34;
  const FONT_CITE = 22;
  const FONT_VERDICT = 24;
  const FONT_SPARK = 34;

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>

      {/* Eyebrow */}
      <div style={{
        position: 'absolute',
        top: height * 0.06,
        left: 0, right: 0,
        textAlign: 'center',
        fontFamily: SANS,
        fontSize: FONT_EYEBROW,
        fontWeight: 700,
        letterSpacing: 6,
        textTransform: 'uppercase' as const,
        color: CLAUDE.INK_SOFT,
        opacity: clamp(headerIn, 0, 1),
      }}>
        {eyebrow}
      </div>

      {/* Heading */}
      <div style={{
        position: 'absolute',
        top: height * 0.09,
        left: CONTENT_L,
        width: CONTENT_W,
        fontFamily: SERIF,
        fontSize: FONT_HEADING,
        fontWeight: 700,
        color: CLAUDE.INK,
        lineHeight: 1.1,
        textAlign: 'left' as const,
        opacity: clamp(headerIn, 0, 1),
        transform: `translateY(${(1 - clamp(headerIn, 0, 1)) * 14}px)`,
        wordBreak: 'break-word' as const,
      }}>
        {heading}
      </div>

      {/* Body */}
      {body && (
        <div style={{
          position: 'absolute',
          top: height * 0.22,
          left: CONTENT_L,
          width: CONTENT_W,
          fontFamily: SANS,
          fontSize: FONT_BODY,
          color: CLAUDE.INK,
          lineHeight: 1.45,
          opacity: clamp(bodyIn, 0, 1),
          transform: `translateY(${(1 - clamp(bodyIn, 0, 1)) * 12}px)`,
          wordBreak: 'break-word' as const,
        }}>
          {body}
        </div>
      )}

      {/* Verbatim quote block */}
      {hasQuote && (
        <div style={{
          position: 'absolute',
          top: body ? height * 0.5 : height * 0.28,
          left: CONTENT_L,
          width: CONTENT_W,
          background: CLAUDE.CARD,
          border: `1px solid ${CLAUDE.BORDER}`,
          borderLeft: `6px solid ${CLAUDE.SPARK}`,
          borderRadius: 16,
          padding: '32px 36px',
          opacity: clamp(quoteIn, 0, 1),
          transform: `translateY(${(1 - clamp(quoteIn, 0, 1)) * 12}px)`,
          boxSizing: 'border-box' as const,
        }}>
          <div style={{
            fontFamily: MONO,
            fontSize: FONT_QUOTE,
            color: CLAUDE.INK,
            lineHeight: 1.5,
            whiteSpace: 'pre-wrap' as const,
            wordBreak: 'break-word' as const,
          }}>
            "{quote}"
          </div>
          {cite && (
            <div style={{
              fontFamily: SANS,
              fontSize: FONT_CITE,
              color: CLAUDE.GHOST,
              marginTop: 16,
              wordBreak: 'break-word' as const,
            }}>
              Source: {cite}
            </div>
          )}
        </div>
      )}

      {/* Verdict pill */}
      {hasVerdict && (
        <div style={{
          position: 'absolute',
          bottom: height * 0.13,
          left: CONTENT_L,
          width: CONTENT_W,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'flex-start' as const,
          opacity: clamp(verdictIn, 0, 1),
          transform: `translateY(${(1 - clamp(verdictIn, 0, 1)) * 8}px)`,
        }}>
          <div style={{
            background: verdictPositive ? 'rgba(217,119,87,0.12)' : 'rgba(61,57,41,0.08)',
            border: `1px solid ${verdictPositive ? CLAUDE.SPARK : CLAUDE.BORDER}`,
            borderRadius: 32,
            padding: '12px 28px',
            fontFamily: SANS,
            fontSize: FONT_VERDICT,
            fontWeight: 700,
            color: verdictPositive ? CLAUDE.SPARK : CLAUDE.INK_SOFT,
            letterSpacing: 1.5,
            textTransform: 'uppercase' as const,
          }}>
            {verdictLabel}
          </div>
        </div>
      )}

      {/* Spark line */}
      <div style={{
        position: 'absolute',
        left: CONTENT_L,
        bottom: height * 0.05,
        display: 'flex',
        alignItems: 'center',
        gap: 14,
        opacity: clamp(sparkIn, 0, 1),
        transform: `translateY(${(1 - clamp(sparkIn, 0, 1)) * 8}px)`,
      }}>
        <span style={{ fontFamily: SERIF, fontSize: FONT_SPARK, fontStyle: 'italic', color: CLAUDE.INK }}>{sparkLine}</span>
      </div>

    </AbsoluteFill>
  );
};
