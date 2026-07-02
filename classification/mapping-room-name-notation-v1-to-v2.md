# Room name notation v1 to v2 mapping

Source: [`room-name-notation-v1-to-v2.mapping.ttl`](sources/mapping-room-name-notation-v1-to-v2.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet mnemonische v1-Notation (RN-RES-BED) numerischen v2-Blattcodes (RN-01-10-01) zu. RN-CIR-AIS wird durch RN-03-10-01 (Flur) ersetzt. Regenerieren mit scripts/generate_room_name_vocabulary.py.
- **description (en):** Maps mnemonic v1 notation codes (RN-RES-BED) to numeric v2 leaf codes (RN-01-10-01). RN-CIR-AIS is superseded by RN-03-10-01 (Corridor). Regenerate with scripts/generate_room_name_vocabulary.py.
- **title (de):** Mapping Raumnamen-Notation v1 nach v2
- **title (en):** Room name notation v1 to v2 mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `v1:rn-cir-ais` | `exactMatch` | `rn:RN-CIR-COR` |
| `v1:rn-cir-cor` | `exactMatch` | `rn:RN-CIR-COR` |
| `v1:rn-cir-elv` | `exactMatch` | `rn:RN-CIR-ELV` |
| `v1:rn-cir-ent` | `exactMatch` | `rn:RN-CIR-ENT` |
| `v1:rn-cir-gal` | `exactMatch` | `rn:RN-CIR-GAL` |
| `v1:rn-cir-lnd` | `exactMatch` | `rn:RN-CIR-LND` |
| `v1:rn-cir-lob` | `exactMatch` | `rn:RN-CIR-LOB` |
| `v1:rn-cir-ram` | `exactMatch` | `rn:RN-CIR-RAM` |
| `v1:rn-cir-str` | `exactMatch` | `rn:RN-CIR-STR` |
| `v1:rn-cir-ves` | `exactMatch` | `rn:RN-CIR-VES` |
| `v1:rn-com-bar` | `exactMatch` | `rn:RN-COM-BAR` |
| `v1:rn-com-caf` | `exactMatch` | `rn:RN-COM-CAF` |
| `v1:rn-com-cus` | `exactMatch` | `rn:RN-COM-CUS` |
| `v1:rn-com-exh` | `exactMatch` | `rn:RN-COM-EXH` |
| `v1:rn-com-fod` | `exactMatch` | `rn:RN-COM-FOD` |
| `v1:rn-com-htl` | `exactMatch` | `rn:RN-COM-HTL` |
| `v1:rn-com-ksk` | `exactMatch` | `rn:RN-COM-KSK` |
| `v1:rn-com-ret` | `exactMatch` | `rn:RN-COM-RET` |
| `v1:rn-com-rst` | `exactMatch` | `rn:RN-COM-RST` |
| `v1:rn-com-sal` | `exactMatch` | `rn:RN-COM-SAL` |
| `v1:rn-hlc-exm` | `exactMatch` | `rn:RN-HLC-EXM` |
| `v1:rn-hlc-img` | `exactMatch` | `rn:RN-HLC-IMG` |
| `v1:rn-hlc-lab` | `exactMatch` | `rn:RN-HLC-LAB` |
| `v1:rn-hlc-nrs` | `exactMatch` | `rn:RN-HLC-NRS` |
| `v1:rn-hlc-or` | `exactMatch` | `rn:RN-HLC-OR` |
| `v1:rn-hlc-pat` | `exactMatch` | `rn:RN-HLC-PAT` |
| `v1:rn-hlc-prm` | `exactMatch` | `rn:RN-HLC-PRM` |
| `v1:rn-hlc-rcv` | `exactMatch` | `rn:RN-HLC-RCV` |
| `v1:rn-hlc-trt` | `exactMatch` | `rn:RN-HLC-TRT` |
| `v1:rn-hlc-wtr` | `exactMatch` | `rn:RN-HLC-WTR` |
| `v1:rn-hyg-chg` | `exactMatch` | `rn:RN-HYG-CHG` |
| `v1:rn-hyg-grd` | `exactMatch` | `rn:RN-HYG-GRD` |
| `v1:rn-hyg-lck` | `exactMatch` | `rn:RN-HYG-LCK` |
| `v1:rn-hyg-shw` | `exactMatch` | `rn:RN-HYG-SHW` |
| `v1:rn-hyg-wc-f` | `exactMatch` | `rn:RN-HYG-WC-F` |
| `v1:rn-hyg-wc-iv` | `exactMatch` | `rn:RN-HYG-WC-IV` |
| `v1:rn-hyg-wc-m` | `exactMatch` | `rn:RN-HYG-WC-M` |
| `v1:rn-hyg-wc-mix` | `exactMatch` | `rn:RN-HYG-WC-MIX` |
| `v1:rn-ind-asm` | `exactMatch` | `rn:RN-IND-ASM` |
| `v1:rn-ind-cln` | `exactMatch` | `rn:RN-IND-CLN` |
| `v1:rn-ind-ldk` | `exactMatch` | `rn:RN-IND-LDK` |
| `v1:rn-ind-mnt` | `exactMatch` | `rn:RN-IND-MNT` |
| `v1:rn-ind-pkg` | `exactMatch` | `rn:RN-IND-PKG` |
| `v1:rn-ind-prd` | `exactMatch` | `rn:RN-IND-PRD` |
| `v1:rn-ind-qc` | `exactMatch` | `rn:RN-IND-QC` |
| `v1:rn-ind-whs` | `exactMatch` | `rn:RN-IND-WHS` |
| `v1:rn-ind-wrk` | `exactMatch` | `rn:RN-IND-WRK` |
| `v1:rn-ind-yrd` | `exactMatch` | `rn:RN-IND-YRD` |
| `v1:rn-lrn-art` | `exactMatch` | `rn:RN-LRN-ART` |
| `v1:rn-lrn-aus` | `exactMatch` | `rn:RN-LRN-AUS` |
| `v1:rn-lrn-cls` | `exactMatch` | `rn:RN-LRN-CLS` |
| `v1:rn-lrn-cmp` | `exactMatch` | `rn:RN-LRN-CMP` |
| `v1:rn-lrn-lct` | `exactMatch` | `rn:RN-LRN-LCT` |
| `v1:rn-lrn-lib` | `exactMatch` | `rn:RN-LRN-LIB` |
| `v1:rn-lrn-sci` | `exactMatch` | `rn:RN-LRN-SCI` |
| `v1:rn-lrn-sem` | `exactMatch` | `rn:RN-LRN-SEM` |
| `v1:rn-lrn-stu` | `exactMatch` | `rn:RN-LRN-STU` |
| `v1:rn-lrn-wrk` | `exactMatch` | `rn:RN-LRN-WRK` |
| `v1:rn-out-bln` | `exactMatch` | `rn:RN-OUT-BLN` |
| `v1:rn-out-cwk` | `exactMatch` | `rn:RN-OUT-CWK` |
| `v1:rn-out-gdn` | `exactMatch` | `rn:RN-OUT-GDN` |
| `v1:rn-out-pat` | `exactMatch` | `rn:RN-OUT-PAT` |
| `v1:rn-out-ply` | `exactMatch` | `rn:RN-OUT-PLY` |
| `v1:rn-out-prt` | `exactMatch` | `rn:RN-OUT-PRT` |
| `v1:rn-out-spl` | `exactMatch` | `rn:RN-OUT-SPL` |
| `v1:rn-out-trr` | `exactMatch` | `rn:RN-OUT-TRR` |
| `v1:rn-res-apt` | `exactMatch` | `rn:RN-RES-APT` |
| `v1:rn-res-bed` | `exactMatch` | `rn:RN-RES-BED` |
| `v1:rn-res-bth` | `exactMatch` | `rn:RN-RES-BTH` |
| `v1:rn-res-clo` | `exactMatch` | `rn:RN-RES-CLO` |
| `v1:rn-res-din` | `exactMatch` | `rn:RN-RES-DIN` |
| `v1:rn-res-ent` | `exactMatch` | `rn:RN-RES-ENT` |
| `v1:rn-res-gst` | `exactMatch` | `rn:RN-RES-GST` |
| `v1:rn-res-kit` | `exactMatch` | `rn:RN-RES-KIT` |
| `v1:rn-res-lau` | `exactMatch` | `rn:RN-RES-LAU` |
| `v1:rn-res-liv` | `exactMatch` | `rn:RN-RES-LIV` |
| `v1:rn-res-stu` | `exactMatch` | `rn:RN-RES-STU` |
| `v1:rn-res-utl` | `exactMatch` | `rn:RN-RES-UTL` |
| `v1:rn-sto-arc` | `exactMatch` | `rn:RN-STO-ARC` |
| `v1:rn-sto-col` | `exactMatch` | `rn:RN-STO-COL` |
| `v1:rn-sto-eqp` | `exactMatch` | `rn:RN-STO-EQP` |
| `v1:rn-sto-gen` | `exactMatch` | `rn:RN-STO-GEN` |
| `v1:rn-sto-jan` | `exactMatch` | `rn:RN-STO-JAN` |
| `v1:rn-sto-mal` | `exactMatch` | `rn:RN-STO-MAL` |
| `v1:rn-sto-sup` | `exactMatch` | `rn:RN-STO-SUP` |
| `v1:rn-sto-uld` | `exactMatch` | `rn:RN-STO-ULD` |
| `v1:rn-tec-boi` | `exactMatch` | `rn:RN-TEC-BOI` |
| `v1:rn-tec-chl` | `exactMatch` | `rn:RN-TEC-CHL` |
| `v1:rn-tec-com` | `exactMatch` | `rn:RN-TEC-COM` |
| `v1:rn-tec-elc` | `exactMatch` | `rn:RN-TEC-ELC` |
| `v1:rn-tec-gen` | `exactMatch` | `rn:RN-TEC-GEN` |
| `v1:rn-tec-hvc` | `exactMatch` | `rn:RN-TEC-HVC` |
| `v1:rn-tec-mmr` | `exactMatch` | `rn:RN-TEC-MMR` |
| `v1:rn-tec-pmp` | `exactMatch` | `rn:RN-TEC-PMP` |
| `v1:rn-tec-spr` | `exactMatch` | `rn:RN-TEC-SPR` |
| `v1:rn-tec-srv` | `exactMatch` | `rn:RN-TEC-SRV` |
| `v1:rn-tec-tra` | `exactMatch` | `rn:RN-TEC-TRA` |
| `v1:rn-tec-wst` | `exactMatch` | `rn:RN-TEC-WST` |
| `v1:rn-voi-air` | `exactMatch` | `rn:RN-VOI-AIR` |
| `v1:rn-voi-atr` | `exactMatch` | `rn:RN-VOI-ATR` |
| `v1:rn-voi-mch` | `exactMatch` | `rn:RN-VOI-MCH` |
| `v1:rn-voi-pln` | `exactMatch` | `rn:RN-VOI-PLN` |
| `v1:rn-voi-prk` | `exactMatch` | `rn:RN-VOI-PRK` |
| `v1:rn-voi-ris` | `exactMatch` | `rn:RN-VOI-RIS` |
| `v1:rn-voi-sha` | `exactMatch` | `rn:RN-VOI-SHA` |
| `v1:rn-voi-str` | `exactMatch` | `rn:RN-VOI-STR` |
| `v1:rn-wrk-adm` | `exactMatch` | `rn:RN-WRK-ADM` |
| `v1:rn-wrk-brk` | `exactMatch` | `rn:RN-WRK-BRK` |
| `v1:rn-wrk-cnf` | `exactMatch` | `rn:RN-WRK-CNF` |
| `v1:rn-wrk-cow` | `exactMatch` | `rn:RN-WRK-COW` |
| `v1:rn-wrk-fcs` | `exactMatch` | `rn:RN-WRK-FCS` |
| `v1:rn-wrk-mng` | `exactMatch` | `rn:RN-WRK-MNG` |
| `v1:rn-wrk-mtg` | `exactMatch` | `rn:RN-WRK-MTG` |
| `v1:rn-wrk-oad` | `exactMatch` | `rn:RN-WRK-OAD` |
| `v1:rn-wrk-off` | `exactMatch` | `rn:RN-WRK-OFF` |
| `v1:rn-wrk-opn` | `exactMatch` | `rn:RN-WRK-OPN` |
| `v1:rn-wrk-phn` | `exactMatch` | `rn:RN-WRK-PHN` |
| `v1:rn-wrk-rec` | `exactMatch` | `rn:RN-WRK-REC` |
