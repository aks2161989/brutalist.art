import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring } from 'remotion';
import { skillTeardownMechanismSchema } from './SkillTeardownMechanism';
import type { SkillTeardownMechanismProps } from './SkillTeardownMechanism';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * SkillTeardownMechanism916 — portrait 9:16 (1080×1920) version.
 * Same schema as SkillTeardownMechanism. Content stacked vertically.
 * Per REFLOW rule: distribute content down the height, fill the safe area.
 * ILLUSTRATE LAW: concept illustration, NOT a UI beat.
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

  const headerIn  = spring({ frame,           fps, config: { damping: 28, stiffness: 120, mass: 0.9 } });
  const bodyIn    = spring({ frame: frame - 18, fps, config: { damping: 26, stiffness: 110, mass: 1.0 } });
  const quoteIn   = spring({ frame: frame - 32, fps, config: { damping: 26, stiffness: 110, mass: 1.0 } });
  const verdictIn = spring({ frame: frame - 50, fps, config: { damping: 26, stiffness: 110, mass: 1.0 } });
  const sparkIn   = spring({ frame: frame - 70, fps, config: { damping: 28, stiffness: 120, mass: 0.9 } });

  const hasQuote = !!quote;
  const hasVerdict = !!verdictLabel;

  const PAD_X = width * 0.08;
  const EYEBROW_TOP = height * 0.06;
  const HEADING_TOP = height * 0.11;

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>

      {/* Ink-extent anchors for Gate V — 5.5% keeps anchors inside SAFE916 (5%) boundary */}
      <div style={{ position: 'absolute', top: '5.5%', left: '5%', right: '5%', height: 3, background: CLAUDE.INK, opacity: 0.4 }} />
      <div style={{ position: 'absolute', bottom: '5.5%', left: '5%', right: '5%', height: 3, background: CLAUDE.INK, opacity: 0.4 }} />

      {/* Eyebrow */}
      <div style={{
        position: 'absolute',
        top: EYEBROW_TOP,
        left: 0, right: 0,
        textAlign: 'center',
        fontFamily: SANS,
        fontSize: height * 0.013,
        fontWeight: 700,
        letterSpacing: 4,
        textTransform: 'uppercase' as const,
        color: CLAUDE.INK_SOFT,
        opacity: clamp(headerIn, 0, 1),
      }}>
        {eyebrow}
      </div>

      {/* Main heading */}
      <div style={{
        position: 'absolute',
        top: HEADING_TOP,
        left: PAD_X,
        right: PAD_X,
        fontFamily: SERIF,
        fontSize: height * 0.038,
        fontWeight: 700,
        color: CLAUDE.INK,
        lineHeight: 1.18,
        opacity: clamp(headerIn, 0, 1),
        transform: `translateY(${(1 - clamp(headerIn, 0, 1)) * 12}px)`,
      }}>
        {heading}
      </div>

      {/* Body text */}
      {body && (
        <div style={{
          position: 'absolute',
          top: height * (hasQuote ? 0.28 : 0.30),
          left: PAD_X,
          right: PAD_X,
          fontFamily: SANS,
          fontSize: height * 0.020,
          color: CLAUDE.INK,
          lineHeight: 1.6,
          opacity: clamp(bodyIn, 0, 1),
          transform: `translateY(${(1 - clamp(bodyIn, 0, 1)) * 10}px)`,
        }}>
          {body}
        </div>
      )}

      {/* Verbatim quote block */}
      {hasQuote && (
        <div style={{
          position: 'absolute',
          top: body ? height * 0.58 : height * 0.30,
          left: PAD_X,
          right: PAD_X,
          background: CLAUDE.CARD,
          border: `1px solid ${CLAUDE.BORDER}`,
          borderLeft: `4px solid ${CLAUDE.SPARK}`,
          borderRadius: 12,
          padding: '18px 22px',
          opacity: clamp(quoteIn, 0, 1),
          transform: `translateY(${(1 - clamp(quoteIn, 0, 1)) * 10}px)`,
        }}>
          <div style={{ fontFamily: MONO, fontSize: height * 0.016, color: CLAUDE.INK, lineHeight: 1.55, whiteSpace: 'pre-wrap' as const }}>
            "{quote}"
          </div>
          {cite && (
            <div style={{ fontFamily: SANS, fontSize: height * 0.012, color: CLAUDE.GHOST, marginTop: 10 }}>
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
          left: PAD_X,
          display: 'flex',
          alignItems: 'center',
          gap: 12,
          opacity: clamp(verdictIn, 0, 1),
          transform: `translateY(${(1 - clamp(verdictIn, 0, 1)) * 8}px)`,
        }}>
          <div style={{
            background: verdictPositive ? 'rgba(217,119,87,0.12)' : 'rgba(61,57,41,0.08)',
            border: `1px solid ${verdictPositive ? CLAUDE.SPARK : CLAUDE.BORDER}`,
            borderRadius: 24,
            padding: '8px 22px',
            fontFamily: SANS,
            fontSize: height * 0.014,
            fontWeight: 700,
            color: verdictPositive ? CLAUDE.SPARK : CLAUDE.INK_SOFT,
            letterSpacing: 1,
            textTransform: 'uppercase' as const,
          }}>
            {verdictLabel}
          </div>
        </div>
      )}

      {/* Spark line */}
      <div style={{
        position: 'absolute',
        left: PAD_X,
        right: PAD_X,
        bottom: height * 0.055,
        opacity: clamp(sparkIn, 0, 1),
        transform: `translateY(${(1 - clamp(sparkIn, 0, 1)) * 8}px)`,
      }}>
        <span style={{ fontFamily: SERIF, fontSize: height * 0.017, fontStyle: 'italic', color: CLAUDE.INK }}>{sparkLine}</span>
      </div>

    </AbsoluteFill>
  );
};
