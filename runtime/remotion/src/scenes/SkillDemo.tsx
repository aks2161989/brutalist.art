import React, { useEffect, useState } from 'react';
import { AbsoluteFill, Img, Series, staticFile, useCurrentFrame, useVideoConfig, interpolate, Easing, delayRender, continueRender, Audio } from 'remotion';
import { z } from 'zod';
import { TransitionSeries, linearTiming } from '@remotion/transitions';
import { fade } from '@remotion/transitions/fade';
import { slide } from '@remotion/transitions/slide';
import { wipe } from '@remotion/transitions/wipe';
import { fitText } from '@remotion/layout-utils';
import { parseSrt, type Caption } from '@remotion/captions';
import { useWindowedAudioData, visualizeAudio } from '@remotion/media-utils';
import { CameraMotionBlur } from '@remotion/motion-blur';
import { Circle as NotateCircle, Highlight as NotateHighlight, Underline as NotateUnderline, StrikeThrough as NotateStrike, Box as NotateBox } from '@remotion/rough-notation';
import { grayscale } from '@remotion/effects/grayscale';
import { duotone } from '@remotion/effects/duotone';
import { halftone } from '@remotion/effects/halftone';
import { vignette } from '@remotion/effects/vignette';
import { roughenEdges } from '@remotion/effects/roughen-edges';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * SkillDemo — one Remotion composition per rule that the installed Remotion agent skills teach
 * (remotion-dev/skills, installed 2026-10-10). Each `kind` SHOWS the rule running in this project
 * (Remotion 4.0.534), on the cream Claude stage, labels in ink, one terracotta accent.
 *
 * kinds: frameDriven · easing · sequence · transitions · fitText · captions · audioViz · transparent · alphaSource
 * · effects · highlights · motionBlur (these three need Remotion ≥ 4.0.529 packages + `--gl=angle` for effects)
 * Built for brutalist.art/youtube/claude-liam-remotion-skills (deep-explainer). Reusable as a teaching card.
 */

export const skillDemoSchema = z.object({
  kind: z.enum(['frameDriven', 'easing', 'sequence', 'transitions', 'fitText', 'captions', 'audioViz', 'transparent', 'alphaSource', 'effects', 'highlights', 'motionBlur']).default('frameDriven'),
  /** captions: a file under public/ (an .srt). audioViz / transparent: a file under public/. */
  src: z.string().default(''),
  durationSeconds: z.number().default(10),
});
export type SkillDemoProps = z.infer<typeof skillDemoSchema>;

const INK = CLAUDE.INK, PAGE = CLAUDE.PAGE, CARD = CLAUDE.CARD, SPARK = CLAUDE.SPARK, SOFT = CLAUDE.INK_SOFT;
const KRAFT = '#DCC9AA', KRAFT_T = '#F3E9D8', GHOST = '#D9D4C7', DARK = '#3A3530', BAR = '#8B8F96';
const SERIF = CLAUDE_FONT.serif, MONO = CLAUDE_FONT.mono, UI = CLAUDE_FONT.ui;
const DEEP = '#A4412A'; // deep terracotta for thin annotation strokes: >=4.5:1 on cream
const clamp = (v: number, a = 0, b = 1) => Math.min(b, Math.max(a, v));

const Label: React.FC<{x: number; y: number; children: React.ReactNode; size?: number; mono?: boolean; color?: string; w?: number; center?: boolean}> =
  ({ x, y, children, size = 36, mono = false, color = INK, w, center }) => (
  <div style={{ position: 'absolute', left: x, top: y, width: w, textAlign: center ? 'center' : 'left', fontFamily: mono ? MONO : SERIF,
                fontSize: size, color, whiteSpace: 'nowrap', lineHeight: 1.1 }}>{children}</div>
);
const Title: React.FC<{text: string}> = ({ text }) => {
  const frame = useCurrentFrame();
  const o = clamp(interpolate(frame, [0, 10], [0, 1]));
  return <div style={{ position: 'absolute', left: 96, top: 72, fontFamily: SERIF, fontSize: 56, fontWeight: 600, color: INK, opacity: o }}>{text}</div>;
};
const Box: React.FC<{x: number; y: number; w: number; h: number; fill?: string; r?: number}> = ({ x, y, w, h, fill = CARD, r = 12 }) => (
  <div style={{ position: 'absolute', left: x, top: y, width: w, height: h, background: fill, border: `4px solid ${INK}`, borderRadius: r, boxSizing: 'border-box' }} />
);

