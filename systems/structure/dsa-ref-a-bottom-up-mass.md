# DSA-Ref-A — Bottom-Up Structural Mass Estimate Framework

**Status:** Detailed estimation framework  
**Reference Design:** DSA-Ref-A (~140 m spin radius, ~300 people)  
**Owner:** Autonomicity Games Inc.  
**Last Updated:** 2026-08-11

## 1. Purpose

Move from the previous wide-range structural mass allocation toward a more traceable, bottom-up estimate that can be refined with actual material properties and load cases.

## 2. Major Structural Elements

| Element | Description | Mass Drivers |
|---------|-------------|--------------|
| Primary rotating pressure vessel / hull | Cylindrical or toroidal living volume | Radius, length, internal pressure, material allowable, safety factor |
| Radial and longitudinal stiffeners | Frames, stringers, bulkheads | Buckling resistance under spin loads + acceleration |
| Floor / deck systems | Habitable decks at design gravity level | Live load, partition loads, equipment |
| Spin bearings & transfer structures | Interface to non-rotating spine | Loads, redundancy, sealing |
| Non-rotating spine | Propulsion, tanks, power, docking | Thrust loads, tank support, docking interface |
| Tankage (structural contribution) | Propellant and water tanks | Pressure, volume, material |
| Radiators & external structures | Thermal rejection, magsail attachment | Area, stiffness, thermal cycling |

## 3. Load Cases That Dominate Mass

1. Steady spin (centrifugal loading of the entire rotating habitat)
2. Spin-up / spin-down transients
3. Residual axial acceleration during fusion burn
4. Docking and berthing loads
5. Internal pressure + meteoroid / debris impact factors
6. Thermal gradients and cyclic loading over decades

## 4. Estimation Approach

- Begin with pressure-vessel sizing for the rotating habitat (thin-wall or stiffened-shell formulas)
- Add stiffening mass fraction calibrated to aerospace practice and large-space-structure studies
- Add deck and outfitting structural contribution
- Add dedicated spin-interface and spine mass
- Apply overall contingency (initially 25–40%) for unknowns at this stage

## 5. Current Working Guidance

Until a full finite-element model exists, the structural + rotating habitat portion of the dry mass budget should be treated as still carrying large uncertainty. Design effort should prioritize:

- High specific-strength materials
- Efficient load paths
- Minimizing non-structural mass inside the rotating section
- Designing the spin interface for inspectability and replacement

## 6. Next Concrete Steps

- Select reference material allowables (composites vs. metallic options)
- Produce a first analytical pressure-vessel + stiffener mass for a 140 m class cylinder of defined length
- Estimate bearing/transfer system mass from analogous large rotating machinery scaled to space
- Reconcile the bottom-up number with the top-level mass budget and update it

---

**This framework is the starting point for replacing the wide structural mass range with a traceable estimate.**
