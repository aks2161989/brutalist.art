# FACTCHECK — The duration-planner Skill · Short (9:16)

This Short is a whole-beat cut of the parent film
`claude-liam-brutalist-skill-duration-planner/vertical/` (parent master SHA-256
`82e1bd11b25b1243becdf762631892904c774deb296f6b5c47db59b6aafca39c`). Every
retained beat's per-beat MP3 and MP4 was copied byte-identical from the parent
via `shorts.py`; no narration was rewritten, sped up, or clipped.

Retained beats: **B00, B01, B04, B05, B07, B08, B10** (7 of 11 parent beats).
Dropped beats: **B02, B03, B06, B09** — reasons in `CUT-PLAN.json`.

## Source authority

The parent film's `FACTCHECK.md` (below) is inherited unchanged (Gate F). This
short-side header records ONLY the delta introduced by the whole-beat cut: what
was dropped, and whether the remaining narration still stands on the source
without the dropped beats.

## Delta from parent — dropped-beat impact

| Dropped beat | Content lost | Does the retained narration still stand on source? |
|---|---|---|
| B02 (skill anatomy) | Folder tree of `SKILL.md`, `reference/`, `scripts/pace_check.py` | Yes — the Short's thesis (B04) and floor table (B05) do not depend on the anatomy view. The verdict (B08) still names `pace_check.py` as advisory, which is verifiable in `SKILL.md` step 6. |
| B03 (five-phase pipeline diagram) | Visualisation of `content_type → measure → floor → ceiling → runtime` | Yes — B04 states the thesis directly, B05 states the consolidation-floor rule directly, and B08 recaps the pipeline verbally. |
| B06 (HOLD_FLOOR / assemble.py sync) | Mechanism: scene base holds final frame; `assemble.py` pads audio with matching silence | The B08 verdict names "Kokoro narration is the master clock; assemble.py pads audio to match the video hold" — the mechanism is stated, not re-taught. This is a table-of-contents-style recap (same pattern used in the explainer-Short's `FACTCHECK.md`). |
| B09 (Your Turn extended composer) | Paste-ready `pace_check.py` prompt + three viewer checks | REPOLOOP-SHORTS-PROMPT §4 explicitly permits dropping the extended exercise. The Short still names the two levers (script-sizing and holds) in plain language; the 16:9 long carries the paste-ready prompt. |

## Verdict-recap dangler

B08 names `assemble.py pads audio to match the video hold` without a Short-side
walkthrough beat. Accepted as a table-of-contents summary (parallel to the
explainer-Short's B08 handling of `two-axis` / `slot-contract`). The claim is
still verifiable against SKILL.md §"The audio-first reality" — nothing was
invented for the recap.

## No fabricated approvals

`approvals: {}` in the beat_sheet metadata. This Short has no human sign-off
yet. The parent film's approvals dictionary is inherited unchanged (also `{}`
at capture). Bear's viewing and editing is next; publishing is a separate
authorized workflow governed by `docs/FELLOWS-SUBMISSION.md`.

---

# Inherited parent FACTCHECK (Gate F — verbatim)

Every factual claim in the narration is a quote from, or a direct paraphrase
of, `skills/make/duration-planner/SKILL.md` (SOURCE-SNAPSHOT SHA-256
`07dc8136…`). No numbers, quotes or mechanisms are invented.

## Verbatim quotes shown on screen

| Beat | On-screen quote | Location in SKILL.md |
|---|---|---|
| B04 | "Duration is an OUTPUT, never a target." | §opening (line 22 of SKILL.md) |
| B05 | "Floors are minimums, enforced with holds." | §"The consolidation floor" (line 87) |
| B06 | "Re-render AND re-assemble together; rendering with one and assembling with the other would desync." | §"The audio-first reality" (lines 47–49) — dropped in Short cut |
| B07 | "Padding to reach 1:00 is as wrong as compressing to reach 0:30." | §"Don't pad" (lines 96–97) |

All quotes copy-pasted from the SKILL file. No paraphrase-shown-as-quote.

## Narration factual claims — checked against source

| Claim | Source line(s) | Verdict |
|---|---|---|
| "duration is an output, never a target" | SKILL.md §opening | verbatim |
| "complex mechanism lands at 3–4 min; definitional at 30–60 s" | SKILL.md §opening line 20 | verbatim (paraphrased for spoken delivery — "three or four minutes … thirty to sixty seconds") |
| "audio-first pipeline; Kokoro is the master clock" | SKILL.md §"The audio-first reality" | matches (timings.json drives the beat clock) |
| "two levers: script-sizing and holds" | SKILL.md §"The audio-first reality" lines 28–37 | matches |
| "HOLD_FLOOR built into scene base; assemble.py pads audio matching silence" | SKILL.md §"The audio-first reality" lines 42–49 | matches (B06 in parent; recapped in B08 in Short) |
| "hold_floor: false disables it per video" | SKILL.md line 47 | matches (parent only — B06 dropped in Short) |
| "title floor 3–5s; realworld 4–5s; structure/geometric 6–8s; data 6–8s; mechanism 6–10s; equation 7–12s" | SKILL.md floor table | matches every row |
| "below-floor → hold; over-ceiling → split" | SKILL.md §"How to pace a video" steps 3–4 | matches |
| "padding to reach a number is a coherence violation → extraneous load" | SKILL.md §"Don't pad" | matches |
| "6-minute rule is engagement (MOOC watch-time), not learning; doesn't replicate in enrolled courses" | SKILL.md §"Engagement is not the target" | matches |
| "pace_check.py is advisory; never edits the sheet" | SKILL.md line 124 | matches |
| "content_type feeds both this skill and media-router" | SKILL.md §"Relationship to the other skills" | matches (not shown on-screen; narration only) |

## Claims deliberately NOT made

- No promise that pace_check.py exists in this exact toolkit snapshot — the
  reel describes what the skill IS supposed to do; the on-screen anatomy tree
  in B02 (parent-only) labels `pace_check.py` as "advisory — never edits",
  which matches the SKILL.md description.
- No promise about a specific total runtime target. B08's verdict says
  "total runtime is a byproduct — the skill reports it and stops."
- No claim of clinical study; the phrase "working memory" is used in the
  general cognitive-load sense the SKILL.md itself uses.

## Third-party / evidence claims

The SKILL.md references `reference/duration-evidence.md` for the underlying
research (segmenting principle, cognitive load theory, contested points).
That reference file is not directly quoted in this reel. The reel restates
the SKILL.md's own summary of the evidence (heuristic floors, contested
6-min rule), which is what a teardown should do — the audit target is the
SKILL, not the primary literature.

## Corrections / hedges preserved from source

- The 6-minute engagement rule → labeled "engagement (watch-time) finding
  from MOOCs" and "doesn't replicate in enrolled courses" — matches SKILL.md
  §"Engagement is not the target" almost word-for-word.
- The contested-evidence note on expertise → not repeated in narration (out
  of scope for a 3-minute teardown); reel design errs toward the SKILL.md
  default ("design at the novice-in-this-sub-domain level").

## Handoff prompt (B09) — verified paste-ready (parent-only)

The prompt asks the viewer to run the duration-planner skill on their own
beat sheet. It matches the SKILL.md's own advertised behaviour (`pace_check.py`
reads a beat sheet + `timings.json`, flags below-floor beats, over-ceiling
beats, reports total runtime, advisory only). Nothing in the prompt asks the
skill to do something the SKILL.md doesn't say it does. B09 is dropped in the
Short; the viewer receives it via the 16:9 long.

## No-source-no-verdict compliance

Every body beat's factual claim is either (a) a verbatim quote block on
screen, or (b) a paraphrase whose source line is cited above. The verdict
(B08) and Your Turn (B09) are recapitulations and are exempt per the
teaching-arc checklist in `skills/make/nopunt/SKILL.md`.
