# CHECKS-REPORT — Brutalist Command: art help (16:9 landscape)

Invocation `run_id = 48e0905963d54723ba7b587f9d86d97e` — 2026-09-12.
Previous build: `run_id = 8bd2a005d9984f9490ef7370c7bb2b2f` — 2026-09-09.
Re-verified 2026-09-12: landscape was already compiled 2026-09-11 after the
art source update (B03/B04/B05/B07/B08 re-rendered 2026-09-11T17:xx). All
landscape build-state input hashes confirmed matching current media files.

## Beat classification

12 / 12 SHOW · 0 HOLD · 0 PUNT

- B00 (ASK, ClaudeComposerAsk) — SHOW (composer types the ask, output lines cascade)
- B01 (BLUF, BrutalistHesitantWriter) — SHOW (writer types the misconception, corrects it in real time)
- B02 (FRAMEWORK, ClaudeCodeBeat) — SHOW (bash case block types line by line)
- B03 (MECHANISM, ClaudeCodeBeat) — SHOW (sed pipeline types then comments type in)
- B04 (WORKED_EXAMPLE, ClaudeCodeBeat) — SHOW (17-line output cascades in)
- B05 (MECHANISM, ClaudeCodeBeat) — SHOW (four aliases + case pattern)
- B06 (MECHANISM, ClaudeCodeBeat) — SHOW (`./art --list` skills table types in)
- B07 (FALSIFIABILITY, ClaudeCodeBeat) — SHOW (failure path types, exit 2 appears)
- B08 (MECHANISM, ClaudeCodeBeat) — SHOW (recovery path + `--help` source lines)
- B09 (VERDICT, ClaudeVerdictArtifact) — SHOW (numbered artifact card, lines stagger in)
- B10 (YOUR_TURN, ClaudeComposerAsk) — SHOW (composer types the diff-the-aliases prompt)
- B11 (OUTRO, ClaudeTitleOutro) — SHOW (title restate, handle, mascot)

## Teaching-arc checklist

- FRAMEWORK: ✓ (B02 — the dispatcher case block)
- WORKED EXAMPLE: ✓ (B04 — the real 17-line output)
- FALSIFIABILITY: ✓ (B07 — `./art bogus` exit 2 does NOT print help)
- SCAFFOLDED TASK: ✓ (B10 — Your Turn: diff the four aliases)
- BOOKENDS: ✓ (B00 ASK, B10 YOUR_TURN, B11 OUTRO restate title, B01 BLUF)
- NO-SOURCE-NO-VERDICT: ✓ (every claim traces to `art:37-116` or `demo/RUN-LOG.md`)

## Runtime gates

- **Kokoro audio** — 12 / 12 beats generated locally with `am_onyx`; total 178.1s
  before conform, 177.0s after per-beat conform. All above 0.6s.
- **Remotion render** — 12 / 12 beats rendered via `remotion_scenes.py`,
  foreground, serial concurrency one, `--scale=2` (native 4K output). Chrome-
  headless-shell via `runtime/scripts/chrome_wrap.sh` (single-process wrapper).
- **compile.py final gates** — encoded a candidate mp4 into a private temp dir,
  ran Gate V (`runtime/qc/final_frame_check.py`) BEFORE promoting to the real
  export path; only replaced the previous verified master after Gate V passed
  clean AND the beat sheet + input hashes were re-verified.
- **Gate V (visual QC)** — final report (`_qc/REPORT.md`):
  ```
  Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0
  Clean — no BLOCKER/MAJOR defects. ✓
  ```
- **Motion histogram** — code-cascade 7/12 (58%). WARNING flagged by
  `compile.py`: over the ~40% pantry cap. Documented and accepted for a
  command-teardown episode where the majority of beats intentionally look at
  the source code / observed shell output. No blocker.
- **Skin lint** — no warnings on landscape.

## Actual commands run (for the record)

```bash
# audio
python3 runtime/scripts/generate_audio_kokoro.py <REEL>

# remotion (foreground, one at a time)
python3 runtime/scripts/remotion_scenes.py <REEL>

# assemble + Gate V
python3 runtime/scripts/compile.py <REEL> --height 2160 --out <REEL>/exports/landscape --force
```

## Real gates that did NOT run (documented, not skipped silently)

- `scripts/type_check.py` (GATE T) — referenced in public docs (SKILL.md,
  CLAUDE-BRAND.md) but not present in this workspace's runtime scripts
  directory. `TYPECHECK.md` records the actual visual-typography review that
  covered the same ground.
- `reference/type-spec.md` — likewise not present; the standing rules are
  covered by `layout.ts` SAFE constant + Gate V's edge-bleed / CANVAS-FILL
  checks.

## Frame evidence (spot-check, human review pending)

- `_qc/contact_sheet.png` (auto, 24 sample frames)
- `qc-sheet.png` (per-beat 12-tile contact sheet from compile.py)
- Individual samples in `_qc/frames/` (B00, B01, B04, B07, B09, B10, B11)

Human review remains required. The signal here is: nothing was silently
skipped, Gate V ran to zero MAJOR, and every beat renders content that
matches its narration.
