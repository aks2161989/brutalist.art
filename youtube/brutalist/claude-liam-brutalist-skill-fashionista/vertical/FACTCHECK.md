# Fact check — narration ↔ source

Every claim below cites `skills/make/fashionista/SKILL.md` in the isolated
toolkit (SOURCE-SNAPSHOT SHA-256 `22614f44…`).

| # | Claim in narration | Source line | Status |
|---|---|---|---|
| 1 | "fashionista is an experiment, not a fashion series" | SKILL.md preamble: "THE EXPERIMENT: can an AI act as a fashion journalist?" + § "The premise (this governs everything)". | Verified. |
| 2 | "Every episode is one trial" | SKILL.md § "The premise": "Every episode is one trial." | Verbatim. |
| 3 | "The audience is the scoring function" | SKILL.md § "The premise": "the audience is the scoring function." | Verbatim. |
| 4 | "Three-beat structure: INTRO / VIDEO / OUTRO" | SKILL.md § "Structure" (fenced block: INTRO 2–3s / THE VIDEO / OUTRO 2–3s). | Verified structure. |
| 5 | "Total runtime = clip duration + ~5 s" | SKILL.md § "Structure" final line: "Total runtime = clip duration + ~5 s." | Verbatim. |
| 6 | "Video is the master clock" | SKILL.md § "VIDEO IS THE MASTER CLOCK". | Verbatim heading. |
| 7 | "Never stretch, loop, freeze-pad, or slow the video" | SKILL.md § "VIDEO IS THE MASTER CLOCK" bullet 1. | Verbatim. |
| 8 | "If the narration runs long: CUT WORDS. The video does not move." | SKILL.md § "VIDEO IS THE MASTER CLOCK" bullet 4. | Verbatim. |
| 9 | "GATE ASK — the cold-open ask never contains the garment name; the naming is the AI's job, on camera" | SKILL.md § "Structure" INTRO block + Gates table row GATE ASK. | Verified. |
| 10 | "Every garment term is spoken with a stated confidence the viewer can hear" | SKILL.md § "The call": "Every garment term is spoken with a stated confidence the viewer can hear." | Verbatim. |
| 11 | "Hedging is content, not weakness" | SKILL.md § "The call" bullet 3. | Verbatim. |
| 12 | "Comment on the clothes only" | SKILL.md § "The call" bullet 5 + Gates table row GATE SUBJECT. | Verified. |
| 13 | "Two error sources — generator error vs. describer error" | SKILL.md § "Two stacked error sources". | Verbatim section title. |
| 14 | "When these are separable, say which one. When they are not, say that too." | SKILL.md § "Two stacked error sources" closing paragraph. | Verbatim. |
| 15 | "Nobody else is doing this — the most interesting thing the series does" | SKILL.md § "Two stacked error sources" final sentence. | Verbatim. |
| 16 | "CALLS.json — term, confidence, reasoning, timestamp, alternatives, verdict" | SKILL.md § "CALLS ledger" JSON schema. | Verified verbatim. |
| 17 | "The verdict slot stays null until a human fills it from comments" | SKILL.md § "CALLS ledger" closing sentence. | Verbatim. |
| 18 | "Spoken correction ask in the outro" | SKILL.md § "Structure" OUTRO block: `SPOKEN: "If you know this garment, tell me what I got wrong."` + Gates table row GATE ASK. | Verified. |
| 19 | "The two cuts (16:9 and 9:16) are built separately from different source footage" | SKILL.md § "The two cuts — built separately, never derived". | Verified. |
| 20 | "Kokoro am_onyx. Free. Never publishes." | SKILL.md front-matter description ("Kokoro am_onyx, free. Never publishes."). | Verbatim. |

## Deliberately NOT claimed

- The reel does not claim to be a fashionista trial. It is a TEARDOWN of the
  skill, per the ai-explainer skill-teardown modifier.
- No specific date, no specific garment call, no CALLS.json row is asserted.
  The ledger schema is shown as documented output.
- No claim about YouTube publishing, transcoding, or 4K approval.
- No unverified upstream URLs or private paths in narration.

## De-sensationalization applied

- "Every episode is one trial" is kept as a claim about structure, not a
  scientific-experiment claim about statistical power. The SKILL.md is
  explicit that the *audience* is the scoring function; this reel is honest
  about the loop being informal.
- The gates table is described as a build check, not a peer-reviewed
  methodology.
