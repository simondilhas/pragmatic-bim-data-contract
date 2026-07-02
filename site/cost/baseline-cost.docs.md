# Baseline unit prices and regional cost benchmarks

Cost enrichment layer for the pragmatic BIM data contract. BaselinePriceBook entries are bound to abstract SKOS product notations from classification vocabularies. All price-book monetary values are EUR and net (VAT excluded). RegionalCostBenchmarkBook supplies material_factor, fx_to_eur, labor_unit_price, and labor_factor for installed-cost calculation in regional currency.

URI: https://schema.pragmaticbim.ch/cost/baseline-cost

Name: baseline_cost_schema



## Classes

| Class | Description |
| --- | --- |
| [BaselinePriceBook](BaselinePriceBook.md) | Container for baseline unit-price entries. Monetary values on entries are always EUR and net (VAT excluded; schema invariant). Labor on entries is hours only; labor money lives on RegionalBenchmark. |
| [CarbonComponent](CarbonComponent.md) | One layer or row contributing to a layer_recipe_sum carbon total. |
| [CarbonEstimate](CarbonEstimate.md) | Generated embodied-carbon estimate per price unit (optional output). Unit-conversion geometry is stored in typed slots — not in assumptions. density_kg_m3 for method density; mass_per_area_kg_m2 for area_yield; area_per_piece_m2 for piece_area. Optional thickness_m documents derived mass_per_area when thickness × density was used. |
| [DemolitionCost](DemolitionCost.md) | Disassembly/demolition labor and disposal per price unit (EUR, net, VAT excluded). |
| [KbobCarbonReference](KbobCarbonReference.md) | Reference to KBOB ecobilans benchmark concept IRIs. Indicator values are resolved from kbob-ecobilans-lca-factors.json, not stored here. |
| [PriceObservation](PriceObservation.md) | One contributed or reference value for a canonical UnitPriceEntry slot. Observations support multi-party authoring and audit; they do not replace the canonical scalar fields on the parent entry. |
| [PriceUncertainty](PriceUncertainty.md) | Relative uncertainty band around point material cost and labor hours. Percent slots are signed fractions relative to the point estimate (for example material_low_pct -0.12 → low = point × 0.88). Derived EUR and hour bounds are optional generator output for convenience. |
| [RegionalBenchmark](RegionalBenchmark.md) | Material and labor factors for one region. |
| [RegionalCostBenchmarkBook](RegionalCostBenchmarkBook.md) | Regional material and labor benchmarks paired with a BaselinePriceBook. Installed cost in regional currency uses fx_to_eur for material EUR→local and labor_unit_price in local currency. All monetary rates are net (VAT excluded). |
| [UnitPriceEntry](UnitPriceEntry.md) | One baseline unit price for one abstract SKOS product concept. All monetary amounts are net (VAT excluded). Canonical scalar slots (material_cost, labor hours, etc.) are the resolved benchmark used for installed-cost calculation; optional observations record contributor inputs and reference sources used to derive or challenge those canonical values. |



## Slots

