---
id: global-drift-ceiling
kind: result
title: "The global-drift ceiling: log₂(n_k/L) ≤ k·log₂(3/2) − X_k + δ at every q, with no hypothesis on L/q"
status: formal
claim: >
  Odd-only 3x+q map, any odd q > 0 (more generally any positive odd cycle with letters ≥ 1). For a cycle
  n_0, …, n_(m−1) with minimum L = n_0, total A, drift δ = A − m·log₂3 and excess X_k = Σ_(i<k)(a_i − 1),
  every index 0 ≤ k ≤ m satisfies log₂(n_k/L) ≤ k·log₂(3/2) − X_k + δ, exactly as n_k·2^(A_k)·3^m ≤
  L·3^k·2^A in integers. In particular the log-height satisfies B = log₂(n_max/L) ≤ (m − 1)·log₂(3/2) + δ.
  No hypothesis on L/q is needed; the per-step ceiling of cycle-height-ceiling is small only when L ≫ mq.
authors:
  - Claude side lane (Opus)
created: 2026-10-19
lean:
  - LeanLane.Cyc.OddCycle.Cpre_mul_pow_le
  - LeanLane.Cyc.OddCycle.global_drift
  - LeanLane.Cyc.OddCycle.Apre_eq_excess_add
  - LeanLane.Cyc.OddCycle.global_drift_log
  - LeanLane.Cyc.OddCycle.h_le_drift
  - LeanLane.Cyc.OddCycle.B_le_drift
evidence:
  - "Checked numerically as an ingredient of ../two-three-mismatch-denominator-laws/s9_denominator_law.py (see that node)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed S9 entry, update 13:29: reviewed S9 and found no hidden q = 1; the closing identity is C006-c's formal log_identity; the drift caveat is intrinsic. Lean unit S9-a verified (iteration 76)"
tags: [cycles, height, drift, 3x+d, formal]
---

# The global-drift ceiling: log₂(n_k/L) ≤ k·log₂(3/2) − X_k + δ at every q, with no hypothesis on L/q

## Statement

Take any primitive positive odd cycle of the odd-only `3x+q` map, `q` odd, with arrows `2^(a_i) n_(i+1) = 3n_i + q`, letters `a_i ≥ 1`, period `m`, total `A`, `D = 2^A − 3^m > 0` and minimum `L = n_0` (index 0 at the minimum). Put `A_k = Σ_(i<k) a_i`, the excess `X_k = Σ_(i<k)(a_i − 1) = A_k − k`, and the drift `δ = δ(w) = A − m·log₂3` (in bits, as in [`conventions/NOTATION.md`](../../../conventions/NOTATION.md)).

For every `0 ≤ k ≤ m`:

```
log₂(n_k / L) ≤ k·log₂(3/2) − X_k + δ,
```

equivalently `n_k·2^(A_k)·3^m ≤ L·3^k·2^A`. Hence the log-height `B = log₂(n_max/L)` satisfies `B ≤ (m − 1)·log₂(3/2) + δ`.

## Proof

Legacy S9 note §1 (side lane), lightly edited. The closing identity says the per-step errors sum exactly:

```
Σ_(i<m) log₂(1 + q/(3n_i)) = log₂(2^A/3^m) = δ(w).
```

Since every term is positive, any partial sum is at most `δ`, and telescoping `log₂ n_(i+1) − log₂ n_i = log₂3 − a_i + log₂(1 + q/(3n_i))` from the minimum gives the ceiling. The Lean proof goes through integers instead: the exact prefix identity `2^(A_k) n_k = 3^k n_0 + q·C_k` and the closing identity `(2^A − 3^m) n_0 = q·C_m`, with `3^j·C_k ≤ C_(k+j)` (`C_k/3^k` nondecreasing).

The per-step ceiling of [`cycle-height-ceiling`](cycle-height-ceiling.md) (S6-a/S7) carries the error as `k·log₂(1 + q/(3L))`, which is small only when `L ≫ mq`. Both ceilings are theorems, so the general form is `log₂(n_k/L) ≤ k·log₂(3/2) − X_k + min(δ, k·log₂(1 + q/(3L)))`.

## Lean

`lean/CycleSpectrum.lean`, Lean unit S9-a (iteration 76; axioms `propext`, `Classical.choice`, `Quot.sound`; receipts `lean/receipts/CycleSpectrum.*`), namespace `LeanLane.Cyc.OddCycle`:

- `Cpre_mul_pow_le`: `3^j·C_k ≤ C_(k+j)`.
- **`global_drift`**: for `k ≤ m`, `n_k·2^(A_k)·3^m ≤ n_0·3^k·2^A` in `ℤ`, from the prefix and closing identities; any `q > 0`, no hypothesis on `L/q`.
- `Apre_eq_excess_add`: `A_k = X_k + k` for letters `≥ 1`.
- **`global_drift_log`**: `log n_k + X_k·log 2 ≤ log L + k·log(3/2) + δ_nat`, with `δ_nat = A·log 2 − m·log 3`, natural logarithms, `k ≤ m`.
- `h_le_drift`, **`B_le_drift`**: with the height attained, `B·log 2 ≤ (m − 1)·log(3/2) + δ_nat`.

**Statement match.** Dividing `global_drift_log` by `log 2` gives the Statement, with `δ = δ_nat/log 2`. The `OddCycle` structure indexes from the minimum, as here. Nothing is assumed about `L/q`, the gap or the period.

## Remarks

- **Where it is used.** It is the one change that turns S6/S7 into denominator laws at every `q`: [`two-three-mismatch-denominator-laws`](two-three-mismatch-denominator-laws/README.md). It is also the ceiling of the repeat bound [`cycle-word-repeat-bound`](cycle-word-repeat-bound/README.md).
- **The caveat is intrinsic** (the Lean lane's review). For words with `L ≲ q` (cycles living at scale `q`) the drift can be linear in `m`, and then the ceiling is weak. Narrow words with all states in `[L, 2L)` already have drift `≥ m·log₂(1 + q/(6L))`. At `q = 1` with `L > 2^71` the drift is tiny.

## History

- Split from the legacy S9 note `experiments/cycle_spectrum/S09/DENOMINATOR_LAW.md` §1 (legacy ID `S09`; side-lane producer batch S9, 2026-10-19) at commit `be73a66`, by the B06 migration (Claude, Opus 5.5). The rest of the note is [`two-three-mismatch-denominator-laws`](two-three-mismatch-denominator-laws/README.md) and [`cycle-word-repeat-bound`](cycle-word-repeat-bound/README.md).
- Side lane (Claude, Opus), feed 2026-10-19 13:22 (LEAD, S9). The Lean lane checked the preview and offered the ceiling as a one-lemma variant of `n_mul_pow_excess_le`; its review (13:29) found no hidden `q = 1`. Formalised as Lean unit S9-a, verified at 14:46 (Lean-lane commit `bb8627b`).
