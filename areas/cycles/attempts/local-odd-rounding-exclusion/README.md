---
id: local-odd-rounding-exclusion
kind: attempt
title: Excluding ordered denominator-one cycles by integer rounding of the complete sorted gaps
status: reviewed
claim: >
  Tried, toward excluding ordered denominator-one cycles of the raw odd-only 3x+1 map: pass from
  sorted normalised states to the complete dyadic gap system (seam included) and use exact odd
  spacing and integer rounding of the gaps to force a lower bound on the reduced denominator.
  Verdict: rejected. The complete gap lattice is unimodularly equivalent to the state lattice, so
  exact gap integrality is the original problem; and the necessary local spacing inequalities, with
  all their nonnegative linear combinations and odd rounding, are satisfied with arbitrarily large
  slack by noninteger rational cycles at additive parameter 1 (the q = 5 cycle 19 → 31 → 49 divided by
  5, and the primitive mechanical cycles of every size with seam gap 3^(m−1)/D). No cycle is excluded.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [complete-gap-lattice-equivalence, odd-spacing-rounding-bound, narrow-cycles-are-mechanical, ordered-cycle-sparse-forcing, mechanical-word-exact-denominator]
certificates: [c010_gap_check.py]
evidence:
  - "GAP_LATTICE.md: the lattice equivalence (sections 1-2), the unchanged ordered operator (section 3), what integrality still accomplishes (section 4) and the all-size slack family (section 5); ODD_ROUNDING.md: the rounding bound and the q = 5, 13, 83 controls; ROUNDING_PROBE.md: independent main-lane lowbit argument and seam audit"
  - "check_integer_gaps.py, integer_gap_audit.json: main-lane checker and receipt (2,459 source cycles, 1,185 normalised, 52 ordered cases, 474 adjacent gap equations, 7,022 circular pair bounds). Fails at its new path: it imports HERE.parent/'C009/check_excursions.py' and hashes ../C004/SIZE_PROBE.md by old path. Passed at be73a66 as experiments/cycle_spectrum/C010/check_integer_gaps.py (archive/legacy-checker-run-be73a66.md)"
  - "c010b_gap_lattice_check.py, c010b_gap_lattice_check.json and c010c_any_arrangement_check.py, c010c_any_arrangement_check.json: side-lane checks of Lean units C010-b and C010-c. Both fail at the new path: they import the side-lane helper modules s1a_integer_cycle_check and jterm_gap_check from their own folder; s1a_integer_cycle_check now lives in ../../results/ordered-gap-closed-form/ (B05), jterm_gap_check in legacy reviews/side_lane/ (a later batch). Passed at be73a66 as reviews/side_lane/c010b_gap_lattice_check.py and c010c_any_arrangement_check.py; their receipts are written only when an output path is given"
  - "check_delivery.py, delivery_checks.json: historical delivery check and receipt; pinned to the historical commits that produced it, fails at HEAD by design (it failed at be73a66 too)"
  - "ARITHMETIC_REVIEW.md, INDEPENDENT_REVIEW.md, EXACT_CHECKER_REVIEW.md, ROOT_REVIEW.md: main-lane reviews; SIDE_REVIEW.md: the main lane's read of the side-lane feed; LITERATURE.md: literature scope; historical_gate.json: historical finite gate"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: c010_gap_check.py
    scope: "Feed 2026-10-19 03:39, REFEREE C010 at main cae57b0: E^m = 2I and the integer inverse of U for m ≤ 12, the q = 5 control passing the sharp bounds, and the seam identity 2B_0 − B_(m−1) = 3^(m−1) on all 381 primitive mechanical words with 2 ≤ m < 30; rejection confirmed"
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed 03:49: GAP_LATTICE.md, ODD_ROUNDING.md and ROUNDING_PROBE.md read in full, no error; unimodular inverse, |det(2E^s − 3I)| = 2^(m+s) − 3^m, the seam identity, every pair bound and every number in the q = 5, 13, 83 controls re-derived. Two precision remarks (distinct Z_j also needs primitivity; the determinant formula needs gcd(s, m) = 1, supplied by the ordered structure)"
aliases: [C010]
tags: [cycles, dyadic-order, gap-lattice, rounding, rejected-mechanism]
---

# Excluding ordered denominator-one cycles by integer rounding of the complete sorted gaps

## Idea

After [`excursion-compression`](../excursion-compression/README.md), the next bounded mechanism toward [`ordered-cycle-denominator-one`](../../questions/ordered-cycle-denominator-one.md) was **global integer rounding in the complete sorted-gap system**: keep every height, odd-state condition and the dyadic seam, and turn exact integer rounding of the gaps into a lower bound on the reduced denominator. A useful cut had to distinguish the integer lattice from the rationally rescaled `q = 5` and `q = 13` controls and yield more than `D | C_h`. Raw odd-only clock, no absorber.

## What happened

