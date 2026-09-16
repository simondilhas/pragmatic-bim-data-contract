# pragmaticBIM Elementplan elements

Source: [`elementplan-elements.skos.ttl`](sources/elementplan-element.ttl)

## Scheme

- **definition (de):** Kostenrelevante Bauteile des pragmaticBIM Elementplans. Jedes Konzept trägt die eine für die Mengenermittlung verwendete IFC-Basismenge (pbs:referenceQuantity in pbs:quantityPset) sowie die zugehörige Verrechnungseinheit (pbs:priceUnit), damit ein Bauteil auf eine eindeutige Mengenbasis für die Kostenermittlung auflöst.
- **definition (en):** Cost-relevant building elements of the pragmaticBIM Elementplan. Each concept carries the one IFC base quantity used for take-off (pbs:referenceQuantity in pbs:quantityPset) and the unit that quantity is billed in (pbs:priceUnit), so an element resolves to a single unambiguous quantity basis for costing.
- **prefLabel (de):** pragmaticBIM Elementplan Bauteile
- **prefLabel (en):** pragmaticBIM Elementplan elements
- **title (de):** pragmaticBIM Elementplan Bauteile
- **title (en):** pragmaticBIM Elementplan elements

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
<th class="pbs-lang-col" data-lang="de" data-field="scope_note">Scope note</th>
<th class="pbs-lang-col" data-lang="en" data-field="label">Label</th>
<th class="pbs-lang-col" data-lang="en" data-field="definition">Definition</th>
<th class="pbs-lang-col" data-lang="en" data-field="scope_note">Scope note</th>
</tr>
</thead>
<tbody>
<tr>
<td>ARC-BEAM</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Unterzug oder Überzug</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Horizontales Tragglied zwischen Stützen oder Wänden, als Unterzug oder Überzug modelliert.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Bepreisung pro Laufmeter; der Trägerquerschnitt steckt im Produktkonzept, die BMP-*-Preise gelten je Laufmeter des Nennquerschnitts dieses Materials.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Beam</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Horizontal load-bearing member spanning between columns or walls, modelled as a downstand or upstand beam.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Priced per running metre; the beam cross-section is carried by the product concept, so the BMP-* prices are per metre of the nominal section of that material.</td>
</tr>
<tr>
<td>ARC-CEILING</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Abhangdecke</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Abgehängte oder direkt applizierte Decke unter der Rohdecke, inklusive Unterkonstruktion.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Suspended ceiling</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Suspended or applied ceiling below the structural slab, including substructure.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>ARC-COLUMN</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Stütze</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Vertikales Tragglied, das Lasten in Decken, Träger oder Fundamente abträgt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Column</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Vertical load-bearing member transferring loads to slabs, beams, or footings.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>ARC-FLOOR-COV</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Bodenaufbau</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bodenaufbau über der Rohdecke, inklusive Unterlagsboden, Trennschichten und sichtbarem Bodenbelag.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Floor build-up</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Floor build-up above the structural slab, including screed, separation layers, and the visible floor finish.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>ARC-FOOTING</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Fundament</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Einzel-, Streifen- oder Plattenfundament zur Lastabtragung in den Baugrund.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Footing</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Pad, strip, or raft footing transferring loads into the ground.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>ARC-RAILING</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Geländer und Absturzsicherung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Geländer, Brüstung oder Absturzsicherung entlang von Decken, Treppen und Öffnungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Railing and fall protection</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Railing, balustrade, or parapet providing fall protection along slabs, stairs, and openings.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>ARC-ROOF-DRAIN</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gefälledämmung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Keilförmige Dämmschicht zur Bildung des Entwässerungsgefälles auf dem Flachdach.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Noch kein Produktschema definiert; die Gefälledämmung wird derzeit nur als Teil des übergeordneten Flachdachaufbaus bepreist.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Tapered roof insulation</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Tapered insulation layer forming the drainage slope of a flat roof.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">No product scheme is defined yet; tapered insulation is currently priced only as part of the parent flat roof assembly.</td>
</tr>
<tr>
<td>ARC-ROOF-FLAT</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Flachdach</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Flachdachaufbau inklusive Tragdecke, Dämmung und Abdichtung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Flat roof</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Flat roof assembly including structural slab, insulation, and waterproofing membrane.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>ARC-ROOF-PITCH</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Steildach</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Steildachaufbau inklusive Konstruktion, Dämmung und Dacheindeckung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Pitched roof</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Pitched roof assembly including structure, insulation, and roof covering.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>ARC-SLAB-BALCONY</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Balkon</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Auskragende oder abgestützte Balkonplatte im Aussenbereich, inklusive thermischer Trennung zur Tragstruktur.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Balcony slab</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Cantilevered or supported exterior balcony slab, including thermal separation to the structure.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>ARC-SLAB-BASE</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Bodenplatte</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Unterste auf dem Boden aufliegende Platte, inklusive Abdichtung und Dämmung, sofern als Teil der Platte modelliert.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Base slab</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Lowest floor slab bearing on the ground, including waterproofing and insulation layers where modelled as part of the slab.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>ARC-SLAB-FLOOR</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Geschossdecke</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Tragende Decke zwischen Geschossen, ohne Bodenaufbau und Abhangdecke.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Floor slab</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Structural slab between storeys, excluding floor build-up and suspended ceiling.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>ARC-STAIR</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Treppe</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Treppenlauf mit Podesten zur Verbindung von Geschossen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Stair</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Stair flight with landings connecting storeys.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>ARC-WALL-CLAD</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Innenwandbekleidung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Innenseitige Wandbekleidung, Verkleidung oder Oberflächenausbau auf der Raumseite einer Wand.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Interior wall covering</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Interior wall covering, lining, or finish applied to the room side of a wall.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>ARC-WALL-CLAD-EXT</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Fassadenbekleidung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenseitige Fassadenbekleidung oder vorgehängte Fassade, als separate Bekleidungsschicht auf der Hüllwand modelliert.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Facade cladding</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Exterior facade cladding or ventilated facade system modelled as a separate covering layer on the envelope wall.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>ARC-WALL-EXT</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aussenwand</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenwand als Gebäudehülle, in frühen Phasen und bei einfachen Fassaden als Mehrschichtbauteil modelliert.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Exterior wall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Exterior wall as building envelope, modelled as a multi-layer component in early phases and for simple facades.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>ARC-WALL-INT</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Nichttragende Innenwand</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Nichttragende Innenwand oder Trennwand, die Innenräume ohne Lastabtrag trennt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Non-load-bearing interior wall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Non-load-bearing interior wall or partition separating interior spaces without carrying vertical loads.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>ARC-WALL-INT-LB</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Tragende Innenwand</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Tragende Innenwand, die Innenräume trennt und vertikale Lasten abträgt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Load-bearing interior wall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Load-bearing interior wall separating interior spaces and carrying vertical loads.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>DOOR</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Tür</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Tür in einer Aussen- oder Innenwand, bepreist über die Fläche der Wandöffnung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Door</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Door in an exterior or interior wall, priced by the area of the wall opening it fills.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>FURN</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Möbel</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Losmöbel oder Einbaumöbel, als zählbares Objekt erfasst.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Bepreisung pro Stück über die Anzahl der Instanzen; der Elementplan publiziert keine Basismenge für Möbel. Noch kein Produktschema definiert.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Furniture</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Loose or fitted furniture item recorded as a countable object.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Priced per piece from instance cardinality; the Elementplan publishes no base quantity for furniture. No product scheme is defined yet.</td>
</tr>
<tr>
<td>LAN-TREE</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Baum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bestehender oder neuer Baum im Umgebungs- oder Landschaftsmodell, als zählbares Objekt erfasst.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Bepreisung pro Stück über die Anzahl der Instanzen; der Elementplan publiziert keine Basismenge für Bäume. Noch kein Produktschema definiert.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Tree</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Existing or new tree in the site or landscape model, recorded as a countable object.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Priced per piece from instance cardinality; the Elementplan publishes no base quantity for trees. No product scheme is defined yet.</td>
</tr>
<tr>
<td>WINDOW</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Fenster</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Fenster in einer Aussen- oder Innenwand, bepreist über die Fläche der Wandöffnung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Dachfenster werden auf derselben m²-Basis bepreist; WICP-SKYLIGHT wurde von einem Stückreferenzwert über eine Nennfläche umgerechnet.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Window</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Window in an exterior or interior wall, priced by the area of the wall opening it fills.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Rooflights are priced on the same m² basis; WICP-SKYLIGHT was rebased from a per-piece reference using a nominal rooflight area.</td>
</tr>
</tbody>
</table>
</div>
