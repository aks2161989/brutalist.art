# PROMPTS — The duration-planner Skill (portrait)

Same prompts, narration, and Kokoro voice as landscape (see
`../PROMPTS.md`). Only the visual rendering differs — Remotion renders each
beat via its native `<Pattern>916` composition.

## Portrait-specific delta vs the landscape build

- `runtime/scripts/shorts.py --vertical` planned the full-length companion.
- `runtime/scripts/remotion_scenes.py <reel>/vertical` re-rendered every
  Remotion beat through its 916 sibling.
- `runtime/scripts/compile.py <reel>/vertical --height 3840 --out <exports>/vertical`
  produced the 2160×3840 master.
- Same environment: `ART_CHROME=<toolkit>/runtime/scripts/chrome_wrap.sh`,
  `ART_CHROME_MODE=chrome-for-testing`.
- `channel_title` metadata removed from vertical sheet (compile-time PIL
  overlay bled past portrait safe.b — folder chip inside the composer beat
  still carries `@HumanitariansAI`).

## Composer prompts SEEN ON SCREEN

Same as landscape — see `../PROMPTS.md`. Portrait rewraps them into more
lines because the safe width is smaller (972 vs 1728), but no character is
changed.
