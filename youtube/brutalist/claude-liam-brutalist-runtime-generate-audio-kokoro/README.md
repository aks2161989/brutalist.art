# Brutalist Utility: generate_audio_kokoro.py

AI Explainer episode 44 in the Brutalist playlist for **@HumanitariansAI**. Persona: **Liam, in for Bear**. Voice: local Kokoro **`am_onyx`**. 12 beats. Native 4K in both aspects.

## Deliverables

- Landscape 3840×2160 — `exports/landscape/claude-liam-brutalist-runtime-generate-audio-kokoro.mp4` (319.7 s, h264 + aac)
- Portrait 2160×3840 — `exports/vertical/claude-liam-brutalist-runtime-generate-audio-kokoro-vertical.mp4` (319.7 s, h264 + aac)

Both files are unpublished local renders. Bear's viewing / editing is the next step in the human pipeline; nothing here has been uploaded or transcoded by YouTube.

## Paperwork

- Landscape: `BRIEF.md`, `BUILD-PROMPT.md`, `FACTCHECK.md`, `SOURCES.md`, `PROMPTS.md`, `SHOTLIST.md`, `SCRIPT.md`, `CHECKS-REPORT.md`, `TYPECHECK.md`, `VISUAL-REVIEW.json`, `beat_sheet.json`, `build-state.json`, `SOURCE-SNAPSHOT.json`, `_qc/REPORT.md`, `_qc/contact_sheet.png`, `demo/`.
- Portrait: `vertical/BUILD-PROMPT.md`, `vertical/FACTCHECK.md`, `vertical/SOURCES.md`, `vertical/PROMPTS.md`, `vertical/SHOTLIST.md`, `vertical/CHECKS-REPORT.md`, `vertical/TYPECHECK.md`, `vertical/VISUAL-REVIEW.json`, `vertical/beat_sheet.json`, `vertical/build-state.json`, `vertical/_qc/REPORT.md`, `vertical/_qc/contact_sheet.png`.

## Human review pending

Both AI `VISUAL-REVIEW.json` records pass Gate V with 0 blockers and 0 majors. They are AI reviewer records, not human sign-offs. Bear's playback + notes in `FEEDBACK.md` remain the final quality gate before publication.

## OUTRO-LOCK note

Per `OUTRO-LOCK.md` the outro card is `ClaudeTitleOutro` / `ClaudeTitleOutro916` with the hardcoded handle `@NikBearBrown` — even for this playlist adaptation to `@HumanitariansAI`. Narration says "for at Humanitarians A I"; the composer folder chips throughout use `@HumanitariansAI`. Flagged here so the human reviewer can confirm the channel treatment before publication.

## Toolkit patches applied to the isolated workspace

- `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` — portrait scale patch (`height > width` ternary) so 9:16 BLUF coverage clears Gate V.
- `runtime/remotion/src/scenes/ClaudeCodeBeat.tsx` — adaptive fontSize clamp bounded by both card height and card width so long code stanzas fit in both aspects.
- `runtime/remotion/src/scenes/ClaudeTitleOutro916.tsx` — added `overflowWrap: 'anywhere'` + `wordBreak: 'break-word'` so unbreakable filenames like `generate_audio_kokoro.py` wrap on portrait.
- `runtime/remotion/src/Root.tsx` — registered `ClaudeCodeBeat916` (1080×1920) and `SkillTeardownMechanism916` (1080×1920) compositions.

These changes live only in this isolated toolkit; the public toolkit is unchanged.
