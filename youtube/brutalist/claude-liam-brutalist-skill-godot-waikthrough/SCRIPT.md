# SCRIPT — The godot-waikthrough Skill
# run_id: 4d4269b669dd4b84a92a266e5bff804f

Persona: **Liam, in for Bear**. Register: Teardown. Voice: Kokoro am_onyx.
Channel: @HumanitariansAI. Slug: claude-liam-brutalist-skill-godot-waikthrough.

---

## B00 — Cold Open (ClaudeComposerAsk) ~23s

Annyeong — this is Liam, in for Bear. There is a Brutalist skill called
godot-waikthrough. Most fellows read that name and assume it is a screen
recorder — drop a Godot project in, get a gameplay video out. It is not. So
I asked Claude to read the full skill and explain what actually happens when
you point it at a game.

*On screen: composer types "What does `godot-waikthrough` actually do? Read
skills/make/godot-waikthrough/SKILL.md — is this a screen recorder, a game
builder, or something else entirely?" → three result lines: "It plays the
game." / "Riff captures the why." / "It makes a narrated walkthrough film."*

---

## B01 — BLUF (BrutalistHesitantWriter) ~20s + 0.8s lead silence

The name reads like a screen recorder. But godot-waikthrough is the riff
skill applied to gameplay: it plays the game through its actual input path,
captures what the engine renders, and invokes riff to narrate what happened
on screen, the mechanism behind it, and the trade-offs the design made.

*On screen: "godot-waikthrough records the game. Capture in. Film out." →
"records" struck in terracotta → replaced with "riffs" → final text settles.*

---

## B02 — Pipeline Framework (WalkerGodotSetup flow) ~26s

Here is the flow. You supply a path to a running Godot project. Claude
identifies implemented features from source and a real run, distinguishing
built from planned and broken. It drives the game through its normal input
path, captures the rendered viewport, and invokes riff — which inspects
captured frames and writes narration around what changed, why it matters,
and the trade-off. The pipeline then assembles and renders a four-K
walkthrough film.

*On screen: five stages reveal in sequence — Identify → Capture → Riff →
Assemble → Render. Riff stage in terracotta.*

---

## B03 — Anatomy / Two Modes (SkillTeardownAnatomy) ~27s

The skill has two modes. Standard mode opens on the game and its objective —
Liam's brief introduction, then riff through the feature coverage. Walker
mode adds four AI-explainer bookends: a Claude composer beat with the
design-document prompt, a hesitant-writer beat summarizing what was built,
the gameplay riff body, then verdict and your-turn. Walker mode is invoked
by putting the word walker before the game path.

*On screen: skill folder tree reveals (SKILL.md highlighted terracotta),
then standard and walker mode entries, with callout box.*

---

## B04 — Phase 1: Identify (GodotDesignBoard) ~27s

Phase one is the inventory. The skill reads the game's design document and
its source, then walks the project — scripts, scenes, input map — and
compares. Every feature gets a status: built, planned, or broken. A feature
that appears in the GDD but has no code yet stays planned. A feature with
code that throws an error stays implemented with empty evidence — not
relabeled planned to pass the check. The inventory drives the play route.

*On screen: GDD excerpt left; feature status cards right — Built, Planned,
Broken, coverage.json. Cards reveal in sequence.*

---

## B05 — Phase 2: Play and Capture (WalkerGodotSetup terminal) ~24s

Phase two plays and captures. The skill drives the game through its normal
input path — manually or with a deterministic input driver. Either way, it
captures the real rendered viewport. The driver may observe position and
state to choose inputs, but it cannot teleport the player, set completion
flags, disable collisions, or call test-only shortcuts. Scripted-input
captures are labeled as such. They are not human playtests.

*On screen: terminal reconstruction showing Godot Movie Maker invocation,
input log lines, and final capture/run-01.mp4 labeled "scripted-input".*

---

