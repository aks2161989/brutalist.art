# SHOTLIST.md — The your-turn Skill (ep 21)

Fourteen beats, one register (Teardown), one voice (Liam / Kokoro `am_onyx`).
Landscape 16:9 native. `shot.show` records what appears before the narration
comments on it — SHOW-DON'T-TELL LAW.

## Beats

| BID | Act | Pattern | What appears |
|---|---|---|---|
| B00 | ASK | ClaudeComposerAsk | Composer types the ask, three RESULT lines land answered |
| B01 | BLUF | BrutalistHesitantWriter | "your-turn is a whole-reel skill." → correction to "closing-block" (0.8s lead) |
| B02 | FRAMEWORK | SkillTeardownAnatomy | Folder tree: SKILL.md + scripts/apply_your_turn.py; callout "Doctrine reads. Script rewrites." |
| B03 | FRAMEWORK | SkillTeardownPipeline | Input `body ends` → three phases VERDICT · YOUR TURN · OUTRO → output `reel ends` |
| B04 | MECHANISM 1 | SkillTeardownMechanism | Handoff branches — from Bear vs from Liam; 0.5s lead pause; verbatim SKILL quote |
| B05 | MECHANISM 2 | SkillTeardownMechanism | drafts.json human gate — one entry per slug, prompt + optional recap |
| B06 | MECHANISM 3 | SkillTeardownMechanism | Verdict card fixes: 84% width + stripLeadNum defensively |
| B07 | MECHANISM 4 | SkillTeardownMechanism | Liam reads prompt in full; `command == narration_text` |
| B08 | MECHANISM 5 | SkillTeardownMechanism | Outro re-reads title; `narration_text = metadata.title` |
| B09 | WORKED EXAMPLE | SkillTeardownMechanism | Actual dry-run report from `demo/` — changed=1, errors=0 |
| B10 | FALSIFIABILITY | SkillTeardownMechanism | What your-turn does NOT do — body edits, publish, human re-render |
| B11 | VERDICT | ClaudeVerdictArtifact | Six-line recap "The your-turn split." |
| B12 | YOUR TURN | ClaudeComposerAsk | greeting `Your turn.`, paste-ready planning prompt Liam reads |
| B13 | OUTRO | ClaudeTitleOutro | "The your-turn Skill." + `@NikBearBrown` + slug-seeded mascot |

## Framing rules honored

- **COLD OPEN LAW** — B00 is `ClaudeComposerAsk` with a RESULT block; narration
  introduces Liam in for Bear in its first breath.
- **EXECUTIVE-SUMMARY LAW** — B01 is `BrutalistHesitantWriter`, correcting the
  reel's actual misconception, ≥9s (10.20s measured).
- **ILLUSTRATE LAW** — inner beats never re-use the Claude composer as
  wallpaper; the Anatomy tree, the Pipeline diagram, the Mechanism cards each
  illustrate a distinct move.
- **HANDOFF LAW** — B12 is `ClaudeComposerAsk` with greeting `Your turn.` and
  a real, paste-ready planning prompt Liam reads aloud.
- **OUTRO LAW / OUTRO-LOCK** — B13 is `ClaudeTitleOutro` with the reel's title
  restated (terracotta period), hardcoded `@NikBearBrown` handle, slug-seeded
  mascot; no subline per lock.
- **SPARK-LINE LAW** — every inner mechanism card carries a ≤4-word spark
  line at the top.

## Aspect

- Landscape: this shot list. Native 16:9 at compile — 3840×2160.
- Portrait companion (see `vertical/`) uses the parallel 916 variants
  (`ClaudeComposerAsk916`, `BrutalistHesitantWriter916`, `SkillTeardownAnatomy916`,
  `SkillTeardownMechanism916`, `ClaudeVerdictArtifact916`, `ClaudeTitleOutro916`)
  registered in the reel-local `scene-source/runtime/remotion/src/Root.tsx`
  overlay. B03's `SkillTeardownPipeline` is swapped to
  `SkillTeardownMechanism916` in portrait per feedback memo
  `skillteardown-pipeline-portrait` — the horizontal phase strip bleeds past
  the portrait safe area.
