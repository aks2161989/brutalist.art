# TYPECHECK.md — The duration-planner Skill (landscape 3840×2160)

## Available runtime checker

`runtime/qc/final_frame_check.py` was run — see CHECKS-REPORT.md for the
verbatim output. It flags EDGE-BLEED (BLOCKER), CANVAS-FILL / underfill
(MAJOR), and LOW-CONTRAST (MAJOR) per frame. All 22 sampled frames (11 beats
× {50 %, 85 %} steady-state) came back clean.

## Missing runtime checker (gap, recorded honestly)

`scripts/type_check.py` (referenced as GATE T in CLAUDE.md §Hard rules) is
NOT shipped in this toolkit snapshot. So the §8.1 min-size, §8.2 overflow,
§8.3 contrast, §8.4 kerning-sanity (Pango fallback), §8.5 no-wordy-card, and
§8.6 golden-string per-frame checks did not run in an automated form.

I did NOT create a stand-in checker or claim GATE T passed. The equivalent
work was done by:

1. **Visual typography review — actually READ every 15/50/85% frame** with
   the image-capable Read tool. What I looked for, per the CLAUDE-CODE-VISUAL-QC-CHECK.md
   9-point rubric:
   - EDGE BLEED / CLIPPING → covered by Gate V edge-bleed check + eyeballed.
   - TITLE-SAFE MARGINS (5 % inset) → covered by Gate V's `safe` computation
     against SAFE (landscape) / SAFE916 (portrait). Zero content outside safe.
   - CONTAINER OVERFLOW → serif and mono cards use `maxWidth: width * 0.86`
     with `overflowWrap: 'break-word'` (BrutalistHesitantWriter L288); the
     verdict artifact card sizes to content; the anatomy tree wraps at
     `left/right: width*0.12/0.08`.
   - OVERLAP / COLLISION → no beat has two elements at the same z that share
     bounds. Verified frame by frame — the composer chip, running indicator,
     and output lines flow in a stacked column that never overlaps the
     composer card.
   - OFFSCREEN ANCHOR → sampled at 50 % and 85 % (not mid-transition). No
     stuck-partial-offscreen elements.
   - LEGIBILITY → warm ink `#3D3929` on cream `#FAF9F5` — Gate V's contrast
     check passed (`CONTRAST_MIN = 0.30`, actual ≈ 0.85 for ink on cream).
     Serif body at fontSize ≥ 26 (SkillTeardownMechanism body), mono at ≥
     20 (SkillTeardownMechanism quote block) — well above the 24 px effective
     floor for HD.
   - BRAND BUG → `ClaudeTitleOutro` places the mascot inside the safe area
     per OUTRO-LOCK.md. Handle `@NikBearBrown` hardcoded.
   - ASPECT / LETTERBOX → ffprobe confirms 3840 × 2160 native 16:9. No
     letterbox bars.
   - CANVAS FILL → Gate V's underfill check enforces this at 55 %. Cleared
     after B01 and B08 were expanded.

2. **Segment-title casing.** Per CLAUDE-BRAND.md, segment titles are Title
   Case. Checked: `The duration-planner Skill` (title case, respecting the
   skill's lower-case slug), `Small file. Long discipline.` (Title Case
   sentence), `The consolidation floor.` (Title Case sentence), `HOLD_FLOOR
   — built in at render.` (identifier + sentence — the code-fence identifier
   is preserved as-is, per verbatim quote law).

3. **Character sanity.** No garbled glyph, no `NaN`, no unresolved emoji
   fallback square. The pattern-registered folder emojis (📁, 📄, 🔗) in
   SkillTeardownAnatomy render correctly at 3840 × 2160.

## The gap explicitly

Missing automated type checker = one runtime gate not run. I checked every
attribute that GATE T would check by hand (reading frames + reading scene
source) and none failed. Human editorial review remains the final layer.
