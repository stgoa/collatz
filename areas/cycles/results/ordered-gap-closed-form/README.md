---
id: ordered-gap-closed-form
kind: result
title: In an ordered cycle every sorted gap is an explicit sum over the forced positions, and every gap is coprime to q
status: formal
claim: >
  Raw odd-only 3x+q map, any q. Let a primitive integer cycle (states n_i, total A, D = 2^A − 3^m > 0,
  heights h_i, band B ≥ max h_i) have circularly ordered normalised successor with rank shift s, scaled
  states Z_i = 2^(B−h_i)·n_i, sorted gaps Δ_r (seam Δ_(m−1) = 2Z_[0] − Z_[m−1]), rank exponents
  e_r = floor(A/m) + [r ≥ m − s], forcing terms T_r = q(2^(B−h_[r+1]) − 2^(B−h_[r])) for r < m − 1 and
  T_(m−1) = q(2^(B+1) − 2^(B−h_[m−1])), rank orbit r_i = r_0 + i·s mod m and E_i = e_(r_0) + … + e_(r_(i−1)).
  Then for every start r_0: (2^A − 3^m)·Δ_(r_0) = Σ_(i<m) 3^(m−1−i)·2^(E_i)·T_(r_i), in which only the
  J forced positions (T ≠ 0) contribute and D divides every such forcing sum. If moreover q is odd and
  gcd(q, n_0) = 1 (reduced), every single sorted gap is coprime to q; in the word normalisation
  (states C_w-rotations, gaps G_r = g·Δ_r, g = gcd(C_w, D)) this reads gcd(D, G_r) = gcd(C_w, D) for every
  r, and in particular gcd(C_w, D) = gcd(D, run-start gaps).
authors:
  - Claude side lane (Opus)
created: 2026-10-19
depends_on: [ordered-cycle-sparse-forcing, dyadic-order-lemma]
lean:
  - LeanLane.Cyc.OrdCycle.gap_unroll
  - LeanLane.Cyc.OrdCycle.E_m
  - LeanLane.Cyc.OrdCycle.gap_closed_form
  - LeanLane.Cyc.OrdCycle.gap_closed_form_filter
  - LeanLane.Cyc.OrdCycle.D_dvd_forcing_sum
  - LeanLane.Cyc.OrdCycle.dvd_gap_run_iff
  - LeanLane.Cyc.OrdCycle.exists_run_start
  - LeanLane.Cyc.OrdCycle.run_start_gaps_coprime
  - LeanLane.Cyc.OrdCycle.dvd_gap_isUnit
  - LeanLane.Cyc.OrdCycle.gap_isCoprime_q
certificates: [s1a_integer_cycle_check.py, s1b_run_start_gcd_check.py, s1cd_gap_coprime_check.py, jterm_gap_check.py]
evidence:
  - "Side-lane feed entry 2026-10-19 06:30 (LEAD, ordered cycles) with its updates 07:33, 07:51 and 08:06: the written statements and proofs (archived with the side-lane feed)"
  - "s1a_integer_cycle_check.json, s1b_run_start_gcd_check.json, s1cd_gap_coprime_check.json, jterm_gap_check.json: receipts of the four certificates (written only when an output path is given; at the B17 migration s1cd and jterm, run with an output path, reproduced their committed receipts byte for byte)"
  - "s1cd_gap_coprime_check.py: side-lane check of Lean units S1-c and S1-d (every gap coprime to q on the 33 actual ordered 3x+q cycles; the 3 actual J = 1 cycles have D = q; the 65 rational ordered J = 1 cycles have gcd(C, D) = 1). It imports the side-lane helper jterm_gap_check from its own folder; since the B17 migration moved jterm_gap_check.py here (legacy reviews/side_lane/jterm_gap_check.py), it passes at its new path and is a certificate. Passed at be73a66 as reviews/side_lane/s1cd_gap_coprime_check.py (archive/legacy-checker-run-be73a66.md)"
  - "jterm_gap_check.py: side-lane probe behind the S1 lead (legacy reviews/side_lane/, moved here byte-identical at the B17 migration); also imported as a helper by side-lane checks in other node folders (local-odd-rounding-exclusion, ordered-cycle-run-renormalisation, band-one-gcd-law-search, ordered-cycle-sparse-forcing), which look for it in their own folder and fail there"
  - "Helper modules: s1a_integer_cycle_check.py (the function cycles(q, N) that finds actual 3x+q cycles by iteration) is imported by side-lane checks in other node folders (ordered-cycle-sparse-forcing, local-odd-rounding-exclusion, shared-background-denominator-law, the S-series nodes); those imports look in their own folder and fail there"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Lean units S1-a (iteration 44), S1-b (iteration 45) and S1-c (iteration 46) verified, with the dictionary between the feed's word normalisation and OrdCycle checked against the definitions (legacy lean/STATE.md rows S1-a to S1-c and their notes)"
    link: ../../../../archive/lean-lane/STATE.md
