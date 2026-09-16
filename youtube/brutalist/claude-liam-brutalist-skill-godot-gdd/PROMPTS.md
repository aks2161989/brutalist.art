# PROMPTS — The godot-gdd Skill
# run_id: 0084792391494bda81c23c7b93a0404a

## Handoff prompt (B10 — Your Turn)

```
Walk me through the GDD for this project using the godot-gdd skill. Tell me which sections
are implemented, which are still proposed, and flag any section where the acceptance test
is missing or unmeasured.
```

**What this does:** Claude reads the GDD via the godot-gdd skill, maps every section to
a status label (proposed/implemented/observed/pending), and flags acceptance tests that
are absent or unmeasured.

**What to look for in the output:**
- Sections labeled "proposed" that you thought were implemented
- Any section where no acceptance test is stated — this is the most common GDD gap
- Any "pending human decision" label — those need your judgment, not Claude's

**Usage:** Point Claude at a real Godot project folder containing a GDD.md (or equivalent).
The skill outputs to `<game-package>/youtube/claude-liam-<game>-gdd/`. The GDD must
exist before you run the skill; it does not write the document for you.

---

## B00 cold open prompt (reconstructed teaching illustration)

```
/godot-gdd walker-jumpman/ GDD.md
```

This shows the skill invocation format: `godot-gdd <game-package-path> [GDD.md path]`.
Labeled as a reconstructed teaching illustration — not a real session output.

---

## Production prompts used in this build

No external generative AI prompts were used. All scene content is deterministic,
sourced from SKILL.md verbatim quotes and scene component props.
