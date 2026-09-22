---
name: blade-slides
description: "Reconstruct approved slide images, screenshots, image-only PPTX/PDF, or flattened pages as high-fidelity, human-editable PowerPoint with meaningful movable modules, native text, safe native geometry, source-faithful transparent assets, semantic Selection Pane names, and real PowerPoint QA. Use for BLADE Slides or image-to-editable-PowerPoint work where visual fidelity and practical layer structure both matter. Do not treat text-overlay drafts, sliced-image mosaics, or flat page images as final BLADE deliverables. 中文完整说明见 SKILL.zh-CN.md。"
metadata:
  short-description: "Human-editable, source-faithful PowerPoint reconstruction / 高保真可编辑 PPT 还原"
  version: "2.1.1"
---

# BLADE Slides V2.1.1

> **中文用户 / Chinese readers:** 完整中文 Skill 请阅读 [SKILL.zh-CN.md](SKILL.zh-CN.md)。所有参考资料均提供对应的中文导航和说明，入口见 [README.md](README.md)。

**Bao Layered Asset Decomposition & Editability for PowerPoint**

BLADE converts an approved slide design into a PowerPoint layer model that behaves more like a human-authored deck: objects are meaningful, modules move cleanly, regular geometry remains editable, complex materials keep their visual quality, and the background remains complete when foreground elements are moved away.

Quality order: **source fidelity > human editability > PowerPoint stability > speed**.

## Required Capabilities

Use the best available tools for:

- source-image inspection, OCR, crop comparison, and alpha inspection;
- image editing or generation for clean backgrounds and isolated transparent assets;
- native PowerPoint construction or conservative OOXML editing;
- authentic logo and brand-asset retrieval;
- final validation in real Microsoft PowerPoint.

If the project provides governance files, visual rules, a trusted template, or an accepted editable baseline, read those first.

## Production Modes

Choose one mode in the layer contract before creating assets.

### `full_rebuild`

Reconstruct a new page or a complete batch from flattened designs. Build and validate pages independently before merging them.

### `local_refinement`

Improve an accepted BLADE deck without rebuilding successful pages. Record:

- `accepted_baseline.source_deck`
- `allowed_change_slides`
- `protected_slides`
- the render or structure comparison used to protect unchanged pages

For object-scoped edits, record target semantic names and permitted properties; protect all other objects on the same slide (see methodology, Local refinement).

Conservative OOXML or library patches are allowed, but the final file must still be opened, saved, reopened, and exported by real Microsoft PowerPoint.

### `review_draft`

Create a fast temporary review file, such as editable text over a flat slide image. This is not a BLADE final. Mark the filename and delivery report as `REVIEW_DRAFT`, and never claim that it is fully layered.

## Freeze The Layer Contract

Create a contract before generating assets:

```bash
python3 <skill-directory>/scripts/init_layer_contract.py \
  --slide-id slide_07 \
  --source /absolute/path/source.png \
  --out /absolute/path/layer_contract.json \
  --mode full_rebuild
```

Assign every visible element to one representation:

| Kind | Use |
| --- | --- |
| `clean_base` | Natural scene after every movable object has been removed |
| `native_text` | Titles, body copy, labels, numbers, footnotes |
| `native_shape` | Regular cards, borders, separators, axes, connectors, pills |
| `transparent_png` | Icons, photo medallions, metallic nodes, complex glass or glow composites |
| `fixed_scene_visual` | Complex visuals bound to perspective, occlusion, or material context and not requested as movable |

OCR is only a draft. Review titles, brand names, proper nouns, abbreviations, numbers, years, currencies, units, and footnotes at 200%-400%. Record verified strings and confusable checks such as `AI / Al` and `1 / I / l`.

Read [methodology.md](references/methodology.md) for the complete decision process and [human-editability.md](references/human-editability.md) for the layer-quality standard.

## Human-Editable Layer Model

A final BLADE page must satisfy all of these conditions:

1. **Meaningful movement units:** cards, icons, title bars, logo cells, medallions, nodes, and callouts move as useful objects rather than many raster fragments.
2. **Native regular geometry:** ordinary lines, borders, cards, axes, and arrows without complex material use safe native shapes. A rectangular outline does not make a glass, metal, or glow shell ordinary geometry.
3. **Source-faithful complex material:** metallic, glass, glow, particle, and hero visuals may remain one clean transparent composite.
4. **Readable Selection Pane:** every significant object uses a semantic name such as `s08_logo_wall_panel` or `s14_milestone_200b`.
5. **Consistent repeated systems:** repeated cards, medallions, logo cells, and navigation elements share dimensions, padding, corner rules, and a `reuse_key`.
6. **No micro-raster mosaic:** do not rebuild borders, corners, shadows, lines, or letters from many tiny picture slices.
7. **Trusted slide canvas:** use the source template size or standard 16:9 at 13.333333 x 7.5 in. Do not preserve an unnecessary doubled canvas.

For significant objects, record:

- `significant: true`
- `powerpoint_name`
- `movement_unit`
- `reuse_key` when applicable

## Preservation-First Decomposition

Define:

