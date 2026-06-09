#!/usr/bin/env python3
"""Generate SKOS TTL for the KBOB/IPB Dokumenttypenkatalog (Anhang C, 2016) from the source PDF."""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

import fitz

REPO_ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = REPO_ROOT / "classification/mapping/20171024_KBOB-IPB_Anhang_C_-_Dokumenttypenkatalog_2016_DE.pdf"
OUT_PATH = REPO_ROOT / "classification/mapping/kbob-document-type-catalog-2016.skos.ttl"

DESC_STARTERS = (
    "Das ",
    "Der ",
    "Die ",
    "Den ",
    "Dem ",
    "Des ",
    "Ein ",
    "Eine ",
    "Einer ",
    "Einem ",
    "Beinhaltet ",
    "Beschreibt ",
    "Beschreibung ",
    "Verzeichnis ",
    "Grafische ",
    "Konzept ",
    "Konzept zum ",
    "Konzept über ",
    "Konzept für ",
    "Regelt ",
    "Auflistung ",
    "Darstellung ",
    "Organisation der ",
    "Organisation ",
    "Registration ",
    "Liste ",
    "Matrix ",
    "Visualisiert ",
    "Stellt ",
    "Dient ",
    "Festhalten ",
    "Dokumentation ",
    "Nachweis ",
    "Schriftliche ",
    "Unterzeichnete ",
    "Bestätigung ",
    "Zusammenstellung ",
    "Antrag ",
    "Anträge ",
    "Bewilligung ",
    "Vereinbarung ",
    "Protokoll ",
    "Angaben ",
    "Kurze ",
    "Weitere ",
    "Globaler ",
    "Neutraler ",
    "Allgemeiner ",
    "Spezifisches ",
    "Spezifische ",
    "Einfacher ",
    "Detaillierte ",
    "Schritt ",
    "In der ",
    "Im ",
    "In ",
    "Auf ",
    "Aufstellung ",
    "Bericht ",
    "Gutachten/",
    "Gutachten ",
    "Studie ",
    "Schätzung ",
    "Gesetzlich ",
    "Versicherung ",
    "Abschrift ",
    "Auszug ",
    "Aus der ",
    "Programm ",
    "Legt ",
    "Bestimmt ",
    "Verfeinert ",
    "Übersicht ",
    "Berechnung ",
    "Prüfung ",
    "Vergleiche ",
    "Informationen ",
    "Sammlung ",
    "Chronologische ",
    "Kopie ",
    "Mitteilung ",
    "Aufforderung ",
    "Planer ",
    "Qualitätsprüfprotokoll ",
    "Automatische ",
    "Offizielle ",
    "Simulation ",
    "Simulation von ",
    "Von ",
    "Wird ",
    "Unter ",
    "Auch ",
    "Nur ",
    "Fristgerecht ",
)

SKIP_SUBSTR = (
    "DTC ",
    "Dokumenttyp",
    "nach BDM15",
    "QUALITÄT",
    "Phase ",
    "Projektdokumentation",
    "Objektdokumentation",
    "Prozessdokumentation",
    "Fachdokumentation",
    "Anlagedokumentation",
    "Office-Format",
    "CAD-Richtlinie",
    "CAFM-Richtlinie",
    "BIM-Richtlinie",
    "keine Aufbewahrung",
    "Aufbewahrung",
    "SIA-PHASEN",
    "DOKUMENTATION",
    "DATEIFORMAT",
    "X X X",
    "Unter Mitwirkung",
    "Version 2016",
    "Dokumenttypenkatalog",
    "bis Ersatz",
    "bis Bearbeitungszweck",
    "entfällt",
    "PDF-A",
    "andere",
    "DWG",
    "Jahre",
)

MARKER_SUFFIX_RE = re.compile(r"\s+(?:x|IFC|[A-Z])(?:\s+(?:x|IFC|[A-Z]))*\s*$")
CODE_RE = re.compile(r"^([A-Z]\d{0,5})\s+(.+)$")


def strip_table_markers(text: str) -> str:
    text = re.sub(r"\s+x(\s+x)+\s*$", "", text).strip()
    return MARKER_SUFFIX_RE.sub("", text).strip()


