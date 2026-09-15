# SOURCES — Brutalist Utility: image_fetch.py

## Primary source

| File | Repo path | SHA-256 (from SOURCE-SNAPSHOT.json) |
|---|---|---|
| image_fetch.py | `runtime/scripts/image_fetch.py` | `f70c29abc2aeb6c39475bbed30b7749c36852722c84d76ef1a69e414e3d89174` |
| source_core.py | `runtime/scripts/source_core.py` | read at run time |
| sources/__init__.py | `runtime/scripts/sources/__init__.py` | read at run time |
| sources/smithsonian.py | `runtime/scripts/sources/smithsonian.py` | read at run time |
| sources/nasa.py | `runtime/scripts/sources/nasa.py` | read at run time |
| sources/wellcome.py | `runtime/scripts/sources/wellcome.py` | read at run time |
| sources/nlm_ihm.py | `runtime/scripts/sources/nlm_ihm.py` | read at run time |

## Skill reference

| File | Repo path | SHA-256 |
|---|---|---|
| ai-explainer SKILL.md | `skills/make/ai-explainer/SKILL.md` | `a7421d4d861b44a983a31e9fcd7451cd32312a139366e74acc2123dfdefbd3c0` |
| nopunt SKILL.md | `skills/make/nopunt/SKILL.md` | `ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505` |
| teardown PROSE.md | `runtime/prose/teardown/PROSE.md` | `6accc1a576ca9b52713abd31507f5deece6dc2612ca90967b25b661e59111786` |

## Example leads read

| Title | SHA-256 prefix | Use |
|---|---|---|
| Every Image Earns Its Place (sainikhil-madison) | `bff640df81` | Beat structure reference — DivergentFates, BinaryBranch, ChipGrid patterns |
| Your Weekly Video, Handled. (rohan-v) | `746409a871` | Weekly-video beat sheet structure reference |

## Demo outputs (local, no network)

All command demonstrations use the source code read directly from the toolkit. No live network fetches were performed; the actual download/upscale/shelve path requires `requests`, network access, and optionally `tpai` — none available in sandbox. The CLI examples shown are source-backed (derived from actual `image_fetch.py` argument parser and docstring). This limitation is logged in FACTCHECK.md.

## Corrections applied (DOUBLE-CHECK LAW)

- The docstring example `npg_NPG.78.164` is taken verbatim from image_fetch.py lines 10–12 as a real record ID format, not invented.
- No metrics, counts, or performance figures asserted — none appear in the source.
- "Topaz Photo AI" is the correct product name (source: TPAI path in source_core.py line 29–30).
- The four adapter IDs (smithsonian, nasa, wellcome, nlm_ihm) are taken directly from the REGISTRY keys in sources/__init__.py.
