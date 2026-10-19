# S9: S6 and S7 as denominator laws for the whole `3x+q` family

**Status:** side-lane producer batch S9 (2026-10-19). A written extension of S6/S7 with a probe. It changes one ingredient, the ceiling, and reuses every other step unchanged. Novelty undetermined. The statements are in the programme's own language: reduced denominators `den(w) = D/gcd(C_w, D)`.

## 1. The global-drift ceiling

Take any primitive word `w` (period `m`, total `A`, `D = 2^A − 3^m > 0`) and its reduced integer cycle.
- The parameter is `q = den(w)`, and the states `n_i = C(w_i)/gcd(C_w, D)` are odd. The arrows are `2^(a_i) n_(i+1) = 3n_i + q`, with every `a_i ≥ 1`.
- The closing identity says the per-step errors sum exactly:

  ```
  Σ_(i<m) log₂(1 + q/(3n_i)) = log₂(2^A/3^m) =: δ(w) = A − m log₂ 3.
  ```

- Hence, for every index `k` counted forward from the minimum `L`:

  ```
  log₂(n_k / L) ≤ k·log₂(3/2) − X_k + δ(w),          X_k = Σ_(i<k)(a_i − 1).
  ```

  This needs no hypothesis on `L/q`. S6-a/S7 used the per-step form `k·log₂(1 + q/(3L))`, which is small only when `L ≫ mq`.
- Unchanged from S7 (F4): `L ≤ m q 2^A/(3D)`.

The run law, the witnesses, the sign lemma, the window and alignment steps, and the witness index all hold verbatim at any odd `q`, since `q` cancels in `δ_i = n_(i+h) − n_i`. In S7's conditions, `κ` becomes `log₂(3/2)`, and `ℓ` becomes `Λ = log₂ L + δ(w)`.

## 2. The laws

Write `λ(w) = log₂(m 2^A/(3D))`. Every primitive positive word `w` satisfies the following.

