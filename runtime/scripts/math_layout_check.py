"""Reject known flattened notation in prose-card scenes, not literal code.

Conservative preflight, not an algebra/visual-QC substitute. Other renderers
remain valid; explicit code displays are deliberately outside this detector.
"""
import re

PROSE_SCENES = {"FormACard", "FormACard916", "WantQuote", "WantQuote916"}
RAW_TEX = re.compile(r"\\(?:frac|dfrac|sum|sqrt|begin)\b|\$\$")
FLAT = re.compile(r"(?:exp\s*\(.*[÷Σ∑]|[Σ∑].*[÷/]|\bp\([a-z]\)\s*/\s*p\([a-z]\)|\b[a-zA-Z]_[a-zA-Z0-9]+\b)")


def math_layout_errors(sheet):
    errors = []
    for beat in sheet.get("beats", []):
        rem = (beat.get("shot") or {}).get("remotion") or {}
        if rem.get("pattern") not in PROSE_SCENES:
            continue
        props = rem.get("props") or {}
        texts = [props.get("quote", ""), *(props.get("lines") or [])]
        if any(isinstance(text, str) and (RAW_TEX.search(text) or FLAT.search(text)) for text in texts):
            errors.append(f'{beat.get("beat_id")}: structured math required; do not put equations in {rem["pattern"]}. See docs/MATH-TYPESETTING.md')
    return errors
