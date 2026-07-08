# Room name to space activity mapping

Source: [`abstract-room-name-to-space-activity.mapping.ttl`](sources/mapping-room-name-to-activity.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet jede normalisierte Raumbezeichnung einer oder mehreren Raumaktivitaetsklassen zu. Der primaere Aktivitaetscode steht zuerst. Regenerieren mit scripts/generate_room_name_vocabulary.py.
- **description (en):** Maps each normalized room name to one or more building space activity classes. Primary activity code is listed first. Regenerate with scripts/generate_room_name_vocabulary.py.
- **title (de):** Mapping abstrakter Raumbezeichnungen zur Raumaktivitaetsklassifikation
- **title (en):** Abstract room name to space activity mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `rn:RN-CIR-AIS` | `mapsToActivity` | `abs:S-CIR-HOR` |
| `rn:RN-CIR-COR` | `mapsToActivity` | `abs:S-CIR-HOR` |
| `rn:RN-CIR-ELV` | `mapsToActivity` | `abs:S-CIR-VRT-MEC` |
| `rn:RN-CIR-ENT` | `mapsToActivity` | `abs:S-CIR-HOR` |
| `rn:RN-CIR-GAL` | `mapsToActivity` | `abs:M-CIR` |
| `rn:RN-CIR-LND` | `mapsToActivity` | `abs:S-CIR-VRT-MAN` |
| `rn:RN-CIR-LOB` | `mapsToActivity` | `abs:M-CIR` |
| `rn:RN-CIR-LOB` | `mapsToActivity` | `abs:S-CIR-HOR` |
| `rn:RN-CIR-RAM` | `mapsToActivity` | `abs:S-CIR-VRT-MAN` |
| `rn:RN-CIR-STR` | `mapsToActivity` | `abs:S-CIR-VRT-MAN` |
| `rn:RN-CIR-VES` | `mapsToActivity` | `abs:S-CIR-HOR` |
| `rn:RN-COM-BAR` | `mapsToActivity` | `abs:M-COM` |
| `rn:RN-COM-CAF` | `mapsToActivity` | `abs:M-COM` |
| `rn:RN-COM-CUS` | `mapsToActivity` | `abs:M-COM` |
| `rn:RN-COM-EXH` | `mapsToActivity` | `abs:M-COM` |
| `rn:RN-COM-FOD` | `mapsToActivity` | `abs:M-COM` |
| `rn:RN-COM-HTL` | `mapsToActivity` | `abs:M-COM` |
| `rn:RN-COM-KSK` | `mapsToActivity` | `abs:M-COM` |
| `rn:RN-COM-RET` | `mapsToActivity` | `abs:M-COM` |
| `rn:RN-COM-RST` | `mapsToActivity` | `abs:M-COM` |
| `rn:RN-COM-SAL` | `mapsToActivity` | `abs:M-COM` |
| `rn:RN-HLC-EXM` | `mapsToActivity` | `abs:M-HEL` |
| `rn:RN-HLC-IMG` | `mapsToActivity` | `abs:M-HEL` |
| `rn:RN-HLC-LAB` | `mapsToActivity` | `abs:M-HEL` |
| `rn:RN-HLC-NRS` | `mapsToActivity` | `abs:M-HEL` |
| `rn:RN-HLC-OR` | `mapsToActivity` | `abs:M-HEL` |
| `rn:RN-HLC-PAT` | `mapsToActivity` | `abs:M-HEL` |
| `rn:RN-HLC-PRM` | `mapsToActivity` | `abs:M-HEL` |
| `rn:RN-HLC-RCV` | `mapsToActivity` | `abs:M-HEL` |
| `rn:RN-HLC-TRT` | `mapsToActivity` | `abs:M-HEL` |
| `rn:RN-HLC-WTR` | `mapsToActivity` | `abs:M-HEL` |
| `rn:RN-HYG-CHG` | `mapsToActivity` | `abs:S-HYG-SHW` |
| `rn:RN-HYG-GRD` | `mapsToActivity` | `abs:S-HYG-GRD` |
| `rn:RN-HYG-LCK` | `mapsToActivity` | `abs:S-STO-LCK` |
| `rn:RN-HYG-SHW` | `mapsToActivity` | `abs:S-HYG-SHW` |
| `rn:RN-HYG-WC-F` | `mapsToActivity` | `abs:S-HYG-WC-F` |
| `rn:RN-HYG-WC-IV` | `mapsToActivity` | `abs:S-HYG-WC-IV` |
| `rn:RN-HYG-WC-M` | `mapsToActivity` | `abs:S-HYG-WC-M` |
| `rn:RN-HYG-WC-MIX` | `mapsToActivity` | `abs:S-HYG-WC-MIX` |
| `rn:RN-IND-ASM` | `mapsToActivity` | `abs:M-WRK-PRD` |
| `rn:RN-IND-CLN` | `mapsToActivity` | `abs:M-WRK-PRD` |
| `rn:RN-IND-LDK` | `mapsToActivity` | `abs:S-PRK-SVC` |
| `rn:RN-IND-MNT` | `mapsToActivity` | `abs:M-WRK-PRD` |
| `rn:RN-IND-PKG` | `mapsToActivity` | `abs:M-WRK-PRD` |
| `rn:RN-IND-PRD` | `mapsToActivity` | `abs:M-WRK-PRD` |
| `rn:RN-IND-QC` | `mapsToActivity` | `abs:M-WRK-PRD` |
| `rn:RN-IND-WHS` | `mapsToActivity` | `abs:M-WRK-PRD` |
| `rn:RN-IND-WRK` | `mapsToActivity` | `abs:M-WRK-PRD` |
| `rn:RN-IND-YRD` | `mapsToActivity` | `abs:M-WRK-PRD` |
| `rn:RN-LRN-ART` | `mapsToActivity` | `abs:M-LRN` |
| `rn:RN-LRN-AUS` | `mapsToActivity` | `abs:M-LRN` |
| `rn:RN-LRN-CLS` | `mapsToActivity` | `abs:M-LRN` |
| `rn:RN-LRN-CMP` | `mapsToActivity` | `abs:M-LRN` |
| `rn:RN-LRN-LCT` | `mapsToActivity` | `abs:M-LRN` |
| `rn:RN-LRN-LIB` | `mapsToActivity` | `abs:M-LRN` |
| `rn:RN-LRN-SCI` | `mapsToActivity` | `abs:M-LRN` |
| `rn:RN-LRN-SEM` | `mapsToActivity` | `abs:M-LRN` |
| `rn:RN-LRN-STU` | `mapsToActivity` | `abs:M-LRN` |
| `rn:RN-LRN-WRK` | `mapsToActivity` | `abs:M-LRN` |
| `rn:RN-OUT-BLN` | `mapsToActivity` | `abs:O` |
| `rn:RN-OUT-CWK` | `mapsToActivity` | `abs:O-CIR-PED` |
| `rn:RN-OUT-GDN` | `mapsToActivity` | `abs:O-GRN-GDN` |
| `rn:RN-OUT-PAT` | `mapsToActivity` | `abs:O-GRN-REC` |
| `rn:RN-OUT-PLY` | `mapsToActivity` | `abs:O-GRN-REC` |
| `rn:RN-OUT-PRT` | `mapsToActivity` | `abs:O-CIR-PED` |
| `rn:RN-OUT-SPL` | `mapsToActivity` | `abs:O-GRN-REC` |
| `rn:RN-OUT-TRR` | `mapsToActivity` | `abs:O` |
| `rn:RN-RES-APT` | `mapsToActivity` | `abs:M-RES` |
| `rn:RN-RES-BED` | `mapsToActivity` | `abs:M-RES` |
| `rn:RN-RES-BTH` | `mapsToActivity` | `abs:M-RES` |
| `rn:RN-RES-CLO` | `mapsToActivity` | `abs:M-RES` |
| `rn:RN-RES-DIN` | `mapsToActivity` | `abs:M-RES` |
| `rn:RN-RES-ENT` | `mapsToActivity` | `abs:M-RES` |
| `rn:RN-RES-GST` | `mapsToActivity` | `abs:M-RES` |
| `rn:RN-RES-KIT` | `mapsToActivity` | `abs:M-RES` |
| `rn:RN-RES-LAU` | `mapsToActivity` | `abs:M-RES` |
| `rn:RN-RES-LIV` | `mapsToActivity` | `abs:M-RES` |
| `rn:RN-RES-STU` | `mapsToActivity` | `abs:M-RES` |
| `rn:RN-RES-UTL` | `mapsToActivity` | `abs:M-RES` |
| `rn:RN-STO-ARC` | `mapsToActivity` | `abs:S-STO-GEN` |
| `rn:RN-STO-COL` | `mapsToActivity` | `abs:S-STO-GEN` |
| `rn:RN-STO-EQP` | `mapsToActivity` | `abs:S-STO-GEN` |
| `rn:RN-STO-GEN` | `mapsToActivity` | `abs:S-STO-GEN` |
| `rn:RN-STO-JAN` | `mapsToActivity` | `abs:S-STO-GEN` |
| `rn:RN-STO-MAL` | `mapsToActivity` | `abs:S-STO-GEN` |
| `rn:RN-STO-SUP` | `mapsToActivity` | `abs:S-STO-GEN` |
| `rn:RN-STO-ULD` | `mapsToActivity` | `abs:S-STO-GEN` |
| `rn:RN-TEC-BOI` | `mapsToActivity` | `abs:S-TEC` |
| `rn:RN-TEC-CHL` | `mapsToActivity` | `abs:S-TEC` |
| `rn:RN-TEC-COM` | `mapsToActivity` | `abs:S-TEC` |
| `rn:RN-TEC-ELC` | `mapsToActivity` | `abs:S-TEC` |
| `rn:RN-TEC-GEN` | `mapsToActivity` | `abs:S-TEC` |
| `rn:RN-TEC-HVC` | `mapsToActivity` | `abs:S-TEC` |
| `rn:RN-TEC-MMR` | `mapsToActivity` | `abs:S-TEC` |
| `rn:RN-TEC-PMP` | `mapsToActivity` | `abs:S-TEC` |
| `rn:RN-TEC-SPR` | `mapsToActivity` | `abs:S-TEC` |
| `rn:RN-TEC-SRV` | `mapsToActivity` | `abs:S-TEC` |
| `rn:RN-TEC-TRA` | `mapsToActivity` | `abs:S-TEC` |
| `rn:RN-TEC-WST` | `mapsToActivity` | `abs:S-TEC` |
| `rn:RN-VOI-AIR` | `mapsToActivity` | `abs:S-VOI` |
| `rn:RN-VOI-ATR` | `mapsToActivity` | `abs:S-VOI-MLT` |
| `rn:RN-VOI-MCH` | `mapsToActivity` | `abs:S-VOI-PLN` |
| `rn:RN-VOI-PLN` | `mapsToActivity` | `abs:S-VOI-PLN` |
| `rn:RN-VOI-PRK` | `mapsToActivity` | `abs:S-PRK-INT` |
| `rn:RN-VOI-RIS` | `mapsToActivity` | `abs:S-VOI-VRT` |
| `rn:RN-VOI-SHA` | `mapsToActivity` | `abs:S-VOI-VRT` |
| `rn:RN-VOI-STR` | `mapsToActivity` | `abs:S-VOI-STR` |
| `rn:RN-WRK-ADM` | `mapsToActivity` | `abs:M-WRK-KNW` |
| `rn:RN-WRK-BRK` | `mapsToActivity` | `abs:M-WRK-KNW` |
| `rn:RN-WRK-CNF` | `mapsToActivity` | `abs:M-WRK-KNW` |
| `rn:RN-WRK-COW` | `mapsToActivity` | `abs:M-WRK-KNW` |
| `rn:RN-WRK-FCS` | `mapsToActivity` | `abs:M-WRK-KNW` |
| `rn:RN-WRK-MNG` | `mapsToActivity` | `abs:M-WRK-KNW` |
| `rn:RN-WRK-MTG` | `mapsToActivity` | `abs:M-WRK-KNW` |
| `rn:RN-WRK-OAD` | `mapsToActivity` | `abs:M-WRK-KNW` |
| `rn:RN-WRK-OFF` | `mapsToActivity` | `abs:M-WRK-KNW` |
| `rn:RN-WRK-OPN` | `mapsToActivity` | `abs:M-WRK-KNW` |
| `rn:RN-WRK-PHN` | `mapsToActivity` | `abs:M-WRK-KNW` |
| `rn:RN-WRK-REC` | `mapsToActivity` | `abs:M-WRK-KNW` |
