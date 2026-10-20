---
id: two-defect-rotation-exclusion
kind: result
title: No nontrivial 3x+1 cycle has a rotation differing from it in exactly two positions (ρ ≥ 3)
status: reviewed
claim: >
  Raw odd-only clock, no absorption. If a positive valuation word w of length m with total A and
  D = 2^A − 3^m > 0 has a nonidentity cyclic rotation differing from w in exactly two positions, then
  its reduced denominator q = D/gcd(C_w, D) is greater than 1, with no bound on period, state height,
  valuation alphabet, mismatch amplitude, arc lengths or shift gcd. Equivalently, the primitive word
  of every nontrivial integer cycle of the odd-only 3x+1 map differs from each of its nonidentity
  rotations in at least three positions (ρ(w) ≥ 3). Conditional on the explicit Matveev bound in
  the Languasco–Luca–Moree–Togbe form and on the period bound m > 1.375·10^11 from Hercher (2023)
  with Barina's verification below 2^71; neither computation was rerun here.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [two-defect-cancellation-bound]
assumes: [languasco-2025-two-primes, matveev-2000-linear-forms, hercher-2023-cycle-length, barina-2025-convergence-2-71]
lean:
  - LeanLane.Cyc.two_defect_q_bound
certificates: [check_exclusion_constants.py, c011_two_defect_check.py]
evidence:
  - "EXCLUSION.md: the written proof of the exclusion with its published inputs (sections 2-5); ROTATION_DEFECTS.md: the two-arc theorem, finiteness, adjacent classification and marker family; DEFECT_OBSTRUCTIONS.md: the 1^t 2^(2t) counterfamily; GENERAL_DEFECTS.md: the coupled-difference identity and the q = 97, 233, 359 controls"
  - "check_rotation_defects.py, rotation_defect_audit.json: main-lane checker and receipt (27,646 rotations, 1,481,154 word positions, 192 two-defect rotations with 384 oriented arc identities, 108 eligible actual cycles of which 22 have unit-amplitude two-defect rotations; 51 cancellation-family examples, twelve moduli, nineteen repetition controls, eight marker cases with 1,020 exact arrows). Fails at its new path: it imports HERE.parent/'C009/check_excursions.py'. Passed at be73a66 as experiments/cycle_spectrum/C011/check_rotation_defects.py (archive/legacy-checker-run-be73a66.md)"
  - "check_coupled_defects.py, coupled_defect_controls.json: main-lane check of the q = 97, 233, 359 coupled controls. Fails at its new path: it loads the corpus as HERE.parent/'C001/actual_cycles.json'. Passed at be73a66 as experiments/cycle_spectrum/C011/check_coupled_defects.py"
  - "check_delivery.py, delivery_checks.json: historical delivery check and receipt; pinned to the historical commits that produced it, fails at HEAD by design (it failed at be73a66 too)"
  - "exclusion_constants.json: receipt of check_exclusion_constants.py; c011_two_defect_check.json: receipt of the side-lane check"
  - "ARITHMETIC_REVIEW.md, INDEPENDENT_REVIEW.md, EXACT_CHECKER_REVIEW.md, ROOT_REVIEW.md: main-lane reviews; SIDE_REVIEW.md: the main lane's read of the side-lane feed; LITERATURE.md: primary-source audit of the published inputs; historical_gate.json: historical finite gate"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: c011_two_defect_check.py
    scope: "Feed 2026-10-19 04:08, REFEREE C011 at main b896512: on every primitive positive word with D > 0, length ≤ 9 and letters 1-5 (20,431 words, 33,360 two-defect rotations): swapped pair, den > 1, the two quadratic bounds in exact integer form; marker family r = 2..6; cancellation counterfamily t ≤ 60. The imported Matveev and Hercher/Barina inputs were not rerun; only their endpoint compatibility is checked. Feed 11:49: two web searches found no prior exclusion of this class (calibration only)"
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed 04:14: ROTATION_DEFECTS.md, EXCLUSION.md and GENERAL_DEFECTS.md read in full, no error; the swap structure, two-arc identity, (5)-(9), the finiteness argument, the adjacent classification, the marker family, all controls and every numerical constant of EXCLUSION.md section 4 (K_0, 2.45e9, 373/2750) re-derived. Lean unit C011-a verified (iteration 32)"
    link: ../../../../archive/side-lane/FEED.md
aliases: [C011]
tags: [cycles, rotation-distance, two-defect, exclusion, conditional]
---

# No nontrivial 3x+1 cycle has a rotation differing from it in exactly two positions (ρ ≥ 3)

## Statement

Let `w` be a positive valuation word of length `m`, total `A`, `D = 2^A − 3^m > 0`. If some nonidentity cyclic rotation of `w` differs from `w` in exactly two positions, then

```
q = D/gcd(C_w, D) > 1.
```

