import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring } from 'remotion';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { skillTeardownPipelineSchema, SkillTeardownPipelineProps } from './SkillTeardownPipeline';

/**
 * SkillTeardownPipeline916 — vertical stacked variant of SkillTeardownPipeline
 * for portrait (1080x1920) rendering. Same schema/props; input → phases → output
 * are stacked top-to-bottom instead of side-by-side, with down-arrows between
 * nodes. Fonts scaled up because the 1920-tall canvas needs bigger text than the
 * landscape 1080-tall one to read from a phone screen.
 * ILLUSTRATE LAW: concept illustration, NOT a UI beat.
 */

export { skillTeardownPipelineSchema };

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;

const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));

const DownArrow: React.FC<{ opacity: number }> = ({ opacity }) => (
  <div style={{ display: 'flex', flexDirection: 'column' as const, alignItems: 'center', opacity, margin: '6px 0' }}>
    <div style={{ width: 3, height: 24, background: CLAUDE.SPARK }} />
    <div style={{
      width: 0, height: 0,
      borderTop: `12px solid ${CLAUDE.SPARK}`,
      borderLeft: '7px solid transparent',
      borderRight: '7px solid transparent',
    }} />
  </div>
);

export const SkillTeardownPipeline916: React.FC<SkillTeardownPipelineProps> = ({
  eyebrow, title, inputLabel, outputLabel, phases, footerNote, sparkLine,
}) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();

  const headerIn = spring({ frame, fps, config: { damping: 28, stiffness: 120, mass: 0.9 } });
  const sparkIn = spring({ frame: frame - 70, fps, config: { damping: 28, stiffness: 120, mass: 0.9 } });

  const allNodes = ['input', ...phases.map((_, i) => `p${i}`), 'output'];
  const nodeIn = allNodes.map((_, i) =>
    spring({ frame: frame - 20 - i * 10, fps, config: { damping: 28, stiffness: 130, mass: 0.85 } })
  );

  const boxW = Math.floor(width * 0.78);

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

      {/* Title */}
      <div style={{
        position: 'absolute',
        top: height * 0.09,
        left: width * 0.06, right: width * 0.06,
        textAlign: 'center',
        fontFamily: SERIF,
        fontSize: 62,
        fontWeight: 700,
        color: CLAUDE.INK,
        lineHeight: 1.15,
        opacity: clamp(headerIn, 0, 1),
        transform: `translateY(${(1 - clamp(headerIn, 0, 1)) * 12}px)`,
      }}>
        {title}
      </div>

      {/* Stacked pipeline (vertical) */}
      <div style={{
        position: 'absolute',
        top: height * 0.20,
        left: 0, right: 0,
        bottom: height * 0.12,
        display: 'flex',
        flexDirection: 'column' as const,
        alignItems: 'center',
        justifyContent: 'flex-start',
      }}>

        {/* INPUT */}
        <div style={{
          width: boxW,
          background: CLAUDE.FOOTER,
          border: `1px solid ${CLAUDE.BORDER}`,
          borderRadius: 14,
          padding: '16px 22px',
          textAlign: 'center' as const,
          opacity: clamp(nodeIn[0], 0, 1),
          transform: `translateY(${(1 - clamp(nodeIn[0], 0, 1)) * 16}px)`,
        }}>
          <div style={{ fontFamily: SANS, fontSize: 16, fontWeight: 700, letterSpacing: 4, textTransform: 'uppercase' as const, color: CLAUDE.INK_SOFT, marginBottom: 4 }}>INPUT</div>
          <div style={{ fontFamily: SERIF, fontSize: 34, color: CLAUDE.INK, fontWeight: 600 }}>{inputLabel}</div>
        </div>

        <DownArrow opacity={clamp(nodeIn[1], 0, 1)} />

        {/* Phases */}
        {phases.map((ph, i) => {
          const ni = i + 1;
          const op = clamp(nodeIn[ni], 0, 1);
          const isLast = i === phases.length - 1;
          return (
            <React.Fragment key={i}>
              <div style={{
                width: boxW,
                background: ph.accent ? 'rgba(217,119,87,0.08)' : CLAUDE.CARD,
                border: `1px solid ${ph.accent ? CLAUDE.SPARK : CLAUDE.BORDER}`,
                borderLeft: `6px solid ${ph.accent ? CLAUDE.SPARK : CLAUDE.INK}`,
                borderRadius: 14,
                padding: '18px 24px',
                textAlign: 'left' as const,
                boxShadow: '0 4px 16px rgba(61,57,41,0.07)',
                opacity: op,
                transform: `translateY(${(1 - op) * 16}px)`,
              }}>
                <div style={{ fontFamily: SERIF, fontSize: 38, color: ph.accent ? CLAUDE.SPARK : CLAUDE.INK, fontWeight: 700, lineHeight: 1.2 }}>{ph.label}</div>
                {ph.desc && (
                  <div style={{ fontFamily: SANS, fontSize: 24, color: CLAUDE.INK_SOFT, marginTop: 8, lineHeight: 1.4 }}>{ph.desc}</div>
                )}
              </div>
              {!isLast && <DownArrow opacity={clamp(nodeIn[ni + 1], 0, 1)} />}
            </React.Fragment>
          );
        })}

        <DownArrow opacity={clamp(nodeIn[phases.length + 1], 0, 1)} />

        {/* OUTPUT */}
        <div style={{
          width: boxW,
          background: 'rgba(217,119,87,0.07)',
          border: `2px solid ${CLAUDE.SPARK}`,
          borderRadius: 14,
          padding: '18px 24px',
          textAlign: 'center' as const,
          opacity: clamp(nodeIn[phases.length + 1], 0, 1),
          transform: `translateY(${(1 - clamp(nodeIn[phases.length + 1], 0, 1)) * 16}px)`,
        }}>
          <div style={{ fontFamily: SANS, fontSize: 16, fontWeight: 700, letterSpacing: 4, textTransform: 'uppercase' as const, color: CLAUDE.SPARK, marginBottom: 4 }}>OUTPUT</div>
          <div style={{ fontFamily: SERIF, fontSize: 34, color: CLAUDE.INK, fontWeight: 600 }}>{outputLabel}</div>
        </div>
      </div>

      {/* Footer note */}
      {footerNote && (
        <div style={{
          position: 'absolute',
          bottom: height * 0.115,
          left: 0, right: 0,
          textAlign: 'center',
          fontFamily: SANS,
          fontSize: 22,
          color: CLAUDE.INK_SOFT,
          opacity: clamp(nodeIn[nodeIn.length - 1], 0, 1),
        }}>
          {footerNote}
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
