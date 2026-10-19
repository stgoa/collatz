# S8: the size method stops at three mismatches (a map)

**Status:** side-lane producer batch S8 (2026-10-19). A negative map backed by explicit words. It excludes nothing. It records exactly where S7's mechanism is exhausted, as the brief asks ("stop expanding an elimination method when its exact obstruction is known").

## 1. What S7 uses, and one new constraint

S7 excludes `s = 3` using only inequalities between sizes, along the maximal admissible profile `y_k = ℓ + Σ_(i<k)(log₂ 3 − a_i + ε)`:

1. **End witnesses:** `1 + t log₂ 3 < y_z`, where `z = e` or `e + h` according to the sign of `δ` on the run.
2. **Start witnesses:** `E + 1 < y_(z′)`, at the run's first position (2-adic). They are equivalent to (1) on each run but are stated separately.
3. **The ceiling with tracked excess**, which is built into `y`.
4. **The sign structure** of `δ` (S7-a, S7-b part 2).

S8 adds one constraint of the same kind, a comparison with the integer fixed point `−1` (word `1^∞`).
- On a run of `r` ones, `n + 1` is multiplied by `3/2` at each step, so `3^r | n_e + 1` at the run's end `e`.
- So **a run of `r` ones ending at `e` forces `1 + r log₂ 3 < y_e`.**
- Near the minimum (`y ≈ ℓ`) this caps runs of ones at about `0.63ℓ`. Letters `≥ 2` must therefore be dense right after the minimum.
- The same device works with any integer cycle as the comparison orbit: `{1}`, `{−1}`, `{−5, −7}` and the `−17` cycle.

## 2. Explicit four-mismatch words meet every constraint

The words are built along one `h`-chain (`gcd(h, m) = 1`) with arcs `[V][1^a][2^b][1^c]`.
- There is one huge letter `V` at `x = m − 1`, and the 2s fill the chain interval `a + 1, …, a + b`. `V` is fixed by `A = ⌈m log₂ 3⌉`.
- The rotation by `h` has exactly four mismatches: `x − h`, `x`, `x + a·h` and `x + (a+b)·h`.
- The parameters are chosen as follows:
  - `h/m ≈ √2 − 1`, which has bounded partial quotients, so the 2s spread evenly (three-gap theorem). Rational-like `h/m` clusters them and breaks constraint (5).
  - `b ≈ 1.6m/ℓ`, so runs of ones near the minimum are short enough.
  - The inner mismatches are placed in the windows where the continuous witness LP is feasible: `p₁ ∈ (1 − h, 1)`, `p₂ ∈ (0, h)` (scaled positions), which requires `h/m ∈ [(1−r)², 1 − (1−r)²]` with `r = slope/log₂ 3 ≈ 0.369`.

Every constraint (1)–(5) is evaluated exactly on the word, and the margin is the smallest slack in bits (`s8_four_mismatch_map.py`):

| `m` | `ℓ` | `b` | margin (bits) | binding constraint |
|---|---|---|---|---|
| 1,000,003 | `ℓ*` = 6,987 | 228 | +2,028 | (5) runs of ones |
| 4,000,037 | `ℓ*` = 7,671 | 834 | +3,872 | (5) |
| 1,000,003 | 3,000 | 542 | +1,226 | (5) |
| 1,000,003 | 1,000 | 1,604 | +354 | (5) |
| 1,000,003 | 200 | 8,004 | +111 | (5) |
| 1,000,003 | 71 | 22,540 | −3,184 | (1) end witnesses |

- **Both test periods are above S7's threshold** (`m0 = 452,695`).
- **At `ℓ = ℓ*`**, the worst case allowed by `gap_all`, every constraint holds with thousands of bits to spare. So **no argument built only from (1)–(5) can exclude `s = 4`.**
- **The survival extends down to `ℓ = 200`.** That is the scale a published irrationality measure for `log₂ 3` would give (Rhin-type, `ℓ ≲ 4.1 log₂ m + O(1)`; not formal).
  - At `ℓ = 71` this single-chain family fails in the search. The 2-density `1.6/ℓ` lowers the slope enough to push `h/m ≈ 0.4142` out of the feasible window.
  - That is a statement about one family and one choice of `h`, not an exclusion.

## 3. What the obstruction looks like

The survivors match S7's structure with one more degree of freedom:
- a tall sawtooth (`log₂ H ≥ 0.396m`) with a single drop `V ≈ 0.58m`;
- a sparse, evenly spread set of 2s;
- two sign changes at `x − h` and `x`, as in S7;
- two further mismatches that carry no sign change. The fourth mismatch frees the third run's witness, which in S7 was pinned a full run below the maximum.

In S7's language, each of the long runs now has a witness high enough on the climb.

## 4. Consequences for the programme

- **`ρ ≥ 4` is the limit of size arguments.** Main's milestone `F(m) → ∞` needs input beyond sizes. The candidates are:
  - arithmetic on the mismatch transition `2^β δ_(e+1) = 3δ_e + (2^α − 2^β) n_(e+1)` (with `α = a_e`, `β = a_(e+h)`), which is the only place new information enters at a mismatch;
  - the mod-`D` relation `Σ_k (2^(W_k) − 2^(W_(k+1)))·3^(m−e_k−1) 2^(A_(e_k+1)) n_(e_k+1) ≡ 0 (mod D)` over the mismatches, the Abel-summed form of C012's coupled system;
  - a much stronger upper bound on `L`, which would help only if it reached `ℓ ≈ 71`.
- **By-product:** a short proof that 1-cycles (`1^(m−1)V`) do not exist for large `m`. Reducing mod `D` gives `D | 3^m − 2^m ≡ 2^m(2^(A−m) − 1)`, so `D ≤ 2^(A−m)`, which contradicts `gap_all` (`D ≥ 2^A/(2^172 m^341)`) once `2^m > 2^172 m^341`.
  - This is Steiner's theorem (1977) by a different route, labelled as known.
  - The same "reduce mod `D` to a small nonzero number" device is the natural tool to try next on the S8 survivors.

## Reproduce

```sh
python3 sidekick/probes/s8_four_mismatch_map.py   # ~10 s
```
