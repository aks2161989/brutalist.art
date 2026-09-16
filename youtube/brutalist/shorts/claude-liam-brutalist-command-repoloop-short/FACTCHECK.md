# FACTCHECK — Brutalist Command: repoloop.sh — Short

Inherits the parent vertical reel's factcheck for every kept beat's spoken
narration and on-screen text. This Short's authoring made no new claims;
the six retained beats (B00, B01, B05, B09, B10, B11) preserve their parent
props and narration byte-for-byte.

Sources (from parent SOURCE-SNAPSHOT.json, captured 2026-09-10T04:28:37):

- `repoloop.sh` — `2d10a246b7bbf5b52abecaaa668fc6f065d1ff937e8492be8054654b631477a0`
- `runtime/scripts/repoloop.py` — `7b82920a93a41eafffd3ddf1c5e62c56d8a79b24576cbc3e06ed9c71dd3020f0`
- `REPOLOOP-PROMPT.md` — `abf55bdc729a9c30216e4375dff0c62b4bf5af4c717ad28be69709de64d5bc97`

## Beat-level checks (Short cut only)

### B00 — cold open ask
- "One fresh Claude subprocess per film, serial" — verified in
  `build_one()` (`repoloop.py:504-568`, `run_process()` → `subprocess.Popen`
  once per item) under `exclusive_lock(state/'worker.lock')`
  (`repoloop.py:662`). No thread pool.
- "sandboxed writes; ANTHROPIC_* env vars stripped" — verified in
  `worker_environment()` (`repoloop.py:268-280`).
- "verify_film() is the fail-closed gate" — verified in `verify_film()`
  (`repoloop.py:396-483`), invoked from `build_one()` (`repoloop.py:564`).

### B01 — BLUF misconception
- Corrected sentence "repoloop.sh is not a render loop. It spawns
  workers." — verified: `repoloop.sh` is a 10-line shim, its only Python
  is `runtime/scripts/repoloop.py`, which spawns `claude -p PROMPT …`
  subprocesses; rendering happens inside those subprocesses, not in
  `repoloop.sh` itself.
- "One Claude subprocess per film, one queue, one lock" — verified via
  `exclusive_lock(state/'worker.lock')` at `repoloop.py:662`.

### B05 — `--dry` output
- The on-screen block is a lightly-abridged VERBATIM copy of the parent
  reel's `demo/RUN-LOG.txt` `--dry` output. "56 films" is the count
  printed at the bottom of that block.

### B09 — verdict lines
- Each of the six lines names a real function/step in the sources. Where
  the Short drops the deep-dive beats (B02, B03, B04, B07), the verdict's
  one-line-per-phase description remains factually complete and
  self-referential:
  - "shim — 3 bash lines" — `repoloop.sh:7-9`.
  - "discover() — inventory derived from the toolkit itself" —
    `repoloop.py:26-33, 75-79, 81-95, 96-98, 101-111`.
  - "merge_queue() — source/feedback change ⇒ pending, old renders
    preserved" — `repoloop.py:186-206`.
  - "snapshot_toolkit() — copies runtime + skills + brands + docs" —
    `repoloop.py:snapshot_toolkit()`; baseline hash in each workspace's
    `toolkit-baseline.json` (see this Short's parent for one such file).
  - "worker_settings() + spawn — sandboxed, ANTHROPIC_* stripped, deny
    git push/gh/curl/wget/ssh" — `repoloop.py:333-346` and `:270-273`.
  - "verify_film() — fail-closed shape + ffprobe + audio + AI
    visual-review gate; never publishes" — `repoloop.py:396-483`; the
    toolkit CLAUDE.md rule 5 ("Never publish — render instead") is the
    corroborating no-upload contract, and no upload code path exists in
    `repoloop.py`.

### B10 — Your Turn prompt
- Every action in the prompt is safe (`--dry`, `--status`, code reading
  only). The forbidden verbs (`--once`, `--forever`, `--start`, `--stop`)
  are named in the prompt so the viewer's Claude session cannot
  accidentally start the loop.
- "merge_queue()'s feedback_sha256 check pushes an edited FEEDBACK.md
  back to status='pending'" — verified in `feedback_digest()` /
  `merge_queue()` at `repoloop.py:182-183` and `:193-198`.

### B11 — outro
- Title restated exactly: "Brutalist Command: repoloop.sh." —
  ClaudeTitleOutro916 per OUTRO-LOCK.md.
- Handle: hardcoded `@NikBearBrown` inside the component (locked). The
  narration says `@HumanitariansAI` because the playlist channel is HAI.
  Both are correct; the mismatch is flagged in README.md for Bear
  before publication.

## Cross-checks against REPOLOOP-SHORTS-PROMPT.md and the SHORTS LAW

- **Strictly under 3:00:** planned total 93.83s / 1:33.8; final measured
  ffprobe duration recorded in CHECKS-REPORT.md after compile.
- **Cut-first, no rewrite:** `strategy: whole-beat-cut` in CUT-PLAN.json.
  No narration was rewritten; no audio was regenerated; no visuals were
  re-rendered. The parent vertical reel is untouched.
- **Voice / captions / paid API / publish:** kokoro `am_onyx` throughout;
  `captions: false`; no paid-API calls; no upload; no `git push`.
- **Independent copies:** shorts.py `copy_asset()` used for every media,
  mp3 and doc — no symlinks or hardlinks. Verified via
  `find … -type l` (0 results) in CHECKS-REPORT.md.
- **≥ 3 beats and shape gates (Short profile):** 6 beats; first beat
  starts with `ClaudeComposerAsk916`; second beat is
  `BrutalistHesitantWriter916`; penultimate greeting `Your Turn` on
  `ClaudeComposerAsk916`; outro `ClaudeTitleOutro916`.
- **Coherence with dropped beats:** the Short's narration does NOT
  reference a "next slide", a numbered walkthrough continuing off-screen,
  or any code beat that was cut. B09's verdict is self-contained.

## Not falsified in this Short (belongs to the long)

The Short does not narrate line-level details of the shim body, the
`discover/merge_queue/build_one` sequence, the `worker_settings` allow/deny
list, the live `--status` block for THIS reel, the full `verify_film` guard
list, or the recovery worked example. Those beats and their factchecks live
in the parent vertical reel's FACTCHECK.md, cited above.

Nothing else to falsify.
