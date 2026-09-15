# SCRIPT — The riff Skill
**Episode:** claude-liam-brutalist-skill-riff  
**Run ID:** deb461319da4431a9518a6feef4fa1ec  
**Date:** 2026-09-12  
**Voice:** Liam, in for Bear — Kokoro am_onyx  
**Channel:** @HumanitariansAI  

---

## B00 — Cold Open (ClaudeComposerAsk)

Bula, this is Liam, in for Bear. The riff skill watches before it speaks. You hand it a local clip, a Remotion scene, or a rendered artifact. It probes the thing, inspects frames and the event sequence, then writes commentary grounded in what visibly happens — not what the filename suggests.

*Screen:* Composer card opens. Greeting "Bula, Liam" types above. Command types in. runningText "probing artifact..." Output lines cascade: "look at it first," "judge what you see," "record the evidence."

---

## B01 — BLUF (BrutalistHesitantWriter)

Watch the writer walk this back. Riff does not generate opinions about visual artifacts. It generates observations. The footage is evidence — timecodes, event sequence, settled frames. The voice is the verdict. Look, then speak.

*Screen:* Writer types "riff\ngenerates opinions." Hesitates on "opinions." Deletes it. Types "observations." Corrected text settles.

*Misconception corrected:* opinions → observations  
*Seed:* riff-b01-2026

---

## B02 — Skill Anatomy (SkillTeardownAnatomy)

A skill in Brutalist is a folder that Claude reads before it works. The riff skill lives at skills/make/riff/, with one file: SKILL.md. That file carries everything — inputs, outputs, voice, the three artifact modes, the integrity rules. No other configuration. Liam reads it before writing a single word of commentary.

*Screen:* Folder tree reveals: skills/make/ → riff/ (accent) → SKILL.md (accent, tagged "doctrine"). Callout: "The file is the instruction. Claude reads it before working."

---

## B03 — Pipeline (SkillTeardownPipeline)

The pipeline is four phases. First: look — probe the artifact, inspect representative frames, keep timecodes, listen to the audio if it bears on a claim. Second: observe — record what is visible, separate from what you infer. Third: write — build each riff beat around what changed, why that matters, and the trade-off. Fourth: record — save everything in RIFF.md.

*Screen:* Pipeline draws left-to-right: artifact → LOOK → OBSERVE → WRITE (terracotta, accent) → RECORD → RIFF.md + film.

---

## B04 — Mechanism 1: Look before writing (SkillTeardownMechanism)

Mechanism one: look before writing. The skill is explicit about this. For a clip, you probe it and inspect representative frames and the event sequence. For a Remotion or Manim scene, you find the existing renderer first, inspect its props and source, then render a small test fixture. For gameplay, you use actual engine capture. Never substitute a fixture, animation, screenshot slideshow, or imagined success.

*Screen:* Heading "Look before writing." Body: three artifact modes. Verbatim quote card: "A frame can show a state; it cannot establish response time, motion, or causality." Verdict pill: "LOOK FIRST — ALWAYS."

---

## B05 — Self-Demo: actual scene search (ClaudeCodeBeat)

Here is that 'look first' step, applied to this build. Before authoring a single beat, we ran ./art scenes to search the scene library. The top hits, RiffSplit and RiffLottery, are reel-local components — context-specific, not generic. The generic SkillTeardown scenes are what we actually needed. That search is the proof of look: if we had skipped it, we might have slated beats that already had purpose-built components sitting two directories away.

*Screen:* Code card shows actual command output from this build (see demo/RUN-LOG.txt). Two commands: ./art scenes "riff commentary observe inspect" → 6 candidates (top 2 reel-local). ./art scenes --check SkillTeardownAnatomy SkillTeardownMechanism → RENDERABLE.

*Source:* demo/RUN-LOG.txt — real output from this workstation, 2026-09-11.

---

## B06 — Mechanism 2: Evidence before interpretation (SkillTeardownMechanism)

Mechanism two: evidence before interpretation. The footage carries the evidence — the event, the timecode, the visible state. The voice carries the interpretation — what changed, why it matters, the trade-off it reveals. They are not the same job. A riff that narrates a list the viewer cannot see is a podcast, not a film. If the voice is doing evidence work, the evidence belongs on screen.

*Screen:* Heading "Footage carries evidence. Voice carries verdict." Body: two roles distinguished. Verbatim quote: "Let the footage carry the evidence and the voice carry the interpretation." Verdict: "FOOTAGE = EVIDENCE."

---

## B07 — Mechanism 3: RIFF.md output (SkillTeardownMechanism)

The output is RIFF.md — a structured log that keeps observations separate from interpretations and hypotheses. Each row records: artifact and time range, the visible observation, the interpretation and its source if needed, the narration line, and a suggested next experiment. Critically: missing or failed renders stay in the report. You do not silently omit what did not work.

*Screen:* Heading "RIFF.md separates the seen from the inferred." Body: five RIFF.md columns. Verbatim quote: "Missing or failed renders stay in the report; do not silently omit them." Verdict: "FAILURES INCLUDED."

---

## B08 — Design Tell (SkillTeardownMechanism)

The design tell is this line — 'never call a scripted route a human playtest or infer fun, fairness, or accessibility from it.' That is not a style preference. That is an epistemic rule encoded directly in the spec. What it gets right: it stops Claude from manufacturing confident claims about human experience from deterministic code. Where it bites: a riff on a game that has not been playtested cannot reach the most interesting question — is it fun? The skill is honest about that limit instead of faking past it.

*Screen:* Heading "Honest by design." Body: what it gets right vs where it bites. Verbatim quote: the integrity rule. Verdict: "HONEST BY DESIGN."

---

## B09 — Verdict (ClaudeVerdictArtifact)

The verdict. Riff is the skill that earns its claims. Look first — probe the artifact, inspect frames, keep timecodes. Evidence second — footage carries the evidence, voice carries the verdict. Record everything — RIFF.md keeps observations separate from inferences, failures included. And: never call a scripted route a human playtest. Four rules. One epistemic discipline.

*Screen:* Artifact card "riff" with four verdict lines cascading in.

---

## B10 — Your Turn (ClaudeComposerAsk)

Your turn. Paste this into Claude Code, pointed at any Remotion scene in your brutalist.art toolkit. Run './art scenes SceneName' and read the props. Render a small test clip. Sample frames with ffmpeg at fifteen, fifty, and eighty-five percent of its duration. Then write a RIFF.md: artifact and time range, visible observation, your interpretation, the narration line, and one suggested next experiment. The rubric: did you separate what you saw from what you inferred? Does every claim in your narration have a corresponding frame or timecode? If not, the evidence is still missing — go back and look.

*Screen:* Composer, greeting "Your Turn." Prompt types in. runningText "paste this into Claude Code..." Output lines: RIFF.md, every claim tied, failures included.

---

## B11 — Outro (ClaudeTitleOutro)

The riff Skill. Liam, in for Bear, for Humanitarians AI.

*Screen:* Title card "The riff Skill." @NikBearBrown handle (hardcoded per OUTRO-LOCK.md). Mascot animation (slug-seeded). Jingle plays. No narration over card.
