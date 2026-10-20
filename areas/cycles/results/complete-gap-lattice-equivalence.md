---
id: complete-gap-lattice-equivalence
kind: result
title: The complete dyadic gaps of a cycle carry exactly the same lattice, gcd and denominator as its states
status: formal
claim: >
  (i) For m ≥ 1 and any vector Z = (Z_0, …, Z_(m−1)), the complete gaps G_j = Z_(j+1) − Z_j (j < m − 1)
  and seam G_(m−1) = 2Z_0 − Z_(m−1) satisfy Z_0 = Σ_j G_j and Z_j = Σ_i G_i + Σ_(i<j) G_i; hence over Z
  the states and the gaps have the same common divisors, over Q they are integral together and a
  scalar clears the denominators of one iff of the other, and all gaps are positive iff
  0 < Z_0 < Z_1 < … < Z_(m−1) < 2Z_0. (ii) For a raw odd-only 3x+q cycle with reduced numerators
  (gcd(q, n_0) = 1) whose maximal dyadic height B is attained, the scaled states Z_i = 2^(B−h_i)·n_i
  have gcd 1, the complete gaps of any arrangement of one period have gcd 1, and the least positive
  common denominator of Z/q and of G/q is exactly q. No order, primitivity or q ≤ L is needed.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: []
lean:
  - LeanLane.Cyc.Z_eq_sum_cgap
  - LeanLane.Cyc.dvd_cgap_iff
  - LeanLane.Cyc.cgap_int_iff
  - LeanLane.Cyc.clears_iff
  - LeanLane.Cyc.cgap_pos_iff
  - LeanLane.Cyc.OddCycle.Z_dvd_isUnit
  - LeanLane.Cyc.OddCycle.cgap_dvd_isUnit
  - LeanLane.Cyc.OddCycle.q_dvd_of_dvd_mul
  - LeanLane.Cyc.OddCycle.clears_q_iff
  - LeanLane.Cyc.OddCycle.q_le_of_clears
  - LeanLane.Cyc.OddCycle.clears_q_cgap_iff
  - LeanLane.Cyc.OrdCycle.gap_eq_cgap
  - LeanLane.Cyc.OrdCycle.gap_dvd_isUnit
evidence:
  - "../attempts/local-odd-rounding-exclusion/GAP_LATTICE.md, sections 1-2: the written proof"
  - "../attempts/local-odd-rounding-exclusion/c010b_gap_lattice_check.py, c010c_any_arrangement_check.py: side-lane checks on 92 actual cycles (ordered and unordered), 337 rational ordered cycles and 1,701 arrangements; they no longer run at the new path (see that node)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: ../attempts/local-odd-rounding-exclusion/c010b_gap_lattice_check.py
    scope: "Feed 2026-10-19 update 10:18: Lean C010-b VERIFIED, statement match with GAP_LATTICE.md sections 1-2 (two scope notes), receipts sha256 abc5ff86…; update 10:32: Lean C010-c VERIFIED (receipts 1379f455…), closing the ordering scope note; independent checks c010b and c010c"
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed 03:49: GAP_LATTICE.md read in full, no error; Lean units C010-b (iteration 56) and C010-c (iteration 57) verified"
    link: ../../../archive/side-lane/FEED.md
tags: [cycles, gap-lattice, formal]
---

# The complete dyadic gaps of a cycle carry exactly the same lattice, gcd and denominator as its states

## Statement

**(i) Linear algebra.** For `m ≥ 1` define the dyadic shift `(EZ)_j = Z_(j+1)` for `j < m − 1`, `(EZ)_(m−1) = 2Z_0`, so `E^m = 2I`; put `U = E − I` and `G = UZ`, the complete gaps with seam `G_(m−1) = 2Z_0 − Z_(m−1)`. Then `(E − I)(I + E + … + E^(m−1)) = E^m − I = I`, so `U` is unimodular with integer inverse `I + E + … + E^(m−1)`:

```
Z_0 = Σ_j G_j,      Z_j = Σ_i G_i + Σ_(i<j) G_i.          (1)
```

