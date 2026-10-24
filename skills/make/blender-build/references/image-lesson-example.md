# Example: reconstructing a stylized spaceship from rendered views

Use this pattern when teaching from a published gallery or video screenshots.
The example describes a new reconstruction, not the history of an existing STL
kit. Replace the references with actual accessible image files or public URLs;
do not give a learner unresolved placeholders as a finished prompt pack.

## Starter prompt for a fresh coding-agent chat

> Help me learn Blender by constructing a stylized spaceship from the attached
> forward-quarter, side, rear, top and front images. These images are all we have;
> do not assume access to the original model, STL kit, blueprints or build scripts.
> First describe the visible major forms and any uncertainty caused by perspective.
> Propose a short sequence of modeling checkpoints, and explain the Blender concept
> behind each. Use X for width, Y for length and Z for height. Choose a convenient
> working scale and label it as an assumption unless the references supply units.
> Start with only the main hull blockout. If you can control Blender, work in a new
> scene and save a checkpoint; otherwise give me a script I can run in Blender's
> Scripting workspace, plus a practical manual alternative. Return front, side and
> quarter views for comparison. Do not add small details until the silhouette is
> checked. Tell me what you actually executed and what is still a proposal.

In the delivered lesson, name the attached files and their view directions
explicitly. Show the target images beside the prompt so viewers know what to
capture from the film or download from GitHub.

## Example teaching checkpoints

| Goal and evidence | Blender concept / practical approach | Agent request and visible check |
|---|---|---|
| Hull silhouette from side and front | Start with a low-resolution UV sphere, scale along the long axis, edit cross-section loops with proportional editing; or generate an editable profile mesh. Explain scale and shading separately. | “Change only the hull. Match its widest section and nose taper to these two views. Render both views and explain the remaining disagreement.” Check width-to-length and height-to-length ratios; do not trust the quarter view alone. |
| Fins from top, rear and quarter | Build a plane outline, extrude thickness or use Solidify, place its origin deliberately and mirror a symmetric partner. | “Add the dorsal and side fins as separate named objects. Show their roots and tips in top and rear views before adding trim.” Check sweep, attachment and symmetry; avoid guessing hidden hinge mechanics. |
| Portholes and trim from close-ups | Model one ring and inset pane; duplicate along a measured path or place copies along the hull. A curve with a bevel profile is one proposed trim technique. | “Make one porthole first and explain its local axes and depth. After I inspect it, repeat it at the visible spacing.” Check surface contact and prevent floating or deeply buried fittings. |
| Engine and turret from rear/detail | Radial duplication for repeated nozzles; simple revolved forms for bells and turret. Use an explicit center/origin. | “Build the visible exterior only. Match the visible nozzle arrangement and explain which depths are estimated.” Check silhouette and spacing, without claiming a functional engine or turret rig. |
| Material and detail pass | Separate material slots, roughness and metallic response; explain geometry seams versus texture alternatives. | “Match the image palette under neutral lights. Explain your chosen surface-detail method rather than claiming it was the original method.” Check color boundaries and silhouette after shading. |
| Comparison and correction | Consistent comparison views, reproducible light setup, incremental saves | “Show target and current front, side and rear views. Identify the largest shape mismatch and correct only that before adding detail.” Accept improvements that hold across multiple views. |

This is an illustrative technique selection, not a tested script or a required
modifier stack. A supplied kit's panel lines may be intentional; distinguish
fidelity to that rendered design from fidelity to another depiction of the same
fictional ship. Do not silently switch between source designs mid-lesson.

## A useful correction prompt

> The side view looks plausible, but the front view shows the hull too narrow and
> the portholes projecting too far. Keep the current length and fin placement.
> Adjust the hull width and porthole seating, save a new checkpoint, then render
> the same front and side views. Explain which coordinates or parameters changed
> and why. Do not compensate by changing the cameras.

The narrator should connect the correction to a visible comparison. If the
film has no actual demonstration, present this as the learner's proposed next
check—not as a correction that has already succeeded.
