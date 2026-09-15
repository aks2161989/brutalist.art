/**
 * CommandTodo.tsx — reel-local components for
 * claude-liam-brutalist-command-todo.
 *
 * Palette: cream #FAF9F5, ink #3D3929, terracotta #D97757 (ONE accent).
 * Each component reads useVideoConfig() and reflows for portrait 9:16,
 * so the same source registers as both 16:9 (1920x1080) and 9:16
 * (1080x1920) compositions in Root.tsx.
 *
 * Registered under the folder "ClaudeLiamCommandTodo" in Root.tsx.
 */
import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate } from 'remotion';
import { z } from 'zod';

const PAGE   = '#FAF9F5';
const INK    = '#3D3929';
const INK_S  = '#73705F';
const GHOST  = '#B0AD9A';
const ACC    = '#D97757';
const CARD   = '#FFFFFF';
const BORDER = '#E5E2D9';
const PILL   = '#EDEBE1';
const CODE_BG = '#181510';
const CODE_FG = '#F1EEE4';

const SERIF = '"Tiempos Text", "EB Garamond", Georgia, "Times New Roman", serif';
const SANS  = '-apple-system, "SF Pro Text", "Segoe UI", "Helvetica Neue", sans-serif';
const MONO  = 'ui-monospace, "SF Mono", Menlo, monospace';

const cl = (v: number, a = 0, b = 1) => Math.min(b, Math.max(a, v));
const SPRING_GENTLE = { damping: 30, stiffness: 120, mass: 0.9 };

/** Safe-area constants matching runtime/remotion/src/tokens/layout.ts (both aspects). */
function useSafe() {
  const { width: W, height: H } = useVideoConfig();
  const portrait = H > W;
  // Landscape safe area is x=96 y=54 (5% of 1080-tall); portrait safe is x=54 y=96.
  const SX = portrait ? 72 : 108;
  const SY = portrait ? 168 : 84;
  return { SX, SY, W, H, portrait };
}

/** Spark + one short serif line — anchored inside the vertical safe area.
 *  Portrait note: measured sy=128 → first ink at physical y=177 in a 2160x3840
 *  render, which trips SAFE916.y=192 (minus 8px margin → threshold 184). The
 *  callers all pass `sy = SY - 40`; adding a portrait bump keeps landscape math
 *  untouched while pushing the first ink well inside safe. Space-evenly on the
 *  content column below means the first card starts far below the container top,
 *  so the shifted spark still has clear negative space around it. */
const SparkLine: React.FC<{ line: string; t: number; bottom?: boolean; sx: number; sy: number; fontPx: number }> = ({ line, t, bottom, sx, sy, fontPx }) => {
  const { width: W, height: H } = useVideoConfig();
  const portraitBump = (H > W && !bottom) ? 60 : 0;
  return (
    <div style={{
      position: 'absolute', left: sx, [bottom ? 'bottom' : 'top']: sy + portraitBump,
      display: 'flex', alignItems: 'baseline', gap: fontPx * 0.35, opacity: t,
    }}>
      <span style={{ fontFamily: SERIF, fontSize: fontPx, color: ACC, lineHeight: 1 }}>*</span>
      <span style={{ fontFamily: SERIF, fontSize: fontPx, color: INK_S, lineHeight: 1 }}>{line}</span>
    </div>
  );
};

// ===========================================================================
// TodoPipeline — beat_sheet.json → art todo → three receipts
// ===========================================================================
export const todoPipelineSchema = z.object({
  spark: z.string().default('One arrow. Beat sheet in, three receipts out.'),
  tagline: z.string().default('Edit the sheet, not the receipts.'),
});
export type TodoPipelineProps = z.infer<typeof todoPipelineSchema>;