// ── 1. frame-driven motion vs CSS transition ─────────────────────────────────
const FrameDriven: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const go = frame >= Math.round(0.15 * durationInFrames);
  const x = interpolate(frame, [0.15 * durationInFrames, 0.55 * durationInFrames], [0, 1180], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.bezier(0.16, 1, 0.3, 1) });
  return <>
    <Title text="Frame-driven motion" />
    <Label x={96} y={250} size={34} mono>{'style={{ transition: "left 2s" }}'}</Label>
    <Label x={96} y={300} size={32} color={SOFT}>CSS transition: teleports in one frame, never animates</Label>
    <div style={{ position: 'absolute', left: 96, top: 360, width: 1728, height: 6, background: GHOST }} />
    <div style={{ position: 'absolute', top: 350 - 56 + 3, left: go ? 96 + 1180 : 96, width: 112, height: 112, background: KRAFT, border: `4px solid ${INK}`,
                  borderRadius: 14, transition: 'left 2s linear', boxSizing: 'border-box' }} />
    <Label x={96} y={620} size={34} mono>{'left: interpolate(frame, [a, b], [0, 1180])'}</Label>
    <Label x={96} y={670} size={32} color={SOFT}>frame-driven: exactly where the frame says, every render</Label>
    <div style={{ position: 'absolute', left: 96, top: 730, width: 1728, height: 6, background: GHOST }} />
    <div style={{ position: 'absolute', top: 720 - 56 + 3, left: 96 + x, width: 112, height: 112, background: KRAFT, border: `4px solid ${INK}`, borderRadius: 14, boxSizing: 'border-box' }} />
    <div style={{ position: 'absolute', left: 96 + x + 44, top: 720 - 56 + 3 + 44, width: 24, height: 24, borderRadius: 12, background: SPARK }} />
    <Label x={96} y={940} size={30} mono color={SOFT}>{`frame ${frame} of ${durationInFrames} · fps ${fps}`}</Label>
  </>;
};

// ── 2. easing + perceptual scale ──────────────────────────────────────────────
const EasingDemo: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const a = 0.08 * durationInFrames, b = 0.58 * durationInFrames;
  const rows: [string, (t: number) => number][] = [
    ['linear', Easing.linear],
    ['Easing.bezier(0.16, 1, 0.3, 1)', Easing.bezier(0.16, 1, 0.3, 1)],
    ['Easing.spring({ damping: 200 })', Easing.spring({ damping: 200 } as any) as any],
  ];
  const t = clamp((frame - a) / (b - a));
  const sa = 0.62 * durationInFrames, sb = 0.95 * durationInFrames;
  const st = clamp((frame - sa) / (sb - sa));
  const lin = 0.3 + (3 - 0.3) * st;                       // linear scale 0.3 → 3
  const per = Math.exp(Math.log(0.3) + (Math.log(3) - Math.log(0.3)) * st);   // perceptual (geometric)
  return <>
    <Title text="Easing" />
    {rows.map(([name, ease], i) => {
      const y = 230 + i * 130;
      const x = 96 + 1200 * ease(t);
      return <React.Fragment key={name}>
        <Label x={96} y={y - 52} size={30} mono color={SOFT}>{name}</Label>
        <div style={{ position: 'absolute', left: 96, top: y + 30, width: 1200 + 64, height: 4, background: GHOST }} />
        <div style={{ position: 'absolute', left: x, top: y, width: 64, height: 64, borderRadius: 32, background: i === 1 ? SPARK : KRAFT, border: `4px solid ${INK}`, boxSizing: 'border-box' }} />
      </React.Fragment>;
    })}
    <Label x={96} y={640} size={34}>Scale, same numbers</Label>
    <Label x={96} y={690} size={30} mono color={SOFT}>linear</Label>
    <Label x={760} y={690} size={30} mono color={SOFT}>{"output: 'perceptual-scale'"}</Label>
    <div style={{ position: 'absolute', left: 300 - 30, top: 860 - 30, width: 60, height: 60, background: KRAFT, border: `3px solid ${INK}`, boxSizing: 'border-box', scale: `${lin}` } as any} />
    <div style={{ position: 'absolute', left: 1000 - 30, top: 860 - 30, width: 60, height: 60, background: KRAFT, border: `3px solid ${INK}`, boxSizing: 'border-box', scale: `${per}` } as any} />
    <Label x={1420} y={830} size={30} mono color={SOFT}>{`t = ${st.toFixed(2)}`}</Label>
    <Label x={1420} y={875} size={30} mono color={SOFT}>{`linear ${lin.toFixed(2)}×`}</Label>
    <Label x={1420} y={920} size={30} mono color={SOFT}>{`perceptual ${per.toFixed(2)}×`}</Label>
  </>;
};

