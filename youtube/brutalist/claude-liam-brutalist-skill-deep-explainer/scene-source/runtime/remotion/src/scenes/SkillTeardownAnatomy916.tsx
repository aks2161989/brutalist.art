import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring } from 'remotion';
import { skillTeardownAnatomySchema } from './SkillTeardownAnatomy';
import type { SkillTeardownAnatomyProps } from './SkillTeardownAnatomy';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * SkillTeardownAnatomy916 — portrait 9:16 (1080×1920) version of SkillTeardownAnatomy.
 * Same schema. Column-oriented reflow: eyebrow + title at top, folder tree spans
 * mid-frame vertical band, callout below tree, spark line at bottom of active band.
 * Safe zone: top 12% (~230px) and bottom 25% (~480px) reserved for platform UI.
 */

export const skillTeardownAnatomy916Schema = skillTeardownAnatomySchema;
export type SkillTeardownAnatomy916Props = SkillTeardownAnatomyProps;

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const MONO = CLAUDE_FONT.mono;

const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));


export const SkillTeardownAnatomy916: React.FC<SkillTeardownAnatomy916Props> = ({
  skillName, oldName, eyebrow, title, files, calloutText, calloutSub, sparkLine,
}) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();

  const headerIn = spring({ frame, fps, config: { damping: 28, stiffness: 120, mass: 0.9 } });
  const sparkIn = spring({ frame: frame - 55, fps, config: { damping: 28, stiffness: 120, mass: 0.9 } });

  const DELAY_PER_FILE = 8;
  const fileIn = files.map((_, i) =>
    spring({ frame: frame - 20 - i * DELAY_PER_FILE, fps, config: { damping: 30, stiffness: 140, mass: 0.8 } })
  );
  const calloutIn = spring({ frame: frame - 20 - files.length * DELAY_PER_FILE - 4, fps, config: { damping: 28, stiffness: 120, mass: 0.9 } });

  // Portrait sizes derived from height
  const EYEBROW_FONT = Math.round(height * 0.014);
  const TITLE_FONT   = Math.round(height * 0.034);
  const FILE_NAME    = Math.round(height * 0.019);
  const FILE_SIZE    = Math.round(height * 0.014);
  const TAG_FONT     = Math.round(height * 0.010);
  const CALLOUT_MAIN = Math.round(height * 0.019);
  const CALLOUT_SUB  = Math.round(height * 0.014);
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
        {eyebrow}{oldName ? ` · was ${oldName}` : ''}
      </div>

      {/* Section title */}
      <div style={{
        position: 'absolute',
        top: height * 0.18,
        left: width * 0.06,
        right: width * 0.06,
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

      {/* Folder tree */}
      <div style={{
        position: 'absolute',
        top: height * 0.30,
        left: width * 0.10,
        right: width * 0.06,
        bottom: height * 0.32,
      }}>
        {files.map((f, i) => {
          const op = clamp(fileIn[i], 0, 1);
          const tx = (1 - op) * -14;
          return (
            <div key={i} style={{
              display: 'flex',
              alignItems: 'center',
              gap: 8,
              paddingLeft: f.indent * 26,
              marginBottom: height * 0.011,
              opacity: op,
              transform: `translateX(${tx}px)`,
            }}>
              <span style={{ fontFamily: MONO, fontSize: FILE_NAME - 2, color: f.accent ? CLAUDE.SPARK : CLAUDE.INK_SOFT }}>{f.icon}</span>
              <span style={{
                fontFamily: MONO,
                fontSize: FILE_NAME,
                color: f.accent ? CLAUDE.SPARK : CLAUDE.INK,
                fontWeight: f.accent ? 700 : 400,
                overflow: 'hidden',
                textOverflow: 'ellipsis',
                whiteSpace: 'nowrap',
                maxWidth: width * 0.55,
              }}>{f.name}</span>
              {f.size && (
                <span style={{ fontFamily: MONO, fontSize: FILE_SIZE, color: CLAUDE.GHOST, marginLeft: 8 }}>{f.size}</span>
              )}
              {f.tag && (
                <div style={{
                  background: CLAUDE.SPARK, borderRadius: 5, padding: '2px 6px', marginLeft: 6,
                  fontFamily: SANS, fontSize: TAG_FONT, fontWeight: 700, color: '#fff',
                  letterSpacing: 1, textTransform: 'uppercase' as const,
                }}>{f.tag}</div>
              )}
            </div>
          );
        })}

        {/* Callout box */}
        {(calloutText || calloutSub) && (
          <div style={{
            marginTop: height * 0.015,
            padding: '14px 18px',
            background: 'rgba(217,119,87,0.07)',
            border: `1px solid ${CLAUDE.SPARK}`,
            borderLeft: `4px solid ${CLAUDE.SPARK}`,
            borderRadius: 10,
            opacity: clamp(calloutIn, 0, 1),
            transform: `translateY(${(1 - clamp(calloutIn, 0, 1)) * 10}px)`,
          }}>
            {calloutText && (
              <div style={{ fontFamily: SANS, fontSize: CALLOUT_MAIN, color: CLAUDE.INK, lineHeight: 1.45 }}
                dangerouslySetInnerHTML={{ __html: calloutText }} />
            )}
            {calloutSub && (
              <div style={{ fontFamily: SANS, fontSize: CALLOUT_SUB, color: CLAUDE.INK_SOFT, marginTop: 6 }}>{calloutSub}</div>
            )}
          </div>
        )}
      </div>

      {/* Spark line — bottom of active band, above the 25% bottom UI-safe strip */}
      <div style={{
        position: 'absolute',
        left: width * 0.06,
        bottom: height * 0.26,
        right: width * 0.06,
        display: 'flex',
        alignItems: 'center',
        gap: 10,
        opacity: clamp(sparkIn, 0, 1),
        transform: `translateY(${(1 - clamp(sparkIn, 0, 1)) * 8}px)`,
      }}>
        <span style={{ fontFamily: SERIF, fontSize: SPARK_FONT, fontStyle: 'italic', color: CLAUDE.INK }}>{sparkLine}</span>
      </div>

    </AbsoluteFill>
  );
};
