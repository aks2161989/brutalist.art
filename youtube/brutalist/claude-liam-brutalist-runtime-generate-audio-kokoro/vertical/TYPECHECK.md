# TYPECHECK — vertical 2160×3840

`runtime/scripts/type_check.py` and `reference/type-spec.md` are not shipped in
this toolkit copy. This is a visual typography inspection standing in for the
absent linter, plus the runtime checks that DO ship (Gate V,
`final_frame_check.py`).

## Method

1. `vertical/_qc/contact_sheet.png` — portrait contact sheet (24 frames, first / 15 % / 50 % / 85 % of every beat plus final frame).
2. Each frame opened with the image-capable Read tool. Inspected: family, weight, hierarchy, leading, tracking, edge safety, alignment on portrait 1080×1920 comp.
3. Cross-checked against `CLAUDE-BRAND.md` and each 916 scene's fixed font stack.

## Type stacks in this vertical

| Component | Family | Purpose |
| --- | ------ | ------- |
| ClaudeComposerAsk916 (B00, B10) | Serif greeting · sans meta · mono command/output | Cold-open / handoff |
| BrutalistHesitantWriter916 (B01) | Serif large — `kokoro / is / paid and / remote.` → corrected | BLUF |
| SkillTeardownMechanism916 (B02) | Sans eyebrow · serif heading · sans body · sans quote · sans verdict | Framework |
| ClaudeCodeBeat916 (B03–B08) | Sans title · monospace body · sans spark | Mechanism cards |
| ClaudeVerdictArtifact916 (B09) | Serif heading · serif lines | Verdict |
| ClaudeTitleOutro916 (B11) | Serif title · sans handle | Outro |

## Findings

- **BLUF (B01)**: after three iterations the final layout is 4 short serif lines at `fontSize: 220, lineSpacing: 1.9`. Ink fills ≥ 55 % of the portrait safe area. Widest line (`paid and`, `free and`) is ~700 px inside the 972 px inner safe width — no edge-bleed.
- **Code cards (B03–B08)**: the adaptive font clamp on `ClaudeCodeBeat.tsx` chose a smaller fontSize than landscape (portrait card is narrower → the width axis dominates). Every 20+ line stanza fits; no clipping. Monospace column alignment preserved.
- **Composer cards (B00, B10)**: after topic + segment shortening, the eyebrow / heading / command / output all fit inside the portrait card without overflow. `folderLabel` reads `@HumanitariansAI`.
- **Framework mechanism (B02)**: heading + body + quote + verdict + spark all inside the portrait safe area; the `SkillTeardownPipeline` horizontal strip was intentionally swapped for `SkillTeardownMechanism916` per prior portrait feedback.
- **Verdict (B09)**: 6-line serif stanza on portrait — lines wrap only where sensible ("input — ...", "engine — ...", etc.).
- **Outro (B11)**: title `Brutalist Utility: generate_audio_kokoro.py.` wraps across three lines because we added `overflowWrap: 'anywhere'` + `wordBreak: 'break-word'` to `ClaudeTitleOutro916.tsx`. Handle `@NikBearBrown` (OUTRO-LOCK) sits beneath.

## What the absent `type_check.py` would have caught (same as landscape)

- Silent @font-face fallbacks.
- Absolute kerning-pair blacklist compliance.
- Tabular figure consistency.

None of these were detectable from frames alone. Honest gap; no fabricated pass.

## Conclusion

Portrait typography is legible, hierarchical, edge-safe on all 24 sampled frames. No `type_check.py` pass claim. Gate V passes independently.
