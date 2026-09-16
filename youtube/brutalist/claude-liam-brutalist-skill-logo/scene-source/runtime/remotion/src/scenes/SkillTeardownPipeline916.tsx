import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring } from 'remotion';
import { skillTeardownPipelineSchema } from './SkillTeardownPipeline';
import type { SkillTeardownPipelineProps } from './SkillTeardownPipeline';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * SkillTeardownPipeline916 — portrait 9:16 (1080×1920) variant.
 * Same schema as landscape. Reflow: R1 (rotation) — flow rotates from
 * horizontal (INPUT→...→OUTPUT) to vertical (INPUT↓...↓OUTPUT). Arrows are
 * down-pointing triangles. Boxes stack in a single column.
 */

export const skillTeardownPipeline916Schema = skillTeardownPipelineSchema;
export type SkillTeardownPipeline916Props = SkillTeardownPipelineProps;

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;

const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));

const DownArrow: React.FC<{ opacity: number }> = ({ opacity }) => (
  <div style={{
    display: 'flex',
    flexDirection: 'column' as const,
    alignItems: 'center',
    opacity,
    margin: '10px 0',
  }}>
    <div style={{ width: 2, height: 34, background: CLAUDE.SPARK }} />
    <div style={{
      width: 0, height: 0,
      borderTop: `14px solid ${CLAUDE.SPARK}`,
      borderLeft: '8px solid transparent',
      borderRight: '8px solid transparent',
    }} />
  </div>
);

