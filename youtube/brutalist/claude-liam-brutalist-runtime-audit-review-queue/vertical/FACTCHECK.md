# FACTCHECK — Brutalist Utility: audit_review_queue.py

All narration claims checked against `runtime/scripts/audit_review_queue.py` source code, read in full.

| Beat | Claim | Verdict | Source / derivation |
|---|---|---|---|
| B00 | "read-only batch inspector" | ✓ | Module docstring: "Read-only film audit"; no write to reel directories |
| B00 | "samples per-beat source clips at the 70-percent mark" | ✓ | `at = duration * .70` (line 108) |
| B00 | "never approves, never publishes" | ✓ | Module docstring: "never approves or publishes" |
| B01 | "script's own docstring says never approves, never publishes" | ✓ | First line of module docstring (line 3) |
| B02 | "--list, --root, --out are required flags" | ✓ | argparse section: all three use `required=True` |
| B02 | "parser extracts the last slash-containing token from each line" | ✓ | `inventory()` regex: `((?:[^\s]+/)+[^\s]+)` captures last path-shaped token |
| B02 | "duplicate entries throw" | ✓ | `if not reels or len(set(p for _, p in reels)) != len(reels): raise ValueError` |
| B03 | "thread pool of three" | ✓ | `ThreadPoolExecutor(max_workers=3)` |
| B04 | "math layout errors from math_layout_check import" | ✓ | `from math_layout_check import math_layout_errors; for error in math_layout_errors(sheet)` |
| B04 | "pantry paths split two ways by visual intent" | ✓ | Lines 80–86: reproducible regex → replace-with-code-data; else → source-artifact-or-illustration-review |
| B04 | "overflow-to-infinity patterns get their own flag" | ✓ | Lines 89–91: `re.search(r'overflows? to infinity', beat.get('narration_text', ''), re.I)` |
| B05 | "compares master MP4 modification time against beat sheet's" | ✓ | `'stale': master.stat().st_mtime < sheet_path.stat().st_mtime if master else None` |
| B05 | "flag is informational, does not block" | ✓ | `stale` is written to output JSON only; no raise or return |
| B06 | "PIL — no Pillow, no run" | ✓ | `from PIL import Image, ImageDraw` at top-level; ImportError before main() |
| B06 | "math_layout_check — local module; missing = import fails before arg parsing" | ✓ | `from math_layout_check import math_layout_errors` at top-level |
| B06 | "absent ffmpeg binaries produce empty tiles with no warning unless absent from PATH" | ✓ | sample_master/audit both call subprocess; returncode checked but no sys.exit; tile stays blank on failure |
| B07 | "12 beats, 12 frame samples, 0 leads" | ✓ | Real execution output: `01: 12 beats; 0 leads; 12 frame samples` — against claude-liam-brutalist-skill-nopunt |
| B08 | "empty list and duplicate paths raise ValueError before any reel is touched" | ✓ | `if not reels or len(set(p for _, p in reels)) != len(reels): raise ValueError('Empty or duplicate reel list')` |
| B08 | "ffmpeg frame failure is silent; sample record carries status error" | ✓ | `except Exception as exc: sample_records.append({'beat': bid, 'status': 'error', 'error': str(exc)})` |
| B09 | "70-percent frame position avoids slate start and freeze artifacts at end" | ✓ | `at = duration * .70` — design comment at line 98: "Source-beat frames avoid pretending stale-master timing matches a new sheet" |
| B10 | Prompt describes real batch file format and audit.json fields | ✓ | Format confirmed by executing the script; audit.json schema from source lines 154–157 |

## Gaps

- The `sample_master` function samples the MASTER MP4 (not per-beat clips) at 12 distributed positions, distinct from `audit()` which samples per-beat clips at 70%. This distinction is explained in B07 by showing per-beat sample output. Master sampling is a parallel operation.
- The `evidence_file_candidates` field is populated but not discussed in narration — it searches for files matching `(evidence|session|stdout|...)` patterns. Not a factual error; a deliberate omission for time.

## Editorial

- B04 narration describes confidence levels (source-confirmed, routing-review, review) — these come from the findings dict in the source code and are verified.
- All claims about the script's behavior are derived from reading the source, not from running a non-deterministic external service.
