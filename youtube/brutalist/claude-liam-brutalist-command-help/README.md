# Brutalist Command: art help

Command teardown of the four `./art help` aliases (`""`, `-h`, `--help`, `help`)
that all hit the same case branch in the top-level `art` dispatcher. Body walks
the actual source (`art:37-116`), contrasts with `./art --list`, demonstrates
a real failure (`./art bogus` exits 2), and shows the two-command recovery.

Persona: **Liam, in for Bear** (Kokoro `am_onyx`, free/local).
Playlist: **Brutalist**, adapted for `@HumanitariansAI` folder chip.

## Deliverables

- **Landscape 16:9 (native 4K, 3840×2160)** — `exports/landscape/claude-liam-brutalist-command-help.mp4` · 177.0s
- **Vertical 9:16 (native 4K portrait, 2160×3840)** — `exports/vertical/claude-liam-brutalist-command-help-vertical.mp4` · 177.0s

Re-verified 2026-09-12 (run_id `48e0905963d54723ba7b587f9d86d97e`): art source
updated 2026-09-11 (godot-* dispatch added; line numbers shifted). Landscape beats
B03/B04/B05/B07/B08 were re-rendered 2026-09-11 and are already in the landscape
export. Vertical was re-compiled 2026-09-12 to incorporate those updated beats.
Both files passed Gate V clean (0 BLOCKER, 0 MAJOR across 24 sampled frames per
aspect). Independent review records:

- `VISUAL-REVIEW.json` (landscape)
- `vertical/VISUAL-REVIEW.json` (portrait)

## Paperwork (both aspects)

| File | Landscape | Portrait |
|---|---|---|
| Beat sheet | `beat_sheet.json` | `vertical/beat_sheet.json` |
| Script | `SCRIPT.md` | (narration identical) |
| Shot list | `SHOTLIST.md` | `vertical/SHOTLIST.md` |
| Sources | `SOURCES.md` | `vertical/SOURCES.md` |
| Fact check | `FACTCHECK.md` | `vertical/FACTCHECK.md` |
| Prompts | `PROMPTS.md` | `vertical/PROMPTS.md` |
| Checks report | `CHECKS-REPORT.md` | `vertical/CHECKS-REPORT.md` |
| Typography review | `TYPECHECK.md` | `vertical/TYPECHECK.md` |
| Build prompt (supplied) | `BUILD-PROMPT.md` | `vertical/BUILD-PROMPT.md` |

Demo captures (used verbatim as evidence in `FACTCHECK.md`) live in `demo/RUN-LOG.md`.

## Bear's next step

**Bear reviews the two mp4s and adds any changes to `FEEDBACK.md`.** Nothing has
been published, uploaded, or committed to git. Future auto-attempts will use
this workspace's saved state; if `FEEDBACK.md` receives edits before the next
attempt, the loop is expected to honor them.

## Known limitations flagged for human review

- Non-fatal `compile.py` motion-histogram warning: 7/12 beats use `code-cascade`
  (58%) — over the ~40% pantry cap. Documented in `CHECKS-REPORT.md`, accepted
  for a command-source teardown, not a blocker.
- Non-fatal `compile.py` SKIN LINT on the vertical build: it flags the 916
  cold-open and 916 outro against the landscape-oriented COLD OPEN / OUTRO
  LAWS — that is the correct pattern on a native portrait beat sheet.
- Missing runtime checkers noted in `TYPECHECK.md` (`scripts/type_check.py`,
  `reference/type-spec.md` — not present in this workspace snapshot). Actual
  visual-typography review was performed on rendered frames instead of relying
  on a checker that does not exist here.
- B04 code card lightly abbreviates a few descriptive tails of the 17-line
  usage sheet to fit the frame width; `demo/RUN-LOG.md` carries the verbatim
  output as the authoritative reference. Flagged in `FACTCHECK.md`.
