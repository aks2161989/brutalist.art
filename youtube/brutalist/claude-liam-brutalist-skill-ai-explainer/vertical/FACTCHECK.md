# FACTCHECK

Every factual claim on screen or in narration was verified against the primary source (`skills/make/ai-explainer/SKILL.md` in the isolated toolkit) at author time. This file lists the claims and where they're sourced.

| Beat | Claim | Source |
|---|---|---|
| B00 | The skill is called `ai-explainer`. | SKILL.md `name: ai-explainer`. |
| B00 | It produces the Claude cut (cream page, warm ink, one terracotta accent). | SKILL.md §Brand facts / CLAUDE-BRAND.md (PAGE `#FAF9F5`, INK `#3D3929`, SPARK `#D97757`; "one accent" rule). |
| B00 | Narrator is Liam, in for Bear, using Kokoro `am_onyx`. | SKILL.md §Channels row `claude-liam` — Liam persona, kokoro am_onyx, Teardown register. IN-FOR-BEAR LAW mandates the out-loud line. |
| B01 | ai-explainer is a workflow that reads a whole SKILL file. | SKILL.md §skill-teardown modifier: "Read the WHOLE skill first. The SKILL.md plus everything it references — templates, reference files, scripts, licenses." Also SKILL.md §Lineage: "extends `skills/make/explainer`". |
| B02 | The skill folder holds a SKILL.md plus referenced files that Claude reads. | SKILL.md §skill-teardown "The SKILL.md plus everything it references"; parent §Anatomy across skills follows the same pattern. |
| B02 | Files named on the folder tree (AUDIT-MODE.md, CLAUDE-BRAND.md, OUTRO-LOCK.md, PROSE.md, PIPELINE-SAFETY.md, parent explainer chassis). | Each named directly by SKILL.md (§Trigger, §Channels table, §Hard rules referencing OUTRO-LOCK.md; §Lineage referencing skills/make/explainer; §Step 2 referencing prose/teardown/PROSE.md; §audit modifier referencing AUDIT-MODE.md). PIPELINE-SAFETY.md read from `docs/PIPELINE-SAFETY.md`, referenced by BUILD-PROMPT.md. |
| B02 | SKILL.md size ≈ 31 KB. | Measured: `wc -c` on the toolkit copy returns ~31KB. Displayed as a rough size hint, not a claim of pixel-exact bytes. |
| B03 | Pipeline: Scaffold → Narrate → Audio → Visuals → Compile. | SKILL.md §Flow: Step 1 Scaffold (brand_variant.py), Step 2 Narration (Teardown register), Step 3 Audio (generate_audio_kokoro.py), Step 4 Visuals (Remotion + Manim + Onda), Step 5 Assemble (compile.py). |
| B03 | Kokoro is the clock; visuals conform. | SKILL.md §Step 3: "Audio-first: per-beat MP3 durations become the clock everything conforms to." |
| B03 | Never uploads. Never publishes. | SKILL.md §Hard rules: "Never publish." CLAUDE.md §Rules 5: "Never publish — render instead." |
| B04 | Bookend spine is cold open, BLUF (hesitant writer), body, verdict, handoff, outro. | SKILL.md §skill-teardown modifier "cold open → hesitant-writer overview (Beat 2 BLUF) → body → verdict page → HANDOFF → title-restate outro." (six moves). |
| B04 quote | "The bookends do not change… The modifier governs the MIDDLE." | SKILL.md §skill-teardown modifier — verbatim. |
| B05 | The Claude interface earns its beats — cold open, ask beats, verdict, handoff, outro. | SKILL.md §ILLUSTRATE LAW — the exact set of allowed UI beats. |
| B05 quote | "Two consecutive beats sharing the same visual scheme is the smell; seven videos of composer wallpaper is the failure this law exists to prevent." | SKILL.md §ILLUSTRATE LAW — verbatim. |
| B06 | Ask → Result contract; ask beat shows the ACTUAL prompt; the result renders in the channel palette. | SKILL.md §ASK → RESULT LAW. |
| B06 quote | Verbatim contents. | SKILL.md §ASK → RESULT LAW — verbatim. |
| B07 | Instructions govern; unread rules become bugs. | Inference from SKILL.md's whole "read the whole SKILL.md before building" law + §GATE L "The library is bigger than any session can hold in its head". |
| B07 | Liam is a named substitute, not a Bear clone; rebuilding on Bear voice is a one-variable beat-sheet change. | SKILL.md §Liam substitute narrator — IN-FOR-BEAR LAW rule 2 verbatim: "A named voice, never a clone… if a reel matters enough for Bear's voice, rebuild it on the `claude` default — that's a one-variable change (the beat sheet's voice fields), not a re-authoring." |
| B08 | Verdict artifact card content. | Summarizes the primary decisions above; no new claim. |
| B09 | Paste-ready prompt uses the skill correctly (Kokoro am_onyx, HAI handle, no captions, no publish). | Prompt cross-checked against SKILL.md §Channels row `claude-liam`, §Hard rules "Never publish", metadata schema in beat sheet. |
| B10 | Title restate + Liam in for Bear signoff. | SKILL.md §OUTRO LAW + IN-FOR-BEAR LAW signoff pattern. |

## Corrections applied

- The BLUF trigger phrase `a template pack` (not just `template`) — corrected to the whole phrase `a workflow that reads a whole SKILL file` (not just `workflow`). This follows the SKILL.md §EXECUTIVE-SUMMARY LAW worked-failure guidance: correct the SENTENCE, not just the word.
- The channel handle used in metadata is `@HumanitariansAI`, per this playlist's fixed choice, even though the SKILL.md's channels table lists `claude-liam` under `@NikBearBrown`. Rationale: the invocation's playlist mandate explicitly reassigns to `@HumanitariansAI`. The outro card uses `ClaudeTitleOutro` (title + slug, no hardcoded handle), so no @NikBearBrown handle is imprinted despite the OUTRO-LOCK scope. See CHECKS-REPORT.md §Outro handling.
- Beat 2 uses an explicit `lead_silence_s: 0.8` per SKILL.md §EXECUTIVE-SUMMARY LAW · TIMING. Whether the audio generator actually inserts silence is verified in CHECKS-REPORT.md — the field alone is not a guarantee, per BUILD-PROMPT.md.

## Source update — invocation a2d6bcc90e44499b906ada378401a3db (2026-09-11)

SKILL.md changed since the original build. See landscape FACTCHECK.md §Source update for the full diff summary. Short version: frontmatter description simplified; two new hard rules added (Executable evidence, Math typesetting). Neither addition affects the episode content or any existing claim. Assessment: no re-render required.

## Nothing invented

- No API result was faked. No paid service was called. No screenshot was substituted for a rendered scene. No signature was invented. No human's private path or credentials appear on screen. All quoted text was read from SKILL.md.
