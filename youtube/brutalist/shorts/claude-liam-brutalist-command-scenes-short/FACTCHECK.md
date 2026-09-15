# FACTCHECK — Brutalist Command: art scenes — Short

Every factual, numeric, or structural claim in the retained narration or
on-screen text traces back to a source in the current toolkit at
`.repoloop/shorts/workspaces/claude-liam-brutalist-command-scenes-short/toolkit/`.

Toolkit revision under test (per SOURCE-SNAPSHOT.json):
`revision.commit = ba2d0e0f043f5b3b35a50d336e0fc66fbfecfc0c`.
`episode.parent_master_sha256 = 06eb7031e272bac545d3a16c0ce48e0ebaeb9a3fedaeeb0b16d294233ce3aea8`
(this Short reuses the parent's native portrait beats without re-rendering).

## Facts that remain in the Short's retained beats

| Claim (as it lands on screen or in narration) | Retained beat | Source | Verified how |
|---|---|---|---|
| 620 renderable compositions in Brutalist | B00, B01, B04 (implicit) | `runtime/remotion/src/scenes.json` after `./art scene-index` | `python3 -c "import json; print(len(json.load(open('runtime/remotion/src/scenes.json'))['scenes']))"` → `620` |
| Aliases `scenes` / `scene` / `scene-search` collapse into the same code path | B00 (spoken) | `toolkit/art:67-70` — one `case` pattern, one `exec python3 scene_search.py` | Read the dispatcher file; verified in parent's SOURCES.md hash `9bb77a7c…` |
| The ranker's three trust tiers score 3 / 2 / 1 points | B04 | `runtime/scripts/scene_search.py` — `n += 3 * weight(t)` on id, `2` on synonyms, `1` on the haystack | Read the file (parent SOURCES.md hash `8ec4ece5…`) |
| Derived-only entry loses 0.5 points | B04 | `scene_search.py` — `if s.get("desc_source") == "derived": n -= 0.5` | Read the file |
| IDF weight tiers: df ≤ 12 → 2.0, df ≤ 60 → 1.5, else 1.0 (rare word wins) | B04 | `scene_search.py` `weight()` | Read the file |
| `./art scenes "sankey flow"` returns FinanceSankey at 8.5 followed by three SourceFlow variants at 4.5 | B05 | Verbatim `demo/RUN-LOG.txt` §2 in the parent workspace | Captured against the toolkit's `scenes.json` — the parent's factcheck cites the same run |
| A genuine miss on `yak shaving trombone` exits status 1 and prints "That is a PUNT. Do not slate it — design the component…" | B08 | `scene_search.py` — `sys.exit(1)` after the punt print block | Captured verbatim in the parent's `demo/RUN-LOG.txt` §10 |
| A miss appends a row to `TEMPLATE-MISSES.md` (unless `--no-log`) | B08 | `scene_search.py` writes to `HERE.parents[2] / "TEMPLATE-MISSES.md"` | Read the file; the ledger row shown in B08 quotes the tool's own message |

## Claims from dropped beats — not asserted anywhere in the Short

The following facts appeared only in beats the Short cut. They are NOT
asserted in this cut, so no factcheck coverage is required here (they remain
verified in the parent film's FACTCHECK.md and belong to the 16:9 long):

- The exact dispatcher location `art:67-70` on screen (B02).
- `scenes.json` schema and the sample record (B03).
- `--check` renderable/not-renderable behaviour with the six-prop preview (B06).
- `--undocumented` → 118 derived scenes (B06).
- Alias byte-identical output across three runs (B07).
- Stop-word guard rejects `the and for with that this` (B07).
- Whole-surface seven-line verdict card (B09).
- The full paste-ready `Your Turn` exercise (B10).

## Deliberate corrections vs the source (retained beats only)

- **B04 "id > synonym > haystack, IDF re-weighted" phrasing.** The script
  itself does not label the tiers this way; the narration names them so viewers
  can hold the three levels in their head. The on-screen code is the raw
  scoring so the narration is falsifiable against the source.
- **B05 rounded score display.** The tool prints `[ 8.5]` and `[ 4.5]`
  verbatim; the narration says "eight point five" and "four point five".

## Voice and identity

- Narrator: Kokoro `am_onyx`, Liam in for Bear. No ElevenLabs, no paid TTS.
- Persona/greeting language is unchanged from the parent (`Namaste, Liam`).
- Outro handle `@NikBearBrown` is hardcoded by `ClaudeTitleOutro916` per
  `OUTRO-LOCK.md` — flagged in the parent's FACTCHECK for human review before
  publication; unchanged in this Short.

## Human review still pending

Bear has not yet signed off on the parent or this Short. Nothing has been
uploaded or published. `art submission` and scheduling remain separate human
workflows.
