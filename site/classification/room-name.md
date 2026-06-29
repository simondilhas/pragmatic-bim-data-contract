# Building space name classification

Source: [`building-space-name-classification.skos.ttl`](sources/room-name.ttl)

## Scheme

- **definition (de):** Normalisierte abstrakte Raumbezeichnungen fuer IfcSpace, abgeleitet von der armasuisse Raumliste und fuer allgemeinen Gebaeudegebrauch reduziert.
- **definition (en):** Normalized abstract room name types for IfcSpace, derived from armasuisse Raumliste and reduced for general building use.
- **prefLabel (de):** Gebaeude-Raumbezeichnungsklassifikation
- **prefLabel (en):** Building Space Name Classification
- **title (en):** Building Space Name Classification

## Hierarchy

```mermaid
classDiagram
direction TB
class n_RN_CIR_AIS["RN-CIR-AIS: Aisle"]
class n_RN_CIR_COR["RN-CIR-COR: Corridor"]
class n_RN_CIR_ELV["RN-CIR-ELV: Elevator Lobby"]
class n_RN_CIR_ENT["RN-CIR-ENT: Entrance Hall"]
class n_RN_CIR_GAL["RN-CIR-GAL: Gallery"]
class n_RN_CIR_LND["RN-CIR-LND: Landing"]
class n_RN_CIR_LOB["RN-CIR-LOB: Lobby"]
class n_RN_CIR_RAM["RN-CIR-RAM: Ramp"]
class n_RN_CIR_STR["RN-CIR-STR: Stairwell"]
class n_RN_CIR_VES["RN-CIR-VES: Vestibule"]
class n_RN_COM_BAR["RN-COM-BAR: Bar"]
class n_RN_COM_CAF["RN-COM-CAF: Cafeteria"]
class n_RN_COM_CUS["RN-COM-CUS: Customer Service Area"]
class n_RN_COM_EXH["RN-COM-EXH: Exhibition Space"]
class n_RN_COM_FOD["RN-COM-FOD: Food Court"]
class n_RN_COM_HTL["RN-COM-HTL: Hotel Room"]
class n_RN_COM_KSK["RN-COM-KSK: Kiosk"]
class n_RN_COM_RET["RN-COM-RET: Retail Space"]
class n_RN_COM_RST["RN-COM-RST: Restaurant"]
class n_RN_COM_SAL["RN-COM-SAL: Sales Floor"]
class n_RN_HLC_EXM["RN-HLC-EXM: Examination Room"]
class n_RN_HLC_IMG["RN-HLC-IMG: Imaging Room"]
class n_RN_HLC_LAB["RN-HLC-LAB: Medical Laboratory"]
class n_RN_HLC_NRS["RN-HLC-NRS: Nurses Station"]
class n_RN_HLC_OR["RN-HLC-OR: Operating Room"]
class n_RN_HLC_PAT["RN-HLC-PAT: Patient Room"]
class n_RN_HLC_PRM["RN-HLC-PRM: Procedure Room"]
class n_RN_HLC_RCV["RN-HLC-RCV: Recovery Room"]
class n_RN_HLC_TRT["RN-HLC-TRT: Treatment Room"]
class n_RN_HLC_WTR["RN-HLC-WTR: Waiting Room"]
class n_RN_HYG_CHG["RN-HYG-CHG: Changing Room"]
class n_RN_HYG_GRD["RN-HYG-GRD: Cloakroom"]
class n_RN_HYG_LCK["RN-HYG-LCK: Locker Room"]
class n_RN_HYG_SHW["RN-HYG-SHW: Shower Room"]
class n_RN_HYG_WC_F["RN-HYG-WC-F: Female Toilet"]
class n_RN_HYG_WC_IV["RN-HYG-WC-IV: Accessible Toilet"]
class n_RN_HYG_WC_M["RN-HYG-WC-M: Male Toilet"]
class n_RN_HYG_WC_MIX["RN-HYG-WC-MIX: Unisex Toilet"]
class n_RN_IND_ASM["RN-IND-ASM: Assembly Area"]
class n_RN_IND_CLN["RN-IND-CLN: Clean Room"]
class n_RN_IND_LDK["RN-IND-LDK: Loading Dock"]
class n_RN_IND_MNT["RN-IND-MNT: Maintenance Bay"]
class n_RN_IND_PKG["RN-IND-PKG: Packaging Area"]
class n_RN_IND_PRD["RN-IND-PRD: Production Hall"]
class n_RN_IND_QC["RN-IND-QC: Quality Control Room"]
class n_RN_IND_WHS["RN-IND-WHS: Warehouse"]
class n_RN_IND_WRK["RN-IND-WRK: Workshop"]
class n_RN_IND_YRD["RN-IND-YRD: Covered Yard"]
class n_RN_LRN_ART["RN-LRN-ART: Art Studio"]
class n_RN_LRN_AUS["RN-LRN-AUS: Auditorium"]
class n_RN_LRN_CLS["RN-LRN-CLS: Classroom"]
class n_RN_LRN_CMP["RN-LRN-CMP: Computer Lab"]
class n_RN_LRN_LCT["RN-LRN-LCT: Lecture Hall"]
class n_RN_LRN_LIB["RN-LRN-LIB: Library Room"]
class n_RN_LRN_SCI["RN-LRN-SCI: Science Lab"]
class n_RN_LRN_SEM["RN-LRN-SEM: Seminar Room"]
class n_RN_LRN_STU["RN-LRN-STU: Study Room"]
class n_RN_LRN_WRK["RN-LRN-WRK: Training Workshop"]
class n_RN_OUT_BLN["RN-OUT-BLN: Balcony"]
class n_RN_OUT_CWK["RN-OUT-CWK: Covered Walkway"]
class n_RN_OUT_GDN["RN-OUT-GDN: Garden Area"]
class n_RN_OUT_PAT["RN-OUT-PAT: Patio"]
class n_RN_OUT_PLY["RN-OUT-PLY: Playground"]
class n_RN_OUT_PRT["RN-OUT-PRT: Portico"]
class n_RN_OUT_SPL["RN-OUT-SPL: Pool Area"]
class n_RN_OUT_TRR["RN-OUT-TRR: Terrace"]
class n_RN_RES_APT["RN-RES-APT: Apartment Unit"]
class n_RN_RES_BED["RN-RES-BED: Bedroom"]
class n_RN_RES_BTH["RN-RES-BTH: Bathroom"]
class n_RN_RES_CLO["RN-RES-CLO: Residential Closet"]
class n_RN_RES_DIN["RN-RES-DIN: Dining Room"]
class n_RN_RES_ENT["RN-RES-ENT: Residential Entry"]
class n_RN_RES_GST["RN-RES-GST: Guest Room"]
class n_RN_RES_KIT["RN-RES-KIT: Kitchen"]
class n_RN_RES_LAU["RN-RES-LAU: Laundry Room"]
class n_RN_RES_LIV["RN-RES-LIV: Living Room"]
class n_RN_RES_STU["RN-RES-STU: Home Study"]
class n_RN_RES_UTL["RN-RES-UTL: Utility Room"]
class n_RN_STO_ARC["RN-STO-ARC: Archive Room"]
class n_RN_STO_COL["RN-STO-COL: Cold Storage"]
class n_RN_STO_EQP["RN-STO-EQP: Equipment Storage"]
class n_RN_STO_GEN["RN-STO-GEN: General Storage"]
class n_RN_STO_JAN["RN-STO-JAN: Janitor Closet"]
class n_RN_STO_MAL["RN-STO-MAL: Mail Room"]
class n_RN_STO_SUP["RN-STO-SUP: Supply Room"]
class n_RN_STO_ULD["RN-STO-ULD: Unloading Storage"]
class n_RN_TEC_BOI["RN-TEC-BOI: Boiler Room"]
class n_RN_TEC_CHL["RN-TEC-CHL: Chiller Room"]
class n_RN_TEC_COM["RN-TEC-COM: Communications Room"]
class n_RN_TEC_ELC["RN-TEC-ELC: Electrical Room"]
class n_RN_TEC_GEN["RN-TEC-GEN: Generator Room"]
class n_RN_TEC_HVC["RN-TEC-HVC: HVAC Plant Room"]
class n_RN_TEC_MMR["RN-TEC-MMR: Meter Room"]
class n_RN_TEC_PMP["RN-TEC-PMP: Pump Room"]
class n_RN_TEC_SPR["RN-TEC-SPR: Sprinkler Room"]
class n_RN_TEC_SRV["RN-TEC-SRV: Server Room"]
class n_RN_TEC_TRA["RN-TEC-TRA: Transformer Room"]
class n_RN_TEC_WST["RN-TEC-WST: Waste Room"]
class n_RN_VOI_AIR["RN-VOI-AIR: Air Space"]
class n_RN_VOI_ATR["RN-VOI-ATR: Atrium Void"]
class n_RN_VOI_MCH["RN-VOI-MCH: Mechanical Void"]
class n_RN_VOI_PLN["RN-VOI-PLN: Plenum"]
class n_RN_VOI_PRK["RN-VOI-PRK: Interior Parking Stall"]
class n_RN_VOI_RIS["RN-VOI-RIS: Riser"]
class n_RN_VOI_SHA["RN-VOI-SHA: Shaft"]
class n_RN_VOI_STR["RN-VOI-STR: Structural Void"]
class n_RN_WRK_ADM["RN-WRK-ADM: Administrative Office"]
class n_RN_WRK_BRK["RN-WRK-BRK: Break Room"]
class n_RN_WRK_CNF["RN-WRK-CNF: Conference Room"]
class n_RN_WRK_COW["RN-WRK-COW: Coworking Space"]
class n_RN_WRK_FCS["RN-WRK-FCS: Focus Room"]
class n_RN_WRK_MNG["RN-WRK-MNG: Manager Office"]
class n_RN_WRK_MTG["RN-WRK-MTG: Meeting Room"]
class n_RN_WRK_OAD["RN-WRK-OAD: Open Administrative Area"]
class n_RN_WRK_OFF["RN-WRK-OFF: Office"]
class n_RN_WRK_OPN["RN-WRK-OPN: Open-Plan Office"]
class n_RN_WRK_PHN["RN-WRK-PHN: Phone Booth"]
class n_RN_WRK_REC["RN-WRK-REC: Reception"]
class n_RN_CIR["RN_CIR: Circulation Room Names"]
class n_RN_COM["RN_COM: Commercial Room Names"]
class n_RN_HLC["RN_HLC: Healthcare Room Names"]
class n_RN_HYG["RN_HYG: Hygiene Room Names"]
class n_RN_IND["RN_IND: Industrial Room Names"]
class n_RN_LRN["RN_LRN: Education Room Names"]
class n_RN_OUT["RN_OUT: Outdoor Room Names"]
class n_RN_RES["RN_RES: Residential Room Names"]
class n_RN_STO["RN_STO: Storage Room Names"]
class n_RN_TEC["RN_TEC: Technical Room Names"]
class n_RN_VOI["RN_VOI: Void Room Names"]
class n_RN_WRK["RN_WRK: Work Room Names"]
n_RN_CIR <|-- n_RN_CIR_AIS
n_RN_CIR <|-- n_RN_CIR_COR
n_RN_CIR <|-- n_RN_CIR_ELV
n_RN_CIR <|-- n_RN_CIR_ENT
n_RN_CIR <|-- n_RN_CIR_GAL
n_RN_CIR <|-- n_RN_CIR_LND
n_RN_CIR <|-- n_RN_CIR_LOB
n_RN_CIR <|-- n_RN_CIR_RAM
n_RN_CIR <|-- n_RN_CIR_STR
n_RN_CIR <|-- n_RN_CIR_VES
n_RN_COM <|-- n_RN_COM_BAR
n_RN_COM <|-- n_RN_COM_CAF
n_RN_COM <|-- n_RN_COM_CUS
n_RN_COM <|-- n_RN_COM_EXH
n_RN_COM <|-- n_RN_COM_FOD
n_RN_COM <|-- n_RN_COM_HTL
n_RN_COM <|-- n_RN_COM_KSK
n_RN_COM <|-- n_RN_COM_RET
n_RN_COM <|-- n_RN_COM_RST
n_RN_COM <|-- n_RN_COM_SAL
n_RN_HLC <|-- n_RN_HLC_EXM
n_RN_HLC <|-- n_RN_HLC_IMG
n_RN_HLC <|-- n_RN_HLC_LAB
n_RN_HLC <|-- n_RN_HLC_NRS
n_RN_HLC <|-- n_RN_HLC_OR
n_RN_HLC <|-- n_RN_HLC_PAT
n_RN_HLC <|-- n_RN_HLC_PRM
n_RN_HLC <|-- n_RN_HLC_RCV
n_RN_HLC <|-- n_RN_HLC_TRT
n_RN_HLC <|-- n_RN_HLC_WTR
n_RN_HYG <|-- n_RN_HYG_CHG
n_RN_HYG <|-- n_RN_HYG_GRD
n_RN_HYG <|-- n_RN_HYG_LCK
n_RN_HYG <|-- n_RN_HYG_SHW
n_RN_HYG <|-- n_RN_HYG_WC_F
n_RN_HYG <|-- n_RN_HYG_WC_IV
n_RN_HYG <|-- n_RN_HYG_WC_M
n_RN_HYG <|-- n_RN_HYG_WC_MIX
n_RN_IND <|-- n_RN_IND_ASM
n_RN_IND <|-- n_RN_IND_CLN
n_RN_IND <|-- n_RN_IND_LDK
n_RN_IND <|-- n_RN_IND_MNT
n_RN_IND <|-- n_RN_IND_PKG
n_RN_IND <|-- n_RN_IND_PRD
n_RN_IND <|-- n_RN_IND_QC
n_RN_IND <|-- n_RN_IND_WHS
n_RN_IND <|-- n_RN_IND_WRK
n_RN_IND <|-- n_RN_IND_YRD
n_RN_LRN <|-- n_RN_LRN_ART
n_RN_LRN <|-- n_RN_LRN_AUS
n_RN_LRN <|-- n_RN_LRN_CLS
n_RN_LRN <|-- n_RN_LRN_CMP
n_RN_LRN <|-- n_RN_LRN_LCT
n_RN_LRN <|-- n_RN_LRN_LIB
n_RN_LRN <|-- n_RN_LRN_SCI
n_RN_LRN <|-- n_RN_LRN_SEM
n_RN_LRN <|-- n_RN_LRN_STU
n_RN_LRN <|-- n_RN_LRN_WRK
n_RN_OUT <|-- n_RN_OUT_BLN
n_RN_OUT <|-- n_RN_OUT_CWK
n_RN_OUT <|-- n_RN_OUT_GDN
n_RN_OUT <|-- n_RN_OUT_PAT
n_RN_OUT <|-- n_RN_OUT_PLY
n_RN_OUT <|-- n_RN_OUT_PRT
n_RN_OUT <|-- n_RN_OUT_SPL
n_RN_OUT <|-- n_RN_OUT_TRR
n_RN_RES <|-- n_RN_RES_APT
n_RN_RES <|-- n_RN_RES_BED
n_RN_RES <|-- n_RN_RES_BTH
n_RN_RES <|-- n_RN_RES_CLO
n_RN_RES <|-- n_RN_RES_DIN
n_RN_RES <|-- n_RN_RES_ENT
n_RN_RES <|-- n_RN_RES_GST
n_RN_RES <|-- n_RN_RES_KIT
n_RN_RES <|-- n_RN_RES_LAU
n_RN_RES <|-- n_RN_RES_LIV
n_RN_RES <|-- n_RN_RES_STU
n_RN_RES <|-- n_RN_RES_UTL
n_RN_STO <|-- n_RN_STO_ARC
n_RN_STO <|-- n_RN_STO_COL
n_RN_STO <|-- n_RN_STO_EQP
n_RN_STO <|-- n_RN_STO_GEN
n_RN_STO <|-- n_RN_STO_JAN
n_RN_STO <|-- n_RN_STO_MAL
n_RN_STO <|-- n_RN_STO_SUP
n_RN_STO <|-- n_RN_STO_ULD
n_RN_TEC <|-- n_RN_TEC_BOI
n_RN_TEC <|-- n_RN_TEC_CHL
n_RN_TEC <|-- n_RN_TEC_COM
n_RN_TEC <|-- n_RN_TEC_ELC
n_RN_TEC <|-- n_RN_TEC_GEN
n_RN_TEC <|-- n_RN_TEC_HVC
n_RN_TEC <|-- n_RN_TEC_MMR
n_RN_TEC <|-- n_RN_TEC_PMP
n_RN_TEC <|-- n_RN_TEC_SPR
n_RN_TEC <|-- n_RN_TEC_SRV
n_RN_TEC <|-- n_RN_TEC_TRA
n_RN_TEC <|-- n_RN_TEC_WST
n_RN_VOI <|-- n_RN_VOI_AIR
n_RN_VOI <|-- n_RN_VOI_ATR
n_RN_VOI <|-- n_RN_VOI_MCH
n_RN_VOI <|-- n_RN_VOI_PLN
n_RN_VOI <|-- n_RN_VOI_PRK
n_RN_VOI <|-- n_RN_VOI_RIS
n_RN_VOI <|-- n_RN_VOI_SHA
n_RN_VOI <|-- n_RN_VOI_STR
n_RN_WRK <|-- n_RN_WRK_ADM
n_RN_WRK <|-- n_RN_WRK_BRK
n_RN_WRK <|-- n_RN_WRK_CNF
n_RN_WRK <|-- n_RN_WRK_COW
n_RN_WRK <|-- n_RN_WRK_FCS
n_RN_WRK <|-- n_RN_WRK_MNG
n_RN_WRK <|-- n_RN_WRK_MTG
n_RN_WRK <|-- n_RN_WRK_OAD
n_RN_WRK <|-- n_RN_WRK_OFF
n_RN_WRK <|-- n_RN_WRK_OPN
n_RN_WRK <|-- n_RN_WRK_PHN
n_RN_WRK <|-- n_RN_WRK_REC
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
<td>RN-CIR-AIS</td>
<td>RN_CIR</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gang</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Schmaler Durchgang zwischen Reihen oder Funktionen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Aisle</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Narrow passage between rows or functions.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-CIR-COR</td>
<td>RN_CIR</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Korridor</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Horizontaler Verbindungsgang.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Corridor</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Horizontal circulation passage.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-CIR-ELV</td>
<td>RN_CIR</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aufzugszone</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Wartebereich an Aufzugshaltestellen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Elevator Lobby</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Waiting area at elevator stops.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-CIR-ENT</td>
<td>RN_CIR</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Entree</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Uebergangsraum am Gebaeudeeingang.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Entrance Hall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Building entrance transition space.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-CIR-GAL</td>
<td>RN_CIR</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Galerie</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Erschliessungsgalerie als Teil der Hauptnutzung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Gallery</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Circulation gallery integral to main activity.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-CIR-LND</td>
<td>RN_CIR</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Podest</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Treppen- oder Rampenpodest.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Landing</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Stair or ramp landing platform.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-CIR-LOB</td>
<td>RN_CIR</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Eingangshalle</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Eingangshalle oder Empfoyer.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Lobby</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Main entrance lobby or reception hall.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-CIR-RAM</td>
<td>RN_CIR</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Rampe</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Geneigte barrierefreie Erschliessung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Ramp</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Inclined accessible circulation route.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-CIR-STR</td>
<td>RN_CIR</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Treppenhaus</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Treppenhaus mit Podesten.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Stairwell</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Enclosed stair and landing volume.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-CIR-VES</td>
<td>RN_CIR</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Vorraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Uebergangsraum zwischen Aussen und Innen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Vestibule</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Transition space between exterior and interior.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-COM-BAR</td>
<td>RN_COM</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Bar</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Getraenkeausschank.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Bar</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for beverage service.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-COM-CAF</td>
<td>RN_COM</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Cafeteria</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Selbstbedienungsgastronomie.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Cafeteria</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Self-service dining space.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-COM-CUS</td>
<td>RN_COM</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kundenbetreuungsbereich</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bereich fuer Kundenbetreuung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Customer Service Area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Area for customer assistance and service.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-COM-EXH</td>
<td>RN_COM</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Ausstellungsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Ausstellungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Exhibition Space</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for displays and exhibitions.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-COM-FOD</td>
<td>RN_COM</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Food-Court</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Gemeinsame Gastronomieflaeche mit mehreren Anbietern.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Food Court</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Shared dining area with multiple vendors.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-COM-HTL</td>
<td>RN_COM</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hotelzimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Uebernachtungszimmer fuer Gaeste.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Hotel Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Guest accommodation room.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-COM-KSK</td>
<td>RN_COM</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kiosk</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kleiner Verkaufs- oder Servicebereich.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Kiosk</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Small retail or service counter space.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-COM-RET</td>
<td>RN_COM</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Verkaufsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Warenpraesentation und Verkauf.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Retail Space</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for displaying and selling goods.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-COM-RST</td>
<td>RN_COM</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Restaurant</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bediente Gastronomie.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Restaurant</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Full-service dining space.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-COM-SAL</td>
<td>RN_COM</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Verkaufsflaeche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Offene Verkaufsflaeche.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Sales Floor</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Open retail sales area.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-HLC-EXM</td>
<td>RN_HLC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Untersuchungsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer aerztliche Untersuchung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Examination Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for clinical examination.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-HLC-IMG</td>
<td>RN_HLC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Bildgebungsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer diagnostische Bildgebung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Imaging Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for diagnostic imaging.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-HLC-LAB</td>
<td>RN_HLC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Medizinisches Labor</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Labor fuer medizinische Analysen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Medical Laboratory</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Laboratory for medical analysis.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-HLC-NRS</td>
<td>RN_HLC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Pflegestationszimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Zentrale Pflegestation.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Nurses Station</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Central nursing and monitoring workspace.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-HLC-OR</td>
<td>RN_HLC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Operationssaal</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer operative Eingriffe.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Operating Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for surgical procedures.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-HLC-PAT</td>
<td>RN_HLC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Patientenzimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer stationaere Pflege.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Patient Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for inpatient care and recovery.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-HLC-PRM</td>
<td>RN_HLC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Eingriffsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer kleinere medizinische Eingriffe.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Procedure Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for minor medical procedures.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-HLC-RCV</td>
<td>RN_HLC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aufwachraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer postoperative Ueberwachung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Recovery Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for post-procedure recovery.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-HLC-TRT</td>
<td>RN_HLC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Behandlungsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer ambulante Behandlung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Treatment Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for outpatient treatment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-HLC-WTR</td>
<td>RN_HLC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wartezimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer wartende Patienten und Besucher.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Waiting Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for patients and visitors to wait.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-HYG-CHG</td>
<td>RN_HYG</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Umkleideraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum zum Umziehen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Changing Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for changing clothes.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-HYG-GRD</td>
<td>RN_HYG</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Garderobe</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Garderobe mit oder ohne Bedienung am Eingang.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Cloakroom</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Staffed or unstaffed coat check at entry.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-HYG-LCK</td>
<td>RN_HYG</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Schliessfachraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum mit persoenlichen Schliessfaechern.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Locker Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room with personal lockers.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-HYG-SHW</td>
<td>RN_HYG</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Duschraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum mit Duscheinrichtungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Shower Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room with shower facilities.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-HYG-WC-F</td>
<td>RN_HYG</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Damen-WC</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">WC fuer Frauen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Female Toilet</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Toilet room for female use.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-HYG-WC-IV</td>
<td>RN_HYG</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Barrierefreies WC</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Rollstuhlgaengiges WC.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Accessible Toilet</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Wheelchair-accessible toilet room.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-HYG-WC-M</td>
<td>RN_HYG</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Herren-WC</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">WC fuer Maenner.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Male Toilet</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Toilet room for male use.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-HYG-WC-MIX</td>
<td>RN_HYG</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Allgemeines WC</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">WC fuer gemischte oder all-gender Nutzung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Unisex Toilet</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Toilet room for mixed or all-gender use.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-IND-ASM</td>
<td>RN_IND</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Montagebereich</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bereich fuer Montage.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Assembly Area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Area for product assembly.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-IND-CLN</td>
<td>RN_IND</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Reinraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Produktionsraum mit kontrollierter Umgebung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Clean Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Controlled-environment production room.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-IND-LDK</td>
<td>RN_IND</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Laderampe</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bereich fuer Be- und Entladung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Loading Dock</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Area for loading and unloading goods.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-IND-MNT</td>
<td>RN_IND</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wartungsbucht</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bucht fuer Geraetewartung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Maintenance Bay</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Bay for equipment maintenance.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-IND-PKG</td>
<td>RN_IND</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Verpackungsbereich</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bereich fuer Verpackung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Packaging Area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Area for packaging goods.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-IND-PRD</td>
<td>RN_IND</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Produktionshalle</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Halle fuer Produktionsprozesse.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Production Hall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Hall for manufacturing processes.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-IND-QC</td>
<td>RN_IND</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Qualitaetskontrollraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Pruefung und Qualitaetskontrolle.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Quality Control Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for inspection and quality testing.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-IND-WHS</td>
<td>RN_IND</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Lagerhalle</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Halle oder Raum fuer Warenlagerung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Warehouse</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room or hall for goods storage.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-IND-WRK</td>
<td>RN_IND</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Werkstatt</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer manuelle Fertigung und Reparatur.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Workshop</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for manual fabrication and repair.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-IND-YRD</td>
<td>RN_IND</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Ueberdachter Hof</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Ueberdachter Aussenarbeits- oder Lagerhof als Raum modelliert.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Covered Yard</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Covered exterior work or storage yard modeled as space.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-LRN-ART</td>
<td>RN_LRN</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kunstatelier</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer bildnerischen Unterricht.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Art Studio</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for visual arts instruction and practice.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-LRN-AUS</td>
<td>RN_LRN</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aula</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Grosse Versammlungshalle fuer Veranstaltungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Auditorium</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Large assembly hall for events.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-LRN-CLS</td>
<td>RN_LRN</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Klassenzimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Schul- oder Gruppenunterricht.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Classroom</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for school or group instruction.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-LRN-CMP</td>
<td>RN_LRN</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Computerraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum mit Computerarbeitsplaetzen fuer Unterricht.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Computer Lab</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room with computer workstations for teaching.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-LRN-LCT</td>
<td>RN_LRN</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hoersaal</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum mit festem Gestuehl fuer Vorlesungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Lecture Hall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room with fixed seating for lectures.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-LRN-LIB</td>
<td>RN_LRN</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Bibliotheksraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Lesen und Bibliotheksnutzung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Library Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for reading and library use.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-LRN-SCI</td>
<td>RN_LRN</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Naturwissenschaftslabor</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Labor fuer naturwissenschaftlichen Unterricht.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Science Lab</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Laboratory for science teaching.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-LRN-SEM</td>
<td>RN_LRN</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Seminarraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Seminare und Workshops.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Seminar Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for seminars and workshops.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-LRN-STU</td>
<td>RN_LRN</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Lernraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer selbststaendiges Lernen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Study Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for self-directed study.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-LRN-WRK</td>
<td>RN_LRN</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Ausbildungswerkstatt</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer praktische Ausbildung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Training Workshop</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for practical skills training.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-OUT-BLN</td>
<td>RN_OUT</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Balkon</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Vom Innern erschlossene Aussenplattform.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Balcony</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Exterior projecting platform accessed from inside.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-OUT-CWK</td>
<td>RN_OUT</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Ueberdachter Gang</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Ueberdachter Aussenweg.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Covered Walkway</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Covered exterior pedestrian route.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-OUT-GDN</td>
<td>RN_OUT</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gartenflaeche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Als Raum modellierte Gartenflaeche.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Garden Area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Landscaped outdoor area as space.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-OUT-PAT</td>
<td>RN_OUT</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Innenhof</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Innenhof oder Patio.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Patio</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Enclosed or semi-enclosed outdoor sitting area.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-OUT-PLY</td>
<td>RN_OUT</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Spielplatz</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenliegender Spielbereich.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Playground</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Outdoor play area.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-OUT-PRT</td>
<td>RN_OUT</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Portikus</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Ueberdachter Aussenanbau am Eingang.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Portico</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Covered exterior entrance structure.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-OUT-SPL</td>
<td>RN_OUT</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Beckenflaeche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenliegende Becken- oder Wasserflaeche.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Pool Area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Outdoor pool or water feature area.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-OUT-TRR</td>
<td>RN_OUT</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Terrasse</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenliegende Terrassenflaeche.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Terrace</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Exterior paved or decked platform.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-RES-APT</td>
<td>RN_RES</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wohneinheit</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Generische Wohneinheit ohne weitere Unterteilung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Apartment Unit</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Generic residential unit space when not subdivided further.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-RES-BED</td>
<td>RN_RES</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Schlafzimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum primaer fuer Schlafen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Bedroom</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room primarily used for sleeping.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-RES-BTH</td>
<td>RN_RES</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Badezimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum mit Bad, Dusche oder Koerperpflege.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Bathroom</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room with bath, shower, or personal hygiene fixtures.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-RES-CLO</td>
<td>RN_RES</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Abstellraum Wohnen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kleiner Abstellraum innerhalb einer Wohneinheit.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Residential Closet</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Small storage within a dwelling unit.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-RES-DIN</td>
<td>RN_RES</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Esszimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Mahlzeiten.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Dining Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for eating meals.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-RES-ENT</td>
<td>RN_RES</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wohnungseingang</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Eingangsbereich innerhalb einer Wohneinheit.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Residential Entry</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Entry space within a dwelling unit.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-RES-GST</td>
<td>RN_RES</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gaestezimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer ueber Nacht bleibende Gaeste.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Guest Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for overnight guests.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-RES-KIT</td>
<td>RN_RES</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kueche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Speisezubereitung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Kitchen</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for food preparation.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-RES-LAU</td>
<td>RN_RES</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Waschkueche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Waeschepflege.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Laundry Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for washing and drying clothes.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-RES-LIV</td>
<td>RN_RES</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wohnzimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Wohnen und Entspannung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Living Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for daily living and relaxation.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-RES-STU</td>
<td>RN_RES</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Arbeitszimmer</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Wohnlicher Raum fuer Arbeit oder Studium.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Home Study</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Residential room for study or home office work.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-RES-UTL</td>
<td>RN_RES</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hauswirtschaftsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer haushaltstechnische Einrichtungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Utility Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for domestic utilities and equipment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-STO-ARC</td>
<td>RN_STO</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Archivraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Dokumenten- und Aktenarchive.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Archive Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for document and record archives.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-STO-COL</td>
<td>RN_STO</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kuehlraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Gekuehlter Lagerraum.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Cold Storage</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Refrigerated storage room.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-STO-EQP</td>
<td>RN_STO</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Geraetelager</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Lager fuer Geraete und Werkzeuge.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Equipment Storage</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Storage for tools and equipment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-STO-GEN</td>
<td>RN_STO</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Allgemeiner Lagerraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer allgemeine Materiallagerung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">General Storage</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for general material storage.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-STO-JAN</td>
<td>RN_STO</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hauswarteschrank</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kleiner Raum fuer Reinigungsmaterial.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Janitor Closet</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Small room for cleaning supplies and equipment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-STO-MAL</td>
<td>RN_STO</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Postraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Postein- und -ausgang.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Mail Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for incoming and outgoing mail.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-STO-SUP</td>
<td>RN_STO</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Materialraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Verbrauchsmaterial.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Supply Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for consumable supplies.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-STO-ULD</td>
<td>RN_STO</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Annahmelager</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Zwischenlager am Annahmeort.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Unloading Storage</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Temporary storage at delivery point.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-TEC-BOI</td>
<td>RN_TEC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Heizungsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Heizkessel und Waermeerzeugung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Boiler Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for boilers and heat generation.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-TEC-CHL</td>
<td>RN_TEC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kaelteraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Kaelteanlagen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Chiller Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for chillers and cooling plant.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-TEC-COM</td>
<td>RN_TEC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kommunikationsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Telekommunikations- und Schwachstromanlagen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Communications Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for telecom and low-voltage systems.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-TEC-ELC</td>
<td>RN_TEC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Elektroraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer elektrische Verteilung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Electrical Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for electrical distribution equipment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-TEC-GEN</td>
<td>RN_TEC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Generatorraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Notstromaggregate.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Generator Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for backup power generation.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-TEC-HVC</td>
<td>RN_TEC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">HLK-Zentralraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Heizungs-, Lueftungs- und Klimaanlagen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">HVAC Plant Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for heating, ventilation, and cooling plant.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-TEC-MMR</td>
<td>RN_TEC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Zaehlerraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Verbrauchszaehler.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Meter Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for utility metering equipment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-TEC-PMP</td>
<td>RN_TEC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Pumpenraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Pumpen und Fluessigkeitstechnik.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Pump Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for pumps and fluid handling.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-TEC-SPR</td>
<td>RN_TEC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Sprinklerraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Sprinkler- und Loeschanlagen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Sprinkler Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for fire suppression equipment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-TEC-SRV</td>
<td>RN_TEC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Serverraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer IT- und Netzwerktechnik.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Server Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for IT and network equipment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-TEC-TRA</td>
<td>RN_TEC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Transformatorenraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Transformatoren.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Transformer Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for electrical transformers.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-TEC-WST</td>
<td>RN_TEC</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Abfallraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer Abfallsammlung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Waste Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for waste collection and handling.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-VOI-AIR</td>
<td>RN_VOI</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Luftraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Nicht nutzbarer Luftraum im Modell.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Air Space</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Non-occupiable air volume in the model.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-VOI-ATR</td>
<td>RN_VOI</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Atrium</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Mehrgeschossiger offener Innenraum.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Atrium Void</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Multistory open interior volume.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-VOI-MCH</td>
<td>RN_VOI</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Technikhohlraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Nicht begehbarer Technikhohlraum.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Mechanical Void</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Non-accessible mechanical void.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-VOI-PLN</td>
<td>RN_VOI</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Installationszwischenraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Installationshohlraum in Decke oder Boden.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Plenum</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Ceiling or floor service void.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-VOI-PRK</td>
<td>RN_VOI</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Innenparkierplatz</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Einzelner Parkierplatz in geschlossener Anlage.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Interior Parking Stall</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Individual parking space within a structure.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-VOI-RIS</td>
<td>RN_VOI</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Steigzone</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Vertikale Gebaeudetechnik-Steigzone.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Riser</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Vertical building services riser.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-VOI-SHA</td>
<td>RN_VOI</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Schacht</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Vertikaler Technik- oder Erschliessungsschacht.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Shaft</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Vertical service or circulation shaft.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-VOI-STR</td>
<td>RN_VOI</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Konstruktionshohlraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Hohlraum in tragenden Bauteilen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Structural Void</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Void within structural elements.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-WRK-ADM</td>
<td>RN_WRK</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Verwaltungsbuero</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Buero fuer Verwaltungspersonal.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Administrative Office</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Office for administrative staff.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-WRK-BRK</td>
<td>RN_WRK</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Pausenraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Informeller Raum fuer Pausen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Break Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Informal staff rest and refreshment space.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-WRK-CNF</td>
<td>RN_WRK</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Konferenzraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer formelle Sitzungen und Praesentationen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Conference Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for formal meetings and presentations.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-WRK-COW</td>
<td>RN_WRK</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Coworking-Flaeche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Gemeinschaftlich genutzter flexibler Arbeitsraum.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Coworking Space</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Shared flexible workspace.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-WRK-FCS</td>
<td>RN_WRK</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Fokusraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kleiner Raum fuer konzentrierte Einzelarbeit.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Focus Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Small room for concentrated individual work.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-WRK-MNG</td>
<td>RN_WRK</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Fuehrungsbuero</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Buero fuer Fuehrungsfunktionen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Manager Office</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Office for management roles.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-WRK-MTG</td>
<td>RN_WRK</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Besprechungsraum</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Raum fuer kleine Besprechungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Meeting Room</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Room for small group meetings.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-WRK-OAD</td>
<td>RN_WRK</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Offene Verwaltungsflaeche</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Offene Verwaltungsarbeitsflaeche.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Open Administrative Area</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Open administrative work area.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-WRK-OFF</td>
<td>RN_WRK</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Buero</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Buero fuer Einzel- oder Gruppenarbeit.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Office</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Enclosed office for individual or shared desk work.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-WRK-OPN</td>
<td>RN_WRK</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Grossraumbuero</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Offene Burolandschaft ohne geschlossene Zellbueros.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Open-Plan Office</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Open office landscape without full-height partitions.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-WRK-PHN</td>
<td>RN_WRK</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Telefonbox</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kleine Kabine fuer Telefongespraeche.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Phone Booth</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Small enclosure for private calls.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN-WRK-REC</td>
<td>RN_WRK</td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Empfang</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Empfang und Wartebereich fuer Besucher.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Reception</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Visitor reception and waiting area.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN_CIR</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Erschliessungsraumbezeichnungen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer Erschliessungsraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Circulation Room Names</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for circulation and access spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN_COM</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gewerberaumbezeichnungen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer Gastronomie- und Verkaufsraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Commercial Room Names</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for hospitality and retail spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN_HLC</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gesundheitsraumbezeichnungen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer medizinische und pflegerische Raeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Healthcare Room Names</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for medical and care spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN_HYG</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hygieneraumbezeichnungen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer Hygiene- und Sanitaerraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Hygiene Room Names</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for sanitary and changing spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN_IND</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Industrieraumbezeichnungen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer Produktions- und Werkraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Industrial Room Names</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for production and workshop spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN_LRN</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Bildungsraumbezeichnungen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer Bildungs- und Lernraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Education Room Names</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for teaching and learning spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN_OUT</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aussenraumbezeichnungen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer als IfcSpace modellierte Aussenraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Outdoor Room Names</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for exterior spaces modeled as IfcSpace.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN_RES</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Wohnraumbezeichnungen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer Wohnnutzungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Residential Room Names</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for residential living spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN_STO</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Lagerraumbezeichnungen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer Lager- und Nebenraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Storage Room Names</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for storage and ancillary spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN_TEC</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Technikraumbezeichnungen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer Technik- und Anlagenraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Technical Room Names</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for building services and plant rooms.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN_VOI</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hohlraumbezeichnungen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer nicht nutzbare Hohl- und Sonderraeume.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Void Room Names</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for non-occupiable void and special spaces.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>RN_WRK</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Arbeitsraumbezeichnungen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Normalisierte Raumbezeichnungen fuer Buero- und Wissensarbeit.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Work Room Names</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Normalized room names for office and knowledge work.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
</tbody>
</table>
</div>
