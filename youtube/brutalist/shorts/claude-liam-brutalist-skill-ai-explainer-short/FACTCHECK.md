# FACTCHECK — Short cut

This Short reuses parent narration audio unchanged. Every factual claim on
screen or in the retained narration was verified against
`skills/make/ai-explainer/SKILL.md` in the isolated toolkit at author time and
is re-listed here for the nine retained beats only. Dropped beats
(B02 general skill anatomy, B09 extended Your Turn) are documented in
CUT-PLAN.json and not audited here.

| Beat | Claim | Source |
|---|---|---|
| B00 | The skill is called `ai-explainer`. | SKILL.md `name: ai-explainer`. |
| B00 | It produces the Claude cut (cream page, warm ink, one terracotta accent). | SKILL.md §Brand facts / CLAUDE-BRAND.md (PAGE `#FAF9F5`, INK `#3D3929`, SPARK `#D97757`; "one accent" rule). |
| B00 | Narrator is Liam, in for Bear, using Kokoro `am_onyx`. | SKILL.md §Channels row `claude-liam` — Liam persona, kokoro am_onyx, Teardown register. IN-FOR-BEAR LAW mandates the out-loud line. |
| B00 | Self-referential — this Short's parent film was built by the skill it tears down. | SKILL.md §skill-teardown modifier lets the skill teardown itself; the parent reel's build stamp confirms `filled_by: remotion:*` for each rendered beat. |
| B01 | ai-explainer is a workflow that reads a whole SKILL file — not a template pack. | SKILL.md §skill-teardown modifier: "Read the WHOLE skill first. The SKILL.md plus everything it references — templates, reference files, scripts, licenses." §Lineage: "extends `skills/make/explainer`". §Hard rules: SKILL.md governs. |
| B01 | Sets the brand and voice, drives every phase, and refuses to publish. | SKILL.md §Brand facts (palette/type baked in), §Flow (five phases), §Hard rules "Never publish". |
| B03 | Pipeline: Scaffold → Narrate → Audio → Visuals → Compile. | SKILL.md §Flow: Step 1 Scaffold (brand_variant.py), Step 2 Narration (Teardown register), Step 3 Audio (generate_audio_kokoro.py), Step 4 Visuals (Remotion + Manim + Onda), Step 5 Assemble (compile.py). |
| B03 | Kokoro is the clock; visuals conform. | SKILL.md §Step 3: "Audio-first: per-beat MP3 durations become the clock everything conforms to." |
| B03 | Compiles to a 4K master beside the reel. Never uploads. Never publishes. | SKILL.md §Hard rules: "Never publish." CLAUDE.md §Rules 5: "Never publish — render instead." compile.py default output height 720; `--height 3840` documented as the 4K path (see compile.py argparse). |
| B04 | Bookend spine is cold open, BLUF (hesitant writer), body, verdict, handoff, outro. | SKILL.md §skill-teardown modifier: "cold open → hesitant-writer overview (Beat 2 BLUF) → body → verdict page → HANDOFF → title-restate outro." (six moves). |
| B04 quote | "The bookends do not change… The modifier governs the MIDDLE." | SKILL.md §skill-teardown modifier — verbatim. |
| B05 | The Claude interface earns its beats — cold open, ask beats, verdict, handoff, outro. | SKILL.md §ILLUSTRATE LAW — the exact set of allowed UI beats. |
| B05 quote | "Two consecutive beats sharing the same visual scheme is the smell; seven videos of composer wallpaper is the failure this law exists to prevent." | SKILL.md §ILLUSTRATE LAW — verbatim. |
| B06 | Ask → Result contract; ask beat shows the ACTUAL prompt; the result renders in the channel palette. | SKILL.md §ASK → RESULT LAW. |
| B06 quote | Verbatim contents. | SKILL.md §ASK → RESULT LAW — verbatim. |
| B07 | Instructions govern; unread rules become bugs. | Inference from SKILL.md's whole "read the whole SKILL.md before building" law + §GATE L "The library is bigger than any session can hold in its head". |
| B07 | Liam is a named substitute, not a Bear clone; rebuilding on Bear voice is a one-variable beat-sheet change. | SKILL.md §Liam substitute narrator — IN-FOR-BEAR LAW rule 2 verbatim: "A named voice, never a clone… if a reel matters enough for Bear's voice, rebuild it on the `claude` default — that's a one-variable change (the beat sheet's voice fields), not a re-authoring." |
| B08 | Verdict artifact card lines each restate a retained beat's claim. | Summarizes the primary decisions above; no new claim. Six lines map to B01, B04, B05, B06, B03, and the Hard rules. |
| B10 | Title restate + Liam in for Bear signoff. | SKILL.md §OUTRO LAW + IN-FOR-BEAR LAW signoff pattern. |

## Corrections and cut-time editorial notes

- Dropped B02 (generic skill-folder anatomy) removes the SKILL.md "31 KB" size
  callout and the folder-tree file list. No retained narration references
  those specifics, so no downstream claim is left dangling.
- Dropped B09 (extended Your Turn) removes the paste-ready-prompt readout.
  This is explicitly permitted by REPOLOOP-SHORTS-PROMPT.md ("the Short need
  not read the long film's full exercise aloud"). No retained beat depends on
  it; the outro card carries the channel invitation.
- Retained B07's "missing Beat two" reference resolves to retained B01 (BLUF).
- Retained B05's "Second decision" resolves to retained B04's "first design
  decision". No numbered reference is left dangling.
- Retained B08's verdict bullet "Prompts as receipts (ASK → RESULT)" is
  grounded in retained B06; the "Fixed bookends. Free interior." bullet in
  retained B04; the "UI earns every beat (ILLUSTRATE LAW)" bullet in
  retained B05; the "Kokoro is the clock. compile.py conforms." bullet in
  retained B03; the "A workflow, not a template pack." bullet in retained
  B01; the "Renders only. Never publishes." bullet in retained B03/B01.
- Metadata.channel was renamed from `channel_title` (which triggers a
  compile-time overlay whose position bleeds outside portrait safe area in
  this toolkit; see FEEDBACK memory `channel-title-portrait-bleed`).
- No new narration was authored; every retained MP3 is a byte-for-byte copy
  of the parent's `mp3/beat-<BID>.mp3`.

## Nothing invented

- No API result was faked. No paid service was called. No screenshot was
  substituted for a rendered scene. No signature was invented. No human's
  private path or credentials appear on screen. All quoted text was read
  from the toolkit's SKILL.md and copied audio.
