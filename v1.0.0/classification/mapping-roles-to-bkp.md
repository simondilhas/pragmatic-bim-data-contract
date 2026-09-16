# Abstract roles to BKP mapping

Source: [`abstract-roles-to-bkp.mapping.ttl`](sources/mapping-roles-to-bkp.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet Blattkonzepte der abstract-roles (SKOS: Gruppen Eigentümer / Mieter / Planer / Unternehmer) BKP-Kostenpositionen zu. Disziplin-Honorare wiederholen sich pro Phase (091/191/…); Architekt listet alle Architekt-IRIs dieser BKP-Datei. Site-Manager liegt unter Planer (Bauüberwachung); BKP verknüpft mit Büro Bauleitung (133) unter Gemeinsame Baustelleneinrichtung. Projektleitung und BIM-Koordination werden in Ausschreibungen oft als Spezialisten-Honorar (096 …) geführt; Verknüpfungen sind relatedMatch. Disambiguierung: Der BKP ist bewusst nicht eindeutig, dieselbe Leistung kann je nach Bauteil, Phase und Vergabe auf verschiedenen Positionen liegen (z. B. 175 Grundwasserabdichtungen gegenueber 225.3 Spezielle Feuchtigkeitsabdichtungen; Gruppe 14 Anpassungen an bestehende Bauten spiegelt Gruppe 2 im Umbau; Gruppe 44 Installationen spiegelt 23-26 in der Umgebung). Sind zwei Positionen gleichwertig, stehen beide als skos:closeMatch; skos:relatedMatch bezeichnet eine sekundaere oder benachbarte Position, keine gleichwertige Alternative.
- **description (en):** Maps leaf concepts in abstract-roles (SKOS: owner / tenant / planner / contractor groups) to BKP cost lines. Discipline Honorare repeat per phase (091/191/…); architect lists every Architekt IRI in this BKP file. Site manager is under planner (construction supervision); BKP links it to Buero Bauleitung (133), i.e. the Bauleitung office under Gemeinsame Baustelleneinrichtung. Project management and BIM coordination often appear as Spezialisten-Honorar (096 …) in tenders; those links are relatedMatch, not equivalence. Disambiguation: BKP is deliberately not bijective, so the same product can be booked under different cost lines depending on building part, phase and awarded trade (e.g. 175 Grundwasserabdichtungen against 225.3 Spezielle Feuchtigkeitsabdichtungen; group 14 Anpassungen an bestehende Bauten mirrors group 2 for refurbishment; group 44 Installationen mirrors 23-26 for site works). Where two positions are equally valid, both are given as skos:closeMatch; skos:relatedMatch marks a secondary or adjacent line, not an equal alternative.
- **title (de):** Mapping abstrakter Workflow-Rollen nach BKP
- **title (en):** Abstract workflow roles to BKP mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `role:aec.architect` | `closeMatch` | `bkp:091` |
| `role:aec.architect` | `closeMatch` | `bkp:191` |
| `role:aec.architect` | `closeMatch` | `bkp:291` |
| `role:aec.architect` | `closeMatch` | `bkp:391` |
| `role:aec.architect` | `closeMatch` | `bkp:491` |
| `role:aec.architect` | `closeMatch` | `bkp:591` |
| `role:aec.architect` | `closeMatch` | `bkp:991` |
| `role:aec.bim-coordinator` | `relatedMatch` | `bkp:096` |
| `role:aec.bim-coordinator` | `relatedMatch` | `bkp:196` |
| `role:aec.bim-coordinator` | `relatedMatch` | `bkp:296` |
| `role:aec.bim-coordinator` | `relatedMatch` | `bkp:396` |
| `role:aec.bim-coordinator` | `relatedMatch` | `bkp:496` |
| `role:aec.bim-coordinator` | `relatedMatch` | `bkp:596` |
| `role:aec.bim-coordinator` | `relatedMatch` | `bkp:996` |
| `role:aec.bim-manager` | `relatedMatch` | `bkp:096` |
| `role:aec.bim-manager` | `relatedMatch` | `bkp:196` |
| `role:aec.bim-manager` | `relatedMatch` | `bkp:296` |
| `role:aec.bim-manager` | `relatedMatch` | `bkp:396` |
| `role:aec.bim-manager` | `relatedMatch` | `bkp:496` |
| `role:aec.bim-manager` | `relatedMatch` | `bkp:596` |
| `role:aec.bim-manager` | `relatedMatch` | `bkp:996` |
| `role:aec.client` | `relatedMatch` | `bkp:55` |
| `role:aec.developer` | `relatedMatch` | `bkp:55` |
| `role:aec.electrical-engineer` | `closeMatch` | `bkp:093` |
| `role:aec.electrical-engineer` | `closeMatch` | `bkp:193` |
| `role:aec.electrical-engineer` | `closeMatch` | `bkp:293` |
| `role:aec.electrical-engineer` | `closeMatch` | `bkp:393` |
| `role:aec.electrical-engineer` | `closeMatch` | `bkp:493` |
| `role:aec.electrical-engineer` | `closeMatch` | `bkp:593` |
| `role:aec.electrical-engineer` | `closeMatch` | `bkp:993` |
| `role:aec.heating-engineer` | `relatedMatch` | `bkp:094` |
| `role:aec.heating-engineer` | `relatedMatch` | `bkp:194` |
| `role:aec.heating-engineer` | `relatedMatch` | `bkp:294` |
| `role:aec.heating-engineer` | `relatedMatch` | `bkp:394` |
| `role:aec.heating-engineer` | `relatedMatch` | `bkp:494` |
| `role:aec.heating-engineer` | `relatedMatch` | `bkp:594` |
| `role:aec.owner` | `relatedMatch` | `bkp:55` |
| `role:aec.plumbing-engineer` | `closeMatch` | `bkp:095` |
| `role:aec.plumbing-engineer` | `closeMatch` | `bkp:195` |
| `role:aec.plumbing-engineer` | `closeMatch` | `bkp:295` |
| `role:aec.plumbing-engineer` | `closeMatch` | `bkp:395` |
| `role:aec.plumbing-engineer` | `closeMatch` | `bkp:495` |
| `role:aec.plumbing-engineer` | `closeMatch` | `bkp:595` |
| `role:aec.project-lead` | `relatedMatch` | `bkp:096` |
| `role:aec.project-lead` | `relatedMatch` | `bkp:196` |
| `role:aec.project-lead` | `relatedMatch` | `bkp:296` |
| `role:aec.project-lead` | `relatedMatch` | `bkp:396` |
| `role:aec.project-lead` | `relatedMatch` | `bkp:496` |
| `role:aec.project-lead` | `relatedMatch` | `bkp:596` |
| `role:aec.project-lead` | `relatedMatch` | `bkp:996` |
| `role:aec.project-manager` | `relatedMatch` | `bkp:096` |
| `role:aec.project-manager` | `relatedMatch` | `bkp:196` |
| `role:aec.project-manager` | `relatedMatch` | `bkp:296` |
| `role:aec.project-manager` | `relatedMatch` | `bkp:396` |
| `role:aec.project-manager` | `relatedMatch` | `bkp:496` |
| `role:aec.project-manager` | `relatedMatch` | `bkp:596` |
| `role:aec.project-manager` | `relatedMatch` | `bkp:996` |
| `role:aec.site-manager` | `relatedMatch` | `bkp:133` |
| `role:aec.structural-engineer` | `closeMatch` | `bkp:092` |
| `role:aec.structural-engineer` | `closeMatch` | `bkp:192` |
| `role:aec.structural-engineer` | `closeMatch` | `bkp:292` |
| `role:aec.structural-engineer` | `closeMatch` | `bkp:392` |
| `role:aec.structural-engineer` | `closeMatch` | `bkp:492` |
| `role:aec.structural-engineer` | `closeMatch` | `bkp:592` |
| `role:aec.sustainability-consultant` | `relatedMatch` | `bkp:096` |
| `role:aec.sustainability-consultant` | `relatedMatch` | `bkp:196` |
| `role:aec.sustainability-consultant` | `relatedMatch` | `bkp:296` |
| `role:aec.sustainability-consultant` | `relatedMatch` | `bkp:396` |
| `role:aec.sustainability-consultant` | `relatedMatch` | `bkp:496` |
| `role:aec.sustainability-consultant` | `relatedMatch` | `bkp:596` |
| `role:aec.sustainability-consultant` | `relatedMatch` | `bkp:996` |
| `role:aec.ventilation-engineer` | `relatedMatch` | `bkp:094` |
| `role:aec.ventilation-engineer` | `relatedMatch` | `bkp:194` |
| `role:aec.ventilation-engineer` | `relatedMatch` | `bkp:294` |
| `role:aec.ventilation-engineer` | `relatedMatch` | `bkp:394` |
| `role:aec.ventilation-engineer` | `relatedMatch` | `bkp:494` |
| `role:aec.ventilation-engineer` | `relatedMatch` | `bkp:594` |
