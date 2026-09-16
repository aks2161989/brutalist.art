# TYPECHECK — The nbb Skill — Short

## Actual runtime typography review

Every kept beat is a Remotion `*916` composition rendered natively at 2160×3840
by the vertical parent and copied unchanged into this Short's `media/`. No
re-layout was necessary. Portrait-safe-area coverage and legibility were
verified by opening the beat-relative 15%/50%/85% PNGs with the image-capable
Read tool (SHA-256s in `VISUAL-REVIEW.json`).

- **B00 — ClaudeComposerAsk916 (16.29 s)** — Serif title `The nbb Skill`
  sits inside portrait safe area under eyebrow `BRUTALIST · SKILL TEARDOWN`.
  Greeting `Hola, Liam` in italic serif. Composer card holds the three-line
  ask; the three answer lines fit below without overflow. Folder chip
  `@HumanitariansAI` legible in the ink footer band. No clipping.
- **B01 — BrutalistHesitantWriter916 (19.38 s)** — Five lines of serif
  (fontSize 130, lineSpacing 2.5). Portrait-aware scale patch active; all five
  lines occupy roughly the middle 55% of the safe area with generous margins.
  Single-token trigger `rewrites` → `scaffolds` fires cleanly on the second
  line; caret is visible at end of state.
- **B03 — SkillTeardownPipeline916 (34.75 s)** — Vertical spine of INPUT →
  five phase cards (SCAFFOLD lit terracotta, then REWRITE, LLM EXERCISE, OUTRO,
  VERIFY) → OUTPUT with sub-labels and a footerNote below OUTPUT. Title
  `Five steps. One derived cut.` sits above the graph. Every label is legible;
  the footer sparkline `Scaffold first. Rewrite second. Ship last.` sits at
  the bottom safe margin.
- **B09 — ClaudeVerdictArtifact916 (34.25 s)** — Artifact card fills roughly
  the middle of the portrait frame with six numbered verdict lines. Numbering
  bullets in terracotta; body in ink. All six lines visible at p50 and p85
  (frames are byte-identical after the reveals complete — expected static state).
- **B11 — ClaudeTitleOutro916 (3.54 s)** — Serif `The nbb Skill.` with a
  terracotta period; handle `@NikBearBrown` centered below. Cream ground with
  slate rules top and bottom. Native portrait framing; nothing bleeds past
  safe margins.

## No burned-in captions

The compiler reports `drawtext: no — PIL overlays` in the compile log. No SRT,
VTT, karaoke, or transcript slide was added. Serif text on B01 and the
verdict card on B09 are compositional visuals, not captions.

## Portrait dimension proof

```
$ ffprobe -v error -show_entries stream=width,height -of csv=p=0 \
    exports/short/claude-liam-brutalist-skill-nbb-short.mp4
2160,3840,,,   (h264 video)
```

Native portrait 4K, no upscale, no crop.

## Legacy type checker

There is no `scripts/type_check.py` on disk in the isolated toolkit. This
report is the actual visual typography review that the legacy checker would
have supported; no fabricated pass is claimed.
