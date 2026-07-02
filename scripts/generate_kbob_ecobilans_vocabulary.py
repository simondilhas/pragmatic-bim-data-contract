#!/usr/bin/env python3
"""Generate KBOB ecobilans Baumaterialien SKOS TTL and LCA factors JSON from the source Excel."""

from __future__ import annotations

import json
import re
from pathlib import Path

import openpyxl

REPO_ROOT = Path(__file__).resolve().parents[1]
XLSX_PATH = (
    REPO_ROOT
    / "classification/Oekobilanzdaten_ Baubereich_Donne_ecobilans_construction_2009-1-2022_v8.02.xlsx"
)
TTL_PATH = REPO_ROOT / "classification/mapping/kbob-ecobilans-baumat.skos.ttl"
JSON_PATH = REPO_ROOT / "classification/mapping/kbob-ecobilans-lca-factors.json"

ID_PATTERN = re.compile(r"^\d{2}\.\d{3}$")

COL_ID = 0
COL_UUID = 1
COL_LABEL_DE = 2
COL_DENSITY = 5
COL_REF_UNIT = 6
COL_UBP_TOTAL = 7
COL_PE_TOTAL = 10
COL_PE_NR_TOTAL = 20
COL_GWP_TOTAL = 25
COL_GWP_MFG = 26
COL_GWP_DISP = 27
COL_LABEL_FR = 29


def ttl_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").strip()


def iri_local(kbob_id: str) -> str:
    return kbob_id.replace(".", "_")


def parse_float(value: object) -> float | None:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip()
    if not text or text == "-":
        return None
    try:
        return float(text.replace(",", "."))
    except ValueError:
        return None


def load_rows() -> list[dict[str, object]]:
    wb = openpyxl.load_workbook(XLSX_PATH, read_only=True, data_only=True)
    ws = wb["Baumaterialien Matériaux"]
    rows: list[dict[str, object]] = []
    for row in ws.iter_rows(min_row=10, values_only=True):
        kbob_id = row[COL_ID]
        if kbob_id is None:
            continue
        kbob_id_str = str(kbob_id).strip()
        if not ID_PATTERN.match(kbob_id_str):
            continue
        label_de = row[COL_LABEL_DE]
        if label_de is None:
            continue
        rows.append(
            {
                "id": kbob_id_str,
                "uuid": str(row[COL_UUID]).strip() if row[COL_UUID] else None,
                "label_de": str(label_de).strip(),
                "label_fr": str(row[COL_LABEL_FR]).strip() if row[COL_LABEL_FR] else None,
                "ref_unit": str(row[COL_REF_UNIT]).strip() if row[COL_REF_UNIT] else None,
                "density": parse_float(row[COL_DENSITY]),
                "ubp_total": parse_float(row[COL_UBP_TOTAL]),
                "pe_total_kwh_oil_eq": parse_float(row[COL_PE_TOTAL]),
                "pe_nr_total_kwh_oil_eq": parse_float(row[COL_PE_NR_TOTAL]),
                "gwp_total_kg_co2eq": parse_float(row[COL_GWP_TOTAL]),
                "gwp_mfg_kg_co2eq": parse_float(row[COL_GWP_MFG]),
                "gwp_disp_kg_co2eq": parse_float(row[COL_GWP_DISP]),
            }
        )
    return rows


def group_code(kbob_id: str) -> str:
    return kbob_id.split(".", 1)[0]


