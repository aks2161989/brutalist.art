"""Local structured MathText -> outlined SVG. No LaTeX process or text fallback."""
import base64
import io
import xml.etree.ElementTree as ET

import matplotlib
matplotlib.use("Agg")
from matplotlib import mathtext
from matplotlib.font_manager import FontProperties


def typeset(expression, color="#3D3929"):
    if not expression or "$" in expression:
        raise ValueError("Provide one math expression without dollar delimiters")
    buffer = io.BytesIO()
    with matplotlib.rc_context({"mathtext.fontset": "stix", "svg.fonttype": "path",
                                "svg.hashsalt": "brutalist-math-v1",
                                "savefig.transparent": True}):
        mathtext.math_to_image("$" + expression + "$", buffer,
                              prop=FontProperties(size=48), format="svg", color=color)
    svg = buffer.getvalue()
    viewbox = ET.fromstring(svg).attrib["viewBox"].split()
    return {"src": "data:image/svg+xml;base64," + base64.b64encode(svg).decode(),
            "aspect": float(viewbox[2]) / float(viewbox[3]), "expression": expression}
