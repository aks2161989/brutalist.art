# SOURCES — Download Brutalist with Claude Code — Short

Every source consulted for the retained six beats of this Short. All native media and narration are byte-for-byte copies of the parent vertical film's completed renders; nothing was regenerated in this run.

## Parent source (the film this Short derives from)

| Path | SHA-256 |
|------|---------|
| `youtube/brutalist/claude-liam-brutalist-download-and-set-up/exports/vertical/claude-liam-brutalist-download-and-set-up-vertical.mp4` | `fbc678c7de34550760b7ac7b618032ac0acfbc3a783a34da67abd8667a1f5b07` |
| `youtube/brutalist/claude-liam-brutalist-download-and-set-up/vertical/beat_sheet.json` | `a9c97a786acd6510a3af93df041b44048b253e967ad8a75c93a1300328606678` |

## Primary sources — the isolated toolkit snapshot (`ba2d0e0`)

| Path | SHA-256 | Used in |
|------|---------|---------|
| `README.md` | `ca2eacdb6366bca0ae09d48ea0855da46aa003691a4f08a2f06b4b83e1b86588` | B00, B05 — the pitch and the free-by-default framing. |
| `setup` | `75040062dfcb20d0437a5a358abc516ed6e4b1e4e9020aaac926e1b9d5b2208d` | B04, B06 — the readiness table and the one download (Kokoro model). |
| `skills/make/ai-explainer/SKILL.md` | `a7421d4d861b44a983a31e9fcd7451cd32312a139366e74acc2123dfdefbd3c0` | Visual language (fidelity palette, ILLUSTRATE LAW, OUTRO LAW). |
| `runtime/prose/teardown/PROSE.md` | `6accc1a576ca9b52713abd31507f5deece6dc2612ca90967b25b661e59111786` | Narration register (Teardown). |
| `docs/PIPELINE-SAFETY.md` | `4619f0d4702317d654cd6498cadc8c277691e4c7565920ef851dbb628aa6298d` | The "free by default" contract; the boundary rules in B06. |
| `REPOLOOP-SHORTS-PROMPT.md` (this-run invocation prompt) | (supplied by supervisor) | Cut-first policy; strict 180s ceiling; no publish. |

## Read-only example leads (per BRIEF)

| Path | SHA-256 | Notes |
|------|---------|-------|
| `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` | `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22` | Reviewed for pacing; no signatures reused, no artefacts republished. |
| `mohammed-h/bond-pricing/beat_sheet.json` | `3c08c99358d62dfb105ecf6cd87d203773606865760550d88573c4f7354c7952` | Reviewed for act shape; no artefacts reused. |

## Reel-local artefacts produced this run

| Path | Purpose |
|------|---------|
| `beat_sheet.json` | The six-beat derivative recipe for this Short. Metadata `kind: short`, `aspect_ratio: 9:16`, `voice: am_onyx`, `voice_kokoro: am_onyx`, `captions: false`. |
| `CUT-PLAN.json` | Kept vs dropped beats, reason per drop, planned duration, cut-first review. |
| `media/B*.mp4` | Independent copies of the parent vertical's native 2160×3840 per-beat renders. |
| `mp3/beat-B*.mp3` | Independent copies of the parent vertical's per-beat narration audio. |
| `exports/short/claude-liam-brutalist-download-and-set-up-short.mp4` | The final compiled Short (produced by `runtime/scripts/compile.py`). |
