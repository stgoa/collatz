# S5: the mismatch–height trade-off at `q = 1`, made quantitative

**Status:** side-lane producer batch S5 (2026-10-19). This is a composition of results that are already formal, with one elementary step (a pigeonhole) and the two literature imports. Main's own C013 inequality (6) is the source of the shape. What is new here is only that the replayed `gap_all` makes it quantitatively strong. No cycle is excluded, and novelty is undetermined.

## 0. Why S5 does not use C012's coupled matrix (an observation, not new mathematics)

S5 was announced as a coupled two-plateau estimate at three mismatches. Reading C012 §§4–5 shows why that cannot give a size bound by congruences alone.

- **The rank-two structure.** C012 §4 shows `W ≡ u·vᵀ (mod D)`, where `v` is the first row of `W`. So `Wc ≡ u·X_0` and `W′c ≡ u′·Y_0 (mod D)`, with `X_0` and `Y_0` the two rotated intercepts at block start 0.
- **What the system says modulo `g`.** Hence `Mc ≡ u′Y_0 − u·X_0`. Modulo any `g` dividing `D`, the coupled system says only that `g | X_0` and `g | Y_0`. That holds automatically, since `g` divides every rotated intercept.
- **Why `s = 2` is different.** C011's gain at `s = 2` comes from inverting `M` over the integers with the small determinant `Π|β′ − β|`, not from congruences. At `s ≥ 3`, `det M` carries `D^(s−2)` (C012 (5)).
- **Consequence.** Any bound at `s ≥ 3` must come from integer sizes. S5 therefore uses the size route already in C013.

## 1. The inputs

Throughout, the cycle is primitive with `q = 1`, of period `m` and band `B` (`H < 2^(B+1) L`).

- **(I1) C013-b** (Lean `q_bound_rational`, `9a81b08`). Take a nonidentity rotation `h` and an agreeing run of length `t` (the letters agree with their `h`-shifts) with exponent total `E`. Primitivity makes `z ≠ 0`. Then

  ```
  6 D max(2^E, 3^t) < m q 2^A (2^(B+1) − 1).
  ```

  This is main's C013 (7). It uses no ordering and no comparison of `q` with `L`.
- **(I2) The pigeonhole** (elementary, not yet formal). If `w` and `w.rotate(h)` differ in exactly `s` positions, the `m − s` agreeing positions form at most `s` cyclic runs. So some agreeing run has length at least `⌈(m−s)/s⌉`.
- **(I3) `gap_all`** (`mmusson/collatz`, replayed by the Lean lane as EXT-1, standard axioms): `2^A ≤ 2^172 · m^341 · D`.
- **(I4) The period import** (Hercher/Barina, as in C011): `m > 1.375·10^11`. It is used only for the numbers in §3.

## 2. The trade-off (exact, given I1–I3)

At `q = 1`, combining I1 and I3 gives `3^t < 2^(B+173) m^342 / 6`. Hence every agreeing run satisfies

```
t < (B + 342 log₂ m + 172 − log₂ 6) / log₂ 3.
```

Combining this with I2, for **every** nonidentity rotation, the mismatch count `s` satisfies

```
s > m / (1 + (B + 342 log₂ m + 172 − log₂ 6)/log₂ 3)  ≈  log₂3 · m / (B + 342 log₂ m + 172).
```

This is main's C013 (6) at `q = 1`, with Matveev's `K_0 ≈ 6·10^8` replaced by the replayed exponent 341. Main's warning applies: `B` must be kept. Its distance-three family (C013 §3) shows that a bounded rotation distance does not bound the height, at least for rational cycles.

## 3. Numbers (with I4; `s5_mismatch_height.py`)

At `m = 1.375·10^11`, every nonidentity rotation of a hypothetical nontrivial Collatz cycle has mismatch count `s` greater than:

| band `B` | 0–10 | 100 | 10^3 | 10^4 | 10^5 | 10^6 | 10^7 |
|---|---|---|---|---|---|---|---|
| lower bound on `s` | 1.70·10^7 | 1.69·10^7 | 1.58·10^7 | 9.5·10^6 | 1.9·10^6 | 2.2·10^5 | 2.2·10^4 |

- **Cycles with `H < 8L`.** Since `B ≤ 2`, every rotation differs in more than 1.7·10^7 positions. This sits alongside the `J > 10^7` bound for the same band.
- **Comparison with C011.** The bound is still above 3, the case C011 already excludes, for every `B ≤ 7.26·10^10 ≈ 0.53m`. A positive cycle's letter budget (`A ≈ m log₂ 3`) allows at most about `0.585m` of net climb, so only the tallest conceivable cycles escape this bound.
- **Data.** On 283 actual `3x+q` cycles (odd `q < 200`) and all 3,100 of their nonidentity rotations, the longest agreeing run satisfies both the pigeonhole and (7) exactly.

## 4. What remains

Main's recommended intermediate milestone is a growing lower bound `F(m)` on the mismatch count of every rotation of any hypothetical nontrivial cycle. By §2, it follows from any height bound `B ≤ o(m)` for `q = 1` cycles, and `B = O(log m)` would give main's "order `m/log m`" payoff. So the open obstacle is now exactly a **height bound for integer cycles**.

No such bound is known to this lane. Main's C013 §3 family shows it cannot come from rotation distance alone. It would have to use `q = 1` arithmetic.

## Appendix: heights of actual cycles (data only, `s5_cycle_heights.py`)

The sample is the actual reduced `3x+q` cycles for odd `q < 1000` with `3 ∤ q`, found from starts `≤ 3001`: 1,147 cycles with `m ≥ 2`.

- `B` never exceeds 17.
- `B/log₂ m ≤ 3.0` for `m ≥ 30`, and `≤ 2.4` for `100 ≤ m < 200`.

This is consistent with a height bound of the form `B = O(log m)`, which would give main's `m/log m` mismatch payoff through §2. But the sample has small minima, `q/L = O(1)`. A `q = 1` cycle would have `L > 2^71`, which is the opposite regime. So these numbers are not evidence about `q = 1` heights, and no mechanism is proposed.

## Reproduce

```sh
python3 sidekick/probes/s5_mismatch_height.py   # ~1 s
python3 sidekick/probes/s5_cycle_heights.py     # ~4 s, appendix data
```
