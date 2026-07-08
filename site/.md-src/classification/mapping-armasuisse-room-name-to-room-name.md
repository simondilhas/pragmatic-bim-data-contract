# armasuisse room name to abstract room name mapping

Source: [`armasuisse-room-name-to-abstract-room-name.mapping.ttl`](sources/mapping-armasuisse-room-name-to-room-name.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet armasuisse-Raumlistenbezeichnungen abstrakten BuildingSpaceNameClassification-Konzepten zu. Militaerspezifische Bezeichnungen bleiben absichtlich ungemappt. Regenerieren mit scripts/generate_armasuisse_room_name_mapping.py.
- **description (en):** Maps armasuisse Raumliste labels to abstract BuildingSpaceNameClassification concepts. Military-specific labels are intentionally unmapped. Regenerate with scripts/generate_armasuisse_room_name_mapping.py.
- **title (de):** Mapping armasuisse Raumbezeichnungen zu abstrakten Raumnamen
- **title (en):** armasuisse room name to abstract room name mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `arma:raumliste-aussen-aussenanlagen-sport` | `closeMatch` | `rn:RN-OUT-PLY` |
| `arma:raumliste-aussen-balkon` | `closeMatch` | `rn:RN-OUT-BLN` |
| `arma:raumliste-aussen-gartenanlage` | `closeMatch` | `rn:RN-OUT-GDN` |
| `arma:raumliste-aussen-strasse-weg` | `closeMatch` | `rn:RN-OUT-CWK` |
| `arma:raumliste-aussen-wasserbecken` | `closeMatch` | `rn:RN-OUT-SPL` |
| `arma:raumliste-innen-abstellraum-hausdienst` | `closeMatch` | `rn:RN-STO-JAN` |
| `arma:raumliste-innen-allgemeine-unterrichts-und-bungsr-ume-ohne-festes-gest-hl` | `closeMatch` | `rn:RN-LRN-CLS` |
| `arma:raumliste-innen-archive-sammlungsr-ume` | `closeMatch` | `rn:RN-STO-ARC` |
| `arma:raumliste-innen-archivraum` | `closeMatch` | `rn:RN-STO-ARC` |
| `arma:raumliste-innen-aufzugs-und-f-rderanlagen` | `closeMatch` | `rn:RN-CIR-ELV` |
| `arma:raumliste-innen-ausbildungshallen` | `closeMatch` | `rn:RN-IND-PRD` |
| `arma:raumliste-innen-ausstellungsr-ume` | `closeMatch` | `rn:RN-COM-EXH` |
| `arma:raumliste-innen-b-roarbeit-allgemein` | `closeMatch` | `rn:RN-WRK-OFF` |
| `arma:raumliste-innen-b-ror-ume` | `closeMatch` | `rn:RN-WRK-OFF` |
| `arma:raumliste-innen-b-ror-ume-profi-kdo` | `closeMatch` | `rn:RN-WRK-OFF` |
| `arma:raumliste-innen-b-ror-ume-verwaltung` | `closeMatch` | `rn:RN-WRK-OFF` |
| `arma:raumliste-innen-b-rotechnik` | `closeMatch` | `rn:RN-TEC-COM` |
| `arma:raumliste-innen-b-rotechnik-rechenzentrum` | `closeMatch` | `rn:RN-TEC-SRV` |
| `arma:raumliste-innen-badezimmer` | `closeMatch` | `rn:RN-RES-BTH` |
| `arma:raumliste-innen-behandlungsr-ume` | `closeMatch` | `rn:RN-HLC-TRT` |
| `arma:raumliste-innen-besondere-unterrichts-und-bungsr-ume-ohne-festes-gest-hl` | `closeMatch` | `rn:RN-LRN-SEM` |
| `arma:raumliste-innen-besprechungsr-ume` | `closeMatch` | `rn:RN-WRK-MTG` |
| `arma:raumliste-innen-besprechungsraum` | `closeMatch` | `rn:RN-WRK-MTG` |
| `arma:raumliste-innen-betriebstechnische-anlagen` | `closeMatch` | `rn:RN-TEC-HVC` |
| `arma:raumliste-innen-bettenraum-mit-allgemeiner-ausstattung` | `closeMatch` | `rn:RN-HLC-PAT` |
| `arma:raumliste-innen-bettenraum-mit-besonderer-ausstattung` | `closeMatch` | `rn:RN-HLC-PAT` |
| `arma:raumliste-innen-bibliotheksr-ume` | `closeMatch` | `rn:RN-LRN-LIB` |
| `arma:raumliste-innen-bildung-unterricht-und-kultur-allgemein` | `closeMatch` | `rn:RN-LRN-CLS` |
| `arma:raumliste-innen-cafeteria` | `closeMatch` | `rn:RN-COM-CAF` |
| `arma:raumliste-innen-chemisches-bakteriologisches-labor` | `closeMatch` | `rn:RN-LRN-SCI` |
| `arma:raumliste-innen-duschenraum` | `closeMatch` | `rn:RN-HYG-SHW` |
| `arma:raumliste-innen-duschenraum-z-t2` | `closeMatch` | `rn:RN-HYG-SHW` |
| `arma:raumliste-innen-eingangshalle` | `closeMatch` | `rn:RN-CIR-LOB` |
| `arma:raumliste-innen-eingangshalle-kunden` | `closeMatch` | `rn:RN-CIR-LOB` |
| `arma:raumliste-innen-elektrische-stromversorgung` | `closeMatch` | `rn:RN-TEC-ELC` |
| `arma:raumliste-innen-fahrzeugabstellfl-che` | `closeMatch` | `rn:RN-VOI-PRK` |
| `arma:raumliste-innen-fahrzeugverkehrsfl-che` | `closeMatch` | `rn:RN-VOI-PRK` |
| `arma:raumliste-innen-film-und-h-rs-le` | `closeMatch` | `rn:RN-LRN-LCT` |
| `arma:raumliste-innen-flur-halle-korridore` | `closeMatch` | `rn:RN-CIR-COR` |
| `arma:raumliste-innen-garderoben` | `closeMatch` | `rn:RN-CIR-ENT` |
| `arma:raumliste-innen-garderoben-duschenraum-z-t2` | `closeMatch` | `rn:RN-HYG-SHW` |
| `arma:raumliste-innen-garderoben-zu-duschen` | `closeMatch` | `rn:RN-HYG-SHW` |
| `arma:raumliste-innen-garderoben-zu-duschen-mit-sanit-reinrichtung-z-t2` | `closeMatch` | `rn:RN-HYG-WC-MIX` |
| `arma:raumliste-innen-garderoben-zu-duschen-z-t2` | `closeMatch` | `rn:RN-HYG-SHW` |
| `arma:raumliste-innen-gase-ohne-heizung-und-fl-ssigkeiten` | `closeMatch` | `rn:RN-TEC-BOI` |
| `arma:raumliste-innen-gemeinschaftsr-ume` | `closeMatch` | `rn:RN-WRK-BRK` |
| `arma:raumliste-innen-grossraumb-ro` | `closeMatch` | `rn:RN-WRK-OPN` |
| `arma:raumliste-innen-halle-mit-hochregallager` | `closeMatch` | `rn:RN-IND-WHS` |
| `arma:raumliste-innen-heiz-u-brauchwassererw-rmung` | `closeMatch` | `rn:RN-TEC-BOI` |
| `arma:raumliste-innen-k-che` | `closeMatch` | `rn:RN-RES-KIT` |
| `arma:raumliste-innen-k-chen` | `closeMatch` | `rn:RN-RES-KIT` |
| `arma:raumliste-innen-kiosk` | `closeMatch` | `rn:RN-COM-KSK` |
| `arma:raumliste-innen-konstruktionsraum` | `closeMatch` | `rn:RN-VOI-MCH` |
| `arma:raumliste-innen-kraft-fitnessraum` | `closeMatch` | `rn:RN-LRN-WRK` |
| `arma:raumliste-innen-kraft-fitnessraum-mit-sanit-reinrichtung-z-t1` | `closeMatch` | `rn:RN-HYG-WC-MIX` |
| `arma:raumliste-innen-lagerr-ume` | `closeMatch` | `rn:RN-STO-GEN` |
| `arma:raumliste-innen-lagerr-ume-f-r-gef-hrliche-g-ter` | `closeMatch` | `rn:RN-STO-GEN` |
| `arma:raumliste-innen-lagerr-ume-material-fw-mag` | `closeMatch` | `rn:RN-STO-GEN` |
| `arma:raumliste-innen-lagerr-ume-material-und-ger-te-infra` | `closeMatch` | `rn:RN-STO-GEN` |
| `arma:raumliste-innen-lagerr-ume-material-vor-ort-lager` | `closeMatch` | `rn:RN-STO-GEN` |
| `arma:raumliste-innen-lagerr-ume-munition` | `closeMatch` | `rn:RN-STO-GEN` |
| `arma:raumliste-innen-lagerr-ume-zu-produktionsk-chen-ungek-hlt` | `closeMatch` | `rn:RN-STO-GEN` |
| `arma:raumliste-innen-lagerung-verteilung-und-verkauf-allgemein` | `closeMatch` | `rn:RN-STO-GEN` |
| `arma:raumliste-innen-leseraum` | `closeMatch` | `rn:RN-LRN-STU` |
| `arma:raumliste-innen-milit-rpost-postb-ro` | `closeMatch` | `rn:RN-WRK-OFF` |
| `arma:raumliste-innen-nebenr-ume-zu-produktionsk-chen` | `closeMatch` | `rn:RN-RES-KIT` |
| `arma:raumliste-innen-physikalisches-technisches-labor` | `closeMatch` | `rn:RN-LRN-SCI` |
| `arma:raumliste-innen-produktionsk-chen` | `closeMatch` | `rn:RN-RES-KIT` |
| `arma:raumliste-innen-raum-f-r-operative-eingriffe` | `closeMatch` | `rn:RN-HLC-OR` |
| `arma:raumliste-innen-raum-mit-allgemeiner-medizinischer-ausstattung` | `closeMatch` | `rn:RN-HLC-TRT` |
| `arma:raumliste-innen-raum-mit-besonderer-medizinischer-ausstattung` | `closeMatch` | `rn:RN-HLC-PRM` |
| `arma:raumliste-innen-sanit-rr-ume` | `closeMatch` | `rn:RN-HYG-WC-MIX` |
| `arma:raumliste-innen-schacht-f-r-f-rderanlagen` | `closeMatch` | `rn:RN-CIR-ELV` |
| `arma:raumliste-innen-schlafraum-berufspiloten` | `closeMatch` | `rn:RN-RES-BED` |
| `arma:raumliste-innen-schlafraum-rz-1x-w` | `closeMatch` | `rn:RN-RES-BED` |
| `arma:raumliste-innen-schlafraum-rz-2x-w` | `closeMatch` | `rn:RN-RES-BED` |
| `arma:raumliste-innen-schlafraum-unteroffiziere` | `closeMatch` | `rn:RN-RES-BED` |
| `arma:raumliste-innen-schlafraum-zeitmilit-r-of-h-h-uof` | `closeMatch` | `rn:RN-RES-BED` |
| `arma:raumliste-innen-schlafraum-zeitmilit-r-uof-sdt` | `closeMatch` | `rn:RN-RES-BED` |
| `arma:raumliste-innen-sitzungszimmer` | `closeMatch` | `rn:RN-RES-BED` |
| `arma:raumliste-innen-sonstige-nutzung-allgemein` | `closeMatch` | `rn:RN-WRK-OPN` |
| `arma:raumliste-innen-spezielle-arbeitszone-mit-sanit-ren-einrichtungen` | `closeMatch` | `rn:RN-HYG-WC-MIX` |
| `arma:raumliste-innen-sporthalle` | `closeMatch` | `rn:RN-LRN-AUS` |
| `arma:raumliste-innen-technologisches-labor` | `closeMatch` | `rn:RN-LRN-SCI` |
| `arma:raumliste-innen-terrasse` | `closeMatch` | `rn:RN-OUT-TRR` |
| `arma:raumliste-innen-toilette-t1` | `closeMatch` | `rn:RN-HYG-WC-MIX` |
| `arma:raumliste-innen-toilette-t2` | `closeMatch` | `rn:RN-HYG-WC-MIX` |
| `arma:raumliste-innen-toilette-t3` | `closeMatch` | `rn:RN-HYG-WC-MIX` |
| `arma:raumliste-innen-toilette-z-t2` | `closeMatch` | `rn:RN-HYG-WC-MIX` |
| `arma:raumliste-innen-treppen` | `closeMatch` | `rn:RN-CIR-STR` |
| `arma:raumliste-innen-umkleideraum` | `closeMatch` | `rn:RN-HYG-SHW` |
| `arma:raumliste-innen-unterrichts-und-bungsr-ume-mit-festem-gest-hl` | `closeMatch` | `rn:RN-LRN-CLS` |
| `arma:raumliste-innen-vorraum` | `closeMatch` | `rn:RN-CIR-VES` |
| `arma:raumliste-innen-warmwasserversorgung` | `closeMatch` | `rn:RN-TEC-PMP` |
| `arma:raumliste-innen-waschk-che` | `closeMatch` | `rn:RN-RES-LAU` |
| `arma:raumliste-innen-wc-duschenraum` | `closeMatch` | `rn:RN-HYG-WC-MIX` |
| `arma:raumliste-innen-wc-duschenraum-z-t2` | `closeMatch` | `rn:RN-HYG-WC-MIX` |
| `arma:raumliste-innen-wc-waschraum` | `closeMatch` | `rn:RN-HYG-WC-MIX` |
| `arma:raumliste-innen-wc-waschraum-z-t2` | `closeMatch` | `rn:RN-HYG-WC-MIX` |
| `arma:raumliste-innen-werkhallen` | `closeMatch` | `rn:RN-IND-PRD` |
| `arma:raumliste-innen-werkst-tten` | `closeMatch` | `rn:RN-IND-WRK` |
| `arma:raumliste-innen-wohnr-ume-schlafr-ume` | `closeMatch` | `rn:RN-RES-BED` |
| `arma:raumliste-innen-wohnzimmer` | `closeMatch` | `rn:RN-RES-BED` |
| `arma:raumliste-innen-zelle` | `closeMatch` | `rn:RN-RES-BED` |
