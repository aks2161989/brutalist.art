# FACTCHECK — Brutalist Utility: write_review_queue_report.py

run_id: aef36acf6a354924acd1af29d9d319cf

All claims verified against the actual source file at runtime/scripts/write_review_queue_report.py (SHA-256: 8de57eb1bb0e4f1345c7a7e26ad99365969eda321c3a7fc81d897867e50d904d).

| Claim | Verdict | Source / derivation | Fix |
|---|---|---|---|
| Script takes one argument: the output directory | ✓ | Line 9: `out=Path(sys.argv[1])` | — |
| Reads audit.json from that directory | ✓ | Line 10: `(out/'audit.json').read_text()` | — |
| Reads review-notes.json from that directory | ✓ | Line 11: `(out/'review-notes.json').read_text()` | — |
| Writes AUDIT.md to the output directory | ✓ | Line 79: `(out/'AUDIT.md').write_text(...)` | — |
| Never mutates reels (read-only) | ✓ | Module docstring: "never mutate reels"; only writes to `out/AUDIT.md`, reads from reels | — |
| Three pantry spellings: pantry_path, pantry_file, pantry | ✓ | Lines 64–65: `shot.get('pantry_path') or shot.get('pantry_file') or shot.get('pantry')` | — |
| Comment names the three spellings | ✓ | Line 61: `# All three legacy spellings occur in this queue.` | — |
| No try-except anywhere in the script | ✓ | Read full source — no try/except blocks present | — |
| IndexError on missing argument | ✓ | Tested locally: `python3 write_review_queue_report.py` → `IndexError: list index out of range` | — |
| FileNotFoundError on missing audit.json | ✓ | Tested locally with empty dir → `FileNotFoundError: .../audit.json` | — |
| KeyError on missing reel number in notes | ✓ | Tested locally with mismatched review-notes.json → `KeyError: '1'` | — |
| Scope statement hardcoded in script | ✓ | Lines 13–21: text literals baked in | — |
| "12 distributed master frames per film" | ✓ | Lines 18–19: hardcoded scope text from script itself | — |
| "676 authored beats" | ✓ | Lines 18–19: hardcoded scope text from script itself | — |
| Reads beat_sheet.json from each reel | ✓ | Line 61: `sheet=json.loads((reel/'beat_sheet.json').read_text())` | — |
| Final section: "Do not change human approvals or publish" | ✓ | Line 49 in text array: exact quote from script | — |
| Script uses `str(n)` key lookup in notes | ✓ | Line 52: `note=notes[str(n)]` | — |

## Demo verification

Script run on synthetic fixture data and observed to produce AUDIT.md with correct structure. Output saved to demo/AUDIT.md. All pantry flags B00 (pantry_path) and B01 (pantry_file) correctly detected from fixture beat_sheet.json.

## No fabrication

No outputs were invented. All narration claims reference lines verified above. The three failure modes shown in B07 were tested and observed in the local run.
