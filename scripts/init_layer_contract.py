#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Create a BLADE Slides V2 layer contract skeleton.")
    parser.add_argument("--slide-id", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--width", type=int, default=3840)
    parser.add_argument("--height", type=int, default=2160)
    parser.add_argument("--slide-width-in", type=float, default=13.333333)
    parser.add_argument("--slide-height-in", type=float, default=7.5)
    parser.add_argument(
        "--mode",
        choices=("full_rebuild", "local_refinement", "review_draft"),
        default="full_rebuild",
    )
    args = parser.parse_args()

    source = str(Path(args.source).expanduser().resolve())
    out = Path(args.out).expanduser().resolve()
    clean_base = str(out.parent / "clean_base.png")
    prefix = args.slide_id.replace("slide_", "s")
    contract = {
        "schema_version": 3,
        "skill_version": "2.0.0",
        "slide_id": args.slide_id,
        "source_image": source,
        "reconstruction_mode": args.mode,
        "delivery_level": "review_draft" if args.mode == "review_draft" else "blade_full",
        "slide_size_px": [args.width, args.height],
        "slide_size_in": [args.slide_width_in, args.slide_height_in],
        "accepted_baseline": {
            "source_deck": "",
            "allowed_change_slides": [],
            "protected_slides": [],
            "protected_render_compare_required": args.mode == "local_refinement",
        },
        "editability_policy": {
            "user_requested_movable": [],
            "preserve_source_pixels": [],
            "hero_visuals": [],
            "script_generated_visuals_forbidden": True,
        },
        "structure_policy": {
            "human_editable_layer_model": True,
            "semantic_names_required": True,
            "regular_geometry_native": True,
            "micro_raster_fragments_forbidden": True,
            "meaningful_module_granularity": True,
            "selection_pane_reviewed": False,
        },
        "visual_fidelity_checks": {
            "nested_corner_pairs": [],
            "optical_material_regions": [],
            "open_gradient_regions": [],
            "repeated_system_motifs": [],
            "icon_semantic_anchors": [],
            "copy_linebreak_locks": [],
            "high_design_paths": [],
            "perspective_bound_scene_elements": [],
            "occlusion_relationships": [],
            "hero_composite_boundaries": [],
            "layer_exclusivity_pairs": [],
            "collision_clearances": [],
            "edge_completeness_checks": [],
            "contained_shape_insets": [],
            "paired_panel_seams": [],
            "repeated_grid_systems": [],
            "asset_safety_padding": [],
        },
        "content_verification": {
            "source_zoom_reviewed": False,
            "proper_nouns": [],
            "confusable_pairs_checked": [
                "AI vs Al",
                "1 vs I vs l",
                "currency symbols and units",
            ],
            "forbidden_text_tokens": [],
        },
        "source_fidelity": {
            "source_critical_reviewed": False,
            "review_evidence": [],
            "layers": {},
        },
        "layers": [
            {
                "id": "clean_base",
                "kind": "clean_base",
                "path": clean_base,
                "bbox_px": [0, 0, args.width, args.height],
                "z_index": 0,
                "editable": False,
                "significant": True,
                "powerpoint_name": f"{prefix}_clean_base",
                "movement_unit": "environment base",
                "semantic_group": "environment",
            }
        ],
        "expected": {
            "slide_count": 1,
            "native_text_min": 0,
            "native_shape_min": 0,
            "native_line_min": 0,
            "picture_min": 1,
            "movable_foreground_min": 0,
            "semantic_named_significant_min": 1,
        },
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(contract, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
