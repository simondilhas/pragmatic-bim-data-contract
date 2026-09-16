#!/usr/bin/env python3
"""Validate the building element vocabulary, member product schemes, and product bridge."""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

from rdflib import Graph, Namespace
from rdflib.namespace import DCTERMS, SKOS

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from element_data import (  # noqa: E402
    COUNT_QUANTITY,
    EL_NS,
    ELEMENTS,
    PRODUCT_SCHEMES,
    elements_with_products,
    scheme_for,
)
from member_product_data import ALL_PRODUCTS, SCHEMES  # noqa: E402

PBS = Namespace("https://schema.pragmaticbim.ch/")
EL = Namespace(EL_NS)

ELEMENT_SKOS = REPO_ROOT / "classification/abstract-element-classification/building-elements.skos.ttl"
PRODUCT_DIR = REPO_ROOT / "classification/abstract-member-product-classification"
MAPPING = REPO_ROOT / "classification/mapping/abstract-elements-to-products.mapping.ttl"
CATALOG = REPO_ROOT / "classification/catalog.yaml"
ENTRIES_DIR = REPO_ROOT / "baseline-unit-prices/entries"

EXPECTED_ELEMENT_COUNT = 22
EXPECTED_PRODUCT_COUNT = 21
VALID_PRICE_UNITS = {"m", "m2", "m3", "pcs"}


def _check_element_data(errors: list[str]) -> None:
    if len(ELEMENTS) != EXPECTED_ELEMENT_COUNT:
        errors.append(
            f"expected {EXPECTED_ELEMENT_COUNT} elements, found {len(ELEMENTS)}"
        )
    if len(ALL_PRODUCTS) != EXPECTED_PRODUCT_COUNT:
        errors.append(
            f"expected {EXPECTED_PRODUCT_COUNT} member products, found {len(ALL_PRODUCTS)}"
        )

    notations: dict[str, int] = defaultdict(int)
    labels_en: dict[str, list[str]] = defaultdict(list)
    labels_de: dict[str, list[str]] = defaultdict(list)

    for element in ELEMENTS:
        notations[element.notation] += 1
        labels_en[element.label_en.lower()].append(element.notation)
        labels_de[element.label_de.lower()].append(element.notation)

        if not element.reference_quantity:
            errors.append(f"{element.notation}: missing reference_quantity")
        if element.price_unit not in VALID_PRICE_UNITS:
            errors.append(f"{element.notation}: invalid price_unit ({element.price_unit})")
        if element.reference_quantity == COUNT_QUANTITY:
            if element.quantity_pset:
                errors.append(
                    f"{element.notation}: count quantity must not declare a quantity_pset"
                )
            if element.price_unit != "pcs":
                errors.append(
                    f"{element.notation}: count quantity requires price_unit pcs"
                )
        elif not element.quantity_pset:
            errors.append(f"{element.notation}: missing quantity_pset")
        elif not element.quantity_pset.startswith("Qto_"):
            errors.append(
                f"{element.notation}: quantity_pset {element.quantity_pset} is not a Qto_ set"
            )
        if not element.ifc_class.startswith("Ifc"):
            errors.append(f"{element.notation}: invalid ifc_class ({element.ifc_class})")
        if element.product_scheme and element.product_scheme not in PRODUCT_SCHEMES:
            errors.append(
                f"{element.notation}: unknown product_scheme {element.product_scheme}"
            )

    for notation, count in notations.items():
        if count > 1:
            errors.append(f"duplicate element notation {notation} ({count}x)")
    for label, owners in labels_en.items():
        if len(owners) > 1:
            errors.append(f"duplicate EN element label '{label}': {owners}")
    for label, owners in labels_de.items():
        if len(owners) > 1:
            errors.append(f"duplicate DE element label '{label}': {owners}")


def _check_product_data(errors: list[str]) -> None:
    notations: dict[str, int] = defaultdict(int)
    for scheme in SCHEMES:
        if scheme.price_unit not in VALID_PRICE_UNITS:
            errors.append(f"{scheme.slug}: invalid price_unit ({scheme.price_unit})")
        scheme_notations = {p.notation for p in scheme.products}
        if scheme.default_product not in scheme_notations:
            errors.append(
                f"{scheme.slug}: default_product {scheme.default_product} is not in the scheme"
            )
        for product in scheme.products:
            notations[product.notation] += 1
            if not product.notation.startswith(scheme.notation_prefix):
                errors.append(
                    f"{product.notation}: does not use scheme prefix {scheme.notation_prefix}"
                )
    for notation, count in notations.items():
        if count > 1:
            errors.append(f"duplicate product notation {notation} ({count}x)")


