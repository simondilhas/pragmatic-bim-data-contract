# Abstract facade covering products

Source: [`facade-covering-products.skos.ttl`](sources/facade-covering-product.ttl)

## Scheme

- **definition (de):** Produkttyp-Klassifikation für Außenfassadenbekleidungen, vorgehängte Fassadensysteme und Sanierungslösungen. Konzipiert für europäische Bauprozesse mit Brandschutz (A1/A2-s1,d0-Konformität), Wärmeleistung (EN ISO 6946, EN ISO 10077), Energiesanierung, Kreislaufwirtschaft und BIM-gestützte digitale Prozesse. Für Katalog-, Spezifikations-, Kosten- und Sanierungsplanung; mit abstrakter Materialklassifikation für dominante Substanz und regionale Bauvorschriften kombinieren.
- **definition (en):** Product-type classification for exterior facade claddings, ventilated facade systems, and retrofit solutions. Designed for European construction workflows incorporating fire performance (A1/A2-s1,d0 compliance), thermal insulation (EN ISO 6946, EN ISO 10077), energy retrofit, circular economy, and digital BIM-enabled processes. For catalog, specification, cost, and retrofit planning; pair with abstract material classification for dominant substance and regional building codes.
- **description (de):** Version 2.0: Europäisch-fokussierte Verbesserung, die Post-Grenfell-Brandschutzerfordernisse (EN 13501-1), EU-Energieleistungsstandards (EPBD 2024), Sanierungs-/Renovierungs-Workflows (Fit-for-55, Energiesprong), vorgefertigte modulare Systeme (BPR 2024) und neuartige Technologien (BIPV, holzbasierte multifunktionale Fassaden) einbeziehen. Unterstützt BIM-Klassifizierung (IfcCovering), Kostenschätzung und digitale Sanierungsketten (DigiFab, 4RinEU-Projekte).
- **description (en):** Market data sourced from: Mordor Intelligence (2025), Grand View Research (2023-2025), Market Data Forecast (2024-2026), Research & Markets (2024), European Commission BUILD UP initiative, International Sustainable Energy Conference (2025). Fire classification references: EN 13501-1, BS 8414, Approved Document B. Thermal standards: EN ISO 6946, EN ISO 10077, EN ISO 7345. Energy directives: EPBD 2024/1275, Directive 2024/1275/EU, Construction Products Regulation (CPR) 2024. Retrofit programs: Energiesprong, 4RinEU, INFINITE project, Life Giga Regio Factory, DigiFab (Horizon Europe).
- **prefLabel (de):** Europäische Fassadenbekleidungsprodukte
- **prefLabel (en):** European facade covering products
- **title (de):** Europäische Fassadenbekleidungsprodukte
- **title (en):** European facade covering products

## Hierarchy

