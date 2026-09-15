import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring } from 'remotion';
import { skillTeardownPipelineSchema } from './SkillTeardownPipeline';
import type { SkillTeardownPipelineProps } from './SkillTeardownPipeline';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * SkillTeardownPipeline916 — portrait 9:16 (1080×1920) version of SkillTeardownPipeline.
 * Same schema. Reflow: nodes STACK vertically with down-arrows instead of the
 * landscape row layout. Safe zone: top 12% and bottom 25% reserved for platform UI.
 */

export const skillTeardownPipeline916Schema = skillTeardownPipelineSchema;
export type SkillTeardownPipeline916Props = SkillTeardownPipelineProps;

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;

const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));

const DownArrow: React.FC<{ opacity: number }> = ({ opacity }) => (
  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', opacity, margin: '4px 0' }}>
    <div style={{ width: 2, height: 22, background: CLAUDE.SPARK }} />
    <div style={{
      width: 0, height: 0,
      borderTop: `10px solid ${CLAUDE.SPARK}`,
      borderLeft: '6px solid transparent',
      borderRight: '6px solid transparent',
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
    spring({ frame: frame - 20 - i * 10, fps, config: { damping: 28, stiffness: 130, mass: 0.85 } })
  );

  const EYEBROW_FONT = Math.round(height * 0.014);
  const TITLE_FONT   = Math.round(height * 0.034);
  const NODE_HEAD    = Math.round(height * 0.012);
  const NODE_LABEL   = Math.round(height * 0.022);
  const NODE_DESC    = Math.round(height * 0.015);
  const FOOTER_FONT  = Math.round(height * 0.016);
  const SPARK_FONT   = Math.round(height * 0.022);

  const boxW = Math.round(width * 0.60);

  const nodeStyle = (accent: boolean, isOutput: boolean) => ({
    width: boxW,
    minHeight: Math.round(height * 0.052),
    background: isOutput ? 'rgba(217,119,87,0.07)' : (accent ? 'rgba(217,119,87,0.07)' : CLAUDE.CARD),
    border: `1px solid ${isOutput ? CLAUDE.SPARK : (accent ? CLAUDE.SPARK : CLAUDE.BORDER)}`,
    borderLeft: `4px solid ${isOutput ? CLAUDE.SPARK : (accent ? CLAUDE.SPARK : CLAUDE.INK)}`,
    borderRadius: 10,
    padding: '10px 14px',
    textAlign: 'center' as const,
    boxShadow: '0 4px 16px rgba(61,57,41,0.07)',
  });

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

      {/* Title */}
      <div style={{
        position: 'absolute',
        top: height * 0.18,
        left: width * 0.06, right: width * 0.06,
        textAlign: 'center',
        fontFamily: SERIF,
        fontSize: TITLE_FONT,
        fontWeight: 700,
        color: CLAUDE.INK,
        lineHeight: 1.15,
        opacity: clamp(headerIn, 0, 1),
        transform: `translateY(${(1 - clamp(headerIn, 0, 1)) * 12}px)`,
      }}>
        {title}
      </div>

      {/* Pipeline column, centered horizontally */}
      <div style={{
        position: 'absolute',
        top: height * 0.26,
        left: 0, right: 0,
        display: 'flex',
        flexDirection: 'column' as const,
        alignItems: 'center',
      }}>

        {/* INPUT node */}
        <div style={{
          opacity: clamp(nodeIn[0], 0, 1),
          transform: `translateY(${(1 - clamp(nodeIn[0], 0, 1)) * 14}px)`,
        }}>
          <div style={nodeStyle(false, false)}>
            <div style={{ fontFamily: SANS, fontSize: NODE_HEAD, fontWeight: 700, letterSpacing: 3, textTransform: 'uppercase' as const, color: CLAUDE.INK_SOFT, marginBottom: 4 }}>INPUT</div>
            <div style={{ fontFamily: SERIF, fontSize: NODE_LABEL, color: CLAUDE.INK, fontWeight: 600 }}>{inputLabel}</div>
          </div>
        </div>

        <DownArrow opacity={clamp(nodeIn[1], 0, 1)} />

        {phases.map((ph, i) => {
          const ni = i + 1;
          const op = clamp(nodeIn[ni], 0, 1);
          return (
            <React.Fragment key={i}>
              <div style={{
                opacity: op,
                transform: `translateY(${(1 - op) * 14}px)`,
              }}>
                <div style={nodeStyle(ph.accent, false)}>
                  <div style={{ fontFamily: SERIF, fontSize: NODE_LABEL, color: ph.accent ? CLAUDE.SPARK : CLAUDE.INK, fontWeight: 600, lineHeight: 1.15 }}>{ph.label}</div>
                  {ph.desc && (
                    <div style={{ fontFamily: SANS, fontSize: NODE_DESC, color: CLAUDE.INK_SOFT, marginTop: 4, lineHeight: 1.3 }}>{ph.desc}</div>
                  )}
                </div>
              </div>
              {i < phases.length - 1 && <DownArrow opacity={clamp(nodeIn[ni + 1], 0, 1)} />}
            </React.Fragment>
          );
        })}

        <DownArrow opacity={clamp(nodeIn[phases.length + 1], 0, 1)} />

        <div style={{
          opacity: clamp(nodeIn[phases.length + 1], 0, 1),
          transform: `translateY(${(1 - clamp(nodeIn[phases.length + 1], 0, 1)) * 14}px)`,
        }}>
          <div style={nodeStyle(true, true)}>
            <div style={{ fontFamily: SANS, fontSize: NODE_HEAD, fontWeight: 700, letterSpacing: 3, textTransform: 'uppercase' as const, color: CLAUDE.SPARK, marginBottom: 4 }}>OUTPUT</div>
            <div style={{ fontFamily: SERIF, fontSize: NODE_LABEL, color: CLAUDE.INK, fontWeight: 600 }}>{outputLabel}</div>
          </div>
        </div>
      </div>

      {/* Footer note */}
      {footerNote && (
        <div style={{
          position: 'absolute',
          bottom: height * 0.30,
          left: width * 0.06, right: width * 0.06,
          textAlign: 'center',
          fontFamily: SANS,
          fontSize: FOOTER_FONT,
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
