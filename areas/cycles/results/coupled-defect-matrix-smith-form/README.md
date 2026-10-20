---
id: coupled-defect-matrix-smith-form
kind: result
title: "The coupled mismatch-cut system has determinant ±D^(s−2)·Π(β'_i − β_i) and only two independent congruences"
status: reviewed
claim: >
  Raw odd-only clock. Let w be a positive word with D = 2^A − 3^m > 0, g = gcd(C_w, D), and v a
  rotation differing from w in s ≥ 2 positions. Cutting both words after every mismatch gives paired
  blocks with common intercepts c_i, and the full-word intercepts satisfy X = W·c, Y = W'·c with
  integer matrices W = D·B^(−1), W' = D·B'^(−1) (B, B' the cyclic block matrices), so g | (M·c)_i
  with M = W' − W. Then |det M| = D^(s−2)·Π_i|β'_i − β_i| (β_i = 2^(B_i) the block weights), every
  k×k minor of M is divisible by D^max(k−2, 0), and at every prime p | D not dividing any β'_i − β_i
  the p-local Smith form of M is diag(1, 1, D, …, D); for unit-amplitude mismatches this holds over
  Z[1/6]. So adjugate elimination gives only g | det(M)·c_i, automatic for s ≥ 3, and modulo any
  g > 1 the system reduces to exactly two independent congruences. The primitive words
  (1^t 2^(2t))^(r−1) 1^t 2^(3t) (r ≥ 2) realise every even s = 2r with |det M| = 2^(A−r)·D^(2r−2), and
  for every M_0 coprime to 6 some t gives M_0 | g. No bound on g or q is claimed.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [two-defect-cancellation-bound]
certificates: [c012_candidate_check.py]
evidence:
  - "COUPLED_SYSTEM.md: the written proofs (sections 1-7); COUPLED_OBSTRUCTIONS.md: the three-defect family, S-unit escape and counting theorem (three-defect-arbitrary-background)"
  - "check_coupled_system.py, coupled_system_audit.json: main-lane checker and receipt (all 27,646 nonidentity rotations of the 1,185 normalised cycles and 11 fixtures; selected determinants and minors). Fails at its new path: it imports HERE.parent/'C009/check_excursions.py'. Passed at be73a66 as experiments/cycle_spectrum/C012/check_coupled_system.py (about 98 s; archive/legacy-checker-run-be73a66.md)"
  - "check_shared_arcs.py, shared_arc_audit.json: main-lane shared-arc checker and receipt (350 fixed-total backgrounds, 3,582 backgrounds with A < 2m, seven prime sets; 177,288 raw arrows, 173,349 rotations). Fails at its new path because it imports check_coupled_system.py, which fails. Passed at be73a66 as experiments/cycle_spectrum/C012/check_shared_arcs.py"
  - "check_delivery.py, delivery_checks.json: historical delivery check and receipt; pinned to the historical commits that produced it, fails at HEAD by design (it failed at be73a66 too)"
  - "c012_candidate_check.json: receipt of the side-lane candidate check"
  - "EXACT_REVIEW.md, INDEPENDENT_CHECKER_REVIEW.md, INDEPENDENT_THEORY_REVIEW.md, ROOT_REVIEW.md: main-lane reviews; SIDE_REVIEW.md: the main lane's read of the side-lane feed; LITERATURE.md: literature scope; historical_gate.json: historical finite gate"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed 2026-10-19 04:45 (in the C012 referee entry) and 04:44: COUPLED_SYSTEM.md read by hand, no error; block identities, det B = det B' = ±D, |det M| = D^(s−2)·Π|β'_i − β_i|, divisibility of every k-minor by D^(k−2), the local Smith form, the family w_(r,t) with the example (1,2,2,1,2,2,2) and det = −2^10·1909² checked"
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: c012_candidate_check.py
    scope: "Feed 04:35, REFEREE C012 at main de7db67: obstructions confirmed as stated (all-cut elimination vacuous for s ≥ 3); the corrected formula C(k, 2^n) and the distance-three family reproduced; candidate tested separately (rotation-defect-denominator-candidate)"
aliases: [C012]
tags: [cycles, rotation-distance, smith-form, rejected-mechanism]
---

# The coupled mismatch-cut system has determinant ±D^(s−2)·Π(β'_i − β_i) and only two independent congruences

## Statement

Let `w = (a_0, …, a_(m−1))` be a positive word, `A = Σa_i`, `D = 2^A − 3^m > 0`, `g = gcd(C_w, D)`, `q = D/g`, and `v` a cyclic rotation of `w` differing in exactly `s` positions; `s ≥ 2` since totals agree. Repeated words are allowed when the rotation is nontrivial; repetitions of `(2)` are not discarded.

**Objects.** Cut both words just after every mismatch: paired blocks `(u_i, u'_i)`, `0 ≤ i < s`, with equal interiors and different last letters. Put `ℓ_i = len(u_i)`, `α_i = 3^(ℓ_i)`, `β_i = 2^(B_i)`, `β'_i = 2^(B'_i)` (block totals), `δ_i = B'_i − B_i ≠ 0`, `Σδ_i = 0`, and `c_i = C_(u_i) = C_(u'_i)` (an intercept omits its last letter). Then `Πβ_i = Πβ'_i = 2^A`, `Πα_i = 3^m`, and the full intercepts `X_i`, `Y_i` at block starts satisfy `β_i·X_(i+1) − α_i·X_i = D·c_i`, `β'_i·Y_(i+1) − α_i·Y_i = D·c_i` (1). Let `B` have diagonal `−α_i` and cyclic superdiagonal `β_i` (and `B'` with `β'`), so `det B = det B' = (−1)^(s−1)·D`, and

```
W = D·B^(−1),  W' = D·B'^(−1)  (integer matrices),   X = W·c,  Y = W'·c,  M = W' − W,  Y − X = M·c.   (2)–(4)
```

`g | (M·c)_i` is exactly the coupled system of all block-cut differences, hence of all full-cut differences (inside a matching run `2^(a_j)·E_(j+1) = 3E_j`, so no further congruence is hidden).

1. **Determinant.** `|det M| = D^(s−2)·Π_i|β'_i − β_i|` (5), nonzero.
2. **Minors.** Every `k × k` minor of `M` is divisible by `D^max(k−2, 0)` (6); every reduction of `M` modulo a prime dividing `D` has rank at most 2.
3. **Local Smith form.** If `p | D` divides no `β'_i − β_i`, the `p`-local Smith form of `M` is `diag(1, 1, D, …, D)` (8). For unit-amplitude mismatches (`δ_i = ±1`) this holds over `Z[1/6]`, and modulo any divisor `g > 1` of `D` the system reduces to exactly two independent congruences on the transformed `c`.
4. **Consequence.** Multiplying the coupled congruences by `adj(M)` yields only `g | det(M)·c_i`, automatic for every `s ≥ 3` because `D | det M`: adjugate elimination is vacuous.
5. **Sharpness on actual cycles.** For `r ≥ 2`, `t ≥ 1`, the word `w_(r,t) = (1^t 2^(2t))^(r−1) 1^t 2^(3t)` has `m = (3r+1)t`, `A = (5r+2)t`, is primitive (unique longest run of twos), differs from its one-step rotation in exactly `s = 2r` positions (all amplitude one), has `2^A/3^m = ((32/27)^r·4/3)^t > 1`, and `|det M| = 2^(A−r)·D^(2r−2)` (10). For every `M_0` coprime to 6, choosing `t` with `2^t ≡ 3^t ≡ 1 (mod M_0)` gives `M_0 | g`.

## Proof

[`COUPLED_SYSTEM.md`](COUPLED_SYSTEM.md) (legacy text). (1) is concatenation; (3) of the note gives the entries of `W` explicitly. **Determinant:** `H = B' − B` is a weighted cyclic permutation matrix with weights `β'_i − β_i`, and `M = −D·B'^(−1)·H·B^(−1)`. **Minors:** from `B·W = D·I`, consecutive rows satisfy `β_i·W_(i+1,·) ≡ α_i·W_(i,·) (mod D)` with units `β_i`, so `W ≡ u·v^T (mod D)`, likewise `W'`, and `M = D·N + (u'v'^T − uv^T)` with the second term of rank at most 2; expanding a minor by multilinearity in columns gives (6). **Smith form:** modulo `p`, `B` and `B'` have rank `s − 1`, their adjugates rank 1 with distinct kernels (a common kernel vector would lie in the kernel of the invertible `H`), so `W' − W` has rank exactly 2 mod `p`; with `t = v_p(D)`, rank 2 gives `e_1 = e_2 = 0`, (6) gives `e_3 ≥ t`, and (5) gives total `(s − 2)t`. **Family:** the minimum of the two β-exponents is `B_i` for each one-run and `B_i − 1` for each two-run; `C_(1^L) = 3^L − 2^L` and `C_(2^L) = 4^L − 3^L` are divisible by `M_0` when `t | L`, and so is `D`.

**Small example.** For `r = 2`, `t = 1`: `w = (1,2,2,1,2,2,2)`, `C = 5095`, `D = q = 1909`, `g = 1`, states `(5095, 8597, 6925, 5671, 9461, 7573, 6157)`, `c = (1, 7, 1, 37)` at the four run starts, and

```
M = [    0,  162,     0,  64 ]
    [ −1024,   0,  −648,   0 ]
    [    0,  256,     0,  54 ]
    [ −864,    0, −1024,   0 ],      det M = −3,731,743,744 = −2^10·1909².
```

This first example is mechanical (already in the narrow class); it is an arithmetic calibration. For `r = 3`, `t = 2`: `m = 20`, `A = 34`, `C = 30,653,364,553`, `D = 13,693,084,783`, `g = 7`, `q = 1,956,154,969`.

## Certificates

- [`c012_candidate_check.py`](c012_candidate_check.py) (about 80 s; side lane, independent code, fixed seed): checks the corrected formula `C(k, 2^n) = 3^n + 2^k(4^n − 3^n)` for the word `(k, 2, …, 2)`; that `(1, U, 3, U, 4, U)` with `U` over `{2, 5}` is primitive with minimum rotation distance exactly 3 (300 random backgrounds); and tests the candidate of [`rotation-defect-denominator-candidate`](../../questions/rotation-defect-denominator-candidate.md) on 18,892,900 rotations of all primitive words of length ≤ 9 with letters 1–5 (0 discriminating, as predicted) and on 59,759 structured words (56,150 discriminating, no failure). It rewrites [`c012_candidate_check.json`](c012_candidate_check.json) identically. The candidate passes are finite evidence, not part of this node's claim.

## Remarks

- **Scope.** This is a proved obstruction to one elimination, not to every integer combination, smaller minors, or size estimates on the two surviving coupled forms. The determinant argument treats the block intercepts `c_i` as free variables and does not use the further constraints from their being pieces of one word and its rotation; [`three-defect-arbitrary-background`](../three-defect-arbitrary-background.md) shows those pieces can still carry arbitrary information. The family does not refute a relative bound on `g/2^A`; its denominators may grow.
- **Controls.** The two-defect theorem is the case `s = 2` (exponent of `D` zero) and loses none of its factors. The `q = 97, 233, 359` controls of [`termwise-plateau-divisibility`](../../attempts/termwise-plateau-divisibility.md) remain counterexamples to dividing individual plateau terms; the matrix keeps their coupled sums. The `q = 5, 7, 13` cycles are unaffected.
- **Relation.** It sharpens the single-lattice warning of [`rotation-lattice-single-divisibility`](../rotation-lattice-single-divisibility.md) for this elimination. Not a comparison win over published exclusions; no novelty claimed.
- **Legacy recommendation.** The batch answered a user question by recommending, as intermediate target under the all-cycle headline, a growing lower bound on rotation distance: [`rotation-distance-growth`](../../questions/rotation-distance-growth.md).

## History

- Migrated from `experiments/cycle_spectrum/C012/` (legacy ID `C012`; `REPORT.md`, proof `COUPLED_SYSTEM.md`) at commit `be73a66`, by the B04 migration (Claude, Opus 5.5). The side-lane check `reviews/side_lane/c012_candidate_check.{py,json}` moved here. All C012 scripts, receipts and notes stay in this folder. Parts became [`three-defect-arbitrary-background`](../three-defect-arbitrary-background.md), [`rotation-defect-denominator-candidate`](../../questions/rotation-defect-denominator-candidate.md) and [`rotation-distance-growth`](../../questions/rotation-distance-growth.md).
- Main lane (ChatGPT/Codex), 2026-10-19, main commit `de7db67`.
- **Link repair in pinned notes (2026-10-19, B04 migration).** `LITERATURE.md` linked to `../C004/`, `../C003/` and `../C011/` legacy paths; only those link targets were repointed. Its SHA-256 pinned in `delivery_checks.json` (`cc31b96e…`) describes the `be73a66` version; `check_delivery.py` already fails by design. No mathematical text changed.
