# Separator wall role classification

Source: [`separator-wall-role-classification-en.skos.ttl`](sources/separator-wall-role.ttl)

## Scheme

- **definition (de):** Topologische Rollenklassifikation fuer wandbasierte Trennelemente (SeparatorWall), abgeleitet aus den angrenzenden Raumbeziehungen.
- **definition (en):** Topological role classification for wall-based separating elements (SeparatorWall), derived from adjacent space relationships.
- **prefLabel (de):** Klassifikation der Trennwandrollen
- **prefLabel (en):** Building Separator Wall Role Classification
- **title (en):** Building Separator Wall Role Classification

## Hierarchy

```mermaid
classDiagram
direction TB
class n_W_ABG["W-ABG: Above ground wall"]
class n_W_BLG["W-BLG: Below ground wall"]
class n_W_CIR_HOR["W-CIR-HOR: Horizontal circulation enclosure wall"]
class n_W_CIR_VRT["W-CIR-VRT: Vertical circulation enclosure wall"]
class n_W_EXT["W-EXT: Exterior wall"]
class n_W_GRD["W-GRD: Below-grade enclosure wall"]
class n_W_INT["W-INT: Interior wall"]
class n_W_PAR["W-PAR: Party wall"]
class n_W_PRT["W-PRT: Internal partition wall"]
class n_W_SVC["W-SVC: Service and shaft enclosure wall"]
class n_W_UNT["W-UNT: Unit boundary wall"]
n_W_EXT <|-- n_W_ABG
n_W_EXT <|-- n_W_BLG
n_W_INT <|-- n_W_CIR_HOR
n_W_INT <|-- n_W_CIR_VRT
n_W_INT <|-- n_W_GRD
n_W_INT <|-- n_W_PAR
n_W_INT <|-- n_W_PRT
n_W_INT <|-- n_W_SVC
n_W_INT <|-- n_W_UNT
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
<td>W-EXT</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aussenwand</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Wand, die konditionierten oder nutzbaren Raum von der Aussenumgebung trennt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Einschliesslich Fassaden- und Huellenwaende, wenn die Aussenabgrenzung die Anforderungen bestimmt; unterteilt nach ober- und unterirdischer Lage.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Exterior wall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Wall separating conditioned or occupied space from the exterior environment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Including facade and envelope walls where exterior separation drives requirements; subdivided by above- and below-ground position.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>W-ABG</td>
<td>W-EXT</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Oberirdische Wand</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenwand oberhalb der Gelaendehoehe, die konditionierten oder nutzbaren Raum von der Aussenumgebung trennt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Einschliesslich Fassadenwaende, Vorhangfassaden, Attikawaende und andere oberirdische Huellenwaende.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Above ground wall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Exterior wall above ground level separating conditioned or occupied space from the exterior environment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Including facade walls, curtain walls, parapet walls, and other above-grade envelope walls.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>W-BLG</td>
<td>W-EXT</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Unterirdische Wand</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenwand unterhalb der Gelaendehoehe, die Innenraum von Erdreich oder aussenseitigen Untergeschossbedingungen trennt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Einschliesslich Kellerumfassungswaende, Stuetzwaende und andere unterirdische Huellenwaende.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Below ground wall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Exterior wall below ground level separating interior from earth or exterior below-grade conditions.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Including basement perimeter walls, retaining walls, and other below-grade envelope walls.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>W-INT</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Innenwand</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Innenwand, deren primaere Rolle durch die topologische Lage zu angrenzenden Raeumen bestimmt wird.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Interior wall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Interior wall whose primary role is defined by adjacent space topology.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>W-CIR-HOR</td>
<td>W-INT</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wand an horizontaler Erschliessung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Wand, die einen horizontalen Erschliessungsraum begrenzt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Einschliesslich Waende an Korridoren, Durchgaengen, Bruecken und Fluchtwegen, die nicht primaer Nutzungseinheitstrennwaende sind.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Horizontal circulation enclosure wall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Wall bounding a horizontal circulation space.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Including corridor, hallway, bridge, and emergency exit route walls that are not primarily unit boundaries.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>W-CIR-VRT</td>
<td>W-INT</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Treppenhauswand / Aufzugwand</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Wand, die einen vertikalen Erschliessungsraum begrenzt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Einschliesslich Waende um Treppenhaeuser, Aufzugsfoyers, Rolltreppen und Rampen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Vertical circulation enclosure wall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Wall bounding a vertical circulation space.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Including walls around staircases, elevator lobbies, escalator spaces, and ramps.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>W-GRD</td>
<td>W-INT</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Keller-Umfassungswand</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Innenwand mit Bezug zu Keller- oder unterirdischen Randbedingungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Einschliesslich Kellerumfassungswaende und erdberuehrte Innentrennungen, wenn der Untergeschosskontext die Anforderungen bestimmt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Below-grade enclosure wall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Interior wall associated with below-grade or cellar perimeter conditions.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Including cellar perimeter walls and retaining-related interior separations where below-grade context drives requirements.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>W-PAR</td>
<td>W-INT</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Brandwand / Grenzwand</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Wand, die dieses Gebaeude von einem Nachbargebaeude oder einer rechtlichen Grundstuecksgrenze trennt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Party wall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Wall separating this building from an adjacent building or legal plot boundary.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>W-PRT</td>
<td>W-INT</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Innere Trennwand</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Wand, die Raeume innerhalb derselben Nutzungseinheit voneinander trennt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Einschliesslich Raum-zu-Raum-Trennwaende, wenn keine Seite Erschliessung, Technik, Einheitstrennung oder Aussenbereich ist.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Internal partition wall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Wall separating spaces within the same occupancy unit.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Including room-to-room partitions where neither side is circulation, service, unit boundary, or exterior.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>W-SVC</td>
<td>W-INT</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Technik- und Schachtwand</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Wand, die Technik-, Versorgungs- oder Hohlraeume begrenzt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Einschliesslich Waende um Technikraeume, Schaechte, Steigzonen und andere Unterstuetzungs- oder Hohlraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Service and shaft enclosure wall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Wall bounding technical, utility, or void spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Including walls around mechanical rooms, shafts, risers, and other support or void spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>W-UNT</td>
<td>W-INT</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wohnungstrennwand</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Wand, die selbstaendige Nutzungs- oder Brandabschnittseinheiten voneinander trennt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Einschliesslich Waende zwischen Wohnungen, Mieteinheiten oder zwischen Einheit und gemeinsamer Erschliessung, wenn die Einheitstrennung die Anforderungen bestimmt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Unit boundary wall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Wall separating independent occupancy or fire-compartment units.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Including walls between dwellings, between tenant units, or between a unit and common circulation where the unit boundary drives requirements.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
</tbody>
</table>
</div>
