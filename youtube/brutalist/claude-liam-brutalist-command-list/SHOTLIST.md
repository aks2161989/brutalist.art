# SHOTLIST — Brutalist Command: art --list

12 beats, all rendered via registered Remotion compositions from the
isolated toolkit's `runtime/remotion/src/`.
Landscape 3840×2160 (native, `--scale=2`). Vertical 2160×3840 (native, `--scale=2`).
Cream ground `#FAF9F5`, warm ink `#3D3929`, terracotta accent `#D97757`.

---

### B00 · ClaudeComposerAsk · ASK
Composer card on cream. Greeting `Salaam, Liam` in serif above the composer,
folder chip reads `@HumanitariansAI`. Ask types into the composer, running
indicator, three concrete output lines cascade in beneath.

### B01 · BrutalistHesitantWriter · BLUF · lead_silence_s: 0.8
Two short serif lines type on cream. `runs` is highlighted terracotta, the
writer hesitates, backspaces, types `prints`. `skill` is highlighted next,
hesitates, backspaces, types `catalog`. Final settled line reads
`art --list prints the skills catalog.` A stable seed keeps the performance
identical on every render.

### B02 · ClaudeCodeBeat · FRAMEWORK
Code card titled `art — the dispatcher (bash)`. The relevant slice of the
`case` block types in — enough to show that `--list|list)` is a two-alias
pattern joined by a pipe. Spark line: `Two aliases. One branch.`

### B03 · ClaudeCodeBeat · MECHANISM
Code card titled `art:41-59 — the --list body`. The header printf types,
then the sixteen skill printfs cascade in as a comment-annotated block.
Spark line: `17 printfs. No lookup.`

### B04 · ClaudeCodeBeat · WORKED_EXAMPLE
Code card titled `$ ./art --list  (verbatim, 17 lines)`. The captured
output cascades in — SKILL/ROLE header, then all 16 rows in the exact
order the file emits them. Terminal prompt line follows.
Spark line: `17 lines. Exits 0. Done.`

### B05 · ClaudeCodeBeat · MECHANISM
Code card titled `the format string: '%-22s %s\n'`. Shows one printf
line, then a diagrammed annotation of what each `%` slot means, then a
one-row sample rendered with the same alignment. Spark line:
`22-char gutter. Scannable table.`

### B06 · ClaudeCodeBeat · MECHANISM
Code card titled `$ ./art list foo bar  (extras ignored)`. Types the
invocation, then a `# same output. exit 0.` comment, then a contrast row
against `./art scenes "…"` (which does read `"$@"`). Spark line:
`--list is a printer, not a runner.`

### B07 · ClaudeCodeBeat · FALSIFIABILITY
Code card titled `$ ./art -list  (the failure path)`. Types the invocation,
then the one-line hint appears on stdout (terracotta), then
`echo $?  # 2` types below. Under it, the `*)` catch-all source from
`art:106-108` types in. Spark line: `Not the catalog. Exit 2.`

### B08 · ClaudeCodeBeat · MECHANISM
Code card titled `wrong guess → recovery in two commands`. Types the
recovery arc: `./art --list`, then `./art <skill> --help`, plus the source
lines `art:109-111` that make the second `--help` work. Spark line:
`List, then --help on a skill.`

### B09 · ClaudeVerdictArtifact · VERDICT
Artifact card in on cream. Numbered lines cascade one at a time:
- `art --list — 17 lines from a hand-typed table (1 header + 16 skills).`
- `art list — the bare-word alias, identical output.`
- `extra args — silently ignored; --list never reads "$@".`
- `unknown token — exit 2, hint on stdout, points to --list.`

### B10 · ClaudeComposerAsk · YOUR_TURN
Composer with greeting `Your turn.` and folder chip `@HumanitariansAI`.
The Your-Turn prompt types into the composer; running indicator; three
expected-outcome lines cascade below.

### B11 · ClaudeTitleOutro · OUTRO
Title-restate outro on cream, polarity and mascot seeded from the reel
slug per `OUTRO-LOCK.md`. Title: `Brutalist Command: art --list.` Handle:
hardcoded `@NikBearBrown`. No subline. Mascot animates below the handle
(translation / scale only, per PIXEL-ART LAW).

---

## Portrait notes (9:16 vertical)

The vertical beat sheet uses `ClaudeComposerAsk916`, `BrutalistHesitantWriter916`,
`ClaudeCodeBeat916` (added natively to `runtime/remotion/src/Root.tsx` in this
isolated toolkit — no landscape scene was cropped), `ClaudeVerdictArtifact916`,
and `ClaudeTitleOutro916`. The B01 hesitant writer text is re-laid as four
short lines instead of two long ones, so the correction (`skill` → `catalog`)
lands centered inside the portrait safe area without wrapping.
