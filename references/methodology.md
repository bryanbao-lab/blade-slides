# BLADE V2 Methodology

> 中文说明：请阅读 [methodology.zh-CN.md](methodology.zh-CN.md)。

## 1. Establish The Truth Set

Before changing anything, collect:

- Approved page render or source image.
- Trusted template or accepted editable baseline, if any.
- Exact slide size and font rules.
- Authentic logos and source-critical photography.
- User-requested movable objects and accepted fixed visuals.
- Previous QA evidence for pages already accepted.

The approved render is the visual truth. The accepted PPTX is the package and layer baseline for local refinements.

## 2. Select A Production Mode

### Full rebuild

Use for a new page or a full batch. Build and validate each page independently. Merge only validated pages.

### Local refinement

Use for corrections to an accepted deck. Record the baseline deck, allowed slide numbers, protected slide numbers, and how protected pages will be compared. Patch only the failed system or object.

### Review draft

Use only for urgent content review. It may use a flat page and editable text overlay, but must be labelled as a draft and never pass the BLADE final gate.

## 3. Decomposition Decision Tree

For every visible element:

1. Is the user expected to edit its text? Use `native_text`.
2. Is it a regular border, line, card, axis or connector? Use `native_shape`.
3. Does it have optical material, source-critical imagery, metallic/glass treatment or complex lighting? Use `transparent_png` as one meaningful module.
4. Is it bound to scene perspective or occlusion and not requested movable? Use `fixed_scene_visual` or fold it into the `clean_base`.
5. Would separating it require environment pixels, fragmented arcs or many small slices? Enlarge the meaningful composite boundary or keep it fixed.

Never choose a representation only to maximize object count.

## 4. Preserve Accepted Systems

Identify repeated systems before rebuilding:

- page title and stage icon placement;
- shared card shells and headings;
- logo-wall grid and cells;
- medallion diameter and inset;
- AI Native / Scale / Differentiation visual anchors;
- chart node and callout language;
- approved brand-logo placement and footer rules;

Measure a single approved master and reuse it. Record `reuse_key` values in the contract.

## 5. Build The Clean Base

Remove only objects listed under `user_requested_movable`. Preserve successful source pixels that do not need editing. Reconstruct exposed environment naturally, using source-preserving ImageGen when local removal would leave obvious patches.

The clean base fails if it contains:

- a second copy or shadow of a movable object;
- filled rectangles where environment should continue;
- erased scene details or distorted architecture;
- regenerated source-critical photos or logos.

## 6. Build Meaningful Foreground Modules

### Panel systems

Use native shapes for ordinary geometry. For complex cut corners, gold edging, glass and soft shadows, create a clean transparent shell with complete borders and safety padding. Keep icon and text separate where useful.

### Paired header and body frames

Build from a shared geometry spec. The common seam, cut-corner angle, line thickness and total width must match. A double line or offset diagonal is a blocking error.

### Circular images and medallions

Start from a crop larger than the intended circle. Reconstruct the complete circle and rim before resizing. Normalize diameter and keep an inset from the card edge. Never crop an already incomplete circle tighter.

### Logo walls

Separate wall panel, header bar, cell shells and individual authentic logos. Use one measured grid. Logos retain original proportions and transparent backgrounds.

### Charts and callouts

Keep grid, axes, data lines, labels and simple connectors native. Use transparent assets for metallic nodes and nontrivial arrow/callout skins. Anchor labels and guide lines to exact source data points.

### Hero composites

Use one source-faithful asset for a platform, network, glow system or other high-design visual if native reconstruction would cheapen it. Keep editable words and explicitly movable icons above the composite.

## 7. Name And Assemble

Use semantic PowerPoint names on all significant objects. Keep z-order intentional. Repeated modules share naming patterns and `reuse_key` values.

Avoid groups that make ordinary edits harder unless the group is itself the intended movement unit. Do not use unsupported custom geometry or XML hacks that risk Office repair.

## 8. Validate Incrementally

For each page, inspect:

- clean base alone;
- movable assets on black, white and checkerboard backgrounds;
- move-away evidence;
- Selection Pane names;
- source/render overlay and key crops;
- exact text and confusable characters;
- PowerPoint export, not only library-rendered previews.

For local refinements, compare protected pages against a fresh render of the accepted baseline before touching the final package.

## 9. Finalize Once

Open, save and export in Microsoft PowerPoint before final technical QA. After validation and SHA-256, do not reopen the deliverable in an application that can silently rewrite it.
