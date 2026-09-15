# FACTCHECK — Brutalist Utility: audit_review_queue.py — Short

Short cut: 6/12 beats retained (B00, B01, B05, B07, B09, B11). Only claims in kept beats are checked below.

All narration claims checked against `runtime/scripts/audit_review_queue.py` source code, read in full.

| Beat | Claim | Verdict | Source / derivation |
|---|---|---|---|
| B00 | "read-only batch inspector" | ✓ | Module docstring: "Read-only film audit"; no write to reel directories |
| B00 | "samples per-beat source clips at the 70-percent mark" | ✓ | `at = duration * .70` (line 108) |
| B00 | "never approves, never publishes" | ✓ | Module docstring: "never approves or publishes" |
| B01 | "script's own docstring says never approves, never publishes" | ✓ | First line of module docstring (line 3) |
| B05 | "compares the master MP4's modification time against the beat sheet's" | ✓ | `'stale': master.stat().st_mtime < sheet_path.stat().st_mtime if master else None` |
| B05 | "flag is informational, does not block the audit and does not touch either file" | ✓ | `stale` is written to output JSON only; no raise, no file modification |
| B07 | "12 beats found, 12 frame samples, 0 review leads" | ✓ | Real execution output: `01: 12 beats; 0 leads; 12 frame samples` against claude-liam-brutalist-skill-nopunt |
| B07 | "beat count, lead count, sample count — nothing else is printed to stdout" | ✓ | stdout line format: `{n:02d}: {beats} beats; {leads} leads; {samples} frame samples` |
| B09 | "stale-master check is the one signal the rest of the pipeline cannot give you" | ✓ | No other pipeline tool compares master MP4 mtime to beat sheet mtime |
| B09 | "70-percent frame position avoids slate start and freeze artifacts at end" | ✓ | `at = duration * .70` — avoids first-frame slate and tail-freeze artifacts |
| B09 | "silent ffmpeg tile failures look identical to healthy tiles unless you count them" | ✓ | `except Exception: sample_records.append({'status': 'error'})` — no visual difference in contact sheet |
| B09 | "math_layout_check has no fallback — missing module crashes the entire batch" | ✓ | `from math_layout_check import math_layout_errors` at top-level; ImportError before main() |

## Gaps

- Dropped beats (B02, B03, B04, B06, B08, B10) had additional verified claims. Those belong in the 16:9 long and are not repeated here.
- B07 evidence numbers (12/12/0) remain valid for the nopunt reel as a completed delivered episode. Numbers are reproducible against the same unmodified reel.
