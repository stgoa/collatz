---
id: ordered-cycle-run-renormalisation
kind: attempt
title: Renormalising ordered cycles by compressing the sorted-gap cycle to its run starts
status: reviewed
claim: >
  Tried, toward excluding ordered q = 1 cycles of the raw odd-only 3x+1 map: compress the m-step sorted-gap
  cycle of an ordered cycle to the J-state cycle of its run starts (an exact generalised Collatz cycle with
  multipliers 3^(t+1), offsets T and the same D), and iterate J → J₂ → … hoping the compressed cycle is again
  narrow and ordered. Verdict: rejected on finite data with an exact diagnosis. The compressed cycle is not
  narrow (spread max u/min u up to 240 on actual band-1 3x+q cycles, 2.5·10^7 on rational ones) and its gap
  cycle is mostly unordered (20 of 31 actual ordered cycles with m ≥ 3, 278 of 334 rational ones), because
  the level-2 forcing T takes both signs while the dyadic order lemma needs one uniform positive offset q.
  The identities survive as bookkeeping; no cycle is excluded.
authors:
  - Claude side lane (Opus)
created: 2026-10-19
depends_on: [run-start-gap-recursion, ordered-gap-closed-form, dyadic-order-lemma]
evidence:
  - "s2_ucycle_explore.py, s2_ucycle_explore.json: side-lane exploration probe (about 15-20 s): checks the run-start identity and the bookkeeping on the 33 actual and 337 rational ordered cycles (m ≤ 9, letters 1-4), and records the oddness, spread and level-2 order counts quoted here. Fails at its new path: it imports the side-lane helpers s1a_integer_cycle_check (now in ../../results/ordered-gap-closed-form/) and jterm_gap_check (legacy reviews/side_lane/, migrated by a later batch) from its own folder. Passed at be73a66 as reviews/side_lane/s2_ucycle_explore.py (archive/legacy-checker-run-be73a66.md)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Pre-review of the S2 announcement (points (b) and (c), incorporated) and feed update 11:11: section 3 accepted as a finite-data rejection with a correct diagnosis; section 1 formalised as S2-a and section 2 as S2-b; the section 4 attribution corrected at the lane's prompting and formalised as S2-c"
aliases: [S02]
tags: [cycles, ordered-cycles, gap-system, renormalisation, rejected-mechanism]
---

# Renormalising ordered cycles by compressing the sorted-gap cycle to its run starts

## Idea

Take an ordered reduced cycle at parameter `q` (C005 order, Lean `OrdCycle`; see [`dyadic-order-lemma`](../../results/dyadic-order-lemma.md)). Its sorted gaps satisfy C006's (G3), and only `J` positions are forced ([`ordered-gap-closed-form`](../../results/ordered-gap-closed-form/README.md)). Compressing each zero-forcing run to its start gives a `J`-state cycle of a generalised Collatz map with the same `D`. The hope was to iterate: compress, find the same structure (narrow, ordered) again, and compress again, `J → J₂ → …`.

Setting and notation (legacy §0). Normalise the scaled states as `Z = 2^(B−h)·n` and sort them. The sorted gaps `Δ_r` include the seam. The forcing is `T_r = q(2^(B−h_[r+1]) − 2^(B−h_[r]))` at interior ranks and `T_(m−1) = q(2^(B+1) − 2^(B−h_[m−1]))` at the seam. The exponents are `e_r = q′ + [r ≥ m−s]`, where `s` is the rank shift and `q′ = floor(A/m)`. The gaps satisfy `2^(e_r)·Δ_(r+s) = 3Δ_r + T_r`.

## What happened

**1. The run-compressed cycle (exact).** The `J` forced positions cut the rank orbit into `J` runs. For run `k`, let `t_k` be the number of unforced steps, `E_k` their exponent total, and `f_k` the forced rank that ends the run. By the run lemma, `2^(E_k)` divides the run-start gap. Put `u_k = Δ_(start_k)/2^(E_k)`. Then

```
2^(e_(f_k) + E_(k+1))·u_(k+1) = 3^(t_k+1)·u_k + T_(f_k),
Σ_k (e_(f_k) + E_k) = A,   Σ_k (t_k + 1) = m.
```

So the run starts form a `J`-state cycle of a generalised Collatz map, with multiplier `3^(t+1)`, offset `T` and the same `D = 2^A − 3^m`. Its cycle equation is S1-a's closed form. This is formal: [`run-start-gap-recursion`](../../results/run-start-gap-recursion.md). It holds on all 33 actual ordered `3x+q` cycles and on all 337 rational ordered cycles (`m ≤ 9`, letters 1 to 4).

