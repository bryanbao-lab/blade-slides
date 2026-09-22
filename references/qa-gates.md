# BLADE V2 QA Gates

> 中文说明：请阅读 [qa-gates.zh-CN.md](qa-gates.zh-CN.md)。

All blocking gates must pass. A visually pleasing thumbnail is not sufficient.

## Gate 1 — Source And Content

- Approved source and baseline identified.
- Exact text, proper nouns, numbers, years, currency and units verified.
- Confusable characters checked, especially `AI / Al` and `1 / I / l`.
- Official logos come from authentic assets.

## Gate 2 — Visual Fidelity

- Full-page source/render comparison.
- 100% crops for title, hero visual, complex cards, Logo wall and charts.
- Borders are continuous; corners and seams are not clipped or doubled.
- Circular assets are complete, round, consistently sized and inset.
- Repeated systems match one measured grid.
- Optical material and source-critical images preserve identity and quality.

## Gate 3 — Human Editability

- Readable business text is native.
- Regular lines and geometry are native where practical.
- Significant objects have semantic Selection Pane names.
- Movable objects correspond to meaningful human operations.
- No micro-raster mosaic is used to simulate editability.
- Fixed visuals are explicitly documented.

## Gate 4 — Clean Base And Alpha

- Clean base contains no duplicate foreground object.
- Transparent assets have real alpha and fully transparent canvas corners.
- Closed-border assets have safety padding and complete visible edges.
- Black, white and checkerboard checks show no matte or environment contamination.
- Glass interiors are checked over the actual background and existing backing layers; combined opacity preserves source-like translucency and text contrast, not merely transparent outer corners.
- Move-away proof shows a clean object and a natural original position.

## Gate 5 — Local Refinement Protection

- Only `allowed_change_slides` changed.
- Protected slides match baseline renders or inventories.
- For object-scoped edits, non-target objects on the changed slide also match the baseline; target changes stay within the recorded property scope, including apparent size after alpha-padding changes.
- Successful pages and accepted systems were not regenerated without cause.

## Gate 6 — PowerPoint Structure

- Standard/trusted template canvas size.
- Expected slide, picture, native text, native shape and native line counts.
- Contract `powerpoint_name` values exist.
- Fonts are available or embedded/substituted by an approved rule.
- No unsupported geometry, broken relation or external dependency.

## Gate 7 — Real Microsoft PowerPoint

- Opens with no Repair dialog.
- Saves and closes normally.
- Reopens successfully.
- Exports PDF/PNG with correct fonts, wrapping and z-order.

## Gate 8 — Final Package

- `unzip -t` passes.
- `validate_layer_contract.py` passes for reconstructed pages.
- `audit_human_editability.py --strict` passes for final BLADE delivery.
- Quarantine removed only for trusted locally generated files.
- Final SHA-256 recorded after all PowerPoint operations.
- File is not reopened or rewritten after the hash.

## Required Deliverable Statement

State clearly:

- production mode;
- what is native text/shape;
- what is independent transparent art;
- what remains fixed for fidelity;
- PowerPoint validation performed;
- known limitations, if any;
- final checksum.
