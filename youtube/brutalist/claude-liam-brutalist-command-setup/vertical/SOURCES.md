# SOURCES.md — Brutalist Command: setup

Ground truth for every claim, quote and code fragment on screen.

## Primary sources (this run's episode)

| Path (repo-relative) | SHA-256 | Role |
|---|---|---|
| `setup` | 75040062dfcb20d0437a5a358abc516ed6e4b1e4e9020aaac926e1b9d5b2208d | The script the reel teardowns. Shebang, short-help block, ElevenLabs guard, `check()` helper, features table, aggregation loop. Referenced by line number in beat cards. |
| `requirements.txt` | c443062622f54a95539c1606add857acc9fcf7c0402955c411bc66bc9a98ddce | The pinned Python contract that `./setup --install` reads. Explains why `numpy>=2.0.2` is the binding floor (Kokoro `>=0.4` pins it; Manim `<0.19` has no upper bound → no conflict). |
| `art` | 9bb77a7c84701d23ab6e73f0a4f48592f17748ffad2c7114b62687bb7f97d0e9 | Dispatcher. Referenced only for the `doctor)` case that execs `setup`; the setup episode centres the script itself. |
| `runtime/scripts/setup_smoke_kokoro.py` | (this workspace) | The live-audio gate `setup` calls: synthesizes with Kokoro, decodes with `ffmpeg -af volumedetect`, asserts `mean_volume > -40 dB`. |

## Support (read during authoring)

- `skills/make/ai-explainer/SKILL.md` — Claude cut doctrine (bookends, ILLUSTRATE LAW, EXECUTIVE-SUMMARY LAW, HANDOFF LAW, OUTRO LAW, PROOF GATE).
- `skills/make/nopunt/SKILL.md` — SHOW / HOLD / CARD classification, teaching-arc checklist.
- `runtime/prose/teardown/PROSE.md` — Teardown register (Feynman × MKBHD).
- `CLAUDE-BRAND.md` — cream #FAF9F5, ink #3D3929, terracotta #D97757 as the one accent.
- `OUTRO-LOCK.md` — @NikBearBrown outro card is locked; hardcoded handle; slug-seeded mascot.
- `CLAUDE-CODE-VISUAL-QC-CHECK.md` — 9-point rubric, ≥2 fps sampling, per-beat 15/50/85% frames.
- `docs/PIPELINE-SAFETY.md` — atomic writes, live verification, ElevenLabs quarantine, review-record contract.
- `docs/FELLOWS-SUBMISSION.md` — read to confirm publishing is a separate human handoff; nothing shipped from this build.

## Verbatim demo evidence (this workstation, this run)

- `demo/RUN-LOG.txt` — four sections against the isolated workspace toolkit:
  1. `setup:1-16` — verbatim shebang + short-help header (source-of-truth on the two-mode surface).
  2. `$ ./setup` all-green (audio row lit by the actual Kokoro synth, cost `$0.00`, exit `0`).
  3. `$ ./setup` with `runtime/models` temporarily unlinked — the audio feature is the only blocked row; both hint lines print underneath; exit `1`.
  4. `$ ./setup` after re-linking — every row green again; exit `0`.

## Example leads (read, adapted, not republished)

Read-only reference sheets copied into the workspace by the supervisor. Neither is republished; both were consulted for staging patterns only.

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` (SHA-256 `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`) — "Your Weekly Video, Handled."; scanned for the Claude bookend spine.
- `satwik-s/2026-09-05-reading-roadmap-ober-is-it-any-good/beat_sheet.json` (SHA-256 `a0d5b44c5495913a7176c05aa7cb540fb63f60bfdbd13e4060d1ebcaa7c68d28`) — "How Would We Know It's Any Good?"; scanned for `ClaudeVerdictArtifact` verdict-lines rhythm.

## Sibling episode consulted (structure only)

- `youtube/brutalist/claude-liam-brutalist-command-doctor/` — the doctor teardown ships the same script from the dispatcher's angle; this episode covers the script itself, with `requirements.txt`, the `--install` pipeline, and the ElevenLabs guard as the differentiators. No files copied.
