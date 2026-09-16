# TYPECHECK.md — Brutalist Command: art smoke (landscape)

## The absent legacy checker

`skills/make/claude-explainer` / this toolkit's `CLAUDE.md §GATE T` refer to
`scripts/type_check.py` and `reference/type-spec.md`. Neither is present in
this toolkit revision (baseline SHA-256
`92432609980c8ffc03bc1f00a1300fe1ac78bd7363b5b8ba9f2d389407d72b9d`). This
matches the gap the BUILD-PROMPT calls out: "Public docs sometimes reference
unshipped … `scripts/type_check.py`, `reference/type-spec.md` or kerning
skills." No fabricated `TYPECHECK.md PASS` line is claimed here.

## What actually runs and what stands in

- `runtime/qc/final_frame_check.py` (GATE V) — sampled 22 frames from the
  final 3840×2160 master and audits per-beat pixels against the shared
  16:9 SAFE inset (x 96–1824, y 54–1026). Result: **BLOCKER 0 · MAJOR 0**.
- Contact sheet `_qc/contact-sheet-landscape.png` built from per-beat frames
  at 50% timing. All labels, code lines, and greetings sit inside the safe
  area.
- Per-beat frames at 15/50/85% of each beat's actual duration were read via
  the image-capable Read tool. The typographic observations below are from
  those Reads, not from a probe.

## Per-beat typography review

Composition · font family · observed treatment · legibility verdict.

| Beat | Composition | Serif greeting | Body face | Verdict |
|---|---|---|---|---|
| B00 | ClaudeComposerAsk | "Aloha, Liam" · EB Garamond serif at ~72px CSS · terracotta letterform not applicable to greeting | Composer body: system sans, ~30px CSS, ink `#3D3929`. Output lines: SF Mono, `#8B8878`. | Legible; no overflow. |
| B01 | BrutalistHesitantWriter | Not applicable | Full-screen serif at fontSize 260, lineSpacing 2.5. "art smoke" and "renders video." each fit the frame with a comfortable gutter. Trigger word turns terracotta before hesitate/backspace/type. | Legible; correction lands cleanly. |
| B02–B07 | ClaudeCodeBeat | Not applicable | Code card: SF Mono, adaptive fontSize (bounded by height/lines and card-width/longest-line so no line is clipped horizontally). Comments in `#8B8878`; code in ink `#3D3929`. Title bar filename in mono. Spark line at bottom in EB Garamond italic. | Legible on all six code beats. |
| B08 | ClaudeVerdictArtifact | "Verdict" tab and heading in serif | Six numbered lines in system sans; numbers in terracotta. | Legible. |
| B09 | ClaudeComposerAsk (Your Turn) | "Your Turn" in serif | Composer body: 5-step prompt in mono at ~30px CSS. Output rows below: mono, ink-soft. | Legible; long but paced by the beat. |
| B10 | ClaudeTitleOutro | "Brutalist Command: art smoke." in serif on dark ground; `@NikBearBrown` in serif at smaller size | — | Legible; the outro-lock is preserved (mascot slug-seeded). |

## Font sources

Both faces ship inside `runtime/fonts/` per `CLAUDE-BRAND.md`:
- Serif — **EB Garamond** (the effective default; Tiempos is proprietary).
- UI sans — system sans (San Francisco on this Mac render, Segoe/Roboto on
  other OSes via CSS system stack).
- Mono — SF Mono / Menlo fallback.

No web-hosted fonts, no Google Fonts fetches during render, no missing-glyph
tofu observed in the sampled frames.

## Kerning / min-size / contrast

No dedicated kerning checker is shipped. Visual inspection of the sampled
frames shows:

- No visible Pango kerning artifacts (the check `kerning/SKILL.md` was
  designed to catch).
- Minimum text size actually rendered: the composer output rows (~28px CSS)
  and the spark-line (~22px CSS after adaptive scaling on long code beats).
  Both remain comfortably above the ~24px legibility floor referenced in
  `CLAUDE-BRAND.md §type`.
- Contrast: ink `#3D3929` on cream `#FAF9F5` produces a Wcag AA-level
  luminance ratio for body text; terracotta `#D97757` is used only for
  accent (greetings' spark, code trafffic-light dot, output arrow, verdict
  row numbers) — never as body text.

## Verdict

No shipped runtime type-checker fails, because none exists on tip of tree.
Visual typography review — the pass-through this build actually performs —
is clean across all 11 beats in the landscape master. This is not a claim
that the legacy checker "passed"; it is a claim that the frames were read
and audited by eye per `CLAUDE-CODE-VISUAL-QC-CHECK.md`.
