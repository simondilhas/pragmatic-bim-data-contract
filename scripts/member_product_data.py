"""Source data for abstract member product classifications.

Covers the four product schemes that carry prices for linear and safety members:
column, beam, stair, and railing products. Consumed by
scripts/generate_element_vocabulary.py and scripts/validate_element_classification.py.
"""

from __future__ import annotations

from dataclasses import dataclass

ABSTRACT_BASE = "https://example.org/abstract/"
ISSUED = "2026-09-16"
LICENSE = "https://creativecommons.org/licenses/by/4.0/"
SOURCE = "https://github.com/simondilhas/pragmatic-bim-data-contract"
CREATOR = "abstract.foundation"


@dataclass(frozen=True)
class MemberProduct:
    notation: str
    label_en: str
    label_de: str
    definition_en: str
    definition_de: str


@dataclass(frozen=True)
class MemberProductScheme:
    slug: str
    filename: str
    prefix: str
    notation_prefix: str
    identifier: str
    title_en: str
    title_de: str
    definition_en: str
    definition_de: str
    scope_note_en: str
    scope_note_de: str
    price_unit: str
    default_product: str
    products: list[MemberProduct]

    @property
    def ns(self) -> str:
        return f"{ABSTRACT_BASE}{self.slug}/"


COLUMN_PRODUCTS: list[MemberProduct] = [
    MemberProduct(
        "CLP-STEEL",
        "Steel column",
        "Stahlstütze",
        "Hot-rolled, welded, or hollow-section steel column including corrosion protection and fire "
        "protection coating where required. Priced per m3 of gross member volume.",
        "Warmgewalzte, geschweisste oder Hohlprofil-Stahlstütze inklusive Korrosionsschutz und "
        "erforderlichem Brandschutzanstrich. Preis pro m3 Bruttovolumen.",
    ),
    MemberProduct(
        "CLP-TIMBER",
        "Timber column",
        "Holzstütze",
        "Solid, glued-laminated, or engineered timber column including connectors and surface "
        "treatment. Priced per m3 of gross member volume.",
        "Vollholz-, Brettschichtholz- oder Konstruktionsholzstütze inklusive Verbindungsmittel und "
        "Oberflächenbehandlung. Preis pro m3 Bruttovolumen.",
    ),
    MemberProduct(
        "CLP-RC",
        "Reinforced concrete column",
        "Stahlbetonstütze",
        "Cast-in-situ or precast reinforced concrete column including formwork and reinforcement. "
        "Priced per m3 of gross member volume.",
        "Ortbeton- oder Fertigteil-Stahlbetonstütze inklusive Schalung und Bewehrung. Preis pro m3 "
        "Bruttovolumen.",
    ),
    MemberProduct(
        "CLP-OTH",
        "Other or unknown column",
        "Andere oder unbekannte Stütze",
        "Fallback for columns whose material or product type is not yet determined, or for composite "
        "and masonry columns outside the listed types.",
        "Rückfallwert für Stützen mit noch unbestimmtem Material oder Produkttyp sowie für Verbund- "
        "und Mauerwerksstützen ausserhalb der gelisteten Typen.",
    ),
]

BEAM_PRODUCTS: list[MemberProduct] = [
    MemberProduct(
        "BMP-STEEL",
        "Steel beam",
        "Stahlträger",
        "Hot-rolled or welded steel beam used as downstand or upstand girder, including corrosion and "
        "fire protection where required. Priced per m3 of gross member volume.",
        "Warmgewalzter oder geschweisster Stahlträger als Unterzug oder Überzug, inklusive Korrosions- "
        "und erforderlichem Brandschutz. Preis pro m3 Bruttovolumen.",
    ),
    MemberProduct(
        "BMP-TIMBER",
        "Timber beam",
        "Holzträger",
        "Solid, glued-laminated, or engineered timber beam including connectors and surface treatment. "
        "Priced per m3 of gross member volume.",
        "Vollholz-, Brettschichtholz- oder Konstruktionsholzträger inklusive Verbindungsmittel und "
        "Oberflächenbehandlung. Preis pro m3 Bruttovolumen.",
    ),
    MemberProduct(
        "BMP-RC",
        "Reinforced concrete beam",
        "Stahlbetonträger",
        "Cast-in-situ or precast reinforced concrete downstand or upstand beam including formwork and "
        "reinforcement. Priced per m3 of gross member volume.",
        "Ortbeton- oder Fertigteil-Stahlbetonträger als Unterzug oder Überzug inklusive Schalung und "
        "Bewehrung. Preis pro m3 Bruttovolumen.",
    ),
    MemberProduct(
        "BMP-OTH",
        "Other or unknown beam",
        "Anderer oder unbekannter Träger",
        "Fallback for beams whose material or product type is not yet determined, or for composite and "
        "masonry beams outside the listed types.",
        "Rückfallwert für Träger mit noch unbestimmtem Material oder Produkttyp sowie für Verbund- und "
        "Mauerwerksträger ausserhalb der gelisteten Typen.",
    ),
]

