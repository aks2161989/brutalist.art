# SCRIPT — The godot-gdd Skill — Short
# run_id: 2d281e32b355480b8350968778f9d049
# Derived from: claude-liam-brutalist-skill-godot-gdd (parent vertical, 12 beats)
# Cut: B02, B03, B05, B07 dropped — 8 beats, 139.3s

---

## B00 — COLD OPEN (19.0s)
*ClaudeComposerAsk916 · type-on*

Annyeong — this is Liam, in for Bear. There is a Brutalist skill called godot-gdd. Fellows look at that name and assume it writes the design document for them — or reads their game code and extracts one. It does neither. So I asked Claude to read the full skill and explain what actually happens when you point it at an existing Godot project with a GDD already written.

---

## B01 — BLUF (14.3s)
*BrutalistHesitantWriter916 · type-on-correct*

godot-gdd reads an existing game design document and builds the film explaining it — section by section, status labeled, evidence grounded. Not a generator. The document must already exist. That constraint is the entire design of the skill.

---

## B04 — STATUS LABELS (17.4s)
*WalkerGodotSetup916 · flow-reveal*

Every body beat carries one of four status labels. Proposed: a design intent not yet built. Implemented: the feature exists in source. Observed: a test or playthrough confirmed it. Pending: a human decision the film cannot make. These labels are not style choices — they are the distinction the skill exists to enforce.

---

## B06 — CHECKER (19.2s)
*ClaudeCodeBeat916 · code-reveal*

Before rendering and at handoff, you run the checker: art godot-gdd dash-dash-check, passing the reel path and the GDD path. It verifies source hash, section coverage, exact excerpts, evidence files, and beat status labels. What it cannot verify: whether the explanation is true, whether the game is fun, or whether the design was approved. Those stay human.

---

## B08 — DESIGN TELL (22.5s)
*GodotDesignBoard916 · card-reveal-with-highlight*

The design tell is the phrase at the center of the skill: a proposal is not a passing test. A feature can be implemented while its player-experience hypothesis is untested. A test suite can pass while acceptance cases remain open. The skill enforces that distinction in every beat's status label — not pessimism, but precision. Collapsing design intent into implementation evidence is the failure the skill exists to prevent.

---

## B09 — VERDICT (18.0s)
*ClaudeVerdictArtifact916 · artifact-reveal*

godot-gdd does one thing precisely: builds a film that walks through an existing game design document — section by section, status labeled, evidence on screen. What it does not do: write the GDD, change the game, approve the design, or certify it is worth playing. Those are yours. The film is the map. The territory stays human.

---

## B10 — YOUR TURN (21.0s)
*ClaudeComposerAsk916 · type-on*

Your turn. Here is a paste-ready prompt. Take a Godot game project you are working on or studying. Paste this into Claude: Walk me through the GDD for this project using the godot-gdd skill. Tell me which sections are implemented, which are still proposed, and flag any section where the acceptance test is missing or unmeasured. That last part — the missing acceptance test — is the gap most GDDs quietly hide.

---

## B11 — OUTRO (8.0s)
*ClaudeTitleOutro916 · title-card · audio_policy: silence*

Liam, in for Bear.

---

## Dropped beats (not in Short)

| Beat | Act | Reason |
|---|---|---|
| B02 | FRAMEWORK | Four-stage pipeline anatomy belongs in the long film |
| B03 | MECHANISM | Coverage contract detail covered implicitly by B09 verdict |
| B05 | WORKED-EXAMPLE | Causal chain walkthrough belongs in the long film |
| B07 | MECHANISM | Walker modifier bookend detail belongs in the long film |
