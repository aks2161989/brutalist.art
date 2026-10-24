import React from 'react';
import {AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, staticFile, useCurrentFrame, useVideoConfig, interpolate, spring} from 'remotion';
import {z} from 'zod';
import {NEU, NEU_RED, FONT_NEU} from '../tokens/neu';
import {SPRING_SMOOTH} from '../tokens/vox';
import {useLato} from '../tokens/lato';
import {SeisLogoRevealInner} from './SeisLogoReveal';

// Dark reference palette (see SeisQA). Cards default to black ground + NU red rule.
const SEIS_DARK = '#0A0A0A';
const SEIS_DIM = '#B0B0B0';

/**
 * SeisFilm — seis-composite: the alumni impact film. A timeline of items rendered back to back:
 *   card   — kinetic text on the SEIS page (section titles, the stat card, the bridge)
 *   clip   — a rendered SeisQA mp4 (or any mp4) played as is
 *   end    — the static SEIS end slide (primary logo, ~10 s)
 * Optional music bed, ducked under speech. NEU brand throughout.
 */
const item = z.object({kind: z.enum(['card', 'clip', 'end', 'logo']), frames: z.number(), src: z.string().default(''), audio: z.string().default(''), duck: z.boolean().default(false),
  eyebrow: z.string().default(''), lines: z.array(z.string()).default([]), emphasis: z.number().default(-1), dark: z.boolean().default(false),
  light: z.boolean().default(false)});   // logo only: white ground + standard lockup (SeisLogoReveal light)
export const seisFilmSchema = z.object({items: z.array(item).default([]), music: z.string().default(''), musicGain: z.number().default(0.12), musicDuck: z.number().default(0.035)});
export type SeisFilmProps = z.infer<typeof seisFilmSchema>;

const Card: React.FC<{it: z.infer<typeof item>}> = ({it}) => {
  const frame = useCurrentFrame(); const {fps, width, height} = useVideoConfig();
  const bg = it.dark ? '#000' : SEIS_DARK; const ink = '#FFFFFF';
  const out = interpolate(frame, [it.frames - 8, it.frames], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const n = Math.max(1, it.lines.length); const size = height * (n <= 2 ? 0.10 : n === 3 ? 0.08 : 0.064);
  return (
    <AbsoluteFill style={{backgroundColor: bg, opacity: out}}>
      {it.eyebrow && <div style={{position: 'absolute', left: width * 0.07, top: height * 0.20, fontFamily: FONT_NEU.display, fontSize: height * 0.024, letterSpacing: 1.5, textTransform: 'uppercase', color: SEIS_DIM, opacity: spring({frame, fps, config: SPRING_SMOOTH})}}>{it.eyebrow}</div>}
      <div style={{position: 'absolute', left: width * 0.07, top: height * 0.25, width: width * 0.12 * spring({frame, fps, config: SPRING_SMOOTH}), height: Math.max(4, height * 0.007), backgroundColor: NEU_RED}} />
      <div style={{position: 'absolute', left: width * 0.07, right: width * 0.07, top: height * 0.38, display: 'flex', flexDirection: 'column', gap: height * 0.03}}>
        {it.lines.map((ln, i) => { const s = spring({frame: frame - 6 - i * 9, fps, config: SPRING_SMOOTH});
          return <div key={i} style={{fontFamily: FONT_NEU.display, fontSize: size, lineHeight: 1.12, color: i === it.emphasis ? NEU_RED : ink, opacity: s, transform: `translateY(${(1 - s) * 18}px)`}}>{ln}</div>; })}
      </div>
      <Img src={staticFile('seis/seis-logo-knockout.png')} style={{position: 'absolute', left: width * 0.07, top: height * 0.07, height: height * 0.070}} />
    </AbsoluteFill>
  );
};
const End: React.FC = () => {
  const frame = useCurrentFrame(); const {fps, width, height} = useVideoConfig(); const s = spring({frame, fps, config: SPRING_SMOOTH});
  return (
    <AbsoluteFill style={{backgroundColor: SEIS_DARK, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center'}}>
      <Img src={staticFile('seis/seis-logo-knockout.png')} style={{height: height * 0.155, opacity: s}} />
      <div style={{width: width * 0.08, height: Math.max(4, height * 0.006), backgroundColor: NEU_RED, marginTop: height * 0.045, opacity: s}} />
      <div style={{fontFamily: FONT_NEU.display, fontSize: height * 0.036, lineHeight: 1.45, color: '#FFFFFF', marginTop: height * 0.045, opacity: s, width: width * 0.70, textAlign: 'center'}}>
        As SEIS continues to evolve, our alumni remain an enduring part of its impact — shaping industries, advancing innovation, and helping define what comes next.
      </div>
    </AbsoluteFill>
  );
};
// soft ease at both ends of every item — reads as a gentle dissolve rather than a hard cut
const Fade: React.FC<{frames: number; children: React.ReactNode}> = ({frames, children}) => {
  const f = useCurrentFrame();
  const o = Math.min(
    interpolate(f, [0, 7], [0, 1], {extrapolateRight: 'clamp'}),
    interpolate(f, [frames - 7, frames], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'})
  );
  return <AbsoluteFill style={{opacity: o}}>{children}</AbsoluteFill>;
};

export const SeisFilm: React.FC<SeisFilmProps> = ({items, music, musicGain, musicDuck}) => {
  useLato(); let t = 0;
  // Music ducks under speech (clips + narrated cards) and lifts on the silent cards.
  // Averaging the target over a +/-9 frame window turns each step into a ~0.6s ramp, so there is no click.
  const starts = React.useMemo(() => {let a = 0; return items.map((it) => {const s0 = a; a += it.frames; return s0;});}, [items]);
  const target = React.useCallback((f: number) => {
    for (let i = 0; i < items.length; i++) if (f >= starts[i] && f < starts[i] + items[i].frames) return items[i].duck ? musicDuck : musicGain;
    return musicGain;
  }, [items, starts, musicGain, musicDuck]);
  const volume = React.useCallback((f: number) => {
    let sum = 0; for (let d = -9; d <= 9; d++) sum += target(Math.max(0, f + d));
    return sum / 19;
  }, [target]);
  return (
    <AbsoluteFill style={{backgroundColor: '#000'}}>
      {music && <Audio src={staticFile(music)} volume={volume} />}
      {items.map((it, i) => { const from = t; t += it.frames;
        return <Sequence key={i} from={from} durationInFrames={it.frames}>
          {it.audio && <Audio src={staticFile(it.audio)} />}
          <Fade frames={it.frames}>
            {it.kind === 'card' ? <Card it={it} /> : it.kind === 'end' ? <End /> : it.kind === 'logo' ? <SeisLogoRevealInner light={it.light} /> : <OffthreadVideo src={staticFile(it.src)} style={{width: '100%', height: '100%'}} />}
          </Fade>
        </Sequence>; })}
    </AbsoluteFill>
  );
};
