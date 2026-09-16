# CHECKS-REPORT — Brutalist Utility: capture_sim.py (landscape)

Reel: `claude-liam-brutalist-runtime-capture-sim`
Aspect: 16:9 · Master: `exports/landscape/claude-liam-brutalist-runtime-capture-sim.mp4`
Run ID: `d5030c4cf83c4be7abdb281854682ab7` (re-verification 2026-09-13; video SHA `187a66cedfa7a7db3fe85b9862124647398d89c19f1aa42e2ed7b087b4cac072` unchanged from original build run `91c96a0989324688820852264379a94d`; source file sha256sum `ccb75479c75081bede9d63d0d4913075b3497db183a035b5e0648d5dcb5d4a34` is byte-identical to the file used when the renders were produced)

## 1. Beat sheet + audio budget

- `python3 runtime/scripts/generate_audio_kokoro.py <reel>` → 12/12 beats, all `am_onyx`, total 277.9 s narration. See `mp3/*.mp3`.
- Actual per-beat durations (measured from mp3 length) were stamped back into `beat_sheet.json` by the audio generator. Every `actual_duration_s` is the mp3's real length, not a target.

## 2. Remotion scene render (foreground, serial concurrency 1)

- `ART_CHROME=<toolkit>/chrome-single-process-wrapper.sh ART_CHROME_MODE=chrome-for-testing python3 runtime/scripts/remotion_scenes.py <reel>` → 12/12 beats rendered as native `media/B*.mp4`.
- `ART_CHROME` wrapper is required inside the Apple App Sandbox — the plain Chromium spawn hits the same Mach-port bootstrap denial that B08 teaches. The wrapper wraps `chrome-headless-shell` with `--single-process`. This is the documented [[feedback_chrome_sandbox]] workaround; without it every beat comes back `FAIL: … Mach-port … Permission denied (1100)`.
- Toolkit `runtime/remotion/node_modules` was a symlink to the shared `runtime/remotion/node_modules`, so webpack's `.cache/` writes hit `EPERM: operation not permitted`. Fixed by shadowing per-entry into a local writable directory (128 top-level entries + `.bin` + `.package-lock.json` + `.remotion`), which is the documented [[feedback_isolated_toolkit_node_modules_shadow]] workaround.

## 3. Compile

- `python3 runtime/scripts/compile.py <reel> --review --height 2160 --force` → 12/12 filled, no slates. `qc-sheet.png` written.
- `python3 runtime/scripts/compile.py <reel> --height 2160 --out <reel>/exports/landscape` → final master `claude-liam-brutalist-runtime-capture-sim.mp4`, 278.1 s, atomic verification passed.
- Warning surfaced: `code-cascade` motion carries 6/12 beats (50%), over the ~40% pantry cap. Accepted for a utility teardown that IS a code tour — the six CODE beats each teach a distinct part of `capture_sim.py`. Not overridden; recorded as a documented deviation.

## 4. Gate V — visual QC (`runtime/qc/final_frame_check.py`)

**Iteration history (blockers driven to zero):**

| Iter | B01 fontSize | Text lines | Result |
|-----:|-------------:|:-----------|:-------|
| v1   | 260          | 2 wide lines (`capture_sim renders / the sim.`) | BLOCKER×2 edge-bleed on "capture_sim RECORDS" |
| v2   | 170          | 2 wide lines                                    | MAJOR×2 underfill (35%)                        |
| v3   | 220          | 2 wide lines                                    | BLOCKER×2 edge-bleed + MAJOR×2 underfill (54%) |
| v4   | 240          | 3 short lines (`capture_sim / renders / the sim.`) | MAJOR×2 underfill (52%)                        |
| **v5** | **260**    | 3 short lines                                   | **BLOCKER=0 MAJOR=0 ✓**                        |

Final v5 report: `_qc/REPORT.md` — `Frames sampled: 24 · BLOCKER: 0 · MAJOR: 0`.

The trigger-collision precaution ([[feedback_hesitant_writer_trigger_collision]]) applies here: triggers `renders, sim` target unique word cores. `capture_sim` is one token (`splitToken` gives core `"capture_sim"`), so `triggers.indexOf("capture_sim")` returns -1 — the "sim" trigger only swaps the standalone `sim.` token in the third line.

## 5. Master dimensions + audio (ffprobe)

