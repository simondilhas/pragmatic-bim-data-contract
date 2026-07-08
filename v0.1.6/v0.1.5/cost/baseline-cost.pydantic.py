from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'cost',
     'default_range': 'string',
     'description': 'Cost enrichment layer for the pragmatic BIM data contract. '
                    'BaselinePriceBook entries are bound to abstract SKOS product '
                    'notations from classification vocabularies. All price-book '
                    'monetary values are EUR and net (VAT excluded). '
                    'RegionalCostBenchmarkBook supplies material_factor, '
                    'fx_to_eur, labor_unit_price, and labor_factor for '
                    'installed-cost calculation in regional currency.',
     'id': 'https://schema.pragmaticbim.ch/cost/baseline-cost',
     'imports': ['linkml:types', 'baseline_cost_schema_enums'],
     'license': 'MIT',
     'name': 'baseline_cost_schema',
     'prefixes': {'cost': {'prefix_prefix': 'cost',
                           'prefix_reference': 'https://schema.pragmaticbim.ch/cost/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'}},
     'see_also': ['https://schema.pragmaticbim.ch/cost/baseline-cost'],
     'source_file': 'contract/cost/baseline_cost_schema.yaml',
     'title': 'Baseline unit prices and regional cost benchmarks'} )

class CurrencyEnum(str, Enum):
    """
    ISO 4217 currency for regional labor rates. Price-book material is always EUR.
    """
    Euro = "EUR"
    Swiss_franc = "CHF"
    Pound_sterling = "GBP"
    US_dollar = "USD"


class PriceUnitEnum(str, Enum):
    """
    Native trade unit for a baseline unit price.
    """
    Square_metre = "m2"
    Cubic_metre = "m3"
    Piece = "pcs"


class KbobMatchTypeEnum(str, Enum):
    closeMatch = "closeMatch"
    relatedMatch = "relatedMatch"
    layer_recipe = "layer_recipe"


class CarbonMethodEnum(str, Enum):
    direct = "direct"
    density = "density"
    area_yield = "area_yield"
    piece_area = "piece_area"
    layer_recipe_sum = "layer_recipe_sum"
    unmapped = "unmapped"
    unconverted = "unconverted"


class ProvenanceStatusEnum(str, Enum):
    """
    How the unit-price point estimate was sourced and validated.
    """
    Estimated = "estimated"
    """
    First fill — not yet checked against anything.
    """
    Expert_reviewed = "expert_reviewed"
    """
    A person with domain knowledge sanity-checked the value.
    """
    Reference_calibrated = "reference_calibrated"
    """
    Cross-checked against KBOB, CWICR, ÖKOBAUDAT, or similar reference data.
    """
    Project_validated = "project_validated"
    """
    Held up against realised cost on a real project.
    """


class PriceObservationAspectEnum(str, Enum):
    """
    Which canonical UnitPriceEntry slot an observation records. Monetary aspects are EUR net (VAT excluded); labor aspects are person-hours per price_unit; waste_pct and transport_pct are fractions (0–1).
    """
    Material_cost = "material_cost"
    """
    Ex-works material cost per price_unit in EUR.
    """
    Waste_allowance = "waste_pct"
    """
    Waste allowance as a fraction of material cost.
    """
    Transport_allowance = "transport_pct"
    """
    Transport-to-site allowance as a fraction of material cost.
    """
    Onsite_labor_hours = "onsite_labor_hours_per_unit"
    """
    Onsite installation labor in person-hours per price_unit.
    """
    Offsite_labor_hours = "offsite_labor_hours_per_unit"
    """
    Factory/offsite labor in person-hours per price_unit.
    """
    Demolition_labor_hours = "demolition_hours_per_unit"
    """
    Demolition labor hours per price unit.
    """
    Demolition_disposal_cost = "demolition_disposal_cost"
    """
    Disposal cost per price unit in EUR.
    """