**1. Complete gaps preserve the whole obstruction** ([`complete-gap-lattice-equivalence`](../../results/complete-gap-lattice-equivalence.md), formal). The gap map `U = E − I` is unimodular, so states and gaps are integral together and have the same gcd and least common denominator. For ordered cycles the state system is `K·Z = q·p` with `K = 2E^s − 3I` (written, [`GAP_LATTICE.md`](GAP_LATTICE.md) §3); `U` and `K` are both polynomials in `E`, so they commute and the gap system `K·G = q·U·p` is the same linear operator in other coordinates, with `|det K| = D = 2^(m+s) − 3^m` (the rank permutation is one `m`-cycle; `gcd(s, m) = 1` by the ordered structure). In modular indices this is the recurrence of [`ordered-cycle-sparse-forcing`](../../results/ordered-cycle-sparse-forcing/README.md), `2^(1 + 1_(j ≥ m−s))·G_((j+s) mod m) = 3G_j + q(p_(j+1) − p_j)` with `p_m = 2p_0`; the seam is correct as stated there. Summing gives `2Σ_(j<s) G_j − Σ_j G_j = q·2^B`, which is exactly the minimum arrow `2Z_s = 3Z_0 + q·2^B`, not a second constraint.

**2. Integrality is the original problem** ([`GAP_LATTICE.md`](GAP_LATTICE.md) §4, written). For legal profiles (positive rational `Z`, prescribed heights with `H_0 = 0`, legal valuations `a_i = c_i + h_i − h_(i+1) ≥ 1`, odd positive parameter), integral gaps force integral states by unimodularity, then integer odd numerators, and `lowbit(Z_j) = p_j` automatically. So all exact gap integrality retains the original integer-cycle problem, oddness included; necessary spacing inequalities are a relaxation. This is not an impossibility theorem for integer cutting planes: eliminating a single profile to its exact fractional solution can certify its non-integrality; the missing step is uniformity over unrestricted legal profiles. [`ROUNDING_PROBE.md`](ROUNDING_PROBE.md) derives the same independently; the invalid affine loop `4 → 13 → 5 → 4` shows why valuation zero must stay excluded.

**3. The relaxation keeps genuinely nonintegral cycles** ([`ODD_ROUNDING.md`](ODD_ROUNDING.md) §4). The sharp local bounds and their sum, [`odd-spacing-rounding-bound`](../../results/odd-spacing-rounding-bound.md) (formal), are necessary but do not separate:

- The actual ordered `q = 5` cycle `n = (19, 31, 49)`, `a = (1,1,3)`, chronological heights `(0,0,1)`, sorted `H = (0,1,0)`, `D = 5`, `C_h = 19`, divided by 5, is an exact rational cycle at additive parameter 1 with sorted normalised `z = (19/5, 49/10, 31/5)`, images `F = (62/5, 76/5, 98/5)` and complete gaps `Δ = (11/10, 13/10, 7/5)`, each above its parameter-one bound `(1/2, 1/2, 1)`. Also `R_1(H) = 2 < L/q = 19/5`, `V(H) = 1/2`, `Γ_1(H) = 11/6`, and the bound (4) gives only `q ≥ 55/109`. Odd-rounding `R_1` to 3 is still below `19/5`; the only nonadjacent same-annulus pair has difference `12/5 ≥ 2`.
- The ordered `q = 13` five-cycle `(283, 431, 653, 493, 373)`, sorted heights `(0,1,0,0,0)`, has parameter-one gaps `(87/26, 93/26, 58/13, 62/13, 73/13)` above `(1/2, 1/2, 2, 2, 1)`; `R_1 = 6 < 283/13`, odd-rounded 7.
- The bound is not vacuous: the ordered `q = 83` cycle `(157, 277, 457, 727, 283, 233, 391)`, sorted heights `(0,2,1,1,0,0,0)`, has `R_1 = 15/2 > 157/83`, so its additive-one rational shape fails the relaxation; the rounded bound gives `q ≥ 2407/545 > 4`.

**4. Arbitrarily large slack at every size** ([`GAP_LATTICE.md`](GAP_LATTICE.md) §5, written). For coprime `A, m` with `m ≥ 2`, `2^A > 3^m` and positive mechanical valuations, the phase intercepts `B_l = Σ_j 3^(m−1−j)·2^floor((jA+l)/m)` give the increasing rational cycle `x_l = B_l/D` with zero height profile (`B_(m−1) < 2B_0`). For `j ≥ 1`, `jA mod m ≠ 0`, so changing `l` from 0 to `m − 1` raises each such floor by one while the `j = 0` term stays `3^(m−1)`:

```
B_(m−1) = 2B_0 − 3^(m−1),      2x_0 − x_(m−1) = 3^(m−1)/D.        (6)
```

