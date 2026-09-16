# TYPECHECK — The nbb Skill (portrait 2160×3840)

## Missing legacy checker (documented gap)

`runtime/scripts/type_check.py` and `reference/type-spec.md` referenced in
some public docs are **NOT present** in this isolated toolkit revision.
Not fabricated — honestly logged.

## What ran instead

Actual visual typography review by frame inspection via
`runtime/qc/final_frame_check.py` (Gate V) on the finished 4K portrait
master. Gate V measures against the portrait safe area (972×1728 within
1080×1920 design reference) and uses the same FILL_MIN 0.55 and edge-bleed
tests as landscape.

## Result

See `_qc/REPORT.md` and `_qc/contact_sheet.png`.

## Fonts / typography sources

- Serif — EB Garamond
- UI Sans — Inter
- Mono — JetBrains Mono

Portrait-specific adjustments:
- BLUF (B01): fontSize 130, lineSpacing 2.5, 5 short lines (per
  `feedback_hesitant_writer_portrait_bluf_recipe`)
- BrutalistHesitantWriter carries the portrait-scale patch
  (`Math.min(width/1080, height/1920)` when height > width) per
  `feedback_hesitant_writer_portrait_scale`
- SkillTeardownAnatomy916 / Pipeline916 / Mechanism916 are native
  portrait variants (same schema, portrait reflow — stacked columns,
  larger type)

## Notes for a human reviewer

- `metadata.channel_title` deliberately OMITTED for portrait per
  `feedback_channel_title_portrait_bleed` (the landscape overlay would
  bleed past the portrait safe.b in 9:16).
- Portrait outro card carries `@NikBearBrown` from ClaudeTitleOutro916
  (OUTRO-LOCK.md).
- Inner composer beats keep `folderLabel: "@HumanitariansAI"` per
  playlist channel.
