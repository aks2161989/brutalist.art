# SHOTLIST — Brutalist Command: art help (9:16 vertical companion)

Native 2160×3840 portrait · 12 beats · Kokoro am_onyx.
Slug: `claude-liam-brutalist-command-help-vertical` (independent build; not a Short).

| ID | Act | Scene | Duration (s) | On-screen |
|---|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk916` | 17.11 | Portrait composer reflow: greeting "Namaste, Liam" stacked above the composer; typed ask + 3 output lines below |
| B01 | BLUF | `BrutalistHesitantWriter916` (seeded `command-help-b01`, portrait props) | 9.71 | 4-line stack `art help / lists / every / skill.`; single trigger swap `skill`→`command` |
| B02 | FRAMEWORK | `ClaudeCodeBeat916` | 15.47 | Portrait code card: the bash `case` block |
| B03 | MECHANISM | `ClaudeCodeBeat916` | 14.76 | Portrait code card: the two-sed pipeline (art:39) |
| B04 | WORKED_EXAMPLE | `ClaudeCodeBeat916` | 12.48 | Portrait code card: `$ ./art help` output |
| B05 | MECHANISM | `ClaudeCodeBeat916` | 15.70 | Portrait code card: the four aliases + case pattern |
| B06 | MECHANISM | `ClaudeCodeBeat916` | 15.02 | Portrait code card: `$ ./art --list` skills table excerpt |
| B07 | FALSIFIABILITY | `ClaudeCodeBeat916` | 15.74 | Portrait code card: `$ ./art bogus` failure + fall-through source |
| B08 | MECHANISM | `ClaudeCodeBeat916` | 18.99 | Portrait code card: recovery + `<skill> --help` source |
| B09 | VERDICT | `ClaudeVerdictArtifact916` (portrait, larger fonts) | 17.30 | Portrait artifact card, 4 numbered lines |
| B10 | YOUR_TURN | `ClaudeComposerAsk916` (greeting "Your turn.") | 19.37 | Portrait composer with paste-ready diff-the-aliases prompt |
| B11 | OUTRO | `ClaudeTitleOutro916` (slug-seeded) | 5.10 | Portrait title restate: "Brutalist Command: art help." · `@NikBearBrown` · mascot |

Total: 177.0s after compile.py per-beat conform.

## Portrait-specific framing rules
- SAFE916 = x 108–2052, y 192–3648 (5% inset from 2160×3840 canvas at 4K native).
- Every beat inspected in-frame; Gate V clean at both 50% and 85% samples per beat.
- No content crosses SAFE916 in any sampled frame (24 total).
- Same cream page (`#FAF9F5`), same ink (`#3D3929`), same single terracotta accent per beat.
