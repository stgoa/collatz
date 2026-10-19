# S4: is there a law for `g = gcd(C, D)` on ordered band-1 cycles? (none found)

**Status:** side-lane producer batch S4 (2026-10-19). Finite data under stated caps. A law hunt with a negative outcome. Heuristics are labelled.

## Construction (Collatz range `m < A < 2m`)

Put `A = m + s` with `gcd(s, m) = 1`. Ranks rotate by `s`, and the exponent at rank `r` is `c = 1 + [r ≥ m−s]`.

- **Profiles.** Letter positivity forces the set of height-1 ranks to be a union of initial segments of the chains `{σ, σ+s, σ+2s, …}`, for `σ ∈ [1, s)`. This is the S1 zero-letter argument.
- **Words.** Each profile gives a word `a_i = c_i + h_i − h_(i+1)`.
- **Realisation.** A profile is kept only if the rational cycle of its word realises it: index 0 is the minimum, the actual heights equal the profile, the normalised states rotate ranks by `s`, and the images keep order.

## Data (`s4_band1_gcd.py`)

Profiles are exhaustive for `m ≤ 18` and sampled (3,000 per pair `(m, A)`) for `m ≤ 34`. Of 598,228 profiles tried, **46,555** are realised.

- **`g = 1`** in 43,732 of them (94%).
- **`g > 1`** in about 2,800, with values from 5 up to **14,303**.
- **`max log g / log D = 0.62`**.
- The shortest relation `2^u ≡ 3^v (mod g)` is short for small `g`, e.g. `5: (−1, 1)`, `7: (−2, 2)`, `23: (−3, 1)`. It is long for others: `2461: (14, 32)`, `14303: (27, 17)`, `2279: (−7, 21)`.
- **Per-`m` trend** (exhaustive up to `m = 16`, then 1,500 samples per `(m, A)`, `m ≤ 40`): the maximum of `log g/log D` jumps between 0 and 0.62 with no drift in either direction. It is 0.62 at `m = 17`, 0.39 at 23, and 0.06 at 39.

## Reading

- **No small-`g` law.** `g` is not bounded by a fixed power of `D` below the observed 0.62, and it does not always divide a short `2^u − 3^v`.
- **What `g` looks like.** It behaves like a divisor of `D` that happens to divide `C`.
- **Heuristic, labelled as such.** The admissible profiles number about `Π_σ (|chain_σ| + 1)`, roughly `2.4^(0.585m)`, far fewer than `D ≈ 3^m`. So a profile with `g = D` (a `q = 1` cycle) would be a coincidence of probability about `(2.4^0.585/3)^m`. That is the same counting heuristic as for general cycles, and it is not a proof.
- **Verdict.** No law to prove here. Together with S2 and S3, every shortcut tried on the ordered band-1 class reduces to the coupled `J`-term `S`-unit divisibility. That divisibility needs estimates uniform in a growing number of terms, which is the obstacle main named at C011–C014.

```sh
python3 reviews/side_lane/s4_band1_gcd.py   # ~3 min
```
