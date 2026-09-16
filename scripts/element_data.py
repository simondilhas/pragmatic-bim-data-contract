"""Source data for the abstract building element classification and its product bridge.

One row per element of the pragmatic BIM element plan that carries cost. Each element
declares exactly one reference quantity (the IFC base quantity used for take-off), the
price unit that quantity is billed in, and the product scheme whose concepts differentiate
the element for pricing.

Element codes, labels, IFC classes, and quantity sets follow the
elementplan_pragmaticbim_swiss_data_add_ons repository, which is authoritative.
Consumed by scripts/generate_element_vocabulary.py and
scripts/validate_element_classification.py.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from baseline_prices_common import SCHEME_IRI_PREFIXES  # noqa: E402

EL_NS = "https://example.org/abstract/building-element/"
ISSUED = "2026-09-16"
LICENSE = "https://creativecommons.org/licenses/by/4.0/"
SOURCE = "https://github.com/simondilhas/pragmatic-bim-data-contract"
CREATOR = "abstract.foundation"

# Sentinel reference quantity for elements priced by instance cardinality rather than
# by an IFC base quantity.
COUNT_QUANTITY = "count"


@dataclass(frozen=True)
class ProductSchemeRef:
    """A product SKOS scheme that differentiates an element for pricing."""

    prefix: str
    notation_prefix: str
    default_product: str

    @property
    def ns(self) -> str:
        return SCHEME_IRI_PREFIXES[self.notation_prefix]


PRODUCT_SCHEMES: dict[str, ProductSchemeRef] = {
    "swp": ProductSchemeRef("swp", "SWP-", "SWP-OTH"),
    "ssp": ProductSchemeRef("ssp", "SSP-", "SSP-OTH"),
    "facp": ProductSchemeRef("facp", "FaCP-", "FaCP-OTHER"),
    "wcp": ProductSchemeRef("wcp", "WCP-", "WCP-OTH"),
    "fcp": ProductSchemeRef("fcp", "FCP-", "FCP-OTH"),
    "ccp": ProductSchemeRef("ccp", "CCP-", "CCP-OTH"),
    "rcp": ProductSchemeRef("rcp", "RCP-", "RCP-OTH"),
    "fdp": ProductSchemeRef("fdp", "FDP-", "FDP-OTH"),
    "wicp": ProductSchemeRef("wicp", "WICP-", "WICP-OTH"),
    "dcp": ProductSchemeRef("dcp", "DCP-", "DCP-OTH"),
    "clp": ProductSchemeRef("clp", "CLP-", "CLP-OTH"),
    "bmp": ProductSchemeRef("bmp", "BMP-", "BMP-OTH"),
    "srp": ProductSchemeRef("srp", "SRP-", "SRP-OTH"),
    "rap": ProductSchemeRef("rap", "RAP-", "RAP-OTH"),
}


@dataclass(frozen=True)
class BuildingElement:
    notation: str
    label_en: str
    label_de: str
    definition_en: str
    definition_de: str
    reference_quantity: str
    quantity_pset: str
    price_unit: str
    ifc_class: str
    product_scheme: str = ""
    scope_note_en: str = ""
    scope_note_de: str = ""


ELEMENTS: list[BuildingElement] = [
    BuildingElement(
        "ARC-WALL-EXT",
        "Exterior wall",
        "Aussenwand",
        "Exterior wall as building envelope, modelled as a multi-layer component in early phases and "
        "for simple facades.",
        "Aussenwand als Gebäudehülle, in frühen Phasen und bei einfachen Fassaden als "
        "Mehrschichtbauteil modelliert.",
        "NetSideArea",
        "Qto_WallBaseQuantities",
        "m2",
        "IfcWall",
        "swp",
    ),
    BuildingElement(
        "ARC-WALL-INT-LB",
        "Load-bearing interior wall",
        "Tragende Innenwand",
        "Load-bearing interior wall separating interior spaces and carrying vertical loads.",
        "Tragende Innenwand, die Innenräume trennt und vertikale Lasten abträgt.",
        "NetSideArea",
        "Qto_WallBaseQuantities",
        "m2",
        "IfcWall",
        "swp",
    ),
    BuildingElement(
        "ARC-WALL-INT",
        "Non-load-bearing interior wall",
        "Nichttragende Innenwand",
        "Non-load-bearing interior wall or partition separating interior spaces without carrying "
        "vertical loads.",
        "Nichttragende Innenwand oder Trennwand, die Innenräume ohne Lastabtrag trennt.",
        "NetSideArea",
        "Qto_WallBaseQuantities",
        "m2",
        "IfcWall",
        "swp",
    ),
    BuildingElement(
        "ARC-WALL-CLAD-EXT",
        "Facade cladding",
        "Fassadenbekleidung",
        "Exterior facade cladding or ventilated facade system modelled as a separate covering layer on "
        "the envelope wall.",
        "Aussenseitige Fassadenbekleidung oder vorgehängte Fassade, als separate Bekleidungsschicht "
        "auf der Hüllwand modelliert.",
        "NetArea",
        "Qto_CoveringBaseQuantities",
        "m2",
        "IfcCovering",
        "facp",
    ),
    BuildingElement(
        "ARC-WALL-CLAD",
        "Interior wall covering",
        "Innenwandbekleidung",
        "Interior wall covering, lining, or finish applied to the room side of a wall.",
        "Innenseitige Wandbekleidung, Verkleidung oder Oberflächenausbau auf der Raumseite einer Wand.",
        "NetArea",
        "Qto_CoveringBaseQuantities",
        "m2",
        "IfcCovering",
        "wcp",
    ),
    BuildingElement(
        "ARC-FLOOR-COV",
        "Floor build-up",
        "Bodenaufbau",
        "Floor build-up above the structural slab, including screed, separation layers, and the visible "
        "floor finish.",
        "Bodenaufbau über der Rohdecke, inklusive Unterlagsboden, Trennschichten und sichtbarem "
        "Bodenbelag.",
        "NetArea",
        "Qto_CoveringBaseQuantities",
        "m2",
        "IfcCovering",
        "fcp",
    ),
    BuildingElement(
        "ARC-CEILING",
        "Suspended ceiling",
        "Abhangdecke",
        "Suspended or applied ceiling below the structural slab, including substructure.",
        "Abgehängte oder direkt applizierte Decke unter der Rohdecke, inklusive Unterkonstruktion.",
        "NetArea",
        "Qto_CoveringBaseQuantities",
        "m2",
        "IfcCovering",
        "ccp",
    ),
    BuildingElement(
        "ARC-SLAB-BASE",
        "Base slab",
        "Bodenplatte",
        "Lowest floor slab bearing on the ground, including waterproofing and insulation layers where "
        "modelled as part of the slab.",
        "Unterste auf dem Boden aufliegende Platte, inklusive Abdichtung und Dämmung, sofern als Teil "
        "der Platte modelliert.",
        "GrossVolume",
        "Qto_SlabBaseQuantities",
        "m3",
        "IfcSlab",
        "fdp",
    ),
    BuildingElement(
        "ARC-SLAB-FLOOR",
        "Floor slab",
        "Geschossdecke",
        "Structural slab between storeys, excluding floor build-up and suspended ceiling.",
        "Tragende Decke zwischen Geschossen, ohne Bodenaufbau und Abhangdecke.",
        "GrossVolume",
        "Qto_SlabBaseQuantities",
        "m3",
        "IfcSlab",
        "ssp",
    ),
    BuildingElement(
        "ARC-SLAB-BALCONY",
        "Balcony slab",
        "Balkon",
        "Cantilevered or supported exterior balcony slab, including thermal separation to the "
        "structure.",
        "Auskragende oder abgestützte Balkonplatte im Aussenbereich, inklusive thermischer Trennung zur "
        "Tragstruktur.",
        "GrossArea",
        "Qto_SlabBaseQuantities",
        "m2",
        "IfcSlab",
        "ssp",
    ),
    BuildingElement(
        "ARC-ROOF-FLAT",
        "Flat roof",
        "Flachdach",
        "Flat roof assembly including structural slab, insulation, and waterproofing membrane.",
        "Flachdachaufbau inklusive Tragdecke, Dämmung und Abdichtung.",
        "GrossArea",
        "Qto_SlabBaseQuantities",
        "m2",
        "IfcSlab",
        "rcp",
    ),
    BuildingElement(
        "ARC-ROOF-PITCH",
        "Pitched roof",
        "Steildach",
        "Pitched roof assembly including structure, insulation, and roof covering.",
        "Steildachaufbau inklusive Konstruktion, Dämmung und Dacheindeckung.",
        "GrossArea",
        "Qto_RoofBaseQuantities",
        "m2",
        "IfcRoof",
        "rcp",
    ),
    BuildingElement(
        "ARC-ROOF-DRAIN",
        "Tapered roof insulation",
        "Gefälledämmung",
        "Tapered insulation layer forming the drainage slope of a flat roof.",
        "Keilförmige Dämmschicht zur Bildung des Entwässerungsgefälles auf dem Flachdach.",
        "NetArea",
        "Qto_CoveringBaseQuantities",
        "m2",
        "IfcCovering",
        "",
        "No product scheme is defined yet; tapered insulation is currently priced only as part of the "
        "parent flat roof assembly.",
        "Noch kein Produktschema definiert; die Gefälledämmung wird derzeit nur als Teil des "
        "übergeordneten Flachdachaufbaus bepreist.",
    ),
    BuildingElement(
        "ARC-FOOTING",
        "Footing",
        "Fundament",
        "Pad, strip, or raft footing transferring loads into the ground.",
        "Einzel-, Streifen- oder Plattenfundament zur Lastabtragung in den Baugrund.",
        "GrossVolume",
        "Qto_FootingBaseQuantities",
        "m3",
        "IfcFooting",
        "fdp",
    ),
    BuildingElement(
        "ARC-COLUMN",
        "Column",
        "Stütze",
        "Vertical load-bearing member transferring loads to slabs, beams, or footings.",
        "Vertikales Tragglied, das Lasten in Decken, Träger oder Fundamente abträgt.",
        "GrossVolume",
        "Qto_ColumnBaseQuantities",
        "m3",
        "IfcColumn",
        "clp",
    ),
    BuildingElement(
        "ARC-BEAM",
        "Beam",
        "Unterzug oder Überzug",
        "Horizontal load-bearing member spanning between columns or walls, modelled as a downstand or "
        "upstand beam.",
        "Horizontales Tragglied zwischen Stützen oder Wänden, als Unterzug oder Überzug modelliert.",
        "GrossVolume",
        "Qto_BeamBaseQuantities",
        "m3",
        "IfcBeam",
        "bmp",
    ),
    BuildingElement(
        "ARC-STAIR",
        "Stair",
        "Treppe",
        "Stair flight with landings connecting storeys.",
        "Treppenlauf mit Podesten zur Verbindung von Geschossen.",
        "GrossVolume",
        "Qto_StairBaseQuantities",
        "m3",
        "IfcStair",
        "srp",
    ),
    BuildingElement(
        "ARC-RAILING",
        "Railing and fall protection",
        "Geländer und Absturzsicherung",
        "Railing, balustrade, or parapet providing fall protection along slabs, stairs, and openings.",
        "Geländer, Brüstung oder Absturzsicherung entlang von Decken, Treppen und Öffnungen.",
        "Length",
        "Qto_RailingBaseQuantities",
        "m",
        "IfcRailing",
        "rap",
    ),
    BuildingElement(
        "WINDOW",
        "Window",
        "Fenster",
        "Window in an exterior or interior wall, priced by the area of the wall opening it fills.",
        "Fenster in einer Aussen- oder Innenwand, bepreist über die Fläche der Wandöffnung.",
        "Area",
        "Qto_WindowBaseQuantities",
        "m2",
        "IfcWindow",
        "wicp",
        "The Area base quantity is not yet published on the WINDOW element in the element plan, which "
        "exposes only OverallWidth and OverallHeight; derive the opening area from those two until the "
        "quantity is added.",
        "Die Basismenge Area ist beim Bauteil WINDOW im Elementplan noch nicht publiziert, dort stehen "
        "nur OverallWidth und OverallHeight; die Öffnungsfläche bis dahin daraus ableiten.",
    ),
    BuildingElement(
        "DOOR",
        "Door",
        "Tür",
        "Door in an exterior or interior wall, priced by the area of the wall opening it fills.",
        "Tür in einer Aussen- oder Innenwand, bepreist über die Fläche der Wandöffnung.",
        "Area",
        "Qto_DoorBaseQuantities",
        "m2",
        "IfcDoor",
        "dcp",
    ),
    BuildingElement(
        "FURN",
        "Furniture",
        "Möbel",
        "Loose or fitted furniture item recorded as a countable object.",
        "Losmöbel oder Einbaumöbel, als zählbares Objekt erfasst.",
        COUNT_QUANTITY,
        "",
        "pcs",
        "IfcFurniture",
        "",
        "Priced per piece from instance cardinality; the element plan publishes no base quantity for "
        "furniture. No product scheme is defined yet.",
        "Bepreisung pro Stück über die Anzahl der Instanzen; der Elementplan publiziert keine "
        "Basismenge für Möbel. Noch kein Produktschema definiert.",
    ),
    BuildingElement(
        "LAN-TREE",
        "Tree",
        "Baum",
        "Existing or new tree in the site or landscape model, recorded as a countable object.",
        "Bestehender oder neuer Baum im Umgebungs- oder Landschaftsmodell, als zählbares Objekt "
        "erfasst.",
        COUNT_QUANTITY,
        "",
        "pcs",
        "IfcGeographicElement",
        "",
        "Priced per piece from instance cardinality; the element plan publishes no base quantity for "
        "trees. No product scheme is defined yet.",
        "Bepreisung pro Stück über die Anzahl der Instanzen; der Elementplan publiziert keine "
        "Basismenge für Bäume. Noch kein Produktschema definiert.",
    ),
]


def elements_with_products() -> list[BuildingElement]:
    return [e for e in ELEMENTS if e.product_scheme]


def scheme_for(element: BuildingElement) -> ProductSchemeRef:
    return PRODUCT_SCHEMES[element.product_scheme]


def used_scheme_prefixes() -> list[str]:
    seen: list[str] = []
    for element in elements_with_products():
        if element.product_scheme not in seen:
            seen.append(element.product_scheme)
    return seen


def ttl_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')
