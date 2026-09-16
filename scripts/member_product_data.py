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
    description_en: str
    description_de: str


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
        "Vertical load-bearing member of steel transferring floor and roof loads to the structure "
        "below. Fabricated in the workshop as rolled, welded, or hollow section and erected on site "
        "with bolted or welded connections. Suitable for slender columns and long spans; corrosion "
        "and fire protection follow the exposure and the required fire resistance.",
        "Vertikales Tragglied aus Stahl, das Decken- und Dachlasten in die darunterliegende Struktur "
        "weiterleitet. Als Walz-, Schweiss- oder Hohlprofil im Werk gefertigt und vor Ort mit "
        "geschraubten oder geschweissten Anschlüssen montiert. Geeignet für schlanke Stützen und "
        "grosse Spannweiten; Korrosions- und Brandschutz richten sich nach Exposition und "
        "gefordertem Feuerwiderstand.",
    ),
    MemberProduct(
        "CLP-TIMBER",
        "Timber column",
        "Holzstütze",
        "Solid, glued-laminated, or engineered timber column including connectors and surface "
        "treatment. Priced per m3 of gross member volume.",
        "Vollholz-, Brettschichtholz- oder Konstruktionsholzstütze inklusive Verbindungsmittel und "
        "Oberflächenbehandlung. Preis pro m3 Bruttovolumen.",
        "Vertical load-bearing member of solid, glued laminated, or engineered timber transferring "
        "floor and roof loads downwards. Prefabricated to length and erected dry on site with steel "
        "connectors. Suitable for timber and hybrid structures where visible surfaces, low dead "
        "load, and short erection times are required.",
        "Vertikales Tragglied aus Vollholz, Brettschichtholz oder Konstruktionsholz, das Decken- und "
        "Dachlasten nach unten weiterleitet. Auf Länge vorgefertigt und vor Ort mit "
        "Stahlverbindungsmitteln trocken montiert. Geeignet für Holz- und Hybridtragwerke mit "
        "sichtbaren Oberflächen, geringem Eigengewicht und kurzer Montagezeit.",
    ),
    MemberProduct(
        "CLP-RC",
        "Reinforced concrete column",
        "Stahlbetonstütze",
        "Cast-in-situ or precast reinforced concrete column including formwork and reinforcement. "
        "Priced per m3 of gross member volume.",
        "Ortbeton- oder Fertigteil-Stahlbetonstütze inklusive Schalung und Bewehrung. Preis pro m3 "
        "Bruttovolumen.",
        "Vertical load-bearing member of reinforced concrete transferring floor and roof loads to "
        "the foundation. Either cast in place with formwork and reinforcement or delivered as a "
        "precast element and grouted into position. Suitable for high loads, inherent fire "
        "resistance, and columns integrated into concrete floor structures.",
        "Vertikales Tragglied aus Stahlbeton, das Decken- und Dachlasten in die Fundation "
        "weiterleitet. Entweder vor Ort mit Schalung und Bewehrung betoniert oder als Fertigteil "
        "geliefert und vergossen. Geeignet für hohe Lasten, inhärenten Feuerwiderstand und in "
        "Betondecken integrierte Stützen.",
    ),
    MemberProduct(
        "CLP-OTH",
        "Other or unknown column",
        "Andere oder unbekannte Stütze",
        "Fallback for columns whose material or product type is not yet determined, or for composite "
        "and masonry columns outside the listed types.",
        "Rückfallwert für Stützen mit noch unbestimmtem Material oder Produkttyp sowie für Verbund- "
        "und Mauerwerksstützen ausserhalb der gelisteten Typen.",
        "Placeholder for columns whose material or product type is not yet fixed at tender stage, "
        "and for composite or masonry columns outside the listed types. Structural function, loads, "
        "and required fire resistance must be stated separately. Use only in early design stages or "
        "where data is incomplete.",
        "Platzhalter für Stützen, deren Material oder Produkttyp zum Zeitpunkt der Ausschreibung "
        "noch nicht festgelegt ist, sowie für Verbund- und Mauerwerksstützen ausserhalb der "
        "gelisteten Typen. Tragfunktion, Lasten und geforderter Feuerwiderstand sind gesondert zu "
        "beschreiben. Nur in frühen Planungsphasen oder bei unvollständiger Datenlage verwenden.",
    ),
]

