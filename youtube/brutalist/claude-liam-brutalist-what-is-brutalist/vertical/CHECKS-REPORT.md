# CHECKS-REPORT.md — What Is Brutalist? · 9:16 portrait companion

*Original build run ID: `7c55b78a2b834162813babc7e106ae2b`. Re-verified under run ID: `51ec9474e1e84326a919a39b823dcfaa`. Portrait companion is independent from the landscape review; the parent's audio and paperwork are shared, the scenes and compile are its own.*

## Beat classification (same as landscape)

10 SHOW / 0 justified-HOLD / 0 PUNT. Teaching-arc rubric per
`skills/make/nopunt/SKILL.md`: FRAMEWORK ✓ · WORKED EXAMPLE ✓ ·
FALSIFIABILITY ✓ · SCAFFOLDED TASK ✓ · BOOKENDS ✓ · NO-SOURCE-NO-VERDICT ✓.

## Runtime commands and their observed outputs

### 1. `art vertical` — plan (foreground, no side effects)

```
./art vertical <reel>
```

- 10 beats retained, full length ~170.3 s.
- Every REMOTION pattern rewired to its `-916` id:
  `ClaudeComposerAsk → ClaudeComposerAsk916`,
  `BrutalistHesitantWriter → BrutalistHesitantWriter916`,
  `WibRecipe → WibRecipe916`, `WibPipeline → WibPipeline916`,
  `WibChange → WibChange916`, `WibDivision → WibDivision916`,
  `WibNotClaims → WibNotClaims916`, `WibVerdict → WibVerdict916`,
  `WibOutro → WibOutro916`.
- Wrote `vertical/beat_sheet.json` with slug
  `claude-liam-brutalist-what-is-brutalist-vertical` and
  `metadata.aspect_ratio: "9:16"`.
- Copied per-beat mp3s to `vertical/mp3/`.

### 2. Portrait scene renders

```
ART_CHROME=<wrapper> ART_CHROME_MODE=chrome-for-testing \
python3 runtime/scripts/remotion_scenes.py <reel>/vertical --force
```

Result — 10/10 beats rendered natively at 2160x3840 (portrait 4K via
`--scale=2` on 1080x1920 compositions). Same Chrome-sandbox wrapper as the
landscape build — see `../CHECKS-REPORT.md § Environment note`.

### 3. Compile — portrait 4K master

```
python3 runtime/scripts/compile.py <reel>/vertical \
  --height 3840 --out <reel>/exports/vertical --force
```

Result:
- All 10 beats conformed to their measured audio durations (same clock as
  landscape — narration mp3s are shared).
- `Gate V (frame-level visual QC)`: **20 frames sampled · 0 BLOCKER · 0 MAJOR ·
  "Clean — no BLOCKER/MAJOR defects. ✓"** (`_qc/REPORT.md`).
- Compiler's atomic verification produced
  `exports/vertical/claude-liam-brutalist-what-is-brutalist-vertical.mp4`
  and its `.verified.json` receipt (state `ready`).
