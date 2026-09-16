# Brutalist Command: repoloop.sh

Playlist: **Brutalist** · Channel: **@HumanitariansAI** · Persona: **Liam, in for Bear**
Voice: Kokoro `am_onyx` (local) · Beats: 12 · Duration: 221.1s (~3:41)

Both films are rendered, gate-checked, and awaiting Bear's viewing/editing —
they are **not published**. The next step is human review, not upload.

## Outputs

- Landscape 16:9 (3840×2160): [`exports/landscape/claude-liam-brutalist-command-repoloop.mp4`](exports/landscape/claude-liam-brutalist-command-repoloop.mp4)
  - Review record: [`VISUAL-REVIEW.json`](VISUAL-REVIEW.json)
- Vertical 9:16 (2160×3840): [`exports/vertical/claude-liam-brutalist-command-repoloop-vertical.mp4`](exports/vertical/claude-liam-brutalist-command-repoloop-vertical.mp4)
  - Review record: [`vertical/VISUAL-REVIEW.json`](vertical/VISUAL-REVIEW.json)

## Paperwork

- Landscape: `SCRIPT.md`, `FACTCHECK.md`, `SOURCES.md`, `SHOTLIST.md`, `PROMPTS.md`, `CHECKS-REPORT.md`, `TYPECHECK.md`, `BUILD-PROMPT.md`, `beat_sheet.json`
- Vertical: `vertical/FACTCHECK.md`, `vertical/SOURCES.md`, `vertical/SHOTLIST.md`, `vertical/PROMPTS.md`, `vertical/CHECKS-REPORT.md`, `vertical/TYPECHECK.md`, `vertical/BUILD-PROMPT.md`, `vertical/beat_sheet.json`

## Known caveats for Bear's review

- The outro card (`ClaudeTitleOutro` / `ClaudeTitleOutro916`) hardcodes the
  `@NikBearBrown` handle in the shipped component and cannot be overridden by
  props. Matches the precedent set by every prior shipped Brutalist episode
  (setup, doctor, approvals, ...); if HAI wants the handle swapped on this
  card, a native isolated-toolkit variant would be the follow-up.
- Motion histogram lands at 7/12 code-cascade beats — the compiler warns
  above its ~40% pantry cap. Intentional for a command teardown; each code
  beat teaches a distinct source range (shim, lifecycle, sandbox, `--dry`,
  `--status`, `verify_film`, failure). Not a regression.
- Portrait BLUF beat (B01) required the BrutalistHesitantWriter portrait
  scale patch to be applied in the isolated toolkit; the live component was
  left untouched. Recipe used: fontSize 155 / lineSpacing 2.2, 5 lines,
  single-word trigger swap `fellows → workers`.
- Legacy `scripts/type_check.py`, `runtime/design/ILLUSTRATIONS.md` and
  `skills/make/kerning/` are absent from this toolkit snapshot. Substituted
  with image-Read visual review — see the two TYPECHECK.md files.

Gate V (final_frame_check.py) returned 0 BLOCKER / 0 MAJOR on both aspects.
Audio decodes at mean -27 dB / peak -2.7 dB on both files.

## Re-verification note (run_id 5e962a94ab5148acb858601a14ef0891 · 2026-09-13)

Source_sha256 changed (repoloop.sh comment header expanded; worker_settings()
gained autoAllowBashIfSandboxed, denyRead, network sections; REPOLOOP-PROMPT.md
refreshed). Beat_sheet.json updated with new run_id and corrected B02/B04 code
props. Existing MP4 exports unchanged and still pass all gates. B02/B04 clips
show the prior-render code snapshots — functionally accurate, slight cosmetic
lag vs. new comment header; browser rendering was blocked by the Mach-port
sandbox. VISUAL-REVIEW.json updated on both aspects.
