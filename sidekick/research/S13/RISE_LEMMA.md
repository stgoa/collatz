# S13: the rise lemma, and a growing mismatch bound for short rotations

**Status:** side-lane producer batch S13 (2026-10-19). A written proof, checked on actual cycles and on exhaustive words. The Lean lane has not reviewed it yet.

**Novelty undetermined.** The case `h = 1` is in the spirit of the classical circuit analysis (Steiner; Simons–de Weger; Hercher), where each circuit's minimum is at least about `2^(t+1)`. This lane has not seen the general-rotation form, or its combination with S5, in the literature.

## 1. Statements

**Setting.**
- `n_0, …, n_(m−1)` is a primitive positive odd cycle of `3x+q`, with `q` odd, `2^(a_p) n_(p+1) = 3n_p + q` and letters `a_p ≥ 1`.
- Its minimum is `L`, with `ℓ' = log₂ L`. The log-profile is `y_p = log₂(n_p/L)`, and `B = max y` is the log-height.
- Constants: `σ = log₂3 − 1`, `η = q/(3L ln 2)` and `κ = log₂3 + η`. For a nontrivial `q = 1` cycle with `L ≥ 2^20`, `η < 5·10^(−7)`.
- Fix a rotation `0 < h < m` and an orientation, i.e. a forward offset `d ∈ {h, m − h}`.
  - A position `p` is a **mismatch** when `a_p ≠ a_(p+d)`.
  - Both orientations have the same number `s = s(h)` of mismatches.

**Rise lemma.** Take a forward stretch from position `u` to position `v` containing `k` mismatches `e_1 < … < e_k` (all positions `u ≤ e < v`).
- Its run starts are `b_0 = u` and `b_j = e_j + 1`. The start `b_0` counts only when `u` is not a mismatch, and `b_k` counts only when its run reaches past `v`.
- Put `Δ⁺ = max_j (y_(b_j+d) − y_(b_j))⁺` over the counted run starts, and `c = ℓ' + 1 + Δ⁺`. Then

```
y_v + c ≤ κ^(k+1) · (y_u + c).
```

In words: inside the stretch, each agreeing run of the rotation can raise the profile by at most a factor `log₂3` (up to the additive constant `c`). The constant `c` is the log of the minimum, plus how much higher a run's partner can sit. The supply of agreement comes only from the larger of the two elements at the run's start.

**Corollary 1 (height against mismatches).** Apply the lemma from the minimum to the maximum:

```
s(h) ≥ k ≥ log_κ(1 + B/c) − 1,      c = ℓ' + 1 + Δ⁺.
```

Two bounds on `Δ⁺`:
- `Δ⁺ ≤ (σ + η)·d` for the forward offset `d`. Choosing the better orientation gives `Δ⁺ ≤ (σ + η)·|h|_m`, with `|h|_m = min(h, m − h)`.
- `Δ⁺ ≤ max_p μ_h(p) ≤ Var(μ_h)/2 ≤ V_h/2 + δ`, in the S12 note's notation. Here `δ = A − m log₂3` is in bits; the Lean statements of S12 use natural logs. *(Clarified after the Lean lane's review.)*

