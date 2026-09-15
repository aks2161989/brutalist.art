# CHECKS-REPORT.md — The sri-explainer Skill (landscape)

## Re-run: 2026-09-12 (run_id a960d8bf6f6e4238996f9688a426dab9)

Source `skills/make/sri-explainer/SKILL.md` changed since the prior build
(run_id `98242bd156b94a388dae9e858c502e8c`). Key change: commit `109241e`
corrected the Notebook look camera rule from "moving camera on every beat" to
"static/locked-off camera on ordinary 2D beats; camera orbit only on real 3D
beats". No beat narrates the camera rule — all 14 beats remain factually
accurate. Clips and audio were not regenerated. Both aspects recompiled with
`--force` against the existing per-beat clips. Gate V re-run: BLOCKER=0
MAJOR=0 on both aspects. VISUAL-REVIEW.json updated with this run_id.

---


## Environment

- Toolkit: isolated workspace at
  `.repoloop/workspaces/claude-liam-brutalist-skill-sri-explainer/toolkit`
- Chrome sandbox wrapper: `ART_CHROME=…/runtime/scripts/chrome_wrap.sh`
  (chrome-headless-shell + `--single-process`; the App Sandbox / Mach-port
  fix. Absent from this isolated toolkit's snapshot; copied in from the
  sibling `claude-liam-brutalist-skill-nopunt` toolkit that already had it.)
- Node modules shadowed: `runtime/remotion/node_modules` was a symlink to
  the public toolkit's directory, which is read-only from this sandbox;
  webpack's `.cache/` needed to write. Replaced the symlink with a per-entry
  symlink shadow whose top-level `.cache/` is a real writable directory.
