# S12: a Denjoy–Koksma height bound along a rotation chain

**Status:** side-lane producer batch S12 (2026-10-19). A rigorous inequality: classical Denjoy–Koksma and Ostrowski, applied to the cycle profile, plus exhaustive data. Its consequence for the mismatch problem is **conditional**. Novelty undetermined: the tools are classical, and this lane has not seen them applied to Collatz cycle profiles.

## 1. The identity

Take any primitive positive cycle (odd `q`, letters `≥ 1`) with log-profile `y_p = log₂ n_p` (indices mod `m`), and a rotation `h` with `gcd(h, m) = 1`. Put

```
μ_h(p) = y_(p+h) − y_p.
```

- `μ_h` has mean exactly 0 over `Z/m`, since `Σ_p μ_h(p) = 0`.
- Along the chain `x, x + h, x + 2h, …`, which visits every position because `gcd(h, m) = 1`, the profile is a **Birkhoff sum** of the rotation by `h`:

  ```
  y(x + Nh) − y(x) = Σ_(k<N) μ_h(x + kh).
  ```

## 2. The bounds

- **(1) Denjoy–Koksma.** Let `p/q` be a convergent of `h/m` with `q < m`, so `|qh − pm| < m/q`. For every start `x`,

  ```
  |Σ_(k<q) μ_h(x + kh)| ≤ Var(μ_h),
  ```

  where `Var` is the cyclic total variation on `Z/m`. The classical proof applies verbatim: the `q` points `x + kh` fall one in each of `q` consecutive arcs, and each term deviates from its arc's average by at most that arc's variation.
- **(2) Ostrowski.** Every `N < m` is `Σ b_i q_i` with `0 ≤ b_i ≤ a_(i+1)`. With (1) and mean 0, the log-height `B = max y − min y` satisfies

  ```
  B ≤ Var(μ_h) · K(h/m),       K(h/m) = Σ_i a_i   (the partial quotients of h/m).
  ```

- **Review note (the Lean lane, 2026-10-19).** (1) holds exactly in the discrete setting, under `gcd(p, q) = 1`, `1 ≤ q < m` and the strict `|qh − pm| < m/q`. Every proper convergent satisfies it. In (2), the Ostrowski digits satisfy `b_0 ≤ a_1 − 1`, so `Σ b_i ≤ K − 1` and the bound sharpens slightly to `Var·(K − 1)`.
- **(3) Variation from the letters.**

  ```
  μ_h(p+1) − μ_h(p) = (a_p − a_(p+h)) + (ε_(p+h) − ε_p),     with ε_p = log₂(1 + q/(3n_p)).
  ```

  Hence

  ```
  Var(μ_h) ≤ V_h + 2δ,     V_h = Σ_(e ∈ mis h) |a_e − a_(e+h)|,     δ = Σ_p ε_p = A − m log₂ 3.
  ```

  Only the mismatches of `h` contribute, apart from the drift. At `q = 1`, `δ ≤ m/(3L ln 2)`, which is below `3·10^(−11)` at `m = 1.375·10^11` with `L > 2^71`.

**Data** (`s12_denjoy_koksma.py`, about 23 s). The test set is every actual `3x+q` cycle with odd `q < 2,000` and every rotation coprime to `m`.

| check | instances | violations | largest ratio |
|---|---|---|---|
| (1), every convergent denominator and start | 12,229,083 | 0 | `|S_q|/Var` = 0.42 |
| (2) | 52,484 pairs | 0 | `B/(Var·K)` = 0.12 |
| (3) | 52,484 pairs | 0 | — |

## 3. Consequence with S5 (conditional)

At `q = 1`, S5 gives `s(h) > log₂3 · m/(B + 342 log₂ m + 173)`. Combine it with (2) and (3), writing `a_M(h) = max_(e ∈ mis h) |a_e − a_(e+h)|` so that `V_h ≤ s·a_M`:

```
s(h) · (s(h) · a_M(h) · K(h/m) + 342 log₂ m + 173) > log₂3 · m,    i.e.  s(h) ≳ √(log₂3 · m/(a_M K)).
```

The smallest `s` allowed, computed exactly:

| `m` | `a_M = 1, K = 10` | `a_M = 2, K = 50` | `a_M = 3, K = 200` | `a_M = 10, K = 1000` |
|---|---|---|---|---|
| `10^7` | 917 | 360 | 156 | 40 |
| `1.375·10^11` | 146,986 | 46,620 | 19,048 | 4,668 |

**Reading.** A rotation with few mismatches forces at least one of two things:
- **(a)** a large letter difference at some mismatch. That is the tall-sawtooth structure of S7, where the huge drop sits at the aligned pair and `V_h ≈ 2V ≈ 2B`.
- **(b)** `h/m` close to a rational with a small denominator, i.e. large `K`.

Otherwise the height is small and S5 forces many mismatches.

## 3a. The denominator form (any mismatch count)

Chain the longest run `t ≥ ⌈(m−s)/s⌉`, the witness `2·3^t < H = L·2^B`, the bound (2)+(3), and `L ≤ m q 2^A/(3D)`. For every primitive word and every rotation `h` coprime to `m` with `s` mismatches:

```
log₂ den(w) > 1 + ⌈(m−s)/s⌉ log₂3 − (V_h + 2δ)·K(h/m) − λ(w),      λ(w) = log₂(m 2^A/(3D)).
```

Unlike S9, which uses the height ceiling and is limited to `s ≤ 3`, this holds for every `s`. It is informative when `V_h·K(h/m)` is small.

Two labels from the Lean lane's review:
- **(a)** `B` here is the real log-height `log₂(n_max/L)`, which is what the `1 +` presupposes. With the integer band of the `OddCycle` structure (`n < 2^(B+1) L`), the 1 cancels.
- **(b)** The law is **complementary to S9, not a replacement**.
  - For S7-type sawtooth words, `V_h` is about the height and this law says nothing; S9 covers `s ≤ 3` there.
  - Conversely, S9 says nothing for `s ≥ 4`, where this law covers low-variation words.

`s12_dk_denominator_law.py` finds no violation in 360,284 exhaustive pairs (words over `{1,2,3}`, `m ≤ 12`), in 52,484 actual-cycle pairs, or in 40 low-variation chain words (18 non-vacuous, slack ≥ 547 bits).

## 4. What it does not give

- **No unconditional height bound.** When a big letter sits at a mismatch, `Var(μ_h)` is about the height itself, and (2) is trivial. This is consistent with tall cycles.
- **Why a tall sawtooth survives (2).** The big drop at `x` makes `μ_h` jump on the arc `(x − h, x]`, an interval of length exactly `h`. That is a bounded-remainder set for the rotation by `h`, so its contribution to the Birkhoff sums is `O(jump)`, not `O(jump · K)`.
  - A sharper version of (2) would split `μ_h` into bounded-remainder bumps (cost `O(jump)`) and the rest (cost `Var · K`). This lane has not developed it.
- **`gcd(h, m) = g > 1`.** The chain covers one residue class. The bound applies within classes (rotation by `h/g` on `Z/(m/g)`), but the offsets between classes add a term of up to about `0.585g` plus the excess of a `g`-window. For large `g` this is weak.

## 5. A first formalizable statement

The Denjoy–Koksma step (1) at a single convergent denominator is a candidate unit for the Lean lane: `|y(x + qh) − y(x)| ≤ Var(μ_h)`. It needs the convergent property `|qh − pm| < m/q`, a one-point-per-arc lemma, and a variation sum. (3) is a one-line telescoping.

## Reproduce

```sh
python3 sidekick/probes/s12_denjoy_koksma.py        # ~23 s
python3 sidekick/probes/s12_dk_denominator_law.py   # ~6 s, the denominator form (§3a)
```
