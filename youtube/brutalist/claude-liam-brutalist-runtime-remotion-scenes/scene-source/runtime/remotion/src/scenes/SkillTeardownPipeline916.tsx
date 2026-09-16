import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring } from 'remotion';
import { skillTeardownPipelineSchema } from './SkillTeardownPipeline';
import type { SkillTeardownPipelineProps } from './SkillTeardownPipeline';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * SkillTeardownPipeline916 — portrait 9:16 (1080×1920) version.
 * Same schema as SkillTeardownPipeline. Phases stacked vertically.
 * Per REFLOW rule: portrait layout distributes content down the height axis.
 * ILLUSTRATE LAW: concept illustration, NOT a UI beat.
 */

export const skillTeardownPipeline916Schema = skillTeardownPipelineSchema;
export type SkillTeardownPipeline916Props = SkillTeardownPipelineProps;

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;

const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));

const DownArrow: React.FC<{ opacity: number }> = ({ opacity }) => (
  <div style={{ display: 'flex', flexDirection: 'column' as const, alignItems: 'center', opacity, marginTop: 0 }}>
    <div style={{ width: 2, height: 28, background: CLAUDE.SPARK }} />
    <div style={{
      width: 0, height: 0,
      borderLeft: '8px solid transparent',
      borderRight: '8px solid transparent',
      borderTop: `12px solid ${CLAUDE.SPARK}`,
    }} />
  </div>
);

