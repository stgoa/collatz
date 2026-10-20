---
id: odd-spacing-rounding-bound
kind: result
title: "Odd spacing and image order bound every sorted gap of an ordered cycle, so L ≥ R_q(H)"
status: formal
claim: >
  Raw odd-only 3x+q map, q odd. Let a primitive positive ordered cycle (m > 1, circular normalised
  successor order) have sorted normalised states z_[0] = L < … < z_[m−1] < 2L with sorted heights H_j,
  and gaps Δ_j = z_[j+1] − z_[j] (seam Δ_(m−1) = 2L − z_[m−1], with H_m = −1). For adjacent heights
  a = H_j, b = H_(j+1): Δ_j ≥ 2/2^a if b = a; Δ_j ≥ 1/2^a if b < a (seam included); and, if
  b = a + k > a, 3·2^b·Δ_j > q(2^k − 1) and Δ_j ≥ [q(2^k − 1) + η(q, k)]/(3·2^b), where η = 6 for even
  k and η = 2 or 4 for odd k according as q ≡ 1 or 5 (mod 6) (η = 4 is valid, if not sharp, for
  q ≡ 3 mod 6). Summing over all m gaps, L ≥ R_q(H) = Σ_j b_q(H_j, H_(j+1)).
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [dyadic-order-lemma]
lean:
  - LeanLane.Cyc.eta_refine
  - LeanLane.Cyc.OddCycle.q_odd
  - LeanLane.Cyc.OrdCycle.gap_ge_of_eq
  - LeanLane.Cyc.OrdCycle.gap_ge_of_lt
  - LeanLane.Cyc.OrdCycle.gap_seam_ge
  - LeanLane.Cyc.OrdCycle.three_gap_gt_of_gt
  - LeanLane.Cyc.OrdCycle.three_gap_ge_of_gt
  - LeanLane.Cyc.OrdCycle.rounding_bound
evidence:
  - "../attempts/local-odd-rounding-exclusion/ODD_ROUNDING.md, sections 1-3: the written proof and the seam check"
  - "../attempts/local-odd-rounding-exclusion/integer_gap_audit.json: all 474 adjacent gap equations and sharp bounds and all 7,022 circular pair bounds pass at actual parameters on the 52 ordered cases (historical receipt; its checker no longer runs at the new path)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: ../attempts/local-odd-rounding-exclusion/c010_gap_check.py
    scope: "Feed 2026-10-19 03:39, REFEREE C010; update 04:28: Lean C010-a VERIFIED, receipts sha256 8569c7d1… checked; checked numerically that 3r − q(2^k − 1) ≥ η at the first admissible odd r for every odd q < 200 (multiples of 3 included) and k < 12"
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed 03:49: ODD_ROUNDING.md read in full, every pair bound re-derived, no error; Lean unit C010-a verified (iteration 31)"
    link: ../../../archive/side-lane/FEED.md
tags: [cycles, dyadic-order, gap-lattice, rounding, formal]
---

# Odd spacing and image order bound every sorted gap of an ordered cycle, so L ≥ R_q(H)

## Statement

Use primitive raw positive odd-only cycles `3n_i + q = 2^(a_i)·n_(i+1)`, `a_i ≥ 1`, with `m > 1` and strictly increasing `F = 3z + q·2^(−h)` in increasing `z = n/2^h` ([`dyadic-order-lemma`](dyadic-order-lemma.md)). Set `H_m = −1` and `n_[m] = L`, so `z_[m] = 2L`. For adjacent sorted ranks with heights `a = H_j`, `b = H_(j+1)` (the destination may be `−1` only at the seam),

```
b_q(a, b) = 2/2^a                                   if b = a;
b_q(a, b) = 1/2^a                                   if b < a (seam included);
b_q(a, b) = [q(2^k − 1) + η(q, k)]/(3·2^b),  k = b − a > 0,  if b > a;

Δ_j ≥ b_q(a, b),                                                    (1)

η(q, k) = 6 (k even);  2 (k odd, q ≡ 1 mod 6);  4 (k odd, q ≡ 5 mod 6).
```

Summing over all `m` gaps (which telescope to `z_[m] − z_[0] = L`):

```
L ≥ R_q(H) = Σ_j b_q(H_j, H_(j+1)).                                 (3)
```

The legacy note assumes `q` coprime to 6 and `q ≤ L`; only `q` odd (forced by positive valuations) and image order are used. For `q ≡ 3 (mod 6)` the true increment for odd `k` is 6, so `η = 4` still bounds.

## Proof