**Corollary 2 (`q = 1`: short rotations, combined with S5).**
- **Inputs.** `ℓ' ≤ 172 + 342 log₂ m − log₂3`, from the drift bound `L ≤ m·2^A/(3D)` (formal: `three_L_D_le`) and `gap_all` (`2^A ≤ 2^172 m^341 D`). `gap_all` is a replayed external result (EXT-1, `mmusson/collatz`), so Corollary 2's numbers inherit its status.
- **The two bounds.**
  - S5's end witness forces `1 + t·log₂3 < ℓ' + B` on the longest run `t ≥ ⌈(m − s)/s⌉`. This weakens as `B` grows.
  - Corollary 1 strengthens as `B` grows.
- **Combination.** Taking the worse of the two over all `B` gives a guaranteed count `F(m, H₀)` for every rotation with `|h|_m ≤ H₀`. It uses no height hypothesis at all (`s13_short_rotations.py`, exact integer search over `s`, bisection over `B`).

| `m` | `|h|_m ≤ 1` | `≤ ℓ'_max` | `≤ 10ℓ'_max` | `≤ √m` | `≤ m^(3/4)` | `≤ m/1000` | `≤ m/100` | `≤ m/10` | `≤ m/3` |
|---|---|---|---|---|---|---|---|---|---|
| `2^19` | 6 | 6 | 4 | 6 | 5 | 6 | 6 | 4 | 3 |
| `10^7` | 11 | 10 | 8 | 11 | 6 | 10 | 7 | 4 | 3 |
| `1.375·10^11` | **28** | **27** | 25 | 23 | 11 | 11 | 7 | 4 | 3 |
| `10^15` | 46 | 45 | 42 | 32 | 15 | 11 | 7 | 4 | 3 |
| `10^20` | 70 | 69 | 65 | 43 | 20 | 11 | 7 | 4 | 3 |
| `10^30` | 117 | 116 | 113 | 68 | 32 | 11 | 7 | 4 | 3 |

The columns are not in increasing order of `H₀` at small `m`; for example, at `m = 2^19`, `√m = 724` while `ℓ'_max = 6,668`. `F` is nonincreasing in `H₀` at fixed `m`.

**Asymptotics.**
- For any `X > 0`: `s(h) ≥ min( m·log₂3/(ℓ' + X + σ), log_κ(1 + X/c) − 1 )`. Take `X = m/log_κ m`.
- With `ℓ' = O(log m)`, every rotation with `|h|_m ≤ m^(1−θ)` then has

```
s(h) ≥ θ · log_κ m − log_κ log_κ m − O(1)
```

  mismatches. Here `κ → log₂3`, so the rate is about `1.505 θ log₂ m`.
- Computed values of `F(m, m^(1−θ))`:

| `m` | `θ = 1/4` | `θ = 1/2` | `θ = 3/4` | `θ = 1` |
|---|---|---|---|---|
| `10^12` | 11 | 25 | 32 | 32 |
| `10^24` | 25 | 53 | 82 | 89 |
| `10^48` | 53 | 111 | 170 | 205 |

**Corollary 3 (localization of small mismatch counts).** At fixed `S`, `F(m, H₀) ≤ S` forces `H₀` above a threshold. So a rotation with `s(h) ≤ S` must have `|h|_m ≥ c_S·m`. The thresholds are essentially independent of `m` once `m ≥ 10^11`:

| `S` | 4 | 5 | 6 | 7 | 8 | 10 | 12 | 15 |
|---|---|---|---|---|---|---|---|---|
| `c_S` at `m = 1.375·10^11` | 0.0752 | 0.0365 | 0.0187 | 0.0100 | 0.0055 | 0.0017 | 0.00057 | 0.00011 |

- S7 already excludes `s ≤ 3`.
- Any rotation with four mismatches, the paused `ρ ≥ 5` case, must therefore have `|h|_m ≥ 0.075m`.
- At `m = 2^19` and `10^7`, only `S ≤ 5` and `S ≤ 10` respectively have a positive threshold (`s13_short_rotations.json`).

**Corollary 4 (word form, any `q`).**
- **Data of the word.** For a primitive positive word `w` with `D > 0`, take its rational cycle `x_p`, with height `B` and minimum `x_min`. Put `κ_w = log₂3 + 1/(3x_min ln 2)` and `λ(w) = log₂(m 2^A/(3D))`.
- **Why it follows.** The integer cycle `den(w)·x_p` is an odd cycle of `3x + den(w)` with the same profile, and `η = 1/(3x_min ln 2)`.
- **The law:**

```
log₂ den(w) ≥ B/(κ_w^(s+1) − 1) − 1 − (σ + η)|h|_m − λ(w).
```

This is a third denominator law, after S9 and S12. It is exponential in `s`, where S12's is linear in `K(h/m)`, and it holds for every rotation, coprime or not.