export const SkillTeardownPipeline916: React.FC<SkillTeardownPipeline916Props> = ({
  eyebrow, title, inputLabel, outputLabel, phases, footerNote, sparkLine,
}) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();

  const headerIn = spring({ frame, fps, config: { damping: 28, stiffness: 120, mass: 0.9 } });
  const sparkIn = spring({ frame: frame - 80, fps, config: { damping: 28, stiffness: 120, mass: 0.9 } });

  const allNodes = ['input', ...phases.map((_, i) => `p${i}`), 'output'];
  const nodeIn = allNodes.map((_, i) =>
    spring({ frame: frame - 20 - i * 10, fps, config: { damping: 28, stiffness: 130, mass: 0.85 } })
  );

  const PAD_X = width * 0.07;
  const BOX_W = width - PAD_X * 2;
  const BOX_H = 90;
  const TITLE_TOP = height * 0.06;
  const PIPELINE_TOP = height * 0.20;

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>

      {/* Ink-extent top anchor */}
      <div style={{ position: 'absolute', top: '4%', left: '5%', right: '5%', height: 3, background: CLAUDE.INK, opacity: 0.4 }} />
      <div style={{ position: 'absolute', bottom: '4%', left: '5%', right: '5%', height: 3, background: CLAUDE.INK, opacity: 0.4 }} />

      {/* Eyebrow */}
      <div style={{
        position: 'absolute',
        top: TITLE_TOP,
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

      {/* Title */}
      <div style={{
        position: 'absolute',
        top: TITLE_TOP + height * 0.04,
        left: PAD_X,
        right: PAD_X,
        textAlign: 'center',
        fontFamily: SERIF,
        fontSize: height * 0.033,
        fontWeight: 700,
        color: CLAUDE.INK,
        lineHeight: 1.15,
        opacity: clamp(headerIn, 0, 1),
        transform: `translateY(${(1 - clamp(headerIn, 0, 1)) * 12}px)`,
      }}>
        {title}
      </div>

      {/* Vertical pipeline */}
      <div style={{
        position: 'absolute',
        top: PIPELINE_TOP,
        left: PAD_X,
        right: PAD_X,
        display: 'flex',
        flexDirection: 'column' as const,
        alignItems: 'center',
        gap: 0,
      }}>

        {/* INPUT node */}
        <div style={{
          width: '100%',
          opacity: clamp(nodeIn[0], 0, 1),
          transform: `translateY(${(1 - clamp(nodeIn[0], 0, 1)) * 12}px)`,
        }}>
          <div style={{
            width: BOX_W, minHeight: BOX_H,
            background: CLAUDE.FOOTER || '#F5F3EE',
            border: `1px solid ${CLAUDE.BORDER}`,
            borderRadius: 10,
            padding: '14px 18px',
            textAlign: 'center' as const,
            boxSizing: 'border-box' as const,
          }}>
            <div style={{ fontFamily: SANS, fontSize: height * 0.012, fontWeight: 700, letterSpacing: 3, textTransform: 'uppercase' as const, color: CLAUDE.INK_SOFT, marginBottom: 6 }}>INPUT</div>
            <div style={{ fontFamily: SERIF, fontSize: height * 0.017, color: CLAUDE.INK, fontWeight: 600, lineHeight: 1.3, whiteSpace: 'pre-line' as const }}>{inputLabel}</div>
          </div>
        </div>

        <DownArrow opacity={clamp(nodeIn[1], 0, 1)} />

        {/* Phase nodes */}
        {phases.map((ph, i) => {
          const ni = i + 1;
          const op = clamp(nodeIn[ni], 0, 1);
          return (
            <React.Fragment key={i}>
              <div style={{
                width: '100%',
                opacity: op,
                transform: `translateY(${(1 - op) * 12}px)`,
              }}>
                <div style={{
                  width: BOX_W, minHeight: BOX_H,
                  background: ph.accent ? 'rgba(217,119,87,0.07)' : CLAUDE.CARD,
                  border: `1px solid ${ph.accent ? CLAUDE.SPARK : CLAUDE.BORDER}`,
                  borderLeft: `4px solid ${ph.accent ? CLAUDE.SPARK : CLAUDE.INK}`,
                  borderRadius: 10,
                  padding: '14px 18px',
                  textAlign: 'left' as const,
                  boxShadow: '0 4px 16px rgba(61,57,41,0.07)',
                  boxSizing: 'border-box' as const,
                }}>
                  <div style={{ fontFamily: SERIF, fontSize: height * 0.018, color: ph.accent ? CLAUDE.SPARK : CLAUDE.INK, fontWeight: 600, lineHeight: 1.25 }}>{ph.label}</div>
                  {ph.desc && (
                    <div style={{ fontFamily: SANS, fontSize: height * 0.013, color: CLAUDE.INK_SOFT, marginTop: 6, lineHeight: 1.4 }}>{ph.desc}</div>
                  )}
                </div>
              </div>
              {i < phases.length - 1 && <DownArrow opacity={clamp(nodeIn[ni + 1], 0, 1)} />}
            </React.Fragment>
          );
        })}

        <DownArrow opacity={clamp(nodeIn[phases.length + 1], 0, 1)} />

        {/* OUTPUT node */}
        <div style={{
          width: '100%',
          opacity: clamp(nodeIn[phases.length + 1], 0, 1),
          transform: `translateY(${(1 - clamp(nodeIn[phases.length + 1], 0, 1)) * 12}px)`,
        }}>
          <div style={{
            width: BOX_W, minHeight: BOX_H,
            background: 'rgba(217,119,87,0.07)',
            border: `2px solid ${CLAUDE.SPARK}`,
            borderRadius: 10,
            padding: '14px 18px',
            textAlign: 'center' as const,
            boxSizing: 'border-box' as const,
          }}>
            <div style={{ fontFamily: SANS, fontSize: height * 0.012, fontWeight: 700, letterSpacing: 3, textTransform: 'uppercase' as const, color: CLAUDE.SPARK, marginBottom: 6 }}>OUTPUT</div>
            <div style={{ fontFamily: SERIF, fontSize: height * 0.017, color: CLAUDE.INK, fontWeight: 600, lineHeight: 1.3, whiteSpace: 'pre-line' as const }}>{outputLabel}</div>
          </div>
        </div>

        {/* Footer note */}
        {footerNote && (
          <div style={{
            marginTop: height * 0.018,
            textAlign: 'center',
            fontFamily: SANS,
            fontSize: height * 0.013,
            color: CLAUDE.INK_SOFT,
            opacity: clamp(nodeIn[nodeIn.length - 1], 0, 1),
          }}>
            {footerNote}
          </div>
        )}
      </div>

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
