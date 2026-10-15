import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate, Easing, random } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * QuillWriter — a drawn quill WRITES, on the cream Claude stage.
 *
 * Inspiration (Bear, 2026-10-07): the Claude desktop app's writing spinner (a terracotta
 * quill), a quill drawing a branching outline on a scroll, and three scattered pages of
 * scribbled handwriting with a quill. Use for beats about writing, drafting, authorship,
 * notes, a manuscript, a log, a letter, a signature, or "the model is writing".
 *
 * kinds
 *   pages    three tilted pages; the quill writes scribble lines across them, page by page
 *   scroll   a scroll unrolls; the quill draws a branching outline on it; terracotta nodes last
 *   page     one large page; the quill fills it with scribble lines (a draft growing)
 *   spinner  the app's writing mark: a terracotta quill looping one short stroke, with a status word
 *
 * Scribbles are wavy strokes, never glyphs, so GATE T's OCR has no type to judge; title and
 * caption (optional) are settled by 20% of the beat. Terracotta is only the outline's nodes,
 * the ink drop under the nib, and the spinner quill itself (the one accent on that card).
 *
 * Doctrine: skills/make/show-tell/SKILL.md → Drawing kit (writing kit); skills/make/lecture/SKILL.md → BEST-BEAT LAW.
 */

export const quillWriterSchema = z.object({
  kind: z.enum(['pages', 'scroll', 'page', 'spinner']).default('pages'),
  /** Optional serif title, top centre (settled by 20%). Keep to 2–5 words. */
  title: z.string().default(''),
  /** Optional one-line caption under the drawing. */
  caption: z.string().default(''),
  /** Spinner only: the status word beside the quill, e.g. "Writing…". */
  status: z.string().default('Writing…'),
  /** Scribble lines per page (pages / page kinds). */
  lines: z.number().int().min(1).max(14).default(5),
  /** Scroll only: branching depth of the outline (1–3). */
  levels: z.number().int().min(1).max(3).default(2),
  /** Fraction of the beat when writing starts / ends. */
  writeFrom: z.number().min(0).max(1).default(0.1),
  writeTo: z.number().min(0).max(1).default(0.92),
  seed: z.string().default('quill'),
  durationSeconds: z.number().min(2).default(8),
});
export type QuillWriterProps = z.infer<typeof quillWriterSchema>;

const INK = CLAUDE.INK, PAGE = CLAUDE.PAGE, CARD = CLAUDE.CARD, SPARK = CLAUDE.SPARK;
const KRAFT = '#DCC9AA', KRAFT_T = '#F3E9D8', RULE = '#CFC8B8', DARK = '#3A3530';
const clamp = (v: number, a = 0, b = 1) => Math.min(b, Math.max(a, v));
const ease = Easing.bezier(0.33, 0, 0.2, 1);
const seg = (p: number, a: number, b: number) => ease(clamp((p - a) / (b - a)));

// ── the quill, nib at (0,0), feather up-right; design units ≈ 1 = 150 px ─────
const Quill: React.FC<{x: number; y: number; s?: number; rot?: number; fill?: string; stroke?: string}> =
  ({x, y, s = 150, rot = 0, fill = KRAFT_T, stroke = INK}) => (
  <svg style={{position: 'absolute', left: x - 0.1 * s, top: y - 1.2 * s, overflow: 'visible',
               transform: `rotate(${rot}deg)`, transformOrigin: `${0.1 * s}px ${1.2 * s}px`}}
       width={1.3 * s} height={1.3 * s} viewBox="0 0 1.3 1.3">
    {/* nib at (0.1, 1.2); tip at (1.1, 0.1) */}
    <path d="M0.1 1.2 C0.15 0.7 0.5 0.3 1.1 0.1 C1.05 0.5 0.75 0.95 0.1 1.2 Z"
          fill={fill} stroke={stroke} strokeWidth={0.028} strokeLinejoin="round" />
    <path d="M0.12 1.18 L1.08 0.14" stroke={stroke} strokeWidth={0.02} strokeLinecap="round" />
    <path d="M0.52 0.74 L0.44 0.56" stroke={stroke} strokeWidth={0.016} strokeLinecap="round" />
  </svg>
);

