import React from 'react';
import {AbsoluteFill, Img, staticFile, useCurrentFrame, useVideoConfig, interpolate} from 'remotion';
import {z} from 'zod';
import {NEU_RED, FONT_NEU} from '../tokens/neu';
import {useLato} from '../tokens/lato';

/**
 * SeisLogoReveal — the unit's mark resolving out of blur ("opacity through blur").
 * The lockup starts wide-blurred and transparent, then sharpens and settles as a red rule draws
 * beneath it. Used as the first beat of the alumni film and rendered standalone as a reusable
 * sting for every SEIS video. Dark ground, knockout lockup, NU red.
 */
export const seisLogoRevealSchema = z.object({
  tagline: z.string().default(''),
  holdFrames: z.number().default(150),
  light: z.boolean().default(false),   // white ground + standard lockup, for light-background decks
});
export type SeisLogoRevealProps = z.infer<typeof seisLogoRevealSchema>;

export const SeisLogoRevealInner: React.FC<{tagline?: string; light?: boolean}> = ({tagline = '', light = false}) => {
  const frame = useCurrentFrame(); const {width, height, durationInFrames} = useVideoConfig();
  // opacity through blur: 48px -> 0px while 0 -> 1, easing out over ~1.4s
  const p = interpolate(frame, [0, 42], [0, 1], {extrapolateRight: 'clamp'});
  const eased = 1 - Math.pow(1 - p, 3);
  const blur = (1 - eased) * 48;
  const scale = 1.06 - eased * 0.06;
  const rule = interpolate(frame, [30, 58], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const tag = interpolate(frame, [48, 70], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const out = interpolate(frame, [durationInFrames - 14, durationInFrames], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill style={{backgroundColor: light ? '#FFFFFF' : '#0A0A0A', alignItems: 'center', justifyContent: 'center', opacity: out}}>
      <Img
        src={staticFile(light ? 'seis/seis-logo.png' : 'seis/seis-logo-knockout.png')}
        style={{height: height * 0.20, opacity: eased, filter: `blur(${blur}px)`, transform: `scale(${scale})`}}
      />
      <div style={{width: width * 0.10 * rule, height: Math.max(4, height * 0.006), backgroundColor: NEU_RED, marginTop: height * 0.045}} />
      {tagline ? (
        <div style={{fontFamily: FONT_NEU.display, fontSize: height * 0.034, color: light ? '#000000' : '#FFFFFF', marginTop: height * 0.04, opacity: tag, letterSpacing: 0.5}}>{tagline}</div>
      ) : null}
    </AbsoluteFill>
  );
};

export const SeisLogoReveal: React.FC<SeisLogoRevealProps> = ({tagline, light}) => {
  useLato();
  return <SeisLogoRevealInner tagline={tagline} light={light} />;
};
