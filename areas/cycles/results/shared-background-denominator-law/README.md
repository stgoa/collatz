---
id: shared-background-denominator-law
kind: result
title: A word built from one repeated background between nonconstant markers has denominator growing like 2^(n(e−1))
status: reviewed
claim: >
  Raw odd-only clock, any 3x+q. Let w = (U, a_0, U, a_1, …, U, a_(r−1)) with U any positive word or the
  empty word (length n, total A_U, intercept C_U), r ≥ 2 positive markers of total T, not all equal,
  and D = 2^A − 3^m > 0 (m = r(n+1), A = r·A_U + T). With P(X) = Σ_j 2^(a_0+…+a_(j−1))·X^(r−1−j),
  Q(X) = X^r − 2^T, G their monic gcd of degree d, e = r − d, R = Res(P/G, Q/G) and η = D/2^A:
  (i) q = |Qbar_h|/gcd(Qbar_h, E·Pbar_h) exactly (homogeneous evaluations at 3^(n+1)/2^(A_U),
  E = 3C_U + 2^(A_U)); (ii) e equals the number of nonzero Fourier coefficients of the marker prefix
  sequence, and every marker rotation with s > 0 mismatches has s·binom(e, 2) ≥ r; (iii)
  1 ≤ |R| ≤ r^(e(d+1))·2^(2Te) and q > η·2^(n(e−1)−d)/|R|; (iv) for fixed r, T and Q_*, only finitely
  many (U, a) have q ≤ Q_*, effectively; (v) if q = 1 and the cycle is nontrivial, then
  n < r + 4T + 2(r − 1)·log₂r + (K/log 2)(1 + log(2m)) with K = 600,000,000, so with T ≤ H·r one has
  r = Ω_H(√(m/log m)). Parts (iv) for A < 2m and (v) are conditional on the explicit Matveev bound.
  Here r counts copies of one background, not rotation mismatches.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: []
assumes: [languasco-2025-two-primes, matveev-2000-linear-forms]
lean:
  - LeanLane.Cyc.C_interleave
  - LeanLane.Cyc.D_interleave
  - LeanLane.Cyc.Ph_eq_sum
  - LeanLane.Cyc.E_bound
certificates: [c013_background_check.py]
evidence:
  - "OVERLAP_CONTROLS.md: the written proofs (sections 1-6), including both cancellation controls; OVERLAP_THEORY.md: the paired-state run law and the distance-three height family (paired-state-run-law, distance-three-height-family)"
  - "check_overlap.py, overlap_audit.json: main-lane checker and receipt. Fails at its new path: it imports HERE.parent/'C012/check_coupled_system.py'. Passed at be73a66 as experiments/cycle_spectrum/C013/check_overlap.py (about 26 s; archive/legacy-checker-run-be73a66.md)"
  - "c013b_run_law_check.py, c013b_run_law_check.json: side-lane check of Lean unit C013-b (12,550 agreeing runs on 77 actual cycles). Fails at the new path: it imports the side-lane helper module s1a_integer_cycle_check from its old folder reviews/side_lane/ (not part of this batch). Passed at be73a66 as reviews/side_lane/c013b_run_law_check.py; its receipt is written only when an output path is given"
  - "check_delivery.py, delivery_checks.json: historical delivery check and receipt; pinned to the historical commits that produced it. It passed until be73a66 and fails after the move, as designed"
  - "THEORY_REVIEW.md, OBSTRUCTION_REVIEW.md, EXACT_REVIEW.md, INDEPENDENT_CHECKER_REVIEW.md, ROOT_REVIEW.md: main-lane reviews; SIDE_REVIEW.md: the main lane's read of the side-lane feed; LITERATURE.md: sources and record comparison; historical_gate.json: historical finite gate (119 fields)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: c013_background_check.py
    scope: "Feed 2026-10-19 05:00, REFEREE C013 at main 1c5c19d: on 4,000 random words (60 with nontrivial polynomial cancellation) the factorisation, the exact q law, bound (3) with R computed from the Sylvester matrix, both main bounds, the uncertainty inequality and the (3,1,3,3,1,1) control. Feed 05:15: Lean C013-a VERIFIED (receipts c6222ea4…)"
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed 05:03: OVERLAP_CONTROLS.md read in full, no error; block identities, exact q law with Gauss's lemma, h | R via Bezout, the Fourier identification, the uncertainty inequality, root separation and bounds (6)-(10), and the (X + 4)²(X³ + 128) control re-derived. Lean unit C013-a verified (iteration 34)"
aliases: [C013]
tags: [cycles, rotation-distance, resultants, finiteness, conditional]
---

