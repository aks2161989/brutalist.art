# FACTCHECK — Brutalist Utility: pantry.py — Short
## run_id: 517c4dadd53d490386ecb25993a16740
## Derived from parent run_id: 1df027e6acef4cf1ad6843ed3815ffb7
## Kept beats: B00, B01, B03, B04, B06, B08, B09, B11
## Dropped: B02, B05, B07, B10 (no dropped-beat claims remain in this Short)

Source verified: `runtime/scripts/pantry.py` SHA-256 `5b059be171601690a436487ba1eb1d0ebefd58d4d4b0b796e971a427e201ba35`

## Claims verified in retained beats

| Claim | Beat | Line(s) | Status |
|---|---|---|---|
| BID_RE pattern matches uppercase letters + two digits | B03 | 11 | VERIFIED: `r"^([A-Z]{1,3}\d{2})"` |
| Valid prefix: `B04_restoration.mov → media/B04.mp4` | B03 | 74-109 | VERIFIED |
| Portrait detection: `vh > vw and not report` → suffix `-916` | B06 | 85 | VERBATIM |
| Source report detection via `is_source_report()` | B06 | 84 | VERIFIED — imported from build_safety |
| B-roll gets `-an` (audio strip); report gets `-c:a aac` | B06 | 90-92 | VERBATIM |
| Duration warning at `d < need * 0.85` | B06 | 98-103 | VERIFIED |
| Missing `pantry/` → `sys.exit(...)` | B08 | 52 | VERBATIM |
| `validate_project(sheet)` called before processing | B08 | 55 | VERBATIM |
| Files without BID prefix are logged as SKIP | B08 | 62-65 | VERBATIM |
| Beat not in sheet → logged as SKIP | B08 | 68-70 | VERBATIM |
| No dry-run flag (argparse block only has `folder` and `--doc-anchor`) | B09 | argparse | VERIFIED |

## Claims NOT made (correctly omitted)

- B02 dropped: abstract Pantry Law quote not present in this Short; B03 covers the concrete rule.
- B05 dropped: image-path DOCUMENT crop, RGB conversion, and width warning not claimed.
- B07 dropped: provenance sidecar and Higgsfield detection details not claimed.
- B10 dropped: Your Turn exercise not shown.
- The Short does NOT claim to cover every pantry.py feature.

## Actual vs. claimed idempotency

The script re-reads pantry/ each time and re-slots every file it finds. Calling pantry.py
idempotent is accurate for its own operations: running it twice produces the same media/ output
without corruption.

## Gap: no dry-run flag

B09 (verdict) states there is no dry-run flag. Verified by reading the argparse block:
only `folder` and `--doc-anchor` are registered. This is an accurate limitation.
