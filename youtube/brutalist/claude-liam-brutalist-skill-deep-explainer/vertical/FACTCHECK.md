# FACTCHECK.md — The deep-explainer Skill

Every claim in the narration is checked against
`skills/make/deep-explainer/SKILL.md` at SHA-256
`c268b6d698fcf117f2cb89f4f5c9efb1bed007c294ea64a5016726a4988c601e`. Direct
quotes are shown on screen in the mechanism beats and match the SKILL.md
verbatim.

| Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| B00 | "There is a skill called deep-explainer" — the skill exists | HOLDS | `skills/make/deep-explainer/SKILL.md` front-matter, `name: deep-explainer` | — |
| B00 | Fellows should not treat it as "just a longer ai-explainer" | HOLDS | Skill sections "When this skill (and when not)" and "Lineage" — the whole file argues this | — |
| B01 | Correction: "act-structured, with two extra gates" | HOLDS | Sections "The spine (fixed)" (act structure) and "THE TWO HARD GATES (beyond the parents')" (D1, D2) | — |
| B02 | Skill folder contains SKILL.md plus three reference files (continuity, shopping-list, vox-beats) | HOLDS | `ls -la skills/make/deep-explainer/reference/` — recorded in `demo/01-skill-folder.txt` | — |
| B03 | "deep-explainer extends ai-explainer, which extends explainer. Nothing below repeals a parent law." | VERBATIM | Section "Lineage — what governs when": "This skill EXTENDS ai-explainer, which extends explainer. Nothing below repeals a parent law; this file only adds the genre's own contracts." | — |
| B03 | Four bookends, show-don't-tell law, illustrate law inherited | HOLDS | Same section names them explicitly (COLD OPEN LAW, ILLUSTRATE LAW, SHOW-DON'T-TELL LAW, OUTRO LAW) | — |
| B04 | Fixed spine: cold open → hesitant writer → acts → verdict → YOUR TURN → outro | HOLDS | Section "The spine (fixed)" — exact enumeration in the SKILL | — |
| B06 | "5–10 min band is the natural landing zone for a multi-act concept, never a target to pad toward" | NEAR-VERBATIM | Section "Lineage — Pacing": "The 5–10 min band is the genre's natural landing zone for a multi-act concept, never a target to pad toward." | Narration paraphrases; on-screen quote is verbatim. |
| B06 | Quote: "If the arc lands at 4:40, ship 4:40." | VERBATIM | Same section, same paragraph. | — |
| B07 | "The old skill had a vox quota — twenty to twenty-five percent" | HOLDS | Section "THE BEAT MIX — no quota (VOX LAW governs)": "The vox percentage is dead (2026-09-02). It used to say ~20–25% of body beats should be pantry stills, with a WARN outside 15–30%." | — |
| B07 | "a still earns its beat only when the still IS the evidence" | NEAR-VERBATIM | Same section: "a still is used when the still IS the evidence — the actual record, the real document the narration makes a claim about — and never as texture." | — |
| B07 | Quote: "A film whose evidence is text, code, or data correctly has zero vox beats." | NEAR-VERBATIM | Same section: "A deep-explainer whose evidence is text, code, or data correctly has **zero** vox beats." Narration shortens "deep-explainer" → "film" for the on-screen quote to fit the card; label preserves the meaning. | On-screen quote reads "A film whose evidence is text, code, or data correctly has zero vox beats." — flagged NEAR-VERBATIM. |
| B08 | Continuity chains only inside vox runs; max 3 beats; never across acts | HOLDS | Section "CONTINUITY — the vox-run contract (and its deliberate limit)": "A run never crosses an act boundary. Max run length 3 beats." | — |
| B08 | Quote: "Never attempt frame-continuity across the whole episode." | NEAR-VERBATIM | Same section: "Never attempt frame-continuity across the whole episode: chaining 40+ beats through prose prompts is exactly the fragility this rule exists to kill." Quote card carries only the first sentence. | — |
| B10 | Gate D1: first compile is a full-length watchable previz; vox slates, Manim/Remotion for real, real audio | HOLDS | Section "Gate D1 — the slate previz IS the first deliverable" — all elements named explicitly | — |
| B10 | Quote: "Never present a previz as a finished cut." | VERBATIM | Last sentence of the Gate D1 section. | — |
| B11 | Gate D2: SHOPPING.md written AFTER audio lock, never before | HOLDS | Section "Gate D2 — the shopping list (duration-locked, tier-tagged)": "`SHOPPING.md` is written **after audio lock** (never before…)" | — |
| B11 | "at least seven point two seconds of X … trimming lossless … stretching lossy" | HOLDS | Section same, and `reference/shopping-list.md`: "A card written after lock asks for '≥ 7.2 s of X': the constraint moves upstream, and trimming down (lossless) becomes the default conform operation." (illustrative example — 7.2s comes from the reference file's own example). | Narration flags "at least seven point two seconds" as an illustrative example. |
| B11 | Quote: "SHOPPING.md is written after audio lock (never before)." | VERBATIM | Same section (opening sentence). | — |
| B12 | Output contract: beat_sheet.json, BUILD-PROMPT.md, BUILD-LOG.md, FACTCHECK.md, SHOPPING.md, SOURCES.md, pantry/, media/, manim/, clips/, mp3/ | VERBATIM | Section "Output contract" of the SKILL — exact enumeration. | — |
| B13 | "actually running end-to-end would take pantry sourcing, human review, and 5–10 minutes of audio" | HOLDS | Section "Workflow (each gate is the human's)" — steps 6 (pantry fill) and Pacing section (5–10 min band). No fabrication. | — |
| B14 | Reach for deep-explainer when source is multi-act; ai-explainer when it's one insight | NEAR-VERBATIM | Section "When this skill (and when not)": "Use deep-explainer when the concept is multi-act … If the source is one insight, it's an ai-explainer." | — |
| B15 | The paste-ready prompt is a genuine invocation of the skill | HOLDS | Skill's own workflow (step 1 "plan") requires reading the source and presenting the act map + lane histogram before authoring; the prompt asks for exactly that. | — |
| B16 | Title: "The deep-explainer Skill." — matches THIS INVOCATION | HOLDS | Supervisor `episode.title` = "The deep-explainer Skill" | — |

## What we did NOT claim (avoided fabrications)

- No claim that Kokoro is unlimited or that any Claude subscription tier is
  described.
- No claim that this film demonstrates a full deep-explainer end-to-end
  run — B13 flags it as a labeled documented limitation, not a demo.
- No claim about specific model versions or dates on screen (DOUBLE-CHECK
  LAW / strip-the-datable is honored).
- No claim about the outro card's channel — the on-screen handle is
  hardcoded `@NikBearBrown` per OUTRO-LOCK.md; SOURCES.md flags this for
  human review before publication.

## Unverified / follow-up

- The "7.2 s" figure in B11 comes from the SKILL's OWN illustrative example
  (`reference/shopping-list.md` line 13). It is a shape-of-the-rule number,
  not a real production measurement. Narration says "at least seven point
  two seconds of X" and preserves that framing.