There is no bound on the period, state height, valuation alphabet, mismatch amplitude, arc lengths or shift gcd. Equivalently, every hypothetical nontrivial integer Collatz cycle has at least three mismatches with every nonidentity rotation of its primitive valuation word: `ρ(w) ≥ 3`, in the notation of [`conventions/NOTATION.md`](../../../../conventions/NOTATION.md). A rotation cannot differ in exactly one position, and a primitive word not in zero; three is not ruled out (for alphabets with at least three letters a rotation distance can be odd).

Two mismatches force primitivity ([`two-defect-cancellation-bound`](../two-defect-cancellation-bound.md)), so repetitions of the trivial word `(2)` lie outside the hypothesis and keep denominator 1.

**Inputs (conditional).** The proof imports two published results, neither rerun here:

1. **Explicit linear form** ([`languasco-2025-two-primes`](../../../../sources/languasco-2025-two-primes.md), the positive rational form of [`matveev-2000-linear-forms`](../../../../sources/matveev-2000-linear-forms.md)): with bases 2, 3, exponents `−A, m`, field degree one, for `B ≥ max(A, m)`,

```
log(1 − 3^m/2^A) > −K_0(1 + log B),   K_0 = 1.4·30^5·2^(9/2)·log 2·log 3 < 600,000,000.     (1)
```

2. **Period bound** ([`hercher-2023-cycle-length`](../../../../sources/hercher-2023-cycle-length.md), Corollary 29 and Remark 30, with [`barina-2025-convergence-2-71`](../../../../sources/barina-2025-convergence-2-71.md): verification below `2^71` contains Hercher's endpoint `3·2^69`): a nontrivial integer cycle has

```
m > M = 137,500,000,000.                                                    (2)
```

Hercher's `K` counts odd members and equals our `m`; his `m` counts local minima. The corrigendum repairs Theorem 21; Corollary 29 uses the separate Lemma 26 method.

## Proof

Written proof: [`EXCLUSION.md`](EXCLUSION.md) §§3–4 (legacy text, lightly edited), on top of [`two-defect-cancellation-bound`](../two-defect-cancellation-bound.md).

With `g = gcd(C_w, D)` and the two exchanged entries `a, a + k`, the elementary bound is `g² < (2^k − 1)²·2^(A−m−k)·3^m`; since one entry is at least `k + 1` and all others are positive, `k ≤ A − m`, so

```
g² < 2^(A−m+k)·3^m ≤ 2^(2A−2m)·3^m,      q > (1 − 3^m/2^A)·(2/√3)^m.        (4)
```

Suppose `q = 1`. Primitivity makes the integer cycle nontrivial; every odd state is at least 3, and multiplying the exact arrows gives `2^A = Π(3 + 1/n_i) < 4^m`, so `A < 2m`. Apply (1) with `B = 2m`, then (4):

```
log q > F(m) = m·log(2/√3) − 600,000,000·(1 + log(2m)).                     (5)
```

Rational certificates: `√2 < 10/7`, `log 2 < 7/10`, `log 3 < 11/10` give `K_0 < (7/5)·30^5·16·(10/7)·(7/10)·(11/10) = 598,752,000`; `log(4/3) = 2·atanh(1/7) > 2/7` gives `log(2/√3) > 1/7 > 7/50`; positive Taylor terms give `exp(27) > 2M`, so `log(2M) < 27`. At the boundary,

```
F(M) > (7/50)·M − 600,000,000·28 = 2,450,000,000 > 0,                        (6)
F'(m) = log(2/√3) − 600,000,000/m > 7/50 − 6/1375 = 373/2750 > 0  (m ≥ M).   (7)
```

So (2) implies `log q > 0`, contradicting `q = 1`. QED.

## Certificates

- [`check_exclusion_constants.py`](check_exclusion_constants.py) (under a second): checks the rational estimates `K_0 < 598,752,000`, the boundary margin 2,450,000,000, the derivative bound `373/2750` and the endpoint containment, and compares with [`exclusion_constants.json`](exclusion_constants.json). It does not replay the imported theorem or computations.
- [`c011_two_defect_check.py`](c011_two_defect_check.py) (about 30 s; side lane, independent code): the theorem's elementary core on every primitive positive word with `D > 0`, length ≤ 9 and letters 1–5 (20,431 words with a two-defect rotation, 33,360 rotations: swapped pair, `den > 1`, `g² < (2^k − 1)²·2^(A−m−k)·3^m`, `den > (1 − 3^m/2^A)(2/√3)^m` in exact integer form); the marker family for `r = 2..6`; the `1^t 2^(2t)` counterfamily for `t ≤ 60`. It rewrites [`c011_two_defect_check.json`](c011_two_defect_check.json) identically.

## Lean

Not `formal`. The elementary core is Lean unit C011-a (see [`two-defect-cancellation-bound`](../two-defect-cancellation-bound.md)); `LeanLane.Cyc.two_defect_q_bound` is `D²·2^(2m) < q²·2^(2A)·3^m`, the cleared form of (4), in the two-defect normal form. The step to `q = 1` uses (1) and (2), which are not Lean targets here. Separately, the side lane's S06 ([`two-mismatch-exclusion-via-gap`](../two-mismatch-exclusion-via-gap/README.md)) re-derives this exclusion without Matveev from the replayed linear-form gap EXT-1 ([`musson-collatz-gap-all`](../../../../sources/musson-collatz-gap-all.md)) for `m ≥ 24,891` and minimum `> 2^71`; its Lean units S6-b/c were verified (feed 2026-10-19 12:35), formal given the gap and the period input.

## Remarks

- **Scope.** The first exclusion in the programme defined by a property of the whole word, with no block decomposition assumed. The class is thin: a typical word differs from every rotation in many places. It says nothing about words with `ρ ≥ 3` (see [`rotation-distance-growth`](../../questions/rotation-distance-growth.md)) or about divergence. No universal numerical cycle record is improved.
- **Controls.** The actual cycles at `d = 5, 7, 13` include two-defect words and are allowed: (4) constrains their actual reduced denominators, and the period input (2) applies only to integer cycles at parameter 1. Real `3x+d` cycles with such words have `den = d` above the bound; the `q = 35` and `q = 505` controls confirm that extra reduced-denominator factors in rotation gcds are retained. Without (2) the argument gives the exclusion for `m ≥ M` only.
- **An unconditional subfamily.** [`two-defect-marker-family`](../two-defect-marker-family.md) proves `q > 1` for an explicit infinite family with growing minimum and growing shortcut local-minimum count, without (1) or (2).
- **Related.** Bounded-denominator finiteness of the class: [`two-defect-bounded-denominator-finiteness`](../two-defect-bounded-denominator-finiteness.md). Why counting mismatches alone fails: [`fixed-defect-unbounded-cancellation`](../fixed-defect-unbounded-cancellation.md). Why the proof does not extend term by term: [`termwise-plateau-divisibility`](../../attempts/termwise-plateau-divisibility.md).
- **Literature and novelty.** Words at Hamming distance two from a conjugate are an established combinatorial object (Gabrić, "Words that almost commute", read for definitions; [`LITERATURE.md`](LITERATURE.md)). The side lane's two web searches (feed 11:49) found no prior exclusion of near-periodic two-defect cycle words; two-defect words can have about `m/3` local minima, so fixed-local-minimum results ([`simons-2005-m-cycles`](../../../../sources/simons-2005-m-cycles.md)) do not cover the class. A Lean-lane suggestion that the class is already covered by the k-cycle literature was withdrawn (feed 11:47 dispute, resolved 11:59). Novelty undetermined.
- **A precision remark, resolved.** The Lean lane noted (feed 04:14) that Matveev's bound is usually stated for the linear form itself, while (1) is displayed for `log(1 − e^(−δ))`, at a cost of at most `log 2`. The main lane checked the cited source: Theorem 2.1 bounds the product-minus-one form directly, so no conversion is needed (recorded in C013's audit and the source node).

