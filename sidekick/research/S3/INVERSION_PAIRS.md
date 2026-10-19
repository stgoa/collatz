# S3: extending C005's ordering to `H < 16L` at `q = 1` (direct route blocked)

**Status:** side-lane producer batch S3 (2026-10-19). Exact reduction plus finite data. A quick negative; no exclusion.

## 1. What blocks ordering at band 3

C005's inversion lemma (2) applies to `z_i < z_j` with `h_j = h_i + k`, where `r = n_j − 2^k n_i` is positive and odd. The sorted images invert exactly when `3r < q(2^k − 1)`.

At `q = 1`:

- `k = 1` would need `3r < 1`, which never happens.
- `k = 2` would need `3r < 3`, which never happens. Equality is excluded by primitivity.
- `k = 3` needs `3r < 7`, so `r = 1`.

So a `q = 1` cycle with `H < 16L` (`B ≤ 3`) is ordered unless it contains a pair `(n, 8n+1)` with `h(n) = 0` and `h(8n+1) = 3`. The two points are then automatically sorted-adjacent: `z = n` and `n + 1/8`, and no `2^(−h)·odd` lies strictly between them when `h ≤ 3`.

If no such pair exists, C005-b's `three_band`, C006-f and the formal `J` bound of 09:43 all extend from `H < 8L` to `H < 16L`.

## 2. The pair's orbit at `q = 1` is forced, but only 2-adically

- `3(8n+1) + 1 = 4(6n+1)` with `6n+1` odd, so the next state is `6n+1`.
- `3(6n+1) + 1 = 2(9n+2)` with `9n+2` odd, so the next state is `9n+2`.
- After that comes `(27n+7)/2^v`.

The constraint `H < 16L ≤ 16n` forces `n < 16L/9` and further range conditions. Each step only adds a 2-adic congruence on `n`. A positive density of `n` survives any finite number of steps, so no finite-step contradiction exists.

## 3. The general relation is a defect recursion

Write the pair as `n_(t+h) = 2^(K_t) n_t − c_t`, starting from `K_0 = 3`, `c_0 = −1`. The pair's two orbits are two rotations of the same cycle. Then

```
K_(t+1) = K_t + a_t − a_(t+h),     c_(t+1) = (2^(K_t) + 3c_t − 1)/2^(a_(t+h)),
```

and closing the cycle requires `(K_m, c_m) = (3, −1)`. This is a rotation-mismatch / overlap problem of C013's type, with a dyadic scale `2^(K_t)`. It is not easier than the general one.

## 4. Data: the `q = 1` inversion type occurs at other `q`

`s3_inversion_pairs.py` scans odd `q < 400` with `3 ∤ q`: 719 cycles with `m ≥ 2`.

- It finds actual inversions at every height gap `k = 1…11`.
- It finds **37 pairs `(n, 8n+1)` at height gap exactly 3**. Examples, as `(q, n, m)`: `(121, 35, 46)`, `(175, 29, 12)`, `(181, 23, 10)`, `(191, 47, 24)`.

So the inversion lemma alone cannot exclude the pair. Excluding it at `q = 1` needs `q = 1`-specific global arithmetic. The `q`-dependence enters through the forced orbit `8n + 1 → (24n + 3 + q)/2^v → …`.

**Verdict:** S3's direct route is blocked. It reduces to the C013-type overlap problem. Switching to S4: the size and structure of `g = gcd(C, D)` on ordered band-1 cycles, to look for a law.

```sh
python3 sidekick/probes/s3_inversion_pairs.py   # ~37 s
```
