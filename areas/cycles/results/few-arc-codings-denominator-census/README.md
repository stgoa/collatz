---
id: few-arc-codings-denominator-census
kind: result
title: "Few-arc rotation codings: an exact census of cancellation and reduced denominators"
status: written
claim: >
  Raw odd-only clock, any 3x+q. Call a positive valuation word of length m an s-arc coding when some
  rotation h with gcd(h, m) = 1 differs from it in exactly s positions; for s = 2 also allow gcd(h, m) ∈
  {2, 3} (one two-arc track, the other tracks constant). Every primitive such word with D = 2^A − 3^m > 0
  was enumerated, one per rotation class, in five censuses: s = 2 with letters ≤ 4 and m ≤ 40 (29,340
  words), letters ≤ 8 and m ≤ 36 (113,165), gcd(h, m) ∈ {2, 3} with letters ≤ 4 and m ≤ 30 (13,207);
  s = 3 with letters ≤ 4 and m ≤ 30 (205,640); s = 4 with letters ≤ 3 and m ≤ 22 (132,131). With
  G = gcd(C_w, D) and q = D/G: (i) the candidate G^s·4^m < 2^(As)·3^m holds for every word, its log₂
  slack is at least 8.75 (s = 2), 17.5 (s = 3) and 13.5 (s = 4) bits and grows about linearly in m;
  (ii) every word with m ≥ 9 has G² < 2^A, with log₂G − A/2 at most −2.81 (s = 2), −0.93 (s = 3) and
  −0.06 (s = 4); the only exception at m ≤ 8 is (1,1,2,2,1,1,3,3), the 3x+11 cycle (13, 25, 43, 35, 29,
  49, 79, 31) with G = 893, q = 11; (iii) every word with m ≥ 9 has log₂q ≥ 0.896·m (s ≤ 3) and
  ≥ 0.812·m (s = 4), and every word with m ≥ 3 has log₂q ≥ 0.74·m except that single m = 8 word;
  (iv) on the near-critical words (A ≤ m·log₂3 + 1) the proved two-defect bound
  q > (1 − 3^m/2^A)(2/√3)^m is below the true q by at least 4.4 bits at every m, by at least 10.2 bits
  for m ≥ 10 and by 50 bits at m = 36. The receipt also records that the two-arc (1,3) words on two equal
  arcs along the track of h = m/2 − 1 have G = (2^m − 3^(m/2))/7 for m = 12, 16, …, 40.
authors:
  - Claude cycles lane (Fable 5.1; directed by Santiago Armstrong)
created: 2026-10-28
depends_on: [two-defect-cancellation-bound]
certificates: [check_few_arc_census.py]
evidence:
  - "few_arc_census.json: the receipt; per census and per m it stores the word count, the discriminating count (m ≥ 6s), the number of words with G > 1, the minimum of log₂q and the word attaining it, the maximum of log₂G − A/2 and of log₂R, and on the near-critical words the minimum of log₂q and (for s = 2) of the margin over the proved bound (7)"
tags: [cycles, denominators, cancellation, rotation-distance, rotation-codings, census]
---

# Few-arc rotation codings: an exact census of cancellation and reduced denominators

## Statement

Notation of [`conventions/NOTATION.md`](../../../../conventions/NOTATION.md) §2: a positive valuation word `w = (a_0, …, a_(m−1))`, total `A`, `D = 2^A − 3^m > 0`, intercept `C_w = Σ_j 3^(m−1−j)·2^(a_0+…+a_(j−1))`, cancellation `G = gcd(C_w, D)`, reduced denominator `q = D/G`. For a rotation `h`, `s(h) = #{i : a_i ≠ a_(i+h)}`.

**Few-arc words.** If `gcd(h, m) = 1`, the map `k ↦ kh mod m` runs once through all positions, so the letters read along the `h`-track, `t_k = a_(kh mod m)`, form a cyclic sequence, and `a_i ≠ a_(i+h)` exactly at the `k` with `t_k ≠ t_(k+1)`. Hence `s(h) = s` means that the track splits into exactly `s` maximal arcs of constant letter with different letters on consecutive arcs, and conversely any such arc pattern defines a word with `s(h) = s`: the word is the **coding of the circle rotation by `h^(−1)/m` into `s` arcs**. For `s = 2` and `gcd(h, m) = g > 1`, [`two-defect-cancellation-bound`](../two-defect-cancellation-bound.md) (part 1) shows that both mismatches lie on one residue class mod `g` and every other class carries a constant letter.

