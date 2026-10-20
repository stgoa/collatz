---
id: excursion-compression
kind: attempt
title: Compressing an ordered cycle at its excursions above the minimum band
status: reviewed
claim: >
  Tried, toward excluding ordered denominator-one cycles of the raw odd-only 3x+1 map: cut a primitive
  ordered cycle at each visit to its minimum dyadic band [L, 2L), compress each positive-height
  excursion by its exact affine relation, and use the excursion congruences, an induced ordered
  return map, or a drift sign to force descent or a new denominator restriction. Verdict: rejected.
  The exact block system has Smith form diag(1, …, 1, D) and gives back only D | C at q = 1; circular
  order is not inherited by the height-zero first-return map (ordered q = 13 cycle 283 → 431 → 653 →
  493 → 373, and the one-point deletion theorem); and excursions have no automatic descent sign
  (q = 13 and q = 83 controls, including a contracting excursion that rises). No cycle is excluded.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [excursion-cut-lemma, one-point-deletion-rank-shift, dyadic-order-lemma]
certificates: [check_return_order.py, c009_excursion_check.py]
evidence:
  - "EXCURSION_ARITHMETIC.md: written cut lemma, elimination, k-block Smith form and controls (sections 1-3); FIRST_RETURN_ORDER.md: the one-point deletion theorem and its q = 13 and q = 83 controls (hash-pinned by check_return_order.py's receipt)"
  - "check_excursions.py, excursions_audit.json: main-lane excursion checker and receipt (8.2 MB: 2,593 first returns, 28,831 prefix cylinders over the 1,185 normalised cycles). Fails at its new path: it loads the corpus as HERE.parent/'C001/actual_cycles.json', C007's census and experiments/phase6/cycle_fixtures.json by old path. Passed at be73a66 as experiments/cycle_spectrum/C009/check_excursions.py (archive/legacy-checker-run-be73a66.md)"
  - "check_delivery.py, delivery_checks.json: historical delivery check and receipt; pinned to the historical commits that produced it, fails at HEAD by design (it failed at be73a66 too)"
  - "INDEPENDENT_EXCURSION.md, ARITHMETIC_REVIEW.md, CHECKER_REVIEW.md, ROOT_REVIEW.md: main-lane independent argument and reviews; SIDE_REVIEW.md: the main lane's read of the side-lane feed; LITERATURE.md: literature scope; historical_gate.json: historical finite gate"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: c009_excursion_check.py
    scope: "Feed 2026-10-19 03:17, REFEREE C009 at main ec48fbd: the q = 13 cycle and its non-shift core (2,0,3,1), the deletion theorem on 13,108 cases (m ≤ 40, coprime s) and 1,770 cases without coprimality (m ≤ 60), the q = 83 excursion and the two open q = 1 paths reproduced; rejection confirmed"
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed 03:19: C009 read in full, no error; cut lemma, elimination, deletion table and every number in the q = 13, q = 83 and q = 1 controls re-derived by hand. Lean units C009-a and C009-b verified"
aliases: [C009]
tags: [cycles, dyadic-order, excursions, rejected-mechanism]
---

# Compressing an ordered cycle at its excursions above the minimum band

## Idea

After the residue route ([`height-residue-hall-matching`](../../questions/height-residue-hall-matching.md)) proved unable to reach `q = 1`, the next bounded test toward [`ordered-cycle-denominator-one`](../../questions/ordered-cycle-denominator-one.md) was to cut an ordered primitive positive odd cycle at each visit to its minimum band `[L, 2L)`, keep each positive-height excursion's exact integer affine relation `2^(A_seg)·n_exit = 3^(length)·n_entry + q·C_seg` together with the complementary path that closes the cycle, and try to obtain descent, an inherited ordered return map (for induction on height), or a denominator restriction beyond `D | C_h`. Raw odd-only clock throughout, no absorber.

## What happened

Three parts of the mechanism fail in different ways (legacy report, lightly edited).

**Exact cuts preserve the lattice but add no congruence.** For a positive valuation block with exact intercept, positive odd endpoints satisfying `2^A·y = 3^ℓ·x + q·C` already force every intermediate state to be an odd integer with the prescribed exact valuation ([`excursion-cut-lemma`](../../results/excursion-cut-lemma.md)). Closing `k` such blocks gives a cyclic integer matrix with rows `−3^(ℓ_j)·x_j + 2^(a_j)·x_(j+1) = q·C_j`, determinant `±D`, and Smith form `diag(1, …, 1, D)` (written proof, [`EXCURSION_ARITHMETIC.md`](EXCURSION_ARITHMETIC.md) §2: at a prime dividing `D`, deleting the closing row and column leaves a triangular minor that is a power of 3; the augmented maximal minors are `D` and the Cramer numerators `q·C_(i)`, with gcd `gcd(D, q·g)`). Its integrality condition at `q = 1` is the original `D | C`: the block form of the single-obstruction calculation of [`rotation-lattice-single-divisibility`](../../results/rotation-lattice-single-divisibility.md). Scaling states and parameter together by `q` leaves heights, excursion membership and sorted-rank inequalities unchanged, so cut algebra plus legal shape is exactly the original word test. Replacing the true weighted intercept by the unweighted mechanical one loses the lattice: in the `q = 13` control it sends 431 to `1985/4` instead of 493.

**Circular order is not inherited.** The exact ordered `q = 13` cycle

