# FACTCHECK — Brutalist Command: art scenes

Every factual, numeric, or structural claim in the narration or on-screen has to
be traceable to a source in the current toolkit at
`.repoloop/workspaces/claude-liam-brutalist-command-scenes/toolkit/`. Anything
that cannot be traced was cut or reworded before the beat sheet was frozen.

Toolkit revision under test: `revision.commit = ba2d0e0f043f5b3b35a50d336e0fc66fbfecfc0c`.
Source snapshot: `SOURCE-SNAPSHOT.json` in the reel root.

## Frozen facts

| Claim (as it lands on screen or in narration) | Source | Verified how |
|---|---|---|
| Aliases `scenes`, `scene`, `scene-search` collapse into one `case` branch at `art:67-70` and `exec` the same script | `toolkit/art` lines 67-70 (`scenes|scene|scene-search) ... exec python3 "$ART_HOME/runtime/scripts/scene_search.py" "$@"`) | Read the dispatcher file (SHA-256 `4759b441...` cited in SOURCE-SNAPSHOT) |
| The library holds 620 renderable compositions | `runtime/remotion/src/scenes.json` after `./art scene-index` in this workspace | `python3 -c "import json; print(len(json.load(open('runtime/remotion/src/scenes.json'))['scenes']))"` → `620` |
| 118 scenes run on derived search text (no header comment) | `./art scenes --undocumented` output — line 1 | Captured verbatim in `demo/RUN-LOG.txt` |
| The three trust tiers score 3 / 2 / 1 points | `scene_search.py` lines 111-125 — `n += 3 * weight(t)` on id, `n += 2 * weight(t)` on synonyms, `n += 1 * weight(t)` on the haystack | Read the file (source SHA `8ec4ece5...`) |
| A derived-only entry loses 0.5 points | `scene_search.py` line 123-124 — `if s.get("desc_source") == "derived": n -= 0.5` | Read the file |
| IDF re-weighting: df ≤ 12 → 2.0, df ≤ 60 → 1.5, else 1.0 | `scene_search.py` lines 107-109 (`weight()`) | Read the file |
| `sankey flow` returns FinanceSankey at score 8.5, followed by three SourceFlow variants and CwcFanOutFlow at 4.5 | Verbatim `./art scenes "sankey flow" --top 5 --no-log` output | Captured in `demo/RUN-LOG.txt` §2 |
| `bar chart` returns BarChart as first hit at score 9.0 | Verbatim output of `./art scenes "bar chart" --top 5 --no-log` | Captured in `demo/RUN-LOG.txt` §3 |
| A pure stop-word query is rejected with the "search for the mechanic, not the sentence" hint | `scene_search.py` line 97 | Verbatim capture in `demo/RUN-LOG.txt` §5 |
| `--check` names its input `RENDERABLE` with aspect + first six props, or `NOT RENDERABLE — no <Composition> in Root.tsx. Authoring this is a punt.` | `scene_search.py` lines 80-87 | Captured in `demo/RUN-LOG.txt` §4 |
| `--undocumented` lists compositions where `desc_source == "derived"` | `scene_search.py` lines 69-77 | Captured in `demo/RUN-LOG.txt` §6 |
| Aliases return byte-identical output on the same argv | `art:67-70` — all three aliases fall into the same `case` and `exec` the same script | Captured across three runs in `demo/RUN-LOG.txt` §8 |
| A genuine miss exits with status 1 and prints the punt instruction | `scene_search.py` line 162 (`sys.exit(1)` after `print("... PUNT ...")`) | Captured for `yak shaving trombone` in `demo/RUN-LOG.txt` §10 |
| A miss appends a row to `TEMPLATE-MISSES.md` at `HERE.parents[2] / "TEMPLATE-MISSES.md"` unless `--no-log` is passed | `scene_search.py` lines 42, 131-155 | Read the file; ledger text on B08 is quoted verbatim from the tool's message |
| `--reel <path>` tags the miss row with the reel that needed it | `scene_search.py` line 66 + 149-150 | Read the file |

## Deliberate corrections vs the source

- **Line wording — "id > synonym > haystack, IDF re-weighted".** The
  script itself does not label these tiers; the rewrite names them so viewers can
  hold the three levels in their head. The verdict card and the FRAMEWORK code
  card both use this labelling; the code in B04 shows the raw scoring so the
  narration is falsifiable against the source.
- **`sankey flow` example.** The rewrite highlights this pairing to make the
  point about rare-word wins. The demo captured in `demo/RUN-LOG.txt` §2 is what
  the tool actually prints; the narration cites the exact scores (8.5 / 4.5) that
  the tool computed in this workspace.

## Deliberate omissions

- Higgsfield, ElevenLabs, Cowork, Drive uploads, and Anthropic account or key
  provisioning are all out of scope for this command reel and are not mentioned.
- No fabricated professor Bear approval, no invented signatures, no claim that
  the film has been reviewed or published — the outro on-screen handle is the
  hardcoded @NikBearBrown card (per OUTRO-LOCK); the folder chip is
  @HumanitariansAI (playlist adaptation).
- The `--top` default value (`8`) is not mentioned in narration but is used
  when relevant (`--top 5` demos); the flag itself is out of scope for the
  reel's teaching arc.

## Known gaps (recorded honestly)

- `scripts/type_check.py` referenced in `skills/make/ai-explainer/SKILL.md` is
  not present in this toolkit. GATE T's automated pass is unavailable; a manual
  visual typography review is documented in `TYPECHECK.md`.
- `reference/type-spec.md` and the standalone `kerning` skill are similarly not
  shipped; the same manual pathway is used.
- `ILLUSTRATIONS.md` is referenced by SKILL.md but not present. Not blocking
  for this reel (no new illustration authored).
