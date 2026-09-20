# BLADE Slides

**Turn finished slide images into source-faithful, human-editable PowerPoint.**

BLADE stands for **Bao Layered Asset Decomposition & Editability**.

Image-first slide design can produce beautiful results, but the final page is often a flat image. BLADE provides an agent workflow, a layer contract, and deterministic QA scripts for reconstructing that approved design as a practical PowerPoint layer system.

The goal is not to vectorize every pixel. The goal is to preserve the approved visual quality while making the parts people actually need to edit behave like a human-authored deck.

## What BLADE Rebuilds

- readable business copy as native PowerPoint text;
- ordinary cards, borders, axes, connectors, and separators as native shapes;
- icons, medallions, metallic nodes, glass, and glow as clean movable transparent assets;
- complex scene-bound visuals as documented fixed scene elements when separating them would damage fidelity;
- meaningful modules with semantic Selection Pane names;
- clean backgrounds that remain natural when foreground elements are moved away.

## What BLADE Rejects

- a full-slide screenshot with editable text placed on top;
- hundreds of tiny image slices pretending to be editable geometry;
- generic `Image 37` / `TextBox 22` object naming throughout the deck;
- incomplete borders, clipped circles, contaminated transparent assets, or duplicated foreground objects;
- a file described as “fully editable” when most of the design remains an undisclosed flat image.

## Repository Contents

```text
blade-slides/
|-- SKILL.md
|-- agents/openai.yaml
|-- assets/layer-contract-template.json
|-- references/
|-- scripts/
|   |-- init_layer_contract.py
|   |-- validate_layer_contract.py
|   |-- audit_human_editability.py
|   `-- self_check.py
|-- requirements.txt
`-- README.md
```

## Requirements

- An AI agent that can read a skill/instruction directory.
- Python 3.10 or newer.
- Pillow and python-pptx for the bundled validators.
- An image editor or image-generation capability for clean backgrounds and isolated visual assets.
- Microsoft PowerPoint for the final approval gate.

The bundled scripts are cross-platform. The final “opens without Repair and exports correctly” gate specifically requires real Microsoft PowerPoint; a library-only or alternate-office-suite test is not equivalent.

## Install

### Codex

```bash
git clone https://github.com/bryanbao-lab/blade-slides.git ~/.codex/skills/blade-slides
python3 -m pip install -r ~/.codex/skills/blade-slides/requirements.txt
```

Then invoke:

```text
Use $blade-slides to reconstruct this approved slide image as a high-fidelity,
human-editable PowerPoint. Keep text native, make regular modules editable,
and preserve complex visuals as clean movable composites where needed.
```

### Other agent runtimes

Clone or copy the repository into your platform's skill/instruction directory as `blade-slides`. If the platform ignores YAML front matter, provide `SKILL.md` as the workflow instruction and keep the `references/`, `scripts/`, and `assets/` paths together.

## Quick Start

Create a layer contract:

```bash
python3 scripts/init_layer_contract.py \
  --slide-id slide_01 \
  --source /absolute/path/source.png \
  --out /absolute/path/layer_contract.json \
  --mode full_rebuild
```

Complete the contract after inspecting the source, then validate one reconstructed page:

```bash
python3 scripts/validate_layer_contract.py \
  /absolute/path/layer_contract.json \
  --pptx /absolute/path/page.pptx \
  --report /absolute/path/validation.json
```

Audit a complete deck for pseudo-editability:

```bash
python3 scripts/audit_human_editability.py \
  /absolute/path/final.pptx \
  --strict \
  --report /absolute/path/human_editability.json
```

Run the repository smoke test locally or in your own CI:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/self_check.py
```

## Production Modes

| Mode | Use |
| --- | --- |
| `full_rebuild` | Reconstruct a new page or complete flattened deck |
| `local_refinement` | Change only specified pages or modules in an accepted deck |
| `review_draft` | Produce a fast temporary file for content review; never present it as BLADE final |

## Core Layer Types

| Type | Meaning |
| --- | --- |
| `clean_base` | Natural background after movable elements are removed |
| `native_text` | Editable text |
| `native_shape` | Safe regular PowerPoint geometry |
| `transparent_png` | Movable source-faithful complex artwork |
| `fixed_scene_visual` | Complex scene-bound visual intentionally kept fixed for fidelity |

## Honest Editability Boundary

BLADE is **fidelity-first layered editability**, not automatic full vectorization.

Some elements should remain high-quality raster composites:

- optical glass and metallic material;
- photography;
- complex light paths and particle networks;
- visuals tightly bound to architecture, people, or perspective.

The workflow requires these boundaries to be explicit. A final handoff should state what is native, what is a movable transparent asset, and what remains fixed.

## Privacy And Public-Safe Packaging

This repository contains:

- no client presentation;
- no company-confidential design or copy;
- no private logo or source image;
- no user-specific filesystem path;
- no API key, token, credential, or OCR output;
- no production QA report derived from a private deck.

The layer examples are generic. Never commit source presentations, extracted media, clean bases, screenshots, or review evidence unless you have the right to publish them.

## Contributing

Bug reports and pull requests are welcome. Useful contributions include:

- additional PowerPoint structural checks;
- safer alpha and edge-completeness diagnostics;
- reproducible public examples with permissive assets;
- cross-platform Microsoft PowerPoint automation notes.

Please do not submit proprietary slide content or unofficial copies of corporate logos.

## Author

Created by [Bryan Bao](https://github.com/bryanbao-lab).

## License

MIT
