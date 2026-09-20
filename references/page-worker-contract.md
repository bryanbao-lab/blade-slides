# Page Worker Contract

> 中文说明：请阅读 [page-worker-contract.zh-CN.md](page-worker-contract.zh-CN.md)。

This reference defines the minimum evidence for one reconstructed page. Use the same structure whether work is performed by one agent or several independent page workers.

## Inputs

- Approved full-page source render.
- Exact slide size in pixels and inches.
- Layer contract with production mode.
- Verified text list, fonts and line-break locks.
- Authentic logos and source-critical media.
- Accepted system measurements or `reuse_key` sources.
- For local refinement: baseline PPTX, allowed slide number and protected pages.

## Required Outputs

```text
page_NNN/
├── clean_base.png
├── assets/
├── layer_contract.json
├── page.pptx
├── preview.png
├── clean_base_proof.png
├── move_away_proof.png
├── alpha_purity_contact_sheet.png
├── source_vs_render.png
├── key_crops/
└── validation.json
```

## Responsibilities

1. Do not invent copy, logos, data, people, products or brand elements.
2. Do not modify another page directory or shared baseline.
3. Keep every significant asset and PowerPoint shape semantically named.
4. Use native shapes for regular geometry; use source-faithful composites for optical material.
5. Do not create micro-raster slices to fake borders, corners, lines or letters.
6. Validate complete edges, circles, repeated grid measurements and meaningful movement units.
7. Save actual move-away evidence, not only a statement that objects are movable.
8. Report any fixed visual and the reason it remains fixed.

## Validation Handoff

The page is not ready for merge until:

- contract validator passes;
- source/render visual check passes;
- significant object names exist in the PPTX;
- clean base and foreground are mutually exclusive;
- PowerPoint opens the page without repair;
- all blockers are absent from `validation.json`.

## Merge Handoff

For full rebuilds, supply one slide only. The parent deck assembler copies validated slides in order through Microsoft PowerPoint.

For local refinements, supply the changed page and a protected-page comparison report. Do not replace or regenerate untouched pages.
