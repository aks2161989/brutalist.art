# CHECKS-REPORT — The nbb Skill (landscape 3840×2160)

Run ID: `176246a8e8ea447f812f68cd066bcb46`
(Original build run_id: `fdf9abc5ba3f40eba314b9262f54a0bc` — exports unchanged)
Toolkit commit: `ba2d0e0f043f5b3b35a50d336e0fc66fbfecfc0c` + local overrides
Source SHA-256 (SOURCE-SNAPSHOT capture, 2026-09-12T06:05:52): `395389a3f3f1b249fda8ab67de2d0668210b50174270d531242b3c737f4626e4`

## Compile — `runtime/scripts/compile.py`

```
python3 runtime/scripts/compile.py \
  youtube/brutalist/claude-liam-brutalist-skill-nbb \
  --height 2160 \
  --out youtube/brutalist/claude-liam-brutalist-skill-nbb/exports/landscape \
  --force
```

- 12/12 beats compiled with per-beat VIDEO source
- Total duration: **346.041667s** (measured from audio timeline)
- Master output: `exports/landscape/claude-liam-brutalist-skill-nbb.mp4`
- ffprobe: width=3840 height=2160 (native 4K, not upscaled)
- WARNING: motion histogram reveal:8 type-on:3 hold:1 — reveal at 66%
  vs ~40% cap. Warning only, not a blocker.

## Verify — `verify_output` (inside compile.py)

- Dimensions match target
- Duration matches measured audio total within tolerance
- Audio present (per-beat timeline, not silent)

## Gate V — `runtime/qc/final_frame_check.py`

```
python3 runtime/qc/final_frame_check.py \
  youtube/brutalist/claude-liam-brutalist-skill-nbb \
  --mp4 <candidate>
```

- 24 frames sampled (each beat at 50% and 85%)
- BLOCKER: 0
- MAJOR: 0
- Result: **Clean** (see `_qc/REPORT.md`)
- Contact sheet: `_qc/contact_sheet.png`

Fix that pushed it clean: BLUF (B01) hesitant-writer text expanded from 3
lines to 4, seed rotated to `nbb-bluf-2026-fdf9abc5-v2`, B01 re-rendered
via `remotion_scenes.py --only B01 --force`. First pass v1 hit 39%
underfill (MAJOR × 2 at 50%/85%); v2 measures clean.

## Scene renderer — `runtime/scripts/remotion_scenes.py`

```
ART_CHROME=/tmp/claude-501/chrome-single-process.sh \
ART_CHROME_MODE=chrome-for-testing \
python3 runtime/scripts/remotion_scenes.py \
  youtube/brutalist/claude-liam-brutalist-skill-nbb
```

All 12 patterns rendered at supersampled 2× (3840×2160):

- B00 → ClaudeComposerAsk
- B01 → BrutalistHesitantWriter
- B02 → SkillTeardownAnatomy
- B03 → SkillTeardownPipeline
- B04–B08 → SkillTeardownMechanism
- B09 → ClaudeVerdictArtifact
- B10 → ClaudeComposerAsk
- B11 → ClaudeTitleOutro

Chrome wrapper is the Apple-App-Sandbox workaround from
`feedback_chrome_sandbox`: `chrome-headless-shell` with
`--single-process --in-process-gpu`. `node_modules` shadowed per
`feedback_isolated_toolkit_node_modules_shadow` (writable `.cache/`).

## Audio — `runtime/scripts/generate_audio_kokoro.py`

```
ART_HOME=$ART_HOME python3 runtime/scripts/generate_audio_kokoro.py \
  youtube/brutalist/claude-liam-brutalist-skill-nbb
```

- 12/12 beats generated with voice `am_onyx`
- Cost: **$0.00**
- Durations become GROUND TRUTH; stamped back to beat_sheet.json

## Local safe demo — `runtime/scripts/brand_variant.py`

Ran against `demo/fixture-reel/` twice. Captured in `demo/nbb-run.log`.

- Run 1: created `demo/nbb-fixture-reel/beat_sheet.nbb.json` (audience=NikBearBrown,
  register=Teardown, palette=teardown, engine=kokoro, voice=am_onyx)
- Run 2: refused without `--force` (idempotency contract)
- Source `demo/fixture-reel/beat_sheet.json` SHA-256 identical before and after
  (`9ee2f785d74523ce5c030d567b9bda7e49bf397bc08e28d1de081b635d28b879`)

## Visual review by AI reviewer

I opened frames extracted at 15/50/85 fracs for every beat (see `_qc/contact_sheet.png`).
Nothing obscured, no unresolved slates, correct outro title text
("The nbb Skill."), correct outro handle (`@NikBearBrown`), correct
inner composer folder chip (`@HumanitariansAI`). The BLUF correction
lands as intended: "rewrites" → "scaffolds". No captions burned in.

## Gaps and honest notes

- `scripts/type_check.py` — NOT PRESENT in this toolkit revision.
  Substituted actual frame inspection via Gate V. See TYPECHECK.md.
- `reference/type-spec.md` — NOT PRESENT. Not fabricated.
- `ILLUSTRATIONS.md` — NOT PRESENT. Not fabricated.
- Batch mode over a whole book was not exercised end-to-end in the demo;
  the fixture is a single-reel scaffold. The claim in the film is
  documented, cited to SKILL.md §"Batch mode", not demonstrated live.
