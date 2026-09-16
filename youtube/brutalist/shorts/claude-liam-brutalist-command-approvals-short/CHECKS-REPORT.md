# CHECKS-REPORT — Brutalist Command: art approvals — Short (9:16)

Run ID `9183b88ae09845c39f780928e0b7b10a`. Reviewer type: AI. Human review pending.

## Rebuild reason

Parent vertical B06 and B09 were re-rendered 2026-09-12 (sparkLine and NOTES.md gate check added to B06; B09 Verdict line 3 updated to name B05/B06 auto-arm in fellows reels). Parent master SHA changed from `0fba75ff…` to `4fd6fbab…`. Short media for B06 and B09 copied from parent vertical; both beats recompiled.

## Cap check — strictly under 3:00

- Container duration (ffprobe format=duration): **126.750 s**
- Video stream duration: 126.750 s
- Audio stream duration: 126.750 s
- Sum of per-beat `render_duration_s` in `beat_sheet.json`: 126.75 s
- Shorts cap: 180.000 s (strict `<`)
- **PASS** — 53.25 s under the cap, comfortably below the 175 s planning ceiling in the BRIEF.

## File contract

- Output path: `youtube/brutalist/shorts/claude-liam-brutalist-command-approvals-short/exports/short/claude-liam-brutalist-command-approvals-short.mp4`
- Dimensions: 2160 × 3840 (native 4K portrait, 9:16)
- Video codec: h264, 24 fps
- Audio codec: aac, 48 kHz, stereo
- Container: mp4
- SHA-256: `b2a0de33775471e2fd923e22487732f66afd89f7fd9605c535155b12774bba35`
- Beat sheet SHA-256: `09f1bdb14cc1df7bf5e9d0742d21a833413d7d27ff5dcda74e15ba09c0e75293`
- File size: 9,714,238 bytes (≈9.3 MB)

## Cut plan

- Strategy: whole-beat-cut (no rewrite)
- Kept: B00, B01, B03, B05, B06, B08, B09, B11 (8 beats)
- Dropped: B02, B04, B07, B10 (see `CUT-PLAN.json` for per-beat reasons)
- Endcard: none (`--no-endcard`)
- Outro rewrite: none (`--no-outro-rewrite`); parent B11 preserved verbatim.

## Beat rewire / re-render check

- Every kept `shot.remotion.pattern` already ends in `916` in the parent's vertical build; every corresponding composition is registered in `runtime/remotion/src/Root.tsx`.
- ONDA CHECK: 0 rewires, 0 blocked. Native portrait media reused unchanged from parent vertical (B06 and B09 are updated Sep 12 renders).
- No audio was regenerated. Parent Kokoro `am_onyx` MP3s for the kept beats were copied verbatim.

## Audio decode

- Decoded end-to-end with `ffmpeg -af volumedetect -f null /dev/null`.
- mean_volume: **−26.9 dB**
- max_volume: **−5.0 dB**
- No decoder errors, no dropped frames, no PTS discontinuities in the log.

## Frame extraction

- Beat-relative sampling at 15%, 50%, 85% for each kept beat: **24 frames** written to `_qc/beat-frames/`. Every frame is hashed and recorded in `VISUAL-REVIEW.json`.

## Visual review (per beat)

| Beat | 50 % frame content | Legibility | Portrait framing |
|---|---|---|---|
| B00 | Composer card + `Selam, Liam` greeting + typed ASK + 3-line running output under `@HumanitariansAI` folder chip | clear serif + composer text; running text soft-wraps inside safe area | clean; nothing bleeds |
| B01 | BLUF landing frame — "art approvals / inspects / subjects." large serif, one word per line | crisp | centered; well within safe area |
| B03 | argparse surface + two-branch main() + metadata.approvals shape | code monospace legible; right-edge soft-truncation on long lines is inherited from the parent 4K render and is a known cosmetic ClaudeCodeBeat916 behavior on very long lines (does not obscure any keyword the narration names) | terminal card centered, spark line reads |
| B05 | Fellows fixture metadata + first `--fingerprints` JSON with `voice.subject_sha256` visible | legible; SHAs deliberately elided in mid | inside safe area |
| B06 | **Updated 2026-09-12**: 5-field record + exact fail-close conjunct + NOTES.md extra gate check; sparkLine reads "Five fields. Human, dated, verbatim — and NOTES.md non-empty." | legible; every field label reads; extra gate line visible | inside safe area |
| B08 | BEFORE / EDIT / AFTER / RECOVERY stack, `[safety] REFUSED` visible | legible; refusal line reads | inside safe area |
| B09 | **Updated 2026-09-12**: Verdict artifact with 6 numbered lines; line 3 now reads "professor_notes arms on requires_approval, a feedback act, or B05/B06 in a fellows reel" | all 6 lines read; updated line 3 legible | artifact centered inside safe area |
| B11 | `Brutalist Command: art approvals.` outro + `@NikBearBrown` handle | serif crisp; terracotta period reads | centered; mascot animates below (single sampled frame is between beats of the animation) |

Blockers: 0. Majors: 0.

## Compiler warnings (surfaced, not blockers)

- `motion histogram: code-cascade:4 / type-on:1 / hesitant-type:1 / artifact-in:1 / outro-card:1` — `code-cascade` at 4/8 (50 %) is above the ~40 % pantry cap the compiler warns about. This is a consequence of the cut (three of four dropped beats are non-code-cascade). Editorially acceptable for the Short because the 16:9 long already carries the motion variety; the Short's purpose is dense mechanism. Not a blocker.
- `SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916'` and `SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916'`. Both are the shipped compositions used across the entire Brutalist playlist and were already surfaced (and left) on the parent build.

## Constraints upheld

- ✅ Parent 16:9 film and full-length vertical are untouched — nothing was written outside the Short's `reel` directory.
- ✅ Native 2160 × 3840. Container/video/audio all < 180 s.
- ✅ No paid API, no upload, no publishing action, no git push.
- ✅ No captions, no subtitle stream added.
- ✅ No credentials or private paths in narration.
- ✅ Independent file copies (`shutil.copy2` via `copy_asset`); no symlinks or hardlinks in the Short reel.
- ✅ Previous rendered Short export (126.75 s, `8c1374ad…`) preserved until replacement passed all current gates; replacement now in place.

## Final verdict

**PASS.** Rendered artifact: `youtube/brutalist/shorts/claude-liam-brutalist-command-approvals-short/exports/short/claude-liam-brutalist-command-approvals-short.mp4` — 126.75 s, 2160 × 3840, 8 beats. Human review is the next step.
