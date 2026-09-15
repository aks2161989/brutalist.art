# SCRIPT — Brutalist Command: art --list (9:16 Short)

Whole-beat cut of the parent vertical companion (rebuilt 2026-09-12; 20 skills).
8 beats retained (B00, B01, B03, B04, B07, B08, B09, B11). No narration
rewrite; every kept beat's `mp3` and `mp4` come from the parent unchanged.
Voice: Kokoro `am_onyx` (Liam, in for Bear). Total run: 127.791 s.

Timings below are actual per-beat renders, in sequence.

---

**B00 — ASK — 16.8 s**

> Salaam, this is Liam, in for Bear. Every fellow in Brutalist has typed dot
> slash art dash dash list at some point. What it does is smaller and more
> literal than most people think. It prints a hand-typed table of twenty
> skills. No lookup, no directory scan. Here is exactly what runs, and where
> it stops.

**B01 — BLUF — 16.2 s** (0.8 s lead silence)

> Watch the writer walk this back, one word at a time. Art dash dash list
> does not run a skill in the toolkit. It prints the skills catalog. Twenty
> rows, one dispatcher, hard-coded in the bash file itself. Two aliases fire
> the same branch, and the branch is a printer, not a runner. Keep that split.

**B03 — MECHANISM — 16.1 s**

> Here is the body. One printf for the header, then twenty more printfs,
> one per skill. Every row is a literal string in the file itself. There is
> no file system scan, no plug-in discovery, no configuration file. If a
> skill is missing from the table, it is missing because nobody added its printf.

**B04 — WORKED EXAMPLE — 17.1 s**

> This is the actual output on my terminal. Twenty-one lines. A header row
> that reads SKILL and ROLE, then twenty skills, sorted the way the file
> lists them. The table now includes four godot skills and a riff utility
> added since the last build. No colours, no pager. It prints, it exits
> zero, it is done.

**B07 — FALSIFIABILITY — 19.3 s**

> Now the near miss. Dot slash art dash list, with one dash instead of two,
> does not print the catalog. It falls into the star branch and exits two,
> with one hint line pointing you at dash dash list. Notice where that line
> lands. It is on standard output, from a bare echo. If you pipe standard
> out to a file, the hint disappears and only the exit code is left behind.

**B08 — MECHANISM (RECOVERY) — 17.5 s**

> The recovery is two commands. Dot slash art dash dash list to see every
> skill by name. Then dot slash art followed by the skill name and dash dash
> help to open that skill's SKILL dot m-d in your pager. So the arc is: list
> to see what exists, then help on a specific skill to read what it does.
> Two commands, whole surface.

**B09 — VERDICT — 19.0 s**

> So the split. Art dash dash list is a printer. Two aliases, one branch,
> a hand-maintained table of twenty skills. Extra arguments are ignored;
> single dash and unknown tokens exit two with a hint on standard out.
> The recovery is two commands: dash dash list to see the names, then art
> followed by a skill name and dash dash help to read what that one does.

**B11 — OUTRO — 6.0 s**

> Brutalist Command: art dash dash list. Liam, in for Bear, for at
> Humanitarians A I.

---

## What was cut, and why the retained cut still stands

- **B02 (FRAMEWORK)** — the surrounding case statement shape. B03 shows the
  actual body; B09 restates "two aliases, one branch" in the verdict.
- **B05 (MECHANISM — format string)** — the `'%-22s %s\n'` decomposition.
  B04's verbatim output already communicates the aligned-column effect;
  the deep read belongs in the long.
- **B06 (MECHANISM — extras ignored)** — worked proof that `list foo bar`
  matches `--list` byte-for-byte. B01 BLUF states printer-vs-runner; B09
  restates "extra positional arguments — silently ignored".
- **B10 (YOUR TURN)** — the extended paste-into-Claude-Code exercise. The
  Short is cut-first; the long film retains the exercise in full.

Nothing in the retained arc depends on a dropped beat. B09's summary lines
about extras being ignored and unknown-token exit-2 are stated as summaries
for an audience of Brutalist fellows already using Claude Code and Unix
conventions — the falsifiability worked example is retained at B07.
