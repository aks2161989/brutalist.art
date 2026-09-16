# SOURCES — Brutalist Utility: smithsonian_fetch.py
# run_id: 742a1549e73142e4b6d655986b0ae560  |  2026-09-14

## Primary source

| File | Repo-relative path | SHA-256 |
|---|---|---|
| smithsonian_fetch.py | runtime/scripts/smithsonian_fetch.py | 1934656d6e640bea90ecf2dccc892d0f0a060a6a256f5ba783296cbcbe6f8733 |

Captured at 2026-09-14T15:14:23Z per SOURCE-SNAPSHOT.json.

## Referenced code elements (all from primary source)

- `_load_index()` — lines 147-163: index existence gate
- `_search()` — lines 166-172: text search with ranking
- `_term_words()` — lines 95-97: tokenization and stop-word removal
- `_score()` — lines 113-125: scoring function
- `_object_type_bonus()` — lines 100-110: apparatus/ephemera type ranking
- `APPARATUS_TYPES` / `EPHEMERA_TYPES` — lines 74-86: type vocabularies
- `_resolve_image_url()` — lines 207-264: CC0 URL resolution via content-detail endpoint
- `_download()` — lines 269-284: streaming download
- `_upscale()` — lines 287-322: Topaz Photo AI optional upscale
- `_write_sidecar()` — lines 325-334: provenance sidecar writer
- `_fetch_and_shelve()` — lines 338-380: orchestration function
- `_copy_to_pantry()` — lines 383-401: pantry intake copy with JPEG→PNG conversion
- `_list_shelved()` — lines 404-418: library listing
- `main()` — lines 423-516: argument parsing and dispatch

## Example sources (read-only leads — not reused)

| Lead | SHA-256 | Used for |
|---|---|---|
| rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json | 746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22 | Beat structure reference only |
| yatra-r/2026-09-03-this-week-gordy/beat_sheet.json | 7e3ea1f61c421e605e583be9b2a7b5f554aa8cadfb6e14dabaee66f471856083 | Beat structure reference only |

Original files were not modified. No private Drive URLs, personal contacts, or old
recordings from example leads appear in this reel.

## Smithsonian Open Access

The Smithsonian Institution Open Access collection provides CC0-licensed content
at https://www.si.edu/openaccess. The API base URL used in the script is:
https://api.si.edu/openaccess/api/v1.0 — this is the script's own documented API base,
not independently verified for currency in this build.

## Local demos

All demos run against the isolated toolkit without network or paid API access.
See demo/demo-log.txt for captured output.
