# FACTCHECK — Brutalist Command: art approvals — Short (9:16)

Every claim the Short's retained narration makes, mapped to source evidence. Dropped beats (B02/B04/B07/B10) are not referenced on screen and are not fact-checked here; the parent long carries their evidence.

## B00 — Cold open

- **"Before I sign anything on a fellows reel, show me exactly what I would be signing. Do not sign it for me. Just print the fingerprints."**
  Source: `runtime/scripts/build_safety.py:231` — `ap.add_argument('--fingerprints', action='store_true', help='print subjects for human review; never signs')`.
  Source: `main()` at `build_safety.py:234-238` — either `approval_subjects()` (print) or `validate_approvals()` (check). Neither writes to the sheet.

## B01 — BLUF

- **"Art approvals does not sign approvals. It inspects the subjects a human is about to sign."**
  Source: `build_safety.py:123-135` `approval_subjects()` returns `{'voice': {...}, 'professor_notes': {...}}` derived from the beat sheet — the *subjects* to sign, not the *records*.
- **"Two verbs. Fingerprints prints. Default validates."**
  Source: `build_safety.py:234-238` — the two-branch `main()` body.
- **"The pen never leaves the human's hand."**
  Source: `build_safety.py:160` — `reviewer_type != 'human'` fails. Nothing in the file mutates `metadata.approvals`; the auditor is read-only.

## B03 — Framework · two verbs

- **"Point it at a reel folder."**
  Source: `build_safety.py:230` — `ap.add_argument('reel', type=Path)`.
- **"--fingerprints prints the subjects — nothing else."**
  Source: `build_safety.py:235-236` — `if a.fingerprints: print(json.dumps(approval_subjects(a.reel, sheet), indent=2))`.
- **"Leave the flag off, and it validates the pasted approvals against those subjects."**
  Source: `build_safety.py:237-238` — `else: validate_approvals(a.reel, sheet)`.
- **"Either way, the file changes zero."**
  Source: no `open(..., 'w')` or `write_text()` calls in either branch.
- **"Approvals live in `metadata.approvals` in the beat sheet, written by a human editor. The command is the auditor."**
  Source: `build_safety.py:148` — `approvals = md.get('approvals') or {}`.

## B05 — Worked example · fellows reel + --fingerprints

- **"Profile fellows, voice policy persistent, and a feedback beat marked professor_notes."**
  Source: `build_safety.py:86-90` `is_fellows()` returns True when `metadata.profile` (or `skill`/`kind`) equals `fellows`, or when `voice_policy == 'persistent-fellow-selected'`.
  Source: `build_safety.py:107-112` `feedback_beats()` matches `requires_approval == 'professor_notes'` or the specific feedback act strings.
- **"Two gates arm: voice, and professor notes."**
  Source: `approval_subjects()` at `build_safety.py:123-135` — `is_fellows()` populates `result['voice']`, `feedback_beats()` populates `result['professor_notes']`.
- **"Two subject blocks, each with a SHA-256."**
  Evidence: `demo/RUN-LOG.txt` section 3, verbatim JSON printed by the actual `--fingerprints` invocation against `/tmp/claude-501/approvals-demo-fellows/`.

## B06 — Mechanism · five-field record

- **"status = approved · reviewer_type = human · reviewed_by non-empty · reviewed_at ISO-8601 with timezone · every subject SHA verbatim from --fingerprints."**
  Source: `build_safety.py:155-164`:
  ```python
  try:
      date = datetime.fromisoformat(str(record.get('reviewed_at', '')).replace('Z', '+00:00'))
      dated = date.utcoffset() is not None
  except ValueError:
      dated = False
  if (record.get('status') != 'approved' or record.get('reviewer_type') != 'human'
          or not str(record.get('reviewed_by', '')).strip() or not dated
          or any(v is None or record.get(k) != v for k, v in expected.items())):
      raise ApprovalError(...)
  ```
- **"reviewer_type must be human — never AI."**
  Source: same conjunct — `!= 'human'` fails everything else, including `'ai'`.
- **"Miss one, mistype one, forget the timezone — the gate refuses."**
  Source: same conjunct + `datetime.fromisoformat(...).utcoffset() is not None`.

## B08 — Failure · stale approval

- **"Both approvals pasted, both gates green. Then B05 narration gets one extra sentence added — after the human signed. Re-run. The command refuses: GATE professor_notes: missing, pending or stale."**
  Evidence: `demo/RUN-LOG.txt` sections 4-5. Same fixture at `/tmp/claude-501/approvals-demo-fellows`, same approvals block, one word added to B05.narration_text. Output: `[safety] REFUSED: GATE professor_notes: missing, pending or stale human approval; inspect build_safety.py <reel> --fingerprints`.
- **"--fingerprints prints the new SHA."**
  Evidence: same log, section 5 tail. Re-running `--fingerprints` after the edit prints a new `narration_sha256` (the recomputed value from `digest()` at `build_safety.py:117`).
- **"The recovery is the same short loop: hand the new subjects to the human, get a fresh dated record, paste it in."**
  Source: the error message names `--fingerprints` explicitly (`build_safety.py:245-246`). That IS the intended recovery — the auditor tells the caller how to unstick itself.

## B09 — Verdict lines (each maps to a source above)

1. **"bare invocation — ./art approvals <reel> [--fingerprints]; wraps python3 runtime/scripts/build_safety.py $@"** → `art:87-89` (dispatcher case) + `build_safety.py:230-231` (argparse).
2. **"two verbs, neither signs"** → `build_safety.py:234-238`.
3. **"two gates, sheet-armed"** → `is_fellows()` + `feedback_beats()` at `build_safety.py:86-112`.
4. **"five fields per record"** → `build_safety.py:155-164`.
5. **"fingerprints from the source every run — pasted SHAs are the human's; recomputed SHAs are the truth"** → `approval_subjects()` at `build_safety.py:123-135`, called on every invocation.
6. **"no aliases; changes zero files — the pen never leaves the human. Downstream renderers call the same validator, so a pending signature never ships."** → `art:37-116` (only `approvals)` pattern dispatches to this file) + the same `validate_approvals()` is called from `remotion_scenes.py:176` and `compile.py`.

## B11 — Outro

- **"Brutalist Command: art approvals. Liam, in for Bear, for at Humanitarians A I."**
  Register/persona restated. `@NikBearBrown` handle is hardcoded per `OUTRO-LOCK.md`; this is called out to the human reviewer in the parent `README.md` — not a silent adaptation.

## Corrections & caveats

- The verdict claim "a fellows reel with a pending signature never ships" is not enforced by `art approvals` alone; it is enforced by every downstream that calls `validate_approvals()`. The narration credits the gate to the *validator*, not to this dispatcher alone.
- Playlist adaptation for @HumanitariansAI: composer folder chip reads `@HumanitariansAI`. Outro card is the shipped `ClaudeTitleOutro916`, whose handle is hardcoded to `@NikBearBrown` per `OUTRO-LOCK.md`. Flagged for the human reviewer.
- No claim in the Short depends on the dropped beats. B03 references "point it at a reel folder" without needing B02's dispatcher visual; B08's stale message is meaningful without B07's `digest()` body because B06 already establishes that every subject SHA must be verbatim from `--fingerprints`.