STAIR_PRODUCTS: list[MemberProduct] = [
    MemberProduct(
        "SRP-STEEL",
        "Steel stair",
        "Stahltreppe",
        "Steel stair flight with stringers and treads of steel or grating, including landings and "
        "surface protection. Priced per m3 of gross flight volume.",
        "Stahltreppenlauf mit Wangen und Stufen aus Stahl oder Gitterrost, inklusive Podeste und "
        "Oberflächenschutz. Preis pro m3 Bruttovolumen des Laufs.",
    ),
    MemberProduct(
        "SRP-TIMBER",
        "Timber stair",
        "Holztreppe",
        "Timber stair flight with stringers, treads, and risers of solid or engineered timber, "
        "including surface treatment. Priced per m3 of gross flight volume.",
        "Holztreppenlauf mit Wangen, Tritt- und Setzstufen aus Vollholz oder Konstruktionsholz, "
        "inklusive Oberflächenbehandlung. Preis pro m3 Bruttovolumen des Laufs.",
    ),
    MemberProduct(
        "SRP-RC",
        "Reinforced concrete stair",
        "Stahlbetontreppe",
        "Cast-in-situ or precast reinforced concrete stair flight including formwork, reinforcement, "
        "and acoustic bearings. Priced per m3 of gross flight volume.",
        "Ortbeton- oder Fertigteil-Stahlbetontreppenlauf inklusive Schalung, Bewehrung und "
        "Schallschutzlager. Preis pro m3 Bruttovolumen des Laufs.",
    ),
    MemberProduct(
        "SRP-OTH",
        "Other or unknown stair",
        "Andere oder unbekannte Treppe",
        "Fallback for stairs whose material or product type is not yet determined, or for stone and "
        "composite stairs outside the listed types.",
        "Rückfallwert für Treppen mit noch unbestimmtem Material oder Produkttyp sowie für Stein- und "
        "Verbundtreppen ausserhalb der gelisteten Typen.",
    ),
]

