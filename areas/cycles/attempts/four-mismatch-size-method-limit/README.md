# S8: the size method stops at three mismatches (a map) — HEADLINE WITHDRAWN

> **Withdrawn 2026-10-19 13:44.** The exhibited words fail the witness inequalities of the rotation by `2h` (6 mismatches), by about `2·10^5` bits at `m = 10^6`. Only the narrow statement survives: the single-rotation relaxation is feasible. Whether all size constraints together exclude four mismatches is open (S10). The text below is kept as written.

**Status:** side-lane producer batch S8 (2026-10-19). A negative map backed by explicit words. It excludes nothing. It records exactly where S7's mechanism is exhausted, as the brief asks ("stop expanding an elimination method when its exact obstruction is known").

**Precise claim.** Write (1)–(5) for the inequalities below, with every state replaced by the envelope `y_k`, the maximal admissible profile.
- That relaxed system is jointly satisfiable by explicit four-mismatch words above S7's threshold, for every `ℓ` from 71 to `ℓ*`. So no argument that uses (1)–(5) only through these size inequalities can exclude `s = 4`.
- This is a feasibility statement about the relaxation, in the same sense as C012's "precise failure of this elimination". An argument that also uses the integrality of the witness integers, the exact cycle equation `n_0 D = C_w`, or the mod-`D` relation is outside its scope (§4).
- **Which S7 step fails.** The fourth mismatch frees the third run's witness, which S7's Step 5 pinned a full run below the maximum.
- (Scope sharpened after the Lean lane's review.)

## 1. What S7 uses, and one new constraint

S7 excludes `s = 3` using only inequalities between sizes, along the maximal admissible profile `y_k = ℓ + Σ_(i<k)(log₂ 3 − a_i + ε)`:

1. **End witnesses:** `1 + t log₂ 3 < y_z`, where `z = e` or `e + h` according to the sign of `δ` on the run.
2. **Start witnesses:** `E + 1 < y_(z′)`, at the run's first position (2-adic). They are equivalent to (1) on each run but are stated separately.
3. **The ceiling with tracked excess**, which is built into `y`.
4. **The sign structure** of `δ` (S7-a, S7-b part 2).

S8 adds one constraint of the same kind, a comparison with the integer fixed point `−1` (word `1^∞`).
- On a run of `r` ones, `n + 1` is multiplied by `3/2` at each step, so `3^r | n_e + 1` at the run's end `e`.
- So **a run of `r` ones ending at `e` forces `n_e + q ≥ 2·3^r`, i.e. `1 + r log₂ 3 ≤ log₂(n_e + q)`.** *[Corrected 2026-10-19, after the Lean lane's review: the first version had the strict `<`. Equality occurs, e.g. at the step `3 → 5` at `q = 1`, where `5 + 1 = 2·3`. The formal statement is `ones_run_le` (S8-a), in the `≤` form. The probes test the strict form, which is only more demanding, so their survivor margins remain valid.]*
- A run of ones starting at height `y` gains `0.585` per step, so it can last at most about `y − 1` steps (`1 + 1.585r < y + 0.585r`). In particular, the run starting at the minimum has length below `ℓ − 1`, and letters `≥ 2` must recur at gaps of order `ℓ` early in the climb. *[Corrected 13:13: the first version said "about `0.63ℓ`", which ignored the run's own gain. The probe evaluates the exact inequality, so the tables are unaffected.]*
- Consistency: reducing `C(w)` mod `D` for this family gives the same constraint. For the first 2, at position `p₀` after the minimum, the reduced representative is below `D` when `p₀ ≳ ℓ`. So "reduce mod `D` to a small number" adds nothing beyond the comparison with `−1` here.
- The same device works with any integer cycle as the comparison orbit: `{1}`, `{−1}`, `{−5, −7}` and the `−17` cycle.

## 2. Explicit four-mismatch words meet every constraint

The words are built along one `h`-chain (`gcd(h, m) = 1`) with arcs `[V][1^a][2^b][1^c]`.
- There is one huge letter `V` at `x = m − 1`, and the 2s fill the chain interval `a + 1, …, a + b`. `V` is fixed by `A = ⌈m log₂ 3⌉`.
- The rotation by `h` has exactly four mismatches: `x − h`, `x`, `x + a·h` and `x + (a+b)·h`.
- The parameters are chosen as follows:
  - `h/m ≈ √2 − 1`, which has bounded partial quotients, so the 2s spread evenly (three-gap theorem). Rational-like `h/m` clusters them and breaks constraint (5).
  - `b ≈ 1.6m/ℓ`, so runs of ones near the minimum are short enough.
  - The inner mismatches are placed in the windows where the continuous witness LP is feasible.

**The continuous LP.** Scale positions by `m`, with the minimum at 0, the huge letter at `x ≈ 1`, and slope `σ = log₂(3/2) − (2-density)`. Put `r = σ/log₂ 3` and `ℓ/m → 0`.
- The signs are `δ < 0` on `(x − h, x]` and `δ > 0` on `(x, x − h]`.
- The two inner mismatches are `p₁ ∈ (1 − h, 1)` (witness `p₁`) and `p₂ ∈ (0, h)` (witness `p₂ + h`). The four runs and their end-witness constraints `t ≤ r·pos(z)` are:
  - `(x, p₂)`: `p₂ ≤ r(p₂ + h)`
  - `(p₂, x − h)`: `1 − h − p₂ ≤ r`
  - `(x − h, p₁)`: `p₁ − (1 − h) ≤ r·p₁`
  - `(p₁, x)`: `1 − p₁ ≤ r`
- **Feasibility.** These hold together iff `p₂ ∈ [1 − h − r, rh/(1−r)]` and `p₁ ∈ [1 − r, (1 − h)/(1 − r)]`. Both intervals are nonempty iff `h ∈ [(1−r)², 1 − (1−r)²]`, which is `[0.398, 0.602]` at `r = 0.369`.
- **The other constraints.** The start witnesses (2) and runs of ones (5) are then checked exactly on the integer word.

Every constraint (1)–(5) is evaluated exactly on the word, and the margin is the smallest slack in bits (`s8_four_mismatch_map.py`):

| `m` | `ℓ` | `b` | margin (bits) | binding constraint |
|---|---|---|---|---|
| 1,000,003 | `ℓ*` = 6,987 | 228 | +2,028 | (5) runs of ones |
| 4,000,037 | `ℓ*` = 7,671 | 834 | +3,872 | (5) |
| 1,000,003 | 3,000 | 542 | +1,226 | (5) |
| 1,000,003 | 1,000 | 1,604 | +354 | (5) |
| 1,000,003 | 200 | 8,004 | +111 | (5) |
| 1,000,003 | 71 | 22,540 | −3,184 | (1) end witnesses (`h/m ≈ 0.4142`, just outside the window) |
| 1,000,003 | 71 | 35,235 | +33 | (5), with `h/m ≈ 0.4393 = [0; 2, 3, 1, 1, …]` |
| 1,000,003 | 100 | 16,011 | +55 | (5), same `h` |

- **Both test periods are above S7's threshold** (`m0 = 452,695`).
- **At `ℓ = ℓ*`**, the worst case allowed by `gap_all`, every constraint holds with thousands of bits to spare. So **no argument built only from (1)–(5) can exclude `s = 4`.**
- **Survival holds for every `ℓ` tested, from 71 to `ℓ*`.** The rotation fraction must sit inside the LP window `[(1−r)², 1 − (1−r)²]`, where `r` drops as the 2-density `≈ 1.6/ℓ` grows, and must have bounded partial quotients. `[0; 2, 3, 1, 1, …] ≈ 0.4393` works at `ℓ = 71`.
- **The first `ℓ = 71` failure** below belonged to `h/m ≈ √2 − 1`, which lies just outside that window at `ℓ = 71`.
- **Earlier wording (superseded):** the survival extends down to `ℓ = 200`. That is the scale a published irrationality measure for `log₂ 3` would give (Rhin-type, `ℓ ≲ 4.1 log₂ m + O(1)`; not formal).
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
python3 reviews/side_lane/s8_four_mismatch_map.py   # ~10 s
```
