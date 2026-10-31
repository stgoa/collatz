---
id: rho-four-census-letters-three
kind: result
title: "Complete census of ρ ≤ 4 words with letters ≤ 3 and m ≤ 20: the near-critical half bound holds, eight far-from-critical words violate it, two of them with a primitive cancellation above 2^(A/2)"
status: written
claim: >
  Raw odd-only clock, any 3x+q. Every primitive positive word with letters in {1, 2, 3}, 9 ≤ m ≤ 20, D = 2^A − 3^m > 0
  and rotation distance ρ(w) ≤ 4 (one representative per rotation class, all shifts h including gcd(h, m) > 1) was
  enumerated through the track structure of a rotation with at most four mismatches: 113,422 words for m ≤ 16
  (certified) and 979,497 for m ≤ 20 (the m = 17–20 part is exploration), 29,052 of them near-critical
  (2^A < 2·3^m). Findings: (i) no near-critical word violates the half bound G² < 2^A, G = gcd(C_w, D), and the
  closest near-critical word for m ≤ 16 is 1.015 bits below it; (ii) exactly eight words violate the half bound,
  all with 2^A/3^m ≥ 2.46, at m = 12 (two), 16 (two), 18 (three) and 20 (one), with excesses between 0.018 and
  3.763 bits; (iii) two of them have gcd(A, m) = 1, so their whole cancellation is primitive:
  w = (1,1,2,2,1,3,1,2,2,2,3,3) (m = 12, A = 23, G = g_prim = 5921 = 2^(12.53) > 2^(11.5), the word of a 3x+1327
  cycle) and w = (1,1,2,2,1,1,2,2,1,2,2,2,1,1,3,2,1,1,3,2) (m = 20, A = 33, G = g_prim = 1,257,863 = 2^(20.26) >
  2^(16.5), a 3x+4057 cycle word); they refute part (A) of primitive-cancellation-below-half as posed; (iv) every
  violating word has its four-mismatch rotations at shifts h with gcd(h, m) ≥ 2 (m/2, m/3, m/4 or m/6), i.e. none is
  a few-arc rotation coding, consistent with the earlier censuses.
authors:
  - Claude cycles lane (Fable 5.1; directed by Santiago Armstrong)
created: 2026-10-31
depends_on: [few-arc-codings-denominator-census, algebraic-and-primitive-cancellation-census]
certificates: [check_rho4_census.py]
evidence:
  - "rho4_census.json: the receipt; Q1 the per-m summary for 9 ≤ m ≤ 16 (words, near-critical words, counts by ρ, violations of the half bound and of the primitive bound, the largest log₂g_prim − A/2, the largest log₂G − A/2 among near-critical words, the violating words), Q2 the eight violating words with their witnesses"
tags: [cycles, denominators, cancellation, rotation-distance, census, counterexample]
---

# Complete census of `ρ ≤ 4` words with letters `≤ 3` and `m ≤ 20`

## Statement

Notation of [`conventions/NOTATION.md`](../../../../conventions/NOTATION.md) §2 and of [`algebraic-and-primitive-cancellation-census`](../algebraic-and-primitive-cancellation-census/README.md) (`e = gcd(A, m)`, `g_prim = gcd(G, Φ_e(2^(A/e), 3^(m/e)))`). A word has `ρ(w) ≤ 4` iff some shift `h` has at most four mismatches; with `g = gcd(h, m)` the `h`-track splits into `g` cycles of length `m/g`, and along each cycle the letters are piecewise constant with `c_k` change points, `Σ c_k ≤ 4`, no `c_k = 1`. Enumerating all shifts, change-point sets and arc letters gives every such word; the enumeration is complete by construction (every word with a four-mismatch shift arises from that shift). The earlier censuses ([`few-arc-codings-denominator-census`](../few-arc-codings-denominator-census/README.md)) kept only `gcd(h, m) = 1` and two `gcd ∈ {2, 3}` families; this one keeps every shift, which is where all the violations live.

