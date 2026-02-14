# High Voltage Module Design

This document contains the detailed design of the high voltage module.
The purpose is to provide concrete information for the powertrain module and act as a decision log, containing not only the final design, but an explanation of why the design was chosen over alternatives.
For now, the scope of the design is limited to parts selection for major components like the battery.
Details like mounting brackets and wiring are currently unspecified because not enough information is available to model them accurately.
Once a donor body is acquired more detail can be added.

## Battery Pack Placement

## Battery Modules


EV battery packs are often built to conform to the shape of the vehicle they came in.
Although the Travelall is large, because of the complex powertrain, space is at a premium and reusing an entire battery pack from an existing EV is not possible.
A custom battery pack(s) will be required for this project.

EV battery packs are made out of multiple battery modules.
Battery modules combine multiple battery cells in series and parallel into a component which is convenient for packaging, or connecting to a BMS (Battery Management System).
The characteristics to consider when selecting a battery module to build a pack are its voltage, capacity, dimensions, weight, cost, thermal management, and connection to a BMS.

This section will cover several battery modules and potential placement in the chassis.

### Nissan Leaf Battery Module

The Nissan Leaf battery modules are a common choice for EV conversions due to their high voltage and small size which lets them be packed into convenient locations.
Pre-2025 the Leaf only had passive battery thermal management meaning heat from the battery had to gradually dissipate to the exterior.
This resulted in high battery degradation due to overheating, but the batteries are very affordable which further contributes to their popularity.

The Leaf modules changed slightly over the years but the general specs are similar.

| Module Parameter | Value |
| --------- | ----- |
| Voltage | 7.6 V |
| Capacity | 500 Wh |
| Dimensions | 12" x 8.8" x 1.4" |
| Weight | 8.4 lbs |
| Approx. Cost | $21.76 buying in bulk from [greentec](https://greentecauto.com/hybrid-battery/repurposed-batteries/nissan-leaf/g2-nissan-leaf-lmo-7-6v-64ah-500wh-bulk-purchase/) |
| Thermal Management | Passive |
| BMS | No |
| Chemistry | NMC |

In order to meet the minimum pack capacity [requirement](system_design.md#capacity) roughly 48 modules are required, although greentec bulk used batteries appear to be de-rated and it may take up to 75 modules according to the bulk battery [listing](https://greentecauto.com/hybrid-battery/repurposed-batteries/nissan-leaf/g2-nissan-leaf-lmo-7-6v-64ah-500wh-bulk-purchase/).

48 modules in series results in a pack voltage of 364 V which is exactly the same at the OEM Leaf making this the perfect combo to use with a Leaf motor / inverter.
75 modules in series would be too high voltage so more realistically the pack would use 80 modules, with two parallel groups of 40 modules in series

| Pack Parameter | Using 48 modules (minimal degradation) | Using 80 modules (assuming degraded) |
| --------- | ----- | ----- |
| Voltage | 364.8 V (all modules in series) | 304 V (2 parallel groups of 40 in series) |
| Capacity | 24 kWh | 24.9 kWh |
| Weight | 403.2 lbs | 672 lbs |
| Cost | $1066 | $1618 |

The leaf batteries are a very affordable option to create a battery pack with a voltage high enough to run a PMSM motor / inverter but they have poor energy density, especially when buying used modules.

#### BMS

The Nissan Leaf battery modules require a centralized (sometimes called direct-monitoring) BMS.
The modules are simply energy storage and have no monitoring hardware or controller except at the pack level.
Reusing OEM BMSs is generally not possible without a lot of effort reverse engineering because they expect to receive specific CAN traffic from other modules in the vehicle which don't exist.
There are many aftermardet BMSs available like the [Orion BMS](https://www.orionbms.com/products/orion-bms-standard/) or [Thunderstruck BMS](https://www.thunderstruck-ev.com/bms/) for under $1500.

### BMW i3 Battery Module

The BMW i3 (2013-2016) battery modules are highly modular like the Leaf battery modules.
Also like the Nissan Leaf modules, each module has a relatively high voltage making it easy to hit the voltages required to run many PMSM inverters.

| Module Parameter | Value |
| --------- | ----- |
| Voltage | 44.4 V |
| Capacity | 2.7 kWh |
| Dimensions | 16.125" x 12.25" x 6" |
| Weight | 54 lbs |
| Approx. Cost | $225  from [greentec](https://greentecauto.com/hybrid-battery/repurposed-batteries/bmw-i3/bmw-i3-nmc-48v-63ah-3kwh-battery-module/) |
| Thermal Management | Active (at pack level) |
| BMS | Distributed |
| Chemistry | NMC |

The BMW i3 battery modules are designed to be used with a chill plate on the bottom to dissipate excess heat.
The original battery pack routed the AC lines under each module.
Given that the batteries are relatively inexpensive, a simple glycol and water coolant loop could be routed through custom chill plates to a radiator instead. 
If the battery temperatures are shown to be too high, a heat pump could be retrofitted to chill the coolant, rather than route refrigerant lines through the battery pack.

Eight battery modules would easily fit in the Travelall (432 lbs not including cooling) wired in series to make a 384v battery pack, but this would mean a total capacity of only 21.6 kWh, a little short of the 23.3 kWh battery capacity [required](system_design.md#capacity). The Nissan leaf battery pack was 384V, and it is possible that adding another module in series could result in a pack [voltage](https://www.diyelectriccar.com/threads/leaf-inverter-voltage-input-limits.206166/) higher than the Leaf inverter can handle.
It may not be possible to meet the pack capacity requirement, with the BMW i3 battery, but it comes close with efficient packaging and good performance.


### Tesla S/X Battery Modules

Tesla battery modules have built in cooling meaning there is no need to build in separate battery pack cooling.
Also means it's easier to put batteries in a couple different locations.
But they are low voltage meaning you need like 12 of them with more being even better.
Therefore minimum battery pack is 288 v, 63.6 kWh which is way bigger than we need capacity wise and heavy at 672 lbs.
Available for 1400+ from EV retailers but much cheaper and questionable battery life off ebay ~400 each with shipping

specs:
5.3 kWh
24v
56 lbs
27"x12"x3"
NCA

### 2012-2014 Rav 4 Batttery

2012-2014 Rav 4 EV batteries were made by tesla using the same 18650 cells and integrated liquid cooling loop as the model s/x but reconfigured into two different modules.

Small module specs:
configuration: 5s48p
capacity: 2.6 kWh
size: 23"x12"x3"
weight: 35 lbs
voltage 18.5V

Large module specs:
configuration: 12s48p
capacity: 6.39 kWh
size: 36"x12"x3"
weight: 75 lbs
voltage 44.4V


One small and one large could be layed end to end to make a single effective 17s48p module 59" long and 9 kWh, 110 lbs, 63V.
That's 5" longer than two S/X modules end to end which would be 10.6 kWh, 112 lbs, 48V. So slightly less efficient per kWh (maybe due to different rating systems from different sources), but would fit very nicely in the car, and also is a higher voltage (low voltage is the problem with tesla modules).
Three of these large + small combos on each side would be a 378V pack (good), 54 kWh pack (very good), 660 lbs in modules alone (heavy, but not bad for the capacity).




## Thermal Management

## BMS

## Charging
