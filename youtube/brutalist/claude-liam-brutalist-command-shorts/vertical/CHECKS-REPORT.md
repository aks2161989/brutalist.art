# CHECKS-REPORT — vertical (9:16, full-length companion)

run_id: `915961a4e22f469590e497ffe1dd9a7f` (re-verified; original build run_id `f2da2cc936694334b92c9a741e8f66e2`)

## Re-verification note (run_id 915961a4e22f469590e497ffe1dd9a7f)

The previous run left `exports/vertical/...verified.json` with hash `4ef22048...` while the actual video had hash `3481e57f...`. The video was correct (built after B02/B03 fix) but the verified.json was not regenerated. Root cause: compile.py wrote `build-state.json` correctly but `verified.json` was left from the prior compilation run. Fix: re-ran `compile.py <vertical_reel> --height 3840 --out exports/vertical` (no --force; existing conformed clips used). The recompile is deterministic — same inputs produced the identical `3481e57f...` MP4. `verified.json` now matches. VISUAL-REVIEW.json updated to this run_id with new beat_sheet_sha256 (compile stamp updated it).

## Source change summary (this revision)

Same as landscape: `art` dispatcher `shorts` case shifted from lines 81-83 to **102-104**, `vertical` case from 84-86 to **105-107**. `shorts.py` SHORTS LAW rules 2/3/4 expanded. B02 ClaudeCodeBeat916 title corrected; B03 code card updated to remove "verbatim" claim.

## What actually ran and passed

- **B02/B03 re-render (portrait)** — `remotion_scenes.py <reel>/vertical --only B02 --force` and `--only B03 --force` using the `ART_CHROME` chrome-wrapper. Both succeeded: `ClaudeCodeBeat916 → media/B02.mp4`, `ClaudeCodeBeat916 → media/B03.mp4`.
- **Reused mp3s** — the same 12 mp3s stamped by `generate_audio_kokoro.py` for
  the landscape master were copied into `vertical/mp3/`. Same narration,
  same durations, same voice (Kokoro `am_onyx`).
- **Compile master** — `python3 runtime/scripts/compile.py <reel>/vertical --height 3840 --force`
  wrote `exports/vertical/claude-liam-brutalist-command-shorts-vertical.mp4`
  (2160×3840 · 296.3s · h.264 + AAC), 12/12 beats filled.
- **Gate V — final_frame_check** — `runtime/qc/final_frame_check.py` → **0 BLOCKER / 0 MAJOR** (24 frames sampled). Contact sheet at `_qc/contact_sheet.png`.
- **Own-eye visual review** — `_qc/contact_sheet.png` and `_qc/final-contact-sheet.png` opened with image-capable Read tool. B00 ClaudeComposerAsk916 portrait composer; B01 BrutalistHesitantWriter916 "art shorts / drops beats / and rewires / graphics." corrected BLUF; B02-B08 ClaudeCodeBeat916 portrait code cards inside safe area; B09 ClaudeVerdictArtifact916 verdict; B10 ClaudeComposerAsk916 Your Turn; B11 ClaudeTitleOutro916 outro.

## Toolkit adjustments needed for this build

1. `Root.tsx` did not register `ClaudeCodeBeat916` — I added a composition
   using the same `ClaudeCodeBeat` component at width 1080 × height 1920. The
   scene is already responsive to `useVideoConfig` (padding/font sized in
   `width * 0.07` / `height * 0.022`), so no scene edit was needed.
2. `BrutalistHesitantWriter.tsx` had `const scale = Math.min(width/1920,
   height/1080)` which collapses to 0.5625 in portrait. Applied the
   3-line patch:
   ```ts
   const scale = height > width
     ? Math.min(width / 1080, height / 1920)
     : Math.min(width / 1920, height / 1080);
   ```
3. `metadata.channel_title` was removed from the vertical beat_sheet.json so
   the compile-time PIL overlay does not push past `safe.b` in portrait.
   The composer's `folderLabel` chip in B00 / B10 still carries
   `@HumanitariansAI`.

## Blockers repaired during this build

1. **Portrait edge-bleed on B00, B10** — the composer's `command` +
   `output[]` fields were long enough to push the bubble past `safe.b`
   (3648 of 3840). Trimmed both. Re-rendered only B00 and B10, then
   recompiled the master. Now the ink bbox sits at y ≤ 1785 of 1920.
2. **Portrait underfill on B01** — the shortened landscape 2-line text
   dropped to 19% fill in portrait. Rewrote to 4 short lines at
   `fontSize: 180 / lineSpacing: 2.6` per the portrait BLUF recipe:
   `art shorts / speeds beats / and crops / graphics.` → `art shorts /
   drops beats / and rewires / graphics.`. Fill jumped to 73%.

## Available runtime checks used

| Gate | Script | Result |
|---|---|---|
| F (paperwork) | compile.py precondition | pass — FACTCHECK.md · SHOTLIST.md · PROMPTS.md present in vertical/ |
| L (beat-mix lint) | compile.py | pass — code-cascade WARNING carries over from landscape (same shape, same intentional emphasis) |
| D (audio decode) | compile.py `verify_output` | pass — 12 audio segments; 296.291 s |
| V (frame check) | runtime/qc/final_frame_check.py | pass — 0 BLOCKER, 0 MAJOR |

## Skin-lint warnings (not defects)

`compile.py` emits two SKIN LINT warnings:
- `B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk`
- `B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro`

These are expected on vertical: the …916 variants are the portrait-native
compositions, which is precisely what the ONDA CHECK rewires to. The lint
was designed for landscape reels and does not know about the vertical fork.
Flagged here for the human reviewer.

## Not attempted

- Same limitations as landscape CHECKS-REPORT.md: no fresh network install,
  no `--rewrite-outro` demo, no captured-media center-cut path.
