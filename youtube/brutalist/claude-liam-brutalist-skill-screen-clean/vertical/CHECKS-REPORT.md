# CHECKS-REPORT — The screen-clean Skill (vertical 2160×3840)

Run ID: `dea2eb64b9844f9e916970a58f8cbdb2` (re-verified 2026-09-12; original build run_id `2c0eeb9aca3643d5ba5e51c8e28c2ca8`)
Toolkit commit (baseline): `ba2d0e0f043f5b3b35a50d336e0fc66fbfecfc0c` + local overrides
Source SHA-256 (episode.source_sha256): `cd5d58c4ce5cd8fd1ce5d12760e927dc17f9b53ca259055e27b3351a62e11803` (changed from `df40ee62…` due to toolkit local overrides; SKILL.md content unchanged at `c50640bf…`)
Source SHA-256 (SOURCE-SNAPSHOT capture): `c50640bff9f4de41030672d6c4de48cfb110aa398d302b1ba8d11f4ddb7c6efb`

**Re-verification note (2026-09-12):** Same trigger as landscape. Gate V re-run on existing vertical MP4: 0 BLOCKER, 0 MAJOR. No scene re-rendering required.

## Audio — `runtime/scripts/generate_audio_kokoro.py`

```
python3 runtime/scripts/generate_audio_kokoro.py \
  youtube/brutalist/claude-liam-brutalist-skill-screen-clean/vertical
```

- 12/12 beats generated with voice `am_onyx` (Kokoro, local, free)
- Cost: **$0.00**
- Same narration text as landscape → same measured durations → same audio
  clock. `beat_sheet.json` in the vertical folder has its own copy with
  `slug: claude-liam-brutalist-skill-screen-clean-vertical` and
  `aspect_ratio: 9:16`.

## Scene renderer — `runtime/scripts/remotion_scenes.py`

```
ART_CHROME=/tmp/claude-501/chrome-single-process.sh \
ART_CHROME_MODE=chrome-for-testing \
python3 runtime/scripts/remotion_scenes.py \
  youtube/brutalist/claude-liam-brutalist-skill-screen-clean/vertical --force
```

All 12 patterns rendered as NATIVE portrait compositions (1080×1920 base,
scale=2 → 2160×3840 output):

- B00 → `ClaudeComposerAsk916` (already registered in Root.tsx)
- B01 → `BrutalistHesitantWriter916` (already registered)
- B02 → `SkillTeardownAnatomy916` (registered in Root.tsx by this build)
- B03 → `SkillTeardownPipeline916` (registered in Root.tsx by this build)
- B04–B08 → `SkillTeardownMechanism916` (registered in Root.tsx by this build)
- B09 → `ClaudeVerdictArtifact916` (already registered)
- B10 → `ClaudeComposerAsk916`
- B11 → `ClaudeTitleOutro916` (already registered)

**Native portrait layouts** — no cropped landscape. The three
`SkillTeardown…916` components were copied from the ep 17 (nbb) workspace
where they were first authored for the same skill-teardown modifier, and
registered natively in this workspace's isolated `Root.tsx` (stack/reflow
layouts sized to 1080×1920).

## Compile — `runtime/scripts/compile.py`

```
python3 runtime/scripts/compile.py \
  youtube/brutalist/claude-liam-brutalist-skill-screen-clean/vertical \
  --height 3840 \
  --out youtube/brutalist/claude-liam-brutalist-skill-screen-clean/exports/vertical \
  --force
```

- 12/12 beats compiled with per-beat VIDEO source
- Total duration: **318.166667 s** (matches landscape — same audio clock)
- Master output:
  `exports/vertical/claude-liam-brutalist-skill-screen-clean-vertical.mp4`
- `ffprobe` v:0 → width=2160 height=3840 (native 4K portrait, not
  upscaled/cropped), codec_name=h264
- `ffprobe` a:0 → codec_name=aac, sample_rate=48000, channels=2
- Audio present: `ffmpeg -af volumedetect` → `mean_volume: -27.1 dB`
- Skin-lint warnings (informational, matches ep 17 nbb pattern):
  - `B00: palette=claude but the cold open is 'ClaudeComposerAsk916' —
    COLD OPEN LAW wants ClaudeComposerAsk` — the 916 variant IS the
    portrait cold open; the lint doesn't know that.
  - `B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO
    LAW wants ClaudeTitleOutro` — same situation.
- Motion histogram warning identical to landscape (`reveal 8/12`). Not a
  blocker; teardown reels lean on reveal.

## Gate V — `runtime/qc/final_frame_check.py`

- 24 frames sampled (each beat at 50 % and 85 %)
- BLOCKER: **0**
- MAJOR: **0**
- Result: **Clean** (`_qc/REPORT.md`)
- Contact sheet: `_qc/contact_sheet.png` (0504cad8…)

### Fixes that pushed Gate V clean

First pass reported 2 BLOCKER + 2 MAJOR:

- `B01_50 / B01_85 — underfill (35–36 % vs 55 % floor)`. Root cause: the
  portrait BLUF hesitant-writer text at fontSize 130 / lineSpacing 2.5
  under-filled with the 6-line breakdown. Fix per memory
  `feedback_hesitant_writer_portrait_bluf_recipe` — raised
  `lineSpacing` first, then a moderate `fontSize` bump: **fontSize
  130 → 160**, **lineSpacing 2.5 → 2.7**. Seed rotated to
  `screen-clean-bluf-vertical-2026-2c0eeb9a-v2`.
- `B10_50 / B10_85 — edge-bleed (composer crosses title-safe bottom)`.
  Root cause: the paste-ready ffmpeg command was ~570 chars, wrapping
  the composer past the safe boundary in portrait. Fix: tightened the
  composer's `command` prop to ~370 chars (still safe by construction,
  still exercises Pass 1, still names the A/B/C table for Pass 2), and
  re-rendered B10. Narration text (spoken over the beat) is unchanged
  — Liam still reads the full doctrine dry-run out loud.

After the two-beat re-render and recompile: `BLOCKER: 0 · MAJOR: 0`.

## Visual review by AI reviewer

Opened the vertical contact sheet + representative proof frames. Confirmed
in native portrait layout:

- B00 (cold open): composer with `Bonjour, Liam` greeting, ask, output,
  folder chip `@HumanitariansAI`.
- B01 (BLUF): correction `auto-blurs → flags` lands on line 2; final
  read stacks the sentence across 6 legible portrait lines: "The
  screen-clean skill / flags / your desktop / into a safe reel beat. /
  The proof is / the sheet." — content fills ≥ 55 % safe area.
- B02 (anatomy): folder tree renders vertically with `SKILL.md`
  accented, both callers tagged.
- B03 (pipeline): five phases stack cleanly, `PROBE` accented.
- B04–B08 (mechanism / falsifiability): eyebrow / heading / body /
  quote / verdict pill stack in portrait.
- B09 (verdict): artifact card fills, six lines readable.
- B10 (Your Turn): composer with the tightened paste-ready command;
  three viewer-checkable output lines below.
- B11 (outro): title "The screen-clean Skill." with terracotta period,
  `@NikBearBrown` handle, seeded mascot.

No burned-in captions, no unresolved slates, inner composer chips read
`@HumanitariansAI`, outro handle stays `@NikBearBrown` (OUTRO-LOCK).

## Gaps and honest notes

Same as landscape (see landscape `CHECKS-REPORT.md`). Portrait review is
independent of landscape's — both aspects pass Gate V independently at
their native resolutions. No upscale or crop was used to synthesize the
portrait.
