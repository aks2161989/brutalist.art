# FACTCHECK — Brutalist Command: art approvals

Every claim the narration makes, mapped to source evidence.

## B00 — Cold open

- **"art approvals prints fingerprints; it does not sign."**
  Source: `art:16`  `./art approvals <reel> --fingerprints  inspect human-review subjects (never signs)`.
  Source: `build_safety.py:231` — `ap.add_argument('--fingerprints', action='store_true', help='print subjects for human review; never signs')`.
  Also: `main()` at `build_safety.py:234-238` calls either `approval_subjects()` (print) or `validate_approvals()` (check). Neither mutates the sheet.

## B01 — BLUF

- **"It inspects the subjects a human is about to sign."**
  Source: `build_safety.py:123-135` `approval_subjects()` returns `{'voice': {...}, 'professor_notes': {...}}` derived from the beat sheet — the *subjects*, not the *records*.

## B02 — Framework · dispatcher

- **"Three lines. `approvals)` → `exec python3 build_safety.py`."**
  Source: `art:87-89`
  ```
  approvals)
    exec python3 "$ART_HOME/runtime/scripts/build_safety.py" "$@"
    ;;
  ```
- **"No aliases; only the exact string `approvals` matches."**
  Source: the `case "$cmd"` block in `art:37-116` — `approvals)` is the only pattern that dispatches to `build_safety.py`. BRIEF.md aliases list is `["approvals"]` — same word, no other spellings.

## B03 — Framework 2 · two verbs

- **"Point it at a reel folder."**
  Source: `build_safety.py:230` — `ap.add_argument('reel', type=Path)`.
- **"`--fingerprints` prints the subjects."**
  Source: `build_safety.py:235-236` — `if a.fingerprints: print(json.dumps(approval_subjects(...), indent=2))`.
- **"No flag → validates the pasted approvals."**
  Source: `build_safety.py:237-238` — `else: validate_approvals(a.reel, sheet)`.
- **"Approvals live in `metadata.approvals` in the beat sheet."**
  Source: `build_safety.py:148` — `approvals = md.get('approvals') or {}`.

## B04 — Worked example 1 · plain command reel

- **"No gate armed → `{}` from `--fingerprints`."**
  Evidence: `demo/RUN-LOG.txt` section 2, verbatim. The fixture at `/tmp/claude-501/approvals-demo-command/beat_sheet.json` sets `kind: "command"` (not fellows) and has no `requires_approval` or feedback-act beat. `approval_subjects()` therefore skips both `is_fellows()` and `feedback_beats()` branches, returning `{}`.
- **"Default → exit 0 with no output."**
  Evidence: same file. `validate_approvals()` iterates the empty subjects dict; nothing to check. No print.

## B05 — Worked example 2 · fellows reel

- **"profile fellows arms the voice gate."**
  Source: `build_safety.py:86-90` `is_fellows()` returns True when `metadata.profile` (or `skill`/`kind`) equals `fellows`. Fixture uses `"profile": "fellows"` and `"kind": "fellows"`.
- **"A `requires_approval: professor_notes` beat arms the professor_notes gate."**
  Source: `build_safety.py:107-112` — `feedback_beats()` matches `requires_approval == 'professor_notes'` or specific act strings.
- **"Two subject blocks, each with a SHA-256."**
  Evidence: `demo/RUN-LOG.txt` section 3, verbatim JSON printed by `--fingerprints`.

## B06 — Mechanism · five fields

- **"status = approved · reviewer_type = human · reviewed_by non-empty · reviewed_at ISO with timezone · every subject SHA matches."**
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
  Five conjuncts — status, reviewer_type, reviewed_by, dated (with utcoffset), and every subject key equal to the recomputed value.
- **"reviewer_type must be `human` — never AI."**
  Source: same line. `!= 'human'` fails everything else, including `'ai'`.

## B07 — Mechanism · re-computed subjects

- **"The command recomputes SHAs from the sheet every run."**
  Source: `build_safety.py:126-134`. `approval_subjects()` calls `digest({'engine': 'kokoro', 'voice': default_voice(sheet)})` for the voice subject and `digest([...])` over the feedback-beat narration texts. `digest()` is `hashlib.sha256(json.dumps(..., sort_keys=True, ...).encode()).hexdigest()`.
- **"Doesn't trust the pasted SHAs."**
  Source: `build_safety.py:162` — the pasted `record.get(k)` is compared against the freshly recomputed `v` from `approval_subjects()`.

## B08 — Failure · stale approval

- **"Change B05 narration → recomputed narration_sha256 differs → GATE professor_notes: missing, pending or stale."**
  Evidence: `demo/RUN-LOG.txt` section 5. Same fixture, same approvals block, one word added to B05.narration_text. Output: `[safety] REFUSED: GATE professor_notes: missing, pending or stale human approval; inspect build_safety.py <reel> --fingerprints`.
- **"Recovery: re-run `--fingerprints`, get the fresh SHA, ask the human to re-sign."**
  Source: the error message itself refers the caller to `--fingerprints` — that IS the intended recovery.

## B09 — Verdict lines (each maps to a source line above)

1. "Five-field auditor" → `build_safety.py:155-164`.
2. "Two verbs, neither one signs" → `build_safety.py:231, 234-238`.
3. "Reads the sheet, decides which gates are armed" → `is_fellows()` + `feedback_beats()` at `build_safety.py:86-112`.
4. "Computes the subjects live" → `approval_subjects()` at `build_safety.py:123-135`.
5. "Either prints them or checks a pasted record against them" → `main()` branch at `build_safety.py:234-238`.
6. "Refuses on missing, wrong, or stale" → `ApprovalError` raise at `build_safety.py:163-164`, `[safety] REFUSED:` prefix at `build_safety.py:245`.
7. "A fellows reel with a pending signature never ships" → this refusal fires from every downstream that calls `validate_approvals()`, notably `remotion_scenes.py:176` and inside `compile.py` (which imports the same module). The gate stops the render pipeline, not just this command.

## B10 — Handoff prompt

- **"Copy the JSON into `metadata.approvals` as human review records."**
  Legal shape verified in fixture at `/tmp/claude-501/approvals-demo-fellows/beat_sheet.json` after the recovery step; the same file `art approvals` returns exit 0 on. Every field verified against `build_safety.py:155-164`.
- **"An agent must never fill in `reviewed_by`."**
  Source: `build_safety.py:160` — `reviewer_type != 'human'` fails. A machine that pastes `reviewer_type: 'human'` and a real name is forging a review — an explicit ban of the register, not of the file format.

## Corrections & caveats

- The "empty folder" fixture (RUN-LOG section 1) also refuses, but with a filesystem error, not an `ApprovalError`. That case is *not* used on screen — the reel's failure beat (B08) uses the stale-approval case because it is the specific refusal the command exists to make.
- The verdict claim "a fellows reel with a pending signature never ships" is not enforced by `art approvals` alone; it is enforced by every downstream that calls `validate_approvals()`. The narration credits the gate to the *validator*, not to this dispatcher alone.
- Playlist adaptation for @HumanitariansAI: composer folder chip reads `@HumanitariansAI`. Outro card is the shipped `ClaudeTitleOutro`, whose handle is hardcoded to `@NikBearBrown` per `OUTRO-LOCK.md` — this is called out for the human reviewer in `README.md` and the beat_sheet.json `metadata.note`. Not silently fixed; the lock is a project-wide rule.