| Slot | Description |
| --- | --- |
| [anchor_region](anchor_region.md) | Region code where material_factor and labor_factor are 1.0 (for example DE_MU). |
| [area_per_piece_m2](area_per_piece_m2.md) | Area per piece (m²/pcs) used when method is piece_area (price pcs, KBOB m²). |
| [aspect](aspect.md) | Canonical slot this observation applies to. |
| [assumptions](assumptions.md) | Human-readable notes only (for example layer_recipe quantity_basis). Not used for unit conversion. |
| [benchmark_uris](benchmark_uris.md) | KBOB ecobilans concept IRIs for carbon lookup. |
| [carbon_method](carbon_method.md) | Method used to normalize carbon to the price unit. |
| [carbon_per_price_unit](carbon_per_price_unit.md) | Generated embodied-carbon estimate; not authored. |
| [carbon_source](carbon_source.md) | Human-readable name of the carbon reference database. |
| [carbon_source_version](carbon_source_version.md) | Version of the carbon reference database (for example 8.02). |
| [code](code.md) | Region code (for example CH_ZH, DE_MU). |
| [components](components.md) | Layer components for layer_recipe_sum carbon totals. |
| [contributed_at](contributed_at.md) | Date the observation was recorded or published. |
| [contributor](contributor.md) | Person or team that supplied the observation. |
| [currency](currency.md) | Local currency for labor rates and installed-cost total. |
| [delivered_material_cost](delivered_material_cost.md) | Derived delivered material cost in EUR (material_cost × (1 + waste_pct) × (1 + transport_pct)). Net, VAT excluded. Optional in authored input. |
| [delivered_material_cost_high](delivered_material_cost_high.md) | Derived upper delivered_material_cost in EUR. |
| [delivered_material_cost_low](delivered_material_cost_low.md) | Derived lower delivered_material_cost in EUR. |
| [demolition](demolition.md) | Disassembly/demolition benchmark for this product. |
| [density_kg_m3](density_kg_m3.md) | Material density (kg/m³) used when method is density (price m³, KBOB kg). |
| [disclaimer](disclaimer.md) | Pointer to notice/disclaimer text. |
| [disposal_cost](disposal_cost.md) | Disposal cost per price unit in EUR (net, VAT excluded). |
| [entries](entries.md) | Baseline unit-price entries keyed by product notation. |
| [fx_to_eur](fx_to_eur.md) | Material FX only. Multiply local currency → EUR (for example 1 CHF × 0.95). EUR book → local uses delivered_eur / fx_to_eur. |
| [gwp_kg_co2eq](gwp_kg_co2eq.md) | Global warming potential in kg CO2eq per price unit. |
| [hours_per_unit](hours_per_unit.md) | Demolition labor hours per price unit. |
| [issued](issued.md) | Publication date of this dataset edition. |
| [kbob](kbob.md) | KBOB ecobilans carbon reference for this product. |
| [kbob_id](kbob_id.md) | KBOB ecobilans row id (for example 05.005). |
| [labor_factor](labor_factor.md) | Regional labor cost multiplier (default 1.0). |
| [labor_high_pct](labor_high_pct.md) | Upper labor bound as signed fraction of labor hours (≥ 0). |
| [labor_low_pct](labor_low_pct.md) | Lower labor bound as signed fraction of labor hours (≤ 0). |
| [labor_unit_price](labor_unit_price.md) | Onsite installation labor rate per hour in currency (net, VAT excluded). |
| [license](license.md) | License URI for the dataset (CC BY 4.0 for benchmark data). |
| [mass_per_area_kg_m2](mass_per_area_kg_m2.md) | Mass per m² (kg/m²) used when method is area_yield (price m², KBOB kg). |
| [material_cost](material_cost.md) | Ex-works material cost per price_unit in EUR (net, VAT excluded). |
| [material_cost_high](material_cost_high.md) | Derived upper material_cost in EUR (net, VAT excluded). |
| [material_cost_low](material_cost_low.md) | Derived lower material_cost in EUR (net, VAT excluded). |
| [material_factor](material_factor.md) | Regional material price level vs anchor region (DE_MU = 1.0). |
| [material_high_pct](material_high_pct.md) | Upper material bound as signed fraction of material_cost (≥ 0). |
| [material_low_pct](material_low_pct.md) | Lower material bound as signed fraction of material_cost (≤ 0). |
| [method](method.md) | Carbon conversion method. |
| [notation](notation.md) | SKOS notation of a layer component product. |
| [notes](notes.md) | Free-text context for the observation. |
| [observations](observations.md) | Optional contributor or reference observations for canonical slot values. Parent entry scalars remain the resolved benchmark for costing. |
| [offsite_labor_hours_high](offsite_labor_hours_high.md) | Derived upper offsite labor hours per price unit. |
| [offsite_labor_hours_low](offsite_labor_hours_low.md) | Derived lower offsite labor hours per price unit. |
| [offsite_labor_hours_per_unit](offsite_labor_hours_per_unit.md) | Factory/offsite labor in person-hours per price_unit. |
| [offsite_labor_unit_price](offsite_labor_unit_price.md) | Factory/offsite labor rate per hour in currency (net, VAT excluded). |
| [onsite_labor_hours_high](onsite_labor_hours_high.md) | Derived upper onsite labor hours per price unit. |
| [onsite_labor_hours_low](onsite_labor_hours_low.md) | Derived lower onsite labor hours per price unit. |
| [onsite_labor_hours_per_unit](onsite_labor_hours_per_unit.md) | Onsite installation labor in person-hours per price_unit. |
| [price_unit](price_unit.md) | Quantity unit the material cost refers to. |
| [primary_match_type](primary_match_type.md) | SKOS mapping match type used for the primary carbon reference. |
| [product](product.md) | Abstract product SKOS notation (for example WICP-WOOD). Foreign key into classification vocabularies. |
| [product_uri](product_uri.md) | Derived SKOS concept IRI for the product notation. |
| [provenance_status](provenance_status.md) | How the unit-price point estimate was sourced and validated. |
| [quantity_per_price_unit](quantity_per_price_unit.md) | Layer quantity per one parent price unit. |
| [quantity_unit](quantity_unit.md) | Unit of the layer quantity. |
| [reference_source](reference_source.md) | Reference dataset, organisation, or document for this observation. |
| [regions](regions.md) | Regional benchmarks keyed by region code. |
| [selects_canonical](selects_canonical.md) | Whether this observation was selected for the parent canonical value. |
| [source](source.md) | Path or URI of the editorial source workbook. |
| [thickness_m](thickness_m.md) | Optional layer thickness (m) when mass_per_area_kg_m2 was derived as thickness_m × density_kg_m3. |
| [transport_pct](transport_pct.md) | Transport-to-site (A4) allowance as a fraction of material cost (0–1). |
| [uncertainty](uncertainty.md) | Relative uncertainty band for material cost and labor hours. Derived low/high amounts are computed from point estimates at generation time. |
| [unit](unit.md) | Unit for demolition quantities. |
| [value](value.md) | Observed numeric value in the same unit as the parent aspect. |
| [version](version.md) | Edition label (for example v12). |
| [waste_pct](waste_pct.md) | Waste allowance as a fraction of material cost (0–1). |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [CarbonMethodEnum](CarbonMethodEnum.md) |  |
| [CurrencyEnum](CurrencyEnum.md) | ISO 4217 currency for regional labor rates. Price-book material is always EUR. |
| [KbobMatchTypeEnum](KbobMatchTypeEnum.md) |  |
| [PriceObservationAspectEnum](PriceObservationAspectEnum.md) | Which canonical UnitPriceEntry slot an observation records. Monetary aspects are EUR net (VAT excluded); labor aspects are person-hours per price_unit; waste_pct and transport_pct are fractions (0–1). |
| [PriceUnitEnum](PriceUnitEnum.md) | Native trade unit for a baseline unit price. |
| [ProvenanceStatusEnum](ProvenanceStatusEnum.md) | How the unit-price point estimate was sourced and validated. |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [ConceptNotation](ConceptNotation.md) | A SKOS notation from the abstract product vocabularies. |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal specification |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form. |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form. |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model. |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model. |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF. |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular day |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
