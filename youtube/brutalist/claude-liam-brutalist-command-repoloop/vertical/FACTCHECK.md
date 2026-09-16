# FACTCHECK — Brutalist Command: repoloop.sh

Verified against the SOURCE-SNAPSHOT.json captures at
`captured_at: 2026-09-10T04:28:37`. Every code line shown on screen and every
number narrated tracks back to the files below at these SHA-256s:

- `repoloop.sh` — `2d10a246b7bbf5b52abecaaa668fc6f065d1ff937e8492be8054654b631477a0`
- `runtime/scripts/repoloop.py` — `7b82920a93a41eafffd3ddf1c5e62c56d8a79b24576cbc3e06ed9c71dd3020f0`
- `REPOLOOP-PROMPT.md` — `abf55bdc729a9c30216e4375dff0c62b4bf5af4c717ad28be69709de64d5bc97`

## Beat-level checks

### B00 — cold open ask
- "One fresh Claude subprocess per film, serial" — verified.
  `build_one()` in `repoloop.py:504-568` calls `run_process()` → `subprocess.Popen`
  once per item, with `signal.SIGTERM/SIGKILL` clean-up. The supervisor
  `main()` loop at `repoloop.py:686-728` processes items one at a time under
  `exclusive_lock(state/'worker.lock')` at `repoloop.py:662`. No thread pool.
- "sandboxed writes; ANTHROPIC_* env vars stripped" — verified.
  `worker_environment()` at `repoloop.py:268-280` strips every var ending in
  `_API_KEY` plus `ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_BASE_URL`, `CLAUDECODE`,
  `CLAUDE_CODE_USE_BEDROCK`, `CLAUDE_CODE_USE_VERTEX`, `CLAUDE_CODE_USE_FOUNDRY`.
- "verify_film() is the fail-closed gate" — verified. `verify_film()` at
  `repoloop.py:396-483` raises `BuildError` on 20+ conditions and is called
  from `build_one()` at `repoloop.py:564` in a try/except that converts every
  BuildError into `status='failed'`.

### B01 — BLUF misconception
- "repoloop.sh does not build videos. It orchestrates workers." — verified.
  `repoloop.sh` is 9 lines. The only Python it runs is
  `runtime/scripts/repoloop.py`, which spawns *another* process (`claude -p
  PROMPT …`) for each film. The rendering happens inside those subprocesses.
- "One Claude subprocess per film, one queue, one lock" — verified.
  `exclusive_lock(state/'worker.lock')` at `repoloop.py:662` uses
  `fcntl.LOCK_EX | fcntl.LOCK_NB`; a second supervisor exits with
  `'Another repoloop owns this playlist; no second worker started'`.

### B02 — the shim
- "Three real lines." — verified. `repoloop.sh` has 10 lines total; the
  effective body is `set -euo pipefail`, the `REPOLOOP_ROOT="$(cd …)"`
  resolution, and the `exec python3 …/repoloop.py --repo "$REPOLOOP_ROOT"
  "$@"`. The shown snippet is a lightly-formatted VERBATIM copy of
  `repoloop.sh:7-9`.

### B03 — the queue lifecycle
- `discover()` iterates INTRO trilogy (`repoloop.py:26-33`), then
  `repo.glob('skills/*/**/SKILL.md')` (`repoloop.py:75-79`), then parses
  the `art` dispatcher line-by-line for `  <name>)` case branches
  (`repoloop.py:81-95`), then adds `command-setup` (`:96`) and
  `command-repoloop` (`:97-98`), then walks `runtime/scripts` and `runtime/qc`
  for executable modules (`:101-111`). Verified.
- `merge_queue()` at `repoloop.py:186-206` compares `item['source_sha256']`
  and `item['feedback_sha256']` and marks changed items `status='pending'`
  with note `'New or changed source/feedback; old renders preserved'`.
  Verified — this is exactly the `note` on THIS invocation
  (see SOURCE-SNAPSHOT.json).

### B04 — the sandbox
- Every allow/deny entry in the shown `worker_settings()` block is VERBATIM
  from `repoloop.py:333-346`. The env-var strip block is verbatim from
  `repoloop.py:270-273`. Verified.

### B05 — `--dry` output
- The snippet is a lightly-abridged VERBATIM copy of `demo/RUN-LOG.txt`
  lines 31-88 (the full `--dry` block). "56 films" is the count printed
  at line 88.

