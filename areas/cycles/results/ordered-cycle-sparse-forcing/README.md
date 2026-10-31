---
id: ordered-cycle-sparse-forcing
kind: result
title: In an ordered cycle, few sorted height changes force an exponentially large minimum
status: formal
claim: >
  Raw odd-only 3x+q map. Let a primitive positive odd numerator cycle with m ≥ 2 states, minimum L,
  reduced denominator q, total A, D = 2^A − 3^m and maximum dyadic height B have circularly ordered
  normalised successor, and let J be one plus the number of adjacent height changes in sorted
  normalised order (the dyadic seam counts). Then L > 2^(ceil(m/J) − 1 − B) and
  q > (D/C_c)·2^(ceil(m/J) − 1 − B), with C_c the lower mechanical intercept of (A, m); for each
  zero-forcing run with exponent sum e_run ≥ its length, L > 2^(e_run − B) and q > (D/C_c)·2^(e_run − B).
  If moreover q ≤ L, then J ≥ B + 1. Every cycle of 3x+q satisfies δ = A·log 2 − m·log 3 ≤ m·q/(3L).
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [dyadic-order-lemma]
lean:
  - LeanLane.Cyc.OrdCycle.G1_first
  - LeanLane.Cyc.OrdCycle.G1_second
  - LeanLane.Cyc.OrdCycle.G1_second_c
  - LeanLane.Cyc.OrdCycle.G1_first_E
  - LeanLane.Cyc.OrdCycle.run_bound_E
  - LeanLane.Cyc.OrdCycle.run_bound_c
  - LeanLane.Cyc.OrdCycle.J_ge_height
  - LeanLane.Cyc.NarrowCycle.gap_recurrence
  - LeanLane.Cyc.OddCycle.D_mul_n_le
  - LeanLane.Cyc.OddCycle.log_identity
  - LeanLane.Cyc.OddCycle.G4
  - LeanLane.Cyc.OddCycle.L_mul_delta_le
certificates: [check_legacy_replay.py]
evidence:
  - "ORDER_RIGIDITY.md: the written proofs (ordered interface, Green comparison, sparse-forcing law (G1), (H1), (G4), controls, generic baselines)"
  - "check_order_rigidity.py, order_rigidity_audit.json, root_replay.json: main-lane finite checker, receipt and root replay record. The checker fails at its new path: it loads the corpus as HERE.parent/'C001/actual_cycles.json', the fixtures from experiments/phase6/ (cycle_fixtures.json, now in ../../../convergence/results/baseline-obligation-transfer-controls/, byte-identical), and pins C005/check_order.py and C005/order_audit.json by old path. Passed at be73a66 as experiments/cycle_spectrum/C006/check_order_rigidity.py (archive/legacy-checker-run-be73a66.md). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "c006b_erun_check.py, c006c_g4_check.py, c006d_g2_check.py, c006e_cc_check.py, c006f_order_word_check.py and their .json receipts: side-lane independent checks of Lean units R71-d and C006-b to C006-f. All fail at their new path: they import helper modules from their own folder (s1a_integer_cycle_check and s1b_run_start_gcd_check, now in ../ordered-gap-closed-form/ (B05); r71c_state_bound_check, now in ../mechanical-cycles-high-rational-controls/ (B12), and jterm_gap_check, now in ../ordered-gap-closed-form/ (B17)). Passed at be73a66 as reviews/side_lane/c006b_erun_check.py, c006c_g4_check.py, c006d_g2_check.py, c006e_cc_check.py, c006f_order_word_check.py (archive/legacy-checker-run-be73a66.md). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "../rotation-block-exclusion/c005_c006_order_check.py, parts (4)-(6): side-lane REFEREE check of C006 on the corpus"
  - "LITERATURE.md: inspected primary input for the analytic corollary and scoped comparisons; INDEPENDENT_REVIEW.md, ROOT_REVIEW.md: main-lane reviews; SIDE_REVIEW.md: the main lane's read of the side-lane feed; DELIVERY_STATUS.md: record of a failed publication attempt"
  - "delivery_checks.json, full_gate.json: historical delivery receipt and historical finite gate"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: ../rotation-block-exclusion/c005_c006_order_check.py
    scope: "Feed 2026-10-19 02:13, REFEREE C005 + C006 at main 1cb02fa: all 50 ordered normalised census cycles with q <= L satisfy L > 2^(ceil(m/J) − 1 − B) and B + 1 <= J; the q = 233 worked example (B = 1, J = 3, q > 208768/14501) reproduced. Feed 03:37 and later updates: VERIFIED Lean C006-a to C006-f, statement match and receipts checked"
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "C006 re-derived by hand with no error (feed 02:13, update 02:19): weighted identity, J >= B + 1, gap system with seam, sparse forcing; Lean units C006-a (iterations 22-29), C006-b, C006-c, C006-e verified"
    link: ../../../../archive/side-lane/FEED.md
aliases: [C006]
tags: [cycles, dyadic-order, sparse-forcing, complexity, formal]
---

# In an ordered cycle, few sorted height changes force an exponentially large minimum

## Statement

