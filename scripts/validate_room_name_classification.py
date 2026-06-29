#!/usr/bin/env python3
"""Validate room name vocabulary, activity mapping, and enum alignment."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml
from rdflib import Graph, Namespace, RDF

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from room_name_data import CONCEPTS, enum_key_from_notation  # noqa: E402

EX = Namespace("https://example.org/mapping/")
RN = Namespace("https://example.org/abstract/building-space-name-classification/")

MAPPING = REPO_ROOT / "classification/mapping/abstract-room-name-to-space-activity.mapping.ttl"
ACT_SKOS = REPO_ROOT / "classification/abstract-room-classification/building_space-activity-classification-en.skos.ttl"
ENUM_PATH = REPO_ROOT / "contract/entity_schema_enums.yaml"
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")


def main() -> None:
    errors: list[str] = []

    if not (100 <= len(CONCEPTS) <= 120):
        errors.append(f"Expected 100-120 leaf concepts, got {len(CONCEPTS)}")

    act_graph = Graph()
    act_graph.parse(ACT_SKOS)
    map_graph = Graph()
    map_graph.parse(MAPPING)

    activity_locals = {
        str(node).rsplit("/", 1)[-1]
        for node in act_graph.subjects(RDF.type, SKOS.Concept)
        if str(node).rsplit("/", 1)[-1] != "scheme"
    }

    for concept in CONCEPTS:
        if not concept.label_en or not concept.label_de:
            errors.append(f"{concept.local_name} missing EN/DE label")

    for concept in CONCEPTS:
        mapped = list(map_graph.objects(RN[concept.local_name], EX.mapsToActivity))
        if not mapped:
            errors.append(f"{concept.local_name} has no activity mapping")
            continue
        for target in mapped:
            local = str(target).rsplit("/", 1)[-1]
            if local not in activity_locals:
                errors.append(f"{concept.local_name} maps to unknown activity {local}")

    enum_doc = yaml.safe_load(ENUM_PATH.read_text(encoding="utf-8"))
    enum_values = enum_doc["enums"]["SpaceNameType"]["permissible_values"]
    for concept in CONCEPTS:
        key = enum_key_from_notation(concept.notation)
        if key not in enum_values:
            errors.append(f"Enum missing key {key} for {concept.notation}")

    if errors:
        print("Room name validation failed:")
        for err in errors:
            print(f"  - {err}")
        raise SystemExit(1)

    print(f"OK: {len(CONCEPTS)} room name concepts, mappings and enum aligned")


if __name__ == "__main__":
    main()
