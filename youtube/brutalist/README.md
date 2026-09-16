# Brutalist — the playlist

Fellows already have Claude Code. These films teach them to use it to make,
inspect and revise research-report videos with Brutalist.

1. **What Is Brutalist?** — film as code; one change, a visible result.
2. **Download Brutalist with Claude Code** — the public repo, setup and readiness.
3. **Your First Brutalist Project** — evidence → beat sheet → rendered report → revision.
4. A separate AI Explainer for **every skill on disk**, then every canonical
   `art` command, setup, this loop and executable runtime/QC utility. Aliases
   share their command's film. The live inventory is [playlist.json](playlist.json).

All episodes: **Liam, in for Bear**, `am_onyx`, Claude-style visuals,
**@HumanitariansAI**, no captions, native 3840×2160 landscape plus a complete
2160×3840 portrait companion. A full-length portrait is not automatically a Short.
Every published Short must be **strictly under 3:00**. The independent
[cut-first Shorts queue](SHORTS.md) makes focused derivatives without rebuilding
the longs. See its [watch list](shorts/WATCH.md); cut complete beats first,
then rewrite only if the remaining explanation cannot stand alone.
The script follows the AI Explainer skill-teardown structure: mechanism, actual
example, failure case, verdict, an actionable Your Turn and a title-restating outro.

## Watch, then request changes

Open [WATCH.md](WATCH.md). Each `review_ready` row links both local MP4s. That
status means rendering and automated checks passed and an AI reviewed frame
evidence. It does **not** mean Bear approved it or that anything was published.

Edit the episode's `FEEDBACK.md` after viewing. The loop detects it at its next
inventory scan (every ten minutes between jobs), requeues the episode and keeps
the previous exports until replacement verification succeeds. Stop the loop
before editing a currently building beat sheet to avoid concurrent edits.

Each film retains its script, beat sheet, sources, source hashes, build prompt,
fact-check, shot list, checks, visual-review evidence and custom scene source.
Completed work survives a restart. Partial work survives a failed attempt.

## Run the factory

From the repository root:

```bash
./repoloop.sh --dry       # list coverage; no Claude session or output writes
./repoloop.sh --prepare   # create briefs and index read-only example leads
./repoloop.sh --start     # detach one serial, continuous supervisor
./repoloop.sh --status    # counts, lock/running state and active worker log
./repoloop.sh --stop      # stop the owned worker; preserve all film files
./repoloop.sh --shorts-only --start   # independent under-3:00 derivative queue
./repoloop.sh --shorts-only --status  # progress for Shorts, not full portraits
```

For a foreground run, `./repoloop.sh --forever`. The default with no flags drains
the currently eligible queue. `--once --only what-is-brutalist` attempts one
named film; `--n 3` bounds a foreground batch. `--landscape-only` is an explicit
diagnostic override, not the playlist's default delivery requirement.

The design adapts `anthropics/bookloop.sh`: one fresh Claude session per item,
one serial job at a time, logs and resumability. Unlike a fixed hand-written
topic list, discovery scans the current public repo and preserves completed
jobs. It checks subscription login and local dependencies first, backs off on
errors, waits on Claude usage limits and pauses between jobs below 12 GB free.
It rescans for new skills/commands and feedback while idle or between films.
The Mac must remain awake, powered and online for Claude sessions. This does
not provide a cloud render farm or unlimited Claude usage.

If Claude reports a revoked/expired login, the whole queue pauses for 30 minutes
instead of burning through every episode. Sign in again with `claude auth login`;
an already running supervisor retries automatically. `--stop` then `--start`
can restart the process, but does not discard a recorded pause or completed work.
Local `claude auth status` can say logged in even when the server rejects the
saved token; the worker checks actual session errors too.

## Safety and isolation

Workers use an ignored `.repoloop/workspaces/` toolkit copy. Custom scene changes
stay there and are exported with that film; the real runtime and fellows'
originals are not writable. Installed dependencies are shared read-only. The
loop never signs a human review, publishes, pushes Git or spends API credits.
Optional paid/service-backed commands get source-backed explanations and safe
local demonstrations, not unauthorized live calls.

Claude runs with `dontAsk`, explicit tool permissions, no MCP servers, disabled
hooks and a fail-closed OS sandbox. Bash networking is localhost-only for
Remotion; optional API-key environment variables are removed. These controls
follow Claude Code's [permissions](https://code.claude.com/docs/en/permissions)
and [sandboxing](https://code.claude.com/docs/en/sandboxing) documentation. The
model session itself uses the existing Claude Code subscription. No
`--dangerously-skip-permissions` or API billing fallback is used.

Fellows' beat sheets are indexed read-only from
`../humanitarians-youtube/fellows` relative to this repository. Override with
`--fellows /path/to/fellows`. [EXAMPLE-SOURCES.json](EXAMPLE-SOURCES.json) records
source paths and hashes; copied raw examples and worker logs remain ignored,
not public course material. Examples are leads, not current verified facts.

Some old public skill references point to checkers that are not shipped here.
Workers must name those gaps in TYPECHECK.md, use the actual available checks
and visually inspect frames. They must not invent a passing checker or human
signature. Export receipts bind the actual MP4 hash; the supervisor also checks
audio, dimensions and this attempt's visual-review evidence before marking
an episode `review_ready`.

Logs, queue state and scratch copies: `.repoloop/`. Rendered media and build
caches are ignored by Git. `.gitignore` cannot enforce file size: inspect the
staged files before any later push and keep files over 25 MB on Drive. This
factory does not push or upload anything.