## History

- Migrated from `experiments/cycle_spectrum/C011/` (legacy ID `C011`; `REPORT.md`, proof `EXCLUSION.md`) at commit `be73a66`, by the B04 migration (Claude, Opus 5.5). The side-lane check `reviews/side_lane/c011_two_defect_check.{py,json}` moved here. All C011 scripts, receipts and notes stay in this folder. Parts became [`two-defect-cancellation-bound`](../two-defect-cancellation-bound.md), [`two-defect-bounded-denominator-finiteness`](../two-defect-bounded-denominator-finiteness.md), [`two-defect-marker-family`](../two-defect-marker-family.md), [`fixed-defect-unbounded-cancellation`](../fixed-defect-unbounded-cancellation.md) and [`termwise-plateau-divisibility`](../../attempts/termwise-plateau-divisibility.md).
- Main lane (ChatGPT/Codex), 2026-10-19, main commit `b896512`. The first draft used a weaker arc bound and proved only `k ≤ m/6` exclusion from an older published period lower bound; retaining the terminal valuations improved the range, then `k ≤ A − m` removed amplitude from the estimate altogether. The earlier valid weaker draft is superseded; no C001–C010 theorem was changed.
- **Link repair in pinned notes (2026-10-19, B04 migration).** `ROTATION_DEFECTS.md`, `DEFECT_OBSTRUCTIONS.md` and `LITERATURE.md` linked to `../C004/`, `../C006/`, `../C002/`, `../C001/` legacy paths, which were repointed to the migrated notes; the R71 link in `ROTATION_DEFECTS.md` §4 (to `experiments/residual_progress/lattice_cycles/BALANCED_DENOMINATORS.md`, not yet migrated) became that path in a code span. Their SHA-256 values pinned in `check_delivery.py`, `delivery_checks.json` and the review notes (`9b390b7f…`, `a769a6a5…`, `7f617777…`) describe the `be73a66` versions; `check_delivery.py` already fails by design. No mathematical text changed.
