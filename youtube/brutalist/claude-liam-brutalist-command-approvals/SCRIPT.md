# SCRIPT — Brutalist Command: art approvals

Register: Teardown. Voice: Liam (in for Bear), Kokoro `am_onyx`.
Channel: @HumanitariansAI (folder chip) — outro is OUTRO-LOCK @NikBearBrown, flagged.

---

## B00 — COLD OPEN · ASK

**Selam, this is Liam, in for Bear. The ask — before I sign anything on a fellows reel, show me exactly what I would be signing. Do not sign it for me. Just print the fingerprints.**

Composer scene, Claude UI. `command` is the ask itself.
Output lines land under the composer: the three things `art approvals` is *not*.

## B01 — BLUF · executive summary

**Watch the writer walk this back. Art approvals does not sign approvals. It inspects the subjects a human is about to sign. Two verbs. Fingerprints prints. Default validates. The pen never leaves the human's hand.**

Hesitant-writer types the misconception and corrects it:
`art approvals / signs approvals.`
`signs` → `inspects`, `approvals` → `subjects`.

Beat window ≥ 9s (EXECUTIVE-SUMMARY LAW; `lead_silence_s: 0.8`).

## B02 — FRAMEWORK · the dispatcher

**The dispatcher is one case in the art file. Three lines: pattern approvals, exec Python on runtime slash scripts slash build underscore safety dot py, forward every argument. No aliases; the dispatcher matches only the exact string approvals. Every rule the command enforces lives in that one Python file.**

`ClaudeCodeBeat` — art:87-89 code fragment, spark line "One case. No aliases. Two verbs."

## B03 — FRAMEWORK 2 · the two verbs

**Two surfaces. Point it at a reel folder. Add dash dash fingerprints, and it prints the subjects a human would need to sign — nothing else. Leave the flag off, and it validates the pasted approvals against those subjects. Either way, the file changes zero. Approvals live in metadata dot approvals in the beat sheet, written by a human editor. The command is the auditor.**

`ClaudeCodeBeat` — the flag table + `metadata.approvals` schema. Spark: "Two verbs. Neither one signs."

## B04 — WORKED EXAMPLE 1 · a plain command reel

**Here is a plain command reel. Not a fellows reel. No feedback beat. Nothing to sign. Dash dash fingerprints prints an empty object. The default returns silent, exit zero. When no gate is armed, the command does the honest thing — nothing.**

`ClaudeCodeBeat` — verbatim from demo/RUN-LOG.txt (section 2). Spark: "No gate armed. Nothing to sign. Silent pass."

## B05 — WORKED EXAMPLE 2 · a fellows reel with both gates

**Now a fellows reel. Profile fellows, voice policy persistent, and a feedback beat marked professor notes. Two gates arm: voice, and professor notes. Dash dash fingerprints prints two subject blocks, each with a SHA-256. Those are the exact strings a human review record has to match. That is the paperwork.**

`ClaudeCodeBeat` — verbatim from demo/RUN-LOG.txt (section 3, --fingerprints). Spark: "Two gates armed. Two subjects. Two SHAs."

## B06 — MECHANISM · what an approval record must contain

**Under the hood, an approval record is five fields. Status equals approved. Reviewer type equals human — never AI. Reviewed by, a non-empty string. Reviewed at, a full ISO timestamp with a timezone. And every subject SHA reprinted verbatim from dash dash fingerprints. Miss one, mistype one, forget the timezone — the gate refuses. The refusal is the feature.**

`ClaudeCodeBeat` — the schema pattern + a legal record example, plus the four ways to fail. Spark: "Five fields. Human, dated, verbatim."

## B07 — MECHANISM 2 · fingerprints from the source, not the record

**And here is the subtle part. The command re-computes those SHAs from the beat sheet every run. It never trusts the ones already pasted. If the narration in the reviewed beat changed by one word after the human signed, the recomputed SHA does not match the pasted one — and the gate refuses. Human review does not stick to a beat sheet, it sticks to a beat sheet as it was on the day the human read it.**

`ClaudeCodeBeat` — the `digest()` + `file_digest()` calls from build_safety.py. Spark: "Fingerprints from the source. Every run."

## B08 — FAILURE + RECOVERY · a stale approval

**One failure worth showing. A fellows reel, both approvals pasted, both gates green. Then B05 narration gets one extra sentence added — after the human signed. Re-run. The command refuses: gate professor notes, missing pending or stale. Dash dash fingerprints prints the new SHA. The recovery is the same short loop: hand the new subjects to the human, get a fresh dated record, paste it in. The pen still does not leave their hand.**

`ClaudeCodeBeat` — the recovery flow verbatim from demo/RUN-LOG.txt (sections 4 & 5). Spark: "One word changed. Approval stale. Human decides."

## B09 — VERDICT

**So — art approvals. A five-field auditor. Two verbs, neither one signs. It reads the beat sheet, decides which gates are armed, computes the subjects live, and either prints them or checks a pasted record against them. It refuses on missing, wrong, or stale. And the refusal is the whole reason the command exists — a fellows reel with a pending signature never ships.**

`ClaudeVerdictArtifact` with title "Brutalist Command: art approvals" and 6 artifact lines.

## B10 — HANDOFF · YOUR TURN

**Your turn. Paste this into Claude Code, pointed at any fellows reel you have on disk: run art approvals with dash dash fingerprints, copy the JSON into metadata dot approvals as human review records with today's date, then re-run art approvals with no flag and confirm the exit code is zero. Look for whether Claude leaves the reviewed by field empty — that is the one field an agent must never fill in. It is the human's signature.**

`ClaudeComposerAsk` with `greeting: "Your Turn"`, three grading lines under the composer.

## B11 — OUTRO

**Brutalist Command: art approvals. Liam, in for Bear, for at Humanitarians A I.**

`ClaudeTitleOutro` (OUTRO-LOCK: hardcoded @NikBearBrown handle — flagged for human reviewer per prior playlist episodes' pattern).
