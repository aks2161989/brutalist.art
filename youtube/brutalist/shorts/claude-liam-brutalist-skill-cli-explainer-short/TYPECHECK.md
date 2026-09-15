# TYPECHECK — Short cut (9:16)

Run: 2026-09-11 · run_id `199fe630ee9744af96cd435a69ed82e4` (re-verified; media unchanged from prior run).

## What ran

The isolated toolkit does not ship `runtime/scripts/type_check.py` or the
`kerning` skill — the parent vertical's `TYPECHECK.md` documented the same
gap. The fallback used for the parent's vertical film applies here too:
a visual typography audit of the sampled portrait frames read with the
image-capable Read tool, against the spec points in ai-explainer §8 (min
size, overflow, contrast, kerning sanity, no-wordy-card, golden strings).

## Per-beat visual read

Sampled per beat at 15% / 50% / 85% (`_qc/beat_frames/`). Every frame was
opened during authoring. Findings:

| Beat | Scene | Min-size / overflow | Contrast / kerning | Wordy? | Golden strings |
|---|---|---|---|---|---|
| B00 | ClaudeComposerAsk916 | greeting "Namaste, Liam" fills top third; composer wraps 2 lines at portrait width; output lines mono-fixed inside safe column | ink #3D3929 on cream #FAF9F5 — high contrast; folder chip legible; terracotta send button | no — ask is one sentence, 3 result lines each ≤ 60 chars | "Namaste, Liam" · "What does typing \`cli\` at Claude actually do in this toolkit?" · "it resolves to skills/make/cli-explainer/SKILL.md" · "365 lines of markdown Claude reads before drafting" · "the file writes the reel — not a screen recorder" · "@HumanitariansAI" |
| B01 | BrutalistHesitantWriter916 (portrait-scale patched) | fontSize 175 with lineSpacing 1.14 gives 5–6 visible lines by 50%; widest word "commissions" fits inside 1944 px safe width | serif ink on cream; strike-through animated on "records" and "terminals" (terracotta) before replacement lands | no — 6 short lines | first frame "records" typed; 50% mid-correction shows "commissions your terminals\|"; 85% shows final "commissions your reels.\|" |
| B02 | SkillTeardownAnatomy916 | folder tree (4 rows) + callout (2 lines) + spark line — all fit inside safe column vertically with ample negative space | ink on cream; "SKILL.md" tag in terracotta as the accent; folder icons legible | no — 4 tree rows, 2 callout lines, one spark line | "SKILL · ANATOMY · WAS TERMINAL-SCREENCAST" · "A skill is a folder." · "skills/make/cli-explainer/" · "SKILL.md   365 lines · 3,262 words   THE INSTRUCTIONS" · "reference/" · "example-cli-beat_sheet.json   one worked reel" · "Claude reads the file. The file writes the reel." · "No compiled binary. No daemon. No service." · "The file is the instruction." |
| B03 | SkillTeardownPipeline916 (portrait 5-phase) | 5 phase boxes + TRIGGER + REEL nodes span the safe column horizontally with consistent 42 px arrow gaps; portrait spine already de-flowed from landscape 7-phase to prevent the parent's edge-bleed BLOCKER (see parent CHECKS-REPORT §"B03") | ink boxes on cream; BUILD LOOP accent box in terracotta | no — one label + one descriptor per node | "SKILL · PIPELINE" · "The required beat spine." · "TRIGGER" · "INTRO / cold open" · "PROBLEM / before the loop" · "BUILD LOOP / ask · code · output" · "REVISION / cycle 2" · "HANDOFF / summary · outro" · "REEL" · "Source: skills/make/cli-explainer/SKILL.md — 'the required beat spine'." · "Same spine, every reel." |
| B10 | ClaudeVerdictArtifact916 | 4 numbered artifact lines wrap inside the card; last line ends inside safe bottom; card header + body legible | ink on cream card; numbered markers in terracotta | no — 4 lines, each 15–25 words | "The cli-explainer Skill." · "What cli-explainer actually is" · "Instructions, not software — 365 lines of markdown Claude reads before drafting the reel; there is no compiled binary, no daemon, no service." · "The narrative spine is locked in every reel it produces (intro · problem · ask · code · output · revision · summary · handoff · outro); the skin is a --tool flag." · "A CLI reel without a check-and-change is incomplete in 16:9 — the doctrine names its own edge case (the shorts cut) in the same paragraph." · "It ships as a folder: SKILL.md plus reference/example-cli-beat_sheet.json — the file is the instruction, and Claude is the compiler." |
| B11 | ClaudeComposerAsk916 | greeting "Your turn." fills top third; the paste-ready prompt wraps 4 lines in the composer; runningText "paste this into Claude…" below | ink on cream; terracotta send button and running-text spark | no — one 40-word prompt | "Your turn." · "Use cli-explainer to build a Brutalist reel about the smallest command in my own workflow. Read skills/make/cli-explainer/SKILL.md first, then propose a beat sheet before you draft narration." · "paste this into Claude…" · "@HumanitariansAI" |
| B12 | ClaudeTitleOutro916 (handle prop override) | title "The cli-explainer Skill." serif on ink card, terracotta period; handle "@HumanitariansAI" beneath — both centered, both inside safe area; horizontal rules at top/bottom | cream text on ink #3D3929 background — inverse of body beats, matches OUTRO-LOCK contract | no — two lines only | "The cli-explainer Skill." · "@HumanitariansAI" |

## Rubric

- **§8.1 min-size**: PASS — every rendered string is at least the visual
  equivalent of 24 px on the 1080 design ref (mono result lines are the
  smallest at ~28 px; verdict body ~40 px; titles ≥120 px).
- **§8.2 overflow**: PASS — every text box is either the composer's fixed
  padded input, the verdict artifact card, the anatomy folder tree, or the
  pipeline node boxes — every one measured with `maxWidth`/wrap semantics
  per SAFE. No offscreen anchor observed.
- **§8.3 contrast**: PASS — ink on cream for body; cream on ink for outro;
  terracotta accent limited to one focal moment per beat (send button OR
  the strike-through OR the "SKILL.md" tag OR the numbered markers OR the
  outro period), never two.
- **§8.4 kerning sanity**: PASS — no Pango fallback observed; serif
  ligatures (e.g. "cli-explainer") render cleanly at portrait scale.
- **§8.5 no-wordy-card**: PASS — verdict card is the wordiest and each
  numbered line is ≤ 25 words.
- **§8.6 golden strings**: PASS — every claim the narration makes has a
  matching on-screen string (see table above).

## Gaps documented

- `runtime/scripts/type_check.py` not shipped in this isolated toolkit;
  fallback = the visual read audit recorded above.
- `runtime/remotion/src/illustrations/ILLUSTRATIONS.md` — present in the
  isolated toolkit; not needed for authored beats here.
- `kerning` skill — not present; visual read audit substituted per parent
  practice.

**Result: no FAIL.** Every §8 point either passes or has an explicit
documented fallback, consistent with the parent vertical's TYPECHECK.md.
