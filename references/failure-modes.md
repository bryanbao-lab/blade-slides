# Failure Modes And Recovery

> 中文说明：请阅读 [failure-modes.zh-CN.md](failure-modes.zh-CN.md)。

## A. Text-Overlay Or Slice-Mosaic Pseudo-Editability

**Symptoms:** hundreds of tiny pictures, generic names, no native lines, large flat areas, or editable text placed over a whole-page image.

**Why it fails:** users cannot move meaningful modules or understand the layer model.

**Recovery:** classify the file as `review_draft`; rebuild important systems as modules; run `audit_human_editability.py`.

## B. Contaminated Transparent Panel

**Symptoms:** moving a card reveals trees, skyline, floor or other source pixels attached below or around it.

**Recovery:** regenerate the shell or recut from a clean source with safety padding; inspect on black, white and checkerboard backgrounds; repeat move-away proof.

## C. Missing Or Double Border

**Symptoms:** top gold edge disappears, corners lose line segments, or paired frames show two offset diagonal lines.

**Recovery:** do not crop on the visible line. Add padding, reconstruct the whole closed path, and derive paired pieces from a shared geometry specification.

## D. Incomplete Circular Medallion

**Symptoms:** left/right rim is clipped, circle becomes oval, or touches the card boundary.

**Recovery:** return to a larger source crop, rebuild the complete circular silhouette and trim, normalize diameter, then position with inset.

## E. Over-Decomposed Logo Wall

**Symptoms:** header bars deform, grid cells drift, logos lose proportions, or the wall looks worse than the source.

**Recovery:** keep one panel, one header, one measured grid of cells, and authentic individual logos. Never slice decorative edges into fragments.

## F. Generic Native Approximation Of Premium Callout

**Symptoms:** a default rounded rectangle replaces a shaped arrow; milestone nodes are flat circles; the original hierarchy and polish disappear.

**Recovery:** use native line/text geometry plus a transparent source-faithful node or callout shell. Preserve anchor relationships and exact data-point positions.

## G. Oversized Default Rounded Corners

**Symptoms:** large pill-like curvature where the source has a restrained radius.

**Recovery:** measure the source radius in relation to height. Use a native rectangle only if the radius can match; otherwise use a clean movable shell asset.

## H. Background Object Duplication

**Symptoms:** moving a card or icon exposes a second copy underneath.

**Recovery:** enforce foreground/base exclusivity. Clean the base, then regenerate move-away and clean-base-only proofs.

## I. Source-Critical Visual Drift

**Symptoms:** wrong building, altered camera angle, changed brand mark, missing labelled entity.

**Recovery:** restore from the original media or source page, not the generated base. Validate visual anchors and label-to-target connection.

## J. `AI` Misread As `Al`

**Symptoms:** OCR or font rendering turns uppercase I into lowercase l.

**Recovery:** verify high-risk strings at 200%-400%, keep a confusable checklist, and scan extracted PPT text before delivery.

## K. Protected Pages Changed During Local Patch

**Symptoms:** unrelated pages shift or re-render differently after one-slide correction.

**Recovery:** stop delivery. Restore from the accepted baseline, patch only allowed slide XML/content, and rerun protected-page render or structure comparison.

## L. PowerPoint Repair Dialog

**Symptoms:** PowerPoint reports repaired content, hangs, or fails on reopen.

**Recovery:** remove unsupported custom geometry, XML hacks, external relationships or problematic groups; return to conservative native shapes and standard OOXML. A package that only passes `unzip -t` is not sufficient.

## M. QA After Final Hash

**Symptoms:** final file hash changes because PowerPoint or Preview reopened and rewrote the package.

**Recovery:** use the fixed finalization order. Any post-hash save requires full technical QA and a new SHA-256.