| `m` | words | near-critical | by `ρ` = 2 / 3 / 4 | `G² ≥ 2^A` | `g_prim² ≥ 2^A` | max `log₂g_prim − A/2` | max `log₂G − A/2`, near-critical |
|---|---|---|---|---|---|---|---|
| 9 | 907 | 100 | 81 / 160 / 666 | 0 | 0 | -1.116 | -5.178 |
| 10 | 2,183 | 144 | 291 / 184 / 1,708 | 0 | 0 | -1.762 | -4.300 |
| 11 | 2,244 | 180 | 89 / 390 / 1,765 | 0 | 0 | -4.601 | -5.541 |
| 12 | 7,110 | 488 | 840 / 318 / 5,952 | 2 | 1 | +1.032 | -1.795 |
| 13 | 5,003 | 339 | 136 / 684 / 4,183 | 0 | 0 | -1.295 | -10.500 |
| 14 | 19,963 | 1,018 | 2,168 / 600 / 17,195 | 0 | 0 | -2.229 | -5.196 |
| 15 | 14,977 | 848 | 659 / 968 / 13,350 | 0 | 0 | -5.587 | -8.300 |
| 16 | 61,035 | 2,574 | 6,319 / 1,042 / 53,674 | 2 | 0 | -1.836 | -2.328 |
| 17 (exploration) | 17,236 | 872 | 252 / 1,664 / 15,320 | 0 | 0 | -5.028 | — |
| 18 (exploration) | 207,127 | 5,910 | 20,244 / 1,682 / 185,201 | 3 | 0 | -0.100 | — |
| 19 (exploration) | 27,163 | 1,341 | 310 / 2,304 / 24,549 | 0 | 0 | -5.084 | — |
| 20 (exploration) | 614,549 | 15,238 | 57,175 / 2,504 / 554,870 | 1 | 1 | +3.763 | — |

Totals: 979,497 words, 29,052 near-critical, 8 violations of the half bound, none near-critical, 2 violations of the primitive bound.

**The eight violations** (all far from critical; `q = D/G` is the modulus of the actual cycle the word belongs to):

| word | `m` | `A` | `G` | `q` | `e` | `g_prim` | `log₂G − A/2` | `2^A/3^m` | four-mismatch shifts |
|---|---|---|---|---|---|---|---|---|---|
| `(1, 1, 2, 2, 3, 1, 2, 2, 3, 3, 2, 2)` | 12 | 24 | 6,475 | 2,509 | 12 | 1 | +0.661 | 31.569 | 4 (gcd 4), 8 (gcd 4) |
| `(1, 1, 2, 2, 1, 3, 1, 2, 2, 2, 3, 3)` | 12 | 23 | 5,921 | 1,327 | 1 | 5,921 | +1.032 | 15.785 | 6 (gcd 6) |
| `(1, 1, 2, 1, 1, 3, 1, 2, 1, 3, 2, 3, 1, 3, 1, 2)` | 16 | 28 | 19,415 | 11,609 | 4 | 1,765 | +0.245 | 6.236 | 8 (gcd 8) |
| `(1, 1, 2, 2, 2, 1, 2, 3, 1, 2, 2, 2, 2, 1, 2, 2)` | 16 | 28 | 16,591 | 13,585 | 4 | 353 | +0.018 | 6.236 | 8 (gcd 8) |
| `(1, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2)` | 18 | 30 | 91,595 | 7,493 | 6 | 7 | +1.483 | 2.772 | 3 (gcd 3), 15 (gcd 3) |
| `(1, 2, 2, 3, 1, 3, 1, 3, 1, 3, 2, 2, 1, 3, 1, 3, 1, 3)` | 18 | 36 | 1,697,227 | 40,261 | 18 | 1 | +2.695 | 177.377 | 8 (gcd 2), 10 (gcd 2) |
| `(1, 2, 2, 2, 2, 2, 2, 3, 1, 3, 2, 2, 2, 2, 2, 2, 1, 3)` | 18 | 36 | 3,151,993 | 21,679 | 18 | 1 | +3.588 | 177.377 | 8 (gcd 2), 10 (gcd 2) |
| `(1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 2, 1, 1, 3, 2, 1, 1, 3, 2)` | 20 | 33 | 1,257,863 | 4,057 | 1 | 1,257,863 | +3.763 | 2.464 | 4 (gcd 4), 16 (gcd 4) |