- Skin lint reported:
  - `B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD
    OPEN LAW wants ClaudeComposerAsk`. **Expected** — the `-916` suffix IS
    the correct portrait composition id (per the `art vertical` planner
    output and the toolkit's rule #4). The lint is a landscape-only string
    match and does not gate the build.
  - `B09: palette=claude but the outro is 'WibOutro916' — OUTRO LAW wants
    ClaudeTitleOutro`. **Deliberate.** Same as landscape — `ClaudeTitleOutro`
    hardcodes `@NikBearBrown` per `OUTRO-LOCK.md` and this reel is on the
    `@HumanitariansAI` channel. `WibOutro916` is the required native custom
    outro variant for the HAI channel.

### 4. Post-encode probes

- Dimensions: **2160 x 3840**, H.264, duration **170.416667 s**.
- Audio: **AAC**, duration **170.458 s**, `mean_volume -27.3 dB`,
  `max_volume -3.0 dB` — non-silent, decodes cleanly.

### 5. Frame extraction and visual inspection

- `ffmpeg … -vf fps=2` → 341 PNGs in `vertical/_qc/frames/`.
- `vertical/_qc/contact_sheet.png` Read directly. Full-resolution samples
  (`v3_B05_85.png`, `v2_B*_85.png`, and inspection sets during iteration)
  Read at 4K resolution during the underfill/edge-bleed debug loop.
- No overlap, clipping, offscreen anchors or unresolved slates. Outro reads
  `What Is Brutalist?` and `@HumanitariansAI` and the subline `LIAM, IN
  FOR BEAR.`.

## Iteration history (what the initial portrait compile flagged, and the fixes)

The first portrait compile failed Gate V with 12 BLOCKER + 2 MAJOR:
- 6 beats had top-edge bleed because the WhatIsBrutalist components used
  `top: portrait ? 68 : 56` — 68 < the portrait safe.y = 96. Fix: bumped
  eyebrow to `portrait ? 130 : 56` and title to `portrait ? 175 : 82`.
- B02 had bottom-edge bleed because the split-panel bottom card exceeded
  1824. Fix: pinned `leftY = 210, leftHFit = 700, rightHFit = 700` in
  portrait so `leftY + leftHFit + gap + rightHFit ≤ 1670 < 1824`.
- B05 had left-edge bleed because the italic SparkLine at `padX = 54`
  (portrait) had a small italic overhang crossing safe.x = 54. Fix: SparkLine
  now uses `padX = 96` uniformly.
- B07 had top/bottom bleed because WibVerdict's card used
  `cardY = pad = 54` and `cardH = height - pad*2`. Fix: WibVerdict uses
  `cardY = padY (130)` and `cardH = height - padY*2` for portrait.
- B01 had underfill (20% then 55% at threshold). Fix: portrait B01 uses a
  six-short-line text and `fontSize: 380` (the landscape 200/three-line
  layout would clip on the narrower portrait canvas). Final fill: >55%.

After the fixes, Gate V passes clean (0/0).

## Available runtime checks — status (same set as landscape)

| Check | Ran | Result | Notes |
|---|---|---|---|
| `runtime/scripts/build_safety.py::validate_project` | ✓ | pass | via compile.py |
| `runtime/scripts/build_safety.py::require_paperwork` | ✓ | pass | FACTCHECK/SHOTLIST/PROMPTS present |
| `runtime/scripts/build_safety.py::validate_approvals` | ✓ | pass | Not fellows-typed |
| `runtime/qc/final_frame_check.py` (Gate V) | ✓ | pass | 20 frames, 0/0 |
| ffprobe dimension check | ✓ | pass | 2160x3840 |
| ffmpeg volumedetect | ✓ | pass | mean_volume -27.3 dB |
| Frame-level Read of contact sheet | ✓ | pass | See VISUAL-REVIEW.json |

## Gaps in public documentation

Same as `../CHECKS-REPORT.md § Gaps`. The missing `type_check.py` was
substituted with a visual audit (see `TYPECHECK.md` in this folder).

## Re-verification pass — 2026-09-10 (run_id 51ec9474e1e84326a919a39b823dcfaa)

Source SHA changed (same toolkit updates as landscape — see `../CHECKS-REPORT.md`).
FEEDBACK.md has no human notes. Beat sheet (f6863d41…), audio, and scene sources
are unchanged. Exports re-verified:

- `shasum` on vertical MP4 matches `.verified.json` record.
- `ffprobe`: 2160x3840, 170.416667 s, H.264 + AAC.
- Audio: mean_volume -27.3 dB, max_volume -3.0 dB — confirmed.
- Portrait contact sheet `_qc/contact_sheet.png` (SHA-256
  `86a719a0d8f8f3849c108a553316e0d0add6a482ac0334c107a7915da85804aa`) read and
  confirmed: all 10 beats, correct portrait content, no new artifacts.
- Gate V report: 0 BLOCKER, 0 MAJOR — unchanged from original build.
- `VISUAL-REVIEW.json` updated to this run_id and new source_sha256.

## Re-verification pass — 2026-09-10 (run_id 17736525ffaf4693a11ba37516aa4d5f)

Source SHA changed again (toolkit commits `ba2d0e0` and `7ee2da6` — same as
landscape; see `../CHECKS-REPORT.md § Re-verification pass 17736525`).
FEEDBACK.md has no human notes. Beat sheet (f6863d41…), audio, and scene sources
are unchanged. Exports re-verified:

- `shasum -a 256` on vertical MP4 matches `.verified.json` record:
  `c339f1b5555e847096f3ea975249042c50b86714c8a29fee20d3eb58398c3f9c` ✓
- `ffprobe`: 2160x3840, 170.416667 s, H.264 + AAC (unchanged from prior pass).
- Audio: mean_volume -27.3 dB, max_volume -3.0 dB — confirmed.
- Portrait contact sheet `_qc/contact_sheet.png` (SHA-256
  `86a719a0d8f8f3849c108a553316e0d0add6a482ac0334c107a7915da85804aa`) read with
  image-capable Read tool and confirmed visually: B00 ClaudeComposerAsk916
  'Ciao, Liam'; B01 BrutalistHesitantWriter916 large serif correction; B02–B07
  Wib*916 portrait layouts; B08 ClaudeComposerAsk916 'Your Turn'; B09 WibOutro916
  '@HumanitariansAI' handle. No new artifacts, no captions, no unresolved slates.
- Gate V report: 0 BLOCKER, 0 MAJOR — unchanged from original build.
- `VISUAL-REVIEW.json` updated to this run_id and new source_sha256.

## Conclusion

Portrait 4K master
`claude-liam-brutalist-what-is-brutalist-vertical.mp4`
(2160x3840, 170.4 s, SHA-256
`c339f1b5555e847096f3ea975249042c50b86714c8a29fee20d3eb58398c3f9c`)
passes all available runtime checks. `VISUAL-REVIEW.json` records the AI
review; human review is pending and is independent of the landscape review.
No blockers remain.
