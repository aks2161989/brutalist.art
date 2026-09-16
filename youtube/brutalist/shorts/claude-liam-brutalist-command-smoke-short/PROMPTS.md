# PROMPTS.md — Brutalist Command: art smoke — Short

No new generation prompts were issued for this Short. Every kept beat's
video was reused byte-identical from the parent reel's finished portrait
renders at `youtube/brutalist/claude-liam-brutalist-command-smoke/vertical/media/`,
and every kept beat's audio was reused byte-identical from
`youtube/brutalist/claude-liam-brutalist-command-smoke/vertical/mp3/`.

## What was actually invoked

- `runtime/scripts/shorts.py <parent>/vertical --output-dir <this-reel>
  --slug claude-liam-brutalist-command-smoke-short
  --drop B02 B04 B05 B06 B09 --no-endcard --no-outro-rewrite`
  — copied the six kept beats + mp3s into this reel, rewrote
  `beat_sheet.json` with `kind: short`, `aspect_ratio: 9:16`, remotion
  patterns rewired via the Onda check to the existing `…916` portrait
  compositions (which were already the parent's native portrait).
- `runtime/scripts/compile.py <this-reel> --height 3840
  --out <this-reel>/exports/short` — assembled the six clips into the
  final 2160×3840 mp4 and produced `_qc/contact_sheet.png` + Gate V report
  (0 BLOCKER, 0 MAJOR across 12 sampled frames).
- Local frame extraction at beat-relative 15 / 50 / 85 % of every kept
  beat, written to `_qc/per-beat/<BID>_<pct>.png` and hashed for
  VISUAL-REVIEW.json.

## What was **not** invoked

- No Kokoro (`generate_audio_kokoro.py`) run in this reel. All narration
  is copied.
- No Remotion re-render (`remotion_scenes.py`). All portrait renders are
  copied.
- No paid API, no upload, no publishing, no network calls.
- No `--review` flag; the compile was the final pass, not a preview.

## Original generation prompts (retained in the parent reel)

The parent's `PROMPTS.md` documents every original Kokoro-narration prompt
and Remotion composition invocation. Nothing in this Short deviates from
those prompts; they were used exactly as the parent recorded them.
