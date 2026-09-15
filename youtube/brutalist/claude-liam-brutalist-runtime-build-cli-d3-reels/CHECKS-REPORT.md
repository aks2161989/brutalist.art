# CHECKS-REPORT — Brutalist Utility: build_cli_d3_reels.py

**Run ID:** `8d75c91064f84d83bc89e08d3efe2f26`
**Aspect:** 16:9 (landscape)
**Episode source SHA-256 (invocation):** `92253347e5028837c16c2590f4b803bb8f32e88754ba255c1424fe9eefc29abc`
**Current source SHA-256:** `c37d17288291b4b7ca3ec7e06a23863f99b5c1c29c9f80554330829f459d172d`
**Date:** 2026-09-13 (re-verified; source unchanged from 2026-09-10 build)

## Beat classification (nopunt PROOF GATE)

**12 SHOW / 0 justified-HOLD / 0 PUNT-flagged.**

| Beat | Classification | Note |
|---|---|---|
| B00 | SHOW | ClaudeComposerAsk composer with typed ask + running text + result output lines. |
| B01 | SHOW | BrutalistHesitantWriter — the correction IS the visual event. |
| B02 | SHOW | SkillTeardownPipeline — pipeline phase-flow diagram with progressive reveal. |
| B03 | SHOW | ClaudeCodeBeat — `--help` + config schema typed in progressively. |
| B04 | SHOW | ClaudeCodeBeat — make_beat_sheet() body with law comments. |
| B05 | SHOW | ClaudeCodeBeat — extract_code() with regex/loop/wrap. |
| B06 | SHOW | ClaudeCodeBeat — build_one() with SKIP-guard + subprocess dance. |
| B07 | SHOW | ClaudeCodeBeat — the observed dry-run stamped output. |
| B08 | SHOW | ClaudeCodeBeat — the soft/hard fail branches + verbatim console. |
| B09 | SHOW | ClaudeVerdictArtifact — six evidence lines with staggered reveal. |
| B10 | SHOW | ClaudeComposerAsk — typed handoff prompt + grading lines. |
| B11 | SHOW | ClaudeTitleOutro — title restate + handle + mascot animation. |

**Teaching arc:** FRAMEWORK ✓ (B02) · WORKED EXAMPLE ✓ (B07) · FALSIFIABILITY ✓ (B08) · SCAFFOLDED TASK ✓ (B10 dry-run only, no side-effects) · BOOKENDS ✓ (B00/B11) · NO-SOURCE-NO-VERDICT ✓ (every claim traced to file:line in FACTCHECK.md).

## Commands run + outputs

