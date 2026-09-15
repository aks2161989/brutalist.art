# Download Brutalist with Claude Code — episode 02

Second film in the Brutalist playlist for **@HumanitariansAI**. Persona **Liam, in for Bear**; Kokoro `am_onyx`; no captions; no publish.

## Deliverables (this session)

| Aspect | File | Dimensions | Duration | Notes |
|--------|------|------------|----------|-------|
| Landscape 16:9 | `exports/landscape/claude-liam-brutalist-download-and-set-up.mp4` | 3840×2160 | 165.1s | Gate V clean. Renders from run 92aed5ea; re-verified run db8a5a5b (source: PIPELINE-SAFETY.md + FELLOWS-SUBMISSION.md added, art script updated — content unchanged). |
| Vertical 9:16 | `exports/vertical/claude-liam-brutalist-download-and-set-up-vertical.mp4` | 2160×3840 | 165.1s | Native portrait, not a crop. Re-verified run db8a5a5b. |

## Where the paperwork lives

- `BRIEF.md`, `FEEDBACK.md`, `SOURCE-SNAPSHOT.json` — supplied by the supervisor.
- `BUILD-PROMPT.md` — supplied verbatim (do not edit).
- `SCRIPT.md`, `SHOTLIST.md`, `PROMPTS.md`, `FACTCHECK.md`, `SOURCES.md`, `TYPECHECK.md`, `CHECKS-REPORT.md`, `VISUAL-REVIEW.json` — this run.
- `beat_sheet.json` — the recipe.
- `demo/setup-output.txt`, `demo/clone-tree.txt` — real local doctor + clone evidence used to fact-check the film.
- `mp3/`, `media/`, `clips/` — audio, per-beat scenes, and conformed clips (landscape).
- `vertical/` — the native 9:16 recipe with its own beat sheet, mp3s, media, clips, and paperwork.
- `_qc/` — extracted frames, contact sheets, `REPORT.md` from Gate V.
- `scene-source/` — captured overlay of the reel-local scene changes (`DownloadBrutalist.tsx` + `Root.tsx` edit) for reproducibility.

## Next step

Bear watches both mp4s. Anything worth changing goes into `FEEDBACK.md`. A subsequent build reads that file and rebuilds the affected beats. Publishing to @HumanitariansAI happens later in the human pipeline — this repo does not upload.
