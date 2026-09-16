# CHECKS-REPORT.md — The godot-waikthrough Skill (landscape)
# run_id: 4d4269b669dd4b84a92a266e5bff804f
# Re-verified 2026-09-12: SKILL.md §4 changed; §1–§3 unchanged; no beat rebuild required.

## Environment

- Toolkit: isolated workspace at `.repoloop/workspaces/claude-liam-brutalist-skill-godot-waikthrough/toolkit`
- Chrome sandbox wrapper: `ART_CHROME=…/runtime/scripts/chrome_wrap_native` with `ART_CHROME_MODE=chrome-for-testing` (Apple App Sandbox Mach-port block)
- Renderer: `python3 runtime/scripts/remotion_scenes.py`, foreground, serial (per BUILD-PROMPT rule #3)
- Compiler: `python3 runtime/scripts/compile.py --height 2160 --out .../exports/landscape`

## Beat rendering (per-beat Remotion)

All 13 landscape beats rendered via remotion_scenes.py. Provenance stamped into `beat_sheet.json` by the renderer.

| Beat | Component | Role |
|---|---|---|
| B00 | ClaudeComposerAsk | cold-open — ask about the skill, three RESULT lines |
| B01 | BrutalistHesitantWriter | BLUF — 'records'→'riffs' correction |
| B02 | WalkerGodotSetup (flow) | pipeline flow: Identify → Capture → Riff → Assemble → Render |
| B03 | SkillTeardownAnatomy | two modes: standard and walker, file listing |
| B04 | GodotDesignBoard | Phase 1 feature inventory: Built/Planned/Broken cards |
| B05 | WalkerGodotSetup (terminal) | Phase 2 capture command, scripted-input label |
| B06 | GodotDevWorkbench (code) | riff mechanic — RIFF.md structure highlighted |
| B07 | WalkerGodotSetup (flow) | walker mode four bookends in exact order |
| B08 | SkillTeardownMechanism | design tell — 'Don't fix the game.' verbatim SKILL.md quote |
| B09 | SkillTeardownMechanism | falsifiability gate + self-demo limitation documented |
| B10 | ClaudeVerdictArtifact | verdict — four artifact lines, @HumanitariansAI brand |
| B11 | ClaudeComposerAsk | Your Turn — paste-ready feature inventory prompt |
| B12 | ClaudeTitleOutro | outro — @NikBearBrown hardcoded per OUTRO-LOCK.md |

## Compile

```
[art] compiled B00-B12 (all VIDEO, all durations match beat_sheet)
[art] build stamp → beat_sheet.json (13/13 filled)
[art] wrote exports/landscape/claude-liam-brutalist-skill-godot-waikthrough.mp4 (269.3s)
[art] slots: 13/13 filled — all VIDEO
```

## Gate V (frame-level QC) — re-run 2026-09-12

```
python3 runtime/qc/final_frame_check.py <reel_dir> --mp4 exports/landscape/…mp4
[gate-v] frames=26 BLOCKER=0 MAJOR=0 → _qc/REPORT.md
```

26 frames sampled (13 beats × 2 fractions: 50%, 85%). Zero blocking edge-bleed defects, zero major underfill/clustered/low-contrast.

## MP4 verification

`ffprobe` — landscape master:
- width=3840, height=2160, codec=h264
- duration=269.3s
- SHA-256 = `6f5f0824b1c025afedb0bfc0dada0f8ca5dc6af43e496f3e89c6f02c86aaa686`

Compiler's atomic verification produced `claude-liam-brutalist-skill-godot-waikthrough.verified.json`.

## Manual visual inspection

Per BUILD-PROMPT rule #6, the contact sheet was read with the image-capable Read tool.
See `_qc/contact_sheet.png` and `VISUAL-REVIEW.json`.

- All 13 beats resolve to real content (no unresolved slates).
- B00 folder chip reads `@HumanitariansAI`.
- B12 outro reads `The godot-waikthrough Skill` + `@NikBearBrown` (OUTRO-LOCK.md compliance).
- Ink stays within landscape title-safe inset; no edge bleed detected.
- All five Godot/skill scene types present: ClaudeComposerAsk, BrutalistHesitantWriter, WalkerGodotSetup, GodotDesignBoard, GodotDevWorkbench, SkillTeardownAnatomy, SkillTeardownMechanism, ClaudeVerdictArtifact, ClaudeTitleOutro.

## Available checks that ran

- `remotion_scenes.py` render (composition ID resolution + Zod schema validation)
- `compile.py` — Gate F (paperwork), Gate V (frame-level QC), atomic verify
- `final_frame_check.py` — re-run 2026-09-12; REPORT.md confirmed clean (frames=26, BLOCKER=0, MAJOR=0)

## Available checks that did NOT run

- `scripts/type_check.py` — not present in this isolated toolkit. See `TYPECHECK.md`.
- Kerning-only lint — inspected as part of manual frame-image review.
- YouTube-side transcoding — not applicable pre-upload.

## Source change assessment

SKILL.md §4 gained: frame-fraction duration preservation rules, compositor ratio verification, `qc.contrast_regions` spec, explicit prohibition on relabeling gameplay as source report. All additions apply to live gameplay production runs. Teaching content (§1 Identify, §2 Play+capture+riff, §3 Assemble) is unchanged. No beat content required updating.
