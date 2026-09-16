# Brutalist Command: art approvals — episode 32

Two native 4K files ready for Bear's viewing/editing pass. **Not published.**

| Aspect | File | Duration | Dimensions | SHA-256 |
|---|---|---|---|---|
| Landscape 16:9 | [`exports/landscape/claude-liam-brutalist-command-approvals.mp4`](exports/landscape/claude-liam-brutalist-command-approvals.mp4) | 200.875 s | 3840 × 2160 | `1b3b85c9a03ff5fddfcb3aa50d2511c7d228f05291ff735578cf99be3952a2bd` |
| Vertical 9:16 | [`exports/vertical/claude-liam-brutalist-command-approvals-vertical.mp4`](exports/vertical/claude-liam-brutalist-command-approvals-vertical.mp4) | 200.875 s | 2160 × 3840 | `4fd6fbab9882f7657b6b0fd15ac6c6403fc87f7cd9dacfdad580bbce7d9c6bc8` |

Both files carry the same 12-beat spine:

- **B00** cold-open Claude composer — `Selam, Liam` greeting, ask about audit-only inspection.
- **B01** BLUF hesitant writer — corrects `art approvals / signs files.` → `art approvals / inspects subjects.`
- **B02** dispatcher case at `art:108-110` — one branch, no aliases, forwards to `build_safety.py`.
- **B03** the two verbs — argparse surface + `metadata.approvals` shape.
- **B04** worked example 1 — a plain command reel; no gates armed; silent pass. Verbatim from `demo/RUN-LOG.txt`.
- **B05** worked example 2 — a fellows reel; `--fingerprints` prints the two SHA-256 subjects. Verbatim.
- **B06** the five-field human review record contract + the exact fail-close conjunct from `build_safety.py:155-164`.
- **B07** `approval_subjects` recomputed every run — pasted SHAs are the human's, live SHAs are the truth.
- **B08** failure + recovery — one word added to B05 narration after signing; gate refuses `stale`. Verbatim.
- **B09** verdict artifact — six-line recap of the whole surface.
- **B10** Your Turn — paste-ready prompt read aloud verbatim, with grading rubric.
- **B11** outro — title restate + `@NikBearBrown` handle per OUTRO-LOCK.

## Watch & edit next

1. `exports/landscape/claude-liam-brutalist-command-approvals.mp4` (~14 MB · 4K H.264 + AAC)
2. `exports/vertical/claude-liam-brutalist-command-approvals-vertical.mp4`  (~14 MB · 4K H.264 + AAC)
3. QC evidence: `_qc/frames-landscape/*.png` (ten stills read individually) and `_qc/contact_sheet.png` (24-frame sheet).
4. `VISUAL-REVIEW.json` in each aspect directory records what was reviewed.

## Playlist adaptation for @HumanitariansAI — one open flag for Bear

Following the same pattern as episodes 29, 30, 31 (art run · art shorts · art vertical), this
episode wears the `@HumanitariansAI` folder chip in every Claude composer beat (B00, B10)
while the outro card (B11) is the shipped `ClaudeTitleOutro`, whose handle is
**hardcoded to `@NikBearBrown` per `OUTRO-LOCK.md`**. The composer chip is data-driven; the
outro is doctrine. Compile emitted a `SKIN LINT` warning about this on both aspects, which
is expected and recorded in each aspect's `CHECKS-REPORT.md`. If Bear wants the outro card
to read `@HumanitariansAI` too, that is a `OUTRO-LOCK.md` policy change, not a per-reel edit.

## Known limitation — portrait code beats

Long monospace code lines in the portrait `ClaudeCodeBeat916` beats (B02-B08) truncate at the
white card's right edge in the 9:16 render. Ink stays inside the card, so Gate-V passes;
the salient part of every line is legible. Same behaviour was shipped by ep 29 `art run`.
Full lines are visible in the landscape master and preserved verbatim in `demo/RUN-LOG.txt`.
Called out in each aspect's `CHECKS-REPORT.md` and `TYPECHECK.md`.

## Motion histogram note

`code-cascade` runs at 7/12 beats (58%), over the ~40% pantry cap. Accepted for a command
teardown where the body IS code — every code beat carries a distinct real artifact.
Compile emitted this warning; recorded in `CHECKS-REPORT.md`.

## What happens next

Bear watches both files, records notes in `FEEDBACK.md`, and either signs off or requests
targeted per-beat rebuilds. Nothing here is published; nothing is uploaded; no external
API was called during this build.

## Artifact tree

```
claude-liam-brutalist-command-approvals/
├── beat_sheet.json                    landscape source (SHA-256 7ae65275…)
├── vertical/
│   ├── beat_sheet.json                portrait source (SHA-256 f1d4362b…)
│   ├── VISUAL-REVIEW.json             AI frame review for portrait
│   ├── CHECKS-REPORT.md               portrait checks
│   ├── TYPECHECK.md                   portrait typography
│   └── media/, mp3/, _qc/             portrait renders + QC
├── exports/
│   ├── landscape/                     4K landscape master + verified.json
│   └── vertical/                      4K portrait master + verified.json
├── media/, mp3/, clips/               landscape renders
├── _qc/                               landscape QC frames + report
├── demo/RUN-LOG.txt                   verbatim ./art approvals runs on 3 fixtures
├── BRIEF.md · FEEDBACK.md · SOURCE-SNAPSHOT.json     supervisor inputs
├── SCRIPT.md · SOURCES.md · FACTCHECK.md              paperwork
├── SHOTLIST.md · PROMPTS.md · CHECKS-REPORT.md        paperwork
├── TYPECHECK.md · BUILD-PROMPT.md                     paperwork
├── VISUAL-REVIEW.json                                 AI frame review for landscape
└── README.md                                          this file
```

## Human review pending

The films have been generated, gate-checked, and inspected frame-by-frame by an AI
reviewer. Bear is the human reviewer. Human sign-off is required before any publication.
