# FACTCHECK — Brutalist Command: art scene-index

Every on-screen claim traced to a source in this workspace. Numbers were
captured against the isolated toolkit at
`.repoloop/workspaces/claude-liam-brutalist-command-scene-index/toolkit`
on 2026-09-09. Sources are read-only for this run.

## The dispatcher

- **Location: `art:71-74`**
  Source: `toolkit/art` lines 71-74 verified by `grep -n "scene-index" art`.
  Case pattern is exactly `scene-index)`; no `|` fall-through.
  Exec target: `python3 "$ART_HOME/runtime/scripts/build_scene_index.py"`
  with `"$ART_HOME/runtime/remotion/src"` + `--todo` + `"$@"`.

- **No aliases.**
  Verified by scanning `art` for every case-pattern containing "scene":
  `scenes|scene|scene-search)` (art:67-70, goes to `scene_search.py`) and
  the single-pattern `scene-index)` (art:71-74). The two branches never
  overlap. `./art scene-index` and its bare python invocation are the only
  paths to `build_scene_index.py`.

## The tool's own doctrine (the LAW quotes on screen)

Verbatim from `runtime/scripts/build_scene_index.py`, lines 1-36:

> "THE LAW: a scene is usable only if Root.tsx declares a `<Composition id="...">`
> for it. A .tsx file in scenes/ is NOT enough — several exist that no
> composition references, and they are invisible to the pipeline. This
> index is generated from Root.tsx for that reason: registered is the only
> truth."

> "THE INDEX IS THE SEARCH SURFACE. scene_search.py can only find a scene
> through the text stored here, so this script's job is to carry as much
> of the component's own account of itself as possible…"

## The numbers

All captured verbatim on this workspace at 2026-09-09, 08:52 local time.

| Claim on screen | Source | Value |
|---|---|---|
| `619 renderable` | `./art scene-index` stdout line 1 | 619 |
| `118 undocumented` | `./art scene-index` stdout line 1 | 118 |
| `0 unresolved (no backing file)` | `./art scene-index` stdout line 1 | 0 |
| `118 scenes need a header sentence` | `./art scene-index` stdout line 2 | 118 |
| `19%` (118/619) | derived from previous two numbers | 19.06% ≈ 19% |
| scenes.json size | `ls -l runtime/remotion/src/scenes.json` | 564,863 bytes |
| SCENE-DOC-TODO.md size | `ls -l SCENE-DOC-TODO.md` | 12,548 bytes |
| exit status of bare invocation | `./art scene-index; echo $?` | 0 |

## The two sample records (B06)

- **`ClaudeComposerAsk`** — `documented=true`, `desc_source="header"`.
  Verified by scanning `scenes.json` for the id.
  File: `scenes/ClaudeComposerAsk.tsx`. Backing file has a JSDoc header
  starting with the exact quoted sentence about the ASK beat.

- **`CodexComposerAsk`** — `documented=false`, `desc_source="derived"`.
  Verified by scanning `scenes.json`. File: `scenes/CodexComposerAsk.tsx`.
  Backing file has NO `/** … */` header attached to the exported const;
  desc string on screen (`"(derived — no header in the component)
  CodexComposerAsk, registered under 'Codex-Templates'; keywords: ask
  codex composer; on screen: 'Inspected the failing path'; …"`) matches
  the record verbatim, ellipsis added only for line breaks in the code card.

## SCENE-DOC-TODO.md sample rows (B07)

Verbatim from `SCENE-DOC-TODO.md` head (first 6 rows after the header).
The rendered card shows the first five rows plus a placeholder for the
remaining 113 (118 - 5). All shown rows are exact:

- `A5aFrameworkChoice | scenes/A5aFrameworkChoice.tsx | A5a-WrapIt`
- `A5aInputWiring | scenes/A5aInputWiring.tsx | A5a-WrapIt`
- `A8DeliverableMap | scenes/A8DeliverableMap.tsx | A8-ShipIt`
- `AdaptiveTherapyRevolution | AdaptiveTherapyRevolution.tsx | claude-liam …`
- `AttritionChain | deckPatterns.tsx | rhetorical patts.`

The "rhetorical patts." label in the card is a compressed rendering of
the real Folder column value
`claude-liam-claude-science — rhetorical patterns (deckPatterns, responsive)`
truncated to fit the code-card width. The other three columns render the
Folder value verbatim, with two ellipses where the string exceeds the
card width. Not a false claim — a display truncation.

## The falsifiability demo (B08)

Reproducible in `demo/RUN-LOG.txt`. A scratch toolkit was built at
`/tmp/claude-501/scene-index-demo/fake_toolkit/runtime/remotion/`:

- `src/scenes/` contains `ClaudeComposerAsk.tsx` **and** `OrphanNewScene.tsx`
  (`ls src/scenes` verified two entries).
- `src/Root.tsx` registers `ClaudeComposerAsk` only (`grep -c '<Composition'`
  returned `1`).
- `./art scene-index` (the same script, `runtime/scripts/build_scene_index.py`,
  pointed at this scratch tree) prints `1 renderable, 0 undocumented, 0 unresolved`.
  scenes.json contains exactly `['ClaudeComposerAsk']`; `OrphanNewScene` is absent.
- After a script-generated edit adds a `<Composition id="OrphanNewScene" …/>`
  block to `Root.tsx`, `grep -c '<Composition'` returns `2`.
- Re-running the script prints `2 renderable, 0 undocumented, 0 unresolved`.
  scenes.json now contains both ids.

That is the LAW in flight — registered is the only truth — and it is
reproducible on any scratch tree.

## The hard failure (RUN-LOG only, not a beat)

Not shown on screen; captured in the run log as the "wrong directory"
recovery path:

- `python3 runtime/scripts/build_scene_index.py /tmp/no-such-dir --todo`
  raises `FileNotFoundError: [Errno 2] No such file or directory:
  '/private/tmp/no-such-dir/Root.tsx'` from line 43 of the script
  (`root_src = (SRC / "Root.tsx").read_text()`), exits with status 1.
  Recovery: use `./art scene-index` — the shell wrapper always passes
  the correct `runtime/remotion/src` path.

## What is NOT on screen (integrity notes)

- No claim of a fresh network install or a paid API. Every command is
  local.
- The "620 in scenes episode" parenthetical on B05 references a
  previously delivered episode's workspace, not this run's output. The
  numbers on screen for THIS run are 619 / 118 / 0.
- The outro card uses the locked `ClaudeTitleOutro` with a hard-coded
  `@NikBearBrown` handle per `OUTRO-LOCK.md`. The composer beats and body
  chip use `@HumanitariansAI` per this playlist's channel adaptation.
  Flagged for the human reviewer.

## Corrections applied vs the source

None. The source is the tool's own dispatcher, source file, and output.
The narration paraphrases the tool's own comments in Teardown register;
verbatim quotes appear on code cards, cited to `build_scene_index.py`.
