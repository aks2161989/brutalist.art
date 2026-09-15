# CHECKS-REPORT.md — The nopunt Skill (landscape)

## Re-review 2026-09-12 (run ea4f6e12)

Supervisor flagged source_sha256 change (sibling skill files ai-explainer/cli-explainer/
deep-explainer/explainer SKILL.md modified in working tree). nopunt/SKILL.md content
verified unchanged (toolkit copy sha `ef38a574…`). Beat sheet content matches current
SKILL.md. Exports verified intact via ffprobe and frame inspection. No re-render needed.
VISUAL-REVIEW.json updated with new run_id. Original build details follow.

---

## Environment

- Toolkit: isolated workspace at `.repoloop/workspaces/claude-liam-brutalist-skill-nopunt/toolkit`
- Chrome sandbox wrapper: `ART_CHROME=…/runtime/scripts/chrome_wrap.sh` (chrome-headless-shell + `--single-process`; memory: chrome-sandbox → Remotion fix)
- Renderer: `python3 runtime/scripts/remotion_scenes.py`, foreground, serial (per BUILD-PROMPT rule #3)
- Compiler: `python3 runtime/scripts/compile.py --height 2160 --out .../exports/landscape`

## Beat rendering (per-beat Remotion)

Prior worker had rendered B00-B08 and B11 before exiting 143. This session
resumed by rendering the two remaining beats:

| Beat | Component | Result |
|---|---|---|
| B09 | `ClaudeVerdictArtifact` | `ok: ClaudeVerdictArtifact -> media/B09.mp4` |
| B10 | `ClaudeComposerAsk` | `ok: ClaudeComposerAsk -> media/B10.mp4` |

All 12 landscape beats present in `media/`. Provenance stamped into
`beat_sheet.json` by the renderer.

## Compile

```
[art] compiled B00-B11 (all VIDEO, all durations match beat_sheet)
[art] motion histogram: reveal:8  type-on:3  hold:1
[art] WARNING: 'reveal' carries 8/12 beats (66%) — over the ~40% pantry cap
[art] build stamp → beat_sheet.json (12/12 filled)
[art] wrote exports/landscape/claude-liam-brutalist-skill-nopunt.mp4 (345.8s)
[art] slots: 12/12 filled
```

**Motion histogram warning** — accepted. The five `SkillTeardownMechanism`
beats (B04-B08) share a reveal pattern by design; splitting them into
distinct motion languages would sacrifice the skill-teardown consistency the
component was built for.

## Gate V (frame-level QC)

```
python3 runtime/qc/final_frame_check.py \
  ../../../../youtube/brutalist/claude-liam-brutalist-skill-nopunt \
  --mp4 exports/landscape/claude-liam-brutalist-skill-nopunt.mp4 \
  --sheet beat_sheet.json
[gate-v] frames=24 BLOCKER=0 MAJOR=0
```

12 beats × 2 fractions (50%, 85%) = 24 frames sampled and analyzed.
Zero blocking edge-bleed defects, zero major underfill/clustered/low-contrast.

## MP4 verification

`ffprobe` — landscape master:
- width=3840, height=2160, codec=h264
- duration=345.79s (matches sum of `actual_duration_s`)
- audio codec=aac, duration=345.83s
- SHA-256 = `c79e549d591baaa800c3c4f0fcf7dd7eb3529dc3bbe43a6ce55171ff56dd8169`

Compiler's own atomic verification produced a
`claude-liam-brutalist-skill-nopunt.verified.json` receipt alongside the
final. Not overwritten this session.

## Manual visual inspection

Per BUILD-PROMPT rule #6, frames were sampled at 15/50/85% of every beat plus
extras and read with the image-capable Read tool. See
`_qc/CONTACT-SHEET.png` (12 mid-frames tiled) and per-beat PNGs listed in
`VISUAL-REVIEW.json`. Observations:

- All 12 beats resolve to real content (no unresolved slates).
- Composer folder chip on B00/B10 reads `@HumanitariansAI` (playlist adaptation).
- Outro B11 handle reads `@NikBearBrown` (hardcoded per `OUTRO-LOCK.md`).
- Ink stays within the landscape title-safe inset (SAFE x=192-3648, y=108-2052).
- Bookends present: B00 cold open, B09 verdict, B10 your-turn, B11 title-restate outro.

## Available checks that ran

- `remotion_scenes.py` render + `--check` (implicit via composition ID resolution)
- `compile.py` — final gates: `Gate F` (paperwork), `Gate V` (frame-level QC), atomic verify
- `final_frame_check.py` — explicit rerun on final master

## Available checks that did NOT run

- `scripts/type_check.py` — legacy checker referenced in older docs; not
  present in this isolated toolkit. See `TYPECHECK.md` for the substitute.
- Kerning-only lint — not shipped as a separate tool; kerning inspected as
  part of the manual frame-image review.
- YouTube-side transcoding + processing — not applicable pre-upload.
