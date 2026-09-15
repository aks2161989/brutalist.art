# SCRIPT — The godot-gdd Skill
# slug: claude-liam-brutalist-skill-godot-gdd
# run_id: 0084792391494bda81c23c7b93a0404a
# voice: Liam (in for Bear), Kokoro am_onyx

---

## B00 — Cold Open (ClaudeComposerAsk)

Annyeong — this is Liam, in for Bear. There is a Brutalist skill called godot-gdd. Fellows look at that name and assume it writes the design document for them — or reads their game code and extracts one. It does neither. So I asked Claude to read the full skill and explain what actually happens when you point it at an existing Godot project with a GDD already written.

*[On screen: composer types `/godot-gdd walker-jumpman/ GDD.md`; output: "8 sections found — 7 covered, 1 excluded by design"]*

---

## B01 — BLUF (BrutalistHesitantWriter)
*[lead_silence_s: 0.8 — typing must begin before voice]*

*[On screen: types "godot-gdd generates a design document / for any Godot game you point it at." — hesitates on "generates" (terracotta), backspaces, replaces with "explains"]*

godot-gdd reads an existing game design document and builds the film explaining it — section by section, status labeled, evidence grounded. Not a generator. The document must already exist. That constraint is the entire design of the skill.

---

## B02 — The Pipeline (WalkerGodotSetup, flow mode)

The pipeline has four stages. Read: the full GDD, including appendices and revision history. Map: every top-level section to a beat or an explicit, documented exclusion. Visualize: each requirement beside real game evidence or a clearly labeled proposed diagram. Assemble: via remotion-scenes and compile-py, same as every Brutalist film.

*[On screen: four panels reveal — Read → Map → Visualize → Assemble; spark line: "Film builder, not document generator."]*

---

## B03 — Coverage Contract (GodotDesignBoard, cards layout)

The coverage contract is the strictest rule. Every substantive top-level section must appear in the film — as a beat, or as an exclusion with a written reason. Skipping a section without a note is a violation, not a judgment call. The skill calls this mapping, not summarizing — and the distinction matters.

*[On screen: SKILL.md excerpt "Map every substantive top-level section..." beside four cards: Vision and Pillars, Loops and Mechanics, Scope and Risks, Exclusions]*

---

## B04 — Status Labels (WalkerGodotSetup, flow mode)

Every body beat carries one of four status labels. Proposed: a design intent not yet built. Implemented: the feature exists in source. Observed: a test or playthrough confirmed it. Pending: a human decision the film cannot make. These labels are not style choices — they are the distinction the skill exists to enforce.

*[On screen: four panels reveal — Proposed, Implemented, Observed, Pending; spark line: "A proposal is not a passing test."]*

---

## B05 — Causal Chain (GodotDesignBoard, flow layout) — WORKED EXAMPLE

The design's causal chain is the frame for every explained section. Player experience produces a design rule. That rule has a system owner. The owner produces visible feedback. Feedback maps to an acceptance test. Walk every GDD section through that chain. Any missing link is a gap — and the film must name it, not paper over it.

*[On screen: SKILL.md excerpt beside four flow cards: Player Experience → Design Rule → Visible Feedback → Acceptance Test]*

---

## B06 — The Checker (ClaudeCodeBeat)

Before rendering and at handoff, you run the checker: art godot-gdd dash-dash-check, passing the reel path and the GDD path. It verifies source hash, section coverage, exact excerpts, evidence files, and beat status labels. What it cannot verify: whether the explanation is true, whether the game is fun, or whether the design was approved. Those stay human.

*[On screen: bash code: `./art godot-gdd --check REEL --gdd GDD.md` with VERIFIES and CANNOT VERIFY sections]*

---

## B07 — Walker Modifier (WalkerGodotSetup, flow mode)

The walker modifier adds four explicit bookends to the standard walkthrough. First, a Claude composer opening shows the invocation — reconstructed and labeled, not a live session. Second, a hesitant writer beat states what is built versus proposed. Third, the design walkthrough proper. Then verdict and handoff. Walker is not a separate skill — it is the same pipeline with Claude bookends at the front.

*[On screen: four panels — Claude Composer → Hesitant Writer → Design Walkthrough → Verdict and Handoff]*

---

## B08 — Design Tell (GodotDesignBoard, cards layout) — FALSIFIABILITY

The design tell is the phrase at the center of the skill: a proposal is not a passing test. A feature can be implemented while its player-experience hypothesis is untested. A test suite can pass while acceptance cases remain open. The skill enforces that distinction in every beat's status label — not pessimism, but precision. Collapsing design intent into implementation evidence is the failure the skill exists to prevent.

*[On screen: SKILL.md excerpt beside three cards: The Phrase, What It Costs, What It Buys]*

---

## B09 — Verdict (ClaudeVerdictArtifact)

godot-gdd does one thing precisely: builds a film that walks through an existing game design document — section by section, status labeled, evidence on screen. What it does not do: write the GDD, change the game, approve the design, or certify it is worth playing. Those are yours. The film is the map. The territory stays human.

*[On screen: artifact card — "The GDD explainer, precisely scoped" with five verdict lines]*

---

## B10 — Your Turn (ClaudeComposerAsk, greeting: "Your turn.")

Your turn. Here is a paste-ready prompt. Take a Godot game project you are working on or studying. Paste this into Claude: Walk me through the GDD for this project using the godot-gdd skill. Tell me which sections are implemented, which are still proposed, and flag any section where the acceptance test is missing or unmeasured. That last part — the missing acceptance test — is the gap most GDDs quietly hide.

*[On screen: composer types the full handoff prompt; output: "2 acceptance tests missing · 1 section pending human decision"]*

---

## B11 — Outro (ClaudeTitleOutro)
*[No narration — jingle only per OUTRO-LOCK.md]*

*[On screen: "The godot-gdd Skill." in serif, @NikBearBrown handle, slug-seeded mascot; Liam, in for Bear.]*
