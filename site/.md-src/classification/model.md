# Abstract model classification

Source: [`model-classification.skos.ttl`](sources/model.ttl)

## Scheme

- **description (de):** BIM-Fachmodelltypen zur Klassifikation von Liefergegenständen. Notation ist das Modell-Token in `{Projektnumber}_{DOMAIN}-{MODEL}_{Userdefined_text}.{ext}`. Fachbereich-Zuordnung im Mapping Modell zu Fachbereich.
- **description (en):** BIM discipline-model types (Fachmodelle) for deliverable classification. Notation is the model token in `{Projektnumber}_{DOMAIN}-{MODEL}_{Userdefined_text}.{ext}`. Domain membership is in the model-to-domain mapping.
- **description (fr):** Types de maquettes disciplinaires BIM pour classer les livrables. La notation est le jeton de maquette dans `{Projektnumber}_{DOMAIN}-{MODEL}_{Userdefined_text}.{ext}`. L'appartenance au domaine est dans le mapping maquette vers domaine.
- **description (it):** Tipi di modello disciplinare BIM per classificare i deliverable. La notazione è il token del modello in `{Projektnumber}_{DOMAIN}-{MODEL}_{Userdefined_text}.{ext}`. L'appartenenza al dominio è nel mapping modello-dominio.
- **prefLabel (de):** Abstrakte Fachmodell-Klassifikation
- **prefLabel (en):** Abstract model classification
- **prefLabel (fr):** Classification abstraite des maquettes
- **prefLabel (it):** Classificazione astratta dei modelli
- **title (en):** Abstract model classification

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
<td class="pbs-lang-col" data-lang="de" data-field="definition">Gebäudearchitektur — Räume, Bauteile und Ausbau in einem Fachmodell, inklusive Nutzflächen und Raumvolumen für Flächennachweise.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Dateiname: `{Projektnumber}_ARC-ARC_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Architecture</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Building architecture — spaces, components, and fit-out in one deliverable, including usable areas and space volumes for area verification.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">File name: `{Projektnumber}_ARC-ARC_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="label">Architecture</td>
<td class="pbs-lang-col" data-lang="fr" data-field="definition">Architecture du bâtiment — locaux, composants et aménagement dans une maquette, y compris surfaces utiles et volumes de locaux pour les justificatifs de surfaces.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="scope_note">Nom de fichier: `{Projektnumber}_ARC-ARC_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="it" data-field="label">Architettura</td>
<td class="pbs-lang-col" data-lang="it" data-field="definition">Architettura dell&#x27;edificio — spazi, componenti e finiture in un modello, comprese superfici utili e volumi dei locali per le verifiche di superficie.</td>
<td class="pbs-lang-col" data-lang="it" data-field="scope_note">Nome file: `{Projektnumber}_ARC-ARC_{Userdefined_text}.{ext}`.</td>
</tr>
<tr>
<td>AUS</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Aushub</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aushub und Erdbau — Abtrags- und Auffüllvolumen, getrennt von der Baugrubensicherung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Dateiname: `{Projektnumber}_STR-AUS_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Earthworks</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Excavation and earthworks — cut and fill volumes, separate from excavation-pit support.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">File name: `{Projektnumber}_STR-AUS_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="label">Terrassement</td>
<td class="pbs-lang-col" data-lang="fr" data-field="definition">Terrassement — volumes de déblai et de remblai, distincts du soutènement de fouille.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="scope_note">Nom de fichier: `{Projektnumber}_STR-AUS_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="it" data-field="label">Scavi</td>
<td class="pbs-lang-col" data-lang="it" data-field="definition">Scavi e movimenti di terra — volumi di scavo e riporto, distinti dalle opere di sostegno.</td>
<td class="pbs-lang-col" data-lang="it" data-field="scope_note">Nome file: `{Projektnumber}_STR-AUS_{Userdefined_text}.{ext}`.</td>
</tr>
<tr>
<td>BET</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Betonbau</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Stahlbetontragwerk — Fundamente, Stützen, Wände, Decken und weitere tragende Betonbauteile.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Dateiname: `{Projektnumber}_STR-BET_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Concrete</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Reinforced-concrete structure — foundations, columns, walls, slabs, and other load-bearing concrete members.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">File name: `{Projektnumber}_STR-BET_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="label">Béton armé</td>
<td class="pbs-lang-col" data-lang="fr" data-field="definition">Ouvrage en béton armé — fondations, poteaux, murs, dalles et autres éléments porteurs en béton.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="scope_note">Nom de fichier: `{Projektnumber}_STR-BET_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="it" data-field="label">Calcestruzzo</td>
<td class="pbs-lang-col" data-lang="it" data-field="definition">Struttura in calcestruzzo armato — fondazioni, colonne, pareti, solette e altri elementi portanti in calcestruzzo.</td>
<td class="pbs-lang-col" data-lang="it" data-field="scope_note">Nome file: `{Projektnumber}_STR-BET_{Userdefined_text}.{ext}`.</td>
</tr>
<tr>
<td>BEW</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Bewehrung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Armierung für Ausführung — Stäbe, Lagen und Positionen gemäss Bewehrungsplanung, getrennt vom Betontragwerk.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Dateiname: `{Projektnumber}_STR-BEW_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Reinforcement</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Reinforcement for execution — bars, layers, and positions according to the reinforcement design, separate from the concrete structure.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">File name: `{Projektnumber}_STR-BEW_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="label">Armature</td>
<td class="pbs-lang-col" data-lang="fr" data-field="definition">Armatures pour l&#x27;exécution — barres, nappes et positions selon le plan d&#x27;armature, distinctes de l&#x27;ouvrage en béton.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="scope_note">Nom de fichier: `{Projektnumber}_STR-BEW_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="it" data-field="label">Armatura</td>
<td class="pbs-lang-col" data-lang="it" data-field="definition">Armatura per l&#x27;esecuzione — barre, strati e posizioni secondo il progetto delle armature, distinta dalla struttura in calcestruzzo.</td>
<td class="pbs-lang-col" data-lang="it" data-field="scope_note">Nome file: `{Projektnumber}_STR-BEW_{Userdefined_text}.{ext}`.</td>
</tr>
<tr>
<td>BGR</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Baugrube</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Baugrubensicherung — Wände, Anker, Aussteifungen und weitere Sicherungselemente.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Dateiname: `{Projektnumber}_STR-BGR_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Excavation pit</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Excavation-pit support — walls, anchors, struts, and other retaining elements.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">File name: `{Projektnumber}_STR-BGR_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="label">Fouille</td>
<td class="pbs-lang-col" data-lang="fr" data-field="definition">Soutènement de fouille — parois, ancrages, butons et autres éléments de sécurisation.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="scope_note">Nom de fichier: `{Projektnumber}_STR-BGR_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="it" data-field="label">Scavo di fondazione</td>
<td class="pbs-lang-col" data-lang="it" data-field="definition">Opere di sostegno dello scavo — pareti, tiranti, puntelli e altri elementi di messa in sicurezza.</td>
<td class="pbs-lang-col" data-lang="it" data-field="scope_note">Nome file: `{Projektnumber}_STR-BGR_{Userdefined_text}.{ext}`.</td>
</tr>
<tr>
<td>FAS</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Fassade</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aussenhülle und Fassadenaufbau — Bekleidung, Öffnungen und fassadenbezogene Schichten, getrennt vom übrigen Architekturmodell.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Dateiname: `{Projektnumber}_ARC-FAS_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Facade</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">External envelope and facade build-up — cladding, openings, and facade-related layers, separate from the rest of the architecture deliverable.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">File name: `{Projektnumber}_ARC-FAS_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="label">Façade</td>
<td class="pbs-lang-col" data-lang="fr" data-field="definition">Enveloppe extérieure et composition de façade — revêtements, ouvertures et couches liées à la façade, séparés du reste de la maquette d&#x27;architecture.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="scope_note">Nom de fichier: `{Projektnumber}_ARC-FAS_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="it" data-field="label">Facciata</td>
<td class="pbs-lang-col" data-lang="it" data-field="definition">Involucro esterno e stratigrafia di facciata — rivestimenti, aperture e strati legati alla facciata, distinti dal resto del modello di architettura.</td>
<td class="pbs-lang-col" data-lang="it" data-field="scope_note">Nome file: `{Projektnumber}_ARC-FAS_{Userdefined_text}.{ext}`.</td>
</tr>
<tr>
<td>GRL</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Grundleitung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Grundleitungen und Kanalisation ausserhalb bzw. unter dem Gebäude — getrennt von der Sanitärinstallation.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Dateiname: `{Projektnumber}_MEP-GRL_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Underground services</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Underground drains and sewerage outside or under the building — separate from in-building plumbing.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">File name: `{Projektnumber}_MEP-GRL_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="label">Collecteurs</td>
<td class="pbs-lang-col" data-lang="fr" data-field="definition">Collecteurs et canalisations enterrées hors ou sous le bâtiment — distincts des installations sanitaires.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="scope_note">Nom de fichier: `{Projektnumber}_MEP-GRL_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="it" data-field="label">Condotte interrate</td>
<td class="pbs-lang-col" data-lang="it" data-field="definition">Condotte interrate e fognature fuori o sotto l&#x27;edificio — distinte dagli impianti sanitari.</td>
<td class="pbs-lang-col" data-lang="it" data-field="scope_note">Nome file: `{Projektnumber}_MEP-GRL_{Userdefined_text}.{ext}`.</td>
</tr>
<tr>
<td>GVM</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Geschossvolumen</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bruttovolumen je Geschoss für Massenstudien, Kennwerte und städtebauliche Nachweise.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Dateiname: `{Projektnumber}_ARC-GVM_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Storey volume</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Gross volume per storey for massing studies, metrics, and urban-design verification.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">File name: `{Projektnumber}_ARC-GVM_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="label">Volume d&#x27;étage</td>
<td class="pbs-lang-col" data-lang="fr" data-field="definition">Volume brut par étage pour études de masse, indicateurs et justificatifs urbanistiques.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="scope_note">Nom de fichier: `{Projektnumber}_ARC-GVM_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="it" data-field="label">Volume di piano</td>
<td class="pbs-lang-col" data-lang="it" data-field="definition">Volume lordo per piano per studi di massa, indicatori e verifiche urbanistiche.</td>
<td class="pbs-lang-col" data-lang="it" data-field="scope_note">Nome file: `{Projektnumber}_ARC-GVM_{Userdefined_text}.{ext}`.</td>
</tr>
<tr>
<td>HEI</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Heizung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Heizungsanlagen — Erzeugung, Verteilung und Abgabe von Wärme.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Dateiname: `{Projektnumber}_MEP-HEI_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Heating</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Heating systems — generation, distribution, and emission of heat.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">File name: `{Projektnumber}_MEP-HEI_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="label">Chauffage</td>
<td class="pbs-lang-col" data-lang="fr" data-field="definition">Installations de chauffage — production, distribution et émission de chaleur.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="scope_note">Nom de fichier: `{Projektnumber}_MEP-HEI_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="it" data-field="label">Riscaldamento</td>
<td class="pbs-lang-col" data-lang="it" data-field="definition">Impianti di riscaldamento — produzione, distribuzione ed emissione di calore.</td>
<td class="pbs-lang-col" data-lang="it" data-field="scope_note">Nome file: `{Projektnumber}_MEP-HEI_{Userdefined_text}.{ext}`.</td>
</tr>
<tr>
<td>HLZ</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Holzbau</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Holztragwerk — Stützen, Träger, Decken und weitere tragende Holzbauteile.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Dateiname: `{Projektnumber}_STR-HLZ_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Timber</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Timber structure — columns, beams, floors, and other load-bearing timber members.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">File name: `{Projektnumber}_STR-HLZ_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="label">Construction bois</td>
<td class="pbs-lang-col" data-lang="fr" data-field="definition">Ouvrage en bois — poteaux, poutres, planchers et autres éléments porteurs en bois.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="scope_note">Nom de fichier: `{Projektnumber}_STR-HLZ_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="it" data-field="label">Costruzione in legno</td>
<td class="pbs-lang-col" data-lang="it" data-field="definition">Struttura in legno — colonne, travi, solai e altri elementi portanti in legno.</td>
<td class="pbs-lang-col" data-lang="it" data-field="scope_note">Nome file: `{Projektnumber}_STR-HLZ_{Userdefined_text}.{ext}`.</td>
</tr>
<tr>
<td>KUE</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kühlung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kälteanlagen — Erzeugung, Verteilung und Abgabe von Kälte.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Dateiname: `{Projektnumber}_MEP-KUE_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Cooling</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Cooling systems — generation, distribution, and emission of cold.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">File name: `{Projektnumber}_MEP-KUE_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="label">Froid</td>
<td class="pbs-lang-col" data-lang="fr" data-field="definition">Installations de froid — production, distribution et émission de froid.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="scope_note">Nom de fichier: `{Projektnumber}_MEP-KUE_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="it" data-field="label">Raffrescamento</td>
<td class="pbs-lang-col" data-lang="it" data-field="definition">Impianti di raffrescamento — produzione, distribuzione ed emissione di freddo.</td>
<td class="pbs-lang-col" data-lang="it" data-field="scope_note">Nome file: `{Projektnumber}_MEP-KUE_{Userdefined_text}.{ext}`.</td>
</tr>
<tr>
<td>LAB</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Labor</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Laboreinrichtung und Speziallabor-Ausstattung — Geräte, Bänke und laborspezifische Einbauten.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Dateiname: `{Projektnumber}_ARC-LAB_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Laboratory</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Laboratory equipment and specialist lab fit-out — appliances, benches, and lab-specific installations.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">File name: `{Projektnumber}_ARC-LAB_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="label">Laboratoire</td>
<td class="pbs-lang-col" data-lang="fr" data-field="definition">Équipements de laboratoire et aménagements spécialisés — appareils, paillasses et installations spécifiques.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="scope_note">Nom de fichier: `{Projektnumber}_ARC-LAB_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="it" data-field="label">Laboratorio</td>
<td class="pbs-lang-col" data-lang="it" data-field="definition">Attrezzature di laboratorio e allestimenti speciali — apparecchi, banchi e installazioni specifiche.</td>
<td class="pbs-lang-col" data-lang="it" data-field="scope_note">Nome file: `{Projektnumber}_ARC-LAB_{Userdefined_text}.{ext}`.</td>
</tr>
<tr>
<td>LAN</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Landschaft</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Umgebungs- und Aussenraumgestaltung — Vegetation, Wege, Plätze und gestaltete Aussenanlagen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Dateiname: `{Projektnumber}_ARC-LAN_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Landscape</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Surroundings and outdoor-space design — vegetation, paths, plazas, and designed external works.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">File name: `{Projektnumber}_ARC-LAN_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="label">Paysage</td>
<td class="pbs-lang-col" data-lang="fr" data-field="definition">Aménagement des abords et des espaces extérieurs — végétation, cheminements, places et aménagements paysagers.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="scope_note">Nom de fichier: `{Projektnumber}_ARC-LAN_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="it" data-field="label">Paesaggio</td>
<td class="pbs-lang-col" data-lang="it" data-field="definition">Sistemazione degli spazi esterni — vegetazione, percorsi, piazze e opere a verde.</td>
<td class="pbs-lang-col" data-lang="it" data-field="scope_note">Nome file: `{Projektnumber}_ARC-LAN_{Userdefined_text}.{ext}`.</td>
</tr>
<tr>
<td>LUE</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Lüftung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Lüftungsanlagen — Luftführung, Geräte und lufttechnische Verteilung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Dateiname: `{Projektnumber}_MEP-LUE_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Ventilation</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Ventilation systems — air routes, equipment, and air-side distribution.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">File name: `{Projektnumber}_MEP-LUE_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="label">Ventilation</td>
<td class="pbs-lang-col" data-lang="fr" data-field="definition">Installations de ventilation — réseaux d&#x27;air, appareils et distribution aéraulique.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="scope_note">Nom de fichier: `{Projektnumber}_MEP-LUE_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="it" data-field="label">Ventilazione</td>
<td class="pbs-lang-col" data-lang="it" data-field="definition">Impianti di ventilazione — condotte d&#x27;aria, apparecchi e distribuzione aeraulica.</td>
<td class="pbs-lang-col" data-lang="it" data-field="scope_note">Nome file: `{Projektnumber}_MEP-LUE_{Userdefined_text}.{ext}`.</td>
</tr>
<tr>
<td>MOB</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Mobiliar</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Einrichtung und Möblierung für Nutzung, Visualisierung und Koordination — keine Laborspezialausstattung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Dateiname: `{Projektnumber}_ARC-MOB_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Furniture</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Furnishings and furniture for use, visualisation, and coordination — not specialist laboratory equipment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">File name: `{Projektnumber}_ARC-MOB_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="label">Mobilier</td>
<td class="pbs-lang-col" data-lang="fr" data-field="definition">Ameublement et mobilier pour usage, visualisation et coordination — hors équipements de laboratoire.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="scope_note">Nom de fichier: `{Projektnumber}_ARC-MOB_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="it" data-field="label">Arredi</td>
<td class="pbs-lang-col" data-lang="it" data-field="definition">Arredi e mobilio per uso, visualizzazione e coordinamento — esclusa l&#x27;attrezzatura di laboratorio.</td>
<td class="pbs-lang-col" data-lang="it" data-field="scope_note">Nome file: `{Projektnumber}_ARC-MOB_{Userdefined_text}.{ext}`.</td>
</tr>
<tr>
<td>SAN</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Sanitär</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Sanitäranlagen — Trinkwasser, Abwasser und sanitäre Apparate im Gebäude, ohne Grundleitungen.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Dateiname: `{Projektnumber}_MEP-SAN_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Plumbing</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Plumbing systems — drinking water, wastewater, and sanitary appliances in the building, excluding underground drains.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">File name: `{Projektnumber}_MEP-SAN_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="label">Sanitaire</td>
<td class="pbs-lang-col" data-lang="fr" data-field="definition">Installations sanitaires — eau potable, eaux usées et appareils sanitaires dans le bâtiment, hors collecteurs enterrés.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="scope_note">Nom de fichier: `{Projektnumber}_MEP-SAN_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="it" data-field="label">Sanitari</td>
<td class="pbs-lang-col" data-lang="it" data-field="definition">Impianti sanitari — acqua potabile, acque reflue e apparecchi sanitari nell&#x27;edificio, escluse le condotte interrate.</td>
<td class="pbs-lang-col" data-lang="it" data-field="scope_note">Nome file: `{Projektnumber}_MEP-SAN_{Userdefined_text}.{ext}`.</td>
</tr>
<tr>
<td>STB</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Stahlbau</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Stahltragwerk — Träger, Stützen, Verbände und weitere tragende Stahlbauteile.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Dateiname: `{Projektnumber}_STR-STB_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Steel</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Steel structure — beams, columns, bracing, and other load-bearing steel members.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">File name: `{Projektnumber}_STR-STB_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="label">Construction métallique</td>
<td class="pbs-lang-col" data-lang="fr" data-field="definition">Ouvrage métallique — poutres, poteaux, contreventements et autres éléments porteurs en acier.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="scope_note">Nom de fichier: `{Projektnumber}_STR-STB_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="it" data-field="label">Carpenteria metallica</td>
<td class="pbs-lang-col" data-lang="it" data-field="definition">Struttura in acciaio — travi, colonne, controventi e altri elementi portanti in acciaio.</td>
<td class="pbs-lang-col" data-lang="it" data-field="scope_note">Nome file: `{Projektnumber}_STR-STB_{Userdefined_text}.{ext}`.</td>
</tr>
<tr>
<td>UMG</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Umgebung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Bestand, Nachbarbebauung und Terrain als räumlicher Kontext — nicht die gestaltete Landschaftsplanung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note">Dateiname: `{Projektnumber}_ARC-UMG_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Surroundings</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Existing stock, neighbouring buildings, and terrain as spatial context — not designed landscape works.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note">File name: `{Projektnumber}_ARC-UMG_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="label">Contexte</td>
<td class="pbs-lang-col" data-lang="fr" data-field="definition">Existant, constructions voisines et terrain comme contexte spatial — distinct de l&#x27;aménagement paysager.</td>
<td class="pbs-lang-col" data-lang="fr" data-field="scope_note">Nom de fichier: `{Projektnumber}_ARC-UMG_{Userdefined_text}.{ext}`.</td>
<td class="pbs-lang-col" data-lang="it" data-field="label">Contesto</td>
<td class="pbs-lang-col" data-lang="it" data-field="definition">Esistente, edificato limitrofo e terreno come contesto spaziale — distinto dalla progettazione paesaggistica.</td>
<td class="pbs-lang-col" data-lang="it" data-field="scope_note">Nome file: `{Projektnumber}_ARC-UMG_{Userdefined_text}.{ext}`.</td>
</tr>
</tbody>
</table>
</div>
