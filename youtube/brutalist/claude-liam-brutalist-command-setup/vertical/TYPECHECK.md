# TYPECHECK.md — vertical

## Runtime typography gates that DO exist

- `runtime/qc/final_frame_check.py` — GATE V. On the 2160×3840 native portrait master: **0 BLOCKER / 0 MAJOR**. Reached this state after two iterations of the B01 hesitant-writer (3-line stack + fontSize/lineSpacing tuning to clear FILL_MIN 0.55) and a shorter B11 segment/prompt to keep the composer inside SAFE916.
- `runtime/scripts/build_safety.py` — invoked from `compile.py` and `shorts.py`; no violations.
- `runtime/scripts/compile.py` SKIN LINT — two informational rows (`B00` uses `ClaudeComposerAsk916`, `B12` uses `ClaudeTitleOutro916`). Both are correct for portrait; the lint is a landscape-first heuristic.

## Legacy checker referenced by older prose that does NOT exist here

Same as landscape: `scripts/type_check.py`, `skills/make/kerning/SKILL.md`, `reference/type-spec.md` are all absent from this toolkit revision. Reported honestly in the landscape TYPECHECK.md; not silently marked passed.

## What was actually inspected for portrait typography

Manual visual QC on `_qc/vertical/beats/` and `_qc/vertical/contact-sheet.jpg`:

- **B00 composer 916**: topic eyebrow `BRUTALIST · COMMAND: SETUP`, segment `./setup`, greeting `Konnichiwa, Liam`, composer body with the ask, running indicator, three output lines. All comfortably inside SAFE916 (54..1026 × 96..1824 CSS reference).
- **B01 hesitant writer 916**: three-line serif stack `setup / verifies / live.`, terracotta accent only on tokens about to be deleted, no edge-bleed, bbox coverage ≥ 55% at both 50% and 85% of beat.
- **B02–B09 code beats 916**: mono face with adaptive font. The narrowest-line beats (B02) size smaller than the URL-bearing B05 beat's compression; all fit within the card, no truncation. Comment lines carry a slightly softer ink than code lines (component contract preserved on portrait).
- **B10 verdict artifact 916**: heading + six numbered lines flow the portrait card; each line is legible without wrap gymnastics.
- **B11 Your Turn composer 916**: paste-ready command wraps naturally inside the composer body; three shorter output lines fit under the composer + folder chip + running indicator without pushing past SAFE916.b. The single-terracotta send button is the ONE accent.
- **B12 outro 916**: title "Brutalist Command: setup." with terracotta period, `@NikBearBrown` handle beneath (per OUTRO-LOCK), slug-seeded pixel-art mascot animating below the handle. PIXEL-ART LAW: translate/scale only, no rotation.

## Portrait FILL-THE-CANVAS observations

- The Gate V threshold (`FILL_MIN = 0.55`) drove the B01 iteration path. Passing state: `text` split to 3 lines, `fontSize` 218, `lineSpacing` 3.45 — matches the recipe in the shared portrait-BLUF playbook.
- Code beats' adaptive font naturally clears FILL_MIN because the card + monospace rows fill the safe area vertically once the width binding is applied.
- No content crosses SAFE916 on the master (final_frame_check.py's edge-bleed detector confirms).

## Fonts loaded

Same font set as landscape (EB Garamond serif, system sans, SF Mono / Menlo mono). Portrait scale factor for the hesitant writer now uses a 1080×1920 design reference (patched); every other component already scaled off a compositional reference, so no landscape-tuned font size collapses on portrait.

## Conclusion

Every runtime typography gate that exists in this toolkit passed clean on the vertical master. The absent legacy `type_check.py` was not silently claimed to pass; it was replaced with per-beat image inspection using the same 9-point rubric as the landscape build.
