# PROMPTS — Brutalist Command: art keys

Local, free pipeline (Kokoro `am_onyx` + Remotion). No paid generation calls.
No Higgsfield, no ElevenLabs, no upload. Every artifact in this reel was
produced by the deterministic scripts under `runtime/scripts/` in the isolated
toolkit copy.

## Beat construction

Every code beat's `code` block is either:
- Literal excerpts from `art` or `runtime/scripts/check_keys.py` (line-numbered
  in the on-screen title bar), verified against SOURCES.md's SHAs, OR
- Verbatim invocation + stdout/stderr captured in `demo/RUN-LOG.txt` (a
  timestamped log of runs on this workstation on 2026-09-09).

No text on any card was invented; nothing was copy-edited "for the visual" if
that would misrepresent what the actual script prints.

## B00 · Ask (cold open)

- Greeting: `Habari, Liam` (Swahili — Ep 34 used Jambo; Habari is fresh).
- Command shown: the one-line audit ask (see `beat_sheet.json`).
- runningText: `running check_keys.py…`
- Three output lines describe what the reel is about to show, in the order
  it will show it: the three status states, the exit-code quirk, the redaction
  proof.

## B10 · Your Turn (handoff)

The paste-ready prompt asks Claude Code to *audit* the script against its
own docstring — write a one-line failing test that would catch the exit-code
drift. The prompt is explicit that Claude should NOT fix the script — the
point is to notice the mismatch, not to submit a PR.

Verbatim on the composer:

```
From a fresh checkout of https://github.com/nikbearbrown/brutalist.art —
(1) open runtime/scripts/check_keys.py. (2) Read the docstring on lines
8-10 verbatim: what does it promise about the exit code? (3) Read the
main() body. What variable's value would need to change for the promise
to hold? (4) Write ONE pytest-style test that would FAIL against the
current code and PASS if the promise were kept — no fix, just the test.
(5) Tell me whether the ./art help line about "SI key" refers to
anything currently probed by the script.
```

Grading (three lines in the composer output slot):
1. Docstring quoted verbatim; the exit-code promise identified.
2. One failing test asserting `main()` returns 1 when a row is `invalid`.
3. SI-key drift acknowledged — no probe exists.

## Determinism / seeds

- `BrutalistHesitantWriter` seed: `keys-b01` (stable, same seed → identical
  performance across renders). Portrait variant uses the same seed.
- `ClaudeTitleOutro` mascot: slug-seeded from
  `claude-liam-brutalist-command-keys` (locked, per `OUTRO-LOCK.md`).
- All Kokoro TTS uses voice `am_onyx`; the generator is deterministic given
  the same text and voice.

## Explicit non-goals

- No `./art keys` invocation is asked to actually *log in* to Higgsfield;
  the reel treats login as out of scope. The point is that the tool
  DOESN'T care whether you log in — it just reports.
- No `.env` values are shown (except the deliberately synthetic
  `MY_SECRET=this-should-never-print` used to demonstrate redaction, which
  is not a real credential anywhere).
- The Your-Turn prompt does not ask for a network call, an install, or a
  commit — only a read + a test.
