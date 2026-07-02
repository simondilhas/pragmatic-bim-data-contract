#!/usr/bin/env python3
"""Export baseline unit price JSON files to flat CSV for review and adaptation."""

from __future__ import annotations

import csv
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PRODUCTS_JSON = REPO_ROOT / "baseline-unit-prices/baseline-products.json"
REGIONAL_JSON = REPO_ROOT / "baseline-unit-prices/regional-benchmarks.json"
REGIONAL_LABOR_JSON = REPO_ROOT / "baseline-unit-prices/regional-labor-benchmarks.json"
REGIONAL_MATERIAL_JSON = REPO_ROOT / "baseline-unit-prices/regional-material-benchmarks.json"
OUT_PRODUCTS_CSV = REPO_ROOT / "baseline-unit-prices/baseline-products.csv"
OUT_REGIONAL_CSV = REPO_ROOT / "baseline-unit-prices/regional-benchmarks.csv"
OUT_REGIONAL_LABOR_CSV = REPO_ROOT / "baseline-unit-prices/regional-labor-benchmarks.csv"
OUT_REGIONAL_MATERIAL_CSV = REPO_ROOT / "baseline-unit-prices/regional-material-benchmarks.csv"


def export_products() -> None:
    data = json.loads(PRODUCTS_JSON.read_text(encoding="utf-8"))
    fieldnames = [
        "product",
        "product_uri",
        "material_cost",
        "price_unit",
        "waste_pct",
        "transport_pct",
        "delivered_material_cost",
        "material_cost_low",
        "material_cost_high",
        "delivered_material_cost_low",
        "delivered_material_cost_high",
        "onsite_labor_hours_per_unit",
        "onsite_labor_hours_low",
        "onsite_labor_hours_high",
        "offsite_labor_hours_per_unit",
        "offsite_labor_hours_low",
        "offsite_labor_hours_high",
        "material_low_pct",
        "material_high_pct",
        "labor_low_pct",
        "labor_high_pct",
        "provenance_status",
        "demolition_hours_per_unit",
        "demolition_disposal_cost",
        "observation_count",
        "reference_sources",
    ]
    with OUT_PRODUCTS_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        entries = data["entries"]
        if isinstance(entries, dict):
            entries = entries.values()
        for entry in entries:
            demolition = entry.get("demolition", {})
            uncertainty = entry.get("uncertainty", {})
            observations = entry.get("observations") or []
            reference_sources = sorted(
                {obs["reference_source"] for obs in observations if obs.get("reference_source")}
            )
            writer.writerow(
                {
                    "product": entry["product"],
                    "product_uri": entry.get("product_uri"),
                    "material_cost": entry["material_cost"],
                    "price_unit": entry["price_unit"],
                    "waste_pct": entry.get("waste_pct"),
                    "transport_pct": entry.get("transport_pct"),
                    "delivered_material_cost": entry.get("delivered_material_cost"),
                    "material_cost_low": uncertainty.get("material_cost_low"),
                    "material_cost_high": uncertainty.get("material_cost_high"),
                    "delivered_material_cost_low": uncertainty.get("delivered_material_cost_low"),
                    "delivered_material_cost_high": uncertainty.get("delivered_material_cost_high"),
                    "onsite_labor_hours_per_unit": entry.get("onsite_labor_hours_per_unit"),
                    "onsite_labor_hours_low": uncertainty.get("onsite_labor_hours_low"),
                    "onsite_labor_hours_high": uncertainty.get("onsite_labor_hours_high"),
                    "offsite_labor_hours_per_unit": entry.get("offsite_labor_hours_per_unit"),
                    "offsite_labor_hours_low": uncertainty.get("offsite_labor_hours_low"),
                    "offsite_labor_hours_high": uncertainty.get("offsite_labor_hours_high"),
                    "material_low_pct": uncertainty.get("material_low_pct"),
                    "material_high_pct": uncertainty.get("material_high_pct"),
                    "labor_low_pct": uncertainty.get("labor_low_pct"),
                    "labor_high_pct": uncertainty.get("labor_high_pct"),
                    "provenance_status": entry.get("provenance_status"),
                    "demolition_hours_per_unit": demolition.get("hours_per_unit"),
                    "demolition_disposal_cost": demolition.get("disposal_cost"),
                    "observation_count": len(observations),
                    "reference_sources": ";".join(reference_sources),
                }
            )


def export_regional() -> None:
    data = json.loads(REGIONAL_JSON.read_text(encoding="utf-8"))
    fieldnames = [
        "code",
        "currency",
        "material_factor",
        "fx_to_eur",
        "labor_factor",
        "labor_unit_price",
        "offsite_labor_unit_price",
    ]
    with OUT_REGIONAL_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        regions = data["regions"]
        if isinstance(regions, dict):
            regions = regions.values()
        for region in regions:
            writer.writerow(region)


def export_regions_legacy() -> None:
    if REGIONAL_LABOR_JSON.exists():
        data = json.loads(REGIONAL_LABOR_JSON.read_text(encoding="utf-8"))
        fieldnames = ["code", "hourly_rate", "offsite_hourly_rate", "currency"]
        with OUT_REGIONAL_LABOR_CSV.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            for region in data["regions"]:
                writer.writerow(region)
    if REGIONAL_MATERIAL_JSON.exists():
        data = json.loads(REGIONAL_MATERIAL_JSON.read_text(encoding="utf-8"))
        fieldnames = ["code", "label_en", "material_factor", "currency", "fx_to_eur"]
        with OUT_REGIONAL_MATERIAL_CSV.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            for region in data["regions"]:
                writer.writerow(region)


def main() -> None:
    if not PRODUCTS_JSON.exists():
        raise SystemExit(
            "Missing JSON input. Run scripts/build_baseline_products.py first."
        )
    export_products()
    print(f"Wrote {OUT_PRODUCTS_CSV.relative_to(REPO_ROOT)}")
    if REGIONAL_JSON.exists():
        export_regional()
        print(f"Wrote {OUT_REGIONAL_CSV.relative_to(REPO_ROOT)}")
    export_regions_legacy()
    if OUT_REGIONAL_LABOR_CSV.exists():
        print(f"Wrote {OUT_REGIONAL_LABOR_CSV.relative_to(REPO_ROOT)}")
    if OUT_REGIONAL_MATERIAL_CSV.exists():
        print(f"Wrote {OUT_REGIONAL_MATERIAL_CSV.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
