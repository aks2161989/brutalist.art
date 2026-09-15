# SCRIPT — Brutalist Command: art icons

Narration for every beat, verbatim, in reading order. Voice: Kokoro `am_onyx`
(Liam-in-for-Bear). Same script drives both landscape and vertical cuts.

---

## B00 — ASK (cold open)

> Sawubona, this is Liam, in for Bear. There are over seven thousand icons in Brutalist. Nobody remembers them. So when you need a mark for a beat, the first move is not to draw. It is to search. Art icons is the library-first check that stops one-off scribbles from piling up in svg.

## B01 — BLUF (hesitant writer)

> Watch the writer walk this back. Art icons does not draw a new icon for you. It finds an existing one, from the seven-thousand icon set. Same command, different job — and it is the difference this whole reel turns on.

## B02 — FRAMEWORK (the dispatcher)

> The dispatcher is a single case statement in the art file. One branch matches three aliases: the word icons, the singular icon, and the long form icon-search. All three exec the same python script. Different words on your terminal, one code path underneath.

## B03 — MECHANISM (the canonical set)

> The library the script searches is a single JSON file at icons dot json. Seven thousand three hundred and thirty icons. Three hundred and seventy-six of them are brand or logo marks. Every icon is a twenty-four unit viewBox, stroke width two, currentColor. That means one component style, one accent hook. They compose.

## B04 — MECHANISM (the ranker)

> The ranker has one job: put the right hit at the top. Four rules, in order of trust. Exact name beats every-word-present, beats name-prefix, beats token-hit. Then it re-weights by inverse document frequency. That means a rare word like sankey outranks a common word like flow, so 'sankey flow' finds chart-sankey and not every flower in the set.

## B05 — WORKED EXAMPLE ("money")

> Here is the shape on a real query. Dot slash art icons quote money quote. Thirty-one hits. Top ten shown. First hit is money-square from Iconoir. Then banknote, coins, wallet from Lucide. Each line shows the name, the source pack, and the svg path. The tokens underneath tell you which words the ranker matched.

## B06 — WORKED EXAMPLE (--check and --show)

> Two more moves. Dash dash check is the anti-redraw question — is this name in the set. It answers three things per name: in set, concept or brand, and the file path. If you missed, it shows you the nearest neighbors. Dash dash show prints the raw SVG, so you can paste it into a component or a mood board without opening the file.

## B07 — WORKED EXAMPLE (--brands filter)

> One filter changes the whole answer. Dash dash brands narrows the search to the three hundred and seventy-six brand and logo icons only. Search github with the filter and you get two hits, both logos. Drop the filter and the ranker starts pulling in concept icons that happen to share tokens. The filter is a scope switch, not a preference.

## B08 — FALSIFIABILITY (the miss)

> And here is what a miss looks like. Quantum entanglement. No match. The tool does not silently return empty. It prints an instruction: a miss is not a licence to draw. Try a nearby concept. Compose two icons. Or accept that the idea is not iconographic. Exit code zero, because the answer 'nothing fits' is the real answer.

## B09 — VERDICT (the surface)

> So the surface. Bare art icons prints the info banner and exits. A query searches the whole set with IDF ranking. Dash dash check answers is-it-in-the-set. Dash dash show hands you the raw SVG. Dash dash brands narrows the corpus to the three hundred and seventy-six logos. Three aliases all point at the same script. And a miss is a real answer, not a licence to draw.

## B10 — YOUR TURN (handoff)

> Your turn. Paste this into Claude Code from the brutalist toolkit root. It walks the whole surface: banner, three search runs of different rarity, a check pair, a show, a brands filter, and one deliberate miss. What you want to see is fair ranking on common words, the rare word winning where it should, three passing checks, one honest miss, and identical output across the three aliases. If any run surprises you, that is a lead — file it against icon_search.py rank.

## B11 — OUTRO (title restate + sign-off)

> Brutalist Command: art icons. Liam, in for Bear, for at Humanitarians A I.

---

## Register notes

- **Teardown** (Feynman × MKBHD): narrate the mechanism, then judge it —
  what this design gets right, where it bites.
- **Sign-off**: "at Humanitarians A I" is spoken letter-by-letter to keep
  Kokoro from swallowing the handle; the on-screen outro card shows
  `@NikBearBrown` per OUTRO-LOCK (locked constant; the folder chip on the
  composer beats reads `@HumanitariansAI`).
- **Hesitant writer trigger**: the whole ungrammatical framing
  "art icons draws / new icons" is what a viewer might arrive with; the
  correction "art icons finds / existing icons" is what the film argues.
  The whole SENTENCE flips, not just one word — per EXECUTIVE-SUMMARY LAW.