aliases: [S1]
tags: [cycles, dyadic-order, ordered-cycles, gap-system, formal]
---

# In an ordered cycle every sorted gap is an explicit sum over the forced positions, and every gap is coprime to q

## Statement

Setting of [`ordered-cycle-sparse-forcing`](../ordered-cycle-sparse-forcing/README.md) (C005/C006 ordered cycles: the sorted ranks rotate by a fixed `s`, and the images do not invert; at `q = 1` this contains every cycle with `H < 8L`, see [`three-band-collatz-cycles-are-ordered`](../three-band-collatz-cycles-are-ordered.md)). Raw odd-only clock, parameter `q` (the `d` of `conventions/NOTATION.md`).

Integer normalisation (the Lean `OrdCycle`): states `n_i`, heights `h_i`, `B` an upper bound on the heights, scaled states `Z_i = 2^(B−h_i)·n_i`, sorted gaps `Δ_r` with the seam `Δ_(m−1) = 2Z_[0] − Z_[m−1]` last, rank exponents `e_r = floor(A/m) + [r ≥ m − s]`, forcing terms

```
T_r = q(2^(B−h_[r+1]) − 2^(B−h_[r]))   (r < m − 1),      T_(m−1) = q(2^(B+1) − 2^(B−h_[m−1]))   (seam),
```

and `J` the number of ranks with `T_r ≠ 0` (the *forced* positions). The gaps obey C006's (G3), `2^(e_r)·Δ_(r+s) = 3Δ_r + T_r`.

1. **Closed form.** For every start `r_0`, with `r_i = r_0 + i·s mod m` and `E_i = e_(r_0) + … + e_(r_(i−1))` (`E_0 = 0`):

```
(2^A − 3^m)·Δ_(r_0) = Σ_(i<m) 3^(m−1−i)·2^(E_i)·T_(r_i).
```

   Only the `J` forced positions contribute, and `D = 2^A − 3^m` divides every forcing sum.
2. **Gap coprimality.** If `q` is odd and `gcd(q, n_0) = 1`, every sorted gap `Δ_r` is coprime to `q`. A fortiori the run-start gaps are jointly coprime to `q` (a *run start* is a rank whose orbit predecessor is forced).

