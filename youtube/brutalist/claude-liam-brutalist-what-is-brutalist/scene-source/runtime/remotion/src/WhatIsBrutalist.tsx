/**
 * WhatIsBrutalist.tsx — reel-local Remotion components for
 * claude-liam-brutalist-what-is-brutalist.
 *
 * Palette: cream #FAF9F5 (CLAUDE.PAGE), warm ink #3D3929 (CLAUDE.INK),
 * terracotta #D97757 (CLAUDE.SPARK — the ONE accent). Serif EB Garamond
 * for greetings and headings, UI sans for chrome, mono for code snippets.
 *
 * Everything is a pure function of frame + useVideoConfig — the same
 * component renders 1920×1080 landscape and 1080×1920 portrait; layouts
 * reflow off the aspect. Registered in Root.tsx under a WhatIsBrutalist
 * folder as `Wib*` and `Wib*916`.
 *
 * The custom outro (WibOutro / WibOutro916) restates the film title with
 * the HARDCODED @HumanitariansAI handle — the shipped ClaudeTitleOutro
 * hardcodes @NikBearBrown per OUTRO-LOCK.md and cannot be reused on the
 * HAI channel. Native custom outro variants for this reel only.
 */
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate} from 'remotion';
import {z} from 'zod';
import {CLAUDE, CLAUDE_FONT} from './tokens/claude';

const SERIF = CLAUDE_FONT.serif;
const SANS  = CLAUDE_FONT.ui;
const MONO  = CLAUDE_FONT.mono;

const cl = (v: number, a = 0, b = 1) => Math.min(b, Math.max(a, v));
const win = (t: number, a: number, b: number) =>
  cl(interpolate(t, [a, b], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}));

const SparkLine: React.FC<{line: string; t: number; bottom?: boolean; portrait?: boolean}> =
  ({line, t, bottom, portrait}) => {
    if (!line) return null;
    const padX = 96; // uniform, > safe.x for both aspects
    // Portrait safe.y=96 top, safe.b=1824 (from 1920). Landscape safe.y=54, safe.b=1026.
    const inset = portrait ? 130 : 72;
    return (
      <div style={{
        position: 'absolute',
        left: padX,
        right: padX,
        [bottom ? 'bottom' : 'top']: inset,
        opacity: t,
        fontFamily: SERIF,
        fontStyle: 'italic',
        fontSize: portrait ? 32 : 26,
        color: CLAUDE.INK,
      }}>
        {line}
      </div>
    );
  };

// ──────────────────────────────────────────────────────────────────
// WibRecipe — B02: "film as code" split-panel.
// Left: a beat_sheet.json snippet types on. Right: the rendered composer
// beat card that the snippet produces. Arrow between them makes the claim
// visible: this JSON becomes that pixels.
// ──────────────────────────────────────────────────────────────────

export const wibRecipeSchema = z.object({
  sparkLine: z.string().default('The JSON is the film.'),
});
export type WibRecipeProps = z.infer<typeof wibRecipeSchema>;

const RECIPE_LINES: {ind: number; text: string; kind: 'key' | 'str' | 'lit' | 'p'}[] = [
  {ind: 0, text: '{',                                    kind: 'p'},
  {ind: 1, text: '"beat_id": "B00",',                    kind: 'key'},
  {ind: 1, text: '"narration_text":',                    kind: 'key'},
  {ind: 2, text: '"Ciao. This is Liam, in for Bear.",',  kind: 'str'},
  {ind: 1, text: '"shot": {',                            kind: 'key'},
  {ind: 2, text: '"pattern": "ClaudeComposerAsk",',      kind: 'key'},
  {ind: 2, text: '"props": {',                           kind: 'key'},
  {ind: 3, text: '"greeting": "Ciao, Liam",',            kind: 'key'},
  {ind: 3, text: '"segment": "What Is Brutalist?"',      kind: 'key'},
  {ind: 2, text: '}',                                    kind: 'p'},
  {ind: 1, text: '}',                                    kind: 'p'},
  {ind: 0, text: '}',                                    kind: 'p'},
];