With `ε = A − m·log₂3 > 0` every complete gap, seam included, exceeds `3^(m−1)/(2D) = 1/[6(2^ε − 1)]`, using the interior-increment bound of [`narrow-cycles-are-mechanical`](../../results/narrow-cycles-are-mechanical/README.md) (`ROTATION_LATTICE.md`). The coprime upper approximations of [`close-pair-lattice-criterion`](../close-pair-lattice-criterion/README.md) (`SIZE_PROBE.md`) have `ε → 0` with `m` unbounded, so for every `K > 2` there is such a rational additive-one cycle with every complete gap above `K`, minimum above `mK`, and `q = D ≤ min B_l` at the raw parameter. Its denominator exceeds 1 (R71's exact denominator, [`mechanical-word-exact-denominator`](../../results/mechanical-word-exact-denominator/README.md); `D ≡ 5` or `7 (mod 8)` once `A ≥ 3`). All sharp pair bounds (at most 2) hold with arbitrarily large slack, the adjacent sum `2m − 1` is already odd, and the rounded denominator bound `(2m − 1)D/B_0 < 2/K` tends to 0. These mechanical cycles are already known nonintegral; the point is that this rounding method cannot recover even their exclusion.

Finite evidence ([`integer_gap_audit.json`](integer_gap_audit.json)): over the 52 ordered cases (51 nonfixed and the trivial cycle), all 474 adjacent gap equations and sharp bounds pass, all 7,022 proper circular pair bounds pass at actual parameters; after rescaling to additive 1, 19 noninteger cycles still pass every circular pair inequality; the summed bound passes 31/52 cases, and 28/52 after odd rounding.

## Why it fails

Exact gap integrality is equivalent to the original lattice condition, and the local spacing inequalities (with all nonnegative combinations and odd rounding) are a strict relaxation that infinitely many genuine nonintegral rational cycles satisfy with unbounded slack. Exclusion by these inequalities is retired. The result does not rule out a stronger inequality using genuinely global information, arbitrary integer cutting planes, or a `q = 1` theorem.

## What survives

- [`complete-gap-lattice-equivalence`](../../results/complete-gap-lattice-equivalence.md) and [`odd-spacing-rounding-bound`](../../results/odd-spacing-rounding-bound.md) (both formal): a valid diagnostic and a clean lattice interface.
- The counterfamily (6) and the `q = 5, 13, 83` controls; the `d = 7` cycle `(5, 11)` lies outside `q ≤ L`.
- **The legacy decision** (main lane, endorsed by the side-lane referee): demote ordered-cycle exclusion from "the route" to an open benchmark, with its conditional payoff `H > 8L`, and return to cyclic word arithmetic: compare a word with a nontrivial rotation and ask whether sparse differences bound `gcd(C_w, D_w)` uniformly. The side lane added that, after the close-pair obstruction, the gain must come from the arithmetic of the sparse difference, not its size. This led to [`two-defect-rotation-exclusion`](../../results/two-defect-rotation-exclusion/README.md).

## Certificates

- [`c010_gap_check.py`](c010_gap_check.py) (under a second; side lane, independent code): exact integer matrices `E^m = 2I` and the inverse of `U` for `m ≤ 12`, the `q = 5` control against the sharp bounds, and the seam identity `2B_0 − B_(m−1) = 3^(m−1)` on all 381 primitive mechanical words with coprime `(A, m)`, `2^A > 3^m` and `2 ≤ m < 30`; it rewrites [`c010_gap_check.json`](c010_gap_check.json) identically.

## History

- Migrated from `experiments/cycle_spectrum/C010/` (legacy ID `C010`; `REPORT.md`, notes `GAP_LATTICE.md`, `ODD_ROUNDING.md`, `ROUNDING_PROBE.md`) at commit `be73a66`, by the B04 migration (Claude, Opus 5.5). The side-lane checks `reviews/side_lane/c010_gap_check.*`, `c010b_gap_lattice_check.*` and `c010c_any_arrangement_check.*` moved here. All C010 scripts, receipts and notes stay in this folder. Parts became [`complete-gap-lattice-equivalence`](../../results/complete-gap-lattice-equivalence.md) and [`odd-spacing-rounding-bound`](../../results/odd-spacing-rounding-bound.md).
- Main lane (ChatGPT/Codex), 2026-10-19, main commit `cae57b0`.
- **Link repair in pinned notes (2026-10-19, B04 migration).** `GAP_LATTICE.md`, `ODD_ROUNDING.md` and `LITERATURE.md` linked to `../C004/`, `../C006/` and `../C001/` legacy paths; only those link targets were repointed. Their SHA-256 values pinned in `check_delivery.py`, `delivery_checks.json` and the review notes (`e8eed1e1…`, `4647d1b5…`, `a000a4ed…`) describe the `be73a66` versions; `check_delivery.py` already fails by design, and `check_integer_gaps.py` (which also hashes `SIZE_PROBE.md` by its old path) no longer runs. No mathematical text changed.
