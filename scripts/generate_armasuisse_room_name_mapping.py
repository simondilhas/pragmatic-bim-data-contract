#!/usr/bin/env python3
"""Generate armasuisse room name to abstract room name mapping TTL."""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from room_name_data import CONCEPTS, RN_NS, ttl_escape  # noqa: E402

DEFAULT_INNEN = Path("/home/simondilhas/Programming/elementplan/arma-elementplan-data/values/raumliste-innen.yaml")
DEFAULT_AUSSEN = Path("/home/simondilhas/Programming/elementplan/arma-elementplan-data/values/raumliste-aussen.yaml")
OUT_PATH = REPO_ROOT / "classification/mapping/armasuisse-room-name-to-abstract-room-name.mapping.ttl"

SANITARY_SUFFIXES = (
    " mit Sanitäreinrichtung",
    " mit Sanitäreinrichtungen",
    " mit Sanitaereinrichtung",
)

# Manual overrides: armasuisse label (base, after sanitary strip) -> abstract notation.
MANUAL_OVERRIDES: dict[str, str] = {
    "Büroräume": "RN-WRK-OFF",
    "Büroräume Verwaltung": "RN-WRK-ADM",
    "Büroräume Profi (Kdo)": "RN-WRK-MNG",
    "Büroräume Miliz (Kp)": "RN-WRK-OFF",
    "Grossraumbüro": "RN-WRK-OPN",
    "Besprechungsraum": "RN-WRK-MTG",
    "Besprechungsräume": "RN-WRK-MTG",
    "Konferenzraum": "RN-WRK-CNF",
    "Küche": "RN-RES-KIT",
    "Küchen": "RN-RES-KIT",
    "Produktionsküchen": "RN-RES-KIT",
    "Waschküche": "RN-RES-LAU",
    "Badezimmer": "RN-RES-BTH",
    "Schlafraum Mannschaft": "RN-RES-BED",
    "Schlafraum Offiziere": "RN-RES-BED",
    "Schlafraum Kdt": "RN-RES-BED",
    "Schlafraum Unteroffiziere": "RN-RES-BED",
    "Schlafraum Berufspiloten": "RN-RES-BED",
    "Wohnräume (Schlafräume)": "RN-RES-BED",
    "Zelle": "RN-RES-BED",
    "Treppen": "RN-CIR-STR",
    "Flur/Halle/Korridore": "RN-CIR-COR",
    "Eingangshalle": "RN-CIR-LOB",
    "Eingangshalle Kunden": "RN-CIR-LOB",
    "Vorraum": "RN-CIR-VES",
    "Aufzugs- und Förderanlagen": "RN-CIR-ELV",
    "Duschenraum": "RN-HYG-SHW",
    "Gemeinschaftsräume": "RN-WRK-BRK",
    "Cafeteria": "RN-COM-CAF",
    "Kiosk": "RN-COM-KSK",
    "Bibliotheksräume": "RN-LRN-LIB",
    "Leseraum": "RN-LRN-STU",
    "Film- und Hörsäle": "RN-LRN-LCT",
    "Allgemeine Unterrichts- und Übungsräume ohne festes Gestühl": "RN-LRN-CLS",
    "Besondere Unterrichts- und Übungsräume ohne festes Gestühl": "RN-LRN-SEM",
    "Sporthalle": "RN-LRN-AUS",
    "Kraft-/Fitnessraum": "RN-LRN-WRK",
    "Werkstätten": "RN-IND-WRK",
    "Werkhallen": "RN-IND-PRD",
    "Ausbildungshallen": "RN-IND-PRD",
    "Halle mit Hochregallager": "RN-IND-WHS",
    "Archive/Sammlungsräume": "RN-STO-ARC",
    "Archivraum": "RN-STO-ARC",
    "Abstellraum/Hausdienst": "RN-STO-JAN",
    "Elektrische Stromversorgung": "RN-TEC-ELC",
    "Heiz- u. Brauchwassererwärmung": "RN-TEC-BOI",
    "Warmwasserversorgung": "RN-TEC-PMP",
    "Betriebstechnische Anlagen": "RN-TEC-HVC",
    "Bürotechnik/Rechenzentrum": "RN-TEC-SRV",
    "Bürotechnik": "RN-TEC-COM",
    "Fahrzeugabstellfläche": "RN-VOI-PRK",
    "Fahrzeugverkehrsfläche": "RN-VOI-PRK",
    "Konstruktionsraum": "RN-VOI-STR",
    "Luftraum": "RN-VOI-AIR",
    "Raum für operative Eingriffe": "RN-HLC-OR",
    "Raum mit allgemeiner medizinischer Ausstattung": "RN-HLC-TRT",
    "Raum mit besonderer medizinischer Ausstattung": "RN-HLC-PRM",
    "Bettenraum mit allgemeiner Ausstattung": "RN-HLC-PAT",
    "Bettenraum mit besonderer Ausstattung": "RN-HLC-PAT",
    "Behandlungsräume": "RN-HLC-TRT",
    "Chemisches/bakteriologisches Labor": "RN-LRN-SCI",
    "Physikalisches/technisches Labor": "RN-LRN-SCI",
    "Technologisches Labor": "RN-LRN-SCI",
    "Ausstellungsräume": "RN-COM-EXH",
    "Balkon": "RN-OUT-BLN",
    "Terrasse": "RN-OUT-TRR",
    "Gartenanlage": "RN-OUT-GDN",
    "Aussenanlagen Sport": "RN-OUT-PLY",
    "Wasserbecken": "RN-OUT-SPL",
    "Strasse/Weg": "RN-OUT-CWK",
    "Sonstige Nutzung allgemein": "RN-WRK-OAD",
}

