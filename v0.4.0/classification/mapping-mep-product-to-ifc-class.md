# MEP product to IFC class mapping

Source: [`mep-product-to-ifc-class.mapping.ttl`](sources/mapping-mep-product-to-ifc-class.ttl)

External target labels are not shipped in this repository; only codes and IRIs are shown.

## Dataset

- **description (de):** Ordnet zuweisbare TGA-Erzeuger- und Endgeraeteprodukte IFC-Entitaetsklassen fuer Ingestion-Hinweise zu. skos:closeMatch wo die Zuordnung typisch, aber nicht ausschliesslich ist.
- **description (en):** Maps assignable MEP unit and terminal product concepts to IFC entity classes for ingestion hints. Uses skos:closeMatch where the mapping is typical but not exclusive.
- **title (de):** Mapping TGA-Produkte zu IFC-Klassen
- **title (en):** MEP product to IFC class mapping

## Links

| Source | Relation | Targets |
| --- | --- | --- |
| `mtp:MTP-COOL-CHILLED-CEILING` | `closeMatch` | `ifcowl:IfcCooledBeam` |
| `mtp:MTP-COOL-FAN-COIL` | `closeMatch` | `ifcowl:IfcUnitaryEquipment` |
| `mtp:MTP-DATA-DATA-OUTLET` | `closeMatch` | `ifcowl:IfcCommunicationsAppliance` |
| `mtp:MTP-DATA-DATA-OUTLET` | `closeMatch` | `ifcowl:IfcOutlet` |
| `mtp:MTP-DATA-SENSOR-ACTUATOR` | `closeMatch` | `ifcowl:IfcActuator` |
| `mtp:MTP-DATA-SENSOR-ACTUATOR` | `closeMatch` | `ifcowl:IfcSensor` |
| `mtp:MTP-DATA-WIFI-AP` | `closeMatch` | `ifcowl:IfcCommunicationsAppliance` |
| `mtp:MTP-ELEC-LIGHT` | `closeMatch` | `ifcowl:IfcLightFixture` |
| `mtp:MTP-ELEC-SOCKET` | `closeMatch` | `ifcowl:IfcOutlet` |
| `mtp:MTP-ELEC-SWITCH` | `closeMatch` | `ifcowl:IfcSwitchingDevice` |
| `mtp:MTP-FIRE-FIRE-DAMPER` | `closeMatch` | `ifcowl:IfcDamper` |
| `mtp:MTP-FIRE-FIRE-DAMPER-ACTUATOR` | `closeMatch` | `ifcowl:IfcActuator` |
| `mtp:MTP-FIRE-SMOKE-DETECTOR` | `closeMatch` | `ifcowl:IfcAlarm` |
| `mtp:MTP-FIRE-SMOKE-DETECTOR` | `closeMatch` | `ifcowl:IfcSensor` |
| `mtp:MTP-FW-SHOWER` | `closeMatch` | `ifcowl:IfcSanitaryTerminal` |
| `mtp:MTP-FW-TAP` | `closeMatch` | `ifcowl:IfcSanitaryTerminal` |
| `mtp:MTP-FW-WC-FLUSH` | `closeMatch` | `ifcowl:IfcSanitaryTerminal` |
| `mtp:MTP-HEAT-FAN-COIL` | `closeMatch` | `ifcowl:IfcUnitaryEquipment` |
| `mtp:MTP-HEAT-RADIATOR` | `closeMatch` | `ifcowl:IfcSpaceHeater` |
| `mtp:MTP-HEAT-UFH-MANIFOLD` | `closeMatch` | `ifcowl:IfcValve` |
| `mtp:MTP-SM-GAS-OUTLET` | `closeMatch` | `ifcowl:IfcGasTerminal` |
| `mtp:MTP-SM-HOSE-REEL` | `closeMatch` | `ifcowl:IfcFireSuppressionTerminal` |
| `mtp:MTP-SM-SPRINKLER-HEAD` | `closeMatch` | `ifcowl:IfcFireSuppressionTerminal` |
| `mtp:MTP-VENT-AIR-VALVE` | `closeMatch` | `ifcowl:IfcAirTerminal` |
| `mtp:MTP-VENT-AIR-VALVE` | `closeMatch` | `ifcowl:IfcAirTerminalBox` |
| `mtp:MTP-VENT-GRILLE` | `closeMatch` | `ifcowl:IfcAirTerminal` |
| `mtp:MTP-WW-FLOOR-DRAIN` | `closeMatch` | `ifcowl:IfcWasteTerminal` |
| `mtp:MTP-WW-SINK-DRAIN` | `closeMatch` | `ifcowl:IfcWasteTerminal` |
| `mtp:MTP-WW-WC-OUTLET` | `closeMatch` | `ifcowl:IfcWasteTerminal` |
| `mup:MUP-COOL-CHILLER` | `closeMatch` | `ifcowl:IfcChiller` |
| `mup:MUP-COOL-FREE-COOLER` | `closeMatch` | `ifcowl:IfcCoolingTower` |
| `mup:MUP-DATA-NETWORK-SWITCH` | `closeMatch` | `ifcowl:IfcCommunicationsAppliance` |
| `mup:MUP-DATA-PATCH-PANEL` | `closeMatch` | `ifcowl:IfcCommunicationsAppliance` |
| `mup:MUP-DATA-SERVER` | `closeMatch` | `ifcowl:IfcCommunicationsAppliance` |
| `mup:MUP-ELEC-GENERATOR` | `closeMatch` | `ifcowl:IfcElectricGenerator` |
| `mup:MUP-ELEC-MAIN-DIST-BOARD` | `closeMatch` | `ifcowl:IfcElectricDistributionBoard` |
| `mup:MUP-ELEC-SUB-DIST-BOARD` | `closeMatch` | `ifcowl:IfcElectricDistributionBoard` |
| `mup:MUP-ELEC-TRANSFORMER` | `closeMatch` | `ifcowl:IfcTransformer` |
| `mup:MUP-ELEC-UPS` | `closeMatch` | `ifcowl:IfcElectricFlowStorageDevice` |
| `mup:MUP-FW-PRESSURE-BOOSTER` | `closeMatch` | `ifcowl:IfcPump` |
| `mup:MUP-FW-WATER-HEATER` | `closeMatch` | `ifcowl:IfcBoiler` |
| `mup:MUP-HEAT-BOILER` | `closeMatch` | `ifcowl:IfcBoiler` |
| `mup:MUP-HEAT-DISTRICT-HEAT-SUBSTATION` | `closeMatch` | `ifcowl:IfcHeatExchanger` |
| `mup:MUP-HEAT-HEAT-PUMP` | `closeMatch` | `ifcowl:IfcUnitaryEquipment` |
| `mup:MUP-SM-COMPRESSOR` | `closeMatch` | `ifcowl:IfcCompressor` |
| `mup:MUP-SM-FIRE-PUMP` | `closeMatch` | `ifcowl:IfcPump` |
| `mup:MUP-SM-GAS-REGULATOR` | `closeMatch` | `ifcowl:IfcFlowMeter` |
| `mup:MUP-VENT-AHU` | `closeMatch` | `ifcowl:IfcUnitaryEquipment` |
| `mup:MUP-VENT-FAN` | `closeMatch` | `ifcowl:IfcFan` |
| `mup:MUP-WW-GREASE-SEPARATOR` | `closeMatch` | `ifcowl:IfcTank` |
| `mup:MUP-WW-LIFTING-STATION` | `closeMatch` | `ifcowl:IfcPump` |