Consequently `G > 0` entrywise iff `0 < Z_0 < Z_1 < … < Z_(m−1) < 2Z_0` (the gap cone is the normalised order cone); `Z` is integral iff `G` is; for integer vectors `gcd(Z) = gcd(G)`; for rational vectors the least positive common denominator of `Z` and of `G` agree. The claim is about whole vectors, not single coordinates.

**(ii) Cycles.** For a reduced numerator cycle `3n_i + q = 2^(a_i)·n_(i+1)`, `L = min n_i`, `h_i = floor(log₂(n_i/L))`, `B = max h_i` attained, set `Z_i = 2^(B−h_i)·n_i ∈ [2^B·L, 2^(B+1)·L)`. Their gcd is 1, so is the gcd of the complete gaps of any arrangement exhausting one period (the sorted one in particular), and after dividing by `q` the states and gaps both have common reduced denominator exactly `q`. This holds for unordered cycles too. Changing from states to gaps does not make the lattice easier.

## Proof

[`GAP_LATTICE.md`](../attempts/local-odd-rounding-exclusion/GAP_LATTICE.md) §§1–2. (i) follows from the displayed inverse, applied to `kZ` and `kG` for every positive integer `k` for the denominator statement. (ii): any odd common divisor of the `Z_i` divides all reduced numerators, and an arrow then makes it divide `q`, contradicting reduction; a state at height `B` makes one `Z_i` odd. Then (i) transfers the statement to the gaps.

## Lean

`lean/CycleSpectrum.lean`, Lean units C010-b (iteration 56) and C010-c (iteration 57) (legacy `lean/STATE.md`, now [`archive/lean-lane/STATE.md`](../../../archive/lean-lane/STATE.md)), axioms `propext`, `Classical.choice`, `Quot.sound`; receipts `lean/receipts/CycleSpectrum.*`.

- (i), over any commutative ring: `cgap Z m j` defines the complete gaps; `Z_eq_sum_cgap` is (1), proved by telescoping (`sum_cgap_prefix`, `sum_cgap`). Over `ℤ`/`ℚ`: `dvd_cgap_iff` (same common divisors), `cgap_int_iff` (integral together), `clears_iff` (a scalar clears `Z` iff it clears `UZ`), `cgap_pos_iff` (gap cone = order cone). The matrix `E` and `E^m = 2I` are not stated as matrices; their content is carried by (1).
- (ii), on `OddCycle` (no order assumed), with hypotheses `IsCoprime q n_0` (reduction) and `∃ i, h_i = B` (maximal height attained, because the structure's `B` is only an upper bound): `Z_dvd_isUnit` (gcd 1), `cgap_dvd_isUnit` (complete gaps of any arrangement `Z ∘ σ` with `σ` onto one period have gcd 1), `q_dvd_of_dvd_mul`, `clears_q_iff` and `q_le_of_clears` (least positive common denominator of `Z/q` is `q`), `clears_q_cgap_iff` (the same for `G/q`). On ordered cycles, `OrdCycle.gap_eq_cgap` identifies the sorted gaps of [`ordered-cycle-sparse-forcing`](ordered-cycle-sparse-forcing/README.md) with these complete gaps, and `OrdCycle.gap_dvd_isUnit` is the sorted case.
- No sortedness, injectivity, primitivity or `m ≥ 2` is needed. The prose's remark that the scaled states are distinct (it needs primitivity as well as oddness; a precision note of the Lean lane, feed 03:49) is neither used nor formalised.

## Remarks

- **Use.** This is the lattice interface of [`local-odd-rounding-exclusion`](../attempts/local-odd-rounding-exclusion/README.md): passing to gaps neither adds nor removes integrality information, so any new obstruction must come from elsewhere.
- **Controls.** Holds on all actual cycles checked by the side lane (92 cycles, ordered and unordered; 81 reduced cycles under 1,701 arrangements). The 11 non-reduced fixed points `n = q` violate the reduction hypothesis and fail the denominator statement, as they should.
- **Novelty.** Elementary; none claimed.

## History

- Split from `experiments/cycle_spectrum/C010/` (legacy ID `C010`; `GAP_LATTICE.md` §§1–2) at commit `be73a66`, by the B04 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19. Formalised by the Lean lane (Claude Lean lane, Fable) as C010-b (ordered cycles) and C010-c (any reduced cycle, any arrangement, as the side lane suggested).