export const WibRecipe: React.FC<WibRecipeProps> = ({sparkLine}) => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();
  const portrait = height > width;
  const t = frame / fps;

  const titleIn = spring({frame, fps, config: {damping: 26, stiffness: 120, mass: 0.9}});
  const arrowIn = win(t, 3.0, 3.6);
  const rightIn = win(t, 3.4, 4.4);

  const pad = 96; const padY = portrait ? 130 : 82;

  // Left card size
  const leftW  = portrait ? width - pad * 2 : (width - pad * 3) * 0.55;
  const leftH  = portrait ? height * 0.42 : height * 0.66;
  const rightW = portrait ? width - pad * 2 : (width - pad * 3) * 0.45;
  const rightH = portrait ? height * 0.36 : height * 0.66;

  const leftX  = pad;
  // Portrait: tighten leftY/leftH so leftY+leftH+gap+rightH stays inside safe.b (1824).
  const leftY  = portrait ? 210 : (height - leftH) / 2;
  const leftHFit = portrait ? 700 : leftH;
  const rightHFit = portrait ? 700 : rightH;
  const rightX = portrait ? pad : (leftX + leftW + pad);
  const rightY = portrait ? (leftY + leftHFit + 80) : (height - rightH) / 2;

  // Type-on: reveal one line every 0.28s
  const linesShown = Math.max(0, Math.min(RECIPE_LINES.length, Math.floor((t - 0.9) / 0.28)));

  // Line font
  const codeSize = portrait ? 24 : 26;
  const codeLead = codeSize * 1.55;

  return (
    <AbsoluteFill style={{background: CLAUDE.PAGE}}>
      {/* Eyebrow */}
      <div style={{
        position: 'absolute', left: pad, top: portrait ? 130 : 56,
        fontFamily: SANS, fontSize: portrait ? 20 : 16, fontWeight: 700,
        letterSpacing: 3, textTransform: 'uppercase' as const,
        color: CLAUDE.INK_SOFT, opacity: cl(titleIn),
      }}>
        BRUTALIST · FILM AS CODE
      </div>

      {/* Title */}
      <div style={{
        position: 'absolute', left: pad, top: portrait ? 175 : 82,
        right: pad,
        fontFamily: SERIF, fontSize: portrait ? 60 : 56, fontWeight: 700,
        color: CLAUDE.INK, letterSpacing: '-0.01em',
        opacity: cl(titleIn), transform: `translateY(${(1 - titleIn) * 10}px)`,
        lineHeight: 1.05,
      }}>
        The recipe <span style={{color: CLAUDE.SPARK}}>is</span> the film.
      </div>

      {/* LEFT — beat_sheet.json card */}
      <div style={{
        position: 'absolute', left: leftX, top: leftY,
        width: leftW, height: leftHFit,
        background: CLAUDE.CARD,
        border: `1px solid ${CLAUDE.BORDER}`,
        borderRadius: 12,
        boxShadow: '0 10px 40px rgba(61,57,41,0.08)',
        overflow: 'hidden',
        opacity: cl(titleIn),
      }}>
        {/* file tab */}
        <div style={{
          padding: '14px 22px', borderBottom: `1px solid ${CLAUDE.BORDER}`,
          display: 'flex', alignItems: 'center', gap: 12,
          background: CLAUDE.FOOTER,
        }}>
          <div style={{width: 10, height: 10, borderRadius: 5, background: CLAUDE.SPARK}} />
          <div style={{fontFamily: MONO, fontSize: 18, color: CLAUDE.INK, fontWeight: 600}}>
            beat_sheet.json
          </div>
        </div>
        {/* code */}
        <div style={{
          padding: '20px 26px',
          fontFamily: MONO, fontSize: codeSize, lineHeight: `${codeLead}px`,
          color: CLAUDE.INK,
        }}>
          {RECIPE_LINES.map((ln, i) => (
            <div key={i} style={{
              opacity: i < linesShown ? 1 : 0,
              transform: `translateY(${i < linesShown ? 0 : 4}px)`,
              transition: 'none',
              paddingLeft: ln.ind * 22,
              color: ln.kind === 'str' ? CLAUDE.SPARK
                   : ln.kind === 'key' ? CLAUDE.INK
                   : CLAUDE.INK_SOFT,
              whiteSpace: 'pre' as const,
            }}>
              {ln.text}
            </div>
          ))}
        </div>
      </div>

      {/* ARROW (rendered only for landscape; portrait uses stacked layout) */}
      {!portrait && (
        <div style={{
          position: 'absolute',
          left: leftX + leftW + 4,
          top: leftY + leftHFit / 2 - 20,
          width: pad - 8,
          display: 'flex',
          alignItems: 'center',
          gap: 6,
          opacity: arrowIn,
        }}>
          <div style={{flex: 1, height: 3, background: CLAUDE.SPARK, borderRadius: 2}} />
          <div style={{
            width: 0, height: 0,
            borderLeft: `18px solid ${CLAUDE.SPARK}`,
            borderTop: '10px solid transparent',
            borderBottom: '10px solid transparent',
          }} />
        </div>
      )}

      {/* Portrait: vertical arrow between the two panels */}
      {portrait && (
        <div style={{
          position: 'absolute',
          left: 0, right: 0,
          top: leftY + leftHFit + 8,
          display: 'flex',
          justifyContent: 'center',
          opacity: arrowIn,
        }}>
          <div style={{
            width: 0, height: 0,
            borderTop: `28px solid ${CLAUDE.SPARK}`,
            borderLeft: '18px solid transparent',
            borderRight: '18px solid transparent',
          }} />
        </div>
      )}

      {/* RIGHT — the rendered composer frame (schematic) */}
      <div style={{
        position: 'absolute', left: rightX, top: rightY,
        width: rightW, height: rightHFit,
        background: CLAUDE.CARD,
        border: `1px solid ${CLAUDE.BORDER}`,
        borderRadius: 14,
        boxShadow: '0 10px 40px rgba(61,57,41,0.08)',
        overflow: 'hidden',
        opacity: cl(rightIn),
        transform: `translateY(${(1 - rightIn) * 12}px)`,
      }}>
        <div style={{
          padding: `${portrait ? 26 : 34}px ${portrait ? 30 : 42}px`,
          height: '100%',
          display: 'flex', flexDirection: 'column', justifyContent: 'space-between',
        }}>
          <div>
            <div style={{
              fontFamily: SANS, fontSize: portrait ? 18 : 16,
              letterSpacing: 3, color: CLAUDE.INK_SOFT, fontWeight: 700,
              textTransform: 'uppercase' as const, marginBottom: 12,
            }}>
              HUMANITARIANS AI · BRUTALIST
            </div>
            <div style={{
              fontFamily: SERIF, fontSize: portrait ? 46 : 48,
              color: CLAUDE.INK, fontWeight: 700, marginBottom: 26,
              lineHeight: 1.12,
            }}>
              <span style={{color: CLAUDE.SPARK}}>*</span> Ciao, Liam<span style={{color: CLAUDE.SPARK}}>.</span>
            </div>
          </div>

          {/* composer card */}
          <div style={{
            border: `1px solid ${CLAUDE.BORDER}`,
            background: CLAUDE.PAGE,
            borderRadius: 10,
            padding: '18px 20px',
          }}>
            <div style={{
              fontFamily: SANS, fontSize: portrait ? 22 : 22, color: CLAUDE.INK, lineHeight: 1.4,
              minHeight: portrait ? 60 : 80,
            }}>
              Ciao. This is Liam, in for Bear.
            </div>
            <div style={{
              display: 'flex', justifyContent: 'space-between', marginTop: 14,
              alignItems: 'center',
            }}>
              <div style={{fontFamily: SANS, fontSize: 14, color: CLAUDE.GHOST}}>
                @HumanitariansAI · Claude
              </div>
              <div style={{
                width: 30, height: 30, borderRadius: 15,
                background: CLAUDE.SPARK, display: 'flex',
                alignItems: 'center', justifyContent: 'center',
                color: CLAUDE.CARD, fontFamily: SANS, fontSize: 18, fontWeight: 700,
              }}>↑</div>
            </div>
          </div>
        </div>
      </div>

      <SparkLine line={sparkLine} t={cl(titleIn)} bottom portrait={portrait} />
    </AbsoluteFill>
  );
};

