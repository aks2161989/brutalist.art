# FACTCHECK — Brutalist Command: art keys

Every specific claim in the narration and on the code cards was verified
against the actual source files listed in SOURCES.md and the verbatim
output in `demo/RUN-LOG.txt`.

## Verified against the isolated toolkit sources

| Claim in the reel | Where in the source | Verified |
|---|---|---|
| The command is one dispatcher case at `art:103-104` that execs `python3 runtime/scripts/check_keys.py` with `"$@"` forwarded. | `art` lines 103-104, quoted verbatim in `demo/RUN-LOG.txt § 4`. | ✅ |
| `check_keys.py` is 83 lines. | `wc -l runtime/scripts/check_keys.py` → `83`. | ✅ |
| The docstring says: "Exit 0 if every present key is valid; 1 if any present key is invalid." | `check_keys.py:9-10`, quoted in `demo/RUN-LOG.txt § 3`. | ✅ |
| Currently the script only checks one service: `higgsfield` (login-based). | `check_keys.py:44-57` — the only `row(…)` calls are inside the higgsfield block. | ✅ |
| The higgsfield probe runs `higgsfield account status` with a 25 s timeout via `subprocess.run`. | `check_keys.py:44-46`. | ✅ |
| Three status paths on the higgsfield probe: `valid` (rc == 0), `invalid` (rc ≠ 0), `unset` (FileNotFoundError → CLI not installed). A fourth `warn` path exists for any other exception and marks the whole run "inconclusive". | `check_keys.py:47-57`. | ✅ |
| The `unset` detail message reads "CLI not installed — AI video beats use free path (Ken Burns stills)". | `check_keys.py:53-54`, matches `demo/RUN-LOG.txt § 2` byte-for-byte. | ✅ |
| Setting `ART_HOME` overrides the repo root. Absent, `REPO` defaults to `Path(__file__).resolve().parents[2]`. | `check_keys.py:18`. | ✅ |
| `.env` is loaded via `load_env()` and populates `os.environ` with `setdefault` — the shell environment wins. | `check_keys.py:20-30`, comment `# shell wins`. | ✅ |
| `.env` is read but **never printed**. Redaction verified by `grep -c 'this-should-never-print'` → `0`. | `demo/RUN-LOG.txt § 5`. | ✅ |
| No `SI_KEY` / `SI` env var probe exists in `check_keys.py`. | `grep -in 'si' runtime/scripts/check_keys.py` → no matches. | ✅ (see drift note) |
| Free-by-default: Kokoro/Manim/Remotion require no keys. | `check_keys.py:3` + `CLAUDE.md` § "Free by default (Fellow Tier)". | ✅ |

## Design tension / documentation drift — the Teardown moment (B08)

Two small doc/reality drifts are called out honestly in the narration.
Neither is treated as a bug that needs to be fixed in this reel — the
purpose is to teach fellows to read the code, not the marketing copy.

1. **Exit code drift.** The docstring says "Exit 0 if every present key is
   valid; 1 if any present key is invalid." In the actual code, line 40
   declares `any_invalid = False` and **never reassigns it**. The higgsfield
   `invalid` branch just appends a red row and moves on. Result: an invalid
   higgsfield row still exits 0 with the message "All present keys
   validated." Verified in `demo/RUN-LOG.txt § 1`: the run shows a red
   `❌ invalid` row followed by the green "All present keys validated."
   footer and `[exit 0]`. The docstring's contract is not enforced.

2. **`art` help drift.** The dispatcher's help block (`art:20`) advertises
   `./art keys — validate optional keys (Higgsfield login, SI key)`. The
   current `check_keys.py` has **no `SI` / Sound Imagination probe**.
   `grep -in 'si\b' runtime/scripts/check_keys.py` returns zero matches.
   Either a probe was removed and the help wasn't refactored, or a probe
   was planned and never landed. Either way, "SI key" is a promise the
   script does not currently keep. `art` help vs. script surface: known
   drift, harmless because no build depends on the second row.

Both drifts are the Teardown point of B08: the docstring is a wish, the
help line is a wish; the actual script is one live probe of one optional
CLI, and its exit code is always 0 unless the whole probe itself throws.

## Narration guardrails (things the reel deliberately does NOT claim)

- We never say "Higgsfield is required." (It is opt-in; the free path runs
  silently when it is absent.)
- We never say "art keys unlocks features." (It reports readiness for one
  optional CLI; the toolkit's own features unlock without it.)
- We never promise Claude account behavior beyond what the local toolkit
  does. The build itself uses local Kokoro and Remotion — no paid API is
  called from any beat.
- Narration mentions ONE workstation truth (higgsfield 0.2.3 installed,
  no active login, no `.env`) but the SCRIPT and code cards do not name
  the machine's user or paths beyond the `/tmp/claude/keys-demo/` scratch
  directory shown in § 5.
- The docstring/help drifts are described neutrally as "the design tell",
  not framed as bugs to bash. The point is that fellows should trust the
  live behavior, not the advertisement — that is the Teardown register.