export const SkillTeardownPipeline916: React.FC<SkillTeardownPipeline916Props> = ({
  eyebrow, title, inputLabel, outputLabel, phases, footerNote, sparkLine,
}) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();

  const headerIn = spring({ frame, fps, config: { damping: 28, stiffness: 120, mass: 0.9 } });
  const sparkIn = spring({ frame: frame - 60, fps, config: { damping: 28, stiffness: 120, mass: 0.9 } });

  const allNodes = ['input', ...phases.map((_, i) => `p${i}`), 'output'];
  const nodeIn = allNodes.map((_, i) =>
    spring({ frame: frame - 20 - i * 12, fps, config: { damping: 28, stiffness: 130, mass: 0.85 } })
  );

  const CONTENT_L = width * 0.06;
  const CONTENT_R = width * 0.06;
  const CONTENT_W = width - CONTENT_L - CONTENT_R;
  const BOX_W = CONTENT_W * 0.9;

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>

      {/* Eyebrow */}
      <div style={{
        position: 'absolute',
        top: height * 0.05,
        left: 0, right: 0,
        textAlign: 'center',
        fontFamily: SANS,
        fontSize: 22,
        fontWeight: 700,
        letterSpacing: 6,
        textTransform: 'uppercase' as const,
        color: CLAUDE.INK_SOFT,
        opacity: clamp(headerIn, 0, 1),
      }}>
        {eyebrow}
      </div>

      {/* Title */}
      <div style={{
        position: 'absolute',
        top: height * 0.08,
        left: CONTENT_L,
        width: CONTENT_W,
        textAlign: 'center' as const,
        fontFamily: SERIF,
        fontSize: 68,
        fontWeight: 700,
        color: CLAUDE.INK,
        opacity: clamp(headerIn, 0, 1),
        transform: `translateY(${(1 - clamp(headerIn, 0, 1)) * 14}px)`,
        lineHeight: 1.15,
      }}>
        {title}
      </div>

      {/* Vertical pipeline stack */}
      <div style={{
        position: 'absolute',
        top: height * 0.18,
        left: 0,
        right: 0,
        display: 'flex',
        flexDirection: 'column' as const,
        alignItems: 'center',
      }}>

        {/* INPUT */}
        <div style={{
          width: BOX_W,
          background: CLAUDE.FOOTER,
          border: `1px solid ${CLAUDE.BORDER}`,
          borderRadius: 14,
          padding: '20px 22px',
          textAlign: 'center' as const,
          opacity: clamp(nodeIn[0], 0, 1),
          transform: `translateY(${(1 - clamp(nodeIn[0], 0, 1)) * 16}px)`,
          boxSizing: 'border-box' as const,
        }}>
          <div style={{ fontFamily: SANS, fontSize: 18, fontWeight: 700, letterSpacing: 3, textTransform: 'uppercase' as const, color: CLAUDE.INK_SOFT, marginBottom: 8 }}>INPUT</div>
          <div style={{ fontFamily: SERIF, fontSize: 34, color: CLAUDE.INK, fontWeight: 600 }}>{inputLabel}</div>
        </div>

        <DownArrow opacity={clamp(nodeIn[1], 0, 1)} />

        {/* Phase nodes */}
        {phases.map((ph, i) => {
          const ni = i + 1;
          const op = clamp(nodeIn[ni], 0, 1);
          return (
            <React.Fragment key={i}>
              <div style={{
                width: BOX_W,
                background: ph.accent ? 'rgba(217,119,87,0.08)' : CLAUDE.CARD,
                border: `1px solid ${ph.accent ? CLAUDE.SPARK : CLAUDE.BORDER}`,
                borderLeft: `6px solid ${ph.accent ? CLAUDE.SPARK : CLAUDE.INK}`,
                borderRadius: 14,
                padding: '20px 22px',
                textAlign: 'center' as const,
                boxShadow: '0 4px 20px rgba(61,57,41,0.08)',
                opacity: op,
                transform: `translateY(${(1 - op) * 16}px)`,
                boxSizing: 'border-box' as const,
              }}>
                <div style={{ fontFamily: SERIF, fontSize: 42, color: ph.accent ? CLAUDE.SPARK : CLAUDE.INK, fontWeight: 700, lineHeight: 1.2 }}>{ph.label}</div>
                {ph.desc && (
                  <div style={{ fontFamily: SANS, fontSize: 22, color: CLAUDE.INK_SOFT, marginTop: 8, lineHeight: 1.4, wordBreak: 'break-word' as const }}>{ph.desc}</div>
                )}
              </div>
              {i < phases.length && <DownArrow opacity={clamp(nodeIn[ni + 1], 0, 1)} />}
            </React.Fragment>
          );
        })}

        {/* OUTPUT */}
        <div style={{
          width: BOX_W,
          background: 'rgba(217,119,87,0.08)',
          border: `2px solid ${CLAUDE.SPARK}`,
          borderRadius: 14,
          padding: '20px 22px',
          textAlign: 'center' as const,
          opacity: clamp(nodeIn[phases.length + 1], 0, 1),
          transform: `translateY(${(1 - clamp(nodeIn[phases.length + 1], 0, 1)) * 16}px)`,
          boxSizing: 'border-box' as const,
        }}>
          <div style={{ fontFamily: SANS, fontSize: 18, fontWeight: 700, letterSpacing: 3, textTransform: 'uppercase' as const, color: CLAUDE.SPARK, marginBottom: 8 }}>OUTPUT</div>
          <div style={{ fontFamily: SERIF, fontSize: 30, color: CLAUDE.INK, fontWeight: 600, wordBreak: 'break-word' as const }}>{outputLabel}</div>
        </div>
      </div>

      {/* Footer note */}
      {footerNote && (
        <div style={{
          position: 'absolute',
          bottom: height * 0.12,
          left: CONTENT_L,
          width: CONTENT_W,
          textAlign: 'center' as const,
          fontFamily: SANS,
          fontSize: 26,
          color: CLAUDE.INK_SOFT,
          lineHeight: 1.4,
          opacity: clamp(nodeIn[nodeIn.length - 1], 0, 1),
          wordBreak: 'break-word' as const,
        }}>
          {footerNote}
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
        <span style={{ fontFamily: SERIF, fontSize: 34, fontStyle: 'italic', color: CLAUDE.INK }}>{sparkLine}</span>
      </div>

    </AbsoluteFill>
  );
};