## 2. Proof

- **(W) The 2-adic start witness.**
  - Suppose `a_p = a_(p+d)` for `b ≤ p < e`, with letter sum `F = a_b + … + a_(e−1)`. Then `n_b ≡ n_(b+d) mod 2^(F+1)`.
  - One way to see it: for odd `x`, the next letter `v₂(3x + q)` and the next state modulo `2^j` depend only on `x mod 2^(j+a)`. Induct on the run.
  - The other way, from the formal run identity: `2^F (n_e − n_(e+d)) = 3^t (n_b − n_(b+d))`. Here `n_e − n_(e+d)` is even and nonzero, because the cycle is primitive and `d ≢ 0`.
  - Either way `max(n_b, n_(b+d)) > 2^(F+1)`, that is `F + 1 < ℓ' + max(y_b, y_(b+d)) ≤ ℓ' + y_b + Δ⁺`.
- **(P) The profile step.**
  - `y_(p+1) − y_p = log₂3 − a_p + ε_p`, with `0 < ε_p = log₂(1 + q/(3n_p)) ≤ η`.
  - A run of `t` letters with sum `F ≥ t`, followed by its mismatch letter (`≥ 1`), raises `y` by at most `(t + 1)log₂3 − F − 1 + (t + 1)η ≤ (σ + η)(F + 1)`.
- **Induction.**
  - Write `Y_j = y_(b_j)`. By (W), `F_j + 1 ≤ Y_j + c`. This is strict for a nonempty run; for an empty run (consecutive mismatches) `F_j + 1 = 1 ≤ c`.
  - So `Y_(j+1) ≤ Y_j + (σ + η)(Y_j + c)`, that is `Y_(j+1) + c ≤ κ(Y_j + c)`.
  - The last, partial run from `b_k` to `v` satisfies the same inequality, by (W) at `b_k`.
  - Chaining `k + 1` factors gives the lemma.
- **The bound on `Δ⁺`.** `y_(b+d) − y_b = d·log₂3 − (a_b + … + a_(b+d−1)) + Σε ≤ (σ + η)·d`.
- **Corollary 1.** Use `u = argmin` (`y_u = 0`), `v = argmax`, and `k ≤ s`.

**Review notes (the Lean lane, 2026-10-19; no hole found).**
- **Primitivity is load-bearing.** In (W), `n_b − n_(b+d) ≠ 0` comes from distinct states at distinct positions, that is, from primitivity and `d ≢ 0`. It does not come from `e` being a mismatch.
  - So (W) applies directly to the last partial run `[b_k, v)` with its own letter sum, and to `k = 0`.
  - For a non-primitive cycle, the `k = 0` instance would claim `B ≤ (κ − 1)(ℓ' + 1)` from nothing. "Primitive" therefore stays an explicit hypothesis.
- **Orientation.** Each orientation is a separate valid lemma. The mismatch sets correspond under `p ↦ p + d`, so `s` is shared, while `Δ⁺` depends on the orientation. Corollary 1 fixes `d = |h|_m` and uses that orientation's bound.
- **Formal form.** Any `Δ` with `log n_(p+d) − log n_p ≤ Δ` on the stretch works; this is strictly weaker than the run-start version and is all that Corollaries 1–4 use. In natural logs, with `Φ_p = log n_p + log 2 + Δ`, the lemma reads `Φ_v ≤ κ^(k+1) Φ_u` with `κ = (log 3 + q/(3L))/log 2`.

## 3. Data

`s13_rise_lemma.py` (about 100 s) found no violation in any check. The counts are totals over the actual cycles and the exhaustive words together:

| check | instances |
|---|---|
| (W) at every run start (and at the minimum), as an exact congruence and as an inequality | 3,358,654 |
| the lemma, every pair `(u, v)`, every rotation, both orientations (`m ≤ 64`); stretches starting at the minimum for larger `m` | 168,379,570 |
| Corollary 1 with the cycle's own `Δ⁺`, and with `(σ + η)|h|_m` | 282,128 each |
| `Δ⁺ ≤ (σ + η)d` | 282,128 |
| Corollary 4 on exhaustive primitive words (`{1,2,3}`, `m ≤ 9`; `{1,…,4}`, `m ≤ 7`; 6,008 words) | 39,512 (minimum margin 5.57 bits) |