**2. Oddness: an exact rule, not automatic** (the Lean lane's point (b)). `u_k` is odd exactly when `v₂(Δ_start) = E_k`, i.e. when the gap at the forced rank `f_k` is odd. Two scaled states `2^(B−h)·n` and `2^(B−h′)·n′`, with `n, n′` odd, differ by an odd number exactly when exactly one of `h, h′` equals `B`; the seam gap `2Z_[0] − Z_[m−1]` is odd exactly when `h_[m−1] = B`. In band 1, `u` is therefore odd for every run that ends at an interior forced rank, and for the seam run exactly when the top sorted height is 1. In band `B ≥ 2` it is often even. Formal as S2-b ([`run-start-gap-recursion`](../../results/run-start-gap-recursion.md)). Data (`s2_ucycle_explore.py`):

| Band and run type | `u` odd (actual / rational) |
|---|---|
| Band 1, interior-ending | 39/39 / 478/478 |
| Band 1, seam-ending | 3/14 / 48/189 (exactly the cases with top height 1) |
| Band 2, interior-ending | 18/33 / 198/344 |

The list `τ ∈ {±1, 2, 3}` used in the S2 announcement is the case `q = 1`, `B = 1` (the Lean lane's point (c)). In general every `T` carries `q·2^(B−·)`.

**3. A minor by-product** (corrected at 11:11 after the Lean lane's review). The earlier version said "a constant factor, roughly 1.58 in the leading term" and attributed it to summing over all runs. That attribution was wrong; the two effects are separate.

- **Summing over all runs gives almost nothing.** `2^B·L ≥ Σ_k 2^(E_k) ≥ J·2^(Σ E_k / J)` (C010-b's `Σ Δ = 2^B·L`) only adds a factor `J` inside `L`, i.e. a `−log₂ J` term in the `J` bound. At `J ≈ 10^7` that is about 0.2%.
- **The factor `A/m ≈ log₂ 3 ≈ 1.585` has a different source.** It comes from bounding the longest run's exponent total by its mechanical density rather than by its length: along the rank orbit `t` consecutive steps visit at least `floor(ts/m)` high ranks, so `E ≥ floor(tA/m)` ([`orbit-exponent-density`](../../results/orbit-exponent-density/README.md), formal as S2-c). Feeding this into the run bound instead of `E ≥ t` multiplies the leading term of the `J` bound by `A/m`, giving `J ≳ (A/m)(m−1)/(c + 3 + (μ+1)·log₂ m)`, about `1.7·10^7` instead of `1.07·10^7` at `m = 1.375·10^11` (estimate, not formalised as one theorem).

## Why it fails

The compressed cycle does not inherit order or narrowness.

- **Not narrow.** The spread `max u/min u` reaches 240 in actual band-1 `3x+q` cycles and `2.5·10^7` in rational band-1 cycles.
- **Not ordered at the next level.** Take the gap cycle itself in orbit order, normalised by its own minimum and heights. Among the 31 actual ordered cycles with `m ≥ 3`, it is unordered in 20, ordered in 9, and has tied normalised gaps in 2. Among the 334 rational ones it is unordered in 278. Its own band reaches 18.
- **The exact reason.** The level-2 forcing `T` takes both signs: a height rise gives `T < 0` and a fall gives `T > 0`. C005's inversion formula, `F_j − F_i = [3r − q(2^k − 1)]/2^(h_j)` ([`dyadic-order-lemma`](../../results/dyadic-order-lemma.md)), is what makes small bands ordered, and it rests on one uniform positive offset `q`. With signed offsets, the image order of the gap cycle is not controlled. The C004/C005/R71 machinery needs exactly that uniform positive offset, so it does not transfer to the gap cycle.

**Verdict:** naive renormalisation `J → J₂ → …` is rejected. A renormalisation would need a sign-insensitive notion of order, and none is proposed here. The rejection is on finite data (the counts above); the diagnosis (signed forcing) is exact.

## What survives

- The identities of §1 and the oddness rule of §2, as bookkeeping on the way to the `J`-term sums: [`run-start-gap-recursion`](../../results/run-start-gap-recursion.md) (formal).
- The orbit exponent density of §3: [`orbit-exponent-density`](../../results/orbit-exponent-density/README.md) (formal).
- With [`band-three-ordering-extension`](../band-three-ordering-extension/README.md) (S03) and [`band-one-gcd-law-search`](../band-one-gcd-law-search/README.md) (S04), this was one of three shortcuts on the ordered band-1 class; each reduces to the coupled `J`-term `S`-unit divisibility (feed 11:05).

## History

- Migrated from `experiments/cycle_spectrum/S02/RENORMALISATION.md` (legacy ID `S02`; side-lane producer batch S2, 2026-10-19) at commit `be73a66`, by the B05 migration (Claude, Opus 5.5). The side-lane probe `reviews/side_lane/s2_ucycle_explore.{py,json}` moved here. The note's §1 became [`run-start-gap-recursion`](../../results/run-start-gap-recursion.md) (with §2) and its §4 [`orbit-exponent-density`](../../results/orbit-exponent-density/README.md).
- Side lane (Claude, Opus), feed entry 2026-10-19 10:52. Reviewed in advance by the Lean lane, whose points (b) (oddness is a rule, not automatic) and (c) (the value set of `τ` is the `q = 1`, `B = 1` case) were incorporated before the note landed.
- **Correction (2026-10-19 11:11, after the Lean lane's review).** §4 (here §3 of "What happened") first attributed a constant-factor (≈1.58) improvement of the `J` bound to summing over all runs; the summing gives only `−log₂ J`, and the factor `A/m` comes from the orbit exponent density. Rewritten accordingly.