**Word normalisation (the feed's form).** For a word `w` with `g = gcd(C_w, D)` and reduced parameter `q = D/g`, the feed's scaled states are `Ẑ_i = 2^(B−h_i)·C(w.rotate i) = g·Z_i`, its gaps `G_r = g·Δ_r` and its forcing `τ_r = T_r/q`, so 1 reads `G_(r_0) = Σ_(i<m) 3^(m−1−i)·2^(E_i)·τ_(r_i)` (the Lean identity divided by `q`, using `D·Δ = q·G`), and 2 reads `gcd(D, G_r) = gcd(C_w, D)` for every single `r`, hence `gcd(C_w, D) = gcd(D, the J run-start gaps)`. At `q = 1`, every actual gap is a `J`-term sum divided by `D`, so `D` must divide all `J` run-start sums: main's coupled signed sum in the ordered class, with explicit exponents and small coefficients (in band 1, `τ ∈ {−1, 1, 2, 3}`).

## Proof

From the side-lane feed entry of 2026-10-19 06:30 and its updates (lightly edited).

**1.** Unroll (G3) once around the rank orbit: by induction, `2^(E_n)·Δ_(r_n) = 3^n·Δ_(r_0) + S_n` with `S_(n+1) = 3S_n + 2^(E_n)·T_(r_n)`, i.e. `S_n = Σ_(i<n) 3^(n−1−i)·2^(E_i)·T_(r_i)`. The orbit closes after `m` steps (`gcd(s, m) = 1`), and `E_m = Σ_r e_r = A` because every rank is visited once and `Σ c_i = Σ a_i` ([`dyadic-order-lemma`](../dyadic-order-lemma.md)). So `2^A·Δ_(r_0) = 3^m·Δ_(r_0) + S_m`. Terms with `T_(r_i) = 0` vanish.

**2.** Let `ℓ` be a prime (in Lean: any divisor) dividing `q`. Then `T_r = q·τ_r ≡ 0 (mod ℓ)`, so (G3) reads `2^(e_r)·Δ_(r+s) ≡ 3Δ_r (mod ℓ)`. Since `ℓ ∤ 6` (`q` odd; reduced cycles have `3 ∤ q`), divisibility by `ℓ` passes in both directions along the orbit, which visits every rank. So `ℓ` divides one gap only if it divides all of them, and then it divides `Σ_r Δ_r = Z_0 = 2^B·n_0`, contradicting `gcd(q, n_0) = 1`. This is C007-a's residue mechanism (`dvd_all_of_dvd`) applied to gaps instead of states. The run-start form (S1-b) is the weaker statement that inside a zero-forcing run a gap only gains factors `3/2^e`.

## Certificates

- [`s1a_integer_cycle_check.py`](s1a_integer_cycle_check.py) (about 1 s): finds the actual `3x+q` cycles by iteration for `q ∈ {5, 7, 11, 13, 17, 19, 23, 29, 61, 233, 1201}`; on all 33 ordered cycles found, the closed form 1 holds for every start `r_0` (exact integers, Lean's own normalisation); the 44 unordered cycles are skipped.
- [`s1b_run_start_gcd_check.py`](s1b_run_start_gcd_check.py) (about 1 s): on the same 33 ordered cycles (22 of their words have `g > 1`): `gcd(q, run-start gaps) = 1`, every rank is reached from a run start along a zero-forcing run, `Σ Δ = 2^B·n_0`, and in the word normalisation `gcd(D, run-start G) = gcd(C, D)`; no single run-start gap shares a factor with `q`.

- [`s1cd_gap_coprime_check.py`](s1cd_gap_coprime_check.py) (about 15 s): on the 33 actual ordered `3x+q` cycles every gap is coprime to `q`; the 3 actual `J = 1` cycles have `D = q`; the 65 rational ordered `J = 1` cycles have `gcd(C, D) = 1`.
- [`jterm_gap_check.py`](jterm_gap_check.py) (about 35 s): on all 337 rational ordered cycles with `m ≤ 9` and letters 1–4, the recurrence (G3), the closed form 1 from every start and `gcd(C, D) = gcd(D, run-start gaps)`; band 1 has `J = 2` in 27 of them, none in the Collatz range `m < A < 2m`, and there the `J = 2` identity of [`band-one-three-forced-positions`](../band-one-three-forced-positions.md) holds; on the 900 ordered Collatz-range cycles with `m ≤ 12` and letters 1–3, band 1 has `J ≥ 3` and the adjacent-rank rotation differs from the word in at most `2J` positions.

All four use `assert` for their checks and exit 0 at the new path. The feed also reports `gcd(D, G_r) = gcd(C, D)` for every `r` on the 337 rational cycles (18 with `g > 1`).

## Lean

`lean/CycleSpectrum.lean`, Lean units S1-a (iteration 44), S1-b (iteration 45) and S1-c (iteration 46), on C006-a's `OrdCycle`; axioms `propext`, `Classical.choice`, `Quot.sound`; receipts `lean/receipts/CycleSpectrum.*`.

- **1.** `gap_unroll` is `2^(E_n)·Δ_(r_n) = 3^n·Δ_(r_0) + S_n` for every `n`; `E_m` is `E_m = A`; `gap_closed_form` is `(2^A − 3^m)·Δ_(r_0) = Σ_(i<m) 3^(m−1−i)·2^(E_i)·T_(r_i)` for every sorted rank `r_0`; `gap_closed_form_filter` restricts to `T ≠ 0` (`card_forced_zero`: from rank 0 these are exactly the `J` forced positions); `D_dvd_forcing_sum` is "D divides every forcing sum", for every `q` since `T` carries `q`.
- **2.** `gap_isCoprime_q`: `q` odd, `IsCoprime q (n 0)` ⇒ `IsCoprime q (gap r)` for every `r < m` (proof with an arbitrary divisor `d ∣ q`: `q_dvd_T`, `dvd_gap_orb`, `dvd_gap_isUnit`). The run-start form is `run_start_gaps_coprime` (with `dvd_gap_run_iff`, `exists_run_start`); "run start" is a rank whose orbit predecessor `orb r (m − 1)` is forced.
- **Dictionary** (checked by the Lean lane against the definitions): `OrdCycle` is the reduced integer cycle with `n_i = C(w.rotate i)/g`, so `Ẑ_i = g·Z_i`, `G_r = g·Δ_r`, `T_r = q·τ_r`, `D = g·q`; the word-normalisation forms above are the Lean statements through this dictionary. Both hypotheses of 2 are needed: tripling every state at parameter `3q` breaks reducedness and the statement; oddness of `q` amounts to letter positivity.

Not formalised: that the run starts are exactly `J` in number; the word-level corollaries as separate theorems.

## Remarks

- **What this is not.** An exact reformulation for the ordered class, valid for every `q`, not an exclusion. No novelty is claimed.
- **Consequences recorded elsewhere.** `J = 1` gives `D = q` ([`single-forced-position-denominator`](../single-forced-position-denominator.md)); in the Collatz range band 1 needs `J ≥ 3` ([`band-one-three-forced-positions`](../band-one-three-forced-positions.md)); the run starts form a `J`-state generalised Collatz cycle ([`run-start-gap-recursion`](../run-start-gap-recursion.md)).
- **Link to rotation distance (observed, not proved).** The rotation that moves each state to the next sorted rank differs from the word in at most `2J` positions: this held on all 900 ordered Collatz-range cycles tested (`m ≤ 12`, letters 1–3), with equality attained ([`jterm_gap_check.py`](jterm_gap_check.py)). A proof sketch gives `2J + 2` (the exponent word's rotation contributes 2 mismatches, each sorted height change at most 2 more). If true, main's target "every rotation has mismatch count `≥ F(m)`" ([`rotation-distance-growth`](../../questions/rotation-distance-growth.md)) would imply `J ≥ F(m)/2` for ordered `q = 1` cycles. Not formalised; heuristic as a general statement.
- **Calibration (feed update 08:22, not backed by a committed script).** Combining C006's `L > 2^(floor((m−1)/J) − B)` with an upper bound on `L` from Matveev (`K_0 < 6·10^8`, [`matveev-2000-linear-forms`](../../../../sources/matveev-2000-linear-forms.md)) and the period bound `m > 1.375·10^11` ([`hercher-2023-cycle-length`](../../../../sources/hercher-2023-cycle-length.md), [`barina-2025-convergence-2-71`](../../../../sources/barina-2025-convergence-2-71.md)), the side lane estimated that every hypothetical nontrivial Collatz cycle with `H < 8L` has `J ≥ 6`, and in general `J > (m−1)/(K_0·log₂(2em) + log₂ m + 2)`. So fixed-`J` statements exclude nothing new at `q = 1`; the closed form can help only through estimates uniform in a `J` that grows with `m`. The formal gap version of this `J` bound is in [`ordered-cycle-height-change-growth`](../ordered-cycle-height-change-growth.md).
- **Controls.** The 33 actual ordered `3x+q` cycles (including `q = 5, 7, 13, 61`) satisfy both statements, as they must: neither uses `q = 1`.

## History

- Created from the side-lane feed entry "LEAD (ordered cycles): every sorted gap is an explicit signed sum over the `J` forced positions, and in the Collatz range band 1 needs `J ≥ 3`" (2026-10-19 06:30, index convention fixed 06:40) and its updates 07:33 (Lean S1-a), 07:51 (Lean S1-b, the stronger single-gap form) and 08:06 (Lean S1-c/d), by the B05 migration (Claude, Opus 5.5). The legacy S1 has no folder of its own; its probes `reviews/side_lane/s1a_integer_cycle_check.{py,json}`, `s1b_run_start_gcd_check.{py,json}` and `s1cd_gap_coprime_check.{py,json}` moved here at commit `be73a66`.
- B17 migration (2026-10-20): the side-lane probe `jterm_gap_check.{py,json}` moved here byte-identical from legacy `reviews/side_lane/` (it was the one side-lane probe left outside the B04/B05 moves). With it in place, `s1cd_gap_coprime_check.py` passes at its new path; both became certificates.
- Authorship: side lane (Claude, Opus); formalisation by the Lean lane (Claude, Fable). The 06:40 fix made `E_i` the sum of the exponents *before* orbit position `i` (`E_0 = 0`), which is the Lean `E`.
