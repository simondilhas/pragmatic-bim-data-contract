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
    GROUPS,
    NOTATION_V1_TO_V2,
    RN_NS,
    RoomNameCategory,
    RoomNameConcept,
    RoomNameGroup,
    activity_local_name,
    enum_key_from_notation,
    ttl_escape,
)

SKOS_OUT = REPO_ROOT / "classification/abstract-room-name-classification/building-space-name-classification.skos.ttl"
MAPPING_OUT = REPO_ROOT / "classification/mapping/abstract-room-name-to-space-activity.mapping.ttl"
MIGRATION_OUT = REPO_ROOT / "classification/mapping/room-name-notation-v1-to-v2.mapping.ttl"
ENUM_PATH = REPO_ROOT / "contract/entity_schema_enums.yaml"


def category_by_local(name: str) -> RoomNameCategory:
    for cat in CATEGORIES:
        if cat.local_name == name:
            return cat
    raise KeyError(name)


def group_by_local(name: str) -> RoomNameGroup:
    for grp in GROUPS:
        if grp.local_name == name:
            return grp
    raise KeyError(name)


def groups_for_category(local_name: str) -> list[RoomNameGroup]:
    return [g for g in GROUPS if g.category == local_name]


def concepts_for_group(local_name: str) -> list[RoomNameConcept]:
    return [c for c in CONCEPTS if c.group == local_name]


def _alt_label_lines(concept: RoomNameConcept) -> list[str]:
    lines: list[str] = []
    for label in concept.alt_labels_en:
        lines.append(f'  skos:altLabel "{ttl_escape(label)}"@en ;')
    for label in concept.alt_labels_de:
        lines.append(f'  skos:altLabel "{ttl_escape(label)}"@de ;')
    return lines


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
        '  dcterms:issued "2026-06-30" ;',
        '  dcterms:license <https://creativecommons.org/licenses/by/4.0/> ;',
        '  dcterms:source <https://github.com/simondilhas/pragmatic-bim-public-rules> ;',
        '  skos:definition "Normalized abstract room name types for general building use on IfcSpace."@en ;',
        '  skos:definition "Normalisierte abstrakte Raumbezeichnungen fuer allgemeinen Gebaeudegebrauch auf IfcSpace."@de ;',
        "  skos:hasTopConcept " + ", ".join(f":{c.local_name}" for c in CATEGORIES) + " .",
        "",
    ]

    for cat in CATEGORIES:
        subgroups = groups_for_category(cat.local_name)
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
                + ", ".join(f":{grp.local_name}" for grp in subgroups)
                + " ;",
                '  dcterms:subject "IfcSpace" ;',
                f'  dcterms:identifier "{cat.notation}" .',
                "",
            ]
        )

    for grp in GROUPS:
        leaves = concepts_for_group(grp.local_name)
        lines.extend(
            [
                f":{grp.local_name} a skos:Concept ;",
                "  skos:inScheme :scheme ;",
                f'  skos:notation "{grp.notation}" ;',
                f'  skos:prefLabel "{ttl_escape(grp.label_en)}"@en ;',
                f'  skos:prefLabel "{ttl_escape(grp.label_de)}"@de ;',
                f'  skos:definition "{ttl_escape(grp.definition_en)}"@en ;',
                f'  skos:definition "{ttl_escape(grp.definition_de)}"@de ;',
                f"  skos:broader :{grp.category} ;",
                "  skos:narrower "
                + ", ".join(f":{leaf.local_name}" for leaf in leaves)
                + " ;",
                '  dcterms:subject "IfcSpace" ;',
                f'  dcterms:identifier "{grp.notation}" .',
                "",
            ]
        )

    for concept in CONCEPTS:
        grp = group_by_local(concept.group)
        block = [
            f":{concept.local_name} a skos:Concept ;",
            "  skos:inScheme :scheme ;",
            f'  skos:notation "{concept.notation}" ;',
            f'  skos:prefLabel "{ttl_escape(concept.label_en)}"@en ;',
            f'  skos:prefLabel "{ttl_escape(concept.label_de)}"@de ;',
            *_alt_label_lines(concept),
            f'  skos:definition "{ttl_escape(concept.definition_en)}"@en ;',
            f'  skos:definition "{ttl_escape(concept.definition_de)}"@de ;',
            f"  skos:broader :{grp.local_name} ;",
            '  dcterms:subject "IfcSpace" ;',
            f'  dcterms:identifier "{concept.notation}" .',
            "",
        ]
        lines.extend(block)

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


def render_notation_migration() -> str:
    notation_to_local = {c.notation: c.local_name for c in CONCEPTS}
    lines = [
        f"@prefix rn: <{RN_NS}> .",
        "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .",
        "@prefix dcterms: <http://purl.org/dc/terms/> .",
        "@prefix ex: <https://example.org/mapping/> .",
        "@prefix v1: <https://example.org/abstract/building-space-name-classification/v1/notation/> .",
        "",
        "ex:roomNameNotationV1ToV2Mapping a dcterms:Dataset ;",
        '  dcterms:title "Room name notation v1 to v2 mapping"@en ;',
        '  dcterms:title "Mapping Raumnamen-Notation v1 nach v2"@de ;',
        "  dcterms:references rn:scheme ;",
        '  dcterms:description "Maps mnemonic v1 notation codes (RN-RES-BED) to numeric v2 leaf codes (RN-01-10-01). RN-CIR-AIS is superseded by RN-03-10-01 (Corridor). Regenerate with scripts/generate_room_name_vocabulary.py."@en ;',
        '  dcterms:description "Ordnet mnemonische v1-Notation (RN-RES-BED) numerischen v2-Blattcodes (RN-01-10-01) zu. RN-CIR-AIS wird durch RN-03-10-01 (Flur) ersetzt. Regenerieren mit scripts/generate_room_name_vocabulary.py."@de .',
        "",
    ]

    for old_notation, new_notation in sorted(NOTATION_V1_TO_V2.items()):
        local = notation_to_local[new_notation]
        slug = old_notation.lower().replace("-", "_")
        lines.append(f"v1:{slug} skos:exactMatch rn:{local} ;")
        lines.append(f'  ex:supersedesNotation "{old_notation}" ;')
        lines.append(f'  ex:mapsToNotation "{new_notation}" .')
        lines.append("")

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
    MIGRATION_OUT.write_text(render_notation_migration(), encoding="utf-8")
    patch_enum_yaml()
    print(
        f"Wrote {SKOS_OUT} ({len(CONCEPTS)} leaf concepts, "
        f"{len(GROUPS)} groups, {len(CATEGORIES)} categories)"
    )
    print(f"Wrote {MAPPING_OUT}")
    print(f"Wrote {MIGRATION_OUT}")
    print(f"Patched {ENUM_PATH} SpaceNameType enum")


if __name__ == "__main__":
    main()
