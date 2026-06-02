# Building space activity classification

Source: [`building_space-activity-classification-en.skos.ttl`](sources/room-activity.ttl)

## Scheme

- **definition (de):** Klassifikationssystem fuer Gebaeude-, Raum- und Aktivitaetsflaechen mit hierarchischer Einteilung von Nutzungs-, Unterstuetzungs- und Aussenbereichen.
- **definition (en):** Building Space and Activity Classification System (BuildingSpaceActivityClassification), version 1.0.3.
- **prefLabel (de):** Klassifikationssystem fuer Gebaeude-, Raum- und Aktivitaetsflaechen
- **prefLabel (en):** Building Space and Activity Classification System
- **title (en):** Building Space and Activity Classification System

## Hierarchy

```mermaid
flowchart TD
  n_M["M: Main Activity Spaces"] --> n_M_CIR["M-CIR: Main Activity Circulation"]
  n_M["M: Main Activity Spaces"] --> n_M_COM["M-COM: Commercial Spaces"]
  n_M["M: Main Activity Spaces"] --> n_M_HEL["M-HEL: Healthcare Spaces"]
  n_M["M: Main Activity Spaces"] --> n_M_LRN["M-LRN: Learning Spaces"]
  n_M["M: Main Activity Spaces"] --> n_M_RES["M-RES: Residential Spaces"]
  n_M["M: Main Activity Spaces"] --> n_M_WRK["M-WRK: Work Spaces"]
  n_M_WRK["M-WRK: Work Spaces"] --> n_M_WRK_KNW["M-WRK-KNW: Knowledge Work Spaces"]
  n_M_WRK["M-WRK: Work Spaces"] --> n_M_WRK_PRD["M-WRK-PRD: Production Work Spaces"]
  n_O["O: Outdoor Spaces"] --> n_O_CIR["O-CIR: Outdoor Circulation"]
  n_O["O: Outdoor Spaces"] --> n_O_GRN["O-GRN: Green Spaces"]
  n_O_CIR["O-CIR: Outdoor Circulation"] --> n_O_CIR_PED["O-CIR-PED: Pedestrian Circulation"]
  n_O_CIR["O-CIR: Outdoor Circulation"] --> n_O_CIR_RD["O-CIR-RD: Roads"]
  n_O_GRN["O-GRN: Green Spaces"] --> n_O_GRN_GDN["O-GRN-GDN: Garden Spaces"]
  n_O_GRN["O-GRN: Green Spaces"] --> n_O_GRN_REC["O-GRN-REC: Recreational Green Spaces"]
  n_O_GRN["O-GRN: Green Spaces"] --> n_O_GRN_SPT["O-GRN-SPT: Sports Spaces"]
  n_S["S: Support Spaces"] --> n_S_CIR["S-CIR: Support Circulation Spaces"]
  n_S["S: Support Spaces"] --> n_S_PRK["S-PRK: Parking Spaces"]
  n_S["S: Support Spaces"] --> n_S_TEC["S-TEC: Technical Spaces"]
  n_S["S: Support Spaces"] --> n_S_VOI["S-VOI: Void Spaces"]
  n_S_CIR["S-CIR: Support Circulation Spaces"] --> n_S_CIR_HOR["S-CIR-HOR: Horizontal Circulation"]
  n_S_CIR["S-CIR: Support Circulation Spaces"] --> n_S_CIR_VRT["S-CIR-VRT: Vertical Circulation"]
  n_S_PRK["S-PRK: Parking Spaces"] --> n_S_PRK_EXT["S-PRK-EXT: Exterior Parking Spaces"]
  n_S_PRK["S-PRK: Parking Spaces"] --> n_S_PRK_INT["S-PRK-INT: Interior Parking Spaces"]
  n_S_PRK["S-PRK: Parking Spaces"] --> n_S_PRK_SVC["S-PRK-SVC: Service Vehicle Spaces"]
  n_S_VOI["S-VOI: Void Spaces"] --> n_S_VOI_MLT["S-VOI-MLT: Multistory Void Spaces"]
  n_S_VOI["S-VOI: Void Spaces"] --> n_S_VOI_PLN["S-VOI-PLN: Plenum Spaces"]
  n_S_VOI["S-VOI: Void Spaces"] --> n_S_VOI_STR["S-VOI-STR: Structural Voids"]
  n_S_VOI["S-VOI: Void Spaces"] --> n_S_VOI_VRT["S-VOI-VRT: Vertical Void Spaces"]
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
<td>M</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hauptnutzungsflaechen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer hauptnutzungsflaechen im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Main Activity Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Primary spaces for building occupants&#x27; activities</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>M-CIR</td>
<td>M</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hauptnutzungserschliessung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer hauptnutzungserschliessung im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Main Activity Circulation</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Circulation spaces integral to main activities</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>M-COM</td>
<td>M</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gewerbeflaechen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer gewerbeflaechen im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Commercial Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Spaces for trading and business activities</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>M-HEL</td>
<td>M</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gesundheitsflaechen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer gesundheitsflaechen im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Healthcare Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Spaces for medical and wellness activities</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>M-LRN</td>
<td>M</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Lernflaechen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer lernflaechen im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Learning Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Spaces for educational and knowledge acquisition</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>M-RES</td>
<td>M</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wohnflaechen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer wohnflaechen im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Residential Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Spaces for daily living and personal life activities</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>M-WRK</td>
<td>M</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Arbeitsflaechen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer arbeitsflaechen im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Work Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Spaces for professional and productive activities</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>M-WRK-KNW</td>
<td>M-WRK</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wissensarbeitsflaechen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer wissensarbeitsflaechen im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Knowledge Work Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Spaces for intellectual and information-based work</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>M-WRK-PRD</td>
<td>M-WRK</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Produktionsarbeitsflaechen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer produktionsarbeitsflaechen im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Production Work Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Spaces for physical production and manufacturing activities</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>O</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aussenflaechen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer aussenflaechen im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Outdoor Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">External spaces associated with the building</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>O-CIR</td>
<td>O</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aussenerschliessung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer aussenerschliessung im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Outdoor Circulation</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">External movement spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>O-CIR-PED</td>
<td>O-CIR</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Fussgaengererschliessung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer fussgaengererschliessung im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Pedestrian Circulation</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Pedestrian movement spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>O-CIR-RD</td>
<td>O-CIR</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Fahrwege</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer fahrwege im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Roads</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Vehicular circulation routes</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>O-GRN</td>
<td>O</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gruenflaechen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer gruenflaechen im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Green Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Landscaped and natural area spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>O-GRN-GDN</td>
<td>O-GRN</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gartenflaechen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer gartenflaechen im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Garden Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Cultivated green spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>O-GRN-REC</td>
<td>O-GRN</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Erholungsgruenflaechen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer erholungsgruenflaechen im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Recreational Green Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Spaces for leisure activities</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>O-GRN-SPT</td>
<td>O-GRN</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Sportflaechen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer sportflaechen im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Sports Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Formal athletic spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>S</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Unterstuetzungsflaechen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer unterstuetzungsflaechen im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Support Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Auxiliary spaces supporting building operations</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>S-CIR</td>
<td>S</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Nebenerschliessungsflaechen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer nebenerschliessungsflaechen im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Support Circulation Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Auxiliary circulation spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>S-CIR-HOR</td>
<td>S-CIR</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Horizontale Erschliessung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer horizontale erschliessung im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Horizontal Circulation</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Spaces for horizontal movement</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>S-CIR-VRT</td>
<td>S-CIR</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Vertikale Erschliessung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer vertikale erschliessung im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Vertical Circulation</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Spaces for vertical movement</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>S-PRK</td>
<td>S</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Parkierungsflaechen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer parkierungsflaechen im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Parking Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Spaces for vehicle storage and management</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>S-PRK-EXT</td>
<td>S-PRK</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aussenparkierungsflaechen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer aussenparkierungsflaechen im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Exterior Parking Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Open-air vehicle parking areas</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>S-PRK-INT</td>
<td>S-PRK</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Innenparkierungsflaechen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer innenparkierungsflaechen im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Interior Parking Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Enclosed vehicle parking areas</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>S-PRK-SVC</td>
<td>S-PRK</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Servicefahrzeugflaechen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer servicefahrzeugflaechen im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Service Vehicle Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Specialized parking for service vehicles</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>S-TEC</td>
<td>S</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Technikflaechen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer technikflaechen im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Technical Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Spaces for building systems and equipment</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>S-VOI</td>
<td>S</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hohlraeume</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer hohlraeume im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Void Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Spaces not suitable for occupancy or activity</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>S-VOI-MLT</td>
<td>S-VOI</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Mehrgeschossige Hohlraeume</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer mehrgeschossige hohlraeume im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Multistory Void Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Vertical open spaces spanning multiple floors</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>S-VOI-PLN</td>
<td>S-VOI</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Installationszwischenraeume</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer installationszwischenraeume im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Plenum Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Horizontal service voids</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>S-VOI-STR</td>
<td>S-VOI</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Konstruktive Hohlraeume</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer konstruktive hohlraeume im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Structural Voids</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Spaces within structural elements</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>S-VOI-VRT</td>
<td>S-VOI</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Vertikale Hohlraeume</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kategorie fuer vertikale hohlraeume im Klassifikationssystem.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Vertical Void Spaces</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Vertical shafts and wells</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
</tbody>
</table>
</div>
