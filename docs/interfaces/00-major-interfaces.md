# Major Subsystem Interfaces — High-Level Control Document

**Status:** Baseline (WP-06 complete)  
**Owner:** Autonomicity Games Inc.  
**Last Updated:** 2026-08-11

This document records the primary interfaces between major systems so that humans and AI agents can maintain consistency as detailed design proceeds.

## 1. Propulsion ↔ Power

- Shared or closely coupled fusion reactors
- High electrical power draw during ignition / nozzle operation
- Thermal rejection shared or coordinated with ship radiators
- Control authority: propulsion burn requests must be validated against power availability and TOLC 8 safety

## 2. Propulsion ↔ Structure / Shielding

- Thrust loads transmitted through primary structure
- Forward particle shield must remain clear of exhaust and magnetic sail interactions
- Magnetic nozzle and magsail fields must not interfere destructively with active radiation shielding

## 3. Habitat (Rotating) ↔ Non-Rotating Spine

- Mechanical: bearings, seals, transfer mechanisms (elevators / airlocks / despin systems)
- Power, data, and fluid transfer across rotating interface
- Safety isolation capability in both directions

## 4. Life Support ↔ Habitat & Structure

- Atmosphere, water, and nutrient loops distributed throughout living volumes
- Water storage deliberately co-located for radiation shielding benefit
- Thermal and humidity control integrated with habitat environmental systems
- Emergency isolation of habitat sections without total loss of life support

## 5. Life Support ↔ Power

- Continuous multi-megawatt lighting and processing loads
- Priority power allocation under emergency conditions (life support near top of hierarchy)

## 6. Shielding ↔ All Habitable Volumes

- Passive mass and active magnetic systems must cover all long-duration occupancy areas
- Storm shelters with enhanced protection and independent life support buffers

## 7. Governance / Control ↔ All Systems

- PATSAGi / Ra-Thor lattice has monitoring and recommendation authority on all critical systems
- Human override remains ultimate
- All major mode changes (burn, spin-up, sail deployment, habitat isolation, etc.) require logged decision records

## 8. Manufacturing / ISRU ↔ Structure & Propulsion

- Future in-space manufacturing must interface with docking, power, and material handling systems
- Propellant loading and tank integration points defined early

---

**Rule:** Any detailed design change that affects an interface above must update this document and the relevant subsystem files. New interface control documents for lower-level assemblies will be added as design matures.
