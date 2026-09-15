# What Is Brutalist? — episode README

*Brutalist playlist · Episode 01 · @HumanitariansAI ·
Liam (in for Bear) · Kokoro `am_onyx` · No captions.*

This folder is the on-disk record of the first film in the Brutalist
playlist. Bear watches next; nothing here has been published.

## Two deliverables (four files)

| Aspect | Master mp4 | Dimensions | Duration | SHA-256 |
|---|---|---|---|---|
| Landscape 16:9 | [`exports/landscape/claude-liam-brutalist-what-is-brutalist.mp4`](exports/landscape/claude-liam-brutalist-what-is-brutalist.mp4) | 3840 × 2160 | 170.4 s | `24c49950c0aa8583f57c285cd67250a28ae1673c2367baf37de89fe02bf7d56e` |
| Portrait 9:16 | [`exports/vertical/claude-liam-brutalist-what-is-brutalist-vertical.mp4`](exports/vertical/claude-liam-brutalist-what-is-brutalist-vertical.mp4) | 2160 × 3840 | 170.4 s | `c339f1b5555e847096f3ea975249042c50b86714c8a29fee20d3eb58398c3f9c` |

Each master has a sibling `.verified.json` receipt (state `ready`) written by
the compiler's atomic verification. `ready` means the automated export checks
passed, not that a human approved the film for release.

## What you'll see

Ten beats, ~2 min 50 s:

1. **B00 — Ask** (cold open, ClaudeComposerAsk). Ciao/Liam greeting; the
   composer types the ask "Explain what Brutalist actually is. Not the slogan
   — the thing on disk."
2. **B01 — BLUF** (BrutalistHesitantWriter). The writer types the wrong
   framing ("a video editor for AI clips" — landscape / "editor" — portrait),
   turns it terracotta, deletes, and re-types the corrected pivot
   ("plain-text-recipe" / "recipe"). The final sentence stands.
3. **B02 — Framework** (WibRecipe). Split-panel: a beat_sheet.json snippet
   materializes on the left / above; the rendered composer that the JSON
   describes appears on the right / below. Terracotta arrow: the JSON becomes
   the pixels.
4. **B03 — Worked example, pipeline** (WibPipeline). BRIEF → BEAT SHEET →
   AUDIO → SCENES → COMPILE → 4K MASTER. No PUBLISH stage — Brutalist never
   uploads.
5. **B04 — Worked example, pure function** (WibChange). A one-field edit in
   the beat sheet's B00 greeting — "Ciao" → "Hola" — visibly re-renders the
   greeting on screen.
6. **B05 — Division of labor** (WibDivision). Two lanes: HUMAN judgment (four
   rows, terracotta) vs AGENT execution (five rows).
7. **B06 — Falsifiability** (WibNotClaims). What Brutalist isn't: not a
   publisher; not a paid API; not a judge of taste.
8. **B07 — Verdict** (WibVerdict). "Film as code, in three lines" — the
   principled restate.
9. **B08 — Your Turn** (ClaudeComposerAsk). A paste-ready prompt for Claude
   Code, read aloud, with three expected artifacts as the viewer's rubric.
10. **B09 — Outro** (WibOutro). Title restate with `@HumanitariansAI`
    hardcoded and the "LIAM, IN FOR BEAR." subline.

## Paperwork map

Both aspects have their own review paperwork; portrait review is independent.

| Landscape | Portrait |
|---|---|
| [`SCRIPT.md`](SCRIPT.md) | *(shared — same narration, same audio)* |
| [`SOURCES.md`](SOURCES.md) | [`vertical/SOURCES.md`](vertical/SOURCES.md) |
| [`FACTCHECK.md`](FACTCHECK.md) | [`vertical/FACTCHECK.md`](vertical/FACTCHECK.md) |
| [`SHOTLIST.md`](SHOTLIST.md) | [`vertical/SHOTLIST.md`](vertical/SHOTLIST.md) |
| [`PROMPTS.md`](PROMPTS.md) | [`vertical/PROMPTS.md`](vertical/PROMPTS.md) |
| [`CHECKS-REPORT.md`](CHECKS-REPORT.md) | [`vertical/CHECKS-REPORT.md`](vertical/CHECKS-REPORT.md) |
| [`TYPECHECK.md`](TYPECHECK.md) | [`vertical/TYPECHECK.md`](vertical/TYPECHECK.md) |
| [`BUILD-PROMPT.md`](BUILD-PROMPT.md) | [`vertical/BUILD-PROMPT.md`](vertical/BUILD-PROMPT.md) |
| [`VISUAL-REVIEW.json`](VISUAL-REVIEW.json) | [`vertical/VISUAL-REVIEW.json`](vertical/VISUAL-REVIEW.json) |

- Narration mp3s (Kokoro `am_onyx`, local, free, $0.00): `mp3/beat-B*.mp3`
  and `vertical/mp3/beat-B*.mp3`.
- Per-beat renders: `media/B*.mp4` and `vertical/media/B*.mp4`.
- Gate-V QC reports and contact sheets: `_qc/` and `vertical/_qc/`.
- Frame extractions (2 fps): `_qc/frames/` and `vertical/_qc/frames/`.

## Bear's viewing/editing is next

Nothing here has been published. Both masters passed the compiler's Gate V
frame-level QC clean (0 BLOCKER, 0 MAJOR) and its atomic verification. The
next step is Bear — watch the two masters end-to-end, listen across every
narration transition, and note anything to change in
[`FEEDBACK.md`](FEEDBACK.md). The build agent regenerates only the affected
beats on rerun.

*Re-verified 2026-09-11 (run_id `07663aa5c9f343758157ff7530f463d7`): toolkit
commits ba2d0e0/7ee2da6 changed source_sha256; no beat content, audio, or scene
sources changed; FEEDBACK.md has no human notes; both MP4 SHA-256s confirmed
on disk against .verified.json records; contact sheets re-read and confirmed
visually with the Read tool (both aspects).*

## Known limitations recorded honestly

- `skills/make/explainer/SKILL.md`, `scripts/type_check.py` and the kerning
  reference are not present in this toolkit snapshot. See the "Gaps" section
  in either `CHECKS-REPORT.md`.
- The compiler prints a skin-lint note that B09 uses `WibOutro` instead of
  the shipped `ClaudeTitleOutro`. This is deliberate: `ClaudeTitleOutro`
  hardcodes `@NikBearBrown` per `OUTRO-LOCK.md`, and this reel is on the
  `@HumanitariansAI` channel. `WibOutro` (native to this reel, in the isolated
  toolkit) is the required HAI variant. The live public toolkit was not
  modified.
- The build ran inside an Apple App Sandbox that blocks Chrome's Mach IPC.
  Remotion renders used a wrapper (`runtime/chrome-wrapper.sh`) around the
  locally-cached `chrome-headless-shell` with `--single-process` /
  `--in-process-gpu`. No sandbox permissions were changed; no Remotion API
  was bypassed; `ART_CHROME` / `ART_CHROME_MODE` are the documented hooks.
- Local 4K masters are not proof of YouTube 4K processing. That check is a
  separate human step after upload.
