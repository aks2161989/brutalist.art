# Ep 21 · The your-turn Skill

Skill teardown of `skills/make/your-turn/SKILL.md` — the closing-block skill
that standardizes the last three Liam-narrated beats of every claude-explainer
reel (VERDICT → YOUR TURN → OUTRO), fixes the small verdict card and the
double-numbered recap lines, and inserts a video-relevant paste-ready prompt
the viewer can run.

Playlist: **Brutalist** · Channel adaptation: `@HumanitariansAI` (composer
folder chip) with the OUTRO-LOCK-hardcoded `@NikBearBrown` on B13. Narrator:
**Liam, in for Bear** (Kokoro `am_onyx`, free). No captions. No API spend.

Re-verified 2026-09-12 under run_id `1ddecabfca38480996c56171bce09bb7`. Source
SKILL.md sha changed since previous build; all verbatim quotes verified accurate
to the current file; no beat changes required; renders preserved.

## Files ready for Bear's review

- **Landscape 16:9** — `exports/landscape/claude-liam-brutalist-skill-your-turn.mp4`
  - 3840×2160 · 250.958s · Gate V clean (BLOCKER=0 MAJOR=0)
  - SHA-256 `fc379bdaceb83f1c4e17ae9ae692407421ad79d37c43cc96bc571ea0e81f3660`
- **Vertical 9:16** — `exports/vertical/claude-liam-brutalist-skill-your-turn-vertical.mp4`
  - 2160×3840 (native 4K portrait) · 250.958s · Gate V clean
  - SHA-256 `bdeb47c89ce4ecf05cf70313aedee7f0e65a4c14a3f793aaaa2bf8362ee12d5a`

Bear's viewing / editing is next. Nothing has been uploaded, published, or
committed to git by this build.

## What the reel argues (14 beats)

1. Cold open (composer, `Hallo, Liam`) — Liam-in-for-Bear introduces the skill.
2. BLUF (hesitant writer) — corrects "a whole-reel" to "a closing-block".
3. Anatomy — one SKILL.md + one `apply_your_turn.py` script.
4. The three-beat block, in fixed order.
5-9. Five mechanism decisions — the persona-aware handoff line; drafts.json
   as the human gate; the enlarged verdict card + strip-leading-numbers fix;
   Liam reads the whole YOUR TURN prompt (command == narration_text); the
   outro re-reads the title (narration_text = title, idempotent).
10. **Worked example** — actual dry-run of `apply_your_turn.py` on a synthetic
    fixture in `demo/`. Report: changed=1, needs_prompt=0, errors=0.
11. Documented limitation — no body edits, no publish, human-triggered re-render.
12. Verdict artifact (six lines).
13. YOUR TURN composer (paste-ready planning prompt).
14. Outro title restate ("The your-turn Skill.").

## Paperwork

- Both aspects: `FACTCHECK.md`, `SOURCES.md`, `SHOTLIST.md`, `PROMPTS.md`,
  `CHECKS-REPORT.md`, `TYPECHECK.md`, `BUILD-PROMPT.md`, `VISUAL-REVIEW.json`
  in the aspect's root (landscape) or `vertical/` (portrait).
- `SCRIPT.md` — full narration for reference.
- `demo/` — synthetic fixture and reports proving the transformer works and
  is idempotent (byte-identical output on second apply).
- `scene-source/` + `scene-source-manifest.json` — the reel-local Root.tsx
  overlay that adds the 916 portrait variants of SkillTeardown* and applies
  the BrutalistHesitantWriter portrait-scale patch.

## Known advisories (not blockers)

- Motion histogram: 71% `reveal` (10 of 14 mechanism-card beats). Expected
  for a SkillTeardown episode where every mechanism beat uses the same
  `SkillTeardownMechanism` reveal pattern.
- Vertical skin_lint: B00 and B13 use `ClaudeComposerAsk916` /
  `ClaudeTitleOutro916`. These are the native portrait variants of the same
  scenes; the lint expects the landscape names. Same warning shipped with
  ep20 (sri-explainer) vertical; documented and expected.
- Missing legacy `type_check.py` — substituted with actual visual PNG
  inspection via the image-capable Read tool. See `TYPECHECK.md`.

## Toolkit fingerprint

Isolated toolkit baseline SHA-256 (per SOURCE-SNAPSHOT.json):
`92432609980c8ffc03bc1f00a1300fe1ac78bd7363b5b8ba9f2d389407d72b9d`.
