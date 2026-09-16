# FACTCHECK — The explainer Skill · Short (9:16)

Every factual claim in the Short's retained narration (B00, B01, B03, B07, B08, B10) is a
direct quote or paraphrase of `skills/make/explainer/SKILL.md` and (for B07's EXECUTABLE-EVIDENCE
sharpening) `docs/EXECUTABLE-EVIDENCE.md`. No numbers, quotes, or mechanisms are invented.
B07 was updated in the parent vertical on 2026-09-11 to include the EXECUTABLE-EVIDENCE.md
content; this Short reuses that updated beat unchanged.

## Verbatim quotes shown on screen (retained beats only)

| Beat | On-screen quote | Location |
|---|---|---|
| B07 | "There is no share to hit… any prior guidance stating a target percentage of vox body beats is superseded by this law." | `explainer SKILL.md · VOX LAW` |

Note: B04, B05, B06 quotes (laundering function, two-axis, slot contract) are present on screen
in those beats, which were dropped from this Short. The B08 verdict card names those mechanisms
by title without quoting them verbatim — acceptable as a recap table-of-contents for the viewer.

## Narration factual claims — checked against source (retained beats)

| Claim | Source | Verdict |
|---|---|---|
| "explainer is the chassis every other explainer bolts onto" | SKILL.md §description + ai-explainer's §Lineage | matches |
| "Vox is a pipeline … sources never match; the treatment does" | SKILL.md §"What Vox actually is" | verbatim |
| "Kokoro voiceover — free, local, and the master clock" | SKILL.md §"The clock" | matches |
| "four sources: Manim fragments, treated stills over Ken Burns, public-domain footage, Remotion annotations" | SKILL.md §design-tokens + §slot contract | matches |
| "Compile conforms every slot to the audio window" | SKILL.md §"THE SLOT CONTRACT" | matches |
| "a still exists for exactly one reason — the still IS the evidence" | SKILL.md §"VOX LAW" | verbatim |
| "If your evidence is locally reproducible — a table, a chart, a test run, code output — execute it and render it" | docs/EXECUTABLE-EVIDENCE.md | matches new B07 update |
| "A terminal photograph is decoration. The running output is the evidence." | docs/EXECUTABLE-EVIDENCE.md | matches |
| "Princeton's actual admissions record — yes. A stock photo of a university — no." | SKILL.md §"VOX LAW" | verbatim example |
| "could this still be swapped … If yes, it is decoration. Cut it." | SKILL.md §"VOX LAW · The test" | matches |
| "shot.type is locked at plan gate; shot.source is late-bound so swaps stay free" | SKILL.md §"THE TWO-AXIS SHOT SYSTEM" | verbatim (verdict card, B08) |
| "Precedence: media/[beat].mp4 > manim/[beat].mp4 > media/[beat].png > SLATE" | SKILL.md §"THE SLOT CONTRACT" first bullet | verbatim (verdict card, B08) |
| "First pass is always a watchable film — slates are a request, not a defect" | SKILL.md §"THE SLOT CONTRACT" | matches (verdict card, B08) |

## Claims deliberately NOT made in the Short

- No promise that any specific runtime script exists beyond what SKILL.md references.
- No claim that a specific runtime target or percentage exists (VOX LAW's "no share to hit"
  explicitly removes percentage guidance).
- No case study shipped as evidence — the tuning is doctrine.

## Verdict-recap danglers (B08 in the Short)

B08's verdict recap names "two-axis shot system" and "slot contract" as skill components without
a Short-side walkthrough beat (B05 and B06 are dropped). Accepted as a table-of-contents summary
of the whole skill shape; the 16:9 long covers each mechanism with a dedicated beat. The viewer
receives a label, not a claim that the detail was shown.

## Availability log

- `generate_audio_kokoro.py` — original audio generated for the parent vertical; no new
  synthesis for this Short. Retained beats' mp3s are byte-copies.
- `remotion_scenes.py` — no re-render for this Short; all beats are native portrait copies
  from the parent vertical.
- `compile.py` — RUN; Short compiled at 3840 height from retained beats.
- `final_frame_check.py` — RUN as Gate V; 12 frames (6 beats × 50%/85%), 0 blockers, 0 majors.
- `type_check.py` (GATE T) — absent in this snapshot; not fabricated as passing.
