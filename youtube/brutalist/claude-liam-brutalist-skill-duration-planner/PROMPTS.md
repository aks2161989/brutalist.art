# PROMPTS — The duration-planner Skill

## Composer prompts SEEN ON SCREEN

### B00 — cold-open ASK (what the ask is)

```
How long should this video be? Read skills/make/duration-planner/SKILL.md and
tell me how the skill actually decides.
```

Running text: `reading skills/make/duration-planner/SKILL.md…`
Output lines that land after send:
- duration is an OUTPUT, not a target
- script-sizing and holds are the two real levers
- content_type sets the consolidation floor

### B09 — YOUR TURN (paste-ready, viewer runs)

```
Run the duration-planner skill on my beat sheet and timings. For every beat,
report content_type, floor, measured narration, whether it needs a hold, and
whether any beat is over its ceiling and should split. Report total runtime
as an output. Do not edit the sheet.
```

Running text: `paste this into Claude Code…`
Output rubric lines (what the viewer should check afterwards):
- check: below-floor beats getting HOLDS, not shorter next beats
- check: over-ceiling beats — one idea or two? split if two.
- check: any padding to a target? cut it — don't ship the coherence violation.

The prompt is READ ALOUD verbatim; the rubric is DISCUSSED (HANDOFF LAW
read-and-discuss requirement). No screen-only prompt.

## Kokoro TTS prompts

Every beat's narration goes to Kokoro `am_onyx` (Liam) via
`runtime/scripts/generate_audio_kokoro.py`. No prompt engineering — the
narration text in `beat_sheet.json` is the input. No SSML.

## Remotion render invocations

Rendered exclusively via:

```bash
python3 runtime/scripts/remotion_scenes.py \
    /Users/.../youtube/brutalist/claude-liam-brutalist-skill-duration-planner
```

The wrapper picks each beat's `shot.remotion.pattern`, invokes the matching
composition with the beat's props, and stamps provenance back to the sheet.
Environment: `ART_CHROME=<toolkit>/runtime/scripts/chrome_wrap.sh`,
`ART_CHROME_MODE=chrome-for-testing` (Apple App Sandbox workaround — points
Remotion at the already-downloaded `chrome-headless-shell` with
`--single-process --in-process-gpu`; see feedback memory
`feedback_chrome_sandbox.md`).

No `npx remotion render` was hand-rolled. No `--concurrency > 1`. No slates.

## Compile invocations

Landscape 4K:
```bash
python3 runtime/scripts/compile.py \
    /Users/.../youtube/brutalist/claude-liam-brutalist-skill-duration-planner \
    --height 2160 \
    --out /Users/.../claude-liam-brutalist-skill-duration-planner/exports/landscape
```

Portrait 4K (planned in `vertical/` from `art vertical`, native 916
compositions in scene source):
```bash
python3 runtime/scripts/compile.py \
    /Users/.../claude-liam-brutalist-skill-duration-planner/vertical \
    --height 3840 \
    --out /Users/.../claude-liam-brutalist-skill-duration-planner/exports/vertical
```

No `--allow-slates`. No `ART_QC=0`. No `ART_FACTS=0`. Compiler's atomic
verification (produces `.verified.json` sibling with SHA-256 receipt) is
enabled.