**The censuses.** Every primitive word of the following kinds was enumerated, with `D > 0`, one representative per rotation class:

| census | `s` | `gcd(h, m)` | letters | `m ≤` | words | with `m ≥ 6s` |
|---|---|---|---|---|---|---|
| `s2_v4` | 2 | 1 | 1–4 | 40 | 29,340 | 28,733 |
| `s2_v8` | 2 | 1 | 1–8 | 36 | 113,165 | 109,927 |
| `s2_gcd` | 2 | 2, 3 (other tracks constant, letters 1–4) | 1–4 | 30 | 13,207 | 12,785 |
| `s3_v4` | 3 | 1 | 1–4 | 30 | 205,640 | 183,286 |
| `s4_v3` | 4 | 1 | 1–3 | 22 | 132,131 | 0 |

A word can appear in several censuses (an `s`-arc coding for one `h` may be an `s′`-arc coding for another); the four-arc census contains the two-marker words of [`two-marker-constant-background-exact-denominator`](../two-marker-constant-background-exact-denominator/README.md), whose rotation distance is 2. "Discriminating" means `m ≥ 6s`, slightly stricter than the `m/s ≥ 5.6` of [`rotation-defect-denominator-candidate`](../../questions/rotation-defect-denominator-candidate.md), where the candidate can fail at all.

**Findings (exact, from the receipt).** Write `log₂R = s·log₂G + 2m − As − m·log₂3`, so the candidate of that question is `R < 1`.

1. **The candidate holds throughout.** `log₂R ≤ −8.75` (`s = 2`, at `m = 3`), `≤ −17.55` (`s = 3`, at `m = 5`), `≤ −13.47` (`s = 4`, at `m = 8`). Per `m`, the maximum of `log₂R` falls about linearly: for `s = 3` it is `−25.6` at `m = 10` and `−99.3` at `m = 30`.
2. **Cancellation is at most half of `2^A`, for `m ≥ 9`.** `log₂G − A/2 ≤ −2.81` in all three two-arc censuses, `≤ −0.93` for `s = 3` (at `m = 10`: `w = (3,2,1,3,2,1,1,2,2,1)`, `G = 269`), and `≤ −0.06` for `s = 4` (at `m = 22`, the two-marker word `(1, 2^10, 3, 2^10)`, `G = 2^22 − 3^11`). The **only** word with `G² ≥ 2^A` in any census is `(1,1,2,2,1,1,3,3)`, `m = 8`, `A = 14`, `G = 893 = 19·47`, `q = 11`: the actual `3x+11` cycle `13 → 25 → 43 → 35 → 29 → 49 → 79 → 31 → 13`.
3. **Denominators grow like `2^(0.9m)`, not `2^(0.2m)`.** For `m ≥ 9`, `log₂q ≥ 0.896·m` in every census with `s ≤ 3` and `≥ 0.812·m` for `s = 4`. For `m ≥ 3`, `log₂q ≥ 0.740·m` everywhere except the `3x+11` word above (`0.432`). The floor `0.896` is attained at `m = 10` by the two-block word `1^4 2^6` (`q = 499`) and the floor `0.812` at `m = 17` by `(2,3,2,3,1,3,1,3,1^9)` (`q = 14,303`).
4. **The proved two-arc bound is far off where it matters.** On the near-critical words `A ≤ m·log₂3 + 1` (the only regime a `q = 1` cycle can occupy), the bound (7) of [`two-defect-cancellation-bound`](../two-defect-cancellation-bound.md), `q > (1 − 3^m/2^A)(2/√3)^m`, is below the true `q` by at least 4.38 bits at every `m`, by at least 10.22 bits for `m ≥ 10`, by 17.3 bits at `m = 17` (`1^7 2^10`: bound `0.44`, `q = 71,515`) and by 50.5 bits at `m = 36`. The margin grows about like `0.7m − log₂(D/2^A)`.
5. **Two exact patterns in the extremes**, both verified by the certificate for the stated ranges and unproved in general: the two-marker words `(1, 2^(n−1), 3, 2^(n−1))` have `G = 4^n − 3^n`, `q = 4^n + 3^n` (proved in [`two-marker-constant-background-exact-denominator`](../two-marker-constant-background-exact-denominator/README.md)); and the two-arc `(1,3)` words on two equal arcs along the track of `h = m/2 − 1` have `G = (2^m − 3^(m/2))/7` for `m = 12, 16, …, 40`, i.e. nearly the whole algebraic factor `2^(A/2) − 3^(m/2)` of `D = 2^(2m) − 3^m`.

