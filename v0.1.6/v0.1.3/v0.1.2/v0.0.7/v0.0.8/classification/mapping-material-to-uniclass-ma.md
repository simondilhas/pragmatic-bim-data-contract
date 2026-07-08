# Abstract material to Uniclass Ma mapping

Source: [`abstract-material-to-uniclass-ma.mapping.ttl`](sources/mapping-material-to-uniclass-ma.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Operatives 1:n-Mapping von abstrakten dominanten Materialklassen auf Uniclass-2015-Ma-Konzepte fuer grobe Nachhaltigkeitsberechnungen. Verwendet skos:broadMatch, da abstrakte Klassen mehrere Ma-Blattkonzepte umfassen.
- **description (en):** Operational 1:n mapping from abstract dominant-material classes to Uniclass 2015 Ma concepts for rough sustainability workflows. Uses skos:broadMatch because abstract classes subsume multiple Ma leaves.
- **title (de):** Mapping abstrakter Materialklassifikation nach Uniclass Ma
- **title (en):** Abstract material classification to Uniclass Ma mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `mat:MAT-CMP` | `broadMatch` | `ma:Ma-20` |
| `mat:MAT-CONC` | `broadMatch` | `ma:Ma-40-19` |
| `mat:MAT-GLS` | `broadMatch` | `ma:Ma-40-35` |
| `mat:MAT-GYP` | `broadMatch` | `ma:Ma-40-15` |
| `mat:MAT-GYP` | `broadMatch` | `ma:Ma-40-15-35` |
| `mat:MAT-INS` | `broadMatch` | `ma:Ma-40-35-34` |
| `mat:MAT-INS` | `broadMatch` | `ma:Ma-40-84-53` |
| `mat:MAT-INS` | `broadMatch` | `ma:Ma-60-65-85-27` |
| `mat:MAT-INS` | `broadMatch` | `ma:Ma-60-65-85-28` |
| `mat:MAT-MET` | `broadMatch` | `ma:Ma-40-52` |
| `mat:MAT-MET` | `broadMatch` | `ma:Ma-40-52-83` |
| `mat:MAT-MSN` | `broadMatch` | `ma:Ma-20-13` |
| `mat:MAT-MSN` | `broadMatch` | `ma:Ma-40-84` |
| `mat:MAT-PLA` | `broadMatch` | `ma:Ma-60-65` |
| `mat:MAT-WOD` | `broadMatch` | `ma:Ma-60-97` |