class BaselinePriceBook(ConfiguredBaseModel):
    """
    Container for baseline unit-price entries. Monetary values on entries are always EUR and net (VAT excluded; schema invariant). Labor on entries is hours only; labor money lives on RegionalBenchmark.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'cost:BaselinePriceBook',
         'from_schema': 'https://schema.pragmaticbim.ch/cost/baseline-cost',
         'slot_usage': {'anchor_region': {'name': 'anchor_region', 'required': True},
                        'entries': {'inlined': True,
                                    'multivalued': True,
                                    'name': 'entries',
                                    'range': 'UnitPriceEntry'},
                        'issued': {'name': 'issued', 'required': True}},
         'tree_root': True})

    version: Optional[str] = Field(default=None, description="""Edition label (for example v12).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaselinePriceBook', 'RegionalCostBenchmarkBook']} })
    issued: date = Field(default=..., description="""Publication date of this dataset edition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaselinePriceBook', 'RegionalCostBenchmarkBook']} })
    anchor_region: str = Field(default=..., description="""Region code where material_factor and labor_factor are 1.0 (for example DE_MU).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaselinePriceBook', 'RegionalCostBenchmarkBook']} })
    source: Optional[str] = Field(default=None, description="""Path or URI of the editorial source workbook.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaselinePriceBook', 'RegionalCostBenchmarkBook']} })
    license: Optional[str] = Field(default=None, description="""License URI for the dataset (CC BY 4.0 for benchmark data).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaselinePriceBook', 'RegionalCostBenchmarkBook']} })
    disclaimer: Optional[str] = Field(default=None, description="""Pointer to notice/disclaimer text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaselinePriceBook', 'RegionalCostBenchmarkBook']} })
    carbon_source: Optional[str] = Field(default=None, description="""Human-readable name of the carbon reference database.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaselinePriceBook']} })
    carbon_source_version: Optional[str] = Field(default=None, description="""Version of the carbon reference database (for example 8.02).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaselinePriceBook']} })
    entries: Optional[dict[str, UnitPriceEntry]] = Field(default=None, description="""Baseline unit-price entries keyed by product notation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaselinePriceBook']} })


class UnitPriceEntry(ConfiguredBaseModel):
    """
    One baseline unit price for one abstract SKOS product concept. All monetary amounts are net (VAT excluded). Canonical scalar slots (material_cost, labor hours, etc.) are the resolved benchmark used for installed-cost calculation; optional observations record contributor inputs and reference sources used to derive or challenge those canonical values.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'cost:UnitPriceEntry',
         'from_schema': 'https://schema.pragmaticbim.ch/cost/baseline-cost',
         'slot_usage': {'material_cost': {'name': 'material_cost',
                                          'range': 'decimal',
                                          'required': True},
                        'observations': {'inlined': True,
                                         'multivalued': True,
                                         'name': 'observations',
                                         'range': 'PriceObservation'},
                        'offsite_labor_hours_per_unit': {'ifabsent': '0.0',
                                                         'minimum_value': 0,
                                                         'name': 'offsite_labor_hours_per_unit',
                                                         'range': 'float'},
                        'onsite_labor_hours_per_unit': {'minimum_value': 0,
                                                        'name': 'onsite_labor_hours_per_unit',
                                                        'range': 'float',
                                                        'required': True},
                        'price_unit': {'name': 'price_unit',
                                       'range': 'PriceUnitEnum',
                                       'required': True},
                        'product': {'identifier': True,
                                    'name': 'product',
                                    'range': 'ConceptNotation',
                                    'required': True},
                        'provenance_status': {'ifabsent': 'estimated',
                                              'name': 'provenance_status',
                                              'range': 'ProvenanceStatusEnum'},
                        'transport_pct': {'minimum_value': 0,
                                          'name': 'transport_pct',
                                          'range': 'float',
                                          'required': True},
                        'waste_pct': {'minimum_value': 0,
                                      'name': 'waste_pct',
                                      'range': 'float',
                                      'required': True}}})

    product: str = Field(default=..., description="""Abstract product SKOS notation (for example WICP-WOOD). Foreign key into classification vocabularies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UnitPriceEntry']} })
    product_uri: Optional[str] = Field(default=None, description="""Derived SKOS concept IRI for the product notation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UnitPriceEntry']} })
    material_cost: Decimal = Field(default=..., description="""Ex-works material cost per price_unit in EUR (net, VAT excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['UnitPriceEntry']} })
    price_unit: PriceUnitEnum = Field(default=..., description="""Quantity unit the material cost refers to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UnitPriceEntry']} })
    waste_pct: float = Field(default=..., description="""Waste allowance as a fraction of material cost (0–1).""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['UnitPriceEntry']} })
    transport_pct: float = Field(default=..., description="""Transport-to-site (A4) allowance as a fraction of material cost (0–1).""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['UnitPriceEntry']} })
    delivered_material_cost: Optional[Decimal] = Field(default=None, description="""Derived delivered material cost in EUR (material_cost × (1 + waste_pct) × (1 + transport_pct)). Net, VAT excluded. Optional in authored input.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UnitPriceEntry']} })
    onsite_labor_hours_per_unit: float = Field(default=..., description="""Onsite installation labor in person-hours per price_unit.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['UnitPriceEntry']} })
    offsite_labor_hours_per_unit: Optional[float] = Field(default=0.0, description="""Factory/offsite labor in person-hours per price_unit.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['UnitPriceEntry'], 'ifabsent': '0.0'} })
    demolition: Optional[DemolitionCost] = Field(default=None, description="""Disassembly/demolition benchmark for this product.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UnitPriceEntry']} })
    kbob: Optional[KbobCarbonReference] = Field(default=None, description="""KBOB ecobilans carbon reference for this product.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UnitPriceEntry']} })
    carbon_per_price_unit: Optional[CarbonEstimate] = Field(default=None, description="""Generated embodied-carbon estimate; not authored.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UnitPriceEntry']} })
    uncertainty: Optional[PriceUncertainty] = Field(default=None, description="""Relative uncertainty band for material cost and labor hours. Derived low/high amounts are computed from point estimates at generation time.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UnitPriceEntry']} })
    provenance_status: Optional[ProvenanceStatusEnum] = Field(default=ProvenanceStatusEnum.estimated, description="""How the unit-price point estimate was sourced and validated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UnitPriceEntry', 'PriceObservation'], 'ifabsent': 'estimated'} })
    observations: Optional[list[PriceObservation]] = Field(default=None, description="""Optional contributor or reference observations for canonical slot values. Parent entry scalars remain the resolved benchmark for costing.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UnitPriceEntry']} })


class PriceObservation(ConfiguredBaseModel):
    """
    One contributed or reference value for a canonical UnitPriceEntry slot. Observations support multi-party authoring and audit; they do not replace the canonical scalar fields on the parent entry.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'cost:PriceObservation',
         'from_schema': 'https://schema.pragmaticbim.ch/cost/baseline-cost',
         'slot_usage': {'aspect': {'name': 'aspect',
                                   'range': 'PriceObservationAspectEnum',
                                   'required': True},
                        'contributed_at': {'name': 'contributed_at', 'range': 'date'},
                        'contributor': {'description': 'Person or team that supplied '
                                                       'the observation (optional '
                                                       'display name or id).',
                                        'name': 'contributor'},
                        'notes': {'description': 'Free-text context (edition, region, '
                                                 'scope, assumptions).',
                                  'name': 'notes'},
                        'provenance_status': {'name': 'provenance_status',
                                              'range': 'ProvenanceStatusEnum'},
                        'reference_source': {'description': 'Reference dataset, '
                                                            'organisation, or document '
                                                            'identifier.',
                                             'name': 'reference_source',
                                             'required': True},
                        'selects_canonical': {'description': 'When true, marks this '
                                                             'observation as the '
                                                             'chosen source for the '
                                                             "parent entry's canonical "
                                                             'value for the given '
                                                             'aspect.',
                                              'name': 'selects_canonical',
                                              'range': 'boolean'},
                        'value': {'name': 'value',
                                  'range': 'decimal',
                                  'required': True}}})

    aspect: PriceObservationAspectEnum = Field(default=..., description="""Canonical slot this observation applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PriceObservation']} })
    value: Decimal = Field(default=..., description="""Observed numeric value in the same unit as the parent aspect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PriceObservation']} })
    reference_source: str = Field(default=..., description="""Reference dataset, organisation, or document identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PriceObservation']} })
    contributor: Optional[str] = Field(default=None, description="""Person or team that supplied the observation (optional display name or id).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PriceObservation']} })
    contributed_at: Optional[date] = Field(default=None, description="""Date the observation was recorded or published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PriceObservation']} })
    provenance_status: Optional[ProvenanceStatusEnum] = Field(default=None, description="""How the unit-price point estimate was sourced and validated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UnitPriceEntry', 'PriceObservation']} })
    notes: Optional[str] = Field(default=None, description="""Free-text context (edition, region, scope, assumptions).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PriceObservation']} })
    selects_canonical: Optional[bool] = Field(default=None, description="""When true, marks this observation as the chosen source for the parent entry's canonical value for the given aspect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PriceObservation']} })


class DemolitionCost(ConfiguredBaseModel):
    """
    Disassembly/demolition labor and disposal per price unit (EUR, net, VAT excluded).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'cost:DemolitionCost',
         'from_schema': 'https://schema.pragmaticbim.ch/cost/baseline-cost',
         'slot_usage': {'disposal_cost': {'minimum_value': 0,
                                          'name': 'disposal_cost',
                                          'range': 'decimal'},
                        'hours_per_unit': {'minimum_value': 0,
                                           'name': 'hours_per_unit',
                                           'range': 'float'},
                        'unit': {'name': 'unit', 'range': 'PriceUnitEnum'}}})

    hours_per_unit: Optional[float] = Field(default=None, description="""Demolition labor hours per price unit.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['DemolitionCost']} })
    disposal_cost: Optional[Decimal] = Field(default=None, description="""Disposal cost per price unit in EUR (net, VAT excluded).""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['DemolitionCost']} })
    unit: Optional[PriceUnitEnum] = Field(default=None, description="""Unit for demolition quantities.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DemolitionCost']} })


class KbobCarbonReference(ConfiguredBaseModel):
    """
    Reference to KBOB ecobilans benchmark concept IRIs. Indicator values are resolved from kbob-ecobilans-lca-factors.json, not stored here.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'cost:KbobCarbonReference',
         'from_schema': 'https://schema.pragmaticbim.ch/cost/baseline-cost',
         'slot_usage': {'benchmark_uris': {'multivalued': True,
                                           'name': 'benchmark_uris',
                                           'range': 'uriorcurie'}}})

    primary_match_type: Optional[KbobMatchTypeEnum] = Field(default=None, description="""SKOS mapping match type used for the primary carbon reference.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KbobCarbonReference']} })
    benchmark_uris: Optional[list[str]] = Field(default=None, description="""KBOB ecobilans concept IRIs for carbon lookup.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KbobCarbonReference']} })
    carbon_method: Optional[CarbonMethodEnum] = Field(default=None, description="""Method used to normalize carbon to the price unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['KbobCarbonReference']} })


class CarbonEstimate(ConfiguredBaseModel):
    """
    Generated embodied-carbon estimate per price unit (optional output). Unit-conversion geometry is stored in typed slots — not in assumptions. density_kg_m3 for method density; mass_per_area_kg_m2 for area_yield; area_per_piece_m2 for piece_area. Optional thickness_m documents derived mass_per_area when thickness × density was used.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'cost:CarbonEstimate',
         'from_schema': 'https://schema.pragmaticbim.ch/cost/baseline-cost',
         'slot_usage': {'area_per_piece_m2': {'minimum_value': 0,
                                              'name': 'area_per_piece_m2',
                                              'range': 'float'},
                        'components': {'inlined': True,
                                       'multivalued': True,
                                       'name': 'components',
                                       'range': 'CarbonComponent'},
                        'density_kg_m3': {'minimum_value': 0,
                                          'name': 'density_kg_m3',
                                          'range': 'float'},
                        'mass_per_area_kg_m2': {'minimum_value': 0,
                                                'name': 'mass_per_area_kg_m2',
                                                'range': 'float'},
                        'method': {'name': 'method', 'range': 'CarbonMethodEnum'},
                        'thickness_m': {'minimum_value': 0,
                                        'name': 'thickness_m',
                                        'range': 'float'}}})

    gwp_kg_co2eq: Optional[float] = Field(default=None, description="""Global warming potential in kg CO2eq per price unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CarbonEstimate', 'CarbonComponent']} })
    method: Optional[CarbonMethodEnum] = Field(default=None, description="""Carbon conversion method.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CarbonEstimate']} })
    density_kg_m3: Optional[float] = Field(default=None, description="""Material density (kg/m³) used when method is density (price m³, KBOB kg).""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['CarbonEstimate']} })
    mass_per_area_kg_m2: Optional[float] = Field(default=None, description="""Mass per m² (kg/m²) used when method is area_yield (price m², KBOB kg).""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['CarbonEstimate']} })
    area_per_piece_m2: Optional[float] = Field(default=None, description="""Area per piece (m²/pcs) used when method is piece_area (price pcs, KBOB m²).""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['CarbonEstimate']} })
    thickness_m: Optional[float] = Field(default=None, description="""Optional layer thickness (m) when mass_per_area_kg_m2 was derived as thickness_m × density_kg_m3.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['CarbonEstimate']} })
    assumptions: Optional[str] = Field(default=None, description="""Human-readable notes only (for example layer_recipe quantity_basis). Not used for unit conversion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CarbonEstimate']} })
    components: Optional[list[CarbonComponent]] = Field(default=None, description="""Layer components for layer_recipe_sum carbon totals.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CarbonEstimate']} })


class PriceUncertainty(ConfiguredBaseModel):
    """
    Relative uncertainty band around point material cost and labor hours. Percent slots are signed fractions relative to the point estimate (for example material_low_pct -0.12 → low = point × 0.88). Derived EUR and hour bounds are optional generator output for convenience.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'cost:PriceUncertainty',
         'from_schema': 'https://schema.pragmaticbim.ch/cost/baseline-cost',
         'slot_usage': {'labor_high_pct': {'minimum_value': 0,
                                           'name': 'labor_high_pct',
                                           'range': 'float',
                                           'required': True},
                        'labor_low_pct': {'maximum_value': 0,
                                          'name': 'labor_low_pct',
                                          'range': 'float',
                                          'required': True},
                        'material_high_pct': {'minimum_value': 0,
                                              'name': 'material_high_pct',
                                              'range': 'float',
                                              'required': True},
                        'material_low_pct': {'maximum_value': 0,
                                             'name': 'material_low_pct',
                                             'range': 'float',
                                             'required': True}}})

    material_low_pct: float = Field(default=..., description="""Lower material bound as signed fraction of material_cost (≤ 0).""", le=0, json_schema_extra = { "linkml_meta": {'domain_of': ['PriceUncertainty']} })
    material_high_pct: float = Field(default=..., description="""Upper material bound as signed fraction of material_cost (≥ 0).""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['PriceUncertainty']} })
    labor_low_pct: float = Field(default=..., description="""Lower labor bound as signed fraction of labor hours (≤ 0).""", le=0, json_schema_extra = { "linkml_meta": {'domain_of': ['PriceUncertainty']} })
    labor_high_pct: float = Field(default=..., description="""Upper labor bound as signed fraction of labor hours (≥ 0).""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['PriceUncertainty']} })
    material_cost_low: Optional[Decimal] = Field(default=None, description="""Derived lower material_cost in EUR (net, VAT excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PriceUncertainty']} })
    material_cost_high: Optional[Decimal] = Field(default=None, description="""Derived upper material_cost in EUR (net, VAT excluded).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PriceUncertainty']} })
    delivered_material_cost_low: Optional[Decimal] = Field(default=None, description="""Derived lower delivered_material_cost in EUR.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PriceUncertainty']} })
    delivered_material_cost_high: Optional[Decimal] = Field(default=None, description="""Derived upper delivered_material_cost in EUR.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PriceUncertainty']} })
    onsite_labor_hours_low: Optional[float] = Field(default=None, description="""Derived lower onsite labor hours per price unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PriceUncertainty']} })
    onsite_labor_hours_high: Optional[float] = Field(default=None, description="""Derived upper onsite labor hours per price unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PriceUncertainty']} })
    offsite_labor_hours_low: Optional[float] = Field(default=None, description="""Derived lower offsite labor hours per price unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PriceUncertainty']} })
    offsite_labor_hours_high: Optional[float] = Field(default=None, description="""Derived upper offsite labor hours per price unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PriceUncertainty']} })


class CarbonComponent(ConfiguredBaseModel):
    """
    One layer or row contributing to a layer_recipe_sum carbon total.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'cost:CarbonComponent',
         'from_schema': 'https://schema.pragmaticbim.ch/cost/baseline-cost',
         'slot_usage': {'notation': {'name': 'notation', 'range': 'ConceptNotation'}}})

    notation: Optional[str] = Field(default=None, description="""SKOS notation of a layer component product.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CarbonComponent']} })
    kbob_id: Optional[str] = Field(default=None, description="""KBOB ecobilans row id (for example 05.005).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CarbonComponent']} })
    quantity_per_price_unit: Optional[float] = Field(default=None, description="""Layer quantity per one parent price unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CarbonComponent']} })
    quantity_unit: Optional[str] = Field(default=None, description="""Unit of the layer quantity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CarbonComponent']} })
    gwp_kg_co2eq: Optional[float] = Field(default=None, description="""Global warming potential in kg CO2eq per price unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CarbonEstimate', 'CarbonComponent']} })


class RegionalCostBenchmarkBook(ConfiguredBaseModel):
    """
    Regional material and labor benchmarks paired with a BaselinePriceBook. Installed cost in regional currency uses fx_to_eur for material EUR→local and labor_unit_price in local currency. All monetary rates are net (VAT excluded).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'cost:RegionalCostBenchmarkBook',
         'from_schema': 'https://schema.pragmaticbim.ch/cost/baseline-cost',
         'slot_usage': {'anchor_region': {'name': 'anchor_region', 'required': True},
                        'issued': {'name': 'issued', 'required': True},
                        'regions': {'inlined': True,
                                    'multivalued': True,
                                    'name': 'regions',
                                    'range': 'RegionalBenchmark'}},
         'tree_root': True})

    version: Optional[str] = Field(default=None, description="""Edition label (for example v12).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaselinePriceBook', 'RegionalCostBenchmarkBook']} })
    issued: date = Field(default=..., description="""Publication date of this dataset edition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaselinePriceBook', 'RegionalCostBenchmarkBook']} })
    anchor_region: str = Field(default=..., description="""Region code where material_factor and labor_factor are 1.0 (for example DE_MU).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaselinePriceBook', 'RegionalCostBenchmarkBook']} })
    source: Optional[str] = Field(default=None, description="""Path or URI of the editorial source workbook.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaselinePriceBook', 'RegionalCostBenchmarkBook']} })
    license: Optional[str] = Field(default=None, description="""License URI for the dataset (CC BY 4.0 for benchmark data).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaselinePriceBook', 'RegionalCostBenchmarkBook']} })
    disclaimer: Optional[str] = Field(default=None, description="""Pointer to notice/disclaimer text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaselinePriceBook', 'RegionalCostBenchmarkBook']} })
    regions: Optional[dict[str, RegionalBenchmark]] = Field(default=None, description="""Regional benchmarks keyed by region code.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RegionalCostBenchmarkBook']} })


class RegionalBenchmark(ConfiguredBaseModel):
    """
    Material and labor factors for one region.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'cost:RegionalBenchmark',
         'from_schema': 'https://schema.pragmaticbim.ch/cost/baseline-cost',
         'slot_usage': {'code': {'identifier': True, 'name': 'code', 'required': True},
                        'currency': {'name': 'currency',
                                     'range': 'CurrencyEnum',
                                     'required': True},
                        'fx_to_eur': {'minimum_value': 0,
                                      'name': 'fx_to_eur',
                                      'range': 'float',
                                      'required': True},
                        'labor_factor': {'ifabsent': '1.0',
                                         'minimum_value': 0,
                                         'name': 'labor_factor',
                                         'range': 'float',
                                         'required': True},
                        'labor_unit_price': {'minimum_value': 0,
                                             'name': 'labor_unit_price',
                                             'range': 'decimal',
                                             'required': True},
                        'material_factor': {'minimum_value': 0,
                                            'name': 'material_factor',
                                            'range': 'float',
                                            'required': True},
                        'offsite_labor_unit_price': {'minimum_value': 0,
                                                     'name': 'offsite_labor_unit_price',
                                                     'range': 'decimal'}}})

    code: str = Field(default=..., description="""Region code (for example CH_ZH, DE_MU).""", json_schema_extra = { "linkml_meta": {'domain_of': ['RegionalBenchmark']} })
    currency: CurrencyEnum = Field(default=..., description="""Local currency for labor rates and installed-cost total.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RegionalBenchmark']} })
    material_factor: float = Field(default=..., description="""Regional material price level vs anchor region (DE_MU = 1.0).""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['RegionalBenchmark']} })
    fx_to_eur: float = Field(default=..., description="""Material FX only. Multiply local currency → EUR (for example 1 CHF × 0.95). EUR book → local uses delivered_eur / fx_to_eur.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['RegionalBenchmark']} })
    labor_factor: float = Field(default=1.0, description="""Regional labor cost multiplier (default 1.0).""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['RegionalBenchmark'], 'ifabsent': '1.0'} })
    labor_unit_price: Decimal = Field(default=..., description="""Onsite installation labor rate per hour in currency (net, VAT excluded).""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['RegionalBenchmark']} })
    offsite_labor_unit_price: Optional[Decimal] = Field(default=None, description="""Factory/offsite labor rate per hour in currency (net, VAT excluded).""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['RegionalBenchmark']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
BaselinePriceBook.model_rebuild()
UnitPriceEntry.model_rebuild()
PriceObservation.model_rebuild()
DemolitionCost.model_rebuild()
KbobCarbonReference.model_rebuild()
CarbonEstimate.model_rebuild()
PriceUncertainty.model_rebuild()
CarbonComponent.model_rebuild()
RegionalCostBenchmarkBook.model_rebuild()
RegionalBenchmark.model_rebuild()
