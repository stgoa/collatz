---
id: run-start-gap-recursion
kind: result
title: The run starts of an ordered cycle's gap system form a J-state generalised Collatz cycle, with an exact oddness rule
status: formal
claim: >
  Raw odd-only 3x+q map, any q, notation of ordered-gap-closed-form. In a circularly ordered integer cycle,
  let r_0 be a run start followed by t zero-forcing steps with exponent total E_t, ending at the forced rank
  f = orb(r_0, t). Then 2^(E_t) divides Δ_(r_0); with u = Δ_(r_0)/2^(E_t), the gap at f is 3^t·u and
  2^(e_f)·Δ_(orb(r_0, t+1)) = 3^(t+1)·u + T_f; at the next run start r_1 (exponent total E′ over its run,
  u′ = Δ_(r_1)/2^(E′)), 2^(e_f + E′)·u′ = 3^(t+1)·u + T_f. Moreover Σ_r Δ_r = 2^B·L and Σ_(r∈R) 2^(E_r) ≤ 2^B·L
  for any set R of run starts. Oddness rule: u is odd iff 2^(E_t+1) ∤ Δ_(r_0) iff the gap at f is odd; a scaled
  state is odd iff its height equals B; an interior gap is odd iff exactly one of its two heights equals B; the
  seam gap is odd iff h_[m−1] = B. Hence in band 1 every run ending at an interior forced rank has u odd, and a
  run ending at the seam has u odd iff the top sorted height is 1.
authors:
  - Claude side lane (Opus)
created: 2026-10-19
depends_on: [ordered-gap-closed-form]
lean:
  - LeanLane.Cyc.OrdCycle.run_dvd
  - LeanLane.Cyc.OrdCycle.run_end_eq
  - LeanLane.Cyc.OrdCycle.run_start_rec
  - LeanLane.Cyc.OrdCycle.run_start_rec_two
  - LeanLane.Cyc.OrdCycle.run_quot_odd_iff
  - LeanLane.Cyc.OrdCycle.E_add
  - LeanLane.Cyc.OrdCycle.sum_gap_eq_lo
  - LeanLane.Cyc.OrdCycle.sum_run_bound
  - LeanLane.Cyc.OddCycle.Z_odd_iff
  - LeanLane.Cyc.OrdCycle.run_quot_odd_iff_end
  - LeanLane.Cyc.OrdCycle.gap_odd_iff
  - LeanLane.Cyc.OrdCycle.gap_seam_odd_iff
  - LeanLane.Cyc.OrdCycle.T_ne_zero_iff
  - LeanLane.Cyc.OrdCycle.band1_u_odd
  - LeanLane.Cyc.OrdCycle.seam_u_odd_iff
evidence:
  - "../attempts/ordered-cycle-run-renormalisation/README.md, sections 1-2 of 'What happened': the written statements (legacy S02 note sections 1-2)"
  - "../attempts/ordered-cycle-run-renormalisation/s2_ucycle_explore.py and its receipt: the identity and the bookkeeping on 33 actual and 337 rational ordered cycles, and the oddness table (39/39 and 478/478 band-1 interior-ending runs odd; seam-ending runs odd exactly when the top height is 1). It no longer runs at the new path (see that node)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Lean units S2-a (iteration 59) and S2-b (iteration 60) verified, statement match recorded in the legacy lean/STATE.md notes S2-a and S2-b; the lane's pre-review fixed that oddness of u is an extra condition, not a consequence"
    link: ../../../archive/lean-lane/STATE.md
tags: [cycles, ordered-cycles, gap-system, formal]
---

# The run starts of an ordered cycle's gap system form a J-state generalised Collatz cycle, with an exact oddness rule

## Statement

Notation of [`ordered-gap-closed-form`](ordered-gap-closed-form/README.md): an ordered integer cycle at parameter `q`, sorted gaps `Δ_r` (seam included), rank exponents `e_r`, forcing `T_r`, rank orbit `orb(r_0, k) = r_0 + k·s mod m`, exponent totals `E(r_0, t) = Σ_(k<t) e(orb(r_0, k))`. A run start is a rank whose orbit predecessor is forced.

