#!/usr/bin/env python3
"""List assignable baseline product codes from the SKOS vocabularies.

Parses every ``classification/**/*product*.skos.ttl`` for ``skos:topConceptOf``
concepts and their notation. LCA layer sub-concepts are excluded (they carry a
layer suffix and are not top concepts). Outputs a product manifest and, on
request, a human CSV or scaffolded per-code entry templates.

Usage:
  python scripts/list_baseline_products.py            # write manifest
  python scripts/list_baseline_products.py --csv      # + product-codes.csv
  python scripts/list_baseline_products.py --scaffold # + missing entries/*.json
  python scripts/list_baseline_products.py --check     # CI: manifest == entries/
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

from rdflib import Graph
from rdflib.namespace import DCTERMS, SKOS

from baseline_prices_common import (
    REPO_ROOT,
    default_price_unit,
    infer_product_category,
    notation_to_iri,
)

SKOS_GLOB = "abstract-*-classification/*product*.skos.ttl"
CLASSIFICATION_DIR = REPO_ROOT / "classification"
BASELINE_DIR = REPO_ROOT / "baseline-unit-prices"
ENTRIES_DIR = BASELINE_DIR / "entries"
MANIFEST_PATH = BASELINE_DIR / "product-manifest.json"
CODES_CSV_PATH = BASELINE_DIR / "product-codes.csv"


def collect_products() -> list[dict[str, object]]:
    products: list[dict[str, object]] = []
    for path in sorted(CLASSIFICATION_DIR.glob(SKOS_GLOB)):
        graph = Graph()
        graph.parse(path, format="turtle")
        for concept in graph.subjects(SKOS.topConceptOf, None):
            notation = graph.value(concept, SKOS.notation)
            if not notation:
                continue
            notation = str(notation)
            scheme = graph.value(concept, SKOS.topConceptOf)
            scheme_id = None
            if scheme is not None:
                scheme_id = graph.value(scheme, DCTERMS.identifier)
            label_en = None
            for label in graph.objects(concept, SKOS.prefLabel):
                if getattr(label, "language", None) == "en":
                    label_en = str(label)
                    break
            products.append(
                {
                    "notation": notation,
                    "scheme": str(scheme_id) if scheme_id else str(scheme or ""),
                    "product_uri": notation_to_iri(notation),
                    "pref_label_en": label_en,
                    "category": infer_product_category(notation),
                    "price_unit": default_price_unit(notation),
                }
            )
    products.sort(key=lambda p: str(p["notation"]))
    return products


def write_manifest(products: list[dict[str, object]]) -> None:
    doc = {
        "count": len(products),
        "source": "classification/**/*product*.skos.ttl",
        "products": products,
    }
    BASELINE_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(products)} products to {MANIFEST_PATH.relative_to(REPO_ROOT)}")


def write_codes_csv(products: list[dict[str, object]]) -> None:
    fieldnames = ["notation", "category", "price_unit", "pref_label_en", "product_uri"]
    with CODES_CSV_PATH.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for product in products:
            writer.writerow(product)
    print(f"Wrote {CODES_CSV_PATH.relative_to(REPO_ROOT)}")


def scaffold_entries(products: list[dict[str, object]]) -> None:
    ENTRIES_DIR.mkdir(parents=True, exist_ok=True)
    created = 0
    for product in products:
        notation = str(product["notation"])
        target = ENTRIES_DIR / f"{notation}.json"
        if target.exists():
            continue
        template = {
            "product": notation,
            "material_cost": None,
            "price_unit": product["price_unit"],
            "onsite_labor_hours_per_unit": None,
            "provenance_status": "estimated",
            "observations": [],
        }
        target.write_text(json.dumps(template, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        created += 1
    print(f"Scaffolded {created} new entry template(s) in {ENTRIES_DIR.relative_to(REPO_ROOT)}")


def check_coverage(products: list[dict[str, object]]) -> int:
    manifest_codes = {str(p["notation"]) for p in products}
    if not ENTRIES_DIR.exists():
        print(f"Missing entries directory: {ENTRIES_DIR.relative_to(REPO_ROOT)}", file=sys.stderr)
        return 1
    entry_codes = {p.stem for p in ENTRIES_DIR.glob("*.json")}

    missing = sorted(manifest_codes - entry_codes)
    extra = sorted(entry_codes - manifest_codes)
    errors = []
    if missing:
        errors.append(f"entries missing for {len(missing)} code(s): {missing}")
    if extra:
        errors.append(f"entries with no matching top concept: {extra}")

    for path in sorted(ENTRIES_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("product") != path.stem:
            errors.append(f"{path.name}: product '{data.get('product')}' != filename")

    if errors:
        print("Manifest coverage check failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    print(f"Coverage OK: {len(manifest_codes)} codes match entries/ on disk")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", action="store_true", help="also write product-codes.csv")
    parser.add_argument("--scaffold", action="store_true", help="create missing entries/*.json templates")
    parser.add_argument("--check", action="store_true", help="fail if manifest != entries/ on disk")
    args = parser.parse_args()

    products = collect_products()

    if args.check:
        return check_coverage(products)

    write_manifest(products)
    if args.csv:
        write_codes_csv(products)
    if args.scaffold:
        scaffold_entries(products)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
