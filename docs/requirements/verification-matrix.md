# System Requirements Verification & Traceability Matrix

**Status:** Baseline matrix  
**Reference Design:** DSA-Ref-A  
**Owner:** Autonomicity Games Inc.  
**Last Updated:** 2026-08-11

This matrix links top-level system requirements to the design artifacts that satisfy them and to the planned verification methods.

| Req ID | Requirement Summary | Primary Design Artifacts | Planned Verification |
|-------|---------------------|--------------------------|----------------------|
| SR-1 | Continuous / near-continuous D–³He ICF propulsion with magnetic nozzle; 0.05–0.12 c class capability | performance-model.md, dsa-ref-a-propellant-model.md, ADR-0001 | Analysis + ground endurance tests (Thread A) + FT-2 |
| SR-2 | Artificial gravity 0.8–1.0 g via rotation; population path from Seed to larger ships | spin-radius-analysis.md, ADR-0002, reference-seed-vessel.md, deck-layout.md | Analysis + subscale spin tests (Thread B) + FT-1 |
| SR-3 | Near-closed-loop life support for multi-year operation | mass-balance.md, dsa-ref-a-life-support-tables.md, dsa-ref-a-fmea-life-support.md | Ground closed-loop campaigns (Thread C) + FT-1/FT-4 |
| SR-4 | Multi-layer radiation/particle shielding + self-healing Daedalus-Skin | shielding docs, daedalus-skin-requirements.md, dose-trade.md | Analysis + material testing (Threads D & F) |
| SR-5 | Triple redundancy / graceful degradation on critical systems; single-failure survivability | safety-case.md, all FMEA documents, integrated-risk-picture.md | FMEA + fault-injection testing + design reviews |
| SR-6 | Permanent PATSAGi / TOLC 8 governance with human sovereignty | TOLC8-decision-protocol.md, COLLABORATION.md, PHASE-STATUS.md | Process audits + decision record reviews |
| SR-7 | Staged construction path; Seed Vessel as practical first step | seed-vessel.md, reference-seed-vessel.md, development-roadmap.md, flight-test-program.md, industrial-capacity-analysis.md | Program reviews + progressive flight-test gates |

## Usage Rule

Any change that affects satisfaction of an SR must update both the relevant design artifact and this matrix. Verification evidence is accumulated against the Technology Maturation Milestones and Flight-Test Program.

---

**This matrix is the living traceability link between requirements and realization.**
