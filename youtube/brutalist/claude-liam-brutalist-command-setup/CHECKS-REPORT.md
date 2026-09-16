# CHECKS-REPORT.md — landscape (3840×2160)

## Build run
run_id: `81d4ac79a3f54016801f0269956c2d7c` · source_sha256: `cf8873d1a540147a49b11feff3dd4ab774fd4f0e0ef9941c52895bd691bb628c`

## Source changes vs prior build (run_id 7213a626)

1. `setup` `--install` pipeline refactored from `||` chaining to `if !` blocks with explicit `b "…"`/`r "…"` output headers. Logic unchanged (four phases, INSTALL_FAILED widens exit, never turns a row green). B05 code block updated to current source.
2. `setup` success output now appends `./art keys` advice and `./art smoke` advice ("a green table means dep checks passed — NOT that a video renders"). B04 code block updated; B04 narration updated to highlight this; B04 audio regenerated (20.78s vs prior 15.79s). Total film: 290.5s (was 285.5s).
3. `requirements.txt` added commented-out optional playwright section (cosmetic; pip contract unchanged).

## PROOF GATE (skills/make/nopunt)

- 13 SHOW / 0 justified-HOLD / 0 PUNT-flagged.
- Teaching arc:
  - FRAMEWORK ✓ (B02 the setup surface + B03 the requirements.txt pip contract)
  - WORKED EXAMPLE ✓ (B04 verbatim all-green run with art smoke advice)
  - FALSIFIABILITY ✓ (B09 recovery — models unlinked → red audio row → exit 1 → recover)
  - SCAFFOLDED TASK ✓ (B11 Your Turn composer with a paste-ready prompt)
  - BOOKENDS ✓ (B00 ask · B01 BLUF · B11 handoff · B12 outro)
  - NO-SOURCE-NO-VERDICT ✓ (every verdict artifact line traces to a specific line in setup or requirements.txt; see FACTCHECK.md)

## Live commands run in the isolated workspace toolkit

Toolkit: `/Users/bear/…/.repoloop/workspaces/claude-liam-brutalist-command-setup/toolkit`.

```
# bare verification, models present (verbatim — demo/RUN-LOG.txt §2)
$ ./setup       → exit 0, 7 rows ✅ ready, cost $0.00,
                  + "Run ./art keys to check optional Higgsfield login."
                  + "A green table above means every dependency checks out live — it does NOT
                     mean a video actually renders. Run ./art smoke for that proof…"

# failure — models unlinked (demo/RUN-LOG.txt §3)
$ ./setup       → exit 1, audio row ❌ blocked + two hint lines

# recovery (demo/RUN-LOG.txt §4)
$ ./setup       → exit 0, all green again + same art smoke advice lines
```

No `./setup --install` was run (per BUILD-PROMPT; the --install pipeline is described from setup's own code, not executed).

## Audio (Kokoro am_onyx)

```
# B04 narration changed — regenerated only B04
$ python3 runtime/scripts/generate_audio_kokoro.py <reel> --only B04
[kokoro] beat-B04.mp3  20.78s  voice=am_onyx
[kokoro] 1 beat(s) generated · cost $0.00

# All 13 beats: existing audio retained for B00-B03, B05-B12
```

Total narration ≈ 290.5 s. B01 audio is 17.69 s (≥ the 9 s BLUF floor); `lead_silence_s: 0.8` is written on the beat, per EXECUTIVE-SUMMARY LAW.

## Remotion renders (foreground, concurrency 1)

```
$ ART_CHROME=/tmp/claude/art-chrome-wrapper.sh ART_CHROME_MODE=chrome-for-testing \
  python3 runtime/scripts/remotion_scenes.py <reel> --only B04 --force
[remotion] B04: ok: ClaudeCodeBeat -> media/B04.mp4

$ … remotion_scenes.py <reel> --only B05 --force
[remotion] B05: ok: ClaudeCodeBeat -> media/B05.mp4
```

Only changed beats re-rendered. B00-B03, B06-B12 clips unchanged.

## Compile (landscape 4K)

```
$ python3 runtime/scripts/compile.py <reel> --height 2160 \
  --out <reel>/exports/landscape --force
[art] compiled B00…B12 VIDEO 290.5s
[art] WARNING: 'code-cascade' carries 8/13 beats (61%) — over the ~40% pantry cap
[art] wrote …/exports/landscape/claude-liam-brutalist-command-setup.mp4  (290.5s)
[art] slots: 13/13 filled
```

Motion-histogram warning is informational (command teardown episodes share visual language by design; accepted on sibling doctor episode at same distribution).

## Final gate (Gate V — final_frame_check.py)

Compile ran `runtime/qc/final_frame_check.py` against the master candidate before atomic replace and reported **0 BLOCKER / 0 MAJOR** — `.verified.json` stamped.

## ffprobe / audio decode

```
$ ffprobe exports/landscape/claude-liam-brutalist-command-setup.mp4
codec=h264  width=3840  height=2160  duration=290.500000  r_frame_rate=24/1
audio=aac  48000 Hz  channels=2

$ ffmpeg -af volumedetect  →  mean_volume: -27.0 dB   max_volume: -2.9 dB
```

## Visual QC — actually looked at (this build)

- `_qc/landscape/frames/` — 581 PNG frames at 2 fps (290.5 s × 2).
- `_qc/landscape/beats/` — midpoint frames for all 13 beats.
- `_qc/landscape/contact-sheet.jpg` — 13-beat grid Read with the image-capable tool.
- Key inspections: B04 FEATURE table with all 7 green rows + new ./art smoke advice lines visible + spark line "Green dep checks ≠ video renders. art smoke proves it."; B05 four-phase --install with if/! pattern; B11 Your Turn handoff; B12 outro @NikBearBrown OUTRO-LOCK. No edge bleed, proper title-safe margins, no captions.

## Known limitations, honestly recorded

- `runtime/qc/final_frame_check.py` covers the runtime rubric; the legacy `scripts/type_check.py` referenced by older AI Explainer prose does NOT exist in this toolkit revision — see TYPECHECK.md.
- `./setup --install` is not exercised locally, per the BUILD-PROMPT. The install pipeline is described from `setup:57-100` source; B05 code block is source-truthful but lightly compressed for card width.
- The B05 code abbreviates some Oswald/Kokoro URLs with `…` for readability in the card — source reference is `setup:57-100` and the full URLs are in the source.
- Motion-histogram: code-cascade carries 61% of beats — informational only; accepted on sibling episode.
- OUTRO-LOCK requires `@NikBearBrown` on the outro card; this playlist targets `@HumanitariansAI`. Composer-footer chip reads `@HumanitariansAI` on every beat; the outro's hardcoded `@NikBearBrown` is called out in README.md for the human reviewer.
