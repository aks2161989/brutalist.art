/**
 * TrainTeacher.tsx — reel-local Remotion components for
 * claude-liam-train-the-teacher.
 *
 * Palette: cream #F2F0E9, ink #3D3929, terracotta #D97757 (ONE accent).
 * All at 1920x1080, registered in Root.tsx under the folder "TrainTeacher".
 *
 * DESIGN RULE FOR THIS SET: the motion IS the claim. Each component was built
 * because a still frame of it would lose the argument — the miss, the lag, the
 * strike, the flat needle, the shrink, the zoom-out, the emptiness. If a beat
 * here would survive as a PowerPoint slide, it is in the wrong component.
 *
 * SOURCE CARE: no component hardcodes a statistic. Every number arrives as a
 * prop from the beat sheet, so a corrected figure is a beat-sheet fix.
 */
import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate } from 'remotion';
import { z } from 'zod';

// -- Palette ------------------------------------------------------------------
const BG     = '#F2F0E9';
const INK    = '#3D3929';
const ACC    = '#D97757';
const SOFT   = '#6C6959';   // was #73705F — 4.37:1 on cream, under WCAG
const GHOST  = '#B0AD9A';
const CARD   = '#FFFFFF';
const BORDER = '#DDD9CC';
/** Terracotta that carries WORDS. Same hue, darkened to clear 4.5:1 on cream
 *  (#D97757 is 2.74:1 and fails GATE T §8.3 as text). Shapes keep ACC. */
const ACC_TEXT = '#AF4B2D';

const SERIF = '"EB Garamond", Georgia, "Times New Roman", serif';
const SANS  = '-apple-system, "SF Pro Text", "Segoe UI", sans-serif';

const SAFE = 96;
const CW   = 1920;
const CH   = 1080;

const cl = (v: number, a = 0, b = 1) => Math.min(b, Math.max(a, v));
const GENTLE = { damping: 30, stiffness: 120, mass: 0.9 };
const FIRM   = { damping: 22, stiffness: 180, mass: 0.8 };

/** Progress 0→1 across a window of the beat, expressed in normalized time. */
const win = (t: number, a: number, b: number) =>
  cl(interpolate(t, [a, b], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));

/** Spark + one short serif line. SPARK-LINE LAW on illustration beats. */
const SparkLine: React.FC<{ line: string; t: number; bottom?: boolean }> = ({ line, t, bottom }) =>
  line ? (
    <div style={{
      position: 'absolute', left: SAFE, [bottom ? 'bottom' : 'top']: SAFE - 24,
      display: 'flex', alignItems: 'baseline', gap: 14, opacity: t,
    }}>
      <span style={{ fontFamily: SERIF, fontSize: 54, color: ACC_TEXT, lineHeight: 1 }}>*</span>
      <span style={{ fontFamily: SERIF, fontSize: 54, color: SOFT, lineHeight: 1 }}>{line}</span>
    </div>
  ) : null;

/** Bottom note, fades up late. */
const Note: React.FC<{ text: string; o: number }> = ({ text, o }) =>
  text ? (
    <div style={{
      position: 'absolute', left: SAFE, right: SAFE, bottom: SAFE - 34,
      fontFamily: SERIF, fontSize: 50, color: SOFT, lineHeight: 1.28,
      opacity: o, textAlign: 'center',
    }}>{text}</div>
  ) : null;

/** Auto-fit a headline to its own length so nothing ever crops. */
const fitTitle = (s: string) => (s.length <= 30 ? 68 : s.length <= 46 ? 58 : 50);


// ===========================================================================
// TtTwoAnswers — the question holds centre; two answers drive in from the
// sides and BOTH STOP SHORT. The gap they leave is the film's thesis, and it
// only exists because they moved.
// ===========================================================================
export const ttTwoAnswersSchema = z.object({
  question: z.string().default('Technology is harming students. What do we do?'),
  left:  z.object({ name: z.string(), sub: z.string().default('') }),
  right: z.object({ name: z.string(), sub: z.string().default('') }),
  gapLabel: z.string().default('neither is about teachers'),
  note: z.string().default(''),
  spark: z.string().default(''),
});
export type TtTwoAnswersProps = z.infer<typeof ttTwoAnswersSchema>;