def _check_generated_ttl(errors: list[str]) -> None:
    if not ELEMENT_SKOS.exists():
        errors.append(f"missing {ELEMENT_SKOS.relative_to(REPO_ROOT)}")
        return

    graph = Graph()
    graph.parse(ELEMENT_SKOS, format="turtle")
    for element in ELEMENTS:
        node = EL[element.notation]
        if (node, SKOS.topConceptOf, None) not in graph:
            errors.append(f"{element.notation}: not a topConcept in the element vocabulary")
        quantity = graph.value(node, PBS.referenceQuantity)
        if quantity is None or str(quantity) != element.reference_quantity:
            errors.append(
                f"{element.notation}: pbs:referenceQuantity mismatch "
                f"({quantity} != {element.reference_quantity})"
            )
        unit = graph.value(node, PBS.priceUnit)
        if unit is None or str(unit) != element.price_unit:
            errors.append(
                f"{element.notation}: pbs:priceUnit mismatch ({unit} != {element.price_unit})"
            )

    for scheme in SCHEMES:
        path = PRODUCT_DIR / scheme.filename
        if not path.exists():
            errors.append(f"missing {path.relative_to(REPO_ROOT)}")
            continue
        product_graph = Graph()
        product_graph.parse(path, format="turtle")
        ns = Namespace(scheme.ns)
        identifier = product_graph.value(ns["scheme"], DCTERMS.identifier)
        if identifier is None or str(identifier) != scheme.identifier:
            errors.append(f"{scheme.filename}: dcterms:identifier mismatch ({identifier})")
        for product in scheme.products:
            if (ns[product.notation], SKOS.topConceptOf, ns["scheme"]) not in product_graph:
                errors.append(f"{product.notation}: not a topConcept of {scheme.slug}")


def _check_mapping(errors: list[str]) -> None:
    if not MAPPING.exists():
        errors.append(f"missing {MAPPING.relative_to(REPO_ROOT)}")
        return

    graph = Graph()
    graph.parse(MAPPING, format="turtle")

    for element in ELEMENTS:
        node = EL[element.notation]
        scheme_targets = list(graph.objects(node, PBS.productScheme))
        if not element.product_scheme:
            if scheme_targets:
                errors.append(
                    f"{element.notation}: has pbs:productScheme but declares no product scheme"
                )
            continue
        ref = scheme_for(element)
        expected_scheme = Namespace(ref.ns)["scheme"]
        if scheme_targets != [expected_scheme]:
            errors.append(
                f"{element.notation}: pbs:productScheme mismatch ({scheme_targets})"
            )
        fallbacks = list(graph.objects(node, SKOS.closeMatch))
        expected_fallback = Namespace(ref.ns)[ref.default_product]
        if fallbacks != [expected_fallback]:
            errors.append(
                f"{element.notation}: skos:closeMatch fallback mismatch ({fallbacks})"
            )


def _check_catalog(errors: list[str]) -> None:
    if not CATALOG.exists():
        errors.append(f"missing {CATALOG.relative_to(REPO_ROOT)}")
        return
    text = CATALOG.read_text(encoding="utf-8")
    expected_paths = [
        "abstract-element-classification/building-elements.skos.ttl",
        *[f"abstract-member-product-classification/{s.filename}" for s in SCHEMES],
        "mapping/abstract-elements-to-products.mapping.ttl",
    ]
    for path in expected_paths:
        if path not in text:
            errors.append(f"catalog.yaml does not register {path}")


def _check_price_coverage(errors: list[str]) -> None:
    if not ENTRIES_DIR.exists():
        errors.append(f"missing {ENTRIES_DIR.relative_to(REPO_ROOT)}")
        return
    for product in ALL_PRODUCTS:
        path = ENTRIES_DIR / f"{product.notation}.json"
        if not path.exists():
            errors.append(f"{product.notation}: no price entry in baseline-unit-prices/entries")
            continue
        entry = json.loads(path.read_text(encoding="utf-8"))
        if not entry.get("material_cost"):
            errors.append(f"{product.notation}: price entry has no material_cost")

    for element in elements_with_products():
        ref = scheme_for(element)
        fallback = ENTRIES_DIR / f"{ref.default_product}.json"
        if not fallback.exists():
            errors.append(
                f"{element.notation}: fallback product {ref.default_product} has no price entry"
            )


def main() -> int:
    errors: list[str] = []
    _check_element_data(errors)
    _check_product_data(errors)
    _check_generated_ttl(errors)
    _check_mapping(errors)
    _check_catalog(errors)
    _check_price_coverage(errors)

    if errors:
        print(f"Element classification validation failed ({len(errors)} error(s)):")
        for error in errors:
            print(f"  - {error}")
        return 1

    unpriced = [e.notation for e in ELEMENTS if not e.product_scheme]
    print(
        f"Element classification OK: {len(ELEMENTS)} elements, "
        f"{len(ALL_PRODUCTS)} member products, {len(elements_with_products())} mapped."
    )
    if unpriced:
        print(f"  Elements without a product vocabulary: {', '.join(unpriced)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
