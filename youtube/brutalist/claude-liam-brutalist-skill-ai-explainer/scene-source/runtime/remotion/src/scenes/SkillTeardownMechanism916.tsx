import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring } from 'remotion';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { skillTeardownMechanismSchema, SkillTeardownMechanismProps } from './SkillTeardownMechanism';

/**
 * SkillTeardownMechanism916 — portrait (1080x1920) variant of
 * SkillTeardownMechanism. Same props/schema; text scaled up so the heading and
 * quote block fill the tall canvas and read on a phone.
 * ILLUSTRATE LAW: concept illustration, NOT a UI beat.
 */

export { skillTeardownMechanismSchema };

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const MONO = CLAUDE_FONT.mono;

const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));

export const SkillTeardownMechanism916: React.FC<SkillTeardownMechanismProps> = ({
  eyebrow, heading, body, quote, cite, verdictLabel, verdictPositive, sparkLine,
}) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();

  const headerIn = spring({ frame, fps, config: { damping: 28, stiffness: 120, mass: 0.9 } });
  const bodyIn = spring({ frame: frame - 18, fps, config: { damping: 26, stiffness: 110, mass: 1.0 } });
  const quoteIn = spring({ frame: frame - 32, fps, config: { damping: 26, stiffness: 110, mass: 1.0 } });
  const verdictIn = spring({ frame: frame - 50, fps, config: { damping: 26, stiffness: 110, mass: 1.0 } });
  const sparkIn = spring({ frame: frame - 65, fps, config: { damping: 28, stiffness: 120, mass: 0.9 } });

  const hasQuote = !!quote;
  const hasVerdict = !!verdictLabel;

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>

      {/* Eyebrow */}
      <div style={{
        position: 'absolute',
        top: height * 0.055,
        left: 0, right: 0,
        textAlign: 'center',
        fontFamily: SANS,
        fontSize: 22,
        fontWeight: 700,
        letterSpacing: 5,
        textTransform: 'uppercase' as const,
        color: CLAUDE.INK_SOFT,
        opacity: clamp(headerIn, 0, 1),
      }}>
        {eyebrow}
      </div>

      {/* Heading — large serif */}
      <div style={{
        position: 'absolute',
        top: height * 0.10,
        left: width * 0.06,
        right: width * 0.06,
        fontFamily: SERIF,
        fontSize: 72,
        fontWeight: 700,
        color: CLAUDE.INK,
        lineHeight: 1.12,
        textAlign: 'center' as const,
        opacity: clamp(headerIn, 0, 1),
        transform: `translateY(${(1 - clamp(headerIn, 0, 1)) * 12}px)`,
      }}>
        {heading}
      </div>

      {/* Body text */}
      {body && (
        <div style={{
          position: 'absolute',
          top: height * (hasQuote ? 0.30 : 0.32),
          left: width * 0.06,
          right: width * 0.06,
          fontFamily: SANS,
          fontSize: 34,
          color: CLAUDE.INK,
          lineHeight: 1.48,
          textAlign: 'center' as const,
          opacity: clamp(bodyIn, 0, 1),
          transform: `translateY(${(1 - clamp(bodyIn, 0, 1)) * 10}px)`,
        }}>
          {body}
        </div>
      )}

      {/* Quote block */}
      {hasQuote && (
        <div style={{
          position: 'absolute',
          top: body ? height * 0.54 : height * 0.32,
          left: width * 0.06,
          right: width * 0.06,
          background: CLAUDE.CARD,
          border: `1px solid ${CLAUDE.BORDER}`,
          borderLeft: `5px solid ${CLAUDE.SPARK}`,
          borderRadius: 14,
          padding: '24px 30px',
          opacity: clamp(quoteIn, 0, 1),
          transform: `translateY(${(1 - clamp(quoteIn, 0, 1)) * 10}px)`,
        }}>
          <div style={{ fontFamily: MONO, fontSize: 28, color: CLAUDE.INK, lineHeight: 1.5, whiteSpace: 'pre-wrap' as const }}>
            "{quote}"
          </div>
          {cite && (
            <div style={{ fontFamily: SANS, fontSize: 20, color: CLAUDE.GHOST, marginTop: 12 }}>
              Source: {cite}
            </div>
          )}
        </div>
      )}

      {/* Verdict pill */}
      {hasVerdict && (
        <div style={{
          position: 'absolute',
          bottom: height * 0.12,
          left: width * 0.06,
          display: 'flex',
          alignItems: 'center',
          gap: 12,
          opacity: clamp(verdictIn, 0, 1),
          transform: `translateY(${(1 - clamp(verdictIn, 0, 1)) * 8}px)`,
        }}>
          <div style={{
            background: verdictPositive ? 'rgba(217,119,87,0.14)' : 'rgba(61,57,41,0.10)',
            border: `2px solid ${verdictPositive ? CLAUDE.SPARK : CLAUDE.BORDER}`,
            borderRadius: 32,
            padding: '10px 26px',
            fontFamily: SANS,
            fontSize: 22,
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
        left: width * 0.06,
        right: width * 0.06,
        bottom: height * 0.075,
        textAlign: 'center' as const,
        opacity: clamp(sparkIn, 0, 1),
        transform: `translateY(${(1 - clamp(sparkIn, 0, 1)) * 8}px)`,
      }}>
        <span style={{ fontFamily: SERIF, fontSize: 30, fontStyle: 'italic', color: CLAUDE.INK }}>{sparkLine}</span>
      </div>

    </AbsoluteFill>
  );
};
