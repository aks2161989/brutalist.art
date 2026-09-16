# FACTCHECK — The guests Skill (portrait / vertical companion)

Same source-of-truth as the landscape pass: `skills/make/guests/SKILL.md` in the
isolated toolkit copy. See `../FACTCHECK.md` for the full per-beat traceability
map — every narration claim in the portrait companion is IDENTICAL to the
landscape claim (same script, same Kokoro mp3s), and every quote block, verdict
pill, folder-tree row, pipeline label and Your Turn rubric item is unchanged.

The only per-aspect difference is layout, not content:

- `pattern` is the `*916` variant of every landscape composition
  (`ClaudeComposerAsk916`, `BrutalistHesitantWriter916`, `SkillTeardownAnatomy916`,
  `SkillTeardownPipeline916`, `SkillTeardownMechanism916`, `ClaudeVerdictArtifact916`,
  `ClaudeTitleOutro916`). All are registered natively in this isolated toolkit's
  `Root.tsx` at 1080×1920, reflowing via `useVideoConfig()` — no center-cropping.
- B01 hesitant writer is authored with a five-line split (`copies the / fellows spine.`
  wraps to two lines) at `fontSize: 118`, `lineSpacing: 2.2` so the serif meets
  the Gate V `FILL_MIN=0.55` coverage rule under the portrait-aware scale patch.
- `metadata.channel_title` is deliberately omitted for portrait — the
  compile-time overlay bleeds past portrait `safe.b` (memory
  `feedback_channel_title_portrait_bleed`); the folder chip inside
  `ClaudeComposerAsk916` still carries `@HumanitariansAI`.

## Boundary claims (identical to landscape)

Same list as `../FACTCHECK.md`: no guest was named, no signature simulated, no
publication claim, no re-use of another episode's results, no evaluation. The
portrait companion inherits every honesty guarantee of the landscape master.