export const TtTwoAnswers: React.FC<TtTwoAnswersProps> = ({ question, left, right, gapLabel, note, spark }) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const t = frame / durationInFrames;

  const qIn = cl(spring({ frame, fps, config: GENTLE }));
  // Cards travel inward, then arrest — the arrest is the point.
  const driveL = cl(spring({ frame: frame - 18, fps, config: { damping: 26, stiffness: 90, mass: 1.1 } }));
  const driveR = cl(spring({ frame: frame - 26, fps, config: { damping: 26, stiffness: 90, mass: 1.1 } }));
  const gapIn  = win(t, 0.58, 0.72);
  const noteIn = win(t, 0.80, 0.92);

  const CARD_W = 520;
  const startOff = 520;        // how far off their resting mark they begin
  const restL = SAFE + 40;
  const restR = CW - SAFE - 40 - CARD_W;

  const card = (side: 'l' | 'r', d: { name: string; sub: string }, drive: number) => {
    const x = side === 'l' ? restL - (1 - drive) * startOff : restR + (1 - drive) * startOff;
    return (
      <div style={{
        position: 'absolute', top: 470, left: x, width: CARD_W,
        background: CARD, border: `2px solid ${BORDER}`, borderRadius: 4,
        padding: '30px 34px 34px', opacity: drive,
      }}>
        <div style={{ width: 84, height: 3, background: INK, opacity: 0.45, marginBottom: 20 }} />
        <div style={{ fontFamily: SERIF, fontSize: 56, color: INK, lineHeight: 1.1 }}>{d.name}</div>
        {d.sub ? (
          <div style={{ fontFamily: SERIF, fontSize: 34, color: SOFT, lineHeight: 1.32, marginTop: 16 }}>{d.sub}</div>
        ) : null}
      </div>
    );
  };

  return (
    <AbsoluteFill style={{ background: BG }}>
      <SparkLine line={spark} t={qIn} />
      <div style={{
        position: 'absolute', top: 210, left: SAFE, right: SAFE, textAlign: 'center',
        fontFamily: SERIF, fontSize: fitTitle(question), color: INK, lineHeight: 1.16,
        opacity: qIn, transform: `translateY(${(1 - qIn) * 18}px)`,
      }}>{question}</div>

      {card('l', left, driveL)}
      {card('r', right, driveR)}

      {/* The gap. A terracotta bracket closes on the empty middle. */}
      <div style={{
        position: 'absolute', top: 520, left: restL + CARD_W, width: restR - (restL + CARD_W),
        height: 240, display: 'flex', flexDirection: 'column',
        alignItems: 'center', justifyContent: 'center', gap: 18, opacity: gapIn,
      }}>
        <div style={{ width: `${gapIn * 100}%`, height: 2, background: ACC, opacity: 0.7 }} />
        <div style={{
          fontFamily: SERIF, fontSize: 40, color: ACC_TEXT, textAlign: 'center',
          lineHeight: 1.24, padding: '0 12px',
          transform: `translateY(${(1 - gapIn) * 14}px)`,
        }}>{gapLabel}</div>
        <div style={{ width: `${gapIn * 100}%`, height: 2, background: ACC, opacity: 0.7 }} />
      </div>

      <Note text={note} o={noteIn} />
    </AbsoluteFill>
  );
};


// ===========================================================================
// TtFrontLoaded — two tracks over two years. The cost track rises immediately
// and holds; the benefit track stays flat, then rises a year later. The band
// between them is the argument, and a still frame cannot show a lag.
// ===========================================================================
export const ttFrontLoadedSchema = z.object({
  title: z.string().default('Costs now. Benefits later.'),
  spanLabels: z.array(z.string()).min(2).max(4).default(['YEAR ONE', 'YEAR TWO']),
  costLabel: z.string().default('disciplinary cost'),
  benefitLabel: z.string().default('test-score benefit'),
  bandLabel: z.string().default('paid here, collected there'),
  note: z.string().default(''),
  spark: z.string().default(''),
});
export type TtFrontLoadedProps = z.infer<typeof ttFrontLoadedSchema>;

