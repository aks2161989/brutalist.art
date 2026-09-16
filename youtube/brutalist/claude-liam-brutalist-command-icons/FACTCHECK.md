# FACTCHECK — Brutalist Command: art icons

Every factual claim in the beat sheet was verified against the actual source files in the isolated toolkit at
`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/.repoloop/workspaces/claude-liam-brutalist-command-icons/toolkit`
and the icons index at `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/icons/icons.json`
(symlinked into the toolkit at `icons/` for reproducible demos).

## Sources of truth

| # | Claim → evidence | File | Verified |
|---|---|---|---|
| 1 | Command exists: `./art icons` (aliases: `icon`, `icon-search`) | `art:60-63` | ✓ |
| 2 | All three aliases exec `runtime/scripts/icon_search.py` | `art:60-63` | ✓ |
| 3 | Canonical set count is 7,330 icons | `icons/icons.json → "count": 7330` | ✓ |
| 4 | 376 icons are brand/logo (`brand: true`) | `python3 -c` count over icons.json — 376 | ✓ |
| 5 | Every icon uses `viewBox="0 0 24 24"` | `icons/icons.json → geometry.viewBox` | ✓ |
| 6 | Stroke-width is 2, stroke is `currentColor`, fill is `none` | `icons/icons.json → geometry` | ✓ |
| 7 | Ranking order: exact name > every-word > name-prefix > token-hit | `icon_search.py:14-16` (docstring) + `rank()` body | ✓ |
| 8 | IDF re-weighting: `idf = log((n+1)/(df+1)) + 1` | `icon_search.py:62` | ✓ |
| 9 | Rare words outrank common ones (docstring claim) | `icon_search.py:17` | ✓ |
| 10 | `--check <name>` answers IN SET / not-in-set + nearest neighbors | `icon_search.py:119-129` | ✓ |
| 11 | `--show <name>` prints raw SVG to stdout | `icon_search.py:112-117` | ✓ |
| 12 | `--brands` narrows to brand/logo icons only | `icon_search.py:66-67` | ✓ |
| 13 | `--no-brands` excludes brand/logo icons | `icon_search.py:68-69` | ✓ |
| 14 | Miss message: "A miss is NOT a licence to draw a one-off." | `icon_search.py:145-147` | ✓ |
| 15 | Miss exits 0 (prints instructions, returns 0) | `icon_search.py:144-148` (returns after print, no sys.exit) | ✓ verified live |
| 16 | `--show <bogus>` exits 1 with `sys.exit(f"not in the set: …")` | `icon_search.py:115` | ✓ verified live |
| 17 | STOP list includes "a, an, the, of, for …" | `icon_search.py:39-40` | ✓ |
| 18 | Query "money" → 31 hits, top hit `money-square` | `demo/RUN-LOG.md` (live capture) | ✓ |
| 19 | Query "sankey flow" → `chart-sankey` first | `demo/RUN-LOG.md` (live capture) | ✓ |
| 20 | Query "github --brands" → 2 hits (`brand-github`, `brand-github-copilot`) | `demo/RUN-LOG.md` (live capture) | ✓ |
| 21 | Query "quantum entanglement" → no match, exit 0 | `demo/RUN-LOG.md` (live capture) | ✓ |
| 22 | Aliases icons / icon / icon-search return identical stdout | `demo/RUN-LOG.md` — 3 diff runs pass | ✓ |

## Numbers double-checked

- **7,330** — the `"count"` field in `icons/icons.json`.
- **376** — `sum(1 for i in icons if i['brand'])` computed live.
- **6,954** — 7330 − 376 (the concept-only corpus quoted in B07 and B09).
- **528px** — from `icons/icons.json → "render": {"line_44pt_px": 528}` (not spoken but reflected in the geometry beat).

## Known limitations

- **`--show <bogus>` exit code**: the beat sheet does not quote the exit code
  for `--show` on a missing name. Live capture confirms exit 1 (`sys.exit`),
  which is a different error path from the miss (exit 0). Included in
  `demo/RUN-LOG.md` for completeness, not in the film — the film keeps
  focus on the search miss (B08) as the primary failure teaching.
- **Icon totals may drift**: `build_icon_set.py` regenerates `icons.json`
  from the `svg/` directory. Numbers 7,330 / 376 are the snapshot as of
  `icons/icons.json` on the source-snapshot commit
  `ba2d0e0f043f5b3b35a50d336e0fc66fbfecfc0c`.
- **STOP list**: the STOP list also filters `icon`, `symbol`, `image`,
  `picture`, `show`, `showing`, `that`, `with`. The narration does not
  enumerate these; not a fact the film asserts.
- **Legacy checkers**: `scripts/type_check.py` and the kerning skill
  referenced in `ai-explainer/SKILL.md` are not present in this toolkit
  snapshot. `TYPECHECK.md` records this honestly rather than claiming a
  missing checker passed.

## No claims requiring correction

The narration does not name model versions, spend rates, product counts
that drift, or dated numbers other than the icon totals (which are
snapshotted here). No claim in the reel goes beyond what the source
files support.