// ──────────────────────────────────────────────────────────────────
// WibPipeline — B03: the six-stage Brutalist pipeline.
// INPUT (your brief) → BEAT SHEET → AUDIO → SCENES → COMPILE →
// OUTPUT (4K master + 9:16 companion).
// Deliberately not called "publish" — Brutalist never uploads.
// ──────────────────────────────────────────────────────────────────

export const wibPipelineSchema = z.object({
  sparkLine: z.string().default('One pass through the machine.'),
});
export type WibPipelineProps = z.infer<typeof wibPipelineSchema>;

const PIPELINE_STAGES = [
  {label: 'BRIEF',      sub: 'you write it'},
  {label: 'BEAT SHEET', sub: 'claude drafts it'},
  {label: 'AUDIO',      sub: 'kokoro (local)'},
  {label: 'SCENES',     sub: 'remotion / manim'},
  {label: 'COMPILE',    sub: 'conform + mux'},
  {label: '4K MASTER',  sub: '+ portrait companion'},
];

export const WibPipeline: React.FC<WibPipelineProps> = ({sparkLine}) => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();
  const portrait = height > width;
  const t = frame / fps;

  const titleIn = spring({frame, fps, config: {damping: 26, stiffness: 120, mass: 0.9}});
  const pad = 96; const padY = portrait ? 130 : 82;

  return (
    <AbsoluteFill style={{background: CLAUDE.PAGE}}>
      <div style={{
        position: 'absolute', left: pad, top: portrait ? 130 : 56,
        fontFamily: SANS, fontSize: portrait ? 20 : 16, fontWeight: 700,
        letterSpacing: 3, textTransform: 'uppercase' as const,
        color: CLAUDE.INK_SOFT, opacity: cl(titleIn),
      }}>
        BRUTALIST · PIPELINE
      </div>
      <div style={{
        position: 'absolute', left: pad, right: pad,
        top: portrait ? 175 : 82,
        fontFamily: SERIF, fontSize: portrait ? 60 : 56, fontWeight: 700,
        color: CLAUDE.INK, letterSpacing: '-0.01em',
        opacity: cl(titleIn), transform: `translateY(${(1 - titleIn) * 10}px)`,
        lineHeight: 1.05,
      }}>
        Brief in. <span style={{color: CLAUDE.SPARK}}>Four K</span> out.
      </div>

      {portrait ? (
        // Vertical stack — one node per row, connector between.
        <div style={{
          position: 'absolute', left: pad, right: pad,
          top: height * 0.22,
          display: 'flex', flexDirection: 'column',
          gap: 12,
        }}>
          {PIPELINE_STAGES.map((s, i) => {
            const nodeIn = win(t, 0.6 + i * 0.14, 1.0 + i * 0.14);
            const isFinal = i === PIPELINE_STAGES.length - 1;
            return (
              <React.Fragment key={i}>
                <div style={{
                  padding: '18px 22px',
                  border: `1px solid ${isFinal ? CLAUDE.SPARK : CLAUDE.BORDER}`,
                  borderLeft: `5px solid ${isFinal ? CLAUDE.SPARK : CLAUDE.INK}`,
                  borderRadius: 10,
                  background: isFinal ? 'rgba(217,119,87,0.06)' : CLAUDE.CARD,
                  opacity: nodeIn,
                  transform: `translateY(${(1 - nodeIn) * 10}px)`,
                  display: 'flex', flexDirection: 'column',
                }}>
                  <div style={{
                    fontFamily: SANS, fontSize: 15, letterSpacing: 2,
                    fontWeight: 700, textTransform: 'uppercase' as const,
                    color: isFinal ? CLAUDE.SPARK : CLAUDE.INK_SOFT,
                  }}>
                    {String(i + 1).padStart(2, '0')} · {s.label}
                  </div>
                  <div style={{
                    fontFamily: SERIF, fontSize: 26, color: CLAUDE.INK,
                    marginTop: 4,
                  }}>
                    {s.sub}
                  </div>
                </div>
                {i < PIPELINE_STAGES.length - 1 && (
                  <div style={{
                    height: 20, display: 'flex', justifyContent: 'center',
                    alignItems: 'center', opacity: cl(nodeIn),
                  }}>
                    <div style={{
                      width: 0, height: 0,
                      borderTop: `14px solid ${CLAUDE.SPARK}`,
                      borderLeft: '10px solid transparent',
                      borderRight: '10px solid transparent',
                    }} />
                  </div>
                )}
              </React.Fragment>
            );
          })}
        </div>
      ) : (
        // Landscape — horizontal rail.
        <div style={{
          position: 'absolute',
          left: pad, right: pad,
          top: height * 0.42,
          display: 'flex', alignItems: 'stretch', justifyContent: 'space-between',
          gap: 0,
        }}>
          {PIPELINE_STAGES.map((s, i) => {
            const nodeIn = win(t, 0.5 + i * 0.15, 1.0 + i * 0.15);
            const isFinal = i === PIPELINE_STAGES.length - 1;
            const boxW = (width - pad * 2 - 6 * (PIPELINE_STAGES.length - 1)) / PIPELINE_STAGES.length;
            return (
              <React.Fragment key={i}>
                <div style={{
                  width: boxW,
                  minHeight: 220,
                  padding: '22px 18px',
                  border: `1px solid ${isFinal ? CLAUDE.SPARK : CLAUDE.BORDER}`,
                  borderTop: `5px solid ${isFinal ? CLAUDE.SPARK : CLAUDE.INK}`,
                  borderRadius: 12,
                  background: isFinal ? 'rgba(217,119,87,0.06)' : CLAUDE.CARD,
                  opacity: nodeIn,
                  transform: `translateY(${(1 - nodeIn) * 12}px)`,
                  boxShadow: '0 6px 24px rgba(61,57,41,0.06)',
                  display: 'flex', flexDirection: 'column',
                  justifyContent: 'space-between',
                }}>
                  <div>
                    <div style={{
                      fontFamily: SANS, fontSize: 13, letterSpacing: 2,
                      fontWeight: 700, textTransform: 'uppercase' as const,
                      color: isFinal ? CLAUDE.SPARK : CLAUDE.INK_SOFT,
                    }}>
                      {String(i + 1).padStart(2, '0')}
                    </div>
                    <div style={{
                      fontFamily: SERIF, fontSize: 28, color: CLAUDE.INK,
                      marginTop: 6, fontWeight: 700, lineHeight: 1.1,
                    }}>
                      {s.label}
                    </div>
                  </div>
                  <div style={{
                    fontFamily: SANS, fontSize: 18, color: CLAUDE.INK_SOFT,
                    marginTop: 18, lineHeight: 1.4,
                  }}>
                    {s.sub}
                  </div>
                </div>
              </React.Fragment>
            );
          })}
        </div>
      )}

      <SparkLine line={sparkLine} t={cl(titleIn)} bottom portrait={portrait} />
    </AbsoluteFill>
  );
};

