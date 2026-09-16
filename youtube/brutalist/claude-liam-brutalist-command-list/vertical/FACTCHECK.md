# FACTCHECK — Brutalist Command: art --list

Every factual claim in this reel traces to a line in the toolkit or to the
captured runs in `demo/RUN-LOG.md`.

| Claim (narration / on-screen) | Source | Evidence |
|---|---|---|
| Two aliases — `--list` and bare `list` — share one branch. | `art:41` | `case` pattern `--list\|list)` matches both. |
| The `--list` branch prints a fixed 17-line table. | `art:42-58` + `demo/RUN-LOG.md` §1 | 1 `printf` header row + 16 skill `printf`s. `wc -l` = 17. |
| No file system scan, no plug-in discovery. | `art:42-58` | Only `printf` calls with hard-coded literals inside the branch body. |
| Extra positional arguments are silently ignored. | `art:41-59` + `demo/RUN-LOG.md` §3 | The branch body never references `"$@"`. `diff bare vs list foo bar` → IDENTICAL, exit `0`. |
| `./art -list` (single dash) is NOT an alias. | `art:41` (only `--list\|list)`) + `demo/RUN-LOG.md` §4 | Falls to `*)` catch-all, exits `2`, prints hint. |
| The unknown-token hint goes to **stdout**, not stderr. | `art:108` | Bare `echo` writes to stdout. `demo/RUN-LOG.md` §4-5 confirm stderr is empty. |
| Unknown token exits `2`. | `art:108` (`exit 2`) | Verified in `demo/RUN-LOG.md` §4-5. |
| The hint text is `art: unknown skill '<token>' (try ./art --list)`. | `art:108` | Verbatim in `demo/RUN-LOG.md` §4-5. |
| `./art <skill> --help` opens the skill's `SKILL.md` in `$PAGER`. | `art:109-111` | `exec "${PAGER:-cat}" "$dir/SKILL.md"`. |
| The printf format is `'%-22s %s\n'`. | `art:42-58` | Every printf in the branch uses this format string. |
| Sixteen skills are printed. | `art:43-58` | 16 `printf` calls after the header row. Header contains "SKILL" / "ROLE". |
| The 16 rows include: ai-explainer, cli-explainer, deep-explainer, anthropics, fashionista, fellows, finance, guests, nbb, hai, explainer, your-turn, logo, duration-planner, nopunt, screen-clean. | `art:43-58` + `demo/RUN-LOG.md` §1 | Verbatim first field of each printf, in the order printed. |

## Non-claims (things the reel intentionally does NOT say)

- The narration does not claim `--list` runs any skill code. It calls the
  branch a **printer**. Running a skill requires typing the skill's name
  as the first arg (falls to `*)` and `exec`s its script, unless the
  skill is a doctrine / instruction-only lane).
- The narration does not name the exact number of skills on disk under
  `skills/make/` — that count can drift as skills are added. It names
  the count in the **printed table** (16), which is what `--list` shows.
- The reel does not claim the printed order matches alphabetical or any
  particular contract. It says only that builders appear before personas
  before doctrines in the current table — which is what the file literally
  writes.

## Time-varying facts flagged

- The exact 16-row set on `main` may change as skills are added or renamed.
  The reel is honest about this — it counts what the file we authored
  against actually prints, and pins that file with the `source_sha256`
  above. If a fellow's checkout has a different row count, the reel's
  method (read the case block, count the `printf`s) still applies.

## Nothing invented

Every quoted string on screen appears verbatim in `art` or in
`demo/RUN-LOG.md`. No mocked commands, no fabricated exit codes, no
imagined error messages.