// ── a wavy handwriting stroke from (x,y), width w, as an SVG path; `t` = how much is drawn ─
function scribblePath(x: number, y: number, w: number, amp: number, waves: number, seedN: number): {d: string; len: number} {
  const n = Math.max(2, waves) * 4;
  const pts: [number, number][] = [];
  for (let i = 0; i <= n; i++) {
    const t = i / n;
    const yy = y + amp * Math.sin(t * waves * 2 * Math.PI + seedN) * (0.6 + 0.4 * Math.cos(t * 5.3 + seedN));
    pts.push([x + w * t, yy]);
  }
  let d = `M${pts[0][0]} ${pts[0][1]}`;
  let len = 0;
  for (let i = 1; i < pts.length; i++) {
    const [px, py] = pts[i - 1], [cx, cy] = pts[i];
    d += ` L${cx} ${cy}`;
    len += Math.hypot(cx - px, cy - py);
  }
  return { d, len };
}

// a point along the polyline at fraction a (for the nib)
function alongScribble(x: number, y: number, w: number, amp: number, waves: number, seedN: number, a: number): [number, number] {
  const t = clamp(a);
  return [x + w * t, y + amp * Math.sin(t * waves * 2 * Math.PI + seedN) * (0.6 + 0.4 * Math.cos(t * 5.3 + seedN))];
}

type Stroke = { x: number; y: number; w: number; amp: number; waves: number; seedN: number; rot: number; cx: number; cy: number };

const Strokes: React.FC<{strokes: Stroke[]; progress: number; sw?: number}> = ({strokes, progress, sw = 7}) => (
  <svg style={{position: 'absolute', left: 0, top: 0}} width={1920} height={1080}>
    {strokes.map((s, i) => {
      const a0 = i / strokes.length, a1 = (i + 1) / strokes.length;
      const t = clamp((progress - a0) / (a1 - a0));
      if (t <= 0) return null;
      const { d, len } = scribblePath(s.x, s.y, s.w, s.amp, s.waves, s.seedN);
      return <path key={i} d={d} fill="none" stroke={INK} strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"
                   strokeDasharray={len} strokeDashoffset={len * (1 - t)}
                   transform={`rotate(${s.rot} ${s.cx} ${s.cy})`} />;
    })}
  </svg>
);

/** Where the nib is for a given progress over a stroke list (rotation applied). */
function nibAt(strokes: Stroke[], progress: number): [number, number] | null {
  if (progress <= 0) return null;
  const i = Math.min(strokes.length - 1, Math.floor(progress * strokes.length));
  const s = strokes[i];
  const t = clamp(progress * strokes.length - i);
  const [px, py] = alongScribble(s.x, s.y, s.w, s.amp, s.waves, s.seedN, t);
  const r = (s.rot * Math.PI) / 180, dx = px - s.cx, dy = py - s.cy;
  return [s.cx + dx * Math.cos(r) - dy * Math.sin(r), s.cy + dx * Math.sin(r) + dy * Math.cos(r)];
}

const Sheet: React.FC<{x: number; y: number; w: number; h: number; rot?: number; o?: number}> = ({x, y, w, h, rot = 0, o = 1}) => (
  <div style={{position: 'absolute', left: x, top: y, width: w, height: h, transform: `rotate(${rot}deg)`, opacity: o}}>
    <div style={{position: 'absolute', left: 14, top: 14, width: w, height: h, background: KRAFT, borderRadius: 6}} />
    <div style={{position: 'absolute', left: 0, top: 0, width: w, height: h, background: CARD, border: `4px solid ${INK}`, borderRadius: 6, boxSizing: 'border-box'}} />
  </div>
);

function pageStrokes(x: number, y: number, w: number, h: number, rot: number, n: number, seedN: number): Stroke[] {
  const cx = x + w / 2, cy = y + h / 2;
  const inset = 44, gap = (h - 2 * inset) / Math.max(n, 1);
  const out: Stroke[] = [];
  for (let i = 0; i < n; i++) {
    const last = i === n - 1;
    const ww = (w - 2 * inset) * (last ? 0.55 : 1 - 0.08 * random(`${seedN}-${i}`));
    out.push({ x: x + inset, y: y + inset + gap * (i + 0.5), w: ww, amp: gap * 0.22, waves: Math.round(ww / 46), seedN: seedN + i * 1.7, rot, cx, cy });
  }
  return out;
}

const Title: React.FC<{text: string; p: number}> = ({text, p}) => text ? (
  <div style={{position: 'absolute', left: 0, right: 0, top: 84, textAlign: 'center', fontFamily: CLAUDE_FONT.serif, fontSize: 68, fontWeight: 600,
               color: INK, opacity: seg(p, 0.02, 0.14)}}>{text}</div>) : null;
