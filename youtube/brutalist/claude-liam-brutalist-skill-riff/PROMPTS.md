# PROMPTS — The riff Skill
**Episode:** claude-liam-brutalist-skill-riff  
**Run ID:** deb461319da4431a9518a6feef4fa1ec  
**Date:** 2026-09-12  

---

## Handoff prompt (B10 — the viewer's paste-ready task)

```
I have a Remotion scene called [SceneName] in my brutalist.art toolkit. Apply the riff skill:
(1) find it with './art scenes [SceneName]' and read the props;
(2) render a small test clip with 'python3 runtime/scripts/remotion_scenes.py';
(3) sample frames with ffmpeg at 15%, 50%, and 85% of its duration;
(4) write RIFF.md — artifact + time range | visible observation | interpretation |
    narration line | suggested next experiment.
Separate what you saw from what you inferred.
Flag any claim in your narration that lacks a corresponding frame or timecode.
```

**Expected artifact:** RIFF.md with five-column observation log  
**Test of success:** every claim in narration has a corresponding timecode or sampled frame; observations and inferences appear in separate columns; any failed renders are listed, not silently omitted

**Why this prompt:** It applies the skill to the viewer's own material using the exact three-step "look first" workflow: find the renderer, render a fixture, inspect frames. The rubric forces the viewer to verify that they followed the evidence-first principle, not just wrote opinions.

---

## Cold open prompt (B00 — the ask Claude answers)

```
I have a Remotion scene that just rendered. Before I write a single word of commentary,
what does the riff skill tell me to do?
```

**Shown answer:** look at it first (probe, inspect frames, keep timecodes) → judge what you see (what changed, why, the trade-off) → record the evidence (RIFF.md separates seen from inferred)

---

## Demo commands (B05 — self-demo, real output)

```bash
# Search the scene library before authoring any beat
./art scenes "riff commentary observe inspect"

# Confirm the scenes we need are RENDERABLE
./art scenes --check SkillTeardownAnatomy SkillTeardownMechanism
```

Source: `demo/RUN-LOG.txt` — actual output from this workstation, 2026-09-11.
