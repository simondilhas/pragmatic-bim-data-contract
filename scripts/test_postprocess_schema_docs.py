#!/usr/bin/env python3
"""Unit tests for schema doc postprocessing."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from postprocess_schema_docs import (
    adjust_search_boost,
    load_class_metadata,
    load_embedded_value_classes,
    split_and_render_classes_sections,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_ROOT = REPO_ROOT / "contract" / "00_pragmatic_bim_data_contract.yaml"


class EmbeddedValueClassTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        _, _, cls.class_parents = load_class_metadata(SCHEMA_ROOT)
        cls.embedded = load_embedded_value_classes(SCHEMA_ROOT, cls.class_parents)

    def test_includes_core_embedded_ranges(self) -> None:
        expected = {
            "LocalizedText",
            "Classification",
            "GeometryRepresentation",
            "QuantityValue",
            "MetadataEntry",
            "PerformanceProperty",
            "PostalAddress",
            "ContactPoint",
            "TimeLink",
        }
        self.assertTrue(expected <= self.embedded)

    def test_includes_performance_subclasses(self) -> None:
        expected = {
            "FireProperty",
            "AcousticProperty",
            "ThermalProperty",
            "StructuralProperty",
            "SecurityProperty",
            "MaterialProperty",
        }
        self.assertTrue(expected <= self.embedded)

    def test_excludes_graph_classes(self) -> None:
        self.assertNotIn("Entity", self.embedded)
        self.assertNotIn("Space", self.embedded)
        self.assertNotIn("Change", self.embedded)


class SplitClassesSectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.class_order, cls.class_descriptions, cls.class_parents = load_class_metadata(SCHEMA_ROOT)
        cls.class_hierarchy_order = {
            name: idx for idx, name in enumerate(sorted(cls.class_order, key=lambda c: cls.class_order[c]))
        }
        cls.embedded = load_embedded_value_classes(SCHEMA_ROOT, cls.class_parents)

    def test_moves_localized_text_to_embedded_section(self) -> None:
        text = "\n".join(
            [
                "# Index",
                "",
                "## Classes",
                "",
                "| Class | Description |",
                "| --- | --- |",
                "| [Entity](Entity.md) | Graph node. |",
                "| [LocalizedText](LocalizedText.md) | Localized text value. |",
                "",
                "## Slots",
                "",
            ]
        )
        result = split_and_render_classes_sections(
            text,
            self.embedded,
            self.class_order,
            self.class_descriptions,
            self.class_hierarchy_order,
        )
        self.assertIn("## Graph classes", result)
        self.assertIn("## Embedded value types", result)
        self.assertIn("[Entity](Entity.md)", result)
        self.assertIn("[LocalizedText](LocalizedText.md)", result)
        graph_part, embedded_part = result.split("## Embedded value types", 1)
        self.assertIn("[Entity](Entity.md)", graph_part)
        self.assertNotIn("[LocalizedText](LocalizedText.md)", graph_part)
        self.assertIn("[LocalizedText](LocalizedText.md)", embedded_part)


class SearchBoostTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        _, _, cls.class_parents = load_class_metadata(SCHEMA_ROOT)
        cls.embedded = load_embedded_value_classes(SCHEMA_ROOT, cls.class_parents)

    def test_lowers_embedded_class_boost(self) -> None:
        text = "---\nsearch:\n  boost: 10.0\n---\n\n# Class: PostalAddress\n"
        result = adjust_search_boost(text, "PostalAddress", self.embedded)
        self.assertIn("boost: 2.0", result)

    def test_keeps_graph_class_boost(self) -> None:
        text = "---\nsearch:\n  boost: 10.0\n---\n\n# Class: Entity\n"
        result = adjust_search_boost(text, "Entity", self.embedded)
        self.assertIn("boost: 10.0", result)

    def test_lowers_exclusive_embedded_slot_boost(self) -> None:
        text = "\n".join(
            [
                "---",
                "search:",
                "  boost: 5.0",
                "---",
                "",
                "# Slot: postal_code",
                "",
                "| Domain Of | [PostalAddress](PostalAddress.md) |",
            ]
        )
        result = adjust_search_boost(text, "postal_code", self.embedded)
        self.assertIn("boost: 3.0", result)

    def test_keeps_mixed_domain_slot_boost(self) -> None:
        text = "\n".join(
            [
                "---",
                "search:",
                "  boost: 5.0",
                "---",
                "",
                "# Slot: localized_names",
                "",
                "| Domain Of | [Entity](Entity.md) |",
            ]
        )
        result = adjust_search_boost(text, "localized_names", self.embedded)
        self.assertIn("boost: 5.0", result)


if __name__ == "__main__":
    unittest.main()
