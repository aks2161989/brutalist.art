# RIFF — The godot-gdd Skill
# run_id: 0084792391494bda81c23c7b93a0404a

## Riff observations from SKILL.md

### What the skill gets right

The coverage contract ("every section or a written exclusion") is a sharp design choice.
It forces the author to admit what they skipped, and why — rather than quietly omitting
inconvenient sections. Most GDD explainers cherry-pick the interesting parts; this one
treats completeness as a first-class requirement.

The four status labels are the most teachable element. "Proposed / Implemented / Observed /
Pending" forces a distinction that GDDs routinely blur: a feature that is implemented may
not be accepted, and a test that passed may not close the acceptance case the GDD defined.
The skill's design is built around that gap.

### Where it bites

The self-demo requirement is hard to satisfy. godot-gdd needs a real game project with
a written GDD to demonstrate anything live. Most Brutalist batch runs will not have a
game project available. The SELF-DEMO LAW says to show a PIPELINE slate naming what is
needed — which this reel does for the checker beat (B06 shows the documented interface
labeled as such, not a fake run).

The walker modifier is well-specified but adds cognitive overhead: four extra bookends
on top of the walkthrough. For a short GDD this may feel ceremonial. The skill doesn't
address how to compress the bookends for a simple two-section GDD — that's left to the
author's judgment.

### Suggested next experiments

- Run godot-gdd on the walker-jumpman game (from godot-gamedev episode) once available,
  and compare what sections get "proposed" vs "observed" labels — the gap is the story.
- Test whether the checker catches a status-label inconsistency between the GDD text
  and the beat_sheet.json labels.

## Artifact references

No clips captured. No gameplay recorded. This reel uses teaching illustrations.
Source-backed evidence: SKILL.md verbatim excerpts in beats B02-B08.
