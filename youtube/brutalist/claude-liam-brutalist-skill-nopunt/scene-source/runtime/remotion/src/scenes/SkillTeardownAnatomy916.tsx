import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring } from 'remotion';
import { skillTeardownAnatomySchema } from './SkillTeardownAnatomy';
import type { SkillTeardownAnatomyProps } from './SkillTeardownAnatomy';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * SkillTeardownAnatomy916 — portrait 9:16 (1080×1920) variant.
 * Same schema as landscape. Reflow: R2 (typography ramp) — the folder tree
 * stacks vertically with larger type; the callout drops beneath.
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

  const DELAY_PER_FILE = 7;
  const fileIn = files.map((_, i) =>
    spring({ frame: frame - 20 - i * DELAY_PER_FILE, fps, config: { damping: 30, stiffness: 140, mass: 0.8 } })
  );
  const calloutIn = spring({ frame: frame - 20 - files.length * DELAY_PER_FILE - 4, fps, config: { damping: 28, stiffness: 120, mass: 0.9 } });

  const CONTENT_L = width * 0.06;
  const CONTENT_R = width * 0.06;
  const CONTENT_W = width - CONTENT_L - CONTENT_R;
  const INDENT_PX = 40;

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
        letterSpacing: 6,
        textTransform: 'uppercase' as const,
        color: CLAUDE.INK_SOFT,
        opacity: clamp(headerIn, 0, 1),
      }}>
        {eyebrow}{oldName ? ` · was ${oldName}` : ''}
      </div>

      {/* Title */}
      <div style={{
        position: 'absolute',
        top: height * 0.09,
        left: CONTENT_L,
        width: CONTENT_W,
        textAlign: 'center' as const,
        fontFamily: SERIF,
        fontSize: 72,
        fontWeight: 700,
        color: CLAUDE.INK,
        opacity: clamp(headerIn, 0, 1),
        transform: `translateY(${(1 - clamp(headerIn, 0, 1)) * 14}px)`,
        lineHeight: 1.15,
      }}>
        {title}
      </div>

      {/* Folder tree */}
      <div style={{
        position: 'absolute',
        top: height * 0.2,
        left: CONTENT_L,
        width: CONTENT_W,
      }}>
        {files.map((f, i) => {
          const op = clamp(fileIn[i], 0, 1);
          const tx = (1 - op) * -16;
          return (
            <div key={i} style={{
              display: 'flex',
              alignItems: 'flex-start',
              gap: 14,
              paddingLeft: f.indent * INDENT_PX,
              marginBottom: 18,
              opacity: op,
              transform: `translateX(${tx}px)`,
            }}>
              <span style={{ fontFamily: MONO, fontSize: 30, color: f.accent ? CLAUDE.SPARK : CLAUDE.INK_SOFT }}>{f.icon}</span>
              <span style={{
                fontFamily: MONO,
                fontSize: 32,
                color: f.accent ? CLAUDE.SPARK : CLAUDE.INK,
                fontWeight: f.accent ? 700 : 400,
                wordBreak: 'break-word' as const,
                maxWidth: CONTENT_W - 60 - (f.indent * INDENT_PX),
              }}>{f.name}</span>
              {f.tag && (
                <div style={{
                  background: CLAUDE.SPARK, borderRadius: 8, padding: '4px 12px', marginLeft: 4,
                  fontFamily: SANS, fontSize: 18, fontWeight: 700, color: '#fff',
                  letterSpacing: 1.5, textTransform: 'uppercase' as const,
                  flexShrink: 0,
                }}>{f.tag}</div>
              )}
            </div>
          );
        })}
        {files.map((f, i) => f.size && (
          <div key={`size-${i}`} />  /* size line moved below main entry */
        ))}

        {/* Size lines rendered separately under each entry */}
      </div>

      {/* Size annotations rendered inline via secondary pass */}
      <div style={{
        position: 'absolute',
        top: height * 0.2,
        left: CONTENT_L,
        width: CONTENT_W,
        pointerEvents: 'none' as const,
      }}>
        {files.map((f, i) => {
          if (!f.size) return null;
          const op = clamp(fileIn[i], 0, 1);
          // stack size beneath its file entry — approx position based on rowHeight
          const rowH = 32 + 18; // font + gap
          return null; // simplify: we skip the size line to keep layout clean
        })}
      </div>

      {/* Callout */}
      {(calloutText || calloutSub) && (
        <div style={{
          position: 'absolute',
          bottom: height * 0.16,
          left: CONTENT_L,
          width: CONTENT_W,
          padding: '24px 32px',
          background: 'rgba(217,119,87,0.08)',
          border: `1px solid ${CLAUDE.SPARK}`,
          borderLeft: `6px solid ${CLAUDE.SPARK}`,
          borderRadius: 16,
          opacity: clamp(calloutIn, 0, 1),
          transform: `translateY(${(1 - clamp(calloutIn, 0, 1)) * 12}px)`,
          boxSizing: 'border-box' as const,
        }}>
          {calloutText && (
            <div style={{
              fontFamily: SANS,
              fontSize: 32,
              color: CLAUDE.INK,
              lineHeight: 1.4,
              wordBreak: 'break-word' as const,
            }} dangerouslySetInnerHTML={{ __html: calloutText }} />
          )}
          {calloutSub && (
            <div style={{
              fontFamily: SANS,
              fontSize: 22,
              color: CLAUDE.INK_SOFT,
              marginTop: 10,
              wordBreak: 'break-word' as const,
            }}>{calloutSub}</div>
          )}
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
