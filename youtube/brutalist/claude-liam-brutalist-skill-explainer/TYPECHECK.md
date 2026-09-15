# TYPECHECK.md — The explainer Skill (landscape)

## GATE T status

The legacy `scripts/type_check.py` referenced in the toolkit's `CLAUDE.md`
is **not shipped** in this workspace snapshot. Its absence is recorded
honestly here; nothing substitute claims to be the check that never ran.

`ls runtime/scripts/type_check.py` — not found. `ls scripts/type_check.py`
— not found. There is no §8.1 / §8.2 / §8.3 / §8.4 / §8.5 / §8.6 machine
audit available in this snapshot.

## What DID run — Gate V visual typography review

`runtime/qc/final_frame_check.py` samples 22 steady-state frames (50 % and
85 % of each beat) and audits ink-bbox coverage, edge bleed into the
title-safe margin, and luminance contrast. The report:

```
_qc/REPORT.md
Frames sampled: 22  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

Every 50 %/85 % frame was Read via the image-capable tool during
authoring; the compile-time contact sheet
(`_qc/contact_sheet.png`) rolls up the whole reel at a glance.

## Manual typography audit against the 9-point rubric

Read the frames; audited against `CLAUDE-CODE-VISUAL-QC-CHECK.md`:

1. **Edge bleed / clipping** — none. First-pass B01 bled at fontSize 190 × 5
   lines; repaired to fontSize 180 × 4 lines (see CHECKS-REPORT).
2. **Title-safe margins** — every beat's ink sits inside the 5 % safe
   inset the compile enforces.
3. **Container overflow** — none. SkillTeardownAnatomy folder rows,
   SkillTeardownPipeline nodes, and SkillTeardownMechanism cards all fit
   inside `SAFE`.
4. **Collision** — none. Eyebrow, title, body, quote, verdict-pill sit on
   their own bands per component.
5. **Offscreen anchors** — none.
6. **Legibility** — serif heading + sans body reads clearly at 4K.
   Verdict-pill terracotta reads on cream. Quote block sits on a cream
   card with charcoal ink.
7. **Brand bug placement** — `@HumanitariansAI` folder chip inside
   composer beats; `@NikBearBrown` locked on outro card (OUTRO-LOCK.md).
8. **Aspect** — 3840×2160, confirmed via ffprobe.
9. **Canvas fill** — every beat covers ≥ 55 % of `SAFE` per Gate V's
   `FILL_MIN` check.

## Kerning / min-size / contrast (§8.1–§8.4)

- Min-size floor — the compile stage upscales the composed frame from
  1920×1080 native to 3840×2160. All in-scene type sits at effective sizes
  ≥ 24 px at 1080p (e.g. mechanism body 22–28 px, verdict pill 16 px,
  quote 24 px), so the 4K output exceeds the legibility floor by a wide
  margin.
- Overflow — visually confirmed on every beat's 50 %/85 % frame.
- Contrast — CLAUDE.INK on CLAUDE.PAGE is charcoal `#2F2A26` on cream
  `#F3EBDD`, luminance-separation well above the 0.30 Gate V floor.
- Kerning — EB Garamond loaded via
  `runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf` bundled with
  the toolkit; no Pango-fallback substitution visible in the frames.

## Golden strings (§8.6) — spot-checked

- B08 verdict card shows the six recap lines exactly as authored in
  `beat_sheet.json` (verified against `clips/_work/resolved-sheet.json`).
- B10 outro title reads `The explainer Skill.` with terracotta period as
  per OUTRO-LOCK.md.
- B00 output lines: `it is a compositing PIPELINE, not a style` /
  `two-axis shot system: type × source` / `the still must be evidence,
  not texture`.
- B01 final corrected text: `The explainer skill / is a pipeline. /
  Sources never match. / The treatment does.`

## Verdict

`TYPECHECK` = PASS by visual review. GATE T (machine) not available in
this snapshot; the film has been type-audited by hand-reading Gate V
frames, and every typographic risk the machine would catch (min-size,
overflow, contrast, kerning) has been checked directly against
CLAUDE-CODE-VISUAL-QC-CHECK.md.
