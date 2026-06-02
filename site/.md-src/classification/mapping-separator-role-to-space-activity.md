# Separator role to space activity mapping

Source: [`separator-role-to-space-activity.mapping.ttl`](sources/mapping-separator-role-to-space-activity.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Start-relatedMatch-Verknuepfungen von topologischen Trennwand- und Trenndeckenrollen zu angrenzenden Raumaktivitaetskonzepten. Prioritaetsregeln bei mehreren Raumtypen (z. B. M-RES plus S-CIR-HOR ergibt W-UNT) gehoeren in PBS-Regeln, nicht in dieses Mapping.
- **description (en):** Starter relatedMatch links from topological separator wall and slab roles to adjacent space activity concepts. Inference priority when multiple space types meet (for example M-RES plus S-CIR-HOR assigning W-UNT) belongs in PBS rules, not in this mapping.
- **title (de):** Mapping von Trennelementrollen zur Gebaeude-Raum-Aktivitaetsklassifikation
- **title (en):** Separator role to Building Space Activity Classification mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `slab:L-EXT` | `relatedMatch` | `space:O` |
| `slab:L-INT-CIR` | `relatedMatch` | `space:S-CIR-HOR` |
| `slab:L-INT-CIR` | `relatedMatch` | `space:S-CIR-VRT` |
| `slab:L-INT-GRD` | `relatedMatch` | `space:S-PRK-INT` |
| `slab:L-INT-UNT` | `relatedMatch` | `space:M` |
| `wall:W-EXT` | `relatedMatch` | `space:O` |
| `wall:W-INT-CIR-HOR` | `relatedMatch` | `space:S-CIR-HOR` |
| `wall:W-INT-CIR-VRT` | `relatedMatch` | `space:S-CIR-VRT` |
| `wall:W-INT-GRD` | `relatedMatch` | `space:S-PRK-INT` |
| `wall:W-INT-SVC` | `relatedMatch` | `space:S-TEC` |
| `wall:W-INT-SVC` | `relatedMatch` | `space:S-VOI` |
| `wall:W-INT-SVC` | `relatedMatch` | `space:S-VOI-MLT` |
| `wall:W-INT-SVC` | `relatedMatch` | `space:S-VOI-PLN` |
| `wall:W-INT-SVC` | `relatedMatch` | `space:S-VOI-STR` |
| `wall:W-INT-SVC` | `relatedMatch` | `space:S-VOI-VRT` |
| `wall:W-INT-UNT` | `relatedMatch` | `space:M` |
