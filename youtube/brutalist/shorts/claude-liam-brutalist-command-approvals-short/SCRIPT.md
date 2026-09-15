# SCRIPT — Brutalist Command: art approvals — Short (9:16)

Full narration read by Liam (Kokoro `am_onyx`), in for Bear, for `@HumanitariansAI`. Reused verbatim from the parent vertical build; no rewrites, no audio regenerated in the Short. Kept beats only.

## B00 — ASK (0:00.00 → 0:09.83)

> Selam, this is Liam, in for Bear. The ask — before I sign anything on a fellows reel, show me exactly what I would be signing. Do not sign it for me. Just print the fingerprints.

## B01 — BLUF (0:09.83 → 0:21.75)

> Watch the writer walk this back. Art approvals does not sign approvals. It inspects the subjects a human is about to sign. Two verbs. Fingerprints prints. Default validates. The pen never leaves the human's hand.

## B03 — Framework · two verbs (0:21.75 → 0:40.71)

> Two surfaces. Point it at a reel folder. Add dash dash fingerprints, and it prints the subjects a human would need to sign — nothing else. Leave the flag off, and it validates the pasted approvals against those subjects. Either way, the file changes zero. Approvals live in metadata dot approvals in the beat sheet, written by a human editor. The command is the auditor.

## B05 — Worked example · fellows fingerprints (0:40.71 → 0:58.33)

> Now a fellows reel. Profile fellows, voice policy persistent, and a feedback beat marked professor notes. Two gates arm: voice, and professor notes. Dash dash fingerprints prints two subject blocks, each with a SHA-256. Those are the exact strings a human review record has to match. That is the paperwork.

## B06 — Mechanism · five-field record (0:58.33 → 1:18.79)

> Under the hood, an approval record is five fields. Status equals approved. Reviewer type equals human — never AI. Reviewed by, a non-empty string. Reviewed at, a full ISO timestamp with a timezone. And every subject SHA reprinted verbatim from dash dash fingerprints. Miss one, mistype one, forget the timezone — the gate refuses. The refusal is the feature.

*Visual updated 2026-09-12: card now shows NOTES.md extra gate check; sparkLine "Five fields. Human, dated, verbatim — and NOTES.md non-empty."*

## B08 — Failure · stale approval (1:18.79 → 1:41.88)

> One failure worth showing. A fellows reel, both approvals pasted, both gates green. Then B05 narration gets one extra sentence added — after the human signed. Re-run. The command refuses: gate professor notes, missing pending or stale. Dash dash fingerprints prints the new SHA. The recovery is the same short loop: hand the new subjects to the human, get a fresh dated record, paste it in. The pen still does not leave their hand.

## B09 — Verdict (1:41.88 → 2:01.29)

> So — art approvals. A five-field auditor. Two verbs, neither one signs. It reads the beat sheet, decides which gates are armed, computes the subjects live, and either prints them or checks a pasted record against them. It refuses on missing, wrong, or stale. And the refusal is the whole reason the command exists — a fellows reel with a pending signature never ships.

*Visual updated 2026-09-12: Verdict line 3 now reads "professor_notes arms on requires_approval, a feedback act, or B05/B06 in a fellows reel."*

## B11 — Outro (2:01.29 → 2:06.75)

> Brutalist Command: art approvals. Liam, in for Bear, for at Humanitarians A I.

## Not in this Short (in the 16:9 long)

- **B02** dispatcher case-lines at `art:87-89`
- **B04** worked example on a plain command reel (no gate armed → `{}` and exit 0)
- **B07** `approval_subjects()` internal digest mechanics — the deterministic `digest()` implementation, recomputed subjects every run
- **B10** Your Turn composer with the full paste-into-Claude-Code exercise