Selected rows of the receipt (`min` and `max` are over the words of that `m`):

| `s = 2`, letters ≤ 8: `m` | words | min `log₂q / m` | max `log₂G − A/2` | near-critical words | their min `log₂q` | their min margin over (7) |
|---|---|---|---|---|---|---|
| 5 | 164 | 0.740 | −1.25 | 3 | 3.70 | 6.96 |
| 8 | 324 | 1.050 | −0.55 | 3 | 10.67 | 11.34 |
| 10 | 433 | 0.896 | −4.30 | 7 | 8.96 | 10.22 |
| 17 | 3,073 | 0.949 | −7.35 | 24 | 16.13 | 17.32 |
| 24 | 2,293 | 1.119 | −2.85 | 12 | 35.15 | 31.21 |
| 30 | 2,937 | 1.178 | −13.24 | 16 | 35.35 | 31.02 |
| 36 | 5,317 | 1.078 | −2.82 | 12 | 56.94 | 50.53 |

| `s = 3`: `m` | words | min `log₂q / m` | max `log₂G − A/2` | max `log₂R` |
|---|---|---|---|---|
| 5 | 96 | 0.740 | −1.54 | −17.55 |
| 10 | 548 | 0.896 | −0.93 | −25.64 |
| 16 | 3,128 | 1.041 | −5.14 | −47.77 |
| 20 | 5,096 | 1.178 | −9.57 | −69.63 |
| 26 | 13,284 | 1.262 | −11.80 | −89.10 |
| 30 | 12,008 | 1.178 | −13.24 | −99.28 |

| `s = 4`: `m` | words | min `log₂q / m` | max `log₂G − A/2` | max `log₂R` |
|---|---|---|---|---|
| 6 | 36 | 0.980 | −0.79 | −24.67 |
| 8 | 228 | **0.432** | **+2.80** | −13.47 |
| 10 | 591 | 0.896 | −0.39 | −37.41 |
| 14 | 2,930 | 1.013 | −0.21 | −51.02 |
| 17 | 15,600 | 0.812 | −5.03 | −67.06 |
| 22 | 23,887 | 1.003 | −0.06 | −79.12 |

## Proof

The claim is a finite computation; this section says why the enumeration is complete and what is computed.

