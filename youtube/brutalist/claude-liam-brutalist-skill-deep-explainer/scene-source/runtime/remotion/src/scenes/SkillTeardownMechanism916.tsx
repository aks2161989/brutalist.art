import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring } from 'remotion';
import { skillTeardownMechanismSchema } from './SkillTeardownMechanism';
import type { SkillTeardownMechanismProps } from './SkillTeardownMechanism';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * SkillTeardownMechanism916 — portrait 9:16 (1080×1920) version of SkillTeardownMechanism.
 * Same schema. Reflow: heading occupies top ~35%; body under it; quote block sits
 * mid-frame; verdict pill and spark line at bottom of the active band.
 * Safe zone: top 12% and bottom 25% reserved for platform UI.
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

  // Portrait sizes
  const EYEBROW_FONT = Math.round(height * 0.014);
  const HEADING_FONT = Math.round(height * 0.036);
  const BODY_FONT    = Math.round(height * 0.020);
  const QUOTE_FONT   = Math.round(height * 0.020);
  const CITE_FONT    = Math.round(height * 0.013);
  const VERDICT_FONT = Math.round(height * 0.015);
  const SPARK_FONT   = Math.round(height * 0.022);

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>

      {/* Eyebrow */}
      <div style={{
        position: 'absolute',
        top: height * 0.14,
        left: 0, right: 0,
        textAlign: 'center',
        fontFamily: SANS,
        fontSize: EYEBROW_FONT,
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
        top: height * 0.185,
        left: width * 0.06,
        right: width * 0.06,
        fontFamily: SERIF,
        fontSize: HEADING_FONT,
        fontWeight: 700,
        color: CLAUDE.INK,
        lineHeight: 1.15,
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
          top: height * (hasQuote ? 0.30 : 0.33),
          left: width * 0.06,
          right: width * 0.06,
          fontFamily: SANS,
          fontSize: BODY_FONT,
          color: CLAUDE.INK,
          lineHeight: 1.5,
          textAlign: 'left' as const,
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
          top: body ? height * 0.50 : height * 0.32,
          left: width * 0.06,
          right: width * 0.06,
          background: CLAUDE.CARD,
          border: `1px solid ${CLAUDE.BORDER}`,
          borderLeft: `4px solid ${CLAUDE.SPARK}`,
          borderRadius: 10,
          padding: '18px 22px',
          opacity: clamp(quoteIn, 0, 1),
          transform: `translateY(${(1 - clamp(quoteIn, 0, 1)) * 10}px)`,
        }}>
          <div style={{
            fontFamily: MONO,
            fontSize: QUOTE_FONT,
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
              fontSize: CITE_FONT,
              color: CLAUDE.GHOST,
              marginTop: 10,
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
          bottom: height * 0.30,
          left: 0, right: 0,
          display: 'flex',
          justifyContent: 'center',
          opacity: clamp(verdictIn, 0, 1),
          transform: `translateY(${(1 - clamp(verdictIn, 0, 1)) * 8}px)`,
        }}>
          <div style={{
            background: verdictPositive ? 'rgba(217,119,87,0.12)' : 'rgba(61,57,41,0.08)',
            border: `1px solid ${verdictPositive ? CLAUDE.SPARK : CLAUDE.BORDER}`,
            borderRadius: 24,
            padding: '8px 20px',
            fontFamily: SANS,
            fontSize: VERDICT_FONT,
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
        left: width * 0.06,
        right: width * 0.06,
        bottom: height * 0.26,
        textAlign: 'center' as const,
        opacity: clamp(sparkIn, 0, 1),
        transform: `translateY(${(1 - clamp(sparkIn, 0, 1)) * 8}px)`,
      }}>
        <span style={{ fontFamily: SERIF, fontSize: SPARK_FONT, fontStyle: 'italic', color: CLAUDE.INK }}>{sparkLine}</span>
      </div>

    </AbsoluteFill>
  );
};