- **(i) Two mismatches.** If some rotation differs from `w` in exactly two positions, then

  ```
  log₂ den(w) > Φ₂(m) − δ(w) − λ(w),     Φ₂(m) = 1 + ⌈(m−2)/2⌉ log₂ 3 − (m−1) log₂(3/2) ≈ 0.2075 m.
  ```

  *Proof (S6's chain).* The longest run has `t ≥ ⌈(m−2)/2⌉`. Then `1 + t log₂ 3 < log₂ H ≤ log₂ L + (m−1) log₂(3/2) + δ(w)`, and `log₂ L ≤ log₂ q + λ(w)`.

- **(ii) Three mismatches.** If some rotation differs from `w` in exactly three positions, then

  ```
  log₂ den(w) > Λ₃(m) − δ(w) − λ(w),     Λ₃(m) = sup{Λ : S7's W, A, P, F hold at ℓ = Λ, ε = 0}.
  ```

  *Proof.* This is S7, contrapositively. If `Λ = log₂ L + δ(w) ≤ Λ₃(m)`, then Steps 1–6 run and exclude the rotation.
  Values: `Λ₃ = 1.8, 4.7, 15.7, 44, 147, 1,458` at `m = 10², 3·10², 10³, 3·10³, 10⁴, 10⁵`, so asymptotically `Λ₃ ≈ 0.0146 m`. Condition W binds.

- **(iii) With `gap_all`.** We have `λ(w) ≤ log₂(m/3) + 172 + 341 log₂ m`. So for near-critical words (`δ(w) < 1`, which includes every word of a cycle with `L ≫ mq`), `den(w) ≥ 2^(Φ_s(m) − 174 − 342 log₂ m)` for `s = 2, 3`.
  - At `q = 1` this returns S6 and S7.
  - At fixed `q` it bounds the period of every near-critical two- or three-mismatch word explicitly.

## 3. What it adds, and the caveat

- **Height is eliminated for `s ≤ 3`.** Main's C013 inequality (6) holds at every `q` but keeps the height `B`; its §5 says the height shortcut "does not eliminate B". The global-drift ceiling eliminates `B` at a cost of `0.585m`.
  - That is affordable for `s = 2` (`0.792 > 0.585`).
  - With S7's refinement, it is also affordable for `s = 3`.
  - S8 shows it is not affordable at `s = 4`, so this is the exact reach of the method.
- **Relation to C011.** C011 proves bounded-denominator finiteness for the two-defect class. (i) is an explicit exponential version, under the drift caveat.
- **The three-mismatch class.** (ii) is, as far as this lane knows, the programme's first denominator law for it. It is consistent with main's C013 §3 distance-three family, which has `ρ = 3` and large denominators.
- **Caveat: the laws describe the regime `L ≫ q`. The caveat is intrinsic (the Lean lane's review).**
  - **The general ceiling** is `log₂(n_k/L) ≤ k log₂(3/2) − X_k + min(δ(w), k·log₂(1 + q/(3L)))`.
  - **The second branch** removes the caveat whenever `log₂(1 + q/(3L)) < 1 − log₂3/2 ≈ 0.2075`, i.e. `L > 2.2q`. The `s = 2` constant then degrades to `0.2075 − log₂(1 + q/(3L))`.
  - **Words with `L ≲ q`** (heavy words, cycles living at scale `q`) can have linear drift. Narrow words with all states in `[L, 2L)` already have drift `≥ m log₂(1 + q/(6L))`. No cheap partial-drift bound is available.
  - **Actual small cycles** all live in that regime. So the laws are statements about the `L ≫ q` regime by nature; `q = 1` cycles, with `L > 2^71`, are deep inside it.

## 4. Checks (`s9_denominator_law.py`, ~30 s)

| test set | rotations with `s = 2` | rotations with `s = 3` | non-vacuous cases | violations |
|---|---|---|---|---|
| every primitive word over `{1,2,3}`, `m ≤ 12` | 1,498 | 1,274 | 0 | 0 |
| random 2- and 3-arc chain words, `m ≤ 1,600` | 163 | 192 | 16 | 0 |
| near-critical chain words (`A = ⌈m log₂ 3⌉`), `m ≤ 3,200` | 50 | 50 | 50 + 20 | 0 |
| C013 §3 family, `(a,b)` up to `(1539, 971)`, `m ≤ 2,913` | — | 5 | 1 (`m = 2,913`) | 0 |
| words of actual `3x+q` cycles, odd `q < 2,000` | 451 | 392 | 0 | 0 |

- **Slack.** Generic words have `den(w) ≈ D`, so the slack is large; it is 281 bits or more in every non-vacuous case.
- **Tightness cannot be tested.** The laws could only be tight for hypothetical small-denominator words, which the data cannot produce. So the table is a consistency check, not evidence of strength.
- **A note on main's family.** Reconciled with the Lean lane: there is no conflict.
  - C013 §5's `≈ 0.447m` is a lower bound (`liminf (log q)/b`), derived from the same inequality as (I1).
  - This probe measures the actual denominators: `den ≈ D`, `log₂ den/m ≈ 1.53–1.58`.
  - So the lower bounds agree with each other, and the actual value lies far above both. Earlier S5/S7 wording called the bound sharp on the family; that is now corrected.

## 5. Remark: the repeat form (`s10_repeat_complexity.py`)

- **The repeat law.** Two occurrences of the same factor of length `t` at cyclic offset `h` form an agreeing run of the rotation by `h`. So the run law gives `max(n_e, n_(e+h)) > 2·3^t`, and with the global-drift ceiling, `t < T = (Λ + (m−1) log₂(3/2) − 1)/log₂ 3`.
- **Complexity.** In complexity terms `p_w(n) = m` for every `n ≥ T`, so **no factor of length `T` repeats**. At `q = 1`, `T ≈ 0.369m + O(log m)`.
- **Excluded word classes.** Any word with `p(T) < m` is excluded for large `m`. That covers Sturmian/Christoffel words (Knight's theorem, for large `m`), 2-interval rotation codings (`p(n) ≤ 2n`), and 3-interval-exchange codings (`p(n) = 2n + 1`).
- **What counting cannot reach.** Codings of a rotation by `k ≥ 3` intervals have only `p(n) ≤ kn`, so counting alone does not exclude them. Three-mismatch chain words are such codings and need S7.
- **Data.**
  - On all 3,918 actual `3x+q` cycles with `q < 2,000`, the longest repeat obeys `2·3^t < H`.
  - The ratio `(1 + t log₂ 3)/log₂ H` reaches 0.97 (`q = 1,723`, `m = 219`, `t = 10`). So the witness bound is nearly sharp on actual cycles.
  - Random rotation codings repeat far beyond `T` (generic rotation numbers have good rational approximations). Only badly approximable rotation numbers, like those of S8's survivors, keep the longest repeat short.
- **Novelty.** This is S5's uniform run bound read as a statement about repeats. What is new is the packaging, not the inequality.

## Reproduce

```sh
python3 sidekick/probes/s9_denominator_law.py   # ~30 s
python3 sidekick/probes/s10_repeat_complexity.py   # ~7 s, the repeat form (§5)
```
