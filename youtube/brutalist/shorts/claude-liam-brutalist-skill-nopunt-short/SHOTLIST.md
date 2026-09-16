# SHOTLIST.md — The nopunt Skill (Short)

All shots are native-portrait Remotion renders reused unchanged from the
parent's `vertical/media/`. No captured footage; no crops; no re-renders in
this derivative. Native resolution 2160×3840. Final container 168.208 s.

| # | Beat | Act | Component | Duration | Motion |
|---|------|-----|-----------|----------|--------|
| 1 | B00 | ASK | `ClaudeComposerAsk916` | 14.58 s | type-on |
| 2 | B01 | BLUF | `BrutalistHesitantWriter916` | 20.38 s | type-on (hesitant writer: `linter` → `catalog`) |
| 3 | B04 | MECHANISM · ACT 1 | `SkillTeardownMechanism916` | 27.96 s | reveal |
| 4 | B05 | MECHANISM · ACT 2 | `SkillTeardownMechanism916` | 36.46 s | reveal |
| 5 | B06 | MECHANISM · ACT 3 | `SkillTeardownMechanism916` | 32.13 s | reveal |
| 6 | B07 | MECHANISM · ACT 4 | `SkillTeardownMechanism916` | 33.21 s | reveal |
| 7 | B11 | OUTRO | `ClaudeTitleOutro916` | 3.50 s | hold (fade-in from black) |

## Palette / brand
- Cream `#FAF9F5`, ink `#3D3929`, terracotta `#D97757` (Claude palette).
- Serif: EB Garamond (headings, `ClaudeTitleOutro916`, hesitant writer body).
- Native portrait; no center-cut required (source was already 9:16).

## Outro (per OUTRO-LOCK)
- Title: "The nopunt Skill" (terracotta full stop).
- Hardcoded handle `@NikBearBrown`.
- Slug-seeded mascot animation (`slug: claude-liam-brutalist-skill-nopunt`).
- Verified visible at t ≈ 165 s (`_qc/frames-beat/B11_50.jpg`).

## Notes on the B07 → B11 join
`ClaudeTitleOutro916` begins with a very short black fade-in (single frame
present in the parent B11 source as well — see `/tmp` first-frame probe
during QC). Content is fully visible by t ≈ 164.75 s, well before Liam's
spoken sign-off begins. Not a defect — inherent to the parent outro
animation, preserved through reuse.

## Files
- Native portrait beat renders: `media/B00.mp4` … `media/B11.mp4` (7 files).
- Per-beat mp3 narration: `mp3/beat-B00.mp3` … `mp3/beat-B11.mp3` (7 files).
- Final Short mp4: `exports/short/claude-liam-brutalist-skill-nopunt-short.mp4`.
