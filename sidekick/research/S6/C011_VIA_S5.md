# S6: C011's two-defect exclusion re-derived without Matveev, via S5-a, `gap_all` and the height ceiling

**Status:** side-lane producer batch S6 (2026-10-19). A written derivation from formal and replayed components plus one elementary inequality, the height ceiling, which the Lean lane offered to formalise. It needs only a weak period input. It proves no new exclusion: it is an alternative route to C011's conclusion, with lighter imports. Novelty undetermined.

## 1. Statement

Let a nontrivial Collatz cycle (`q = 1`) be primitive, with period `m ≥ 24,891` and minimum `L > 2^71`. Then **no nonidentity rotation of its valuation word differs from it in exactly two positions**. That is C011's conclusion.

More generally, a rotation with exactly three mismatches requires `B > 0.528m − 342 log₂ m − 172`, which is near the top of the possible height range.

## 2. Derivation

1. **S5-a** (Lean `mismatch_height`, formal, `c0cdc48`). Take `q = 1`, a gap hypothesis `2^A ≤ 2^c m^μ D`, and `h ≢ 0`. Then there is a `t` with `m ≤ s(t+1)` and `6·3^t < 2^(B+1+c) m^(μ+1)`.
2. **`gap_all`** (`mmusson/collatz`, replayed as EXT-1, standard axioms) supplies the gap hypothesis with `(c, μ) = (172, 341)`.
3. **The height ceiling** (the Lean lane's argument in its S5 review; elementary, not yet formal). Along the arc from the minimum to the maximum, each step multiplies by `(3 + 1/n_i)/2^(a_i) ≤ (3/2)(1 + 1/(3L))`. So `B ≤ (log₂ 3 − 1)(m − 1) + (m − 1)·log₂(1 + 1/(3L))`. (This is the corrected form: an earlier version had `+ 1` and `m` in place of `m − 1`.) With `L > 2^71` the last term is below `10^(−20)·m`.
4. **Combining.** If `s = 2`, then `t ≥ ⌈m/2⌉ − 1`. Taking logarithms gives
   `log₂ 6 + (⌈m/2⌉ − 1) log₂ 3 < (log₂ 3 − 1)(m − 1) + 173 + ε + 342 log₂ m`.
   The left side grows like `0.792m` and the right like `0.585m + 342 log₂ m`. The probe finds the inequality false for every `m ≥ 24,891` (it was `24,895` with the earlier `+1`), and the slope is positive from `m ≥ 2^12` on.
5. **`s = 3`.** Here `t ≥ ⌈m/3⌉ − 1`, which gives `B > (log₂ 3/3)m − 342 log₂ m − O(1) ≈ 0.528m − 342 log₂ m − 172`.

## 3. What changes compared with C011

| | C011 (main) | S6 |
|---|---|---|
| Linear-forms input | Matveev (Languasco–Luca–Moree–Togbe), `K_0 < 6·10^8`, imported, not formal | `gap_all`, formal in `mmusson/collatz` and replayed here (EXT-1) |
| Period input | `m > 1.375·10^11` (Hercher/Barina) | `m ≥ 24,891` |
| Minimum input | (through the period input) | `L > 2^71` (Barina), used only to make the `ε` term negligible; any `L ≥ 2^20` suffices |
| Formal status | written proof with two imports | S5-a formal; `gap_all` formal elsewhere; the ceiling elementary; the period input imported |

For the period input, Hercher's bound or even Eliahou's 1993 bound is far more than needed. *[Corrected 2026-10-19: Eliahou's 17,087,915 bounds the total cycle length `A`, so in odd steps it gives `m ≳ 1.08·10^7`. An earlier version wrote `m ≥ 17,087,915`.]*

## 3a. Remarks from the Lean lane's review

- **The minimum enters only through the threshold.** The slope comparison needs `log₂(1 + 1/(3L)) < log₂3/2 − (log₂ 3 − 1) ≈ 0.2075`, which holds for `L ≥ 3`. So the exclusion holds eventually for every positive cycle. `L ≥ 2^20` only fixes the threshold, and `L > 2^71` makes the term negligible. The result is really about the period.
- **The relation to the k-cycle literature.** Simons–de Weger and its successors exclude cycles with few local minima (k-cycles). The two-defect class is a different kind of low complexity: words that are near-periodic with one defect pair. Those words can have about `m/3` local minima.
  - **Example.** The positive-range words `x(122)^k`, with one inserted letter, have a rotation by 3 with exactly two mismatches. At `m = 118` they have 78 run boundaries.
  - So the k-cycle results do not cover C011's class. C011 itself is the relevant exclusion, and S6 changes only its route.

## 4. Limits

- **Not a new exclusion.** C011's statement is unchanged. What changes is the route, which no longer needs Matveev.
- **The period input is still computational.** Some computation must rule out cycles of period below 24,891.
- **The `s = 3` clause** is the S5 trade-off at its top end. Three mismatches are possible only for nearly maximal height.

## Reproduce

```sh
python3 sidekick/probes/s6_c011_via_s5.py   # ~1 s; m0 = 24,891
```
