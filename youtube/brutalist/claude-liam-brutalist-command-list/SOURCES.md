# SOURCES — Brutalist Command: art --list

## Primary source

- **`art` dispatcher** — the top-level bash script in the toolkit root.
  Isolated toolkit path:
  `.repoloop/workspaces/claude-liam-brutalist-command-list/toolkit/art`
  - SHA-256 (this invocation): `387d12c338fe3e8e05a3c2202be86ea81beaf548c2fd11ec3ee4876694f8b562`
  - Public URL for the same file: <https://github.com/nikbearbrown/brutalist.art/blob/main/art>
  - Relevant lines:
    - `art:37-116` — the whole `case "$cmd" in ... esac` dispatcher.
    - `art:41-59` — the `--list|list)` branch (17 `printf` calls: 1 header
      row + 16 skills).
    - `art:106-115` — the `*)` catch-all that emits the
      `art: unknown skill '<token>' (try ./art --list)` line and `exit 2`s.
    - `art:109-111` — the second `--help` path invoked by `./art <skill> --help`.

## Supporting sources

- **`CLAUDE.md`** (toolkit root) — the `./art --list` entry point is
  documented in "Entry point" (§ Skill reference / Entry point).
- **`skills/make/ai-explainer/SKILL.md`** — the fixed production
  contract for this playlist (cold open on `ClaudeComposerAsk`, BLUF via
  `BrutalistHesitantWriter`, verdict, Your Turn, outro).
- **`OUTRO-LOCK.md`** — the outro card's hardcoded `@NikBearBrown` handle,
  slug-seeded mascot, and title-restate rule.
- **`runtime/prose/teardown/PROSE.md`** — the Teardown register applied
  to this reel's narration.
- **`docs/PIPELINE-SAFETY.md`** — the runtime contract for narration audio,
  approvals, and export safety.

## Read-only example leads (adapted, never republished)

Per `BRIEF.md`:
- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — *Your Weekly
  Video, Handled.* (SHA-256
  `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`).
  Adapted only for staging cadence — no assets, no signature, no result claims
  are reused from this reel.
- `tanmay-kulkarni/2026-08-23-where-the-record-stops/beat_sheet.json` —
  *Where the Record Stops* (SHA-256
  `fc19c0a2f9373b8212dfce57589363ab192b84a9453e8edab5571c010b0a2511`).
  Not directly used; scanned for framing patterns only.

## Observed local runs (see `demo/RUN-LOG.md`)

- `./art --list` → 17 lines, exit `0`, stderr empty.
- `./art list` → identical stdout, exit `0`.
- `./art list foo bar` → identical stdout, exit `0`.
- `./art -list` → exit `2`, stdout carries the hint (bare `echo`), stderr empty.
- `./art bogus` → exit `2`, same shape of hint.

## Public repo (for viewers)

- Toolkit source: <https://github.com/nikbearbrown/brutalist.art>
- The exact dispatcher line numbers on `main` may drift over time; the
  SHA-256 above pins the copy this reel was authored against.

## Corrections applied to the source (per DOUBLE-CHECK LAW)

- The `--list|list)` branch is described as **printing** rather than
  "running" a skill anywhere the narration is tempted to conflate the
  two (see B01's hesitant correction and B06's mechanism beat).
- The failure hint from `./art bogus` and `./art -list` is written by
  a **bare `echo`**, so it lands on **stdout**, not stderr. Narration
  says so plainly rather than defaulting to the more common "one line
  to stderr" phrasing.

## Nothing paid, nothing published

No API keys, no paid tools, no upload steps were used to build this
reel. Kokoro (local), Remotion (local), and `ffmpeg` are the entire
render surface. Output stays under this reel folder for Bear's review.
