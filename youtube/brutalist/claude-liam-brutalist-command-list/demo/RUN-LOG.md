# Demo run log — `./art --list` and its alias `./art list`

Workspace: `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/.repoloop/workspaces/claude-liam-brutalist-command-list/toolkit`
Source SHA-256 of `art` dispatcher: `387d12c338fe3e8e05a3c2202be86ea81beaf548c2fd11ec3ee4876694f8b562`

All output below is verbatim from this workspace, run in this session.

---

## 1. `./art --list` — captured stdout (17 lines, exit 0)

```bash
$ ./art --list
```

```text
SKILL                  ROLE
ai-explainer           builder — Claude-branded explainer reel (the tight cut)
cli-explainer          builder — prompt → code → moving output (the build reel)
deep-explainer         builder — 5-10 min documentary episode (vox pantry beats)
anthropics             builder — reads Anthropic artifacts against their own claims; practitioner-report register
fashionista            builder — AI fashion-call experiment; sports-announcer call + correction ask; Kokoro am_onyx
fellows                builder — wraps a HAI fellow's video report in Claude bookends for @HumanitariansAI
finance                builder — templatized SEC EDGAR filings reel; 11 beats, 5 charts, fully deterministic
guests                 builder — wraps a board-member or invited-speaker video in Claude bookends for @HumanitariansAI
nbb                    persona — Teardown register, Liam in for Bear (Kokoro am_onyx)
hai                    persona — Plain register (simple, direct), Kokoro Bella (af_bella)
explainer              doctrine — parent chassis the builders inherit (not an entry point)
your-turn              doctrine — the closing three-beat standard
logo                   builder — brand sting outro; random-once animation + brand SVG + jingle (the mp3 is the clock)
duration-planner       doctrine — duration is an output, never a target
nopunt                 doctrine — maps animatable beat-types to Brutalist primitives; consult before placing any placeholder
screen-clean           doctrine — prepares screen recordings (Zoom/Teams/Meet) for use as a reel beat
```

- `$?` = `0`
- `wc -l` = `17` (1 header + 16 skills)
- stderr is empty

## 2. `./art list` — the bare-word alias

```bash
$ ./art list
```

- `$?` = `0`
- `diff --list output vs list output` → IDENTICAL

Both aliases fall into the same `case` branch (`art:41-59`), which contains
sixteen `printf` calls plus a header row — one printf per skill. There is
no directory scan and no lookup; the strings are hard-coded.

## 3. `./art list foo bar` — extra positional args are ignored

```bash
$ ./art list foo bar
```

- Same 17-line output as bare `./art list`.
- `$?` = `0`
- `diff bare vs list-with-extras` → IDENTICAL

The `--list` / `list` branch never reads `"$@"`, so extra tokens fall through
harmlessly (compare with `./art scenes`, `./art run`, etc., which `exec` a
Python script and pass `"$@"` on).

## 4. `./art -list` — the failure path (single dash, not a real alias)

```bash
$ ./art -list
```

- `$?` = `2`
- stdout: `art: unknown skill '-list' (try ./art --list)`
- stderr is empty

The token `-list` matches neither the `--list|list)` branch nor any of the
sub-command branches, so the case falls through to the `*)` catch-all
(`art:106-115`), which prints a one-line hint to **stdout** and exits `2`.

Note: the hint line is written by a bare `echo` — it lands on stdout, not
stderr. If you pipe stdout to a file, you will lose the hint AND the shell
exit will still be `2`. The recovery is to actually type the two dashes:
`./art --list`.

## 5. `./art bogus` — same failure branch, different token

```bash
$ ./art bogus
```

- `$?` = `2`
- stdout: `art: unknown skill 'bogus' (try ./art --list)`

Same shape as `./art -list` — proves the `*)` catch-all is the source of the
`try ./art --list` hint, and that the hint always names `--list`, not `list`.

---

## Reproduction

```bash
cd /path/to/brutalist.art     # or the isolated workspace toolkit
./art --list                  # 17-line skills table, exit 0
./art list                    # identical output, exit 0
./art list foo bar            # same output, extra args silently ignored
./art -list                   # exit 2, one-line hint on stdout
./art bogus                   # exit 2, one-line hint on stdout
```

No network calls. No paid API. Runs on any machine that has `bash`. The
whole dispatcher is one script — `art:37-116` — and the `--list` branch is
`art:41-59`.
