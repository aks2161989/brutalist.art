# FACTCHECK.md — The anthropics Skill — Short

*This Short retains 7 beats from the parent film verbatim (B00, B01, B03, B04, B07, B08, B10) and drops 4 (B02 anatomy, B05 probes, B06 register, B09 Your Turn). Every factual claim below is the parent's, re-scoped to only the beats this Short actually contains. Nothing new was written or verified.*

## Verifiable-against-file claims — retained beats only

| Beat | Claim | Verified against | Verdict |
|---|---|---|---|
| B00 | "reads a whole company's output — code, papers, content, capabilities" | `skills/make/anthropics/SKILL.md` description block, first three lines | ✓ |
| B03 | "four modes" (`--repo`, `--paper`, `--content`, `--capability`) | SKILL.md §"Four modes, one router" table (4 rows) | ✓ |
| B03 | "dash-repo dispatches to git-explainer's analysis engine; dash-paper dispatches to ai-paper" | SKILL.md, sentence directly under the table | ✓ |
| B03 | `--capability` is the mode "no vendor channel will ever ship" | SKILL.md "the one thing no vendor channel can ship" (description block) and "because no vendor channel ships 'the competitor is better at this.'" | ✓ (paraphrase) |
| B04 | "If the episode could be made by reading the docs, it is not this series." | SKILL.md, verbatim | ✓ |
| B04 | "Every episode needs at least one spine beat only visible by opening the artifact and running it." | SKILL.md, verbatim (compressed slightly for cadence — "only visible by opening the artifact and running it" is from the file) | ✓ |
| B07 | "git-explainer and ai-paper aren't shipped inside this toolkit snapshot" | `ls skills/make/` — neither directory is present in the snapshot recorded by `SOURCE-SNAPSHOT.json`. Recorded in parent `SOURCES.md` "Not used, and why". | ✓ (observed) |
| B07 | "Never generate an image that poses as evidence of a fact." | SKILL.md §"The generation-honesty law", verbatim | ✓ |

## Numbers on screen — reconciliation (retained beats only)

- **4 modes** appears in B03's on-screen pipeline nodes AND in B03 narration. The SKILL.md table has exactly 4 rows.
- **1 router** appears on B03 as the framing verb and in narration. The SKILL.md heading is "Four modes, one router".
- The number **142** (line count of `SKILL.md`) was cited in the dropped B02 anatomy. This Short does **not** cite that number — the anatomy claim was cut cleanly and does not survive in any other beat.

## Speech / display convention (unchanged from parent)

- Narration says `dash-repo`, `dash-paper`, `dash-content`, `dash-capability`; on-screen labels keep the literal `--repo` / `--paper` / `--content` / `--capability`. This is a Kokoro-pronunciation choice for the audio channel only; the visual channel is exact.

## Claims deliberately not made

- The Short does **not** claim to run the `anthropics` skill against a real Anthropic artefact.
- The Short does **not** claim this SKILL file is the current tip of the public repo — only that its SHA-256 matches `SOURCE-SNAPSHOT.json` at build time.
- The Short does **not** repeat any competitor names or specific model comparisons.
- The Short does **not** include the parent's verbatim probes list (B05), register quotes (B06), or paste-ready --capability prompt (B09). Those claims live in the 16:9 long — not here.

## Verdict-card bullets vs. retained narration

The verdict card (B08) shows five lines. Three are earned by kept beats (B00/B01/B04/B07). Two — "Behaviour is the thesis; defaults are the tell" and "Independence stated once. Situated. Honest about matches." — are capsules of the dropped B05 / B06 material. In the Short's narration they collapse into "It reads the artifact rather than the artifact's press release, and it says so out loud." The card reads correctly as a summary; the two capsule lines act as teasers for the 16:9 long rather than callbacks to previously spoken content. Flagged as a minor coherence note.