- `user_requested_movable`: objects that must move, resize, or remain editable;
- `preserve_source_pixels`: successful photography, screens, environmental UI, or decoration that does not need editing;
- `hero_visuals`: high-design anchors such as platforms, flywheels, light paths, and complex networks;
- `script_generated_visuals_forbidden: true`: scripts may measure, typeset, and assemble, but must not cheaply approximate premium visuals.

Do not leave requested movable objects in the clean base. Do not damage the approved design merely to increase object count. Choose layer boundaries according to human editing intent and visual completeness.

### Source-Critical Visuals

Evidence photographs, named buildings, historical images, product imagery, and official logos must preserve identity:

- extract them from original media or the approved source page, not from a regenerated background;
- record visual anchors and source-versus-render evidence;
- never generate, trace, recolor, or approximate an official logo.

### Fixed Scene Boundary

Keep a complex structure as `fixed_scene_visual` when it is tightly bound to architecture, people, surfaces, perspective, or occlusion and the user does not need to move it. Text, ordinary cards, and explicitly movable icons above it can still be separated. Do not disguise environmental pixels inside a supposedly transparent movable asset.

## Edge, Panel, Circle, And Grid Fidelity

These are blocking checks:

- **Complete border:** gold, white, or other closed edging remains continuous; transparent corners contain no source background.
- **Safety padding:** the visible alpha bounds do not touch the asset canvas; leave room for borders, glow, and shadow.
- **Complete circle:** photo medallions, rings, and milestone nodes remain closed and round, use consistent diameter, and sit inside their container rather than touching it.
- **Shared seam:** paired header/body frames share the same baseline, cut-corner angle, and border thickness.
- **Logo wall:** separate the wall panel, header bar, cell shells, and authentic logos; keep logo proportions.
- **Repeated modules:** measure one approved master and reuse it instead of redrawing each copy by eye.

For complex panels, a clean movable shell PNG plus native text and icons is acceptable. It must have complete geometry, transparent corners, and sufficient padding. For layered glass, read methodology's Panel systems checks for actual composite opacity, not just the presence of alpha.

## Charts And Premium Callouts

Prefer a hybrid model:

- native grids, axes, data lines, guide lines, connectors, and text;
- transparent source-faithful assets for metallic nodes or nontrivial callout skins;
- independent native text above visual shells;
- explicit checks that labels, guide lines, and nodes remain anchored to the correct data points.

Do not replace a shaped arrow with a generic rounded rectangle, or use oversized default corner radii that change the design.

## Build And Assemble

Recommended page directory:

```text
page_NNN/
|-- clean_base.png
|-- assets/
|-- layer_contract.json
|-- page.pptx
|-- preview.png
|-- clean_base_proof.png
|-- move_away_proof.png
|-- alpha_purity_contact_sheet.png
`-- validation.json
```

Build rules:

- create text boxes by semantic block, not by visual line fragment;
- use multiple runs inside one text box for mixed-color titles;
- require true alpha with no white edge, rectangular matte, environmental residue, or leftover text;
- use intentional z-order, typically `clean_base -> fixed/composite visuals -> native shapes -> icons -> text`;
- match PowerPoint shape names to contract `powerpoint_name` values;
- move every movable module away from its original position and verify both the object and exposed background.

Read [page-worker-contract.md](references/page-worker-contract.md) when building pages independently or in parallel.

### Merge Strategy

- `full_rebuild`: copy validated whole slides through real PowerPoint Slide Sorter where possible.
- `local_refinement`: patch only `allowed_change_slides`; compare protected pages against the accepted baseline.

## QA Gates

A final delivery must pass:

1. exact text, proper nouns, figures, currencies, units, line breaks, and confusable characters;
2. full-page and key-crop source/render comparison;
3. object types, semantic names, repeated systems, z-order, and canvas size;
4. move-away, clean-base-only, alpha, and Selection Pane review;
5. OOXML package checks, contract validation, and human-editability audit;
6. real Microsoft PowerPoint open, save, close, reopen, and export with no repair.

```bash
python3 <skill-directory>/scripts/validate_layer_contract.py \
  /absolute/path/layer_contract.json \
  --pptx /absolute/path/page.pptx \
  --report /absolute/path/validation.json

python3 <skill-directory>/scripts/audit_human_editability.py \
  /absolute/path/final.pptx \
  --strict \
  --report /absolute/path/human_editability.json
```

Read [qa-gates.md](references/qa-gates.md) for all blocking gates and [failure-modes.md](references/failure-modes.md) for recovery patterns.

## Finalization Order

1. Open, inspect, save, close, reopen, and export in real Microsoft PowerPoint.
2. Remove quarantine only from trusted locally generated files when appropriate for the operating system.
3. Run package, contract, editability, and visual checks.
4. Record the final SHA-256.
5. Do not reopen the deliverable with software that may rewrite it after the hash. If it changes, repeat QA and hashing.

## Honest Delivery Language

- A `review_draft` is mainly for fast content review and may retain flattened visuals.
- A BLADE final must state what is native, what is an independent transparent asset, and what remains fixed for fidelity.
- Never describe a flat page image, sliced-image mosaic, or text-overlay deck as fully layered and editable.

Deliver the PPTX together with a preview, layer contract, QA evidence, real PowerPoint validation result, known fidelity boundaries, and final checksum.