# A word built from one repeated background between nonconstant markers has denominator growing like 2^(n(e−1))

## Statement

Let `U` be a positive valuation word or empty (length `n ≥ 0`, total `A_U`, intercept `C_U`; `A_U = C_U = 0` if empty), `a = (a_0, …, a_(r−1))` a positive marker word, `r ≥ 2`, total `T`, and

```
w = (U, a_0, U, a_1, …, U, a_(r−1)),   m = r(n+1),   A = r·A_U + T,
u = 2^(A_U),   α = 3^(n+1),   E = 3C_U + u,
P(X) = Σ_(j<r) 2^(P_j)·X^(r−1−j)  (P_j = a_0 + … + a_(j−1)),   Q(X) = X^r − 2^T.
```

No contraction or order is assumed on `U`; repeated words are allowed in the algebra. Assume `D > 0`.

1. **Exact factor extraction.** `C_w = E·u^(r−1)·P(α/u)` and `D = −u^r·Q(α/u)` (1). With `G` the monic gcd of `P, Q` (degree `d`, `e = r − d`), `Pbar = P/G`, `Qbar = Q/G` and homogeneous evaluations `G_h = u^d·G(α/u)`, `Pbar_h = u^(e−1)·Pbar(α/u)`, `Qbar_h = u^e·Qbar(α/u)` (integers): `q = |Qbar_h|/gcd(Qbar_h, E·Pbar_h)` (2). With `R = Res(Pbar, Qbar) ≠ 0` and `h = gcd(Qbar_h, Pbar_h)`: `h | R` and `q ≥ |Qbar_h|/(E·|R|)` (3).
2. **Fourier support.** With `θ = 2^(T/r)` and `x_j = 2^(P_j)·θ^(−j)` (period `r`), `e` is the number of nonzero Fourier coefficients of `x` (4); `e = 1` iff the markers are constant, so nonconstant markers have `e ≥ 2`. Every marker shift with `s > 0` mismatches satisfies `s·binom(e, 2) ≥ r` (5) (not the stronger, unproved `s·e ≥ r`).
3. **Denominator law.** `1 ≤ |R| ≤ r^(e(d+1))·2^(2Te)` (7), and with `η = D/2^A`,

```
q > η·2^(n(e−1)−d)/|R| ≥ η·2^(n(e−1)−d)/(r^(e(d+1))·2^(2Te)).            (10)
```

4. **Bounded-denominator finiteness.** For fixed `r`, `T` and `Q_*`, only finitely many `(U, a)` with nonconstant `a`, `D > 0` and `q ≤ Q_*` exist; the bound is effective, `U` varies freely. Constant markers are excluded (the word is then a repetition of one block).
5. **Restriction at `q = 1`.** If the represented rational cycle has `q = 1`, the markers are nonconstant and the primitive cycle is nontrivial, then `A < 2m` and

```
n < r + 4T + 2(r − 1)·log₂r + (K/log 2)·(1 + log(2m)),   K = 600,000,000;      (13)
```

so for representations with `T ≤ H·r` (fixed `H ≥ 1`), `r = Ω_H(√(m/log m))` (14).

