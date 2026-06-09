#!/usr/bin/env python3
"""Generate KBOB document types → document function mapping TTL."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from rdflib import Graph, RDF, SKOS, URIRef

REPO_ROOT = Path(__file__).resolve().parents[1]
KBOB_PATH = REPO_ROOT / "classification/mapping/kbob-document-types.skos.ttl"
OUT_PATH = REPO_ROOT / "classification/mapping/kbob-document-types-to-document-function.mapping.ttl"

KBOB_NS = "https://example.org/ch/kbob/document-types/2016/"
DOCFN_NS = "https://example.org/ch/document-function/"

# Longest-prefix wins. Values: (predicate, [docfn local names]).
PREFIX_RULES: dict[str, tuple[str, list[str]]] = {
    # B — Konzepte und Beschriebe
    "B01011": ("closeMatch", ["reg_laws"]),
    "B01012": ("closeMatch", ["reg_norms"]),
    "B01013": ("closeMatch", ["reg_norms"]),
    "B01014": ("closeMatch", ["reg_norms"]),
    "B01": ("closeMatch", ["req_project_briefs"]),
    "B02": ("closeMatch", ["req_project_briefs", "tec_documents"]),
    "B03": ("closeMatch", ["req_functional_specifications"]),
    "B04": ("closeMatch", ["req_project_briefs"]),
    "B05": ("closeMatch", ["tec_documents"]),
    "B06": ("closeMatch", ["tec_documents"]),
    "B07": ("closeMatch", ["reg_compliance_reports", "tec_documents"]),
    "B10": ("closeMatch", ["req_functional_specifications"]),
    "B11": ("closeMatch", ["req_functional_specifications", "tec_documents"]),
    "B12": ("closeMatch", ["req_functional_specifications", "tec_documents"]),
    "B13": ("closeMatch", ["leg_contracts", "reg_cmp_declarations"]),
    "B14": ("closeMatch", ["fin_balance_sheets", "tec_documents"]),
    "B15": ("closeMatch", ["tec_documents"]),
    "B17": ("closeMatch", ["tec_documents", "adm_recaps"]),
    "B18": ("closeMatch", ["tec_manuals"]),
    "B19": ("closeMatch", ["tec_documents"]),
    "B20": ("closeMatch", ["tec_documents"]),
    # K — Verträge und Kosten
    "K01": ("closeMatch", ["fin_balance_sheets"]),
    "K02": ("closeMatch", ["req_tender_documents"]),
    "K03": ("closeMatch", ["leg_contracts"]),
    "K04": ("closeMatch", ["fin_balance_sheets"]),
    "K05": ("closeMatch", ["fin_invoices"]),
    "K06": ("closeMatch", ["fin_invoices", "fin_balance_sheets"]),
    "K07": ("closeMatch", ["leg_contracts"]),
    "K08": ("closeMatch", ["fin_balance_sheets", "tec_documents"]),
    "K09": ("closeMatch", ["leg_contracts"]),
    # O — Organisation
    "O01": ("closeMatch", ["adm_internal_policies"]),
    "O02": ("closeMatch", ["adm_recaps", "adm_meeting_minutes"]),
    "O03001": ("closeMatch", ["tec_manuals"]),
    "O03": ("closeMatch", ["adm_internal_policies"]),
    "O04": ("closeMatch", ["reg_compliance_reports", "adm_internal_policies"]),
    "O05": ("closeMatch", ["adm_internal_policies"]),
    "O06": ("relatedMatch", ["administrative"]),
    "O07": ("closeMatch", ["tec_plans"]),
    "O08": ("relatedMatch", ["administrative"]),
    "O09": ("relatedMatch", ["administrative"]),
    "O10001": ("closeMatch", ["adm_meeting_minutes"]),
    "O10004": ("closeMatch", ["adm_memos"]),
    "O10008": ("closeMatch", ["adm_memos"]),
    "O10009": ("closeMatch", ["adm_memos"]),
    "O10010": ("closeMatch", ["adm_memos"]),
    "O10011": ("closeMatch", ["adm_memos"]),
    "O10012": ("relatedMatch", ["leg_settlement_agreements"]),
    "O10013": ("relatedMatch", ["leg_contracts"]),
    "O10019": ("closeMatch", ["leg_contracts"]),
    "O10020": ("closeMatch", ["adm_memos"]),
    "O10": ("closeMatch", ["adm_meeting_minutes", "adm_memos"]),
    "O11": ("closeMatch", ["fin_receipts"]),
    "O12": ("closeMatch", ["mks_brochures"]),
    "O13": ("closeMatch", ["reg_cmp_filings"]),
    "O14": ("closeMatch", ["reg_cmp_filings"]),
    "O15": ("closeMatch", ["tec_documents", "adm_meeting_minutes"]),
    "O16": ("closeMatch", ["adm_recaps"]),
    # V — Visualisierungen
    "V02011": ("closeMatch", ["tec_schematics"]),
    "V08024": ("closeMatch", ["tec_schematics"]),
    "V08": ("closeMatch", ["tec_plans", "tec_schematics"]),
    "V07": ("closeMatch", ["tec_plans"]),
    "V01": ("closeMatch", ["tec_plans"]),
    "V02": ("closeMatch", ["tec_plans"]),
    "V03": ("closeMatch", ["tec_plans"]),
    "V04": ("closeMatch", ["tec_plans"]),
    "V05": ("closeMatch", ["tec_plans"]),
    "V06": ("closeMatch", ["tec_plans"]),
    "V09": ("closeMatch", ["tec_plans"]),
    "V10": ("closeMatch", ["tec_plans"]),
    "V11": ("closeMatch", ["tec_plans"]),
    "V": ("closeMatch", ["tec_plans"]),
}

SORTED_PREFIXES = sorted(PREFIX_RULES, key=len, reverse=True)


def rule_for_code(code: str) -> tuple[str, list[str]]:
    for prefix in SORTED_PREFIXES:
        if code.startswith(prefix):
            return PREFIX_RULES[prefix]
    raise KeyError(f"No mapping rule for KBOB code {code}")


def load_leaves() -> list[str]:
    graph = Graph().parse(KBOB_PATH, format="turtle")
    concepts = list(graph.subjects(RDF.type, SKOS.Concept))
    leaves: list[str] = []
    for concept in concepts:
        if list(graph.objects(concept, SKOS.narrower)):
            continue
        notation = next(graph.objects(concept, SKOS.notation), None)
        if notation is None:
            continue
        leaves.append(str(notation))
    return sorted(leaves)


def render_ttl(leaves: list[str]) -> str:
    grouped: dict[tuple[str, tuple[str, ...]], list[str]] = defaultdict(list)
    for code in leaves:
        predicate, targets = rule_for_code(code)
        grouped[(predicate, tuple(targets))].append(code)

    lines = [
        "@prefix kbob: <https://example.org/ch/kbob/document-types/2016/> .",
        "@prefix docfn: <https://example.org/ch/document-function/> .",
        "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .",
        "@prefix dcterms: <http://purl.org/dc/terms/> .",
        "@prefix map: <https://example.org/mapping/> .",
        "",
        "map:kbobDocumentTypesToDocumentFunctionMapping a dcterms:Dataset ;",
        '  dcterms:title "KBOB document types to document function mapping"@en ;',
        '  dcterms:title "Mapping KBOB-Dokumenttypen zur Dokumentfunktion"@de ;',
        '  dcterms:title "Mapping types de documents KBOB vers fonction documentaire"@fr ;',
        "  dcterms:references kbob:scheme, docfn:scheme ;",
        '  dcterms:issued "2026-06-09" ;',
        '  dcterms:description "Maps leaf concepts in the KBOB/IPB document type catalogue (BDM15, Annex C, 2016) to abstract document function classes. Category-prefix rules assign each leaf via longest-prefix match; skos:closeMatch denotes primary functional fit, skos:relatedMatch weaker association. Regenerate with scripts/generate_kbob_to_document_function_mapping.py."@en ;',
        '  dcterms:description "Ordnet Blattkonzepte des KBOB/IPB-Dokumenttypenkatalogs (BDM15, Anhang C, 2016) abstrakten Dokumentfunktionsklassen zu. Kategorie-Praefixregeln weisen jedes Blatt per laengstem Praefix zu; skos:closeMatch fuer primaere Funktion, skos:relatedMatch fuer schwaechere Zuordnung. Regenerieren mit scripts/generate_kbob_to_document_function_mapping.py."@de .',
        "",
    ]

    for (predicate, targets), codes in sorted(grouped.items(), key=lambda item: item[0][1]):
        target_list = ", ".join(f"docfn:{target}" for target in targets)
        lines.append(f"# {codes[0]} … ({len(codes)} leaves) → {', '.join(targets)}")
        for code in codes:
            lines.append(f"kbob:{code} skos:{predicate} {target_list} .")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    leaves = load_leaves()
    OUT_PATH.write_text(render_ttl(leaves), encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({len(leaves)} leaf mappings)")


if __name__ == "__main__":
    main()
