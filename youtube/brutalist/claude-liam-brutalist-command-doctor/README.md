# Brutalist Command: art doctor — episode 34

Two native 4K files ready for Bear's viewing/editing pass. **Not published.**

| Aspect | File | Duration | Dimensions | SHA-256 |
|---|---|---|---|---|
| Landscape 16:9 | [`exports/landscape/claude-liam-brutalist-command-doctor.mp4`](exports/landscape/claude-liam-brutalist-command-doctor.mp4) | 216.79 s | 3840 × 2160 | `ea42f210bc59574e909b23f708d252b66e2531735494797faf161a7ba78ba411` |
| Vertical 9:16  | [`exports/vertical/claude-liam-brutalist-command-doctor-vertical.mp4`](exports/vertical/claude-liam-brutalist-command-doctor-vertical.mp4) | 216.79 s | 2160 × 3840 | `6841c2a078a80271abf298ffe2db0e8b4e571101373abc2d50144523effcb67d` |

Both files carry the same 12-beat spine:

- **B00** cold-open Claude composer — `Jambo, Liam` greeting, ask about verifying-not-installing.
- **B01** BLUF hesitant writer — corrects `art doctor / installs deps.` → `art doctor / verifies live.`
- **B02** dispatcher case at `art:96-99` — one branch, no aliases, execs `./setup` with `$@` forwarded.
- **B03** two modes, one FEATURES table — `./art doctor` verifies; `./art doctor --install` installs then verifies.
- **B04** worked example — the verbatim green table from a ready toolkit; cost $0.00, exit 0.
- **B05** bash 3.2 compat — the `check()` helper with dynamic `OK_<id>`/`MISS_<id>` vars via `eval`.
- **B06** live verification, not receipts — `kokoro_synth` must synthesise + decode a phrase above -40 dB.
- **B07** aggregation loop (`setup:156-172`) — 13 atomic checks → 7 features; any missing hint prints beneath.
- **B08** failure + recovery — hide the Kokoro `.onnx` file, audio row goes red + two hint lines + exit 1. Verbatim.
- **B09** verdict artifact — six-line recap of the whole surface, in the order you use it.
- **B10** Your Turn — paste-ready "read art doctor, do not install" prompt read aloud verbatim, with grading rubric.
- **B11** outro — title restate + `@NikBearBrown` handle per OUTRO-LOCK.

## Watch & edit next

1. `exports/landscape/claude-liam-brutalist-command-doctor.mp4` (~15 MB · 4K H.264 + AAC)
2. `exports/vertical/claude-liam-brutalist-command-doctor-vertical.mp4` (~16 MB · 4K H.264 + AAC)
3. QC evidence: `_qc/frames-landscape/*.png` (36 stills, three per beat) and
   `_qc/contact_sheet.png` (16-frame sheet). Portrait companions live under
   `vertical/_qc/`.
4. `VISUAL-REVIEW.json` in each aspect directory records what was reviewed.

## Playlist adaptation for @HumanitariansAI — one open flag for Bear

Following the same pattern as episodes 29-32 (art run · art shorts · art vertical
· art approvals), this episode wears the `@HumanitariansAI` folder chip in every
Claude composer beat (B00, B10) while the outro card (B11) is the shipped
`ClaudeTitleOutro`, whose handle is **hardcoded to `@NikBearBrown` per
`OUTRO-LOCK.md`**. The composer chip is data-driven; the outro is doctrine.
Compile emitted a `SKIN LINT` warning about this on the vertical aspect
(expected; the landscape aspect passes cleanly because it uses the shipped
components in their native orientation). Recorded in each aspect's
`CHECKS-REPORT.md`. If Bear wants the outro card to read `@HumanitariansAI`
too, that is an `OUTRO-LOCK.md` policy change, not a per-reel edit.

## Known limitation — portrait code beats

Long monospace code lines in the portrait `ClaudeCodeBeat916` beats (B02-B08)
truncate at the white card's right edge in the 9:16 render. Ink stays inside
the card, so Gate V passes; the salient part of every line is legible. Same
behaviour was shipped by episodes 29-32. Full lines are visible in the
landscape master and preserved verbatim in `demo/RUN-LOG.txt`. Called out in
each aspect's `CHECKS-REPORT.md` and `TYPECHECK.md`.

## Motion histogram note

`code-cascade` runs at 7/12 beats (58%), over the ~40% pantry cap. Accepted
for a command teardown where the body IS code — every code beat carries a
distinct real artifact. Compile emitted this warning; recorded in
`CHECKS-REPORT.md`.

## Toolkit patches applied (isolated toolkit only, this run)

- `runtime/remotion/src/Root.tsx` — added a native `ClaudeCodeBeat916`
  composition (1080×1920, same component and schema as the landscape
  ClaudeCodeBeat). Ran `./art scene-index` to register it.
- `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` — applied the
  4-line portrait scale patch (per the feedback memory) so 9:16 BLUF
  coverage clears the Gate V 55% floor.
- `runtime/remotion/node_modules/` — replaced the symlink with a shadow
  directory of per-package symlinks + writable `.cache/` (sandbox workaround).

Public toolkit and fellows folders were not modified.

## What happens next

Bear watches both files, records notes in `FEEDBACK.md`, and either signs
off or requests targeted per-beat rebuilds. Nothing here is published;
nothing is uploaded; no external API was called during this build.

## Artifact tree

```
claude-liam-brutalist-command-doctor/
├── beat_sheet.json                    landscape source (SHA-256 a2252dade…)
├── vertical/
│   ├── beat_sheet.json                portrait source (SHA-256 9d0c0217…)
│   ├── VISUAL-REVIEW.json             AI frame review for portrait
│   ├── CHECKS-REPORT.md               portrait checks
│   ├── TYPECHECK.md                   portrait typography
│   ├── SOURCES.md · FACTCHECK.md · SHOTLIST.md · PROMPTS.md · BUILD-PROMPT.md
│   └── media/, mp3/, _qc/             portrait renders + QC
├── exports/
│   ├── landscape/                     4K landscape master + verified.json
│   └── vertical/                      4K portrait master + verified.json
├── media/, mp3/, clips/               landscape renders
├── _qc/                               landscape QC frames + report + contact sheet
├── demo/RUN-LOG.txt                   verbatim ./art doctor runs on this workstation
├── BRIEF.md · FEEDBACK.md · SOURCE-SNAPSHOT.json     supervisor inputs
├── SCRIPT.md · SOURCES.md · FACTCHECK.md              paperwork
├── SHOTLIST.md · PROMPTS.md · CHECKS-REPORT.md        paperwork
├── TYPECHECK.md · BUILD-PROMPT.md                     paperwork
├── VISUAL-REVIEW.json                                 AI frame review for landscape
└── README.md                                          this file
```

## Human review pending

The films have been generated, gate-checked, and inspected frame-by-frame by
an AI reviewer. Bear is the human reviewer. Human sign-off is required
before any publication.
