# Building space name classification

Source: [`building-space-name-classification.skos.ttl`](sources/room-name.ttl)

## Scheme

- **definition (de):** Normalisierte abstrakte Raumbezeichnungen fuer allgemeinen Gebaeudegebrauch auf IfcSpace.
- **definition (en):** Normalized abstract room name types for general building use on IfcSpace.
- **prefLabel (de):** Gebaeude-Raumbezeichnungsklassifikation
- **prefLabel (en):** Building Space Name Classification
- **title (en):** Building Space Name Classification

## Hierarchy

```mermaid
classDiagram
direction TB
class n_RN_01["RN-01: Residential"]
class n_RN_01_10["RN-01-10: Living and sleeping"]
class n_RN_01_10_01["RN-01-10-01: Bedroom"]
class n_RN_01_10_02["RN-01-10-02: Living Room"]
class n_RN_01_10_03["RN-01-10-03: Dining Room"]
class n_RN_01_10_04["RN-01-10-04: Home Study"]
class n_RN_01_10_05["RN-01-10-05: Guest Room"]
class n_RN_01_20["RN-01-20: Residential services"]
class n_RN_01_20_01["RN-01-20-01: Kitchen"]
class n_RN_01_20_02["RN-01-20-02: Bathroom"]
class n_RN_01_20_03["RN-01-20-03: Laundry Room"]
class n_RN_01_20_04["RN-01-20-04: Utility Room"]
class n_RN_01_30["RN-01-30: Dwelling unit level"]
class n_RN_01_30_01["RN-01-30-01: Residential Entry"]
class n_RN_01_30_02["RN-01-30-02: Residential Closet"]
class n_RN_01_30_03["RN-01-30-03: Apartment Unit"]
class n_RN_02["RN-02: Work"]
class n_RN_02_10["RN-02-10: Individual work"]
class n_RN_02_10_01["RN-02-10-01: Office"]
class n_RN_02_10_02["RN-02-10-02: Open-Plan Office"]
class n_RN_02_10_03["RN-02-10-03: Focus Room"]
class n_RN_02_10_04["RN-02-10-04: Phone Booth"]
class n_RN_02_10_05["RN-02-10-05: Coworking Space"]
class n_RN_02_20["RN-02-20: Collaboration"]
class n_RN_02_20_01["RN-02-20-01: Meeting Room"]
class n_RN_02_20_02["RN-02-20-02: Conference Room"]
class n_RN_02_20_03["RN-02-20-03: Break Room"]
class n_RN_02_30["RN-02-30: Reception and administration"]
class n_RN_02_30_01["RN-02-30-01: Reception"]
class n_RN_02_30_02["RN-02-30-02: Administrative Office"]
class n_RN_02_30_03["RN-02-30-03: Manager Office"]
class n_RN_02_30_04["RN-02-30-04: Open Administrative Area"]
class n_RN_03["RN-03: Circulation"]
class n_RN_03_10["RN-03-10: Horizontal circulation"]
class n_RN_03_10_01["RN-03-10-01: Corridor"]
class n_RN_03_10_02["RN-03-10-02: Lobby"]
class n_RN_03_10_03["RN-03-10-03: Entrance Hall"]
class n_RN_03_10_04["RN-03-10-04: Vestibule"]
class n_RN_03_20["RN-03-20: Vertical circulation"]
class n_RN_03_20_01["RN-03-20-01: Stairwell"]
class n_RN_03_20_02["RN-03-20-02: Elevator Lobby"]
class n_RN_03_20_03["RN-03-20-03: Ramp"]
class n_RN_03_20_04["RN-03-20-04: Landing"]
class n_RN_03_30["RN-03-30: Activity-integral circulation"]
class n_RN_03_30_01["RN-03-30-01: Gallery"]
class n_RN_04["RN-04: Hygiene"]
class n_RN_04_10["RN-04-10: Toilets"]
class n_RN_04_10_01["RN-04-10-01: Male Toilet"]
class n_RN_04_10_02["RN-04-10-02: Female Toilet"]
class n_RN_04_10_03["RN-04-10-03: Accessible Toilet"]
class n_RN_04_10_04["RN-04-10-04: Unisex Toilet"]
class n_RN_04_20["RN-04-20: Wash and change"]
class n_RN_04_20_01["RN-04-20-01: Shower Room"]
class n_RN_04_20_02["RN-04-20-02: Changing Room"]
class n_RN_04_20_03["RN-04-20-03: Locker Room"]
class n_RN_04_30["RN-04-30: Coat check"]
class n_RN_04_30_01["RN-04-30-01: Cloakroom"]
class n_RN_05["RN-05: Healthcare"]
class n_RN_05_10["RN-05-10: Inpatient care"]
class n_RN_05_10_01["RN-05-10-01: Patient Room"]
class n_RN_05_10_02["RN-05-10-02: Recovery Room"]
class n_RN_05_20["RN-05-20: Clinical treatment"]
class n_RN_05_20_01["RN-05-20-01: Treatment Room"]
class n_RN_05_20_02["RN-05-20-02: Operating Room"]
class n_RN_05_20_03["RN-05-20-03: Procedure Room"]
class n_RN_05_20_04["RN-05-20-04: Examination Room"]
class n_RN_05_30["RN-05-30: Diagnostics and support"]
class n_RN_05_30_01["RN-05-30-01: Imaging Room"]
class n_RN_05_30_02["RN-05-30-02: Medical Laboratory"]
class n_RN_05_30_03["RN-05-30-03: Waiting Room"]
class n_RN_05_30_04["RN-05-30-04: Nurses Station"]
class n_RN_06["RN-06: Education"]
class n_RN_06_10["RN-06-10: Instruction"]
class n_RN_06_10_01["RN-06-10-01: Classroom"]
class n_RN_06_10_02["RN-06-10-02: Lecture Hall"]
class n_RN_06_10_03["RN-06-10-03: Seminar Room"]
class n_RN_06_10_04["RN-06-10-04: Computer Lab"]
class n_RN_06_20["RN-06-20: Self-directed learning"]
class n_RN_06_20_01["RN-06-20-01: Library Room"]
class n_RN_06_20_02["RN-06-20-02: Study Room"]
class n_RN_06_20_03["RN-06-20-03: Training Workshop"]
class n_RN_06_30["RN-06-30: Assembly and special subjects"]
class n_RN_06_30_01["RN-06-30-01: Auditorium"]
class n_RN_06_30_02["RN-06-30-02: Art Studio"]
class n_RN_06_30_03["RN-06-30-03: Science Lab"]
class n_RN_07["RN-07: Commercial"]
class n_RN_07_10["RN-07-10: Dining and beverage"]
class n_RN_07_10_01["RN-07-10-01: Cafeteria"]
class n_RN_07_10_02["RN-07-10-02: Restaurant"]
class n_RN_07_10_03["RN-07-10-03: Bar"]
class n_RN_07_10_04["RN-07-10-04: Food Court"]
class n_RN_07_20["RN-07-20: Retail and exhibition"]
class n_RN_07_20_01["RN-07-20-01: Retail Space"]
class n_RN_07_20_02["RN-07-20-02: Sales Floor"]
class n_RN_07_20_03["RN-07-20-03: Kiosk"]
class n_RN_07_20_04["RN-07-20-04: Customer Service Area"]
class n_RN_07_20_05["RN-07-20-05: Exhibition Space"]
class n_RN_07_30["RN-07-30: Hospitality"]
class n_RN_07_30_01["RN-07-30-01: Hotel Room"]
class n_RN_08["RN-08: Industrial"]
class n_RN_08_10["RN-08-10: Production"]
class n_RN_08_10_01["RN-08-10-01: Workshop"]
class n_RN_08_10_02["RN-08-10-02: Production Hall"]
class n_RN_08_10_03["RN-08-10-03: Assembly Area"]
class n_RN_08_10_04["RN-08-10-04: Packaging Area"]
class n_RN_08_10_05["RN-08-10-05: Clean Room"]
class n_RN_08_20["RN-08-20: Logistics"]
class n_RN_08_20_01["RN-08-20-01: Warehouse"]
class n_RN_08_20_02["RN-08-20-02: Loading Dock"]
class n_RN_08_20_03["RN-08-20-03: Quality Control Room"]
class n_RN_08_20_04["RN-08-20-04: Maintenance Bay"]
class n_RN_08_30["RN-08-30: Special industrial"]
class n_RN_08_30_01["RN-08-30-01: Covered Yard"]
class n_RN_09["RN-09: Technical"]
class n_RN_09_10["RN-09-10: HVAC and plumbing plant"]
class n_RN_09_10_01["RN-09-10-01: HVAC Plant Room"]
class n_RN_09_10_02["RN-09-10-02: Pump Room"]
class n_RN_09_10_03["RN-09-10-03: Boiler Room"]
class n_RN_09_10_04["RN-09-10-04: Chiller Room"]
class n_RN_09_10_05["RN-09-10-05: Sprinkler Room"]
class n_RN_09_20["RN-09-20: Electrical and IT plant"]
class n_RN_09_20_01["RN-09-20-01: Electrical Room"]
class n_RN_09_20_02["RN-09-20-02: Server Room"]
class n_RN_09_20_03["RN-09-20-03: Generator Room"]
class n_RN_09_20_04["RN-09-20-04: Transformer Room"]
class n_RN_09_20_05["RN-09-20-05: Communications Room"]
class n_RN_09_30["RN-09-30: Metering and waste"]
class n_RN_09_30_01["RN-09-30-01: Meter Room"]
class n_RN_09_30_02["RN-09-30-02: Waste Room"]
class n_RN_10["RN-10: Storage"]
class n_RN_10_10["RN-10-10: General storage types"]
class n_RN_10_10_01["RN-10-10-01: General Storage"]
class n_RN_10_10_02["RN-10-10-02: Supply Room"]
class n_RN_10_10_03["RN-10-10-03: Equipment Storage"]
class n_RN_10_10_04["RN-10-10-04: Unloading Storage"]
class n_RN_10_10_05["RN-10-10-05: Janitor Closet"]
class n_RN_10_20["RN-10-20: Specialized storage"]
class n_RN_10_20_01["RN-10-20-01: Archive Room"]
class n_RN_10_20_02["RN-10-20-02: Mail Room"]
class n_RN_10_20_03["RN-10-20-03: Cold Storage"]
class n_RN_11["RN-11: Outdoor"]
class n_RN_11_10["RN-11-10: Exterior platforms"]
class n_RN_11_10_01["RN-11-10-01: Balcony"]
class n_RN_11_10_02["RN-11-10-02: Terrace"]
class n_RN_11_10_03["RN-11-10-03: Patio"]
class n_RN_11_20["RN-11-20: Landscape and recreation"]
class n_RN_11_20_01["RN-11-20-01: Garden Area"]
class n_RN_11_20_02["RN-11-20-02: Playground"]
class n_RN_11_20_03["RN-11-20-03: Pool Area"]
class n_RN_11_30["RN-11-30: Covered exterior routes"]
class n_RN_11_30_01["RN-11-30-01: Covered Walkway"]
class n_RN_11_30_02["RN-11-30-02: Portico"]
class n_RN_12["RN-12: Void"]
class n_RN_12_10["RN-12-10: Vertical voids"]
class n_RN_12_10_01["RN-12-10-01: Shaft"]
class n_RN_12_10_02["RN-12-10-02: Riser"]
class n_RN_12_20["RN-12-20: Plenums and air volumes"]
class n_RN_12_20_01["RN-12-20-01: Plenum"]
class n_RN_12_20_02["RN-12-20-02: Mechanical Void"]
class n_RN_12_20_03["RN-12-20-03: Air Space"]
class n_RN_12_30["RN-12-30: Structural and special voids"]
class n_RN_12_30_01["RN-12-30-01: Atrium Void"]
class n_RN_12_30_02["RN-12-30-02: Structural Void"]
class n_RN_12_30_03["RN-12-30-03: Interior Parking Stall"]
n_RN_01 <|-- n_RN_01_10
n_RN_01 <|-- n_RN_01_20
n_RN_01 <|-- n_RN_01_30
n_RN_01_10 <|-- n_RN_01_10_01
n_RN_01_10 <|-- n_RN_01_10_02
n_RN_01_10 <|-- n_RN_01_10_03
n_RN_01_10 <|-- n_RN_01_10_04
n_RN_01_10 <|-- n_RN_01_10_05
n_RN_01_20 <|-- n_RN_01_20_01
n_RN_01_20 <|-- n_RN_01_20_02
n_RN_01_20 <|-- n_RN_01_20_03
n_RN_01_20 <|-- n_RN_01_20_04
n_RN_01_30 <|-- n_RN_01_30_01
n_RN_01_30 <|-- n_RN_01_30_02
n_RN_01_30 <|-- n_RN_01_30_03
n_RN_02 <|-- n_RN_02_10
n_RN_02 <|-- n_RN_02_20
n_RN_02 <|-- n_RN_02_30
n_RN_02_10 <|-- n_RN_02_10_01
n_RN_02_10 <|-- n_RN_02_10_02
n_RN_02_10 <|-- n_RN_02_10_03
n_RN_02_10 <|-- n_RN_02_10_04
n_RN_02_10 <|-- n_RN_02_10_05
n_RN_02_20 <|-- n_RN_02_20_01
n_RN_02_20 <|-- n_RN_02_20_02
n_RN_02_20 <|-- n_RN_02_20_03
n_RN_02_30 <|-- n_RN_02_30_01
n_RN_02_30 <|-- n_RN_02_30_02
n_RN_02_30 <|-- n_RN_02_30_03
n_RN_02_30 <|-- n_RN_02_30_04
n_RN_03 <|-- n_RN_03_10
n_RN_03 <|-- n_RN_03_20
n_RN_03 <|-- n_RN_03_30
n_RN_03_10 <|-- n_RN_03_10_01
n_RN_03_10 <|-- n_RN_03_10_02
n_RN_03_10 <|-- n_RN_03_10_03
n_RN_03_10 <|-- n_RN_03_10_04
n_RN_03_20 <|-- n_RN_03_20_01
n_RN_03_20 <|-- n_RN_03_20_02
n_RN_03_20 <|-- n_RN_03_20_03
n_RN_03_20 <|-- n_RN_03_20_04
n_RN_03_30 <|-- n_RN_03_30_01
n_RN_04 <|-- n_RN_04_10
n_RN_04 <|-- n_RN_04_20
n_RN_04 <|-- n_RN_04_30
n_RN_04_10 <|-- n_RN_04_10_01
n_RN_04_10 <|-- n_RN_04_10_02
n_RN_04_10 <|-- n_RN_04_10_03
n_RN_04_10 <|-- n_RN_04_10_04
n_RN_04_20 <|-- n_RN_04_20_01
n_RN_04_20 <|-- n_RN_04_20_02
n_RN_04_20 <|-- n_RN_04_20_03
n_RN_04_30 <|-- n_RN_04_30_01
n_RN_05 <|-- n_RN_05_10
n_RN_05 <|-- n_RN_05_20
n_RN_05 <|-- n_RN_05_30
n_RN_05_10 <|-- n_RN_05_10_01
n_RN_05_10 <|-- n_RN_05_10_02
n_RN_05_20 <|-- n_RN_05_20_01
n_RN_05_20 <|-- n_RN_05_20_02
n_RN_05_20 <|-- n_RN_05_20_03
n_RN_05_20 <|-- n_RN_05_20_04
n_RN_05_30 <|-- n_RN_05_30_01
n_RN_05_30 <|-- n_RN_05_30_02
n_RN_05_30 <|-- n_RN_05_30_03
n_RN_05_30 <|-- n_RN_05_30_04
n_RN_06 <|-- n_RN_06_10
n_RN_06 <|-- n_RN_06_20
n_RN_06 <|-- n_RN_06_30
n_RN_06_10 <|-- n_RN_06_10_01
n_RN_06_10 <|-- n_RN_06_10_02
n_RN_06_10 <|-- n_RN_06_10_03
n_RN_06_10 <|-- n_RN_06_10_04
n_RN_06_20 <|-- n_RN_06_20_01
n_RN_06_20 <|-- n_RN_06_20_02
n_RN_06_20 <|-- n_RN_06_20_03
n_RN_06_30 <|-- n_RN_06_30_01
n_RN_06_30 <|-- n_RN_06_30_02
n_RN_06_30 <|-- n_RN_06_30_03
n_RN_07 <|-- n_RN_07_10
n_RN_07 <|-- n_RN_07_20
n_RN_07 <|-- n_RN_07_30
n_RN_07_10 <|-- n_RN_07_10_01
n_RN_07_10 <|-- n_RN_07_10_02
n_RN_07_10 <|-- n_RN_07_10_03
n_RN_07_10 <|-- n_RN_07_10_04
n_RN_07_20 <|-- n_RN_07_20_01
n_RN_07_20 <|-- n_RN_07_20_02
n_RN_07_20 <|-- n_RN_07_20_03
n_RN_07_20 <|-- n_RN_07_20_04
n_RN_07_20 <|-- n_RN_07_20_05
n_RN_07_30 <|-- n_RN_07_30_01
n_RN_08 <|-- n_RN_08_10
n_RN_08 <|-- n_RN_08_20
n_RN_08 <|-- n_RN_08_30
n_RN_08_10 <|-- n_RN_08_10_01
n_RN_08_10 <|-- n_RN_08_10_02
n_RN_08_10 <|-- n_RN_08_10_03
n_RN_08_10 <|-- n_RN_08_10_04
n_RN_08_10 <|-- n_RN_08_10_05
n_RN_08_20 <|-- n_RN_08_20_01
n_RN_08_20 <|-- n_RN_08_20_02
n_RN_08_20 <|-- n_RN_08_20_03
n_RN_08_20 <|-- n_RN_08_20_04
n_RN_08_30 <|-- n_RN_08_30_01
n_RN_09 <|-- n_RN_09_10
n_RN_09 <|-- n_RN_09_20
n_RN_09 <|-- n_RN_09_30
n_RN_09_10 <|-- n_RN_09_10_01
n_RN_09_10 <|-- n_RN_09_10_02
n_RN_09_10 <|-- n_RN_09_10_03
n_RN_09_10 <|-- n_RN_09_10_04
n_RN_09_10 <|-- n_RN_09_10_05
n_RN_09_20 <|-- n_RN_09_20_01
n_RN_09_20 <|-- n_RN_09_20_02
n_RN_09_20 <|-- n_RN_09_20_03
n_RN_09_20 <|-- n_RN_09_20_04
n_RN_09_20 <|-- n_RN_09_20_05
n_RN_09_30 <|-- n_RN_09_30_01
n_RN_09_30 <|-- n_RN_09_30_02
n_RN_10 <|-- n_RN_10_10
n_RN_10 <|-- n_RN_10_20
n_RN_10_10 <|-- n_RN_10_10_01
n_RN_10_10 <|-- n_RN_10_10_02
n_RN_10_10 <|-- n_RN_10_10_03
n_RN_10_10 <|-- n_RN_10_10_04
n_RN_10_10 <|-- n_RN_10_10_05
n_RN_10_20 <|-- n_RN_10_20_01
n_RN_10_20 <|-- n_RN_10_20_02
n_RN_10_20 <|-- n_RN_10_20_03
n_RN_11 <|-- n_RN_11_10
n_RN_11 <|-- n_RN_11_20
n_RN_11 <|-- n_RN_11_30
n_RN_11_10 <|-- n_RN_11_10_01
n_RN_11_10 <|-- n_RN_11_10_02
n_RN_11_10 <|-- n_RN_11_10_03
n_RN_11_20 <|-- n_RN_11_20_01
n_RN_11_20 <|-- n_RN_11_20_02
n_RN_11_20 <|-- n_RN_11_20_03
n_RN_11_30 <|-- n_RN_11_30_01
n_RN_11_30 <|-- n_RN_11_30_02
n_RN_12 <|-- n_RN_12_10
n_RN_12 <|-- n_RN_12_20
n_RN_12 <|-- n_RN_12_30
n_RN_12_10 <|-- n_RN_12_10_01
n_RN_12_10 <|-- n_RN_12_10_02
n_RN_12_20 <|-- n_RN_12_20_01
n_RN_12_20 <|-- n_RN_12_20_02
n_RN_12_20 <|-- n_RN_12_20_03
n_RN_12_30 <|-- n_RN_12_30_01
n_RN_12_30 <|-- n_RN_12_30_02
n_RN_12_30 <|-- n_RN_12_30_03
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
<td>RN-01</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wohnen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer Wohnnutzungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Residential</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for residential living spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-10</td>
<td>RN-01</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wohnen und Schlafen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raeume fuer Wohnen, Schlafen und Essen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Living and sleeping</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Rooms for daily living, sleeping, and dining.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-10-01</td>
<td>RN-01-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Schlafzimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum primaer fuer Schlafen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Bedroom</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room primarily used for sleeping.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-10-02</td>
<td>RN-01-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wohnzimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Wohnen und Entspannung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Living Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for daily living and relaxation.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-10-03</td>
<td>RN-01-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Esszimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Mahlzeiten.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Dining Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for eating meals.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-10-04</td>
<td>RN-01-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Arbeitszimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Wohnlicher Raum fuer Arbeit oder Studium.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Home Study</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Residential room for study or home office work.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-10-05</td>
<td>RN-01-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gaestezimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer ueber Nacht bleibende Gaeste.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Guest Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for overnight guests.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-20</td>
<td>RN-01</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wohnliche Dienste</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kueche, Bad, Waesche und Hauswirtschaft in Wohneinheiten.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Residential services</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Kitchen, bathroom, laundry, and utility spaces within dwellings.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-20-01</td>
<td>RN-01-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kueche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Speisezubereitung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Kitchen</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for food preparation.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-20-02</td>
<td>RN-01-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Badezimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum mit Bad, Dusche oder Koerperpflege.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Bathroom</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room with bath, shower, or personal hygiene fixtures.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-20-03</td>
<td>RN-01-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Waschkueche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Waeschepflege.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Laundry Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for washing and drying clothes.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-20-04</td>
<td>RN-01-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hauswirtschaftsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer haushaltstechnische Einrichtungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Utility Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for domestic utilities and equipment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-30</td>
<td>RN-01</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wohneinheitsebene</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Eingang, Abstell- und Gesamtwohnflaechen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Dwelling unit level</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Entry, storage, and whole-unit spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-30-01</td>
<td>RN-01-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wohnungseingang</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Eingangsbereich innerhalb einer Wohneinheit.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Residential Entry</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Entry space within a dwelling unit.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-30-02</td>
<td>RN-01-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Abstellraum Wohnen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kleiner Abstellraum innerhalb einer Wohneinheit.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Residential Closet</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Small storage within a dwelling unit.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-01-30-03</td>
<td>RN-01-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wohneinheit</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Generische Wohneinheit ohne weitere Unterteilung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Apartment Unit</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Generic residential unit space when not subdivided further.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Arbeit</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer Buero- und Wissensarbeit.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Work</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for office and knowledge work.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-10</td>
<td>RN-02</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Einzelarbeit</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Geschlossene und Fokus-Arbeitsplaetze.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Individual work</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Enclosed and focus workspaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-10-01</td>
<td>RN-02-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Buero</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Buero fuer Einzel- oder Gruppenarbeit.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Office</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Enclosed office for individual or shared desk work.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-10-02</td>
<td>RN-02-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Grossraumbuero</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Offene Burolandschaft ohne geschlossene Zellbueros.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Open-Plan Office</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Open office landscape without full-height partitions.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-10-03</td>
<td>RN-02-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Fokusraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kleiner Raum fuer konzentrierte Einzelarbeit.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Focus Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Small room for concentrated individual work.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-10-04</td>
<td>RN-02-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Telefonbox</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kleine Kabine fuer Telefongespraeche.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Phone Booth</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Small enclosure for private calls.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-10-05</td>
<td>RN-02-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Coworking-Flaeche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Gemeinschaftlich genutzter flexibler Arbeitsraum.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Coworking Space</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Shared flexible workspace.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-20</td>
<td>RN-02</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Zusammenarbeit</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Besprechungs- und informelle Teamraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Collaboration</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Meeting and informal collaboration spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-20-01</td>
<td>RN-02-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Besprechungsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer kleine Besprechungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Meeting Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for small group meetings.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-20-02</td>
<td>RN-02-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Konferenzraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer formelle Sitzungen und Praesentationen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Conference Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for formal meetings and presentations.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-20-03</td>
<td>RN-02-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Pausenraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Informeller Raum fuer Pausen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Break Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Informal staff rest and refreshment space.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-30</td>
<td>RN-02</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Empfang und Verwaltung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Empfang, Fuehrung und offene Verwaltungsflaechen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Reception and administration</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Reception, management, and open administrative areas.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-30-01</td>
<td>RN-02-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Empfang</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Empfang und Wartebereich fuer Besucher.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Reception</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Visitor reception and waiting area.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-30-02</td>
<td>RN-02-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Verwaltungsbuero</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Buero fuer Verwaltungspersonal.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Administrative Office</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Office for administrative staff.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-30-03</td>
<td>RN-02-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Fuehrungsbuero</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Buero fuer Fuehrungsfunktionen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Manager Office</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Office for management roles.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-02-30-04</td>
<td>RN-02-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Offene Verwaltungsflaeche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Offene Verwaltungsarbeitsflaeche.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Open Administrative Area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Open administrative work area.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-03</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Erschliessung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer Erschliessungsraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Circulation</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for circulation and access spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-03-10</td>
<td>RN-03</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Horizontale Erschliessung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Flure, Hallen und horizontale Zugaenge.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Horizontal circulation</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Corridors, lobbies, and horizontal access routes.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-03-10-01</td>
<td>RN-03-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Flur</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Horizontaler Verbindungsflur, einschliesslich schmaler Durchgaenge zwischen Reihen oder Funktionen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Corridor</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Horizontal circulation passage, including narrow aisles between rows or functions.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-03-10-02</td>
<td>RN-03-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Eingangshalle</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Eingangshalle oder Empfoyer.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Lobby</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Main entrance lobby or reception hall.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-03-10-03</td>
<td>RN-03-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Entree</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Uebergangsraum am Gebaeudeeingang.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Entrance Hall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Building entrance transition space.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-03-10-04</td>
<td>RN-03-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Vorraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Uebergangsraum zwischen Aussen und Innen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Vestibule</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Transition space between exterior and interior.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-03-20</td>
<td>RN-03</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Vertikale Erschliessung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Treppen, Rampen, Aufzuege und Podeste.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Vertical circulation</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Stairs, ramps, lifts, and landings.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-03-20-01</td>
<td>RN-03-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Treppenhaus</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Treppenhaus mit Podesten.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Stairwell</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Enclosed stair and landing volume.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-03-20-02</td>
<td>RN-03-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aufzugszone</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Wartebereich an Aufzugshaltestellen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Elevator Lobby</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Waiting area at elevator stops.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-03-20-03</td>
<td>RN-03-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Rampe</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Geneigte barrierefreie Erschliessung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Ramp</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Inclined accessible circulation route.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-03-20-04</td>
<td>RN-03-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Podest</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Treppen- oder Rampenpodest.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Landing</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Stair or ramp landing platform.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-03-30</td>
<td>RN-03</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hauptnutzungserschliessung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Erschliessung als Teil der Hauptnutzung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Activity-integral circulation</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Circulation spaces integral to the main building activity.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-03-30-01</td>
<td>RN-03-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Galerie</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Erschliessungsgalerie als Teil der Hauptnutzung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Gallery</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Circulation gallery integral to main activity.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-04</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hygiene</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer Hygiene- und Sanitaerraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Hygiene</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for sanitary and changing spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-04-10</td>
<td>RN-04</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Toiletten</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">WC-Raeume nach Barrierefreiheit und Geschlechterausstattung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Toilets</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Toilet rooms by accessibility and gender provision.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-04-10-01</td>
<td>RN-04-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Herren-WC</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">WC fuer Maenner.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Male Toilet</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Toilet room for male use.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-04-10-02</td>
<td>RN-04-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Damen-WC</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">WC fuer Frauen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Female Toilet</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Toilet room for female use.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-04-10-03</td>
<td>RN-04-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Barrierefreies WC</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Rollstuhlgaengiges WC.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Accessible Toilet</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Wheelchair-accessible toilet room.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-04-10-04</td>
<td>RN-04-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Allgemeines WC</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">WC fuer gemischte oder all-gender Nutzung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Unisex Toilet</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Toilet room for mixed or all-gender use.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-04-20</td>
<td>RN-04</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Waschen und Umziehen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Duschen, Umziehen und Schliessfaecher.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Wash and change</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Shower, changing, and locker spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-04-20-01</td>
<td>RN-04-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Duschraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum mit Duscheinrichtungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Shower Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room with shower facilities.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-04-20-02</td>
<td>RN-04-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Umkleideraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum zum Umziehen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Changing Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for changing clothes.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-04-20-03</td>
<td>RN-04-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Schliessfachraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum mit persoenlichen Schliessfaechern.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Locker Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room with personal lockers.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-04-30</td>
<td>RN-04</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Mantelablage</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Garderobe und Mantelablage am Eingang.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Coat check</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Coat check and entry cloakroom spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-04-30-01</td>
<td>RN-04-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Garderobe</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Garderobe mit oder ohne Bedienung am Eingang.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Cloakroom</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Staffed or unstaffed coat check at entry.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gesundheit</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer medizinische und pflegerische Raeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Healthcare</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for medical and care spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-10</td>
<td>RN-05</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Stationaere Pflege</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raeume fuer stationaeren Aufenthalt und Erholung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Inpatient care</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Rooms for inpatient stay and recovery.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-10-01</td>
<td>RN-05-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Patientenzimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer stationaere Pflege.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Patient Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for inpatient care and recovery.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-10-02</td>
<td>RN-05-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aufwachraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer postoperative Ueberwachung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Recovery Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for post-procedure recovery.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-20</td>
<td>RN-05</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Klinische Behandlung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Behandlungs-, Operations- und Eingriffsraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Clinical treatment</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Treatment, surgery, and procedure spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-20-01</td>
<td>RN-05-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Behandlungsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer ambulante Behandlung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Treatment Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for outpatient treatment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-20-02</td>
<td>RN-05-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Operationssaal</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer operative Eingriffe.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Operating Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for surgical procedures.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-20-03</td>
<td>RN-05-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Eingriffsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer kleinere medizinische Eingriffe.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Procedure Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for minor medical procedures.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-20-04</td>
<td>RN-05-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Untersuchungsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer aerztliche Untersuchung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Examination Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for clinical examination.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-30</td>
<td>RN-05</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Diagnostik und Support</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bildgebung, Labor, Warten und Pflegestation.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Diagnostics and support</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Imaging, laboratory, waiting, and nursing support spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-30-01</td>
<td>RN-05-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Bildgebungsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer diagnostische Bildgebung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Imaging Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for diagnostic imaging.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-30-02</td>
<td>RN-05-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Medizinisches Labor</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Labor fuer medizinische Analysen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Medical Laboratory</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Laboratory for medical analysis.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-30-03</td>
<td>RN-05-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wartezimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer wartende Patienten und Besucher.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Waiting Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for patients and visitors to wait.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-05-30-04</td>
<td>RN-05-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Pflegestationszimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Zentrale Pflegestation.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Nurses Station</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Central nursing and monitoring workspace.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Bildung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer Bildungs- und Lernraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Education</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for teaching and learning spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-10</td>
<td>RN-06</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Unterricht</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Klassenzimmer, Hoersaele und Seminarraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Instruction</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Classrooms, lecture halls, and seminar spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-10-01</td>
<td>RN-06-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Klassenzimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Schul- oder Gruppenunterricht.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Classroom</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for school or group instruction.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-10-02</td>
<td>RN-06-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hoersaal</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum mit festem Gestuehl fuer Vorlesungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Lecture Hall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room with fixed seating for lectures.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-10-03</td>
<td>RN-06-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Seminarraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Seminare und Workshops.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Seminar Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for seminars and workshops.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-10-04</td>
<td>RN-06-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Computerraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum mit Computerarbeitsplaetzen fuer Unterricht.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Computer Lab</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room with computer workstations for teaching.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-20</td>
<td>RN-06</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Selbstgesteuertes Lernen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bibliothek, Lernraeume und Ausbildungswerkstaetten.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Self-directed learning</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Library, study, and training workshop spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-20-01</td>
<td>RN-06-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Bibliotheksraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Lesen und Bibliotheksnutzung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Library Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for reading and library use.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-20-02</td>
<td>RN-06-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Lernraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer selbststaendiges Lernen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Study Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for self-directed study.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-20-03</td>
<td>RN-06-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Ausbildungswerkstatt</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer praktische Ausbildung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Training Workshop</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for practical skills training.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-30</td>
<td>RN-06</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Versammlung und Fachraeume</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aula, Ateliers und naturwissenschaftliche Laboratorien.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Assembly and special subjects</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Auditoria, art studios, and science laboratories.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-30-01</td>
<td>RN-06-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aula</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Grosse Versammlungshalle fuer Veranstaltungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Auditorium</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Large assembly hall for events.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-30-02</td>
<td>RN-06-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kunstatelier</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer bildnerischen Unterricht.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Art Studio</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for visual arts instruction and practice.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-06-30-03</td>
<td>RN-06-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Naturwissenschaftslabor</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Labor fuer naturwissenschaftlichen Unterricht.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Science Lab</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Laboratory for science teaching.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gewerbe</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer Gastronomie- und Verkaufsraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Commercial</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for hospitality and retail spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-10</td>
<td>RN-07</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gastronomie</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Cafeterias, Restaurants, Bars und Food-Courts.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Dining and beverage</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Cafeterias, restaurants, bars, and food courts.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-10-01</td>
<td>RN-07-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Cafeteria</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Selbstbedienungsgastronomie.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Cafeteria</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Self-service dining space.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-10-02</td>
<td>RN-07-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Restaurant</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bediente Gastronomie.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Restaurant</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Full-service dining space.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-10-03</td>
<td>RN-07-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Bar</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Getraenkeausschank.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Bar</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for beverage service.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-10-04</td>
<td>RN-07-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Food-Court</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Gemeinsame Gastronomieflaeche mit mehreren Anbietern.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Food Court</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Shared dining area with multiple vendors.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-20</td>
<td>RN-07</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Verkauf und Ausstellung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Verkaufs-, Ausstellungs- und Kioskbereiche.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Retail and exhibition</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Retail, sales, kiosk, and exhibition spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-20-01</td>
<td>RN-07-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Verkaufsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Warenpraesentation und Verkauf.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Retail Space</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for displaying and selling goods.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-20-02</td>
<td>RN-07-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Verkaufsflaeche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Offene Verkaufsflaeche.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Sales Floor</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Open retail sales area.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-20-03</td>
<td>RN-07-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kiosk</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kleiner Verkaufs- oder Servicebereich.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Kiosk</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Small retail or service counter space.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-20-04</td>
<td>RN-07-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kundenbetreuungsbereich</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bereich fuer Kundenbetreuung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Customer Service Area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Area for customer assistance and service.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-20-05</td>
<td>RN-07-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Ausstellungsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Ausstellungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Exhibition Space</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for displays and exhibitions.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-30</td>
<td>RN-07</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Beherbergung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Hotel- und Gaestezimmer.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Hospitality</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Hotel and guest accommodation rooms.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-07-30-01</td>
<td>RN-07-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hotelzimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Uebernachtungszimmer fuer Gaeste.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Hotel Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Guest accommodation room.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Industrie</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer Produktions- und Werkraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Industrial</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for production and workshop spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-10</td>
<td>RN-08</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Produktion</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Werkstaetten, Produktionshallen, Montage und Reinraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Production</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Workshops, production halls, assembly, and clean rooms.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-10-01</td>
<td>RN-08-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Werkstatt</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer manuelle Fertigung und Reparatur.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Workshop</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for manual fabrication and repair.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-10-02</td>
<td>RN-08-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Produktionshalle</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Halle fuer Produktionsprozesse.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Production Hall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Hall for manufacturing processes.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-10-03</td>
<td>RN-08-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Montagebereich</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bereich fuer Montage.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Assembly Area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Area for product assembly.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-10-04</td>
<td>RN-08-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Verpackungsbereich</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bereich fuer Verpackung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Packaging Area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Area for packaging goods.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-10-05</td>
<td>RN-08-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Reinraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Produktionsraum mit kontrollierter Umgebung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Clean Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Controlled-environment production room.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-20</td>
<td>RN-08</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Logistik</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Lagerung, Be-/Entladung, Qualitaetskontrolle und Wartung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Logistics</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Warehousing, loading, quality control, and maintenance.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-20-01</td>
<td>RN-08-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Lagerhalle</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Halle oder Raum fuer Warenlagerung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Warehouse</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room or hall for goods storage.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-20-02</td>
<td>RN-08-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Laderampe</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bereich fuer Be- und Entladung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Loading Dock</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Area for loading and unloading goods.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-20-03</td>
<td>RN-08-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Qualitaetskontrollraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Pruefung und Qualitaetskontrolle.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Quality Control Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for inspection and quality testing.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-20-04</td>
<td>RN-08-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wartungsbucht</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bucht fuer Geraetewartung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Maintenance Bay</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Bay for equipment maintenance.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-30</td>
<td>RN-08</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Spezielle Industrie</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Ueberdeckte Hoefe und spezielle Industrieraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Special industrial</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Covered yards and special industrial spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-08-30-01</td>
<td>RN-08-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Ueberdachter Hof</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Ueberdachter Aussenarbeits- oder Lagerhof als Raum modelliert.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Covered Yard</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Covered exterior work or storage yard modeled as space.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Technik</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer Technik- und Anlagenraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Technical</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for building services and plant rooms.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-10</td>
<td>RN-09</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">HLK und Sanitaertechnik</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Heizungs-, Kaelte-, Pumpen- und Sprinklerzentralen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">HVAC and plumbing plant</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Heating, cooling, pumping, and fire suppression plant rooms.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-10-01</td>
<td>RN-09-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">HLK-Zentralraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Heizungs-, Lueftungs- und Klimaanlagen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">HVAC Plant Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for heating, ventilation, and cooling plant.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-10-02</td>
<td>RN-09-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Pumpenraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Pumpen und Fluessigkeitstechnik.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Pump Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for pumps and fluid handling.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-10-03</td>
<td>RN-09-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Heizungsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Heizkessel und Waermeerzeugung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Boiler Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for boilers and heat generation.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-10-04</td>
<td>RN-09-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kaelteraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Kaelteanlagen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Chiller Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for chillers and cooling plant.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-10-05</td>
<td>RN-09-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Sprinklerraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Sprinkler- und Loeschanlagen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Sprinkler Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for fire suppression equipment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-20</td>
<td>RN-09</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Elektro- und IT-Technik</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Elektro-, Generator-, Transformator-, Server- und Kommunikationsraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Electrical and IT plant</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Electrical, generator, transformer, server, and telecom rooms.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-20-01</td>
<td>RN-09-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Elektroraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer elektrische Verteilung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Electrical Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for electrical distribution equipment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-20-02</td>
<td>RN-09-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Serverraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer IT- und Netzwerktechnik.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Server Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for IT and network equipment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-20-03</td>
<td>RN-09-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Generatorraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Notstromaggregate.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Generator Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for backup power generation.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-20-04</td>
<td>RN-09-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Transformatorenraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Transformatoren.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Transformer Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for electrical transformers.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-20-05</td>
<td>RN-09-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kommunikationsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Telekommunikations- und Schwachstromanlagen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Communications Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for telecom and low-voltage systems.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-30</td>
<td>RN-09</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Zaehler und Entsorgung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Zaehlerraeume und Abfallraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Metering and waste</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Meter rooms and waste handling spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-30-01</td>
<td>RN-09-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Zaehlerraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Verbrauchszaehler.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Meter Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for utility metering equipment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-09-30-02</td>
<td>RN-09-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Abfallraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Abfallsammlung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Waste Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for waste collection and handling.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Lager</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer Lager- und Nebenraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Storage</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for storage and ancillary spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-10</td>
<td>RN-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Allgemeine Lagertypen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Allgemeine, Material-, Geraete- und Hauswartlager.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">General storage types</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">General, supply, equipment, and janitor storage.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-10-01</td>
<td>RN-10-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Allgemeiner Lagerraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer allgemeine Materiallagerung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">General Storage</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for general material storage.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-10-02</td>
<td>RN-10-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Materialraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Verbrauchsmaterial.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Supply Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for consumable supplies.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-10-03</td>
<td>RN-10-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Geraetelager</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Lager fuer Geraete und Werkzeuge.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Equipment Storage</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Storage for tools and equipment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-10-04</td>
<td>RN-10-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Annahmelager</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Zwischenlager am Annahmeort.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Unloading Storage</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Temporary storage at delivery point.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-10-05</td>
<td>RN-10-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hauswarteschrank</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kleiner Raum fuer Reinigungsmaterial.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Janitor Closet</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Small room for cleaning supplies and equipment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-20</td>
<td>RN-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Speziallager</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Archive, Postraeume und Kuehllager.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Specialized storage</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Archives, mail rooms, and cold storage.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-20-01</td>
<td>RN-10-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Archivraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Dokumenten- und Aktenarchive.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Archive Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for document and record archives.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-20-02</td>
<td>RN-10-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Postraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Postein- und -ausgang.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Mail Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for incoming and outgoing mail.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-10-20-03</td>
<td>RN-10-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kuehlraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Gekuehlter Lagerraum.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Cold Storage</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Refrigerated storage room.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aussen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer als IfcSpace modellierte Aussenraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Outdoor</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for exterior spaces modeled as IfcSpace.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-10</td>
<td>RN-11</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aussenplattformen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Balkone, Terrassen und Innenhoefe.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Exterior platforms</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Balconies, terraces, and patios.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-10-01</td>
<td>RN-11-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Balkon</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Vom Innern erschlossene Aussenplattform.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Balcony</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Exterior projecting platform accessed from inside.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-10-02</td>
<td>RN-11-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Terrasse</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenliegende Terrassenflaeche.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Terrace</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Exterior paved or decked platform.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-10-03</td>
<td>RN-11-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Innenhof</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Innenhof oder Patio.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Patio</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Enclosed or semi-enclosed outdoor sitting area.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-20</td>
<td>RN-11</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Landschaft und Freizeit</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Gaerten, Spielplaetze und Beckenflaechen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Landscape and recreation</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Gardens, playgrounds, and pool areas.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-20-01</td>
<td>RN-11-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gartenflaeche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Als Raum modellierte Gartenflaeche.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Garden Area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Landscaped outdoor area as space.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-20-02</td>
<td>RN-11-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Spielplatz</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenliegender Spielbereich.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Playground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Outdoor play area.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-20-03</td>
<td>RN-11-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Beckenflaeche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenliegende Becken- oder Wasserflaeche.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Pool Area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Outdoor pool or water feature area.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-30</td>
<td>RN-11</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Ueberdachte Aussenwege</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Ueberdachte Fusswege und Portiken.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Covered exterior routes</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Covered walkways and porticos.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-30-01</td>
<td>RN-11-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Ueberdachter Fussweg</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Ueberdachter Aussenweg fuer Fussgaenger.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Covered Walkway</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Covered exterior pedestrian route.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-11-30-02</td>
<td>RN-11-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Portikus</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Ueberdachter Aussenanbau am Eingang.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Portico</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Covered exterior entrance structure.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-12</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hohlraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer nicht nutzbare Hohl- und Sonderraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Void</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for non-occupiable void and special spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-12-10</td>
<td>RN-12</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Vertikale Hohlraeume</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Schaechte und Steigzonen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Vertical voids</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Shafts and service risers.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-12-10-01</td>
<td>RN-12-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Schacht</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Vertikaler Technik- oder Erschliessungsschacht.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Shaft</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Vertical service or circulation shaft.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-12-10-02</td>
<td>RN-12-10</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Steigzone</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Vertikale Gebaeudetechnik-Steigzone.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Riser</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Vertical building services riser.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-12-20</td>
<td>RN-12</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Installations- und Luftraeume</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Installationshohlraeume und modellierter Luftraum.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Plenums and air volumes</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Plenums, mechanical voids, and modeled air spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-12-20-01</td>
<td>RN-12-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Installationszwischenraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Installationshohlraum in Decke oder Boden.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Plenum</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Ceiling or floor service void.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-12-20-02</td>
<td>RN-12-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Technikhohlraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Nicht begehbarer Technikhohlraum.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Mechanical Void</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Non-accessible mechanical void.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-12-20-03</td>
<td>RN-12-20</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Luftraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Nicht nutzbarer Luftraum im Modell.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Air Space</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Non-occupiable air volume in the model.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-12-30</td>
<td>RN-12</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Konstruktions- und Sonderraeume</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Atrien, Konstruktionshohlraeume und Innenparkierung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Structural and special voids</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Atria, structural voids, and interior parking stalls.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-12-30-01</td>
<td>RN-12-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Atrium</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Mehrgeschossiger offener Innenraum.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Atrium Void</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Multistory open interior volume.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-12-30-02</td>
<td>RN-12-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Konstruktionshohlraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Hohlraum in tragenden Bauteilen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Structural Void</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Void within structural elements.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-12-30-03</td>
<td>RN-12-30</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Innenparkierplatz</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Einzelner Parkierplatz in geschlossener Anlage.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Interior Parking Stall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Individual parking space within a structure.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
</tbody>
</table>
</div>
