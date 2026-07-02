#!/usr/bin/env python3
"""Shared helpers for the baseline unit-price pipeline.

Pure functions and constants reused by the product manifest, per-code entry
build, and (legacy) Excel/carbon enrichment scripts. No I/O side effects beyond
reading the values passed in.
"""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

LICENSE = "https://creativecommons.org/licenses/by/4.0/"
DISCLAIMER = "See baseline-unit-prices/NOTICE.md"
ANCHOR_REGION = "DE_MU"

# prefix -> human category label used by cost-adjustments.json
NOTATION_PREFIX_CATEGORIES = [
    ("SWP-", "Wall Separator"),
    ("SSP-", "Slab Separator"),
    ("DCP-", "Door Connector"),
    ("WICP-", "Window Connector"),
    ("FCP-", "Floor Covering"),
    ("WCP-", "Wall Covering"),
    ("CCP-", "Ceiling Covering"),
    ("FaCP-", "European Facade Covering"),
    ("FDP-", "Foundation Product"),
    ("RCP-", "Roof Covering"),
]

# notation suffixes marking LCA layer sub-concepts (excluded from entries/)
LAYER_NOTATION_SUFFIXES = (
    "-FRAME",
    "-GLZ-2P",
    "-INS",
    "-SUB",
    "-FIN",
    "-RENDER",
    "-MEM",
    "-CONC",
    "-STL",
    "-WOD",
    "-MSN",
)

LAYER_CATEGORY_BY_PREFIX = {
    "WICP-": "Window Connector Layer",
    "SSP-": "Slab Separator Layer",
    "FaCP-": "European Facade Covering Layer",
    "RCP-": "Roof Covering Layer",
    "FDP-": "Foundation Product Layer",
}

SCHEME_IRI_PREFIXES = {
    "SWP-": "https://example.org/abstract/wall-separator-product/",
    "SSP-": "https://example.org/abstract/slab-separator-product/",
    "DCP-": "https://example.org/abstract/door-connector-product/",
    "WICP-": "https://example.org/abstract/window-connector-product/",
    "FCP-": "https://example.org/abstract/floor-covering-product/",
    "WCP-": "https://example.org/abstract/wall-covering-product/",
    "CCP-": "https://example.org/abstract/ceiling-covering-product/",
    "FaCP-": "https://example.org/abstract/facade-covering-product/",
    "RCP-": "https://example.org/abstract/roof-covering-product/",
    "FDP-": "https://example.org/abstract/foundation-product/",
}

DEFAULT_UNCERTAINTY = {
    "material_low_pct": -0.12,
    "material_high_pct": 0.18,
    "labor_low_pct": -0.10,
    "labor_high_pct": 0.25,
}


# Notations priced by volume (m3) or by piece (pcs). Everything else is m2.
# PriceUnitEnum only permits m2 / m3 / pcs, so foundation elements priced by
# running metre in practice are anchored to their dominant concrete volume (m3).
PRICE_UNIT_M3 = {
    "SWP-ORTBETON",
    "SWP-PREFAB-CONC",
    "SSP-INSITU",
    "FDP-PAD",
    "FDP-STRIP",
    "FDP-RAFT",
    "FDP-RETAINING",
    "FDP-PILE",
    "FDP-MICRO-PILE",
    "FDP-OTH",
}
PRICE_UNIT_PCS = {"WICP-SKYLIGHT"}


def default_price_unit(notation: str) -> str:
    if notation.startswith("DCP-"):
        return "pcs"
    if notation in PRICE_UNIT_PCS:
        return "pcs"
    if notation in PRICE_UNIT_M3:
        return "m3"
    return "m2"


def notation_to_iri(notation: str) -> str:
    for prefix, base in SCHEME_IRI_PREFIXES.items():
        if notation.startswith(prefix):
            return f"{base}{notation}"
    return notation


def normalize_unit(unit: str | None) -> str:
    if not unit:
        return ""
    u = str(unit).strip().lower()
    replacements = {"m²": "m2", "m³": "m3", "m^2": "m2", "m^3": "m3", "piece": "pcs", "stück": "pcs"}
    return replacements.get(u, u)


