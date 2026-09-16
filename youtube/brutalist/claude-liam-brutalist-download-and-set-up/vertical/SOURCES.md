# SOURCES — Download Brutalist with Claude Code

Every source consulted for this episode, with repo-relative path and SHA-256 as captured in `SOURCE-SNAPSHOT.json`.

## Primary sources — the isolated toolkit snapshot (`ba2d0e0`)

| Path | SHA-256 | Used in |
|------|---------|---------|
| `README.md` | `ca2eacdb6366bca0ae09d48ea0855da46aa003691a4f08a2f06b4b83e1b86588` | B00, B01, B03, B05 — the pitch, the two entry points, the free-by-default framing. |
| `setup` | `75040062dfcb20d0437a5a358abc516ed6e4b1e4e9020aaac926e1b9d5b2208d` | B04, B06 — the readiness table and the one download (Kokoro model). |
| `art` | `9bb77a7c84701d23ab6e73f0a4f48592f17748ffad2c7114b62687bb7f97d0e9` | B03 — the second entry-point script. |
| `skills/make/ai-explainer/SKILL.md` | `a7421d4d861b44a983a31e9fcd7451cd32312a139366e74acc2123dfdefbd3c0` | All beats — the visual language (fidelity palette, ILLUSTRATE LAW, HANDOFF LAW, OUTRO LAW). |
| `skills/make/nopunt/SKILL.md` | `ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505` | Whole-sheet exit checks (SHOW/HOLD/CARD classification, teaching-arc). |
| `runtime/prose/teardown/PROSE.md` | `6accc1a576ca9b52713abd31507f5deece6dc2612ca90967b25b661e59111786` | Narration register. |
| `docs/PIPELINE-SAFETY.md` | `4619f0d4702317d654cd6498cadc8c277691e4c7565920ef851dbb628aa6298d` | The "free by default" contract; the boundary rules in B06. |
| `docs/FELLOWS-SUBMISSION.md` | `7825c728f040b0f7a49bbd950a5a2bef70c8a59ff2fbe0538716c8d3381f5223` | Fellows workflow expectations; the "Your Turn" prompt shape. |
| `REPOLOOP-PROMPT.md` | `abf55bdc729a9c30216e4375dff0c62b4bf5af4c717ad28be69709de64d5bc97` | The supervisor's paperwork requirements. |

## Cross-referenced doctrine (read but not directly cited in narration)

| Path | Why |
|------|-----|
| `CLAUDE.md` | House rules (audio-first, videos travel with their book, no publish). |
| `CLAUDE-BRAND.md` | Palette + typography source for the Claude fidelity brand. |
| `OUTRO-LOCK.md` | Why the shipped `ClaudeTitleOutro` cannot be reused on the HAI channel — it hardcodes `@NikBearBrown`. Justifies the reel-local `DbcOutro` component. |
| `CLAUDE-CODE-VISUAL-QC-CHECK.md` | Frame-sampling and 9-point rubric procedure (see `CHECKS-REPORT.md`). |
| `DESIGN-PRINCIPLES.md` | Beat 2 = executive summary law; hesitant-writer rendering. |

## Read-only example leads (per BUILD-PROMPT)

| Path | SHA-256 | Notes |
|------|---------|-------|
| `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` | `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22` | Reviewed for pacing and Kokoro voicing patterns; no signatures reused, no artefacts republished. |
| `mohammed-h/Bond-Pricing/beat_sheet.json` | `3c08c99358d62dfb105ecf6cd87d203773606865760550d88573c4f7354c7952` | Reviewed for act shape; no artefacts reused. |

## Reel-local sources produced this run

| Path | Purpose |
|------|---------|
| `beat_sheet.json` | The recipe for THIS reel; ten beats. |
| `demo/setup-output.txt` | Real doctor output from the isolated toolkit (`./setup`, exit 0, all seven features `✅ ready`). |
| `demo/clone-tree.txt` | Real folder listing of the isolated clone. |
| `runtime/remotion/src/DownloadBrutalist.tsx` | Reel-local Remotion components (`DbcPasteReady`, `DbcCloneTree`, `DbcDoctor`, `DbcLanes`, `DbcNotClaims`, `DbcVerdict`, `DbcOutro`). |
| `runtime/remotion/src/Root.tsx` (edited) | New `<Folder name="DownloadBrutalist">` block with 14 compositions (7 landscape + 7 portrait 916). |
| `runtime/scripts/chrome-single-process.sh` | Chrome wrapper for Apple App Sandbox (documented `ART_CHROME` hook; not a bypass). |