- **The inputs.**
  - Actual cycles: all 4,218 cycles of `3x+q` with `m ≥ 2`, for odd `q < 2000` with `3 ∤ q` (seeds `≤ 1001`), covering 101,552 rotations.
  - Exhaustive words: 6,008 primitive words with `D > 0`, one per rotation class.
  - The controls `q = 5` (4 cycles), `q = 7` (1), `q = 13` (8) and `q = 61` (1) have no violation.
- **Sharpness.** The smallest slack over all lemma checks is 0.30 mismatch units on actual cycles and 0.55 on words.
- **Why the factor is right.** A run of `t` ones from `n = 2^(t+1) − q` ends at `2·3^t − q`. So one run multiplies `log₂(n + q)` by `log₂3 − O(1/t)`, and the per-run factor `log₂3` cannot be lowered.
- **Example.** The near-tight checks are such runs. The `3x+499` cycle of length 50 climbs from `1549 = 2^11 − 499` through nine `1`s with no mismatch of `h = 1`, with slack 0.32.

## 4. What this gives, and what it does not

- **A growing bound for a class of rotations defined by `|h|_m` alone.** No height hypothesis and no property of the word are needed. As far as this lane knows, it is the first such bound in the programme.
  - S5 and S12 give growth only under a height or variation hypothesis.
  - C011, S6 and S7 give the constants 3 and 4.
- **It moves the main objective.** Every rotation with `|h|_m = o(m)` has `s(h) → ∞`. Any hypothetical cycle with a bounded-mismatch rotation has it at a rotation by a fixed fraction of the period (Corollary 3).
- **Long rotations are unchanged.** For `|h|_m ≥ m/10` the combined count is at most 4, and S7's formal `ρ ≥ 4` is at least as strong there.
  - The obstruction is exactly S7/S8/S10's: a tall profile whose rise is fed by a partner a fixed fraction of the period ahead, so `Δ⁺ ≈ σ|h|`.
  - Neither this lemma nor S12 (which is silent when the drop sits at a mismatch) touches it.
- **Comparison with S12 (Denjoy–Koksma).**
  - S12 gives `B ≤ (K − 1)·Var`.
  - The rise lemma gives `B ≤ (κ^(s+1) − 1)(ℓ' + 1 + Δ⁺)`. It is exponential in `s`, needs no coprimality, and charges only `Δ⁺ ≤ Var/2`.
  - They are complementary. When `ℓ'` is small next to `Var`, the rise lemma is the stronger one exactly when `κ^(s+1) − 1 < 2(K − 1)`. S12 has no `ℓ'` term, so it is the stronger one when `Var` is small next to `ℓ'`.
- **`h = 1`.** Here the lemma says each block of equal letters can at most multiply `log₂ n` by `log₂3`, which is close to the classical circuit inequality. For the statistic "number of circuits", Hercher's `≥ 92` is far stronger at the imported periods. The gain here is uniformity in `h`.

## 5. Candidate units for the Lean lane

- **S13-a, the rise lemma for `OddCycle`.**
  - (W) as a start witness, derived from the existing run identity (`z_run`, `witness_gt`).
  - (P), and the induction over the runs of the stretch.
  - Statement: `y_v + c ≤ κ^(k+1)(y_u + c)`, in natural logs if more convenient.
- **S13-b, Corollary 1 and the `Δ⁺ ≤ (σ + η)d` bound.** Then the combination with C013-b/S5, which is the table's inequality chain at symbolic `m`.

## Reproduce

```sh
python3 sidekick/probes/s13_rise_lemma.py        # ~100 s, all checks above
python3 sidekick/probes/s13_short_rotations.py   # ~1 s, the q = 1 tables
```
