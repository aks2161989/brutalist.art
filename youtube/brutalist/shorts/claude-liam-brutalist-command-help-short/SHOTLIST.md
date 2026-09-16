# SHOTLIST — Brutalist Command: art help (9:16 Short)

Native 2160×3840 portrait · 8 beats · Kokoro am_onyx.
Slug: `claude-liam-brutalist-command-help-short`.
Whole-beat cut of `claude-liam-brutalist-command-help-vertical`. Every retained
beat's rendered mp4 was copied unchanged from the parent's `vertical/media/`.

| ID | Act | Scene (parent 916 comp) | Render s | On-screen |
|---|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk916` | 17.125 | Portrait composer: greeting "Namaste, Liam"; ask "What does ./art help actually do — and what does it not do?"; folder chip `@HumanitariansAI`; output list: 17-line sheet + 4 aliases + different scope from `--list` |
| B01 | BLUF | `BrutalistHesitantWriter916` (seeded `command-help-b01`) | 9.75 | 4-line stack `art help / lists / every / skill.`; single trigger swap `skill` → `command` |
| B03 | MECHANISM | `ClaudeCodeBeat916` | 14.792 | Portrait code card `art:39` — two-sed pipeline; spark: "The help IS the header, minus the hash." |
| B04 | WORKED_EXAMPLE | `ClaudeCodeBeat916` | 12.500 | Portrait code card `$ ./art help  (verbatim, 17 lines)`; spark: "17 lines. Exits 0. Done." |
| B05 | MECHANISM | `ClaudeCodeBeat916` | 15.708 | Portrait code card: four aliases + the `""|-h|--help|help)` pattern; spark: "Empty. Dash-h. Dash-dash-help. help." |
| B06 | CONTRAST | `ClaudeCodeBeat916` | 15.042 | Portrait code card `$ ./art --list` — the skills catalog; spark: "help = commands. --list = skills." |
| B09 | VERDICT | `ClaudeVerdictArtifact916` | 17.333 | Portrait artifact card: four numbered scopes (`art help`, `art --list`, `art <skill> --help`, unknown token) |
| B11 | OUTRO | `ClaudeTitleOutro916` (slug-seeded) | 5.125 | Portrait title restate: "Brutalist Command: art help." · `@NikBearBrown` · mascot |

Total: **107.375 s** (measured on the final container, video and audio — all equal).

## Cut decisions

- **Dropped:** B02, B07, B08, B10. Reasons in `CUT-PLAN.json`.
- **No endcard, no outro rewrite** — the parent's B11 lands unchanged (locked
  outro per parent `OUTRO-LOCK.md`; `@NikBearBrown` hardcoded).
- **No visual regeneration** — every kept beat's rendered mp4 is a 2160×3840
  native portrait file reused as-is from the parent's `vertical/media/`. No
  center-cut, no `remotion_scenes.py` re-run, no pantry override.

## Portrait framing rules (inherited from parent)

- SAFE916 = x 108–2052, y 192–3648 (5% inset from 2160×3840 at 4K native).
- Sampled at beat-relative 15% / 50% / 85% for each of 8 beats (24 samples).
  All frame hashes captured in `VISUAL-REVIEW.json`.
- Code beats (B03, B04, B05, B06) inherit the parent's known code-card
  behaviour: code text is allowed to bleed past the right edge on wide lines
  (the leading columns — command tokens and comments — stay legible; the
  narration covers the trailing detail). Same behaviour as the parent film;
  no new regression introduced by the cut.