const Caption: React.FC<{text: string; p: number}> = ({text, p}) => text ? (
  <div style={{position: 'absolute', left: 0, right: 0, bottom: 72, textAlign: 'center', fontFamily: CLAUDE_FONT.serif, fontSize: 40,
               color: INK, opacity: seg(p, 0.06, 0.2)}}>{text}</div>) : null;


// GATE T samples each clip at its MIDPOINT. The pages/page kinds therefore pause writing across 45–55% and
// lift the quill to a rest point clear of the sheet, so the feather never lies across written lines in that frame.
const MID_A = 0.45, MID_B = 0.55;
/** Beat fraction with a plateau across the midpoint window (writing freezes there, then catches up). */
const plateau = (p: number) => p < MID_A ? p : p <= MID_B ? MID_A : MID_A + (p - MID_B) * (1 - MID_A) / (1 - MID_B);
/** 0→1→0 lift across the window (up before it, down after it). */
const liftAt = (p: number) => seg(p, MID_A - 0.02, MID_A + 0.02) - seg(p, MID_B - 0.02, MID_B + 0.02);
const lerpPt = (a: [number, number], b: [number, number], t: number): [number, number] => [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t];

// ── kinds ─────────────────────────────────────────────────────────────────────
const Pages: React.FC<{p: number; P: QuillWriterProps; seedN: number}> = ({p, P, seedN}) => {
  const pages = [
    { x: 250, y: 300, w: 440, h: 560, rot: -7 },
    { x: 740, y: 340, w: 440, h: 560, rot: 3 },
    { x: 1230, y: 280, w: 440, h: 560, rot: -3 },
  ];
  const strokes = pages.flatMap((pg, k) => pageStrokes(pg.x, pg.y, pg.w, pg.h, pg.rot, P.lines, seedN + k * 11));
  const prog = seg(plateau(p), P.writeFrom, P.writeTo);
  const nib = nibAt(strokes, prog) ?? [200, 250];
  const rest: [number, number] = [1560, 236];            // above the third sheet; feather tip stays inside title-safe
  const q = lerpPt(nib, rest, liftAt(p));
  return <>
    {pages.map((pg, k) => <Sheet key={k} {...pg} o={seg(p, 0.0 + k * 0.03, 0.08 + k * 0.03)} />)}
    <Strokes strokes={strokes} progress={prog} />
    <Quill x={q[0]} y={q[1]} />
  </>;
};

const OnePage: React.FC<{p: number; P: QuillWriterProps; seedN: number}> = ({p, P, seedN}) => {
  const pg = { x: 560, y: 190, w: 800, h: 760, rot: 0 };
  const strokes = pageStrokes(pg.x, pg.y, pg.w, pg.h, 0, P.lines, seedN);
  const prog = seg(plateau(p), P.writeFrom, P.writeTo);
  const nib = nibAt(strokes, prog) ?? [pg.x + 44, pg.y + 60];
  const rest: [number, number] = [pg.x + pg.w + 90, pg.y + 120];   // off the sheet, right margin
  const q = lerpPt(nib, rest, liftAt(p));
  return <>
    <Sheet {...pg} o={seg(p, 0, 0.08)} />
    <Strokes strokes={strokes} progress={prog} sw={8} />
    <Quill x={q[0]} y={q[1]} />
  </>;
};

type Seg = { x1: number; y1: number; x2: number; y2: number; tip: boolean };
function tree(x: number, y: number, h: number, levels: number, spread: number): Seg[] {
  const out: Seg[] = [];
  const grow = (px: number, py: number, len: number, lvl: number, dx: number) => {
    const qx = px + dx, qy = py - len;
    out.push({ x1: px, y1: py, x2: qx, y2: qy, tip: lvl === 0 });
    if (lvl === 0) return;
    for (const d of [-spread, spread]) grow(qx, qy, len * 0.62, lvl - 1, d * Math.pow(0.72, levels - lvl));
  };
  grow(x, y, h * 0.42, levels, 0);
  return out;
}