```mermaid
classDiagram
direction TB
class n_FaCP_RENDER_ETICS_WDVS["FaCP-RENDER-ETICS-WDVS: Render / ETICS facade system"]
class n_FaCP_RENDER_ETICS_WDVS_INS["FaCP-RENDER-ETICS-WDVS-INS: ETICS insulation layer"]
class n_FaCP_RENDER_ETICS_WDVS_RENDER["FaCP-RENDER-ETICS-WDVS-RENDER: ETICS render finish layer"]
n_FaCP_RENDER_ETICS_WDVS <|-- n_FaCP_RENDER_ETICS_WDVS_INS
n_FaCP_RENDER_ETICS_WDVS <|-- n_FaCP_RENDER_ETICS_WDVS_RENDER
```

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
<td>FaCP-BIPV-INTEGRATED</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gebäudeintegrierte Photovoltaik-Fassade</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Fassadenbekleidungssystem mit integrierten kristallinen Silizium-, Dünnschicht- oder Perowskit-Photovoltaikzellen. Kann auf Metall-, Keramik- oder Glasunterlagen für ästhetische und energieerzetgende Dualfunktion angewendet werden.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Nichttragende Fassadenbekleidung mit zusätzlicher Stromerzeugung; Photovoltaikzellen sind in die sichtbare Aussenschicht des Wandaufbaus integriert. Aktive Module ersetzen herkömmliche Bekleidungspaneele auf einer Unterkonstruktion oder in einem Elementsystem und werden durch den Hohlraum zu Wechselrichtern verkabelt, sodass Wetterschutz und Energiegewinnung in derselben Schicht erbracht werden. Geeignet für Neubau und repräsentative Erneuerung an gut besonnten Fassaden; Modultemperatur, Zugänglichkeit für Unterhalt und Austausch sowie Kabelführung sind in der Planung zu lösen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Building-integrated photovoltaic facade</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Facade cladding system with integrated crystalline silicon, thin-film, or perovskite photovoltaic cells. Can be applied to metal, ceramic, or glass substrates for aesthetic and energy-generating dual function.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Non-load-bearing facade cladding that additionally generates electricity, with photovoltaic cells integrated into the visible outer layer of the wall build-up. Active modules replace conventional cladding panels on a sub-frame or unitised system and are wired through the cavity to inverters, so weather protection and energy generation are delivered by the same layer. Suitable for new build and prestige renewal on well-exposed facades; module temperature, access for maintenance and replacement, and cable routing must be resolved in the design.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Emerging technology; market penetration &lt;5% (2025). Fire rating: substrate-dependent (typically A2-s1,d0 capable). Thermal: varies; integration with ventilated cavity improves performance. Regulatory support: EU directive incentivizes BIPV on new construction and major renovations (EPBD 2024). Cost premium: 20-40% over conventional facade (decreasing). Electrical performance: 150-200 W/m² output typical. Integration challenges: cell temperature management, maintenance access, wiring concealment. Regional drivers: Southern EU (higher insolation), new commercial buildings, flagship retrofits.</td>
</tr>
<tr>
<td>FaCP-BRICK-SLIP</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Ziegelriemchen- / Klinker-Vorhangfassade</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Dünne Ziegelriemchen-, Fliesen- oder Mauersteinbekleidung als vorgehängte hinterlüftete Fassade auf Unterkonstruktion, einschliesslich Sanierungs-Klinkerfassaden über Daemmung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Nichttragende Bekleidung im Mauerwerksbild aus dünnen Ziegelriemchen oder kleinformatigen Platten vor der gedämmten Aussenwand, ohne Lastabtrag aus dem Gebäude. Die Riemchen werden auf Trägerschienen, Trägerplatten oder einer verputzten Trägerschicht auf hinterlüfteter Unterkonstruktion eingehängt oder verklebt, mit verfugten oder offenen Stossfugen. Geeignet für Neubau und Sanierung, wenn das Bild massiven Sichtmauerwerks bei geringem Eigengewicht gefordert ist, etwa bei Aussendämmung einer bestehenden Klinkerfassade.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Unterscheidet sich von tragendem Mauerwerk (SWP-MASONRY) und grossformatigen Keramik-Vorhangfassaden (FaCP-CERAMIC-VENTILATED). Typisch für Sanierung über bestehendem Untergrund.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Brick slip / tile-hung ventilated facade</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Thin brick slip, tile, or masonry-unit ventilated rainscreen cladding on subframe, including retrofit tile-hung systems over insulation.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Non-load-bearing cladding with a masonry appearance from thin brick slips or small-format tiles in front of the insulated exterior wall, without any load transfer from the building. The slips are hung or bonded onto carrier rails, carrier boards, or a rendered carrier layer on a ventilated sub-frame, with pointed or open joints. Suitable for new build and retrofit where the appearance of solid facing masonry is required at low dead load, for instance when an existing brick facade is insulated from outside.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Distinct from load-bearing masonry walls (SWP-MASONRY) and large-format ceramic ventilated tiles (FaCP-CERAMIC-VENTILATED). Typical for retrofit over existing substrates.</td>
</tr>
<tr>
<td>FaCP-CERAMIC-VENTILATED</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Vorgehängte Keramikfliesenfassade</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Keramik-, Feinsteinzeug- oder Steingut-Fliesensystem für vorgehängte Fassaden mit Belüftungshohlraum. Dominierender Produkttyp im europäischen Markt (33,9% Wertanteil, 2023). Integriert Isolationsschicht, Belüftungshohlraum und mechanische Befestigungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Nichttragende Wetterschutzschicht aus Keramik-, Feinsteinzeug- oder Steingutplatten vor der tragenden Aussenwand. Die Platten werden sichtbar oder verdeckt auf einer Metall-Unterkonstruktion befestigt, sodass zwischen Dämmung und Bekleidung ein durchgehender Hinterlüftungsraum bleibt. Geeignet für Neubau und Sanierung an exponierten Fassaden mit hohen Anforderungen an Schlagregenschutz, Farbstabilität und geringen Unterhalt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Brandschutz: typischerweise A1 oder A2-s1,d0 (EN 13501-1). Wärmeleistung: kompatibel mit U-Werten 0,24-0,15 W/m²K in vorgehängter Konfiguration. Regionale Dominanz: Italien, Spanien, Portugal, Mitteleuropa. Geeignet für Sanierungsanwendungen (nicht-tragende Überlagerung auf bestehender Fassade). Wachsender Markt CAGR 6,1% 2024-2030.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Ventilated ceramic tile system</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Ceramic, porcelain, or stoneware ventilated facade tile or panel system with rear-ventilated cavity. Dominant product type in European market (33.9% by value, 2023). Integrates insulation layer, air cavity, and mechanical fixings.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Non-load-bearing weather protection layer of ceramic, porcelain, or stoneware tiles and panels set in front of the load-bearing exterior wall. The units are fixed visibly or concealed onto a metal sub-frame so that a continuous ventilated cavity remains between insulation and cladding. Suitable for new build and retrofit on exposed facades with high requirements for driving-rain protection, colour stability, and low maintenance.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Fire rating: typically A1 or A2-s1,d0 (EN 13501-1). Thermal performance: compatible with U-values 0.24-0.15 W/m²K in ventilated configuration. Regional dominance: Italy, Spain, Portugal, Central Europe. Suitable for retrofit applications (non-structural overlay on existing facade). Growing market CAGR 6.1% 2024-2030.</td>
</tr>
<tr>
<td>FaCP-EXTERIOR-PAINT-COATING</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aussenanstrich / Schutzanstrichsystem</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aufgetragener Aussenanstrich, Beschichtung oder Oberflächenschicht auf Fassadenflaechen (Minerallack, Silikatfarbe, Acryl, Polyurethan oder Epoxid). Kann primäre Fertigungsschicht oder sekundäre Schutzschicht über Untergrund sein.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Nichttragende Beschichtung, dünnschichtig direkt auf dem Fassadenuntergrund aufgebracht; sie wirkt als Schutz- und Gestaltungsoberfläche und nicht als eigene Bekleidungsschicht. Der Auftrag erfolgt nach Reinigung und Instandsetzung des Untergrunds in Grund- und Deckanstrich mit Pinsel, Rolle oder Spritzverfahren, wobei die Dampfdurchlässigkeit auf den Untergrund abzustimmen ist, damit die Wand abtrocknen kann. Geeignet für Neubauoberflächen und Fassadenrenovation als wiederkehrende Unterhaltsmassnahme; Schichtdicke, Farbton und Untergrundvorbereitung sind vorzugeben.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Exterior paint / protective coating finish</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Applied exterior paint, coating, or finish layer on facade surfaces (mineral paint, silicate paint, acrylic, polyurethane, or epoxy). Can be primary finish or secondary protective layer over substrate.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Non-load-bearing coating applied thinly and directly onto the facade substrate, acting as protective and decorative surface rather than as a separate cladding layer. It is applied after cleaning and repair of the substrate in primer and topcoat passes by brush, roller, or spray, and its vapour permeability must be matched to the substrate so that the wall can dry out. Suitable for new build finishes and for facade refurbishment as a recurring maintenance measure; film build, colour, and surface preparation are to be specified.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Fire rating: typically D-s2,d0 or E (thin organic layer). Thermal: minimal direct contribution (surface emissivity property). Maintenance: critical for long-term facade durability; repainting cycle 10-15 years typical. Regional: used universally; quality/formulation varies (climate adaptation). Sustainability: organic solvent content (VOC) regulated by EU Directive 2004/42/EC. Innovation: self-cleaning coatings (TiO₂), phase-change materials (PCM) for thermal regulation emerging.</td>
</tr>
<tr>
<td>FaCP-FIBER-CEMENT-BOARD</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Faserzement-Fassadensystem</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Faserzement-, verstärktes Zementbrett oder Kunststein-Fassadenbrett/-Paneelsystem. Einschliesslich flacher Bretter, profilierter Bretter und konstruierter faserverstärkter Paneele.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Nichttragende mineralische Plattenbekleidung aus Faserzement- oder verstärkten Zementplatten vor der gedämmten Aussenwand. Die Platten werden zugeschnitten und genietet, geschraubt oder verdeckt auf einer Metall- oder Holz-Unterkonstruktion mit Hinterlüftungsraum und definiertem Fugenbild befestigt. Geeignet für Neubau und Sanierung, wenn eine dauerhafte, unterhaltsarme und formstabile mineralische Oberfläche gefordert ist; Kantenschutz und sorgfältige Handhabung der spröden Platten sind zu berücksichtigen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Fibre-cement board facade</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Fibre-cement, reinforced cement board, or artificial stone facade board/panel system. Includes flat boards, profiled boards, and engineered fiber-reinforced panels.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Non-load-bearing mineral board cladding of fibre-cement or reinforced cement panels in front of the insulated exterior wall. The boards are cut to size and riveted, screwed, or concealed-fixed to a metal or timber sub-frame with a ventilated cavity and a defined joint pattern. Suitable for new build and retrofit where a durable, low-maintenance, dimensionally stable mineral surface is required; edge protection and careful handling of the brittle boards are to be considered.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Fire rating: A1 or A2-s1,d0 (mineral-based, non-combustible). Thermal: moderate; requires integrated insulation layer for U &lt;0.20. Regional: common in Central Europe (Germany, Austria, Poland), France. Advantages: durability (30-50 years), low maintenance, weather-resistant. Disadvantages: brittleness, weight, installation skill sensitivity. Retrofit: moderate suitability (weight consideration on support structure). Market share: declining slightly as ceramic and wood options grow.</td>
</tr>
<tr>
<td>FaCP-HPL-PANEL</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">HPL- / Kompaktplatten-Fassade</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Hochdrucklaminat- (HPL) oder Kompaktplatten-System als vorgehängte hinterlüftete Fassade mit Unterkonstruktion und mechanischer Befestigung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Nichttragende hinterlüftete Bekleidung aus Kompaktplatten in Hochdrucklaminat vor der gedämmten Aussenwand. Die Platten werden mit sichtbaren Nieten oder Schrauben oder mit verdeckter Rückseitenbefestigung auf einer Metall- oder Holz-Unterkonstruktion befestigt, die einen offenen Hinterlüftungsraum und die Plattenbewegung zulässt. Geeignet für Neubau und Sanierung an Gewerbe- und Institutionsfassaden mit Bedarf an robusten, leicht reinigbaren Oberflächen, auch in stoss- und graffitibelasteten Sockelbereichen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Unterscheidet sich von generischen Kunststoffpaneelen (FaCP-SYNTHETIC-VENTILATED), wenn HPL/Kompaktplatte die dominante spezifizierte Produktfamilie ist. Häufig an Gewerbe- und Institutionalfassaden in Mitteleuropa.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">HPL / compact laminate facade panel</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">High-pressure laminate (HPL) or compact laminate ventilated rainscreen panel system with subframe and mechanical fixings.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Non-load-bearing rainscreen cladding of compact high-pressure laminate boards in front of the insulated exterior wall. The boards are fixed with visible rivets or screws, or with concealed rear fixings, to a metal or timber sub-frame that keeps an open ventilated cavity and permits panel movement. Suitable for new build and retrofit on commercial and institutional facades needing a hard-wearing, easily cleaned surface, including plinth areas exposed to impact and graffiti.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Distinct from generic synthetic panels (FaCP-SYNTHETIC-VENTILATED) where HPL/compact laminate is the dominant specified product family. Common on commercial and institutional facades in Central Europe.</td>
</tr>
<tr>
<td>FaCP-METAL-COMPOSITE-PANEL</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Metallverbund-Fassadenpaneel (AVP)</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aluminium-Verbundplatte (AVP), Metallkassette oder anderes metallkaschiertes Verbundpaneelsystem. Vorgefertigte Sandwichpaneele mit Aluminium-Deckschichten und Kern (Polyethylen, Mineralwolle oder brandgeschützter Kern).</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Nichttragende Fassadenhaut aus werkseitig gefertigten Sandwichpaneelen mit Metalldeckschichten und verklebtem Kern, vorgehängt vor der gedämmten Aussenwand. Die Paneele werden zu Kassetten oder Schalen gekantet und mechanisch auf einer ausgerichteten Metall-Unterkonstruktion befestigt, mit definierten Fugen und Hinterlüftung. Geeignet für Neubau und rasche Sanierung grosser ebener Flächen; der Kern ist als nichtbrennbar nachzuweisen, wenn Gebäudehöhe oder Nutzung dies verlangen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">WARNUNG: Brandschutzklasse hängt stark vom Kernmaterial ab. PE-Kern-Paneele: Klasse E oder D (in vielen EU-Ländern nach Grenfell eingeschränkt/verboten). Mineralwolle-Kern-Paneele: A2-s1,d0-konform (bevorzugt für Hochhäuser). Modularität: hoch; schnelle Montage (1-2 m²/Stunde vor Ort). Wärmeleistung: gute Integration mit Isolationsschicht; erreicht U-Werte 0,15 W/m²K. Sanierungsanwendung: ausgezeichnet; nicht-tragende Überlagerung. Verbotsstatus: UK, Frankreich, Deutschland, Niederlande beschränken brennbare Kerne auf Gebäuden &gt;11-18m.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Metal composite facade panel (ACP)</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Aluminium composite panel (ACP), metal cassette, or other metal-faced composite panel system. Pre-fabricated sandwich panels with aluminium faces and core (polyethylene, mineral wool, or fire-rated core).</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Non-load-bearing facade skin of factory-made sandwich panels with metal faces and a bonded core, hung in front of the insulated exterior wall. The panels are folded into cassettes or trays and mechanically fixed to an aligned metal sub-frame, with defined joints and cavity ventilation. Suitable for new build and fast retrofit of large flat surfaces; the core must be declared non-combustible where building height or use demands it.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">CRITICAL: Fire rating heavily depends on core material. PE-core panels: Class E or D (restricted/banned in many EU countries post-Grenfell). Mineral-wool-core panels: A2-s1,d0 compliant (preferred for high-rise). Modularity: high; fast assembly (1-2m²/hour on-site). Thermal performance: good integration with insulation layer; achieves U-values 0.15 W/m²K. Retrofit application: excellent; non-structural overlay. Ban status: UK, France, Germany, Netherlands restrict combustible cores on buildings &gt;11-18m.</td>
</tr>
<tr>
<td>FaCP-METAL-SHEET-STANDING-SEAM</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Stehfalz-Metallblechfassade</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Profiliertes Metallblech (Aluminium, Stahl, Kupfer, Zink) oder Stehfalz-Fassadenbekleidung mit verschlossenen/verschränkten Nähten. Einschliesslich dichter Metallkassettensysteme.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Nichttragende Metallhaut aus Profilblech oder Stehfalzbahnen in Aluminium, Stahl, Kupfer oder Zink vor der Aussenwand. Die Bahnen werden auf einer hinterlüfteten Holz- oder Metall-Unterkonstruktion gefalzt oder geklipst, mit Schiebehaftern für die thermische Längenänderung. Geeignet für Neubau und leichte Sanierungsüberkleidungen an exponierten und geometrisch anspruchsvollen Fassaden mit hoher Anforderung an Wasserdichtigkeit bei geringem Zusatzgewicht.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Metal sheet standing-seam facade</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Profiled metal sheet (aluminium, steel, copper, zinc) or standing-seam facade cladding with locked/interlocking seams. Includes weathertight metal cassette systems.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Non-load-bearing metal skin of profiled sheet or standing-seam bands in aluminium, steel, copper, or zinc in front of the exterior wall. The bands are seamed or clipped onto a ventilated timber or metal sub-frame using sliding clips that accommodate thermal movement. Suitable for new build and lightweight retrofit overlays on exposed and geometrically demanding facades where high watertightness is required at low added dead load.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Fire rating: A2-s1,d0 (aluminium composite core requires verification; pure metal A1). Thermal break requirement: integrated in frame to achieve U &lt;0.20 W/m²K. Market growth: 6.4% CAGR 2024-2030 (fastest growing segment). Regional strength: Scandinavia, Germany, Alpine region. Advantages: watertightness, long spans, architectural expression. Retrofit: excellent for non-structural overlay, minimal weight.</td>
</tr>
<tr>
<td>FaCP-NATURAL-STONE-VENTILATED</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Vorgehängte Natursteinfassade</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Natursteinplatten-, -fliesen- oder Paneelsystem für vorgehängte Fassaden (Granit, Kalkstein, Schiefer, Marmor). Einschliesslich steinkaschierter Metallkassetten und Unterkonstruktionssysteme mit Wärmebrechern.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Nichttragende Bekleidung aus Natursteinplatten oder steinkaschierten Kassetten vor der tragenden Aussenwand. Die Platten werden mit Hinterschnitt- oder Dornankern auf einer justierbaren, thermisch getrennten Metall-Unterkonstruktion gehalten; Dämmung und Hinterlüftungsraum liegen dahinter. Geeignet für repräsentative Neubauten und Fassadenerneuerungen mit langer Nutzungsdauer, wenn schwere Formate und ein zusätzlicher Lastzuschlag akzeptiert werden.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Ventilated natural stone cladding</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Natural stone slab, tile, or panel ventilated facade system (granite, limestone, slate, marble). Includes stone-faced metal cassettes and sub-frame support systems with thermal breaks.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Non-load-bearing cladding of natural stone slabs or stone-faced cassettes carried in front of the load-bearing exterior wall. The slabs are held by undercut or dowel anchors on an adjustable, thermally separated metal sub-frame, with insulation and ventilated cavity behind the stone. Suitable for representative new build and facade renewal with long service life, provided that heavy formats and an additional dead-load allowance are accepted.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Fire rating: A1 (natural stone inherently non-combustible). Thermal performance: requires integrated insulation layer; U-values 0.20-0.12 W/m²K achievable. Weight consideration: structural frame design critical. Regional: Northern Europe (Nordic stone), Mediterranean (limestone/marble), Central Europe (slate). High durability (&gt;60 years). Retrofit suitability: good for facade replacement on load-bearing walls.</td>
</tr>
<tr>
<td>FaCP-OTHER</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Sonstige / unbekannte Fassadenbekleidung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Fassadenbekleidungsprodukt nicht klassifiziert oder noch unbekannt; neuartige Materialien oder Versuchssysteme nicht in primärer Taxonomie aufgeführt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Platzhalter für Fassadenbekleidungen, deren Produkt- oder Systemtyp zum Zeitpunkt der Ausschreibung noch nicht festgelegt oder nicht klassifizierbar ist. Funktionale Anforderungen wie Wetterschutz, Wärmeschutz, Brandverhalten, Untergrund- und Befestigungsprinzip sowie erwartete Nutzungsdauer sind gesondert zu beschreiben. Nur in frühen Planungsphasen oder bei unvollständiger Bestandskenntnis verwenden.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Fallback für frühe Entwurfsstufen, fehlende Daten oder neuartige Fassadensysteme (z.B. intelligente Beschichtungen, biobasierte Verbundstoffe, graphen-verstärkte Materialien). Sollte vor detaillierter Spezifikation auf spezifischen Typ aufgelöst werden.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Other / unknown facade covering</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Facade covering product not classified or not yet known; emerging materials or experimental systems not listed in primary taxonomy.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Placeholder for facade coverings whose product or system type is not yet fixed at tender stage or cannot be classified. Functional requirements such as weather protection, thermal performance, reaction to fire, substrate and fixing principle, and expected service life must be stated separately in the specification. Use only in early design stages or where information on the existing facade is incomplete.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Fallback for early design stages, missing data, or novel facade systems (e.g., smart coatings, bio-based composites, graphene-enhanced materials). Should be resolved to specific type before detailed specification.</td>
</tr>
<tr>
<td>FaCP-PREFAB-MODULAR-METAL</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Vorgefertigtes modulares Metallfassaden-System</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Werkseitig montiertes modulares Fassadensystem mit Aluminium-, Stahl- oder Verbundmetallrahmen, integrierten Isolationsschichten, Verkleidungspaneelen (Metallverbund, Natursteinfurnier oder Keramikoberfläche) und mechanisch befestigter Unterkonstruktion.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Nichttragendes Fassadenmodul, werkseitig aus Metallrahmen mit integrierter Dämmung und fertiger Bekleidungsschale montiert. Die Elemente werden geschosshoch vor das Primärtragwerk gesetzt und an Konsolen verankert, die Justierung und thermische Trennung erlauben; die Modulfugen werden mit Dichtprofilen oder Versiegelung geschlossen. Geeignet für Neubau und späteren teilweisen Austausch an hohen Gewerbe-, Industrie- und Technikgebäuden mit Anforderungen an Montagegeschwindigkeit, Masshaltigkeit und wiederholbare Details.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Prefabricated modular metal facade system</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Factory-assembled modular facade system using aluminium, steel, or composite metal frames with integrated insulation layers, cladding panels (metal composite, natural stone veneer, or ceramic facing), and mechanically-fixed sub-structure.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Non-load-bearing facade module assembled in the factory from metal frames with integrated insulation and a finished cladding face. The units are set storey-high in front of the primary structure and anchored on brackets that allow adjustment and thermal separation, with gasketed or sealed joints between modules. Suitable for new build and later partial replacement on tall commercial, industrial, and technical buildings requiring erection speed, dimensional accuracy, and repeatable details.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Applications: high-rise commercial, data centers, industrial facilities. Fire rating: A2-s1,d0 (metal frame + non-combustible insulation core). Thermal break: mandatory; achieved via composite frame or inserted strips. Modularity: dimensions typically 1.5m x 5-7m height. Assembly: fast; anchored to building structure at discrete points. Quality control: factory-built precision reduces site defects. Thermal performance: U-values 0.12-0.15 W/m²K achievable. Regional strength: Germany, Switzerland, Nordic countries (commercial sector). Sustainability: modular design allows future upgrade/replacement without full facade demolition.</td>
</tr>
<tr>
<td>FaCP-PREFAB-MODULAR-TIMBER</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Vorgefertigtes modulares Holzfassaden-System</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Fabrikmässig gefertigtes modulares holzbasiertes Fassadensystem oder Umhüllung. Typischerweise mit Holztragrahmen, integrierter Isolation, Belüftungshohlraum, Fertigungsschicht (Holz, Putz oder Verbundstoff) und vorintegrierten TGA-Rohbauten (Fenster, Lüftung, Solaranlagen).</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Nichttragendes Fassadenmodul, werkseitig als Holzrahmenelement mit Dämmung, Luftdichtungsschicht, Bekleidung und häufig bereits eingebauten Fenstern gefertigt. Die Module werden geschosshoch angeliefert, eingehoben und punktweise am bestehenden oder neuen Tragwerk verankert; Fugen werden abgedichtet und Installationen vor Ort angeschlossen. Geeignet für Neubau und Sanierung im bewohnten Zustand, wenn Bauzeit und Störung gering bleiben müssen und die Bestandsgeometrie der Fassade vermessen vorliegt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Innovationsschwerpunkt: Multifunktionale Fassade mit thermischen, akustischen und TGA-Funktionen werkseitig. Sanierungsanwendung (4RinEU-, Energiesprong-Projekte): schnelle Einsatzbarkeit auf bestehendem Tragwerk; Vor-Ort-Montagezeit 1-2 Wochen für Wohngebäude. Brandschutz: A2-s1,d0 erreichbar mit Mineralwollintegration. Montage-Vorteil: reduziert Vor-Ort-Arbeit um 70%, verbessert Präzision, minimiert Bewohnerstörung. Regionale Piloten: Niederlande, Norwegen, Spanien, Italien (sozialer Wohnungsbau-Sanierungen). Regulatorische Unterstützung: BPR 2024 erleichtert Fertigteilmodul-Handel über EU-Grenzen. Kosten: 10-15% Prämie durch Energieeinsparungen und reduzierte Arbeit amortisiert. Lieferkette: wachsende Kapazität (Blokable, Fertigungskonsortien).</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Prefabricated modular timber facade system</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Factory-manufactured modular timber-based facade exoskeleton or wrapper system. Typically includes structural timber frame, integrated insulation, ventilated cavity, finishing layer (wood, plaster, or composite), and pre-integrated MEP rough-ins (windows, ventilation, solar fittings).</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Non-load-bearing facade module manufactured in the factory as a timber-framed element with insulation, air-tight layer, cladding, and often windows already fitted. The modules are delivered storey-high, lifted into place, and anchored at discrete points to the existing or new load-bearing structure, with joints sealed and services connected on site. Suitable for new build and for retrofit of occupied buildings where site time and disruption must stay minimal and the existing facade geometry has been surveyed.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Innovation focus: multifunctional facade integrating thermal, acoustic, and MEP functions off-site. Retrofit application (4RinEU, Energiesprong projects): rapid deployment on existing load-bearing structure; on-site assembly time 1-2 weeks for residential. Fire rating: A2-s1,d0 achievable with mineral wool integration. Assembly advantage: reduces on-site labor by 70%, improves precision, minimizes occupant disruption. Regional pilots: Netherlands, Norway, Spain, Italy (social housing retrofits). Regulatory support: CPR 2024 facilitates prefab module trading across EU borders. Cost: 10-15% premium amortized over energy savings and reduced labor. Supply chain: growing capacity (Blokable, prefabrication consortia).</td>
</tr>
<tr>
<td>FaCP-RENDER-ETICS-WDVS</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Putzsystem / WDVS-Fassade</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Mineralputz, Aussenputz, Waermedaemmverbundsystem (WDVS/ETICS, EPS, Mineralwolle, PIR) oder Zement-/Kunstharzfassadenoberfläche. Mit Klebstoff und mechanischer Verankerung am Untergrund befestigt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Nichttragendes, geklebtes Aussendämm- und Putzsystem, direkt auf der tragenden Aussenwand ohne Hinterlüftungsraum. Die Dämmplatten werden auf den Untergrund geklebt und mechanisch verdübelt und anschliessend mit bewehrtem Unterputz mit eingelegtem Armierungsgewebe und Deckputz überzogen. Geeignet für Neubau und energetische Sanierung massiver Wände mit Verdickung des Wandaufbaus von aussen; Ebenheit, Dübeltragfähigkeit und Feuchtezustand des Untergrunds sind zu prüfen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Brandschutz: hängt vom Isolierungskern ab. EPS (traditionell): typischerweise D-s2,d0 oder E (Hochhaus verboten). Mineralwolle/PIR-Kern: A2-s1,d0-konform. Wärmeleistung: ausgezeichnet (U-Werte 0,12-0,08 W/m²K erreichbar). Sanierungsdominanz: 60-70% der EU-Tiefenenergetischen Sanierungen verwenden ETICS (Fit-for-55-Treiber). Nachhaltigkeitsbedenken: EPS-Abfall; Mineralwollealternativen wachsen. Montage: gemässigte Fachkompetenz; wetterabhängig. Regional: universelle Anwendung über alle EU-Klimazonen. Lebenszyklus: 20-40 Jahre (Deckschicht-Erneuerung erforderlich).</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Render / ETICS facade system</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Mineral render, plaster, external thermal insulation composite system (ETICS / WDVS, EPS, mineral wool, PIR), or cement/acrylic facade finish. Bonded to substrate with adhesive and mechanical fixing.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Non-load-bearing bonded external insulation and render system applied directly onto the load-bearing exterior wall without a ventilated cavity. Insulation boards are adhesive-bonded and mechanically anchored to the substrate and then covered with a reinforced base coat with embedded mesh and a finishing render. Suitable for new build and for energy retrofit of solid walls where the wall is thickened from outside; flatness, anchor capacity, and moisture condition of the substrate must be verified.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Fire rating: depends on insulation core. EPS (traditional): typically D-s2,d0 or E (banned high-rise). Mineral wool / PIR core: A2-s1,d0 compliant. Thermal performance: excellent (U-values 0.12-0.08 W/m²K achievable). Retrofit dominance: 60-70% of EU deep energy retrofits use ETICS (Fit-for-55 policy driver). Sustainability concern: EPS waste; mineral wool alternatives growing. Installation: moderate skill; weather-dependent. Regional: universal application across all EU climates. Lifecycle: 20-40 years (finishing coat renewal needed).</td>
</tr>
<tr>
<td>FaCP-RENDER-ETICS-WDVS-INS</td>
<td>FaCP-RENDER-ETICS-WDVS</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">WDVS Daemm-Schicht</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Daemmplatten-Schicht eines WDVS/ETICS-Fassadensystems (EPS, Mineralwolle oder PIR).</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Dämmschicht innerhalb eines geklebten Putzfassadensystems; sie bildet die Wärmeschutzebene zwischen tragender Wand und Putzoberfläche. Die Platten werden auf dem ausgeglichenen Untergrund fugendicht und versetzt im Kleber verlegt und mit auf Windlast und Untergrund abgestimmten Dübeln gesichert, wobei die Schichtdicke die Wärmeleistung des Gesamtaufbaus bestimmt. Sie wird separat ausgewiesen, weil Dicke, Dämmstoff und Brandverhalten unabhängig vom Deckputz festgelegt und kalkuliert werden.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">LCA-Schichtkomponente von FaCP-RENDER-ETICS-WDVS. Fuer Oekobilanz-Zerlegung und CO2-Berechnung; keine eigenstaendige Fassadenprodukt-Klassifikation.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">ETICS insulation layer</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Insulation board layer of an ETICS / WDVS facade system (EPS, mineral wool, or PIR).</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Insulation layer within a bonded render facade system, forming the thermal barrier between the load-bearing wall and the render finish. The boards are laid in adhesive on the levelled substrate with tight, offset joints and secured with anchors sized to wind load and substrate, the layer thickness governing the thermal performance of the whole build-up. It is stated separately because thickness, insulation material, and fire behaviour are specified and costed independently of the render finish.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">LCA layer component of FaCP-RENDER-ETICS-WDVS. Used for ecobilans decomposition and carbon calculation; not a standalone facade product classification.</td>
</tr>
<tr>
<td>FaCP-RENDER-ETICS-WDVS-RENDER</td>
<td>FaCP-RENDER-ETICS-WDVS</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">WDVS Putz-Schicht</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Putz- oder Oberputz-Schicht eines WDVS/ETICS-Fassadensystems.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Putzschicht eines geklebten Aussendämmsystems; sie schützt die Dämmung gegen Witterung, Stoss und UV-Strahlung und bildet die sichtbare Fassadenoberfläche. Sie wird mehrlagig auf die Dämmplatten aufgebracht, als bewehrter Unterputz mit eingelegtem Armierungsgewebe und anschliessendem Deckputz, wobei Struktur und Farbton vorzugeben sind. Sie wird separat ausgewiesen, weil die Oberfläche in kürzeren Zyklen erneuert wird als die Dämmung und ihre Stossfestigkeit sowie Dampfdurchlässigkeit eigene Anforderungen sind.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">LCA-Schichtkomponente von FaCP-RENDER-ETICS-WDVS. Fuer Oekobilanz-Zerlegung und CO2-Berechnung; keine eigenstaendige Fassadenprodukt-Klassifikation.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">ETICS render finish layer</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Render or plaster finish layer of an ETICS / WDVS facade system.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Render finish layer of a bonded external insulation system, protecting the insulation against weather, impact, and ultraviolet radiation and forming the visible facade surface. It is applied in several passes onto the insulation boards as a reinforced base coat with embedded mesh followed by the finishing coat, with texture and colour to be specified. It is stated separately because the finish is renewed in shorter cycles than the insulation and its impact resistance and vapour permeability are requirements of their own.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">LCA layer component of FaCP-RENDER-ETICS-WDVS. Used for ecobilans decomposition and carbon calculation; not a standalone facade product classification.</td>
</tr>
<tr>
<td>FaCP-RETROFIT-OVERCLADDING</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Sanierungsüberkleidungssystem (Verbund)</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Nicht-tragende Fassadenüberlagerung oder Umhüllung über bestehende Fassade bei Sanierungs-/Renovierungsprojekten. Kombiniert Verkleidungsschicht (typischerweise ETICS, Lüftungspaneel oder Fertigmodul) mit mechanischen Befestigungen und/oder Klebstoff auf bestehendem Untergrund. Primäre Anwendung: EU Fit-for-55-Tiefensanierungen im Wohn-/Gewerbebebestand.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Nichttragende Überkleidung über der erhaltenen bestehenden Fassade; sie ergänzt Dämmung und eine neue wetterschützende Oberfläche, ohne die alte Wand zu entfernen. Der neue Aufbau wird durch die alte Oberfläche im tragenden Untergrund verankert, entweder geklebt mit Putz oder auf einer ausgleichenden Unterkonstruktion, die Unebenheiten des Bestands aufnimmt. Geeignet für die energetische Erneuerung des Gebäudebestands; Zustand, Ebenheit und Verankerungsfähigkeit der alten Fassade sowie neue Fenster-, Dachrand- und Sockeldetails sind vorab zu klären.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Schlüsselvorteil: nicht-destruktiv; vermeidet Fassadenabriss/Entsorgungsabfall. Wärmeverbesserung: typische Sanierung fügt 80-120mm Isolation hinzu, reduziert U-Wert von &gt;0,5 W/m²K (vor 1980ern) auf &lt;0,15 W/m²K (nZEB-Standard). Montage: erfordert anfängliche Fassadenprüfung, Feuchte-Bewertung, Stützkonstruktionsplanung. Arbeitsintensiv aber geringere Vor-Ort-Störung vs. traditioneller Fassadenaustausch. Regulative Treiber: EPBD 2024 verlangt Gebäudesanierung bis 2050; EU-Mittel (REPowerEU) unterstützen Sanierungsprojekte. Marktvolumen: 60-70% europäischer Fassadenarbeit (2024-2030). Regionale Variation: Sanierungsintensität höchste in Nord-/Mitteleuropa (älterer Gebäudebestand, Klimatreiber).</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Retrofit overcladding system (composite)</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Non-structural facade overlay or wrapper applied over existing facade on retrofit/renovation projects. Combines cladding layer (typically ETICS, ventilated panel, or prefab module) anchored to existing substrate with mechanical fixings and/or adhesive. Primary application: EU Fit-for-55 deep energy retrofits on residential/commercial stock.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Non-load-bearing overlay built over a retained existing facade, adding insulation and a new weather-protecting surface without removing the old wall. The new build-up is anchored through the old surface into the load-bearing substrate, either bonded with render or carried on a levelling sub-frame that takes up the unevenness of the existing wall. Suitable for energy refurbishment of existing stock; condition, flatness, and anchor capacity of the old facade as well as new window, eaves, and plinth details must be established beforehand.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Key advantage: non-destructive; avoids facade demolition/disposal waste. Thermal improvement: typical retrofit adds 80-120mm insulation, achieving U-value reduction from &gt;0.5 W/m²K (pre-1980s) to &lt;0.15 W/m²K (nZEB standard). Installation: requires initial facade inspection, moisture assessment, support frame design. Labor intensive but lower on-site disruption vs. traditional facade replacement. Regulatory drivers: EPBD 2024 requires building renovation within 2050 timeline; EU funds (REPowerEU) support retrofit projects. Market volume: 60-70% of European facade work (2024-2030). Regional variation: retrofit intensity highest in Northern/Central Europe (older building stock, climate drivers).</td>
</tr>
<tr>
<td>FaCP-SYNTHETIC-VENTILATED</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kunststoff-Vorgehängte Fassade</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">HPL (Hochdrucklaminat), Kunststoff-, Acryl-, Verbundlaminat oder andere synthetische vorgehängte Fassadenpaneele. Einschliesslich glasfaserverstärkter Kunststoff (GFK) und Polykarbonat-Systemen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Nichttragende Bekleidung aus Kunststoffpaneelen wie Laminaten, Kunststoffplatten oder faserverstärkten Verbundwerkstoffen, vorgehängt vor der gedämmten Aussenwand. Die Paneele werden mechanisch auf einer Metall- oder Holz-Unterkonstruktion mit Hinterlüftungsraum befestigt, mit Befestigungen und Fugenbreiten für die vergleichsweise grosse thermische Längenänderung des Materials. Geeignet für Gewerbe-, Industrie- und niedrige Gebäude; Farbbeständigkeit unter UV-Belastung, Stossfestigkeit und Brandverhalten der Paneele sind anzugeben.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Synthetic ventilated facade panel</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">HPL (high-pressure laminate), plastic, acrylic, composite laminate, or other synthetic ventilated facade panel cladding. Includes fibre-reinforced plastic (FRP) and polycarbonate systems.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Non-load-bearing cladding of synthetic panels such as laminates, plastics, or fibre-reinforced composites hung in front of the insulated exterior wall. The panels are mechanically fixed to a metal or timber sub-frame with a ventilated cavity, using fixings and joint widths that allow the comparatively large thermal movement of the material. Suitable for commercial, industrial, and low-rise buildings; colour fastness under ultraviolet exposure, impact resistance, and reaction to fire of the panel must be stated.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Fire rating: typically D-s2,d0 or E (combustibility concern; restricted on high-rise residential). Thermal: insulation layer required; moderate U-values 0.15-0.20 W/m²K. Maintenance: low; weather resistant. Durability: 20-30 years (UV degradation concern). Regional: niche market; used for industrial, commercial, or low-rise applications. Circular economy: limited end-of-life recycling. Growth: slower than other systems (environmental concerns, regulatory tightening).</td>
</tr>
<tr>
<td>FaCP-TIMBER-VENTILATED</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Holz-Vorgehängte Fassade</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Holz-, Massivholz-, Konstruktionsholz- oder Holzwerkstoff-Fassadensystem mit Belüftung, Lamellen, Bretter oder Paneelsystem. Einschliesslich Massivholzbretter, Lärche, Zeder, thermisch modifiziertes Holz (TMH) und Kreuzschichtholz (KVH) -Verkleidungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Nichttragende Holzbekleidung aus Brettern, Lamellen oder Holzwerkstoffplatten vor der gedämmten Aussenwand. Die Befestigung erfolgt mit sichtbaren oder verdeckten Verbindungsmitteln auf einer Lattung, die allseitige Hinterlüftung und Abtrocknung der Bekleidung sicherstellt. Geeignet für Neubau und Sanierung bei geringem Zusatzgewicht; Oberflächenbehandlung, Hirnholzausbildung und zulässiger Vergrauungsgrad sind festzulegen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Brandschutz: typischerweise D-s2,d0 oder Klasse E (Flammschutzbehandlung erforderlich für mehrgeschossige Wohngebäude; A2-s1,d0 erreichbar mit Verkoolungsschicht-Design). Holzbasierte multifunktionale Fertigsysteme entstehend (4RinEU-, Energiesprong-Projekte). Regionale Stärke: Skandinavien (nordische Tradition), Österreich, Bayern. Nachhaltigkeitsvorteil: erneuerbarer Werkstoff, Kreislaufwirtschaft-ausgerichtet, graue Energie geringer als mineralische Alternativen. Sanierungsanwendung: ausgezeichnet für modulare Fertigsysteme; schnelle Vor-Ort-Montage (reduziert Arbeitsstörungen). EU-Politische Unterstützung: Holzbauten unter der 2024-Grünen-Gebäude-Richtlinie angeregt.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Timber ventilated facade system</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Wood, solid timber, engineered wood, or wood-composite ventilated facade cladding, slats, boards, or panel system. Includes solid timber boards, larch, cedar, thermally-modified wood (TMW), and cross-laminated timber (CLT) facings.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Non-load-bearing timber cladding of boards, slats, or wood-based panels mounted in front of the insulated exterior wall. Fixing is by visible or concealed fasteners onto a battened sub-frame that ensures rear ventilation and all-round drying of the cladding. Suitable for new build and retrofit at low added dead load; surface treatment, end-grain detailing, and the accepted degree of weathering are to be specified.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Fire rating: typically D-s2,d0 or E class (flame-retardant treatment required for multi-story residential, A2-s1,d0 achievable with charring layer design). Timber-based multifunctional prefab systems emerging (4RinEU, Energiesprong projects). Regional strength: Scandinavia (Nordic tradition), Austria, Bavaria. Sustainability advantage: renewable material, circular economy aligned, embodied carbon lower than mineral alternatives. Retrofit application: excellent for modular prefab systems; quick on-site installation (reduces labor disruption). EU policy support: timber construction incentivized under 2024 Green Building Directive.</td>
</tr>
</tbody>
</table>
</div>
