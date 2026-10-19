# Explicit Tao

**Status: closed. Leg 1 ended at a scoped barrier** (2026-10-18).

**Goal.** Make Tao (2019) explicit: compute `C(δ)` such that all but density `δ` of integers dip below `C(δ)`, and compare it with the verified range.

**Outcome.**
- L2–L3: written proof with a finite certificate.
- L4: the printed architecture is vacuous unless `log x > 6.27·10^13`. The claim that re-optimisation cannot help is a candidate (`open`).
- L5–L6 and Legs 2–3: not started.

- [`STATE.md`](STATE.md): the plan, lemma table and decisions. [`LOG.md`](LOG.md): the log. [`lemmas/`](lemmas/): the lemma notes.
- Checks: [`check_L2.py`](check_L2.py) and [`check_L4_window.py`](check_L4_window.py), with receipts in [`receipts/`](receipts/).

Verify: `python3 scripts/run_checks.py --line explicit_tao`.
