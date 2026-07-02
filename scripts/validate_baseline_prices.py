#!/usr/bin/env python3
"""Validate baseline unit price JSON against the cost LinkML schema."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA = REPO_ROOT / "contract/cost/baseline_cost_schema.yaml"
PRODUCTS = REPO_ROOT / "baseline-unit-prices/baseline-products.json"
REGIONAL = REPO_ROOT / "baseline-unit-prices/regional-benchmarks.json"
LIST_SCRIPT = REPO_ROOT / "scripts/list_baseline_products.py"

VALID_PRICE_UNITS = ("m2", "m3", "pcs")

METHOD_REQUIRED_SLOT = {
    "density": "density_kg_m3",
    "area_yield": "mass_per_area_kg_m2",
    "piece_area": "area_per_piece_m2",
}

METHOD_FORBIDDEN_SLOTS = {
    "direct": ("density_kg_m3", "mass_per_area_kg_m2", "area_per_piece_m2", "thickness_m"),
    "density": ("mass_per_area_kg_m2", "area_per_piece_m2"),
    "area_yield": ("area_per_piece_m2",),
    "piece_area": ("density_kg_m3", "mass_per_area_kg_m2", "thickness_m"),
    "layer_recipe_sum": ("density_kg_m3", "mass_per_area_kg_m2", "area_per_piece_m2", "thickness_m"),
    "unmapped": ("density_kg_m3", "mass_per_area_kg_m2", "area_per_piece_m2", "thickness_m"),
    "unconverted": ("density_kg_m3", "mass_per_area_kg_m2", "area_per_piece_m2", "thickness_m"),
}


def run_validate(target_class: str, data_path: Path) -> int:
    result = subprocess.run(
        [
            "linkml-validate",
            "-C",
            target_class,
            "-s",
            str(SCHEMA),
            str(data_path),
        ],
        cwd=SCHEMA.parent,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(result.stdout, file=sys.stderr)
        print(result.stderr, file=sys.stderr)
    return result.returncode


def validate_carbon_geometry(products_path: Path) -> list[str]:
    data = json.loads(products_path.read_text(encoding="utf-8"))
    entries = data.get("entries", {})
    if isinstance(entries, list):
        entries = {entry["product"]: entry for entry in entries}

    errors: list[str] = []
    for product, entry in entries.items():
        carbon = entry.get("carbon_per_price_unit")
        if not carbon:
            continue
        method = carbon.get("method")
        if not method:
            continue

        required = METHOD_REQUIRED_SLOT.get(method)
        if required and carbon.get(required) is None:
            errors.append(f"{product}: method {method} requires {required}")

        for slot in METHOD_FORBIDDEN_SLOTS.get(method, ()):
            if carbon.get(slot) is not None:
                errors.append(f"{product}: method {method} must not set {slot}")

        density = carbon.get("density_kg_m3")
        mass = carbon.get("mass_per_area_kg_m2")
        if method == "area_yield" and density is not None and mass is not None:
            if mass == density and density > 200:
                errors.append(
                    f"{product}: mass_per_area_kg_m2 equals density_kg_m3 ({mass}); "
                    "likely kg/m³ used as kg/m²"
                )

        thickness = carbon.get("thickness_m")
        if thickness is not None and density is not None and mass is not None:
            expected = round(thickness * density, 4)
            if abs(mass - expected) > max(0.5, expected * 0.05):
                errors.append(
                    f"{product}: mass_per_area_kg_m2 ({mass}) inconsistent with "
                    f"thickness_m × density_kg_m3 ({expected})"
                )

    return errors


def validate_uncertainty(products_path: Path) -> list[str]:
    data = json.loads(products_path.read_text(encoding="utf-8"))
    entries = data.get("entries", {})
    if isinstance(entries, list):
        entries = {entry["product"]: entry for entry in entries}

    errors: list[str] = []
    for product, entry in entries.items():
        uncertainty = entry.get("uncertainty")
        if not uncertainty:
            errors.append(f"{product}: missing uncertainty")
            continue

        material_cost = entry.get("material_cost")
        for pct_key, bound_key in (
            ("material_low_pct", "material_cost_low"),
            ("material_high_pct", "material_cost_high"),
        ):
            pct = uncertainty.get(pct_key)
            bound = uncertainty.get(bound_key)
            if pct is None or bound is None:
                errors.append(f"{product}: uncertainty missing {pct_key} or {bound_key}")
                continue
            if material_cost is not None:
                expected = round(material_cost * (1 + pct), 1)
                if abs(bound - expected) > 0.05:
                    errors.append(
                        f"{product}: {bound_key}={bound} inconsistent with "
                        f"material_cost × (1 + {pct_key}) ({expected})"
                    )

        onsite = entry.get("onsite_labor_hours_per_unit")
        for pct_key, bound_key in (
            ("labor_low_pct", "onsite_labor_hours_low"),
            ("labor_high_pct", "onsite_labor_hours_high"),
        ):
            pct = uncertainty.get(pct_key)
            bound = uncertainty.get(bound_key)
            if pct is None or bound is None:
                errors.append(f"{product}: uncertainty missing {pct_key} or {bound_key}")
                continue
            if onsite is not None:
                expected = round(onsite * (1 + pct), 2)
                if abs(bound - expected) > 0.01:
                    errors.append(
                        f"{product}: {bound_key}={bound} inconsistent with "
                        f"onsite_labor_hours_per_unit × (1 + {pct_key}) ({expected})"
                    )

        low_pct = uncertainty.get("material_low_pct")
        high_pct = uncertainty.get("material_high_pct")
        if low_pct is not None and high_pct is not None and low_pct > high_pct:
            errors.append(f"{product}: material_low_pct ({low_pct}) > material_high_pct ({high_pct})")

    return errors


def validate_observations(products_path: Path) -> list[str]:
    data = json.loads(products_path.read_text(encoding="utf-8"))
    entries = data.get("entries", {})
    if isinstance(entries, list):
        entries = {entry["product"]: entry for entry in entries}

    errors: list[str] = []
    for product, entry in entries.items():
        observations = entry.get("observations")
        if not observations:
            continue
        canonical_by_aspect: dict[str, bool] = {}
        for idx, obs in enumerate(observations):
            aspect = obs.get("aspect")
            if not aspect:
                errors.append(f"{product}: observations[{idx}] missing aspect")
                continue
            if obs.get("selects_canonical"):
                if canonical_by_aspect.get(aspect):
                    errors.append(
                        f"{product}: multiple observations with selects_canonical for aspect {aspect}"
                    )
                canonical_by_aspect[aspect] = True
                canonical_value = entry.get(aspect)
                if aspect == "demolition_hours_per_unit":
                    demolition = entry.get("demolition") or {}
                    canonical_value = demolition.get("hours_per_unit")
                elif aspect == "demolition_disposal_cost":
                    demolition = entry.get("demolition") or {}
                    canonical_value = demolition.get("disposal_cost")
                obs_value = obs.get("value")
                if canonical_value is not None and obs_value is not None:
                    if abs(float(canonical_value) - float(obs_value)) > 0.05:
                        errors.append(
                            f"{product}: observation selects_canonical for {aspect} "
                            f"({obs_value}) differs from canonical ({canonical_value})"
                        )
    return errors


def validate_coverage() -> int:
    result = subprocess.run(
        [sys.executable, str(LIST_SCRIPT), "--check"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(result.stdout, file=sys.stderr)
        print(result.stderr, file=sys.stderr)
    return result.returncode


def validate_data_quality(products_path: Path) -> list[str]:
    data = json.loads(products_path.read_text(encoding="utf-8"))
    entries = data.get("entries", {})
    if isinstance(entries, list):
        entries = {entry["product"]: entry for entry in entries}

    errors: list[str] = []
    for product, entry in entries.items():
        material_cost = entry.get("material_cost")
        if material_cost is None or float(material_cost) <= 0:
            errors.append(f"{product}: material_cost must be positive (got {material_cost})")
        if entry.get("price_unit") not in VALID_PRICE_UNITS:
            errors.append(f"{product}: invalid price_unit ({entry.get('price_unit')})")

        observations = entry.get("observations") or []
        canonical = [
            obs
            for obs in observations
            if obs.get("selects_canonical") and obs.get("reference_source")
        ]
        if not canonical:
            errors.append(
                f"{product}: needs at least one observation with selects_canonical "
                "and a non-empty reference_source"
            )
    return errors


def main() -> int:
    if not SCHEMA.is_file():
        raise SystemExit(f"Missing schema: {SCHEMA}")
    for path in (PRODUCTS, REGIONAL):
        if not path.is_file():
            raise SystemExit(f"Missing data file: {path}. Run build_baseline_products.py first.")

    coverage_code = validate_coverage()
    if coverage_code:
        return coverage_code

    code = run_validate("BaselinePriceBook", PRODUCTS)
    if code:
        return code
    code = run_validate("RegionalCostBenchmarkBook", REGIONAL)
    if code:
        return code

    geometry_errors = validate_carbon_geometry(PRODUCTS)
    if geometry_errors:
        print("Carbon geometry validation failed:", file=sys.stderr)
        for error in geometry_errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    uncertainty_errors = validate_uncertainty(PRODUCTS)
    if uncertainty_errors:
        print("Uncertainty validation failed:", file=sys.stderr)
        for error in uncertainty_errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    observation_errors = validate_observations(PRODUCTS)
    if observation_errors:
        print("Observation validation failed:", file=sys.stderr)
        for error in observation_errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    data_quality_errors = validate_data_quality(PRODUCTS)
    if data_quality_errors:
        print("Data quality validation failed:", file=sys.stderr)
        for error in data_quality_errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print("Baseline price JSON validates against contract/cost/baseline_cost_schema.yaml")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
