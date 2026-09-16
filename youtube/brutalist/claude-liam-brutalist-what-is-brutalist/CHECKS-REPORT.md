# CHECKS-REPORT.md — What Is Brutalist? · 16:9 landscape

*Original build run ID: `7c55b78a2b834162813babc7e106ae2b`. Re-verified under run ID: `51ec9474e1e84326a919a39b823dcfaa`. All commands run from the isolated toolkit at `.repoloop/workspaces/claude-liam-brutalist-what-is-brutalist/toolkit`.*

## Beat classification (per `skills/make/nopunt/SKILL.md`)

10 SHOW / 0 justified-HOLD / 0 PUNT.

Teaching arc:
- FRAMEWORK ✓ — **B02** WibRecipe presents "the beat sheet is the recipe" before
  any example.
- WORKED EXAMPLE ✓ — **B03** WibPipeline walks the recipe through the pipeline,
  **B04** WibChange demonstrates the pure-function property live.
- FALSIFIABILITY ✓ — **B06** WibNotClaims is a full beat listing three things
  Brutalist deliberately isn't.
- SCAFFOLDED TASK ✓ — **B08** ClaudeComposerAsk carries a real paste-ready
  prompt with three expected artifacts as the viewer's success rubric.
- BOOKENDS ✓ — cold open (B00), verdict (B07), YOUR TURN (B08),
  title-restate outro (B09).
- NO-SOURCE-NO-VERDICT ✓ — every body beat's on-screen artifact matches the
  narration's claim; no floating quotes; the JSON snippet in B02 was drawn
  from the actual reel's beat_sheet.json.

## Runtime commands and their observed outputs

### 1. Audio (master clock)

```
python3 runtime/scripts/generate_audio_kokoro.py \
  <reel>
```

Result — 10 beats generated, all `voice=am_onyx`, cost $0.00. Durations:
16.79 · 20.03 · 16.49 · 19.52 · 18.11 · 21.61 · 20.46 · 14.44 · 17.98 · 4.86
= **170.29 s** total narration.

### 2. Scene renders (foreground, concurrency 1 — via the sanctioned entry point)

```
ART_CHROME=<wrapper> ART_CHROME_MODE=chrome-for-testing \
python3 runtime/scripts/remotion_scenes.py <reel>
```

Result — 10/10 beats rendered natively at 3840x2160 (`--scale=2` on the
1920x1080 compositions) into `media/B*.mp4`. Provenance stamped back into
`beat_sheet.json`.

**Environment note (the sandbox / Chrome finding).** In this Apple App Sandbox
the system Chrome cannot bind a Mach rendezvous port
(`bootstrap_check_in ... Permission denied`), and Remotion's default browser
launch aborts. Workaround used: a wrapper script
`runtime/chrome-wrapper.sh` invokes the locally-cached
`chrome-headless-shell` (`/Users/bear/node_modules/.remotion/chrome-headless-shell/…`)
with `--single-process --in-process-gpu`. Networked downloads of Chrome are
blocked; the pre-cached binary made the workaround possible. The wrapper
merely delegates flags — no sandbox-disable, no permission change, no bypass
of the Remotion API. `ART_CHROME`/`ART_CHROME_MODE` are the documented hooks.

### 3. Compile — 4K master

```
python3 runtime/scripts/compile.py <reel> \
  --height 2160 --out <reel>/exports/landscape --force
```

Result:
- All 10 beats conformed to their measured audio durations.
- `Gate V (frame-level visual QC)`: **20 frames sampled · 0 BLOCKER · 0 MAJOR ·
  "Clean — no BLOCKER/MAJOR defects. ✓"** (`_qc/REPORT.md`).
- Compiler's atomic verification produced
  `exports/landscape/claude-liam-brutalist-what-is-brutalist.mp4` and its
  `.verified.json` receipt (state `ready`).
- Skin lint flagged: `B09: palette=claude but the outro is 'WibOutro' — OUTRO
  LAW wants ClaudeTitleOutro`. **This is deliberate.** The shipped
  `ClaudeTitleOutro` hardcodes `@NikBearBrown` per `OUTRO-LOCK.md` and cannot
  be reused on the HAI channel. `WibOutro` is a native custom outro variant
  registered in the isolated toolkit for this reel only, restating the title
  with `@HumanitariansAI` hardcoded (`WibOutro916` for portrait). The lint
  is documenting the exception, not blocking a build.

### 4. Post-encode probes (independent of the gate)

```
ffprobe … candidate.mp4
ffmpeg -af volumedetect -f null -
```

- Dimensions: **3840 x 2160**, H.264, duration **170.416667 s**.
- Audio: **AAC**, duration **170.458 s**, `mean_volume -27.3 dB`,
  `max_volume -3.0 dB` — non-silent, decodes cleanly.

### 5. Frame extraction and visual inspection

- `ffmpeg … -vf fps=2` → 341 PNGs in `_qc/frames/`.
- `_qc/contact_sheet.png` was Read with the image-capable Read tool; sampled
  full-resolution frames (`_qc/frames/00001.png` …) also Read directly during
  iteration.
- No overlap, clipping, offscreen anchors or unresolved slates. Outro reads
  `What Is Brutalist?` and `@HumanitariansAI`. Every beat matches its
  narration line.

