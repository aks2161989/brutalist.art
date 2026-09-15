# The godot-gdd Skill — episode

Two native 4K files ready for Bear's viewing/editing pass. **Not published.**

| Aspect | File | Duration | Dimensions | SHA-256 |
|---|---|---|---|---|
| Landscape 16:9 | [`exports/landscape/claude-liam-brutalist-skill-godot-gdd.mp4`](exports/landscape/claude-liam-brutalist-skill-godot-gdd.mp4) | 214.33 s | 3840 × 2160 | `a847318b49f4743bb53cb15205359a907641446377f63c4219243111afcff68c` |
| Vertical 9:16 | [`exports/vertical/claude-liam-brutalist-skill-godot-gdd-vertical.mp4`](exports/vertical/claude-liam-brutalist-skill-godot-gdd-vertical.mp4) | 214.33 s | 2160 × 3840 | `1783e5968feca78646de4a578acd4958f0b231ecc5dd7579d02fb0a278a23a75` |

Both files share the same 12-beat spine:

- **B00** cold-open Claude composer — `Annyeong, Liam` greeting; `/godot-gdd walker-jumpman/ GDD.md` types; output reveals.
- **B01** BLUF hesitant writer — "generates" corrects to "explains" in view; introduces the mechanism ("source reader").
- **B02** WalkerGodotSetup (flow) — four pipeline panels: Read → Map → Visualize → Assemble.
- **B03** GodotDesignBoard (cards) — SKILL.md excerpt left; four coverage cards highlight sequentially.
- **B04** WalkerGodotSetup (flow) — status label panels: Proposed, Implemented, Observed, Pending.
- **B05** GodotDesignBoard (flow) — causal chain excerpt left; four chain cards flow with ↓ arrows.
- **B06** ClaudeCodeBeat — checker command, VERIFIES block, CANNOT VERIFY block; lines reveal.
- **B07** WalkerGodotSetup (flow) — four walker bookend panels: Composer → Hesitant → Walkthrough → Verdict.
- **B08** GodotDesignBoard (cards) — "A proposal is not a passing test"; three design-tell cards.
- **B09** ClaudeVerdictArtifact — verdict card: five lines on what godot-gdd does and does not do.
- **B10** ClaudeComposerAsk — "Your turn." handoff; prompt types; output reveals gap count.
- **B11** ClaudeTitleOutro — "The godot-gdd Skill." title, @NikBearBrown, mascot; jingle.

## Watch & edit next

1. `exports/landscape/claude-liam-brutalist-skill-godot-gdd.mp4` (4K H.264 + AAC)
2. `exports/vertical/claude-liam-brutalist-skill-godot-gdd-vertical.mp4` (4K portrait H.264 + AAC)
3. QC evidence: `_qc/contact_sheet.png` (24-frame sheet) + `vertical/_qc/contact_sheet.png`.
4. `VISUAL-REVIEW.json` and `vertical/VISUAL-REVIEW.json` record what was reviewed.

## Portrait fix log — defects resolved before delivery

The portrait aspect required six component fixes to pass Gate V (0 BLOCKERs, 0 MAJORs):

1. **GodotDesignBoard.tsx** — `@NikBearBrown` footer was below `safe.b=3648` at `bottom:height*0.04`; patched to `bottom:height*0.045+(portrait?45:0)`.
2. **WalkerGodotSetup.tsx** — four flow panels overflowed shell bottom; patched with `overflow:'hidden'` on the flow content div.
3. **ClaudeCodeBeat.tsx** — added portrait detection + adaptive font so long bash lines don't bleed past portrait card edges.
4. **Root.tsx** — registered `ClaudeCodeBeat916` at 1080×1920 so B06 renders natively rather than center-cropping landscape into portrait.
5. **ClaudeVerdictArtifact916.tsx** — `brandLabel` was not destructured or rendered; added rendering at `bottom:height*0.065` (ink fill 51.4% → 69.4%).
6. **vertical/beat_sheet.json** — B01 `lineSpacing` 2.6 → 3.4; B06 `pattern` → `ClaudeCodeBeat916`.

Full fix details in `vertical/CHECKS-REPORT.md`.

## Playlist adaptation for @HumanitariansAI — one open flag for Bear

Every Claude composer beat (B00, B10) carries the `@HumanitariansAI` folder chip.
The outro card (B11) is the locked `ClaudeTitleOutro` with `@NikBearBrown` hardcoded
per `OUTRO-LOCK.md`. Compile emitted a `SKIN LINT` warning on both aspects — expected
behavior, recorded in `CHECKS-REPORT.md`. If Bear wants the outro to read
`@HumanitariansAI`, that requires an `OUTRO-LOCK.md` policy change, not a per-reel edit.

## What happens next

Bear watches both files, records notes in `FEEDBACK.md`, and either signs off or requests
targeted per-beat rebuilds. Nothing here is published; nothing is uploaded; no external
API was called during this build.

## Artifact tree

```
claude-liam-brutalist-skill-godot-gdd/
├── beat_sheet.json                    landscape source
├── vertical/
│   ├── beat_sheet.json                portrait source (ClaudeCodeBeat916 for B06)
│   ├── VISUAL-REVIEW.json             AI frame review for portrait
│   ├── CHECKS-REPORT.md               portrait checks + fix log
│   ├── TYPECHECK.md                   portrait typography
│   ├── BUILD-PROMPT.md                portrait build invocation record
│   ├── FACTCHECK.md                   portrait factcheck (refs landscape)
│   ├── SHOTLIST.md                    portrait scene-swap table
│   └── media/, _qc/                   portrait renders + QC
├── exports/
│   ├── landscape/                     4K landscape master
│   └── vertical/                      4K portrait master
├── media/, mp3/                       landscape renders + audio
├── _qc/                               landscape QC frames + contact sheet + report
├── BRIEF.md                           supervisor brief
├── SCRIPT.md                          narration script
├── SOURCES.md                         source file list
├── SOURCE-SNAPSHOT.json               source hashes at build time
├── FACTCHECK.md                       landscape claim verification
├── SHOTLIST.md                        landscape beat table
├── PROMPTS.md                         visible prompts documented
├── FEEDBACK.md                        Bear's edit notes (pending)
├── CHECKS-REPORT.md                   landscape checks
├── TYPECHECK.md                       landscape typography
├── VISUAL-REVIEW.json                 AI frame review for landscape
├── BUILD-PROMPT.md                    the build prompt used
└── README.md                          this file
```

## Human review pending

The films have been generated, gate-checked, and inspected frame-by-frame by an AI
reviewer. Bear is the human reviewer. Human sign-off is required before any publication.
