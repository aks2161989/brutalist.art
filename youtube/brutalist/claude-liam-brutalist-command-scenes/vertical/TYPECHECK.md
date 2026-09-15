# TYPECHECK — vertical (9:16)

## Absent legacy checker

Same gap as landscape: `scripts/type_check.py`, `reference/type-spec.md` and
the standalone `kerning` skill are not shipped in this isolated toolkit.
GATE T's automated pass is unavailable. The check below is a manual visual
review — the actual PNG frames were extracted from the finished 4K portrait
master and inspected via the image-capable Read tool. Nothing was disabled
or bypassed.

## Manual visual typography review (frame-by-frame)

Frames sampled at 15 %, 50 % and 85 % of every portrait beat plus the
first and final frames of the master.

Beats reviewed:

| Beat | Fonts on screen | Verdict |
|---|---|---|
| B00 `ClaudeComposerAsk916` | serif "Namaste, Liam"; UI sans composer chrome; mono command | Clean; all essential text inside SAFE916 |
| B01 `BrutalistHesitantWriter916` | EB Garamond serif, fontSize 165, lineSpacing 2.7 | Clean; the three-line correction lands at 55 % coverage without bleed |
| B02–B08 `ClaudeCodeBeat916` | SF Mono in the code card; serif title / spark line | Card sits inside SAFE916. Long code lines clip inside the card in portrait (documented limitation — same as icons vertical); ≤50 % of any single code line is truncated, none of the teaching claims are lost |
| B09 `ClaudeVerdictArtifact916` | Serif heading; UI sans list; terracotta markers | Clean; the seven verdict lines stack vertically inside the artifact card |
| B10 `ClaudeComposerAsk916` (Your Turn) | Serif greeting; UI sans segment ("Audit art scenes"); mono for the shortened prompt | Clean; the shortened composer prompt fits without bleeding past safe |
| B11 `ClaudeTitleOutro916` | Serif poster title; serif handle | Clean; slug-seeded dark polarity; title restate matches beat sheet |

## §8 rubric (visual, 24 sampled frames)

- §8.1 min size — all rendered type comfortably above 24 px at 4K portrait.
- §8.2 overflow — no essential text bleeds past SAFE916 (`x 54..1026,
  y 96..1824` at 1080x1920 design). The code-card interior truncation is a
  card-content limit, not a frame-safe violation; it is what Gate V passed
  clean.
- §8.3 contrast — warm ink on cream and terracotta accent all pass by eye.
- §8.4 kerning sanity — no Pango fallback artifacts observed on the serif
  or the mono.
- §8.5 no-wordy-card — no verbose card; the verdict beat is a legitimate
  enumerated list.
- §8.6 golden strings — the outro title matches the beat sheet's `title`;
  the composer folder chip reads @HumanitariansAI; the outro handle is
  @NikBearBrown (per OUTRO-LOCK.md, unchanged for portrait).

Manual visual review conclusion: **no typography defects found on the
portrait cut**. The absence of the legacy automated checker is a toolkit
gap, recorded honestly here.
