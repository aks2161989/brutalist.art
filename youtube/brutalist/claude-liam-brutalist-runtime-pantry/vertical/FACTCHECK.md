# FACTCHECK — Brutalist Utility: pantry.py
## run_id: 1df027e6acef4cf1ad6843ed3815ffb7

Source verified: `runtime/scripts/pantry.py` SHA-256 `5b059be171601690a436487ba1eb1d0ebefd58d4d4b0b796e971a427e201ba35`

## Claims verified against source

| Claim | Beat | Line(s) | Status |
|---|---|---|---|
| "raw finds never go straight into media/" | B02 | 3-7 (docstring) | VERBATIM from docstring |
| BID_RE pattern matches uppercase letters + two digits | B03 | 11 | VERIFIED: `r"^([A-Z]{1,3}\d{2})"` |
| Valid prefix: `B04_restoration.mov → media/B04.mp4` | B03 | 74-109 | VERIFIED |
| Portrait detection: `vh > vw and not report` → suffix `-916` | B06 | 85 | VERBATIM |
| Source report detection via `is_source_report()` | B06 | 84 | VERIFIED — imported from build_safety |
| B-roll gets `-an` (audio strip); report gets `-c:a aac -b:a 192k` | B06 | 90-92 | VERBATIM |
| Duration warning at `d < need * 0.85` | B06 | 98-103 | VERIFIED |
| DOCUMENT crop: 16:9 height, anchored from top | B05 | 115-119 | VERBATIM |
| RGB conversion for non-RGB/L images | B05 | 121-122 | VERBATIM |
| Width warning `< 1920` | B05 | 124-125 | VERBATIM |
| Missing `pantry/` → `sys.exit(...)` | B08 | 52 | VERBATIM |
| `validate_project(sheet)` called before processing | B08 | 55 | VERBATIM |
| Files without BID prefix are logged as SKIP | B08 | 62-65 | VERBATIM |
| Beat not in sheet → logged as SKIP | B08 | 68-70 | VERBATIM |
| Sidecar `.source.txt` written after slotting | B07 | 130-138 | VERBATIM |
| Higgsfield detection via filename tokens | B07 | 105 (`hf_`, `humanitarians.ai`, `midjourney`, `_mj_`, `grok`) | VERIFIED |
| AI sidecar has disclosure template | B07 | 134-135 | VERBATIM |
| Non-AI sidecar has URL/License/Credit placeholders | B07 | 136-137 | VERBATIM |

## Claims NOT made (correctly omitted)

- The episode does NOT claim pantry.py handles Higgsfield generation itself.
  pantry.py only detects AI-looking filenames; the generation is separate.
- The episode does NOT claim restoration (WARMONO/NATGEO) is part of pantry.py.
  The docstring says assets arrive "already restored" — pantry.py does the rest.
- The episode does NOT claim compile.py's hash manifest is in pantry.py.
  The hash manifest is compile.py's concern; pantry.py is idempotent but does not
  itself maintain a hash manifest (noted accurately in B02 narration as "reprocesses whatever is in pantry/").

## Actual vs. claimed idempotency

The script re-reads pantry/ each time and re-slots every file it finds. The compile.py hash
manifest governs whether already-slotted, unchanged media gets recompiled. Calling pantry.py
idempotent is accurate for its own operations: running it twice produces the same media/ output
without corruption.

## Gap: no dry-run flag

B09 (verdict) states there is no dry-run flag. Verified by reading the argparse block:
only `folder` and `--doc-anchor` are registered. This is an accurate limitation.
