# TYPECHECK.md — The nopunt Skill (Short)

This is a derivative Short. No new Remotion / Manim source was authored in this
session; the seven kept beats reuse the parent's finished native-portrait
renders and mp3s unchanged.

## Static / schema checks

- `beat_sheet.json` passes `runtime/scripts/build_safety.py::validate_project` at derivation time (`shorts.py` calls it before writing) and again at compile time (`compile.py` calls it before rendering).
- `metadata`: `kind: short`, `aspect_ratio: 9:16`, `voice: am_onyx`, `voice_kokoro: am_onyx`, `captions: false`, `playlist: Brutalist`, `total_estimated_duration_seconds: 168.21`, `short_validation.status: ready`.
- `dropped_beats: ["B02", "B03", "B08", "B09", "B10"]`.
- `derived_from: claude-liam-brutalist-skill-nopunt-vertical`.
- Kept beats: `["B00", "B01", "B04", "B05", "B06", "B07", "B11"]`.
- Every retained beat still carries `render_duration_s`, `audio_file`, and a `build` record from the parent; the compile pass re-stamps `build` with the derivative's compile timestamps and 7/7 filled status.

## Typography / visual type review

Portrait renders inspected via extracted beat-relative frames
(`_qc/frames-beat/B*_{15,50,85}.jpg`):

- **B00** (`ClaudeComposerAsk916`) — brand serif eyebrow, EB Garamond title
  `The nopunt Skill`, cream ground, composer card with monospace body, terracotta send button, three answer lines in monospace with terracotta bullet — all within safe.b, no bleed.
- **B01** (`BrutalistHesitantWriter916`) — three-line design, serif, single
  design box, hesitant-writer swap from `linter` → `catalog` visible mid-beat, cursor blink visible. Fills ≥55% of safe area (portrait BLUF recipe applied).
- **B04 / B05 / B06 / B07** (`SkillTeardownMechanism916`) — MECHANISM eyebrow,
  bold serif heading, body copy, monospace quote block with terracotta rule and cite, terracotta verdict pill, italic spark line. No overflow. All within safe.b at 2160×3840.
- **B11** (`ClaudeTitleOutro916`) — title `The nopunt Skill` with terracotta full stop, `@NikBearBrown` handle centered, slug-seeded mascot corner (fade-in animation intrinsic to composition).

## Legibility

Preview frames scaled to 540×960 during QC extraction; text is legible at
that scale (which corresponds to ~13.5% of a 4K portrait file), meaning at
native 2160×3840 all body copy easily satisfies portrait legibility. No
truncation or overflow observed in any of 21 beat-relative frames.

## What is NOT type-checked

- No TypeScript / TSC pass (the Remotion source in `runtime/remotion/` is unchanged in this Short's session; type contracts were enforced when the parent's B00 / B01 / B04-07 / B11 were originally rendered).
- No linter for `SKILL.md` markdown; content is treated as read-only source.
- No spellcheck was run; on-screen text is verbatim from the parent renders which the parent job already reviewed.

## Sandbox / write-scope

- All writes limited to `youtube/brutalist/shorts/claude-liam-brutalist-skill-nopunt-short/` and the isolated toolkit workspace.
- No writes to the parent reel (`youtube/brutalist/claude-liam-brutalist-skill-nopunt/`), the public toolkit, examples, or fellows directories.
- No git commit, no push, no upload attempted.
