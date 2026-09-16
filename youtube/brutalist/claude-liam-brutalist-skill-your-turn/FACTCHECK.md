# FACTCHECK.md — The your-turn Skill (ep 21)

Every load-bearing claim in this reel points back to `skills/make/your-turn/SKILL.md`
(current sha256 `aecd503a11c413c2b7e123f5b3c0d80832a1e5d071ea523b243b5c130f514865`;
episode.source_sha256 `8250e8ccd8779eb2629de62b05699c311dc1e5a4caeb70f1a1260e9a8d10f126`;
re-verified 2026-09-12 under run_id `1ddecabfca38480996c56171bce09bb7`) or
its script `skills/make/your-turn/scripts/apply_your_turn.py`. Quotes on Mechanism / Anatomy
cards are verbatim from the SKILL.md.

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
