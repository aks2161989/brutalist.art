# SCRIPT — Brutalist Command: art keys — Short

Six-beat cut, 99.6 s. Every line is the parent's narration for the retained
beat, unchanged. No lines were re-written, spliced or shortened. Voice:
Kokoro `am_onyx` (Liam, in for Bear).

## B00 · ASK (11.6 s)

> Habari, this is Liam, in for Bear. The ask — before I fill a single beat
> sheet, tell me which optional keys this box has, and whether the toolkit
> actually needs any of them. Just probe. Do not spend anything.

## B01 · BLUF (14.1 s)

> Watch the writer walk this back. The toolkit is free by default. Art keys
> does not block a render — nothing does. It audits one optional upgrade,
> and it audits it live. A red row here means Higgsfield is not logged in.
> It never means you cannot render.

## B04 · WORKED_EXAMPLE — the "invalid" run (18.4 s)

> Here is this box today. Higgsfield is installed. There is no active login
> and the network is unreachable. The command fires the probe. Return code
> non-zero, so the row lands as invalid — with the literal fix line 'run
> higgsfield auth login.' And then, quietly, the script exits zero. Watch
> that gap. The red row is diagnostic, not a gate.

## B08 · FAILURE_RECOVERY — the design tell (32.0 s)

> One design tell worth calling out. The docstring says exit zero if every
> present key is valid, one if any is invalid. Read the code. The variable
> any underscore invalid is declared false on line forty and never
> reassigned. So the invalid branch does not actually flip the exit code.
> And the art help line advertises an 'SI key' check — grep the script for
> SI, and you get zero hits. So the surface promises two things the code
> does not enforce. Both are harmless today — nothing in the pipeline gates
> on this exit — but if you ever need to fail a CI job on a red row, you
> now know exactly which line to patch.

## B09 · VERDICT (18.1 s)

> So — art keys. A live probe of one optional CLI, wrapped in a two-line
> dispatcher case, that prints a colored table and always exits zero. The
> toolkit needs no keys. This command exists so a red row is visible before
> you go looking for it. Run it once when you clone the repo, and run it
> again the day you install Higgsfield. In between, ignore it.

## B11 · OUTRO (5.4 s)

> Brutalist Command: art keys. Liam, in for Bear, for at Humanitarians A I.

## Note on the transitions

B01 → B04: BLUF ("audits upgrades, not blocks renders") → concrete
demonstration of a red row co-existing with `[exit 0]`.
B04 → B08: "watch that gap" → the mechanism behind why the gap exists
(the exit-code drift on `any_invalid`).
B08 → B09: two drifts → whole-surface recap that names them again
("the docstring's exit-1-on-invalid contract is not enforced").
B09 → B11: verdict → title/handle sign-off.