Use the raw positive odd-only map, without absorption. Represent a rational `3x+1` cycle by odd numerators `n_i` and common reduced denominator `q`, so `3n_i + q = 2^(a_i)·n_(i+1)` with exact `a_i ≥ 1`. Let `m > 1` be its primitive odd period, `A = Σa_i`, `L = min n_i`, `D = 2^A − 3^m`, `δ = A·log 2 − m·log 3 > 0`. Assume that the normalised successor preserves circular order ([`dyadic-order-lemma`](../dyadic-order-lemma.md)).

Remove powers of two to put each state into `[L, 2L)`, retaining its height `h_i = floor(log₂(n_i/L))`, and put `B = max h_i`. In sorted normalised order let `J` be one plus the number of adjacent height changes; the extra one is the dyadic seam, which cannot be discarded. Let `C_c` be the lower mechanical intercept of `(A, m)` (`C_lower(A, m)` in the report).

**Sparse-forcing law (G1).**

```
L > 2^(ceil(m/J) − 1 − B),
q > (D/C_c)·2^(ceil(m/J) − 1 − B).
```

An exact zero-forcing run improves the exponent from its length to the sum `e_run ≥` length of its one/two exponents: `L > 2^(e_run − B)` and `q > (D/C_c)·2^(e_run − B)` for each such run, checked without floating-point logarithms.

**Height bound (H1).** If also `q ≤ L`: chronological height rises by at most one at each odd step, so reaching height `B` from 0 visits all `B + 1` labels, and a sorted list with that many distinct labels has at least `B` changes:

```
J ≥ B + 1.
```

A separate height bound is therefore redundant when `J` is bounded.

**Logarithmic identity (G4)**, for every cycle (no order needed): multiplying the arrows,

```
δ = Σ_i log(1 + q/(3n_i)) ≤ m·q/(3L).
```

Combining (G4) with the first inequality of (G1) gives the third form `q > (3δ/m)·2^(ceil(m/J) − 1 − B)`; with an imported two-logarithm lower bound for `δ` this yields effective finiteness, recorded separately as [`ordered-cycle-height-change-growth`](../ordered-cycle-height-change-growth.md).

This is a restriction on the complexity of a possible cycle. It does not exclude any ordered denominator-one cycle.

## Proof

Written proof: [`ORDER_RIGIDITY.md`](ORDER_RIGIDITY.md) §3, "Proof of the elementary part". Legacy summary:

> For positive gaps scaled to integers, each edge without a height change satisfies `2^c·G_next = 3G`, with `c` equal to one or two. The successor rank shift visits every gap. Among its `J` runs there is one of length at least `ceil(m/J) − 1`; binary divisibility makes its first gap large.

In detail: with the sorted gaps `Δ_j`, `G_j = 2^B·Δ_j ∈ Z_(>0)` and forcing terms `T_j = 2^B(ε_[j+1] − ε_[j])` (seam included, `ε_[m] = 2ε_[0] = 2q`), the gap system is `2^(1 + 1_{j ≥ m−s})·G_((j+s) mod m) = 3G_j + T_j` (G3). Along a zero-forcing run of length `t`, `2^(e_run)·G_end = 3^t·G_start`, so `G_start ≥ 2^(e_run) ≥ 2^t`; the gaps are positive and sum to `L`, so each is below `L`, hence `G_start < 2^B·L`. The comparison `D·L ≤ q·C_c` comes from the weighted identity `D·L = q·C_h` with `C_h ≤ C_c` (the positive Green comparison (4) of `ORDER_RIGIDITY.md` §2). The cyclic pigeonhole on `J` forced positions gives a run of length `floor((m−1)/J) = ceil(m/J) − 1`.

## Lean

`lean/CycleSpectrum.lean`, Lean units C006-a, C006-b, C006-c and C006-e (legacy `lean/STATE.md`, now [`archive/lean-lane/STATE.md`](../../../../archive/lean-lane/STATE.md)). Axioms `propext`, `Classical.choice`, `Quot.sound`; receipts `lean/receipts/CycleSpectrum.*`. No external input.

The domain is the structure `OrdCycle m`: an `OddCycle` (odd periodic numerators, `n_0` the positive minimum, exact arrows `2^(a_i)·n_(i+1) = 3n_i + q`, heights bounded by `B`) whose scaled normalised states `Z_i` and images `F_i` satisfy `Z_i < Z_j ⇔ F_i < F_j` (the ordered hypothesis), with its exponent window, `m ≥ 2`, and distinct states over one period.

