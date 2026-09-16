# SCRIPT — Brutalist Command: repoloop.sh — Short

Kokoro `am_onyx`, no captions, native 2160×3840. Six beats.

Planned duration (sum of parent `render_duration_s` per kept beat): **93.83s**.
Every mp3 was copied bit-identical from the parent vertical reel; no
regeneration.

## B00 · Cold open · ClaudeComposerAsk916 · 11.07s
> Vanakkam, this is Liam, in for Bear. The ask — how do I build the whole
> Brutalist playlist without babysitting every film? Show me the loop that
> runs one fresh Claude worker per episode, on repeat.

## B01 · BLUF · BrutalistHesitantWriter916 · 11.80s
> Watch the writer walk this back. Repoloop dot sh does not render films.
> It spawns workers. One Claude subprocess per film, one queue, one lock —
> the loop drains the pending list and stops only when told.

## B05 · Worked example · ClaudeCodeBeat916 · 18.47s
> Here is dash dash dry, verbatim. Fifty-six films — three onboarding,
> eighteen skills, seventeen art commands, twelve utilities, six Q C
> helpers. Setup and repoloop are canonical commands, not skills. The
> list is derived from the toolkit, not a hand-maintained manifest. If
> you add a SKILL dot m d tomorrow, the loop finds it.

## B09 · Verdict · ClaudeVerdictArtifact916 · 19.86s
> So — repoloop dot sh. A three-line shim over a serial film factory.
> Six moving parts, in the order you touch them: the shim, discover,
> merge queue, snapshot toolkit, sandboxed worker, verify film. No
> parallelism. No auto-publish. No A P I-key fallback. A stop file
> gracefully terminates. A worker lock forbids duplicates. Six things —
> nothing else.

## B10 · Your Turn · ClaudeComposerAsk916 · 26.82s
> Your turn. Paste this into Claude Code, pointed at your own copy of the
> Brutalist toolkit: run dot slash repoloop dot sh dash dash dry and group
> the films by kind. Then run dot slash repoloop dot sh dash dash status
> and read out the pending count, the review-ready count, and the active
> run I D. Then explain in one line what would happen if I edited FEEDBACK
> dot m d inside an already review-ready reel folder — walk the code in
> repoloop dot py that decides. Do not start the loop.

## B11 · Outro · ClaudeTitleOutro916 · 5.67s
> Brutalist Command: repoloop dot s h. Liam, in for Bear, for at
> Humanitarians A I.

## Cut coherence review (whole-beat cut, no rewrite)

- **B00 → B01:** ask motivates the BLUF; the writer walks back the
  misconception the ask sets up. No dangling reference.
- **B01 → B05:** BLUF establishes "one Claude subprocess per film";
  B05's `--dry` inventory concretely shows *what* those films are (56
  of them, derived from the toolkit itself). No dangling reference.
- **B05 → B09:** the verdict's second line ("discover() — inventory
  derived from the toolkit itself: intro trilogy + skills/*/SKILL.md +
  case-branches in art + runtime & qc executables") is exactly what the
  viewer just saw in B05. No dangling reference.
- **B09 → B10:** Your Turn's assignment names `--dry` (already seen in
  B05) and `--status` (named in the verdict's implicit surface but not
  shown as a demo). The `merge_queue()` walk in the assignment maps to
  the third verdict line. No dangling reference.
- **B10 → B11:** standard sign-off, mirrors B00's opening ("Liam, in
  for Bear").

## What this Short does NOT do

- Does not walk the three-line shim body (dropped B02).
- Does not step through `discover / merge_queue / build_one` in code
  (dropped B03).
- Does not step through `worker_settings + worker_environment` (dropped
  B04).
- Does not show a live `--status` block (dropped B06).
- Does not step through `verify_film` guards (dropped B07).
- Does not show the unknown-`--only` recovery demo (dropped B08).

Those beats live in the 16:9 landscape reel and the full-length native
portrait reel under `youtube/brutalist/claude-liam-brutalist-command-repoloop/`.
This Short's B09 verdict enumerates their subjects so the surface stays
complete without the deep dives.