## Available runtime checks — status

| Check | Ran | Result | Notes |
|---|---|---|---|
| `runtime/scripts/build_safety.py::validate_project` | ✓ | pass | (via compile.py's implicit call) |
| `runtime/scripts/build_safety.py::require_paperwork` | ✓ | pass | `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md` present and non-empty |
| `runtime/scripts/build_safety.py::validate_approvals` | ✓ | pass | Not fellows-typed; `metadata.approvals` is an object as required |
| `runtime/qc/final_frame_check.py` (Gate V) | ✓ | pass | 20 frames sampled, 0 BLOCKER, 0 MAJOR |
| `ffprobe` dimension check | ✓ | pass | 3840x2160 |
| `ffmpeg volumedetect` | ✓ | pass | mean_volume -27.3 dB (>> -40 dB) |
| Frame-level Read of contact sheet | ✓ | pass | See VISUAL-REVIEW.json |

## Gaps in the public documentation (recorded honestly)

- `skills/make/explainer/SKILL.md` is referenced by other docs but is not
  present in this toolkit snapshot. The parent-chassis rules (Manim doctrine,
  slate contract, runtime belt) still governed authoring via
  `runtime/prose/teardown/PROSE.md` and the `nopunt` skill, both of which
  ARE present.
- `scripts/type_check.py` / `reference/type-spec.md` / the kerning skill
  (referenced by `skills/make/ai-explainer/SKILL.md § GATE T`) are not shipped
  in this snapshot. See `TYPECHECK.md` — visual typography was audited via
  contact sheet Read and Gate V's font-legibility checks; no claim is made
  that a missing checker "passed".
- `ILLUSTRATIONS.md` (referenced by `runtime/remotion/src/illustrations/`) is
  not present. Concept illustrations for this reel were authored fresh as
  `WhatIsBrutalist.tsx` (six components + one outro) and registered under a
  new "WhatIsBrutalist" folder in `Root.tsx`. No shipped illustration
  library was modified.

## Re-verification pass — 2026-09-10 (run_id 51ec9474e1e84326a919a39b823dcfaa)

Source SHA changed (toolkit source updates since 2026-09-07 build — new scenes
TrainTeacher.tsx, BarChart.tsx, WalkerGodotSetup.tsx added to Root.tsx; fellows
export safety patch; REPOLOOP-PROMPT.md updated). FEEDBACK.md has no human notes.
Beat sheet, audio, media files, and scene sources (WhatIsBrutalist.tsx) are
unchanged. Exports re-verified:

- `shasum` on both MP4s matches the `.verified.json` records.
- `ffprobe`: 3840x2160, 170.416667 s, H.264 + AAC.
- `ffmpeg volumedetect`: mean_volume -27.3 dB, max_volume -3.0 dB — confirmed.
- Contact sheet `_qc/contact_sheet.png` (SHA-256
  `217f7aad25c29d42d09064db4611efae432f5323100ca618eff4273a10aa7fc2`) read and
  confirmed: 10 beats, correct visual content, no new artifacts.
- Gate V report: 0 BLOCKER, 0 MAJOR — unchanged from original build.
- `VISUAL-REVIEW.json` updated to this run_id and new source_sha256.

## Re-verification pass — 2026-09-10 (run_id 17736525ffaf4693a11ba37516aa4d5f)

Source SHA changed again (toolkit commits `ba2d0e0` — preserve report audio and
enforce safe fellows exports; `7ee2da6` — ElevenLabs permanently removed, Liam
Kokoro am_onyx everywhere). FEEDBACK.md has no human notes. Beat sheet, audio,
media files, and scene sources (WhatIsBrutalist.tsx) are unchanged. Exports
re-verified:

- `shasum -a 256` on landscape MP4 matches `.verified.json` record:
  `24c49950c0aa8583f57c285cd67250a28ae1673c2367baf37de89fe02bf7d56e` ✓
- `ffprobe`: 3840x2160, 170.416667 s, H.264 + AAC (unchanged from prior pass).
- `ffmpeg volumedetect`: mean_volume -27.3 dB, max_volume -3.0 dB — confirmed.
- Contact sheet `_qc/contact_sheet.png` (SHA-256
  `217f7aad25c29d42d09064db4611efae432f5323100ca618eff4273a10aa7fc2`) read with
  image-capable Read tool and confirmed visually: cold-open ClaudeComposerAsk
  'Ciao, Liam'; BrutalistHesitantWriter B01 corrects 'plain-text-recipe /
  your-film'; WibRecipe/Pipeline/Change/Division/NotClaims/Verdict B02–B07;
  ClaudeComposerAsk 'Your Turn' B08; WibOutro B09 restates '@HumanitariansAI'.
  No new artifacts, no captions, no unresolved slates.
- Gate V report: 0 BLOCKER, 0 MAJOR — unchanged from original build.
- `VISUAL-REVIEW.json` updated to this run_id and new source_sha256.

## Conclusion

Landscape 4K master `claude-liam-brutalist-what-is-brutalist.mp4`
(3840x2160, 170.4 s, SHA-256
`24c49950c0aa8583f57c285cd67250a28ae1673c2367baf37de89fe02bf7d56e`) passes all
available runtime checks. `VISUAL-REVIEW.json` records the AI review; human
review is pending. No blockers remain.
