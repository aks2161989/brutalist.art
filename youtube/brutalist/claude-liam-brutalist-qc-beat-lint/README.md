# Brutalist Utility: beat_lint.py — episode 57

AI Explainer teardown of `runtime/qc/beat_lint.py`. Twelve beats.
Voice: Kokoro `am_onyx` — Liam, in for Bear. Playlist: Brutalist.
Channel chip: `@HumanitariansAI`; outro: `@HumanitariansAI`
(ClaudeTitleOutroHAI — not @NikBearBrown).

## Films to watch

- Landscape (16:9, native 4K):
  `exports/landscape/claude-liam-brutalist-qc-beat-lint.mp4`
- Portrait (9:16, native 4K):
  `exports/vertical/claude-liam-brutalist-qc-beat-lint-vertical.mp4`

Both passed Gate V clean (0 BLOCKER, 0 MAJOR).

## What this episode covers

`beat_lint.py` is the plan-time linter for the Brutalist explainer pipeline.
It reads `beat_sheet.json` and enforces:

- **Rule 3** — no `lane:remotion` beat may use a text-card pattern
  (SlateCard, TextCard, TitleCard, CardText, QuoteCard) when it should
  be a real illustration.
- **Rule 4** — the only legal placeholder types are STILL and vox-anim.
- **Rule 7** — branding contract; `brand_labels.json` maps channel IDs.

Exit 0 = clean. Exit 2 = defects. Run it before audio, before Remotion.

## Beat mix (12 beats)

| ID  | Act       | Scene                  |
|-----|-----------|------------------------|
| B00 | ASK       | ClaudeComposerAsk      |
| B01 | BLUF      | BrutalistHesitantWriter|
| B02 | FRAMEWORK | BeatLintPipeline       |
| B03 | MECHANISM | ClaudeCodeBeat         |
| B04 | MECHANISM | ClaudeCodeBeat         |
| B05 | MECHANISM | ClaudeCodeBeat         |
| B06 | DEMO      | ClaudeCodeBeat         |
| B07 | DEMO      | ClaudeCodeBeat         |
| B08 | VERDICT   | ClaudeVerdictArtifact  |
| B09 | MECHANISM | ClaudeCodeBeat         |
| B10 | HANDOFF   | ClaudeComposerAsk      |
| B11 | OUTRO     | ClaudeTitleOutroHAI    |

## Paperwork

- Landscape: `SCRIPT.md`, `SOURCES.md`, `FACTCHECK.md`, `SHOTLIST.md`,
  `PROMPTS.md`, `CHECKS-REPORT.md`, `TYPECHECK.md`, `VISUAL-REVIEW.json`
- Portrait: `vertical/{CHECKS-REPORT,TYPECHECK}.md`,
  `vertical/VISUAL-REVIEW.json`

Contact sheets: `_qc/contact_sheet.png` and `vertical/_qc/contact_sheet.png`.

## What ran locally (safe)

- `python3 runtime/qc/beat_lint.py demo/` — clean on the demo fixture
- All renders: `remotion_scenes.py` via local node CLI with Chrome
  single-process wrapper (Apple App Sandbox workaround)
- Audio: Kokoro `am_onyx`, zero API cost

## What did not run

- No paid TTS call. No API keys used.
- No push, no upload, no publication.
- No captions, subtitle tracks, or burned-in transcript.
- No remote clone, `setup --install`, or `art keys` call.

## Next

Bear's viewing and editing is the next step. Add requests to
`FEEDBACK.md`; a future automatic run will pick them up.
