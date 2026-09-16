# Baseline unit prices — notice and disclaimer

## Disclaimer

These baseline unit prices and embodied-carbon estimates are provided free of
charge under [CC BY 4.0](LICENSE) for informational and early-design use only.
They are not cost estimates, life-cycle assessments, or professional advice.
The authors and contributors disclaim all liability for decisions made using
this data.

Data is provided **as is**, without warranty of any kind, express or implied,
including but not limited to accuracy, completeness, fitness for a particular
purpose, or non-infringement. You assume all risk arising from use of this
data.

## Authored benchmark data

Unit prices and labor hour benchmarks in
`PragmaticBIM_Strict_SKOS_Unified_Prices-v12.xlsx` are indicative reference
values for abstract SKOS product classifications. Regional labor rates,
regional material factors, waste and transport allowances, and
disassembly/demolition costs are illustrative benchmarks only.

### EUR baseline and adaptation assumptions

- Material costs are **re-baselined from CHF to a EUR (DE-level) anchor** via
  `chf_to_eur_base_factor` in `cost-adjustments.json` (default `0.80`, combining
  a CHF→EUR FX rate with removal of the Swiss price premium). The EUR base
  therefore represents a eurozone/Germany price level, not a Swiss one.
- Regional adaptation uses `material_factor` and `fx_to_eur` in
  `regional-material-benchmarks.json` (Germany `DE_MU` = 1.00). FX rates are
  volatile; treat them as a dated input, not a constant.

### Cost scope

- **Included:** delivered material (ex-works material + waste allowance +
  A4 transport-to-site), onsite installation labor, offsite/factory labor for
  prefab elements, and separate disassembly/demolition labor + disposal cost.
- **Excluded:** contingency (project-management scope), design/professional
  fees, VAT, plant/equipment beyond what is embedded in labor rates, and any
  site-specific preliminaries.

Waste and transport are expressed as a share of material cost; demolition
`disposal_cost` is per price unit. Labor-hour corrections (e.g. in-situ
concrete adjusted to include formwork and rebar) and offsite hours are recorded
in `labor-overrides.json` and applied over the Excel source, which is never
modified by the generator.

**License:** [CC BY 4.0](LICENSE) — free to use and adapt with attribution.

Suggested attribution:

> Baseline unit prices (v12), pragmatic-bim-data-contract contributors,
> https://github.com/simondilhas/pragmatic-bim-data-contract — CC BY 4.0

## Third-party data — KBOB ecobilans

Embodied carbon values are derived from KBOB ecobilans construction material
LCA factors:

- **Source file:** `Oekobilanzdaten_ Baubereich_Donne_ecobilans_construction_2009-1-2022_v8.02.xlsx`
- **Version:** 8.02
- **Programme:** [KBOB / IPB / SIA ecobilans](https://www.kbob.admin.ch)

KBOB ecobilans data is third-party reference data. Verify compliance with
KBOB/IPB terms for your use case. Carbon figures in the generated JSON are
**indicative estimates** based on best-fit mappings from abstract product
classifications to KBOB material rows; they are not project-specific LCAs.

Mappings and factors are stored under `classification/mapping/` and
regenerated with:

```bash
python scripts/generate_kbob_ecobilans_vocabulary.py
python scripts/generate_baseline_unit_prices.py
```

## Unit conversion assumptions

Where baseline price units differ from KBOB reference units (e.g. m³ concrete
from kg factors, doors priced per piece from m² KBOB rows), default
conversion assumptions are documented in
`classification/mapping/kbob-ecobilans-price-unit-defaults.json` and echoed
in the `assumptions` field of each product's `carbon_per_price_unit` in
`baseline-products.json`.

Composite products (HBV slabs, window frame+glazing, ETICS facades) use layer
recipes in `classification/mapping/kbob-ecobilans-layer-recipes.json`.
