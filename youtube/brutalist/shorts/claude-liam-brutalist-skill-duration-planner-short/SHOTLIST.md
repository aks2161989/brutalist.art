# SHOTLIST — The duration-planner Skill · Short (9:16)

Whole-beat cut of the parent portrait companion `claude-liam-brutalist-skill-duration-planner/vertical/`. Native 2160×3840 output (composed at 1080×1920, compiled to 4K portrait). 7 of the parent's 11 beats retained; every retained beat's `media/<bid>.mp4` was copied byte-identical from the parent — no re-render, no crop, no upscale, no re-encode of the source audio.

| Beat | Composition (9:16) | Type | Duration (s) | Source in this Short |
|---|---|---|---|---|
| B00 | `ClaudeComposerAsk916` | ASK | 14.583 | `media/B00.mp4` — parent-vertical reuse |
| B01 | `BrutalistHesitantWriter916` | BLUF | 15.000 | `media/B01.mp4` — parent-vertical reuse |
| B04 | `SkillTeardownMechanism916` | MECHANISM · ACT 1 | 21.708 | `media/B04.mp4` — parent-vertical reuse |
| B05 | `SkillTeardownMechanism916` | WORKED EXAMPLE | 22.542 | `media/B05.mp4` — parent-vertical reuse |
| B07 | `SkillTeardownMechanism916` | FALSIFIABILITY | 24.333 | `media/B07.mp4` — parent-vertical reuse |
| B08 | `ClaudeVerdictArtifact916` | VERDICT | 18.583 | `media/B08.mp4` — parent-vertical reuse |
| B10 | `ClaudeTitleOutro916` | OUTRO | 3.958 | `media/B10.mp4` — parent-vertical reuse |

Total kept ≈ **120.71 s** (2 min 0.7 s). Compiled Short: container 120.708 s / video 120.667 s / audio 120.708 s — strictly under the 180 s Shorts cap with 59.29 s of headroom.

## Beats dropped from the parent

| Beat | Composition | Act | Parent runtime (s) | Cut reason |
|---|---|---|---|---|
| B02 | `SkillTeardownAnatomy916` | FRAMEWORK · SKILL ANATOMY | 18.79 | Skill folder tree belongs in the 16:9 long. |
| B03 | `SkillTeardownPipeline916` | FRAMEWORK · PIPELINE | 20.17 | Five-phase pipeline diagram is the mechanism proof B04/B05 already carry. |
| B06 | `SkillTeardownMechanism916` | MECHANISM · ACT 3 · HOLD_FLOOR | 25.88 | Implementation detail; recapped in one line in B08. |
| B09 | `ClaudeComposerAsk916` | YOUR TURN | 28.58 | Long-form CTA; the 16:9 long carries the paste-ready prompt. |

Total dropped ≈ **93.4 s**. Parent full runtime 214.1 s → Short 120.7 s.

## No re-render

Because the parent vertical is already native 9:16, `shorts.py` detected each
retained media file as native 2160×3840 and reused it unchanged (log lines
`[short] Bxx native portrait reused unchanged`). No `remotion_scenes.py` pass
was needed for the Short. The parent's OUTRO-LOCK/COLD-OPEN-LAW skin-lint
warnings are inherited unchanged as false positives (the `*916` variants ARE
the correct portrait compositions).

## Audio

Per-beat `mp3/beat-Bxx.mp3` files copied byte-identical from the parent for
every retained beat. No regeneration. Kokoro `am_onyx` throughout. No
subtitles, no burned-in captions, no compile-side overlay changes.

## Endcard

`--no-endcard` — the Short ends on B10 (the parent's OUTRO-LOCK outro).