// ── 3. Series + premount ───────────────────────────────────────────────────────
const Clip: React.FC<{label: string; fill: string}> = ({ label, fill }) => {
  const frame = useCurrentFrame();
  const o = clamp(interpolate(frame, [0, 8], [0, 1]));
  return <div style={{ position: 'absolute', left: 560, top: 230, width: 800, height: 380, background: fill, border: `4px solid ${INK}`, borderRadius: 16,
                       boxSizing: 'border-box', opacity: o, display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: SERIF, fontSize: 72, color: INK }}>{label}</div>;
};
const SequenceDemo: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const n = 3, len = Math.floor(durationInFrames / n);
  const x0 = 96, w = 1728, px = (f: number) => x0 + (w * f) / durationInFrames;
  const fills = [KRAFT_T, KRAFT, '#C7AE86'];
  return <>
    <Title text="Series and premount" />
    <div style={{ position: 'absolute', left: 520, top: 190, width: 880, height: 460, background: DARK, borderRadius: 20 }} />
    <Series>
      {['Intro', 'Main', 'Outro'].map((l, i) => (
        <Series.Sequence key={l} durationInFrames={len} premountFor={fps}><Clip label={l} fill={fills[i]} /></Series.Sequence>
      ))}
    </Series>
    <Label x={96} y={680} size={34} mono>{'<Series.Sequence durationInFrames={len} premountFor={fps}>'}</Label>
    {/* ruler */}
    <div style={{ position: 'absolute', left: x0, top: 800, width: w, height: 70, background: CARD, border: `3px solid ${INK}`, borderRadius: 8, boxSizing: 'border-box' }} />
    {[0, 1, 2].map((i) => <React.Fragment key={i}>
      {i > 0 && <div style={{ position: 'absolute', left: px(i * len - fps), top: 803, width: px(i * len) - px(i * len - fps), height: 64, background: GHOST }} />}
      <div style={{ position: 'absolute', left: px(i * len), top: 800, width: 3, height: 70, background: INK }} />
      <Label x={px(i * len) + 14} y={812} size={30} mono color={SOFT}>{['Intro', 'Main', 'Outro'][i]}</Label>
    </React.Fragment>)}
    <div style={{ position: 'absolute', left: px(frame) - 2, top: 790, width: 5, height: 92, background: SPARK }} />
    <Label x={96} y={900} size={30} color={SOFT}>grey band = premountFor one second before the cut · the clip is mounted and ready</Label>
  </>;
};

