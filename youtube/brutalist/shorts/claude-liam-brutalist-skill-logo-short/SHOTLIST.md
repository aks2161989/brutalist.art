# SHOTLIST — The logo Skill — Short (9:16)

7 beats retained from the 12-beat vertical parent. Native 2160×3840. All beats
are the parent's existing Remotion renders, copied unchanged. Total measured
run: 155.375 s (strictly under the 3:00 Shorts cap).

| Beat | Pattern | Purpose | Dur (s) |
|------|---------|---------|---------|
| B00 | ClaudeComposerAsk916 | Cold open — Liam introduces the ask; three result lines preview the whole Short. | 15.25 |
| B01 | BrutalistHesitantWriter916 | BLUF — deletes "fixed" and writes "random" to correct the misconception `logo` invites. lead_silence_s: 0.8. | 18.17 |
| B04 | SkillTeardownMechanism916 | ACT 1 — the MP3 is the clock (`--tail` pads silence, `calculateMetadata` derives frames; trim can only bite silence). | 28.79 |
| B05 | SkillTeardownMechanism916 | ACT 2 — random once, then locked (`SystemRandom` → `shot.remotion.picked`; `--reroll` re-spins). | 27.33 |
| B08 | SkillTeardownMechanism916 | FALSIFIABILITY ACT 5 — no `logos/nik-bear-brown/` by design; @NikBearBrown uses `ClaudeTitleOutro` instead. | 33.50 |
| B09 | ClaudeVerdictArtifact916 | Six-line verdict card — locked lottery, MP3 clock, pool = quality bar, drawOn earned, aspect follows metadata, NBB opts out. | 29.00 |
| B11 | ClaudeTitleOutro916 | Title restate — "The logo Skill." · @NikBearBrown (per OUTRO-LOCK). Liam sign-off. | 3.33 |

## Beats dropped from the vertical parent

Dropped by `shorts.py --drop B02 B03 B06 B07 B10` (whole-beat cut, no rewrite):

| Beat | Pattern | Reason dropped |
|------|---------|----------------|
| B02 | SkillTeardownAnatomy916 | Folder-tree walkthrough belongs in the 16:9 long. |
| B03 | SkillTeardownPipeline916 | Six-step scaffolder flow is generic pipeline anatomy; the two design laws (B04/B05) and the verdict already carry the mental model. |
| B06 | SkillTeardownMechanism916 | ACT 3 (pool curation, medhavy 42→25→12 case study) — dropping avoids a dangling "Third decision" in the retained cut. |
| B07 | SkillTeardownMechanism916 | ACT 4 (drawOn earned, SVG parser) — same dangling-numbering hazard. |
| B10 | ClaudeComposerAsk916 | Your-Turn detailed dry-run assignment belongs in the long. |

## Native-portrait reuse

Every retained beat is the parent's rendered `media/<bid>.mp4`, verified
2160×3840 by `ffprobe` (aspect check `width*16 == height*9`) and copied
independently into `short/media/` by `shorts.py`. No re-render, no crop, no
regenerated audio. Kokoro `am_onyx` mp3s copied unchanged into `short/mp3/`.

## Reveal choreography

Every retained beat carries a `shot.show` block in `beat_sheet.json` for its
scene-driven reveals — composer type-on for B00, hesitant-writer type-on with
mid-word terracotta deletion for B01, per-row Spring staggers for B04/B05/B08,
line-by-line reveal for the verdict artifact B09, and a hold on the outro B11.
