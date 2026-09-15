# FACTCHECK — Brutalist Command: art icons — Short

This Short reads only 7 of the parent long's 12 beats and adds no new claims.
Every factual claim spoken in this Short is a subset of the parent's
FACTCHECK, verified against the same source files. No fact has been
re-verified from scratch for the Short (audio and visuals are byte-for-byte
from the parent), but every claim's original evidence is cited below so
the trace stays intact.

## Claims spoken in THIS Short (7 kept beats) → parent evidence

| Beat | Claim (as spoken) | Source of truth | Parent FACTCHECK row |
|---|---|---|---|
| B00 | "over seven thousand icons in Brutalist" | `icons/icons.json → "count": 7330` | #3 |
| B00 (output) | `7,330 icons — 376 brand/logo, viewBox 0 0 24 24, stroke 2` | `icons/icons.json → count / geometry`; `sum(1 for i in icons if i['brand'])` = 376 | #3, #4, #5, #6 |
| B00 (output) | `ranked: exact name > every word > prefix > token hit (IDF)` | `runtime/scripts/icon_search.py:14-16` docstring + `rank()` body | #7 |
| B00 (output) | `aliases: icons, icon, icon-search — same case branch, same output` | `art:60-63` case block | #1, #2, #22 |
| B01 | "art icons finds existing icons" / "from the seven-thousand icon set" | Combined restatement of #3 + `icon_search.py` search-not-generate design | #3 (plus icon_search.py has no create/write path) |
| B04 | "exact name beats every-word-present, beats name-prefix, beats token-hit" | `runtime/scripts/icon_search.py:14-16` + `rank()` implementation | #7 |
| B04 | "re-weights by inverse document frequency" / `idf = { w: math.log((n + 1) / (df.get(w, 0) + 1)) + 1 for w in words }` | `runtime/scripts/icon_search.py:62` | #8 |
| B04 | "'sankey flow' finds chart-sankey and not every flower in the set" | `demo/RUN-LOG.md` live capture | #19 |
| B05 | `./art icons "money"` → "Thirty-one hits. Top ten shown. First hit is money-square from Iconoir. Then banknote, coins, wallet from Lucide." | `demo/RUN-LOG.md` live capture | #18 |
| B08 | `./art icons "quantum entanglement"` → "No match … Exit code zero" | `demo/RUN-LOG.md` live capture; `icon_search.py:144-148` control flow | #15, #21 |
| B08 | "A miss is NOT a licence to draw a one-off." (on-screen) / "a miss is not a licence to draw" (spoken) | `runtime/scripts/icon_search.py:145-147` | #14 |
| B09 | "Bare art icons prints the info banner and exits." | `runtime/scripts/icon_search.py` main() when argv is empty | Consistent with parent B09 verdict — parent FACTCHECK does not enumerate the bare-invocation case separately; the info banner text lives in icon_search.py's main. |
| B09 | "A query searches the whole set with IDF ranking." | Same as #7, #8 | #7, #8 |
| B09 | "Dash dash check answers is-it-in-the-set." | `runtime/scripts/icon_search.py:119-129` | #10 |
| B09 | "Dash dash show hands you the raw SVG." | `runtime/scripts/icon_search.py:112-117` | #11 |
| B09 | "Dash dash brands narrows the corpus to the three hundred and seventy-six logos." | `runtime/scripts/icon_search.py:66-67` + brand count from #4 | #4, #12 |
| B09 | "Three aliases all point at the same script." | `art:60-63` | #1, #2, #22 |
| B09 | "a miss is a real answer, not a licence to draw." | Same as B08 | #14 |
| B11 | "Brutalist Command: art icons. Liam, in for Bear, for at Humanitarians A I." | No factual claim; presenter + channel attribution as per OUTRO-LOCK.md | — |

## Claims NOT spoken in this Short (present in the parent long, dropped here)

The following parent claims are dropped because their beats (B02, B03, B06,
B07, B10) were cut. They remain fact-checked in the parent's FACTCHECK.md
but are not asserted by this Short — the Short takes on no residual burden
of proof for them:

- Dispatcher `exec python3 "$ART_HOME/runtime/scripts/icon_search.py" "$@"`
  literal line (B02 code card).
- `icons/icons.json → "render": {"line_44pt_px": 528}` "44pt at 528px" claim
  (only shown as text in B03 code card, not narrated).
- Sample icon record shapes with `tokens: [...]` and `file: "svg/..."` (B03
  code card).
- `--check` output row shape ("IN SET concept" vs "not in the set"
  formatting), B06.
- `--show` verbatim SVG element for `database` (B06).
- `github --brands` → 2 hits (`brand-github`, `brand-github-copilot`), B07.
- `--no-brands` narrows to 6,954 concept icons (B07 code card; note: the
  B09 verdict spoken narration DOES restate "6,954 concept icons", so this
  number IS spoken in this Short — see B09 verdict row above).
- Long paste-ready audit prompt for `./art icons` (B10 composer).

## Numbers double-checked (unchanged from parent)

- **7,330** icons — `icons/icons.json → count`.
- **376** brand/logo icons — computed live via `sum(1 for i in icons if i['brand'])`.
- **6,954** concept icons — 7,330 − 376 (quoted in B09 verdict card).
- **31** hits on `./art icons "money"` — parent's `demo/RUN-LOG.md` capture.

## Honest caveats

- The parent long shipped as Ep 24 with all 22 rows verified; this Short did
  not re-run those verifications, but its narration is a strict subset of
  the parent's verified narration.
- Icon totals could drift if `build_icon_set.py` is rerun on a different SVG
  set. The Short's numbers are the same snapshot as the parent
  (`icons/icons.json` at commit `ba2d0e0f043f5b3b35a50d336e0fc66fbfecfc0c`
  per `SOURCE-SNAPSHOT.json`).
- The B09 verdict names features (`--show`, `--brands`, aliases) that this
  Short does not demonstrate on-screen. Definitions are one-liners drawn
  from the same source files as the parent long's dedicated beats; a viewer
  who wants to see them actually run is directed by the Short's editorial
  scope to the 16:9 long.
