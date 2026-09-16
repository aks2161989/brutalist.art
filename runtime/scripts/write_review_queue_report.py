#!/usr/bin/env python3
"""Combine source inventory and human-readable visual findings; never mutate reels."""
import json
from pathlib import Path
import sys


def main():
    out=Path(sys.argv[1])
    audit=json.loads((out/'audit.json').read_text())
    notes=json.loads((out/'review-notes.json').read_text())
    rows=audit['reels']
    text=['# isdone film audit — September 11, 2026', '',
          'Scope: **all 26 films in the supplied isdone list, 676 authored beats**. '
          'Source/asset routing was inspected for every reel. Twelve distributed master frames '
          'per film (312 total) were visually reviewed; 586 additional source/compiled-beat '
          'samples were generated for drill-down, not all independently inspected. '
          'This is a queue-wide source and sampled-visual audit, not continuous playback, '
          'a full fact-check, or approval to publish.', '',
          '## Main findings', '',
          '- **29 unnecessary pending pantry requests** across chapters 2–6 and the older Chapter 1 cut '
          '(list numbers 10, 11, 13, 15, 16, 19). Replace with executed code, data or native diagrams. '
          'The four requests in the newer Chapter 1 (#9) have already been replaced.',
          '- **Two broken equations plus the overflow narration recur in #19.** '
          'The corrected #9 provides the derivation and execution evidence, not a timing template.',
          '- **Code/output clipping is widespread.** Frames and beat-specific examples are listed below. '
          'A real run is still unusable if its decisive line is outside the viewport.',
          '- **Execution provenance needs strengthening.** Some FACTCHECK files report real local tests, '
          'but raw stdout/scripts are not preserved alongside the film. This is a reproducibility gap, '
          'not proof that the run was fabricated. #25 explicitly acknowledges an illustrative traceback.',
          '- **Queue state is not content QA.** #12 reports 31 slates while sampled frames are rendered. '
          '#6 really is mostly slates. Several masters are stale or below native 4K. No approval ledger was changed.', '',
          '## Rules and tooling changed', '',
          'Public AI/deep/general/CLI explainer guidance now requires structured mathematical notation, '
          'executed evidence, honest reconstruction labels and rendered-frame review. Shared rules apply '
          'to all film builders, including the separate sandbox used by the course loop. '
          'Both compiler copies retain a renderer inventory but no longer demand a 40% media quota. '
          'Genuine archival images/documents remain legitimate; no paid sourcing was performed.', '',
          'The skill-creator guidance kept these as shared, scoped production rules rather than a '
          'ban on useful archival imagery. New audit code has two passing tests; math checks have five; '
          'pipeline safety has 45. Remotion TypeScript check passed. The four edited public '
          'explainer skill manifests pass skill validation; overly long legacy discovery descriptions '
          'were shortened while keeping the detailed instructions in their bodies.', '',
          '## Repair order', '',
          '1. Finish the existing #9 layout/type cleanup; its math/data repair is rendered but is not a clean master.',
          '2. #19 and chapters 2–6: replace unnecessary sourcing, capture executions, split clipped code, render and inspect.',
          '3. CLI exercises/assignments: preserve real run receipts and pair code with visible output.',
          '4. Reconcile stale/slate state, fix portrait/chart sizing and finish the genuinely incomplete films.',
          '', 'Do not change human approvals or publish in response to this audit. Changing skills does not retroactively repair an MP4.', '',
          '## Every film', '']
    for row in rows:
        n=row['number'];note=notes[str(n)];reel=Path(row['reel'])
        text += [f'### {n:02d}. {reel.name}', '',
                 f'**{note["priority"]}** — {note["finding"]}', '',
                 f'Master probe: {row["width"]} × {row["height"]}; '
                 f'{float(row["duration"] or 0):.1f}s; stale at snapshot: {row["stale"]}; '
                 f'declared slates: {len(row["declared_slates"])} (metadata, not a pixel count).', '',
                 f'[Reel]({reel}) · [Master samples]({out.resolve() / f"{n:02d}-master.jpg"}) · '
                 f'[Source evidence]({out.resolve() / f"{n:02d}-source.json"})', '']
        # All three legacy spellings occur in this queue.
        sheet=json.loads((reel/'beat_sheet.json').read_text())
        for beat in sheet.get('beats',[]):
            shot=beat.get('shot') or {}
            path=shot.get('pantry_path') or shot.get('pantry_file') or shot.get('pantry')
            if path:
                intent=shot.get('visual_intent') or shot.get('brief') or shot.get('sourcing') or shot.get('subject') or ''
                text += [f'- **{beat["beat_id"]}** — {intent}']
        text += ['']
    text += ['## Audit artifacts and limits', '',
             '`audit.json` records hashes, master selection, probes, candidates and sample origins. '
             '`review-notes.json` records the actual visual review conclusions. '
             '`NN-contact.jpg` shows available local beat media at 70%; '
             '`NN-master.jpg` samples the actual selected master without assuming stale sheets align to it. '
             'The largest root/mp4 file was selected to match isdone.py. Missing cached beat files, '
             'missing raw receipts and missing source matches are disclosed, not silently treated as PASS.', '',
             'Specific pixels were sampled, not every animation state. Run 15/50/85% beat-level QC, '
             'formula reveal-state checks and actual execution tests during each repair. '
             'Primary-source attribution and scholarly claims require a separate full fact-check.']
    (out/'AUDIT.md').write_text('\n'.join(text)+'\n')


if __name__=='__main__':
    main()