RAILING_PRODUCTS: list[MemberProduct] = [
    MemberProduct(
        "RAP-BALUSTER",
        "Metal baluster railing",
        "Staketengeländer",
        "Railing with vertical metal balusters between posts and handrail, galvanized or coated. "
        "Priced per m of railing length.",
        "Geländer mit vertikalen Metallstaketen zwischen Pfosten und Handlauf, verzinkt oder "
        "beschichtet. Preis pro m Geländerlänge.",
    ),
    MemberProduct(
        "RAP-GLASS-FRAMED",
        "Framed laminated glass railing",
        "VSG-Geländer gerahmt",
        "Railing with laminated safety glass infill held in a metal frame or channel profile. Priced "
        "per m of railing length.",
        "Geländer mit Verbundsicherheitsglas-Füllung in Metallrahmen oder Klemmprofil. Preis pro m "
        "Geländerlänge.",
    ),
    MemberProduct(
        "RAP-GLASS-POINT",
        "Point-fixed structural glass railing",
        "VSG-Geländer punktgehalten",
        "All-glass railing with laminated safety glass panes on point fixings or a base clamping "
        "profile, without vertical posts. Priced per m of railing length.",
        "Ganzglasgeländer mit Verbundsicherheitsglasscheiben auf Punkthaltern oder Klemmprofil im "
        "Fussbereich, ohne vertikale Pfosten. Preis pro m Geländerlänge.",
    ),
    MemberProduct(
        "RAP-PERFORATED-METAL",
        "Perforated or expanded metal railing",
        "Lochblech- oder Streckmetallgeländer",
        "Railing with perforated sheet or expanded metal infill panels in a metal frame. Priced per m "
        "of railing length.",
        "Geländer mit Lochblech- oder Streckmetallfüllung in Metallrahmen. Preis pro m Geländerlänge.",
    ),
    MemberProduct(
        "RAP-CABLE-MESH",
        "Cable or mesh infill railing",
        "Drahtseil- oder Netzgeländer",
        "Railing with tensioned stainless steel cables or woven mesh infill between posts. Priced per m "
        "of railing length.",
        "Geländer mit gespannten Edelstahlseilen oder Netzfüllung zwischen den Pfosten. Preis pro m "
        "Geländerlänge.",
    ),
    MemberProduct(
        "RAP-TIMBER",
        "Timber railing",
        "Holzgeländer",
        "Railing with timber posts, rails, and infill including surface treatment. Priced per m of "
        "railing length.",
        "Geländer mit Pfosten, Riegeln und Füllung aus Holz inklusive Oberflächenbehandlung. Preis pro "
        "m Geländerlänge.",
    ),
    MemberProduct(
        "RAP-PARAPET-SOLID",
        "Solid parapet",
        "Massive Brüstung",
        "Fall protection formed by a solid concrete or masonry parapet with coping, acting as the "
        "guarding element. Priced per m of parapet length.",
        "Absturzsicherung als massive Beton- oder Mauerwerksbrüstung mit Abdeckung, die die "
        "Schutzfunktion übernimmt. Preis pro m Brüstungslänge.",
    ),
    MemberProduct(
        "RAP-HANDRAIL",
        "Handrail only",
        "Handlauf",
        "Wall-mounted or post-mounted handrail without infill, used where no fall protection infill is "
        "required. Priced per m of handrail length.",
        "Wand- oder pfostenmontierter Handlauf ohne Füllung, wo keine Absturzsicherung mit Füllung "
        "erforderlich ist. Preis pro m Handlauflänge.",
    ),
    MemberProduct(
        "RAP-OTH",
        "Other or unknown railing",
        "Anderes oder unbekanntes Geländer",
        "Fallback for railings whose product type is not yet determined, or for special guarding "
        "systems outside the listed types.",
        "Rückfallwert für Geländer mit noch unbestimmtem Produkttyp sowie für spezielle "
        "Absturzsicherungssysteme ausserhalb der gelisteten Typen.",
    ),
]


