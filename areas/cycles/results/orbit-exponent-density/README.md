---
id: orbit-exponent-density
kind: result
title: Along the rank orbit of an ordered cycle, t steps carry exponent total at least floor(tA/m)
status: formal
claim: >
  For integers m ≥ 1, 1 ≤ s < m with gcd(s, m) = 1, q′ ≥ 1, A = m·q′ + s, rank exponents
  e_r = q′ + [r ≥ m − s] and orbit r_k = (r_0 + k·s) mod m, the exponent total E(r_0, t) = Σ_(k<t) e(r_k)
  satisfies E(r_0, t) + floor(r_0/m) = t·q′ + floor((r_0 + t·s)/m) exactly, hence floor(t·A/m) ≤ E(r_0, t)
  for r_0 < m. Applied to an ordered cycle of the raw odd-only 3x+q map with J forced positions, some
  zero-forcing run of length floor((m−1)/J) has 2^E < 2^B·L with E ≥ floor(floor((m−1)/J)·A/m).
authors:
  - Claude side lane (Opus)
created: 2026-10-19
depends_on: [ordered-cycle-sparse-forcing]
lean:
  - LeanLane.Cyc.OrdCycle.div_succ_step
  - LeanLane.Cyc.OrdCycle.E_eq_div
  - LeanLane.Cyc.OrdCycle.E_ge_mul_div
  - LeanLane.Cyc.OrdCycle.G1_first_E_density
certificates: [s2c_density_check.py]
evidence:
  - "../../attempts/ordered-cycle-run-renormalisation/README.md, 'What happened' section 3: the written argument (legacy S02 note section 4, as corrected at 11:11)"
  - "s2c_density_check.json: receipt of the certificate (written only when an output path is given)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Lean unit S2-c verified (iteration 62), statement match recorded in the legacy lean/STATE.md note S2-c; the lane's review had prompted the re-attribution of the A/m factor to this density"
    link: ../../../../archive/lean-lane/STATE.md
tags: [cycles, ordered-cycles, mechanical-words, formal]
---

# Along the rank orbit of an ordered cycle, t steps carry exponent total at least floor(tA/m)

## Statement

Let `m ≥ 1`, `1 ≤ s < m` with `gcd(s, m) = 1`, `q′ ≥ 1`, `A = m·q′ + s`, rank exponents `e_r = q′ + [r ≥ m − s]` (the mechanical exponent word of an ordered cycle, [`dyadic-order-lemma`](../dyadic-order-lemma.md)), orbit `r_k = (r_0 + k·s) mod m` and `E(r_0, t) = Σ_(k<t) e(r_k)`. Then

```
E(r_0, t) + floor(r_0/m) = t·q′ + floor((r_0 + t·s)/m)        (exact),
floor(t·A/m) ≤ E(r_0, t)                                     (r_0 < m).
```

For an ordered cycle with `J` forced positions, (G1)'s first inequality of [`ordered-cycle-sparse-forcing`](../ordered-cycle-sparse-forcing/README.md) holds with this density in place of `E ≥ t`: some zero-forcing run of length `floor((m−1)/J)` has `2^E < 2^B·L` with `E ≥ floor(floor((m−1)/J)·A/m)`.

## Proof

Legacy S02 §4 as corrected (now in [`ordered-cycle-run-renormalisation`](../../attempts/ordered-cycle-run-renormalisation/README.md)). One orbit step adds `1` to `floor((r_0 + k·s)/m)` exactly when it starts at a high rank `r_k ≥ m − s` (a wrap); so `E = t·q′ + #wraps`, which is the exact identity. Then `floor((r_0 + ts)/m) ≥ floor(ts/m)` and `t·q′ + floor(ts/m) = floor(t(mq′ + s)/m) = floor(tA/m)`. The application replaces C006-b's `E ≥ t` by this bound in `G1_first_E`.

## Certificates

- [`s2c_density_check.py`](s2c_density_check.py) (about 2 s): checks both identities on random `(m, s, q′, r_0, t)` with `t` up to `3m` (8,829,024 cases in its receipt [`s2c_density_check.json`](s2c_density_check.json)); exits 0 at the new path. Its checks are `assert` statements.

## Lean

`lean/CycleSpectrum.lean`, Lean unit S2-c (iteration 62); axioms `propext`, `Classical.choice`, `Quot.sound`. In `OrdCycle`, with `s = numHigh`: `div_succ_step` (one orbit step adds `1` to `floor((r₀ + ks)/m)` exactly at a high rank), `E_eq_div` (the exact identity, in the additive form above), `E_ge_mul_div` (`r₀ < m` ⇒ `floor(t·A/m) ≤ E r₀ t`, through `Apre_eq_ord` and `A = m·q′ + s`; natural-number division), `G1_first_E_density` (the application to the pigeonhole run of C006-b's `G1_first_E`). The statement matches the claim; the Lean works inside an ordered cycle, where `s`, `q′` and `A` come from the cycle.

## Remarks

- **The numerical consequence is not formal.** Feeding the density into C006-d's gap chain multiplies the leading term of the `J` bound by `A/m ≈ log₂ 3`: `J ≳ (A/m)(m−1)/(175 + 342·log₂ m)`, about `1.7·10^7` instead of `1.07·10^7` at `m = 1.375·10^11` (side-lane estimate, feed 11:11). It is not stated as one theorem; the gap constants are those of [`musson-collatz-gap-all`](../../../../sources/musson-collatz-gap-all.md) and the period is [`hercher-2023-cycle-length`](../../../../sources/hercher-2023-cycle-length.md) with [`barina-2025-convergence-2-71`](../../../../sources/barina-2025-convergence-2-71.md). The formal gap form of the `J` bound itself is in [`ordered-cycle-height-change-growth`](../ordered-cycle-height-change-growth.md).
- Novelty: elementary; none claimed.

## History

- Split from `experiments/cycle_spectrum/S02/RENORMALISATION.md` §4 (legacy ID `S02`) at commit `be73a66`, by the B05 migration (Claude, Opus 5.5). The side-lane check `reviews/side_lane/s2c_density_check.{py,json}` moved here.
- Side lane (Claude, Opus). **Correction (2026-10-19 11:11, after the Lean lane's review):** the first version attributed the `≈1.58` factor to summing over all runs; it comes from this density. Formalised by the Lean lane as S2-c.