BEAM_PRODUCTS: list[MemberProduct] = [
    MemberProduct(
        "BMP-STEEL",
        "Steel beam",
        "Stahlträger",
        "Hot-rolled or welded steel beam used as downstand or upstand girder, including corrosion and "
        "fire protection where required. Priced per running metre on a nominal HEA 300 section.",
        "Warmgewalzter oder geschweisster Stahlträger als Unterzug oder Überzug, inklusive Korrosions- "
        "und erforderlichem Brandschutz. Preis pro Laufmeter bei Nennquerschnitt HEA 300.",
        "Horizontal load-bearing member of steel spanning between supports and carrying floor or "
        "roof loads into columns and walls. Fabricated in the workshop and erected as a downstand or "
        "upstand girder with bolted or welded connections. Suitable for long spans and shallow "
        "construction depths; corrosion and fire protection follow the exposure and the required "
        "fire resistance.",
        "Horizontales Tragglied aus Stahl, das zwischen Auflagern spannt und Decken- oder Dachlasten "
        "in Stützen und Wände einleitet. Im Werk gefertigt und als Unterzug oder Überzug mit "
        "geschraubten oder geschweissten Anschlüssen montiert. Geeignet für grosse Spannweiten und "
        "geringe Konstruktionshöhen; Korrosions- und Brandschutz richten sich nach Exposition und "
        "gefordertem Feuerwiderstand.",
    ),
    MemberProduct(
        "BMP-TIMBER",
        "Timber beam",
        "Holzträger",
        "Solid, glued-laminated, or engineered timber beam including connectors and surface treatment. "
        "Priced per running metre on a nominal 200 x 400 mm section.",
        "Vollholz-, Brettschichtholz- oder Konstruktionsholzträger inklusive Verbindungsmittel und "
        "Oberflächenbehandlung. Preis pro Laufmeter bei Nennquerschnitt 200 x 400 mm.",
        "Horizontal load-bearing member of solid, glued laminated, or engineered timber spanning "
        "between supports. Prefabricated to length and connected on site with steel fasteners and "
        "beam hangers. Suitable for timber and hybrid structures with visible members, low dead "
        "load, and dry erection.",
        "Horizontales Tragglied aus Vollholz, Brettschichtholz oder Konstruktionsholz, das zwischen "
        "Auflagern spannt. Auf Länge vorgefertigt und vor Ort mit Stahlverbindungsmitteln und "
        "Trägerschuhen angeschlossen. Geeignet für Holz- und Hybridtragwerke mit sichtbaren "
        "Traggliedern, geringem Eigengewicht und trockener Montage.",
    ),
    MemberProduct(
        "BMP-RC",
        "Reinforced concrete beam",
        "Stahlbetonträger",
        "Cast-in-situ or precast reinforced concrete downstand or upstand beam including formwork and "
        "reinforcement. Priced per running metre on a nominal 300 x 600 mm section.",
        "Ortbeton- oder Fertigteil-Stahlbetonträger als Unterzug oder Überzug inklusive Schalung und "
        "Bewehrung. Preis pro Laufmeter bei Nennquerschnitt 300 x 600 mm.",
        "Horizontal load-bearing member of reinforced concrete acting as downstand or upstand beam "
        "within a concrete floor structure. Cast in place with formwork and reinforcement, or set as "
        "a precast element and connected monolithically. Suitable for high loads, monolithic "
        "connection to slabs, and inherent fire resistance.",
        "Horizontales Tragglied aus Stahlbeton als Unterzug oder Überzug innerhalb einer "
        "Betondeckenkonstruktion. Vor Ort mit Schalung und Bewehrung betoniert oder als Fertigteil "
        "versetzt und monolithisch angeschlossen. Geeignet für hohe Lasten, monolithischen Anschluss "
        "an Decken und inhärenten Feuerwiderstand.",
    ),
    MemberProduct(
        "BMP-OTH",
        "Other or unknown beam",
        "Anderer oder unbekannter Träger",
        "Fallback for beams whose material or product type is not yet determined, or for composite and "
        "masonry beams outside the listed types.",
        "Rückfallwert für Träger mit noch unbestimmtem Material oder Produkttyp sowie für Verbund- und "
        "Mauerwerksträger ausserhalb der gelisteten Typen.",
        "Placeholder for beams whose material or product type is not yet fixed at tender stage, and "
        "for composite or masonry beams outside the listed types. Span, loads, and required fire "
        "resistance must be stated separately. Use only in early design stages or where data is "
        "incomplete.",
        "Platzhalter für Träger, deren Material oder Produkttyp zum Zeitpunkt der Ausschreibung noch "
        "nicht festgelegt ist, sowie für Verbund- und Mauerwerksträger ausserhalb der gelisteten "
        "Typen. Spannweite, Lasten und geforderter Feuerwiderstand sind gesondert zu beschreiben. "
        "Nur in frühen Planungsphasen oder bei unvollständiger Datenlage verwenden.",
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
        "Stair flight of steel for vertical circulation between levels, including landings and "
        "fixings to the surrounding structure. Stringers, treads of plate or grating, and landings "
        "are prefabricated, lifted into place, and bolted or welded to walls and slabs. Suitable for "
        "escape, technical, and external stairs as well as refurbishment where light, quickly "
        "erected flights are required.",
        "Stahltreppenlauf für die vertikale Erschliessung zwischen Geschossen, inklusive Podeste und "
        "Befestigungen an der umgebenden Struktur. Wangen, Stufen aus Blech oder Gitterrost und "
        "Podeste werden vorgefertigt, eingehoben und an Wänden und Decken verschraubt oder "
        "verschweisst. Geeignet für Flucht-, Technik- und Aussentreppen sowie für Sanierungen mit "
        "leichten, schnell montierten Läufen.",
    ),
    MemberProduct(
        "SRP-TIMBER",
        "Timber stair",
        "Holztreppe",
        "Timber stair flight with stringers, treads, and risers of solid or engineered timber, "
        "including surface treatment. Priced per m3 of gross flight volume.",
        "Holztreppenlauf mit Wangen, Tritt- und Setzstufen aus Vollholz oder Konstruktionsholz, "
        "inklusive Oberflächenbehandlung. Preis pro m3 Bruttovolumen des Laufs.",
        "Stair flight of solid or engineered timber for vertical circulation between levels. "
        "Stringers, treads, and risers are prefabricated in the workshop, fitted on site, and "
        "finished with a surface treatment. Suitable for interior stairs in housing and low-rise "
        "buildings where visible timber surfaces and low dead load are wanted.",
        "Holztreppenlauf aus Vollholz oder Konstruktionsholz für die vertikale Erschliessung "
        "zwischen Geschossen. Wangen, Tritt- und Setzstufen werden im Werk vorgefertigt, vor Ort "
        "eingebaut und mit einer Oberflächenbehandlung versehen. Geeignet für Innentreppen im "
        "Wohnungsbau und in niedrigen Gebäuden mit sichtbaren Holzoberflächen und geringem "
        "Eigengewicht.",
    ),
    MemberProduct(
        "SRP-RC",
        "Reinforced concrete stair",
        "Stahlbetontreppe",
        "Cast-in-situ or precast reinforced concrete stair flight including formwork, reinforcement, "
        "and acoustic bearings. Priced per m3 of gross flight volume.",
        "Ortbeton- oder Fertigteil-Stahlbetontreppenlauf inklusive Schalung, Bewehrung und "
        "Schallschutzlager. Preis pro m3 Bruttovolumen des Laufs.",
        "Stair flight of reinforced concrete for vertical circulation, usually part of the "
        "fire-separated escape route. Cast in place with formwork and reinforcement or delivered as "
        "a precast flight and set on acoustic bearings that interrupt structure-borne sound. "
        "Suitable for escape stairwells with heavy wear and requirements on fire resistance and "
        "sound insulation.",
        "Stahlbetontreppenlauf für die vertikale Erschliessung, in der Regel Teil des "
        "brandschutztechnisch abgetrennten Fluchtwegs. Vor Ort mit Schalung und Bewehrung betoniert "
        "oder als Fertigteillauf geliefert und auf Schallschutzlagern versetzt, die den Körperschall "
        "unterbrechen. Geeignet für Fluchttreppenhäuser mit hoher Beanspruchung sowie Anforderungen "
        "an Feuerwiderstand und Schallschutz.",
    ),
    MemberProduct(
        "SRP-OTH",
        "Other or unknown stair",
        "Andere oder unbekannte Treppe",
        "Fallback for stairs whose material or product type is not yet determined, or for stone and "
        "composite stairs outside the listed types.",
        "Rückfallwert für Treppen mit noch unbestimmtem Material oder Produkttyp sowie für Stein- und "
        "Verbundtreppen ausserhalb der gelisteten Typen.",
        "Placeholder for stairs whose material or product type is not yet fixed at tender stage, and "
        "for stone or composite stairs outside the listed types. Geometry, use, and fire and "
        "acoustic requirements must be stated separately. Use only in early design stages or where "
        "data is incomplete.",
        "Platzhalter für Treppen, deren Material oder Produkttyp zum Zeitpunkt der Ausschreibung "
        "noch nicht festgelegt ist, sowie für Stein- und Verbundtreppen ausserhalb der gelisteten "
        "Typen. Geometrie, Nutzung sowie Brand- und Schallschutzanforderungen sind gesondert zu "
        "beschreiben. Nur in frühen Planungsphasen oder bei unvollständiger Datenlage verwenden.",
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
        "Fall protection with vertical metal balusters between posts and handrail, closing the edge "
        "of floors, stairs, and balconies. Prefabricated frames are anchored to slab edges, treads, "
        "or parapets and finished by galvanizing or coating. Suitable for areas used by children, "
        "where climbable horizontal members must be avoided.",
        "Absturzsicherung mit vertikalen Metallstaketen zwischen Pfosten und Handlauf, die den Rand "
        "von Decken, Treppen und Balkonen schliesst. Vorgefertigte Rahmen werden an Deckenrändern, "
        "Stufen oder Brüstungen befestigt und verzinkt oder beschichtet. Geeignet für Bereiche mit "
        "Kinderaufenthalt, in denen überkletterbare horizontale Glieder zu vermeiden sind.",
    ),
    MemberProduct(
        "RAP-GLASS-FRAMED",
        "Framed laminated glass railing",
        "VSG-Geländer gerahmt",
        "Railing with laminated safety glass infill held in a metal frame or channel profile. Priced "
        "per m of railing length.",
        "Geländer mit Verbundsicherheitsglas-Füllung in Metallrahmen oder Klemmprofil. Preis pro m "
        "Geländerlänge.",
        "Fall protection with laminated safety glass infill held in a metal frame or clamping "
        "channel. Panes are cut to size in the factory and glazed into the frame, which is anchored "
        "to the slab edge or parapet. Suitable where transparency and an unobstructed view are "
        "wanted while the frame carries the horizontal loads.",
        "Absturzsicherung mit Verbundsicherheitsglas-Füllung in Metallrahmen oder Klemmprofil. Die "
        "werkseitig zugeschnittenen Scheiben werden in den Rahmen eingeglast, der am Deckenrand oder "
        "auf der Brüstung befestigt wird. Geeignet, wo Transparenz und freie Sicht gefordert sind und "
        "der Rahmen die Horizontallasten übernimmt.",
    ),
    MemberProduct(
        "RAP-GLASS-POINT",
        "Point-fixed structural glass railing",
        "VSG-Geländer punktgehalten",
        "All-glass railing with laminated safety glass panes on point fixings or a base clamping "
        "profile, without vertical posts. Priced per m of railing length.",
        "Ganzglasgeländer mit Verbundsicherheitsglasscheiben auf Punkthaltern oder Klemmprofil im "
        "Fussbereich, ohne vertikale Pfosten. Preis pro m Geländerlänge.",
        "Fall protection as an all-glass balustrade in which the laminated safety glass panes are "
        "themselves the load-bearing element, without vertical posts. Panes are set on point fixings "
        "or clamped in a base channel anchored to the slab edge, with a top rail where required. "
        "Suitable for representative areas with maximum transparency; the panes must remain in place "
        "after one ply breaks.",
        "Absturzsicherung als Ganzglasgeländer, bei dem die Verbundsicherheitsglasscheiben selbst das "
        "tragende Element bilden, ohne vertikale Pfosten. Die Scheiben werden auf Punkthalter gesetzt "
        "oder in ein am Deckenrand befestigtes Klemmprofil eingespannt, bei Bedarf mit oberem "
        "Abschlussprofil. Geeignet für repräsentative Bereiche mit maximaler Transparenz; die "
        "Scheiben müssen nach Bruch einer Lage in Lage bleiben.",
    ),
    MemberProduct(
        "RAP-PERFORATED-METAL",
        "Perforated or expanded metal railing",
        "Lochblech- oder Streckmetallgeländer",
        "Railing with perforated sheet or expanded metal infill panels in a metal frame. Priced per m "
        "of railing length.",
        "Geländer mit Lochblech- oder Streckmetallfüllung in Metallrahmen. Preis pro m Geländerlänge.",
        "Fall protection with perforated sheet or expanded metal infill panels in a metal frame. The "
        "prefabricated panels are set into the frame, which is anchored to the slab edge or parapet "
        "and then galvanized or coated. Suitable where a semi-transparent, robust, non-climbable "
        "infill with wind permeability is wanted.",
        "Absturzsicherung mit Lochblech- oder Streckmetallfüllung in Metallrahmen. Die vorgefertigten "
        "Füllelemente werden in den Rahmen eingesetzt, der am Deckenrand oder auf der Brüstung "
        "befestigt und anschliessend verzinkt oder beschichtet wird. Geeignet, wo eine "
        "halbtransparente, robuste und nicht überkletterbare Füllung mit Winddurchlässigkeit "
        "gefordert ist.",
    ),
    MemberProduct(
        "RAP-CABLE-MESH",
        "Cable or mesh infill railing",
        "Drahtseil- oder Netzgeländer",
        "Railing with tensioned stainless steel cables or woven mesh infill between posts. Priced per m "
        "of railing length.",
        "Geländer mit gespannten Edelstahlseilen oder Netzfüllung zwischen den Pfosten. Preis pro m "
        "Geländerlänge.",
        "Fall protection with tensioned stainless steel cables or woven mesh infill spanning between "
        "posts. Posts are anchored to the structure and the infill is tensioned against them on "
        "site, so the posts must be designed for the tension forces. Suitable for external walkways "
        "and industrial areas; mesh infill is used where climbing must be prevented.",
        "Absturzsicherung mit gespannten Edelstahlseilen oder Netzfüllung zwischen den Pfosten. Die "
        "Pfosten werden an der Struktur befestigt und die Füllung vor Ort gegen sie gespannt, weshalb "
        "die Pfosten für die Spannkräfte auszulegen sind. Geeignet für äussere Laubengänge und "
        "industrielle Bereiche; Netzfüllungen dort, wo Überklettern verhindert werden muss.",
    ),
    MemberProduct(
        "RAP-TIMBER",
        "Timber railing",
        "Holzgeländer",
        "Railing with timber posts, rails, and infill including surface treatment. Priced per m of "
        "railing length.",
        "Geländer mit Pfosten, Riegeln und Füllung aus Holz inklusive Oberflächenbehandlung. Preis pro "
        "m Geländerlänge.",
        "Fall protection with posts, rails, and infill of timber, forming the guarding element at "
        "floors, stairs, and balconies. Prefabricated timber parts are fixed to the structure with "
        "steel connectors and given a surface treatment matched to the exposure. Suitable for "
        "interior stairs and sheltered external areas; weathered positions require detailing that "
        "drains water and allows maintenance.",
        "Absturzsicherung mit Pfosten, Riegeln und Füllung aus Holz als Schutzelement an Decken, "
        "Treppen und Balkonen. Die vorgefertigten Holzteile werden mit Stahlverbindungsmitteln an der "
        "Struktur befestigt und erhalten eine der Exposition angepasste Oberflächenbehandlung. "
        "Geeignet für Innentreppen und gedeckte Aussenbereiche; bewitterte Lagen erfordern "
        "wasserableitende und unterhaltsfreundliche Detaillierung.",
    ),
    MemberProduct(
        "RAP-PARAPET-SOLID",
        "Solid parapet",
        "Massive Brüstung",
        "Fall protection formed by a solid concrete or masonry parapet with coping, acting as the "
        "guarding element. Priced per m of parapet length.",
        "Absturzsicherung als massive Beton- oder Mauerwerksbrüstung mit Abdeckung, die die "
        "Schutzfunktion übernimmt. Preis pro m Brüstungslänge.",
        "Fall protection formed by a solid concrete or masonry parapet with a coping, taking over the "
        "guarding function without a separate railing. Built together with the surrounding structure "
        "as cast-in-place concrete, precast element, or masonry, and closed on top by a coping that "
        "sheds water. Suitable for roof edges, balconies, and loggias where a closed, opaque edge "
        "with low maintenance is wanted.",
        "Absturzsicherung als massive Beton- oder Mauerwerksbrüstung mit Abdeckung, welche die "
        "Schutzfunktion ohne separates Geländer übernimmt. Zusammen mit der umgebenden Struktur als "
        "Ortbeton, Fertigteil oder Mauerwerk erstellt und oben mit einer wasserableitenden Abdeckung "
        "geschlossen. Geeignet für Dachränder, Balkone und Loggien mit geschlossenem, undurchsichtigem "
        "Abschluss und geringem Unterhalt.",
    ),
    MemberProduct(
        "RAP-HANDRAIL",
        "Handrail only",
        "Handlauf",
        "Wall-mounted or post-mounted handrail without infill, used where no fall protection infill is "
        "required. Priced per m of handrail length.",
        "Wand- oder pfostenmontierter Handlauf ohne Füllung, wo keine Absturzsicherung mit Füllung "
        "erforderlich ist. Preis pro m Handlauflänge.",
        "Handrail without infill, giving guidance and support along stairs, ramps, and corridors "
        "where no fall protection infill is required. Mounted on brackets to the wall or on posts, "
        "with a continuously graspable profile and ends returned to the wall. Suitable for "
        "barrier-free routes and as a second handrail on stairs that already have fall protection.",
        "Handlauf ohne Füllung für Führung und Halt an Treppen, Rampen und Korridoren, wo keine "
        "Absturzsicherung mit Füllung erforderlich ist. Mit Konsolen an der Wand oder auf Pfosten "
        "montiert, mit durchgehend umgreifbarem Profil und zur Wand zurückgeführten Enden. Geeignet "
        "für hindernisfreie Wege und als zweiter Handlauf an Treppen, die bereits über eine "
        "Absturzsicherung verfügen.",
    ),
    MemberProduct(
        "RAP-OTH",
        "Other or unknown railing",
        "Anderes oder unbekanntes Geländer",
        "Fallback for railings whose product type is not yet determined, or for special guarding "
        "systems outside the listed types.",
        "Rückfallwert für Geländer mit noch unbestimmtem Produkttyp sowie für spezielle "
        "Absturzsicherungssysteme ausserhalb der gelisteten Typen.",
        "Placeholder for railings whose product type is not yet fixed at tender stage, and for "
        "special guarding systems outside the listed types. Guarding function, horizontal loads, and "
        "infill requirements must be stated separately. Use only in early design stages or where "
        "data is incomplete.",
        "Platzhalter für Geländer, deren Produkttyp zum Zeitpunkt der Ausschreibung noch nicht "
        "festgelegt ist, sowie für spezielle Absturzsicherungssysteme ausserhalb der gelisteten "
        "Typen. Schutzfunktion, Horizontallasten und Anforderungen an die Füllung sind gesondert zu "
        "beschreiben. Nur in frühen Planungsphasen oder bei unvollständiger Datenlage verwenden.",
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
        scope_note_en="Assign one concept per beam element. Baseline cost is priced per running metre "
        "of beam length (Qto_BeamBaseQuantities.Length), on a nominal cross-section per material "
        "recorded in the price entry. Covers architectural (ARC-BEAM) and structural beam elements; "
        "distinct from slab separator products (SSP) used for slabs.",
        scope_note_de="Ein Konzept pro Trägerbauteil zuordnen. Basiskosten pro Laufmeter Trägerlänge "
        "(Qto_BeamBaseQuantities.Length), bezogen auf einen im Preiseintrag dokumentierten "
        "Nennquerschnitt je Baustoff. Umfasst architektonische (ARC-BEAM) und tragende "
        "Trägerbauteile; abgegrenzt von Deckentrennelementprodukten (SSP).",
        price_unit="m",
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
