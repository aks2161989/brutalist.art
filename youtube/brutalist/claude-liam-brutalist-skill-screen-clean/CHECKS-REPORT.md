# CHECKS-REPORT — The screen-clean Skill (landscape 3840×2160)

Run ID: `dea2eb64b9844f9e916970a58f8cbdb2` (re-verified 2026-09-12; original build run_id `2c0eeb9aca3643d5ba5e51c8e28c2ca8`)
Toolkit commit (baseline): `ba2d0e0f043f5b3b35a50d336e0fc66fbfecfc0c` + local overrides listed in `SOURCE-SNAPSHOT.json`
Source SHA-256 (episode.source_sha256): `cd5d58c4ce5cd8fd1ce5d12760e927dc17f9b53ca259055e27b3351a62e11803` (changed from `df40ee62…` due to toolkit local overrides; SKILL.md content unchanged at `c50640bf…`)
Source SHA-256 (SOURCE-SNAPSHOT capture): `c50640bff9f4de41030672d6c4de48cfb110aa398d302b1ba8d11f4ddb7c6efb`

**Re-verification note (2026-09-12):** The source_sha256 change was triggered by toolkit file changes (RequireReport.tsx, Root.tsx, TrainTeacher.tsx, BarChart.tsx) — none of which are used by this episode's scenes. SKILL.md content is unchanged. Video exports match prior verified hashes. Gate V was re-run on both existing MP4s (foreground, no re-render): 0 BLOCKER, 0 MAJOR each. No scene re-rendering was required.

## Audio — `runtime/scripts/generate_audio_kokoro.py`

```
python3 runtime/scripts/generate_audio_kokoro.py \
  youtube/brutalist/claude-liam-brutalist-skill-screen-clean
```

- 12/12 beats generated with voice `am_onyx` (Kokoro, local, free)
- Cost: **$0.00**
- Durations become GROUND TRUTH and are stamped back into `beat_sheet.json`
- Total narration: 296.03 s of audio (before per-beat freeze-pad conform)

## Scene renderer — `runtime/scripts/remotion_scenes.py`

```
ART_CHROME=/tmp/claude-501/chrome-single-process.sh \
ART_CHROME_MODE=chrome-for-testing \
python3 runtime/scripts/remotion_scenes.py \
  youtube/brutalist/claude-liam-brutalist-skill-screen-clean --force
```

All 12 patterns rendered at supersampled 2× (target 3840×2160):

- B00 → `ClaudeComposerAsk`
- B01 → `BrutalistHesitantWriter`
- B02 → `SkillTeardownAnatomy`
- B03 → `SkillTeardownPipeline`
- B04–B08 → `SkillTeardownMechanism`
- B09 → `ClaudeVerdictArtifact`
- B10 → `ClaudeComposerAsk`
- B11 → `ClaudeTitleOutro`

Environment workarounds applied:

- Chrome wrapper (`ART_CHROME`) is the Apple-App-Sandbox workaround from
  memory `feedback_chrome_sandbox`: `chrome-headless-shell` invoked with
  `--single-process --in-process-gpu`.
- The isolated toolkit's `runtime/remotion/node_modules` was a read-only
  symlink into the live toolkit. Per memory
  `feedback_isolated_toolkit_node_modules_shadow` it was shadowed with a
  directory of per-entry symlinks and a writable local `.cache/` so
  webpack could persist its production cache. This is the standard fix.

## Compile — `runtime/scripts/compile.py`

```
python3 runtime/scripts/compile.py \
  youtube/brutalist/claude-liam-brutalist-skill-screen-clean \
  --height 2160 \
  --out youtube/brutalist/claude-liam-brutalist-skill-screen-clean/exports/landscape \
  --force
```

- 12/12 beats compiled with per-beat VIDEO source
- Total duration: **318.166667 s** (from measured audio timeline)
- Master output: `exports/landscape/claude-liam-brutalist-skill-screen-clean.mp4`
- `ffprobe` v:0 → width=3840 height=2160 (native 4K, not upscaled), codec_name=h264
- `ffprobe` a:0 → codec_name=aac, sample_rate=48000, channels=2
- Audio present: `ffmpeg -af volumedetect` → `mean_volume: -27.1 dB`
- Motion histogram: `reveal:8  type-on:3  hold:1`
  - WARNING (not blocker): `reveal` at 66% vs ~40% pantry cap. Skill-teardown
    reels lean on reveal for the four mechanism cards + anatomy + pipeline +
    falsifiability, which is the register. Same warning appeared on ep 17
    (nbb) and passed the same way.

## Gate V — `runtime/qc/final_frame_check.py`

