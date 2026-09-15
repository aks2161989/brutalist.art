# PROMPTS — Brutalist Command: art --list

Two composer beats carry typed prompts. Both use `ClaudeComposerAsk`
(landscape) / `ClaudeComposerAsk916` (portrait), and both are read aloud
by Liam so the audio and the video carry the same line.

---

## B00 · Cold-open ASK

Composer greeting: `Salaam, Liam`
Composer topic: `BRUTALIST · COMMAND: ART --LIST`
Composer segment: `art --list`
Running indicator: `reading the entry point…`

**Command typed into the composer** (single line):

```text
What does ./art --list actually print — and where does it stop?
```

**Three output lines that cascade under the composer:**

```text
prints a 17-line skills table (1 header + 16 skills)
two aliases: --list and bare list
different scope from ./art help (the commands sheet)
```

---

## B10 · Your Turn HANDOFF

Composer greeting: `Your turn.`
Composer topic: `BRUTALIST · YOUR TURN`
Composer segment: `Prove the --list branch is a printer`
Running indicator: `paste this into Claude Code…`

**Command typed into the composer** (paste-ready — the prompt the narration
reads aloud):

```text
From the brutalist.art toolkit root, run ./art --list and ./art list.
Save each stdout to /tmp/art-list-<alias>.txt and capture $? into
each file. Then: (1) diff the two files, (2) run `wc -l` on each,
(3) open ./art at line 41 and count the printf calls in the
--list|list) branch, (4) confirm that count equals the number of
non-header rows in the printed table. Report: any diff, any exit
code that is not 0, the row count vs the printf count, and the
first mismatch (if any) between the file's printf order and the
printed table order. Bonus: run ./art -list (single dash) and
./art list foo bar and report each one's exit code and whether
its stdout matches ./art --list.
```

**Three expected-outcome lines under the composer:**

```text
two identical stdouts (17 lines each, exit 0)
16 printf calls under the --list|list) branch — one per row
./art -list exits 2 with a one-line hint on stdout
```

**What the fellow should look for in Claude's answer:** confirmation
that both aliases produce identical output, that the branch really is
a hand-typed table (no directory scan), and that `-list` with one dash
is not an alias — it exits 2 and points you at `--list`.

---

## Prompts not to invent

The reel does **not** invent a "list your skills" workflow, a plug-in
scanner, or any interactive prompt. `--list` is a printer. Anything the
narration or the composer says a fellow can verify by pasting the
prompt above into their own Claude Code session on a fresh clone of the
public toolkit at <https://github.com/nikbearbrown/brutalist.art>.
