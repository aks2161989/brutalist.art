# GDD-COVERAGE — The godot-gdd Skill
# run_id: 0084792391494bda81c23c7b93a0404a

This file documents how godot-gdd/SKILL.md's top-level sections map to beats in this explainer film.
Note: this is a meta-level coverage document (skill teardown), not coverage of an actual game GDD.

## SKILL.md section coverage

| SKILL.md Section | Beat(s) | Coverage type |
|---|---|---|
| Opening / invocation syntax | B00, B02 | Covered — pipeline overview |
| Read before explaining (section mapping, causal chain) | B03, B05 | Covered — coverage contract + worked example |
| A proposal is not a passing test (status labels) | B04, B08 | Covered — status labels + design tell |
| Visualize the GDD with the game | B05 | Covered — causal chain, mention of evidence requirement |
| Liam and Walker structure | B07 | Covered — walker modifier |
| Evidence, rendering and handoff (checker) | B06 | Covered — checker syntax and limits |
| Outro / title requirement | B11 | Covered — ClaudeTitleOutro per OUTRO-LOCK.md |

## Sections excluded from beats (with written reason)

| Section | Exclusion reason |
|---|---|
| Full required document list (GDD-COVERAGE.md, gdd-evidence.json, RIFF.md) | Output file list covered implicitly in B02 (assemble stage); listing all filenames in narration is a podcast move, not a teaching beat. Documented here. |
| Manim/Remotion rendering detail (remotion_scenes.py invocation) | Covered by the Brutalist pipeline episode; not specific to godot-gdd |
| godot-capture contract reference | Requires godot-waikthrough skill context; out of scope for this episode |

## Self-demo limitation (documented)

godot-gdd requires a real Godot game project with a written GDD. No real game project
is available in this sandbox invocation. All teaching illustrations are labeled:
- "PROPOSED FRAMEWORK · teaching illustration" (GodotDesignBoard status banners)
- Walker-jumpman is a fictional game name used as illustrative example only

A real run would require: a game package directory, a GDD.md file, and a `project.godot`
in the game subdirectory. The checker (`./art godot-gdd --check REEL --gdd GDD.md`)
was not executed; its interface is shown from SKILL.md documentation only.