```
python3 runtime/qc/final_frame_check.py \
  youtube/brutalist/claude-liam-brutalist-skill-screen-clean \
  --mp4 <compile candidate.mp4>
```

- 24 frames sampled (each beat at 50 % and 85 %)
- BLOCKER: **0**
- MAJOR: **0**
- Result: **Clean** (`_qc/REPORT.md`, preserved as `_qc/REPORT-landscape.md`)
- Contact sheet: `_qc/contact_sheet.png` (55536d7e76…), preserved as
  `_qc/contact_sheet_landscape.png`

### Fix that pushed Gate V clean

First pass BLUF (B01) failed at 41% coverage of the safe area (MAJOR × 2 at
50 % and 85 %). Root cause: the initial 4-line text had two short lines
("into a safe", "reel beat.") that kept the block small. Fix:

1. Rebalanced to four ~22-char lines and rewrote the trailing line to
   surface the second mechanism the film argues (`The proof is the sheet.`
   — a compact echo of Pass-2 falsifiability):

   ```
   The screen-clean skill
   auto-blurs your desktop
   into a safe reel beat.
   The proof is the sheet.
   ```

2. Rotated `seed` to `screen-clean-bluf-2026-2c0eeb9a-v3` (v1 = original,
   v2 = 4-line at fontSize 148, v3 = the winning combination).
3. Raised `fontSize` from 148 → 172 and `lineSpacing` from 1.25 → 1.35 —
   the well-known lift for landscape underfill.
4. Re-rendered only B01 via `remotion_scenes.py --only B01 --force`, then
   `compile.py --force` for reassembly. Gate V re-ran and returned clean.

## Visual review by AI reviewer

Opened the contact sheet and inspected representative beat frames with the
image-capable Read tool. All 12 beats read clearly. Specifically confirmed:

- B00 (cold open): composer with `Bonjour, Liam` greeting, ask text, three
  output lines, folder chip `@HumanitariansAI`, effort label `Teardown`.
- B01 (BLUF): correction `auto-blurs → flags` lands. Final read on screen:
  "The screen-clean skill flags your desktop into a safe reel beat. The
  proof is the sheet."
- B02 (anatomy): folder tree with `skills/make/screen-clean/SKILL.md`
  accented, `fellows/` and `guests/` tagged `caller`, callout box quotes
  "Format is orthogonal to relationship."
- B03 (pipeline): 5-phase card with `PROBE` accented terracotta, plus
  input/output nodes.
- B04–B08 (mechanism, falsifiability): each carries eyebrow, heading,
  body, verbatim quote, cite, verdict pill, and spark line.
- B09 (verdict): six lines readable; artifact heading
  "A gate. A crop. A flag. A sheet."
- B10 (Your Turn): composer greeting `Your Turn`, paste-ready ffmpeg
  command visible, three viewer-checkable output lines.
- B11 (outro): title "The screen-clean Skill." with terracotta period,
  hardcoded `@NikBearBrown` handle (OUTRO-LOCK), slug-seeded mascot.

No burned-in captions anywhere. No unresolved slates. Inner composer chips
read `@HumanitariansAI`; the outro handle stays `@NikBearBrown`.

## Local safe demo — `demo/`

Two synthetic screen recordings generated with `ffmpeg -f lavfi`
(2560×1600, 6 s, dark grey fill). Nothing personal touched.

- `silent-screen-recording.mp4` + `anullsrc` audio → `mean_volume: -91.0 dB`
  → STOP (below the -40 dB gate).
- `voiced-screen-recording.mp4` + 440 Hz sine → `mean_volume: -21.1 dB`
  → proceed.

Full command log preserved in `demo/screen-clean-run.log`.

## Gaps and honest notes

- `scripts/type_check.py` — NOT PRESENT in this toolkit revision.
  Substituted actual frame inspection via Gate V. See `TYPECHECK.md`.
- `reference/type-spec.md` — NOT PRESENT. Not fabricated.
- `ILLUSTRATIONS.md` — NOT PRESENT. Not fabricated.
- Passes 2, 3, 4, 5 of `screen-clean` are illustrated per REBUILD LAW from
  the SKILL.md (the A/B/C table is redrawn; the privacy list is quoted).
  They were not exercised end-to-end against a real recording, because
  none was provided and the doctrine matters more than a live crop for a
  teardown reel. Documented in `FACTCHECK.md § Boundary`.
- Higgsfield / paid tiers were not invoked. No API keys read. No push,
  no upload, no publication.
- The reveal-heavy motion histogram warning is documented above and is
  not a blocker per compile.py's own gate logic. It matches the
  same-shape warning on episode 17 (nbb).