export const TtFrontLoaded: React.FC<TtFrontLoadedProps> = ({
  title, spanLabels, costLabel, benefitLabel, bandLabel, note, spark,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const t = frame / durationInFrames;
  const titleIn = cl(spring({ frame, fps, config: GENTLE }));

  const L = SAFE + 60, R = CW - SAFE - 60;
  const W = R - L;
  const mid = L + W / 2;
  const baseCost = 470;      // baseline of the upper (cost) track
  const baseBen  = 786;      // baseline of the lower (benefit) track

  // Cost climbs across the first half of the plot, then holds flat.
  const costRise = win(t, 0.16, 0.40);
  // Benefit does nothing until the second span — the lag is literal.
  const benRise  = win(t, 0.52, 0.78);
  const bandIn   = win(t, 0.62, 0.74);
  const noteIn   = win(t, 0.84, 0.94);

  const costH = costRise * 180;
  const benH  = benRise * 165;

  // Cost path: rises over the first span, holds level across the second.
  const costPath = `M ${L} ${baseCost} L ${L + (mid - L) * Math.min(1, costRise / 0.85)} ${baseCost - costH}`
    + (costRise > 0.85 ? ` L ${mid + (R - mid) * win(t, 0.40, 0.92)} ${baseCost - costH}` : '');
  const benPath = `M ${L} ${baseBen} L ${mid} ${baseBen}`
    + (benRise > 0 ? ` L ${mid + (R - mid) * benRise} ${baseBen - benH}` : '');

  return (
    <AbsoluteFill style={{ background: BG }}>
      <SparkLine line={spark} t={titleIn} />
      <div style={{
        position: 'absolute', top: 200, left: SAFE, right: SAFE, textAlign: 'center',
        fontFamily: SERIF, fontSize: fitTitle(title), color: INK, opacity: titleIn,
      }}>{title}</div>

      <svg width={CW} height={CH} style={{ position: 'absolute', inset: 0 }}>
        {/* Span divider */}
        <line x1={mid} y1={330} x2={mid} y2={861} stroke={GHOST} strokeWidth={1} strokeDasharray="6 8" />
        {/* Baselines */}
        <line x1={L} y1={baseCost} x2={R} y2={baseCost} stroke={BORDER} strokeWidth={2} />
        <line x1={L} y1={baseBen}  x2={R} y2={baseBen}  stroke={BORDER} strokeWidth={2} />

        {/* The band: cost exists, benefit does not. Drawn only across span one. */}
        {bandIn > 0 ? (
          <rect x={L} y={baseCost - costH - 8} width={(mid - L) * bandIn} height={(baseBen - (baseCost - costH)) + 8}
            fill={ACC} opacity={0.10} />
        ) : null}

        <path d={costPath} fill="none" stroke={ACC} strokeWidth={6} strokeLinecap="round" strokeLinejoin="round" />
        <path d={benPath}  fill="none" stroke={INK} strokeWidth={6} strokeLinecap="round" strokeLinejoin="round" />
      </svg>

      {/* Span labels */}
      {[L + (mid - L) / 2, mid + (R - mid) / 2].map((x, i) => (
        <div key={i} style={{
          position: 'absolute', left: x - 160, width: 320, top: 884, textAlign: 'center',
          fontFamily: SANS, fontSize: 26, letterSpacing: '0.2em', color: SOFT,
          textTransform: 'uppercase', opacity: titleIn,
        }}>{spanLabels[i] ?? ''}</div>
      ))}

      {/* Track labels ride the line ends */}
      <div style={{
        position: 'absolute', left: L, top: baseCost + 12,
        fontFamily: SERIF, fontSize: 38, color: ACC_TEXT, opacity: cl(costRise * 1.4),
      }}>{costLabel}</div>
      <div style={{
        position: 'absolute', left: L, top: baseBen + 14,
        fontFamily: SERIF, fontSize: 38, color: INK, opacity: titleIn * 0.85,
      }}>{benefitLabel}</div>

      {/* Band label sits inside the band */}
      <div style={{
        position: 'absolute', left: L + 24, top: baseBen - 118, width: (mid - L) - 48,
        fontFamily: SERIF, fontSize: 40, color: ACC_TEXT, lineHeight: 1.22, opacity: bandIn,
      }}>{bandLabel}</div>

      <Note text={note} o={noteIn} />
    </AbsoluteFill>
  );
};


// ===========================================================================
// TtCorrection — the audit workhorse. A published sentence sits on the page;
// a terracotta rule sweeps THROUGH the wrong span; the span greys out and the
// correction drops in beneath it. The sweep is the beat.
// ===========================================================================
export const ttCorrectionSchema = z.object({
  sourceLabel: z.string().default('AS PUBLISHED'),
  before: z.string().default(''),
  wrong: z.string().default('the wrong span'),
  after: z.string().default(''),
  corrected: z.string().default('what the source actually says'),
  verdict: z.string().default('CORRECTED'),
  citation: z.string().default(''),
  note: z.string().default(''),
  spark: z.string().default(''),
});
export type TtCorrectionProps = z.infer<typeof ttCorrectionSchema>;

export const TtCorrection: React.FC<TtCorrectionProps> = ({
  sourceLabel, before, wrong, after, corrected, verdict, citation, note, spark,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const t = frame / durationInFrames;

  const lineIn  = cl(spring({ frame: frame - 4, fps, config: GENTLE }));
  const sweep   = win(t, 0.34, 0.52);          // the strike travels
  const grey    = win(t, 0.44, 0.58);          // the wrong span retires
  const dropIn  = cl(spring({ frame: frame - Math.round(durationInFrames * 0.56), fps, config: FIRM }));
  const stampIn = cl(spring({ frame: frame - Math.round(durationInFrames * 0.70), fps, config: FIRM }));
  const noteIn  = win(t, 0.84, 0.94);

  // Fit the published sentence to its own length.
  const total = (before + wrong + after).length;
  const px = total <= 90 ? 62 : total <= 130 ? 54 : total <= 180 ? 47 : 41;
  const cpx = corrected.length <= 90 ? 58 : corrected.length <= 140 ? 52 : 46;
  // Estimate the sentence's wrapped height so the card follows it instead of
  // floating at a fixed offset — Gate V flagged 26-37% fill on these beats.
  const perLine  = Math.max(1, Math.floor((CW - SAFE * 2) / (px * 0.47)));
  const sentLines = Math.max(1, Math.ceil(total / perLine));
  const cardTop  = 300 + sentLines * px * 1.34 + 82;

  return (
    <AbsoluteFill style={{ background: BG }}>
      <SparkLine line={spark} t={lineIn} />

      <div style={{
        position: 'absolute', top: 226, left: SAFE, fontFamily: SANS, fontSize: 34,
        letterSpacing: '0.22em', color: SOFT, textTransform: 'uppercase', opacity: lineIn,
      }}>{sourceLabel}</div>

      {/* The published sentence, with the strike riding through it. */}
      <div style={{
        position: 'absolute', top: 300, left: SAFE, right: SAFE,
        fontFamily: SERIF, fontSize: px, color: INK, lineHeight: 1.34,
        opacity: lineIn, transform: `translateY(${(1 - lineIn) * 16}px)`,
      }}>
        <span>{before}</span>
        <span style={{
          color: grey > 0 ? GHOST : INK,
          backgroundImage: `linear-gradient(${ACC}, ${ACC})`,
          backgroundRepeat: 'no-repeat',
          backgroundSize: `${sweep * 100}% 5px`,
          backgroundPosition: '0 58%',
          boxDecorationBreak: 'clone',
          WebkitBoxDecorationBreak: 'clone',
        }}>{wrong}</span>
        <span>{after}</span>
      </div>

      {/* The correction drops in beneath, on a card. */}
      <div style={{
        position: 'absolute', left: SAFE, right: SAFE, top: cardTop,
        background: CARD, border: `2px solid ${BORDER}`, borderLeft: `6px solid ${ACC}`,
        borderRadius: 4, padding: '30px 36px 34px',
        opacity: dropIn, transform: `translateY(${(1 - dropIn) * 34}px)`,
      }}>
        <div style={{
          fontFamily: SANS, fontSize: 36, letterSpacing: '0.22em', color: ACC_TEXT,
          textTransform: 'uppercase', marginBottom: 16, opacity: stampIn,
        }}>{verdict}</div>
        <div style={{ fontFamily: SERIF, fontSize: cpx, color: INK, lineHeight: 1.3 }}>{corrected}</div>
        {citation ? (
          <div style={{ fontFamily: SANS, fontSize: 42, color: SOFT, marginTop: 18, opacity: stampIn }}>{citation}</div>
        ) : null}
      </div>

      <Note text={note} o={noteIn} />
    </AbsoluteFill>
  );
};


// ===========================================================================
// TtNullResult — two meters. One climbs. The other does not. The whole finding
// is the difference in their behaviour over time, which a slide cannot hold.
// ===========================================================================
export const ttNullResultSchema = z.object({
  title: z.string().default('What moved, and what did not'),
  inputLabel: z.string().default(''),
  // FALSE when the source reports direction only. Bars still move; no number
  // is put on screen that the source does not state.
  showValues: z.boolean().default(true),
  left:  z.object({ label: z.string(), value: z.number(), caption: z.string().default('') }),
  right: z.object({ label: z.string(), value: z.number(), caption: z.string().default('') }),
  flatLabel: z.string().default('no significant effect'),
  note: z.string().default(''),
  spark: z.string().default(''),
});
export type TtNullResultProps = z.infer<typeof ttNullResultSchema>;

export const TtNullResult: React.FC<TtNullResultProps> = ({
  title, inputLabel, showValues, left, right, flatLabel, note, spark,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const t = frame / durationInFrames;
  const titleIn = cl(spring({ frame, fps, config: GENTLE }));
  const inputIn = win(t, 0.10, 0.24);

  const climb = win(t, 0.28, 0.56);
  // The right meter is given the SAME window — so the eye watches it not move.
  const rightClimb = win(t, 0.28, 0.56);
  const flatIn = win(t, 0.62, 0.76);
  const noteIn = win(t, 0.84, 0.94);

  const TRACK_H = 330;
  const top = 372;
  const base = top + TRACK_H;

  const meter = (x: number, d: { label: string; value: number; caption: string }, p: number, accent: boolean) => {
    const h = TRACK_H * cl(d.value / 100) * p;
    return (
      <div key={d.label} style={{ position: 'absolute', left: x, top, width: 300 }}>
        <div style={{ position: 'absolute', left: 0, top: 0, width: 300, height: TRACK_H, border: `2px solid ${BORDER}`, background: CARD }} />
        <div style={{
          position: 'absolute', left: 0, top: TRACK_H - h, width: 300, height: h,
          background: accent ? ACC_TEXT : INK, opacity: accent ? 0.9 : 0.82,
        }} />
        {/* the reading rides the top of the fill */}
        <div style={{
          position: 'absolute', left: 318, top: TRACK_H - h - 30, width: 300,
          fontFamily: SERIF, fontSize: 52, color: accent ? ACC : INK, opacity: p,
        }}>{showValues ? (d.value > 0 ? `+${d.value}` : '0') : ''}</div>
        <div style={{ position: 'absolute', left: 0, top: TRACK_H + 26, width: 390 }}>
          <div style={{ fontFamily: SERIF, fontSize: 36, color: INK, lineHeight: 1.18 }}>{d.label}</div>
          {d.caption ? (
            <div style={{
              fontFamily: SERIF, fontSize: 28, color: SOFT, lineHeight: 1.26, marginTop: 10,
            }}>{d.caption}</div>
          ) : null}
        </div>
      </div>
    );
  };

  return (
    <AbsoluteFill style={{ background: BG }}>
      <SparkLine line={spark} t={titleIn} />
      <div style={{
        position: 'absolute', top: 200, left: SAFE, right: SAFE, textAlign: 'center',
        fontFamily: SERIF, fontSize: fitTitle(title), color: INK, opacity: titleIn,
      }}>{title}</div>

      {inputLabel ? (
        <div style={{
          position: 'absolute', top: 300, left: SAFE, right: SAFE, textAlign: 'center',
          fontFamily: SANS, fontSize: 28, letterSpacing: '0.18em', color: SOFT,
          textTransform: 'uppercase', opacity: inputIn,
        }}>{inputLabel}</div>
      ) : null}

      {meter(430, left, climb, false)}
      {meter(1130, right, rightClimb, true)}

      {/* The flat line drawn across the right meter's zero. */}
      <svg width={CW} height={CH} style={{ position: 'absolute', inset: 0, pointerEvents: 'none' }}>
        <line x1={1130} y1={base} x2={1130 + 300 * flatIn} y2={base} stroke={ACC_TEXT} strokeWidth={5} />
      </svg>
      <div style={{
        position: 'absolute', left: 1454, top: base - 30, width: 370,
        fontFamily: SERIF, fontSize: 36, color: ACC_TEXT, lineHeight: 1.2, opacity: flatIn,
      }}>{flatLabel}</div>

      <Note text={note} o={noteIn} />
    </AbsoluteFill>
  );
};


// ===========================================================================
// TtScaleDecay — one bar, three stops. As the programme's scale counter climbs,
// the effect bar SHRINKS in place. Attenuation is a movement, not a number.
// ===========================================================================
export const ttScaleDecaySchema = z.object({
  title: z.string().default('What happens when it scales'),
  unit: z.string().default('SD'),
  // FALSE when the source documents the direction of attenuation but not a
  // pooled magnitude. The bar still shrinks; no number is asserted.
  showValue: z.boolean().default(true),
  qualitative: z.array(z.string()).default([]),
  stops: z.array(z.object({
    scaleLabel: z.string(),
    effect: z.number(),
    caption: z.string().default(''),
  })).min(2).max(4),
  note: z.string().default(''),
  spark: z.string().default(''),
});
export type TtScaleDecayProps = z.infer<typeof ttScaleDecaySchema>;

export const TtScaleDecay: React.FC<TtScaleDecayProps> = ({ title, unit, showValue, qualitative, stops, note, spark }) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const t = frame / durationInFrames;
  const titleIn = cl(spring({ frame, fps, config: GENTLE }));
  const noteIn  = win(t, 0.86, 0.95);

  // Walk the stops across the middle 70% of the beat.
  const START = 0.14, END = 0.84;
  const n = stops.length;
  const pos = cl((t - START) / (END - START)) * (n - 1);
  const i = Math.min(n - 2, Math.floor(pos));
  const f = cl(pos - i);
  const cur = stops[i], nxt = stops[Math.min(n - 1, i + 1)];
  const eff = cur.effect + (nxt.effect - cur.effect) * f;

  const maxEff = Math.max(...stops.map((s) => s.effect)) || 1;
  const BAR_MAX = 430;
  const base = 830;
  const h = BAR_MAX * cl(eff / maxEff) * cl(win(t, 0.06, 0.16) * 1.2);
  const barX = 1180, barW = 300;

  // Ghost of where it started — the shrink needs something to shrink FROM.
  const ghostH = BAR_MAX * cl(stops[0].effect / maxEff) * cl(win(t, 0.06, 0.16) * 1.2);

  return (
    <AbsoluteFill style={{ background: BG }}>
      <SparkLine line={spark} t={titleIn} />
      <div style={{
        position: 'absolute', top: 200, left: SAFE, right: SAFE, textAlign: 'center',
        fontFamily: SERIF, fontSize: fitTitle(title), color: INK, opacity: titleIn,
      }}>{title}</div>

      {/* Left: the scale reading, ticking up */}
      <div style={{ position: 'absolute', left: SAFE + 40, top: 420, width: 820 }}>
        <div style={{
          fontFamily: SANS, fontSize: 26, letterSpacing: '0.22em', color: SOFT,
          textTransform: 'uppercase', opacity: titleIn,
        }}>SCALE OF THE PROGRAMME</div>
        <div style={{ fontFamily: SERIF, fontSize: 66, color: INK, lineHeight: 1.14, marginTop: 20, minHeight: 160 }}>
          {f < 0.5 ? cur.scaleLabel : nxt.scaleLabel}
        </div>
        <div style={{
          fontFamily: SERIF, fontSize: 36, color: SOFT, lineHeight: 1.3, marginTop: 12, minHeight: 96,
        }}>{f < 0.5 ? cur.caption : nxt.caption}</div>
      </div>

      {/* Right: the effect bar, shrinking in place */}
      <svg width={CW} height={CH} style={{ position: 'absolute', inset: 0 }}>
        <rect x={barX} y={base - ghostH} width={barW} height={ghostH} fill="none" stroke={GHOST} strokeWidth={2} strokeDasharray="7 8" />
        <rect x={barX} y={base - h} width={barW} height={h} fill={ACC} opacity={0.9} />
        <line x1={barX - 40} y1={base} x2={barX + barW + 40} y2={base} stroke={INK} strokeWidth={3} opacity={0.5} />
      </svg>
      <div style={{
        position: 'absolute', left: barX + barW + 34, top: base - h - 34,
        fontFamily: SERIF, fontSize: 60, color: ACC_TEXT,
      }}>{showValue
          ? <>{eff.toFixed(2)}<span style={{ fontSize: 34, color: SOFT, marginLeft: 10 }}>{unit}</span></>
          : <span style={{ fontSize: 46, color: ACC_TEXT }}>{(f < 0.5 ? qualitative[i] : qualitative[Math.min(qualitative.length - 1, i + 1)]) ?? ''}</span>}</div>
      <div style={{
        position: 'absolute', left: barX, top: base + 26, width: barW + 200,
        fontFamily: SANS, fontSize: 26, letterSpacing: '0.2em', color: SOFT, textTransform: 'uppercase',
      }}>EFFECT ON ACHIEVEMENT</div>

      <Note text={note} o={noteIn} />
    </AbsoluteFill>
  );
};


// ===========================================================================
// TtDenominator — a headline percentage fills the frame, then the camera pulls
// BACK and the real denominator assembles around it. The correction is the
// zoom-out; freeze either end of it and you get one of the two mistakes.
// ===========================================================================
export const ttDenominatorSchema = z.object({
  headline: z.string().default('57%'),
  headlineClaim: z.string().default('of students without home Wi-Fi'),
  universe: z.number().int().min(20).max(200).default(100),
  numerator: z.number().int().default(4),
  secondary: z.number().int().default(3),
  numeratorLabel: z.string().default('smartphone-only'),
  secondaryLabel: z.string().default('no home access'),
  universeLabel: z.string().default('children ages 3–18'),
  correction: z.string().default('the denominator is the small group, not the population'),
  note: z.string().default(''),
  spark: z.string().default(''),
});
export type TtDenominatorProps = z.infer<typeof ttDenominatorSchema>;

export const TtDenominator: React.FC<TtDenominatorProps> = ({
  headline, headlineClaim, universe, numerator, secondary,
  numeratorLabel, secondaryLabel, universeLabel, correction, note, spark,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const t = frame / durationInFrames;
  const bigIn = cl(spring({ frame, fps, config: GENTLE }));

  // The pull-back: headline shrinks and rises; the grid builds behind it.
  const pull = win(t, 0.30, 0.56);
  const gridIn = win(t, 0.36, 0.72);
  const corrIn = win(t, 0.72, 0.84);
  const noteIn = win(t, 0.86, 0.95);

  const bigScale = 1 - pull * 0.62;
  const bigY = 300 - pull * 78;

  const COLS = 20;
  const rows = Math.ceil(universe / COLS);
  const cell = 44, gap = 8;
  const gridW = COLS * cell + (COLS - 1) * gap;
  const gridX = (CW - gridW) / 2;
  const gridY = 470;

  return (
    <AbsoluteFill style={{ background: BG }}>
      <SparkLine line={spark} t={bigIn} />

      {/* The grid — 100 squares; only the flagged ones colour in. */}
      <svg width={CW} height={CH} style={{ position: 'absolute', inset: 0 }}>
        {Array.from({ length: universe }).map((_, k) => {
          const r = Math.floor(k / COLS), c = k % COLS;
          const isNum = k < numerator;
          const isSec = k >= numerator && k < numerator + secondary;
          const flagged = isNum || isSec;
          // Flagged squares land first, the rest fill in behind them.
          const own = flagged ? win(t, 0.36, 0.46) : win(t, 0.44 + (k / universe) * 0.22, 0.52 + (k / universe) * 0.22);
          return (
            <rect key={k}
              x={gridX + c * (cell + gap)} y={gridY + r * (cell + gap)}
              width={cell} height={cell}
              fill={isNum ? ACC : isSec ? INK : CARD}
              stroke={flagged ? 'none' : BORDER} strokeWidth={2}
              opacity={own * gridIn} />
          );
        })}
      </svg>

      {/* Headline: starts enormous, pulls back to a caption over the grid. */}
      <div style={{
        position: 'absolute', left: 0, right: 0, top: bigY, textAlign: 'center',
        fontFamily: SERIF, color: ACC_TEXT, fontSize: 300 * bigScale, lineHeight: 1,
        opacity: bigIn,
      }}>{headline}</div>
      <div style={{
        position: 'absolute', left: SAFE, right: SAFE, top: bigY + 300 * bigScale + 8,
        textAlign: 'center', fontFamily: SERIF, fontSize: 46 - pull * 12,
        color: SOFT, opacity: bigIn * (1 - pull * 0.45),
      }}>{headlineClaim}</div>

      {/* Legend under the grid */}
      <div style={{
        position: 'absolute', left: gridX, top: gridY + rows * (cell + gap) + 26,
        display: 'flex', gap: 44, alignItems: 'center', opacity: gridIn,
      }}>
        {[[ACC, `${numerator} — ${numeratorLabel}`], [INK, `${secondary} — ${secondaryLabel}`], [BORDER, `${universe - numerator - secondary} — ${universeLabel}`]].map(([col, lab], k) => (
          <div key={k} style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
            <div style={{ width: 24, height: 24, background: col as string, border: `2px solid ${BORDER}` }} />
            <span style={{ fontFamily: SERIF, fontSize: 32, color: SOFT }}>{lab as string}</span>
          </div>
        ))}
      </div>

      <div style={{
        position: 'absolute', left: SAFE, right: SAFE, bottom: SAFE + 42, textAlign: 'center',
        fontFamily: SERIF, fontSize: 44, color: ACC_TEXT, lineHeight: 1.26, opacity: corrIn,
        transform: `translateY(${(1 - corrIn) * 16}px)`,
      }}>{correction}</div>

      <Note text={note} o={noteIn} />
    </AbsoluteFill>
  );
};


// ===========================================================================
// TtAbsence — a query is typed into a search field; candidate rows rise and
// then dissolve one by one; a counter settles on what is actually left. The
// emptiness has to ARRIVE — that is the beat.
// ===========================================================================
export const ttAbsenceSchema = z.object({
  query: z.string().default('randomized trials: AI-specific teacher PD → student outcomes'),
  ghosts: z.array(z.string()).min(1).max(6).default(['a trial', 'a trial', 'a trial']),
  survivorLabel: z.string().default('what survives the filter'),
  survivor: z.string().default('almost nothing'),
  verdict: z.string().default('The absence is the finding.'),
  note: z.string().default(''),
  spark: z.string().default(''),
});
export type TtAbsenceProps = z.infer<typeof ttAbsenceSchema>;

export const TtAbsence: React.FC<TtAbsenceProps> = ({
  query, ghosts, survivorLabel, survivor, verdict, note, spark,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const t = frame / durationInFrames;
  const barIn = cl(spring({ frame, fps, config: GENTLE }));

  // Query types out.
  const typed = win(t, 0.06, 0.28);
  const shown = query.slice(0, Math.round(typed * query.length));
  const caret = Math.floor(frame / 9) % 2 === 0 && typed < 1;

  const survIn = win(t, 0.70, 0.82);
  const verdIn = win(t, 0.82, 0.92);
  const noteIn = win(t, 0.88, 0.97);

  const rowTop = 470, rowH = 92;

  return (
    <AbsoluteFill style={{ background: BG }}>
      <SparkLine line={spark} t={barIn} />

      {/* The search field */}
      <div style={{
        position: 'absolute', left: SAFE, right: SAFE, top: 250,
        background: CARD, border: `2px solid ${BORDER}`, borderRadius: 6,
        padding: '26px 30px', minHeight: 96, display: 'flex', alignItems: 'center',
        opacity: barIn, transform: `translateY(${(1 - barIn) * 16}px)`,
      }}>
        <span style={{ fontFamily: SERIF, fontSize: 42, color: ACC_TEXT, marginRight: 18 }}>*</span>
        <span style={{ fontFamily: SANS, fontSize: 36, color: INK, lineHeight: 1.2 }}>
          {shown}{caret ? <span style={{ color: ACC_TEXT }}>|</span> : null}
        </span>
      </div>

      {/* Candidate rows rise, then dissolve on a stagger. */}
      {ghosts.map((g, k) => {
        const a = 0.32 + k * 0.055;
        const rise = win(t, a, a + 0.05);
        const fade = win(t, a + 0.10, a + 0.19);
        const o = rise * (1 - fade);
        return (
          <div key={k} style={{
            position: 'absolute', left: SAFE + 40, right: SAFE + 40, top: rowTop + k * rowH,
            background: CARD, border: `2px solid ${BORDER}`, borderRadius: 4,
            padding: '18px 26px', opacity: o,
            transform: `translateX(${(1 - rise) * -26}px) translateY(${fade * 14}px)`,
            filter: `blur(${fade * 3}px)`,
          }}>
            <span style={{ fontFamily: SERIF, fontSize: 36, color: SOFT }}>{g}</span>
          </div>
        );
      })}

      {/* What is left */}
      <div style={{
        position: 'absolute', left: SAFE, right: SAFE, top: rowTop + 40,
        textAlign: 'center', opacity: survIn,
      }}>
        <div style={{
          fontFamily: SANS, fontSize: 26, letterSpacing: '0.22em', color: SOFT,
          textTransform: 'uppercase', marginBottom: 22,
        }}>{survivorLabel}</div>
        <div style={{
          fontFamily: SERIF, fontSize: 110, color: ACC_TEXT, lineHeight: 1.06,
          transform: `translateY(${(1 - survIn) * 18}px)`,
        }}>{survivor}</div>
      </div>

      <div style={{
        position: 'absolute', left: SAFE, right: SAFE, bottom: SAFE + 46, textAlign: 'center',
        fontFamily: SERIF, fontSize: 52, color: INK, opacity: verdIn,
      }}>{verdict}</div>

      <Note text={note} o={noteIn} />
    </AbsoluteFill>
  );
};


// ===========================================================================
// TtVerdictGrid — the sub-claims land one at a time and each takes a stamped
// verdict. Reading order is the argument's order, so the stagger matters.
// ===========================================================================
export const ttVerdictGridSchema = z.object({
  title: z.string().default('The claim, decomposed'),
  rows: z.array(z.object({
    key: z.string().default(''),
    claim: z.string(),
    verdict: z.string().default('MIXED'),
    accent: z.boolean().default(false),
  })).min(2).max(7),
  note: z.string().default(''),
  spark: z.string().default(''),
});
export type TtVerdictGridProps = z.infer<typeof ttVerdictGridSchema>;

export const TtVerdictGrid: React.FC<TtVerdictGridProps> = ({ title, rows, note, spark }) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const t = frame / durationInFrames;
  const titleIn = cl(spring({ frame, fps, config: GENTLE }));
  const noteIn  = win(t, 0.88, 0.96);

  const top = 330, bottom = 940;
  const rowH = Math.min(120, (bottom - top) / rows.length);
  const KEY_W = 84;
  const VERD_W = 420;
  const longest = Math.max(...rows.map((r) => r.claim.length));
  const claimPx = longest <= 52 ? 40 : longest <= 72 ? 35 : 31;

  return (
    <AbsoluteFill style={{ background: BG }}>
      <SparkLine line={spark} t={titleIn} />
      <div style={{
        position: 'absolute', top: 200, left: SAFE, fontFamily: SERIF,
        fontSize: fitTitle(title), color: INK, opacity: titleIn,
      }}>{title}</div>

      {rows.map((r, k) => {
        const a = 0.10 + k * (0.62 / rows.length);
        const rowIn = cl(spring({ frame: frame - Math.round(durationInFrames * a), fps, config: GENTLE }));
        const stamp = cl(spring({ frame: frame - Math.round(durationInFrames * (a + 0.05)), fps, config: FIRM }));
        const y = top + k * rowH;
        return (
          <div key={k} style={{
            position: 'absolute', left: SAFE, right: SAFE, top: y, height: rowH,
            display: 'flex', alignItems: 'center',
            opacity: rowIn, transform: `translateX(${(1 - rowIn) * -24}px)`,
          }}>
            <div style={{
              width: KEY_W, fontFamily: SANS, fontSize: 30, letterSpacing: '0.14em',
              color: r.accent ? ACC_TEXT : GHOST,
            }}>{r.key}</div>
            <div style={{
              flex: 1, paddingRight: 40, fontFamily: SERIF, fontSize: claimPx,
              color: INK, lineHeight: 1.2,
            }}>{r.claim}</div>
            <div style={{
              width: VERD_W, flexShrink: 0, textAlign: 'right',
              fontFamily: SANS, fontSize: 27, letterSpacing: '0.18em',
              color: r.accent ? ACC_TEXT : SOFT, textTransform: 'uppercase',
              opacity: stamp, transform: `scale(${0.94 + stamp * 0.06})`, transformOrigin: 'right center',
            }}>{r.verdict}</div>
            <div style={{
              position: 'absolute', left: 0, right: 0, bottom: 0, height: 1,
              background: BORDER, opacity: rowIn,
            }} />
          </div>
        );
      })}

      <Note text={note} o={noteIn} />
    </AbsoluteFill>
  );
};


// ===========================================================================
// TtEffectBars — horizontal bars scaled to the DATA MAX, where the printed
// value is a verbatim string from the beat sheet.
//
// Why this exists: ReqBars normalises to 100 and appends a hardcoded '%'. That
// turns 0.49 SD into "49%" and a 4-percentage-point gain into "4%" — both wrong
// units — and renders a 4-point bar as an invisible stub. In a film about
// misreported numbers that is not a cosmetic bug. Here the unit is a beat-sheet
// decision and the component cannot mislabel it.
// ===========================================================================
export const ttEffectBarsSchema = z.object({
  title: z.string().default('Effects'),
  scaleNote: z.string().default(''),
  data: z.array(z.object({
    label: z.string(),
    value: z.number(),            // drives bar length only
    display: z.string(),          // printed verbatim — the unit lives here
    accent: z.boolean().default(false),
  })).min(2).max(4),
  caveat: z.string().default(''), // the result that complicates the good news
  note: z.string().default(''),
  spark: z.string().default(''),
});
export type TtEffectBarsProps = z.infer<typeof ttEffectBarsSchema>;

export const TtEffectBars: React.FC<TtEffectBarsProps> = ({
  title, scaleNote, data, caveat, note, spark,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const t = frame / durationInFrames;
  const titleIn = cl(spring({ frame, fps, config: GENTLE }));
  const capIn   = win(t, 0.68, 0.80);
  const noteIn  = win(t, 0.84, 0.94);

  const max = Math.max(...data.map((d) => d.value)) || 1;
  const LAB_W  = 620;
  const trackX = SAFE + LAB_W + 30;
  const trackW = CW - trackX - SAFE - 300;
  const top    = caveat ? 350 : 380;
  const rowH   = Math.min(210, ((caveat ? 760 : 880) - top) / data.length);

  return (
    <AbsoluteFill style={{ background: BG }}>
      <SparkLine line={spark} t={titleIn} />
      <div style={{
        position: 'absolute', top: 200, left: SAFE, right: SAFE,
        fontFamily: SERIF, fontSize: fitTitle(title), color: INK, opacity: titleIn,
      }}>{title}</div>
      {scaleNote ? (
        <div style={{
          position: 'absolute', top: 272, left: SAFE, fontFamily: SANS, fontSize: 25,
          letterSpacing: '0.2em', color: SOFT, textTransform: 'uppercase',
          opacity: win(t, 0.08, 0.20),
        }}>{scaleNote}</div>
      ) : null}

      {data.map((d, k) => {
        const grow = cl(spring({
          frame: frame - Math.round(durationInFrames * (0.16 + k * 0.20)),
          fps, config: GENTLE,
        }));
        const y = top + k * rowH + (rowH - 92) / 2;
        const w = trackW * (d.value / max) * grow;
        const col = d.accent ? ACC_TEXT : INK;
        return (
          <div key={k}>
            <div style={{
              position: 'absolute', left: SAFE, top: y + 16, width: LAB_W, textAlign: 'right',
              fontFamily: SERIF, fontSize: d.label.length > 32 ? 36 : 40,
              color: INK, lineHeight: 1.16, opacity: grow,
            }}>{d.label}</div>
            <div style={{
              position: 'absolute', left: trackX, top: y, width: Math.max(4, w), height: 92,
              background: col, opacity: d.accent ? 0.92 : 0.8,
            }} />
            <div style={{
              position: 'absolute', left: trackX + Math.max(4, w) + 26, top: y + 10,
              fontFamily: SERIF, fontSize: 52, color: INK, opacity: grow,
              whiteSpace: 'nowrap',
            }}>{d.display}</div>
          </div>
        );
      })}

      {caveat ? (
        <div style={{
          position: 'absolute', left: SAFE, right: SAFE, top: 812,
          borderTop: `2px solid ${BORDER}`, paddingTop: 22,
          fontFamily: SERIF, fontSize: 42, color: SOFT, lineHeight: 1.24,
          opacity: capIn, transform: `translateY(${(1 - capIn) * 14}px)`,
        }}>
          <span style={{ color: ACC_TEXT }}>&#42;&nbsp;</span>{caveat}
        </div>
      ) : null}

      <Note text={note} o={noteIn} />
    </AbsoluteFill>
  );
};
