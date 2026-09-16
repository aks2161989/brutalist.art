# FACTCHECK — Brutalist Utility: smithsonian_fetch.py — Short
# Short run_id: 7d5225769ced4a06a72051a66def374b  |  2026-09-14
# Retained beats: B00, B01, B03, B07, B09, B11
# Dropped: B02, B04, B05, B06, B08, B10 (their claim sections below are inactive in this Short — claims verified in parent)
# Parent run_id: 742a1549e73142e4b6d655986b0ae560

## Source
- File: runtime/scripts/smithsonian_fetch.py
- SHA-256: 1934656d6e640bea90ecf2dccc892d0f0a060a6a256f5ba783296cbcbe6f8733
  (from SOURCE-SNAPSHOT.json at capture time; matches episode source_sha256 c6051cd9)

## Claim-by-claim verification (against source code)

### B00 — Intro claims
- "CC0 images from the Smithsonian Institution" — VERIFIED: SI_API_BASE = SI Open Access; _resolve_image_url checks access == "CC0"
- "one at a time" — VERIFIED: no batch; single record per run
- "local index" — VERIFIED: _load_index() reads INDEX = LIBRARY / "index.jsonl"
- "resolves the full-resolution URL through the SI API" — VERIFIED: _resolve_image_url calls /content/{record_id}
- "optionally upscales with Topaz Photo AI" — VERIFIED: _upscale() called if TPAI path exists
- "shelves the result" — VERIFIED: _fetch_and_shelve() copies to IMAGES dir

### B01 — BLUF claims
- "CC0-only by design" — VERIFIED: access == "CC0" gate in _resolve_image_url; fallback also checks CC0
- "source sidecar — SI object id, credit, license, URL" — VERIFIED: _write_sidecar writes SI_ID, Title, Unit, Credit, Source URL, License
- "written automatically" — VERIFIED: _write_sidecar called unconditionally inside _fetch_and_shelve

### B02 — Pipeline claims
- "index must already exist" — VERIFIED: _load_index() calls sys.exit() if INDEX does not exist (line 149-151)
- "lookup by id or text search" — VERIFIED: _get_by_id() and _search() functions
- "content-detail endpoint for full-res URL" — VERIFIED: GET /content/{record_id} in _resolve_image_url
- "download → upscale → shelve" — VERIFIED: _download(), _upscale(), shutil.copy2() to IMAGES

### B03 — Search claims
- "tokenizes query, dropping stop words, short words" — VERIFIED: _term_words() strips words len<3 and STOP_WORDS
- "scores every record" — VERIFIED: _score() applied to all records in _search()
- "candidates display with SI unit, object type, thumbnail URL" — VERIFIED: print statement line 472-475

### B04 — Scoring mechanism
- "title match: 4 points" — VERIFIED: s += 4.0 when w in title_words (line 118-119)
- "token match: 2 points" — VERIFIED: s += 2.0 when w in toks (line 120-121)
- "apparatus bonus +1.5" — VERIFIED: _object_type_bonus() returns 1.5 for APPARATUS_TYPES (line 104-105)
- "ephemera penalty -1.0" — VERIFIED: _object_type_bonus() returns -1.0 for EPHEMERA_TYPES (line 107-108)
- APPARATUS_TYPES include: "computer", "terminal", "instrument" — VERIFIED lines 74-81
- EPHEMERA_TYPES include: "pamphlet", "photograph", "report" — VERIFIED lines 82-86

### B05 — URL resolution claims
- "S3-indexed records have URL stored directly" — VERIFIED: image_url = rec.get("image_url", "") check line 350
- "descriptiveNonRepeating → online_media → media[]" — VERIFIED: JSON path in _resolve_image_url lines 231-235
- "type Images and access CC0" — VERIFIED: "Images" in media_type and access == "CC0" (lines 246-249)
- "Fallback: any CC0 media" — VERIFIED: second loop checks only access == "CC0" (lines 252-261)

### B06 — Topaz claims
- "checks whether tpai exists at expected path" — VERIFIED: not Path(TPAI).exists() check (line 289)
- "compares source and output dimensions" — VERIFIED: PIL.Image.open() comparison in _upscale() lines 313-321
- "WARN if not larger" — VERIFIED: status = "WARN — not larger than source" (line 319)
- "shelves original if tpai missing" — VERIFIED: shutil.copy2(dl_path, lib_jpg) path when upscaled is None (line 375)

### B07 — Sidecar claims
- "CC0, SI_ID, Title, Unit, Credit, Source URL, License" — VERIFIED: _write_sidecar() exact fields lines 326-333
- ".source.txt filename" — VERIFIED: _library_path() returns stem + ".source.txt" (line 197)

### B08 — Pantry integration claims
- "converts JPEG to PNG for pantry intake" — VERIFIED: PIL Image.open().convert("RGB").save(dst) in _copy_to_pantry lines 392-396
- "--copy requires --beat" — VERIFIED: sys.exit() if a.copy and not a.beat (line 449)
- "next step prompt printed" — VERIFIED: print statements lines 399-400

### B09 — Verdict claims
- "strictly CC0" — VERIFIED: see B01
- "index-first" — VERIFIED: see B02
- "Topaz degrades gracefully" — VERIFIED: see B06
- "--yes auto-accepts top hit" — VERIFIED: rec = hits[0] when a.yes (line 478)

## Gaps / limitations
- Cannot verify API rate limiting behavior without a real SI API key and network access.
- Cannot verify actual Topaz upscale output quality without tpai installed.
- Smithsonian Open Access license URL cited is from sidecar code (https://www.si.edu/openaccess) — correct per public SI docs.
- "Limited anonymous use" claim from docstring (line 42-43) is not verifiable here; it is the script's own documented claim.

## Unverified/stripped claims
- No model version numbers used.
- No count statistics that would drift.
- No invented figures.
