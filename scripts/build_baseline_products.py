#!/usr/bin/env python3
"""Build the merged baseline price book from per-code entry files.

Reads every ``baseline-unit-prices/entries/*.json`` (the git source of truth),
applies category defaults from ``cost-adjustments.json`` (waste, transport,
demolition, uncertainty), derives ``delivered_material_cost`` and uncertainty
bounds, and writes the ``BaselinePriceBook`` document. Carbon/KBOB fields are
intentionally not produced here (deferred to the eco pass).

Also merges the regional material and labor benchmark sources into the
``RegionalCostBenchmarkBook`` document.

Usage:
  python scripts/build_baseline_products.py           # write outputs
  python scripts/build_baseline_products.py --check    # CI: fail if stale
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from baseline_prices_common import (
    ANCHOR_REGION,
    DISCLAIMER,
    LICENSE,
    build_uncertainty,
    compute_delivered_material_cost,
    format_demolition,
    infer_product_category,
    notation_to_iri,
    resolve_provenance_status,
    resolve_uncertainty_config,
)
from list_baseline_products import collect_products

REPO_ROOT = Path(__file__).resolve().parents[1]
BASELINE_DIR = REPO_ROOT / "baseline-unit-prices"
ENTRIES_DIR = BASELINE_DIR / "entries"
COST_ADJUSTMENTS_PATH = BASELINE_DIR / "cost-adjustments.json"
REGIONAL_MATERIAL_PATH = BASELINE_DIR / "regional-material-benchmarks.json"
REGIONAL_LABOR_PATH = BASELINE_DIR / "regional-labor-benchmarks.json"

OUT_PRODUCTS = BASELINE_DIR / "baseline-products.json"
OUT_REGIONAL = BASELINE_DIR / "regional-benchmarks.json"

VERSION = "v13"
SOURCE = "baseline-unit-prices/entries/"


def load_entries() -> list[dict]:
    if not ENTRIES_DIR.exists():
        raise SystemExit(
            f"Missing {ENTRIES_DIR.relative_to(REPO_ROOT)}. "
            "Run list_baseline_products.py --scaffold first."
        )
    entries = []
    for path in sorted(ENTRIES_DIR.glob("*.json")):
        entry = json.loads(path.read_text(encoding="utf-8"))
        entry["__file"] = path.name
        entries.append(entry)
    return entries


def validate_entries(entries: list[dict], strict: bool) -> list[str]:
    errors: list[str] = []
    manifest_codes = {str(p["notation"]) for p in collect_products()}
    entry_codes = {str(e.get("product")) for e in entries}

    missing = sorted(manifest_codes - entry_codes)
    extra = sorted(entry_codes - manifest_codes)
    if missing:
        errors.append(f"missing entries for {len(missing)} top concept(s): {missing}")
    if extra:
        errors.append(f"entries with no matching top concept: {extra}")

    for entry in entries:
        notation = entry.get("product")
        fname = entry.get("__file")
        if not notation:
            errors.append(f"{fname}: missing product")
            continue
        if entry.get("price_unit") not in ("m2", "m3", "pcs"):
            errors.append(f"{notation}: invalid or missing price_unit ({entry.get('price_unit')})")
        material_cost = entry.get("material_cost")
        if material_cost is None:
            errors.append(f"{notation}: missing material_cost")
        elif strict and float(material_cost) <= 0:
            errors.append(f"{notation}: material_cost must be positive (got {material_cost})")
        if entry.get("onsite_labor_hours_per_unit") is None:
            errors.append(f"{notation}: missing onsite_labor_hours_per_unit")
    return errors


def build_entry(entry: dict, cost_adjustments: dict) -> dict:
    notation = str(entry["product"])
    price_unit = str(entry["price_unit"])
    category = infer_product_category(notation)
    cat_defaults = cost_adjustments.get("categories", {}).get(category, {})
    overrides = cost_adjustments.get("product_overrides", {}).get(notation, {})

    material_cost = entry.get("material_cost")
    material_cost = round(float(material_cost), 1) if material_cost is not None else None

    waste_pct = entry.get("waste_pct", overrides.get("waste_pct", cat_defaults.get("waste_pct", 0.0)))
    transport_pct = entry.get(
        "transport_pct", overrides.get("transport_pct", cat_defaults.get("transport_pct", 0.0))
    )
    delivered = entry.get("delivered_material_cost")
    if delivered is None:
        delivered = compute_delivered_material_cost(material_cost, waste_pct, transport_pct)

    onsite = entry.get("onsite_labor_hours_per_unit")
    offsite = entry.get("offsite_labor_hours_per_unit") or 0.0

    result: dict[str, object] = {
        "product": notation,
        "product_uri": notation_to_iri(notation),
        "material_cost": material_cost,
        "price_unit": price_unit,
        "waste_pct": waste_pct,
        "transport_pct": transport_pct,
        "onsite_labor_hours_per_unit": onsite,
    }
    if delivered is not None:
        result["delivered_material_cost"] = delivered
    if offsite:
        result["offsite_labor_hours_per_unit"] = offsite

    demo_source = entry.get("demolition")
    if demo_source is None:
        demo_defaults = overrides.get("demolition", cat_defaults.get("demolition", {}))
        demo_source = {
            "hours_per_unit": demo_defaults.get("hours_per_unit"),
            "disposal_cost": demo_defaults.get("disposal_cost"),
        }
    demolition = format_demolition({**demo_source, "unit": price_unit})
    if demolition:
        result["demolition"] = demolition

    unc_cfg = resolve_uncertainty_config(notation, category, cost_adjustments)
    price = {"material_cost": material_cost, "delivered_material_cost": delivered}
    labor = {"onsite_hours_per_unit": onsite, "offsite_hours_per_unit": offsite}
    result["uncertainty"] = build_uncertainty(price, labor, unc_cfg)

    result["provenance_status"] = entry.get(
        "provenance_status", resolve_provenance_status(notation, cost_adjustments)
    )
    if entry.get("observations"):
        result["observations"] = entry["observations"]
    return result


def build_products_doc(entries: list[dict], cost_adjustments: dict) -> dict:
    issued = cost_adjustments.get("issued", "2026-07-01")
    built = {}
    for entry in sorted(entries, key=lambda e: str(e["product"])):
        built[str(entry["product"])] = build_entry(entry, cost_adjustments)
    return {
        "version": VERSION,
        "issued": issued,
        "anchor_region": ANCHOR_REGION,
        "source": SOURCE,
        "license": LICENSE,
        "disclaimer": DISCLAIMER,
        "entries": built,
    }


def build_regional_doc(issued: str) -> dict:
    material = json.loads(REGIONAL_MATERIAL_PATH.read_text(encoding="utf-8"))
    labor = json.loads(REGIONAL_LABOR_PATH.read_text(encoding="utf-8"))
    material_by_code = {str(r["code"]): r for r in material.get("regions", [])}

    regions: dict[str, dict] = {}
    for lab in labor.get("regions", []):
        code = str(lab["code"])
        mat = material_by_code.get(code, {})
        region: dict[str, object] = {
            "code": code,
            "currency": lab.get("currency", mat.get("currency")),
            "material_factor": mat.get("material_factor", 1.0),
            "fx_to_eur": mat.get("fx_to_eur", 1.0),
            "labor_factor": 1.0,
            "labor_unit_price": lab.get("hourly_rate"),
        }
        if lab.get("offsite_hourly_rate") is not None:
            region["offsite_labor_unit_price"] = lab["offsite_hourly_rate"]
        regions[code] = region

    return {
        "version": VERSION,
        "issued": issued,
        "anchor_region": material.get("anchor", ANCHOR_REGION),
        "source": SOURCE,
        "license": LICENSE,
        "disclaimer": DISCLAIMER,
        "regions": regions,
    }


def dump(path: Path, doc: dict) -> None:
    path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if outputs are stale")
    parser.add_argument(
        "--no-strict",
        action="store_true",
        help="allow zero/missing material_cost (default requires positive)",
    )
    args = parser.parse_args()

    cost_adjustments = json.loads(COST_ADJUSTMENTS_PATH.read_text(encoding="utf-8"))
    entries = load_entries()

    errors = validate_entries(entries, strict=not args.no_strict)
    if errors:
        print("Entry validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    issued = cost_adjustments.get("issued", "2026-07-01")
    products_doc = build_products_doc(entries, cost_adjustments)
    regional_doc = build_regional_doc(issued)

    if args.check:
        stale = []
        for path, doc in ((OUT_PRODUCTS, products_doc), (OUT_REGIONAL, regional_doc)):
            expected = json.dumps(doc, indent=2, ensure_ascii=False) + "\n"
            current = path.read_text(encoding="utf-8") if path.exists() else None
            if current != expected:
                stale.append(str(path.relative_to(REPO_ROOT)))
        if stale:
            print("Stale build outputs (run build_baseline_products.py):", file=sys.stderr)
            for path in stale:
                print(f"  - {path}", file=sys.stderr)
            return 1
        print("Build outputs are up to date")
        return 0

    dump(OUT_PRODUCTS, products_doc)
    dump(OUT_REGIONAL, regional_doc)
    print(f"Wrote {len(products_doc['entries'])} entries to {OUT_PRODUCTS.relative_to(REPO_ROOT)}")
    print(f"Wrote {len(regional_doc['regions'])} regions to {OUT_REGIONAL.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
