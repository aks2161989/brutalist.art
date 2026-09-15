# Demo captures — art icon-build

Recorded: 2026-09-09
Toolkit: `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/.repoloop/workspaces/claude-liam-brutalist-command-icon-build/toolkit`
`svg/` and `icons/` were symlinked to the public `brutalist.art/svg` and
`brutalist.art/icons` trees for reproducible captures (source is read-only;
no re-cut of the shipped canonical set was written by these runs).

Every line below is verbatim from a live run in this workspace. Numbers
in the film all trace back to this log.

## Alias equivalence — `icon-build` is the only spelling

```
$ grep -n "icon-build" art
64:  icon-build)
65:    exec python3 "$ART_HOME/runtime/scripts/build_icon_set.py" "$@"
```

The `case` block at `art:64-66` is a SINGLE branch — no alternates.
There is no shorter alias; the only entry point is `./art icon-build`.

## Source directory sizes — the problem the cut solves

```
$ du -sh svg/lucide svg/tabler-icons svg/iconoir svg/feather
 48M  svg/lucide
 77M  svg/tabler-icons
 30M  svg/iconoir
 18M  svg/feather

$ du -sh svg/material-design-icons svg/RemixIcon svg/anthropics svg/heroicons
9.1G  svg/material-design-icons
 59M  svg/RemixIcon
3.1M  svg/anthropics
 14M  svg/heroicons

$ du -sh svg/
 12G  svg/
```

Twelve gigabytes on disk. `material-design-icons` alone is 9.1 GB. Not
shippable in git.

## Anthropics — no LICENSE anywhere

```
$ find svg/anthropics -iname 'LICENSE*' -o -iname 'COPYING' -o -iname 'NOTICE*'
(no output — none of the license names is present)
```

Unknown provenance cannot be redistributed. The script excludes it on
purpose (see build_icon_set.py:70-74).

## $ ./art icon-build --help

```
usage: build_icon_set.py [-h] [--dry-run] [--limit LIMIT]

options:
  -h, --help     show this help message and exit
  --dry-run
  --limit LIMIT
```

$? = 0

## $ ./art icon-build --dry-run

```
SOURCE PASSES (priority order — first to claim a concept keeps it)
  lucide       kept 1749, dropped-as-duplicate 7, unparseable 0
  tabler       kept 4134, dropped-as-duplicate 602, unparseable 0
  iconoir      kept 1045, dropped-as-duplicate 626, unparseable 0
  feather      kept 26, dropped-as-duplicate 261, unparseable 0
  brand        kept 376, dropped-as-duplicate 0, unparseable 0

CANONICAL SET: 7330 concepts  (376 brand/logo, 6954 general)
  geometry 0 0 24 24 · stroke-width 2 · currentColor · round caps
  = 44 pt line at 528px render

--dry-run: nothing written.
```

$? = 0

## $ ./art icon-build --limit 5 --dry-run  (small trial cut)

```
SOURCE PASSES (priority order — first to claim a concept keeps it)
  lucide       kept 5, dropped-as-duplicate 0, unparseable 0

CANONICAL SET: 5 concepts  (0 brand/logo, 5 general)
  geometry 0 0 24 24 · stroke-width 2 · currentColor · round caps
  = 44 pt line at 528px render

--dry-run: nothing written.
```

$? = 0

Only the first source (`lucide`, top of PRIORITY) runs; the trial stops
as soon as the limit is hit. Confirms the priority order.

## $ ./art icon-build --dry-run  (with svg/ symlink removed → missing sources)

```
SOURCE PASSES (priority order — first to claim a concept keeps it)
  lucide       source dir absent
  tabler       source dir absent
  iconoir      source dir absent
  feather      source dir absent
  brand        source dir absent

CANONICAL SET: 0 concepts  (0 brand/logo, 0 general)
  geometry 0 0 24 24 · stroke-width 2 · currentColor · round caps
  = 44 pt line at 528px render

--dry-run: nothing written.
```

$? = 0

Empty in, empty out — logged honestly per source. No silent success.
`--dry-run` proves what a real run would produce before you commit.

## $ ./art icon-build --bogus-flag  (the error path)

```
usage: build_icon_set.py [-h] [--dry-run] [--limit LIMIT]
build_icon_set.py: error: unrecognized arguments: --bogus-flag
```

$? = 2  (argparse exits 2 on unknown flag)

## The output artifacts (from the shipped canonical set)

```
$ du -sh icons icons/svg
 30M  icons
 29M  icons/svg

$ ls icons | sort
NOTICE.md
icons.json
svg

$ python3 -c "import json; d=json.load(open('icons/icons.json')); \
              print('count:', d['count']); \
              print('brand:', sum(1 for i in d['icons'] if i['brand']));\
              print('sources:', list(d['sources'].keys()))"
count: 7330
brand: 376
sources: ['lucide', 'tabler', 'iconoir', 'feather', 'brand']
```

## $ head -8 icons/NOTICE.md  (the licence obligation, met)

```
# NOTICE — upstream licences for the canonical icon set
These icons are MODIFIED copies: every icon was rewritten to a single
geometry (24×24), a single line width (stroke 2), and `currentColor`.
ISC and MIT both permit that, on the condition that the copyright notice
travels with the work. It is reproduced in full below.

---

## lucide — ISC License
```

## The excluded libraries — the four principled drops

From `build_icon_set.py:68-76` (verbatim comment block):

```
# EXCLUDED ON PURPOSE — do not re-add without resolving the reason.
#   anthropics/  614 stroke icons, NO LICENSE FILE anywhere in the directory
#                and no README naming an upstream. Unknown provenance cannot
#                be redistributed from a public repo. Resolve the source and
#                its licence first; only then consider adding it.
#   RemixIcon/   100% filled — no line width to normalise (rule 1).
#   material-design-icons/  filled, and 1.79 M files / 9.1 GB (rule 1 + rule 2).
#   heroicons/   mostly solid; its outline set duplicates lucide concepts that
#                lucide already serves at a cleaner single weight.
```

## The 44 pt math

From `build_icon_set.py:53-56` and `icons.json → render.line_44pt_px`:

```
VIEWBOX = "0 0 24 24"
STROKE_W = 2
RENDER_PX_FOR_44PT = 528          # 2 * (528/24) == 44
```

A stroke of `2` in a `24`-unit viewBox rendered at `528 px` = `2 * (528/24) = 44 pt`.
Render smaller and the stroke stays proportional — that is the point of
normalising in the source instead of baking a pixel width into it.
