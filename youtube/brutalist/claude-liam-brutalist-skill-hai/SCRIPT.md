# SCRIPT.md — The hai Skill (claude-liam teardown)

Episode: `claude-liam-brutalist-skill-hai`
Run id: `d660d0c9949a427980931d1c010c2f47`
Register: Teardown · Voice: Kokoro `am_onyx` · Persona: Liam, in for Bear · Channel: `@HumanitariansAI`

Narration is the voice's copy only. Show/motion cues live in `SHOTLIST.md` and `beat_sheet.json`.

---

## B00 — ASK (ClaudeComposerAsk cold open)

> Hallo, this is Liam, in for Bear. Today we tear down the `hai` skill. It is the audience-preset that forks any reel into a Humanitarians AI cut — Plain register, muted palette, one required exercise. The trick is that the original is never touched. Here is the mental model.

## B01 — BLUF (BrutalistHesitantWriter)

Typed text: `The hai skill\nreformats a reel\nfor the HAI audience.`
Trigger: `reformats` → Replacement: `forks`

> The easy read — the one the word "brand variant" invites — is that `hai` reformats an existing reel. It does not. Nothing is reformatted. Nothing is overwritten. `hai` FORKS the sheet into a new `hai-` directory beside it, and every downstream change happens there. The source stays byte-identical.

## B02 — FRAMEWORK · ANATOMY (SkillTeardownAnatomy)

> First, the anatomy. On the toolkit side there is SKILL.md — the doctrine, the six-step flow, and the register rules. Then there is `brand_variant.py`, a small deterministic scaffolder. On the OUTPUT side, `hai` places a sibling directory next to whatever you pointed it at — for a reel, `hai-<slug>` beside the reel; for a lecture, into `hai-lectures/`. Inside that directory sits `beat_sheet.hai.json`, a metadata block already stamped for the humanitarians channel, and a `_variant_todo` checklist you work through with Claude. Small on disk. Human where it matters.

## B03 — FRAMEWORK · PIPELINE (SkillTeardownPipeline)

> The flow is fixed. Six steps. Scaffold first — deterministic, no spend, no writes to the source. Then rewrite every beat's narration in the Plain register. Optional: at most one Irreducibly-Human tangent — a bounded aside, most reels get none. Then, second-to-last, insert one CLI worked exercise the viewer can actually paste and run. Last beat, replace with the Humanitarians AI outro. Then verify the ending order. Same shape every episode. The middle is your reel; the shape is the skill's.

## B04 — MECHANISM · ACT 1 · NON-DESTRUCTIVE FORK (SkillTeardownMechanism)

> First design decision, and it sets the safety posture. Every `hai` run writes to a new directory beside the source and never modifies `beat_sheet.json`, build scripts, or media. The scaffolder even refuses to overwrite its own output — you get an "already exists, use --force" error, not a silent clobber. The doctrine reads: source files are never modified. The consequence: `hai` is safe to run against a canonical reel mid-production. Your original cut keeps rendering; the humanitarians cut branches off.

## B05 — MECHANISM · ACT 2 · PLAIN REGISTER (SkillTeardownMechanism)

> Second decision. Plain register is not a softer tone — it is a checklist. Every rewritten beat leads with method, states when to use it, and, required, states when NOT to and where it fails. That third line is the AI main event for busy practitioners. It is not hedging; it is the diagnostic they need. If your rewrite has no failure mode named, you have not done the register — you have just changed adjectives.

## B06 — MECHANISM · ACT 3 · THE CLI EXERCISE (SkillTeardownMechanism)

> Third decision, and it is the one that separates `hai` from a re-skin. The second-to-last beat is a CLI worked exercise, and the schema has five parts. A paste-ready `claude` ask. A concrete OUTPUT description — a plot, a table, a sourced brief. One CHANGE — a single diff that deepens or stress-tests the result. The second OUTPUT after the change. And a next step naming the viewer's own data or question. The rule is genuinely runnable. Not illustrative. Not synthetic. If the viewer cannot copy the ask and run it today, the exercise is a slate in disguise.

## B07 — MECHANISM · ACT 4 · BATCH MODE (SkillTeardownMechanism)

> Fourth decision. Point `hai` at a book directory and it scaffolds every reel and every lecture inside it — one `find`, one loop, one `brand_variant.py` per source. What batch mode does not do is the Plain-register rewrite, the tangent, the exercise, or the outro. Those are per-video, and the SKILL.md is explicit that a batch scaffolder is not a variant renderer. You get thirty `_variant_todo` checklists to work through with Claude, not thirty finished cuts.

## B08 — FALSIFIABILITY (SkillTeardownMechanism)

> Falsifiability. Read the sources together and you find a real disagreement about the HAI voice. `SKILL.md` says af_kore. The runtime scaffolder writes af_bella. And the current brand spec at brands/hai.md says am_onyx, after ElevenLabs was removed in September. Three files, three voices. This teardown IS a claude-liam reel, so we ship am_onyx with Liam's sign-off — the OUTRO-LOCK still governs here. But if you build a real HAI cut this week, treat brands/hai.md as the source of truth, override the scaffolder's voice field, and log the discrepancy. That is what the register asks of you: name the failure mode plainly.

## B09 — VERDICT (ClaudeVerdictArtifact)

> The verdict. `hai` is a non-destructive fork with a checklist, not a re-skin. Six steps, one directory beside the source. The Plain register is a diagnostic, not a tone — the "when NOT to" line is mandatory. The CLI exercise must actually run. Batch mode scaffolds every reel and lecture in a book, but the register rewrite is still per-video. And the voice field is contested across three source files — trust brands/hai.md, override in the sheet, log the discrepancy.

## B10 — YOUR TURN (ClaudeComposerAsk)

> Your turn. Paste this into Claude Code. Read the `hai` skill. Pick one of your own reels — a real one you have already delivered — and run `brand_variant.py` on it with the `hai` argument. Confirm the source `beat_sheet.json` is byte-identical afterwards by comparing SHAs. Then, without shipping the reel, draft the Plain-register rewrite of one body beat: method, when to use, when NOT to and where it fails. Draft the CLI exercise using the five-part schema. Then check three things. Is the source SHA unchanged. Does every rewritten beat name a failure mode. Does the CLI ask genuinely run today, or is it illustrative?

## B11 — OUTRO (ClaudeTitleOutro)

> That was the `hai` Skill. Liam, in for Bear.