[`ODD_ROUNDING.md`](../attempts/local-odd-rounding-exclusion/ODD_ROUNDING.md) §§2–3. Equal heights: a positive difference of two odd integers, numerator at least 2. `b < a`: the numerator `2^(a−b)·n_[j+1] − n_[j]` is a positive (odd) integer, at least 1; at the seam it is `2^(a+1)·L − n_[m−1]`. `b > a`: `r = n_[j+1] − 2^k·n_[j]` is positive and odd, and strict increase of `F` says `3r > q(2^k − 1)`. Since `3r ≡ 3 (mod 6)`, the least admissible `3r` is the first number `≡ 3 (mod 6)` strictly above `q(2^k − 1)`: for even `k` that number is itself `≡ 3`, needing increment 6; for odd `k` it is `≡ q (mod 6)`, needing 2 or 4. Dividing by `3·2^b` gives (1); summing gives (3). §1 of the note checks that the seam in the gap recurrence of [`ordered-cycle-sparse-forcing`](ordered-cycle-sparse-forcing/README.md) is correct.

## Lean

`lean/CycleSpectrum.lean`, Lean unit C010-a (legacy `lean/STATE.md`, now [`archive/lean-lane/STATE.md`](../../../archive/lean-lane/STATE.md), iteration 31), axioms `propext`, `Classical.choice`, `Quot.sound`; receipts `lean/receipts/CycleSpectrum.*`. Stated on `OrdCycle` (ordered primitive odd cycle, `m ≥ 2`) in scaled coordinates `G_r = 2^B·Δ_r`:

- `gap_ge_of_eq`: `2·2^(B−a) ≤ G_r` (equal heights); `gap_ge_of_lt`: `2^(B−a) ≤ G_r` (downward); `gap_seam_ge`: `2^(B−a) ≤ G_(m−1)` with `G_(m−1) = 2y_0 − y_(m−1)`, `y_0 = 2^B·L`.
- Upward: `three_gap_gt_of_gt` (`2^(B−b)·q(2^k − 1) < 3G_r`, the prose's `3r > q(2^k − 1)`), sharpened by `three_gap_ge_of_gt` through `eta_refine` (odd `r, q`, `k ≥ 1`, `q(2^k − 1) < 3r ⇒ q(2^k − 1) + η ≤ 3r`; `3 ∤ q` not needed). `OddCycle.q_odd`: positive valuations make `q` odd.
- `rounding_bound`: `Σ_(r<m) pairBound3 r ≤ 3·2^B·L`, where `pairBound3 r` is `3·2^B·b_q(H_r, H_(r+1))` case by case; dividing by `3·2^B` gives (3). Hypothesis: `q` odd only.

Not formalised (and not part of the claim): the sharpness remark below, and the bookkeeping rewriting of the next section.

## Remarks

- **Rewriting as a denominator bound** (written, `ODD_ROUNDING.md` §3, not in Lean). With `V(H) = Σ_(H_(j+1) > H_j) (2^(−H_j) − 2^(−H_(j+1)))`, `R_q(H) = q·V(H)/3 + Γ_(q mod 6)(H)` for positive rationals `Γ_1`, `Γ_5` depending only on the sorted heights; substituting the cycle identity `L = q·C_h/D` (`C_h` the true weighted intercept) gives `q·[C_h/D − V(H)/3] ≥ Γ_(q mod 6)(H)` and `q ≥ Γ/[C_h/D − V/3]`. A proposed ordered profile with nonpositive bracket cannot be realised.
- **Sharpness.** Each bound in (1) is attained by an isolated ordered pair with odd numerators (choose the minimal `r` and `n_[j]` large and odd). This asserts neither simultaneous attainment around a cycle nor compatibility with the successor arrows.
- **What it cannot do.** It is a necessary inequality only: genuine nonintegral rational cycles satisfy it with arbitrarily large slack, see [`local-odd-rounding-exclusion`](../attempts/local-odd-rounding-exclusion/README.md). It does separate some shapes: the ordered `q = 83` cycle's additive-one rational shape fails it (`R_1 = 15/2 > 157/83`, rounded bound `q ≥ 2407/545 > 4`).
- **Novelty.** Elementary; none claimed.

## History

- Split from `experiments/cycle_spectrum/C010/` (legacy ID `C010`; `ODD_ROUNDING.md` §§1–3) at commit `be73a66`, by the B04 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19. Formalised by the Lean lane (Claude Lean lane, Fable) as C010-a, iteration 31; the side lane noted (feed 03:39) that the hypothesis `3 ∤ q` can be dropped.