// ──────────────────────────────────────────────────────────────────
// WibChange — B04: one property change → one visible change.
// Left panel: the beat_sheet.json line before ("greeting": "Ciao, Liam")
// with the changed word terracotta; right panel: the rendered composer
// greeting shifts from "Ciao, Liam" to "Hola, Liam". Motion enacts the
// argument.
// ──────────────────────────────────────────────────────────────────

export const wibChangeSchema = z.object({
  sparkLine: z.string().default('Change the recipe. Get a new film.'),
});
export type WibChangeProps = z.infer<typeof wibChangeSchema>;

export const WibChange: React.FC<WibChangeProps> = ({sparkLine}) => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();
  const portrait = height > width;
  const t = frame / fps;

  const titleIn = spring({frame, fps, config: {damping: 26, stiffness: 120, mass: 0.9}});
  const editIn   = win(t, 1.6, 2.1);   // strike the old word
  const rerender = win(t, 3.0, 3.5);   // re-render pulse
  const shown    = win(t, 3.5, 4.0);   // new greeting appears

  const pad = 96; const padY = portrait ? 130 : 82;

  const oldWord = 'Ciao';
  const newWord = 'Hola';

  const codeSize = portrait ? 30 : 30;

  // Left card (code line)
  const leftW  = portrait ? width - pad * 2 : (width - pad * 3) * 0.5;
  const leftH  = portrait ? height * 0.30 : height * 0.4;
  const rightW = portrait ? width - pad * 2 : (width - pad * 3) * 0.5;
  const rightH = portrait ? height * 0.30 : height * 0.4;

  const leftX = pad;
  const leftY = portrait ? height * 0.20 : (height - leftH) / 2;

  const rightX = portrait ? pad : leftX + leftW + pad;
  const rightY = portrait ? leftY + leftH + height * 0.06 : (height - rightH) / 2;

  const greeting = shown > 0.5 ? newWord : oldWord;

  return (
    <AbsoluteFill style={{background: CLAUDE.PAGE}}>
      <div style={{
        position: 'absolute', left: pad, top: portrait ? 130 : 56,
        fontFamily: SANS, fontSize: portrait ? 20 : 16, fontWeight: 700,
        letterSpacing: 3, textTransform: 'uppercase' as const,
        color: CLAUDE.INK_SOFT, opacity: cl(titleIn),
      }}>
        BRUTALIST · PURE FUNCTION
      </div>
      <div style={{
        position: 'absolute', left: pad, right: pad, top: portrait ? 175 : 82,
        fontFamily: SERIF, fontSize: portrait ? 60 : 56, fontWeight: 700,
        color: CLAUDE.INK, opacity: cl(titleIn),
        transform: `translateY(${(1 - titleIn) * 10}px)`,
        lineHeight: 1.05,
      }}>
        One field. <span style={{color: CLAUDE.SPARK}}>One change.</span>
      </div>

      {/* LEFT — edited beat sheet line */}
      <div style={{
        position: 'absolute', left: leftX, top: leftY,
        width: leftW, height: leftH,
        background: CLAUDE.CARD,
        border: `1px solid ${CLAUDE.BORDER}`,
        borderRadius: 12,
        boxShadow: '0 10px 40px rgba(61,57,41,0.08)',
        overflow: 'hidden',
        opacity: cl(titleIn),
      }}>
        <div style={{
          padding: '14px 22px', borderBottom: `1px solid ${CLAUDE.BORDER}`,
          display: 'flex', alignItems: 'center', gap: 12,
          background: CLAUDE.FOOTER,
        }}>
          <div style={{width: 10, height: 10, borderRadius: 5, background: CLAUDE.SPARK}} />
          <div style={{fontFamily: MONO, fontSize: 18, color: CLAUDE.INK, fontWeight: 600}}>
            beat_sheet.json · B00
          </div>
          <div style={{marginLeft: 'auto',
            fontFamily: SANS, fontSize: 13, letterSpacing: 2,
            color: editIn > 0.5 ? CLAUDE.SPARK : CLAUDE.INK_SOFT,
            fontWeight: 700, textTransform: 'uppercase' as const,
          }}>
            {editIn > 0.5 ? 'EDITED' : 'BEFORE'}
          </div>
        </div>
        <div style={{
          padding: '30px 26px',
          fontFamily: MONO, fontSize: codeSize, lineHeight: 1.6,
          color: CLAUDE.INK,
        }}>
          <div style={{whiteSpace: 'pre' as const}}>
            <span style={{color: CLAUDE.INK}}>{'"greeting": "'}</span>
            <span style={{
              color: editIn > 0.5 ? CLAUDE.INK_SOFT : CLAUDE.INK,
              textDecoration: editIn > 0.5 && shown < 0.5 ? 'line-through' : 'none',
              display: editIn > 0.5 && shown > 0.5 ? 'none' : 'inline',
            }}>{oldWord}</span>
            {shown > 0.5 && (
              <span style={{color: CLAUDE.SPARK, fontWeight: 700}}>{newWord}</span>
            )}
            <span style={{color: CLAUDE.INK}}>{', Liam"'}</span>
          </div>
          <div style={{
            marginTop: 24,
            fontFamily: SANS, fontSize: 20, color: CLAUDE.INK_SOFT,
            opacity: editIn,
          }}>
            $ python3 remotion_scenes.py --only B00
          </div>
          <div style={{
            marginTop: 6,
            fontFamily: SANS, fontSize: 18, color: CLAUDE.INK_SOFT,
            opacity: rerender,
          }}>
            → re-rendering B00.mp4…
          </div>
        </div>
      </div>

      {/* RIGHT — rendered composer greeting */}
      <div style={{
        position: 'absolute', left: rightX, top: rightY,
        width: rightW, height: rightH,
        background: CLAUDE.CARD,
        border: `2px solid ${shown > 0.5 ? CLAUDE.SPARK : CLAUDE.BORDER}`,
        borderRadius: 14,
        boxShadow: '0 10px 40px rgba(61,57,41,0.08)',
        overflow: 'hidden',
        opacity: cl(titleIn),
        transform: `scale(${1 + rerender * 0.02 - shown * 0.02})`,
      }}>
        <div style={{
          padding: `${portrait ? 36 : 44}px ${portrait ? 30 : 42}px`,
          height: '100%',
          display: 'flex', flexDirection: 'column', justifyContent: 'center',
          alignItems: 'flex-start',
        }}>
          <div style={{
            fontFamily: SANS, fontSize: portrait ? 16 : 14,
            letterSpacing: 3, color: CLAUDE.INK_SOFT, fontWeight: 700,
            textTransform: 'uppercase' as const, marginBottom: 12,
          }}>
            B00 · RENDERED
          </div>
          <div style={{
            fontFamily: SERIF, fontSize: portrait ? 78 : 88, fontWeight: 700,
            color: CLAUDE.INK, lineHeight: 1.05,
          }}>
            <span style={{color: CLAUDE.SPARK}}>*</span>{' '}{greeting}<span style={{color: CLAUDE.SPARK}}>,</span> Liam<span style={{color: CLAUDE.SPARK}}>.</span>
          </div>
          <div style={{
            marginTop: 24,
            fontFamily: SANS, fontSize: portrait ? 20 : 18,
            color: CLAUDE.INK_SOFT,
          }}>
            {shown > 0.5 ? 'Spanish "hello."' : 'Italian "hello."'}
          </div>
        </div>
      </div>

      <SparkLine line={sparkLine} t={cl(titleIn)} bottom portrait={portrait} />
    </AbsoluteFill>
  );
};

