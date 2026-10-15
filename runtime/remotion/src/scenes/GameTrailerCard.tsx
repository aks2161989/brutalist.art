import React from 'react';
import { AbsoluteFill, Img, useCurrentFrame, useVideoConfig, spring } from 'remotion';
import { z } from 'zod';
import { useLato } from '../tokens/lato';

/**
 * GameTrailerCard — the game's own title and end card for a godot-trailer film
 * (skills/make/godot-trailer/). Reach for this when a game trailer needs its
 * title reveal (`kind: "title"`) or its final call-to-action card (`kind:
 * "endcard"`: title, exact platforms, availability line, ONE dominant
 * directive button). It carries the GAME's identity, not the Claude brand: a
 * near-black ground, off-white type, Lato, and an optional accent and game icon
 * passed as props. No @NikBearBrown handle, no mascot, no jingle — a trailer
 * ends on its call to action, never on a channel sign-off or a fade to black.
 * The card never fades out: it springs in, then holds until the beat ends, so
 * the viewer can read it. Every string is a prop the trailer's `cta` block was
 * verified against (export_presets.cfg / README / git remote); nothing is
 * invented here. Duration-agnostic — the compiler conforms the clip to the beat.
 */

export const gameTrailerCardSchema = z.object({
  kind: z.enum(['title', 'endcard']).default('endcard'),
  title: z.string().default('⚠ SET title IN BEAT SHEET'),
  platforms: z.array(z.string()).default([]),
  availability: z.string().default(''),
  directive: z.string().default(''),
  /** The one place to do it, e.g. a repository or store address. Shown under the button, never a second action. */
  address: z.string().default(''),
  background: z.string().default('#0B0B0D'),
  foreground: z.string().default('#F4F1EA'),
  accent: z.string().default('#F4F1EA'),
  /** A custom game icon as a data: URI. Omit it when the game still uses the engine's default icon. */
  iconDataUri: z.string().default(''),
});
export type GameTrailerCardProps = z.infer<typeof gameTrailerCardSchema>;

const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));
const CHAR_ADV = 0.6; // conservative average advance, in em, for Lato Bold/Regular

export const GameTrailerCard: React.FC<GameTrailerCardProps> = ({
  kind, title, platforms, availability, directive, address,
  background, foreground, accent, iconDataUri,
}) => {
  useLato();
  const frame = useCurrentFrame();
  const { fps, height, width } = useVideoConfig();

  const pop = (at: number) => {
    const sp = spring({ frame: frame - at, fps, config: { damping: 22, stiffness: 150, mass: 0.8 } });
    return frame >= at ? clamp(sp, 0, 1) : 0;
  };

  const availW = width * 0.84;
  const floor = Math.round(height * 0.05);      // GATE T floor is 4.5 % of height
  const fit = (text: string, want: number) =>
    Math.max(floor, Math.min(Math.round(want), Math.floor(availW / (Math.max(text.length, 1) * CHAR_ADV))));

  const isTitle = kind === 'title';
  const titleSz = fit(title, height * (isTitle ? 0.2 : 0.13));
  const platformLine = platforms.join('   ·   ');
  const showInfo = !isTitle && platforms.length > 0;
  const tIn = pop(isTitle ? 6 : 4);

  return (
    <AbsoluteFill style={{ background, alignItems: 'center', justifyContent: 'center', color: foreground }}>
      <div style={{
        display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center',
        gap: Math.round(height * 0.035), padding: '0 8%',
        fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif",
      }}>
        {!isTitle && iconDataUri && (
          <Img src={iconDataUri} style={{
            height: Math.round(height * 0.14), width: Math.round(height * 0.14),
            opacity: pop(0), transform: `scale(${0.9 + 0.1 * pop(0)})`,
          }} />
        )}
        <div style={{
          fontSize: titleSz, fontWeight: 700, letterSpacing: '-0.02em', lineHeight: 1.05,
          opacity: tIn, transform: `translateY(${(1 - tIn) * 18}px)`,
        }}>{title}</div>

        {showInfo && (
          <div style={{ opacity: pop(18), display: 'flex', flexDirection: 'column', alignItems: 'center', gap: Math.round(height * 0.012) }}>
            <div style={{ fontSize: fit(platformLine, height * 0.055), fontWeight: 400, opacity: 0.88 }}>{platformLine}</div>
            {availability && (
              <div style={{ fontSize: fit(availability, height * 0.055), fontWeight: 700 }}>{availability}</div>
            )}
          </div>
        )}

        {!isTitle && directive && (
          <div style={{
            marginTop: Math.round(height * 0.02),
            padding: `${Math.round(height * 0.022)}px ${Math.round(height * 0.05)}px`,
            borderRadius: Math.round(height * 0.014),
            background: accent, color: background,
            fontSize: fit(directive, height * 0.06), fontWeight: 700, letterSpacing: '0.01em',
            opacity: pop(34), transform: `scale(${0.92 + 0.08 * pop(34)})`,
          }}>{directive}</div>
        )}

        {!isTitle && address && (
          <div style={{
            fontSize: fit(address, height * 0.05), fontWeight: 400, opacity: pop(46) * 0.9,
            transform: `translateY(${(1 - pop(46)) * 8}px)`,
          }}>{address}</div>
        )}
      </div>
    </AbsoluteFill>
  );
};
