import React from 'react';
import {AbsoluteFill, Img, OffthreadVideo, staticFile, useCurrentFrame, useVideoConfig, interpolate, Easing} from 'remotion';
import {z} from 'zod';
import {CLAUDE_FONT} from '../tokens/claude';

/**
 * ShaderLab: shader code and its REAL result, together. The result is a video (or still) captured from the Godot Shader Lab or the Godot editor,
 * shown in a framed window on the Claude stage; the tool inside the window keeps its own look (SHOW-THE-THING). Built 2026-10-14 in the Godot
 * Shaders pilot build (spec: books/csye-7270-building-virtual-environments/youtube/_godot-shaders-series/COMPONENT-SPECS.md).
 *
 * layout   'side'  code left, result right | 'stack' result above, short excerpt below | 'video' result only | 'code' code only
 * code     the real .gdshader / GDScript text (14 lines at most), monospace with line numbers
 * cues     {at: 0..1, lines: number[], label?: string}: the line(s) highlighted from `at` on; a cue may target a blank line; `label` (<= 60 chars)
 *          is a definition tag drawn ON the highlighted line (ink on pale ground, never terracotta text)
 * video    staticFile path of the capture (MP4 or PNG/JPG for a still)       videoAspect  width / height of the capture (default 16/9)
 * readouts {at, text, x, y}: short value labels on the result; the same (x, y) REPLACES the earlier one
 * rings    {at, box: [x0, y0, x1, y1]}: one terracotta ring (grey backing) around a part of the result, fractions of the window
 * ramp     {at, from, to, seconds?, period?, sine?: {omega, t0?}}: a thin 0 to 1 strip of separate tiles under the result with a terracotta marker.
 *          Linear by default; `period` repeats it; `sine` makes the marker follow 0.5 + 0.5 sin(omega (t - t0)) (the pulse of a TIME shader)
 * Rules: type floors at 4K (design 1920x1080, rendered at scale 2); the capture is never cropped past its window; terracotta is never text.
 */
export const shaderLabSchema = z.object({
  title: z.string().default(''),
  layout: z.enum(['side', 'stack', 'video', 'code']).default('side'),
  code: z.string().default(''),
  codeFile: z.string().default(''),
  cues: z.array(z.object({at: z.number().min(0).max(1), lines: z.array(z.number()), label: z.string().max(60).optional()})).default([]),
  video: z.string().default(''),
  videoLabel: z.string().default(''),
  videoAspect: z.number().default(16 / 9),
  readouts: z.array(z.object({at: z.number(), text: z.string(), x: z.number(), y: z.number()})).default([]),
  rings: z.array(z.object({at: z.number(), box: z.array(z.number()).length(4)})).default([]),
  ramp: z.object({at: z.number(), from: z.number(), to: z.number(), seconds: z.number().optional(), period: z.number().optional(),
    sine: z.object({omega: z.number(), t0: z.number().default(0)}).optional()}).optional(),
  caption: z.string().default(''),
  durationSeconds: z.number().default(10),
});
type P = z.infer<typeof shaderLabSchema>;

const INK = '#3D3929', GREY = '#8B8F96', MUTE = '#5D584F', STAGE = '#F2F0E9', CARD = '#FFFEFB', HILITE = '#E6D3C2', SPARKDEEP = '#A64A24', SPARK = '#D97757';
const MONO = CLAUDE_FONT.mono, SERIF = CLAUDE_FONT.serif;
const CODE_FS = 32, LINE_H = 48, PAD_X = 22, NUM_W = 68;
const isStill = (p: string) => /\.(png|jpe?g|webp)$/i.test(p);

const ease = (x: number) => Easing.bezier(0.2, 0.7, 0.2, 1)(Math.min(1, Math.max(0, x)));