def parse_float(value: object) -> float | None:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip()
    if not text:
        return None
    try:
        return float(text.replace(",", "."))
    except ValueError:
        return None


def infer_product_category(notation: str) -> str:
    if any(notation.endswith(suffix) for suffix in LAYER_NOTATION_SUFFIXES):
        for prefix, category in LAYER_CATEGORY_BY_PREFIX.items():
            if notation.startswith(prefix):
                return category
    for prefix, category in NOTATION_PREFIX_CATEGORIES:
        if notation.startswith(prefix):
            return category
    return ""


def resolve_uncertainty_config(notation: str, category: str, cost_adjustments: dict) -> dict:
    default = cost_adjustments.get("default_uncertainty", DEFAULT_UNCERTAINTY)
    cat_unc = cost_adjustments.get("categories", {}).get(category, {}).get("uncertainty", {})
    prod_unc = cost_adjustments.get("product_overrides", {}).get(notation, {}).get("uncertainty", {})
    return {**default, **cat_unc, **prod_unc}


def resolve_provenance_status(notation: str, cost_adjustments: dict, fallback: str = "estimated") -> str:
    default = cost_adjustments.get("default_provenance_status", fallback)
    override = cost_adjustments.get("product_overrides", {}).get(notation, {}).get("provenance_status")
    return str(override or default)


def scale_bounds(
    value: float | None,
    low_pct: float,
    high_pct: float,
    ndigits: int = 1,
) -> tuple[float | None, float | None]:
    if value is None:
        return None, None
    return round(value * (1 + low_pct), ndigits), round(value * (1 + high_pct), ndigits)


def build_uncertainty(price: dict, labor: dict, unc_cfg: dict) -> dict:
    uncertainty: dict[str, object] = {
        "material_low_pct": unc_cfg["material_low_pct"],
        "material_high_pct": unc_cfg["material_high_pct"],
        "labor_low_pct": unc_cfg["labor_low_pct"],
        "labor_high_pct": unc_cfg["labor_high_pct"],
    }

    mat_low, mat_high = scale_bounds(
        price.get("material_cost"),
        unc_cfg["material_low_pct"],
        unc_cfg["material_high_pct"],
    )
    if mat_low is not None and mat_high is not None:
        uncertainty["material_cost_low"] = mat_low
        uncertainty["material_cost_high"] = mat_high

    del_low, del_high = scale_bounds(
        price.get("delivered_material_cost"),
        unc_cfg["material_low_pct"],
        unc_cfg["material_high_pct"],
    )
    if del_low is not None and del_high is not None:
        uncertainty["delivered_material_cost_low"] = del_low
        uncertainty["delivered_material_cost_high"] = del_high

    onsite_low, onsite_high = scale_bounds(
        labor.get("onsite_hours_per_unit"),
        unc_cfg["labor_low_pct"],
        unc_cfg["labor_high_pct"],
        ndigits=2,
    )
    if onsite_low is not None and onsite_high is not None:
        uncertainty["onsite_labor_hours_low"] = onsite_low
        uncertainty["onsite_labor_hours_high"] = onsite_high

    offsite = labor.get("offsite_hours_per_unit") or 0.0
    if offsite:
        off_low, off_high = scale_bounds(
            offsite,
            unc_cfg["labor_low_pct"],
            unc_cfg["labor_high_pct"],
            ndigits=2,
        )
        if off_low is not None and off_high is not None:
            uncertainty["offsite_labor_hours_low"] = off_low
            uncertainty["offsite_labor_hours_high"] = off_high

    return uncertainty


def compute_delivered_material_cost(
    material_cost: float | None,
    waste_pct: float,
    transport_pct: float,
) -> float | None:
    if material_cost is None:
        return None
    return round(material_cost * (1 + waste_pct) * (1 + transport_pct), 1)


def format_demolition(demolition: dict) -> dict | None:
    if not demolition.get("hours_per_unit") and not demolition.get("disposal_cost"):
        return None
    entry: dict[str, object] = {"unit": demolition["unit"]}
    if demolition.get("hours_per_unit") is not None:
        entry["hours_per_unit"] = demolition["hours_per_unit"]
    if demolition.get("disposal_cost") is not None:
        entry["disposal_cost"] = demolition["disposal_cost"]
    return entry
