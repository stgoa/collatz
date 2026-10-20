---
id: rise-lemma
kind: result
title: "The rise lemma: each agreeing run of a rotation multiplies the log-height by at most log₂3"
status: formal
claim: >
  Odd-only 3x+q map, odd q. Let n_0, …, n_(m−1) be a primitive positive odd cycle with letters ≥ 1, minimum
  L = n_0, log-profile y_p = log₂(n_p/L), κ = log₂3 + q/(3L·ln 2), and fix an offset d ≢ 0 (mod m) of a
  rotation. For a forward stretch from u to v containing k mismatches of d (positions u ≤ e < v with
  a_e ≠ a_(e+d)), and any Δ ≥ 0 with y_(p+d) − y_p ≤ Δ on the stretch, y_v + c ≤ κ^(k+1)·(y_u + c) with
  c = log₂L + 1 + Δ. Corollary 1: from the minimum to the maximum, the mismatch count s(h) of the rotation
  satisfies s(h) ≥ log_κ(1 + B/c) − 1 with B = max y, and Δ = (log₂3 − 1 + q/(3L·ln 2))·|h|_m is admissible
  in the better orientation (both orientations have the same s). No gap, period or height hypothesis.
authors:
  - Claude side lane (Opus)
created: 2026-10-19
depends_on: [paired-state-run-law]
lean:
  - LeanLane.Cyc.OddCycle.eta
  - LeanLane.Cyc.OddCycle.kappa
  - LeanLane.Cyc.OddCycle.Phi
  - LeanLane.Cyc.OddCycle.eps_le_eta
  - LeanLane.Cyc.OddCycle.kappa_mul_log2
  - LeanLane.Cyc.OddCycle.one_le_kappa
  - LeanLane.Cyc.OddCycle.Phi_nonneg
  - LeanLane.Cyc.OddCycle.le_runSum
  - LeanLane.Cyc.OddCycle.runSum_mono
  - LeanLane.Cyc.OddCycle.rise_bound
  - LeanLane.Cyc.OddCycle.rise_le_mul
  - LeanLane.Cyc.OddCycle.witness_two_pow
  - LeanLane.Cyc.OddCycle.witness_log
  - LeanLane.Cyc.OddCycle.run_step
  - LeanLane.Cyc.OddCycle.rise_lemma
  - LeanLane.Cyc.OddCycle.rise_from_min
  - LeanLane.Cyc.OddCycle.rise_from_min_uniform
  - LeanLane.Cyc.OddCycle.mis_card_neg
  - LeanLane.Cyc.OddCycle.log_rise_from_min
evidence:
  - "s13_rise_lemma.py, s13_rise_lemma.json: side-lane probe (about 100 s): checks (W), the lemma for every pair (u, v) (m ≤ 64) or from the minimum (larger m), every rotation and both orientations, Corollary 1, the bound on Δ⁺, and Corollary 4 on exhaustive words; no violation (counts in Certificates). Fails at its new path: it imports s1a_integer_cycle_check from its own folder (now in ../ordered-gap-closed-form/); with that folder on PYTHONPATH it exits 0 and leaves its receipt byte-identical (checked at migration). Passed at be73a66 as reviews/side_lane/s13_rise_lemma.py (archive/legacy-checker-run-be73a66.md)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed S13 entry, update 17:40: adversarial review of S13 §§1-2, no hole found; (W) and (P) confirmed including empty runs, a mismatch at u and the trivial last factor; primitivity load-bearing; orientation; the uniform-Δ formal form. Lean units S13-a (iteration 93) and S13-d's log_rise_from_min (iteration 95) verified"
    link: ../../../../archive/side-lane/FEED.md
aliases: [S13]
tags: [cycles, rotation-distance, height, rise-lemma, formal]
---

# The rise lemma: each agreeing run of a rotation multiplies the log-height by at most log₂3

## Statement

**Setting.** `n_0, …, n_(m−1)` is a primitive positive odd cycle of `3x+q`, with `q` odd, `2^(a_p) n_(p+1) = 3n_p + q` and letters `a_p ≥ 1`. Its minimum is `L`, with `ℓ' = log₂ L`. The log-profile is `y_p = log₂(n_p/L)`, and `B = max y` is the log-height. Constants: `σ = log₂3 − 1`, `η = q/(3L·ln 2)` and `κ = log₂3 + η`. (For a nontrivial `q = 1` cycle with `L ≥ 2^20`, `η < 5·10^(−7)`.) Fix a rotation `0 < h < m` and an orientation, i.e. a forward offset `d ∈ {h, m − h}`. A position `p` is a **mismatch** when `a_p ≠ a_(p+d)`; both orientations have the same number `s = s(h)` of mismatches.

