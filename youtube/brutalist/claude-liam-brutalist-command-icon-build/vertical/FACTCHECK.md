# FACTCHECK — Brutalist Command: art icon-build

Every factual claim in the beat sheet was verified against the actual source
files in the isolated toolkit at
`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/.repoloop/workspaces/claude-liam-brutalist-command-icon-build/toolkit`
and the shipped canonical index at
`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/icons/icons.json`
(symlinked into the workspace at `icons/` for reproducible captures — read-only).

## Sources of truth

| # | Claim → evidence | File | Verified |
|---|---|---|---|
| 1  | Command exists: `./art icon-build` (NO aliases; only the exact word) | `art:64-66` (single case branch, no alternates) | ✓ (grep) |
| 2  | The branch execs `runtime/scripts/build_icon_set.py` | `art:65` | ✓ |
| 3  | Upstream `svg/` totals ~12 GB on disk | `du -sh svg/` — 12G | ✓ (demo/RUN-LOG.md) |
| 4  | `material-design-icons` is 9.1 GB, dropped for rule 1 + rule 2 | `du -sh svg/material-design-icons` — 9.1G; `build_icon_set.py:73-74` | ✓ |
| 5  | `RemixIcon` is 100% filled, dropped for rule 1 | `build_icon_set.py:72` | ✓ |
| 6  | `heroicons` duplicates lucide, dropped for rule 2 | `build_icon_set.py:75-76` | ✓ |
| 7  | `anthropics/` has NO LICENSE anywhere, dropped for provenance | `find svg/anthropics -iname LICENSE\*` → no output; `build_icon_set.py:70-71` | ✓ |
| 8  | The four RULES quoted verbatim from the docstring | `build_icon_set.py:14-27` | ✓ |
| 9  | Priority order: lucide > tabler > iconoir > feather > brand (tabler brand-*) | `build_icon_set.py:59-66` (SOURCES list) | ✓ |
| 10 | 44 pt math: stroke 2 in a 24 viewBox at 528 px = 44 pt exactly | `build_icon_set.py:53-56` (`RENDER_PX_FOR_44PT = 528  # 2 * (528/24) == 44`) | ✓ |
| 11 | Constant ships in icons.json as `render.line_44pt_px` | `icons/icons.json → "render": {"line_44pt_px": 528}` | ✓ |
| 12 | `--dry-run` reports source passes and writes nothing | live capture, `demo/RUN-LOG.md § "$ ./art icon-build --dry-run"` | ✓ |
| 13 | `--dry-run` counts: lucide 1749, tabler 4134, iconoir 1045, feather 26, brand 376 | `demo/RUN-LOG.md`; matches `icons.json → sources`  | ✓ |
| 14 | Total: 7,330 concepts (376 brand, 6,954 general) | `icons.json → count: 7330`; live sum | ✓ |
| 15 | `--limit N` stops at N icons from the first priority source only | live capture with `--limit 5 --dry-run` — only lucide runs | ✓ |
| 16 | `--limit` combined with `--dry-run` writes nothing | live capture | ✓ |
| 17 | Missing `svg/` → each source reports "source dir absent"; total 0 concepts; exit 0 | live capture with symlink removed | ✓ |
| 18 | Unknown flag (e.g. `--bogus-flag`) → argparse error, exit 2 | live capture | ✓ |
| 19 | Output artifacts: `icons/svg/*.svg` + `icons.json` + `NOTICE.md` | `build_icon_set.py:246-279`; live `ls icons/` | ✓ |
| 20 | `icons/` totals ~30 MB (29 MB in `svg/`) | `du -sh icons` — 30 M | ✓ |
| 21 | NOTICE.md carries ISC (lucide) + MIT (tabler, iconoir, feather) copyright blocks in full | `head icons/NOTICE.md`; `build_icon_set.py:82-87` (LICENSES tuple) | ✓ |
| 22 | Ratio: 12 GB → 30 MB ≈ 400× reduction | 12288 MB / 30 MB ≈ 410 | ✓ |
| 23 | Icons rewritten to viewBox 0 0 24 24, stroke-width 2, currentColor, round caps | `build_icon_set.py:166-190` (`normalise()`); `icons.json → geometry` | ✓ |
| 24 | `feather` retains only 26 of ~287 because lucide already claims the concepts | `demo/RUN-LOG.md` — feather kept 26, dropped 261 as duplicate | ✓ |

## Numbers double-checked

- **12 GB** — `du -sh svg/` on the shared brutalist.art tree (2026-09-09).
- **2.4 M files** — the module docstring's own count (`build_icon_set.py:5-6`).
- **~2.4 million** is the same figure; the reel rounds to "two point four million".
- **9.1 GB** — `du -sh svg/material-design-icons` on the shared tree.
- **7,330 / 376 / 6,954** — from `icons.json → count` and a live Python sum on `icons`.
- **528 px** — from `icons.json → render.line_44pt_px` and `RENDER_PX_FOR_44PT`.
- **30 MB / 29 MB** — from `du -sh icons` and `du -sh icons/svg`.

## Known limitations

- **`icons/` numbers may drift.** `build_icon_set.py` regenerates `icons.json`
  from whatever `svg/` currently holds. The 7,330 / 376 counts are the snapshot
  as of the shipped `icons/icons.json` at commit
  `ba2d0e0f043f5b3b35a50d336e0fc66fbfecfc0c` (also the SOURCE-SNAPSHOT commit).
  A future run against a changed `svg/` will produce different numbers.
- **We did NOT rewrite the shipped `icons/` set** during this build. Every
  `icon-build` invocation captured in `demo/RUN-LOG.md` uses `--dry-run`; no
  new bytes were written to the public `brutalist.art/icons` tree.
- **`heroicons` duplication claim.** The doctrine says the outline set
  "duplicates lucide concepts that lucide already serves at a cleaner single
  weight." We did not enumerate the concept overlap in this build — we quote
  the module's own reason.
- **Legacy checkers.** `scripts/type_check.py` and the kerning skill referenced
  in `ai-explainer/SKILL.md` are not present in this toolkit snapshot.
  `TYPECHECK.md` distinguishes actual visual typography review (done) from the
  absent legacy checker.

## No claims requiring correction

The narration does not name model versions, spend rates, or dated numbers
other than the icon counts (which are snapshotted here) and the disk-size
figures (which are `du -sh` reads on the shared tree, logged in
`demo/RUN-LOG.md`). No claim in the reel goes beyond what the source files
support.