The two words with `e = 1` are the refutation of part (A) of [`primitive-cancellation-below-half`](../../questions/primitive-cancellation-below-half.md) as posed on 2026-10-31: `g_prim = G` and `G > 2^(A/2)`. Both are doubled or near-periodic words (shifts `m/2` and `m/4`), far from critical (`2^A/3^m = 15.8` and `2.46`).

## Proof

Finite computation. Completeness of the enumeration: if `ρ(w) ≤ 4` there is a shift `h` with `mism(w, h) ≤ 4`; the letters along each cycle of `i ↦ i + h` change exactly at the mismatches on that cycle, so the word is determined by the shift, the change points and the letters of the arcs, with adjacent arcs carrying different letters and no cycle carrying a single change point (a cycle's letter must return to itself). The certificate re-derives `ρ` exactly for every word and checks it is at most 4. The statistics are exact integer computations; `log₂` values are rounded to three decimals.

## Certificates

[`check_rho4_census.py`](check_rho4_census.py) (standard library, about 25 s): **Q1** the complete enumeration for `9 ≤ m ≤ 16`, letters `≤ 3`, with the per-`m` summary above; **Q2** the eight violating words (including those found at `m = 18, 20` by the same code run as exploration): primitivity, `D > 0`, `ρ = 4` with exactly the listed witnesses, `G`, `e`, `g_prim`, the violation and the non-near-criticality; **Q3** the receipt [`rho4_census.json`](rho4_census.json) (`--write-receipt` regenerates it). The `m = 17–20` rows of the table come from the same program run without the cap (about twenty minutes) and are not certified.

## Remarks

- **What survives of the half-cancellation idea.** The plain bound `G² < 2^A` fails for far-from-critical words (where `G = D/q` with `D ≈ 2^A` and a small `q` suffices) and so does the primitive bound when `gcd(A, m) = 1`; both hold on every near-critical word here, with margin at least 1.0 bits for `m ≤ 16`. The restriction to near-critical words is natural for the purpose (a `q = 1` cycle is near-critical) and is the form kept open in [`primitive-cancellation-below-half`](../../questions/primitive-cancellation-below-half.md).
- **Heuristic (labelled).** In the random-divisor model of [`algebraic-and-primitive-cancellation-census`](../algebraic-and-primitive-cancellation-census/README.md), `P(G ≥ x) ≈ c·N/x` with `c` between 0.1 and 0.5, a word violates the half bound with probability about `c·2^(−A/2)`. Summed over the 950,000 far-from-critical words (typical `A/2` between 12 and 17) this predicts a handful of violations, as observed (8). Summed over the 29,052 near-critical words (`A/2 ≈ 0.79m`) it predicts about `0.3·c`, consistent with none; the number of near-critical `ρ ≤ 4` words with letters `≤ 3` grows like `2^(0.68m)` in this range while `2^(A/2)` grows like `2^(0.79m)`, so the expected number of near-critical violations per `m` decreases. The census therefore neither supports nor undermines the near-critical form beyond "no violation yet"; it does show that the general forms were wrong for a statistical reason, not a structural one.
- **Where the violations sit.** All eight have their four-mismatch rotations at shifts with `gcd(h, m) ∈ {m/2, m/3, m/4, m/6}`: doubled words (`h = m/2`), `(a b b a)`-type words and words with a periodic background of period 3, 4 or 6 and few defects. None is a rotation coding with `gcd(h, m) = 1`, so the few-arc censuses could not see them. The `m = 12`, `e = 1` word is `(u, v)` with `v = u + e_1 + 2e_4`, a two-letter change with odd `S_v − S_u`, outside the doubled-word theorem (which needs `A` even).
- **Controls.** Every word in the census is an actual `3x+q` cycle word with `q = D/G` (NOTATION §2); the eight violations are cycles of `3x+2509`, `3x+1327`, `3x+11609`, `3x+13585`, `3x+7493`, `3x+40261`, `3x+21679` and `3x+4057`. Nothing is claimed about `q = 1`.
- **Novelty.** Undetermined; the enumeration method is elementary.

## History

- Written 2026-10-31 by the Claude cycles lane (Fable 5.1), directed by Santiago Armstrong, to close the `gcd(h, m) > 1` gap of the earlier censuses; it refuted part (A) of the lane's own question of the same day.
