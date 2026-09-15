# FACTCHECK.md — The your-turn Skill (Short)

Derived from the parent's FACTCHECK. The Short retains 8 of the parent's 14 beats
(B00, B01, B03, B09, B10, B11, B12, B13). Every load-bearing claim in the retained
narration still points back to `skills/make/your-turn/SKILL.md`
(episode.source_sha256 `a78e89d72b9770dca820ea922194e86e39c251b8acab17028921cd8edf5d0193`) or
its script `skills/make/your-turn/scripts/apply_your_turn.py`. Quotes on the Mechanism
card (B03) are verbatim from the SKILL.md.

## Short-specific note

The Short does NOT show these long-form details as their own beats:

- 0.5s lead pause and the persona-aware handoff branch (long: B04)
- The drafts.json file format and human-gate walkthrough (long: B05)
- The 860px→84% verdict-card width fix and the `stripLeadNum` component
  defence (long: B06)
- The `props.command == narration_text` invariant (long: B07)
- The `metadata.title → narration_text` copy step for the outro (long: B08)
- The full SKILL.md + apply_your_turn.py folder tree (long: B02)

The Short still makes the following summary claims about them, all
truthfully supported by the SKILL and script:

- B03 asserts "Liam reads the whole thing aloud" (long: B07 evidence)
  and "Liam re-reads the reel's own title" (long: B08 evidence).
- B11 (verdict) enumerates "handoff is PERSONA-AWARE — prior Bear → 'Thanks
  Bear'; prior Liam → 'Let's recap'" (long: B04 evidence) and "drafts.json
  is the HUMAN GATE — one prompt per slug, reviewed before any spend" (long:
  B05 evidence) and "Verdict card FIXED once — 84% width, leading numbers
  stripped defensively" (long: B06 evidence).

Nothing in the retained cut references numbered decisions ("First decision",
"Second decision", …) — the scaffolding those beats belonged to was
completely removed.

## Load-bearing claims and their evidence

| Claim (on screen / in narration) | Evidence |
|---|---|
| "your-turn is a closing-block skill; last three beats only" | SKILL.md ¶2: "It is a CLOSING-BLOCK skill, not a whole-reel skill — it edits the last three beats of an existing `beat_sheet.json`." |
| "VERDICT → YOUR TURN → OUTRO order" | SKILL.md § "The block (in order)" |
| "handoff: prior body was Bear → 'Thanks Bear, let's recap with Claude.'; prior was Liam → 'Let's recap with Claude.'" | SKILL.md § "Voices (inherited)" line 55, and `apply_your_turn.py` L31-32, L92-95 |
| "0.5s lead pause" | SKILL.md § "The block (in order)" step 1, and `apply_your_turn.py` L33 (`LEAD_SILENCE_S = 0.5`) |
| "drafts.json is the human gate" | SKILL.md § "Auto-drafting the YOUR TURN prompt" — "This is the one non-deterministic step and the one human gate — review `drafts.json` before applying." |
| "prompt drafted per slug, 3-5 sentences, first person, ending in multi-part ask" | SKILL.md § "Auto-drafting the YOUR TURN prompt" |
| "verdict card was hard-pinned to 860px on a 1920 frame; now fills ~84% width" | SKILL.md § "Fixes folded in" — "was hard-pinned to 860px on a 1920 frame. Now fills ~84% width with legible type." |
| "~160 recap lines across catalog had authored '1.' / '2.' collisions; transformer strips leading numbers, component strips defensively" | SKILL.md § "Fixes folded in" — literal wording |
| "Liam reads the WHOLE prompt aloud; props.command == narration_text" | SKILL.md § "The block (in order)" step 2 |
| "OUTRO narration = title, props.title = title, handle = @NikBearBrown" | SKILL.md § "The block (in order)" step 3; `apply_your_turn.py` L194-200 |
| "idempotent — re-run stacks nothing" | SKILL.md § "Rules" ¶ after Commands: "The transformer is idempotent — re-running never stacks handoffs or re-numbers." |
| "sheets without a verdict card / other families are skipped untouched" | Same paragraph. |
| "only edits closing three beats; body out of scope" | SKILL.md § "Rules" rule 4 |
| "never publishes; re-render + re-upload is a separate human-triggered step" | SKILL.md § "Rules" rule 3 |
| "reach elsewhere if the sheet has no your-turn or Liam outro — this skill skips it" | `apply_your_turn.py` L144-145: `if yt is None and outro is None: return False, ["skip: no claude-explainer closing (no your-turn / liam outro)"]` |
| "phase gate: review drafts.json BEFORE any audio spend or render" | SKILL.md § "Rules" rule 2 |
| "demo/ dry-run report: changed=1, skipped=0, needs_prompt=0, errors=0" | `demo/demo-report.json` (dry-run) and `demo/demo-applied-report.json` — captured live. |

## Independent verification (this session, 2026-09-09)

Ran `apply_your_turn.py` twice against a synthetic fixture in `demo/`:

1. **Dry-run**: reported `changed=1 inserted_verdict=0 skipped=0 needs_prompt=0 errors=0 (dry-run)`. Notes for the fixture:
   - `verdict: stripped authored line numbers`
   - `verdict: cleaned + handoff (from Bear)`
   - `your-turn: set relevant prompt + narration`
   - `outro: Liam re-reads title`
2. **Full apply, then re-run** — the fixture's md5 was byte-identical after the
   second apply (`78c9dbf88a8bb124431f1f938e6afd46`), confirming the SKILL's
   idempotency claim.
3. **Diff (see `demo/diff.txt`)** — matches the mechanism claims: the "1." /
   "2." / "3." prefixes on verdict lines were stripped; "Thanks Bear, let's
   recap with Claude." was prepended to the verdict narration because the
   prior beat's `engine` was `elevenlabs`; `lead_silence_s: 0.5` was added;
   `narration_text` and `props.command` in the YOUR TURN beat were both
   replaced by the `drafts.json` prompt (identical strings); `narration_text`
   and `props.title` in the OUTRO beat were both set to `metadata.title`,
   with `props.handle = "@NikBearBrown"`.

## Corrections applied

- **B01 (BLUF) audio-first check** — initial narration produced 8.68s of audio
  (below the 9s BLUF floor per EXECUTIVE-SUMMARY LAW / TIMING). Rewrote the
  BLUF to `"...standardized."` → `"...standardized."` with the framing beat
  extended; new audio 10.20s ≥ 9s. Verified against the shipped rule text.

## Known limitations documented on screen

B10 explicitly lists the three things your-turn does NOT do (body edits,
publish, human re-render). Nothing in the reel implies it batch-re-renders or
uploads.

## Corrections NOT NEEDED

- The SKILL.md still describes `BEAR = elevenlabs` in the script docstring
  (L26). This playlist enforces Kokoro am_onyx for every voice, so we do NOT
  invoke ElevenLabs in the demo — we test the transformer's persona branch
  by declaring `engine: "elevenlabs"` on synthetic body beats. The fixture
  never generates audio; only the branch is exercised.