// ── 4. TransitionSeries ────────────────────────────────────────────────────────
const Scene: React.FC<{label: string; fill: string; dark?: boolean}> = ({ label, fill, dark }) => (
  <AbsoluteFill style={{ background: fill, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
    <div style={{ fontFamily: SERIF, fontSize: 120, color: dark ? CARD : INK }}>{label}</div>
  </AbsoluteFill>
);
const TransitionsDemo: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const T = 20, scene = Math.floor((durationInFrames + 2 * T) / 3);
  const kinds = ['fade()', 'slide({direction: "from-right"})', 'wipe()'];
  const cur = frame < scene - T ? 0 : frame < 2 * scene - 2 * T ? 1 : 2;
  return <>
    <Title text="TransitionSeries" />
    <div style={{ position: 'absolute', left: 520, top: 170, width: 880, height: 510, background: DARK, borderRadius: 20 }} />
    <div style={{ position: 'absolute', left: 560, top: 200, width: 800, height: 450, border: `4px solid ${INK}`, borderRadius: 16, overflow: 'hidden' }}>
      <TransitionSeries>
        <TransitionSeries.Sequence durationInFrames={scene}><Scene label="A" fill={KRAFT_T} /></TransitionSeries.Sequence>
        <TransitionSeries.Transition presentation={fade()} timing={linearTiming({ durationInFrames: T })} />
        <TransitionSeries.Sequence durationInFrames={scene}><Scene label="B" fill={KRAFT} /></TransitionSeries.Sequence>
        <TransitionSeries.Transition presentation={slide({ direction: 'from-right' })} timing={linearTiming({ durationInFrames: T })} />
        <TransitionSeries.Sequence durationInFrames={scene}><Scene label="C" fill={DARK} dark /></TransitionSeries.Sequence>
      </TransitionSeries>
    </div>
    <Label x={96} y={720} size={32} mono>{`3 scenes × ${scene} frames − 2 transitions × ${T} = ${3 * scene - 2 * T} frames`}</Label>
    <Label x={96} y={770} size={30} color={SOFT}>the overlap shortens the composition; subtract it when you size the timeline</Label>
    <Label x={96} y={860} size={34} mono>{cur === 0 ? kinds[0] : cur === 1 ? kinds[1] : kinds[2]}</Label>
    <Label x={1420} y={860} size={30} mono color={SOFT}>{`frame ${frame}`}</Label>
  </>;
};

// ── 5. fitText ─────────────────────────────────────────────────────────────────
const FitTextDemo: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const text = 'Installing Software on an HPC Cluster Without Root';
  const W = 760;
  const [size, setSize] = useState<number | null>(null);
  const [handle] = useState(() => delayRender('fonts'));
  useEffect(() => {
    document.fonts.ready.then(() => {
      const { fontSize } = fitText({ text, withinWidth: W - 48, fontFamily: 'EB Garamond', fontWeight: 600 });
      setSize(Math.min(fontSize, 96)); continueRender(handle);
    });
  }, [handle]);
  const show = frame >= Math.round(0.3 * durationInFrames);
  return <>
    <Title text="Measure before you place" />
    <Label x={96} y={200} size={30} mono color={SOFT}>{'fontSize: 72'}</Label>
    <div style={{ position: 'absolute', left: 96, top: 250, width: W, height: 300, background: CARD, border: `4px solid ${INK}`, borderRadius: 12, boxSizing: 'border-box', overflow: 'hidden', padding: 24 }}>
      <div style={{ fontFamily: SERIF, fontSize: 72, fontWeight: 600, color: INK, whiteSpace: 'nowrap', lineHeight: 1.1 }}>{text}</div>
    </div>
    <Label x={96} y={580} size={30} color={SOFT}>clipped: the box is 760 px wide, the words are not</Label>
    <Label x={1064} y={200} size={30} mono color={SOFT}>{`fitText({ withinWidth: ${W - 48} })`}</Label>
    <div style={{ position: 'absolute', left: 1064, top: 250, width: W, height: 300, background: CARD, border: `4px solid ${INK}`, borderRadius: 12, boxSizing: 'border-box', padding: 24, display: 'flex', alignItems: 'center' }}>
      {size && show ? <div style={{ fontFamily: SERIF, fontSize: size, fontWeight: 600, color: INK, whiteSpace: 'nowrap', lineHeight: 1.1 }}>{text}</div> : null}
    </div>
    <Label x={1064} y={580} size={30} color={SOFT}>{size && show ? `measured: fontSize ${size.toFixed(1)} fits` : 'measuring…'}</Label>
    {size && show ? <div style={{ position: 'absolute', left: 1064 + W - 36, top: 250 - 12, width: 28, height: 28, borderRadius: 14, background: SPARK }} /> : null}
    <Label x={96} y={760} size={34} mono>{"import { fitText, measureText } from '@remotion/layout-utils'"}</Label>
  </>;
};

