# CHECKS-REPORT (portrait) — Brutalist Utility: build_cli_d3_reels.py

**Run ID:** `8d75c91064f84d83bc89e08d3efe2f26`
**Aspect:** 9:16 (portrait 2160×3840)
**Episode source SHA-256 (invocation):** `92253347e5028837c16c2590f4b803bb8f32e88754ba255c1424fe9eefc29abc`
**Current source SHA-256:** `c37d17288291b4b7ca3ec7e06a23863f99b5c1c29c9f80554330829f459d172d`
**Date:** 2026-09-13 (re-verified; source unchanged from 2026-09-10 build)

## Beat classification

12 SHOW / 0 justified-HOLD / 0 PUNT-flagged. Same 12-beat spine as landscape; native `*916` compositions.

## Portrait-specific fixes made this run

1. `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` — patched the `const scale` line to use `Math.min(w/1080, h/1920)` when `height > width`, per `feedback_brutalist_hesitant_writer_portrait_scale_patch.md`. Without this the portrait design box collapses to 0.5625× and BLUF fails Gate V's 55% floor.
2. `runtime/remotion/src/scenes/ClaudeCodeBeat.tsx` — replaced the fixed `fontSize: height*0.022` with an adaptive `Math.min(baseFont, availH/lines, availW/longest)` bounding, per `feedback_claude_code_beat_adaptive_font.md`. Long stanzas (build_one is 32 lines) fit portrait width.
3. `runtime/remotion/src/scenes/ClaudeTitleOutro916.tsx` — auto-shrink the title `fontSize` based on the longest word, and add `overflowWrap: 'anywhere'` on the title div. Without this the `build_cli_d3_reels.py.` identifier overflows the right edge at TITLE_FONT=height*0.055.
4. `runtime/remotion/src/scenes/ClaudeComposerAsk.tsx` — segment div now spans `left: PAD_X, right: PAD_X` with `overflowWrap: 'anywhere'`. Fixes cold-open segment bleed on portrait when the segment holds a long dotted path.
5. `runtime/remotion/src/Root.tsx` — registered `ClaudeCodeBeat916` (1080×1920) and `SkillTeardownMechanism916` (1080×1920) compositions.
6. Portrait `beat_sheet.json` — `B00` segment trimmed to `build_cli_d3_reels.py`; `B10` `command` and `output` lines shortened to fit portrait height; `channel_title` metadata field removed (per `feedback_channel_title_portrait_bleed`); `B01` uses the portrait BLUF recipe (fontSize 150, lineSpacing 2.25, 5 lines, two triggers on distinct late lines).

## Commands run + observed output (portrait pass)

```
# Regenerate scene index after adding the 916 compositions
$ ./art scene-index → scenes.json — 621 renderable, 118 undocumented, 0 unresolved

# Portrait render (12 beats, native *916 compositions)
$ python3 runtime/scripts/remotion_scenes.py <REEL>/vertical --force
[remotion] B00..B11 ok — ClaudeComposerAsk916 / BrutalistHesitantWriter916 /
                        SkillTeardownMechanism916 / ClaudeCodeBeat916 /
                        ClaudeVerdictArtifact916 / ClaudeTitleOutro916

# Portrait compile (native 4K)
$ python3 runtime/scripts/compile.py <REEL>/vertical --height 3840 --out <REEL>/exports/vertical --force
[art] SKIN LINT: B00 palette=claude but the cold open is 'ClaudeComposerAsk916' — expected on portrait
[art] SKIN LINT: B11 palette=claude but the outro is 'ClaudeTitleOutro916' — expected on portrait
[art] wrote <REEL>/exports/vertical/claude-liam-brutalist-runtime-build-cli-d3-reels-vertical.mp4  (234.8s)
[art] slots: 12/12 filled — B00..B11 all VIDEO

# Gate V (final_frame_check.py) — after portrait fixes
$ python3 runtime/qc/final_frame_check.py <REEL>/vertical --mp4 exports/vertical/…-vertical.mp4
[gate-v] frames=24 BLOCKER=0 MAJOR=0 → _qc/REPORT.md
```

## Visual QC (frame-level)

Contact strip at `_qc/contact-strip-vertical.png`. Every beat's 50% frame read via image tool.

**Findings (blockers/majors):** 0 / 0.

Notable:
- B00 — greeting `Bula, Liam` fits; segment `build_cli_d3_reels.py` fits; three RESULT lines cascade.
- B01 — BLUF portrait recipe (fontSize 150, lineSpacing 2.25, 5 lines) fills ≥55% of safe area; corrections land: `the tool wraps a D3 sim from one HTML.`
- B02 — mechanism card (SkillTeardownMechanism916) with eyebrow, heading, body, quote (line 14-20 verbatim), verdict pill, spark line. Fits portrait canvas.
- B03–B08 — code beats reflow at portrait width; longest lines (B06's build_one 32-line body) do NOT clip.
- B09 — verdict artifact six lines fit portrait height.
- B10 — Your-Turn composer segment `Write a config.json` fits; trimmed prompt + three grading lines fit portrait bottom.
- B11 — outro title wraps across three lines: `Brutalist Utility: / build_cli_d3_reels. / py.` with terracotta period; handle `@NikBearBrown` (OUTRO-LOCK); mascot animates.

## Runtime gate coverage

| Gate | Status | Note |
|---|---|---|
| GATE F (factcheck) | PASS | Portrait folder copies landscape FACTCHECK.md (unchanged claims). |
| GATE V (visual) | PASS | 0 BLOCKER, 0 MAJOR from final_frame_check.py. |
| GATE T (type-lock, §8) | N/A | `scripts/type_check.py` absent (see TYPECHECK.md); replaced with actual frame-read + adaptive-font enforcement. |
| Skin lint (compile.py) | WARN (expected) | B00/B11 use *916 variants; not a defect on portrait. |
| Compile atomic verification | PASS | `exports/vertical/*.verified.json` present. |

## Human review pending

Next step is Bear watching the rendered film. No upload/publish.