export const TodoPipeline: React.FC<TodoPipelineProps> = ({ spark, tagline }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const { SX, SY, portrait } = useSafe();
  const t = cl(spring({ frame, fps, config: SPRING_GENTLE }));
  const midIn  = cl(spring({ frame: frame - 20, fps, config: SPRING_GENTLE }));
  const rightIn = cl(spring({ frame: frame - 44, fps, config: SPRING_GENTLE }));
  const cardIn = (i: number) => cl(spring({ frame: frame - 60 - i * 10, fps, config: SPRING_GENTLE }));
  const tagIn  = cl(interpolate(frame, [140, 165], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));

  const leftLabel = 'beat_sheet.json';
  const midLabel = './art todo <reel>';
  const receipts = [
    { name: 'todo.json',  who: 'FOR AGENTS',   accent: false },
    { name: 'STATUS.md',  who: 'FOR YOU',      accent: false },
    { name: 'ToDo.md',    who: 'FOR HUMAN OWNERS', accent: true },
  ];

  const NodeCard = (label: string, sub: string, opacity: number, accent = false, big = false) => (
    <div style={{
      background: CARD, border: `2px solid ${accent ? ACC : BORDER}`,
      borderRadius: 20, padding: big ? '30px 40px' : '24px 32px',
      boxShadow: '0 12px 40px rgba(61,57,41,0.12)', opacity,
      display: 'flex', flexDirection: 'column', gap: 10, alignItems: 'center',
      minWidth: portrait ? (big ? 780 : 620) : (big ? 520 : 380),
    }}>
      <div style={{ fontFamily: SANS, fontSize: portrait ? 20 : 22, letterSpacing: '0.18em', color: accent ? ACC : INK_S, textTransform: 'uppercase' }}>{sub}</div>
      <div style={{ fontFamily: MONO, fontSize: big ? (portrait ? 62 : 54) : (portrait ? 50 : 44), color: INK }}>{label}</div>
    </div>
  );

  const Arrow = (opacity: number, vertical = false) => (
    <div style={{
      display: 'flex', alignItems: 'center', justifyContent: 'center',
      opacity, transform: vertical ? 'rotate(90deg)' : 'none',
    }}>
      <div style={{ height: 4, width: 120, background: INK }} />
      <div style={{
        width: 0, height: 0, borderLeft: `26px solid ${INK}`,
        borderTop: '18px solid transparent', borderBottom: '18px solid transparent',
        marginLeft: -2,
      }} />
    </div>
  );

  const ReceiptStack = () => (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 16 : 22 }}>
      {receipts.map((r, i) => (
        <div key={r.name} style={{
          background: CARD, border: `2px solid ${r.accent ? ACC : BORDER}`,
          borderRadius: 16, padding: portrait ? '16px 26px' : '18px 30px',
          minWidth: portrait ? 780 : 460,
          boxShadow: '0 8px 26px rgba(61,57,41,0.10)',
          opacity: cardIn(i), transform: `translateY(${(1 - cardIn(i)) * 14}px)`,
          display: 'flex', flexDirection: 'column', gap: 4,
        }}>
          <div style={{ fontFamily: SANS, fontSize: 18, letterSpacing: '0.18em', color: r.accent ? ACC : INK_S, textTransform: 'uppercase' }}>{r.who}</div>
          <div style={{ fontFamily: MONO, fontSize: portrait ? 46 : 42, color: INK }}>{r.name}</div>
        </div>
      ))}
    </div>
  );

  return (
    <AbsoluteFill style={{ background: PAGE, color: INK }}>
      <SparkLine line={spark} t={t} sx={SX} sy={SY - 40} fontPx={portrait ? 32 : 36} />
      {portrait ? (
        <div style={{
          position: 'absolute', top: SY, left: SX, right: SX, bottom: SY,
          display: 'flex', flexDirection: 'column', alignItems: 'center',
          justifyContent: 'space-evenly', gap: 8,
        }}>
          {NodeCard(leftLabel, 'BEATS · SHOT · DURATIONS', t, false, false)}
          {Arrow(midIn, true)}
          {NodeCard(midLabel, 'READ · DERIVE · WRITE', midIn, false, true)}
          {Arrow(rightIn, true)}
          <ReceiptStack />
          <div style={{ fontFamily: SERIF, fontSize: 34, fontStyle: 'italic', color: INK, opacity: tagIn }}>{tagline}</div>
        </div>
      ) : (
        <div style={{
          position: 'absolute', top: SY, left: SX, right: SX, bottom: SY + 60,
          display: 'flex', flexDirection: 'row', alignItems: 'center',
          justifyContent: 'space-evenly',
        }}>
          {NodeCard(leftLabel, 'BEATS · SHOT · DURATIONS', t)}
          {Arrow(midIn)}
          {NodeCard(midLabel, 'READ · DERIVE · WRITE', midIn, false, true)}
          {Arrow(rightIn)}
          <ReceiptStack />
        </div>
      )}
      {!portrait && (
        <div style={{
          position: 'absolute', bottom: SY, left: 0, right: 0, textAlign: 'center',
          fontFamily: SERIF, fontSize: 38, fontStyle: 'italic', color: INK, opacity: tagIn,
        }}>{tagline}</div>
      )}
    </AbsoluteFill>
  );
};

