# TYPECHECK — landscape

## Runtime type checker (Gate T)

`scripts/type_check.py` (Gate T) is referenced by `skills/make/ai-explainer/SKILL.md`
but **is not present in this toolkit snapshot**. Not patched around: no fabricated pass.

```
$ ls runtime/qc/type_check.py 2>&1
ls: runtime/qc/type_check.py: No such file or directory
```

## Visual typography review (substitute for Gate T)

Thirteen stills extracted from the finished 4K landscape master and read individually.
Typography confirmed across all beats:

- **Serif is EB Garamond** — greetings, segment titles, card headings, poster titles.
- **UI sans and mono** on composer chrome and code blocks — no mixed families, no
  substitution glitches.
- **Terracotta is the ONE accent** — send button (B00/B11), hesitation triggers (B01),
  numbered bullets in verdict (B10), outro title period (B12).
- **Titles and headings are Title Case** — never all-caps, never sentence case.

## §8 checks

- **§8.1 min-size** — body copy on mechanism beats renders at `height * 0.022` ≈ 24px
  landscape. All headings and titles well above the legibility floor.
- **§8.2 overflow** — Gate-V edge-bleed check clean on all 26 frames; no ink crossed
  the title-safe inset on any sampled frame.
- **§8.3 contrast** — ink `#3D3929` on cream `#FAF9F5` clears WCAG 4.5:1 comfortably.
  Gate-V `low-contrast` heuristic reported no defects.
- **§8.4 kerning sanity** — all fonts bundled as TTF in `runtime/fonts`; no external
  face requests; no tofu characters observed in any still.
- **§8.5 no-wordy-card** — verdict (B10, 4 lines, ~8 words each) is within the verdict
  pattern's design intent.
- **§8.6 golden strings** — all Mechanism and Anatomy quote cards carry verbatim text
  from `skills/make/godot-gamedev/SKILL.md`; no invented strings.

## Conclusion

Gate-T not present. Visual typography confirmed clean via frame-level review of thirteen
stills. No BLOCKER or MAJOR typography defects. Human review pending.
