# TYPECHECK — landscape (16:9)

## Absent legacy checker

The Claude explainer SKILL.md references `scripts/type_check.py`,
`reference/type-spec.md`, and a standalone `kerning` skill for GATE T's
automated typography pass. None of those exist in this isolated toolkit at
revision `ba2d0e0f...`. The rule stands: repair the episode, not the check.
Nothing was disabled or bypassed. GATE T's automated pass is not available;
the fields it would have populated are marked below as "manual" checks
performed by reading actual rendered PNG frames.

## Manual visual typography review (frame-by-frame)

Frames were extracted from the finished 3840x2160 master and inspected
individually via the image-capable Read tool. Beats sampled at ≥15 %, 50 %
and 85 % of each beat's span, plus the first and final frames.

Beats reviewed:

| Beat | Fonts on screen | Verdict |
|---|---|---|
| B00 `ClaudeComposerAsk` | serif "Namaste, Liam"; UI sans in composer chrome + segment; mono for typed command | Clean; type-safe within the 5% inset; no kerning artifacts |
| B01 `BrutalistHesitantWriter` | EB Garamond serif, 280 px at design scale | Clean; the corrected trigger words render in ink after their brief terracotta pass |
| B02–B08 `ClaudeCodeBeat` | SF Mono (code card); serif title; serif spark line | Clean; all long lines fit horizontally inside the code card in landscape; no clipping observed at 50 % / 85 % sample points |
| B09 `ClaudeVerdictArtifact` | Serif heading; UI sans bullet list; terracotta numeral markers | Clean; the seven-line list fits within the artifact card with generous margin |
| B10 `ClaudeComposerAsk` (Your Turn) | Serif greeting "Your turn."; UI sans segment; mono for typed prompt | Clean; the long paste-ready prompt wraps inside the composer card without bleeding past safe |
| B11 `ClaudeTitleOutro` | Serif poster title; serif handle; slug-seeded mascot | Clean; the title restate reads "Brutalist Command: art scenes." and the hardcoded `@NikBearBrown` handle sits below it |

## §8 rubric (checked visually against 24 sampled frames)

- §8.1 min size — all rendered type comfortably above the 24 px legibility
  floor at 4K.
- §8.2 overflow — no text container overflows a card or crosses the safe
  inset. Verified by Read-ing frames.
- §8.3 contrast — warm ink `#3D3929` on cream `#FAF9F5` and the terracotta
  accent `#D97757` all pass by eye; no low-contrast pairing on screen.
- §8.4 kerning sanity — no Pango fallback artifacts observed.
- §8.5 no-wordy-card — no card that just recites a paragraph; the verdict
  card is a legitimate seven-line enumerated summary.
- §8.6 golden strings — the outro title matches the beat sheet's `title`
  exactly ("Brutalist Command: art scenes."); the composer `folderLabel`
  reads @HumanitariansAI (per playlist adaptation); the outro handle is
  @NikBearBrown (per OUTRO-LOCK.md, unchanged).

Manual visual review conclusion: **no typography defects found on the
landscape cut**. The absence of the legacy checker is a toolkit gap,
recorded honestly here — not claimed as a green pass.
