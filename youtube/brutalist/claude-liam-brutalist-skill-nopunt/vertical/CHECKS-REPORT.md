# CHECKS-REPORT.md — The nopunt Skill (vertical 9:16)

## Re-review 2026-09-12 (run ea4f6e12)

Supervisor flagged source_sha256 change (sibling skill files). nopunt/SKILL.md content
unchanged; exports verified intact (ffprobe: 2160x3840 h264 345.79s). Inspected portrait
frames (B00, B01, B04, B09×2, B10, B11) — all within SAFE916 inset, no bleed, no
overflow. VISUAL-REVIEW.json updated with new run_id. No re-render needed.
Original build details follow.

---

## Environment

- Toolkit: isolated workspace at `.repoloop/workspaces/claude-liam-brutalist-skill-nopunt/toolkit`
- Chrome sandbox wrapper: `ART_CHROME=…/runtime/scripts/chrome_wrap.sh`
- Renderer: `python3 runtime/scripts/remotion_scenes.py`, foreground, serial
- Compiler: `python3 runtime/scripts/compile.py --height 3840 --out .../exports/vertical`
- Planner: `./art vertical` produced the vertical `beat_sheet.json` with 916
  composition rewires (ClaudeComposerAsk → ClaudeComposerAsk916,
  BrutalistHesitantWriter → BrutalistHesitantWriter916,
  SkillTeardownAnatomy/Pipeline/Mechanism → *916, ClaudeVerdictArtifact →
  ClaudeVerdictArtifact916, ClaudeTitleOutro → ClaudeTitleOutro916). All 12
  portrait compositions are natively registered in `runtime/remotion/src/Root.tsx`
  at `1080×1920` — no landscape crop.

## Beat rendering (per-beat Remotion)

All 12 portrait beats rendered by `remotion_scenes.py` (foreground). B01 and
B10 were re-rendered twice more after Gate V surfaced portrait-specific fit
problems (see "Gate V debugging" below).

## Gate V debugging (why the first compile failed)

The initial `--height 3840` final compile refused with Gate V blocker output:
`edge-bleed` on every one of 24 sampled frames. Root cause investigation:

1. Extracted the compile's --review candidate MP4 and per-beat raw MP4s.
2. B00 raw beat: ink bounds x=[172, 1980] y=[398, 3570] against safe
   x=[108, 2052] y=[192, 3648]. Well within safe. So the raw beat was fine.
3. The compile-time bleed came from `metadata.channel_title` — a compile-time
   overlay that draws the handle centered at the bottom of the FIRST beat.
   In portrait, the safe.b line sits above where the overlay lands. Removed
   `channel_title` and `channel` from `vertical/beat_sheet.json`
   (memory: channel-title-portrait-bleed).
4. Second compile refused with 2 blockers + 2 majors: B01 22% underfill and
   B10 edge-bleed at the bottom.
5. Fixed B01 by bumping `fontSize` 148→300 and `lineSpacing` 1.25→3.0 and
   shortening `text` to a compact 3-line variant that retains the
   `linter→catalog` trigger swap. Portrait-scaled coverage went 22% → 60%.
6. Fixed B10 by shortening the composer `command` prop so the composer card
   plus three output lines fit inside safe.b (3648 in portrait 4K).
7. Third compile passed Gate V (frames=24 BLOCKER=0 MAJOR=0).

## Compile (final)

```
[art] compiled B00-B11 (all VIDEO, all durations match beat_sheet)
[art] motion histogram: reveal:8  type-on:3  hold:1
[art] WARNING: 'reveal' carries 8/12 beats (66%) — over the ~40% pantry cap
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
[art] build stamp → beat_sheet.json (12/12 filled)
[art] wrote exports/vertical/claude-liam-brutalist-skill-nopunt-vertical.mp4 (345.8s)
[art] slots: 12/12 filled
```

**SKIN LINT warnings** — accepted. The COLD OPEN LAW / OUTRO LAW linter
recognizes only the landscape component names; the portrait *916 aliases are
the correct native portrait pattern per `./art vertical` rewire. No action.

**Motion histogram warning** — accepted, same reason as landscape.

## Gate V (frame-level QC)

```
python3 runtime/qc/final_frame_check.py \
  ../../../../youtube/brutalist/claude-liam-brutalist-skill-nopunt/vertical \
  --mp4 exports/vertical/claude-liam-brutalist-skill-nopunt-vertical.mp4 \
  --sheet vertical/beat_sheet.json
[gate-v] frames=24 BLOCKER=0 MAJOR=0
```

## MP4 verification

`ffprobe` — vertical master:
- width=2160, height=3840, codec=h264
- duration=345.79s
- audio codec=aac, duration=345.83s
- SHA-256 = `0a345d44717058db9e6164b0acf6936b0031489cc422c930056018d1594d2ba9`

Dimensions confirm native 4K portrait — not an upscaled landscape crop.

## Manual visual inspection

Frames sampled at 15/50/85% of every beat plus extras and read with the
image-capable Read tool. See `_qc/CONTACT-SHEET.png` (12 mid-frames tiled)
and per-beat PNGs listed in `VISUAL-REVIEW.json`. Observations:

- B01 BrutalistHesitantWriter916 now displays legibly, trigger swap intact.
- B10 ClaudeComposerAsk916 command fits inside safe.b with no overflow.
- All 12 beats resolve to real content.
- Composer folder chip on B00/B10 reads `@HumanitariansAI`.
- Outro B11 handle reads `@NikBearBrown` (per OUTRO-LOCK).
- Portrait safe area (x=108-2052, y=192-3648) respected on every beat.

## Available checks that did NOT run

- `scripts/type_check.py` — legacy checker not shipped in this toolkit.
- YouTube-side transcoding + processing checks — not applicable pre-upload.
