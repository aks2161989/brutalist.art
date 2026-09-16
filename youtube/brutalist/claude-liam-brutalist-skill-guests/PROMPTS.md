# PROMPTS — The guests Skill

The two on-screen prompts (cold open + Your Turn) and notes on the isolated
toolkit changes made for this run.

## B00 — Cold open composer

**Greeting:** `Hallo, Liam` (world-language hello — German, one-word cue, fits
the persona word-budget per ai-explainer SKILL.md §The greeting).

**Topic / Segment:** `BRUTALIST · SKILL TEARDOWN` / `The guests Skill`.

**Ask:**

```
What is the `guests` skill? Read skills/make/guests/SKILL.md
and tell me what it actually does with a board member's video.
```

**Answer (three result lines):**

1. a frame around a board member's recording
2. six beats · Claude bookends · standard HAI outro
3. no feedback beat — the guest is not evaluated

**Folder chip:** `@HumanitariansAI` — the playlist's channel context.

## B10 — Your Turn composer

**Greeting:** `Your Turn`. **Topic:** `BRUTALIST · PLAN A GUESTS DRY-RUN`.
**Segment:** `Plan a guests reel without shipping it`.

**Paste-ready prompt (Liam reads aloud):**

```
Read skills/make/guests/SKILL.md. Then plan (DO NOT RUN) a dry-run guests
episode for a hypothetical board member with a 3-min talk: (1) the
ClaudeComposerAsk cold open naming STANDING + SUBJECT; (2) a summary beat
from a fabricated transcript LABELED as a fixture; (3) a descriptive RECAP
with zero evaluative words; (4) a Your Turn prompt; (5) metadata.approvals
for GATE G as a PENDING record with a real subject fingerprint. Do not run
generate_audio_kokoro.py or compile.py.
```

**Three-check rubric (rendered as the composer's output):**

1. check: exactly SIX beats — no feedback beat between video and recap?
2. check: recap is DESCRIPTIVE only — zero evaluative or grading words?
3. check: outro names the standard HAI outro, not ClaudeTitleOutro?

Rationale: the prompt asks for a PLAN, not a run, per ai-explainer
skill-teardown modifier SELF-DEMO LAW feasibility fallback. Running the
skill requires a guest's real video and a signed REVIEW.md — a third-party
gate that cannot be auto-passed. Each check maps to a specific SKILL.md rule.

## Scene changes inside the isolated toolkit (this run only)

Overlaid on the baseline snapshot recorded in SOURCE-SNAPSHOT.json — the
live public library is not modified.

| File | Change | Why |
|---|---|---|
| `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` | portrait-aware scale (`isPortrait ? min(w/1080, h/1920) : min(w/1920, h/1080)`) | Sibling of `fellows`; without this patch the serif collapses to ≈56 % on 9:16 (memory `feedback_hesitant_writer_portrait_scale`). |
| `runtime/remotion/src/scenes/SkillTeardownAnatomy916.tsx` | new — portrait wrapper | Enables native 9:16 rendering of the anatomy card; shares source with the landscape component and reflows via `useVideoConfig()`. |
| `runtime/remotion/src/scenes/SkillTeardownPipeline916.tsx` | new — portrait wrapper | Same pattern. |
| `runtime/remotion/src/scenes/SkillTeardownMechanism916.tsx` | new — portrait wrapper | Same pattern. |
| `runtime/remotion/src/Root.tsx` | registered the three `*916` compositions in the `SkillTeardown-Generic` folder | A file in `scenes/` is invisible without a `<Composition id="…">` — the scene index is generated from Root.tsx. |
| `runtime/remotion/node_modules` (symlink) | repointed from the read-only public toolkit to a writable copy under `$TMPDIR/nmroot/node_modules` | webpack's persistent cache under `.cache/webpack/` cannot be unlinked when the packages carry `com.apple.provenance` xattr under Apple's App Sandbox. Cache location and package tree are unchanged; only writability changed. Live public `runtime/remotion/node_modules` is untouched. |
| `runtime/remotion/remotion.config.ts` | NOT ADDED (rolled back) | `overrideWebpackConfig` triggers a cache-invalidation `unlink()` that also fails under the sandbox; the symlink rebase is sufficient without any override. |

The three `SkillTeardown*916` wrappers and the `BrutalistHesitantWriter`
portrait patch are the same files the sibling `claude-liam-brutalist-skill-fellows`
episode saved into its `scene-source/` directory (copied verbatim). Their
content is not this run's original work; the credit is preserved in
`SOURCES.md`.

## Chrome-wrapper (render infrastructure, not a scene)

Remotion needs a Chrome binary that can survive Apple's App Sandbox
Mach-port block on child renderers (memory `feedback_chrome_sandbox`). The
render was launched with:

```
ART_CHROME=/tmp/claude-501/rw/chrome-wrap.sh
ART_CHROME_MODE=chrome-for-testing
```

where `chrome-wrap.sh` is:

```bash
#!/usr/bin/env bash
exec "/Users/bear/node_modules/.remotion/chrome-headless-shell/mac-arm64/chrome-headless-shell-mac-arm64/chrome-headless-shell" \
    --single-process --in-process-gpu --disable-crash-reporter "$@"
```

`ART_CHROME`/`ART_CHROME_MODE` are the documented Remotion hooks, not a
sandbox bypass. Same approach used by the sibling episodes.
