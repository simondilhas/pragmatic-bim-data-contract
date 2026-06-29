#!/usr/bin/env python3
"""Generate room name SKOS vocabulary, activity mapping, and SpaceNameType enum."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from room_name_data import (  # noqa: E402
    ABS_NS,
    CATEGORIES,
    CONCEPTS,
    RN_NS,
    RoomNameCategory,
    RoomNameConcept,
    activity_local_name,
    enum_key_from_notation,
    ttl_escape,
)

SKOS_OUT = REPO_ROOT / "classification/abstract-room-name-classification/building-space-name-classification.skos.ttl"
MAPPING_OUT = REPO_ROOT / "classification/mapping/abstract-room-name-to-space-activity.mapping.ttl"
ENUM_PATH = REPO_ROOT / "contract/entity_schema_enums.yaml"


def category_by_local(name: str) -> RoomNameCategory:
    for cat in CATEGORIES:
        if cat.local_name == name:
            return cat
    raise KeyError(name)


def concepts_for_category(local_name: str) -> list[RoomNameConcept]:
    return [c for c in CONCEPTS if c.category == local_name]


def render_skos() -> str:
    lines = [
        f"@prefix : <{RN_NS}> .",
        "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .",
        "@prefix dcterms: <http://purl.org/dc/terms/> .",
        "",
        ":scheme a skos:ConceptScheme ;",
        '  skos:prefLabel "Building Space Name Classification"@en ;',
        '  skos:prefLabel "Gebaeude-Raumbezeichnungsklassifikation"@de ;',
        '  dcterms:title "Building Space Name Classification"@en ;',
        '  dcterms:identifier "BuildingSpaceNameClassification" ;',
        '  dcterms:creator "abstract" ;',
        '  dcterms:issued "2026-06-29" ;',
        '  dcterms:license <https://creativecommons.org/licenses/by/4.0/> ;',
        '  dcterms:source <https://github.com/simondilhas/pragmatic-bim-public-rules> ;',
        '  skos:definition "Normalized abstract room name types for general building use on IfcSpace."@en ;',
        '  skos:definition "Normalisierte abstrakte Raumbezeichnungen fuer allgemeinen Gebaeudegebrauch auf IfcSpace."@de ;',
        "  skos:hasTopConcept " + ", ".join(f":{c.local_name}" for c in CATEGORIES) + " .",
        "",
    ]

    for cat in CATEGORIES:
        leaves = concepts_for_category(cat.local_name)
        lines.extend(
            [
                f":{cat.local_name} a skos:Concept ;",
                "  skos:inScheme :scheme ;",
                "  skos:topConceptOf :scheme ;",
                f'  skos:notation "{cat.notation}" ;',
                f'  skos:prefLabel "{ttl_escape(cat.label_en)}"@en ;',
                f'  skos:prefLabel "{ttl_escape(cat.label_de)}"@de ;',
                f'  skos:definition "{ttl_escape(cat.definition_en)}"@en ;',
                f'  skos:definition "{ttl_escape(cat.definition_de)}"@de ;',
                "  skos:narrower "
                + ", ".join(f":{leaf.local_name}" for leaf in leaves)
                + " ;",
                '  dcterms:subject "IfcSpace" ;',
                f'  dcterms:identifier "{cat.notation}" .',
                "",
            ]
        )

    for concept in CONCEPTS:
        cat = category_by_local(concept.category)
        lines.extend(
            [
                f":{concept.local_name} a skos:Concept ;",
                "  skos:inScheme :scheme ;",
                f'  skos:notation "{concept.notation}" ;',
                f'  skos:prefLabel "{ttl_escape(concept.label_en)}"@en ;',
                f'  skos:prefLabel "{ttl_escape(concept.label_de)}"@de ;',
                f'  skos:definition "{ttl_escape(concept.definition_en)}"@en ;',
                f'  skos:definition "{ttl_escape(concept.definition_de)}"@de ;',
                f"  skos:broader :{cat.local_name} ;",
                '  dcterms:subject "IfcSpace" ;',
                f'  dcterms:identifier "{concept.notation}" .',
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


def render_activity_mapping() -> str:
    lines = [
        f"@prefix rn: <{RN_NS}> .",
        f"@prefix abs: <{ABS_NS}> .",
        "@prefix dcterms: <http://purl.org/dc/terms/> .",
        "@prefix ex: <https://example.org/mapping/> .",
        "",
        "ex:roomNameToSpaceActivityMapping a dcterms:Dataset ;",
        '  dcterms:title "Abstract room name to space activity mapping"@en ;',
        '  dcterms:title "Mapping abstrakter Raumbezeichnungen zur Raumaktivitaetsklassifikation"@de ;',
        "  dcterms:references rn:scheme, abs:scheme ;",
        '  dcterms:description "Maps each normalized room name to one or more building space activity classes. Primary activity code is listed first. Regenerate with scripts/generate_room_name_vocabulary.py."@en ;',
        '  dcterms:description "Ordnet jede normalisierte Raumbezeichnung einer oder mehreren Raumaktivitaetsklassen zu. Der primaere Aktivitaetscode steht zuerst. Regenerieren mit scripts/generate_room_name_vocabulary.py."@de .',
        "",
    ]

    for concept in CONCEPTS:
        targets = ", ".join(f"abs:{activity_local_name(code)}" for code in concept.activity_codes)
        lines.append(f"rn:{concept.local_name} ex:mapsToActivity {targets} .")

    return "\n".join(lines).rstrip() + "\n"


def render_enum_block() -> str:
    lines = [
        "  SpaceNameType:",
        "    enum_uri: pbs:SpaceNameType",
        "    description: Normalized abstract room name type for IfcSpace; finer-grained than space activity classification.",
        "    permissible_values:",
    ]
    for concept in CONCEPTS:
        key = enum_key_from_notation(concept.notation)
        meaning = f"{RN_NS}{concept.local_name}"
        lines.extend(
            [
                f"      {key}:",
                f'        description: "{ttl_escape(concept.definition_en)}"',
                f"        meaning: {meaning}",
                f"        title: {concept.label_en}",
                "        alt_descriptions:",
                "          de:",
                "            source: de",
                f"            description: {concept.label_de}",
            ]
        )
    return "\n".join(lines) + "\n"


def patch_enum_yaml() -> None:
    text = ENUM_PATH.read_text(encoding="utf-8")
    text = re.sub(
        r"\n  SpaceNameType:.*?(?=\n  SystemDiscipline:)",
        "",
        text,
        flags=re.DOTALL,
    )
    marker = "  SystemDiscipline:"
    if marker not in text:
        raise RuntimeError(f"Could not find {marker.strip()} in {ENUM_PATH}")
    before, after = text.split(marker, 1)
    ENUM_PATH.write_text(before + render_enum_block() + marker + after, encoding="utf-8")


def main() -> None:
    SKOS_OUT.parent.mkdir(parents=True, exist_ok=True)
    SKOS_OUT.write_text(render_skos(), encoding="utf-8")
    MAPPING_OUT.write_text(render_activity_mapping(), encoding="utf-8")
    patch_enum_yaml()
    print(f"Wrote {SKOS_OUT} ({len(CONCEPTS)} leaf concepts, {len(CATEGORIES)} categories)")
    print(f"Wrote {MAPPING_OUT}")
    print(f"Patched {ENUM_PATH} SpaceNameType enum")


if __name__ == "__main__":
    main()
