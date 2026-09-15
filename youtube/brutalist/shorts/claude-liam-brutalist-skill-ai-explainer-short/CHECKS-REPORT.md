# CHECKS-REPORT — Short cut

Reel: `The ai-explainer Skill — Short` · slug `claude-liam-brutalist-skill-ai-explainer-short`
Run: 2026-09-08 · This invocation `run_id` `45f186bf1fca4b968ee2e25954316048`.

This is a DERIVATIVE cut of the parent long-form vertical companion. Every retained beat's video and audio was reused unchanged (byte-for-byte copies of `parent/vertical/media/<BID>.mp4` and `parent/vertical/mp3/beat-<BID>.mp3`). No Remotion render ran. No Kokoro synth ran. No paid API was called. The parent film and its exports were not modified.

## What was compiled

- Aspect: 9:16 native portrait, 2160×3840 (from parent's native portrait media, no re-render).
- Frame rate: 24 fps · Video: h264 `yuv420p` crf 16 · Audio: AAC 48 kHz stereo, per-beat MP3 preserved.
- Timeline: 147.916667s planned · 147.916667s measured video · 147.916000s measured audio · 147.916667s container.
- 9/9 beats filled from `media/<BID>.mp4` — 0 slates.
- Compiled Short: `exports/short/claude-liam-brutalist-skill-ai-explainer-short.mp4` (9.06 MiB).

## Cut evidence

See `CUT-PLAN.json` for the full plan and per-beat rationale.

- Strategy: **whole-beat-cut** (no rewrite needed).
- Dropped: **B02** (generic skill-folder anatomy, 17.54s) and **B09** (extended Your Turn, 21.46s). Combined savings 38.72s.
- Kept: B00 (ASK), B01 (BLUF), B03 (FRAMEWORK), B04 (MECHANISM · ACT 1), B05 (MECHANISM · ACT 2), B06 (MECHANISM · ACT 3), B07 (FALSIFIABILITY), B08 (VERDICT), B10 (OUTRO).
- Internal references intact: B05 "Second decision" → B04 "first design decision"; B07 "missing Beat two" → B01 BLUF; B07 "wallpaper reel" → B05 ILLUSTRATE LAW; B07 "stale outro handle" → B10 outro; B08 verdict bullets each map to a retained beat.
- `metadata.channel_title` renamed to `metadata.channel` to avoid the portrait-bleed pattern documented in the `channel-title-portrait-bleed` feedback memory (this toolkit's `compile.py` still uses the un-patched `H-h-40` overlay Y).
- Outro (B10) is the parent's `ClaudeTitleOutroHAI916` unchanged; no `--rewrite-outro` and no endcard.

## Actual commands run

```
python3 runtime/scripts/shorts.py \
  /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/youtube/brutalist/claude-liam-brutalist-skill-ai-explainer/vertical \
  --output-dir /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/youtube/brutalist/shorts/claude-liam-brutalist-skill-ai-explainer-short \
  --slug claude-liam-brutalist-skill-ai-explainer-short \
  --drop B02 B09 --no-endcard --no-outro-rewrite

python3 runtime/scripts/compile.py \
  /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/youtube/brutalist/shorts/claude-liam-brutalist-skill-ai-explainer-short \
  --height 3840 \
  --out /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/youtube/brutalist/shorts/claude-liam-brutalist-skill-ai-explainer-short/exports/short
```

`shorts.py` reported "9 beats · ~147.9s (2:27.9) OK" and "native portrait reused unchanged" for every retained beat. `compile.py` reported "9/9 filled" with all statuses VIDEO and no slates. Two skin-lint warnings were emitted (`ClaudeComposerAsk916` cold open, `ClaudeTitleOutroHAI916` outro) — both inherited from the parent's Claude-palette / native-HAI-outro substitution and are the same warnings recorded in the parent's build stamp; they are not a Short-specific regression.

## Duration gates (strictly < 180.0s)

`build_safety.SHORTS_CAP_S = 180.0` — the compiler enforced this on:

- The measured timeline (`compile_reel` → `require_short_duration(sum(beat_duration), 'Measured Short timeline')`).
- The encoded container duration (`verify_output` → `require_short_duration(duration, 'Encoded Short container')`).
- Every video/audio stream duration (`verify_output` per-stream loop).

Measured (ffprobe):

| Stream | Duration | Under 180.0? |
|---|---:|:---:|
| Container `format.duration` | 147.916667 s | ✅ (32.08 s headroom) |
| Video stream `duration` | 147.916667 s | ✅ |
| Audio stream `duration` | 147.916000 s | ✅ |

The `.verified.json` written by `compile.py` records `duration_s: 147.916…` and `sha256: c62879fe…` for the final container.

## Frame-level visual QC (spot inspection, actual)

Contact sheets extracted from the compiled portrait Short:

- `_qc/beat_frames/<BID>_015.jpg`, `_050.jpg`, `_085.jpg` — 27 samples (9 beats × 3 phases), 1080×1920 (downsampled 2× from the 4K source for storage).
- `_qc/frames/f_0001.jpg` … `f_0296.jpg` — 296 samples at 2 fps (every 0.5 s), 540×960 thumbs.

Every frame path is hashed in `VISUAL-REVIEW.json` with a fresh SHA-256 from this run.

Human-loaded mid-frames spot-checked with the Read tool (six beats — cold open, BLUF, framework, tell, verdict, outro):

| Beat | Scene | 50% frame check |
|---|---|---|
| B00 | ClaudeComposerAsk916 | "Hej, Liam" greeting, prompt text visible, @HumanitariansAI folder tag, three output lines resolved, terracotta send + running-indicator asterisk, cream ground, spark on the left margin. All copy inside safe area. |
| B01 | HesitantWriterFramed916 | Mid-correction: "The ai-explainer skill / is a workflow. / I|" (about to retype the third line). Spark line `A workflow, not a template.` anchored above bottom rule. Serif face, ink on cream. |
| B03 | SkillTeardownPipeline916 | Portrait stack: INPUT (SKILL.md + topic) → Scaffold → Narrate → Audio (terracotta card) → Visuals → Compile → OUTPUT `<slug>.mp4`. Footer note + spark line both fit above safe.b. |
| B07 | SkillTeardownMechanism916 | Heading "Where it bites." + "unread rule ships as a bug… Liam is a named substitute" body + IN-FOR-BEAR LAW quote card + neutral "REQUIRES A READER" pill + spark line. All inside safe area. |
| B08 | ClaudeVerdictArtifact916 | Six numbered lines (workflow / bookends / UI earns beat / prompts as receipts / Kokoro clock / renders only) all fit legibly on the artifact card; terracotta numerals; cream card on cream ground. |
| B10 | ClaudeTitleOutroHAI916 | Dark outro card: "The ai-explainer / Skill." with "@HumanitariansAI" beneath. Framing rules inside safe area. |

**Result: blockers 0, majors 0.** No edge-bleed, underfill, or low-contrast defect found in the spot inspection. See `VISUAL-REVIEW.json` for the full frame manifest.

## Metadata integrity

- `metadata.kind = "short"` (required for the compiler's Short-cap gates).
- `metadata.aspect_ratio = "9:16"`, `metadata.captions = false`, `metadata.voice = "am_onyx"`, `metadata.voice_kokoro = "am_onyx"`, `metadata.playlist = "Brutalist"`, `metadata.channel = "@HumanitariansAI"` (renamed from the parent's `channel_title` — see rationale above).
- `metadata.short_validation = { status: "ready", errors: [] }` — set by `shorts.py`.
- `metadata.dropped_beats = ["B02", "B09"]`, `metadata.derived_from = "claude-liam-brutalist-skill-ai-explainer-vertical"`.
- `metadata.build` was re-stamped by `compile.py` (9/9 filled, no slates, cut=master).

## Provenance

- Parent reel: `youtube/brutalist/claude-liam-brutalist-skill-ai-explainer/`.
- Parent vertical beat sheet SHA-256: `2a3180835a89524f132558d6de7b83fcaf384cc5e8e1c9f9cc3cbb0030e308e5`.
- Parent 2160×3840 master SHA-256: `d8dca0f414440a0816284375159ce89da59284b549735f26aaa9dc7bf46e9cb5` (not modified; not re-encoded).
- This Short's final master SHA-256: `c62879fe949ae2d67afc814d2b3726e7bce83afb2731a5c1c3611f90b0965e93`.
- This Short's beat sheet SHA-256: recorded in `VISUAL-REVIEW.json`.

## Publishing / distribution

Explicit non-actions — the Shorts contract forbids all of these:

- No upload, no push, no publish attempt.
- No credentials read or written.
- No related-video selection.
- No fabricated human approvals; `metadata.approvals = {}`.
- No signature reused; `presenter` stays "Liam (in for Bear)".
