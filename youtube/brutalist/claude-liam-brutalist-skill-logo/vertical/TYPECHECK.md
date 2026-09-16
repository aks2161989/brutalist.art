# TYPECHECK — The logo Skill (portrait)

## Legacy `scripts/type_check.py` — MISSING

Same gap as the landscape TYPECHECK.md — the legacy `type_check.py` is not
shipped in this toolkit copy. This TYPECHECK is a visual-review substitute.

## Substitute — visual typography review (portrait)

Every beat's frames at 50/85% were extracted (`vertical/_qc/samples/`) and Read
as images. Portrait-specific typography checks:

### Portrait-native sizing decisions

- `SkillTeardown*916.tsx` wrappers use portrait-tuned type ramps:
  - Anatomy title: 72px serif; body: 32px mono; callout: 32px sans (all
    substantially larger than landscape defaults to preserve legibility in
    9:16).
  - Mechanism heading: 96px serif; body: 40px sans; quote: 32px mono.
  - Pipeline title: 70px serif; phase labels: 42px sans.
- `BrutalistHesitantWriter916` runs at fontSize 130 lineSpacing 2.5 with the
  portrait-aware `Math.min(width/1080, height/1920)` scale patch. Without the
  patch, the shipped scale would collapse to 0.5625, shrinking the serif to
  unreadable size (`feedback_hesitant_writer_portrait_scale`).
- `ClaudeComposerAsk916` reuses the landscape composer with the 916
  composition dimensions (1080x1920); wrapping handles narrow width naturally.

### §8.1 minimum size

- All body copy renders at effective ≥32px on the 4K master. Comfortably above
  the 24px floor.
- The 916 anatomy `tag` badges (18px sans) are labels, not primary text.

### §8.2 overflow

- Portrait fit iteration log (see CHECKS-REPORT.md):
  - B01 hesitant writer: reduced to 5 lines to fit vertical.
  - B03 pipeline: compressed 6 phases → 4 to fit vertical safe area.
  - B10 handoff: shortened command to fit composer input.
- After the three fixes above, no visible clipping at any 50/85% sample.
- Gate V confirmed 0 edge-bleed BLOCKERS on the final master.

### §8.3 contrast

- Same Claude palette as landscape — cream `#FAF9F5` + warm ink `#3D3929`
  yields >8:1 luminance contrast throughout the reel. Terracotta accent used
  sparingly; verdict pills use the accent as background with white text.
- Dark polarity outro (B11) — polarity is deterministic per slug seed. This
  slug hashes to dark; cream text on ink is high contrast by construction.

### §8.4 kerning sanity (Pango fallback catch)

- Same fonts as landscape (EB Garamond serif via Claude tokens, SF Pro UI,
  SF Mono). No Pango DejaVu fallback observed on any portrait sample.
- Numerals (`1080×1920`, `--tail 1.0s`, etc.) render as tabular-lining
  digits — the intended fidelity.

### §8.5 no-wordy-card

- Every 916 card body ≤ 45 words. The B10 composer's command is the paste-ready
  handoff prompt, intentionally longer (~85 words in portrait) — that's the
  viewer's homework, not a "read this while I talk" wall-of-text.

### §8.6 golden strings

Not applicable (no `golden.json` fixture for this reel; substitute is the
visual read audit).

## Verdict

**No PANGO fallback observed. No overflow observed after B01/B03/B10 fixes.
No contrast defect observed.** The absent legacy `type_check.py` is a known
toolkit gap, substituted here by the image-capable Read audit.

Bear's editing pass is next.
