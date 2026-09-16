# CHECKS-REPORT.md — The riff Skill (landscape)

## Environment

- Toolkit: isolated workspace at `.repoloop/workspaces/claude-liam-brutalist-skill-riff/toolkit`
- Chrome sandbox wrapper: `ART_CHROME=…/runtime/scripts/chrome_wrap_native` with shadow `.bin/remotion` Node.js shebang wrapper (Apple App Sandbox Mach-port block patched via `--single-process` on darwin)
- Renderer: `python3 runtime/scripts/remotion_scenes.py`, foreground, serial (per BUILD-PROMPT rule #3)
- Compiler: `python3 runtime/scripts/compile.py --height 2160 --out .../exports/landscape`

## Beat rendering (per-beat Remotion)

All 12 landscape beats rendered via remotion_scenes.py. Provenance stamped into `beat_sheet.json` by the renderer.

| Beat | Component | Pattern |
|---|---|---|
| B00 | ClaudeComposerAsk | cold-open composer prompt |
| B01 | BrutalistHesitantWriter | hesitant-writing animation — "riff generates opinions" corrects to "observations" |
| B02 | SkillTeardownAnatomy | skill anatomy: folder tree reveals skills/make/riff/SKILL.md |
| B03 | SkillTeardownPipeline | 4-phase pipeline with terracotta arrows |
| B04 | SkillTeardownMechanism | mechanism card 1 — what riff does |
| B05 | ClaudeCodeBeat | self-demo: real ./art scenes output |
| B06 | SkillTeardownMechanism | mechanism card 2 — how riff structures output |
| B07 | SkillTeardownMechanism | mechanism card 3 — riff doctrine |
| B08 | SkillTeardownMechanism | design tell — what makes riff distinct |
| B09 | ClaudeVerdictArtifact | artifact card with 4 verdict lines |
| B10 | ClaudeComposerAsk | Your Turn prompt |
| B11 | ClaudeTitleOutro | Liam sign-off, @HumanitariansAI |

## Compile

```
[art] compiled B00-B11 (all VIDEO, all durations match beat_sheet)
[art] build stamp → beat_sheet.json (12/12 filled)
[art] wrote exports/landscape/claude-liam-brutalist-skill-riff.mp4 (234.5s)
[art] slots: 12/12 filled — B00:VIDEO B01:VIDEO B02:VIDEO B03:VIDEO B04:VIDEO B05:VIDEO B06:VIDEO B07:VIDEO B08:VIDEO B09:VIDEO B10:VIDEO B11:VIDEO
```

## Gate V (frame-level QC)

Run: `python3 runtime/qc/final_frame_check.py <reel> --mp4 exports/landscape/claude-liam-brutalist-skill-riff.mp4`

```
[gate-v] frames=24 BLOCKER=0 MAJOR=0 → _qc/REPORT.md
```

Re-run under current invocation run_id `deb461319da4431a9518a6feef4fa1ec` on existing export.
12 beats × 2 fractions (50%, 85%) = 24 frames sampled and analyzed.
Zero blocking edge-bleed defects, zero major underfill/clustered/low-contrast.

## MP4 verification

`ffprobe` — landscape master:
- width=3840, height=2160, codec=h264
- duration=234.5s
- SHA-256 = `44a8ebe91140e31bee457d003d794fc68cb920ca8d215a2c70d13c6ac4c8a124`

Compiler's atomic verification produced `claude-liam-brutalist-skill-riff.verified.json`.

## Manual visual inspection

Per BUILD-PROMPT rule #6, the contact sheet and individual beat frames were reviewed.
See `_qc/contact_sheet.png` and `VISUAL-REVIEW.json`.

- All 12 beats resolve to real content (no unresolved slates).
- Composer folder chip on B00 reads `@HumanitariansAI`.
- Outro B11 reads `Liam, in for Bear.` + `@HumanitariansAI`.
- Ink stays within landscape title-safe inset.
- B01 fontSize reduced to 100 to prevent edge-bleed at 4K; contextTitle and brandLabel added for fill coverage.
- B05 ClaudeCodeBeat shows real `./art scenes` terminal output in monospace.

## Available checks that ran

- `remotion_scenes.py` render (composition ID resolution + Zod schema validation)
- `compile.py` — Gate F (paperwork), Gate V (frame-level QC), atomic verify
- `final_frame_check.py` — runs inside compile; REPORT.md confirmed clean

## Available checks that did NOT run

- `scripts/type_check.py` — not present in this isolated toolkit. See `TYPECHECK.md`.
- Kerning-only lint — inspected as part of manual frame-image review.
- YouTube-side transcoding — not applicable pre-upload.
