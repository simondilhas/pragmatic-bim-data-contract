# Connection physical type classification

Source: [`connection-physical-type-en.skos.ttl`](sources/connection-physical-type.ttl)

## Scheme

- **definition (de):** Klassifikation physischer Verbindungselemente, die Raeume verbinden, abgestimmt auf IFC-Entitaetstypen.
- **definition (en):** Classification of physical connector elements that connect spaces, aligned with IFC entity types.
- **prefLabel (de):** Typ physischer Verbindungselemente
- **prefLabel (en):** Connection Physical Type
- **title (en):** Connection Physical Type

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
<td>cable</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kabel</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Verbindungssegment fuer elektrische oder Datenkabel.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Cable</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Electrical or data cable connector segment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>conduit</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Leerrohr</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Verbindungssegment fuer elektrische oder Datenleerrohre.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Conduit</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Electrical or data conduit connector segment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>door</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Tuer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Zugangsverbindung fuer Personen ueber ein Tuerlement.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Door</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Human access connector via a door element.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>duct</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Luftkanal</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Verbindungssegment fuer Luftverteilung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Duct</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Air distribution connector segment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>network_other</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Sonstiges Netz</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Sonstiges Netzverbindungssegment, das nicht durch kontrollierte Werte abgedeckt ist.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Network Other</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Other network connector segment not covered by controlled values.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>opening_other</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Sonstige Oeffnung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Sonstige oeffnungsartige Verbindung, die nicht durch Tuer oder Fenster abgedeckt ist.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Opening Other</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Other opening-style connector not covered by door or window.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>pipe</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Rohr</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Verbindungssegment fuer Fluessigkeits- oder Gasverteilung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Pipe</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Fluid or gas distribution connector segment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>window</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Fenster</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Sicht- und Tageslichtverbindung ueber ein Fensterelement.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Window</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Visual and daylight connector via a window element.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
</tbody>
</table>
</div>
