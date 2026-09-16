# PROMPTS — The godot-gdd Skill — Short
# run_id: 2d281e32b355480b8350968778f9d049

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
- Any section where no acceptance test is stated — the gap most GDDs quietly hide
- Any "pending human decision" label — those need your judgment, not Claude's

**Usage:** Point Claude at a real Godot project folder containing a GDD.md. The GDD must
exist before you run the skill; it does not write the document for you.

---

## B00 cold open prompt (reconstructed teaching illustration)

```
/godot-gdd walker-jumpman/ GDD.md
```

Skill invocation format: `godot-gdd <game-package-path> [GDD.md path]`.
Labeled as a reconstructed teaching illustration — not a real session output.

---

## Production prompts used in this Short

No external generative AI prompts were used. All scene content is deterministic,
sourced from parent vertical beat sheet props (SKILL.md verbatim quotes).
Narration audio reused from parent vertical unchanged.
