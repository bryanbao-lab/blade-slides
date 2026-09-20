# ImageGen Prompt Patterns

Use these patterns only when source pixels cannot be cleanly preserved by extraction. Always attach the approved source image and state what must remain unchanged.

## Clean Base

```text
Edit the supplied 16:9 slide image into a clean scene plate.
Remove only: [EXACT MOVABLE OBJECTS].
Preserve exactly: composition, camera, architecture, lighting, palette, landscape,
approved fixed hero visual, and all source-critical imagery.
Naturally reconstruct only the areas exposed by the removed objects.
Do not add text, logos, panels, icons, borders, or generic UI.
Output one 3840x2160 clean background image.
```

## Transparent Panel Shell

```text
Recreate only the referenced panel shell as a separate transparent PNG.
Preserve its exact proportions, complete continuous border, cut-corner geometry,
gold/white edge treatment, glass material, highlight and restrained shadow.
Remove all text, icons, logos and environmental background pixels.
Leave generous transparent safety padding around every visible edge and glow.
The four corners of the PNG canvas must be fully transparent.
```

## Complete Circular Medallion

```text
Reconstruct the referenced circular photo medallion as one transparent PNG.
The entire circle and every ring must be visible and geometrically round.
Preserve the source photo identity, camera direction, gold/white trim and subtle shadow.
Do not crop the left, right, top or bottom rim. Add transparent safety padding.
Do not include any card background or adjacent text.
```

## Premium Milestone Node Or Arrow Shell

```text
Recreate only the referenced metallic milestone node / shaped arrow shell.
Preserve the source silhouette, gold material, highlight, glow and transparency.
Remove every word and number so native PowerPoint text can be placed above it.
Do not simplify it into a generic rounded rectangle or flat circle.
Output a clean transparent PNG with safety padding and no environmental pixels.
```

## Source-Critical Object Cleanup

```text
Use the supplied source crop as identity truth.
Remove only the overlaying label, border or obstruction: [ITEM].
Do not change the subject, logo, camera, orientation, landmark, color or proportions.
Return the complete object with transparent background and natural missing-detail repair.
```

After each generation, inspect black/white/checkerboard backgrounds, complete edges and move-away behavior. ImageGen output that changes identity or geometry must be rejected.
