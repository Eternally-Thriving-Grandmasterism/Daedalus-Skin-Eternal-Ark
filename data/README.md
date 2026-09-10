# data/ — machine-readable mirrors of locked numbers

**Owner:** Autonomicity Games Inc.
**Authority:** Ra-Thor + Permanent PATSAGi Councils under TOLC 8
**Contact:** info@Rathor.ai
**Proof Ladder:** Design / systems-engineering posture. Nothing in this directory is measured data.

Files here transcribe numbers that already exist in the prose documents. They add no new
numbers and no new architecture. The prose remains authoritative; if a value here disagrees
with its `source` document, the document wins and the data file is the bug.

| File | Mirrors | Checked by |
|------|---------|------------|
| [mass-budget-locked.toml](mass-budget-locked.toml) | Dry-mass band, category locks, 15.0 kt seed target, 0.05 c public floor, 0.055 c internal lock | [tests/test_mass_budget.py](../tests/test_mass_budget.py) |

## Rules

1. **Every quantity carries an explicit `unit`.** The test suite fails on a unitless quantity.
2. **Every quantity carries a `source`** naming the document it was transcribed from.
3. A quantity is either `kind = "point"` (has `value`) or `kind = "band"` (has `min` and `max`).
4. `disclosure` separates `public` from `internal`. The 0.05 c floor is public; the 0.055 c
   lock is internal. A test asserts they are different numbers, so collapsing one into the
   other is a red build rather than a silent edit.

## What a green build means

The locked numbers are mutually consistent: the 15.0 kt target sits inside the 12.4–20.15 kt
band, the 15.0 kt allocation sums to 15,000 t, planning values sit inside their locked bands,
and the 15 % change-rule trigger still equals 5,850 t + 15 %.

## What a green build does not mean

It does not confirm the 5,850 t CFRP habitat mass (WP-HF-01 Pass A, not run), the 450–750 t
shielding band (Pass B, not run), or MS-B deployment (Gate E1, no test article). It does not
make sustained D–³He ICF, industrial ³He supply, or multi-decade integrated reliability any
closer to demonstrated. See [TECHNOLOGY-READINESS-AND-REALISM.md](../docs/TECHNOLOGY-READINESS-AND-REALISM.md).

## Running locally

```bash
python3 -m unittest discover -s tests -t . -v
```

Requires Python 3.11 or newer (`tomllib`). No third-party dependencies.
