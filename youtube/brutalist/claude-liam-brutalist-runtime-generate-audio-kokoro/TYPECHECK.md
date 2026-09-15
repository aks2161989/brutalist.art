# TYPECHECK — landscape 3840×2160

The public docs reference a `runtime/scripts/type_check.py` and
`reference/type-spec.md`; neither ships in the isolated toolkit copy that
built this reel. This is a visual typography inspection standing in for the
absent typography linter, plus the runtime checks that DO ship (Gate V,
`final_frame_check.py`).

## Method

1. `_qc/contact_sheet.png` — 12-beat contact sheet emitted by `final_frame_check.py`. Sampled at 15 %, 50 %, 85 % of every beat plus first and last frame — 24 frames total.
2. Read each frame with the image-capable Read tool. Inspected: family, weight, hierarchy (title vs body vs spark), leading, tracking, edge safety, alignment.
3. Cross-checked against `CLAUDE-BRAND.md` and the shipped scene components' fixed font stacks.

## Type stacks in this reel

| Component | Family (title / body / mono) | Purpose |
| --- | --- | --- |
| ClaudeComposerAsk (B00, B10) | Serif greeting · sans meta · mono command/output | Cold-open / handoff |
| BrutalistHesitantWriter (B01) | Serif large — `kokoro / is paid / and remote.` | BLUF correction |
| SkillTeardownPipeline (B02) | Sans eyebrow · serif title · sans phase labels · sans spark | Framework |
| ClaudeCodeBeat (B03–B08) | Sans title · monospace code body · sans spark | Mechanism cards |
| ClaudeVerdictArtifact (B09) | Serif heading · serif lines | Verdict |
| ClaudeTitleOutro (B11) | Serif title · sans handle | Outro |

All families are declared in the shipped scene TSX files; nothing was overridden per-beat.

## Findings

- **BLUF (B01)**: after two iterations (see CHECKS-REPORT.md) the final layout is 3 short serif lines at `fontSize: 260, lineSpacing: 1.2`. Cap height and descenders fit inside the 90 % safe area at both 50 % and 85 % of the beat. Correction typography (terracotta strikethrough during backspace, then black inserted phrase) is legible.
- **Code cards (B03–B08)**: the adaptive font clamp (see PROMPTS.md) chose fontSize ≈ 32–38 pt for the 20+ line stanzas and ≈ 44 pt for the shorter CLI-surface card. No line clipping; no horizontal overflow. Monospace column alignment preserved.
- **Verdict (B09)**: 6-line serif stanza. Line lengths ≤ 90 chars; leading is generous enough that lines don't collide.
- **Outro (B11)**: title is single-line at the shipped size; `@NikBearBrown` chip sits above the mascot with clear separation.
- **Cold-open composer (B00) + Your Turn composer (B10)**: 4-line commands with 3 output bullets each fit inside the composer card without overflow. `folderLabel` shows `@HumanitariansAI`.

## What the absent `type_check.py` would have caught

- Hard font-loading regressions (Remotion falls back silently to system fonts on missing @font-face).
- Absolute kerning-pair blacklist compliance.
- Numeric tabular figure lookup consistency.

None of these were detectable from the rendered frames alone. Recorded as an honest gap; no fabricated pass.

## Conclusion

Visual typography is consistent, hierarchically clear, edge-safe on all 24 sampled frames. No `type_check.py` pass claim is made — that checker does not exist in this toolkit copy. Gate V passes independently.
