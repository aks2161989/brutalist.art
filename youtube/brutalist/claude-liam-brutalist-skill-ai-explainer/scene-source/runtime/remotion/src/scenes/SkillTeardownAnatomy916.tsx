import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring } from 'remotion';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { skillTeardownAnatomySchema, SkillTeardownAnatomyProps } from './SkillTeardownAnatomy';

/**
 * SkillTeardownAnatomy916 — portrait (1080x1920) native variant of
 * SkillTeardownAnatomy. Same props/schema; sizes scaled up so the folder tree
 * fills the tall canvas and reads on a phone. Vertical list is portrait-native.
 * ILLUSTRATE LAW: concept illustration, NOT a UI beat.
 */

export { skillTeardownAnatomySchema };

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const MONO = CLAUDE_FONT.mono;

const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));

export const SkillTeardownAnatomy916: React.FC<SkillTeardownAnatomyProps> = ({
  skillName, oldName, eyebrow, title, files, calloutText, calloutSub, sparkLine,
}) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();

  const headerIn = spring({ frame, fps, config: { damping: 28, stiffness: 120, mass: 0.9 } });
  const sparkIn = spring({ frame: frame - 70, fps, config: { damping: 28, stiffness: 120, mass: 0.9 } });

  const DELAY_PER_FILE = 8;
  const fileIn = files.map((_, i) =>
    spring({ frame: frame - 20 - i * DELAY_PER_FILE, fps, config: { damping: 30, stiffness: 140, mass: 0.8 } })
  );
  const calloutIn = spring({ frame: frame - 20 - files.length * DELAY_PER_FILE - 4, fps, config: { damping: 28, stiffness: 120, mass: 0.9 } });

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>

      {/* Eyebrow */}
      <div style={{
        position: 'absolute',
        top: height * 0.06,
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
        {eyebrow}{oldName ? ` · was ${oldName}` : ''}
      </div>

      {/* Section title */}
      <div style={{
        position: 'absolute',
        top: height * 0.10,
        left: width * 0.06, right: width * 0.06,
        textAlign: 'center',
        fontFamily: SERIF,
        fontSize: 68,
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
        top: height * 0.22,
        left: width * 0.08,
        right: width * 0.06,
        bottom: height * 0.12,
      }}>
        {files.map((f, i) => {
          const op = clamp(fileIn[i], 0, 1);
          const tx = (1 - op) * -16;
          return (
            <div key={i} style={{
              display: 'flex',
              alignItems: 'center',
              gap: 14,
              paddingLeft: f.indent * 40,
              marginBottom: 22,
              opacity: op,
              transform: `translateX(${tx}px)`,
            }}>
              <span style={{ fontFamily: MONO, fontSize: 32, color: f.accent ? CLAUDE.SPARK : CLAUDE.INK_SOFT }}>{f.icon}</span>
              <span style={{
                fontFamily: MONO,
                fontSize: 34,
                color: f.accent ? CLAUDE.SPARK : CLAUDE.INK,
                fontWeight: f.accent ? 700 : 400,
              }}>{f.name}</span>
              {f.size && (
                <span style={{ fontFamily: MONO, fontSize: 24, color: CLAUDE.GHOST, marginLeft: 12 }}>{f.size}</span>
              )}
              {f.tag && (
                <div style={{
                  background: CLAUDE.SPARK, borderRadius: 8, padding: '4px 12px', marginLeft: 8,
                  fontFamily: SANS, fontSize: 18, fontWeight: 700, color: '#fff',
                  letterSpacing: 1.5, textTransform: 'uppercase' as const,
                }}>{f.tag}</div>
              )}
            </div>
          );
        })}

        {/* Callout box */}
        {(calloutText || calloutSub) && (
          <div style={{
            marginTop: 26,
            padding: '20px 26px',
            background: 'rgba(217,119,87,0.07)',
            border: `1px solid ${CLAUDE.SPARK}`,
            borderLeft: `5px solid ${CLAUDE.SPARK}`,
            borderRadius: 14,
            opacity: clamp(calloutIn, 0, 1),
            transform: `translateY(${(1 - clamp(calloutIn, 0, 1)) * 10}px)`,
          }}>
            {calloutText && (
              <div style={{ fontFamily: SANS, fontSize: 32, color: CLAUDE.INK, lineHeight: 1.45 }}
                dangerouslySetInnerHTML={{ __html: calloutText }} />
            )}
            {calloutSub && (
              <div style={{ fontFamily: SANS, fontSize: 22, color: CLAUDE.INK_SOFT, marginTop: 8 }}>{calloutSub}</div>
            )}
          </div>
        )}
      </div>

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