def render_ttl(rows: list[dict[str, object]]) -> str:
    groups: dict[str, list[str]] = {}
    for row in rows:
        groups.setdefault(group_code(row["id"]), []).append(row["id"])

    top_groups = sorted(groups)
    lines = [
        "@prefix : <https://example.org/ch/kbob/ecobilans/baumat/2009-1-2022/> .",
        "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .",
        "@prefix dcterms: <http://purl.org/dc/terms/> .",
        "",
        ":scheme a skos:ConceptScheme ;",
        '  skos:prefLabel "KBOB ecobilans construction materials"@en ;',
        '  skos:prefLabel "KBOB Oekobilanzdaten Baumaterialien"@de ;',
        '  dcterms:title "KBOB / ecobau / IPB 2009/1:2022 Baumaterialien"@en ;',
        '  dcterms:identifier "KBOBEcobilansBaumat2009-1-2022" ;',
        '  dcterms:creator "KBOB / ecobau / IPB" ;',
        '  dcterms:issued "2022" ;',
        f'  dcterms:source "{XLSX_PATH.name}" ;',
        '  skos:definition "Life-cycle inventory indicators for construction materials from KBOB ecobilans dataset version 8.02. Leaf concepts correspond to Baumaterialien rows; group headers are broader concepts by ID prefix."@en ;',
        '  skos:definition "Oekobilanz-Kennwerte fuer Baumaterialien aus dem KBOB-Oekobilanzdatensatz Version 8.02. Blattkonzepte entsprechen Baumaterialien-Zeilen; Gruppenkoepfe sind broader-Konzepte nach ID-Praefix."@de ;',
        "  skos:hasTopConcept "
        + ", ".join(f":G_{code}" for code in top_groups)
        + " .",
        "",
    ]

    for group in top_groups:
        child_ids = sorted(groups[group])
        lines.extend(
            [
                f":G_{group} a skos:Concept ;",
                "  skos:inScheme :scheme ;",
                "  skos:topConceptOf :scheme ;",
                f'  skos:notation "G-{group}" ;',
                f'  skos:prefLabel "KBOB group {group}"@en ;',
                f'  skos:prefLabel "KBOB Gruppe {group}"@de ;',
                "  skos:narrower "
                + ", ".join(f":{iri_local(item)}" for item in child_ids)
                + " ;",
            ]
        )
        lines[-1] = lines[-1].rstrip(" ;") + " ."
        lines.append("")

    for row in rows:
        local = iri_local(row["id"])
        lines.append(f":{local} a skos:Concept ;")
        lines.append("  skos:inScheme :scheme ;")
        lines.append(f"  skos:broader :G_{group_code(row['id'])} ;")
        lines.append(f'  skos:notation "{ttl_escape(row["id"])}" ;')
        lines.append(f'  skos:prefLabel "{ttl_escape(row["label_de"])}"@de ;')
        if row.get("label_fr"):
            lines.append(f'  skos:prefLabel "{ttl_escape(str(row["label_fr"]))}"@fr ;')
        if row.get("ref_unit"):
            lines.append(f'  dcterms:extent "{ttl_escape(str(row["ref_unit"]))}" ;')
        if row.get("uuid"):
            lines.append(f'  dcterms:identifier "{ttl_escape(str(row["uuid"]))}" ;')
        lines[-1] = lines[-1].rstrip(" ;") + " ."
        lines.append("")

    return "\n".join(lines)


def render_json(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "source": XLSX_PATH.name,
        "version": "8.02",
        "scheme": "https://example.org/ch/kbob/ecobilans/baumat/2009-1-2022/scheme",
        "factors": {
            f"https://example.org/ch/kbob/ecobilans/baumat/2009-1-2022/{iri_local(row['id'])}": {
                "id": row["id"],
                "uuid": row["uuid"],
                "ref_unit": row["ref_unit"],
                "density": row["density"],
                "ubp_total": row["ubp_total"],
                "pe_total_kwh_oil_eq": row["pe_total_kwh_oil_eq"],
                "pe_nr_total_kwh_oil_eq": row["pe_nr_total_kwh_oil_eq"],
                "gwp_total_kg_co2eq": row["gwp_total_kg_co2eq"],
                "gwp_mfg_kg_co2eq": row["gwp_mfg_kg_co2eq"],
                "gwp_disp_kg_co2eq": row["gwp_disp_kg_co2eq"],
            }
            for row in rows
        },
    }


def main() -> None:
    rows = load_rows()
    TTL_PATH.write_text(render_ttl(rows), encoding="utf-8")
    JSON_PATH.write_text(json.dumps(render_json(rows), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {TTL_PATH} ({len(rows)} leaf concepts)")
    print(f"Wrote {JSON_PATH}")


if __name__ == "__main__":
    main()