// ── 6. captions from a real .srt ──────────────────────────────────────────────
const CaptionsDemo: React.FC<{src: string}> = ({ src }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const [caps, setCaps] = useState<Caption[] | null>(null);
  const [handle] = useState(() => delayRender('srt'));
  useEffect(() => {
    fetch(staticFile(src)).then((r) => r.text()).then((t) => { setCaps(parseSrt({ input: t }).captions); continueRender(handle); });
  }, [src, handle]);
  const ms = (frame / fps) * 1000;
  const cur = caps?.find((c) => ms >= c.startMs && ms < c.endMs) ?? null;
  const idx = cur && caps ? caps.indexOf(cur) : -1;
  const words = cur ? cur.text.trim().split(/\s+/) : [];
  const prog = cur ? clamp((ms - cur.startMs) / Math.max(1, cur.endMs - cur.startMs)) : 0;
  return <>
    <Title text="Captions as data" />
    <Label x={96} y={170} size={30} mono color={SOFT}>{`parseSrt({ input: await srt.text() })  ·  ${src.split('/').pop()}`}</Label>
    <div style={{ position: 'absolute', left: 96, top: 250, width: 1000, height: 560, background: DARK, borderRadius: 16, padding: 40, boxSizing: 'border-box' }}>
      <div style={{ fontFamily: SERIF, fontSize: 52, color: CARD, lineHeight: 1.25 }}>
        {words.map((w, i) => <span key={i} style={{ color: i / Math.max(1, words.length) < prog ? SPARK : CARD }}>{w} </span>)}
      </div>
    </div>
    <div style={{ position: 'absolute', left: 1130, top: 250, width: 640, height: 560, background: CARD, border: `4px solid ${INK}`, borderRadius: 16, padding: 28, boxSizing: 'border-box', fontFamily: MONO, fontSize: 26, color: INK, lineHeight: 1.4, whiteSpace: 'pre', overflow: 'hidden' }}>
      {cur ? `{\n  "text": ${JSON.stringify(cur.text.trim().slice(0, 20) + (cur.text.trim().length > 20 ? '…' : ''))},\n  "startMs": ${cur.startMs},\n  "endMs": ${cur.endMs},\n  "timestampMs": ${cur.timestampMs ?? 'null'},\n  "confidence": null\n}` : '{ … }'}
      {caps ? `\n\ncue ${idx + 1} of ${caps.length}` : ''}
    </div>
    <Label x={96} y={860} size={30} color={SOFT}>a real caption file from the research computing series; each word lights on its own time</Label>
  </>;
};

// ── 7. audio visualization of the beat's own narration ────────────────────────
const AudioVizDemo: React.FC<{src: string}> = ({ src }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const { audioData, dataOffsetInSeconds } = useWindowedAudioData({ src: staticFile(src), frame, fps, windowInSeconds: 10 });
  const bars = audioData ? visualizeAudio({ fps, frame, audioData, numberOfSamples: 64, optimizeFor: 'speed', dataOffsetInSeconds }) : new Array(64).fill(0);
  return <>
    <Title text="Audio visualization" />
    <Label x={96} y={170} size={30} mono color={SOFT}>{"useWindowedAudioData({ src, frame, fps })  →  visualizeAudio({ numberOfSamples: 64 })"}</Label>
    <div style={{ position: 'absolute', left: 96, top: 300, width: 1728, height: 520, display: 'flex', alignItems: 'flex-end', gap: 6 }}>
      {bars.map((v, i) => <div key={i} style={{ flex: 1, height: `${clamp(v * 1.6) * 100}%`, background: i < 8 ? SPARK : INK, borderRadius: 4, minHeight: 6 }} />)}
    </div>
    <div style={{ position: 'absolute', left: 96, top: 826, width: 1728, height: 4, background: GHOST }} />
    <Label x={96} y={880} size={30} color={SOFT}>these bars are this narration, analysed as it plays · bass left, treble right</Label>
  </>;
};

