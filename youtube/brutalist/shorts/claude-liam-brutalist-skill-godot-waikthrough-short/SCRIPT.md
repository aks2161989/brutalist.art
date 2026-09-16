# Script — The godot-waikthrough Skill — Short

run_id: 109fafd34ed24e8fa79141774f22d69a
Kind: short (8/13 beats retained from vertical companion)
Duration: 158.0s (2:38)

---

## B00 — ASK (16.2s)

**Annyeong — this is Liam, in for Bear. There is a Brutalist skill called godot-waikthrough. Most fellows read that name and assume it is a screen recorder — drop a Godot project in, get a gameplay video out. It is not. So I asked Claude to read the full skill and explain what actually happens when you point it at a game.**

---

## B01 — BLUF (15.6s)

**The name reads like a screen recorder. But godot-waikthrough is the riff skill applied to gameplay: it plays the game through its actual input path, captures what the engine renders, and invokes riff to narrate what happened on screen, the mechanism behind it, and the trade-offs the design made.**

---

## B02 — PIPELINE (22.7s)

**Here is the flow. You supply a path to a running Godot project. Claude identifies implemented features from source and a real run, distinguishing built from planned and broken. It drives the game through its normal input path, captures the rendered viewport, and invokes riff — which inspects captured frames and writes narration around what changed, why it matters, and the trade-off. The pipeline then assembles and renders a four-K walkthrough film.**

---

## B06 — MECHANISM (20.5s)

**The riff mechanic is the heart of the skill. After capturing, riff inspects each feature's captured frames and writes narration around three things: what changed on screen, why that mechanism works that way, and the useful trade-off the design made. Source-code facts and untested judgments are identified as such. The human judges feel and fun. Riff plays, records, explains, and checks.**

---

## B08 — MECHANISM / DESIGN TELL (21.7s)

**The design tell is explicit in the skill file — and worth reading verbatim. The skill cannot secretly fix the game. No teleporting the player past a blocker, no disabling collisions to claim a passed level, no calling test-only shortcuts to manufacture a completion receipt. A driver may observe position and state to choose inputs. It may not change the game. The honest path: if it cannot run, report the exact blocker.**

---

## B10 — VERDICT (20.5s)

**Verdict. What the skill gets right: it makes the evidence contract explicit from the first phase. Identify from source plus a real run, not the GDD. Capture the real viewport, not a substitute fixture. Riff on what is visible, not what the code says should happen. The limitation is structural: this skill requires a real running game as input. Give it a shallow game and the walkthrough film will be shallow too.**

---

## B11 — HANDOFF / YOUR TURN (33.8s)

**Your turn. Here is the paste-ready prompt. 'Read skills-slash-make-slash-godot-waikthrough-slash-SKILL-dot-M-D in full. I have a Godot 4 project at [path]. Produce a Phase 1 feature inventory: list every implemented feature from source and mark each as built, planned, or broken. Then write coverage-dot-json for my game.' Replace [path] with any Godot 4 project folder you have. When Claude comes back, verify the inventory against what you know the game actually does. If a feature is missing, ask it to read that specific script and trace the input path. The inventory quality is the quality of the walkthrough film. Liam, in for Bear.**

---

## B12 — OUTRO (7.0s, silence)

**Liam, in for Bear.**

---

## Dropped

- B03 (Anatomy — two-mode folder structure): long-film depth
- B04 (Phase 1 detail — GDD vs inventory cards): worked-example for long
- B05 (Phase 2 capture — terminal walkthrough): implementation detail
- B07 (Walker mode bookend order): advanced-use detail
- B09 (Falsifiability/self-demo): B08 covers honesty contract; B10 names the structural limitation
