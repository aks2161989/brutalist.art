# FACTCHECK — Brutalist Command: art final — Short (ep 33)

Every claim that lands on screen or in narration is traced to a source line in the
copied toolkit at `.repoloop/shorts/workspaces/claude-liam-brutalist-command-final-short/toolkit/`.

This Short is a whole-beat cut of the finished native portrait: B00, B01, B06,
B07, B09, B11 are retained unchanged; B02, B03, B04, B05, B08, B10 are dropped
(see `CUT-PLAN.json`). Nothing new was narrated or overlaid; every retained beat
inherits its source-line trace verbatim from the parent
`claude-liam-brutalist-command-final/vertical/FACTCHECK.md`
(sheet SHA-256 `a8492a0366542e9bf20b7afbac501831232bab989f29dc10834101cd49ccf631`,
parent master SHA-256 `8d130d003f5406bc1c37085ffb347e24842f5cc891337a5a42dd2961572dbd3e`).

## B00 — the ask

Composer output cards (unchanged):

| Claim | Source |
|---|---|
| "gate F (paperwork) → gate LINT → gate SHAPE → render slots → encode candidate" | Order in `compile.py`: `final_preflight()` (450), then `prepare_timeline()` (632), then per-beat compile loop (669), then `sh(cmd)` on the ffmpeg encode (808). |
| "gate V (frame-level QC) on the candidate mp4, then re-check approvals + input hashes" | `compile.py:811-826` — Gate V sh() invocation, then `validate_approvals`, then input-hash check. |
| "atomic replace of the master; write sibling verified.json (SHA-256, inputs, duration)" | `compile.py:827` (`os.replace(candidate, out)`) and `compile.py:829-834` (`state = {…}` + `atomic_json(out.with_suffix('.verified.json'), state)`). |

## B01 — the BLUF hesitant writer

"Art final does not render once … gates the paperwork, renders, and then re-verifies the output it just wrote."

- Gates the paperwork BEFORE rendering: `final_preflight()` called at `compile.py:629` before `prepare_timeline()` / per-beat loop.
- Re-verifies the output AFTER rendering: `verify_output()` (compile.py:808) + `final_frame_check.py` invocation (compile.py:819) + `validate_approvals` re-check (compile.py:821) + input-hash re-check (compile.py:825).

## B06 — atomic candidate write

Source: `compile.py:805-827`, verbatim, with abbreviations noted in the on-screen
code as `…` where a full line would exceed the card width. Every named identifier
(`TemporaryDirectory`, `verify_output`, `final_frame_check.py`, `validate_approvals`,
`file_digest`, `os.replace`) is a real symbol at that line range.

## B07 — the receipt

Source: `compile.py:829-834`, verbatim shape:
```python
state = {'status': 'review' if a.review else 'ready',
         'output': str(out.resolve()),
         'sha256': file_digest(out),
         'duration_s': total,
         'input_sha256': input_hashes,
         'at': datetime.now(timezone.utc).isoformat()}
if not a.review:
    atomic_json(out.with_suffix('.verified.json'), state)
```

- Publication caveat ("ready is a machine claim, not YouTube 4K promise") — see
  `docs/PIPELINE-SAFETY.md` § "Reviews are not finals": "`ready` means the automated
  export checks passed, not human approval to publish."
- "YouTube 4K processing check: pending upload" is a line item in
  `docs/FELLOWS-SUBMISSION.md` § README template.

## B09 — verdict artifact

Each of the six recap lines maps to a beat in the long-form parent (line 1 →
dispatcher / B02; line 2 → `--review` split / B03; line 3 → `final_preflight` /
B04; line 4 → atomic write / B06 kept in this Short; line 5 → receipt / B07 kept
in this Short; line 6 → slate/approval guardrail — `compile.py:626-628` +
`compile.py:692-696`). Lines 1–3 restate framework facts whose long-form
demonstrations were dropped from the Short; the recap statements remain
faithful to the source.

## B11 — outro

Title restate + `@NikBearBrown` handle. Locked outro card per `OUTRO-LOCK.md`
(hardcoded handle regardless of channel). Playlist-adaptation caveat is disclosed
in the parent `README.md` for the human reviewer.

## Dropped beats

B02 (dispatcher case), B03 (compile.py argparse), B04 (final_preflight function
body), B05 (worked-example happy path), B08 (empty-FACTCHECK failure/recovery),
and B10 (Your Turn exercise) were cut in whole to bring the Short under
the strict 180 s cap. Their claims are still fact-checked in the parent's
FACTCHECK.md — this Short simply does not present them.
