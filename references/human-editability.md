# Human Editability Standard

> 中文说明：请阅读 [human-editability.zh-CN.md](human-editability.zh-CN.md)。

## Outcome

BLADE editability is not measured by object count. A PowerPoint user should be able to understand, select, move, replace, and reuse meaningful objects on the canvas and in the Selection Pane.

## Meaningful Movement Units

A movement unit should match an object a human would naturally select:

- a complete card shell, not separate top, bottom, corners, and shadow fragments;
- a complete logo cell, not several crops of one logo;
- a complete photo medallion with a continuous ring and adequate safety padding;
- a complete milestone node, metallic sphere, or arrow shell;
- a complete hero composite, not dozens of low-quality approximate light rays.

Text and the module shell are usually separate. Keep an icon separate when the user may replace, move, or reuse it.

## Rapid-Conversion Anti-Patterns

The following can only be a `review_draft`, never a BLADE final:

- editable text placed over a full-slide screenshot;
- hundreds of tiny image slices used to reconstruct borders, rounded corners, individual letters, or decoration;
- regular lines represented entirely by raster assets while the deck contains no native lines;
- generic object names such as `Image 37` or `TextBox 22` throughout the Selection Pane;
- an unnecessarily doubled slide canvas that distorts all coordinates and font sizes;
- a movable module that exposes a duplicate object, residue, or an erase patch when moved.

## Selection Pane Naming

Every `significant: true` object needs a unique, stable, semantic name. Examples:

```text
s05_aum_chart_shell
s05_benefit_card_01
s08_logo_wall_panel
s08_logo_cell_brand_a
s09_module_circle_01
s14_milestone_200b
s14_ma_arrow_shell
```

Names should communicate slide, system or module, and role. Do not use color or coordinates as the only meaning because style and position can change.

## Granularity Examples

### Panel or card

Recommended layers: `shell` + `icon` + `title` + `body`. Use a native shell for ordinary geometry. Use one transparent shell PNG when cut corners, metallic edging, glass, or optical shadow cannot be reproduced faithfully with safe native shapes.

### Logo wall

Recommended layers: `wall_panel` + `header_bar` + `cell_shell_N` + `logo_N`. Logos must be authentic source assets with their original proportions and transparent backgrounds.

### Photo medallion

Use one complete `transparent_png` containing the photograph, continuous ring, and necessary shadow. Do not reconstruct the ring from separate arcs. Keep text independent.

### Chart and callout

Use native grid, axis, line, and text objects together with transparent premium milestone nodes or arrow shells. The annotation and node may move independently, but their anchor relationship must be recorded and verified.

### Fixed scene visual

When a complex platform is bound to architecture, people, and perspective, keep the platform fixed in the scene while leaving its cards and text independent. Fixed content is a documented fidelity decision, not an undisclosed omission.

## Micro-Raster Rule

The following normally fail:

- a picture placement with width or height below approximately 0.18 in, unless it is an intentional small icon;
- a media asset with one dimension at or below 8 px and the other at least ten times larger, unless it is an approved texture line;
- several narrow PNG files replacing regular straight lines while native line count is zero.

Any exception must use `asset_role: line_texture` or document why native geometry cannot preserve the source, together with source comparison evidence.

## Geometry And Containment

- Closed borders must be continuous. Keep at least 2 px between visible alpha bounds and the asset canvas, with additional room for glow and shadow.
- Medallions must be closed and round, use consistent diameter, and retain an inset from their card.
- Paired title/body frames share the same seam baseline, cut-corner geometry, and border thickness.
- Build one master and a measured grid before copying repeated cells.

## Baseline Protection

A local refinement must declare `allowed_change_slides` and `protected_slides`. Protect unchanged pages with at least one of:

- before/after PNG comparison from the same PowerPoint render chain;
- shape count, shape-name, object-type, and key-position comparison;
- both methods for higher-risk pages.

If a protected page changes, the patch fails.

## Final Human Check

Open the Selection Pane in PowerPoint and inspect high-risk pages:

1. Are object names understandable?
2. Does selecting a card select the complete shell?
3. Does moving a card, medallion, logo, or callout expose a clean background with no duplicate?
4. Can text be edited without breaking hierarchy or container geometry?
5. Can repeated modules be adjusted through one consistent system instead of repairing many fragments?
