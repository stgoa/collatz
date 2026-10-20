---
id: height-bound-via-residues-or-relaxation
kind: attempt
title: Proving B ≤ q − 1 from disjoint height residues or from real order inequalities
status: reviewed
claim: >
  Tried, toward the candidate B ≤ q − 1 for ordered cycles: (i) states in different height bands
  occupy disjoint residue classes mod q, so B + 1 ≤ φ(q); (ii) real order inequalities, correct
  heights and positive exponents force the integer conclusion; (iii) the pairwise min–top inequality
  bounds B. Verdict: all three fail. (i) The ordered q = 5 period-17 cycle from 187 has raw residue 2
  at all four heights 0-3. (ii) The ordered q = 5 cycle from 347 divided by 5 satisfies all real
  circle conditions with additive term 1 and B = 3, yet its reduced denominator is 5. (iii) The
  pairwise inequality is compatible with q ≤ L for every B ≥ q. None is a counterexample to the candidate.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [ordered-cycle-residue-law]
evidence:
  - "../questions/height-denominator-candidate/HEIGHT_DENOMINATOR.md, sections 2-3; INDEPENDENT_ARITHMETIC.md: the written obstructions"
  - "../questions/height-denominator-candidate/arithmetic_obstructions.json: residue control, rational-rescaling control and 99 relaxed pair checks (historical receipt)"
  - "../questions/height-denominator-candidate/c007_height_check.py, part (4): side-lane check of the q = 5 residues"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    scope: "Feed 2026-10-19 02:28, REFEREE C007: the ordered q = 5 cycle from 187 has raw residue 2 at heights 0, 1, 2 and 3 (residue sets {2,3}, {2,3}, {1,2,3}, {1,2,3,4}); the two exact obstructions judged valuable and neither a counterexample to the law"
    link: ../../../archive/side-lane/FEED.md
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed 02:41, update 02:53: the Lean lane's read of C007 found no error (modular lemma, min-to-top inequality, q = 5 height-residue sets)"
    link: ../../../archive/side-lane/FEED.md
tags: [cycles, residues, dyadic-order, relaxation]
---

# Proving B ≤ q − 1 from disjoint height residues or from real order inequalities

## Idea

For the candidate [`height-denominator-candidate`](../questions/height-denominator-candidate/README.md), three cheap routes: (i) inject height levels into disjoint residue classes mod `q` (all residues are units, so `B + 1 ≤ φ(q)`); (ii) derive the bound from the real circle inequalities of an ordered cycle alone; (iii) bound `B` from the ordered min–top inequality `3(n_i − 2^B·L) > q(2^B − 1)`.

## What happened

- **(i) Residue injection.** By the modular lemma of [`ordered-cycle-residue-law`](../results/ordered-cycle-residue-law.md), for fixed normalised word `c` the residue orbit loses the height profile entirely. In the exact ordered `q = 5`, period-17 cycle beginning `(187, 283, 427, 643, 967, 1453, 1091, 1639, 2461, 1847, 2773, 2081, 781, 587, 883, 1327, 1993)`, the sets `n_i mod 5` by height are `{2,3}`, `{2,3}`, `{1,2,3}`, `{1,2,3,4}` for heights 0–3: residue 2 occurs at every level. Normalised residues also overlap between levels.
- **(ii) Real order inequalities.** Take the actual primitive ordered `q = 5` cycle from 347, numerators `(347, 523, 787, 1183, 1777, 667, 1003, 1507, 2263, 3397, 2549, 1913, 359, 541, 407, 613, 461)`, `B = 3`. Dividing every state by 5, the rational states `x_i = n_i/5` satisfy `3x_i + 1 = 2^(a_i)·x_(i+1)` with the same positive valuation word, dyadic heights, successor rank order and `B = 3`, and minimum `347/5 > 1`. Its reduced denominator stays 5; the rescaled points are not odd integers and the first cleared circular gap is `96/5`.
- **(iii) Pairwise relaxation.** For `B ≥ q`, (3) is compatible with `q ≤ L`: `r` of order `q·2^B/3` satisfies the lower bound while the upper bound permits values of order `L·2^B`. The C006 zero-forcing estimate has exponent `ceil(m/J) − 1 − B`, which also gives no bound of the form `B < q` when `J` is large.

## Why it fails

(i) The full residue sets at different heights need not be disjoint. (ii) Any proof using only normalised order, the height coboundary and real positivity would also apply to the rational rescaling of the `q = 5` cycle, so it must use integer-lattice data (`G_j = 2^B·Δ_j ∈ Z_(>0)` for reduced numerator coordinates) or the full weighted test `D·L = q·C_h`, `q = D/gcd(C_h, D)`, which distinguish reduced `q = 1` from reduced `q = 5`. (iii) A pairwise test discards the coupling of all rank inequalities.

## What survives

- Overlap refutes disjointness but **not** a system of distinct representatives: the `q = 5` raw sets admit `0 → 2, 1 → 3, 2 → 1, 3 → 4`, and all 1,184 tested `q > 1` cycles admit such matchings ([`ordered-cycle-height-census`](../results/ordered-cycle-height-census.md), Remarks). A universal matching theorem for ordered cycles is an open sufficient mechanism (it would give `B + 1 ≤ φ(q)`); `q = 1` is untested.
- Any proof must couple `D | C_h` with integrality and all rank inequalities at once.

## History

- Split from `experiments/cycle_spectrum/C007/` (legacy ID `C007`; `REPORT.md`, `HEIGHT_DENOMINATOR.md` §§2–3, `INDEPENDENT_ARITHMETIC.md`) at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19. Review tightened the scope before publication: repeated residues disprove disjointness of the full sets, not a choice of distinct representatives.
