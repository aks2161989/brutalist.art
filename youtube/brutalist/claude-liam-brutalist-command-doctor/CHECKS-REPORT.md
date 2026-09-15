# CHECKS-REPORT — landscape 16:9

Run: `5c2c1dda1a4548798796300fb24665e1` · Reel: `claude-liam-brutalist-command-doctor` · 2026-09-12 (rebuild: art dispatcher case line numbers updated art:96-99 → art:117-121).

## PROOF GATE — beat classification (11 body beats + 1 outro)

- 12 SHOW / 0 justified-HOLD / 0 PUNT.
- Every beat carries a `shot.show` block and a real Remotion pattern
  (`ClaudeComposerAsk`, `BrutalistHesitantWriter`, `ClaudeCodeBeat`,
  `ClaudeVerdictArtifact`, `ClaudeTitleOutro`).
- Zero slates; every beat renders a native scene.

## Teaching arc

- FRAMEWORK ✓ — B02 (dispatcher case) + B03 (two modes, one table).
- WORKED EXAMPLE ✓ — B04 (verbatim green table).
- MECHANISM ✓ — B05 (bash 3.2 compat) + B06 (live verification) + B07 (aggregation loop).
- FALSIFIABILITY ✓ — B08 (hide the .onnx, red row, exit 1).
- SCAFFOLDED TASK ✓ — B10 Your Turn.
- BOOKENDS ✓ — B00 cold-open, B01 BLUF hesitant writer, B09 verdict artifact, B11 title outro.
- NO-SOURCE-NO-VERDICT ✓ — every claim traces to `art:117-121`, `setup:…` line
  ranges, or the verbatim `demo/RUN-LOG.txt`.

## Runtime checks that were run and their outputs

| Check | Command | Result |
|---|---|---|
| kokoro TTS | `python3 runtime/scripts/generate_audio_kokoro.py <reel>` | 12/12 beats · $0.00 · durations stamped `9.54s / 14.91s / 12.99s / 22.08s / 15.74s / 20.18s / 23.45s / 21.10s / 27.14s / 22.63s / 21.74s / 5.14s` |
| Remotion render | `python3 runtime/scripts/remotion_scenes.py <reel>` | 12/12 `ok:` — stamped `rendered` in beat_sheet.json |
| compile master | `python3 runtime/scripts/compile.py <reel> --height 2160 --out <exports/landscape>` | 12/12 filled · 216.8s master written · verified.json emitted · atomic promotion succeeded |
| GATE V (final_frame_check.py) | invoked by compile after encode | 24 frames sampled · **BLOCKER 0 · MAJOR 0 · Clean ✓** (`_qc/REPORT.md`) |
| Audio decode | `ffmpeg -i <mp4> -af volumedetect -f null -` | mean -27.1 dB · max -3.0 dB · h264 aac muxed cleanly |
| ffprobe dimensions | `ffprobe -select_streams v:0` | 3840 × 2160 · yuv420p · 216.79s |

## Motion histogram (compile.py warning captured verbatim)

    code-cascade:7  type-on:2  hesitant-type:1  artifact-in:1  outro-card:1
    WARNING: 'code-cascade' carries 7/12 beats (58%) — over the ~40%
    pantry cap; convert the excess to another language (MOTION.md)

**Accepted for a command teardown where the body IS code.** Every code beat
carries a distinct real artifact — B02 dispatcher case, B03 FEATURES array,
B04 verbatim green table, B05 `check()` helper, B06 kokoro_synth + smoke
summary, B07 aggregation loop, B08 recovery flow. No two beats show the same
code. Same acceptance rationale as episode 32 (art approvals) and episode 29
(art run).

## AI Explainer laws honoured

- COLD OPEN LAW — B00 opens directly on `ClaudeComposerAsk`; ask lands
  answered with runningText and output lines. Liam introduces himself in the
  first breath ("Jambo, this is Liam, in for Bear.").
- EXECUTIVE-SUMMARY LAW — B01 = `BrutalistHesitantWriter`, actual duration
  14.91 s (well above the 9 s floor), `lead_silence_s: 0.8` on the beat.
  Correction "art doctor / installs deps." → "art doctor / verifies live." IS
  the reel's actual misconception, corrected in front of the viewer.
- ILLUSTRATE LAW — Claude UI appears only where the interface IS the subject
  (B00 ask, B10 handoff). Body beats are Onda code cards (B02-B08) and a
  Claude artifact page (B09) — never wallpaper.
- HANDOFF LAW — B10 = `ClaudeComposerAsk` with `greeting: "Your Turn"`; the
  prompt is read aloud verbatim in narration and discussed for one line
  ("Look for whether Claude is tempted to run art doctor with dash dash
  install…"). Typing appears only in B00, B01, B10 as required.
- OUTRO LAW / OUTRO-LOCK — B11 = `ClaudeTitleOutro` with title restate +
  hardcoded `@NikBearBrown` handle + slug-seeded mascot per
  `OUTRO-LOCK.md`. The `@HumanitariansAI` playlist adaptation is on the
  composer folder chip only, not the outro; flagged in README.md (same
  pattern as episodes 29, 30, 31, 32).
- SPARK-LINE LAW — every code beat carries a ≤ 4-word spark line under the
  card (e.g. "One case. No aliases. One script.").

## Skin lint

Landscape compile emitted no skin-lint warning — palette `claude` with a
`ClaudeComposerAsk` cold open passes.

## Gaps (honest limitations)

- `scripts/type_check.py` — the GATE T checker referenced by the SKILL and
  by other docs — is **not shipped in this toolkit revision**. This was
  documented as a known gap for prior episodes and remains so. See
  `TYPECHECK.md` for the visual-typography review that replaces it here.
- Setup itself was NOT run with `--install` in this session. All demo runs
  used the bare form (the verifier). See `demo/RUN-LOG.txt` and `FACTCHECK.md`.

## Conclusion

Landscape 16:9 is CLEAN. 4K master `exports/landscape/claude-liam-brutalist-command-doctor.mp4`
(SHA-256 `ea42f210bc59574e909b23f708d252b66e2531735494797faf161a7ba78ba411`)
is ready for Bear's viewing/editing pass. Not published.