// ── 8. a transparent still on a checkerboard ─────────────────────────────────
const TransparentDemo: React.FC<{src: string}> = ({ src }) => {
  const frame = useCurrentFrame();
  const o = clamp(interpolate(frame, [12, 30], [0, 1]));
  const checker = `repeating-conic-gradient(${DARK} 0% 25%, ${BAR} 0% 50%) 0 0 / 80px 80px`;
  return <>
    <Title text="Transparent output" />
    <div style={{ position: 'absolute', left: 96, top: 200, width: 1728, height: 660, background: checker, border: `4px solid ${INK}`, borderRadius: 16, boxSizing: 'border-box', overflow: 'hidden' }}>
      {src ? <Img src={staticFile(src)} style={{ position: 'absolute', left: 1728 / 2 - 330, top: 20, width: 660, height: 620, objectFit: 'contain', opacity: o }} /> : null}
    </div>
    <Label x={96} y={900} size={30} mono color={SOFT}>{'--image-format=png --pixel-format=yuva444p10le --codec=prores --prores-profile=4444'}</Label>
  </>;
};

// ── the alpha source: a quill on nothing, rendered once with `npx remotion still` ──
const AlphaSource: React.FC = () => (
  <AbsoluteFill style={{ background: 'transparent' }}>
    <svg style={{ position: 'absolute', left: 300, top: 60, overflow: 'visible' }} width={1300} height={1000} viewBox="0 0 1.3 1.3">
      <path d="M0.1 1.2 C0.15 0.7 0.5 0.3 1.1 0.1 C1.05 0.5 0.75 0.95 0.1 1.2 Z" fill={KRAFT_T} stroke={INK} strokeWidth={0.028} strokeLinejoin="round" />
      <path d="M0.12 1.18 L1.08 0.14" stroke={INK} strokeWidth={0.02} strokeLinecap="round" />
      <path d="M0.52 0.74 L0.44 0.56" stroke={INK} strokeWidth={0.016} strokeLinecap="round" />
      <circle cx={0.1} cy={1.2} r={0.035} fill={SPARK} />
    </svg>
  </AbsoluteFill>
);


// ── 10. @remotion/effects on a real Professor Bear portrait (WebGL2) ──────────
const EffectsDemo: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const t = clamp(interpolate(frame, [8, durationInFrames - 20], [0, 1]));
  // a portrait with no writing in it (the chalkboard shots read as small text to GATE T); still one of his 16x9 set
  const src = staticFile('professor-bear/professor-bear-16x9-06.jpg');
  const W = 840, H = 360;
  const cells = [
    { x: 96,  y: 150, code: 'grayscale({ amount })', fx: [grayscale({ amount: t })] },
    { x: 984, y: 150, code: 'duotone({ darkColor })', fx: [duotone({ darkColor: INK, lightColor: KRAFT_T, threshold: 0.4 })] },
    { x: 96,  y: 590, code: 'halftone({ dotSize })', fx: [halftone({ dotSize: Math.round(8 + 22 * t), dotSpacing: Math.round(8 + 22 * t), dotColor: SPARK })] },
    { x: 984, y: 590, code: 'vignette() + roughenEdges()', fx: [vignette({ amount: 0.35 + 0.5 * t }), roughenEdges({ border: 8 + 40 * t })] },
  ];
  return <>
    <Title text="Effects: one line on an image" />
    {cells.map((c, i) => <React.Fragment key={i}>
      <div style={{ position: 'absolute', left: c.x, top: c.y, width: W, height: H, border: `4px solid ${INK}`, borderRadius: 14, overflow: 'hidden', background: DARK, boxSizing: 'border-box' }}>
        <Img src={src} style={{ width: W - 8, height: H - 8, objectFit: 'cover' }} effects={c.fx} />
      </div>
      <Label x={c.x} y={c.y + H + 10} size={50} mono>{c.code}</Label>
    </React.Fragment>)}
  </>;
};

