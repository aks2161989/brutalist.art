# FACTCHECK — Brutalist Command: art final (ep 33)

Every claim that lands on screen or in narration is traced to a source line in the
copied toolkit at `.repoloop/workspaces/claude-liam-brutalist-command-final/toolkit/`
(source_sha256 `15dc70372375121fb4a194daa1bac7042ceb4f232345e27a08a353cd14129a10` for
the two named source files, per `SOURCE-SNAPSHOT.json`).

## B00 — the ask

Ask lines (composer output cards):

| Claim | Source |
|---|---|
| "gate F (paperwork) → gate LINT → gate SHAPE → render slots → encode candidate" | Order in `compile.py`: `final_preflight()` (450), then `prepare_timeline()` (632), then per-beat compile loop (669), then `sh(cmd)` on the ffmpeg encode (808). |
| "gate V (frame-level QC) on the candidate mp4, then re-check approvals + input hashes" | `compile.py:811-826` — Gate V sh() invocation, then `validate_approvals`, then input-hash check. |
| "atomic replace of the master; write sibling verified.json (SHA-256, inputs, duration)" | `compile.py:827` (`os.replace(candidate, out)`) and `compile.py:829-834` (`state = {…}` + `atomic_json(out.with_suffix('.verified.json'), state)`). |

## B01 — the BLUF hesitant writer

"Art final does not render once … gates the paperwork, renders, and then re-verifies the output it just wrote."

- Gates the paperwork BEFORE rendering: `final_preflight()` called at `compile.py:629` before `prepare_timeline()` / per-beat loop.
- Re-verifies the output AFTER rendering: `verify_output()` (compile.py:808) + `final_frame_check.py` invocation (compile.py:819) + `validate_approvals` re-check (compile.py:821) + input-hash re-check (compile.py:825).

## B02 — the dispatcher case

Source: the top-level `art` bash dispatcher (SHA-256 `9bb77a7c84701d23ab6e73f0a4f48592f17748ffad2c7114b62687bb7f97d0e9`).

Verbatim from `art:90-95`:
```
  final)
    case " $* " in
      *" --height "*|*" --height="*) exec python3 "$ART_HOME/runtime/scripts/compile.py" "$@" ;;
      *)              exec python3 "$ART_HOME/runtime/scripts/compile.py" "$@" --height 2160 ;;
    esac
    ;;
```

- Exact string match — no glob alias. See dispatcher table at `art:37-116`; only `"final"` matches.
- `--height 2160` default when the user did not pass one — cross-referenced against the `--help` output at `art:2-18`: "verified master — no review label (→ `<slug>.mp4`)".

## B03 — compile.py argparse

Source: `compile.py:593-609`, verbatim in the beat.

- Every flag on-screen exists in `main()`. `--allow-slates` help text: "legacy review-only option; final masters always reject slates" (compile.py:600).
- `--out` fallback chain claim in the code comment mirrors `compile.py:719-736` (`--out DIR` > `$ART_OUT` > `<toolkit>/renders/`).

## B04 — final_preflight

Source: `compile.py:451-463`, verbatim on-screen.

- `require_paperwork(folder)` — the FACTCHECK/SHOTLIST/PROMPTS triad claim is verified in `build_safety.py:PAPERWORK_FILES`; the empty-FACTCHECK failure demo in B08 exercises this same check.
- `beat_lint.py` and `gate_shape.py` exist in `runtime/qc/` and are called as subprocesses (`sh([sys.executable, gate, folder / sheet_name])`).

## B05 — worked example: the demo

All stdout lines in the code card are verbatim from `demo/RUN-LOG.txt` § 2. The
`sha256` and `input_sha256` fields in the shown JSON are the actual values written
to `/tmp/claude-501/art-final-demo/exports/art-final-demo.verified.json` during
this build session (elided in the on-screen render to fit the card width;
full values in RUN-LOG.txt and reproduced as-is).

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

## B08 — failure and recovery

Verbatim from `demo/RUN-LOG.txt` § 3. Failure text matches
`build_safety.py:require_paperwork()`'s error string
(`"GATE F: missing or empty FACTCHECK.md; review is allowed, final is blocked"`).
The SHA-256 identity of the mp4 before and after the refusal is captured in the
run log as observed identical `5910ade9793c943b2…3403eb5eecfae93e3`.

## B09 — verdict artifact

Each of the six lines maps to a beat above (B02→line 1, B03→line 2, B04→line 3,
B06→line 4, B07→line 5, and the slate/`--allow-slates` guardrail is
`compile.py:626-628` + `compile.py:692-696`).

## B10 — Your Turn

The prompt is a concrete, paste-ready 5-step verification task. It does not
promise any Claude behaviour; the "grading" lines describe what the RUN-LOG
already showed (verified.json.sha256 == shasum -a 256 of the mp4).

## B11 — outro

Title restate + `@NikBearBrown` handle. Locked outro card per `OUTRO-LOCK.md`
(hardcoded handle regardless of channel). Playlist-adaptation caveat is disclosed
in `README.md` for the human reviewer.
