# PROMPTS.md — Brutalist Command: art smoke

Every Remotion beat here renders with props authored directly in
`beat_sheet.json`. No text-to-image, no LLM generation, no paid API.
The single natural-language prompt shown ON SCREEN in the reel is the
Your-Turn handoff in B09.

## B09 — Your Turn prompt (paste-ready, exact text as it appears on screen)

```
From my brutalist.art toolkit root:
(1) run ./art smoke and save the whole stdout+stderr to /tmp/smoke.txt.
(2) Do NOT edit runtime/scripts/smoke_test.sh or the fixture.
(3) Read smoke_test.sh once.
(4) In three lines, tell me:
    (a) which of GATE SIZE, GATE TYPE, GATE AUDIO the run reached;
    (b) which stage refused (Kokoro / run.sh / one of the three gates)
        and quote the one-line error;
    (c) which file on disk the FAILING gate would have measured had the run
        gotten there (name the path relative to the scratch dir).
(5) Tell me whether you were tempted to patch smoke_test.sh or the fixture,
    and why you did not.
```

**Why it earns the beat.** The prompt is an INTERESTING one for a fellow: it
teaches how to read a shell test and defends the gate contract against the
easy-out response of patching the failing check. The narration reads it aloud
verbatim and discusses what to watch for in Claude's answer.

**Expected artifact.** A three-line report identifying the reached stages
and the refused stage, plus a short reflection on the "do not patch" clause.

**Test of success.** Claude names the failing stage (currently GATE 0's
`generate_audio_kokoro.py`, refusing on the slug regex), quotes the
`[kokoro] REFUSED:` line verbatim, points at the file the failing gate
never got to measure (`_smoke-slate.mp4` in the scratch dir), and explicitly
declines to patch the script.

## Illustration prompts

None — all illustrations for this reel are pure Remotion compositions
driven by props in `beat_sheet.json`. There is no image-generation step.