1. **Run law.** If `T(orb(r_0, k)) = 0` for `k < t`, then `2^(E_t) | Δ_(r_0)`, and with `u = Δ_(r_0)/2^(E_t)` the gap at the forced rank `f = orb(r_0, t)` is `3^t·u`.
2. **Run-start recursion.** `2^(e_f)·Δ_(orb(r_0, t+1)) = 3^(t+1)·u + T_f`; at the next run start, `2^(e_f + E′)·u′ = 3^(t+1)·u + T_f`. With `Σ_k (e_(f_k) + E_k) = A` and `Σ_k (t_k + 1) = m`, the run starts form a `J`-state cycle of a generalised Collatz map with multipliers `3^(t+1)`, offsets `T` and the same `D`; its cycle equation is the closed form of [`ordered-gap-closed-form`](ordered-gap-closed-form/README.md).
3. **Sizes.** `Σ_(r<m) Δ_r = 2^B·L` and `Σ_(r∈R) 2^(E_r) ≤ 2^B·L` for every set `R` of run starts.
4. **Oddness rule.** `u` is odd iff `2^(E_t+1) ∤ Δ_(r_0)` iff the gap at `f` is odd. A scaled state `2^(B−h)·n` is odd iff `h = B`; an interior gap is odd iff exactly one of its two heights equals `B`; the seam gap `2Z_[0] − Z_[m−1]` is odd iff `h_[m−1] = B`. In band 1, every run ending at an interior forced rank has odd `u`, and a seam-ending run has odd `u` iff the top sorted height is 1.

## Proof

Legacy S02 §§1–2, now in [`ordered-cycle-run-renormalisation`](../attempts/ordered-cycle-run-renormalisation/README.md). 1–2 are the unrolled gap recursion (`gap_unroll` of [`ordered-gap-closed-form`](ordered-gap-closed-form/README.md)) at `n = t` and `n = t + 1`: inside a run the forcing sum is zero, so `2^(E_t)·Δ_f = 3^t·Δ_(r_0)`, and `gcd(2, 3) = 1` gives the divisibility. 3 is `Σ Δ = Z_0` with every run-start gap at least `2^(E_r)`. 4: a difference of two scaled states with odd `n, n′` is odd iff exactly one of the two powers `2^(B−h)`, `2^(B−h′)` is `1`; by 1, `v₂(Δ_f) = v₂(u)` since `3^t` is odd. In band 1 an interior forced rank has two different heights in `{0, 1}`, so exactly one equals `B = 1`.

## Lean

`lean/CycleSpectrum.lean`, Lean units S2-a (iteration 59) and S2-b (iteration 60); axioms `propext`, `Classical.choice`, `Quot.sound`; receipts `lean/receipts/CycleSpectrum.*`.

- **S2-a.** For a run start `r₀` with `t` zero-forcing steps: `run_dvd` (`2^(E_t) ∣ Δ_(r₀)`), `run_end_eq` (`Δ_(orb r₀ t) = 3^t·(Δ_(r₀)/2^(E_t))`), `run_start_rec` (the identity of 2), `run_start_rec_two` (two-run form with `u′` at the next run start), `run_quot_odd_iff` (`u` odd ⇔ `2^(E_t+1) ∤ Δ_(r₀)`), `E_add` (the bookkeeping behind `Π 2^(E′) = 2^A`), `sum_gap_eq_lo` (`Σ Δ = 2^B·L`), `sum_run_bound` (3). The partition of the orbit into runs (the list of run starts) and the products `Π 3^(t_k+1) = 3^m`, `Π 2^(E′_k) = 2^A` are not formalised as one statement; they follow from `E_m`, `orb_m` and `E_add` once the partition is given.
- **S2-b.** `Z_odd_iff` (`Z_i` odd ⇔ `h_i = B`), `run_quot_odd_iff_end` (`u` odd ⇔ the gap at the forced rank `orb r₀ t` is odd), `gap_odd_iff` (stated as `h_[r+1] = B ↔ ¬ h_[r] = B`), `gap_seam_odd_iff`, `T_ne_zero_iff` (interior forcing ⇔ change of height), `band1_u_odd`, `seam_u_odd_iff`. The prose's "interior" is `orb r₀ t + 1 < m` and its "seam run" is `orb r₀ t = m − 1`.

Not consequences, and not claimed: `u` odd in general (S1 gives only `2^(E_t) | Δ`), and the value set `τ ∈ {±1, 2, 3}`, which is the `q = 1`, `B = 1` case (at `B = 2` the values are `±1, ±2, ±3` and `4, 6, 7`; for general `q` everything carries the factor `q`).

## Remarks

- The attempt to iterate this compression is rejected: [`ordered-cycle-run-renormalisation`](../attempts/ordered-cycle-run-renormalisation/README.md).
- The AM–GM step `Σ_k 2^(E_k) ≥ J·2^(Σ E_k/J)` is not formalised; it improves the `J` bound only by `−log₂ J`.
- Novelty: bookkeeping identities; none claimed.

## History

- Split from `experiments/cycle_spectrum/S02/RENORMALISATION.md` §§1–2 (legacy ID `S02`) at commit `be73a66`, by the B05 migration (Claude, Opus 5.5). Side lane (Claude, Opus), feed 2026-10-19 10:52. Formalised pre-emptively by the Lean lane as S2-a (before the note landed, from the feed announcement) and S2-b (from the note's §2, legacy commit `28f4491`).
