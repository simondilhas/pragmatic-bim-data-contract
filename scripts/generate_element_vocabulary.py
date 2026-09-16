#!/usr/bin/env python3
"""Generate the Elementplan element vocabulary, member product schemes, and product bridge.

Writes:
  classification/pragmaticbim-elementplan-classification/elementplan-elements.skos.ttl
  classification/abstract-member-product-classification/*-products.skos.ttl
  classification/mapping/elementplan-elements-to-products.mapping.ttl
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from element_data import (  # noqa: E402
    COUNT_QUANTITY,
    CREATOR,
    EL_NS,
    ELEMENTS,
    ISSUED,
    LICENSE,
    PRODUCT_SCHEMES,
    SOURCE,
    elements_with_products,
    scheme_for,
    ttl_escape,
    used_scheme_prefixes,
)
from member_product_data import SCHEMES, MemberProductScheme  # noqa: E402

ELEMENT_OUT = (
    REPO_ROOT
    / "classification/pragmaticbim-elementplan-classification/elementplan-elements.skos.ttl"
)
PRODUCT_DIR = REPO_ROOT / "classification/abstract-member-product-classification"
MAPPING_OUT = REPO_ROOT / "classification/mapping/elementplan-elements-to-products.mapping.ttl"

PBS_NS = "https://schema.pragmaticbim.ch/"
MAP_NS = "https://example.org/mapping/"

ELEMENT_SCHEME_DEFINITION_EN = (
    "Cost-relevant building elements of the pragmaticBIM Elementplan. Each concept carries the one "
    "IFC base quantity used for take-off (pbs:referenceQuantity in pbs:quantityPset) and the unit that "
    "quantity is billed in (pbs:priceUnit), so an element resolves to a single unambiguous quantity "
    "basis for costing."
)
ELEMENT_SCHEME_DEFINITION_DE = (
    "Kostenrelevante Bauteile des pragmaticBIM Elementplans. Jedes Konzept trägt die eine für die "
    "Mengenermittlung verwendete IFC-Basismenge (pbs:referenceQuantity in pbs:quantityPset) sowie die "
    "zugehörige Verrechnungseinheit (pbs:priceUnit), damit ein Bauteil auf eine eindeutige "
    "Mengenbasis für die Kostenermittlung auflöst."
)
ELEMENT_SCOPE_NOTE_EN = (
    "Element codes, labels, IFC classes, and quantity sets follow the pragmaticBIM Elementplan Swiss "
    "add-ons package, which is authoritative. Exactly one reference quantity per element; where the "
    "Elementplan publishes several base quantities, only the costing quantity is recorded here. "
    "Products that differentiate an element for pricing are linked through the Elementplan elements to "
    "products mapping bridge."
)
ELEMENT_SCOPE_NOTE_DE = (
    "Bauteilcodes, Bezeichnungen, IFC-Klassen und Mengengruppen folgen dem Add-ons-Paket des "
    "pragmaticBIM Elementplans Schweiz, das führend ist. Genau eine Referenzmenge pro Bauteil; wo der "
    "Elementplan mehrere Basismengen publiziert, ist hier nur die Kostenmenge erfasst. Produkte zur "
    "Differenzierung eines Bauteils für die Bepreisung werden über die Mapping-Brücke Elementplan "
    "Bauteile zu Produkten verknüpft."
)

MAPPING_DESCRIPTION_EN = (
    "Links each cost-relevant building element to the product SKOS scheme whose concepts differentiate "
    "it for pricing (pbs:productScheme), plus the catch-all product used as fallback when a model "
    "carries no product classification (skos:closeMatch). Any concept of the referenced scheme is a "
    "valid product for the element; all of them share the element reference quantity and price unit. "
    "Elements without a pbs:productScheme have no product vocabulary yet. Regenerate with "
    "scripts/generate_element_vocabulary.py."
)
MAPPING_DESCRIPTION_DE = (
    "Verknüpft jedes kostenrelevante Bauteil mit dem Produkt-SKOS-Schema, dessen Konzepte es für die "
    "Bepreisung differenzieren (pbs:productScheme), sowie mit dem Sammelprodukt als Rückfallwert, wenn "
    "ein Modell keine Produktklassifikation trägt (skos:closeMatch). Jedes Konzept des referenzierten "
    "Schemas ist ein gültiges Produkt für das Bauteil; alle teilen Referenzmenge und "
    "Verrechnungseinheit des Bauteils. Bauteile ohne pbs:productScheme haben noch kein "
    "Produktvokabular. Regenerieren mit scripts/generate_element_vocabulary.py."
)


def _scheme_header(
    identifier: str,
    title_en: str,
    title_de: str,
    definition_en: str,
    definition_de: str,
    scope_note_en: str,
    scope_note_de: str,
    top_concepts: list[str],
) -> list[str]:
    return [
        ":scheme a skos:ConceptScheme ;",
        f'  skos:prefLabel "{ttl_escape(title_en)}"@en ;',
        f'  skos:prefLabel "{ttl_escape(title_de)}"@de ;',
        f'  dcterms:title "{ttl_escape(title_en)}"@en ;',
        f'  dcterms:title "{ttl_escape(title_de)}"@de ;',
        f'  dcterms:identifier "{identifier}" ;',
        f'  dcterms:creator "{CREATOR}" ;',
        f'  dcterms:issued "{ISSUED}"^^xsd:date ;',
        f'  dcterms:modified "{ISSUED}"^^xsd:date ;',
        f"  dcterms:license <{LICENSE}> ;",
        f"  dcterms:source <{SOURCE}> ;",
        "  dcterms:references map:elementplanElementsToProductsMapping ;",
        f'  skos:definition "{ttl_escape(definition_en)}"@en ;',
        f'  skos:definition "{ttl_escape(definition_de)}"@de ;',
        f'  skos:scopeNote "{ttl_escape(scope_note_en)}"@en ;',
        f'  skos:scopeNote "{ttl_escape(scope_note_de)}"@de ;',
        "  skos:hasTopConcept",
        *[
            f"    :{notation}," if idx < len(top_concepts) - 1 else f"    :{notation} ."
            for idx, notation in enumerate(top_concepts)
        ],
        "",
    ]


def render_element_skos() -> str:
    lines = [
        f"@prefix : <{EL_NS}> .",
        f"@prefix pbs: <{PBS_NS}> .",
        f"@prefix map: <{MAP_NS}> .",
        "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .",
        "@prefix dcterms: <http://purl.org/dc/terms/> .",
        "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .",
        "",
    ]
    lines.extend(
        _scheme_header(
            "ElementplanElement",
            "pragmaticBIM Elementplan elements",
            "pragmaticBIM Elementplan Bauteile",
            ELEMENT_SCHEME_DEFINITION_EN,
            ELEMENT_SCHEME_DEFINITION_DE,
            ELEMENT_SCOPE_NOTE_EN,
            ELEMENT_SCOPE_NOTE_DE,
            [e.notation for e in ELEMENTS],
        )
    )

    for element in ELEMENTS:
        block = [
            f":{element.notation} a skos:Concept ;",
            "  skos:inScheme :scheme ;",
            "  skos:topConceptOf :scheme ;",
            f'  skos:notation "{element.notation}" ;',
            f'  skos:prefLabel "{ttl_escape(element.label_en)}"@en ;',
            f'  skos:prefLabel "{ttl_escape(element.label_de)}"@de ;',
            f'  skos:definition "{ttl_escape(element.definition_en)}"@en ;',
            f'  skos:definition "{ttl_escape(element.definition_de)}"@de ;',
        ]
        if element.scope_note_en:
            block.append(f'  skos:scopeNote "{ttl_escape(element.scope_note_en)}"@en ;')
        if element.scope_note_de:
            block.append(f'  skos:scopeNote "{ttl_escape(element.scope_note_de)}"@de ;')
        block.append(f'  pbs:referenceQuantity "{element.reference_quantity}" ;')
        if element.quantity_pset:
            block.append(f'  pbs:quantityPset "{element.quantity_pset}" ;')
        block.extend(
            [
                f'  pbs:priceUnit "{element.price_unit}" ;',
                f'  dcterms:subject "{element.ifc_class}" ;',
                f'  dcterms:identifier "{element.notation}" .',
                "",
            ]
        )
        lines.extend(block)

    return "\n".join(lines).rstrip() + "\n"


def render_product_skos(scheme: MemberProductScheme) -> str:
    lines = [
        f"@prefix : <{scheme.ns}> .",
        f"@prefix pbs: <{PBS_NS}> .",
        f"@prefix map: <{MAP_NS}> .",
        "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .",
        "@prefix dcterms: <http://purl.org/dc/terms/> .",
        "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .",
        "",
    ]
    lines.extend(
        _scheme_header(
            scheme.identifier,
            scheme.title_en,
            scheme.title_de,
            scheme.definition_en,
            scheme.definition_de,
            scheme.scope_note_en,
            scheme.scope_note_de,
            [p.notation for p in scheme.products],
        )
    )

    for product in scheme.products:
        lines.extend(
            [
                f":{product.notation} a skos:Concept ;",
                "  skos:inScheme :scheme ;",
                "  skos:topConceptOf :scheme ;",
                f'  skos:notation "{product.notation}" ;',
                f'  skos:prefLabel "{ttl_escape(product.label_en)}"@en ;',
                f'  skos:prefLabel "{ttl_escape(product.label_de)}"@de ;',
                f'  skos:definition "{ttl_escape(product.definition_en)}"@en ;',
                f'  skos:definition "{ttl_escape(product.definition_de)}"@de ;',
                f'  pbs:priceUnit "{scheme.price_unit}" ;',
                f'  dcterms:identifier "{product.notation}" .',
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


def render_mapping() -> str:
    prefixes = used_scheme_prefixes()
    lines = [
        f"@prefix el: <{EL_NS}> .",
    ]
    for prefix in prefixes:
        lines.append(f"@prefix {prefix}: <{PRODUCT_SCHEMES[prefix].ns}> .")
    lines.extend(
        [
            f"@prefix pbs: <{PBS_NS}> .",
            f"@prefix map: <{MAP_NS}> .",
            "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .",
            "@prefix dcterms: <http://purl.org/dc/terms/> .",
            "",
            "map:elementplanElementsToProductsMapping a dcterms:Dataset ;",
            '  dcterms:title "pragmaticBIM Elementplan elements to products mapping"@en ;',
            '  dcterms:title "Mapping pragmaticBIM Elementplan Bauteile zu Produkten"@de ;',
            "  dcterms:references el:scheme, "
            + ", ".join(f"{prefix}:scheme" for prefix in prefixes)
            + " ;",
            f'  dcterms:issued "{ISSUED}" ;',
            f'  dcterms:description "{ttl_escape(MAPPING_DESCRIPTION_EN)}"@en ;',
            f'  dcterms:description "{ttl_escape(MAPPING_DESCRIPTION_DE)}"@de .',
            "",
        ]
    )

    for element in ELEMENTS:
        if not element.product_scheme:
            continue
        scheme = scheme_for(element)
        lines.extend(
            [
                f"el:{element.notation} pbs:productScheme {scheme.prefix}:scheme ;",
                f'  pbs:referenceQuantity "{element.reference_quantity}" ;',
                f'  pbs:priceUnit "{element.price_unit}" ;',
                f"  skos:closeMatch {scheme.prefix}:{scheme.default_product} .",
                "",
            ]
        )

    unpriced = [e for e in ELEMENTS if not e.product_scheme]
    if unpriced:
        lines.append(
            "# No product vocabulary yet: "
            + ", ".join(e.notation for e in unpriced)
            + "."
        )

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    ELEMENT_OUT.parent.mkdir(parents=True, exist_ok=True)
    ELEMENT_OUT.write_text(render_element_skos(), encoding="utf-8")
    print(f"Wrote {ELEMENT_OUT.relative_to(REPO_ROOT)} ({len(ELEMENTS)} elements)")

    PRODUCT_DIR.mkdir(parents=True, exist_ok=True)
    for scheme in SCHEMES:
        target = PRODUCT_DIR / scheme.filename
        target.write_text(render_product_skos(scheme), encoding="utf-8")
        print(f"Wrote {target.relative_to(REPO_ROOT)} ({len(scheme.products)} products)")

    MAPPING_OUT.write_text(render_mapping(), encoding="utf-8")
    count_elements = len([e for e in ELEMENTS if e.reference_quantity == COUNT_QUANTITY])
    print(
        f"Wrote {MAPPING_OUT.relative_to(REPO_ROOT)} "
        f"({len(elements_with_products())} mapped, {count_elements} priced by count)"
    )


if __name__ == "__main__":
    main()
