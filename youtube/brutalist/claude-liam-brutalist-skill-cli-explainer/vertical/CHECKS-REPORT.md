# Checks — portrait (vertical companion)

Run: 2026-09-08 · run_id c1bd87ad4f3a4cbfb9163dca2cd83e44 · attempt 3 (original).
Re-verified: 2026-09-11 · run_id 1685612a4a7c43a99fc9b8f1ce087a15 · source-change re-sign.

## Runtime gates

**`art vertical` plan** — `shorts.py --vertical` invoked with `--handle @HumanitariansAI`.
- Full-length companion (no cap, no drops, no rewritten outro, no endcard).
- Every one of the 13 REMOTION beats rewired via the ONDA CHECK to its `<Pattern>916` companion:
  ClaudeComposerAsk → ClaudeComposerAsk916, BrutalistHesitantWriter → BrutalistHesitantWriter916, SkillTeardownAnatomy → SkillTeardownAnatomy916, SkillTeardownPipeline → SkillTeardownPipeline916, ClaudeCodeBeat → ClaudeCodeBeat916, SkillTeardownMechanism → SkillTeardownMechanism916, ClaudeVerdictArtifact → ClaudeVerdictArtifact916, ClaudeTitleOutro → ClaudeTitleOutro916.
- No `-916.mp4` crops of a Remotion render are used.

**Gate V (final_frame_check.py)** — sampled 26 frames (13 beats × 50%/85%) against the 2160×3840 portrait title-safe area (SAFE w=1944 h=3456). Ink bbox / SAFE-area coverage `FILL_MIN >= 0.55`.
- Command: `runtime/qc/final_frame_check.py <reel>/vertical --mp4 <candidate.mp4> --sheet <resolved-sheet.json>`
- Result: **PASS** — BLOCKER 0, MAJOR 0. `_qc/REPORT.md` reads "Clean — no BLOCKER/MAJOR defects. ✓".

**compile.py finish gate (`verify_output`)** — atomic candidate encode + probe verification of duration/frame-count/audio decode.
- Command: `runtime/scripts/compile.py <reel>/vertical --height 3840 --out exports/vertical`
- Result: **PASS** — wrote `exports/vertical/claude-liam-brutalist-skill-cli-explainer-vertical.mp4` (194.6s master, 2160x3840@24, h264, per-beat Kokoro am_onyx audio). `.verified.json` receipt written next to the master.

## Portrait iterations

Two beats needed portrait-specific tuning; both are recorded in the vertical `beat_sheet.json` and their landscape counterparts are unchanged.

**B01 — BrutalistHesitantWriter916.**
- The shipped scene applies portrait-aware scale = `min(width/1080, height/1920)` per the `hesitant-writer-portrait-scale` correction, so `fontSize` is measured against the 1080-wide portrait design ref.
- First try (fontSize 270, 3 lines): overflowed the 1944 px portrait safe width — `cli-explainer` alone (13 chars × ≈ 0.41 × 540 output px) at ≈ 2870 px would edge-bleed.
- Second try (fontSize 175, 6 lines, charMs 105): passed 85% but underfilled 50% (only 4 lines visible, 38% coverage) because the corrections finished late in the beat.
- Third try (fontSize 175, 6 lines, charMs 55): 50% at 50% coverage — still under the 55% floor.
- Final (fontSize 175, 6 lines, charMs 42, jitter 10, lineSpacing 1.14): 6 lines steady by the 50% sample, gate V clean at both samples. Widest line "commissions" (11 chars) sits inside the 1944 px safe width.

**B03 — SkillTeardownPipeline916.**
- Landscape uses 7 phases (+ INPUT + OUTPUT = 9 nodes) at a fixed 200-px max box + 42-px arrow struct; the horizontal row `9 × boxW + 8 × 42` overflows the 1944 px portrait safe width by ≈ 65 px on each side (BLOCKER `edge-bleed` on left and right).
- Fixed by reducing phases to 5 (INTRO → PROBLEM → BUILD LOOP → REVISION → HANDOFF) in the portrait sheet only. Landscape B03 keeps its 7-phase spine.
- The narrative is preserved: the abbreviated portrait spine still shows the required check-and-change (BUILD LOOP → REVISION), and the narration continues to enumerate the full 9-step landscape spine — the portrait card is the compressed view.

## Manual visual pass

Extracted mid-frames from B02, B05, B10, B11, B12 (see `/tmp/claude/vsample/`) and the compile-time `_qc/contact_sheet.png` (sha256 a8aa5896…) then read them with the image-capable Read tool.
- B02 anatomy: folder tree fits the safe column, callout stack sits mid-frame.
- B05/B08 code beats: SKILL.md excerpts render legibly at portrait line-widths — no code wrap breaks a keyword mid-token.
- B10 verdict: four numbered artifact lines stack; last line ends before the safe bottom.
- B11 Your-Turn composer: prompt types into the composer at portrait width without clipping.
- B12 outro: title `The cli-explainer Skill.` with terracotta period, handle `@HumanitariansAI` on the ink card — matches the landscape outro.

## Documented gaps

Same as the landscape file: no `scripts/type_check.py`, no `ILLUSTRATIONS.md`, no `reference/type-spec.md`, no kerning skill. Visual typography audit performed by frame Reads — see `TYPECHECK.md`.

## Re-verification notes (2026-09-11, run_id 1685612a4a7c43a99fc9b8f1ce087a15)

Source change detected: `source_sha256` changed from `e9e2b5b8...` to `050ab021...` because COMMON files changed (runtime/prose/teardown/PROSE.md renamed from voices/; REPOLOOP-PROMPT.md newly tracked). The SKILL.md content is UNCHANGED (SHA f7aab411). The beat_sheet.json was updated to record the current SKILL.md SHA. All rendered clips and exports are identical to the previous pass — no re-render required.

- Portrait export SHA verified unchanged: `13cdc99770348dd77eac9ab6870d2d1cdd37cb80bbcfb04d9771cc6dcd74bfaa`
- Contact sheet SHA verified unchanged: `a8aa5896a2cc0c3ee03bf58edae1b060a19db5a750dec249976bd2efd90d2b17`
- Gate V REPORT.md: "Clean — no BLOCKER/MAJOR defects. ✓" (unchanged)
- Contact sheet reviewed via image tool — all 13 portrait-native beats pass visual inspection.
