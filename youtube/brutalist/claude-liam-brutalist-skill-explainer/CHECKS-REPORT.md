# CHECKS-REPORT.md — The explainer Skill (landscape 3840×2160)

Every current runtime check run against the final master. Outputs quoted from
the tool. Failures were repaired in the reel, not in the check.

**Rebuilt 2026-09-11** (run_id `251584521128464e8b35431dce545cb1`): source SKILL.md
changed — VOX LAW gained EXECUTABLE-EVIDENCE.md reference. B07 narration and props
updated; B07 audio regenerated (30.59s, +1.09s); B07 scene re-rendered; landscape
recompiled with --force. New duration: 253.7s. Gate V: clean.

## Environment

- Toolkit: isolated workspace copy at
  `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/.repoloop/workspaces/claude-liam-brutalist-skill-explainer/toolkit`.
- Run id: `251584521128464e8b35431dce545cb1` (original build: `45e2af0d64bd4e67b0ce03bb5b591d29`).
- Date: 2026-09-11 (original build: 2026-09-08).
- Browser (Remotion): `chrome-headless-shell` v149.0.7790.0 via
  `runtime/scripts/chrome_wrap.sh` (`--single-process --in-process-gpu
  --disable-crash-reporter --disable-features=MojoIpcz --no-sandbox
  --disable-dev-shm-usage`) with `ART_CHROME_MODE=chrome-for-testing`. The
  Apple App Sandbox blocks the system Chrome (Mach-port checkin denied), so
  the wrapper points Remotion at the cached chrome-for-testing binary at
  `runtime/remotion/node_modules/.remotion/chrome-headless-shell/mac-arm64/…`.
  This wrapper is the exact one documented in `feedback_chrome_sandbox.md`
  and required by every prior batch episode.
- One environment repair: `runtime/remotion/node_modules` was a symlink to a
  read-only shared tree, so webpack's `.cache/` could not be written.
  Replaced with a real directory of symlinks to each dependency (including
  `.bin`, `.package-lock.json`, `.remotion`), plus a fresh writable
  `.cache/`. No source code was copied; the package tree still points at the
  shared one.

## Kokoro audio (mp3/timings.json)

```
$ python3 runtime/scripts/generate_audio_kokoro.py <reel> --only B07
[kokoro] beat-B07.mp3  30.59s  voice=am_onyx
[kokoro] 1 beat(s) generated · cost $0.00 · durations are GROUND TRUTH
```

B07 only regenerated (narration updated to cover EXECUTABLE-EVIDENCE.md). All other
beats' audio unchanged from 2026-09-08:
- B00: 15.42s · B01: 18.84s · B02: 23.82s · B03: 21.70s · B04: 22.53s
- B05: 29.27s · B06: 28.50s · B07: 30.59s (↑1.09s) · B08: 26.71s
- B09: 32.58s · B10: 3.48s

Every beat is Kokoro `am_onyx` (Liam). Total narration ≈ 253.63 s (4 min 14 s).

## Remotion render (runtime/scripts/remotion_scenes.py)

```
# 2026-09-11 rebuild — only B07 re-rendered:
$ python3 runtime/scripts/remotion_scenes.py <reel> --only B07 --force
[remotion] B07: ok: SkillTeardownMechanism -> media/B07.mp4
[remotion] stamped provenance in beat_sheet.json + updated consumers.json
```

All other beats rendered 2026-09-08 (unchanged):
B00: ClaudeComposerAsk · B01: BrutalistHesitantWriter · B02: SkillTeardownAnatomy ·
B03: SkillTeardownPipeline · B04–B06: SkillTeardownMechanism · B08: ClaudeVerdictArtifact ·
B09: ClaudeComposerAsk · B10: ClaudeTitleOutro

Foreground, serial (default concurrency), via `remotion_scenes.py` — no
hand-rolled `npx remotion render`. Every beat resolved to a real scene; no
slates.

## Compile (runtime/scripts/compile.py)

```
$ python3 runtime/scripts/compile.py <reel> --height 2160 --out exports/landscape --force
[art] compiled B00  VIDEO    15.5s  ← B00.mp4
[art] compiled B01  VIDEO    18.9s  ← B01.mp4
[art] compiled B02  VIDEO    23.8s  ← B02.mp4
[art] compiled B03  VIDEO    21.7s  ← B03.mp4
[art] compiled B04  VIDEO    22.5s  ← B04.mp4
[art] compiled B05  VIDEO    29.3s  ← B05.mp4
[art] compiled B06  VIDEO    28.5s  ← B06.mp4
[art] compiled B07  VIDEO    30.6s  ← B07.mp4
[art] compiled B08  VIDEO    26.8s  ← B08.mp4
[art] compiled B09  VIDEO    32.6s  ← B09.mp4
[art] compiled B10  VIDEO     3.5s  ← B10.mp4
[art] motion histogram: reveal:7  type-on:3  hold:1
[art] WARNING: 'reveal' carries 7/11 beats (63%) — over the ~40% pantry cap;
      convert the excess to another language (MOTION.md)
[art] build stamp → beat_sheet.json (11/11 filled)
[art] wrote exports/landscape/claude-liam-brutalist-skill-explainer.mp4
      (253.7s, audio: per-beat timeline (source audio preserved))
[art] slots: 11/11 filled
```

