/**
 * DownloadBrutalist.tsx — reel-local Remotion components for
 * claude-liam-brutalist-download-and-set-up (episode 02 in the Brutalist
 * playlist for @HumanitariansAI).
 *
 * Palette: cream #FAF9F5 (CLAUDE.PAGE), warm ink #3D3929 (CLAUDE.INK),
 * terracotta #D97757 (CLAUDE.SPARK — the ONE accent). Serif EB Garamond
 * for greetings and headings, UI sans for chrome, mono for shell and
 * folder names.
 *
 * Everything is a pure function of frame + useVideoConfig — the same
 * component renders 1920×1080 landscape and 1080×1920 portrait; layouts
 * reflow off the aspect. Registered in Root.tsx under a DownloadBrutalist
 * folder as `Dbc*` and `Dbc*916`.
 *
 * DbcOutro hardcodes @HumanitariansAI — the shipped ClaudeTitleOutro
 * hardcodes @NikBearBrown per OUTRO-LOCK.md and cannot be reused on the
 * HAI channel. Native custom outro variant for this reel only.
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
    const padX = 96;
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
        fontSize: portrait ? 32 : 28,
        color: CLAUDE.INK,
        textAlign: 'center',
      }}>
        {line}
      </div>
    );
  };

const Eyebrow: React.FC<{text: string; opacity: number; portrait: boolean}> =
  ({text, opacity, portrait}) => (
    <div style={{
      position: 'absolute',
      left: 96, top: portrait ? 130 : 56, right: 96,
      fontFamily: SANS,
      fontSize: portrait ? 22 : 18,
      fontWeight: 700,
      letterSpacing: 3,
      textTransform: 'uppercase' as const,
      color: CLAUDE.INK_SOFT,
      opacity,
    }}>
      {text}
    </div>
  );

const Title: React.FC<{
  first: string;
  spark: string;
  rest?: string;
  opacity: number;
  portrait: boolean;
  translateY: number;
}> = ({first, spark, rest, opacity, portrait, translateY}) => (
  <div style={{
    position: 'absolute',
    left: 96, right: 96,
    top: portrait ? 180 : 88,
    fontFamily: SERIF,
    fontSize: portrait ? 66 : 58,
    fontWeight: 700,
    color: CLAUDE.INK,
    letterSpacing: '-0.01em',
    opacity,
    transform: `translateY(${translateY}px)`,
    lineHeight: 1.06,
  }}>
    {first}
    <span style={{color: CLAUDE.SPARK}}>{spark}</span>
    {rest}
  </div>
);

// ──────────────────────────────────────────────────────────────────
// DbcPasteReady — B02: the paste-ready Claude Code prompt.
// A composer-style card holds the ask; three response chips underneath
// name the concrete steps the agent will take.
// ──────────────────────────────────────────────────────────────────

export const dbcPasteReadySchema = z.object({
  sparkLine: z.string().default('One paste. Two commands.'),
});
export type DbcPasteReadyProps = z.infer<typeof dbcPasteReadySchema>;

const PASTE_PROMPT_LINES = [
  'Clone https://github.com/nikbearbrown/brutalist.art',
  'into this folder, then run ./setup --install for me.',
  'When it finishes, read ./setup back and tell me which',
  'features are green and which are red.',
];

const STEP_CHIPS = [
  {tag: '01', label: 'CLONE',   detail: 'git clone → your folder'},
  {tag: '02', label: 'INSTALL', detail: './setup --install (free deps + Kokoro)'},
  {tag: '03', label: 'VERIFY',  detail: './setup → readiness table'},
];

export const DbcPasteReady: React.FC<DbcPasteReadyProps> = ({sparkLine}) => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();
  const portrait = height > width;
  const t = frame / fps;

  const titleIn = spring({frame, fps, config: {damping: 26, stiffness: 120, mass: 0.9}});
  const cardIn  = win(t, 0.5, 1.2);
  const linesShown = Math.max(0, Math.min(PASTE_PROMPT_LINES.length, Math.floor((t - 1.2) / 0.5)));

  const pad = 96;
  const cardX = pad;
  const cardW = width - pad * 2;
  const cardY = portrait ? 320 : 240;
  const cardH = portrait ? 620 : 460;

  const chipsY = cardY + cardH + (portrait ? 100 : 100);
  const chipW = portrait ? width - pad * 2 : (width - pad * 2 - 40) / 3;
  const chipH = portrait ? 150 : 220;

  return (
    <AbsoluteFill style={{background: CLAUDE.PAGE}}>
      <Eyebrow text="BRUTALIST · PASTE-READY" opacity={cl(titleIn)} portrait={portrait} />
      <Title
        first="One paste. "
        spark="Two commands."
        opacity={cl(titleIn)}
        portrait={portrait}
        translateY={(1 - titleIn) * 10}
      />

      {/* Composer-shaped prompt card */}
      <div style={{
        position: 'absolute', left: cardX, top: cardY,
        width: cardW, height: cardH,
        background: CLAUDE.CARD,
        border: `1px solid ${CLAUDE.BORDER}`,
        borderRadius: 16,
        boxShadow: '0 14px 44px rgba(61,57,41,0.10)',
        overflow: 'hidden',
        opacity: cardIn,
        transform: `translateY(${(1 - cardIn) * 12}px)`,
      }}>
        {/* header: composer chrome */}
        <div style={{
          padding: '18px 26px',
          borderBottom: `1px solid ${CLAUDE.BORDER}`,
          background: CLAUDE.FOOTER,
          display: 'flex', alignItems: 'center', gap: 14,
        }}>
          <div style={{width: 12, height: 12, borderRadius: 6, background: CLAUDE.SPARK}} />
          <div style={{
            fontFamily: SANS, fontSize: portrait ? 22 : 20,
            color: CLAUDE.INK_SOFT, letterSpacing: 2,
            fontWeight: 700, textTransform: 'uppercase' as const,
          }}>
            claude code · composer
          </div>
          <div style={{marginLeft: 'auto',
            fontFamily: SANS, fontSize: portrait ? 22 : 20,
            color: CLAUDE.INK_SOFT,
          }}>
            @HumanitariansAI
          </div>
        </div>

        {/* prompt body */}
        <div style={{
          padding: portrait ? '40px 40px' : '52px 60px',
          fontFamily: SERIF, fontSize: portrait ? 44 : 44,
          color: CLAUDE.INK, lineHeight: 1.35,
        }}>
          {PASTE_PROMPT_LINES.map((ln, i) => (
            <div key={i} style={{
              opacity: i < linesShown ? 1 : 0,
              transform: `translateY(${i < linesShown ? 0 : 6}px)`,
              marginBottom: 8,
            }}>
              {ln}
            </div>
          ))}
        </div>

        {/* send button row */}
        <div style={{
          position: 'absolute', right: 26, bottom: 22,
          display: 'flex', alignItems: 'center', gap: 12,
        }}>
          <div style={{
            fontFamily: SANS, fontSize: 18, color: CLAUDE.GHOST,
          }}>
            press ↵ to send
          </div>
          <div style={{
            width: 44, height: 44, borderRadius: 22,
            background: CLAUDE.SPARK,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            color: CLAUDE.CARD, fontFamily: SANS, fontSize: 24, fontWeight: 700,
          }}>↑</div>
        </div>
      </div>

      {/* Step chips */}
      <div style={{
        position: 'absolute',
        left: pad, right: pad, top: chipsY,
        display: 'flex', flexDirection: portrait ? 'column' : 'row',
        gap: portrait ? 20 : 20, justifyContent: 'space-between',
      }}>
        {STEP_CHIPS.map((c, i) => {
          const chipIn = win(t, 2.6 + i * 0.3, 3.1 + i * 0.3);
          return (
            <div key={i} style={{
              width: chipW, height: chipH,
              padding: '18px 22px',
              background: CLAUDE.CARD,
              border: `1px solid ${CLAUDE.BORDER}`,
              borderLeft: `5px solid ${CLAUDE.SPARK}`,
              borderRadius: 12,
              opacity: chipIn,
              transform: `translateY(${(1 - chipIn) * 10}px)`,
              display: 'flex', flexDirection: 'column',
              justifyContent: portrait ? 'center' : 'space-between',
            }}>
              <div style={{
                fontFamily: SANS, fontSize: 14,
                letterSpacing: 3, color: CLAUDE.SPARK, fontWeight: 700,
              }}>
                {c.tag} · {c.label}
              </div>
              <div style={{
                fontFamily: MONO, fontSize: portrait ? 22 : 22,
                color: CLAUDE.INK, marginTop: portrait ? 6 : 14,
                lineHeight: 1.3,
              }}>
                {c.detail}
              </div>
            </div>
          );
        })}
      </div>
      {/* sparkLine intentionally suppressed — the three chips carry the message. */}
      {false && sparkLine ? null : null}
    </AbsoluteFill>
  );
};