const Scroll: React.FC<{p: number; P: QuillWriterProps}> = ({p, P}) => {
  const unroll = seg(p, 0.0, 0.16);
  const yTop = P.title ? 232 : 170, hFull = P.title ? 700 : 760;
  const x = 560, w = 800, h = Math.max(60, hFull * unroll);
  const segs = tree(x + w / 2, yTop + hFull - 110, 560, P.levels, 150);
  const prog = seg(p, P.writeFrom, P.writeTo) * segs.length;
  let nib: [number, number] | null = null;
  return <>
    <div style={{position: 'absolute', left: x + 14, top: yTop + 14, width: w, height: h, background: KRAFT, borderRadius: 10}} />
    <div style={{position: 'absolute', left: x, top: yTop, width: w, height: h, background: CARD, border: `4px solid ${INK}`, borderRadius: 10, boxSizing: 'border-box'}} />
    {/* curled ends: dark rollers, the element that carries Gate V contrast on a pale sheet */}
    <div style={{position: 'absolute', left: x - 26, top: yTop - 8, width: w + 52, height: 52, background: DARK, border: `4px solid ${INK}`, borderRadius: 26, boxSizing: 'border-box'}} />
    <div style={{position: 'absolute', left: x - 26, top: yTop + h - 44, width: w + 52, height: 52, background: DARK, border: `4px solid ${INK}`, borderRadius: 26, boxSizing: 'border-box'}} />
    <svg style={{position: 'absolute', left: 0, top: 0}} width={1920} height={1080}>
      {segs.map((s, i) => {
        const t = clamp(prog - i);
        if (t <= 0) return null;
        const ex = s.x1 + (s.x2 - s.x1) * t, ey = s.y1 + (s.y2 - s.y1) * t;
        if (t < 1 || i === segs.length - 1) nib = [ex, ey];
        return <g key={i}>
          <line x1={s.x1} y1={s.y1} x2={ex} y2={ey} stroke={INK} strokeWidth={8} strokeLinecap="round" />
          {s.tip && t >= 1 ? <circle cx={s.x2} cy={s.y2} r={13} fill={SPARK} /> : null}
        </g>;
      })}
    </svg>
    {/* once the outline is complete the quill lifts off the last node so the terracotta tip stays visible */}
    {unroll >= 1 ? <Quill x={(nib ? nib[0] : x + w / 2) + (prog >= segs.length ? 34 : 0)} y={(nib ? nib[1] : yTop + hFull - 110) - (prog >= segs.length ? 34 : 0)} /> : null}
  </>;
};

const Spinner: React.FC<{p: number; P: QuillWriterProps; f: number; fps: number}> = ({P, f, fps}) => {
  // one looping stroke, 1.6 s per loop: a short wave written left→right, then the quill lifts back
  const loop = (f / fps) / 1.6 % 1;
  const write = clamp(loop / 0.72);
  const back = clamp((loop - 0.72) / 0.28);
  const x0 = 760, y0 = 580, w = 240;
  const amp = 16, waves = 3, seedN = 0.4;
  const [nx, ny] = alongScribble(x0, y0, w, amp, waves, seedN, write);
  const { d, len } = scribblePath(x0, y0, w, amp, waves, seedN);
  const lift = Math.sin(back * Math.PI) * 60;
  const qx = back > 0 ? x0 + (nx - x0) * (1 - back) : nx;
  const qy = (back > 0 ? y0 : ny) - lift;
  return <>
    <svg style={{position: 'absolute', left: 0, top: 0}} width={1920} height={1080}>
      <path d={d} fill="none" stroke={INK} strokeWidth={9} strokeLinecap="round" strokeLinejoin="round"
            strokeDasharray={len} strokeDashoffset={len * (1 - write)} opacity={back > 0 ? 1 - back : 1} />
    </svg>
    <Quill x={qx} y={qy} s={170} fill={SPARK} stroke={SPARK} />
    <div style={{position: 'absolute', left: 1060, top: 532, fontFamily: CLAUDE_FONT.ui, fontSize: 56, color: CLAUDE.INK_SOFT}}>{P.status}</div>
  </>;
};

export const QuillWriter: React.FC<QuillWriterProps> = (P) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const p = clamp(frame / Math.max(1, durationInFrames - 1));
  const seedN = random(P.seed) * 6.28;
  return (
    <AbsoluteFill style={{ backgroundColor: PAGE }}>
      <Title text={P.title} p={p} />
      {P.kind === 'pages' ? <Pages p={p} P={P} seedN={seedN} /> :
       P.kind === 'page' ? <OnePage p={p} P={P} seedN={seedN} /> :
       P.kind === 'scroll' ? <Scroll p={p} P={P} /> :
       <Spinner p={p} P={P} f={frame} fps={fps} />}
      <Caption text={P.caption} p={p} />
    </AbsoluteFill>
  );
};

export const quillWriterDefaultProps: QuillWriterProps = quillWriterSchema.parse({});