// ── 11. @remotion/rough-notation: hand-drawn highlights driven by the frame ───
const HighlightsDemo: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const at = (k: number) => clamp(interpolate(frame, [10 + k * 0.17 * durationInFrames, 10 + k * 0.17 * durationInFrames + 28], [0, 1]));
  const row = (y: number, code: string, node: React.ReactNode) => <>
    <div style={{ position: 'absolute', left: 96, top: y, fontFamily: SERIF, fontSize: 64, color: INK, whiteSpace: 'nowrap' }}>{node}</div>
    <Label x={1180} y={y + 22} size={30} mono color={SOFT}>{code}</Label>
  </>;
  return <>
    <Title text="Text highlights: a component, not a drawing" />
    {row(190, '<Circle progress={…}>', <>The hand-drawn <NotateCircle color={DEEP} progress={at(0)} strokeWidth={5}>ring</NotateCircle></>)}
    {row(350, '<Highlight progress={…}>', <>Mark the <NotateHighlight color="rgba(217,119,87,0.45)" progress={at(1)}>one word</NotateHighlight> that matters</>)}
    {row(510, '<Underline progress={…}>', <>Underline the <NotateUnderline color={INK} progress={at(2)} strokeWidth={5}>claim</NotateUnderline></>)}
    {row(670, '<StrikeThrough progress={…}>', <>Cross out the <NotateStrike color={DEEP} progress={at(3)} strokeWidth={5}>guess</NotateStrike></>)}
    {row(830, '<Box progress={…}>', <>Box the <NotateBox color={INK} progress={at(4)} strokeWidth={5}>evidence</NotateBox></>)}
  </>;
};

// ── 12. @remotion/motion-blur: the same fast move, sharp vs shutter-blurred ───
const FastCard: React.FC = () => {
  // the child must read useCurrentFrame() itself: the blur re-renders it at fractional frames
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const x = interpolate(frame, [12, 12 + 0.32 * durationInFrames], [0, 1380], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.bezier(0.7, 0, 0.2, 1) });
  return <div style={{ position: 'absolute', left: 96 + x, top: 0, width: 280, height: 190, background: KRAFT, border: `5px solid ${INK}`, borderRadius: 16, boxSizing: 'border-box',
                       fontFamily: SERIF, fontSize: 44, color: INK, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>Fast card</div>;
};
const MotionBlurDemo: React.FC = () => (
  <>
    <Title text="Motion blur: a real shutter" />
    <Label x={96} y={190} size={34} mono>no blur: every frame a hard edge</Label>
    <div style={{ position: 'absolute', left: 0, top: 250, width: 1920, height: 190 }}><FastCard /></div>
    <Label x={96} y={560} size={34} mono>{'<CameraMotionBlur shutterAngle={240} samples={12}>'}</Label>
    <div style={{ position: 'absolute', left: 0, top: 620, width: 1920, height: 190 }}>
      <CameraMotionBlur shutterAngle={240} samples={12}><FastCard /></CameraMotionBlur>
    </div>
    <Label x={96} y={900} size={30} color={SOFT}>the card is averaged over the moments the shutter is open</Label>
  </>
);

export const SkillDemo: React.FC<SkillDemoProps> = ({ kind, src }) => {
  if (kind === 'alphaSource') return <AlphaSource />;
  return (
    <AbsoluteFill style={{ backgroundColor: PAGE }}>
      {kind === 'frameDriven' ? <FrameDriven /> :
       kind === 'easing' ? <EasingDemo /> :
       kind === 'sequence' ? <SequenceDemo /> :
       kind === 'transitions' ? <TransitionsDemo /> :
       kind === 'fitText' ? <FitTextDemo /> :
       kind === 'effects' ? <EffectsDemo /> :
       kind === 'highlights' ? <HighlightsDemo /> :
       kind === 'motionBlur' ? <MotionBlurDemo /> :
       kind === 'captions' ? <CaptionsDemo src={src || 'remotion-skills/aicr-introduction.srt'} /> :
       kind === 'audioViz' ? <AudioVizDemo src={src || 'remotion-skills/narration-B26.mp3'} /> :
       <TransparentDemo src={src || 'remotion-skills/quill-alpha.png'} />}
    </AbsoluteFill>
  );
};
export const skillDemoDefaultProps: SkillDemoProps = skillDemoSchema.parse({});
