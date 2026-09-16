# TYPECHECK — The guests Skill — Short (visual typography review)

This project has no legacy type checker (mypy/tsc is not part of the current
build). "TYPECHECK" here is the visual typography and layout review of the
compiled Short — the schema fields on the beat sheet were validated at build
time by `runtime/scripts/build_safety.py::validate_project` (raised no error).

## Beat sheet schema (runtime check)

```
$ python3 -c "import json; from runtime.scripts.build_safety import validate_project; \
    validate_project(json.loads(open('beat_sheet.json').read()))"
```

Ran clean inside both `shorts.py` and `compile.py`. Every `beat_id` matches
`[A-Z][A-Z0-9_]*`; `metadata.slug` matches the filename-safe regex; the
persistent-voice check (`metadata.voice` == `metadata.voice_kokoro` ==
`am_onyx`) passed.

## Composition prop schemas (Zod, at render time)

Every retained beat's render was the parent's native portrait — already
validated against its 916 composition's Zod schema when the parent reel was
rendered. The Short reused the finished mp4s and did not re-invoke Remotion;
therefore the Zod schemas were not re-executed on this run. Prop text
(narration, verdict lines, pipeline labels) is identical to the parent's
sheet — no risk of schema drift from the Short's cut.

## Visual typography review (per beat)

| Beat | Composition | Coverage | Contrast | Portrait safe.b/t/l/r | Notes |
|---|---|---|---|---|---|
| B00 | ClaudeComposerAsk916 | Composer chrome + three-line answer + folder chip inside safe area; large negative space below (per Claude UI treatment). | INK on cream + terracotta send button — high. | All labels inside safe area; folder chip at ~0.60 y. | No `channel_title` overlay — deliberately omitted (memory `feedback_channel_title_portrait_bleed`). |
| B01 | BrutalistHesitantWriter916 | Five-line serif fills the vertical safe area (portrait-aware scale patch, `fontSize:130 lineSpacing:2.4`) — coverage clearly ≥ 55% per FILL_MIN. | INK serif + terracotta 'copies' before correction — high. | Widest line ('A board member') fits horizontally with generous margin. | Correction lands cleanly: 'copies' → 'prunes the fellows spine.' |
| B03 | SkillTeardownPipeline916 | Seven stacked nodes span most of the safe area; INPUT and OUTPUT pill cards frame the six phases. | INK on cream + terracotta on THE VIDEO node — high. | All nodes inside safe area; the footerNote ('Only the middle…') sits close to the OUTPUT card edge but remains legible and inside safe.b. | Sparkline 'Bookends around the guest's file.' visible at bottom. |
| B09 | ClaudeVerdictArtifact916 | Verdict card with 6 numbered lines fills mid-portrait area; artifact title 'The guests Skill' + heading 'A frame. Not a re-edit.' above the list. | INK body + terracotta bullets — high. | All lines inside card and inside safe area. | Line 4 'GATE G' and line 5 'screen-clean' introduce those terms in one line each — self-defining in the compressed summary. |
| B11 | ClaudeTitleOutro916 | Title + handle sit centered on ink ground; brand rails at top/bottom. | Cream on ink — high. | Title and handle inside safe area. | Slug-seeded pixel-mascot animates near the end of the 3.2 s beat (not visible in every sampled frame — sample is beat-relative 15/50/85%). |

## Palette lint carry-overs

The compiler emitted two `SKIN LINT` lines (B00 and B11) noting the `*916`
composition names against the aspect-blind `palette=claude` rule. These are
the vertical parent's already-accepted portrait-native trade-offs, listed in
the parent's `metadata.build.skin_warnings` — not new to this Short.

## No captions burned in

`metadata.captions=false`. Frame review confirmed no subtitle track and no
burned-in text captions.

## Conclusion

Typography passes. No blockers, no majors. Human review of the final export
is pending.
