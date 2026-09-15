# CHECKS-REPORT — The logo Skill (landscape)

Run ID: `f971dbe48eef4a7c82cd58515b018d69` · (re-verified from `19539b2db46647a796f0f26e66bb6e76`) · commit-baseline: `ba2d0e0f`.

## Beat-authoring gate (PROOF GATE)

- 12 beats · **SHOW**: 12 · **HOLD**: 0 · **PUNT**: 0.
- Every body beat carries a `shot.show` block with ordered visual events.
- Every SHOW/HOLD claim beat names its on-screen artifact in `shot.show`
  (composer output rows, folder tree, phase nodes, quote blocks, verdict rows).
- Legibility contract: ≥15% negative space; un-highlighted elements at full opacity;
  no side-by-side comparisons in this reel (mechanism cards use quote-block +
  verdict-pill instead).

## Teaching-arc checklist

- FRAMEWORK ✓ (B02 anatomy, B03 pipeline — both before the worked mechanism beats)
- WORKED EXAMPLE ✓ (B04 the-clock, B05 lock, B06 pool, B07 drawOn — each a real
  design decision cited to the source)
- FALSIFIABILITY ✓ (B08 — no logos/nik-bear-brown/, verified against SKILL.md +
  OUTRO-LOCK.md + this reel's own outro composition)
- SCAFFOLDED TASK ✓ (B10 — the paste-ready dry-run prompt with three-check rubric,
  demonstrated live against `demo/fixture-reel/`)
- BOOKENDS ✓ (B00 cold open · B01 hesitant BLUF · B10 handoff · B11 title outro)
- NO-SOURCE-NO-VERDICT ✓ (every verdict pill and every quote card carries a `cite`
  string; the six verdict lines in B09 restate B04–B08)

## Audio

```
$ python3 runtime/scripts/generate_audio_kokoro.py <reel>
[kokoro] beat-B00.mp3  15.25s  voice=am_onyx
[kokoro] beat-B01.mp3  18.13s  voice=am_onyx
[kokoro] beat-B02.mp3  32.94s  voice=am_onyx
[kokoro] beat-B03.mp3  31.94s  voice=am_onyx
[kokoro] beat-B04.mp3  28.78s  voice=am_onyx
[kokoro] beat-B05.mp3  27.31s  voice=am_onyx
[kokoro] beat-B06.mp3  33.05s  voice=am_onyx
[kokoro] beat-B07.mp3  29.46s  voice=am_onyx
[kokoro] beat-B08.mp3  33.49s  voice=am_onyx
[kokoro] beat-B09.mp3  28.99s  voice=am_onyx
[kokoro] beat-B10.mp3  34.35s  voice=am_onyx
[kokoro] beat-B11.mp3  3.33s   voice=am_onyx
[kokoro] 12 beat(s) generated · cost $0.00
```

Kokoro `am_onyx` (local, free). Durations written back into `beat_sheet.json`
as `actual_duration_s`. No paid TTS.

## Isolated-toolkit runtime patches (recorded for provenance)

The isolated toolkit's `runtime/remotion/node_modules/` was set up per the
standing repoloop pattern (`feedback_isolated_toolkit_node_modules_shadow`).
Two additional patches were required to render inside Apple's App Sandbox on
this workstation; both are edits **inside the isolated toolkit** only — the
real public toolkit is unchanged.

1. `toolkit/runtime/remotion/node_modules/@remotion/renderer/dist/open-browser.js`:
   added `ART_CHROME_SINGLE_PROCESS=1` env-triggered `--single-process
   --in-process-gpu --disable-crash-reporter` flags. Chrome cannot bind Mach
   ports in this sandbox otherwise (`feedback_chrome_sandbox`).
2. `toolkit/runtime/scripts/remotion_scenes.py`: replaced `npx remotion render`
   with `node --preserve-symlinks .../@remotion/cli/remotion-cli.js render …`
   so require() stays inside the shadow node_modules where (1) is patched.

These enable the mandatory current runtime checks — they do not bypass any
gate.

## Remotion renders

```
$ ART_CHROME=<chrome-headless-shell> ART_CHROME_MODE=chrome-for-testing \
    ART_CHROME_SINGLE_PROCESS=1 \
    python3 runtime/scripts/remotion_scenes.py <reel> --force

[remotion] B00: ok: ClaudeComposerAsk       -> media/B00.mp4
[remotion] B01: ok: BrutalistHesitantWriter -> media/B01.mp4
[remotion] B02: ok: SkillTeardownAnatomy    -> media/B02.mp4
[remotion] B03: ok: SkillTeardownPipeline   -> media/B03.mp4
[remotion] B04: ok: SkillTeardownMechanism  -> media/B04.mp4
[remotion] B05: ok: SkillTeardownMechanism  -> media/B05.mp4
[remotion] B06: ok: SkillTeardownMechanism  -> media/B06.mp4
[remotion] B07: ok: SkillTeardownMechanism  -> media/B07.mp4
[remotion] B08: ok: SkillTeardownMechanism  -> media/B08.mp4
[remotion] B09: ok: ClaudeVerdictArtifact   -> media/B09.mp4
[remotion] B10: ok: ClaudeComposerAsk       -> media/B10.mp4
[remotion] B11: ok: ClaudeTitleOutro        -> media/B11.mp4
[remotion] stamped provenance in beat_sheet.json + updated consumers.json
```

`--concurrency=1 --scale=2 --image-format=png --crf=16` per `remotion_scenes.py`
defaults. All beats rendered at native 1920x1080 comp; `--scale=2` super-samples
to 3840x2160 for the master.

### Re-render after Gate V feedback

The first Gate V pass flagged B01 (hesitant writer) with `underfill` (47% <
55%). Root cause: three-line BLUF text was too spare for the safe area. Fix:
added `after every reel.` as a fourth line so the composition fills the canvas.
B01 was re-rendered (`--only B01 --force`) and the master recompiled.

## Compile (landscape)

```
$ python3 runtime/scripts/compile.py <reel> --height 2160 \
      --out <reel>/exports/landscape --force

[art] compiled B00  VIDEO    15.2s  ← B00.mp4
[art] compiled B01  VIDEO    18.2s  ← B01.mp4  (post-fix render)
[art] compiled B02  VIDEO    33.0s  ← B02.mp4
[art] compiled B03  VIDEO    32.0s  ← B03.mp4
[art] compiled B04  VIDEO    28.8s  ← B04.mp4
[art] compiled B05  VIDEO    27.3s  ← B05.mp4
[art] compiled B06  VIDEO    33.1s  ← B06.mp4
[art] compiled B07  VIDEO    29.5s  ← B07.mp4
[art] compiled B08  VIDEO    33.5s  ← B08.mp4
[art] compiled B09  VIDEO    29.0s  ← B09.mp4
[art] compiled B10  VIDEO    34.4s  ← B10.mp4
[art] compiled B11  VIDEO     3.3s  ← B11.mp4
[art] motion histogram: reveal:8  type-on:3  hold:1
[art] WARNING: 'reveal' carries 8/12 beats (66%) — over the ~40% pantry cap
[art] build stamp → beat_sheet.json (12/12 filled)
[art] wrote .../exports/landscape/claude-liam-brutalist-skill-logo.mp4
      (317.2s, audio: per-beat timeline (source audio preserved))
[art] slots: 12/12 filled — B00:VIDEO B01:VIDEO … B11:VIDEO
```

Verified atomically to
`exports/landscape/claude-liam-brutalist-skill-logo.verified.json` after Gate V
passed clean. See probe below.

**Motion-histogram warning** is a soft lint, not a blocker (compile.py lines
701–708). The eight `reveal` beats are the anatomy, pipeline, five mechanism
beats, and the verdict — all cards that *reveal their contents on the audio
clock*. Converting them to `type-on` would misrepresent them (only the composer
and hesitant writer type); converting to `hold` would remove the reveal
structure the cards were designed for. Accepted as-is with this justification.

## Gate V — visual QC (final_frame_check.py)

```
[gate-v] frames=24 BLOCKER=0 MAJOR=0 → _qc/REPORT.md
[gate-v] clean.
```

(First pass flagged 2 × MAJOR `underfill` on B01_50 and B01_85; both cleared
after the B01 re-render.)

## Frame inspection (image-capable Read)

Per-beat frames sampled at 15/50/85% and Read as images:
- `_qc/samples/B00_85.png` — cold open composer, three result lines visible,
  Hola, Liam greeting, @HumanitariansAI chip in footer.
- `_qc/samples/B01_85.png` — hesitant writer showing final corrected sentence
  ("The logo skill / plays a random brand sting / after every reel. / The MP3
  is the clock.") in EB Garamond — the misconception → correction landed.
- `_qc/samples/B02_85.png` — folder tree with all rows revealed, callout pill.
- `_qc/samples/B03_85.png` — six-phase pipeline diagram with PICK & LOCK
  highlighted in terracotta.
- `_qc/samples/B04_85.png` — MP3-is-the-clock mechanism card, quote + verdict.
- `_qc/samples/B08_85.png` — Falsifiability card with the `logos/nik-bear-brown/`
  quote.
- `_qc/samples/B09_50.png` — six-line verdict card, all rows visible and legible.
- `_qc/samples/B10_50.png` — Your Turn composer with paste-ready prompt and
  three-check rubric visible.
- `_qc/samples/B11_50.png` — Title outro "The logo Skill." with terracotta
  period, @NikBearBrown handle (per OUTRO-LOCK), pixel mascot.

Contact sheet at `qc-sheet.png` (1920x810 tiled).

## Static/lint checks that shipped in the toolkit

- `runtime/qc/final_frame_check.py` — Gate V (canvas fill, contrast, edge
  bleed). Ran clean.
- `runtime/qc/compile.py` motion-histogram lint — WARNING only, justified above.

## Gaps and honestly-recorded limitations

- **`runtime/scripts/type_check.py` is not present in this toolkit** (referenced
  by `skills/make/ai-explainer/SKILL.md §Hard rules · GATE T`, but missing on
  disk). Consequence: no `TYPECHECK.md` FAIL/PASS from the shipped checker.
  Substitute: the visual typography review documented in `TYPECHECK.md` (frame
  reads) — clearly labeled as a substitute for the absent legacy checker.
- **`ILLUSTRATIONS.md`, `reference/type-spec.md`, kerning skills** — also
  referenced by AI Explainer doctrine, also absent. Same substitute policy.
- **`--audit` mode / AUDIT-MODE.md** — referenced by SKILL.md, not shipped in
  this isolated toolkit. Not applicable to this reel regardless.
- **Higgsfield / paid capabilities** — not invoked (playlist runs on the free
  path per BRIEF).

## No unauthorized actions

- No `git push`, no upload, no publish.
- No API-key fallback (Kokoro local; Claude Code subscription for authoring only).
- The public toolkit at `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/`
  was not modified — all patches are in the isolated `.repoloop/workspaces/…/toolkit/`.
- The two example beat sheets were read as leads, never overwritten or reused.

Bear's viewing and editing is next; publication is separate.
