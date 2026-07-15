# Abstract person relationship types

Source: [`person-relationship-type.skos.ttl`](sources/person-relationship-type.ttl)

## Scheme

- **description (de):** CRM-orientierte Personenbeziehungstypen für soziale, familiäre, berufliche, organisatorische, kommerzielle und Interessen-Verknüpfungen.
- **description (en):** CRM-oriented person relationship predicates for social, family, professional, organizational, commercial, and interest links.
- **prefLabel (de):** Abstrakte Personenbeziehungstypen
- **prefLabel (en):** Abstract person relationship types
- **title (en):** Abstract person relationship types

## Hierarchy

```mermaid
classDiagram
direction TB
class n_AUN["AUN: Aunt or uncle of"]
class n_CHD["CHD: Child of"]
class n_CIL["CIL: Child-in-law of"]
class n_CLT["CLT: Client of"]
class n_COL["COL: Was colleague of"]
class n_CSN["CSN: Cousin of"]
class n_CST["CST: Consulted for"]
class n_EXP["EXP: Has expertise in"]
class n_FRI["FRI: Friend of"]
class n_GCH["GCH: Grandchild of"]
class n_GPR["GPR: Grandparent of"]
class n_GRP_COM["GRP-COM: Commercial relationships"]
class n_GRP_FAM["GRP-FAM: Family relationships"]
class n_GRP_INT["GRP-INT: Interest and expertise"]
class n_GRP_ORG["GRP-ORG: Organization relationships"]
class n_GRP_PRO["GRP-PRO: Professional relationships (person)"]
class n_GRP_SOC["GRP-SOC: Social relationships"]
class n_HKM["HKM: Has key account manager"]
class n_INT["INT: Has interest"]
class n_ITR["ITR: Introduced by"]
class n_KAM["KAM: Is key account manager for"]
class n_KNW["KNW: Knows"]
class n_LRN["LRN: Learning about"]
class n_MTR["MTR: Mentored by"]
class n_NNP["NNP: Niece or nephew of"]
class n_PAR["PAR: Parent of"]
class n_PIL["PIL: Parent-in-law of"]
class n_REF["REF: Referred by"]
class n_RPT["RPT: Reports to"]
class n_SIB["SIB: Sibling of"]
class n_SPO["SPO: Spouse of"]
class n_STU["STU: Studied at"]
class n_TCH["TCH: Teaches at"]
class n_VND["VND: Vendor of"]
class n_WAT["WAT: Works at"]
class n_WRK["WRK: Worked at"]
n_GRP_COM <|-- n_HKM
n_GRP_COM <|-- n_KAM
n_GRP_FAM <|-- n_AUN
n_GRP_FAM <|-- n_CHD
n_GRP_FAM <|-- n_CIL
n_GRP_FAM <|-- n_CSN
n_GRP_FAM <|-- n_GCH
n_GRP_FAM <|-- n_GPR
n_GRP_FAM <|-- n_NNP
n_GRP_FAM <|-- n_PAR
n_GRP_FAM <|-- n_PIL
n_GRP_FAM <|-- n_SIB
n_GRP_FAM <|-- n_SPO
n_GRP_INT <|-- n_EXP
n_GRP_INT <|-- n_INT
n_GRP_INT <|-- n_LRN
n_GRP_ORG <|-- n_CLT
n_GRP_ORG <|-- n_CST
n_GRP_ORG <|-- n_STU
n_GRP_ORG <|-- n_TCH
n_GRP_ORG <|-- n_VND
n_GRP_ORG <|-- n_WAT
n_GRP_ORG <|-- n_WRK
n_GRP_PRO <|-- n_COL
n_GRP_PRO <|-- n_MTR
n_GRP_PRO <|-- n_REF
n_GRP_PRO <|-- n_RPT
n_GRP_SOC <|-- n_FRI
n_GRP_SOC <|-- n_ITR
n_GRP_SOC <|-- n_KNW
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
<th class="pbs-lang-col" data-lang="de" data-field="scope_note">Scope note</th>
<th class="pbs-lang-col" data-lang="en" data-field="label">Label</th>
<th class="pbs-lang-col" data-lang="en" data-field="definition">Definition</th>
<th class="pbs-lang-col" data-lang="en" data-field="scope_note">Scope note</th>
</tr>
</thead>
<tbody>
<tr>
<td>AUN</td>
<td>GRP-FAM</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Tante/Onkel von</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person ist Tante oder Onkel einer anderen Person, einschliesslich durch Blutsverwandtschaft, Adoption oder Heirat mit einer Tante bzw. einem Onkel.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Aunt or uncle of</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person is an aunt or uncle of another person, including by blood, adoption, or marriage to an aunt or uncle.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_person.</td>
</tr>
<tr>
<td>CHD</td>
<td>GRP-FAM</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kind von</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person ist leibliches, adoptiertes oder rechtliches Kind einer anderen Person.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Child of</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person is a biological, adoptive, or legal child of another person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_person.</td>
</tr>
<tr>
<td>CIL</td>
<td>GRP-FAM</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Schwiegerkind von</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person ist Ehepartner, Ehepartnerin oder eingetragene Partnerin bzw. Partner des Kindes einer anderen Person.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Child-in-law of</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person is the spouse or registered partner of another person&#x27;s child.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_person.</td>
</tr>
<tr>
<td>CLT</td>
<td>GRP-ORG</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kunde von</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person oder deren Organisation ist Kunde der Zielorganisation.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_company.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Client of</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person or their organization is a client of the target organization.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_company.</td>
</tr>
<tr>
<td>COL</td>
<td>GRP-PRO</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">War Kollege/Kollegin von</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person hat mit einer anderen Person in derselben Organisation oder auf demselben Projekt zusammengearbeitet.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Was colleague of</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person worked alongside another person in the same organization or project.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_person.</td>
</tr>
<tr>
<td>CSN</td>
<td>GRP-FAM</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Cousin/Cousine von</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person ist Cousin oder Cousine einer anderen Person über gemeinsame Grosseltern oder entferntere gemeinsame Vorfahren.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Cousin of</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person is a cousin of another person through a shared grandparent or more distant common ancestor.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_person.</td>
</tr>
<tr>
<td>CST</td>
<td>GRP-ORG</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Berater/Beraterin für</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person erbrachte Beratungsleistungen für eine Organisation ohne Anstellung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_company.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Consulted for</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person provided consulting services to an organization without being an employee.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_company.</td>
</tr>
<tr>
<td>EXP</td>
<td>GRP-INT</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hat Expertise in</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person verfügt über nachgewiesene fachliche Tiefe in einem Themenbereich.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_topic.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Has expertise in</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person has demonstrated professional depth in a topic area.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_topic.</td>
</tr>
<tr>
<td>FRI</td>
<td>GRP-SOC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Freund/Freundin von</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person betrachtet eine andere Person als Freundin oder Freund.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Friend of</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person considers another person a friend.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_person.</td>
</tr>
<tr>
<td>GCH</td>
<td>GRP-FAM</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Enkelkind von</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person ist leibliches, adoptiertes oder rechtliches Enkelkind einer anderen Person.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Grandchild of</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person is a biological, adoptive, or legal grandchild of another person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_person.</td>
</tr>
<tr>
<td>GPR</td>
<td>GRP-FAM</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Grosselternteil von</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person ist leibliches, adoptiertes oder rechtliches Grosselternteil einer anderen Person.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Grandparent of</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person is a biological, adoptive, or legal grandparent of another person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_person.</td>
</tr>
<tr>
<td>GRP-COM</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kommerzielle Beziehungen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Commercial relationships</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>GRP-FAM</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Familienbeziehungen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Family relationships</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>GRP-INT</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Interessen und Expertise</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Interest and expertise</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>GRP-ORG</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Organisationsbeziehungen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Organization relationships</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>GRP-PRO</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Berufliche Beziehungen (Person)</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Professional relationships (person)</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>GRP-SOC</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Soziale Beziehungen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Social relationships</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition"></td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>HKM</td>
<td>GRP-COM</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hat Key-Account-Manager</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Die kommerzielle Beziehung der Person wird von einem Key-Account-Manager betreut.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_person (der Key-Account-Manager).</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Has key account manager</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person&#x27;s commercial relationship is managed by a key account manager.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_person (the KAM).</td>
</tr>
<tr>
<td>INT</td>
<td>GRP-INT</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hat Interesse</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person hat persönliches oder berufliches Interesse an einem Themenkonzept.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_topic.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Has interest</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person has personal or professional interest in a topic concept.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_topic.</td>
</tr>
<tr>
<td>ITR</td>
<td>GRP-SOC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Vorgestellt von</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person wurde einer anderen Person oder einem Kontext durch jemanden vorgestellt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_person (die vorstellende Person).</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Introduced by</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person was introduced to another person or context by someone.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_person (the introducer).</td>
</tr>
<tr>
<td>KAM</td>
<td>GRP-COM</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Ist Key-Account-Manager für</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person ist Key-Account-Manager für eine Kundenorganisation oder einen Ansprechpartner.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_company (Kundenorganisation) oder related_person (Hauptansprechpartner).</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Is key account manager for</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person acts as key account manager for a client organization or contact.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_company (account org) or related_person (primary contact).</td>
</tr>
<tr>
<td>KNW</td>
<td>GRP-SOC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kennt</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person kennt eine andere Person durch soziale oder berufliche Bekanntschaft.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Knows</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person knows another person through social or professional acquaintance.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_person.</td>
</tr>
<tr>
<td>LRN</td>
<td>GRP-INT</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Lernt über</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person entwickelt oder erkundet Interesse an einem Themenbereich.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_topic.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Learning about</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person is developing or exploring interest in a topic area.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_topic.</td>
</tr>
<tr>
<td>MTR</td>
<td>GRP-PRO</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Mentoring durch</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person erhielt berufliche Orientierung oder Mentoring durch eine andere Person.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_person (die Mentorin oder der Mentor).</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Mentored by</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person received career or professional guidance from another person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_person (the mentor).</td>
</tr>
<tr>
<td>NNP</td>
<td>GRP-FAM</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Nichte/Neffe von</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person ist Nichte oder Neffe einer anderen Person, einschliesslich durch Blutsverwandtschaft, Adoption oder Heirat mit einer Tante bzw. einem Onkel.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Niece or nephew of</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person is a niece or nephew of another person, including by blood, adoption, or marriage to an aunt or uncle.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_person.</td>
</tr>
<tr>
<td>PAR</td>
<td>GRP-FAM</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Elternteil von</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person ist leibliches, adoptiertes oder rechtliches Elternteil einer anderen Person.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Parent of</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person is a biological, adoptive, or legal parent of another person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_person.</td>
</tr>
<tr>
<td>PIL</td>
<td>GRP-FAM</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Schwiegerelternteil von</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person ist Elternteil des Ehepartners, der Ehepartnerin oder der eingetragenen Partnerin bzw. des Partners einer anderen Person.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Parent-in-law of</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person is the parent of another person&#x27;s spouse or registered partner.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_person.</td>
</tr>
<tr>
<td>REF</td>
<td>GRP-PRO</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Empfohlen von</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person wurde geschäftlich durch eine andere Person empfohlen oder vermittelt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Referred by</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person was referred or introduced for business by another person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_person.</td>
</tr>
<tr>
<td>RPT</td>
<td>GRP-PRO</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Berichtet an</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person berichtet an oder wird von einer anderen Person geführt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Reports to</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person reports to or is supervised by another person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_person.</td>
</tr>
<tr>
<td>SIB</td>
<td>GRP-FAM</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Geschwister von</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person teilt mindestens ein Elternteil mit einer anderen Person oder ist Stiefgeschwister durch Familienzusammenschluss.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Sibling of</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person shares at least one parent with another person, or is a step-sibling through family union.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_person.</td>
</tr>
<tr>
<td>SPO</td>
<td>GRP-FAM</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Ehepartner/in von</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person ist Ehepartnerin, Ehepartner oder eingetragene Partnerin bzw. Partner einer anderen Person.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Spouse of</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person is the spouse or registered partner of another person.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_person.</td>
</tr>
<tr>
<td>STU</td>
<td>GRP-ORG</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Studierte an</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person hat an einer akademischen oder Ausbildungsinstitution studiert oder eine Ausbildung absolviert.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_company. valid_from und valid_to für Studienzeiträume verwenden.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Studied at</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person completed or pursued formal education at an academic or training institution.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_company. Use valid_from and valid_to for study periods.</td>
</tr>
<tr>
<td>TCH</td>
<td>GRP-ORG</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Lehrt an</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person unterrichtet, doziert oder hat eine Lehrtätigkeit an einer Institution.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_company. teaches_at ohne valid_to kann eine aktuelle Lehrtätigkeit anzeigen.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Teaches at</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person teaches, lectures, or otherwise holds a teaching appointment at an institution.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_company. Open-ended teaches_at without valid_to may indicate a current appointment.</td>
</tr>
<tr>
<td>VND</td>
<td>GRP-ORG</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Lieferant für</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person oder deren Organisation liefert Waren oder Dienstleistungen an die Zielorganisation.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_company.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Vendor of</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person or their organization supplies goods or services to the target organization.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_company.</td>
</tr>
<tr>
<td>WAT</td>
<td>GRP-ORG</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Arbeitet bei</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person ist derzeit bei einer Organisation angestellt oder zugeordnet.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_company. works_at ohne valid_to kann Person.belongs_to_company entsprechen.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Works at</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person is currently employed by or affiliated with an organization.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_company. Open-ended works_at without valid_to may mirror Person.belongs_to_company.</td>
</tr>
<tr>
<td>WRK</td>
<td>GRP-ORG</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">War tätig bei</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Person war früher bei einer Organisation angestellt oder zugeordnet.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Ziel-Slot: related_company. valid_from und valid_to für Anstellungszeiträume verwenden.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Worked at</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Person was formerly employed by or affiliated with an organization.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">Target slot: related_company. Use valid_from and valid_to for employment periods.</td>
</tr>
</tbody>
</table>
</div>
