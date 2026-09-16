# FACTCHECK — Brutalist Command: art help

All claims verified against `toolkit/art` at
`episode.source_sha256 = 387d12c338fe3e8e05a3c2202be86ea81beaf548c2fd11ec3ee4876694f8b562`
in this invocation (run_id `8bd2a005d9984f9490ef7370c7bb2b2f`, 2026-09-09).

## Claims and their evidence

| # | Claim | Source | Verified |
|---|---|---|---|
| 1 | Four aliases (empty, `-h`, `--help`, `help`) share one case branch | `art:38` — `""|-h|--help|help)` pattern | ✅ ran all four, identical stdout, exit 0 (see `demo/RUN-LOG.md`) |
| 2 | Help text is not stored — it is the file's own header, extracted at run time | `art:39` — `sed -n '2,18p' "$ART_HOME/art" \| sed 's/^# \{0,1\}//'` | ✅ diff of `sed -n '2,18p' art \| sed 's/^# \{0,1\}//'` against `./art help` output — identical |
| 3 | Output is 17 lines | `wc -l < <(./art help)` returned 17 | ✅ recorded in `demo/RUN-LOG.md` |
| 4 | Byte count of output is 1225 | `wc -c < <(./art help)` returned 1225 | ✅ recorded in `demo/RUN-LOG.md` |
| 5 | All four aliases exit 0 | `./art help &>/dev/null; echo $?` returned 0 for each | ✅ recorded |
| 6 | `./art --list` prints the skills table (16 rows) — different scope from `help` | `art:41-59` — the `--list\|list)` branch prints two-column table | ✅ ran and captured; 16 skill rows plus header |
| 7 | An unknown token exits 2 with one-line stderr pointing at `--list` | `art:106-108` — the `*)` fall-through branch: `echo "art: unknown skill '$cmd' (try ./art --list)"; exit 2` | ✅ `./art bogus`; captured message + exit 2 |
| 8 | `./art <skill> --help` opens that skill's SKILL.md via `$PAGER` (defaults to `cat`) | `art:109-111` — `exec "${PAGER:-cat}" "$dir/SKILL.md"` | ✅ ran `./art ai-explainer --help`; first two lines match `skills/make/ai-explainer/SKILL.md` frontmatter (`---\nname: ai-explainer`) |
| 9 | The 17-line usage sheet quoted in B04 matches the file's rendered output character-for-character | shell diff against `demo/RUN-LOG.md` | ⚠️ minor: in B04 the code card lightly abbreviates a few descriptive tails to fit the frame (e.g. drops "— run BEFORE authoring a beat", drops "(cap check + auto-shorten)"). The command tokens themselves and the row order are verbatim. Full verbatim output is captured in `demo/RUN-LOG.md` — that is the authoritative reference. Trade-off flagged for human reviewer. |

## Not claimed / carefully avoided

- No claim that Brutalist has "unlimited Claude" — the file itself says "Free by default" only for local Kokoro/Manim/Remotion.
- No claim that this is a fresh network install; `./art help` was run on the installed isolated copy.
- No claim that the mp4 is on YouTube. Output lives in `exports/` for human review only.

## Corrections applied to the script

None during this session — B04 abbreviation flagged above, not corrected, since the demo log carries the verbatim.

## Sources of the demo runs

- `demo/RUN-LOG.md` (this reel) — captured 2026-09-09 in the isolated workspace.
- All commands were run against `$ART_HOME` = the isolated toolkit copy for this episode, not the public toolkit.
