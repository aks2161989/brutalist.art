# FACTCHECK — Brutalist Command: art icon-build — Short

This Short is a whole-beat cut of the parent 9:16 vertical
(`youtube/brutalist/claude-liam-brutalist-command-icon-build/vertical`, master SHA-256 `3566906b923fb2b0ef211f5ed1dcb434109b2ad68144d389d43edeeecf4a86a2`). Every retained clip is the parent's native 2160×3840 render, byte-copied — no re-render, no new claim was authored for this cut. The parent factcheck is authoritative; only the rows still on screen in this Short are re-listed here.

## Claims retained in the Short

Verified against the toolkit sources listed in the parent SOURCES.md (which is copied alongside this file).

| # | Retained beat | Claim → evidence | Source |
|---|---|---|---|
| 1 | B00, B04, B09 | `./art icon-build` execs `runtime/scripts/build_icon_set.py` — single dispatcher branch, no aliases | `art:64-66` |
| 2 | B00, B03 hook (still stated in B00's ASK/result lines) | Raw `svg/` totals ~12 GB / ~2.4 M files | `du -sh svg/`; `build_icon_set.py:5-6` docstring |
| 3 | B00, B09 | Canonical output totals ~30 MB / 7,330 icons | `du -sh icons`; `icons/icons.json → count` |
| 4 | B00, B04, B09 | Geometry: viewBox `0 0 24 24`, stroke width 2, `currentColor` | `build_icon_set.py:53-56` and `:166-190`; `icons.json → geometry` |
| 5 | B01 | The command is subtractive — it cuts an existing corpus, not additive downloading of new icons | `build_icon_set.py` module docstring; every capture in `demo/RUN-LOG.md` reads from `svg/` |
| 6 | B04 | The four rules quoted verbatim from the module docstring | `build_icon_set.py:14-27` |
| 7 | B06 | `--dry-run` writes nothing and reports per-source passes | `build_icon_set.py:200-244` (dry-run branch); `demo/RUN-LOG.md` |
| 8 | B06 | `--dry-run` counts: lucide 1749/-7, tabler 4134/-602, iconoir 1045/-626, feather 26/-261, brand 376 → 7,330 total | `demo/RUN-LOG.md`; matches `icons.json → sources` |
| 9 | B09 | `--limit N` stops at the first N icons from the first priority source only | live capture; parent factcheck row 15 |
| 10 | B09 | Four excluded libraries: material-design (filled), RemixIcon (filled), heroicons (dup), anthropics (no LICENSE) | `build_icon_set.py:68-76`; parent factcheck rows 4–7 |
| 11 | B09 | 44 pt math: stroke 2 in a 24 viewBox at 528 px = 44 pt exactly; ships in `icons.json → render.line_44pt_px = 528` | `build_icon_set.py:53-56`; `icons/icons.json` |
| 12 | B09 | NOTICE.md carries ISC (lucide) + MIT (tabler/iconoir/feather) copyright blocks | `head icons/NOTICE.md`; `build_icon_set.py:82-87` |

Rows 11 and 12 are named in the verdict list even though the deeper walkthrough beats (B05 and B07) were cut; the shorter Short surfaces the fact without the derivation.

## Claims dropped with their beats

The following parent-factcheck rows are no longer on screen because their beat was cut. They remain true (parent factcheck is authoritative); they are simply not repeated in this Short.

- Parent row 15 line about `--limit 3 --dry-run` (B10 Your-Turn's specific exercise) — B10 dropped.
- Parent row 19–20 output-artifacts tree walk-through — B07 dropped.
- Parent rows 17–18 error/exit-code behaviours — never in the parent narration either.

## Numbers double-checked (still on screen in this Short)

- **12 GB** — `du -sh svg/` on the shared tree.
- **2.4 M files** — `build_icon_set.py:5-6` docstring.
- **9.1 GB** — the material-design line; retained in the verdict.
- **7,330 / 376 / 6,954** — from `icons.json → count` and a live sum.
- **528 px / 44 pt** — from `icons.json → render.line_44pt_px` and `RENDER_PX_FOR_44PT`.
- **30 MB** — from `du -sh icons`.

## Known limitations

Same as the parent vertical, unchanged here:

- **`icons/` numbers may drift** — a future run against a changed `svg/` will produce different counts.
- **No re-cut** — the shipped `icons/` set was NOT overwritten during this build. Every relevant capture uses `--dry-run`.
- **`heroicons` duplication** — we quote the module's own reason; we did not enumerate the concept overlap set.
- **Legacy checkers absent** — see `TYPECHECK.md`.

## No claims requiring correction

No claim in this Short goes beyond what the source files support. No dated numbers other than the icon counts (snapshotted here) and the `du -sh` disk sizes.