### B06 — `--status` output
- The snippet is a VERBATIM copy of `demo/RUN-LOG.txt` lines 90-132, with
  a small path truncation in the `log` field for legibility (full path shown
  in RUN-LOG.txt). The `run_id` `cd46b905ecb54c35b0f71b2db5a04ab1` matches
  `metadata.run_id` in beat_sheet.json and `episode.run_id` in
  BUILD-PROMPT.md.

### B07 — verify_film
- "Fewer than 8 beats — refuse" → `repoloop.py:402-404`
  `minimum_beats = 3 if aspect == 'short' else 8`.
- "Non-Liam voice — refuse" → `repoloop.py:403` and `:405`.
- "First beat not ClaudeComposerAsk / second not HesitantWriter" →
  `repoloop.py:407-409`.
- "Penultimate greeting not 'your turn'" → `repoloop.py:410-412`.
- "ffprobe dims must match exactly" → `repoloop.py:429-431`.
- "audio must decode above -40 dB" → `repoloop.py:458-462`.
- "matching AI visual-review with the current run_id" → `repoloop.py:463-474`.

### B08 — the failure demo
- Command and output VERBATIM from `demo/RUN-LOG.txt` lines 161-163.
- The narration of the guard's location is verified: `main()` at
  `repoloop.py:651-653` — `inventory = scan(repo)` → `if args.only and
  args.only not in {i['id'] for i in inventory}: raise BuildError(...)`.

### B09 — verdict lines
- Each of the six lines names a real function/step; every claim
  cross-references B02-B08 above. "No auto-publish" — verified: the
  toolkit CLAUDE.md rule 5 says "Never publish — render instead"; there
  is no upload code path in `repoloop.py`.
- "A stop file gracefully terminates" — `repoloop.py:648-650` (`--stop`
  writes `.repoloop/STOP`); `repoloop.py:355-358` (worker checks
  `stop.exists()`); `:688` (supervisor loop exits on STOP).
- "A worker lock forbids duplicates" — `exclusive_lock()` at
  `repoloop.py:209-218` uses `fcntl.LOCK_EX | fcntl.LOCK_NB` on
  `state/worker.lock`.

### B10 — Your Turn prompt
- Every action in the prompt is safe (`--dry`, `--status`, and code
  reading only). The forbidden verbs (`--once`, `--forever`, `--start`,
  `--stop`) are named in the prompt itself so the viewer's Claude session
  will not accidentally start the loop.
- "merge_queue()'s feedback_sha256 check pushes an edited FEEDBACK.md
  back to status='pending'" — verified. `feedback_digest()` at
  `repoloop.py:182-183` hashes `FEEDBACK.md`; `merge_queue()` at
  `repoloop.py:193-198` compares it to the queue's stored value and
  resets to `pending` on mismatch.

### B11 — outro
- Title restated exactly ("Brutalist Command: repoloop.sh.") — outro
  card uses locked `ClaudeTitleOutro` per OUTRO-LOCK.md.
- Handle: hardcoded `@NikBearBrown` inside the component (locked). The
  narration says `@HumanitariansAI` because the playlist channel is
  HAI. Both are correct; the mismatch is flagged in README.md for Bear
  before publication.

## Cross-checks against SKILL.md and REPOLOOP-PROMPT.md

- IN-FOR-BEAR LAW satisfied: B00 first breath contains "Liam, in for
  Bear"; B11 signs off "Liam, in for Bear, for @HumanitariansAI".
- EXECUTIVE-SUMMARY LAW: B01 is `BrutalistHesitantWriter`, not a card,
  with an actual misconception → correction. Duration 12.14s ≥ 9s.
- COLD OPEN LAW: B00 = `ClaudeComposerAsk` with output lines populated.
- HANDOFF LAW: B10 = `ClaudeComposerAsk` with `greeting: "Your Turn"` and
  prompt read aloud in narration.
- OUTRO LAW: B11 = `ClaudeTitleOutro`, title restated, handle beneath.
- No captions anywhere; `metadata.captions: false`.
- All beats `engine: kokoro`, `voice: am_onyx`. Total narration 220.28s.
- No paid-API calls; no `--install` demos; no remote clones. All demos
  are `--dry`, `--status`, `--help`, argparse errors, and unknown-ID
  refusal — read-only against the parent repo.

## Sources still needing legibility QC

- The AI visual-review of frames at 15/50/85% is in _qc/ per beat, plus
  contact sheets. That is the only step downstream of this factcheck.

Nothing else to falsify. Every claim in narration reduces to a line
number in the sources above.