KEYWORD_RULES: list[tuple[str, str]] = [
    (r"\bwc\b|toilette|sanitär|klosett", "RN-HYG-WC-MIX"),
    (r"dusch|umkleid", "RN-HYG-SHW"),
    (r"garderobe|cloak", "RN-HYG-GRD"),
    (r"schliessfach|locker", "RN-HYG-LCK"),
    (r"büro|office", "RN-WRK-OFF"),
    (r"besprech|meeting", "RN-WRK-MTG"),
    (r"konferenz|conference", "RN-WRK-CNF"),
    (r"korridor|flur|gang\b|corridor", "RN-CIR-COR"),
    (r"trepp|stair", "RN-CIR-STR"),
    (r"aufzug|lift|förder", "RN-CIR-ELV"),
    (r"werkstatt|workshop", "RN-IND-WRK"),
    (r"lager|storage|archiv", "RN-STO-GEN"),
    (r"labor", "RN-LRN-SCI"),
    (r"klassenzimmer|classroom|unterricht", "RN-LRN-CLS"),
    (r"hörsaal|lecture", "RN-LRN-LCT"),
    (r"bibliothek|library", "RN-LRN-LIB"),
    (r"küche|kitchen", "RN-RES-KIT"),
    (r"schlaf|bedroom|zimmer\b", "RN-RES-BED"),
    (r"patient|betten", "RN-HLC-PAT"),
    (r"elektr|strom", "RN-TEC-ELC"),
    (r"heiz|boiler|wärme", "RN-TEC-BOI"),
    (r"server|rechenzentrum|it-raum", "RN-TEC-SRV"),
    (r"parkier|garage|stellplatz", "RN-VOI-PRK"),
    (r"schacht|shaft|steig", "RN-VOI-SHA"),
    (r"balkon|balcon", "RN-OUT-BLN"),
    (r"terrasse|terrace", "RN-OUT-TRR"),
    (r"garten|garden", "RN-OUT-GDN"),
]

MILITARY_PATTERNS = (
    r"\bIh\b",
    r"\bFlz\b",
    r"\bFz\b",
    r"\bKdt\b",
    r"\bVpf\b",
    r"\bMiliz\b",
    r"\bOffizier",
    r"\bMannschaft",
    r"\bSchiess",
    r"\bPilot",
    r"\bCUA\b",
    r"\bRIGA\b",
    r"\bWache\b",
    r"\bTrp\b",
)


