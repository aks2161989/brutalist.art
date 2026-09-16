import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * ClaudeVerdictArtifact — reusable verdict/artifact page in the Claude fidelity skin.
 * Renders an artifact window card (cream stage, white card, staggered lines).
 * Per ILLUSTRATE LAW this is a UI beat (verdict) — the Claude UI is the subject here.
 *
 * 2026-07 (your-turn skill): card enlarged from 860px to fill the frame at
 * legible size (was a ~45%-width UI mock marooned in dead space). Line numbers
 * are drawn by the component from list position; a defensive sanitizer strips
 * any leading "N." / "N)" an author typed into a line so the number never
 * renders twice. Feed artifactLines as BARE sentences.
 */

export const claudeVerdictArtifactSchema = z.object({
  artifactTitle: z.string().default('Verdict'),
  artifactHeading: z.string().default('The split'),
  artifactLines: z.array(z.string()).default([
    'Chat: synchronous judgment — you, in the loop.',
    'Cowork: asynchronous recipes — runs while you rehearse.',
    'Code: the pipeline room — systems you own.',
  ]),
});
export type ClaudeVerdictArtifactProps = z.infer<typeof claudeVerdictArtifactSchema>;

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;

const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));

// Strip a leading "1." / "2)" / "3 -" an author may have typed into the line —
// the component owns the numbering, so authored digits would double-render.
const stripLeadNum = (s: string) => s.replace(/^\s*\d+\s*[.)\-–—:]\s*/, '');


export const ClaudeVerdictArtifact: React.FC<ClaudeVerdictArtifactProps> = ({
  artifactTitle, artifactHeading, artifactLines,
}) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();

  const cardIn = spring({ frame, fps, config: { damping: 28, stiffness: 140, mass: 0.8 } });
  const headIn = spring({ frame: frame - 8, fps, config: { damping: 28, stiffness: 140, mass: 0.8 } });

  // Fill the frame: ~88% of width — the earlier 1560 cap left dead space at 4K
  // (card ended up ~40% of canvas). Cap now scales with the composition so
  // 1920 base yields ~1690, and 3840 yields ~3380; type is unchanged.
  const cardW = Math.min(width * 0.88, width - 200);
  const portrait = height > width;
  // In portrait the same content becomes vertically underfilled — pad the card
  // to at least 68% of canvas height so the safe area is populated, per FILL law.
  const cardMinH = portrait ? Math.round(height * 0.7) : 0;
  const lines = (artifactLines ?? []).map(stripLeadNum);

  return (
    <AbsoluteFill style={{ background: '#F2F0E9', alignItems: 'center', justifyContent: 'center' }}>
      {/* Artifact card */}
      <div style={{
        width: cardW,
        height: cardMinH || undefined,
        display: 'flex',
        flexDirection: 'column',
        background: CLAUDE.CARD,
        borderRadius: 24,
        boxShadow: '0 20px 72px rgba(61,57,41,0.16)',
        border: `1px solid ${CLAUDE.BORDER}`,
        overflow: 'hidden',
        transform: `scale(${clamp(cardIn, 0, 1)})`,
        opacity: clamp(cardIn, 0, 1),
      }}>
        {/* Title bar */}
        <div style={{
          background: CLAUDE.PAGE, borderBottom: `1px solid ${CLAUDE.BORDER}`,
          padding: '30px 56px', display: 'flex', alignItems: 'center', gap: 16,
        }}>
          <span style={{ fontFamily: SERIF, fontSize: 40, color: CLAUDE.INK, fontWeight: 600 }}>
            {artifactTitle}
          </span>
        </div>

        {/* Artifact body */}
        <div style={{ padding: '64px 80px 72px', flex: '1 1 auto' }}>
          {/* Heading */}
          <div style={{
            fontFamily: SERIF, fontSize: 62, fontWeight: 700, color: CLAUDE.INK,
            marginBottom: 48,
            opacity: clamp(headIn, 0, 1),
          }}>
            {artifactHeading}
          </div>

          {/* Lines */}
          {lines.map((line, i) => {
            const lineIn = spring({ frame: frame - (i + 2) * 7, fps, config: { damping: 28, stiffness: 140, mass: 0.8 } });
            const op = clamp(lineIn, 0, 1);
            const ty = (1 - op) * 12;
            return (
              <div key={i} style={{
                display: 'flex', alignItems: 'flex-start', gap: 28,
                marginBottom: 34, opacity: op, transform: `translateY(${ty}px)`,
              }}>
                <span style={{ fontFamily: SANS, fontSize: 38, color: CLAUDE.SPARK, flexShrink: 0, marginTop: 4, fontWeight: 700 }}>
                  {i + 1}.
                </span>
                <span style={{ fontFamily: SANS, fontSize: 38, color: CLAUDE.INK, lineHeight: 1.55 }}>
                  {line}
                </span>
              </div>
            );
          })}
        </div>
      </div>
    </AbsoluteFill>
  );
};
