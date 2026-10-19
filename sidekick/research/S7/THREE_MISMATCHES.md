# S7: no rotation with exactly three mismatches at `q = 1`

**Status:** side-lane producer batch S7 (2026-10-19). A written proof from elementary steps, plus the replayed `gap_all` and two imports (Barina's minimum, a period bound). There is a probe for the threshold and controls on actual `3x+q` cycles. The Lean lane reviewed it adversarially and found no gap (§5a). The sign lemma is formal (S7-a). Novelty undetermined.

## 1. Statement

Take a nontrivial primitive Collatz cycle (`q = 1`) with period `m ≥ 452,695` and minimum `L > 2^71`. Then **no nonidentity rotation of its valuation word differs from it in exactly three positions**.

- Every nonidentity rotation differs in at least one position, by primitivity. It never differs in exactly one, because the totals agree: `Σ a_i = Σ a_(i+h)`. (The Lean lane is formalising this as `mis_card_ne_one`.)
- C011 (main), or S6 (formal as S6-b/c for `m ≥ 2^15`), excludes exactly two.
- So with any period import above 452,695, for example Eliahou's bound (total cycle length `A ≥ 17,087,915`, so `m ≳ 1.08·10^7` odd steps) or the Hercher/Barina bound used in C011, **every nonidentity rotation of a hypothetical nontrivial Collatz cycle differs in at least four positions**. In main's notation that is `ρ(w) ≥ 4`; C011 gave `ρ(w) ≥ 3`.

## 2. Setting and four standing facts

- **The cycle.** Odd states `n_i` (indices mod `m`), all distinct. The arrows are `2^(a_i) n_(i+1) = 3n_i + 1` with every `a_i ≥ 1`, and `A = Σ a_i`, `D = 2^A − 3^m > 0`. Index 0 is the minimum `L`, `j` is the position of the maximum `H`, and `ℓ = log₂ L`. (This `ℓ` is the logarithm of the minimum. It is not the additive constant in S5's trade-off.)
- **The rotation.** For a rotation `h ≢ 0`, put `δ_i = n_(i+h) − n_i`. It is nonzero (distinct states) and even.
  - The mismatch set is `M = {i : a_i ≠ a_(i+h)}`, with `|M| = s`.
  - The mismatches cut the circle into `s` agreeing runs, of lengths `t_k ≥ 0` with `Σ t_k = m − s`.

**(F1) The run law with witnesses** (main's `OVERLAP_THEORY` §1; Lean `q_bound_rational` family).
- At an agreeing position `i`, `2^(a_i) δ_(i+1) = 3δ_i`.
- So along a run of length `t` that ends at the mismatch `e`, `2^E δ_e = 3^t δ_(start)`. Hence `3^t | δ_e`, and since `δ_e` is even, `|δ_e| ≥ 2·3^t`.
- The **witness** of that run is the larger of the two states compared: `z = e + h` if `δ_e > 0`, and `z = e` if `δ_e < 0`. It satisfies `n_z > 2·3^t`.

**(F2) Sign persistence.** By (F1), `δ` keeps its sign at every agreeing position. It can change sign only at mismatches. Going once round the cycle, there are as many `+ → −` changes as `− → +` changes.

**(F3) The ceiling from the minimum** (Lean S6-a, `n_le_climb`). Put `κ = log₂(3/2) + ε` with `ε = log₂(1 + 1/(3L))`.
- For every index `0 ≤ k ≤ m − 1`, counting letters forward from the minimum: `log₂ n_k ≤ ℓ + k·κ`. This holds at every index, in the climb or not, because every letter is at least 1.
- Tracking the letters, `log₂(n_k / L) ≤ kκ − Σ_(i<k)(a_i − 1)`.

**(F4) The size of the minimum.**
- `Σ log(1 + 1/(3n_i)) = log(2^A/3^m) ≥ D/2^A`, and the left side is at most `m/(3L)`. So `L ≤ m 2^A/(3D)`.
- With `gap_all` (`2^A ≤ 2^172 m^341 D`; replayed as EXT-1), `ℓ ≤ ℓ*(m) = 172 + 342 log₂ m − log₂ 3`. The formal pieces are the Lean lane's `L_mul_delta_le` and `delta_ge_gap`, plus the gap.

## 3. Proof (`s = 3`)

**Step 1 (sizes).**
- Each witness has `n_z ≤ H ≤ L·2^((m−1)κ)`. So every run satisfies `t ≤ t_max`, the largest integer below `T = (ℓ + (m−1)κ − 1)/log₂ 3 ≈ 0.369m + 0.631ℓ`. This `t_max` is a uniform bound on every run, not the length of the longest one.
- The three runs sum to `m − 3`, so every run has length at least `m − 3 − 2t_max ≈ 0.262m − 1.26ℓ`. Write `σ_min = m − 2(t_max + 1)` for the resulting lower bound on the **spacing** (run length plus one) between consecutive mismatches. "Spacing" is used to avoid the programme's `gap`, which means `Δ_r`.
- The longest run has length at least `t* = ⌈(m−3)/3⌉`, so `log₂ H > 1 + t* log₂ 3`. `X*` and `d*` below use this worst case, the smallest possible longest run, which makes them as large as possible. Combined with (F3) up to `j`:
  - the **climb excess** `X_c = Σ_(i<j)(a_i − 1)` satisfies `X_c < X* = (m−1)κ − 1 − t* log₂ 3 + ℓ ≈ 0.057m + ℓ`. The climb bound used is `log₂(H/L) ≤ jκ − X_c`, the exact form of S6-a's `h_le_climb`.
  - the **descent window** `W = [j, m)` has length `d = m − j < d* = m − (1 + t* log₂ 3 − ℓ)/κ ≈ 0.097m + 1.71ℓ`. Keeping `X_c` gives the sharper `d < d* − X_c/κ`, which is not needed.

**Step 2 (two sign changes, located).**
- `δ_(j−h) = H − n_(j−h) > 0` and `δ_(m−h) = L − n_(m−h) < 0`. So some mismatch `e_a ∈ W − h = [j−h, m−h)` is a `+ → −` change.
- `δ_j = n_(j+h) − H < 0` and `δ_m = n_h − L > 0`. So some mismatch `e_b ∈ W` is a `− → +` change.
- By (F2) the number of changes is even and at most three, so it is exactly two. The third mismatch `e_c` is not a change.
- So `δ < 0` on the forward stretch `(e_a, e_b]` and `δ > 0` on `(e_b, e_a]`.

**Step 3 (the windows are disjoint).** Take the representative `1 ≤ h ≤ m − 1`. Both window conditions are needed: `d ≤ h ≤ m − d`.
- Suppose `h < d` or `h > m − d`. Then `W` and `W − h` overlap.
  - If `h < d`, the union is `[j − h, m)`, of length `d + h ≤ 2d − 1`.
  - If `h > m − d`, the union wraps: it is `[j, m) ∪ [0, m − h)`, of length `d + (m − h) ≤ 2d − 1`.
  - The union contains `e_a` and `e_b`. They are distinct because their change types differ (`+ → −` against `− → +`). So two mismatches would lie in an arc of at most `2d − 1` positions, while every two mismatches are at least `σ_min` apart. Condition **W**, `σ_min ≥ 2d_max − 1`, rules this out.
- With `h ≥ d`, the copies `W + h = [j + h − m, h)` start at or after index 0. With `h ≤ m − d = j`, they end at or before `j`. So `W + h ⊂ [0, j)`, the climb, and symmetrically `W − h ⊂ [0, j)`.
- Each of `W` and `W − h` contains exactly one mismatch, `e_b` and `e_a` respectively. This uses `σ_min > d_max`, which condition W also covers. It is the second place where `m ≥ m0` enters.

**Step 4 (alignment: `e_a + h = e_b`).**
- Every `i ∈ W` other than `e_b` is agreeing, so `a_i = a_(i+h)` with `i + h` in the climb. Hence `Σ_(W ∖ {e_b}) (a_i − 1) ≤ X_c`.
- Likewise every `i ∈ W` other than `e_a + h` has `a_i = a_(i−h)` with `i − h` in the climb.
- If `e_a + h ≠ e_b`, then `e_b − h ∈ W − h` is not a mismatch, so `a_(e_b) = a_(e_b − h)` is a climb letter and `a_(e_b) − 1 ≤ X_c`. With the first estimate this gives `X_d ≤ 2X_c`, where `X_d = Σ_W (a_i − 1)`. (This is the Lean lane's shorter form. Adding the two estimates gives the same conclusion.)
- Then `A − m = X_c + X_d ≤ 3X_c < 3X*`. Condition **A**, `⌈m log₂ 3⌉ − m ≥ 3X*`, contradicts this. So `x := e_b = e_a + h`.
- A by-product: the excess in `W` sits at `x`, with `a_x − 1 ≥ X_d − X_c > A − m − 2X* ≈ 0.47m`. The whole descent is one huge letter.

**Step 5 (the third witness lies inside the climb).** The mismatches are `x − h`, `x` and `e_c`. There are two cyclic orders.

- **Order 1: `x − h → x → e_c` (forward).**
  - The run `(x, e_c)`, of length `t′`, ends at `e_c`. That position lies in the stretch `(x, x − h]`, where `δ > 0`, so the larger of the two compared states is `n_(e_c + h)`. Its witness is `z = e_c + h`, with `n_z > 2·3^(t′)`.
  - The forward spacings are `t + 1` (from `x − h` to `x`), `t′ + 1` and `t″ + 1`, and they sum to `m`. So `z ≡ x − (t″ + 1)`.
  - As an index, `x ∈ [j, m − 1]`. Condition **P** (`m − d_max ≥ t_max + 1`) gives `x ≥ t″ + 1`. P is in fact implied by Step 3, since `(x, m)` lies inside `W` and holds no mismatch, so `e_c < x − h`. An independent review found that it never binds; it is kept as a check. So `z` is the integer `x − (t″ + 1) ∈ [0, m)`, `n_z = n_(e_c + h)` by the congruence, and `z ≤ m − 2 − t″ = t + t′ + 1`.
  - Since `t″ + 1 > d`, also `z < m − d = j`. So `z` is a climb index, reached forward from the minimum. (F3) would apply at any index anyway.
- **Order 2: `x − h → e_c → x`.**
  - The run `(x − h, e_c)`, of length `t₁`, ends at `e_c`. That position lies in `(x − h, x]`, where `δ < 0`, so the larger state is `n_(e_c)` itself. Its witness is `z = e_c`.
  - As an index, `z = x − (t₂ + 1) ≤ t₁ + t₃ + 1`, where `t₂` is the run `(e_c, x)` and `t₃` the run `(x, x − h)`. Again `z < j`, so there is no wrap.
- **In both orders** one run `τ` has its witness at an index at most `τ + τ° + 1`, where `τ°` is one of the other two runs. By (F1) and (F3), `τ log₂ 3 + 1 < ℓ + (τ + τ° + 1)κ`.
- Since `log₂ 3 − κ = 1 − ε`, this gives `τ (1 − ε) < ℓ + (τ° + 1)κ − 1 ≤ ℓ + (t_max + 1)κ − 1`. So `τ ≲ ℓ + 0.585·t_max`.

**Step 6 (the count).** The special run `τ` is at most `τ_max`, the largest integer below `(ℓ + (t_max + 1)κ − 1)/(1 − ε)`. The other two runs are each at most `t_max`, because `t_max` bounds every run. So `m − 3 = Σ t_k ≤ 2t_max + τ_max ≈ 0.954m + 2.63ℓ`. Condition **F** contradicts this. ∎

**Thresholds.** All four conditions get harder as `ℓ` or `ε` grows. So they are evaluated at `ℓ = ℓ*(m)` (from F4) and `ε` at `L = 2^71`.
- The probe scans every `m` up to `10^7`. The last failure is at `m = 452,694`, where condition W binds.
- Beyond the scan the margins grow linearly. Condition W's margin is about `0.069m − 4.68ℓ*(m)`, which increases for `m > 3.4·10^4`, and the others behave alike.
- Hence `m0 = 452,695`.

## 4. Numbers (`s7_three_mismatch.py`, Part 1)

The conditions are evaluated at the worst case `ℓ = ℓ*(m)`. Each entry is a margin, and positive means the condition holds.

| `m` | W | A | P | F | `t_max` | `d_max` | `σ_min` |
|---|---|---|---|---|---|---|---|
| 452,695 | 4 | 168,101 | 226,349 | 3,457 | 171,236 | 55,109 | 110,221 |
| 10^6 | 35,499 | 394,080 | 517,749 | 27,586 | 373,477 | 108,773 | 253,044 |
| 17,087,915 | 1.13·10^6 | 7.07·10^6 | 9.11·10^6 | 7.6·10^5 | 6.31·10^6 | 1.67·10^6 | 4.46·10^6 |
| 1.14·10^11 (Hercher) | 7.8·10^9 | 4.7·10^10 | 6.1·10^10 | 5.2·10^9 | 4.2·10^10 | 1.1·10^10 | 3.0·10^10 |

## 5. Controls on actual `3x+q` cycles (Part 2)

The sample is the 616 cycles with `m ≥ 3` for odd `q < 400`, `3 ∤ q`, from starts up to 3,001. It includes the controls `q = 5, 7, 13, 61`.

- **The exact, `q`-independent claims hold on every rotation checked:** 287 rotations with exactly two mismatches and 196 with exactly three.
  - The two located sign changes (Step 2) are always present.
  - With three mismatches, there are always exactly two changes.
  - Every run end satisfies `|δ_e| ≥ 2·3^t` and its witness bound.
  - The `q`-version of the ceiling, `n_z ≤ L·Π_(i<pos z)(3/2)(1 + q/(3n_i))`, holds.
- **Alignment holds in 78 of the 196 three-mismatch rotations.** In every aligned case the witness identity of Step 5 (`z = x − (t° + 1)`, with no wrap) holds exactly.
- **What fails at `q > 1` is the size input.**
  - These cycles have `log₂ L / m ≈ 1.5–1.6`, so all four conditions fail by wide margins, and three-mismatch rotations duly exist. One example is `q = 13`, `m = 5`, `L = 287`, `h = 2`, which is aligned (order 1).
  - The same holds for main's C013 §3 distance-three family of rational cycles. *[Corrected 13:29: an earlier version wrote `log₂ q ≈ 0.447m`. That is C013 §5's lower bound; the actual denominators are `den ≈ D`, `log₂ den ≈ 1.55m` (S9).]*
  - The proof uses `q = 1` only through `ℓ = O(log m)` (F4) and `ε ≈ 0`.

## 5a. Review and a consistency check

- **The Lean lane's review** (2026-10-19, of `d978b57`) attacked Steps 3–5 line by line and found no gap.
  - It asked for four points to be made explicit, now done: the wrap case of Step 3; that `X*` and `d*` use the worst case `t*`; that the witness index `z` is an integer in `[0, m)` with `n_z = n_(e_c+h)`; and that `s ≠ 1` comes from the equal totals, not from primitivity.
  - S7-a, the sign lemma, is formal. The other steps are planned as S7-b, S7-c and S7-d.
- **Consistency with known results.** Two short arguments recover the Steiner/Simons exclusions of 1-cycles and 2-cycles for `m ≥ m0`, through rotations alone.
  - **One letter `≥ 2`.** Every rotation of a word with exactly one letter `≥ 2` has two mismatches, so S6 excludes it.
  - **Two letters `V, W ≥ 2`, at `x` and `y`.** The rotation by `r = y − x` can only mismatch at `x`, `y` and `2x − y`. So it has 3 mismatches (`V ≠ W`), 2 (`V = W`), or, when `2r ≡ 0`, 2 or 0.
  - S6, S7 and primitivity exclude every case.
  - This is a check that the theorem has content, not a new result. Words with three or more letters `≥ 2` are not reached this way.
- **An independent review agent also found no gap** (2026-10-19).
  - It recomputed the four conditions in 80-digit decimal arithmetic. W is −1 at 452,694 and 4 at 452,695, so `m0` is exact.
  - It tested every q-independent step (2–5) under its actual hypotheses on all primitive words up to length 14 (rational cycles). `s7_stress_rational.py 3 14` reproduces this here: 5,116 three-mismatch rotations, with no failure. The Step 4 transfer is exercised on 260 unaligned rotations, and Step 5 on 444 aligned ones.
  - Its minor points are applied: `ε` is computed with `log1p`, "longer than" is now "at least", P is noted as redundant, and the Eliahou citation is corrected.
- **The Lean lane's observation (from S7-b part 3b).** Steps 2–4 hold for any mismatch count `s`, given the spacing bound `σ ≥ 2d − 1` and condition A.
  - The count `s = 3` enters only in Step 1, which produces `σ_min` and `X*`.
  - "`σ_min > d_max`" can be weakened to `σ_min ≥ d_max`.
  - This is exactly where S8's four-mismatch words escape.
- **Relation to the literature.**
  - `ρ ≥ 4` improves this programme's `ρ ≥ 3` (C011).
  - The k-cycle literature bounds a different statistic, the number of local minima, as settled in the S6 dispute. No comparison with it is implied beyond the check above.

## 6. Limits and what it does not give

- **The output is `ρ ≥ 4`, not a growing `F(m)`.** At `s = 4`, the pigeonhole gives only `log₂ H > 0.396m`. Then the descent window can be about `0.32m` and the runs need not be bounded below. Steps 3–4 fail, so a new idea is needed.
  - Step 5's device does extend: each run's witness sits at a computable position, and witnesses far inside the climb are cheap. A bound for general `s` would need the witnesses to be spread out.
- **Imports.**
  - `gap_all` (formal in `mmusson/collatz`, replayed) is used only through `ℓ ≤ ℓ*(m)`. An irrationality measure for `log₂ 3` with a smaller exponent (Rhin-type) would lower `m0` a lot, but none is formal.
  - Barina's `L > 2^71` is used only to make `ε` negligible; `L ≥ 2^20` changes nothing visible.
  - The period import is any `m ≥ 452,695`.
- **Formalisation.** The proof splits into four lemmas, each elementary:
  - the sign lemma (F2 plus Step 2);
  - window disjointness;
  - alignment by excess transfer;
  - the refined ceiling at the witness (S6-a's `n_le_climb` at a position).
  - The numeric step has the same shape as S6-b's `numeric_step`.

## Reproduce

```sh
python3 sidekick/probes/s7_three_mismatch.py   # ~15 s: threshold scan to 10^7, then 616 control cycles
python3 sidekick/probes/s7_stress_rational.py 3 14   # ~30 s: every primitive word over {1,2,3} up to length 14
```
