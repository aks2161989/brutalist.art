# Brutalist Command: art keys

Episode 36 of the Brutalist Command playlist for @HumanitariansAI —
Liam in for Bear (Kokoro `am_onyx`, Teardown register).

## What's in the box

- **Landscape master (16:9)** →
  [`exports/landscape/claude-liam-brutalist-command-keys.mp4`](exports/landscape/claude-liam-brutalist-command-keys.mp4)
  — 3840×2160, 218.583 s, ~14 MB · Gate V clean (0 BLOCKER, 0 MAJOR).
- **Vertical master (9:16)** →
  [`exports/vertical/claude-liam-brutalist-command-keys-vertical.mp4`](exports/vertical/claude-liam-brutalist-command-keys-vertical.mp4)
  — 2160×3840, 218.583 s, ~15 MB · Gate V clean (0 BLOCKER, 0 MAJOR).

Both files have sibling `verified.json` receipts (SHA-256, per-input
hashes, atomic-write timestamp).

## The reel in one paragraph

Twelve beats. Cold open ask (Habari, Liam — "which optional keys does
this box have?"). Hesitant-writer BLUF: "art keys / blocks renders." →
"art keys / audits upgrades." Dispatcher case at `art:103-104` (two
lines, no aliases). Four-status taxonomy (valid / invalid / unset /
warn). Two verbatim demonstrations — higgsfield offline (`❌ invalid`,
exit 0) and higgsfield removed from `PATH` (`· unset`, exit 0). The 17-line
higgsfield probe body (`check_keys.py:44-58`). The `.env` loader plus a
`grep -c` redaction proof (zero matches for a synthetic secret). The
Teardown moment: the docstring promises exit-1-on-invalid, `any_invalid
= False` on line 40 is never reassigned, so exit is always 0. Verdict
artifact (six lines). Your-Turn: audit the script against its own
docstring — don't fix it, just write the failing pytest. Outro title
restate + `@NikBearBrown` handle.

## Bear — please review

- **What's next**: your viewing and any edit notes in `FEEDBACK.md`.
  Nothing is published, uploaded, pushed to git, or transcoded on
  YouTube's side yet — this is a local review cut.
- **Known things to look at**:
  1. **B01 hesitant-writer BLUF.** Was the misconception "art keys
     blocks renders" → "art keys audits upgrades" the right cognitive
     move? The chapter's other option was framing keys as a required
     setup step; I picked the "gate vs diagnostic" framing because
     that's what most fellows will assume.
  2. **B08 design tell.** I named two doc/reality drifts by their line
     numbers: docstring vs `any_invalid = False`, and the `art:20`
     "SI key" phrase that has no matching probe. FACTCHECK.md verifies
     both. If you'd rather I stayed off the Teardown critique of the
     script itself, say so and I'll rewrite B08 as a "when to use this"
     beat instead.
  3. **OUTRO-LOCK on this reel is `@NikBearBrown`** even though the
     channel adaptation is @HumanitariansAI. This is intentional per
     `OUTRO-LOCK.md` (locked component). Say the word if you want a
     one-off override in the outro before the video ships to the HAI
     channel.
  4. **Portrait code cards.** ClaudeCodeBeat916 truncates long lines at
     the right edge on the vertical variant — a known limitation from
     ep 32/34. Salient text stays visible; full code is in the
     landscape master. Flip to landscape on YouTube for the full code
     view.

## Paperwork

- [`SCRIPT.md`](SCRIPT.md) — the twelve narration texts, source of truth
  for Kokoro.
- [`SOURCES.md`](SOURCES.md) — the two isolated-toolkit source files
  (`art`, `runtime/scripts/check_keys.py`), the read-only fellows leads,
  and the SHA-anchored provenance chain.
- [`FACTCHECK.md`](FACTCHECK.md) — every specific claim in the narration,
  cross-referenced to the source file line ranges and demo/RUN-LOG.txt
  sections.
- [`SHOTLIST.md`](SHOTLIST.md) — per-beat scene, motion, and show block.
- [`PROMPTS.md`](PROMPTS.md) — the paste-ready Your-Turn prompt and
  determinism notes.
- [`CHECKS-REPORT.md`](CHECKS-REPORT.md) · [`TYPECHECK.md`](TYPECHECK.md) —
  landscape (also present under `vertical/`).
- [`VISUAL-REVIEW.json`](VISUAL-REVIEW.json) — landscape record for the
  supervisor.
- [`vertical/`](vertical/) — the portrait companion reel with its own
  paperwork.
- [`demo/RUN-LOG.txt`](demo/RUN-LOG.txt) — the five verbatim command
  sections (higgsfield offline, higgsfield unset, source excerpts,
  dispatcher case, redaction proof).

## Provenance

- `episode.run_id` = `b7896f5b2d2a441186ff1451881c0a5b` (re-verified 2026-09-13; previous run abdef8f04e1246deaf8cf7ab26ae350b was interrupted by Claude usage limit — exports unchanged)
- `episode.source_sha256` = `7c3b6abf2ec61bb70122fe12ba1e2d5bad049db19db16ddb3a1026cad274e8c6`
- Toolkit: isolated copy at
  `.repoloop/workspaces/claude-liam-brutalist-command-keys/toolkit`
  (SHA-256 baseline in `SOURCE-SNAPSHOT.json`).
- Voice: Kokoro `am_onyx` (free, local); ElevenLabs and any paid TTS
  disabled at policy level.
- Chrome: `chrome-headless-shell` via `ART_CHROME` wrapper with
  `--single-process --in-process-gpu` (see
  `feedback_chrome_sandbox_remotion_fix`).
- Node modules: shadowed under a per-package-symlink `node_modules/`
  with a writable `.cache/` (see
  `feedback_isolated_toolkit_node_modules_shadow`).
