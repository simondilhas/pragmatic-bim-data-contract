# Abstract domain classification

Source: [`domain-classification.skos.ttl`](sources/domain.ttl)

## Scheme

- **description (de):** Fachbereiche für BIM-Liefergegenstände (Architektur, Tragwerk, Gebäudetechnik). Dateinamen-Präfix in `{Projektnumber}_{DOMAIN}-{MODEL}_{Userdefined_text}.{ext}`.
- **description (en):** Discipline domains for BIM deliverables (architecture, structural, MEP). File-name prefix in `{Projektnumber}_{DOMAIN}-{MODEL}_{Userdefined_text}.{ext}`.
- **description (fr):** Domaines disciplinaires pour les livrables BIM (architecture, structure, CVC/sanitaire). Préfixe de nom de fichier dans `{Projektnumber}_{DOMAIN}-{MODEL}_{Userdefined_text}.{ext}`.
- **description (it):** Domini disciplinari per i deliverable BIM (architettura, struttura, impianti). Prefisso del nome file in `{Projektnumber}_{DOMAIN}-{MODEL}_{Userdefined_text}.{ext}`.
- **prefLabel (de):** Abstrakte Fachbereich-Klassifikation
- **prefLabel (en):** Abstract domain classification
- **prefLabel (fr):** Classification abstraite des domaines
- **prefLabel (it):** Classificazione astratta dei domini
- **title (en):** Abstract domain classification

## Concepts

<div class="pbs-vocab-concepts" data-default-lang="en" data-active-lang="en">
<div class="pbs-lang-switcher" role="group" aria-label="Language">
<button type="button" class="pbs-lang-btn" data-lang="de">DE</button>
<button type="button" class="pbs-lang-btn" data-lang="en">EN</button>
<button type="button" class="pbs-lang-btn" data-lang="fr">FR</button>
<button type="button" class="pbs-lang-btn" data-lang="it">IT</button>
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
<th class="pbs-lang-col" data-lang="fr" data-field="label">Label</th>
<th class="pbs-lang-col" data-lang="fr" data-field="definition">Definition</th>
<th class="pbs-lang-col" data-lang="fr" data-field="scope_note">Scope note</th>
<th class="pbs-lang-col" data-lang="it" data-field="label">Label</th>
<th class="pbs-lang-col" data-lang="it" data-field="definition">Definition</th>
<th class="pbs-lang-col" data-lang="it" data-field="scope_note">Scope note</th>
</tr>
</thead>
<tbody>
<tr>
<td>ARC</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Architektur</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Fachbereich Architektur — Gebäudeentwurf, Räume, Hülle, Ausbau, Möblierung, Laboreinrichtung, Landschaft und räumlicher Kontext.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Dateinamen-Fachbereich ARC, z. B. `{Projektnumber}_ARC-ARC_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Architecture</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Architecture discipline — building design, spaces, envelope, fit-out, furniture, laboratory fit-out, landscape, and spatial context models.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">File-name domain token ARC, for example `{Projektnumber}_ARC-ARC_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="label">Architecture</td>
<td class="pbs-lang-col" data-lang="fr" data-field="definition">Discipline architecture — conception du bâtiment, locaux, enveloppe, aménagement, mobilier, laboratoires, paysage et contexte spatial.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="scope_note">Jeton de domaine ARC dans le nom de fichier, p. ex. `{Projektnumber}_ARC-ARC_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="it" data-field="label">Architettura</td>
<td class="pbs-lang-col" data-lang="it" data-field="definition">Disciplina architettura — progettazione dell&#x27;edificio, spazi, involucro, finiture, arredi, laboratori, paesaggio e contesto spaziale.</td>
<td class="pbs-lang-col" data-lang="it" data-field="scope_note">Token di dominio ARC nel nome file, ad es. `{Projektnumber}_ARC-ARC_{Userdefined_text}.{ext}`.</td>
</tr>
<tr>
<td>MEP</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gebäudetechnik</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Fachbereich Gebäudetechnik — Heizung, Kühlung, Lüftung, Sanitär und Grundleitungen. Elektromodelle sind in diesem Vokabular nicht enthalten.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Dateinamen-Fachbereich MEP, z. B. `{Projektnumber}_MEP-HEI_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">MEP</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Building services discipline — heating, cooling, ventilation, plumbing, and underground drainage models. Electrical models are not in this vocabulary.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">File-name domain token MEP, for example `{Projektnumber}_MEP-HEI_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="label">Technique du bâtiment</td>
<td class="pbs-lang-col" data-lang="fr" data-field="definition">Discipline technique du bâtiment — chauffage, froid, ventilation, sanitaire et collecteurs enterrés. Les maquettes électriques ne figurent pas dans ce vocabulaire.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="scope_note">Jeton de domaine MEP dans le nom de fichier, p. ex. `{Projektnumber}_MEP-HEI_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="it" data-field="label">Impianti</td>
<td class="pbs-lang-col" data-lang="it" data-field="definition">Disciplina impianti — riscaldamento, raffrescamento, ventilazione, sanitari e condotte interrate. I modelli elettrici non sono in questo vocabolario.</td>
<td class="pbs-lang-col" data-lang="it" data-field="scope_note">Token di dominio MEP nel nome file, ad es. `{Projektnumber}_MEP-HEI_{Userdefined_text}.{ext}`.</td>
</tr>
<tr>
<td>STR</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Tragwerk</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Fachbereich Tragwerk — Stahlbeton, Stahl und Holz, Bewehrung, Baugrubensicherung und Aushub.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Dateinamen-Fachbereich STR, z. B. `{Projektnumber}_STR-BET_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Structural</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Structural discipline — concrete, steel, and timber load-bearing models, reinforcement, excavation-pit support, and earthworks.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">File-name domain token STR, for example `{Projektnumber}_STR-BET_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="label">Structure</td>
<td class="pbs-lang-col" data-lang="fr" data-field="definition">Discipline structure — béton armé, acier et bois, armatures, soutènement de fouille et terrassement.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="scope_note">Jeton de domaine STR dans le nom de fichier, p. ex. `{Projektnumber}_STR-BET_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="it" data-field="label">Struttura</td>
<td class="pbs-lang-col" data-lang="it" data-field="definition">Disciplina struttura — calcestruzzo, acciaio e legno, armatura, opere di sostegno e scavi.</td>
<td class="pbs-lang-col" data-lang="it" data-field="scope_note">Token di dominio STR nel nome file, ad es. `{Projektnumber}_STR-BET_{Userdefined_text}.{ext}`.</td>
</tr>
</tbody>
</table>
</div>
