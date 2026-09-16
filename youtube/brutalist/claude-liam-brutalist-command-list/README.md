# Brutalist Command: art --list

Episode 23 in the Brutalist playlist for **@HumanitariansAI**. Voice:
**Liam, in for Bear** (Kokoro `am_onyx`, free, local). Aliases covered:
`./art --list` and `./art list` (both share one `case` branch at
`art:58-80`). Rebuilt 2026-09-12 after source grew from 16 to 20 skills.

## Deliverables

Two watchable rendered films — landscape + a full-length native
portrait companion (not a shortened Short):

- **Landscape 3840 × 2160 · 191.1s** →
  `exports/landscape/claude-liam-brutalist-command-list.mp4`
- **Vertical 2160 × 3840 · 196.9s** →
  `exports/vertical/claude-liam-brutalist-command-list-vertical.mp4`

Verified sidecar receipts (dimension / hash / duration / input-hash
snapshot) live next to each mp4 as `*.verified.json`.

Both files come with:

- [beat_sheet.json](beat_sheet.json) · [vertical/beat_sheet.json](vertical/beat_sheet.json)
- [SCRIPT.md](SCRIPT.md) — the narration text (no captions).
- [SOURCES.md](SOURCES.md) · [vertical/SOURCES.md](vertical/SOURCES.md)
- [FACTCHECK.md](FACTCHECK.md) · [vertical/FACTCHECK.md](vertical/FACTCHECK.md)
- [SHOTLIST.md](SHOTLIST.md) · [vertical/SHOTLIST.md](vertical/SHOTLIST.md)
- [PROMPTS.md](PROMPTS.md) · [vertical/PROMPTS.md](vertical/PROMPTS.md)
- [CHECKS-REPORT.md](CHECKS-REPORT.md) · [vertical/CHECKS-REPORT.md](vertical/CHECKS-REPORT.md)
- [TYPECHECK.md](TYPECHECK.md) · [vertical/TYPECHECK.md](vertical/TYPECHECK.md)
- [VISUAL-REVIEW.json](VISUAL-REVIEW.json) · [vertical/VISUAL-REVIEW.json](vertical/VISUAL-REVIEW.json)
- [demo/RUN-LOG.md](demo/RUN-LOG.md) — the actual captured `./art --list`,
  `./art list`, `./art list foo bar`, `./art -list`, `./art bogus` runs
  from this workspace.

## What the reel establishes

`./art --list` and `./art list` are two aliases that both fall into the
same `--list|list)` branch of the `art` bash dispatcher. The branch is
21 `printf` calls — one header row plus one row per skill — with a
`'%-22s %s\n'` format string. Skills grew from 16 to 20 between builds
(added: godot-waikthrough, godot-gamedev, godot-gdd, riff). There is no
directory scan or plug-in discovery: the file **is** the table.

Extra positional arguments are silently ignored, because the branch
body never reads `"$@"`. A single-dash token like `./art -list` is
**not** an alias — it falls through to the `*)` catch-all, prints a
one-line hint to **stdout** (bare `echo`), and exits `2`. The recovery
is two commands: `./art --list` to see every skill, then `./art <skill> --help`
to open that skill's `SKILL.md` in `$PAGER`.

## Human review is next, not publication

These files sit under the reel folder. No upload, no publish, no push.
Bear's review + edits are the next step. If Bear leaves review notes in
`FEEDBACK.md`, the next unattended pass reads them and applies them.

## Remaining limitations

- `code-cascade` covers 58% of the beats (motion histogram WARN). A
  command teardown intentionally spends most of its time looking at
  source code and observed shell output; the motion budget was accepted,
  not evaded.
- The public `scripts/type_check.py` referenced by SKILL.md is not
  present in this workspace. TYPECHECK.md records the actual visual
  typography audit that stands in.
- Vertical build emits two skin-lint WARN lines on B00 and B11 that name
  the `-916` compositions (expected for portrait builds on `claude`
  palette). Same pattern ships on the sibling ep-help vertical.
- The vertical B01 narration is longer than the landscape B01 because
  the portrait BLUF recipe uses a 5-line stack with two corrections and
  the settled state must be visible by the 50% frame-sample point.
