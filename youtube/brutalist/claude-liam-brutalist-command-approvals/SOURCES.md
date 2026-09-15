# SOURCES — Brutalist Command: art approvals

Primary sources for this episode (this-invocation SHA-256):

- `art` — `9bb77a7c84701d23ab6e73f0a4f48592f17748ffad2c7114b62687bb7f97d0e9`
  - Dispatcher case for `approvals` at lines 87-89: `exec python3 "$ART_HOME/runtime/scripts/build_safety.py" "$@"`.
  - `--help` block at lines 15-16: `./art approvals <reel> --fingerprints  inspect human-review subjects (never signs)`.
- `runtime/scripts/build_safety.py` — `479e167ffc80c4a2c235b425149b3922fd96a2e7388a40636f2dfa63b56015bf`
  - `main()` at lines 228-238 — the argparse surface, the two verbs.
  - `approval_subjects()` at lines 123-135 — the fingerprint computation (voice + professor_notes).
  - `validate_approvals()` at lines 138-166 — the five-field record contract and the fellows-narrator preflight.
  - `is_fellows()` at lines 86-90 — the profile check that arms the voice gate.
  - `feedback_beats()` at lines 107-112 — the beat scan that arms the professor_notes gate.
  - `digest()` + `file_digest()` at lines 22-32 — deterministic SHA-256 over sorted JSON / streamed bytes.

Read-only example leads (SHA-256 confirmed against BRIEF.md; used as staging references only, never re-published):

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22` — the fellow-facing setup arc (approve, don't type). Adopted stance: fellows already have Claude Code; this reel teaches the audit verb, not the setup.
- `yatra-r/2026-09-03-this-week-gordy/beat_sheet.json` — `7e3ea1f61c421e605e583be9b2a7b5f554aa8cadfb6e14dabaee66f471856083` — the weekly cadence and audience posture. Correction: this episode is a command teardown for Brutalist users, not a project update.

Demo evidence (this workstation, this session):

- `demo/RUN-LOG.txt` — verbatim stdout/stderr from five `./art approvals` invocations against three throwaway fixtures under `/tmp/claude-501/approvals-demo-*/`. Every code block on screen is drawn from this file.
- Fixtures: `approvals-demo-empty/` (no beat_sheet), `approvals-demo-command/` (kind=command, no gates), `approvals-demo-fellows/` (profile=fellows + a `requires_approval: professor_notes` beat + a `source_report` beat).

Toolkit revision: `ba2d0e0f043f5b3b35a50d336e0fc66fbfecfc0c` (recorded in `SOURCE-SNAPSHOT.json`).

No paid API, no upload, no external network calls. All demos ran locally.
