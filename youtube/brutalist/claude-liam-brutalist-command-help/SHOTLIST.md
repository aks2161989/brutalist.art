# SHOTLIST — Brutalist Command: art help

12 beats · 16:9 native @ 3840×2160 · 9:16 native @ 2160×3840 · Kokoro am_onyx.

| ID | Act | Scene | Duration (s) | On-screen |
|---|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | 17.11 | Composer with greeting "Namaste, Liam"; typed question about art help; runningText + 3 output lines |
| B01 | BLUF | `BrutalistHesitantWriter` (seeded `command-help-b01`) | 11.09 | Hesitant type: "art help is a menu of every skill." → "art help is a 17-line usage sheet from the file header." Trigger phrase 'menu of every skill' → '17-line usage sheet from the file header' |
| B02 | FRAMEWORK | `ClaudeCodeBeat` | 15.47 | Code card: `case "$cmd" in` with the four-alias pattern and fall-through star |
| B03 | MECHANISM | `ClaudeCodeBeat` | 14.76 | Code card: the two-sed pipeline extracted from `art:39` |
| B04 | WORKED_EXAMPLE | `ClaudeCodeBeat` | 12.48 | Code card: `$ ./art help` — the abbreviated 17-line usage sheet as printed |
| B05 | MECHANISM | `ClaudeCodeBeat` | 15.70 | Code card: the four alias invocations + the `""|-h|--help|help)` case pattern from art:38 |
| B06 | MECHANISM | `ClaudeCodeBeat` | 15.02 | Code card: `$ ./art --list` — 11-row excerpt of the skills catalog |
| B07 | FALSIFIABILITY | `ClaudeCodeBeat` | 15.74 | Code card: `$ ./art bogus` — the error line, exit 2, and the `*)` fall-through source |
| B08 | MECHANISM | `ClaudeCodeBeat` | 18.99 | Code card: the recovery path — `--list` then `<skill> --help`, with the second `--help` source (art:109-111) |
| B09 | VERDICT | `ClaudeVerdictArtifact` | 17.30 | Artifact card: "Four scopes" — help / --list / <skill> --help / unknown, one line each |
| B10 | YOUR_TURN | `ClaudeComposerAsk` (greeting "Your turn.") | 19.37 | Composer with paste-ready diff-the-aliases prompt; runningText; three expected-outcome lines |
| B11 | OUTRO | `ClaudeTitleOutro` (slug-seeded) | 5.10 | Title restate: "Brutalist Command: art help." · `@NikBearBrown` · slug-seeded mascot |

Total narration audio: ~178s. Chosen because measured, not targeted.

## Framing rules
- All 12 beats stay inside `SAFE` = 5% inset (`SAFE169`: x 192..3648, y 108..2052 at 3840×2160).
- Cream page background `#FAF9F5`; ink `#3D3929`; single terracotta accent `#D97757` per beat.
- Serif for titles + greeting; UI sans for chrome; SF Mono for code.
- No captions, subtitle tracks or transcript slides.
- Only three beats type on-screen text: B00 (ask), B01 (hesitant writer), B10 (handoff).

## Portrait notes
- Portrait build is a separate `beat_sheet.json` in `vertical/` with `aspect_ratio: 9:16` and slug `claude-liam-brutalist-command-help-vertical`.
- Every scene registered in `runtime/remotion/src/Root.tsx` has a 916 variant used by that portrait build.
- `BrutalistHesitantWriter916` re-uses the same component with the patched portrait design-box (see `feedback_hesitant_writer_portrait_scale_patch` — applied in-place to `BrutalistHesitantWriter.tsx`).
