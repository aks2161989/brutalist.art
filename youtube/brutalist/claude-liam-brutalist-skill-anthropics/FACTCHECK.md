# FACTCHECK.md — The anthropics Skill

*Every factual claim in the narration is checked against the SKILL file,
the toolkit tree, or a demo output. Corrections are recorded here.*

## Verifiable-against-file claims

| Beat | Claim | Verified against | Verdict |
|---|---|---|---|
| B00 | "reads a whole company's output — code, papers, content, capabilities" | SKILL.md description block, first three lines | ✓ |
| B02 | "one hundred and forty-two lines" | `wc -l skills/make/anthropics/SKILL.md` → 142 | ✓ |
| B02 | "one SKILL file" | `ls skills/make/anthropics/` → only `SKILL.md` in the isolated toolkit | ✓ |
| B03 | "four modes" (`--repo`, `--paper`, `--content`, `--capability`) | SKILL.md §"Four modes, one router" table (4 rows) | ✓ |
| B03 | "dash-repo dispatches to git-explainer's analysis engine; dash-paper dispatches to ai-paper" | SKILL.md, sentence directly under the table | ✓ |
| B03 | "no vendor channel can ever ship" the `--capability` mode | SKILL.md "the one thing no vendor channel can ship" (description block) and "because no vendor channel ships 'the competitor is better at this.'" | ✓ (paraphrase) |
| B04 | "If the episode could be made by reading the docs, it is not this series." | SKILL.md, verbatim | ✓ |
| B04 | "Every episode needs at least one spine beat only visible by opening the artifact and running it." | SKILL.md, verbatim (compressed slightly for cadence — "only visible by opening the artifact and running it" is from the file) | ✓ |
| B05 | "Structure and history come free from a repo. Behaviour is the thesis." | SKILL.md §"--repo behavioural probes" — "Structure and history are artifacts of a repo's shape. Behaviour is the thesis." (compressed) | ✓ |
| B05 | The probes list (network, filesystem, DEFAULTS, gating, LICENSE, maintenance) | SKILL.md bullet list §"--repo behavioural probes" | ✓ |
| B05 | "a feature that exists but ships off tells a different story than the paragraph describing it" | SKILL.md DEFAULTS bullet, verbatim | ✓ |
| B05 | "does the released code reproduce the published claim?" | SKILL.md §"--paper: the sharpest fair question" — "Does the released code reproduce the published claim?" | ✓ |
| B05 | "the honest answer is often partially" | SKILL.md "the honest answer is often *partially*" | ✓ |
| B06 | "Another perspective, not a correction." | SKILL.md §"The register", verbatim | ✓ |
| B06 | "builds with Claude daily; nobody is paying for this" | SKILL.md "Builds with Claude daily; nobody is paying for this." (verbatim) | ✓ |
| B06 | "Situated, therefore durable." + "date and a real task" | SKILL.md "Situated, therefore durable." and "situated in a date and a real task" | ✓ |
| B06 | "A matching claim is a finding." | SKILL.md heading, verbatim | ✓ |
| B06 | "manufacturing gaps is the dishonesty this beat is positioned against" | SKILL.md, verbatim | ✓ |
| B07 | "git-explainer and ai-paper aren't shipped inside this toolkit snapshot" | `ls skills/make/` — neither directory is present. Recorded in SOURCES.md "Not used, and why" | ✓ (observed) |
| B07 | "Never generate an image that poses as evidence of a fact." | SKILL.md §"The generation-honesty law", verbatim | ✓ |
| B09 | "Is every claim cited to a file line or an on-screen output?" | SKILL.md §"Fairness rails" — "Every claim cites `file:line` or shows the output." | ✓ |

## Numbers on screen — reconciliation

- **142 lines** appears in B02 narration and on B02's on-screen anatomy card
  (badge next to `SKILL.md`). Source: `wc -l` observed at build time. No
  other line-count number appears anywhere else in the reel — internal
  consistency (Verify Gate) holds by construction.
- **4 modes** appears in B03's on-screen pipeline nodes AND in B03
  narration. The SKILL.md table has exactly 4 rows.
- **1 router** appears on B03 as the framing verb and in narration. The
  SKILL.md heading is "Four modes, one router".

## Corrections applied

- The narration writes `dash-repo`, `dash-paper`, `dash-content`,
  `dash-capability` where the SKILL.md file writes `--repo`, `--paper`,
  `--content`, `--capability`. Kokoro pronounces `--repo` as "dash dash
  repo" which is unnatural at speaking pace; the on-screen labels keep the
  literal double-dash form. This is a de-sensationalization for the audio
  channel only — the visual channel is exact.
- The narration says "one hundred and forty-two lines" instead of "142"
  because Kokoro speaks digits comfortably in either form and long-form
  numerals read as text remove ambiguity.

## Claims deliberately not made

- The reel does **not** claim to run the `anthropics` skill against a real
  Anthropic artefact. That would require the sibling skills (`git-explainer`
  and `ai-paper`) which are absent, and a live target repo. The reel names
  the constraint plainly (B07) instead — this is the SKILL file's own
  fairness rail: "Absence of code is never evidence of bad faith."
- The reel does **not** claim this SKILL file is the current tip of the
  public repo — only that its SHA-256 matches this build's
  `SOURCE-SNAPSHOT.json`.
- The reel does **not** repeat any competitor names or specific model
  comparisons the SKILL file gestures at (e.g. "Codex is better at image
  generation"). Those are the SKILL's own example of *what a capability
  episode would look like*, not this reel's claims.