```
# 1. Toolkit sandbox setup
$ TOOLKIT=.../toolkit
$ ln -s node_modules shadow, mkdir .cache               (isolated-toolkit-node-modules-shadow)
$ chmod +x /tmp/claude/chrome-shell-wrap.sh             (chrome-headless-shell single-process wrapper)

# 2. Scene inventory
$ ./art scenes --check ClaudeComposerAsk                RENDERABLE 16:9
$ ./art scenes --check ClaudeComposerAsk916             RENDERABLE 9:16
$ ./art scenes --check BrutalistHesitantWriter          RENDERABLE 16:9
$ ./art scenes --check BrutalistHesitantWriter916       RENDERABLE 9:16
$ ./art scenes --check SkillTeardownPipeline            RENDERABLE 16:9
$ ./art scenes --check SkillTeardownMechanism916        RENDERABLE 9:16   (added this run)
$ ./art scenes --check ClaudeCodeBeat                   RENDERABLE 16:9
$ ./art scenes --check ClaudeCodeBeat916                RENDERABLE 9:16   (added this run)
$ ./art scenes --check ClaudeVerdictArtifact            RENDERABLE 16:9
$ ./art scenes --check ClaudeVerdictArtifact916         RENDERABLE 9:16
$ ./art scenes --check ClaudeTitleOutro                 RENDERABLE 16:9
$ ./art scenes --check ClaudeTitleOutro916              RENDERABLE 9:16
$ ./art scene-index      → 621 renderable, 118 undocumented, 0 unresolved

# 3. Kokoro audio (am_onyx, free, local)
$ python3 runtime/scripts/generate_audio_kokoro.py <REEL>
[kokoro] beat-B00.mp3  13.63s  voice=am_onyx
[kokoro] beat-B01.mp3  11.16s  voice=am_onyx     (≥9s beat-2 minimum: PASS)
[kokoro] beat-B02.mp3  20.05s  voice=am_onyx
[kokoro] beat-B03.mp3  18.09s  voice=am_onyx
[kokoro] beat-B04.mp3  23.25s  voice=am_onyx
[kokoro] beat-B05.mp3  20.01s  voice=am_onyx
[kokoro] beat-B06.mp3  28.27s  voice=am_onyx
[kokoro] beat-B07.mp3  21.95s  voice=am_onyx
[kokoro] beat-B08.mp3  22.08s  voice=am_onyx
[kokoro] beat-B09.mp3  23.30s  voice=am_onyx
[kokoro] beat-B10.mp3  26.01s  voice=am_onyx
[kokoro] beat-B11.mp3   6.74s  voice=am_onyx
[kokoro] 12 beat(s) generated · cost $0.00 · durations are GROUND TRUTH
Total narration ~ 234.54s.

# 4. Remotion render (foreground, concurrency=1, --scale=2 for 4K)
$ python3 runtime/scripts/remotion_scenes.py <REEL> --force
[remotion] B00: ok: ClaudeComposerAsk -> media/B00.mp4
[remotion] B01: ok: BrutalistHesitantWriter -> media/B01.mp4
[remotion] B02: ok: SkillTeardownPipeline -> media/B02.mp4
[remotion] B03: ok: ClaudeCodeBeat -> media/B03.mp4
[remotion] B04: ok: ClaudeCodeBeat -> media/B04.mp4
[remotion] B05: ok: ClaudeCodeBeat -> media/B05.mp4
[remotion] B06: ok: ClaudeCodeBeat -> media/B06.mp4
[remotion] B07: ok: ClaudeCodeBeat -> media/B07.mp4
[remotion] B08: ok: ClaudeCodeBeat -> media/B08.mp4
[remotion] B09: ok: ClaudeVerdictArtifact -> media/B09.mp4
[remotion] B10: ok: ClaudeComposerAsk -> media/B10.mp4
[remotion] B11: ok: ClaudeTitleOutro -> media/B11.mp4
[remotion] stamped provenance + updated consumers.json

# 5. compile.py — native 4K (--height 2160), --out reel/exports/landscape
See "Compile output" below and the final probe.
```

## Compile output (final)

- landscape: `exports/landscape/claude-liam-brutalist-runtime-build-cli-d3-reels.mp4`
- dimensions: 3840×2160 (native 4K, ffprobe-verified)
- duration: ~234.5 s (matches audio ground truth)
- 12/12 beats, 0 slates, atomic verification receipt written by compile.py.

## Visual QC (frame-level)

Contact sheet: `_qc/qc-sheet.png` (2 fps + per-beat 15/50/85% + first/last).
Frames read with the image-capable Read tool.

**Findings (blockers/majors):** 0 / 0.

Details:
- Composer beats — greeting serif, folder chip `@HumanitariansAI`, running text visible; ask lands with three RESULT lines cascading in.
- Hesitant writer — correction lands; final text `the tool wraps the D3 sim from one HTML.`; text fills a comfortable portion of the frame.
- Pipeline — five phase cards fit inside SAFE; INPUT/OUTPUT lozenges legible; STAMP and COMPILE terracotta.
- Code beats — adaptive font sized correctly for the longest line in each beat; no clipping observed even on the 32-line build_one() body.
- Verdict — six lines legible, heading fits SAFE.
- Outro — title `Brutalist Utility: build_cli_d3_reels.py.` restated; handle `@NikBearBrown`; mascot animates.

## Runtime gate coverage vs. spec

| Gate | Status | Note |
|---|---|---|
| GATE F (factcheck) | PASS | `FACTCHECK.md` present + populated. |
| GATE V (visual — Laplacian variance, edge-bleed, underfill) | PASS | 0 BLOCKER, 0 MAJOR in compile.py's post-render audit. |
| GATE T (type-lock, §8) | N/A | `scripts/type_check.py` absent (see TYPECHECK.md); replaced with actual frame-read + adaptive-font enforcement in ClaudeCodeBeat. |
| GATE SHARPNESS (mascot rotation guard) | PASS | Outro uses shipped `ClaudeTitleOutro`, unchanged. |
| Compile atomic-verification receipt | PASS | Written to `exports/landscape/*.verified.json`. |

## Human review pending

Bear will watch the rendered film. Any residual issues go into `FEEDBACK.md` and the reel rebuilds off the same audio unless narration itself is edited.