// ──────────────────────────────────────────────────────────────────
// WibDivision — B05: human judgment vs agent execution.
// Two lanes; HUMAN column terracotta because judgment is the sole
// spot that will not be automated.
// ──────────────────────────────────────────────────────────────────

export const wibDivisionSchema = z.object({
  sparkLine: z.string().default('Taste is not a step Claude does slowly.'),
});
export type WibDivisionProps = z.infer<typeof wibDivisionSchema>;

const HUMAN_ROWS = [
  'Write the brief',
  'Watch the cut',
  'Ask for a fix',
  'Approve for publish',
];
const AGENT_ROWS = [
  'Draft the beat sheet',
  'Generate the narration',
  'Render every scene',
  'Compile the 4K master',
  'Verify the file',
];

export const WibDivision: React.FC<WibDivisionProps> = ({sparkLine}) => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();
  const portrait = height > width;
  const t = frame / fps;

  const titleIn = spring({frame, fps, config: {damping: 26, stiffness: 120, mass: 0.9}});
  const pad = 96; const padY = portrait ? 130 : 82;

  const laneW = portrait ? width - pad * 2 : (width - pad * 3) / 2;
  const laneHeadH = portrait ? 100 : 110;

  const humanX = pad;
  const humanY = portrait ? height * 0.20 : height * 0.28;
  const agentX = portrait ? pad : humanX + laneW + pad;
  const agentY = portrait
    ? humanY + laneHeadH + HUMAN_ROWS.length * 66 + 40
    : humanY;

  const rowBaseDelay = 0.6;
  const rowStep = 0.16;

  const Lane: React.FC<{
    title: string;
    subtitle: string;
    rows: string[];
    x: number; y: number; w: number;
    delayOffset: number;
    accent: boolean;
  }> = ({title, subtitle, rows, x, y, w, delayOffset, accent}) => (
    <>
      <div style={{
        position: 'absolute', left: x, top: y,
        width: w, height: laneHeadH,
        padding: '18px 22px',
        borderTop: `5px solid ${accent ? CLAUDE.SPARK : CLAUDE.INK}`,
        background: accent ? 'rgba(217,119,87,0.06)' : CLAUDE.CARD,
        border: `1px solid ${accent ? CLAUDE.SPARK : CLAUDE.BORDER}`,
        borderRadius: 12,
        opacity: cl(titleIn),
      }}>
        <div style={{
          fontFamily: SANS, fontSize: portrait ? 15 : 14, letterSpacing: 3,
          fontWeight: 700, textTransform: 'uppercase' as const,
          color: accent ? CLAUDE.SPARK : CLAUDE.INK_SOFT,
        }}>
          {subtitle}
        </div>
        <div style={{
          fontFamily: SERIF, fontSize: portrait ? 44 : 42, fontWeight: 700,
          color: CLAUDE.INK, marginTop: 4,
        }}>
          {title}
        </div>
      </div>
      {rows.map((r, i) => {
        const rowIn = win(t, delayOffset + i * rowStep, delayOffset + 0.5 + i * rowStep);
        return (
          <div key={i} style={{
            position: 'absolute',
            left: x, top: y + laneHeadH + 8 + i * 60,
            width: w, minHeight: 52, padding: '10px 20px',
            background: CLAUDE.CARD, border: `1px solid ${CLAUDE.BORDER}`,
            borderLeft: `4px solid ${accent ? CLAUDE.SPARK : CLAUDE.INK_SOFT}`,
            borderRadius: 8,
            opacity: rowIn, transform: `translateX(${(1 - rowIn) * 12}px)`,
            display: 'flex', alignItems: 'center',
          }}>
            <div style={{
              fontFamily: SANS, fontSize: portrait ? 24 : 24,
              color: CLAUDE.INK,
            }}>
              {r}
            </div>
          </div>
        );
      })}
    </>
  );

  return (
    <AbsoluteFill style={{background: CLAUDE.PAGE}}>
      <div style={{
        position: 'absolute', left: pad, top: portrait ? 130 : 56,
        fontFamily: SANS, fontSize: portrait ? 20 : 16, fontWeight: 700,
        letterSpacing: 3, textTransform: 'uppercase' as const,
        color: CLAUDE.INK_SOFT, opacity: cl(titleIn),
      }}>
        BRUTALIST · DIVISION OF LABOR
      </div>
      <div style={{
        position: 'absolute', left: pad, right: pad, top: portrait ? 175 : 82,
        fontFamily: SERIF, fontSize: portrait ? 60 : 56, fontWeight: 700,
        color: CLAUDE.INK, opacity: cl(titleIn),
        transform: `translateY(${(1 - titleIn) * 10}px)`,
        lineHeight: 1.05,
      }}>
        Your lane. <span style={{color: CLAUDE.SPARK}}>Claude's lane.</span>
      </div>

      <Lane title="You" subtitle="HUMAN · JUDGMENT"
        rows={HUMAN_ROWS}
        x={humanX} y={humanY} w={laneW}
        delayOffset={rowBaseDelay}
        accent={true}
      />
      <Lane title="Claude" subtitle="AGENT · EXECUTION"
        rows={AGENT_ROWS}
        x={agentX} y={agentY} w={laneW}
        delayOffset={rowBaseDelay + 0.3}
        accent={false}
      />

      <SparkLine line={sparkLine} t={cl(titleIn)} bottom portrait={portrait} />
    </AbsoluteFill>
  );
};

