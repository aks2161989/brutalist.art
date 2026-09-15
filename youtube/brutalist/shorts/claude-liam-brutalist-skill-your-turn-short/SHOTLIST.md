# SHOTLIST — The your-turn Skill (Short)

Native 9:16 · 2160×3840 · 24 fps · 131.75s · 8 beats, no endcard.
Every shot is a native portrait Remotion render copied unchanged from the parent's `vertical/media/` slot.

| Beat | Range (s) | Duration | Pattern | Motion | What's on screen |
|------|-----------|----------|---------|--------|------------------|
| B00  | 0.000 – 17.250 | 17.25 | ClaudeComposerAsk916 | type-on | "Hallo, Liam" greeting, composer typing the ask about your-turn, three RESULT lines land: closing-block skill / VERDICT · YOUR TURN · TITLE / idempotent skip-if-absent |
| B01  | 17.250 – 27.458 | 10.21 | BrutalistHesitantWriter916 | type-on | Four-line serif stanza; "whole-reel" flashes terracotta then deletes; final stanza stands: your-turn is / not a / closing-block / skill. |
| B03  | 27.458 – 46.375 | 18.92 | SkillTeardownMechanism916 | reveal | Eyebrow SKILL · BLOCK; heading "Three beats. In order."; enumerated body (VERDICT/YOUR TURN/OUTRO); verbatim SKILL.md quote card; pill "THREE-BEAT BLOCK · IN ORDER" |
| B09  | 46.375 – 66.458 | 20.08 | SkillTeardownMechanism916 | reveal | Eyebrow WORKED EXAMPLE · DRY RUN; heading "One fixture. Zero errors."; body shows dry-run report (changed=1, skipped=0, needs_prompt=0, errors=0); pill "IDEMPOTENT · RE-RUN STACKS NOTHING" |
| B10  | 66.458 – 86.917 | 20.46 | SkillTeardownMechanism916 | reveal | Eyebrow SKILL · LIMITATION; heading "What your-turn does NOT do."; three limits (body out of scope / never publishes / human-triggered re-render); grey pill "DOCUMENTED LIMITATION" |
| B11  | 86.917 – 104.375 | 17.46 | ClaudeVerdictArtifact916 | reveal | Card title "The your-turn Skill"; heading "The your-turn split."; six numbered lines revealed in order |
| B12  | 104.375 – 126.958 | 22.58 | ClaudeComposerAsk916 | type-on | Greeting "Your turn."; paste-ready assignment prompt (3–5 sentence brief, first-person, multi-part ask); three viewer checks in the output block |
| B13  | 126.958 – 131.750 | 4.79 | ClaudeTitleOutro916 | hold | Poster serif "The your-turn Skill" with terracotta period; "@NikBearBrown" handle; seeded mascot glyph |

## Framing verification

24 beat-relative frames extracted at 15/50/85 % of each beat and hashed into `_qc/frames/`; each entry listed in VISUAL-REVIEW.json with its actual SHA-256. Every frame is 2160×3840 and ink stays inside the portrait safe area. Frames confirm:

- No text hits the left/right bleed on any card. The Mechanism916 pattern replaces the horizontal Pipeline strip that would have bled in portrait (feedback memo `skillteardown-pipeline-portrait`).
- BLUF stanza (B01) resolves to the corrected "closing-block" wording well within safe area at 85 % (portrait BLUF recipe: fontSize 145 + lineSpacing 2.7 with a 4-line stanza).
- Verdict card (B11) fills ~84 % of frame width; all six numbered lines visible, no clipping.
- Outro (B13) is the OUTRO-LOCK "ClaudeTitleOutro916" with the hardcoded @NikBearBrown handle — flagged for human reviewer before publication per parent metadata.

## Framing rules honored

- **COLD OPEN LAW** — B00 is `ClaudeComposerAsk916` with a RESULT block; narration introduces Liam in for Bear in its first breath.
- **EXECUTIVE-SUMMARY LAW** — B01 is `BrutalistHesitantWriter916`, correcting the reel's actual misconception, 10.21s measured (≥9s minimum for parent applies; Short simply inherits the parent beat unchanged).
- **ILLUSTRATE LAW** — the retained middle beats each illustrate a distinct move (three-beat block, worked-example report, limitation card, verdict split, viewer prompt).
- **HANDOFF LAW** — B12 is `ClaudeComposerAsk916` with greeting `Your turn.` and a real paste-ready planning prompt Liam reads aloud.
- **OUTRO LAW / OUTRO-LOCK** — B13 is `ClaudeTitleOutro916` with the reel's title restated (terracotta period), hardcoded `@NikBearBrown` handle, slug-seeded mascot; no subline per lock.

## What's NOT in the Short

Six beats from the long-form teardown are dropped for length; each drop is justified in CUT-PLAN.json:

- **B02** SkillTeardownAnatomy916 (folder tree)
- **B04** MECHANISM 1 · persona-aware handoff
- **B05** MECHANISM 2 · drafts.json human gate
- **B06** MECHANISM 3 · verdict-card fixes
- **B07** MECHANISM 4 · Liam reads the whole prompt
- **B08** MECHANISM 5 · outro re-reads the title

None of the dropped beats introduces a claim that a kept beat depends on. B11's six-line verdict summarizes the persona-aware handoff and drafts.json gate in one card each.
