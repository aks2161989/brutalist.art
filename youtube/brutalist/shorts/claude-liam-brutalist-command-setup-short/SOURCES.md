# SOURCES.md — Brutalist Command: setup — Short

This is a whole-beat cut derived from the parent vertical. No new claims are introduced; every retained beat's audio, video and props are the parent's, byte-for-byte, except for the beat-sheet metadata (`slug`, `kind`, `derived_from`, `dropped_beats`).

## Parent (this Short's only primary source)

| Path | SHA-256 | Role |
|---|---|---|
| `youtube/brutalist/claude-liam-brutalist-command-setup/exports/vertical/claude-liam-brutalist-command-setup-vertical.mp4` | `029440a32ad41994d0618a2ceec06061bfe42d00715e3ee66a7a1b1ff208c94f` | Parent full-length native portrait master. The Short is a cut of six of its 13 beats. |
| `youtube/brutalist/claude-liam-brutalist-command-setup/vertical/beat_sheet.json` | as `episode.source_sha256` `054c7cecc190d6382f0639e23d118233511dbf21b0f7d4bae81af1282795071c` | Beat sheet the Short was cut from. Every kept beat's `render_duration_s`, `audio_file`, `shot.remotion.props`, `narration_text` and per-beat MP4 is reused unchanged. |

## Parent's ground-truth chain (relied on transitively)

The parent's `SOURCES.md` — `youtube/brutalist/claude-liam-brutalist-command-setup/vertical/SOURCES.md` — lists the `setup` script, `requirements.txt`, `runtime/scripts/setup_smoke_kokoro.py`, and the four `demo/RUN-LOG.txt` sections. All B04/B09 verbatim on-screen output traces to that log; all cited line numbers trace to that copy of `setup`. This Short does not re-verify those chains — the parent's FACTCHECK.md was accepted at parent build time (2026-09-10 UTC).

## Read for this Short (only)

- `BUILD-PROMPT.md`, `BRIEF.md`, `FEEDBACK.md` in this reel.
- `REPOLOOP-SHORTS-PROMPT.md`, `REPOLOOP-PROMPT.md` in the toolkit root.
- `CLAUDE.md`, `skills/make/ai-explainer/SKILL.md`, `skills/make/explainer/SKILL.md`, `skills/make/nopunt/SKILL.md` in the toolkit — for the ILLUSTRATE / EXECUTIVE-SUMMARY / HANDOFF / OUTRO laws, and for the "cut first, don't cram the long template" instruction.
- `runtime/scripts/shorts.py` — the cut utility used (whole-beat cut, `--drop`, `--no-endcard`, `--no-outro-rewrite`).
- `runtime/scripts/compile.py`, `runtime/scripts/build_safety.py` — the guarded compiler and its `require_short_duration` gate.

## Example leads (read only in the parent build; not consulted for this Short)

The parent's example leads (`rohan-v/2026-08-28-agent-first-brutalist`, `satwik-s/2026-09-05-reading-roadmap-ober-is-it-any-good`) were used at parent build time for staging patterns only. This Short does not republish, re-verify, or re-cite them; no human signature is reused.

## What is NOT a source of this Short

- No new AI generation. Audio is copied from the parent per-beat MP3s (Kokoro `am_onyx` from the parent build), video is the parent's native portrait per-beat MP4s. No regeneration ran.
- No paid API. No network calls of any kind during this cut/compile.
- No new demo output. The `demo/RUN-LOG.txt` sections cited in FACTCHECK.md were captured on the parent workstation at parent build time.
