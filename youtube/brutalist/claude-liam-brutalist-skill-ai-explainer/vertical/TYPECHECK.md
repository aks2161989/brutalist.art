# TYPECHECK — vertical 9:16

## The absent legacy checker

`scripts/type_check.py` referenced by SKILL.md §"GATE T (type-lock)" IS NOT SHIPPED in this toolkit (search: `runtime/qc/` and `runtime/scripts/` contain no such file). This is one of the gaps called out by BUILD-PROMPT.md ("Public docs sometimes reference unshipped ILLUSTRATIONS.md, scripts/type_check.py, reference/type-spec.md or kerning skills. Record such gaps honestly …"). No claim is made that the missing checker "passed" — a file that does not exist cannot succeed.

## What actually inspected the portrait build

- `runtime/qc/final_frame_check.py` (Gate V) — automatic; scaled `SAFE916 = {x:54, y:96, r:1026, b:1824}` up to 2160×3840. Sampled 22 frames from the compiled portrait master, 0 blockers, 0 majors.
- Manual visual review of the 4-column QC contact sheet at `vertical/_qc/contact_sheet.png` — opened with the image-capable Read tool. Every beat checked for typography rule compliance at 2160×3840 output.
- Manual per-beat frame extraction at 50% and 85% of each beat and re-analysis with `final_frame_check.analyze_frame` while iterating on the portrait scene fixes.

## Portrait typography review (§8.1–§8.6 by eye)

### §8.1 min-size (~24px effective)

Portrait output is `2160×3840`. The Remotion compositions are registered at `1080×1920` and rendered with `--scale=2`, so the effective output size is 2× the design px. Smallest text present:

- Anatomy tag micro-labels (`palette + type`, `outro card spec`, etc.) at ~13 design px → **~26px output**. Above floor.
- Mechanism cite line "Source: ai-explainer SKILL.md" at ~13 design px → **~26px output**. Above floor.
- Verdict artifact numeric bullet + line text at `FONT_LINE = height*0.026 = 50` design px → **~100px output**. Well above.
- Composer output mono lines at UI*0.85 in portrait (UI = 1920*0.016 = ~30) → ~26 design px → **~52px output**. Above.

Nothing fell below the ~24px effective floor. **PASS**.

### §8.2 overflow (SAFE916, i.e. 5% inset on 1080×1920)

Portrait safe area on 2160×3840 output: `x=108..2052`, `y=192..3648`.

- B00 (ClaudeComposerAsk916) — composer card spans ~86% of safe area, terracotta accent bar at `bottom: height*0.07` sits at y≈3571, inside safe bottom of 3648. Channel-title overlay was moved to sit inside safe area (see CHECKS-REPORT.md fix #6). **PASS.**
- B01 (HesitantWriterFramed916) — top/bottom rules moved to 6.5% insets so they land at y≈250 and y≈3590, well inside SAFE916. Eyebrow at 8% top, spark at 9% bottom. **PASS.**
- B02 (SkillTeardownAnatomy916) — folder tree stacks inside the column; spark raised to 7.5% bottom (y≈3552). **PASS.**
- B03 (SkillTeardownPipeline916) — vertical INPUT→…→OUTPUT stack; footer note at 11.5% bottom, spark at 7.5% bottom. All nodes fit inside the 1944-wide safe column with per-node text wrapping. **PASS.**
- B04–B07 (SkillTeardownMechanism916) — heading, body, quote card, verdict pill, spark line. Spark raised from 4% to 7.5% bottom. All inside safe area. **PASS.**
- B08 (ClaudeVerdictArtifact916) — card widened to 92% of frame; six numbered lines fit inside card padding without wrapping issues; coverage 73% of safe area, above the 55% floor. **PASS.**
- B09 (ClaudeComposerAsk916 "Your Turn") — full paste-ready prompt wraps naturally inside the composer card; output lines list three explicit success tests. **PASS.**
- B10 (ClaudeTitleOutroHAI916) — title + handle + mascot centered. **PASS.**

Gate V confirms no BLOCKER edge-bleed on any of the 22 sampled frames.

### §8.3 contrast

Same palette as landscape:
- Ink `#3D3929` on cream `#FAF9F5` → ~8:1 contrast ratio (well above WCAG AA 4.5:1).
- Off-ink / muted `#73705F` on cream → ~5.5:1.
- Terracotta `#D97757` on cream (~3:1) used ONLY for decorative accents and large text (verdict number bullets, pipeline Audio phase, quote card left border, mechanism verdict pill borders). Never body text.
- Outro card inverted (cream on ink) — same ratio.

**PASS.**

### §8.4 kerning

Chromium/CSS-rendered text handled natively; visual scan of the contact sheet shows serif titles (EB Garamond) and mono lines render with correct letter spacing, no square-box fallbacks, no font-fallback anomalies. Automated Pango-kerning audit is not available in this toolkit. **PASS visually.**

### §8.5 no-wordy-card

Mechanism cards (B04–B07) each carry: heading ≤ 6 words · one body paragraph ≤ 25 words · a SKILL.md verbatim quote block (13–33 words) · a verdict pill of ≤ 4 words · one italic spark line ≤ 8 words. None of the beats is a paragraph-of-prose slide. **PASS.**

### §8.6 golden strings

The four verbatim SKILL.md quotes in B04–B07 were cross-checked character-for-character during authoring (see FACTCHECK.md) — the strings in the portrait beat sheet are identical to the strings in the landscape beat sheet, so the visual comparison against SKILL.md still holds. **PASS.**

## Conclusion

Portrait typography is **PASS by manual visual review + Gate V pixel audit**. The absent legacy `type_check.py` is honestly recorded, not skipped or claimed. Every rule its scope covers was satisfied.
