# SHOTLIST — The duration-planner Skill (portrait companion)

Portrait 9:16 reel, native 2160×3840 output (composed at 1080×1920, compiled
to 4K portrait). Same 11 beats as landscape; every scene renders through its
native `<Pattern>916` composition — no cropping, no letterbox, no upscale.

| Beat | Composition (9:16) | Type | Duration (s) | Portrait-specific note |
|---|---|---|---|---|
| B00 | `ClaudeComposerAsk916` | ASK | 14.57 | Composer stacks vertically. Same greeting `Sawadee, Liam`, same command, same three output lines. `channel_title` metadata REMOVED (see CHECKS-REPORT.md) — the folder chip inside the composer still shows `@HumanitariansAI`. |
| B01 | `BrutalistHesitantWriter916` | BLUF | 15.00 | Reflowed to 7 short lines (`Your / video / duration / is your / target. / Size the / script.`) at fontSize 210. Requires the scale-bug patch to the shared BrutalistHesitantWriter (`portrait ? min(w/1080, h/1920) : min(w/1920, h/1080)`) so the serif fills the portrait safe area — see feedback memory `feedback_hesitant_writer_portrait_scale.md`. Landscape math unchanged. `lead_silence_s: 0.8` preserved. |
| B02 | `SkillTeardownAnatomy916` | FRAMEWORK | 18.79 | Native portrait composition (added to Root.tsx in `SkillTeardown-Generic`). Folder tree reflows vertically inside `left: width*0.12, right: width*0.08`. |
| B03 | `SkillTeardownPipeline916` | FRAMEWORK | 20.16 | Native portrait. Pipeline nodes squeeze to `boxW = min(200, (w*0.78)/n − 20) = 120` at 1080 wide — still legible. |
| B04 | `SkillTeardownMechanism916` | MECHANISM · ACT 1 | 21.70 | Native portrait. Heading, body, quote, verdict pill stack vertically in the taller safe. |
| B05 | `SkillTeardownMechanism916` | WORKED EXAMPLE | 22.51 | Same, with the content_type floor rows. |
| B06 | `SkillTeardownMechanism916` | MECHANISM · ACT 3 | 25.86 | Same, HOLD_FLOOR. |
| B07 | `SkillTeardownMechanism916` | FALSIFIABILITY | 24.32 | Same, padding-is-a-coherence-violation. |
| B08 | `ClaudeVerdictArtifact916` | VERDICT | 18.58 | Card sizes to `min(w*0.84, 1560)`; at 1080 wide → cardW = 907. 6 verdict lines wrap once each. |
| B09 | `ClaudeComposerAsk916` | YOUR TURN | 28.57 | Same paste-ready prompt as landscape; wraps into 3 command lines on portrait. |
| B10 | `ClaudeTitleOutro916` | OUTRO | 3.95 | Native portrait; handle `@NikBearBrown` hardcoded per OUTRO-LOCK.md; slug-seeded mascot. |

Total ~ **214 s** (3 min 34 s). Same as landscape — the audio didn't change,
only visual props for portrait reflow. Native full-length companion. NOT a
Shorts cut (which would cap at 3 min).

## Composition registrations added (Root.tsx)

Three native 1080×1920 sibling compositions for the shared
SkillTeardown components (they use `useVideoConfig()` for all layout math,
so no component fork was needed):

```tsx
<Composition id="SkillTeardownAnatomy916"    width={1080} height={1920} … />
<Composition id="SkillTeardownPipeline916"   width={1080} height={1920} … />
<Composition id="SkillTeardownMechanism916"  width={1080} height={1920} … />
```

Ran `./art scene-index` after registration. `./art scenes --check` confirmed
all three are RENDERABLE at 9:16.

## Component patch: BrutalistHesitantWriter portrait scale

`runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` L223 patched from
`Math.min(width/1920, height/1080)` to a portrait-aware branch. Rationale:
per feedback memory, the shipped math collapses to 0.5625 at 9:16, halving
the serif and dropping B01 portrait to 19 % underfill. Patched math uses
`min(w/1080, h/1920)` when `height > width`, keeping the landscape 16:9
computation identical. Applies universally to the whole reel batch, not just
this episode.