## B06 — The Riff Mechanic (GodotDevWorkbench code) ~23s

The riff mechanic is the heart of the skill. After capturing, riff inspects
each feature's captured frames and writes narration around three things:
what changed on screen, why that mechanism works that way, and the useful
trade-off the design made. Source-code facts and untested judgments are
identified as such. The human judges feel and fun. Riff plays, records,
explains, and checks.

*On screen: RIFF.md structure shown as code with line highlights — artifact
+ time range, observation, mechanism, trade-off, narration. Right panel:
field descriptions.*

---

## B07 — Walker Bookend Sequence (WalkerGodotSetup flow) ~27s

In walker mode, the film gains four structured bookends, in this exact order.
First: a Claude composer beat where the prompt begins "Please use Walker to
convert my game design document about dot-dot-dot" and describes the game's
actual idea. Second: a hesitant-writer beat summarizing what was built — not
the GDD promises, the actual delivered slice. Third: the gameplay riff body.
Fourth: verdict, then your-turn, then the regular outro.

*On screen: six-stage flow — B00 GDD prompt → B01 Built result → Gameplay
body → Verdict → Your Turn → Regular outro.*

---

## B08 — Design Tell (SkillTeardownMechanism) ~25s

The design tell is explicit in the skill file — and worth reading verbatim.
The skill cannot secretly fix the game. No teleporting the player past a
blocker, no disabling collisions to claim a passed level, no calling
test-only shortcuts to manufacture a completion receipt. A driver may observe
position and state to choose inputs. It may not change the game. The honest
path: if it cannot run, report the exact blocker.

*On screen: heading "Don't fix the game." Body text. Verbatim quote:
"Do not secretly fix the game to make a demonstration succeed. If it cannot
run, report the exact blocker; no fake gameplay in place of an engine run."
Verdict pill: "Honest contract".*

---

## B09 — Falsifiability / Self-Demo Limitation (SkillTeardownMechanism) ~26s

The falsifiability gate is built into the design: if the game cannot run,
the skill does not fake the result — it reports the exact blocker. No
substitute fixture, no screenshot slideshow, no imagined success. This reel
runs that limitation honestly. There is no Godot project in this isolated
build, so we demonstrated the mechanism with labeled teaching illustrations.
A full godot-waikthrough build needs a real running game.

*On screen: heading "If it can't run, report the blocker." Body + check
command quote. Verdict pill: "Honest limitation".*

---

## B10 — Verdict (ClaudeVerdictArtifact) ~24s

Verdict. What the skill gets right: it makes the evidence contract explicit
from the first phase. Identify from source plus a real run, not the GDD.
Capture the real viewport, not a substitute fixture. Riff on what is visible,
not what the code says should happen. The limitation is structural: this
skill requires a real running game as input. Give it a shallow game and the
walkthrough film will be shallow too.

*On screen: verdict artifact — four lines landing in sequence.*

---

## B11 — Your Turn (ClaudeComposerAsk) ~50s

Your turn. Here is the paste-ready prompt. "Read skills-slash-make-slash-
godot-waikthrough-slash-SKILL-dot-M-D in full. I have a Godot 4 project at
[path]. Produce a Phase 1 feature inventory: list every implemented feature
from source and mark each as built, planned, or broken. Then write
coverage-dot-json for my game." Replace [path] with any Godot 4 project
folder you have. When Claude comes back, verify the inventory against what
you know the game actually does. If a feature is missing, ask it to read
that specific script and trace the input path. The inventory quality is the
quality of the walkthrough film. Liam, in for Bear.

*On screen: composer types prompt, send button arms terracotta.*

---

## B12 — Outro (ClaudeTitleOutro) 7s (silence)

*On screen: "The godot-waikthrough Skill." — EB Garamond serif, terracotta
period. @NikBearBrown handle. Slug-seeded mascot animation. Regular jingle.*

narration_text field: "Liam, in for Bear." (for record; audio_policy: silence)
