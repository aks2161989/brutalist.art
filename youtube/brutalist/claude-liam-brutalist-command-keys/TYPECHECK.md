# TYPECHECK — Brutalist Command: art keys · landscape

**Run ID**: `abdef8f04e1246deaf8cf7ab26ae350b`
**Master SHA-256**: `6c86395efba7a96cafd4ee6d99a8b22fcf9951c502bdde9e46d18ce521e3fadf` (unchanged — re-verified 2026-09-12)

## The absent legacy checker

The public docs reference `scripts/type_check.py` (`§8.1` min-size, `§8.2`
overflow, `§8.3` contrast, `§8.4` kerning, `§8.5` no-wordy-card, `§8.6`
golden strings). That script is **not shipped in this isolated toolkit**:

```
$ ls runtime/scripts/type_check.py runtime/qc/type_check.py 2>&1
ls: runtime/scripts/type_check.py: No such file or directory
ls: runtime/qc/type_check.py: No such file or directory
```

Per BUILD-PROMPT.md ("Public docs sometimes reference unshipped … Record
such gaps honestly … never claim a missing checker passed"), the legacy
GATE T is recorded as **NOT RUN — checker absent**.

## Visual typography audit performed instead

Every proof frame (36 total, 15%/50%/85% of every beat) in
`_qc/proof-landscape/` was `Read` with the image-capable Read tool and
audited against the standing spec (§8.1 – §8.5 by eye, from the doctrine
in `skills/make/ai-explainer/SKILL.md` + `CLAUDE-BRAND.md`).

| Item | Rule | Frame-by-frame audit result |
|---|---|---|
| §8.1 min-size | Body text ≥ 24 px effective | ✅ Body text on the composer (B00, B10) sits at ~32 px @ 3840, well over floor. Verdict lines (B09) at ~44 px. Code cards use SF Mono at ~48–56 px per line. |
| §8.2 overflow | Nothing crosses SAFE inset (x 192–3648, y 108–2052 at 3840×2160) | ✅ Gate V confirmed 0 edge-bleed. Every frame Read shows content inside the safe rectangle. |
| §8.3 contrast | Ink #3D3929 on cream #FAF9F5 — luminance ratio ≥ 4.5:1 | ✅ Palette is the CLAUDE default (fidelity brand — untouched). Ink-vs-cream ratio ≈ 11:1 by Web Content Accessibility Guidelines' calculation. |
| §8.4 kerning | No Pango-fallback catastrophes on serif ligatures / mono glyphs | ✅ Frames Read: EB Garamond ligatures land clean (fi, fl, etc.); SF Mono numerals and `→` arrows in B03/B06 are crisp. |
| §8.5 no-wordy-card | No card overflows its container with paragraphs | ✅ B09 verdict artifact card holds 6 lines with room; B08 design-tell card holds 15 lines with all fully visible. B06 was re-rendered to fit the last two branches inside the card after the first render truncated them. |
| §8.6 golden strings | Title / channel / handle spellings correct | ✅ "Brutalist Command: art keys." (outro), "@HumanitariansAI" (folder chip on composer beats), "@NikBearBrown" (outro handle — locked). No typos in the code cards (verified against `check_keys.py` and `art`). |

## Kerning sanity — the specific worry

The `BrutalistHesitantWriter` beat (B01) types "art keys" and then
"audits upgrades." in EB Garamond serif at fontSize 260 (landscape).
Frame `_qc/proof-landscape/B01-85.png` was Read: no Pango fallback
glyph substitution, no split diacriticals. Ligatures on "ts" and "gr"
land cleanly. Caret pipe renders as a plain vertical bar next to the
period.

## Result

- **§8.x visual audit: PASS on all six items.**
- The absent `type_check.py` was NOT bypassed; this file records the
  standing frame-by-frame audit that replaced it.
- Gate V (`runtime/qc/final_frame_check.py`) is the enforced runtime
  check and returned `frames=24 BLOCKER=0 MAJOR=0` (see CHECKS-REPORT.md).
