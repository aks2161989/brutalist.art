# SCRIPT — Brutalist Command: art icon-build

Narration for every beat, verbatim, in reading order. Voice: Kokoro `am_onyx`
(Liam-in-for-Bear). Landscape uses the master; vertical uses the same script
except B10 (see § "Vertical B10 revision").

---

## B00 — ASK (cold open)

> Merhaba, this is Liam, in for Bear. There are twelve gigabytes of raw icons in the svg folder. Two point four million files. Nobody ships that. Art icon-build cuts a set you can actually put in git. Thirty megabytes. Seven thousand three hundred icons. One geometry, one line width, one color hook.

## B01 — BLUF (hesitant writer)

> Watch the writer walk this back. Art icon-build does not download new icons. It cuts a canonical set from ones that already sit on disk. Twelve gigabytes in, thirty megabytes out. Subtractive, not additive — and that is the difference this whole reel turns on.

## B02 — FRAMEWORK (the dispatcher)

> The dispatcher is one case branch in the art file. No aliases this time — only the exact word icon-build hits it. That branch execs a single python script, build_icon_set dot py. Everything else in this film is what that script actually does.

## B03 — MECHANISM (the problem)

> The problem it solves. The svg folder holds a dozen upstream icon libraries. Twelve gigabytes on disk. Two point four million files. Almost all of it is variants — every style, every density, every platform — of a much smaller number of actual ideas. None of it fits in git. None of it is searchable. That is the corpus icon-build turns into something you can ship.

## B04 — MECHANISM (the four rules)

> Four rules do the cutting. Rule one: stroke only. A filled icon has no line width, so filled libraries are dropped whole. Rule two: one icon per thing. Names are normalised — the same concept in five outline styles collapses to one. Rule three: one geometry, one weight. Everything is rewritten to a twenty-four unit viewBox and stroke width two. Rule four: black and white. Every color becomes currentColor, so one icon serves ink on cream and cream on ink.

## B05 — MECHANISM (the 44 pt math)

> Here is why twenty-four and two is the forty-four point set. A stroke of two in a twenty-four unit viewBox scales with the render. At the canonical render size, five hundred and twenty-eight pixels, two times five twenty-eight over twenty-four is forty-four, exactly. That constant ships in icons dot json as line-forty-four-pt-px, so a beat never has to rediscover it. Render smaller and the line stays proportional. That is the point of normalising the source instead of baking a pixel width in.

## B06 — WORKED EXAMPLE (`--dry-run`)

> Dot slash art icon-build dash dash dry-run. Every run reports the source passes in priority order. Lucide keeps seventeen forty-nine, drops seven duplicates. Tabler keeps four thousand one thirty-four, drops six hundred and two. Iconoir keeps ten forty-five, drops six hundred and twenty-six. Feather keeps only twenty-six because lucide already owns the others. Brand keeps three hundred and seventy-six. Total: seven thousand three hundred and thirty. Nothing written to disk.

## B07 — WORKED EXAMPLE (output artifacts)

> Drop the dash dash dry-run and it writes three things. A folder of seven thousand three hundred and thirty svg files, one per concept. An index file, icons dot json, that names each one, its source pack, its tokens, and whether it is a logo. And a NOTICE dot md that carries the ISC and MIT copyright notices, in full. That last one is the licence obligation, met.

## B08 — FALSIFIABILITY (the drops)

> And here is what the tool refuses to include. Material design icons: filled, and nine point one gigabytes on its own — rule one and rule two. Remix icon: one hundred percent filled — rule one. Heroicons: its outline set duplicates lucide, which lucide already serves at a cleaner single weight — rule two. Anthropics: no LICENSE file anywhere. Unknown provenance cannot be redistributed. Every drop is named in the module docstring. Nothing is silently swept in.

## B09 — VERDICT (the surface)

> So the surface. Bare art icon-build re-cuts the whole set and writes it to icons slash. Dash dash dry-run reports the same passes without writing. Dash dash limit N takes a small trial. Under the hood, four rules throw work away on purpose, one dispatcher branch runs the whole thing, and one NOTICE dot md carries the ISC and MIT copyright notices out with every ship. Twelve gigabytes of raw variants become thirty megabytes of shippable line drawings.

## B10 — YOUR TURN (landscape)

> Your turn. Paste this into Claude Code from the brutalist toolkit root. It runs the safe preview, a limited trial, and then reads three things off the shipped set: the count, the geometry, and the first two ISC-and-MIT license names in NOTICE dot md. What you want to see: same seven thousand three hundred and thirty in the preview and in the JSON, the trial cut stops at your limit, and NOTICE contains both an ISC block and an MIT block. If the preview count drifts from the JSON count, that is a lead — svg has changed since the last cut and the shipped set is stale.

## B11 — OUTRO (title restate + sign-off)

> Brutalist Command: art icon-build. Liam, in for Bear, for at Humanitarians A I.

---

## Vertical B10 revision

Portrait B10 uses a slightly shorter narration (25.5 s vs 30.2 s) to match a
3-step composer prompt that fits the 1080-wide safe area:

> Your turn. Paste this into Claude Code from the brutalist toolkit root. It runs the safe preview, a limited trial cut, and then reads the licence file. What you want to see: seven thousand three hundred and thirty concepts in the preview, the trial cut stops in lucide only, and NOTICE dot md carries an ISC block for lucide and an MIT block for the others. If the preview count drifts from icons dot json, that is a lead — svg has changed and the shipped set is stale.

---

## Register notes

- **Teardown** (Feynman × MKBHD): narrate the mechanism, then judge it —
  what this design gets right, where it bites.
- **Sign-off**: "at Humanitarians A I" is spoken letter-by-letter to keep
  Kokoro from swallowing the handle; the on-screen outro card shows
  `@NikBearBrown` per OUTRO-LOCK (locked constant; the folder chip on the
  composer beats reads `@HumanitariansAI`).
- **Hesitant writer trigger**: the whole framing "art icon-build downloads /
  new icons" is what a viewer might arrive with; the correction "art icon-build
  cuts / existing icons" is what the film argues (subtractive, not additive).
  The whole SENTENCE flips, not just one word — per EXECUTIVE-SUMMARY LAW.
- **Numerical spellings**: figures are spelled out as words in the narration
  so Kokoro reads them cleanly (seven thousand three hundred, not 7,330).