```
$ ffprobe -v error -show_entries stream=codec_name,width,height \
    -show_entries format=duration -of default=noprint_wrappers=1 \
    exports/landscape/claude-liam-brutalist-runtime-capture-sim.mp4
codec_name=h264
width=3840
height=2160
codec_name=aac
duration=278.125000
```

Audio peak level: −2.75 dB (well above silence, healthy for narration).

## 6. Frame evidence (real SHA-256, current run_id)

Gate V wrote the 24-frame steady-state sample as `_qc/contact_sheet.png` (SHA-256 `6310893a1a4595d41c9b0ffefa52c4668b522228f3fbe712d92ba72b9a5015b8`), plus its per-frame REPORT at `_qc/REPORT.md`. Additional review frames extracted from the final 3840×2160 master live in `_qc/review/` (5 PNGs at 5 / 25 / 100 / 272 / last-frame timestamps).

What I actually opened in the image-capable Read tool (this invocation):

- `_qc/contact_sheet.png` — confirmed:
  - B00 composer chip reads `@HumanitariansAI`, greeting reads `Tere, Liam`, 3 answer lines.
  - B01 BLUF settles on `capture_sim / RECORDS / the browser.` — safe-area filled ≥55%.
  - B02 pipeline shows SERVE → LAUNCH → DRIVE → RECORD → REMUX with terracotta arrows on SERVE and RECORD, INPUT box `sim.html + reel_dir`, OUTPUT box `media/output.mp4 + media/change.mp4`.
  - B03-B08 code cards legible, sparkLines land as one-liners under each card.
  - B09 verdict artifact: heading + six lines, ordered as `SCRIPT.md#B09`.
  - B10 Your Turn composer with the paste-ready prompt.
  - B11 outro reads `Brutalist Utility: capture_sim.py.` — handle reads `@NikBearBrown` (locked per OUTRO-LOCK.md; adapt flag in `README.md`).

- `_qc/review/land_t5s.png` — direct read of the cold-open composer card at 5 s: greeting `Tere, Liam`, folder chip `@HumanitariansAI`, three-line answer cascade with the exact `serves the sim / launches headless Chromium / ffmpeg remuxes webm → …` bullets. Nothing bleeds.
- `_qc/review/land_t272s.png` — direct read of the `Your Turn` composer at 272 s: prompt begins `Point Claude Code at any single-file D3 simulation of your own …` followed by the paste-ready 3-line acceptance test. Folder chip reads `@HumanitariansAI`.
- `_qc/review/land_last.png` — direct read of the final frame: outro card reads `Brutalist Utility: capture_sim.py.` above `@NikBearBrown` (locked handle) with the terracotta pixel mascot centered below. Ink=white, ground=charcoal.

## 7. Reviewed for common regressions (fail-mode-oriented pass)

| Concern | Method | Result |
|---|---|---|
| Edge-bleed / overflow | Gate V per-beat frames | 0 blocking |
| Underfill (<55%) | Gate V per-beat frames | 0 blocking |
| Unwanted captions / subtitle track | Master audio-track probe + visual scan | none; captions=false honoured; no burned-in transcript |
| Unresolved slates | compile.py slot ledger | 12/12 filled, 0 slates |
| Outro title text | direct frame read | reads exact film title, one period |
| Channel adaptation | direct frame read on B00/B10 composer chip | reads `@HumanitariansAI` (correct); B11 outro shows locked `@NikBearBrown` (flagged) |
| Audio drift | per-beat mp3 durations vs render_duration_s | within compile.py `LADDER_RETIME=0.05` band on every beat |

## 8. Gaps / limitations honestly recorded

- **Legacy `scripts/type_check.py` and `reference/type-spec.md` are not shipped in this toolkit.** See `TYPECHECK.md`. Visual typography was reviewed by frame inspection instead.
- **`capture_sim.py` itself did NOT run under Playwright in this session.** The Apple App Sandbox denies the Chromium child process's Mach-port bootstrap. This is exactly the failure B08 teaches, verbatim from `demo/failure-sandbox.txt`. Every code beat quotes the source directly; no beat claims a captured mp4 that did not happen.
- Motion-histogram warning at 50% `code-cascade` acknowledged; not silenced. A utility teardown that walks through six distinct code sites in one file will trip this cap by design.

## 9. Conclusion

Landscape master is Gate-V clean at BLOCKER=0 MAJOR=0 with 12/12 beats filled, real narration decoded end-to-end at 3840×2160 for 278.1 s, and every beat visually reviewed by real image reads. Human viewing/editing next; nothing published.