// ──────────────────────────────────────────────────────────────────
// DbcCloneTree — B03: what a fresh clone actually drops on disk.
// A single folder header and the seven visible children arrive one
// per beat. setup and art carry a terracotta chip so the eye lands
// on the two entry points.
// ──────────────────────────────────────────────────────────────────

export const dbcCloneTreeSchema = z.object({
  sparkLine: z.string().default('A clone is a folder. Everything lives inside it.'),
});
export type DbcCloneTreeProps = z.infer<typeof dbcCloneTreeSchema>;

type TreeRow = {name: string; kind: 'dir' | 'sh' | 'md'; note: string; entry?: boolean};
const TREE_ROWS: TreeRow[] = [
  {name: 'setup',         kind: 'sh',  note: 'free doctor script',           entry: true},
  {name: 'art',           kind: 'sh',  note: 'skills entry point',           entry: true},
  {name: 'README.md',     kind: 'md',  note: 'read this first'},
  {name: 'skills/',       kind: 'dir', note: '15 builder recipes'},
  {name: 'runtime/',      kind: 'dir', note: 'Kokoro + Remotion + Python'},
  {name: 'docs/',         kind: 'dir', note: 'pipeline safety + fellows'},
  {name: 'brands/',       kind: 'dir', note: 'palette tokens + logos'},
];

