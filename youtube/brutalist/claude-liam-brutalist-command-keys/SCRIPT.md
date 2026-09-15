# SCRIPT — Brutalist Command: art keys

Teardown register · Liam in for Bear · Kokoro `am_onyx` · @HumanitariansAI.
Twelve beats. Audio-first: the mp3 durations are the master clock; the words
below are the source-of-truth text sent to Kokoro.

## B00 — ASK  (cold open, ClaudeComposerAsk)

> Habari, this is Liam, in for Bear. The ask — before I fill a single beat
> sheet, tell me which optional keys this box has, and whether the toolkit
> actually needs any of them. Just probe. Do not spend anything.

## B01 — BLUF  (BrutalistHesitantWriter, hesitant-type)

> Watch the writer walk this back. The toolkit is free by default. Art keys
> does not block a render — nothing does. It audits one optional upgrade,
> and it audits it live. A red row here means Higgsfield is not logged in.
> It never means you cannot render.

## B02 — FRAMEWORK  (ClaudeCodeBeat)

> The dispatcher is one case in the art file — two lines. Pattern "keys",
> then exec python three on check_keys.py, with every argument forwarded.
> No aliases. Whatever the script decides is the whole command's behavior.

## B03 — FRAMEWORK 2  (ClaudeCodeBeat)

> Four status paths, one probe. Return code zero — valid, green ready.
> Non-zero — invalid, red, with the exact fix line printed next to it.
> No such command on this box — unset, yellow, with a note that the free
> path runs silently. Any other exception — warn, and the whole run is
> flagged inconclusive. Each row is one line the human can read.

## B04 — WORKED EXAMPLE 1  (ClaudeCodeBeat, the "invalid" run)

> Here is this box today. Higgsfield is installed. There is no active
> login and the network is unreachable. The command fires the probe.
> Return code non-zero, so the row lands as invalid — with the literal
> fix line "run higgsfield auth login." And then, quietly, the script
> exits zero. Watch that gap. The red row is diagnostic, not a gate.

## B05 — WORKED EXAMPLE 2  (ClaudeCodeBeat, the "unset" run)

> Same command, one variable changed. Take higgsfield off the path.
> The subprocess call raises FileNotFoundError, and the except branch
> writes "CLI not installed — AI video beats use free path (Ken Burns
> stills)." Yellow row. Exit zero again. No error at all — the free
> path is the default and always has been.

## B06 — MECHANISM 1  (ClaudeCodeBeat, the probe body)

> This is the whole probe. Twenty lines. A subprocess call with a
> twenty-five-second timeout. Return code zero writes the valid row.
> Non-zero writes the invalid row with the failure text quoted. A
> FileNotFoundError writes the unset row. Anything else — a broken
> pipe, a kernel signal, anything — flips the inconclusive flag and
> writes a warn row. That is every branch. There is no other service
> checked.

## B07 — MECHANISM 2  (ClaudeCodeBeat, .env + redaction)

> One more mechanism worth showing. The script reads a repo-root dot-env
> file, if one exists, via load_env — using os dot environ dot setdefault,
> so anything already in the shell wins. But it never prints a value.
> To prove it — write a fake secret into dot env, run the script, and
> grep the output for the secret. Zero matches. The dot env is scanned
> for keys the script wants; the values stay silent.

## B08 — FAILURE / DESIGN TELL  (ClaudeCodeBeat)

> One design tell worth calling out. The docstring says exit zero if
> every present key is valid, one if any is invalid. Read the code.
> The variable any underscore invalid is declared false on line forty
> and never reassigned. So the "invalid" branch does not actually flip
> the exit code. And the art help line advertises an "SI key" check
> — grep the script for SI, and you get zero hits. So the surface
> promises two things the code does not enforce. Both are harmless
> today — nothing in the pipeline gates on this exit — but if you ever
> need to fail a CI job on a red row, you now know exactly which line
> to patch.

## B09 — VERDICT  (ClaudeVerdictArtifact)

Six lines land on the artifact card. Narration reads them aloud:

> So — art keys. A live probe of one optional CLI, wrapped in a two-line
> dispatcher case, that prints a colored table and always exits zero.
> The toolkit needs no keys. This command exists so a red row is visible
> before you go looking for it. Run it once when you clone the repo,
> and run it again the day you install Higgsfield. In between, ignore it.

## B10 — YOUR TURN  (ClaudeComposerAsk with paste-ready prompt)

> Your turn. Paste this into Claude Code, pointed at your own copy of
> the toolkit. Do not fix the script. Just audit it. Ask Claude to
> quote the docstring on lines eight to ten, name the exact variable
> that would need to change for the promise to hold, and write one
> pytest test that would fail on the current code and pass if the
> promise were kept. Then ask whether the "SI key" phrase in the art
> help still refers to anything that exists. Look for whether Claude
> is tempted to just patch the file. Reading is not fixing. Notice
> first, then decide.

## B11 — OUTRO  (ClaudeTitleOutro)

> Brutalist Command: art keys. Liam, in for Bear, for at Humanitarians
> A I.

---

**Register notes.** No captions, no karaoke, no burned-in transcript.
Bookends (B00, B10, B11) may run longer than the 45–70 word inner-beat
budget; the body beats stay tight and let the code cards carry the
evidence. B08 is deliberately the longest inner beat — the design tell
needs both drifts named and both quantified.
