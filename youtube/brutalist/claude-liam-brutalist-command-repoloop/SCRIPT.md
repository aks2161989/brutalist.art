# SCRIPT — Brutalist Command: repoloop.sh

Persona: **Liam, in for Bear.** Voice: Kokoro `am_onyx`. Register: Teardown.
Playlist: Brutalist. Channel: `@HumanitariansAI`.

## B00 — ClaudeComposerAsk (cold open · IN-FOR-BEAR LAW)
**Greeting:** `Vanakkam, Liam` (Tamil, one word; fresh — does not collide with
setup=Konnichiwa, approvals=Selam, doctor=Jambo, run=Ciao, etc.). Slug char-sum
is not a Wagwan slot; Wagwan is Bear's only.
> Vanakkam, this is Liam, in for Bear. The ask — how do I build the whole
> Brutalist playlist without babysitting every film? Show me the loop that
> runs one fresh Claude worker per episode, on repeat.

## B01 — BrutalistHesitantWriter (BLUF · EXECUTIVE-SUMMARY LAW · ≥9s + 0.8s lead)
Misconception → correction: `renders films.` → `spawns workers.`
> Watch the writer walk this back. Repoloop dot sh does not render films.
> It spawns workers. One Claude subprocess per film, one queue, one
> lock — the loop drains the pending list and stops only when told.

## B02 — FRAMEWORK · the shim (ClaudeCodeBeat)
> The shell entrypoint is three lines. Set errexit, resolve its own
> directory, and exec Python on runtime slash scripts slash repoloop dot
> py, forwarding every argument. There is no logic in bash. The factory
> lives in the Python file.

## B03 — FRAMEWORK · the queue lifecycle (ClaudeCodeBeat)
> The factory has one shape. Discover the inventory from the toolkit
> itself — the intro trilogy, every SKILL dot md, every case branch in the
> art dispatcher, every executable runtime and Q C script. Merge that
> inventory into the on-disk queue, marking anything with changed source
> or feedback as pending. Then, for each pending item, snapshot the
> toolkit into an isolated workspace and spawn one Claude worker under a
> fail-closed sandbox.

## B04 — FRAMEWORK · the sandboxed worker (ClaudeCodeBeat)
> The worker's rights are constrained. Read anywhere it needs. Edit only
> inside its scratch workspace and its reel folder. Bash is allowed — but
> git push, g h, curl, wget, and s s h are denied outright. Dot env, dot
> s s h, dot a w s, and dot config slash gcloud are denied for reads.
> The worker's Anthropic environment variables are stripped so no A P I
> key can slip in. Kokoro is pinned to the local model. No M C P
> servers.

## B05 — WORKED_EXAMPLE · `--dry` (ClaudeCodeBeat · verbatim)
> Here is dash dash dry, verbatim. Fifty-six films — three onboarding,
> eighteen skills, seventeen art commands, twelve utilities, six Q C
> helpers. Setup and repoloop are canonical commands, not skills. The
> list is derived from the toolkit, not a hand-maintained manifest. If
> you add a SKILL dot m d tomorrow, the loop finds it.

## B06 — WORKED_EXAMPLE · `--status` (ClaudeCodeBeat · verbatim)
> And here is dash dash status, live. Thirty-seven review-ready. Eighteen
> pending. One building — that is this reel. Its run I D and log path
> are printed for you. Because the loop takes a f-cntl lock on worker
> dot lock, running is a truth about a single supervisor, not a truth
> about a machine.

## B07 — MECHANISM · verify_film (ClaudeCodeBeat)
> This is the fail-closed gate. Verify film reads the beat sheet for
> both aspects. Fewer than eight beats — refuse. Non-Liam voice —
> refuse. First beat not Claude Composer Ask — refuse. Second beat
> missing Hesitant Writer — refuse. Penultimate greeting not Your Turn
> — refuse. Output M P 4 dimensions must match the requested aspect
> exactly. Audio must decode above minus forty d B. And a matching A I
> visual-review record with the current run I D must exist. The
> refusal is the whole point of the command.

## B08 — FAILURE_RECOVERY (ClaudeCodeBeat · verbatim)
> One failure worth showing. Ask the loop for an inventory I D that does
> not exist. The guard fires immediately: Unknown dash dash only I D,
> inspect dash dash dry. Exit two, no queue mutation, no worker
> spawned. Recovery is one command — dash dash dry — read the real
> slugs and try again. The loop's contract is that unknown work is
> never work.

## B09 — VERDICT (ClaudeVerdictArtifact · 6 lines)
> So — repoloop dot sh. A three-line shim over a serial film factory.
> Six moving parts, in the order you touch them: the shim, discover,
> merge queue, snapshot toolkit, sandboxed worker, verify film. No
> parallelism. No auto-publish. No A P I-key fallback. A stop file
> gracefully terminates. A worker lock forbids duplicates. Six things
> — nothing else.

## B10 — YOUR TURN (ClaudeComposerAsk · greeting "Your Turn")
> Your turn. Paste this into Claude Code, pointed at your own copy of the
> Brutalist toolkit: run dot slash repoloop dot sh dash dash dry and
> group the films by kind. Then run dot slash repoloop dot sh dash dash
> status and read out the pending count, the review-ready count, and
> the active run I D. Then explain in one line what would happen if I
> edited FEEDBACK dot m d inside an already review-ready reel folder —
> walk the code in repoloop dot py that decides. Do not start the loop.

## B11 — OUTRO (ClaudeTitleOutro)
> Brutalist Command: repoloop dot sh. Liam, in for Bear, for at
> Humanitarians A I.
