# Brutalist Command: art final — episode 33

Two native 4K files ready for Bear's viewing/editing pass. **Not published.**

**Rebuild note (run_id 9bd89bb7cb05441183300f026a38f958):** Source updated (commit ba2d0e0 "Preserve report audio and enforce safe fellows exports") — compile.py +237 lines shifted `final_preflight` from 451-463 to 454-466 and the atomic-replace block from 800-822 to 803-825; the input-hash check gained a `not Path(p).is_file()` guard. B04 and B06 re-rendered with corrected on-screen line numbers and updated code; both reels recompiled with --force. All other beats unchanged.

| Aspect | File | Duration | Dimensions | SHA-256 |
|---|---|---|---|---|
| Landscape 16:9 | [`exports/landscape/claude-liam-brutalist-command-final.mp4`](exports/landscape/claude-liam-brutalist-command-final.mp4) | 239.2 s | 3840 × 2160 | `a80eef513fe5a6c205fd429387e17a91bdf6dabb30c7faff09f827acd75ae146` |
| Vertical 9:16 | [`exports/vertical/claude-liam-brutalist-command-final-vertical.mp4`](exports/vertical/claude-liam-brutalist-command-final-vertical.mp4) | 239.2 s | 2160 × 3840 | `c25e50dbe6ad8063089904c96ca06562fbe0f09545af6a8ccf3e307dbb239746` |

Both files carry the same 12-beat spine:

- **B00** cold-open Claude composer — `Hei, Liam` greeting, ask about verified 4K compile + last-good-file preservation.
- **B01** BLUF hesitant writer — corrects `art final / renders once.` → `art final / verifies twice.`
- **B02** dispatcher case at `art:111-116` — one branch, two paths (`--height` check + `--height 2160` default when unset).
- **B03** `compile.py` argparse surface — the small nine-flag surface + `--out` fallback chain.
- **B04** `final_preflight` (compile.py:454-466) — paperwork triad + `beat_lint` + `gate_shape`, fails before rendering.
- **B05** worked example — verbatim `./art final /tmp/…-demo` output + the actual verified.json body. From `demo/RUN-LOG.txt` § 2.
- **B06** atomic candidate write (compile.py:803-825) — `TemporaryDirectory` → Gate V → approvals recheck → input-hash recheck → `os.replace`.
- **B07** the verified.json receipt shape — 5 keys; `ready` is a machine claim, not human sign-off, not YouTube 4K promise.
- **B08** failure + recovery — empty `FACTCHECK.md` refusal + observed SHA-256 identity + one-line recovery. Verbatim.
- **B09** verdict artifact — six-line recap of the whole surface.
- **B10** Your Turn — paste-ready prompt: run art final, cat the receipt, hash the mp4, compare, investigate on drift.
- **B11** outro — title restate + `@NikBearBrown` handle per OUTRO-LOCK.

## Watch & edit next

1. `exports/landscape/claude-liam-brutalist-command-final.mp4` (~17 MB · 4K H.264 + AAC).
2. `exports/vertical/claude-liam-brutalist-command-final-vertical.mp4` (~18 MB · 4K H.264 + AAC).
3. QC evidence: `_qc/proof-landscape-r3/*.png` (8 stills), `vertical/_qc/proof-vertical-r3/*.png` (6 stills), and `_qc/REPORT.md` (Gate V machine report).
4. `VISUAL-REVIEW.json` in each aspect directory records what was reviewed with real SHA-256s.

## Playlist adaptation for @HumanitariansAI — one open flag for Bear

Following the same pattern as episodes 29-32 (`art run` · `art shorts` · `art
vertical` · `art approvals`), this episode wears the `@HumanitariansAI` folder
chip in every Claude composer beat (B00, B10) while the outro card (B11) is the
shipped `ClaudeTitleOutro`, whose handle is **hardcoded to `@NikBearBrown` per
`OUTRO-LOCK.md`**. The composer chip is data-driven; the outro is doctrine.
Compile emitted a `SKIN LINT` warning about this on both aspects (portrait only —
landscape is clean), which is expected and recorded in each aspect's
`CHECKS-REPORT.md`. If Bear wants the outro card to read `@HumanitariansAI` too,
that is a `OUTRO-LOCK.md` policy change, not a per-reel edit.

## Known limitation — portrait code beats

Long monospace code lines in the portrait `ClaudeCodeBeat916` beats (B02-B08)
truncate at the white card's right edge in the 9:16 render. Ink stays inside
the card, so Gate-V passes; the salient part of every line is legible. Same
behaviour shipped in eps 29-32. Full lines are visible in the landscape master
and preserved verbatim in `demo/RUN-LOG.txt`. Called out in each aspect's
`CHECKS-REPORT.md` and `TYPECHECK.md`.

## Motion histogram note

`code-cascade` runs at 7/12 beats (58%), over the ~40% pantry cap. Accepted for
a command teardown where the body IS code — every code beat carries a distinct
real artifact (dispatcher, argparse, final_preflight, verbatim transcript,
atomic replace, receipt shape, failure+recovery). Compile emitted this warning;
recorded in `CHECKS-REPORT.md`.

## Isolated-toolkit patches applied

Two changes to the isolated toolkit only (public toolkit unchanged):

1. **BrutalistHesitantWriter.tsx** — scale-computation ternary so portrait
   canvases don't collapse `scale` to 0.5625 (per
   `feedback_brutalist_hesitant_writer_portrait_scale_patch`).
2. **Root.tsx** — registered `ClaudeCodeBeat916` (1080×1920 wrapper of the
   shared `ClaudeCodeBeat`). Missing from this toolkit revision, present in
   the sheets ep 29-32 already ship.

## What happens next

Bear watches both files, records notes in `FEEDBACK.md`, and either signs off
or requests targeted per-beat rebuilds. Nothing here is published; nothing is
uploaded; no external API was called during this build.

## Artifact tree

```
claude-liam-brutalist-command-final/
├── beat_sheet.json                    landscape source (SHA-256 ae45c2e6…)
├── vertical/
│   ├── beat_sheet.json                portrait source (SHA-256 c98d2c53…)
│   ├── VISUAL-REVIEW.json             AI frame review for portrait
│   ├── CHECKS-REPORT.md               portrait checks + iteration history
│   ├── TYPECHECK.md                   portrait typography
│   └── media/, mp3/, _qc/             portrait renders + QC
├── exports/
│   ├── landscape/                     4K landscape master + verified.json
│   └── vertical/                      4K portrait master + verified.json
├── media/, mp3/, clips/               landscape renders
├── _qc/                               landscape QC frames + report
├── demo/RUN-LOG.txt                   verbatim ./art final runs on 2 fixtures
├── BRIEF.md · FEEDBACK.md · SOURCE-SNAPSHOT.json     supervisor inputs
├── SCRIPT.md · SOURCES.md · FACTCHECK.md              paperwork
├── SHOTLIST.md · PROMPTS.md · CHECKS-REPORT.md        paperwork
├── TYPECHECK.md · BUILD-PROMPT.md                     paperwork
├── VISUAL-REVIEW.json                                 AI frame review for landscape
└── README.md                                          this file
```

## Human review pending

The films have been generated, gate-checked, and inspected frame-by-frame by an
AI reviewer. Bear is the human reviewer. Human sign-off is required before any
publication.