export const ShaderLab: React.FC<P> = (p) => {
  const frame = useCurrentFrame();
  const {fps, durationInFrames} = useVideoConfig();
  const t = frame / durationInFrames;           // fraction of the beat
  const sec = frame / fps;                      // seconds into the beat
  const lines = p.code ? p.code.split('\n') : [];
  const hasCode = lines.length > 0 && (p.layout === 'side' || p.layout === 'stack' || p.layout === 'code');
  const hasVideo = !!p.video && p.layout !== 'code';

  // the active cue: the last one whose time has come
  let active: {at: number; lines: number[]; label?: string} | null = null;
  for (const c of p.cues) if (t >= c.at) active = c;
  const activeSet = new Set<number>(active ? active.lines : []);

  // ---- geometry (design px; the render is scaled x2)
  const top = p.title ? 150 : 70;
  const bottom = 1020;
  const zoneH = bottom - top;
  // long lines wrap (never clip): characters per row from the card width at the code font size
  const cardW0 = p.layout === 'code' ? 1280 : p.layout === 'stack' ? 1100 : 736;
  const buildRows = (fsz: number) => {
    const perRow = Math.max(20, Math.floor((cardW0 - NUM_W - PAD_X - 24) / (0.602 * fsz)));
    const out: {no: number; text: string; first: boolean}[] = [];
    lines.slice(0, 14).forEach((ln, i) => {
      const txt = ln.replace(/\t/g, '    ');
      if (txt.length <= perRow) out.push({no: i + 1, text: txt, first: true});
      else {
        let rest = txt, first = true;
        while (rest.length > 0) {
          const room = first ? perRow : perRow - 6;
          let cut = rest.length;
          if (rest.length > room) {
            cut = room;
            for (let j = room; j > room * 0.5; j--) { if (' ,.(/'.includes(rest[j - 1])) { cut = j; break; } }
          }
          out.push({no: i + 1, text: (first ? '' : '      ') + rest.slice(0, cut), first});
          rest = rest.slice(cut).replace(/^ +/, ''); first = false;
        }
      }
    });
    return out;
  };
  // code that would wrap past 18 rows is set a little smaller (27 px, 42 px rows) so no line is ever clipped
  let fsBase = p.layout === 'code' ? 36 : CODE_FS;
  let LH = LINE_H;
  let rows = buildRows(fsBase);
  if (p.layout !== 'code' && rows.length > 18) { fsBase = 27; LH = 42; rows = buildRows(fsBase); }
  const codeH = Math.min(rows.length, LH === 42 ? 21 : 18) * LH + 36;

  let codeBox = {left: 112, top, width: 736, height: codeH};
  let winW = 928;
  let winLeft = 884, winTop = top;
  if (p.layout === 'side') {
    // a squarer capture gets a squarer window: never taller than 640 px, centred in the result column
    const col0 = winLeft, colW = winW;
    winW = Math.min(colW, 640 * p.videoAspect);
    winLeft = col0 + (colW - winW) / 2;
    const winH0 = winW / p.videoAspect;
    // result column: label line (34) + window + ramp (70) + caption (44)
    const colH = 34 + winH0 + (p.ramp ? 70 : 0) + (p.caption ? 44 : 0);
    winTop = top + Math.max(34, (zoneH - colH) / 2 + 34);
    codeBox = {left: 112, top: top + Math.max(0, (zoneH - codeH) / 2 - 20), width: 736, height: codeH};
  } else if (p.layout === 'stack') {
    const excerptH = Math.min(rows.length, 4) * LH + 36;
    const winH = Math.min(520, zoneH - excerptH - (p.ramp ? 70 : 0) - (p.caption ? 44 : 0) - 34 - 40);
    winW = Math.min(1500, winH * p.videoAspect);
    winLeft = (1920 - winW) / 2;
    winTop = top + 34;
    codeBox = {left: Math.max(80, (1920 - 1100) / 2), top: winTop + winH + (p.ramp ? 70 : 0) + (p.caption ? 44 : 0) + 24, width: 1100, height: excerptH};
  } else if (p.layout === 'video') {
    const maxH = zoneH - 34 - (p.ramp ? 70 : 0) - (p.caption ? 50 : 0) - 10;
    winW = Math.min(1560, maxH * p.videoAspect);
    winLeft = (1920 - winW) / 2;
    winTop = top + 34;
  } else {
    codeBox = {left: Math.max(80, (1920 - 1280) / 2), top: top + Math.max(0, (zoneH - (Math.min(rows.length, 14) * 52 + 36)) / 2), width: 1280, height: Math.min(rows.length, 14) * 52 + 36};
  }
  const winH = winW / p.videoAspect;
  const lineH = p.layout === 'code' ? 52 : LH;
  const fs = fsBase;

  // ---- readouts: the latest per (x, y) that has started
  const shown = new Map<string, {text: string; at: number; x: number; y: number}>();
  for (const r of [...p.readouts].sort((a, b) => a.at - b.at)) if (t >= r.at) shown.set(`${r.x},${r.y}`, r);
  // ---- ring: the latest started
  let ring: {at: number; box: number[]} | null = null;
  for (const r of p.rings) if (t >= r.at) ring = r;

  // ---- ramp marker value
  let rampV = -1;
  if (p.ramp && t >= p.ramp.at) {
    const dt = sec - p.ramp.at * (durationInFrames / fps);
    if (p.ramp.sine) rampV = 0.5 + 0.5 * Math.sin(p.ramp.sine.omega * (sec - p.ramp.sine.t0));
    else {
      const len = p.ramp.seconds ?? 2.4;
      const ph = p.ramp.period ? (dt % p.ramp.period) / p.ramp.period : Math.min(1, dt / len);
      rampV = p.ramp.from + (p.ramp.to - p.ramp.from) * ph;
    }
  }

  const media = hasVideo ? (isStill(p.video)
    ? <Img src={staticFile(p.video)} style={{width: '100%', height: '100%', objectFit: 'contain', display: 'block'}} />
    : <OffthreadVideo src={staticFile(p.video)} muted style={{width: '100%', height: '100%', objectFit: 'contain', display: 'block'}} />) : null;

  const shownRows = p.layout === 'stack' ? rows.slice(0, 4) : rows;   // the stack excerpt shows whole rows only
  const codeCard = hasCode ? (
    <div style={{position: 'absolute', left: codeBox.left, top: codeBox.top, width: codeBox.width, height: codeBox.height, background: CARD,
      border: `3px solid ${GREY}`, borderRadius: 16, boxSizing: 'border-box', padding: '18px 0', overflow: 'hidden'}}>
      {shownRows.map((row, i) => {
        const line = row.text;
        const on = activeSet.has(row.no);
        // ONE tag per cue, on the last highlighted row, and only where it fits to the right of that row's code; otherwise it is drawn below the card
        const lastOn = active ? Math.max(...shownRows.map((r, k) => (activeSet.has(r.no) ? k : -1))) : -1;
        const tagW = active && active.label ? active.label.length * 14.5 + 60 : 0;
        const tagFits = i === lastOn && tagW > 0 && NUM_W + 7 + line.length * 0.602 * fs + 24 + tagW <= codeBox.width - 10;
        const label = tagFits ? (active as {label?: string}).label : '';
        return <div key={i} style={{position: 'relative', display: 'flex', height: lineH, alignItems: 'center', fontFamily: MONO, fontSize: fs,
          background: on ? HILITE : 'transparent', borderLeft: `7px solid ${on ? SPARKDEEP : 'transparent'}`, paddingRight: PAD_X}}>
          <span style={{width: NUM_W, flexShrink: 0, textAlign: 'right', paddingRight: 18, color: MUTE}}>{row.first ? row.no : ''}</span>
          <span style={{whiteSpace: 'pre', color: INK}}>{line || ' '}</span>
          {label ? <span style={{position: 'absolute', right: 10, top: 2, bottom: 2, display: 'flex', alignItems: 'center', background: '#FFFFFF', border: `2px solid ${GREY}`,
            borderRadius: 12, padding: '0 14px', fontFamily: SERIF, fontSize: 28, color: INK, whiteSpace: 'nowrap'}}>{label}</span> : null}
        </div>;
      })}
    </div>
  ) : null;

  const belowTag = (() => {
    if (!hasCode || !active || !active.label) return null;
    const lastOn = Math.max(...shownRows.map((r, k) => (activeSet.has(r.no) ? k : -1)));
    if (lastOn < 0) return null;
    const tagW = active.label.length * 14.5 + 60;
    const fits = NUM_W + 7 + shownRows[lastOn].text.length * 0.602 * fs + 24 + tagW <= codeBox.width - 10;
    if (fits) return null;
    return <div style={{position: 'absolute', left: codeBox.left, top: codeBox.top + codeBox.height + (p.codeFile ? 50 : 14), display: 'flex', alignItems: 'center', background: '#FFFFFF',
      border: `2px solid ${GREY}`, borderRadius: 12, padding: '6px 14px', fontFamily: SERIF, fontSize: 28, color: INK, whiteSpace: 'nowrap', maxWidth: codeBox.width}}>{active.label}</div>;
  })();

  const winBox = hasVideo ? (
    <>
      {p.videoLabel ? <div style={{position: 'absolute', left: Math.min(winLeft, 884), bottom: 1080 - (winTop - 10), width: p.layout === 'side' ? Math.max(winW, 928) : Math.max(winW, Math.min(1500, 1824 - winLeft)), fontFamily: SERIF, fontSize: 32, lineHeight: 1.15, color: MUTE}}>{p.videoLabel}</div> : null}
      <div style={{position: 'absolute', left: winLeft, top: winTop, width: winW, height: winH, border: `4px solid ${GREY}`, borderRadius: 12, boxSizing: 'content-box',
        marginLeft: -4, marginTop: -4, background: '#D9D5CA', overflow: 'hidden'}}>{media}</div>
      {/* ring: terracotta over a grey backing */}
      {ring ? (() => {
        const k = ease((t - ring.at) / 0.05);
        const [x0, y0, x1, y1] = ring.box;
        const style = (extra: React.CSSProperties): React.CSSProperties => ({position: 'absolute', left: winLeft + x0 * winW - 10, top: winTop + y0 * winH - 10,
          width: (x1 - x0) * winW + 20, height: (y1 - y0) * winH + 20, borderRadius: 22, boxSizing: 'border-box', opacity: k, ...extra});
        return <>
          <div style={style({border: `16px solid rgba(139,143,150,0.55)`})} />
          <div style={style({border: `8px solid ${SPARK}`, left: winLeft + x0 * winW - 6, top: winTop + y0 * winH - 6, width: (x1 - x0) * winW + 12, height: (y1 - y0) * winH + 12})} />
        </>;
      })() : null}
      {/* readouts */}
      {[...shown.values()].map((r, i) => {
        const k = ease((t - r.at) / 0.04);
        const halfW = (r.text.length * 17 + 56) / 2 + 6;           // estimated half width of the pill: keep it inside the window
        const cx = Math.min(winW - halfW, Math.max(halfW, r.x * winW));
        return <div key={i} style={{position: 'absolute', left: winLeft + cx, top: winTop + r.y * winH, transform: `translate(-50%, -50%) scale(${0.9 + 0.1 * k})`,
          opacity: k, background: 'rgba(255,255,255,0.96)', border: `3px solid ${GREY}`, borderRadius: 999, padding: '4px 22px', fontFamily: SERIF, fontSize: 32, color: INK, whiteSpace: 'nowrap'}}>{r.text}</div>;
      })}
      {/* ramp: separate narrow tiles with gaps (never one continuous dark strip) */}
      {p.ramp ? (() => {
        const n = 56, y = winTop + winH + 22, tw = winW / n;
        return <>
          {Array.from({length: n}).map((_, i) => {
            const v = i / (n - 1);
            const c0 = [217, 212, 199], c1 = [95, 163, 145];
            const col = `rgb(${Math.round(c0[0] + (c1[0] - c0[0]) * v)},${Math.round(c0[1] + (c1[1] - c0[1]) * v)},${Math.round(c0[2] + (c1[2] - c0[2]) * v)})`;
            return <div key={i} style={{position: 'absolute', left: winLeft + i * tw + 1, top: y, width: tw - 2, height: 18, background: col}} />;
          })}
          <div style={{position: 'absolute', left: winLeft, top: y + 24, fontFamily: SERIF, fontSize: 28, color: INK}}>0</div>
          <div style={{position: 'absolute', left: winLeft + winW - 14, top: y + 24, fontFamily: SERIF, fontSize: 28, color: INK}}>1</div>
          {rampV >= 0 ? <div style={{position: 'absolute', left: winLeft + rampV * winW - 14, top: y - 5, width: 28, height: 28, borderRadius: 14, background: SPARK, border: `3px solid ${GREY}`, boxSizing: 'border-box'}} /> : null}
        </>;
      })() : null}
      {p.caption ? <div style={{position: 'absolute', left: winLeft, top: winTop + winH + (p.ramp ? 78 : 18), width: winW, fontFamily: SERIF, fontSize: 30, color: INK}}>{p.caption}</div> : null}
    </>
  ) : null;

  return (
    <AbsoluteFill style={{background: STAGE, color: INK, fontFamily: SERIF, fontVariantNumeric: 'lining-nums'}}>
      {p.title ? <div style={{position: 'absolute', left: 112, top: 52, fontSize: 56, lineHeight: 1.1, color: INK}}>{p.title}</div> : null}
      {codeCard}
      {p.codeFile && hasCode ? <div style={{position: 'absolute', left: codeBox.left, top: codeBox.top + codeBox.height + 12, fontFamily: SERIF, fontSize: 26, color: MUTE}}>{p.codeFile}</div> : null}
      {belowTag}
      {winBox}
    </AbsoluteFill>
  );
};