export const DbcCloneTree: React.FC<DbcCloneTreeProps> = ({sparkLine}) => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();
  const portrait = height > width;
  const t = frame / fps;

  const titleIn = spring({frame, fps, config: {damping: 26, stiffness: 120, mass: 0.9}});
  const cardIn  = win(t, 0.4, 1.0);

  const pad = 96;
  const cardX = pad;
  const cardW = width - pad * 2;
  const cardY = portrait ? 320 : 260;
  const cardH = portrait ? 1180 : 700;

  const rowStart = 0.9;
  const rowStep = 0.35;

  const headerH = portrait ? 96 : 88;
  const rowH = portrait ? Math.floor((cardH - headerH - 60) / TREE_ROWS.length)
                        : Math.floor((cardH - headerH - 40) / TREE_ROWS.length);

  return (
    <AbsoluteFill style={{background: CLAUDE.PAGE}}>
      <Eyebrow text="BRUTALIST · WHAT LANDS ON DISK" opacity={cl(titleIn)} portrait={portrait} />
      <Title
        first="A folder. "
        spark="Nothing outside it."
        opacity={cl(titleIn)}
        portrait={portrait}
        translateY={(1 - titleIn) * 10}
      />

      <div style={{
        position: 'absolute', left: cardX, top: cardY,
        width: cardW, height: cardH,
        background: CLAUDE.CARD,
        border: `1px solid ${CLAUDE.BORDER}`,
        borderRadius: 16,
        boxShadow: '0 12px 40px rgba(61,57,41,0.08)',
        overflow: 'hidden',
        opacity: cardIn,
        transform: `translateY(${(1 - cardIn) * 12}px)`,
      }}>
        {/* header */}
        <div style={{
          padding: portrait ? '26px 32px' : '24px 32px',
          borderBottom: `1px solid ${CLAUDE.BORDER}`,
          background: CLAUDE.FOOTER,
          display: 'flex', alignItems: 'center', gap: 16,
          height: headerH, boxSizing: 'border-box' as const,
        }}>
          <div style={{
            width: 20, height: 16, background: CLAUDE.SPARK,
            borderRadius: 3,
          }} />
          <div style={{
            fontFamily: MONO, fontSize: portrait ? 30 : 30,
            color: CLAUDE.INK, fontWeight: 700,
          }}>
            brutalist.art/
          </div>
          <div style={{
            marginLeft: 'auto',
            fontFamily: SANS, fontSize: 16, letterSpacing: 3,
            color: CLAUDE.INK_SOFT, fontWeight: 700,
            textTransform: 'uppercase' as const,
          }}>
            git clone result
          </div>
        </div>

        {/* rows */}
        <div style={{padding: '18px 40px'}}>
          {TREE_ROWS.map((r, i) => {
            const rowIn = win(t, rowStart + i * rowStep, rowStart + 0.5 + i * rowStep);
            const glyph = r.kind === 'dir' ? '▸' : r.kind === 'sh' ? '▪' : '·';
            return (
              <div key={r.name} style={{
                display: 'flex', alignItems: 'center',
                minHeight: rowH,
                borderBottom: i < TREE_ROWS.length - 1 ? `1px dashed ${CLAUDE.BORDER}` : 'none',
                opacity: rowIn,
                transform: `translateX(${(1 - rowIn) * 12}px)`,
              }}>
                <div style={{
                  width: 40, textAlign: 'center',
                  fontFamily: MONO, fontSize: portrait ? 32 : 30,
                  color: r.entry ? CLAUDE.SPARK : CLAUDE.INK_SOFT,
                }}>
                  {glyph}
                </div>
                <div style={{
                  fontFamily: MONO, fontSize: portrait ? 34 : 32,
                  color: CLAUDE.INK, fontWeight: r.entry ? 700 : 500,
                  width: portrait ? 340 : 340,
                }}>
                  {r.name}
                </div>
                <div style={{
                  fontFamily: SANS, fontSize: portrait ? 26 : 24,
                  color: CLAUDE.INK_SOFT, flex: 1,
                }}>
                  {r.note}
                </div>
                {r.entry && (
                  <div style={{
                    fontFamily: SANS, fontSize: 14, letterSpacing: 2,
                    padding: '4px 10px', background: 'rgba(217,119,87,0.12)',
                    color: CLAUDE.SPARK, fontWeight: 700,
                    borderRadius: 4, textTransform: 'uppercase' as const,
                  }}>
                    entry
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>

      <SparkLine line={sparkLine} t={cl(titleIn)} bottom portrait={portrait} />
    </AbsoluteFill>
  );
};

// ──────────────────────────────────────────────────────────────────
// DbcDoctor — B04: ./setup readiness table.
// A single terminal card with the shell prompt, header row, seven
// feature rows (all green — those are the actual features setup checks
// in this toolkit), and a green closing line.
// ──────────────────────────────────────────────────────────────────

export const dbcDoctorSchema = z.object({
  sparkLine: z.string().default('The doctor tells you what is blocked, and how to fix it.'),
});
export type DbcDoctorProps = z.infer<typeof dbcDoctorSchema>;

type Row = {feature: string; deps: string};
const DOCTOR_ROWS: Row[] = [
  {feature: 'audio (Kokoro Bella/Onyx)',   deps: 'ffmpeg · kokoro · model · synth'},
  {feature: 'captions + word clock',       deps: 'ffmpeg · faster-whisper'},
  {feature: 'Manim beats',                 deps: 'ffmpeg · manim · Pillow'},
  {feature: 'Manim equation beats',        deps: 'ffmpeg · manim · LaTeX'},
  {feature: 'Remotion beats + bookends',   deps: 'node ≥ 20 · npm install'},
  {feature: 'slates / previz / compile',   deps: 'ffmpeg · Pillow'},
  {feature: 'fonts (EB Garamond + Oswald)', deps: 'runtime/fonts · Google Fonts'},
];

const OK = '#3f7f3f';

export const DbcDoctor: React.FC<DbcDoctorProps> = ({sparkLine}) => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();
  const portrait = height > width;
  const t = frame / fps;

  const titleIn = spring({frame, fps, config: {damping: 26, stiffness: 120, mass: 0.9}});
  const cardIn  = win(t, 0.3, 1.0);
  const cmdIn   = win(t, 1.0, 1.5);
  const headIn  = win(t, 1.5, 2.0);

  const pad = 96;
  const cardX = pad;
  const cardW = width - pad * 2;
  const cardY = portrait ? 320 : 240;
  const cardH = portrait ? 1300 : 756;

  const rowStart = 2.1;
  const rowStep = 0.35;

  return (
    <AbsoluteFill style={{background: CLAUDE.PAGE}}>
      <Eyebrow text="BRUTALIST · READINESS TABLE" opacity={cl(titleIn)} portrait={portrait} />
      <Title
        first="Green means "
        spark="ready."
        opacity={cl(titleIn)}
        portrait={portrait}
        translateY={(1 - titleIn) * 10}
      />

      <div style={{
        position: 'absolute', left: cardX, top: cardY,
        width: cardW, height: cardH,
        background: '#111815',
        border: `1px solid #1e2724`,
        borderRadius: 16,
        boxShadow: '0 14px 44px rgba(0,0,0,0.20)',
        overflow: 'hidden',
        opacity: cardIn,
        transform: `translateY(${(1 - cardIn) * 12}px)`,
        padding: portrait ? '36px 40px' : '36px 44px',
        boxSizing: 'border-box' as const,
      }}>
        {/* prompt line */}
        <div style={{
          fontFamily: MONO, fontSize: portrait ? 34 : 30,
          color: '#c8c3b0',
          opacity: cmdIn,
        }}>
          <span style={{color: OK}}>$</span> ./setup
        </div>

        {/* section title */}
        <div style={{
          marginTop: portrait ? 34 : 28,
          fontFamily: MONO, fontSize: portrait ? 26 : 22,
          color: '#e8e2ce', fontWeight: 700,
          opacity: headIn,
        }}>
          brutalist — readiness (free-only toolkit: no keys, ever)
        </div>

        {/* table head */}
        <div style={{
          marginTop: portrait ? 30 : 24,
          display: 'flex',
          fontFamily: MONO, fontSize: portrait ? 22 : 20,
          color: '#a8a396', letterSpacing: 2,
          textTransform: 'uppercase' as const,
          opacity: headIn,
          borderBottom: '1px dashed #2b332e',
          paddingBottom: 10,
        }}>
          <div style={{width: portrait ? 620 : 520}}>FEATURE</div>
          <div style={{flex: 1}}>DEPENDENCIES</div>
          <div style={{width: portrait ? 140 : 140, textAlign: 'right' as const}}>STATUS</div>
        </div>

        {/* rows */}
        <div style={{marginTop: 6}}>
          {DOCTOR_ROWS.map((r, i) => {
            const rowIn = win(t, rowStart + i * rowStep, rowStart + 0.6 + i * rowStep);
            return (
              <div key={r.feature} style={{
                display: 'flex', alignItems: 'center',
                padding: portrait ? '14px 0' : '12px 0',
                borderBottom: i < DOCTOR_ROWS.length - 1 ? '1px dashed #1c2320' : 'none',
                opacity: rowIn,
                transform: `translateX(${(1 - rowIn) * 12}px)`,
              }}>
                <div style={{
                  width: portrait ? 620 : 520,
                  fontFamily: MONO, fontSize: portrait ? 26 : 24,
                  color: '#f2ecd6',
                }}>
                  {r.feature}
                </div>
                <div style={{
                  flex: 1,
                  fontFamily: MONO, fontSize: portrait ? 22 : 20,
                  color: '#a8a396',
                }}>
                  {r.deps}
                </div>
                <div style={{
                  width: portrait ? 140 : 140, textAlign: 'right' as const,
                  fontFamily: MONO, fontSize: portrait ? 26 : 24,
                  color: OK, fontWeight: 700,
                }}>
                  ✓ ready
                </div>
              </div>
            );
          })}
        </div>

        {/* summary line */}
        <div style={{
          marginTop: portrait ? 30 : 22,
          fontFamily: MONO, fontSize: portrait ? 26 : 24,
          color: OK, fontWeight: 700,
          opacity: win(t, rowStart + DOCTOR_ROWS.length * rowStep + 0.2,
                          rowStart + DOCTOR_ROWS.length * rowStep + 0.9),
        }}>
          All core features ready. Voices: Bella (af_bella) and Onyx (am_onyx). Cost: $0.00.
        </div>
      </div>
      {/* sparkLine intentionally suppressed — the dark card is the whole exhibit. */}
      {false && sparkLine ? null : null}
    </AbsoluteFill>
  );
};

// ──────────────────────────────────────────────────────────────────
// DbcLanes — B05: three lanes. Claude Code subscription (runs the
// agent), optional paid Anthropic API (metered), Brutalist pipeline
// (Kokoro / Remotion / Manim — free). The middle lane is muted; the
// left and right are the ones fellows actually depend on.
// ──────────────────────────────────────────────────────────────────

export const dbcLanesSchema = z.object({
  sparkLine: z.string().default('Subscription runs the agent. Brutalist itself is free.'),
});
export type DbcLanesProps = z.infer<typeof dbcLanesSchema>;

type LaneSpec = {
  tag: string;
  title: string;
  price: string;
  rows: string[];
  accent: 'spark' | 'ghost' | 'ink';
};

const LANE_SPECS: LaneSpec[] = [
  {
    tag: '01', title: 'Claude Code',
    price: 'Your subscription',
    rows: ['the desktop composer', 'the agent that reads + writes', 'runs on your plan'],
    accent: 'spark',
  },
  {
    tag: '02', title: 'Anthropic API',
    price: 'Paid · optional',
    rows: ['only for scripted calls', 'metered per token', 'not needed for Brutalist'],
    accent: 'ghost',
  },
  {
    tag: '03', title: 'Brutalist pipeline',
    price: 'Free · local',
    rows: ['Kokoro voice (local)', 'Remotion (your machine)', 'Manim (your machine)'],
    accent: 'ink',
  },
];

export const DbcLanes: React.FC<DbcLanesProps> = ({sparkLine}) => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();
  const portrait = height > width;
  const t = frame / fps;

  const titleIn = spring({frame, fps, config: {damping: 26, stiffness: 120, mass: 0.9}});
  const pad = 96;

  const laneStartY = portrait ? 400 : 260;
  const laneW = portrait ? width - pad * 2 : (width - pad * 2 - 40) / 3;
  const laneH = portrait ? 340 : 580;
  const laneGap = portrait ? 30 : 20;

  const bannerY = portrait
    ? laneStartY + LANE_SPECS.length * (laneH + laneGap) + 30
    : laneStartY + laneH + 50;

  return (
    <AbsoluteFill style={{background: CLAUDE.PAGE}}>
      <Eyebrow text="BRUTALIST · THREE LANES" opacity={cl(titleIn)} portrait={portrait} />
      <Title
        first="Subscription. Optional key. "
        spark="Free pipeline."
        opacity={cl(titleIn)}
        portrait={portrait}
        translateY={(1 - titleIn) * 10}
      />

      {LANE_SPECS.map((l, i) => {
        const laneIn = win(t, 0.6 + i * 0.4, 1.2 + i * 0.4);
        const x = portrait ? pad : pad + i * (laneW + laneGap);
        const y = portrait ? laneStartY + i * (laneH + laneGap) : laneStartY;
        const accentColor = l.accent === 'spark' ? CLAUDE.SPARK
                          : l.accent === 'ghost' ? CLAUDE.GHOST
                          : CLAUDE.INK;
        const bgTint = l.accent === 'spark' ? 'rgba(217,119,87,0.06)'
                     : l.accent === 'ghost' ? 'rgba(169,164,145,0.06)'
                     : CLAUDE.CARD;
        return (
          <div key={l.title} style={{
            position: 'absolute', left: x, top: y,
            width: laneW, height: laneH,
            background: bgTint,
            border: `1px solid ${accentColor}`,
            borderTop: `6px solid ${accentColor}`,
            borderRadius: 14,
            padding: portrait ? '22px 26px' : '26px 28px',
            boxSizing: 'border-box' as const,
            opacity: laneIn,
            transform: `translateY(${(1 - laneIn) * 12}px)`,
            display: 'flex', flexDirection: 'column',
          }}>
            <div style={{
              fontFamily: SANS, fontSize: 14, letterSpacing: 3,
              color: accentColor, fontWeight: 700,
              textTransform: 'uppercase' as const,
            }}>
              {l.tag} · {l.price}
            </div>
            <div style={{
              fontFamily: SERIF, fontSize: portrait ? 52 : 46,
              color: CLAUDE.INK, marginTop: 6, fontWeight: 700,
              lineHeight: 1.05,
            }}>
              {l.title}
            </div>
            <div style={{
              marginTop: portrait ? 18 : 24,
              display: 'flex', flexDirection: 'column', gap: portrait ? 10 : 14,
              flex: 1,
            }}>
              {l.rows.map((row, ri) => (
                <div key={ri} style={{
                  display: 'flex', gap: 12, alignItems: 'baseline',
                  fontFamily: SANS, fontSize: portrait ? 26 : 24,
                  color: CLAUDE.INK,
                }}>
                  <span style={{color: accentColor, fontWeight: 700, minWidth: 16}}>·</span>
                  <span>{row}</span>
                </div>
              ))}
            </div>
          </div>
        );
      })}

      {/* banner */}
      <div style={{
        position: 'absolute',
        left: pad, right: pad,
        top: bannerY,
        padding: portrait ? '20px 26px' : '22px 30px',
        background: 'rgba(217,119,87,0.08)',
        borderLeft: `6px solid ${CLAUDE.SPARK}`,
        borderRadius: 10,
        display: 'flex', alignItems: 'baseline', gap: 20,
        opacity: win(t, 2.4, 3.0),
      }}>
        <div style={{
          fontFamily: SANS, fontSize: 15, letterSpacing: 3,
          fontWeight: 700, color: CLAUDE.SPARK,
          textTransform: 'uppercase' as const,
        }}>
          SETUP COST
        </div>
        <div style={{
          fontFamily: SERIF, fontSize: portrait ? 44 : 46,
          color: CLAUDE.INK, fontWeight: 700,
        }}>
          $0.00
        </div>
        <div style={{
          fontFamily: SANS, fontSize: portrait ? 24 : 22,
          color: CLAUDE.INK_SOFT, marginLeft: 'auto',
        }}>
          Brutalist itself never asks for a card.
        </div>
      </div>
      {/* sparkLine intentionally suppressed — the setup-cost banner delivers it. */}
      {false && sparkLine ? null : null}
    </AbsoluteFill>
  );
};

// ──────────────────────────────────────────────────────────────────
// DbcNotClaims — B06: the honest not-list. Three rows enumerating
// what setup deliberately does NOT do, plus the one download it
// actually performs.
// ──────────────────────────────────────────────────────────────────

export const dbcNotClaimsSchema = z.object({
  sparkLine: z.string().default('The tool has a shape. That shape is the honesty.'),
});
export type DbcNotClaimsProps = z.infer<typeof dbcNotClaimsSchema>;

const NOT_ROWS = [
  {label: 'No accounts created.',        body: 'setup asks for zero credentials.'},
  {label: 'No files outside this folder.', body: 'everything lives inside your clone.'},
  {label: 'No upload. One download.',    body: '~340MB Kokoro voice model from a GitHub release, the first --install.'},
];

export const DbcNotClaims: React.FC<DbcNotClaimsProps> = ({sparkLine}) => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();
  const portrait = height > width;
  const t = frame / fps;

  const titleIn = spring({frame, fps, config: {damping: 26, stiffness: 120, mass: 0.9}});
  const pad = 96;

  const rowStart = portrait ? 320 : 300;
  const rowH = portrait ? 380 : 200;
  const rowGap = 24;

  return (
    <AbsoluteFill style={{background: CLAUDE.PAGE}}>
      <Eyebrow text="BRUTALIST · SETUP HONESTY" opacity={cl(titleIn)} portrait={portrait} />
      <Title
        first="What setup "
        spark="won't do."
        opacity={cl(titleIn)}
        portrait={portrait}
        translateY={(1 - titleIn) * 10}
      />

      {NOT_ROWS.map((r, i) => {
        const rowIn = win(t, 0.6 + i * 0.6, 1.2 + i * 0.6);
        return (
          <div key={r.label} style={{
            position: 'absolute',
            left: pad, right: pad,
            top: rowStart + i * (rowH + rowGap),
            padding: portrait ? '32px 34px' : '28px 34px',
            background: CLAUDE.CARD,
            border: `1px solid ${CLAUDE.BORDER}`,
            borderLeft: `6px solid ${CLAUDE.SPARK}`,
            borderRadius: 12,
            opacity: rowIn,
            transform: `translateY(${(1 - rowIn) * 14}px)`,
            display: 'flex', flexDirection: portrait ? 'column' : 'row',
            alignItems: portrait ? 'flex-start' : 'baseline',
            gap: portrait ? 12 : 26,
          }}>
            <div style={{
              fontFamily: SERIF, fontSize: portrait ? 60 : 48,
              fontWeight: 700, color: CLAUDE.SPARK,
              minWidth: portrait ? 'auto' : 480,
              lineHeight: 1.08,
            }}>
              {r.label}
            </div>
            <div style={{
              fontFamily: SANS, fontSize: portrait ? 34 : 28,
              color: CLAUDE.INK, lineHeight: 1.35,
            }}>
              {r.body}
            </div>
          </div>
        );
      })}

      <SparkLine line={sparkLine} t={cl(titleIn)} bottom portrait={portrait} />
    </AbsoluteFill>
  );
};

// ──────────────────────────────────────────────────────────────────
// DbcVerdict — B07 verdict artifact card. Same structure as the
// what-is-brutalist WibVerdict (three numbered lines under a heading)
// sized to fill the safe area.
// ──────────────────────────────────────────────────────────────────

export const dbcVerdictSchema = z.object({
  artifactTitle: z.string().default('Verdict'),
  artifactHeading: z.string().default('Download Brutalist, in three lines.'),
  artifactLines: z.array(z.string()).default([
    'Clone the public repo. You now own the toolkit as plain files.',
    'Run ./setup --install once, then ./setup any time. The doctor tells you what is ready.',
    'Brutalist itself is free. Your Claude Code subscription runs the agent.',
  ]),
  sparkLine: z.string().default('That is how you download Brutalist.'),
});
export type DbcVerdictProps = z.infer<typeof dbcVerdictSchema>;

const stripLeadNum = (s: string) => s.replace(/^\s*\d+\s*[.)\-–—:]\s*/, '');

export const DbcVerdict: React.FC<DbcVerdictProps> = ({
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
        <div style={{
          background: CLAUDE.PAGE,
          borderBottom: `1px solid ${CLAUDE.BORDER}`,
          padding: portrait ? '28px 44px' : '32px 56px',
          display: 'flex', alignItems: 'center', gap: 20,
        }}>
          <div style={{width: 14, height: 14, borderRadius: 7, background: CLAUDE.SPARK}} />
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
            BRUTALIST · DOWNLOAD
          </span>
        </div>

        <div style={{
          padding: portrait ? '48px 44px' : '72px 84px',
          display: 'flex', flexDirection: 'column',
          height: `calc(100% - ${portrait ? 100 : 116}px)`,
          boxSizing: 'border-box' as const,
        }}>
          <div style={{
            fontFamily: SERIF, fontWeight: 700,
            fontSize: portrait ? 68 : 84,
            color: CLAUDE.INK,
            marginBottom: portrait ? 48 : 68,
            opacity: cl(headIn),
            letterSpacing: '-0.01em',
            lineHeight: 1.05,
          }}>
            {artifactHeading.replace(/([.?!…]+)\s*$/, '')}
            <span style={{color: CLAUDE.SPARK}}>
              {(artifactHeading.match(/([.?!…]+)\s*$/) || ['.', '.'])[1]}
            </span>
          </div>

          <div style={{
            display: 'flex', flexDirection: 'column',
            gap: portrait ? 38 : 44, flex: 1,
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
                    fontFamily: SANS, fontSize: portrait ? 40 : 44,
                    color: CLAUDE.INK, lineHeight: 1.35,
                  }}>
                    {line}
                  </span>
                </div>
              );
            })}
          </div>

          {sparkLine ? (
            <div style={{
              marginTop: portrait ? 40 : 32,
              fontFamily: SERIF, fontStyle: 'italic',
              fontSize: portrait ? 34 : 38,
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
// DbcOutro — the title-restate outro. Hardcodes @HumanitariansAI
// (the shipped ClaudeTitleOutro hardcodes @NikBearBrown per
// OUTRO-LOCK.md; this is the required native custom variant for the
// HAI channel — never modifies the live library).
// ──────────────────────────────────────────────────────────────────

export const dbcOutroSchema = z.object({
  title: z.string().default('Download Brutalist with Claude Code.'),
  subline: z.string().default('Liam, in for Bear.'),
});
export type DbcOutroProps = z.infer<typeof dbcOutroSchema>;

const HAI_HANDLE = '@HumanitariansAI';

export const DbcOutro: React.FC<DbcOutroProps> = ({title, subline}) => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();
  const portrait = height > width;

  const fadeIn = interpolate(frame, [0, 18], [0, 1], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });
  const handleIn = spring({frame: frame - 20, fps, config: {damping: 24, stiffness: 100}});
  const sublineIn = spring({frame: frame - 40, fps, config: {damping: 24, stiffness: 100}});
  const eyebrowIn = spring({frame: frame - 6, fps, config: {damping: 24, stiffness: 100}});

  const pm = title.match(/^([\s\S]*?)\s*([.?!…]+)\s*$/);
  const titleBody  = pm ? pm[1] : title;
  const titlePunct = pm ? pm[2] : '.';

  const pad = 96;

  return (
    <AbsoluteFill style={{
      background: CLAUDE.PAGE,
      opacity: fadeIn,
    }}>
      {/* Eyebrow */}
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
        BRUTALIST · EPISODE 02
      </div>

      {/* Rule */}
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

      {/* Title */}
      <div style={{
        position: 'absolute',
        top: portrait ? 280 : 260,
        left: pad, right: pad,
        textAlign: 'center',
        fontFamily: SERIF,
        fontWeight: 700,
        fontSize: portrait ? 110 : 140,
        color: CLAUDE.INK,
        letterSpacing: '-0.02em',
        lineHeight: 1.02,
      }}>
        {titleBody}
        <span style={{color: CLAUDE.SPARK}}>{titlePunct}</span>
      </div>

      {/* Handle — HARDCODED to @HumanitariansAI */}
      <div style={{
        position: 'absolute',
        top: portrait ? 1300 : 780,
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

      {/* Subline */}
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
