#!/usr/bin/env python3
"""Validate room name vocabulary, activity mapping, and enum alignment."""

from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

import yaml
from rdflib import Graph, Namespace, RDF

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from room_name_data import (  # noqa: E402
    CATEGORIES,
    CONCEPTS,
    GROUPS,
    NOTATION_V1_TO_V2,
    enum_key_from_notation,
)

EX = Namespace("https://example.org/mapping/")
RN = Namespace("https://example.org/abstract/building-space-name-classification/")

MAPPING = REPO_ROOT / "classification/mapping/abstract-room-name-to-space-activity.mapping.ttl"
ACT_SKOS = REPO_ROOT / "classification/abstract-room-classification/building_space-activity-classification-en.skos.ttl"
ENUM_PATH = REPO_ROOT / "contract/entity_schema_enums.yaml"
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")

EXPECTED_LEAF_COUNT = 117


def _check_unique_pref_labels(errors: list[str]) -> None:
    en: dict[str, list[str]] = defaultdict(list)
    de: dict[str, list[str]] = defaultdict(list)
    nodes: list[tuple[str, str, str, list[str], list[str]]] = []

    for cat in CATEGORIES:
        nodes.append((cat.local_name, cat.label_en, cat.label_de, [], []))
    for grp in GROUPS:
        nodes.append((grp.local_name, grp.label_en, grp.label_de, [], []))
    for concept in CONCEPTS:
        nodes.append(
            (concept.local_name, concept.label_en, concept.label_de,
             concept.alt_labels_en, concept.alt_labels_de)
        )

    all_en_prefs = {n[1].lower() for n in nodes}
    all_de_prefs = {n[2].lower() for n in nodes}

    for local, label_en, label_de, alt_en, alt_de in nodes:
        en[label_en.lower()].append(local)
        de[label_de.lower()].append(local)
        for alt in alt_en:
            if alt.lower() in all_en_prefs:
                errors.append(f"{local} altLabel EN '{alt}' collides with a prefLabel")
        for alt in alt_de:
            if alt.lower() in all_de_prefs:
                errors.append(f"{local} altLabel DE '{alt}' collides with a prefLabel")

    for label, locals in en.items():
        if len(locals) > 1:
            errors.append(f"Duplicate EN prefLabel '{label}': {locals}")
    for label, locals in de.items():
        if len(locals) > 1:
            errors.append(f"Duplicate DE prefLabel '{label}': {locals}")


def _check_hierarchy(errors: list[str]) -> None:
    cat_locals = {c.local_name for c in CATEGORIES}
    grp_locals = {g.local_name for g in GROUPS}
    grp_by_cat: dict[str, list[str]] = defaultdict(list)
    for grp in GROUPS:
        if grp.category not in cat_locals:
            errors.append(f"Group {grp.local_name} references unknown category {grp.category}")
        grp_by_cat[grp.category].append(grp.local_name)

    leaf_by_grp: dict[str, list[str]] = defaultdict(list)
    for concept in CONCEPTS:
        if concept.group not in grp_locals:
            errors.append(f"Leaf {concept.local_name} references unknown group {concept.group}")
        if concept.category not in cat_locals:
            errors.append(f"Leaf {concept.local_name} references unknown category {concept.category}")
        leaf_by_grp[concept.group].append(concept.local_name)

    for cat in CATEGORIES:
        if not grp_by_cat[cat.local_name]:
            errors.append(f"Category {cat.local_name} has no groups")

    for grp in GROUPS:
        if not leaf_by_grp[grp.local_name]:
            errors.append(f"Group {grp.local_name} has no leaves")


def _check_v1_migration(errors: list[str]) -> None:
    leaf_notations = {c.notation for c in CONCEPTS}
    for old, new in NOTATION_V1_TO_V2.items():
        if new not in leaf_notations:
            errors.append(f"NOTATION_V1_TO_V2[{old}] maps to unknown leaf notation {new}")


def main() -> None:
    errors: list[str] = []

    if len(CONCEPTS) != EXPECTED_LEAF_COUNT:
        errors.append(f"Expected {EXPECTED_LEAF_COUNT} leaf concepts, got {len(CONCEPTS)}")

    _check_hierarchy(errors)
    _check_unique_pref_labels(errors)
    _check_v1_migration(errors)

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

    print(
        f"OK: {len(CONCEPTS)} leaf concepts, {len(GROUPS)} groups, "
        f"{len(CATEGORIES)} categories; mappings and enum aligned"
    )


if __name__ == "__main__":
    main()