// ===========================================================================
// TodoCommand — the exact syntax + three flag rows
// ===========================================================================
export const todoCommandSchema = z.object({
  spark: z.string().default('Four surfaces. Nothing else.'),
  command: z.string().default('./art todo <reel> [flags]'),
  flags: z.array(z.object({
    flag: z.string(),
    effect: z.string(),
  })).default([
    { flag: '--open',            effect: 'only beats still needing a clip' },
    { flag: '--method <name>',   effect: 'filter to one lane · manim | remotion | ai-video-prompt | historical-image | user-capture' },
    { flag: '--json',            effect: 'print todo.json to stdout — for agents' },
  ]),
});
export type TodoCommandProps = z.infer<typeof todoCommandSchema>;

export const TodoCommand: React.FC<TodoCommandProps> = ({ spark, command, flags }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const { SX, SY, portrait } = useSafe();
  const t = cl(spring({ frame, fps, config: SPRING_GENTLE }));
  const cmdIn = cl(spring({ frame: frame - 14, fps, config: SPRING_GENTLE }));
  const flagIn = (i: number) => cl(spring({ frame: frame - 40 - i * 18, fps, config: SPRING_GENTLE }));

  const cmdFontPx = portrait ? 48 : 78;
  const flagFontPx = portrait ? 44 : 56;
  const effectFontPx = portrait ? 30 : 34;

  return (
    <AbsoluteFill style={{ background: PAGE, color: INK }}>
      <SparkLine line={spark} t={t} sx={SX} sy={SY - 40} fontPx={portrait ? 32 : 36} />

      <div style={{
        position: 'absolute', left: SX, right: SX, top: SY + 60, bottom: SY + 20,
        display: 'flex', flexDirection: 'column', justifyContent: 'center',
        gap: portrait ? 40 : 44,
      }}>
        {/* Command bar */}
        <div style={{
          background: CODE_BG, borderRadius: 20, padding: portrait ? '32px 40px' : '38px 52px',
          fontFamily: MONO, fontSize: cmdFontPx, color: CODE_FG, letterSpacing: '-0.01em',
          opacity: cmdIn, transform: `translateY(${(1 - cmdIn) * 14}px)`,
          boxShadow: '0 14px 42px rgba(61,57,41,0.20)',
        }}>
          <span style={{ color: ACC }}>$ </span>{command}
        </div>

        {/* Flag rows */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 28 : 30 }}>
          {flags.map((f, i) => {
            const accent = i === flags.length - 1;
            return (
              <div key={f.flag} style={{
                display: 'flex', flexDirection: portrait ? 'column' : 'row',
                alignItems: portrait ? 'flex-start' : 'baseline',
                gap: portrait ? 8 : 34, opacity: flagIn(i),
                transform: `translateX(${(1 - flagIn(i)) * -18}px)`,
              }}>
                <div style={{
                  fontFamily: MONO, fontSize: flagFontPx,
                  color: accent ? ACC : INK, minWidth: portrait ? 'auto' : 420,
                }}>{f.flag}</div>
                <div style={{
                  fontFamily: SERIF, fontSize: effectFontPx, color: INK_S, lineHeight: 1.35,
                }}>{f.effect}</div>
              </div>
            );
          })}
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ===========================================================================
// TodoRun — a real terminal transcript with staggered rows
// ===========================================================================
export const todoRunSchema = z.object({
  spark: z.string().default('Live receipt. Five beats, zero filled.'),
  command: z.string().default('$ ./art todo demo/example-reel'),
  header: z.string().default('[todo] example-reel: 0/5 filled → todo.json + STATUS.md + ToDo.md'),
  rows: z.array(z.object({
    id: z.string(),
    status: z.string(),
    method: z.string(),
    who: z.string(),
    slot: z.string(),
    accent: z.boolean().default(false),
  })).default([
    { id: 'B00', status: 'needs-fill', method: 'remotion',         who: 'pipeline', slot: 'media/B00.mp4', accent: false },
    { id: 'B01', status: 'needs-fill', method: 'manim',            who: 'pipeline', slot: 'manim/B01.mp4', accent: false },
    { id: 'B02', status: 'needs-fill', method: 'historical-image', who: 'human',    slot: 'media/B02.png (or .mp4)', accent: true },
    { id: 'B03', status: 'needs-fill', method: 'user-capture',     who: 'human',    slot: 'media/B03.mp4', accent: true },
    { id: 'B04', status: 'needs-fill', method: 'ai-video-prompt',  who: 'human',    slot: 'media/B04.mp4', accent: true },
  ]),
});
export type TodoRunProps = z.infer<typeof todoRunSchema>;

export const TodoRun: React.FC<TodoRunProps> = ({ spark, command, header, rows }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const { SX, SY, portrait } = useSafe();
  const t = cl(spring({ frame, fps, config: SPRING_GENTLE }));
  const cmdIn = cl(spring({ frame: frame - 8, fps, config: SPRING_GENTLE }));
  const hdrIn = cl(spring({ frame: frame - 22, fps, config: SPRING_GENTLE }));
  const rowIn = (i: number) => cl(spring({ frame: frame - 42 - i * 16, fps, config: SPRING_GENTLE }));

  const font = portrait ? 30 : 30;
  const rowH = portrait ? 62 : 60;

  return (
    <AbsoluteFill style={{ background: PAGE, color: INK }}>
      <SparkLine line={spark} t={t} sx={SX} sy={SY - 40} fontPx={portrait ? 30 : 34} />

      <div style={{
        position: 'absolute', left: SX, right: SX, top: SY + 40, bottom: SY + 20,
        background: CODE_BG, borderRadius: 18, padding: portrait ? '26px 24px' : '34px 44px',
        boxShadow: '0 14px 42px rgba(61,57,41,0.20)',
        display: 'flex', flexDirection: 'column', gap: 10,
        overflow: 'hidden',
      }}>
        <div style={{ fontFamily: MONO, fontSize: font * 1.15, color: CODE_FG, opacity: cmdIn }}>
          <span style={{ color: ACC }}>{command.slice(0, 1)}</span>
          {command.slice(1)}
        </div>
        <div style={{ fontFamily: MONO, fontSize: font, color: GHOST, opacity: hdrIn }}>
          {header}
        </div>
        <div style={{ marginTop: 8 }} />
        {rows.map((r, i) => (
          <div key={r.id} style={{
            display: 'grid', gridTemplateColumns: portrait
              ? '80px 1fr 130px'
              : '90px 1fr 220px 130px 1fr',
            gap: portrait ? 14 : 22, alignItems: 'baseline', height: rowH,
            fontFamily: MONO, fontSize: font, color: CODE_FG, opacity: rowIn(i),
            transform: `translateX(${(1 - rowIn(i)) * -12}px)`,
          }}>
            <div style={{ color: ACC }}>{r.id}</div>
            <div style={{ color: GHOST }}>{r.status}</div>
            {!portrait && <div>{r.method}</div>}
            <div style={{ color: r.accent ? ACC : GHOST }}>{r.who}</div>
            <div style={{
              gridColumn: portrait ? '1 / span 3' : 'auto',
              color: r.accent ? '#F0C4B0' : CODE_FG,
              fontSize: portrait ? font * 0.85 : font, opacity: 0.95,
              paddingLeft: portrait ? 82 : 0,
            }}>
              {portrait ? `${r.method} → ${r.slot}` : r.slot}
            </div>
          </div>
        ))}
      </div>
    </AbsoluteFill>
  );
};

// ===========================================================================
// TodoEntry — one JSON entry with six fields highlighted in turn
// ===========================================================================
export const todoEntrySchema = z.object({
  spark: z.string().default('One entry. Six fields. Nothing invented.'),
});
export type TodoEntryProps = z.infer<typeof todoEntrySchema>;

const ENTRY = [
  { key: 'beat_id',    value: '"B02"',                          note: 'the beat this row is about' },
  { key: 'status',     value: '"needs-fill"',                   note: 'is the slot on disk yet?' },
  { key: 'method',     value: '"historical-image"',             note: 'from beat_plan.fill_plan(beat)' },
  { key: 'who',        value: '"human"',                        note: '"pipeline" or "human"' },
  { key: 'slot',       value: '"media/B02.png (or .mp4)"',      note: 'the filename the pantry expects' },
  { key: 'prompt',     value: '"find: the 1963 chart …"',       note: 'search seed for the owner' },
  { key: 'label',      value: '"The 1963 chart of energy …"',   note: 'first 100 chars of the beat text' },
];

export const TodoEntry: React.FC<TodoEntryProps> = ({ spark }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const { SX, SY, portrait } = useSafe();
  const t = cl(spring({ frame, fps, config: SPRING_GENTLE }));

  const rowIn = (i: number) => cl(spring({ frame: frame - 14 - i * 12, fps, config: SPRING_GENTLE }));
  // Which row carries the terracotta bar right now.
  const litRow = Math.min(ENTRY.length - 1, Math.max(0, Math.floor((frame - 24) / 26)));

  const keyPx  = portrait ? 34 : 38;
  const valPx  = portrait ? 28 : 34;
  const notePx = portrait ? 22 : 26;

  return (
    <AbsoluteFill style={{ background: PAGE, color: INK }}>
      <SparkLine line={spark} t={t} sx={SX} sy={SY - 40} fontPx={portrait ? 32 : 36} />

      <div style={{
        position: 'absolute', left: SX, right: SX, top: SY + 40, bottom: SY + 20,
        background: CARD, borderRadius: 20, padding: portrait ? '26px 30px' : '36px 48px',
        border: `1px solid ${BORDER}`, boxShadow: '0 14px 42px rgba(61,57,41,0.10)',
        display: 'flex', flexDirection: 'column', gap: portrait ? 10 : 16,
        overflow: 'hidden',
      }}>
        <div style={{
          fontFamily: MONO, fontSize: keyPx * 0.75, color: INK_S,
        }}>{'{'}</div>
        {ENTRY.map((row, i) => {
          const lit = i === litRow;
          return (
            <div key={row.key} style={{
              display: 'grid',
              gridTemplateColumns: portrait ? '10px 1fr' : '10px minmax(180px, 220px) minmax(300px, 1fr) 1fr',
              gap: portrait ? 12 : 26, alignItems: 'baseline',
              opacity: rowIn(i), padding: portrait ? '4px 0' : '6px 0',
              transform: `translateX(${(1 - rowIn(i)) * -12}px)`,
            }}>
              <div style={{
                width: 10, height: keyPx * 0.9, background: lit ? ACC : 'transparent',
                borderRadius: 3, alignSelf: 'center',
              }} />
              <div style={{ fontFamily: MONO, fontSize: keyPx, color: lit ? ACC : INK, fontWeight: 500 }}>
                "{row.key}":
              </div>
              <div style={{ fontFamily: MONO, fontSize: valPx, color: INK_S }}>{row.value}</div>
              {portrait ? (
                <div style={{
                  gridColumn: '1 / span 2', fontFamily: SERIF, fontStyle: 'italic',
                  fontSize: notePx, color: INK_S, paddingLeft: 22, lineHeight: 1.35,
                }}>{row.note}</div>
              ) : (
                <div style={{ fontFamily: SERIF, fontStyle: 'italic', fontSize: notePx, color: INK_S, lineHeight: 1.35 }}>
                  {row.note}
                </div>
              )}
            </div>
          );
        })}
        <div style={{
          fontFamily: MONO, fontSize: keyPx * 0.75, color: INK_S,
        }}>{'}'}</div>
      </div>
    </AbsoluteFill>
  );
};

// ===========================================================================
// TodoMethods — the five fill lanes as a table
// ===========================================================================
export const todoMethodsSchema = z.object({
  spark: z.string().default('Five lanes. The sheet decides. Two are on the machine.'),
});
export type TodoMethodsProps = z.infer<typeof todoMethodsSchema>;

const METHODS: Array<{ name: string; who: 'pipeline' | 'human'; note: string }> = [
  { name: 'remotion',         who: 'pipeline', note: 'shot.remotion.pattern → media/<BID>.mp4' },
  { name: 'manim',            who: 'pipeline', note: 'shot.manim / engine=manim → manim/<BID>.mp4' },
  { name: 'historical-image', who: 'human',    note: 'shot.source=archive → media/<BID>.png' },
  { name: 'user-capture',     who: 'human',    note: 'shot.source=screen / capture → media/<BID>.mp4' },
  { name: 'ai-video-prompt',  who: 'human',    note: 'no annotation → suggest a 5–10s clip' },
];

export const TodoMethods: React.FC<TodoMethodsProps> = ({ spark }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const { SX, SY, portrait } = useSafe();
  const t = cl(spring({ frame, fps, config: SPRING_GENTLE }));
  const rowIn = (i: number) => cl(spring({ frame: frame - 14 - i * 14, fps, config: SPRING_GENTLE }));

  const namePx = portrait ? 58 : 74;
  const notePx = portrait ? 26 : 36;
  const chipPx = portrait ? 22 : 26;

  return (
    <AbsoluteFill style={{ background: PAGE, color: INK }}>
      <SparkLine line={spark} t={t} sx={SX} sy={SY - 40} fontPx={portrait ? 32 : 38} />

      <div style={{
        position: 'absolute', left: SX, right: SX,
        top: SY + 40, bottom: SY + 20,
        display: 'flex', flexDirection: 'column', overflow: 'hidden',
      }}>
        {/* Table header */}
        <div style={{
          display: 'grid',
          gridTemplateColumns: portrait ? '1fr 160px' : '460px 220px 1fr',
          gap: portrait ? 18 : 44, alignItems: 'baseline',
          fontFamily: SANS, fontSize: portrait ? 22 : 26, letterSpacing: '0.18em',
          textTransform: 'uppercase', color: INK_S,
          borderBottom: `2px solid ${BORDER}`, paddingBottom: 14, opacity: t,
          marginBottom: portrait ? 18 : 22,
        }}>
          <div>method</div>
          <div>owner</div>
          {!portrait && <div>how the sheet says it</div>}
        </div>

        {/* Rows — flex:1 spreads across the entire remaining vertical space */}
        <div style={{ flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
          {METHODS.map((m, i) => {
            const isHuman = m.who === 'human';
            return (
              <div key={m.name} style={{
                display: 'grid',
                gridTemplateColumns: portrait ? '1fr 160px' : '460px 220px 1fr',
                gap: portrait ? 18 : 44, alignItems: 'center',
                opacity: rowIn(i), transform: `translateX(${(1 - rowIn(i)) * -12}px)`,
                borderBottom: i === METHODS.length - 1 ? 'none' : `1px solid ${BORDER}`,
                paddingBottom: portrait ? 14 : 18,
              }}>
                <div style={{
                  fontFamily: MONO, fontSize: namePx,
                  color: isHuman ? ACC : INK, lineHeight: 1.05,
                }}>{m.name}</div>
                <div style={{
                  display: 'inline-block',
                  padding: portrait ? '10px 18px' : '12px 22px', borderRadius: 999,
                  background: isHuman ? '#F7DACD' : PILL,
                  color: isHuman ? '#8B3E20' : INK_S,
                  fontFamily: SANS, fontSize: chipPx, letterSpacing: '0.16em',
                  textTransform: 'uppercase', textAlign: 'center', width: 'fit-content',
                }}>{m.who}</div>
                {portrait ? (
                  <div style={{
                    gridColumn: '1 / span 2', fontFamily: SERIF, fontStyle: 'italic',
                    fontSize: notePx, color: INK_S, lineHeight: 1.35, paddingTop: 4,
                  }}>{m.note}</div>
                ) : (
                  <div style={{
                    fontFamily: SERIF, fontStyle: 'italic', fontSize: notePx, color: INK_S,
                    lineHeight: 1.35,
                  }}>{m.note}</div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ===========================================================================
// TodoAgentLoop — --method manim --open as a work queue
// ===========================================================================
export const todoAgentLoopSchema = z.object({
  spark: z.string().default('An agent walks the filter. When a beat fills, it drops off.'),
});
export type TodoAgentLoopProps = z.infer<typeof todoAgentLoopSchema>;

export const TodoAgentLoop: React.FC<TodoAgentLoopProps> = ({ spark }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const { SX, SY, portrait } = useSafe();
  const t = cl(spring({ frame, fps, config: SPRING_GENTLE }));
  const cmdIn   = cl(spring({ frame: frame - 6,   fps, config: SPRING_GENTLE }));
  const queueIn = cl(spring({ frame: frame - 30,  fps, config: SPRING_GENTLE }));
  const rendIn  = cl(spring({ frame: frame - 62,  fps, config: SPRING_GENTLE }));
  const rerunIn = cl(spring({ frame: frame - 96,  fps, config: SPRING_GENTLE }));
  const clearIn = cl(spring({ frame: frame - 130, fps, config: SPRING_GENTLE }));

  const cmdPx  = portrait ? 34 : 44;
  const cardPx = portrait ? 30 : 34;
  const arrowH = portrait ? 22 : 28;
  const cardPadY = portrait ? 14 : 18;
  const cardPadX = portrait ? 22 : 30;

  const Card = (title: string, body: React.ReactNode, opacity: number, accent = false) => (
    <div style={{
      background: CARD, border: `2px solid ${accent ? ACC : BORDER}`,
      borderRadius: 16, padding: `${cardPadY}px ${cardPadX}px`,
      boxShadow: '0 10px 32px rgba(61,57,41,0.12)', opacity,
      display: 'flex', flexDirection: 'column', gap: 4,
      transform: `translateY(${(1 - opacity) * 12}px)`,
      minWidth: portrait ? 640 : 900,
    }}>
      <div style={{ fontFamily: SANS, fontSize: portrait ? 16 : 18, letterSpacing: '0.18em', color: accent ? ACC : INK_S, textTransform: 'uppercase' }}>{title}</div>
      <div style={{ fontFamily: MONO, fontSize: cardPx, color: INK }}>{body}</div>
    </div>
  );

  const Down = (opacity: number) => (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', opacity }}>
      <div style={{ width: 4, height: arrowH, background: INK }} />
      <div style={{
        width: 0, height: 0, borderTop: `18px solid ${INK}`,
        borderLeft: '14px solid transparent', borderRight: '14px solid transparent',
      }} />
    </div>
  );

  return (
    <AbsoluteFill style={{ background: PAGE, color: INK }}>
      <SparkLine line={spark} t={t} sx={SX} sy={SY - 40} fontPx={portrait ? 30 : 36} />
      <div style={{
        position: 'absolute', left: SX, right: SX,
        top: SY + 30, bottom: SY + 20,
        display: 'flex', flexDirection: 'column', alignItems: 'center',
        justifyContent: 'space-between', overflow: 'hidden',
      }}>
        {/* Filter command bar */}
        <div style={{
          background: CODE_BG, borderRadius: 14, padding: `${cardPadY + 4}px ${cardPadX + 6}px`,
          fontFamily: MONO, fontSize: cmdPx, color: CODE_FG,
          opacity: cmdIn, transform: `translateY(${(1 - cmdIn) * 14}px)`,
          boxShadow: '0 12px 32px rgba(61,57,41,0.22)',
        }}>
          <span style={{ color: ACC }}>$ </span>./art todo &lt;reel&gt;{' '}
          <span style={{ color: ACC }}>--method manim --open</span>
        </div>
        {Down(queueIn)}
        {Card('QUEUE', (
          <div style={{ display: 'flex', gap: 18 }}>
            <span style={{ color: ACC }}>B01</span>
            <span style={{ color: INK_S }}>manim/B01.mp4</span>
          </div>
        ), queueIn)}
        {Down(rendIn)}
        {Card('RENDER + DROP', (
          <span>render_manim → save at slot</span>
        ), rendIn)}
        {Down(rerunIn)}
        {Card('RE-RUN', (
          <span><span style={{ color: ACC }}>$ </span>./art todo &lt;reel&gt; --method manim --open</span>
        ), rerunIn)}
        {Down(clearIn)}
        {Card('QUEUE', (
          <div style={{ display: 'flex', gap: 12, alignItems: 'baseline' }}>
            <span style={{ color: INK_S }}>(empty)</span>
            <span style={{ color: ACC, fontFamily: SERIF, fontStyle: 'italic', fontSize: cardPx * 0.85 }}>
              filled — drops off
            </span>
          </div>
        ), clearIn, true)}
      </div>
    </AbsoluteFill>
  );
};

// ===========================================================================
// TodoFailure — the "no beat_sheet.json" refusal and its recovery
// ===========================================================================
export const todoFailureSchema = z.object({
  spark: z.string().default('Refuses loud. No sheet, no ledger.'),
});
export type TodoFailureProps = z.infer<typeof todoFailureSchema>;

export const TodoFailure: React.FC<TodoFailureProps> = ({ spark }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const { SX, SY, portrait } = useSafe();
  const t = cl(spring({ frame, fps, config: SPRING_GENTLE }));
  const cmdIn  = cl(spring({ frame: frame - 6,  fps, config: SPRING_GENTLE }));
  const errIn  = cl(spring({ frame: frame - 30, fps, config: SPRING_GENTLE }));
  const exitIn = cl(spring({ frame: frame - 62, fps, config: SPRING_GENTLE }));
  const recIn  = cl(spring({ frame: frame - 96, fps, config: SPRING_GENTLE }));

  const cmdPx = portrait ? 36 : 52;
  const errPx = portrait ? 30 : 44;

  return (
    <AbsoluteFill style={{ background: PAGE, color: INK }}>
      <SparkLine line={spark} t={t} sx={SX} sy={SY - 40} fontPx={portrait ? 32 : 38} />

      <div style={{
        position: 'absolute', left: SX, right: SX, top: SY + 60, bottom: SY + 40,
        display: 'flex', flexDirection: 'column', justifyContent: 'center',
        gap: portrait ? 26 : 34, overflow: 'hidden',
      }}>
        {/* Terminal card */}
        <div style={{
          background: CODE_BG, borderRadius: 18, padding: portrait ? '28px 30px' : '34px 44px',
          boxShadow: '0 14px 42px rgba(61,57,41,0.22)',
          display: 'flex', flexDirection: 'column', gap: 16,
        }}>
          <div style={{ fontFamily: MONO, fontSize: cmdPx, color: CODE_FG, opacity: cmdIn }}>
            <span style={{ color: ACC }}>$ </span>./art todo demo/empty-reel
          </div>
          <div style={{
            fontFamily: MONO, fontSize: errPx, color: '#F0C4B0',
            opacity: errIn, transform: `translateX(${(1 - errIn) * -14}px)`,
          }}>
            [todo] no beat_sheet.json in .../demo/empty-reel
          </div>
          <div style={{
            display: 'inline-flex', alignSelf: 'flex-start',
            padding: '10px 20px', borderRadius: 999,
            background: ACC, color: '#FFFFFF',
            fontFamily: SANS, fontSize: 24, letterSpacing: '0.14em', textTransform: 'uppercase',
            opacity: exitIn,
          }}>exit 1 · refused</div>
        </div>

        {/* Recovery card */}
        <div style={{
          background: CARD, border: `2px solid ${BORDER}`, borderRadius: 18,
          padding: portrait ? '26px 30px' : '32px 40px',
          opacity: recIn, transform: `translateY(${(1 - recIn) * 14}px)`,
          boxShadow: '0 10px 32px rgba(61,57,41,0.10)',
          display: 'flex', flexDirection: 'column', gap: 12,
        }}>
          <div style={{ fontFamily: SANS, fontSize: 20, letterSpacing: '0.18em', color: INK_S, textTransform: 'uppercase' }}>
            RECOVERY · not a flag
          </div>
          <div style={{ fontFamily: SERIF, fontSize: portrait ? 36 : 44, color: INK, lineHeight: 1.3 }}>
            Author the sheet, or point <span style={{ fontFamily: MONO, color: ACC }}>./art todo</span> at a folder that has one.
          </div>
          <div style={{ fontFamily: SERIF, fontSize: portrait ? 24 : 28, fontStyle: 'italic', color: INK_S, lineHeight: 1.35 }}>
            The ledger refuses to guess. No hidden defaults, no scaffolding — that is a feature.
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};
