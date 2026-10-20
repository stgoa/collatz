---
id: generic-cycle-minimum-baselines
kind: result
title: Order-free baselines for cycle minima and denominators (extremal, packing, product)
status: written
claim: >
  Raw odd-only map, any positive cycle (no order assumed) with odd numerators n_i, reduced
  denominator q, totals (A, m), D = 2^A − 3^m. (8) min n_i ≤ q·C_lower(A, m)/D, strictly unless the
  word is a rotation of the lower mechanical word. With r_h the number of states of dyadic height h,
  B the maximum height, P = max(2r_0 − 1, max_(1≤h≤B) ceil(r_h/2^(h−1))) and P_odd the least odd
  integer ≥ P: (9) q ≥ ceil(P_odd·D/C_lower(A, m)); (10) m ≤ ((2^(B+1) − 1)L + 1)/2 and
  q ≥ ceil((2m − 1)·D/((2^(B+1) − 1)·C_lower(A, m))). (11) 2^A/3^m = Π(1 + q/(3n_i)) ≤
  Π_(j<m) (1 + q/(3(L + 2j))).
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: []
evidence:
  - "../ordered-cycle-sparse-forcing/ORDER_RIGIDITY.md, section 5: the written proofs"
  - "../ordered-cycle-sparse-forcing/INDEPENDENT_REVIEW.md: main-lane review (the generic extremal argument and odd-lattice capacities are valid without circular order)"
tags: [cycles, baselines, extremal, packing]
---

# Order-free baselines for cycle minima and denominators (extremal, packing, product)

## Statement

For an arbitrary positive valuation word `a` with totals `(A, m)`, a cycle with odd numerators `n_i`, reduced denominator `q`, minimum `L`, and `C_lower(A, m)` the intercept of the lower mechanical word:

1. **Generic extremal bound.**

```
min_i n_i ≤ q·C_lower(A, m)/(2^A − 3^m),          (8)
```

strictly if the word is not a rotation of the lower mechanical word.

2. **Odd-lattice packing.** Let `r_h` count states of dyadic height `h`, `B = max h_i`. The available normalised positions in `[L, 2L)` number at most `(L+1)/2` at height zero and `2^(h−1)·L` at height `h ≥ 1`. With `P = max(2r_0 − 1, max_(1≤h≤B) ceil(r_h/2^(h−1)))` and `P_odd` the least positive odd integer `≥ P`, `L ≥ P_odd`, and with (8)

```
q ≥ ceil(P_odd·D/C_lower(A, m)).                   (9)
```

Summing the capacities instead gives

```
m ≤ ((2^(B+1) − 1)·L + 1)/2,
q ≥ ceil((2m − 1)·D/((2^(B+1) − 1)·C_lower(A, m))).   (10)
```

3. **Product baseline.** Because the `n_i` are distinct odd integers,

```
2^A/3^m = Π_i (1 + q/(3n_i)) ≤ Π_(j=0)^(m−1) (1 + q/(3(L + 2j))).   (11)
```

## Proof

[`ORDER_RIGIDITY.md`](ordered-cycle-sparse-forcing/ORDER_RIGIDITY.md) §5. For (8): put `b_j = A_j − j·A/m`, extended periodically, and rotate the word to an index where `b_j` is maximal; every rotated prefix then obeys `A'_j ≤ floor(jA/m)`, and termwise comparison of the intercepts gives (8). (9)–(10) count odd positions; (11) multiplies the arrows.

## Remarks

- **Not order-specific.** These all-size inequalities can exclude denominator 1 for specified `(A, m, B)` or height histograms. Their arithmetic content is the odd lattice and the generic extremal bound, not the successor rank order. They are weak near the critical regime `2^A/3^m ≈ 1` and do not exclude all ordered integer cycles. (11) can dominate the packing restriction. Any claim of an order-based denominator gain must be compared with (8)–(11), not only with the mechanical-word gcd theorem; for example on the `q = 233`, `B = 1`, `J = 3` profile of [`ordered-cycle-sparse-forcing`](ordered-cycle-sparse-forcing/README.md) the histogram bound gives only `q ≥ 2`, against `q ≥ 15` from the order-based run bound.
- **Literature.** (8) is consistent with the published mechanical extremal direction (Christoffel words maximise the cycle minimum: [`halbeisen-1997-rational-cycles`](../../../sources/halbeisen-1997-rational-cycles.md), and the Fernández–Ibáñez 2026 preprint); it is recorded as a generic comparison, not as a new consequence of order. Novelty not claimed.
- **Status.** `written`: reviewed only within the main lane.

## History

- Split from `experiments/cycle_spectrum/C006/` (legacy ID `C006`; `ORDER_RIGIDITY.md` §5, `REPORT.md` "A concrete gain and the comparison baseline") at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19.