- **Completeness.** By the track argument in the Statement, the words with a rotation `h`, `gcd(h, m) = 1`, of exactly `s` mismatches are exactly the `s`-arc codings: choose the track step `h` (all `h` coprime to `m`), the `s − 1` cut points of the track (all `(s−1)`-subsets of `{1, …, m−1}`), and the arc letters (all `s`-tuples in `{1, …, V}` with consecutive entries, cyclically, distinct). Position `j` receives the letter of the arc containing `j·h^(−1) mod m`. For `gcd(h, m) = g ∈ {2, 3}` and `s = 2`, the active class may be taken to be `0 mod g` after a rotation of the word; its track has `m/g` points and step `h/g`, and the other classes carry arbitrary constant letters in `{1, …, 4}`. Words that are periodic (a repeated block has the block's `q`) are dropped; for `s = 2` and `s = 3` with `gcd(h, m) = 1` none occur (a periodic word with period `p` has `(m/p)·s_p` mismatches with `s_p ≥ 2`), and for `s = 4` exactly 258 doubled two-arc words were dropped.
- **Per word**, exact integers: `C_w`, `A`, `D`, `G = gcd(C_w, D)`, `q`, then `log₂R`, `log₂G − A/2` and `log₂q` in floating point rounded to four decimals. The near-critical test is `A ≤ m·log₂3 + 1`; the margin over (7) is `log₂q − [log₂D − A + m(1 − log₂3/2)]`, which is `log₂` of the ratio of `q` to the bound `(1 − 3^m/2^A)(2/√3)^m`.
- **Checks.** The certificate fails on any word with `R ≥ 1` (C1), on any word with `m ≥ 9` and `G² ≥ 2^A` (C2), on any change in the per-`m` summary (C3, C5), on the two-marker closed form for `n ≤ 60` (C4), and on the half-swap identity for `m = 12, …, 40` (C6).

The `3x+11` and `3x+25` cycles quoted were recomputed from the words (states `C_(w^(j))/G`).

## Certificates

[`check_few_arc_census.py`](check_few_arc_census.py) (standard library, about 50 s) recomputes the five censuses and the two exact patterns and compares the summary with [`few_arc_census.json`](few_arc_census.json) byte for byte; `--write-receipt` regenerates the receipt. It checks finite statements only.

## Remarks

- **What this adds to the candidate.** [`rotation-defect-denominator-candidate`](../../questions/rotation-defect-denominator-candidate.md) had 56,150 discriminating random cases, none of them an exhaustive sweep in the regime `m/s ≥ 5.6`; the three-arc census alone has 183,286 discriminating words, every one of them. The slack is enormous: `R ≤ 2^(−8.75)` even at the worst word, and for `s = 3` the worst `log₂R` at each `m` falls like `−3.3m`. The candidate is not close to sharp anywhere in this range.
- **The sharp statement appears to be "cancellation at most half".** Finding 2 says `G < 2^(A/2)` for `m ≥ 9`, and the two-marker family shows that `2^(A/2)` cannot be lowered in the exponent (`G = 2^(A/2) − 3^(m/2)`). This bound implies the candidate for every `s ≥ 1`: `G ≤ 2^(A/2)` gives `G^s·4^m ≤ 2^(As/2)·4^m < 2^(As)·3^m` because `A ≥ m > 2m(2 − log₂3)/s`. It is stated as [`half-cancellation-for-few-mismatch-words`](../../questions/half-cancellation-for-few-mismatch-words.md), together with its payoff at `q = 1`.
- **Why the proved bound loses in the critical regime.** (5) of [`two-defect-cancellation-bound`](../two-defect-cancellation-bound.md) bounds `gcd(C_u, C_v)` of the two natural-order arcs by `√(C_u·C_v)`, which is exact in the two-marker family (`C_u = C_v`) but is off by about `m/2` bits for the near-critical two-block words, where the two arc intercepts are nearly coprime (`gcd = 71` at `m = 17`). Any effective improvement in the critical regime must bound the gcd of two arc intercepts by something far below their geometric mean; the finite data suggests it is typically `O(1)`.
- **Where the large cancellations come from.** Every large `G` in the censuses sits in an algebraic factor of `D`: when `gcd(A, m) = e > 1`, `2^(A/e) − 3^(m/e)` divides `D`, and words with a compatible symmetry (the half-swap `(u, ū)` structure of the `(1,3)` words, where `ū` exchanges the two letters; the two markers at distance `m/2`) make `C_w` divisible by it. These words have `A = 2m`, far from critical. Near-critical words have `gcd(A, m)` small, and their `G` is small.
- **Controls.** The `3x+11` cycle at `m = 8` is the only word of the censuses with `G² ≥ 2^A`, and it is a genuine cycle; the pattern `(1,2,2)^2` and the other dropped periodic words are the `3x+5` cycle `23 → 37 → 29` and its relatives. Actual cycles with small `d` and larger `m` have large rotation distance (every stored cycle has `s ≥ m/5`, see the candidate node), so they are outside the few-arc censuses, as they must be.
- **Scope.** Finite ranges only: no statement about `m` beyond the tables, and nothing about `q = 1` cycles, which would need `m > 1.375·10^11`. Novelty undetermined; the enumeration method (words with `s(h) = s` as rotation codings) is elementary.

## History

- Written 2026-10-28 by the Claude cycles lane (Fable 5.1), directed by Santiago Armstrong, as the first new result after the knowledge-graph migration. Exploration scripts live outside the repository; the certificate is the record.