// ──────────────────────────────────────────────────────────────────
// WibNotClaims — B06: what Brutalist ISN'T.
// Three-row limitation list. Each row a claim about what the tool
// deliberately does NOT do.
// ──────────────────────────────────────────────────────────────────

export const wibNotClaimsSchema = z.object({
  sparkLine: z.string().default('The honest boundary.'),
});
export type WibNotClaimsProps = z.infer<typeof wibNotClaimsSchema>;

const NOT_ITEMS = [
  {label: 'Not a publisher.',        body: 'It renders a 4K file. You upload it.'},
  {label: 'Not a paid API.',         body: 'Kokoro runs locally. Claude runs on your subscription.'},
  {label: 'Not a judge of taste.',   body: 'It will render any bad idea. Watching the cut is your job.'},
];

export const WibNotClaims: React.FC<WibNotClaimsProps> = ({sparkLine}) => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();
  const portrait = height > width;
  const t = frame / fps;

  const titleIn = spring({frame, fps, config: {damping: 26, stiffness: 120, mass: 0.9}});
  const pad = 96; const padY = portrait ? 130 : 82;

  const rowStep = 0.6;
  const rowY0 = portrait ? height * 0.24 : height * 0.32;
  const rowH  = portrait ? 200 : 150;

  return (
    <AbsoluteFill style={{background: CLAUDE.PAGE}}>
      <div style={{
        position: 'absolute', left: pad, top: portrait ? 130 : 56,
        fontFamily: SANS, fontSize: portrait ? 20 : 16, fontWeight: 700,
        letterSpacing: 3, textTransform: 'uppercase' as const,
        color: CLAUDE.INK_SOFT, opacity: cl(titleIn),
      }}>
        BRUTALIST · THE HONEST NOT-LIST
      </div>
      <div style={{
        position: 'absolute', left: pad, right: pad, top: portrait ? 175 : 82,
        fontFamily: SERIF, fontSize: portrait ? 60 : 56, fontWeight: 700,
        color: CLAUDE.INK, opacity: cl(titleIn),
        transform: `translateY(${(1 - titleIn) * 10}px)`,
        lineHeight: 1.05,
      }}>
        What Brutalist <span style={{color: CLAUDE.SPARK}}>isn't.</span>
      </div>

      {NOT_ITEMS.map((it, i) => {
        const rowIn = win(t, 0.6 + i * rowStep, 1.2 + i * rowStep);
        return (
          <div key={i} style={{
            position: 'absolute', left: pad, right: pad,
            top: rowY0 + i * (rowH + 20),
            padding: '20px 26px',
            background: CLAUDE.CARD, border: `1px solid ${CLAUDE.BORDER}`,
            borderLeft: `6px solid ${CLAUDE.SPARK}`,
            borderRadius: 12,
            opacity: rowIn, transform: `translateY(${(1 - rowIn) * 14}px)`,
            display: 'flex', flexDirection: portrait ? 'column' : 'row',
            alignItems: portrait ? 'flex-start' : 'baseline', gap: portrait ? 8 : 22,
          }}>
            <div style={{
              fontFamily: SERIF, fontSize: portrait ? 44 : 44, fontWeight: 700,
              color: CLAUDE.SPARK, minWidth: portrait ? 'auto' : 340,
              lineHeight: 1.1,
            }}>
              {it.label}
            </div>
            <div style={{
              fontFamily: SANS, fontSize: portrait ? 26 : 26,
              color: CLAUDE.INK, lineHeight: 1.4,
            }}>
              {it.body}
            </div>
          </div>
        );
      })}

      <SparkLine line={sparkLine} t={cl(titleIn)} bottom portrait={portrait} />
    </AbsoluteFill>
  );
};

