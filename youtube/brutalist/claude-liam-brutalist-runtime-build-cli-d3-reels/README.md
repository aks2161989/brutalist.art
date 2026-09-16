# Brutalist Utility: build_cli_d3_reels.py

Episode 46 of the Brutalist playlist. AI Explainer teardown of `runtime/scripts/build_cli_d3_reels.py` — the 432-line batch orchestrator that wraps already-built D3 sim HTMLs into Claude-skin explainer reels, unattended, one config in and N review cuts out.

- **Voice:** Kokoro `am_onyx` (Liam, in for Bear)
- **Playlist:** Brutalist · Channel: @HumanitariansAI
- **Run ID:** `8d75c91064f84d83bc89e08d3efe2f26` (re-verified 2026-09-13; source unchanged)
- **Length:** ~234.79 s across 12 beats, both aspects

## Deliverables (both native 4K, Gate V clean)

| Aspect | File | Dimensions | SHA-256 |
|---|---|---|---|
| Landscape | `exports/landscape/claude-liam-brutalist-runtime-build-cli-d3-reels.mp4` | 3840×2160 | `17c51cf571786c86a48c59547c221516c5c0c853b10a57c586f0baffd068e3b1` |
| Vertical | `exports/vertical/claude-liam-brutalist-runtime-build-cli-d3-reels-vertical.mp4` | 2160×3840 | `849929b4cbd476cb0782fa8359926923ba58132902db4008a883a29242aa7d17` |

## Contents

- `beat_sheet.json` (12 beats, landscape) · `vertical/beat_sheet.json` (12 beats, portrait)
- `FACTCHECK.md`, `SOURCES.md`, `SHOTLIST.md`, `PROMPTS.md`, `TYPECHECK.md`, `CHECKS-REPORT.md` — per aspect
- `demo/config.json`, `demo/sim-source/00-tiny-wave.html`, `demo/beat_sheet_dryrun.json`, `demo/help.txt`, `demo/failure-html-missing.txt`, `demo/RUN-LOG.txt` — disposable synthetic fixtures used to demonstrate the tool's behavior source-backed
- `media/`, `mp3/`, `clips/`, `_qc/` — per-beat working files
- `VISUAL-REVIEW.json` — AI review record (this invocation's run_id, current SHAs, real frame evidence hashes)

## Playlist adaptation flag for the human reviewer

The **OUTRO card is locked** by `OUTRO-LOCK.md` — it stamps the hardcoded `@NikBearBrown` handle even though this reel lives in the Brutalist playlist under `@HumanitariansAI`. Playlist adaptation is currently on:
- the metadata `channel` field (`@HumanitariansAI`)
- the composer `folderLabel` prop on B00 and B10 (`@HumanitariansAI`)
- this README

**If the human reviewer wants the outro card to show `@HumanitariansAI`**, that requires either editing `runtime/remotion/src/scenes/ClaudeTitleOutro916.tsx` to accept a handle prop, or restating the outro doctrine — same call-out flagged on ep39 and ep40.

## Human review next

Bear watches the two files and can leave notes in `FEEDBACK.md`. Nothing has been published, uploaded, or committed to git.