**Inputs.** Part 4 in the branch `A < 2m`, and part 5, use the explicit Matveev bound of [`languasco-2025-two-primes`](../../../../sources/languasco-2025-two-primes.md) (the form of [`matveev-2000-linear-forms`](../../../../sources/matveev-2000-linear-forms.md)): `log η > −K(1 + log(2m))` for `A < 2m`. Parts 1–3 are elementary.

## Proof

Written proof: [`OVERLAP_CONTROLS.md`](OVERLAP_CONTROLS.md) §§1–4 (legacy text, summarised). (1): each block `(U, a_j)` has the same affine numerator `αx + E`, divided by `u·2^(a_j)`. (2): monic Gauss lemma. (3): the integral Bezout identity for `R`, evaluated at `α/u` and cleared, gives an integer combination of `Pbar_h, Qbar_h` equal to `R·u^N`; `h` divides `D`, which is prime to 6, so `h | R`. (4): `P(θζ^k) = θ^(r−1)·ζ^(k(r−1))·Σ_j x_j·ζ^(−kj)` at the roots of `Q`. (5): the sequence `y_j = x_(j+k+1)·x_j − x_(j+k)·x_(j+1)` has ordinary support `s` and Fourier support at most `binom(e, 2)`; Cauchy–Schwarz and Parseval give (support)·(Fourier support) ≥ `r`. (7): roots of `Q` have modulus `θ`, separation at least `4θ/r`, and `|P(β)| ≤ r·2^(2T)`. (8)–(10): `C_U ≤ (u/2^n)(3^n − 2^n)`, `E < u·α/2^n`, then (3) and (6). Finiteness: with `R_0 = r^(r²)·2^(2Tr)`, `C_0 = 2^(3−r)/R_0`, (9) gives `q > C_0·η·2^n`; if `A ≥ 2m`, `η ≥ 1/4` bounds `n`; if `A < 2m`, the Matveev input gives `q > C_0·exp[n·log 2 − K(1 + log(2r(n+1)))]`, whose exponent tends effectively to infinity; once `n` is bounded, `A_U` is bounded in each branch. (13): from (10) with `d = r − e`, dividing by `e − 1` and using `e ≥ 2`, `d ≤ r − 2`; (14): `m < C_H·r²·log m`.

## Certificates

- [`c013_background_check.py`](c013_background_check.py) (about 2 s; side lane, independent code, fixed seed): on 4,000 random words with background length ≤ 8, 2–6 nonconstant markers and `D > 0` (60 with nontrivial polynomial cancellation, `deg G` from 1 to 3): (1), the exact law (2), bound (3) with `R` from the Sylvester matrix, both forms of (10), the uncertainty inequality (5), and the `(3,1,3,3,1,1)` control `G = X + 4`. It rewrites [`c013_background_check.json`](c013_background_check.json) identically.

## Lean

Not `formal`. Lean unit C013-a (`lean/CycleSpectrum.lean`, legacy `lean/STATE.md`, iteration 34; axioms `propext`, `Classical.choice`, `Quot.sound`, the identities `propext` only) formalises the exact skeleton: `C_interleave` (`C_w = (3C_U + 2^(A_U))·P_h`), `D_interleave` (`D_w = 2^(T + r·A_U) − 3^(r(n+1))`), `Ph_eq_sum` (the closed form of the homogenised `P_h`) and `E_bound` ((8): `2^n·E ≤ u(3^(n+1) − 2^(n+1))`). Not Lean targets: the polynomial gcd and resultant steps (2)–(3), the Fourier–uncertainty inequality (5), the bounds (6)–(14) and the Matveev input. The growth law itself rests on the written proof.

## Remarks

