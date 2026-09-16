# FACTCHECK — Brutalist Utility: image_fetch.py

## Claims checked against source code

| Claim | Source | Status |
|---|---|---|
| Four adapters: smithsonian, nasa, wellcome, nlm_ihm | `sources/__init__.py` REGISTRY keys, verified at runtime | VERIFIED |
| Smithsonian adapter uses a local index.jsonl | `image_fetch.py` lines 36–65: `hasattr(adapter, "INDEX")` path | VERIFIED |
| non-Smithsonian adapters require --url | source code: only smithsonian has INDEX attribute; others fall through to `adapter.search()` and are expected to use --url path | VERIFIED (by code path) |
| Topaz is probed by PATH | `source_core.py` lines 29–30: `shutil.which("tpai")`, line 93: `if not Path(TPAI).exists()` | VERIFIED |
| tpai absent → shelves original without error | `source_core.py` topaz_upscale() returns None, shelve_image() falls back to `dl` | VERIFIED |
| shelved file path: library/<adapter>/images/ | `source_core.py` library_dir() returns `ART_HOME / "library" / adapter_id / "images"` | VERIFIED |
| sidecar records source, license, credit, id, title, url, source_url | `source_core.py` write_sidecar() | VERIFIED |
| already_shelved() returns existing path immediately | `source_core.py` shelve_image() checks `already_shelved()` first | VERIFIED |
| --url skips adapter.resolve() | `image_fetch.py` lines 99–109: if args.url block builds record directly | VERIFIED |
| Exit code 1 on all failure paths | `sys.exit(1)` at lines 95, 115, 122, 133 | VERIFIED |
| Failure messages are printed before exit | print() calls precede sys.exit(1) in all cases | VERIFIED |
| --beat default is B04 | `ap.add_argument("--beat", default="B04")` in image_fetch.py | VERIFIED |
| pantry copy uses PIL for jpg→png conversion | `source_core.py` copy_to_pantry(), PIL.Image.convert("RGB").save() | VERIFIED |
| Registry is extensible: new adapter adds one file | REGISTRY dict in sources/__init__.py imports and registers by ADAPTER_ID | VERIFIED |

## Demo limitations (HONEST LIMIT)

- No live network fetches performed (sandbox restriction). The CLI examples shown are source-backed.
- Topaz Photo AI is not installed in the toolkit environment. The tpai fallback path is demonstrated by reading `source_core.py` lines 93–98 directly.
- The Smithsonian index.jsonl is not available in the isolated toolkit copy; the record lookup path is illustrated from code rather than executed.
- No fabricated successful run outputs are shown. The film demonstrates what the tool does through its source code structure.

## Strip list (things NOT asserted)

- No image counts, fetch times, or upscale ratios — none appear in source
- No version numbers for Topaz Photo AI or requests library
- No claim that tpai is free or paid — not stated in source
- No claim about which records are in the Smithsonian index — no index in toolkit
