# FACTCHECK — Brutalist Command: art help (9:16 Short)

The Short is a whole-beat cut of the parent vertical companion. Every retained
beat's audio and video was copied unchanged; no narration was regenerated.
Therefore every claim visible or audible in the Short was already verified in
the parent's factcheck. This file records only what applies to the *retained*
beats — dropped-beat claims are out of scope for the Short.

Parent factcheck reference:
`youtube/brutalist/claude-liam-brutalist-command-help/vertical/FACTCHECK.md`
(parent `run_id 8bd2a005d9984f9490ef7370c7bb2b2f`, 2026-09-09).

All claims verified against `toolkit/art` at
`episode.source_sha256 = 387d12c338fe3e8e05a3c2202be86ea81beaf548c2fd11ec3ee4876694f8b562`.

## Retained claims and their evidence

| # | Beat | Claim | Source | Verified in parent |
|---|---|---|---|---|
| 1 | B00, B05 | Four aliases (empty, `-h`, `--help`, `help`) share one case branch | `art:38` — `""|-h|--help|help)` pattern | ✅ ran all four, identical stdout, exit 0 (parent `demo/RUN-LOG.md`) |
| 2 | B00, B03 | Help text is not stored — it is the file's own header, extracted at run time | `art:39` — `sed -n '2,18p' "$ART_HOME/art" \| sed 's/^# \{0,1\}//'` | ✅ diff of the sed pipeline against `./art help` output — identical |
| 3 | B00, B04 | Output is 17 lines | `wc -l < <(./art help)` returned 17 | ✅ parent `demo/RUN-LOG.md` |
| 4 | B04 | 17-line usage sheet content matches the file's rendered output | shell diff against `demo/RUN-LOG.md` | ⚠️ minor: B04's code card lightly abbreviates a few descriptive tails to fit the frame; command tokens and row order are verbatim. Same trade-off carried from the parent film — flagged there for human reviewer. |
| 5 | B06 | `./art --list` prints the skills table with 16 rows | `art:41-59` — the `--list\|list)` branch | ✅ ran and captured; 16 skill rows plus header |
| 6 | B09 | An unknown token exits 2 with one-line stderr pointing at `--list` | `art:106-108` — the `*)` fall-through | ✅ `./art bogus`; captured message + exit 2 |
| 7 | B09 | `./art <skill> --help` opens that skill's SKILL.md via `$PAGER` (defaults to `cat`) | `art:109-111` — `exec "${PAGER:-cat}" "$dir/SKILL.md"` | ✅ ran `./art ai-explainer --help`; first two lines match `skills/make/ai-explainer/SKILL.md` frontmatter |

Claims associated with B02 (framework), B07 (falsifiability), B08 (recovery),
and B10 (your-turn prompt) are only visible in the parent film; they are not
part of the Short and are not re-restated here.

## Not claimed / carefully avoided

Same as parent — no claim about paid API, uploads, or that this Short is
published anywhere. The output lives in `exports/short/` for review only.
