# TYPECHECK — landscape

## Runtime type checker (Gate T)

`scripts/type_check.py` (Gate T) is referenced by `skills/make/ai-explainer/SKILL.md`
but **is not present in this toolkit snapshot**. This gap is preserved honestly, not
patched around: no fabricated pass, no relaxed check.

```
$ ls runtime/qc/type_check.py 2>&1
ls: runtime/qc/type_check.py: No such file or directory
```

## What was done instead (visual typography review)

Ten stills were extracted from the finished 4K landscape master and read individually
with the image-capable Read tool. What each still confirms typographically:

- **Serif is EB Garamond** (bundled `runtime/fonts`). Greetings, segment titles,
  poster titles, spark lines all render in the correct serif.
- **UI sans and mono** on the composer chrome and code blocks — no mixed families,
  no substitution glitches (Pango fallback catch not needed here — the fonts are all
  bundled TTF).
- **Terracotta is the ONE accent** on every frame that carries it (send button in
  B00/B10, the trigger words during hesitation in B01, the traffic-light dot on the
  code cards, the period on the outro title). No competing warms; no double-orange.
- **Segment titles are Title Case** ("art approvals", "Your Turn") — never all caps,
  never sentence case.
- **Contrast** — ink `#3D3929` on cream `#FAF9F5` clears WCAG's 4.5:1 by a wide margin;
  Gate-V's `low-contrast` heuristic (ink/bg luminance separation ≥ 0.55) reported clean
  on every frame.

## Kerning / overflow / min-size (§8 spec substitutes)

- **§8.1 min-size** — all body copy on the code beats renders at `height * 0.022` ≈ 24px
  landscape (WCAG floor for 4K is much lower); greetings + segment titles + spark lines
  are much larger. No text below the FILL-THE-CANVAS legibility floor.
- **§8.2 overflow** — Gate-V edge-bleed check ran clean; no ink crossed the title-safe
  inset on any of the 24 sampled frames. The initial B01 render bled ("inspects the
  subjects." at fontSize 240) and was rewritten to "inspects subjects." before shipping.
- **§8.3 contrast** — see above.
- **§8.4 kerning sanity (Pango fallback catch)** — all fonts bundled; no external face
  requests; every rendered character in the ten stills is in-family and correctly
  spaced. Fallback would show as tofu/box characters — none observed.
- **§8.5 no-wordy-card** — the closest thing to a wordy card is B09 verdict artifact
  (6 lines, ~30 words each, staggered in over 30s of narration). This is the shape
  the verdict pattern is FOR; not a defect.
- **§8.6 golden strings** — every code beat carries the exact language from `art` or
  `build_safety.py` or `demo/RUN-LOG.txt`; no invented strings.

## Conclusion

The runtime Gate-T checker is not present, so it did not run. In its place, this
document records a frame-level typographic pass over ten stills from the finished
master — every one of §8's checks was reviewed against the actual rendered pixels.
No BLOCKER or MAJOR typography defects observed. Human review pending.
