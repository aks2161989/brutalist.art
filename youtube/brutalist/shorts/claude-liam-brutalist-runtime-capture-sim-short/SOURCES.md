# SOURCES — Brutalist Utility: capture_sim.py (Short)

The Short is a derivative cut of the vertical parent; no new external sources were introduced.

## Primary source under teardown

- `runtime/scripts/capture_sim.py` — 662 lines, SHA-256 `ccb75479c75081bede9d63d0d4913075b3497db183a035b5e0648d5dcb5d4a34`.
  - Public URL: <https://github.com/nikbearbrown/brutalist.art/blob/main/runtime/scripts/capture_sim.py>
  - Referenced in beats: B01 (behavior overview), B02 (pipeline), B07 (docstring rule), B08 (except block), B09 (whole surface).

## Concrete example fixtures (quoted in B07)

- `demo/sim-source/00-tiny-wave.html` — tiny D3 v7 sine-wave fixture with `input#k[type=range] min=1 max=6 step=0.1`.
- `demo/scripts/tiny-wave-sweep.json` — 5-step script that opens with `{"set":"#k","value":1}` (never with `wait`).
- Both files live in the parent reel; the Short reads them from the parent unchanged.

## Observed evidence (quoted in B08)

- `demo/failure-sandbox.txt` — verbatim capture of `capture_sim.py` failing inside the Claude Code Apple App Sandbox. FATAL Mach-port bootstrap denial from `base/apple/mach_port_rendezvous_mac.cc:159`; exit code 1; no mp4 written. Reproducible on this workstation.

## Parent reel provenance

- Parent reel path: `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/youtube/brutalist/claude-liam-brutalist-runtime-capture-sim`
- Parent vertical master: `exports/vertical/claude-liam-brutalist-runtime-capture-sim-vertical.mp4`
- Parent master SHA-256: `fedfb0ca5e06ee130b855af4fc688bae02293fe05182660c39946f5079d686ab`
- Parent beat sheet: `vertical/beat_sheet.json`
- This invocation's `episode.source_sha256`: `9fa7a3d82e96f9deff301f026e0c84701a6fba04c7d7a58c7bbac59bd16751df`
- This invocation's `run_id`: `3ad75bda3d804b798a7d10d87c431d44`

## Reused native portrait media (unchanged copies)

| Beat | Video (SHA-256) | Audio (SHA-256) |
|------|-----------------|-----------------|
| B00 | 28ee2b687290a91b679ac189d5696c1e2e4a0d54ca248b99c5d0e8daeb015434 | 4c8f37b44846518b55bbf0141a7af7eaa3075c01c06b698c87414c64762896eb |
| B01 | 5c4c6fc53562295243fc1f9e79ab3a900ef13a9bf03f1bcf7c2888c15a05497b | 6d66d77d6881514ce2875441ee39656665bd7ebc8331b709c202afc87c80b034 |
| B02 | a71b079d2cc026ae3c771f79f3d7c3278bd1d2be6c6e8b1de2f2101ed68d65cc | ef78b9df85f04ab4f0c177dfe787b2867ba5b4d71b33ded3daccc40a0cb6a441 |
| B07 | 4023ec5f6a221a2d03d864caa6e0b5be3f952153dd4e066c4ee97f4e0e69e8e5 | 9c6b274df18abd0cc8930fe2b9f0fb3660d7dcd303ad69061d3216571fb16a24 |
| B08 | 4f4d25ab91a554391b035d03876bd30b4d6e650dcd03a2406a126e011733e847 | 4073ae368d991d4ced4438d965d36b89192d36f0a3d743212a3ee1a3e378af59 |
| B09 | f33eb3484fa9b82fc21608f6f440ccb8feb3cc0af02a993d18f500184a466623 | 0f0fd834f8f90e5eb98300d1290e48a21220f7cb4c8cb602e36cc425997bd83a |
| B11 | 5b96e0f62b0067ff5bd921640f9dc1743223bc682771edb50a43036f5b56e151 | 7e8d1d800dae369d1539aa4cbb6e7ed05aefe52abaead55f0f14f68472b76ed7 |

## Read-only example beat sheets (shape leads only)

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — SHA-256 `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`.
- `sanjana-rao/08-24-2026-playlist-architecture-as-product-strategy/playlist-architecture-short/beat_sheet.json` — SHA-256 `787621776bcd8810d8719a61f577f3589707bbf59151655fcbbdd10555b318a0`.

Neither example contributed narration, captured media, or approvals to this Short.
