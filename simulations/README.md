# Simulations & Analysis

This directory will hold physics models, trajectory calculations, mass/energy budgets, life support balances, structural analyses, and related computational work.

## What Can Be Run Today

Nothing in this directory has been solved by a physics code. See the
[HF-01 CI capability card](hf-01-ci-capability-card.md) for the inventory: no FEA solver and no
Monte-Carlo transport code is available to this repository's CI, and Gate E1 needs hardware.
All three WP-HF-01 passes are **not run**.

The one executable piece is `tools/hf01_pass_a_toy.py`, closed-form membrane arithmetic that
reproduces [hf-01-pass-a-analytical-sanity.md](hf-01-pass-a-analytical-sanity.md). It is not FEA
and it refuses to emit a recommended habitat mass.

## Planned Contents
- Rocket equation and staging calculators
- Trajectory and time-of-flight models
- Closed-loop life support mass flow simulations
- Radiation transport / shielding effectiveness studies
- Structural load and spin dynamics models
- Thermal / radiator performance estimates

All models remain under Autonomicity Games Inc. ownership and are developed under PATSAGi / TOLC 8 oversight.