// ──────────────────────────────────────────────────────────────────
// WibVerdict — B07 verdict artifact card sized for FILL-THE-CANVAS.
// Same information architecture as ClaudeVerdictArtifact (title bar,
// heading, three numbered lines) but the card fills the whole safe area
// so gate V doesn't flag it as underfill.
// ──────────────────────────────────────────────────────────────────

export const wibVerdictSchema = z.object({
  artifactTitle: z.string().default('Verdict'),
  artifactHeading: z.string().default('Film as code, in three lines.'),
  artifactLines: z.array(z.string()).default([
    'The recipe is text.',
    'The film is a pure function of the recipe.',
    'Judgment stays yours. Everything else can be automated.',
  ]),
  sparkLine: z.string().default('That is what Brutalist actually is.'),
});
export type WibVerdictProps = z.infer<typeof wibVerdictSchema>;

const stripLeadNum = (s: string) => s.replace(/^\s*\d+\s*[.)\-–—:]\s*/, '');

export const WibVerdict: React.FC<WibVerdictProps> = ({
  artifactTitle, artifactHeading, artifactLines, sparkLine,
}) => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();
  const portrait = height > width;
  const pad = 96; const padY = portrait ? 130 : 82;

  const cardIn = spring({frame, fps, config: {damping: 28, stiffness: 140, mass: 0.8}});
  const headIn = spring({frame: frame - 8, fps, config: {damping: 28, stiffness: 140, mass: 0.8}});

  const cardX = pad;
  const cardY = padY;
  const cardW = width - pad * 2;
  const cardH = height - padY * 2;

  const lines = (artifactLines ?? []).map(stripLeadNum);

  return (
    <AbsoluteFill style={{background: CLAUDE.PAGE}}>
      <div style={{
        position: 'absolute',
        left: cardX, top: cardY,
        width: cardW, height: cardH,
        background: CLAUDE.CARD,
        border: `1px solid ${CLAUDE.BORDER}`,
        borderRadius: 24,
        boxShadow: '0 20px 72px rgba(61,57,41,0.16)',
        overflow: 'hidden',
        transform: `scale(${cl(cardIn) * 0.02 + 0.98})`,
        opacity: cl(cardIn),
      }}>
        {/* Title bar */}
        <div style={{
          background: CLAUDE.PAGE,
          borderBottom: `1px solid ${CLAUDE.BORDER}`,
          padding: portrait ? '28px 44px' : '32px 56px',
          display: 'flex', alignItems: 'center', gap: 20,
        }}>
          <div style={{
            width: 14, height: 14, borderRadius: 7,
            background: CLAUDE.SPARK,
          }} />
          <span style={{
            fontFamily: SERIF, fontSize: portrait ? 42 : 46,
            color: CLAUDE.INK, fontWeight: 600,
          }}>
            {artifactTitle}
          </span>
          <span style={{
            marginLeft: 'auto',
            fontFamily: SANS, fontSize: portrait ? 22 : 22,
            fontWeight: 700, letterSpacing: 3,
            textTransform: 'uppercase' as const,
            color: CLAUDE.INK_SOFT,
          }}>
            BRUTALIST · WHAT IS
          </span>
        </div>

        {/* Body */}
        <div style={{
          padding: portrait ? '48px 44px' : '72px 84px',
          display: 'flex', flexDirection: 'column',
          height: `calc(100% - ${portrait ? 100 : 116}px)`,
        }}>
          {/* Heading */}
          <div style={{
            fontFamily: SERIF, fontWeight: 700,
            fontSize: portrait ? 72 : 88,
            color: CLAUDE.INK,
            marginBottom: portrait ? 56 : 72,
            opacity: cl(headIn),
            letterSpacing: '-0.01em',
            lineHeight: 1.05,
          }}>
            {artifactHeading.replace(/([.?!…]+)\s*$/, '')}
            <span style={{color: CLAUDE.SPARK}}>
              {(artifactHeading.match(/([.?!…]+)\s*$/) || ['.', '.'])[1]}
            </span>
          </div>

          {/* Numbered lines */}
          <div style={{
            display: 'flex', flexDirection: 'column',
            gap: portrait ? 44 : 52, flex: 1,
          }}>
            {lines.map((line, i) => {
              const lineIn = spring({frame: frame - (i + 2) * 8, fps, config: {damping: 28, stiffness: 140, mass: 0.8}});
              const op = cl(lineIn);
              return (
                <div key={i} style={{
                  display: 'flex', alignItems: 'flex-start', gap: portrait ? 30 : 40,
                  opacity: op, transform: `translateY(${(1 - op) * 14}px)`,
                }}>
                  <span style={{
                    fontFamily: SANS, fontSize: portrait ? 60 : 68,
                    color: CLAUDE.SPARK, fontWeight: 700,
                    flexShrink: 0, marginTop: portrait ? 4 : 6,
                    lineHeight: 1,
                  }}>
                    {i + 1}.
                  </span>
                  <span style={{
                    fontFamily: SANS, fontSize: portrait ? 44 : 48,
                    color: CLAUDE.INK, lineHeight: 1.35,
                  }}>
                    {line}
                  </span>
                </div>
              );
            })}
          </div>

          {/* Spark line */}
          {sparkLine ? (
            <div style={{
              marginTop: portrait ? 40 : 32,
              fontFamily: SERIF, fontStyle: 'italic',
              fontSize: portrait ? 36 : 40,
              color: CLAUDE.INK_SOFT,
              opacity: cl(spring({frame: frame - 60, fps, config: {damping: 28, stiffness: 100}})),
            }}>
              {sparkLine}
            </div>
          ) : null}
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ──────────────────────────────────────────────────────────────────
// WibOutro — the title-restate outro card for THIS reel.
// Hardcodes @HumanitariansAI (the shipped ClaudeTitleOutro hardcodes
// @NikBearBrown per OUTRO-LOCK.md; this is the required native custom
// variant for the HAI channel — never modifies the live library).
// ──────────────────────────────────────────────────────────────────

export const wibOutroSchema = z.object({
  title: z.string().default('What Is Brutalist?'),
  subline: z.string().default('Liam, in for Bear.'),
});
export type WibOutroProps = z.infer<typeof wibOutroSchema>;

const HAI_HANDLE = '@HumanitariansAI';

export const WibOutro: React.FC<WibOutroProps> = ({title, subline}) => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();
  const portrait = height > width;

  const fadeIn = interpolate(frame, [0, 18], [0, 1], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });
  const handleIn = spring({frame: frame - 20, fps, config: {damping: 24, stiffness: 100}});
  const sublineIn = spring({frame: frame - 40, fps, config: {damping: 24, stiffness: 100}});

  // Terminal punctuation in terracotta
  const pm = title.match(/^([\s\S]*?)\s*([.?!…]+)\s*$/);
  const titleBody  = pm ? pm[1] : title;
  const titlePunct = pm ? pm[2] : '.';

  const pad = 96; const padY = portrait ? 130 : 82;
  const eyebrowIn = spring({frame: frame - 6, fps, config: {damping: 24, stiffness: 100}});

  return (
    <AbsoluteFill style={{
      background: CLAUDE.PAGE,
      opacity: fadeIn,
    }}>
      {/* Eyebrow — small tracked-caps line near the top of safe */}
      <div style={{
        position: 'absolute',
        top: portrait ? 130 : 110,
        left: pad, right: pad,
        textAlign: 'center',
        fontFamily: SANS,
        fontSize: portrait ? 32 : 30,
        fontWeight: 700,
        letterSpacing: 8,
        textTransform: 'uppercase' as const,
        color: CLAUDE.INK_SOFT,
        opacity: cl(eyebrowIn),
      }}>
        BRUTALIST · EPISODE 01
      </div>

      {/* Terracotta rule under eyebrow */}
      <div style={{
        position: 'absolute',
        top: portrait ? 190 : 165,
        left: '50%',
        transform: `translateX(-50%) scaleX(${cl(eyebrowIn)})`,
        transformOrigin: 'center',
        width: portrait ? 220 : 260,
        height: 4,
        background: CLAUDE.SPARK,
        opacity: cl(eyebrowIn),
      }} />

      {/* Title — poster serif, terracotta punctuation, upper-centered */}
      <div style={{
        position: 'absolute',
        top: portrait ? 300 : 240,
        left: pad, right: pad,
        textAlign: 'center',
        fontFamily: SERIF,
        fontWeight: 700,
        fontSize: portrait ? 180 : 200,
        color: CLAUDE.INK,
        letterSpacing: '-0.02em',
        lineHeight: 1.02,
      }}>
        {titleBody}
        <span style={{color: CLAUDE.SPARK}}>{titlePunct}</span>
      </div>

      {/* Handle — HARDCODED to @HumanitariansAI, mid-lower */}
      <div style={{
        position: 'absolute',
        top: portrait ? 1150 : 720,
        left: pad, right: pad,
        textAlign: 'center',
        fontFamily: SERIF,
        fontSize: portrait ? 100 : 108,
        color: CLAUDE.INK,
        opacity: cl(handleIn) * 0.92,
        transform: `translateY(${(1 - cl(handleIn)) * 10}px)`,
      }}>
        {HAI_HANDLE}
      </div>

      {/* Subline — near bottom of safe area */}
      <div style={{
        position: 'absolute',
        bottom: portrait ? 140 : 110,
        left: pad, right: pad,
        textAlign: 'center',
        fontFamily: SANS,
        fontSize: portrait ? 48 : 52,
        color: CLAUDE.INK_SOFT,
        opacity: cl(sublineIn),
        transform: `translateY(${(1 - cl(sublineIn)) * 8}px)`,
        letterSpacing: 4,
        textTransform: 'uppercase' as const,
        fontWeight: 700,
      }}>
        {subline}
      </div>
    </AbsoluteFill>
  );
};