- Renderer: `python3 runtime/scripts/remotion_scenes.py`, foreground, serial
  (per BUILD-PROMPT rule #4).
- Compiler: `python3 runtime/scripts/compile.py --height 2160 --out
  …/exports/landscape`.

## Beat rendering (per-beat Remotion)

All 14 beats rendered successfully as native 3840×2160 mp4s via
`--scale=2 --image-format=png --crf=16` (see `remotion_scenes.py`).

| Beat | Component | Result |
|---|---|---|
| B00 | `ClaudeComposerAsk` | `ok: ClaudeComposerAsk -> media/B00.mp4` |
| B01 | `BrutalistHesitantWriter` | `ok: BrutalistHesitantWriter -> media/B01.mp4` |
| B02 | `SkillTeardownAnatomy` | `ok: SkillTeardownAnatomy -> media/B02.mp4` |
| B03 | `SkillTeardownMechanism` | `ok: SkillTeardownMechanism -> media/B03.mp4` |
| B04 | `SkillTeardownPipeline` | `ok: SkillTeardownPipeline -> media/B04.mp4` |
| B05–B09, B10 | `SkillTeardownMechanism` × 6 | `ok: SkillTeardownMechanism -> media/B0{5..9,10}.mp4` |
| B11 | `ClaudeVerdictArtifact` | `ok: ClaudeVerdictArtifact -> media/B11.mp4` |
| B12 | `ClaudeComposerAsk` | `ok: ClaudeComposerAsk -> media/B12.mp4` |
| B13 | `ClaudeTitleOutro` | `ok: ClaudeTitleOutro -> media/B13.mp4` |

Provenance stamped into `beat_sheet.json` by the renderer.

## Compile

```
[art] compiled B00-B13 (all VIDEO, all durations match beat_sheet)
[art] motion histogram: reveal:10  type-on:3  hold:1
[art] WARNING: 'reveal' carries 10/14 beats (71%) — over the ~40% pantry cap
[art] build stamp → beat_sheet.json (14/14 filled)
[art] wrote exports/landscape/claude-liam-brutalist-skill-sri-explainer.mp4 (281.8s)
[art] slots: 14/14 filled
```

**Motion histogram warning** — accepted, same reason as the nopunt and
deep-explainer skill teardowns before this one: the eight
`SkillTeardownMechanism` beats (B03, B05–B09, B10) share a reveal pattern
by design. Splitting them into distinct motion languages would sacrifice
the skill-teardown consistency the component was built for.

## Gate V (frame-level QC)

```
python3 runtime/qc/final_frame_check.py \
  <reel> --mp4 exports/landscape/claude-liam-brutalist-skill-sri-explainer.mp4 \
  --sheet clips/_work/resolved-sheet.json
[gate-v] frames=28 BLOCKER=0 MAJOR=0 → _qc/REPORT.md
```

14 beats × 2 fractions (50 %, 85 %) = 28 frames sampled and analyzed.
Zero blocking edge-bleed defects, zero major underfill / clustered /
low-contrast.

Note on iteration — B01 first came back at `MAJOR underfill (23 %)`
because the ink bbox was too small on the cream stage. Bumped
`fontSize` 158 → 190 and `lineSpacing` 1.25 → 1.5, and expanded the
overview from 2 lines to 3 (`"sri-explainer takes\na concept\nand
explains it."`); re-rendered; then Gate V returned clean.

## MP4 verification

`ffprobe` — landscape master:

- `width=3840  height=2160  codec_name=h264`
- `duration=281.750000` (matches sum of `actual_duration_s`)
- audio `codec_name=aac  duration=281.750000`
- SHA-256 = `b0d0e60a03bda0e896525f74fe7bdb433cda8fd96403e8c1f51196edcfb8235a`

The compiler's atomic verification produced a
`claude-liam-brutalist-skill-sri-explainer.verified.json` receipt beside
the final.

## Manual visual inspection

Per BUILD-PROMPT rule #6, frames were sampled from `media/B{beat}.mp4`
at 50 % / 85 % of each beat's span for Gate V, plus a per-beat mid-frame
extracted with `ffmpeg -ss <mid> -vframes 1` and opened with the image-
capable Read tool. Observations:

- All 14 beats resolve to real content (no unresolved slates).
- Composer folder chip on B00/B12 reads `@HumanitariansAI` (playlist
  adaptation).
- B01 BLUF: writer types "sri-explainer takes / a concept / and explains
  it.", 'concept' turns terracotta then deletes and 'chapter' types in,
  final corrected sentence "sri-explainer takes / a chapter / and
  explains it." stands.
- B02 anatomy card: folder tree with SKILL.md accent + terracotta
  DOCTRINE tag, callout box lands cleanly.
- B04 pipeline: five phase nodes (Cold open → HOOK → SETUP → MECHANISM
  → GROUNDING → OUTRO) with HOOK terracotta-accented.
- B05–B10 mechanism cards: quote block cite lines read cleanly at 4K;
  verdict pills all fit inside safe area.
- B11 verdict artifact: cream card with six verdict lines, numbered.
- B13 outro (`ClaudeTitleOutro`): title "The sri-explainer Skill.", the
  hardcoded `@NikBearBrown` handle, and a slug-seeded pixel mascot (per
  OUTRO-LOCK.md) — the mascot is 1 of the 18 crisp-safe animations.
- Ink stays within the landscape title-safe inset
  (SAFE x=192-3648, y=108-2052 at 4K).

## Available checks that ran

- `remotion_scenes.py --list` and per-composition renders (implicit
  `--check` via composition ID resolution — a bad name would fail loud).
- `./art scenes --check <Name>` for every named composition — recorded
  in `demo/scenes-search.log`.
- `./art scene-index` — regenerated `runtime/remotion/src/scenes.json`
  after registering the three `SkillTeardown*916` compositions in the
  isolated toolkit's `Root.tsx`.
- `compile.py` final gates: `Gate F` (paperwork), `Gate V` (frame-level
  QC), atomic verify (`.verified.json` receipt).
- `final_frame_check.py` — run inside the compile pipeline.

## Available checks that did NOT run

- `scripts/type_check.py` — the legacy checker referenced in some older
  docs is NOT present in this isolated toolkit. See `TYPECHECK.md` for
  the substitute review.
- Kerning-only lint — not shipped as a separate tool; kerning inspected
  as part of the manual frame-image review.
- YouTube-side transcoding + processing checks — not applicable pre-
  upload; nothing was uploaded.
