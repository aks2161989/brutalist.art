# Brutalist Utility: image_fetch.py
**@HumanitariansAI Brutalist playlist — Episode 45**

Liam in for Bear. AI Explainer skill-teardown treatment.

## Deliverables

| File | Duration | Aspect | Status |
|---|---|---|---|
| `exports/landscape/claude-liam-brutalist-runtime-image-fetch.mp4` | 172.2s | 3840×2160 | Gate V ✓ |
| `exports/vertical/claude-liam-brutalist-runtime-image-fetch-vertical.mp4` | 172.2s | 2160×3840 | Gate V ✓ |

## Content summary

image_fetch.py is the Brutalist pipeline's multi-source archival image fetch tool. Four adapters (smithsonian, nasa, wellcome, nlm_ihm), one interface. Topaz Photo AI upscale is optional — probed by PATH, gracefully absent when not installed. Every shelved image gets a `.source.json` provenance sidecar recording source, license, credit, and URL. One command covers resolve → download → upscale → shelve → sidecar → pantry copy.

## Beat arc

| Beat | Act | Scene | Duration |
|---|---|---|---|
| B00 | COLD OPEN | ClaudeComposerAsk — Liam greets, command types, output lands | 10.8s |
| B01 | BLUF | BrutalistHesitantWriter — "downloader" corrects to "pipeline" | 14.0s |
| B02 | THE PIPELINE | SkillTeardownPipeline — six phases from call to shelf | 22.1s |
| B03 | THE TWO PATHS | ClaudeCodeBeat — smithsonian (no --url) vs nasa (with --url) | 19.6s |
| B04 | CLI FLAGS | ClaudeCodeBeat — full invocation with --copy --beat | 18.3s |
| B05 | FOUR ADAPTERS | SkillTeardownMechanism — one interface, four archives | 21.3s |
| B06 | DESIGN TELL | SkillTeardownMechanism — Topaz PATH probe, graceful fallback | 20.2s |
| B07 | VERDICT | ClaudeVerdictArtifact — four artifact lines stagger in | 19.6s |
| B08 | HANDOFF | ClaudeComposerAsk — Your Turn paste-ready Smithsonian prompt | 18.2s |
| B09 | OUTRO | ClaudeTitleOutroHAI — "Brutalist Utility: image_fetch.py." @HumanitariansAI | 8.0s |

## Voice & branding
- Voice: Kokoro am_onyx (Liam persona)
- Channel: @HumanitariansAI
- Palette: claude (cream, charcoal, terracotta)
- No captions, no subtitles

## For the human reviewer
- Re-verified 2026-09-14 (run_id e3271f85). Outro fixed: ClaudeTitleOutroHAI / ClaudeTitleOutroHAI916 now used, showing @HumanitariansAI in both aspects.
- All Gate V checks pass: 0 BLOCKER / 0 MAJOR on both aspects
- @HumanitariansAI appears in B00 folder chip, B08 folder chip, and B09 outro on both landscape and portrait
- Portrait B05 uses BrutalistAdaptCLI916 (four-adapter CLI terminal) for reliable portrait fill
- No upload, no commit, no publication — ready for Bear's review and editing