SCHEMES: list[MemberProductScheme] = [
    MemberProductScheme(
        slug="column-product",
        filename="column-products.skos.ttl",
        prefix="clp",
        notation_prefix="CLP-",
        identifier="ColumnProduct",
        title_en="Abstract column products",
        title_de="Abstrakte Stützenprodukte",
        definition_en="Product-type classification for vertical load-bearing members (columns and "
        "posts) by dominant construction material. Used to attach baseline unit prices and embodied "
        "carbon references to the column element of the pragmaticBIM Elementplan.",
        definition_de="Produkttyp-Klassifikation für vertikale Tragglieder (Stützen und Pfosten) nach "
        "dominierendem Baustoff. Dient der Zuordnung von Basis-Einheitspreisen und Referenzen für "
        "graue Emissionen zum Stützenbauteil des pragmaticBIM Elementplans.",
        scope_note_en="Assign one concept per column element. Baseline cost is priced per m3 of gross "
        "member volume (Qto_ColumnBaseQuantities.GrossVolume). Covers architectural (ARC-COLUMN) and "
        "structural column elements; distinct from wall separator products (SWP) used for walls.",
        scope_note_de="Ein Konzept pro Stützenbauteil zuordnen. Basiskosten pro m3 Bruttovolumen "
        "(Qto_ColumnBaseQuantities.GrossVolume). Umfasst architektonische (ARC-COLUMN) und tragende "
        "Stützenbauteile; abgegrenzt von Wandtrennelementprodukten (SWP).",
        price_unit="m3",
        default_product="CLP-OTH",
        products=COLUMN_PRODUCTS,
    ),
    MemberProductScheme(
        slug="beam-product",
        filename="beam-products.skos.ttl",
        prefix="bmp",
        notation_prefix="BMP-",
        identifier="BeamProduct",
        title_en="Abstract beam products",
        title_de="Abstrakte Trägerprodukte",
        definition_en="Product-type classification for horizontal load-bearing members (downstand and "
        "upstand beams, girders) by dominant construction material. Used to attach baseline unit "
        "prices and embodied carbon references to the beam element of the pragmaticBIM Elementplan.",
        definition_de="Produkttyp-Klassifikation für horizontale Tragglieder (Unterzüge, Überzüge, "
        "Träger) nach dominierendem Baustoff. Dient der Zuordnung von Basis-Einheitspreisen und "
        "Referenzen für graue Emissionen zum Trägerbauteil des pragmaticBIM Elementplans.",
        scope_note_en="Assign one concept per beam element. Baseline cost is priced per m3 of gross "
        "member volume (Qto_BeamBaseQuantities.GrossVolume). Covers architectural (ARC-BEAM) and "
        "structural beam elements; distinct from slab separator products (SSP) used for slabs.",
        scope_note_de="Ein Konzept pro Trägerbauteil zuordnen. Basiskosten pro m3 Bruttovolumen "
        "(Qto_BeamBaseQuantities.GrossVolume). Umfasst architektonische (ARC-BEAM) und tragende "
        "Trägerbauteile; abgegrenzt von Deckentrennelementprodukten (SSP).",
        price_unit="m3",
        default_product="BMP-OTH",
        products=BEAM_PRODUCTS,
    ),
    MemberProductScheme(
        slug="stair-product",
        filename="stair-products.skos.ttl",
        prefix="srp",
        notation_prefix="SRP-",
        identifier="StairProduct",
        title_en="Abstract stair products",
        title_de="Abstrakte Treppenprodukte",
        definition_en="Product-type classification for stair flights and landings by dominant "
        "construction material. Used to attach baseline unit prices and embodied carbon references to "
        "the stair element of the pragmaticBIM Elementplan.",
        definition_de="Produkttyp-Klassifikation für Treppenläufe und Podeste nach dominierendem "
        "Baustoff. Dient der Zuordnung von Basis-Einheitspreisen und Referenzen für graue Emissionen "
        "zum Treppenbauteil des pragmaticBIM Elementplans.",
        scope_note_en="Assign one concept per stair element. Baseline cost is priced per m3 of gross "
        "flight volume (Qto_StairBaseQuantities.GrossVolume), not per flight or per step. Railings on "
        "stairs are classified separately with railing products (RAP).",
        scope_note_de="Ein Konzept pro Treppenbauteil zuordnen. Basiskosten pro m3 Bruttovolumen des "
        "Laufs (Qto_StairBaseQuantities.GrossVolume), nicht pro Lauf oder Stufe. Geländer an Treppen "
        "werden separat mit Geländerprodukten (RAP) klassifiziert.",
        price_unit="m3",
        default_product="SRP-OTH",
        products=STAIR_PRODUCTS,
    ),
    MemberProductScheme(
        slug="railing-product",
        filename="railing-products.skos.ttl",
        prefix="rap",
        notation_prefix="RAP-",
        identifier="RailingProduct",
        title_en="Abstract railing products",
        title_de="Abstrakte Geländerprodukte",
        definition_en="Product-type classification for railings, balustrades, and fall protection "
        "systems by infill and construction type. Used to attach baseline unit prices and embodied "
        "carbon references to the railing element of the pragmaticBIM Elementplan.",
        definition_de="Produkttyp-Klassifikation für Geländer, Brüstungen und "
        "Absturzsicherungssysteme nach Füllung und Konstruktionsart. Dient der Zuordnung von "
        "Basis-Einheitspreisen und Referenzen für graue Emissionen zum Geländerbauteil des pragmatic "
        "BIM Elementplans.",
        scope_note_en="Assign one concept per railing element. Baseline cost is priced per m of "
        "railing length (Qto_RailingBaseQuantities.Length). Complements the IFC railing "
        "PredefinedType, which records the guarding function rather than the product type.",
        scope_note_de="Ein Konzept pro Geländerbauteil zuordnen. Basiskosten pro m Geländerlänge "
        "(Qto_RailingBaseQuantities.Length). Ergänzt den IFC-PredefinedType für Geländer, der die "
        "Schutzfunktion und nicht den Produkttyp abbildet.",
        price_unit="m",
        default_product="RAP-OTH",
        products=RAILING_PRODUCTS,
    ),
]


ALL_PRODUCTS: list[MemberProduct] = [p for scheme in SCHEMES for p in scheme.products]


def scheme_by_prefix(prefix: str) -> MemberProductScheme:
    for scheme in SCHEMES:
        if scheme.prefix == prefix:
            return scheme
    raise KeyError(prefix)
