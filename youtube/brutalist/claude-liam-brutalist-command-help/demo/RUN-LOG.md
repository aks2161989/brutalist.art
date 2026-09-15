# Demo captures — art help / -h / --help / (empty)

Recorded: 2026-09-09T05:33:48Z
Toolkit: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/.repoloop/workspaces/claude-liam-brutalist-command-help/toolkit

## ./art help
```
art — one entry point for the brutalist toolkit (the pared-down brutalist-art).

  ./art --list                 list the skills
  ./art <skill> --help         show a skill's SKILL.md
  ./art scenes "<beat need>"   LIBRARY-FIRST scene search — run BEFORE authoring a beat
  ./art scenes --check <Name>  is that composition renderable? (the anti-slate check)
  ./art scene-index            regenerate scenes.json + SCENE-DOC-TODO.md after adding one
  ./art icons "<what it needs>" CANONICAL icon search — run BEFORE drawing a mark
  ./art icons --check <name>   is that icon in the set? (the anti-redraw check)
  ./art icon-build             re-cut the canonical set from svg/ (rarely needed)
  ./art todo  <reel> [flags]   per-video beat ledger (which beats need filling, how)
  ./art run   <reel> [flags]   compile a review cut
  ./art shorts <reel> [flags]  derive the 9:16 Short (cap check + auto-shorten)
  ./art vertical <reel>       full-length 9:16 companion (no shortening)
  ./art approvals <reel> --fingerprints  inspect human-review subjects (never signs)
  ./art final <reel>           verified master — no review label (→ <slug>.mp4)
  ./art doctor                 dependency readiness (wraps ./setup)
```

## ./art
```
art — one entry point for the brutalist toolkit (the pared-down brutalist-art).

  ./art --list                 list the skills
  ./art <skill> --help         show a skill's SKILL.md
  ./art scenes "<beat need>"   LIBRARY-FIRST scene search — run BEFORE authoring a beat
  ./art scenes --check <Name>  is that composition renderable? (the anti-slate check)
  ./art scene-index            regenerate scenes.json + SCENE-DOC-TODO.md after adding one
  ./art icons "<what it needs>" CANONICAL icon search — run BEFORE drawing a mark
  ./art icons --check <name>   is that icon in the set? (the anti-redraw check)
  ./art icon-build             re-cut the canonical set from svg/ (rarely needed)
  ./art todo  <reel> [flags]   per-video beat ledger (which beats need filling, how)
  ./art run   <reel> [flags]   compile a review cut
  ./art shorts <reel> [flags]  derive the 9:16 Short (cap check + auto-shorten)
  ./art vertical <reel>       full-length 9:16 companion (no shortening)
  ./art approvals <reel> --fingerprints  inspect human-review subjects (never signs)
  ./art final <reel>           verified master — no review label (→ <slug>.mp4)
  ./art doctor                 dependency readiness (wraps ./setup)
```

## ./art -h
```
art — one entry point for the brutalist toolkit (the pared-down brutalist-art).

  ./art --list                 list the skills
  ./art <skill> --help         show a skill's SKILL.md
  ./art scenes "<beat need>"   LIBRARY-FIRST scene search — run BEFORE authoring a beat
  ./art scenes --check <Name>  is that composition renderable? (the anti-slate check)
  ./art scene-index            regenerate scenes.json + SCENE-DOC-TODO.md after adding one
  ./art icons "<what it needs>" CANONICAL icon search — run BEFORE drawing a mark
  ./art icons --check <name>   is that icon in the set? (the anti-redraw check)
  ./art icon-build             re-cut the canonical set from svg/ (rarely needed)
  ./art todo  <reel> [flags]   per-video beat ledger (which beats need filling, how)
  ./art run   <reel> [flags]   compile a review cut
  ./art shorts <reel> [flags]  derive the 9:16 Short (cap check + auto-shorten)
  ./art vertical <reel>       full-length 9:16 companion (no shortening)
  ./art approvals <reel> --fingerprints  inspect human-review subjects (never signs)
  ./art final <reel>           verified master — no review label (→ <slug>.mp4)
  ./art doctor                 dependency readiness (wraps ./setup)
```

## ./art --help
```
art — one entry point for the brutalist toolkit (the pared-down brutalist-art).

  ./art --list                 list the skills
  ./art <skill> --help         show a skill's SKILL.md
  ./art scenes "<beat need>"   LIBRARY-FIRST scene search — run BEFORE authoring a beat
  ./art scenes --check <Name>  is that composition renderable? (the anti-slate check)
  ./art scene-index            regenerate scenes.json + SCENE-DOC-TODO.md after adding one
  ./art icons "<what it needs>" CANONICAL icon search — run BEFORE drawing a mark
  ./art icons --check <name>   is that icon in the set? (the anti-redraw check)
  ./art icon-build             re-cut the canonical set from svg/ (rarely needed)
  ./art todo  <reel> [flags]   per-video beat ledger (which beats need filling, how)
  ./art run   <reel> [flags]   compile a review cut
  ./art shorts <reel> [flags]  derive the 9:16 Short (cap check + auto-shorten)
  ./art vertical <reel>       full-length 9:16 companion (no shortening)
  ./art approvals <reel> --fingerprints  inspect human-review subjects (never signs)
  ./art final <reel>           verified master — no review label (→ <slug>.mp4)
  ./art doctor                 dependency readiness (wraps ./setup)
```

## Failure: ./art bogus
```
art: unknown skill 'bogus' (try ./art --list)
$? = 2
```

## Recovery: ./art --list
```
SKILL                  ROLE
ai-explainer           builder — Claude-branded explainer reel (the tight cut)
cli-explainer          builder — prompt → code → moving output (the build reel)
deep-explainer         builder — 5-10 min documentary episode (vox pantry beats)
anthropics             builder — reads Anthropic artifacts against their own claims; practitioner-report register
fashionista            builder — AI fashion-call experiment; sports-announcer call + correction ask; Kokoro am_onyx
fellows                builder — wraps a HAI fellow's video report in Claude bookends for @HumanitariansAI
finance                builder — templatized SEC EDGAR filings reel; 11 beats, 5 charts, fully deterministic
guests                 builder — wraps a board-member or invited-speaker video in Claude bookends for @HumanitariansAI
nbb                    persona — Teardown register, Liam in for Bear (Kokoro am_onyx)
hai                    persona — Plain register (simple, direct), Kokoro Bella (af_bella)
explainer              doctrine — parent chassis the builders inherit (not an entry point)
your-turn              doctrine — the closing three-beat standard
logo                   builder — brand sting outro; random-once animation + brand SVG + jingle (the mp3 is the clock)
duration-planner       doctrine — duration is an output, never a target
nopunt                 doctrine — maps animatable beat-types to Brutalist primitives; consult before placing any placeholder
screen-clean           doctrine — prepares screen recordings (Zoom/Teams/Meet) for use as a reel beat
```

## Byte / line counts
```
help lines:  17
help bytes:  1225
help exits:  0
bogus exits: 2
```
