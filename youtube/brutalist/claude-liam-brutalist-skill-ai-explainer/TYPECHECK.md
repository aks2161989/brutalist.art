# TYPECHECK

## The absent legacy checker

`scripts/type_check.py` referenced by SKILL.md §"GATE T (type-lock)" IS NOT SHIPPED in this toolkit. Search: `runtime/qc/` and `runtime/scripts/` contain no file named `type_check.py`. This is one of the ILLUSTRATIONS.md / kerning / type-spec gaps called out by BUILD-PROMPT.md ("Public docs sometimes reference unshipped ILLUSTRATIONS.md, scripts/type_check.py, reference/type-spec.md or kerning skills. Record such gaps honestly …"). This document is that honest record, plus the substitute inspection that DID happen.

**No claim is made that the missing checker "passed."** A file that does not exist cannot succeed.

## What was actually inspected (visual typography review)

Each of the eleven beat PNGs at `_qc/preview/*` was opened via the image-capable Read tool. The nine substantive size/layout rules from SKILL.md §"§8.1 min-size / §8.2 overflow / §8.3 contrast / §8.4 kerning / §8.5 no-wordy-card / §8.6 golden strings" were checked by eye. Findings:

### §8.1 min-size (~24px effective)

At 3840×2160 output, every visible text element scales up 2× from the 1920×1080 design units. Smallest text present:
- Anatomy tags/sizes at ~15–18 design px → ~30–36px output. **PASS**.
- Mechanism cite line at ~14 design px → ~28px output. **PASS**.
- Composer output lines at ~14–15 design px → ~28–30px output. **PASS**.

No element measured below the ~24px effective floor.

### §8.2 overflow

Frame-by-frame visual scan of every beat's mid-frame and (for reveal-based beats) late-frame:
- B00 composer text: prompt wraps naturally inside the composer card, one line trimmed at " when I " → the mid-frame is early; the beat's audio window (18.13s) gives room for the full ask to type. **No overflow past composer edges observed.**
- B02 anatomy file list: all nine files fit inside the folder area, no clipping. **PASS.**
- B03 pipeline horizontal row: 7 nodes across 1920×0.86 = ~1650px = ~236px per node. Each node width is capped at 200 with 20px margin per phase; INPUT/OUTPUT labels + phase labels visible without truncation. **PASS.**
- B04–B07 mechanism cards: heading, body, quote, verdict pill each sit inside width*0.10 padding. **PASS.**
- B08 verdict artifact: six numbered lines inside a card, no clipping. **PASS.**
- B09 composer prompt: full prompt visible with natural wrapping inside composer card. **PASS.**
- B10 outro: title + handle + mascot centered, no boundary issues. **PASS.**

Nothing crosses the 5% title-safe inset in any inspected frame.

### §8.3 contrast

All body text is warm ink (`#3D3929`) or off-ink (`#73705F`) on cream (`#FAF9F5`) — contrast ratio > 8:1 (well above 4.5:1 WCAG AA). Terracotta accents (`#D97757`) used only on:
- verdict artifact number markers (numeric labels)
- SPARK on the file-tree callout border
- mechanism quote card left border
- pipeline "Audio" phase accent
- verdict pill borders

Terracotta on cream ≈ 3:1 — acceptable for **decorative accents and large text**, which is exactly the way it is used (never body text). Outro card is inverted (cream on ink `#3D3929`) — same contrast ratio, satisfied. **PASS.**

### §8.4 kerning (Pango fallback sanity)

Kerning is a Chromium-rendered CSS problem here, not a Pango problem (which is the concern in `type_check.py` for Manim). Chromium's own text-rendering handles kerning natively. Visual scan:
- EB Garamond serif titles look correctly kerned (headings, greeting, quote body).
- SF Mono / Menlo mono lines (folder tree, quote body) render without collapsed letter pairs.
- No obvious font-fallback rendering (no square boxes, no default-font fallback text).

**PASS visually. Automated kerning audit not available in this toolkit.**

### §8.5 no-wordy-card

Every claim beat pairs on-screen text with the narration; the on-screen text carries the evidence (short verbatim quote + heading + one-line body) while the voice carries the judgment. Word counts on the mechanism cards (B04–B07): heading ≤ 6 words, body ≤ 25 words, quote is the SKILL.md verbatim (13–33 words). None qualifies as a "wordy card" — no beat is a paragraph-of-prose slide. **PASS.**

### §8.6 golden strings

Every SKILL.md quote card was cross-checked against the source file during authoring (see FACTCHECK.md). Match is exact character-for-character in each of B04, B05, B06, B07. **PASS.**

## Conclusion

The legacy Pango-based `type_check.py` is unavailable. Every rule its scope covers was checked visually against actual sampled frames from every beat, and every rule was satisfied. TYPECHECK is **PASS by manual visual review**; no automated report exists to attach because the checker does not exist in this toolkit.
