---
id: band-one-gcd-law-search
kind: attempt
title: Searching for a law for gcd(C, D) on ordered band-1 words
status: reviewed
claim: >
  Tried, toward excluding ordered band-1 (H < 4L) q = 1 cycles of the raw odd-only 3x+1 map in the
  Collatz range m < A < 2m: find a law bounding g = gcd(C_w, D_w) on the words realised by ordered band-1
  height profiles (a provable g < D would exclude band 1 at q = 1). Verdict: no law found, on finite data.
  Of 598,228 profiles tried (exhaustive for m ≤ 18, sampled to m ≤ 34), 46,555 are realised; g = 1 in
  43,732, g > 1 in about 2,800 with values up to 14,303 and max log g / log D = 0.62, the per-m maximum of
  log g / log D jumps between 0 and 0.62 with no drift (m ≤ 40), the shortest relation 2^u ≡ 3^v (mod g) is
  sometimes long, and g divides a proper cyclic block denominator in only 1,213 of the 1,413 exhaustive
  g > 1 cases (m ≤ 18). A counting comparison of profiles with D is labelled heuristic. No cycle is excluded.
authors:
  - Claude side lane (Opus)
created: 2026-10-19
depends_on: [band-one-three-forced-positions, ordered-gap-closed-form, ordered-cycle-sparse-forcing]
evidence:
  - "s4_band1_gcd.py, s4_band1_gcd.json: side-lane exploration probe (about 3 min): profile construction, realisation test, g statistics and per-m trend. Fails at its new path: it imports the side-lane helper jterm_gap_check from its own folder (legacy reviews/side_lane/, migrated by a later batch). Passed at be73a66 as reviews/side_lane/s4_band1_gcd.py (archive/legacy-checker-run-be73a66.md)"
  - "s4b_block_divisor_test.py, s4b_block_divisor_test.json: side-lane exploration probe (about 40-50 s), exhaustive for m ≤ 18: 1,413 profiles with g > 1, g divides some proper cyclic block denominator 2^(A_u) − 3^|u| in 1,213. Imports s4_band1_gcd from this folder and fails with it at the new path. Passed at be73a66 as reviews/side_lane/s4b_block_divisor_test.py (archive/legacy-checker-run-be73a66.md)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Pre-review of S4 (feed update 11:11: framing g = C_w/n_0, so g < D is just q > 1, and the question is C006's (G1)/(G2) comparison) and acceptance of S4 as a labelled negative search (feed update 11:19 to the S3 entry)"
aliases: [S04]
tags: [cycles, ordered-cycles, band-one, gcd, negative-search]
---

# Searching for a law for gcd(C, D) on ordered band-1 words

## Idea

On ordered band-1 cycles, earlier data had `g = gcd(C, D) ∈ {1, 5, 7, 23}`, each of the form `2^a − 3^b` with small exponents. S4 asked whether `g` is always small or has a recognisable structure. A provable bound with `g < D` would exclude band 1 at `q = 1`.

## What happened

**Construction (Collatz range `m < A < 2m`).** Put `A = m + s` with `gcd(s, m) = 1`. Ranks rotate by `s`, and the exponent at rank `r` is `c = 1 + [r ≥ m−s]`.

- **Profiles.** Letter positivity forces the set of height-1 ranks to be a union of initial segments of the chains `{σ, σ+s, σ+2s, …}`, for `σ ∈ [1, s)`. This is the S1 zero-letter argument ([`band-one-three-forced-positions`](../../results/band-one-three-forced-positions.md)).
- **Words.** Each profile gives a word `a_i = c_i + h_i − h_(i+1)`.
- **Realisation.** A profile is kept only if the rational cycle of its word realises it: index 0 is the minimum, the actual heights equal the profile, the normalised states rotate ranks by `s`, and the images keep order.

**Data** (`s4_band1_gcd.py`). Profiles are exhaustive for `m ≤ 18` and sampled (3,000 per pair `(m, A)`) for `m ≤ 34`. Of 598,228 profiles tried, **46,555** are realised.

