# Abstract MEP unit products

Source: [`mep-unit-products.skos.ttl`](sources/mep-unit-product.ttl)

## Scheme

- **definition (de):** Produkttyp-Klassifikation fuer TGA-Erzeuger- oder Wandlereinheiten (Erzeuger-/Wandlerrolle; entspricht SystemType.unit). Fuer Katalog-, Spezifikations- und Kostenworkflows auf Equipment und gruppierten IfcSystem-Anlagen.
- **definition (en):** Product-type classification for MEP generating or converting units (producer/converter role; aligns with SystemType.unit). For catalog, specification, and cost workflows on Equipment and grouped IfcSystem plant.
- **prefLabel (de):** Abstrakte TGA-Erzeuger-/Wandlerprodukte
- **prefLabel (en):** Abstract MEP unit products
- **title (en):** Abstract MEP unit products

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
<th class="pbs-lang-col" data-lang="de" data-field="description">Description</th>
<th class="pbs-lang-col" data-lang="de" data-field="scope_note">Scope note</th>
<th class="pbs-lang-col" data-lang="en" data-field="label">Label</th>
<th class="pbs-lang-col" data-lang="en" data-field="definition">Definition</th>
<th class="pbs-lang-col" data-lang="en" data-field="description">Description</th>
<th class="pbs-lang-col" data-lang="en" data-field="scope_note">Scope note</th>
</tr>
</thead>
<tbody>
<tr>
<td>MUP-COOL-CHILLER</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Kaelteanlage / Kaeltemaschine</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Kaelteanlage zur Erzeugung von Kaltwasser oder Direktverdampfungskuehlung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Entzieht dem Kaltwasser- oder Kältemittelkreis Wärme und gibt sie an die Umgebungsluft oder einen Rückkühlkreis ab, um die von den Kälteverbrauchern geforderte Vorlauftemperatur zu halten. Lieferung als werkseitig montierte Einheit für die Innenaufstellung in der Kältezentrale oder die Aussenaufstellung auf schwingungsentkoppelter Unterlage, Anschluss an Kaltwasservor- und -rücklauf, Rückkühlung, Stromversorgung und Kondensatentwässerung, Stufenschaltung und Sollwerte über die Gebäudeautomation. Geeignet für Gebäude mit dauerndem oder prozessbedingtem Kältebedarf; erfordert Platz für Luftwege und Wartung, Beachtung der Schallemission sowie Zugang für Servicearbeiten am Kältekreis und den Komponentenaustausch.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Chiller</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Chiller plant producing chilled water or direct expansion cooling.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Removes heat from the chilled water or refrigerant circuit and rejects it to the ambient air or a recooling circuit, holding the supply temperature required by the cooling consumers. Delivered as a factory-assembled unit for indoor placement in the refrigeration plant room or for outdoor placement on a vibration-isolated base, connected to chilled water flow and return, recooling, power supply, and condensate drainage, with staging and setpoints controlled from building automation. Suitable for buildings with continuous or process-driven cooling demand; requires space for air paths and maintenance, attention to noise emission, and access for refrigerant circuit servicing and component replacement.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>MUP-COOL-FREE-COOLER</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Freecooler</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Trockenkuehler, Kuehlturm oder Freecooling-Waermeabgabeeinheit.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Gibt Wärme aus einem Wasserkreis direkt an die Aussenluft ab und stellt Kälte ohne maschinelle Kälteerzeugung bereit, solange die Aussenbedingungen dies zulassen, oder dient als Rückkühler einer Kältemaschine. Lieferung als werkseitig montierte Einheit für Aussenaufstellung oder belüfteten Technikbereich auf schwingungsentkoppelter Unterlage oder Stahlrahmen, Anschluss an Vor- und Rücklauf, Stromversorgung und im Nassbetrieb an Wasserversorgung und Entwässerung, Umschaltung und Ventilatorregelung über die Gebäudeautomation. Geeignet für Gebäude mit ganzjährigem Kältebedarf und verfügbarer Aussenaufstellung; erfordert freie Luftwege, Schutz gegen Luftkurzschluss, Frostschutzmassnahmen und Zugang für Reinigung und Wartung der Wärmeübertrager.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Free cooler</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Dry cooler, cooling tower, or free-cooling heat rejection unit.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Rejects heat from a water circuit directly to the outdoor air and supplies cooling without mechanical refrigeration whenever outdoor conditions allow, or serves as recooler for a chiller. Delivered as a factory-assembled unit for outdoor placement or a ventilated plant area on a vibration-isolated support or steel frame, connected to circuit flow and return, power supply, and, in wet operation, water supply and drainage, with changeover and fan control from building automation. Suitable for buildings with year-round cooling demand and available outdoor placement; requires unobstructed air paths, protection against air short-circuiting, frost protection measures, and access for coil cleaning and maintenance.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>MUP-DATA-NETWORK-SWITCH</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Netzwerk-Switch / Rack</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Aktiver Netzwerk-Switch, Router oder rackmontierte ICT-Verteilungseinheit.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Vermittelt den Datenverkehr zwischen den angeschlossenen Endgeräten und dem Netzwerk-Backbone und speist bei Bedarf Endgeräte über dieselbe Verkabelung mit Energie. Lieferung als rackmontierte Komponente im Kommunikationsschrank mit gesicherter Stromversorgung, Uplink-Anbindung und Einbindung in Netzwerk- und Gebäudeautomationsmanagement. Geeignet für die Etagen- und Zonenverteilung von Gebäude-ICT- und Gebäudeautomationsnetzen; erfordert Rackplatz, Wärmeabfuhr aus dem Schrank und kontrollierten Zugang für Konfiguration und Austausch.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Network switch / rack</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Active network switch, router, or rack-mounted ICT distribution unit.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Forwards data traffic between the connected end devices and the network backbone and, where required, supplies terminal devices with power over the same cabling. Delivered as rack-mounted equipment in a communications cabinet with secured power supply, uplink connections, and integration into network and building automation management. Suitable for floor and zone distribution of building ICT and building automation networks; requires rack space, heat removal from the cabinet, and controlled access for configuration and replacement.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>MUP-DATA-PATCH-PANEL</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Patchpanel</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Patchpanel oder Kreuzschiene der strukturierten Verkabelung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Schliesst die strukturierte Verkabelung eines Verteilbereichs ab und erlaubt das Rangieren einzelner Verbindungen auf die aktive Technik mittels Patchkabel. Lieferung als vorgefertigte Panels oder Rangierfelder, montiert in Schrank oder Rack eines Kommunikationsraums, Verkabelung aufgelegt, geprüft und beschriftet, mit Kabelführung für Zugentlastung und Biegeradien. Geeignet für die flexible Umbelegung von Anschlüssen im Betrieb; erfordert Rackplatz, Rangierfreiraum an der Front und eine dokumentierte Portbeschriftung für den Unterhalt.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Patch panel</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Structured cabling patch panel or cross-connect frame.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Terminates the structured cabling of a distribution area and allows individual links to be cross-connected to active equipment with patch cords. Delivered as prefabricated panels or cross-connect frames mounted in a cabinet or rack in a communications room, with the cabling terminated, tested, and labelled and with cable management for strain relief and bend radii. Suitable for flexible reassignment of outlets during operation; requires rack space, patching clearance at the front, and documented port labelling for maintenance.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>MUP-DATA-SERVER</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Server</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Server oder Edge-Compute-Appliance in der Gebaeude-ICT-Infrastruktur.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Stellt Rechen- und Speicherkapazität für gebäudebezogene Anwendungen wie Automation, Zutrittskontrolle oder Medientechnik bereit. Lieferung als rackmontierte Hardware in einem Kommunikations- oder Serverraum mit gesicherter Stromversorgung, Netzwerkanbindung und Kühlung, Inbetriebnahme gemeinsam mit den betriebenen Anwendungen. Geeignet dort, wo Gebäudedaten lokal verarbeitet oder vorgehalten werden müssen; erfordert kontrolliertes Raumklima, überwachten Zugang und einen definierten Weg für Wartung, Datensicherung und Hardwareerneuerung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Server</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Server or edge compute appliance in building ICT infrastructure.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Provides computing and storage capacity for building-related applications such as automation, access control, or media services. Delivered as rack-mounted hardware in a communications or server room with secured power supply, network connection, and cooling, and commissioned together with the applications it hosts. Suitable where building data must be processed or retained locally; requires a controlled room climate, monitored access, and a defined path for maintenance, data backup, and hardware renewal.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>MUP-ELEC-GENERATOR</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Notstromaggregat</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Reserve- oder Notstromaggregat.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Erzeugt bei Ausfall der Netzversorgung elektrische Energie vor Ort und versorgt Sicherheits- und ausgewählte Ersatzverbraucher bis zur Rückkehr der Normalversorgung. Lieferung als werkseitig montiertes Aggregat auf schwingungsentkoppeltem Fundament oder in einem Aussengehäuse, mit Brennstoffversorgung, Abgas- und Verbrennungsluftführung, Kühlluftwegen sowie automatischer Zuschaltung auf die Verteilung über die Gebäudeautomation. Geeignet für Gebäude mit sicherheitsrelevanten oder betriebskritischen Verbrauchern; erfordert einen brandabgetrennten Aufstellort, Schall- und Abgasführung, Brennstofflagerung sowie regelmässige Probeläufe und Wartung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Backup generator</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Standby or emergency electrical generator set.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Generates electricity on site when the mains supply fails and feeds safety and selected standby loads until normal supply returns. Delivered as a factory-assembled set on a vibration-isolated foundation or in an outdoor enclosure, with fuel supply, exhaust and combustion air routes, cooling air paths, and automatic transfer to the distribution under control of building automation. Suitable for buildings with safety-relevant or business-critical loads; requires a fire-separated plant location, noise and exhaust routing, fuel storage, and periodic test runs and servicing.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>MUP-ELEC-MAIN-DIST-BOARD</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hauptverteilung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Hauptverteilung (HV) am Gebaeude- oder Anschlusseingang.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Übernimmt die Einspeisung und verteilt sie auf Unterverteilungen und Hauptverbraucher, mit den Schutz-, Schalt-, Trenn- und Messstellen am Gebäude- oder Anschlusseingang. Lieferung als werkseitig gefertigte und geprüfte Felder, Aufstellung auf Sockel in einem Elektroraum, Anschluss über Schienen und Kabel an Einspeisung und Abgänge, Zustands- und Störmeldungen an die Gebäudeautomation. Geeignet als zentraler Versorgungsknoten eines Gebäudes; erfordert einen zugänglichen Elektroraum mit Bedienfreiräumen, Reserveplatz für spätere Abgänge und sicheren Zugang für Prüfung und Wartung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Main distribution board</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Main electrical distribution board (Hauptverteilung) at building or site entry.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Receives the incoming supply and distributes it to sub-distribution boards and main loads, providing the protection, switching, isolation, and metering points at building or site entry. Delivered as factory-built and tested cubicles, set on a plinth in an electrical room and connected by busbar and cable to the incoming supply and the outgoing circuits, with status and fault signals passed to building automation. Suitable as the central supply node of a building; requires an accessible electrical room with operating clearances, spare capacity for later circuits, and safe access for testing and maintenance.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>MUP-ELEC-SUB-DIST-BOARD</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Unterverteilung</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Unterverteilung (UV) fuer Etage, Zone oder Mietbereich.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Verteilt die Energie innerhalb einer Etage, Zone oder Mietfläche und stellt Schutz und Schaltung für die zugeordneten Endstromkreise bereit. Lieferung als werkseitig gefertigter Schrank für Wand-, Einbau- oder Standmontage in Steigzone, Korridor oder Nebenraum, Anschluss über eine Zuleitung an die vorgelagerte Verteilung, bei Bedarf Meldung der Stromkreiszustände an die Gebäudeautomation. Geeignet für etappierten Ausbau und Mieterwechsel; erfordert eine zugängliche Lage mit Bedienfreiraum und Reserveplätze für spätere Stromkreise.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Sub-distribution board</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Sub-distribution board (Unterverteilung) serving a floor, zone, or tenant.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Distributes power within a floor, zone, or tenancy and provides protection and switching for the final circuits it serves. Delivered as a factory-built cabinet for wall, recess, or floor mounting in a riser, corridor, or ancillary room, connected to the upstream distribution by a feeder cable and, where required, reporting circuit states to building automation. Suitable for staged fit-out and tenant changes; requires an accessible location with operating clearance and spare ways for later circuits.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>MUP-ELEC-TRANSFORMER</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Transformator</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Leistungstransformator zur Spannungswandlung fuer die Gebaeudeverteilung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Wandelt die einspeisende Mittelspannung auf das für die Gebäudeverteilung erforderliche Niederspannungsniveau und versorgt die Hauptverteilung. Lieferung als werkseitig montierte und geprüfte Einheit, Aufstellung auf lastverteilendem Fundament in einem eigenen Transformatorenraum, Anschluss an Mittelspannungsschaltanlage und Niederspannungsverteilung, Temperatur- und Störzustände an die Gebäudeautomation gemeldet. Geeignet für Gebäude mit eigener Übergabestation; erfordert Transportweg, Freiräume für Kühlluft und Wartung sowie Vorsorge für einen Austausch innerhalb der Nutzungsdauer.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Transformer</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Power transformer converting voltage for building distribution.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Converts the incoming medium-voltage supply to the low-voltage level required for building distribution and feeds the main distribution board. Delivered as a factory-assembled and tested unit, set on a load-distributing base in a dedicated transformer room and connected to medium-voltage switchgear and low-voltage distribution, with temperature and fault states reported to building automation. Suitable for buildings with their own supply station; requires a transport route, clearances for cooling air and maintenance, and provision for replacement within the service life.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>MUP-ELEC-UPS</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">USV-Anlage</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Unterbrechungsfreie Stromversorgung (USV) fuer kritische Verbraucher.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Überbrückt Versorgungsunterbrüche und Spannungsstörungen für kritische Verbraucher durch unterbrechungsfreie Umschaltung auf gespeicherte Energie. Lieferung als werkseitig montierte Einheit mit Batterie- oder Speicherschränken, Aufstellung in einem belüfteten oder gekühlten Technikraum, Einbindung zwischen vorgelagerter Verteilung und den geschützten Stromkreisen, Betriebs- und Speicherzustände an die Gebäudeautomation gemeldet. Geeignet dort, wo ein Versorgungsausfall nicht zulässig ist; erfordert ausreichende Bodentragfähigkeit, Wärmeabfuhr, einen Bypass für Servicearbeiten und geplanten Austausch der Speicherkomponenten innerhalb der Nutzungsdauer.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Uninterruptible power supply</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Uninterruptible power supply (UPS) unit for critical loads.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Bridges supply interruptions and voltage disturbances for critical loads by switching over to stored energy without interruption. Delivered as a factory-assembled unit with battery or storage cabinets, placed in a ventilated or cooled technical room and connected between the upstream distribution and the protected circuits, with operating and storage states reported to building automation. Suitable where a loss of supply is not acceptable; requires floor loading capacity, heat removal, a bypass for servicing, and planned replacement of the storage components within the service life.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>MUP-FW-PRESSURE-BOOSTER</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Druckerhoehungsanlage</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Trinkwasser-Druckerhoehungsanlage.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Erhöht den Druck der Trinkwasserversorgung, damit an allen Verbrauchern einschliesslich oberer Geschosse und entfernter Entnahmestellen der erforderliche Fliessdruck verfügbar ist. Lieferung als werkseitig montierte Pumpengruppe mit Steuerschrank, Druckbehälter und Sensorik auf schwingungsentkoppelter Unterlage im Hauseinführungs- oder Technikraum, Anschluss an die Einspeiseleitung und die Gebäudeverteilung, bedarfsgeführte Drehzahlregelung und Störmeldungen an die Gebäudeautomation. Geeignet für hohe Gebäude und Grundstücke mit unzureichendem Netzdruck; erfordert einen entwässerten Aufstellort, Beachtung von Schall- und Schwingungsübertragung sowie Zugang für Pumpen- und Steuerungswartung bei aufrechterhaltener Versorgung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Pressure booster</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Potable water pressure booster pump set (Druckerhoehung).</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Raises the pressure of the potable water supply so that the required flow pressure is available at all consumers, including upper floors and remote draw-off points. Delivered as a factory-assembled pump set with control cabinet, pressure vessel, and sensors on a vibration-isolated base in the service entry or plant room, connected to the incoming main and the building distribution, with demand-led speed control and fault signals to building automation. Suitable for tall buildings and sites with insufficient network pressure; requires a drained plant location, attention to noise and vibration transmission, and access for pump and control maintenance while supply is maintained.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>MUP-FW-WATER-HEATER</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Warmwasserbereiter</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Warmwasserbereiter oder Brauchwassererwaermer.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Erwärmt Trinkwasser auf die erforderliche Temperatur und hält einen Vorrat bereit, damit der Spitzenbedarf an den Entnahmestellen gedeckt wird. Lieferung als werkseitig gefertigte Einheit mit Speicherbehälter, Heizflächen oder Elektroheizeinsätzen, Dämmung und Sicherheitsarmaturen, Aufstellung auf Sockel im Technikraum, Anschluss an Wärmeerzeuger oder Stromversorgung, Kalt- und Warmwasserleitungen, Zirkulation und Entwässerung, Temperatur- und Hygienebetriebsarten über die Gebäudeautomation. Geeignet für die Warmwasserversorgung von Wohn- und Gewerbebauten; erfordert Bodentragfähigkeit und Raumhöhe für Einbringung und Ziehen der Heizeinsätze sowie Zugang für Kontrolle, Entkalkung und Austausch von Anode oder Komponenten.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Water heater / DHW boiler</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Domestic hot water heater or boiler (Warmwasserbereiter).</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Heats potable water to the required temperature and holds a reserve so that peak draw-off demand is covered at the taps. Delivered as a factory-made unit with storage vessel, heating surfaces or electric elements, insulation, and safety fittings, set on a plinth in the plant room and connected to the heat source or power supply, cold and hot water lines, circulation, and drainage, with temperature and hygiene operating modes controlled from building automation. Suitable for hot water supply in residential and commercial buildings; requires floor loading capacity and headroom for delivery and withdrawal of heating elements, and access for inspection, descaling, and replacement of anode or components.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>MUP-HEAT-BOILER</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Heizkessel</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Waermeerzeuger-Heizkessel fuer Raum- oder Prozesswaerme.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Erzeugt Wärme für Raum- oder Prozesswärme und übergibt sie mit der erforderlichen Vorlauftemperatur und dem erforderlichen Volumenstrom an den Heizkreis. Lieferung als werkseitig montierte Einheit, Aufstellung auf Sockel in der Heizzentrale, Anschluss an Brennstoffversorgung, Abgasanlage, Heizungsvor- und -rücklauf, Sicherheitseinrichtungen und Ausdehnung, Folge- und Temperaturregelung in die Gebäudeautomation eingebunden. Geeignet als Grund- oder Spitzenlasterzeuger in Einzel- und Mehrkesselanlagen; erfordert eine brandabgetrennte Heizzentrale, Zuluft- und Abgasführung, Transport- und Servicefreiräume sowie Zugang für Brenner- und Wärmetauscherwartung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Boiler</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Heat generator boiler for space or process heating.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Generates heat for space heating or process use and transfers it to the heating circuit at the required flow temperature and flow rate. Delivered as a factory-assembled unit set on a plinth in the heating plant room and connected to fuel supply, flue, heating flow and return, safety devices, and expansion, with sequence and temperature control integrated into building automation. Suitable as lead or peak-load generator in single and multi-unit plant; requires a fire-separated plant room, combustion air and flue routing, transport and service clearances, and access for burner and heat exchanger maintenance.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>MUP-HEAT-DISTRICT-HEAT-SUBSTATION</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Waermeuebergabestation</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Fernwaermeuebergabestation oder Waermeuebergabestation.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Überträgt Wärme aus dem externen Versorgungsnetz auf die Heiz- und Warmwasserkreise des Gebäudes, trennt Primär- und Sekundärseite hydraulisch und regelt die sekundäre Vorlauftemperatur. Lieferung als werkseitig montierte und geprüfte Kompaktstation mit Wärmetauscher, Pumpen, Regelventilen, Sicherheitseinrichtungen und Messung, Aufstellung im Übergaberaum nahe der Hauseinführung, Anschluss an Netzanschluss und Gebäudeverteilung, Regel- und Verbrauchsdaten an die Gebäudeautomation. Geeignet für Gebäude mit Anschluss an ein Fern- oder Nahwärmenetz; erfordert einen kompakten Übergaberaum mit Entwässerung, Freiraum für die Reinigung des Wärmetauschers und Zugang des Netzbetreibers zur Messeinrichtung.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">District heat substation</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">District heating substation or heat interface unit (Waermeuebergabestation).</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Transfers heat from the external supply network to the building heating and hot water circuits, separates the primary and secondary sides hydraulically, and controls the secondary flow temperature. Delivered as a factory-assembled and tested skid with heat exchanger, pumps, control valves, safety devices, and metering, placed in the transfer room near the service entry and connected to the network connection and the building distribution, with control and consumption data passed to building automation. Suitable for buildings supplied from a district or local heating network; requires a compact transfer room with drainage, clearance for cleaning the heat exchanger, and access for the network operator to the metering equipment.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>MUP-HEAT-HEAT-PUMP</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Waermepumpe</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Waermepumpenanlage fuer Heizbetrieb (optional auch Kuehlbetrieb).</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Hebt Wärme aus Luft, Erdreich, Wasser oder Abwärme auf ein nutzbares Temperaturniveau für den Heizkreis und liefert im reversiblen Betrieb zusätzlich Kälte. Lieferung als werkseitig montierte Innen- oder Ausseneinheit auf schwingungsentkoppelter Unterlage, Anschluss an Quellenkreis, Heizungsvor- und -rücklauf, Speicher, Stromversorgung und Kondensatentwässerung, Betriebsarten und Quellentemperaturen über die Gebäudeautomation geregelt. Geeignet dort, wo eine Wärmequelle auf dem Grundstück erschlossen werden kann; erfordert Quellenerschliessung, Platz und Freiräume um das Gerät, Beachtung der Schallemission am Aufstellort und Zugang für Servicearbeiten am Kältekreis.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Heat pump</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Heat pump unit for heating (and optionally cooling) operation.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Raises heat taken from air, ground, water, or waste heat to a usable temperature for the heating circuit and, in reversible operation, also supplies cooling. Delivered as a factory-assembled indoor or outdoor unit on a vibration-isolated base, connected to the source circuit, heating flow and return, buffer storage, power supply, and condensate drainage, with operating modes and source temperatures controlled through building automation. Suitable where a heat source can be developed on the site; requires source installation works, space and clearances around the unit, attention to noise emission at the installation point, and access for servicing the refrigerant circuit.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>MUP-SM-COMPRESSOR</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Druckluftkompressor</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Drucklufterzeugungs-Kompressor.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Erzeugt Druckluft mit dem von den angeschlossenen Verbrauchern geforderten Druck und der geforderten Qualität und hält die Versorgung über einen Behälter auch bei schwankendem Bedarf aufrecht. Lieferung als werkseitig montierte Einheit mit Antrieb, Kühlung, Behälter und Luftaufbereitung auf schwingungsentkoppelter Unterlage in einem belüfteten Technikraum, Anschluss an das Verteilnetz, die Stromversorgung, die Kondensatentwässerung und die Wärmeabfuhr, Lastregelung und Störmeldungen an die Gebäudeautomation. Geeignet für Werkstätten, Labore und Prozessbereiche; erfordert kühle Ansaugluft und Wärmeabfuhr aus dem Raum, Beachtung der Schallübertragung sowie Zugang für Filter-, Öl- und Komponentenservice.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Compressed air compressor</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Compressed air generation compressor unit.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Generates compressed air at the pressure and quality required by the connected consumers and maintains supply from a receiver against fluctuating demand. Delivered as a factory-assembled unit with drive, cooling, receiver, and air treatment on a vibration-isolated base in a ventilated plant room, connected to the distribution network, power supply, condensate drainage, and heat removal, with load control and fault signals passed to building automation. Suitable for workshops, laboratories, and process areas; requires cool intake air and heat rejection from the room, attention to noise transmission, and access for filter, oil, and component servicing.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>MUP-SM-FIRE-PUMP</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Sprinklerpumpe / Loeschwasserpumpe</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Sprinkler- oder Loeschwasserpumpenanlage.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Stellt dem Sprinkler- oder Hydrantennetz Löschwasser mit dem erforderlichen Druck und Volumenstrom bereit, sobald Bedarf erkannt wird, und hält das Netz im Bereitschaftsbetrieb unter Druck. Lieferung als werkseitig montierte Pumpengruppe mit Antrieb, Steuerschrank und Armaturen auf schwingungsentkoppeltem Fundament in einem eigenen, brandabgetrennten Pumpenraum, Anschluss an Vorratsbehälter oder Zuleitung, Steigleitungsnetz, Strom- oder Brennstoffversorgung und Entwässerung, Bereitschafts- und Störzustände überwacht und an Gebäudeautomation und Alarmierung gemeldet. Geeignet für Gebäude mit automatischen Löschanlagen oder druckbeaufschlagten Hydrantennetzen; erfordert eine gesicherte Versorgung und einen geschützten Pumpenraum mit Entwässerung sowie Zugang für regelmässige Probeläufe und Funktionskontrollen über die Nutzungsdauer.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Fire pump</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Fire suppression or sprinkler pump set.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Supplies the sprinkler or hydrant network with firefighting water at the required pressure and flow rate as soon as demand is detected, and holds the network pressurised in standby. Delivered as a factory-assembled pump set with drive, control cabinet, and fittings on a vibration-isolated foundation in a dedicated fire-separated pump room, connected to the storage tank or supply main, the riser network, power or fuel supply, and drainage, with readiness and fault states monitored and reported to building automation and the alarm system. Suitable for buildings with automatic extinguishing systems or pressurised hydrant networks; requires a secured supply and a protected pump room with drainage, and access for periodic test runs and functional checks over the service life.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>MUP-SM-GAS-REGULATOR</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Gasdruckregler</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Gasdruckregel- oder Messstation.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Reduziert den Gasdruck der Zuleitung auf den Betriebsdruck der Gebäudeinstallation, hält ihn bei wechselndem Bedarf konstant, erfasst die entnommene Menge und schliesst die Versorgung im Störungsfall ab. Lieferung als werkseitig montierte und geprüfte Station mit Filter, Regler, Sicherheitseinrichtungen und Zähler, Aufstellung in einem eigenen belüfteten Stationsraum oder Schrank an der Hauseinführung, Anschluss an Zu- und Abgangsleitung, Abblaseleitungen ins Freie geführt, Absperr- und Messsignale für die Gebäudeautomation verfügbar. Geeignet für Gebäude mit gasbefeuerten Anlagen oder Prozessverbrauchern; erfordert einen brandabgetrennten, belüfteten Aufstellort mit Zugang von aussen für den Netzbetreiber und Freiraum für Kontrolle und Zählerwechsel.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Gas pressure regulator</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Gas pressure regulation or metering station.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Reduces the gas pressure of the supply line to the operating pressure of the building installation, keeps it constant under varying demand, records the quantity taken, and shuts off the supply in case of a fault. Delivered as a factory-assembled and tested station with filter, regulator, safety devices, and meter, placed in a dedicated ventilated station room or cabinet at the service entry and connected to the incoming and outgoing gas lines, with relief lines led to the outside and shut-off and metering signals available to building automation. Suitable for buildings with gas-fired plant or process consumers; requires a fire-separated and ventilated location with access from outside for the network operator and clearance for inspection and meter exchange.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>MUP-VENT-AHU</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Lueftungsgeraet / Monoblock</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Packagiertes Lueftungsgeraet (RLT) oder Monoblock-Lueftungsanlage.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Konditioniert Aussen- und Abluft einer Lüftungszone durch Filterung, Wärmerückgewinnung, Heizung, Kühlung und bei Bedarf Feuchtebehandlung und fördert die Zu- und Abluftvolumenströme. Lieferung als werkseitig montierter Monoblock oder als vor Ort gefügte Modulsektionen, Aufstellung auf schwingungsentkoppeltem Grundrahmen in der Technikzentrale oder auf dem Dach, Anschluss an Kanalnetz, Heiz- und Kältekreise, Kondensatentwässerung und Stromversorgung, Regelung in die Gebäudeautomation eingebunden. Geeignet für Zonen mit definierten Anforderungen an Luftqualität oder Komfort; erfordert Platz in der Technikzentrale mit Freiräumen für Filter- und Komponentenzugang, einen Transportweg für die grösste Sektion und Vorsorge für den Austausch von Komponenten über die Nutzungsdauer.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Air handling unit / monoblock</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Packaged air handling unit (AHU) or monoblock ventilation plant.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Conditions outdoor and extract air for a ventilation zone by filtering, heat recovery, heating, cooling, and where required humidity treatment, and moves the supply and extract air volumes. Delivered as a factory-assembled monoblock or as modular sections joined on site, set on a vibration-isolated base frame in a plant room or on the roof and connected to ductwork, heating and cooling circuits, condensate drainage, and power supply, with its control integrated into building automation. Suitable for zones with defined air quality or comfort requirements; requires plant room space with clearances for filter and component access, a transport route for the largest section, and provision for component replacement over the service life.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>MUP-VENT-FAN</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Ventilator</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Eigenstaendiger Zuluft-, Abluft- oder Umluft-Ventilator.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Fördert Zu-, Ab- oder Umluft durch einen Kanal- oder Schachtabschnitt und überwindet dessen Strömungswiderstand, damit der erforderliche Luftvolumenstrom sichergestellt ist. Lieferung als werkseitig montierte Einheit für Kanal-, Wand-, Schacht- oder Sockelmontage auf schwingungsentkoppelter Unterlage, Anschluss an das Kanalnetz über flexible Verbindungen, an die Stromversorgung und an die Drehzahlregelung der Gebäudeautomation. Geeignet für Einzelräume, Schächte sowie Rauch- oder Prozessabluftaufgaben; erfordert Zugang für Inspektion, Laufradreinigung und Motorwechsel sowie Beachtung der Schallübertragung am Einbauort.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Fan</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Standalone supply, extract, or transfer fan unit.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Moves supply, extract, or transfer air through a duct or shaft section and overcomes its flow resistance so that the required air volume is maintained. Delivered as a factory-assembled unit for duct, wall, shaft, or base mounting on a vibration-isolated support, connected to the ductwork through flexible connectors, to the power supply, and to speed control from building automation. Suitable for single rooms, shafts, and smoke or process extract duties; requires access for inspection, impeller cleaning, and motor replacement, and attention to noise transmission at the installation point.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>MUP-WW-GREASE-SEPARATOR</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Fettabscheider</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Fett- oder Oelabscheider fuer Kuechen- oder Prozessabwasser.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Hält in Küchen- oder Prozessabwasser mitgeführte Fette und Öle zurück, bevor dieses in die öffentliche Kanalisation gelangt, und schützt damit nachgeschaltete Leitungen und Anlagen vor Ablagerungen. Lieferung als werkseitig gefertigter Behälter, Aufstellung freistehend im Raum oder erdverlegt im Aussenbereich mit befahrbarer Abdeckung, Anschluss an Zu- und Ablauf mit erforderlichem Gefälle sowie bei entsprechender Ausrüstung an die Stromversorgung für Entsorgungs- und Warneinrichtungen, Füllstands- und Alarmmeldungen für die Gebäudeautomation verfügbar. Geeignet für Gastronomie- und Lebensmittelbereiche; erfordert einen zugänglichen Aufstellort mit Entwässerung und Belüftung, freie Zufahrt und Anschlussstelle für die Entleerung per Saugfahrzeug sowie regelmässige Entleerung und Reinigung im Betrieb.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Grease separator</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Grease or oil separator for kitchen or process wastewater.</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Retains grease and oil carried in kitchen or process wastewater before discharge into the public sewer and thereby protects downstream pipes and plant from deposits. Delivered as a factory-made tank, installed free-standing in a room or buried outside with a trafficable cover, connected to inflow and outflow at the required gradient and, where so equipped, to power supply for disposal and warning devices, with filling level and alarm signals available to building automation. Suitable for catering and food-processing areas; requires an accessible location with drainage and ventilation, a clear access route and connection point for emptying by tanker, and regular emptying and cleaning during operation.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
<tr>
<td>MUP-WW-LIFTING-STATION</td>
<td></td>
<td class="pbs-lang-col" data-lang="de" data-field="label">Hebeanlage</td>
<td class="pbs-lang-col" data-lang="de" data-field="definition">Abwasser-Hebeanlage oder Foerderstation.</td>
<td class="pbs-lang-col" data-lang="de" data-field="description">Sammelt Abwasser von Entwässerungsstellen unterhalb der Rückstauebene und fördert es über diese Ebene in die Freispiegelentwässerung. Lieferung als werkseitig montierte Einheit mit Sammelbehälter, einer oder mehreren Pumpen, Rückfluss- und Absperrarmaturen sowie Steuerschrank, Aufstellung auf ebener Unterlage in Schacht oder Technikraum, Anschluss an Zulauf, Druckleitung, Lüftung und Stromversorgung, Niveau- und Störmeldungen an die Gebäudeautomation. Geeignet für Sanitärräume, Einstellhallen und Küchenbereiche in Untergeschossen; erfordert einen zugänglichen, entwässerten und belüfteten Aufstellort, geruchsdichten Einbau sowie Zugang für Reinigung, Laufradkontrolle und Pumpentausch.</td>
<td class="pbs-lang-col" data-lang="de" data-field="scope_note"></td>
<td class="pbs-lang-col" data-lang="en" data-field="label">Lifting station</td>
<td class="pbs-lang-col" data-lang="en" data-field="definition">Wastewater lifting or pumping station (Hebeanlage).</td>
<td class="pbs-lang-col" data-lang="en" data-field="description">Collects wastewater from drainage points below the backflow level and pumps it above that level into the gravity drain. Delivered as a factory-assembled unit with collecting tank, one or more pumps, non-return and isolating fittings, and control cabinet, placed on a level base in a pit or plant room and connected to inflow, pressure pipe, vent, and power supply, with level and fault signals reported to building automation. Suitable for sanitary rooms, parking garages, and kitchen areas in basement levels; requires an accessible, drained and ventilated location, odour-tight installation, and access for cleaning, impeller inspection, and pump replacement.</td>
<td class="pbs-lang-col" data-lang="en" data-field="scope_note"></td>
</tr>
</tbody>
</table>
</div>