- `LeanLane.Cyc.OrdCycle.G1_first`: `2^((m−1)/J) < 2^B·n_0`, i.e. `L > 2^(ceil(m/J)−1−B)` (`(m−1)/J` is natural-number division, equal to `ceil(m/J) − 1`). `J` is the count of forced positions along the orbit, shown equal to one plus the sorted-height changes (`J_eq_changes`).
- `G1_second`: `D·2^((m−1)/J) < 2^B·q·C_h` with the true weighted intercept; `G1_second_c` (C006-e): the same with `C_c`, which is (G1)'s second inequality in C006's own form.
- `run_bound_E`, `G1_first_E` (C006-b): the `e_run` refinement, `2^(e_run) | Δ_(r₀)`, hence `2^(e_run) < 2^B·n_0` with `e_run ≥ t`; `run_bound_c`: `D·2^(e_run) < 2^B·q·C_c` for each zero-forcing run.
- `J_ge_height`: under `q ≤ n_0` and all `a_i ≥ 1`, `h_j + 1 ≤ J` for every `j`, i.e. (H1).
- `NarrowCycle.gap_recurrence`: the gap system (G3) with its seam; `OddCycle.D_mul_n_le`: `D·L ≤ q·C_c`.
- `OddCycle.log_identity` and `OddCycle.G4` (C006-c): (G4) over ℝ for every `OddCycle` (any `q`, no order or reducedness hypothesis); `L_mul_delta_le`: the cleared form `3Lδ ≤ m·q`.

The Lean (G1) needs neither `q ≤ L` nor reducedness; the prose states the domain `q ≤ L`, which only (H1) uses. The third form of (G1) is not stated as one declaration; it is the one-line combination of `L_mul_delta_le` and `G1_first`, and is therefore not part of this node's claim.

## Remarks

- **Worked example.** The actual `q = 233` cycle `1663, 2611, 4033, 3083, 4741, 1807, 2827, 4357` has valuations `(1,1,2,1,3,1,1,3)`, `B = 1`, `J = 3`. A zero-forcing run has length five and exponent sum eight, giving `q > 208768/14501`, i.e. `q ≥ 15`. The height-histogram bound of [`generic-cycle-minimum-baselines`](../generic-cycle-minimum-baselines/README.md) gives only `q ≥ 2` on that profile. Both permit the actual cycle.
- **Structure.** Every wide ordered cycle has a descent in its sorted height list (from `H_((j+s) mod m) − H_j ≤ 1_{j ≥ m−s}`); a necessary condition, not an exclusion.
- **What it does not do.** It leaves finite exceptions and profiles whose number of height changes grows; it does not exclude every ordered denominator-one cycle or prove finiteness at a fixed denominator without the change-count bound. The remaining bridge is the congruence of [`ordered-cycle-denominator-one`](../../questions/ordered-cycle-denominator-one.md); failed shortcuts are in [`ordered-cycle-shortcuts`](../../attempts/ordered-cycle-shortcuts/README.md) and [`mechanical-normalized-word-transfer`](../../attempts/mechanical-normalized-word-transfer.md); the one-defect case is [`one-height-defect-ordered-cycles`](../../questions/one-height-defect-ordered-cycles.md).
- **Literature.** T. Brox, *Collatz cycles with few descents* (Acta Arith. 92, 2000) counts descending odd states chronologically; `J` counts changes of dyadic height in sorted normalised rank, including the seam. The counts are different; no domination or record improvement is claimed. Topological rotation-number language (Milnor) retains no arithmetic denominator exclusion. Novelty undetermined. See [`LITERATURE.md`](LITERATURE.md).
- **Finite evidence.** The checker covered all 2,459 stored source cycles at 333 parameters, their 1,184 distinct normalised cycles and all eleven raw fixtures. Fifty nontrivial normalised cycles satisfy the order domain, forty-six of them wide. A separate exhaustive grid constructs 360,618 legal odd cycles and distinguishes minimum-phase failure, height inconsistency and order failure; exactly 317,459 profiles meet the ordered domain. Finite success is not a proof for untested periods or heights.

## History

- Migrated from `experiments/cycle_spectrum/C006/` (legacy ID `C006`; `REPORT.md`, proof `ORDER_RIGIDITY.md`) at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). The side-lane checks `reviews/side_lane/c006b`–`c006f_*` moved here. Parts became [`ordered-cycle-height-change-growth`](../ordered-cycle-height-change-growth.md), [`generic-cycle-minimum-baselines`](../generic-cycle-minimum-baselines/README.md), [`ordered-cycle-shortcuts`](../../attempts/ordered-cycle-shortcuts/README.md), [`mechanical-normalized-word-transfer`](../../attempts/mechanical-normalized-word-transfer.md) (with C005) and [`one-height-defect-ordered-cycles`](../../questions/one-height-defect-ordered-cycles.md).
- Main lane (ChatGPT/Codex), 2026-10-19. The sole textual slip found in review: the proof referred to the "second" inequality of (G1) after using the product identity, which proves the **third**; corrected before the review note was saved. A receipt-format issue was corrected (`ROOT_REVIEW.md`); not a mathematical correction. The first publication attempt failed (approval review at capacity, [`DELIVERY_STATUS.md`](DELIVERY_STATUS.md)); C005 and C006 were published together in commit `1cb02fa`.
- Formalised by the Lean lane (Claude Lean lane, Fable), 2026-10-19: C006-a (iterations 22–29), C006-b (50), C006-c (51), C006-e (54); C006-d and C006-f are recorded in [`ordered-cycle-height-change-growth`](../ordered-cycle-height-change-growth.md) and [`dyadic-order-lemma`](../dyadic-order-lemma.md).
