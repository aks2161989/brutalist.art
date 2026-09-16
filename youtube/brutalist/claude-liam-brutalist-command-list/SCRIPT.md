# SCRIPT — Brutalist Command: art --list

Persona: **Liam, in for Bear** — Kokoro `am_onyx` (free, local).
Playlist: **Brutalist**, adapted for the `@HumanitariansAI` folder chip.

Narration is the WORDS; SHOTLIST.md describes the VISUALS. No captions.

Aliases covered: `./art --list` and `./art list` (both share one `case`
branch at `art:58-80`). Source updated 2026-09-12: 16 → 20 skills.

---

### B00 · ASK · ClaudeComposerAsk

> Salaam, this is Liam, in for Bear. Every fellow in Brutalist has typed
> dot slash art dash dash list at some point. What it does is smaller and
> more literal than most people think. It prints a hand-typed table of
> twenty skills. No lookup, no directory scan. Here is exactly what runs,
> and where it stops.

### B01 · BLUF · BrutalistHesitantWriter · lead_silence_s: 0.8

> Watch the writer walk this back. Art dash dash list does not run a skill
> in the toolkit. It prints the skills catalog. Twenty rows, one dispatcher,
> hard-coded in the file itself.

### B02 · FRAMEWORK · ClaudeCodeBeat

> The whole dispatcher is one bash case statement. The second branch of
> that case is two aliases joined by a pipe: dash dash list and the bare
> word list. Both hit the same body. You never need to remember which
> spelling; the case pattern takes both.

### B03 · MECHANISM · ClaudeCodeBeat

> Here is the body. One printf for the header, then twenty more printfs,
> one per skill. Every row is a literal string in the file itself. There
> is no file system scan, no plug-in discovery, no configuration file.
> If a skill is missing from the table, it is missing because nobody added
> its printf.

### B04 · WORKED_EXAMPLE · ClaudeCodeBeat

> This is the actual output on my terminal. Twenty-one lines. A header row
> that reads SKILL and ROLE, then twenty skills, sorted the way the file
> lists them. The table now includes four godot skills and a riff utility
> added since the last build. No colours, no pager. It prints, it exits
> zero, it is done.

### B05 · MECHANISM · ClaudeCodeBeat

> The format string is worth reading. Percent dash twenty-two s, space,
> percent s, backslash n. That means: left-pad the first field to
> twenty-two characters, one space, then the second field, then a newline.
> Every row is aligned to the same twenty-two-character gutter, which is
> why the table is scannable without a monospace-aware terminal.

### B06 · MECHANISM · ClaudeCodeBeat

> Watch what happens with extra arguments. Dot slash art list foo bar
> prints the same twenty-one lines and exits zero. The branch never reads
> the rest of the command line. Compare that to a runner branch like
> scenes or run, which passes every remaining argument straight to a
> Python script. List is a printer, not a runner.

### B07 · FALSIFIABILITY · ClaudeCodeBeat

> Now the near miss. Dot slash art dash list, with one dash instead of
> two, does not print the catalog. It falls into the star branch and
> exits two, with one hint line pointing you at dash dash list. Notice
> where that line lands. It is on standard output, from a bare echo. If
> you pipe standard out to a file, the hint disappears and only the exit
> code is left behind.

### B08 · MECHANISM · ClaudeCodeBeat

> The recovery is two commands. Dot slash art dash dash list to see every
> skill by name. Then dot slash art followed by the skill name and dash
> dash help to open that skill's SKILL dot m-d in your pager. So the arc
> is: list to see what exists, then help on a specific skill to read
> what it does. Two commands, whole surface.

### B09 · VERDICT · ClaudeVerdictArtifact

> So the split. Art dash dash list is a printer. Two aliases, one branch,
> a hand-maintained table of twenty skills. Extra arguments are ignored;
> single dash and unknown tokens exit two with a hint on standard out. The
> recovery is two commands: dash dash list to see the names, then art
> followed by a skill name and dash dash help to read what that one does.

### B10 · YOUR_TURN · ClaudeComposerAsk

> Your turn. Paste this into Claude Code from the brutalist toolkit root.
> Ask it to run both aliases, diff the two outputs, count the rows, then
> open the case block that produces them and confirm every printf resolves
> to exactly one row of the printed table. What you should see is two
> identical outputs of twenty-one lines, twenty printf calls plus a header,
> and no orphans on either side.

### B11 · OUTRO · ClaudeTitleOutro

> Brutalist Command: art dash dash list. Liam, in for Bear, for at
> Humanitarians A I.