def strip_sanitary(label: str) -> str:
    for suffix in SANITARY_SUFFIXES:
        if label.endswith(suffix):
            return label[: -len(suffix)]
    return label


def normalize_label(label: str) -> str:
    return unicodedata.normalize("NFKC", label).strip()


def is_military_specific(label: str) -> bool:
    return any(re.search(pattern, label, re.IGNORECASE) for pattern in MILITARY_PATTERNS)


def notation_to_local(notation: str) -> str:
    return notation.replace("-", "_")


def load_labels(path: Path) -> list[str]:
    if not path.is_file():
        return []
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return list(data.get("values", {}).get("de") or [])


def resolve_label(label: str) -> str | None:
    base = strip_sanitary(normalize_label(label))
    if is_military_specific(base):
        return None
    if base in MANUAL_OVERRIDES:
        return MANUAL_OVERRIDES[base]
    lowered = base.lower()
    for pattern, notation in KEYWORD_RULES:
        if re.search(pattern, lowered):
            return notation
    return None


def render_ttl(innen_path: Path, aussen_path: Path) -> str:
    known_locals = {c.local_name for c in CONCEPTS}
    lines = [
        f"@prefix rn: <{RN_NS}> .",
        "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .",
        "@prefix dcterms: <http://purl.org/dc/terms/> .",
        "@prefix arma: <https://example.org/ch/armasuisse/value/> .",
        "@prefix map: <https://example.org/mapping/> .",
        "",
        "map:armasuisseRoomNameToAbstractRoomNameMapping a dcterms:Dataset ;",
        '  dcterms:title "armasuisse room name to abstract room name mapping"@en ;',
        '  dcterms:title "Mapping armasuisse Raumbezeichnungen zu abstrakten Raumnamen"@de ;',
        "  dcterms:references rn:scheme ;",
        '  dcterms:description "Maps armasuisse Raumliste labels to abstract BuildingSpaceNameClassification concepts. Military-specific labels are intentionally unmapped. Regenerate with scripts/generate_armasuisse_room_name_mapping.py."@en ;',
        '  dcterms:description "Ordnet armasuisse-Raumlistenbezeichnungen abstrakten BuildingSpaceNameClassification-Konzepten zu. Militaerspezifische Bezeichnungen bleiben absichtlich ungemappt. Regenerieren mit scripts/generate_armasuisse_room_name_mapping.py."@de .',
        "",
    ]

    seen: set[str] = set()
    mapped = 0
    unmapped: list[str] = []
    for source_id, path in (("raumliste-innen", innen_path), ("raumliste-aussen", aussen_path)):
        source_key = source_id.replace("-", "_")
        for label in load_labels(path):
            notation = resolve_label(label)
            if notation is None:
                unmapped.append(label)
                continue
            local = notation_to_local(notation)
            if local not in known_locals:
                unmapped.append(label)
                continue
            normalized = strip_sanitary(normalize_label(label))
            if normalized in seen:
                continue
            seen.add(normalized)
            slug = re.sub(r"[^a-zA-Z0-9]+", "_", normalized).strip("_").lower()
            if not slug:
                slug = "entry"
            lines.append(
                f'arma:{source_key}_{slug} skos:closeMatch rn:{local} ;'
                f'\n  skos:prefLabel "{ttl_escape(normalized)}"@de .'
            )
            mapped += 1

    lines.extend(
        [
            "",
            f"# mapped={mapped} unmapped={len(unmapped)}",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--innen", type=Path, default=DEFAULT_INNEN)
    parser.add_argument("--aussen", type=Path, default=DEFAULT_AUSSEN)
    parser.add_argument("--out", type=Path, default=OUT_PATH)
    args = parser.parse_args()
    args.out.write_text(render_ttl(args.innen, args.aussen), encoding="utf-8")
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