- **Two cancellation controls.** The primitive marker word `(3,1,3,3,1,1)` has `P = (X + 4)²(X³ + 128)`, `Q = X^6 − 4096`, `G = X + 4`, `e = 5`: polynomial cancellation is not merely a repetition effect (this marker has a two-defect rotation by three, so its interleavings lie in the class of [`two-defect-rotation-exclusion`](../two-defect-rotation-exclusion/README.md)). Conversely, the actual `q = 5` cycle of period 17 and minimum 347, word `(1,1,1,1,3,1,1,1,1,2,2,4,1,2,1,2,2)`, `m = 17`, `A = 27`, `C = 352,383,011`, `D = 5,077,565`, has `G = 1` (`X^17 − 2^27` is irreducible since `gcd(17, 27) = 1`) but `gcd(C, D) = 1,015,513`: polynomial coprimality does not prevent numerical cancellation, so the resultant and `E` factors cannot be dropped (data in [`mechanical_blocks_audit.json`](../rotation-block-exclusion/mechanical_blocks_audit.json)).
- **Scope.** `r` counts copies of one identical shared background, not mismatches with a rotation; a general sparse-rotation word need not have this representation, and even within the class its mismatch count may be smaller than `r`. So this does not establish [`rotation-distance-growth`](../../questions/rotation-distance-growth.md). Finite `q = 1` exceptions at fixed `r, T` are not excluded. The constants are effective but large; no practical cutoff is claimed.
- **Coverage limits** (unreviewed C014 draft): a word of prime period has no such representation with nonempty `U` and nonconstant markers, under any cut or repetition ([`compatible-arcs-common-partition-limits`](../compatible-arcs-common-partition-limits/README.md)).
- **Related.** The paired-state run law of the same batch: [`paired-state-run-law`](../paired-state-run-law.md); the height obstruction: [`distance-three-height-family`](../distance-three-height-family.md). The side lane's S11 (legacy `experiments/cycle_spectrum/S11/`, not yet migrated) replaces Matveev by the replayed gap EXT-1 ([`musson-collatz-gap-all`](../../../../sources/musson-collatz-gap-all.md)), making (14) effective: about 46,000–61,000 background copies at the period import (feed 2026-10-19 14:57).
- **Evidence labels.** The legacy report calls its stored successes and a bounded structured probe of the candidate [`rotation-defect-denominator-candidate`](../../questions/rotation-defect-denominator-candidate.md) "nondiscriminating"; the unreviewed C014 draft disputes that label (see the question node).
- **Controls.** Actual `q = 5, 7, 13` cycles keep their true reduced denominators; no rescaling to additive 1 is treated as an integer cycle. Constant markers and repetitions of `(2)` are outside part 4.
- **Novelty.** None claimed; structural restriction and effective finiteness in a specified class, no universal record.

## History

- Migrated from `experiments/cycle_spectrum/C013/` (legacy ID `C013`; `REPORT.md`, proof `OVERLAP_CONTROLS.md`) at commit `be73a66`, by the B04 migration (Claude, Opus 5.5). The side-lane checks `reviews/side_lane/c013_background_check.{py,json}` and `c013b_run_law_check.{py,json}` moved here. All C013 scripts, receipts and notes stay in this folder. Parts became [`paired-state-run-law`](../paired-state-run-law.md) and [`distance-three-height-family`](../distance-three-height-family.md).
- Main lane (ChatGPT/Codex), 2026-10-19, main commit `1c5c19d`. A Lean-lane remark about an extra `log 2` loss in the Matveev step (feed 04:14–04:15) was checked against the source: Theorem 2.1 is stated for the product-minus-one form, so no change was needed (feed 05:00).
- **Link repair in pinned notes (2026-10-19, B04 migration).** `OVERLAP_CONTROLS.md`, `THEORY_REVIEW.md` and `LITERATURE.md` linked to `../C011/` and `../C005/` legacy paths; only those link targets were repointed. Their SHA-256 values pinned in `delivery_checks.json` and the review notes (`66d6b4ee…`, `1ae516a5…`, `ce5a52ae…`) describe the `be73a66` versions; `check_delivery.py` no longer runs after the move anyway. No mathematical text changed.
