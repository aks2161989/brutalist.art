# SCRIPT — Brutalist Command: art icons — Short

7 beats · 107.6 s · Liam (in for Bear) · Kokoro `am_onyx` · @HumanitariansAI.
Narration below is the actual audio in the Short — reused byte-for-byte from
the parent's per-beat MP3s. No line was regenerated or truncated.

## B00 — ASK (cold open) · 16.17 s

> Sawubona, this is Liam, in for Bear. There are over seven thousand icons in
> Brutalist. Nobody remembers them. So when you need a mark for a beat, the
> first move is not to draw. It is to search. Art icons is the library-first
> check that stops one-off scribbles from piling up in svg.

Visual: `ClaudeComposerAsk916` — greeting types above the composer, ask lands,
result lines cascade (7,330 count · IDF ranking · three aliases).

## B01 — BLUF (hesitant writer) · 12.17 s

> Watch the writer walk this back. Art icons does not draw a new icon for you.
> It finds an existing one, from the seven-thousand icon set. Same command,
> different job — and it is the difference this whole reel turns on.

Visual: `BrutalistHesitantWriter916` — "art icons / draws / new icons" is
typed then corrected in place to "art icons / finds / existing icons."

## B04 — MECHANISM (the ranker) · 18.63 s

> The ranker has one job: put the right hit at the top. Four rules, in order
> of trust. Exact name beats every-word-present, beats name-prefix, beats
> token-hit. Then it re-weights by inverse document frequency. That means a
> rare word like sankey outranks a common word like flow, so 'sankey flow'
> finds chart-sankey and not every flower in the set.

Visual: `ClaudeCodeBeat916` — four ranking rules + IDF one-liner.

## B05 — WORKED EXAMPLE ("money") · 17.08 s

> Here is the shape on a real query. Dot slash art icons quote money quote.
> Thirty-one hits. Top ten shown. First hit is money-square from Iconoir.
> Then banknote, coins, wallet from Lucide. Each line shows the name, the
> source pack, and the svg path. The tokens underneath tell you which words
> the ranker matched.

Visual: `ClaudeCodeBeat916` — verbatim capture of `./art icons "money"`, top 10.

## B08 — FALSIFIABILITY (the miss) · 17.54 s

> And here is what a miss looks like. Quantum entanglement. No match. The
> tool does not silently return empty. It prints an instruction: a miss is
> not a licence to draw. Try a nearby concept. Compose two icons. Or accept
> that the idea is not iconographic. Exit code zero, because the answer
> 'nothing fits' is the real answer.

Visual: `ClaudeCodeBeat916` — miss message in terracotta, three-line doctrine
below, exit code 0.

## B09 — VERDICT (the whole surface) · 20.46 s

> So the surface. Bare art icons prints the info banner and exits. A query
> searches the whole set with IDF ranking. Dash dash check answers
> is-it-in-the-set. Dash dash show hands you the raw SVG. Dash dash brands
> narrows the corpus to the three hundred and seventy-six logos. Three
> aliases all point at the same script. And a miss is a real answer, not a
> licence to draw.

Visual: `ClaudeVerdictArtifact916` — 7-line artifact card covering bare
invocation, query, `--check`, `--show`, `--brands`, aliases and the miss.
This card names and defines every flag that the dropped beats demonstrated,
so the summary is self-contained.

## B11 — OUTRO (title restate) · 5.58 s

> Brutalist Command: art icons. Liam, in for Bear, for at Humanitarians A I.

Visual: `ClaudeTitleOutro916` — serif title, `@NikBearBrown` handle
(hardcoded per OUTRO-LOCK.md), slug-seeded mascot.

## What is NOT in the Short

The following parent-long beats are dropped from this cut and their subject
matter is not spoken:

- B02 — dispatcher case-statement code walk (`art:60-63`, `exec python3 …`).
- B03 — `icons/icons.json` geometry walkthrough (viewBox, stroke, `render` block, sample records).
- B06 — `--check` and `--show` worked examples (`brain-circuit`/`database`/`bogus-icon-name` run, raw SVG print).
- B07 — `--brands` filter worked example (`./art icons "github" --brands` → 2 hits).
- B10 — "Your turn" paste-ready audit prompt (four search runs + alias diff).

These belong in the 16:9 long. The verdict (B09) names every deferred flag
by name and defines it in one line, so the Short remains a self-contained
high-level answer to "what does `./art icons` do and when is it useful?"
