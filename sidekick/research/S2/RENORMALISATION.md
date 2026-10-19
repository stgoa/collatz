# S2: renormalising ordered cycles by run compression (rejected, with its exact obstruction)

**Status:** side-lane producer batch S2 (2026-10-19). It reports exact identities, finite data and a negative finding. No cycle exclusion and no novelty claim. It was reviewed in advance by the Lean lane, whose points (b) and (c) are incorporated below.

## Setting

Take an ordered reduced cycle at parameter `q` (C005 order; Lean `OrdCycle`). Normalise the scaled states as `Z = 2^(B−h) n` and sort them. The sorted gaps `Δ_r` include the seam. The forcing is

- `T_r = q(2^(B−h_[r+1]) − 2^(B−h_[r]))` at interior ranks;
- `T_(m−1) = q(2^(B+1) − 2^(B−h_[m−1]))` at the seam.

The exponents are `e_r = q′ + [r ≥ m−s]`, where `s` is the rank shift. The gaps satisfy C006's (G3), `2^(e_r) Δ_(r+s) = 3Δ_r + T_r`.

## 1. The run-compressed cycle (exact)

The `J` forced positions cut the rank orbit into `J` runs. For run `k`, let:

- `t_k` be the number of unforced steps;
- `E_k` be their exponent total;
- `f_k` be the forced rank that ends the run.

By the run lemma, `2^(E_k)` divides the run-start gap. Put `u_k = Δ_(start_k)/2^(E_k)`. Then

```
2^(e_(f_k) + E_(k+1)) u_(k+1) = 3^(t_k+1) u_k + T_(f_k),
Σ_k (e_(f_k) + E_k) = A,   Σ_k (t_k + 1) = m.
```

So the run starts form a `J`-state cycle of a generalised Collatz map, with multiplier `3^(t+1)`, offset `T` and the same `D = 2^A − 3^m`.

- Its cycle equation is S1-a's closed form.
- The Lean lane is formalising the recursion as S2-a.
- It holds on all 33 actual ordered `3x+q` cycles and on all 337 rational ordered cycles (`m ≤ 9`, letters 1 to 4).

## 2. Oddness: an exact rule, not automatic (Lean lane's point (b))

`u_k` is odd exactly when `v₂(Δ_start) = E_k`, i.e. when the gap at the forced rank `f_k` is odd.

- Two scaled states `2^(B−h)n` and `2^(B−h′)n′`, with `n, n′` odd, differ by an odd number exactly when exactly one of `h, h′` equals `B`.
- The seam gap `2Z_[0] − Z_[m−1]` is odd exactly when `h_[m−1] = B`.

In band 1, `u` is therefore odd for every run that ends at an interior forced rank, and for the seam run exactly when the top sorted height is 1. In band `B ≥ 2` it is often even.

Data (`s2_ucycle_explore.py`):

| Band and run type | `u` odd |
|---|---|
| Band 1, interior-ending (actual / rational) | 39/39 / 478/478 |
| Band 1, seam-ending | 3/14 / 48/189 (exactly the cases with top height 1) |
| Band 2, interior-ending | 18/33 / 198/344 |

The list `τ ∈ {±1, 2, 3}` used in the S2 announcement is the case `q = 1`, `B = 1` (the Lean lane's point (c)). In general every `T` carries `q·2^(B−·)`.

## 3. The obstruction: the compressed cycle does not inherit order or narrowness

S2's hope was to iterate: compress, find the same structure again, and compress again. The data rejects this.

- **Not narrow.** The spread `max u/min u` reaches 240 in actual band-1 `3x+q` cycles and 2.5·10^7 in rational band-1 cycles.
- **Not ordered at the next level.** Take the gap cycle itself in orbit order, normalised by its own minimum and heights. Among the 31 actual ordered cycles with `m ≥ 3`, it is unordered in 20, ordered in 9, and has tied normalised gaps in 2. Among the 334 rational ones it is unordered in 278. Its own band reaches 18.
- **The exact reason.** The level-2 forcing `T` takes both signs. A height rise gives `T < 0` and a fall gives `T > 0`. C005's inversion lemma (2), `F_j − F_i = [3r − q(2^k − 1)]/2^(h_j)`, is what makes small bands ordered, and it rests on one uniform positive offset `q`. With signed offsets, the image order of the gap cycle is not controlled. The C004/C005/R71 machinery needs exactly that uniform positive offset, so it does not transfer to the gap cycle.

**Verdict:** naive renormalisation `J → J₂ → …` is rejected. The identities of §1 stay, as bookkeeping on the way to S1-a's `J`-term sums. A renormalisation would need a sign-insensitive notion of order, and none is proposed here.

## 4. A minor by-product (corrected at 11:11 after the Lean lane's review)

The earlier version said "a constant factor, roughly 1.58 in the leading term" and attributed it to summing over all runs. That attribution was wrong. The two effects are separate.

- **Summing over all runs gives almost nothing.** `2^B L ≥ Σ_k 2^(E_k) ≥ J·2^(Σ E_k / J)` (C010-b's `Σ Δ = 2^B L`) only adds a factor `J` inside `L`, i.e. a `−log₂ J` term in the `J` bound. At `J ≈ 10^7` that is about 0.2%.
- **The factor `A/m ≈ log₂ 3 ≈ 1.585` has a different source.** It comes from bounding the longest run's exponent total by its mechanical density rather than by its length. Along the rank orbit, `e = q′ + [high rank]`, and `t` consecutive steps visit at least `⌊ts/m⌋` high ranks, so `E ≥ ⌊t(mq′ + s)/m⌋ = ⌊tA/m⌋`.
  - Feeding this into `run_bound_E_L` instead of `E ≥ t` (C006-b's `E_ge`) multiplies the leading term of the `J` bound by `A/m`.
  - That gives `J ≳ (A/m)(m−1)/(c + 3 + (μ+1) log₂ m)`, about `1.7·10^7` instead of `1.07·10^7` at `m = 1.375·10^11`.
  - It is minor and not formalised.

## Reproduce

```sh
python3 sidekick/probes/s2_ucycle_explore.py   # ~15 s; identities PASS; oddness and spread statistics
```

The probe also runs the level-2 order test (`level2_order`). Its receipt `s2_ucycle_explore.json` records the counts quoted in §3.