```
n = (283, 431, 653, 493, 373),  a = (1,1,2,2,2),  h = (0,0,1,0,0),  A = 8, m = 5
```

has sorted normalised states `283, 653/2, 373, 431, 493`, strictly increasing scaled images `862, 986, 1132, 1306, 1492`, and normalised successor shift 3 on five ranks. Deleting 653 and keeping first returns leaves the sorted core `(283, 373, 431, 493)` with successor ranks `(2, 0, 3, 1)`, not a circular shift. The general reason is [`one-point-deletion-rank-shift`](../../results/one-point-deletion-rank-shift.md): deleting one rank from a shift by `s` yields a shift only for `s = 1` or `s = m − 1`.

**Excursions have no automatic descent sign.** In the `q = 13` cycle, `431 → 653 → 493` rises (slope `9/8`). A contracting slope is not enough either: the ordered `q = 83` cycle `(157, 277, 457, 727, 283, 233, 391)` has the excursion `277 → 457 → 727 → 283` with `32·283 = 27·277 + 83·19`, slope `27/32 < 1`, yet it rises by 6. At `q = 1`, the **open paths** (not cycles) `7 → 11 → 17 → 13` and `19 → 29 → 11` show rising and falling excursions with locally increasing sorted images.

Finite evidence ([`excursions_audit.json`](excursions_audit.json)): over the 1,185 normalised cycles, 2,593 first returns and 28,831 prefix cylinders with complementary closure. In the ordered domain (51 nonfixed cycles and the `q = 1` fixed point):

| Ordered-domain observation | Count |
| --- | ---: |
| Height-zero first returns | 177 |
| Returns traversing positive height | 60 |
| Positive excursions that descend / rise | 48 / 12 |
| Positive excursions with contracting / expanding slope | 50 / 10 |
| Contracting positive excursions that rise | 2 |
| Cycles whose induced core loses circular order | 12 |

## Why it fails

The exact algebra returns the old divisibility condition, the proposed ordered induction class is not closed under compression, and local excursion shape carries no drift sign. The bounded pass reached its own pivot criterion ("if one bounded symbolic pass merely recovers `D | C_h`, pivot"). This rejects the automatic recursion and a local drift proof; it does not exclude a `q = 1`-specific argument that couples the **joint** shape and divisibility conditions, and does not decide divergence.

## What survives

- [`excursion-cut-lemma`](../../results/excursion-cut-lemma.md) (formal) and [`one-point-deletion-rank-shift`](../../results/one-point-deletion-rank-shift.md) (formal).
- The controls: the ordered `q = 13` five-cycle, the `q = 83` contracting-but-rising excursion, the `q = 5` cycle `(19, 31, 49)` under a one-excursion cut (`D = 5`, `C = 31`), and the `d = 7` cycle `(5, 11)` outside `q ≤ L`.
- The legacy next step: global integer rounding in the complete sorted-gap system, tried in [`local-odd-rounding-exclusion`](../local-odd-rounding-exclusion/README.md).
- **Payoff of the target, as recorded in the legacy report.** [`three-band-collatz-cycles-are-ordered`](../../results/three-band-collatz-cycles-are-ordered.md) says every primitive `q = 1` cycle with `H < 8L` is ordered, so excluding all nontrivial ordered integer cycles would give `H > 8L` for every nontrivial Collatz cycle (equality is impossible for odd states). This is an implication inside the repository, not a novelty claim.

## Certificates

- [`check_return_order.py`](check_return_order.py) (about 4 s): checks the deletion formula on 105,388 finite permutations through `m = 80` (6,250,510 arrows), reconstructs 16,368 positive odd endpoint pairs across `q = 1, 5, 7, 13` with 76,464 exact arrows (constructed paths, not counted as cycles), and replays the two actual controls; it recomputes and compares its receipt [`return_order_audit.json`](return_order_audit.json), which pins `FIRST_RETURN_ORDER.md` by SHA-256.
- [`c009_excursion_check.py`](c009_excursion_check.py) (under a second; side lane, independent code): the `q = 13` cycle and its non-shift core, the deletion theorem for `3 ≤ m ≤ 40`, the `q = 83` excursion and the open `q = 1` paths; it rewrites [`c009_excursion_check.json`](c009_excursion_check.json) identically.

## History

- Migrated from `experiments/cycle_spectrum/C009/` (legacy ID `C009`; `REPORT.md`, notes `EXCURSION_ARITHMETIC.md`, `FIRST_RETURN_ORDER.md`) at commit `be73a66`, by the B04 migration (Claude, Opus 5.5). The side-lane check `reviews/side_lane/c009_excursion_check.{py,json}` moved here. All C009 scripts, receipts and notes stay in this folder. Parts became [`excursion-cut-lemma`](../../results/excursion-cut-lemma.md) and [`one-point-deletion-rank-shift`](../../results/one-point-deletion-rank-shift.md).
- Main lane (ChatGPT/Codex), 2026-10-19, main commit `ec48fbd`. The side lane called it "a well-run negative result" (feed 03:17).
- **Link repair in pinned notes (2026-10-19, B04 migration).** `EXCURSION_ARITHMETIC.md` and `LITERATURE.md` linked to `../C004/` and `../C001/` legacy paths; only those link targets were repointed. Their SHA-256 values pinned in `check_delivery.py`, `delivery_checks.json` and the review notes (`7d4a0f74…`, `ee6fd4f8…`) describe the `be73a66` versions; `check_delivery.py` already fails by design. No mathematical text changed.