Motion warning is advisory: skill-teardown Mechanism/Pipeline/Anatomy beats
are all `reveal`-motion by design. It is a house pantry-cap warning, not a
gate failure.

## Gate V — final_frame_check.py (frame-level visual QC)

First-pass Gate V failed:

```
[gate-v] frames=22 BLOCKER=2 MAJOR=0 → _qc/REPORT.md
_qc/REPORT.md:
  ### B01_50.png
  - **BLOCKER** `edge-bleed` — content crosses the title-safe top/bottom edge
  ### B01_85.png
  - **BLOCKER** `edge-bleed` — content crosses the title-safe top/bottom edge
```

Cause: B01 hesitant writer used `fontSize: 190, lineSpacing: 1.15, 5 lines`
which totalled 190 × 1.15 × 5 ≈ 1092 px — past the 972 px landscape safe
height (y 54–1026). Repair (in the reel, not in Gate V):

- Reduced `fontSize` to 180.
- Reduced to 4 lines (`The explainer skill / is a style. / Sources never
  match. / The treatment does.`).
- Tightened `lineSpacing` to 1.18 to keep readability.
- Total height 180 × 1.18 × 4 ≈ 850 px — fits within the safe area with
  margin.

Re-rendered B01 only (`remotion_scenes.py --only B01`), removed the stale
`clips/B01.mp4`, recompiled. Second-pass Gate V (and the 2026-09-11 rebuild Gate V):

```
$ python3 runtime/qc/final_frame_check.py <reel>
      --mp4 exports/landscape/claude-liam-brutalist-skill-explainer.mp4
[gate-v] frames=22 BLOCKER=0 MAJOR=0 → _qc/REPORT.md
```

`_qc/REPORT.md`:

```
# Gate V — visual QC report
Frames sampled: 22  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

22 frames = 11 beats × (50 %, 85 %) steady-state samples.
`_qc/contact_sheet.png` covers the reel at a glance. Frames were Read via
the image-capable tool during authoring iteration.

## Compiler final gate — atomic verified.json

The compiler writes an atomic receipt beside the master:

```
$ ls exports/landscape/
claude-liam-brutalist-skill-explainer.mp4
claude-liam-brutalist-skill-explainer.verified.json
```

`verified.json` pins the master's SHA-256 and every input (`media/B00.mp4 …
B10.mp4`, `mp3/beat-B00.mp3 … B10.mp3`) that fed it. `ready` means the
automated export checks passed — human review is separate.

## FFprobe dimensions and audio decode

```
$ ffprobe -v error -show_entries stream=width,height,codec_type,duration \
      -of default=nw=1 exports/landscape/claude-liam-brutalist-skill-explainer.mp4
codec_type=video
width=3840
height=2160
duration=253.666667
codec_type=audio
duration=253.666000
```

Native 4K UHD (16:9). Audio stream present, decoded, same duration as video.
Duration increased from 252.54s to 253.67s due to B07 audio regeneration (+1.09s).

## Motion histogram observation

`reveal` at 7/11 beats (63 %) exceeds the pantry cap (~40 %). This is
expected for a skill-teardown reel: the ILLUSTRATE LAW body beats
(SkillTeardownAnatomy · Pipeline · four Mechanism cards) all use "reveal"
motion (staged element-in animation). Not a gate failure, just a house
pantry-cap warning. Watching the film, the motion reads as varied because
the Anatomy tree, Pipeline flow, and Mechanism quote-blocks reveal in
different ways.

## No captions / subtitles

`captions: false` in metadata. No SRT/VTT/CC track authored, no transcript
slide substituted for a demonstration.

## No paid calls, no publishing

Kokoro is local, free. Remotion is local, free. No API calls. No upload,
no YouTube handoff, no GitHub push. The mp4 lives in
`youtube/brutalist/claude-liam-brutalist-skill-explainer/exports/landscape/`
for Bear's viewing.

## What did NOT run (recorded honestly)

- No `slate cut` self-demo. The reel *explains* the command; running it
  here would produce a different reel altogether (a new topic reel), not a
  teardown of the skill. The B09 handoff prompt is paste-ready so a fellow
  can invoke it in their own environment.
- No `pantry.py` demo. This reel deliberately has zero pantry stills — VOX
  LAW makes zero-vox a correct outcome for a doctrine teardown. The
  runtime pantry script is described but not exercised.
- No `scripts/type_check.py` GATE T run. That checker is referenced in the
  toolkit's `CLAUDE.md` but not shipped in this snapshot. Instead, visual
  typography was verified by reading frames — see TYPECHECK.md.
- No `art keys`, no `setup --install`, no external clones. Setup is
  demonstrated by reference (github.com/nikbearbrown/brutalist.art) but
  not actually run.

## Files that exist

- Landscape master: `exports/landscape/claude-liam-brutalist-skill-explainer.mp4`
  (3840×2160, 253.67s — rebuilt 2026-09-11)
- Landscape receipt: `exports/landscape/claude-liam-brutalist-skill-explainer.verified.json`
- QC report: `_qc/REPORT.md` (clean, 0 BLOCKER/MAJOR)
- QC contact sheet: `_qc/contact_sheet.png`
- 11 media beats: `media/B00.mp4 … B10.mp4` (B07 re-rendered 2026-09-11)
- 11 audio beats: `mp3/beat-B00.mp3 … B10.mp3` (B07 regenerated 2026-09-11)
- 11 conformed clips: `clips/B00.mp4 … B10.mp4`
