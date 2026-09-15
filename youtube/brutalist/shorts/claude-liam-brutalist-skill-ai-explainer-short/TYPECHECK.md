# TYPECHECK — Short cut

No source code was authored or modified in this Short build. The Short is a
cut+concat derivative of the parent's finished portrait media; the runtime
scripts invoked (`runtime/scripts/shorts.py`, `runtime/scripts/compile.py`,
`runtime/scripts/build_safety.py`) were used **unmodified** from the isolated
toolkit copy at
`.repoloop/shorts/workspaces/claude-liam-brutalist-skill-ai-explainer-short/toolkit`.

## Schema validations that ran

- `build_safety.validate_project(sheet)` — invoked by both `shorts.py` (twice: once on the parent sheet, once on the derivative sheet before `atomic_json`) and by `compile.py` (on the derivative sheet at compile entry). Passed both times: nonempty beats list; every `beat_id` matches `[A-Z][A-Z0-9_]*` and is unique; every beat/shot is an object; slug is a filename-safe string; `voice` and `voice_kokoro` agree (`am_onyx`).
- `build_safety.validate_approvals(folder, sheet)` — invoked by `compile.py` on entry and again after the final-frame check. Passed: this Short is not a fellows profile and has no `professor_notes`/`FEEDBACK` beats, so no `approval_subjects` are required. `metadata.approvals = {}` is the correct empty-object state.
- `build_safety.require_short_duration(...)` — invoked at three points:
  1. `shorts.py` at plan time on the sum of retained beats' durations (147.916s).
  2. `compile.py` on the measured timeline (147.916s).
  3. `compile.py::verify_output` on the encoded container duration (147.916667s) and each stream duration (video 147.916667s, audio 147.916000s).
  All three checks accept the value as strictly less than 180.0.

## Preflight gates

`compile.py::final_preflight` (fires on non-review runs — this run was a final, no `--review`):

- `require_paperwork(folder)` — verified `FACTCHECK.md`, `SHOTLIST.md`, and `PROMPTS.md` all exist and are non-empty.
- `runtime/qc/beat_lint.py` `<folder>/beat_sheet.json` — passed silently (exit 0).
- `runtime/qc/gate_shape.py` `<folder>/beat_sheet.json` — passed silently (exit 0).
- `runtime/qc/final_frame_check.py <folder> --mp4 <candidate> --sheet <resolved-sheet>` — passed silently (exit 0). This is the compiler's Gate V.
- Short-specific: `metadata.short_validation.status == "ready"` — satisfied at cut time by `shorts.py`.

## Post-render integrity checks

- `verify_output` decoded the full candidate MP4 (`ffmpeg -xerror -f null -`) with no errors and verified both `video` and `audio` codec_type streams are present.
- `require_audible(candidate, 'Compiled output')` measured `max_volume > -80 dB`.
- After the frame gate, the beat sheet was re-read and compared byte-for-byte against the snapshot taken at compile entry; any mid-encode edit would have raised `BuildError('Beat sheet changed during rendering; rebuild the new revision')`. No such error was raised.
- Every input media file's SHA-256 was re-hashed at the end and compared against the hash captured at compile entry; any mid-encode replacement would have raised `BuildError('Source media or narration changed during rendering; rebuild the new revision')`. No such error was raised.
- `atomic_json(candidate.with_suffix('.verified.json'), state)` wrote the audit record.

## Runtime observations

- 9/9 beats resolved to `VIDEO` status via `resolve_slot(folder, bid)`. Zero slates. The master-law check `slated and not a.review and not a.allow_slates` never triggered.
- Motion histogram: `reveal:6  type-on:2  hold:1` — `compile.py` warned that `reveal` carries 66% (over the ~40% MOTION.md pantry cap). This is an inherited property of the parent's scene mix (all three MECHANISM beats + the two FRAMEWORK/VERDICT beats + tell use `reveal`), not a Short-specific regression, and is not a blocking gate.
- Skin lint (advisory only) emitted the two warnings the parent's build stamp already carried:
  - `B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk`
  - `B10: palette=claude but the outro is 'ClaudeTitleOutroHAI916' — OUTRO LAW wants ClaudeTitleOutro`
  Both are the parent's deliberate HAI-channel substitutions and are not introduced by this Short.

## No type errors, no lint failures, no runtime errors

Both `shorts.py` and `compile.py` returned status 0. The `.verified.json`
record was written. No `BuildError`, `ApprovalError`, `OSError`,
`subprocess.SubprocessError`, or `TypeError` was raised during either
invocation. The final gate output the compile stamp
`build stamp → beat_sheet.json (9/9 filled)`.