def parse_pdf(path: Path) -> tuple[dict[str, dict[str, str]], list[str]]:
    doc = fitz.open(path)
    rows: list[str] = []
    for page in doc:
        words = page.get_text("words")
        by_y: dict[float, list[tuple[float, str]]] = defaultdict(list)
        for w in words:
            by_y[round(w[1], 0)].append((w[0], w[4]))
        for y in sorted(by_y):
            line = strip_table_markers(" ".join(t for _, t in sorted(by_y[y])))
            if not line or line.startswith("Bauwerksdokumentation") or "Copyright 2016" in line:
                continue
            if any(skip in line for skip in SKIP_SUBSTR):
                continue
            rows.append(line)

    entries: dict[str, dict[str, str]] = {}
    order: list[str] = []
    for line in rows:
        m = CODE_RE.match(line)
        if not m:
            continue
        code, rest = m.group(1), m.group(2).strip()
        if len(code) == 1:
            if code not in entries:
                entries[code] = {"code": code, "name": rest, "desc": ""}
                order.append(code)
            continue

        desc = ""
        name = rest
        for starter in DESC_STARTERS:
            idx = rest.find(starter)
            if idx > 0:
                name, desc = rest[:idx].strip(), rest[idx:].strip()
                break
        if not desc and len(code) >= 5 and " " in rest:
            name, desc = rest.split(" ", 1)
        if code not in entries:
            entries[code] = {"code": code, "name": name, "desc": desc}
            order.append(code)
    return entries, order


def parent_code(code: str, all_codes: set[str]) -> str | None:
    if len(code) == 1:
        return None
    best: str | None = None
    for other in all_codes:
        if other != code and code.startswith(other):
            if best is None or len(other) > len(best):
                best = other
    return best


def ttl_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").strip()


def iri_for(code: str) -> str:
    return f":{code}"


def render_ttl(entries: dict[str, dict[str, str]], order: list[str], pdf_path: Path) -> str:
    codes = set(entries)
    parents = {code: parent_code(code, codes) for code in codes}
    children: dict[str, list[str]] = defaultdict(list)
    for code, parent in parents.items():
        if parent:
            children[parent].append(code)

    top_codes = [code for code in order if len(code) == 1]
    lines: list[str] = [
        "@prefix : <https://example.org/ch/kbob-dtc/> .",
        "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .",
        "@prefix dcterms: <http://purl.org/dc/terms/> .",
        "",
        ":scheme a skos:ConceptScheme ;",
        '  skos:prefLabel "KBOB/IPB Dokumenttypenkatalog"@de ;',
        '  skos:prefLabel "KBOB/IPB document type catalog"@en ;',
        '  dcterms:title "KBOB/IPB Dokumenttypenkatalog (Anhang C)"@de ;',
        '  dcterms:identifier "KBOBDocumentTypeCatalog2016" ;',
        '  dcterms:creator "KBOB/IPB" ;',
        '  dcterms:issued "2016-01" ;',
        f'  dcterms:source "{pdf_path.name}" ;',
        '  skos:definition "Dokumenttypenkatalog gemaess BDM15 / Anhang C des KBOB/IPB Dokumentationsmodells BWD (Version 2016-01)."@de ;',
        '  skos:definition "Document type catalog per BDM15 / Annex C of the KBOB/IPB building documentation model BWD (version 2016-01)."@en ;',
        "  skos:hasTopConcept " + ", ".join(iri_for(code) for code in top_codes) + " .",
        "",
    ]

    for code in order:
        entry = entries[code]
        kids = sorted(children.get(code, []), key=lambda item: (len(item), item))
        lines.append(f"{iri_for(code)} a skos:Concept ;")
        lines.append("  skos:inScheme :scheme ;")
        if len(code) == 1:
            lines.append("  skos:topConceptOf :scheme ;")
        if parents[code]:
            lines.append(f"  skos:broader {iri_for(parents[code])} ;")
        lines.append(f'  skos:notation "{ttl_escape(code)}" ;')
        lines.append(f'  skos:prefLabel "{ttl_escape(entry["name"])}"@de ;')
        if entry["desc"]:
            lines.append(f'  skos:definition "{ttl_escape(entry["desc"])}"@de ;')
        if kids:
            lines.append("  skos:narrower " + ", ".join(iri_for(kid) for kid in kids) + " ;")
        lines[-1] = lines[-1].rstrip(" ;") + " ."
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    entries, order = parse_pdf(PDF_PATH)
    OUT_PATH.write_text(render_ttl(entries, order, PDF_PATH), encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({len(entries)} concepts)")


if __name__ == "__main__":
    main()
