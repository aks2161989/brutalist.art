# CHECKS-REPORT — vertical (9:16) — Brutalist Command: art scene-index

Portrait cut. Same paperwork discipline as the landscape master; per-aspect.
Updated 2026-09-12 (run 88f42532): same source-driven fixes as landscape —
art:71-74→art:92-95 in B02 ClaudeCodeBeat916 title, 619→620 in B00/B05/B07/B09.

## Gate F

- `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`, `BUILD-PROMPT.md`, `TYPECHECK.md`
  present in `vertical/`. `SOURCES.md` re-used from the landscape master
  (identical primary sources; noted in the portrait FACTCHECK.md).
- `beat_sheet.json` — 12 beats, all `*916` patterns.

Result: PASS.

## Gate V

Ran against `exports/vertical/claude-liam-brutalist-command-scene-index-vertical.mp4`.

```
[gate-v] frames=24 BLOCKER=0 MAJOR=0 → vertical/_qc/frames/REPORT.md
```

Iterated to reach clean:
- B01 initially failed as MAJOR `underfill` at 16% — the shipped
  `BrutalistHesitantWriter.tsx` scale collapses to 0.5625 on 1080×1920.
  Patched the component per [[feedback_brutalist_hesitant_writer_portrait_scale_patch]]:
  `scale = height > width ? min(w/1080,h/1920) : min(w/1920,h/1080)`.
  fontSize 155, lineSpacing 2.9 now clears 55%.
- B10 initially failed as BLOCKER `edge-bleed` (bottom) — the paste
  prompt wrapped past the composer safe. Shortened the prompt while
  keeping the four steps (same intent as the landscape master;
  documented in `FACTCHECK.md`).

## Audio

Portrait re-generates identical Kokoro `am_onyx` audio (byte-identical
MP3s; measured durations match the landscape master exactly).

## ffprobe — final container

```
Duration: 00:04:28.50, start: 0.000000, bitrate: 516 kb/s
Stream #0:0 Video: h264 (High), yuv420p, 2160x3840, 24 fps, 24 tbr
Stream #0:1 Audio: aac (LC), 48000 Hz, stereo, fltp
```

Native 4K portrait, h.264 + AAC, decodes cleanly.

## Motion histogram (same warning, same rationale)

```
code-cascade: 7   type-on: 2   hesitant-type: 1   artifact-in: 1   outro-card: 1
WARNING: 'code-cascade' carries 7/12 beats (58%) — over the ~40% pantry cap
```

## Skin lint (informational only, expected under portrait reformat law)

```
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
```

Expected. Reformat law requires native portrait variants for every beat.
The lint does not block compilation; per the [scenes ep] pattern these
warnings are recorded and left unchanged.

## Known portrait-only limitations

- `ClaudeCodeBeat916` does not word-wrap. Long code lines in B04-B08
  clip horizontally inside the code card, but the card itself is inside
  `SAFE916`, so Gate V still passes. Fellows should prefer the
  landscape master for reading raw code contents.

## Final compile

```
[art] wrote exports/vertical/claude-liam-brutalist-command-scene-index-vertical.mp4  (268.3s, ...)
```

Gate V (2026-09-12 rebuild): `[gate-v] frames=24 BLOCKER=0 MAJOR=0 → vertical/_qc/REPORT.md`
Contact sheet written to `vertical/_qc/contact_sheet.png` and reviewed via Read tool.
SHA-256: `f7cbed1ea45539e6025af8a08d3bd2921943bae569b32158c669ad0b60aa11f6`
