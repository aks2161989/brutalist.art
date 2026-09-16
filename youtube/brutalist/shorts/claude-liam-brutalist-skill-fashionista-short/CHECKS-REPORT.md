# Checks report — The fashionista Skill (Short)

Run id: `5112069ad63347e9ab02657ed099ad9d`
Reel: `youtube/brutalist/shorts/claude-liam-brutalist-skill-fashionista-short/`
Master: `exports/short/claude-liam-brutalist-skill-fashionista-short.mp4`

Re-verified for this invocation. Source change (REPOLOOP-SHORTS-PROMPT.md updated) triggered re-invocation;
fashionista SKILL.md (`22614f44…`) and all media files confirmed bit-identical to previous build — no re-render required.

## 1. Cut plan

`runtime/scripts/shorts.py <parent>/vertical --output-dir <reel> --slug
claude-liam-brutalist-skill-fashionista-short --drop B02 B03 B08 B10
--no-endcard --no-outro-rewrite`

- Kept beats: B00, B01, B04, B05, B06, B07, B09, B11 (8 of 12).
- Dropped beats: B02 (anatomy), B03 (pipeline), B08 (CALLS schema),
  B10 (Your-Turn extended).
- Native portrait media (2160×3840) copied unchanged from
  `<parent>/vertical/media/` and `<parent>/vertical/mp3/`.
- Media file SHA256s verified against parent vertical: all 8 beats match exactly.
- Compiler stamp: `8/8 filled — B00:VIDEO B01:VIDEO B04:VIDEO B05:VIDEO
  B06:VIDEO B07:VIDEO B09:VIDEO B11:VIDEO`.
- No endcard added; parent outro (B11) preserved.
- CUT-PLAN.json checked in beside this report.

## 2. Duration — strictly under 180 s

`ffprobe -v error -show_entries format=duration,stream=codec_type,duration,width,height
-of json exports/short/claude-liam-brutalist-skill-fashionista-short.mp4`

| Signal | Value | Rule | Result |
|---|---|---|---|
| Container `format.duration` | 160.833 s | < 180.0 | PASS (19.17 s headroom) |
| Video stream duration | 160.791667 s | < 180.0 | PASS |
| Audio stream duration | 160.833 s | < 180.0 | PASS |
| Planned timeline (beat sheet sum of `render_duration_s`) | 160.83 s | ≤ 175 s | PASS |
| Container video width×height | 2160×3840 | 9:16 native | PASS |
| Export SHA-256 | `9e55bb80195c6365f2e808538b291764921eb5795baf703adaa8bb4ce3a0edcd` | matches build-state.json | PASS |

## 3. Audio decode

`ffmpeg -i <master> -af volumedetect -vn -sn -f null /dev/null`

- `mean_volume: -27.0 dB` (well above the −40 dB SKILL.md audio gate).
- `max_volume: -2.9 dB` (no clipping).
- Per-beat mp3 files enumerated in the compiler's `.verified.json`
  input manifest; each was copied atomically from the parent's
  `vertical/mp3/` and hashed by the compiler.

## 4. Static / semantic linters (compile.py)

- Slot fill: 8/8 filled (`--allow-slates` not needed; final rejects slates).
- Skin lint (warnings only, retained by design):
  - `B00: palette=claude but the cold open is 'ClaudeComposerAsk916'` —
    the 916 wrapper is the correct portrait cold-open composition; the
    landscape COLD OPEN LAW string check does not know about 916 suffixes.
  - `B11: palette=claude but the outro is 'ClaudeTitleOutro916'` — same,
    for OUTRO LAW. `OUTRO-LOCK.md` behaviour (handle `@NikBearBrown`,
    slug-seeded mascot) is unchanged and confirmed in the last-frame image.
- Motion histogram: `reveal:5  type-on:2  hold:1`. Compiler warned the
  `reveal` share (5/8, 62%) exceeds the ~40% MOTION.md cap. This is a
  Short-length artefact from dropping four middle mechanism beats. The
  compiler's warning is retained in this report; no repair (converting
  a mechanism `reveal` to another language would degrade legibility on the
  8-beat Short).
- Beat sheet validation (`build_safety.validate_project`): passed; `metadata`
  slug/aspect/kind consistent (`slug: claude-liam-brutalist-skill-fashionista-short`,
  `kind: short`, `aspect_ratio: 9:16`, `voice: am_onyx`, `captions: false`,
  `playlist: Brutalist`, `short_validation.status: ready`).

## 5. Visual review (evidence)

Frames under `_qc/`; per-file SHA-256s recorded in VISUAL-REVIEW.json
(run_id `5112069ad63347e9ab02657ed099ad9d`).

Inspected directly this run:

- `_qc/first.jpg` — cream ground; the ClaudeComposerAsk916 card hold before
  fade-in (expected — `at: 0.02` show note). No bleed, no caption.
- `_qc/B00-p50.jpg` — composer card, `BRUTALIST · SKILL TEARDOWN` eyebrow,
  `The fashionista Skill` title, `Hallo, Liam`, ask text, folder label
  `@HumanitariansAI`, three-line running output (`an experiment, not a
  fashion series` / `the audience is the scoring function` / `hedging is the
  content, not weakness`), terracotta send button armed. Portrait framing
  correct; all ink inside safe area.
- `_qc/B07-p50.jpg` — `FALSIFIABILITY · ACT 4` / `Two stacked errors.`
  heading, GENERATOR ERROR / DESCRIBER ERROR body, verbatim quote block
  (`"Nobody else is doing this and it is the most interesting thing the
  series does."`), `NOBODY ELSE SEPARATES THE TWO LANES` verdict pill,
  `Two lanes of wrongness.` spark line. Portrait safe area respected.
- `_qc/B09-p85.jpg` — ClaudeVerdictArtifact916 card, `An experiment. Not a
  series.` heading, all six numbered verdict lines fully revealed and
  legible within portrait canvas. No overflow.
- `_qc/last.jpg` — ink ground, `The fashionista Skill.` title with terracotta
  period, `@NikBearBrown` handle. OUTRO-LOCK compliant.

All 27 QC assets (first, last, contact-sheet, 3×8 beat-relative frames)
present and hashed in VISUAL-REVIEW.json.

## 6. Blockers / majors

None. See VISUAL-REVIEW.json (`blockers: 0`, `majors: 0`).

Minor / documented:
- Compiler motion-histogram warning as noted in §4. Retained.
- Skin-lint warnings for the 916 wrappers as noted in §4. Retained.

Human review is pending (Bear's viewing/editing is next). This report does
not claim human approval.
