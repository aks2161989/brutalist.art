# PROMPTS — Brutalist Command: art help

## The Your Turn prompt (B10, verbatim)

```
From the brutalist.art toolkit root, run each of these and compare:
  ./art
  ./art -h
  ./art --help
  ./art help
  ./art bogus

Save stdout for each to /tmp/art-<alias>.txt, capture $? into the same file, then
diff every pair of the first four. Report: any diff, any non-zero exit for the
first four, and the exit code + stderr line for bogus. Confirm the fifth exits 2
and points at --list.
```

### Expected outcome (also shown on-screen in B10)

- Four identical stdouts across the first four invocations.
- Four exit codes of `0`.
- One exit code of `2` for `bogus`, stderr line points at `--list`.
- If any pair differs, the case pattern at `art:38` (`""|-h|--help|help)`) is broken;
  file a bug against that line and attach the diff.

## Ask (B00) — the framing question

```
What does ./art help actually do — and what does it not do?
```

The reel answers: it does one thing — prints 17 lines pulled from the file's own
header by `sed -n '2,18p' … | sed 's/^# \{0,1\}//'`. It does not list the skills;
`./art --list` does that.

## Cast

- Persona: Liam (in for Bear) — Kokoro `am_onyx`. IN-FOR-BEAR LAW: introduced in
  B00 and signed off in B11 out loud.
- Channel handle: `@HumanitariansAI` for the composer folder chip; `@NikBearBrown`
  for the outro card per `OUTRO-LOCK.md`.

## No paid generation, no uploads

Every prompt runs against a local shell + a local audio model + a local Remotion
project. Nothing here calls an API you pay for and nothing publishes.
