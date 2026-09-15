# SHOTLIST — Brutalist Utility: smithsonian_fetch.py
# run_id: 742a1549e73142e4b6d655986b0ae560  |  2026-09-14
# Classification: SHOW / HOLD / CARD per nopunt SKILL.md

| Beat | Scene | Classification | Show events |
|---|---|---|---|
| B00 | ClaudeComposerAsk | SHOW | Greeting types → command types → running indicator → output lines stagger |
| B01 | BrutalistHesitantWriter | SHOW | "downloader" struck/replaced; "manually" struck/replaced |
| B02 | SkillTeardownPipeline | SHOW | 6 nodes animate in: INDEX→LOOKUP→RESOLVE→DOWNLOAD→UPSCALE→SHELVE |
| B03 | ClaudeCodeBeat | SHOW | Search command + ranked candidate output with object type tags |
| B04 | SkillTeardownMechanism | SHOW | Scoring table: title(+4), token(+2), apparatus(+1.5), ephemera(-1); verbatim quote |
| B05 | ClaudeCodeBeat | SHOW | Content-detail JSON path; CC0 access gate highlighted |
| B06 | SkillTeardownMechanism | SHOW | Two paths: tpai found vs not found; WARN case; verdict pill |
| B07 | ClaudeCodeBeat | SHOW | Sidecar file: CC0, SI_ID, Title, Unit, Credit, Source URL, License |
| B08 | ClaudeCodeBeat | SHOW | --copy --beat command; pantry path output; next-step message |
| B09 | ClaudeVerdictArtifact | SHOW | Artifact card with gets-right / bites lines staggering |
| B10 | ClaudeComposerAsk | SHOW | "Your turn." greeting → prompt types → running → output |
| B11 | ClaudeTitleOutroHAI | SHOW | Title card: episode title + @HumanitariansAI + mascot |

## Teaching arc (nopunt checklist)

- [x] FRAMEWORK beat — B02: explicit 6-stage pipeline before examples
- [x] WORKED EXAMPLE — B03: text search worked through scoring framework on screen (B04)
- [x] FALSIFIABILITY / edge-case — B06 (Topaz not present), B08 (--copy missing --beat)
- [x] SCAFFOLDED viewer task — B10: prompt + explicit test (inspect .source.txt for CC0 + SI id)
- [x] Four bookends — B00 (cold open) + B09 (verdict) + B10 (Your Turn) + B11 (outro) ✓
- [x] No source, no verdict — every factual beat backed by source code; verdict (B09) recapitulates

## ILLUSTRATE LAW audit

Claude UI appears at: B00 (cold open subject = the tool invocation), B10 (handoff — viewer prompt)
B09 uses ClaudeVerdictArtifact (verdict UI — allowed per law)
B11 uses ClaudeTitleOutroHAI (outro — allowed per law)
Inner beats B02-B08 use SkillTeardownPipeline, SkillTeardownMechanism, ClaudeCodeBeat — all concept illustrations, not UI wallpaper ✓

## PPT test

No beat is a static headline + paragraph. B02 animates phase nodes. B03 shows
code card (moving). B04 shows heading + score table as animating elements.
B05 shows code. B06 animates verdict pill. B07 shows code. B08 shows code.
B09 animates verdict lines. B10 types prompt. B11 fades in. All PASS.