**Rise lemma.** Take a forward stretch from `u` to `v` containing `k` mismatches `e_1 < … < e_k` (all positions `u ≤ e < v`), and let `Δ ≥ 0` bound `y_(p+d) − y_p` on the stretch. With `c = ℓ' + 1 + Δ`,

```
y_v + c ≤ κ^(k+1) · (y_u + c).
```

In words: inside the stretch, each agreeing run of the rotation can raise the profile by at most a factor `log₂3` (up to the additive constant `c`). The constant `c` is the log of the minimum, plus how much higher a run's partner can sit.

**The run-start version (written, reviewed; the legacy note's form).** It suffices to take `Δ = Δ⁺ = max_j (y_(b_j+d) − y_(b_j))⁺` over the run starts `b_0 = u` (counted only when `u` is not a mismatch) and `b_j = e_j + 1` (`b_k` counted only when its run reaches past `v`). The supply of agreement comes only from the larger of the two elements at a run's start. The formal form above, with a uniform `Δ`, is strictly weaker and is all that the corollaries use.

**Corollary 1 (height against mismatches).** Apply the lemma from the minimum to the maximum:

```
s(h) ≥ k ≥ log_κ(1 + B/c) − 1,      c = ℓ' + 1 + Δ.
```

Two bounds on `Δ`:
- `Δ⁺ ≤ (σ + η)·d` for the forward offset `d`. Choosing the better orientation gives `Δ⁺ ≤ (σ + η)·|h|_m`, with `|h|_m = min(h, m − h)`.
- `Δ⁺ ≤ max_p μ_h(p) ≤ Var(μ_h)/2 ≤ V_h/2 + δ`, in the notation of [`denjoy-koksma-height-bound`](../denjoy-koksma-height-bound/README.md). Here `δ = A − m·log₂3` is in bits; the Lean statements of S12 use natural logs. This bound is used in [`largest-letter-rho-reduction`](../largest-letter-rho-reduction.md).

## Proof

Legacy note `RISE_LEMMA.md` (S13, side lane), §2, lightly edited.

- **(W) The 2-adic start witness.**
  - Suppose `a_p = a_(p+d)` for `b ≤ p < e`, with letter sum `F = a_b + … + a_(e−1)`. Then `n_b ≡ n_(b+d) mod 2^(F+1)`.
  - One way to see it: for odd `x`, the next letter `v₂(3x + q)` and the next state modulo `2^j` depend only on `x mod 2^(j+a)`. Induct on the run.
  - The other way, from the formal run identity ([`paired-state-run-law`](../paired-state-run-law.md)): `2^F (n_e − n_(e+d)) = 3^t (n_b − n_(b+d))`. Here `n_e − n_(e+d)` is even and nonzero, because the cycle is primitive and `d ≢ 0`.
  - Either way `max(n_b, n_(b+d)) > 2^(F+1)`, that is `F + 1 < ℓ' + max(y_b, y_(b+d)) ≤ ℓ' + y_b + Δ⁺`.
- **(P) The profile step.**
  - `y_(p+1) − y_p = log₂3 − a_p + ε_p`, with `0 < ε_p = log₂(1 + q/(3n_p)) ≤ η`.
  - A run of `t` letters with sum `F ≥ t`, followed by its mismatch letter (`≥ 1`), raises `y` by at most `(t + 1)·log₂3 − F − 1 + (t + 1)η ≤ (σ + η)(F + 1)`.
- **Induction.**
  - Write `Y_j = y_(b_j)`. By (W), `F_j + 1 ≤ Y_j + c`. This is strict for a nonempty run; for an empty run (consecutive mismatches) `F_j + 1 = 1 ≤ c`.
  - So `Y_(j+1) ≤ Y_j + (σ + η)(Y_j + c)`, that is `Y_(j+1) + c ≤ κ(Y_j + c)`.
  - The last, partial run from `b_k` to `v` satisfies the same inequality, by (W) at `b_k`.
  - Chaining `k + 1` factors gives the lemma.
- **The bound on `Δ⁺`.** `y_(b+d) − y_b = d·log₂3 − (a_b + … + a_(b+d−1)) + Σε ≤ (σ + η)·d`.
- **Corollary 1.** Use `u = argmin` (`y_u = 0`), `v = argmax`, and `k ≤ s`.

**Review notes (the Lean lane, 2026-10-19; no hole found).**
- **Primitivity is load-bearing.** In (W), `n_b − n_(b+d) ≠ 0` comes from distinct states at distinct positions, that is, from primitivity and `d ≢ 0`. It does not come from `e` being a mismatch. So (W) applies directly to the last partial run `[b_k, v)` with its own letter sum, and to `k = 0`. For a non-primitive cycle, the `k = 0` instance would claim `B ≤ (κ − 1)(ℓ' + 1)` from nothing. "Primitive" therefore stays an explicit hypothesis.
- **Orientation.** Each orientation is a separate valid lemma. The mismatch sets correspond under `p ↦ p + d`, so `s` is shared, while `Δ⁺` depends on the orientation. Corollary 1 fixes `d = |h|_m` and uses that orientation's bound.
- **Formal form.** Any `Δ` with `log n_(p+d) − log n_p ≤ Δ` on the stretch works; this is strictly weaker than the run-start version and is all that Corollaries 1–4 use. In natural logs, with `Φ_p = log n_p + log 2 + Δ`, the lemma reads `Φ_v ≤ κ^(k+1)·Φ_u` with `κ = (log 3 + q/(3L))/log 2`.

## Certificates

None run by CI; `s13_rise_lemma.py` (about 100 s) is a probe (see `evidence`). It found no violation in any check; the counts are totals over the actual cycles and the exhaustive words together:

| check | instances |
|---|---|
| (W) at every run start (and at the minimum), as an exact congruence and as an inequality | 3,358,654 |
| the lemma, every pair `(u, v)`, every rotation, both orientations (`m ≤ 64`); stretches starting at the minimum for larger `m` | 168,379,570 |
| Corollary 1 with the cycle's own `Δ⁺`, and with `(σ + η)|h|_m` | 282,128 each |
| `Δ⁺ ≤ (σ + η)d` | 282,128 |
| Corollary 4 on exhaustive primitive words (`{1,2,3}`, `m ≤ 9`; `{1,…,4}`, `m ≤ 7`; 6,008 words) | 39,512 (minimum margin 5.57 bits) |

- **The inputs.** Actual cycles: all 4,218 cycles of `3x+q` with `m ≥ 2`, for odd `q < 2000` with `3 ∤ q` (seeds `≤ 1001`), covering 101,552 rotations. Exhaustive words: 6,008 primitive words with `D > 0`, one per rotation class. The controls `q = 5` (4 cycles), `q = 7` (1), `q = 13` (8) and `q = 61` (1) have no violation.
- **Sharpness.** The smallest slack over all lemma checks is 0.30 mismatch units on actual cycles and 0.55 on words.
- **Why the factor is right.** A run of `t` ones from `n = 2^(t+1) − q` ends at `2·3^t − q`. So one run multiplies `log₂(n + q)` by `log₂3 − O(1/t)`, and the per-run factor `log₂3` cannot be lowered.
- **Example.** The near-tight checks are such runs. The `3x+499` cycle of length 50 climbs from `1549 = 2^11 − 499` through nine `1`s with no mismatch of `h = 1`, with slack 0.32.

## Lean

`lean/CycleSpectrum.lean` (axioms `propext`, `Classical.choice`, `Quot.sound`; receipts `lean/receipts/CycleSpectrum.*`), namespace `LeanLane.Cyc.OddCycle`:

- **S13-a** (iteration 93). Definitions `eta` (`η = q/(3n₀)`), `kappa` (`κ = (log 3 + η)/log 2`), `Phi Δ p` (`Φ_p = log n_p + log 2 + Δ`); helpers `eps_le_eta`, `kappa_mul_log2`, `one_le_kappa`, `Phi_nonneg`, `le_runSum`, `runSum_mono`; (P) **`rise_bound`** (`log n_(i+t) − log n_i ≤ t(log 3 + η) − F·log 2`), **`rise_le_mul`** (`log n_(p+d) − log n_p ≤ d(log 3 + η − log 2)`, the uniform `Δ`); (W) **`witness_two_pow`** (`2^(F+1) ∣ n_(i+d) − n_i` on an agreeing run, from `z_run_factor`), **`witness_log`** (`(F + 1)·log 2 ≤ log n_i + Δ`; nonvanishing from `z_ne_zero`, i.e. primitivity); **`run_step`**; **`rise_lemma`** (`Φ_v ≤ κ^(k+1)·Φ_u`, `k` the number of mismatches of `[u, v)`); **`rise_from_min`** (`Φ_j ≤ κ^(s+1)·Φ_0` for `j ≤ m`, `s = |mis d|`) and **`rise_from_min_uniform`** (with `Δ = d(log 3 + η − log 2)`).
- **S13-c** (iteration 94): **`mis_card_neg`** (`|mis(m − h)| = |mis h|`, the orientation lemma).
- **S13-d** (iteration 95): **`log_rise_from_min`** (`log(1 + B/C) ≤ (s + 1)·log κ` with `C = log n₀ + log 2 + Δ`, `B = log n_j − log n₀`), the logarithmic form of Corollary 1; with `mis_card_neg` it gives Corollary 1 in the better orientation.

**Statement match.** `Φ = (y + c)·log 2` with `c = ℓ' + 1 + Δ/log 2`, and `κ = log₂3 + q/(3L·ln 2)`, exactly as in the Statement (the Statement's `Δ` is in bits). Hypotheses: `hprim` (distinct states), letters `≥ 1`, `d % m ≠ 0`, `Δ ≥ 0`, with `Δ` bounding the partner offset on `[u, v]`. No mismatch at the run's end is used, matching the review. Not formal: the run-start `Δ⁺` refinement (written, reviewed) and the base-2 rearrangement of Corollary 1 beyond `log_rise_from_min`.

## Remarks

The rest of the legacy note (§4), lightly edited. The corollaries became separate nodes: Corollaries 2, 3 and 5 [`short-rotation-mismatch-growth`](../short-rotation-mismatch-growth/README.md) (numbers conditional on EXT-1), Corollary 4 [`rise-lemma-denominator-law`](../rise-lemma-denominator-law.md), Corollaries 6–7 [`largest-letter-rho-reduction`](../largest-letter-rho-reduction.md).

- **Novelty undetermined.** The case `h = 1` is in the spirit of the classical circuit analysis (Steiner; Simons–de Weger; Hercher), where each circuit's minimum is at least about `2^(t+1)`. The side lane had not seen the general-rotation form, or its combination with S5, in the literature. For the statistic "number of circuits", Hercher's `≥ 92` ([`hercher-2023-cycle-length`](../../../../sources/hercher-2023-cycle-length.md)) is far stronger at the imported periods; the gain here is uniformity in `h`.
- **Comparison with S12** ([`denjoy-koksma-height-bound`](../denjoy-koksma-height-bound/README.md)). S12 gives `B ≤ (K − 1)·Var`. The rise lemma gives `B ≤ (κ^(s+1) − 1)(ℓ' + 1 + Δ⁺)`. It is exponential in `s`, needs no coprimality, and charges only `Δ⁺ ≤ Var/2`. They are complementary. When `ℓ'` is small next to `Var`, the rise lemma is the stronger one exactly when `κ^(s+1) − 1 < 2(K − 1)`. S12 has no `ℓ'` term, so it is the stronger one when `Var` is small next to `ℓ'`.
- **Long rotations are unchanged.** For `|h|_m ≥ m/10` the combined count of Corollary 2 is at most 4, and S7's formal `ρ ≥ 4` ([`three-mismatch-exclusion`](../three-mismatch-exclusion/README.md)) is at least as strong there. The obstruction is exactly S7/S8/S10's: a tall profile whose rise is fed by a partner a fixed fraction of the period ahead, so `Δ⁺ ≈ σ|h|`. Neither this lemma nor S12 (which is silent when the drop sits at a mismatch) touches it.

## History

- Migrated from `experiments/cycle_spectrum/S13/RISE_LEMMA.md` (legacy ID `S13`; side-lane producer batch S13, 2026-10-19) at commit `be73a66`, by the B06 migration (Claude, Opus 5.5). The note's Corollaries 2–7 became three further nodes (Remarks). The probe `reviews/side_lane/s13_rise_lemma.{py,json}` moved here. The note's status line read "A written proof, checked on actual cycles and on exhaustive words. The Lean lane has not reviewed it yet", written before the review below; its §5 ("candidate units for the Lean lane") is superseded by the Lean section, and its "Reproduce" block pointed to the old paths.
- Side lane (Claude, Opus), feed 2026-10-19 17:32 (LEAD, S13).
- **Review (17:40).** The Lean lane's adversarial review found no hole (ACK of primitivity, orientation and the formal form). **CORRECTION (clarification):** in the second `Δ⁺` bound, `Δ⁺ ≤ V_h/2 + δ`, `δ = A − m·log₂3` is in bits (the S12 note's convention), while the Lean statements of S12 use natural logs; marked in the note. The reviewer's independent spot checks agreed (`ℓ'_max(1.375·10^11) ≈ 12,824`, `F(1) = 28`, `F(√m) = 23`, `c_4 ≈ 0.0752`).
- Formalised by the Lean lane (Claude, Fable): S13-a at 17:58 (`95ae39f`), S13-c at 18:12 (`1c33452`), S13-d at 18:21 (`8b56b8e`, the lane's final commit). Both lanes stopped at 18:21 at the user's request.
