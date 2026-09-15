# CHECKS-REPORT — Brutalist Utility: build_cli_d3_reels.py — Short

## Re-verification — 2026-09-13 · run_id 9e7c8cd745cc42dfb5d20355e43ac2e0

Source trigger: peripheral changes in build_safety.py, compile.py, shorts.py, and skills/make/\*.md files; parent vertical beat_sheet.json, media files, and mp3s unchanged. All 6 Short media files and mp3s confirmed via SHA-256 — exact match to original build (see `exports/short/*.verified.json`). Export file SHA-256 confirmed: `879ddc4b8277e37aec3e82786d879f962b19ab690308df8b1d309804f5bd7f02`. Duration re-measured: 96.958s container, 96.917s video, 96.958s audio — strictly under 180.000s. All 18 beat-relative frame files re-hashed and confirmed unchanged. VISUAL-REVIEW.json updated with this invocation's run_id and source_sha256. beat_sheet.json run_id updated to 9e7c8cd745cc42dfb5d20355e43ac2e0. No re-render required; no parent files modified.

---


## Ship

- Output: `exports/short/claude-liam-brutalist-runtime-build-cli-d3-reels-short.mp4`
- SHA-256: `879ddc4b8277e37aec3e82786d879f962b19ab690308df8b1d309804f5bd7f02`
- Container duration (ffprobe): `96.958000s`
- Video stream duration (ffprobe): `96.916667s`
- Audio stream duration (ffprobe): `96.958000s`
- Dimensions: `2160 × 3840` (h264, 24 fps, 2326 frames)
- Audio: `aac` per-beat timeline (source Kokoro `am_onyx` MP3s preserved unchanged)
- All three measured durations are **strictly under the 180.000s Shorts cap** with 83s of headroom.

## Cut plan

- Strategy: `whole-beat-cut` (see `CUT-PLAN.json`).
- Parent: 12 beats · 234.8s · `849929b4cbd476cb0782fa8359926923ba58132902db4008a883a29242aa7d17`.
- Kept 6/12: B00 · B01 · B02 · B07 · B09 · B11.
- Dropped 6/12: B03 · B04 · B05 · B06 · B08 · B10 (each a code-cascade walkthrough or the long-form Your-Turn CTA — belong in the 16:9 long).
- Planned duration: 96.96s. Measured duration: 96.96s. Match.

## What ran

1. `python3 runtime/scripts/shorts.py <parent>/vertical --output-dir <reel> --slug claude-liam-brutalist-runtime-build-cli-d3-reels-short --drop B03 B04 B05 B06 B08 B10 --no-endcard --no-outro-rewrite`
   - Output: "6 beats · ~97.0s (1:37.0) OK"; every kept beat resolved as "native portrait reused unchanged".
2. `python3 runtime/scripts/compile.py <reel> --height 3840 --out <reel>/exports/short`
   - Output: "6/6 filled" · every beat status VIDEO · wrote 97.0s master.

No `remotion_scenes.py` re-render was needed — all 6 kept beats are Remotion `*916` compositions already rendered in the parent's vertical/media/. No audio was regenerated (no rewritten outro). Compile ran without `--review` per rule (no `[REVIEW]` overlay on the shippable file).

## Rules honored

- SHORTS LAW: 96.958s < 180.000s (final measured, all three streams).
- No parent files touched (`youtube/brutalist/claude-liam-brutalist-runtime-build-cli-d3-reels/**` is read-only from this workspace's perspective; shorts.py copied files, never symlinked).
- No unrelated toolkit files touched.
- No ElevenLabs. No paid API calls. No credentials read. No `.env` accessed.
- No `--review` on the final compile. No burned-in captions. No subtitle track.
- Native 2160 × 3840 output. No aspect-ratio crop from a landscape master.
- Outro `@NikBearBrown` handle preserved (parent B11 unchanged).
- No git commits, no publish, no upload.

## Slots

- 6/6 filled — every beat has both media/*.mp4 and mp3/beat-*.mp3, verbatim from the parent.
- 0 slates, 0 blockers, 0 majors.

## Skin lint (benign, inherited from parent)

- B00: pattern `ClaudeComposerAsk916` — expected; the 916 suffix is the portrait variant used across every playlist Short.
- B11: pattern `ClaudeTitleOutro916` — expected; same reason.

Compile.py's SKIN LINT is written against the landscape base names; the 916 variants are the correct portrait renders for a Short. Not a defect.

## Provenance

- Beat sheet SHA-256: `7353fdb610969a9cce6d3241c9efdc6e37d4863ec3bfd0541a91f17f006d7070`
- Beat media/mp3 SHA-256 recorded in `exports/short/*.verified.json`.
- Full frame-evidence hashes in `VISUAL-REVIEW.json` (18 frames at beat-relative 15/50/85 %, plus a full 2 fps sweep in `_qc/f_*.png`).

## Waiting on

Human viewing (Bear) — no other blocker.