- **`g = 1`** in 43,732 of them (94%).
- **`g > 1`** in about 2,800, with values from 5 up to **14,303**.
- **`max log g / log D = 0.62`**.
- The shortest relation `2^u ≡ 3^v (mod g)` is short for small `g`, e.g. `5: (−1, 1)`, `7: (−2, 2)`, `23: (−3, 1)`. It is long for others: `2461: (14, 32)`, `14303: (27, 17)`, `2279: (−7, 21)`.
- **Per-`m` trend** (exhaustive up to `m = 16`, then 1,500 samples per `(m, A)`, `m ≤ 40`): the maximum of `log g/log D` jumps between 0 and 0.62 with no drift in either direction. It is 0.62 at `m = 17`, 0.39 at 23, and 0.06 at 39.

**Framing (feed update 11:11, following the Lean lane's pre-review; exact).** `g = C_w/n_0`, because `n_0·D = q·C_w` and `q = D/g`. So `g < D` is just `q > 1`. The formal bound `g ≤ C_c/n_0` (C006-e, [`ordered-cycle-sparse-forcing`](../../results/ordered-cycle-sparse-forcing/README.md)) is tight up to the trivial factor `C_w/C_c ∈ [1/2, 1]` in band 1 (observed `[0.59, 0.99]`). So S4's question is exactly C006's (G1)/(G2) comparison; S4 adds no new quantity, only the negative data.

**Specificity.** The observation "`g ∈ {5, 7, 23}` has the form `2^a − 3^b`" carries little weight: six of the ten numbers coprime to 6 below 30 have that form.

**Structural test** (`s4b_block_divisor_test.py`, exhaustive for `m ≤ 18`: 1,413 profiles with `g > 1`). `g` divides some proper cyclic block denominator `2^(A_u) − 3^|u|` in 1,213 of them (86%) and in none of the 200 others. Examples: `g = 31` at `(m, A) = (12, 23)` and `g = 79` at `(14, 23)`. So there is no block-divisor law either.

## Why it fails

- **No small-`g` law.** `g` is not bounded by a fixed power of `D` below the observed 0.62, and it does not always divide a short `2^u − 3^v`.
- **What `g` looks like.** It behaves like a divisor of `D` that happens to divide `C`.
- **Heuristic, labelled as such, not a proof.** The admissible profiles number about `Π_σ (|chain_σ| + 1)`, roughly `2.4^(0.585m)`, far fewer than `D ≈ 3^m`. So a profile with `g = D` (a `q = 1` cycle) would be a coincidence of probability about `(2.4^0.585/3)^m`. That is the same counting heuristic as for general cycles.
- **Verdict.** No law to prove here. All statements above are finite data under the stated caps.

## What survives

- The data, as a calibration for any proposed `g`-law on ordered band-1 words.
- **Where S2–S4 leave this class** (feed 11:05). Three shortcuts on the ordered band-1 class (`H < 4L`) were tried and each failed: renormalising by run compression ([`ordered-cycle-run-renormalisation`](../ordered-cycle-run-renormalisation/README.md): the level-2 forcing has signed offsets), excluding the band-3 inversion pair directly ([`band-three-ordering-extension`](../band-three-ordering-extension/README.md): the pair type occurs at other `q`), and a small-gcd law (this node: none found). Each reduces to the coupled `J`-term `S`-unit divisibility of [`ordered-gap-closed-form`](../../results/ordered-gap-closed-form/README.md), with `J > 10^7` for any hypothetical cycle ([`ordered-cycle-height-change-growth`](../../results/ordered-cycle-height-change-growth.md), conditional on the gap). That needs estimates uniform in growing `J`, the obstacle main named at C011–C014. The side lane's next batch changed mechanism, not class.

## History

- Migrated from `experiments/cycle_spectrum/S04/BAND1_GCD.md` (legacy ID `S04`; side-lane producer batch S4, "a law hunt with a negative outcome; heuristics are labelled") at commit `be73a66`, by the B05 migration (Claude, Opus 5.5). The side-lane probes `reviews/side_lane/s4_band1_gcd.{py,json}` and `s4b_block_divisor_test.{py,json}` moved here; the framing, specificity and structural-test paragraphs come from the feed update of 2026-10-19 11:11.
- Side lane (Claude, Opus), feed 2026-10-19 11:05.
