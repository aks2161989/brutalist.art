# PROMPTS.md — What Is Brutalist?

*Every "ask" the reel actually shows on screen, with the exact string, the
scene it renders in, and what happens when someone runs it.*

## B00 — the cold-open ask

**Composer topic:** `HUMANITARIANS AI · BRUTALIST`
**Segment:** `What Is Brutalist?`
**Greeting:** `Ciao, Liam`
**Running text:** `reading the toolkit…`
**Folder chip:** `@HumanitariansAI`

**Ask (typed into the composer):**

```
Explain what Brutalist actually is. Not the slogan — the thing on disk.
```

**Result lines (shown beneath the composer):**

- a beat sheet is a plain-text recipe
- the film is a pure function of the recipe
- judgment stays human — everything else automates

Narration introduces Liam in the first breath and hands off to the body.

## B02 — the beat_sheet.json shown in WibRecipe

Exact excerpt authored from the actual `beat_sheet.json` for this reel
(reformatted for on-screen legibility). Every field maps to a real property in
the file.

```json
{
  "beat_id": "B00",
  "narration_text": "Ciao. This is Liam, in for Bear.",
  "shot": {
    "pattern": "ClaudeComposerAsk",
    "props": {
      "greeting": "Ciao, Liam",
      "segment": "What Is Brutalist?"
    }
  }
}
```

Not synthetic. The narration string above is a truncated form of B00's actual
narration for on-screen size; the full narration is in `SCRIPT.md`.

## B04 — the one edited property shown in WibChange

```
"greeting": "Ciao, Liam"       →       "greeting": "Hola, Liam"
```

Shell line rendered under the code:

```
$ python3 remotion_scenes.py --only B00
→ re-rendering B00.mp4…
```

`remotion_scenes.py --only <BID>` is the actual documented flag (see
`python3 runtime/scripts/remotion_scenes.py --help`). No fictional command.

## B08 — the paste-ready HANDOFF prompt (read aloud, verbatim)

**Composer topic:** `HUMANITARIANS AI · BRUTALIST`
**Segment:** `Your First Brutalist Film`
**Greeting:** `Your Turn` (the persona-less HANDOFF greeting)
**Running text:** `paste this into Claude…`

**Ask (typed into the composer, read aloud in narration):**

```
Clone https://github.com/nikbearbrown/brutalist.art into this folder,
run ./setup --install for me, then draft a beat sheet for a two-minute
Brutalist film about my current project. Keep me out of the terminal —
just tell me what to approve.
```

**Expected artifacts (shown beneath the composer, also the viewer's success
rubric):**

- Claude clones the public toolkit into the folder.
- Claude runs `./setup --install` (which installs the free Python + Remotion
  deps and downloads the Kokoro voice model — ~340 MB, one-time).
- Claude drafts a `beat_sheet.json` the viewer can read and edit.

**Test of success:** the viewer can open the beat sheet in their editor,
change one narration string, ask Claude to re-render that beat, and see a new
`media/<BID>.mp4` land in the folder. That is the same demonstration the reel
performed in B04.

## Where a paid gate would apply (labeled, never faked)

None on the fellow path. `Optional Higgsfield` (`CLAUDE.md §OPTIONAL UPGRADE`)
would gate certain AI-video beats — but Brutalist's default is Ken Burns
stills. This reel makes no Higgsfield ask.
