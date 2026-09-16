# SOURCES.md — What Is Brutalist?

*Brutalist playlist · claude-liam · @HumanitariansAI. This film explains the
Brutalist toolkit itself; the sources below are what the film reads from and
adapts, not what it repackages.*

## Primary — the toolkit's own instructions (SOURCE-SNAPSHOT.json)

Every one of these files was captured by the queue supervisor into
`SOURCE-SNAPSHOT.json` at 2026-09-07T22:28:00 UTC and read in full before the
beat sheet was authored. SHA-256 values below reproduce that snapshot exactly.

| Path (repo-relative) | SHA-256 |
|---|---|
| `README.md` | `ca2eacdb6366bca0ae09d48ea0855da46aa003691a4f08a2f06b4b83e1b86588` |
| `art` | `9bb77a7c84701d23ab6e73f0a4f48592f17748ffad2c7114b62687bb7f97d0e9` |
| `setup` | `75040062dfcb20d0437a5a358abc516ed6e4b1e4e9020aaac926e1b9d5b2208d` |
| `skills/make/ai-explainer/SKILL.md` | `a7421d4d861b44a983a31e9fcd7451cd32312a139366e74acc2123dfdefbd3c0` |
| `skills/make/nopunt/SKILL.md` | `ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505` |
| `runtime/prose/teardown/PROSE.md` | `6accc1a576ca9b52713abd31507f5deece6dc2612ca90967b25b661e59111786` |
| `docs/PIPELINE-SAFETY.md` | `4619f0d4702317d654cd6498cadc8c277691e4c7565920ef851dbb628aa6298d` |
| `docs/FELLOWS-SUBMISSION.md` | `7825c728f040b0f7a49bbd950a5a2bef70c8a59ff2fbe0538716c8d3381f5223` |
| `REPOLOOP-PROMPT.md` | `abf55bdc729a9c30216e4375dff0c62b4bf5af4c717ad28be69709de64d5bc97` |

`SOURCE-SNAPSHOT.json` aggregate SHA-256:
`ddf47cf29eca4e4d7b85618b272f501a53a1482c6dcd9b90f2eb817df758619b`
(matches `episode.source_sha256` for this invocation.)

Also read while authoring: `CLAUDE.md`, `CLAUDE-BRAND.md`, `OUTRO-LOCK.md`,
`CLAUDE-CODE-VISUAL-QC-CHECK.md`, `DESIGN-PRINCIPLES.md`,
`skills/make/explainer/SKILL.md` was searched for but is not present in this
toolkit — that is logged as an availability gap in `CHECKS-REPORT.md`.

## Public setup URL used on screen (B08 handoff)

`https://github.com/nikbearbrown/brutalist.art` — the public DOT toolkit
repository named in `REPOLOOP-PROMPT.md`. The clone/install path was validated
against the isolated toolkit copy for this run (`demo/setup-help.txt`,
`demo/art-list.txt`), and the paste-ready prompt shown in the composer at B08
is the same one a fellow would run on a fresh machine.

## Read-only example leads (BRIEF.md)

These beat sheets were read (not republished, not reused verbatim) for staging
patterns and register calibration only. Original repo-relative paths and the
SHA-256 values as supplied by BRIEF.md:

| Repo path | SHA-256 | Title |
|---|---|---|
| `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` | `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22` | Your Weekly Video, Handled. |
| `satwik-s/2026-08-29-reading-roadmap-reason-or-retreive/beat_sheet.json` | `dbc4a4477f568e752c29c853af32c61e950cae087a2a54961db39d99339e021b` | Does It Reason, or Just Retrieve? |

These are leads, not verified facts. No signatures, private Drive links,
personal contacts, or claimed outputs from those runs are carried forward.
Duration/setup content that has since drifted (setup was rewritten and
ElevenLabs was removed) was corrected against the actual current source files.

## Native custom scenes authored for THIS reel

All in the isolated toolkit at
`.repoloop/workspaces/claude-liam-brutalist-what-is-brutalist/toolkit/runtime/remotion/src/WhatIsBrutalist.tsx`,
registered as folder "WhatIsBrutalist" in `Root.tsx`. The live public library
was not modified. Same component supports both 16:9 and 9:16 aspects; portrait
compositions are registered natively as separate `Wib*916` ids.

- `WibRecipe` / `WibRecipe916` — beat_sheet.json snippet ↔ rendered composer.
- `WibPipeline` / `WibPipeline916` — BRIEF → BEAT SHEET → AUDIO → SCENES →
  COMPILE → 4K MASTER (no PUBLISH — this reel is explicit about that).
- `WibChange` / `WibChange916` — one edited field → one visible change.
- `WibDivision` / `WibDivision916` — HUMAN judgment lane vs AGENT execution lane.
- `WibNotClaims` / `WibNotClaims916` — the honest not-list.
- `WibOutro` / `WibOutro916` — title-restate outro with HARDCODED
  `@HumanitariansAI` handle. The shipped `ClaudeTitleOutro` hardcodes
  `@NikBearBrown` per `OUTRO-LOCK.md` and cannot be reused on the HAI channel;
  this native variant is the required substitute.

## No paid sources, no uploads, no fabricated approvals

No paid API, no Higgsfield, no ElevenLabs, no stock media, no invented
signature. Kokoro `am_onyx` ran locally at $0.00. The Claude subscription was
used to author code and paperwork inside the isolated sandbox; the finished
films stay in the reel folder for Bear to watch before any human decision to
publish.
