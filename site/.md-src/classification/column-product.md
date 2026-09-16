# Abstract column products

Source: [`column-products.skos.ttl`](sources/column-product.ttl)

## Scheme

- **definition (de):** Produkttyp-Klassifikation für vertikale Tragglieder (Stützen und Pfosten) nach dominierendem Baustoff. Dient der Zuordnung von Basis-Einheitspreisen und Referenzen für graue Emissionen zum Stützenbauteil des pragmaticBIM Elementplans.
- **definition (en):** Product-type classification for vertical load-bearing members (columns and posts) by dominant construction material. Used to attach baseline unit prices and embodied carbon references to the column element of the pragmaticBIM Elementplan.
- **prefLabel (de):** Abstrakte Stützenprodukte
- **prefLabel (en):** Abstract column products
- **title (de):** Abstrakte Stützenprodukte
- **title (en):** Abstract column products

## Concepts

<div class="pbs-vocab-concepts" data-default-lang="en" data-active-lang="en">
<div class="pbs-lang-switcher" role="group" aria-label="Language">
<button type="button" class="pbs-lang-btn" data-lang="de">DE</button>
<button type="button" class="pbs-lang-btn" data-lang="en">EN</button>
</div>
<table>
<thead>
<tr>
<th>Notation</th>
<th>Broader</th>
<th class="pbs-lang-col" data-lang="de" data-field="label">Label</th>
<th class="pbs-lang-col" data-lang="de" data-field="definition">Definition</th>
<th class="pbs-lang-col" data-lang="de" data-field="description">Description</th>
<th class="pbs-lang-col" data-lang="de" data-field="scope_note">Scope note</th>
<th class="pbs-lang-col" data-lang="en" data-field="label">Label</th>
<th class="pbs-lang-col" data-lang="en" data-field="definition">Definition</th>
<th class="pbs-lang-col" data-lang="en" data-field="description">Description</th>
<th class="pbs-lang-col" data-lang="en" data-field="scope_note">Scope note</th>
</tr>
</thead>
<tbody>
<tr>
<td>CLP-OTH</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Andere oder unbekannte Stütze</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Rückfallwert für Stützen mit noch unbestimmtem Material oder Produkttyp sowie für Verbund- und Mauerwerksstützen ausserhalb der gelisteten Typen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Platzhalter für Stützen, deren Material oder Produkttyp zum Zeitpunkt der Ausschreibung noch nicht festgelegt ist, sowie für Verbund- und Mauerwerksstützen ausserhalb der gelisteten Typen. Tragfunktion, Lasten und geforderter Feuerwiderstand sind gesondert zu beschreiben. Nur in frühen Planungsphasen oder bei unvollständiger Datenlage verwenden.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Other or unknown column</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Fallback for columns whose material or product type is not yet determined, or for composite and masonry columns outside the listed types.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Placeholder for columns whose material or product type is not yet fixed at tender stage, and for composite or masonry columns outside the listed types. Structural function, loads, and required fire resistance must be stated separately. Use only in early design stages or where data is incomplete.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>CLP-RC</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Stahlbetonstütze</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Ortbeton- oder Fertigteil-Stahlbetonstütze inklusive Schalung und Bewehrung. Preis pro m3 Bruttovolumen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Vertikales Tragglied aus Stahlbeton, das Decken- und Dachlasten in die Fundation weiterleitet. Entweder vor Ort mit Schalung und Bewehrung betoniert oder als Fertigteil geliefert und vergossen. Geeignet für hohe Lasten, inhärenten Feuerwiderstand und in Betondecken integrierte Stützen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Reinforced concrete column</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Cast-in-situ or precast reinforced concrete column including formwork and reinforcement. Priced per m3 of gross member volume.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Vertical load-bearing member of reinforced concrete transferring floor and roof loads to the foundation. Either cast in place with formwork and reinforcement or delivered as a precast element and grouted into position. Suitable for high loads, inherent fire resistance, and columns integrated into concrete floor structures.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>CLP-STEEL</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Stahlstütze</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Warmgewalzte, geschweisste oder Hohlprofil-Stahlstütze inklusive Korrosionsschutz und erforderlichem Brandschutzanstrich. Preis pro m3 Bruttovolumen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Vertikales Tragglied aus Stahl, das Decken- und Dachlasten in die darunterliegende Struktur weiterleitet. Als Walz-, Schweiss- oder Hohlprofil im Werk gefertigt und vor Ort mit geschraubten oder geschweissten Anschlüssen montiert. Geeignet für schlanke Stützen und grosse Spannweiten; Korrosions- und Brandschutz richten sich nach Exposition und gefordertem Feuerwiderstand.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Steel column</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Hot-rolled, welded, or hollow-section steel column including corrosion protection and fire protection coating where required. Priced per m3 of gross member volume.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Vertical load-bearing member of steel transferring floor and roof loads to the structure below. Fabricated in the workshop as rolled, welded, or hollow section and erected on site with bolted or welded connections. Suitable for slender columns and long spans; corrosion and fire protection follow the exposure and the required fire resistance.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>CLP-TIMBER</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Holzstütze</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Vollholz-, Brettschichtholz- oder Konstruktionsholzstütze inklusive Verbindungsmittel und Oberflächenbehandlung. Preis pro m3 Bruttovolumen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Vertikales Tragglied aus Vollholz, Brettschichtholz oder Konstruktionsholz, das Decken- und Dachlasten nach unten weiterleitet. Auf Länge vorgefertigt und vor Ort mit Stahlverbindungsmitteln trocken montiert. Geeignet für Holz- und Hybridtragwerke mit sichtbaren Oberflächen, geringem Eigengewicht und kurzer Montagezeit.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Timber column</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Solid, glued-laminated, or engineered timber column including connectors and surface treatment. Priced per m3 of gross member volume.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Vertical load-bearing member of solid, glued laminated, or engineered timber transferring floor and roof loads downwards. Prefabricated to length and erected dry on site with steel connectors. Suitable for timber and hybrid structures where visible surfaces, low dead load, and short erection times are required.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
</tbody>
</table>
</div>
