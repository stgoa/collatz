---
id: digit-count-invariant-colourings-constant
kind: result
title: A 3x+1 invariant colouring that depends only on the binary digit count is constant
status: reviewed
claim: >
  Let s_2(n) be the number of 1s in the binary expansion of n, C any set and F any function from the positive
  integers to C. If h(n) = F(s_2(n)) satisfies h(3n+1) = h(n) for every positive odd n > 1 (doubling invariance is
  automatic), then F, and hence h, is constant. No finiteness or periodicity assumption on F is needed. In
  particular every binary-automatic colouring G(s_2(n) mod m), for every m >= 1 and every output map G, that is
  invariant under the 3x+1 map is constant. Scope: 3x+1 only; the d = 5 and d = 61 divisibility invariants do not
  factor through s_2.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
certificates: [verify_examples.py, v003_digit_count_check.py]
evidence:
  - "digit_sum.md: the written proof (main lane); literature.md: V003's primary-literature notes L1-L6 (L5 for the cylinder rigidity, L6 for the scaling counterexample)"
  - "PROOF_REVIEW.md: main-lane independent algebra and scope review of all V003 notes; GOAL_REVIEW.md: main-lane goal-completion audit; side_review.md: the main lane's read of the side-lane feed at sidekick c583fc3"
  - "delivery_checks.json: historical delivery receipt (links, frozen-file hashes, changed files at baseline c47d91b); no script in the repository regenerates it"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: v003_digit_count_check.py
    scope: "Feed 18:46 (REFEREE V003, main 2ac44ef): 'The proof is correct and elementary'; the identity family n_k = 32(2^k - 1) + 9 checked for k = 2..3000, the sources 5, 13, 23, a union-find over odd n < 2*10^5 putting all binary weights in one class, and the 1_(5|n), 1_(61|n), Thue-Morse controls"
aliases: [V003]
tags: [invariants, colourings, digit-count, automatic, rigidity]
---

# A 3x+1 invariant colouring that depends only on the binary digit count is constant

## Statement

Let `s_2(n)` count the 1s in the binary expansion of `n`. For **any** set `C` and **any** function `F : {1, 2, …} → C`, suppose

```
h(n) = F(s_2(n)),
h(3n+1) = h(n)   for every positive odd n > 1.
```

Then `F`, and hence `h`, is constant. Doubling invariance is automatic, because multiplying by 2 appends a zero bit, so this applies to absorbed odd-only component invariants. The displayed `3n+1` is a colour identity, not a declaration of a new clock.

This simultaneously classifies every binary-automatic colouring `G(s_2(n) mod m)`, for every `m` and every output map `G` (retain the digit count modulo `m` while reading bits). That family includes nonperiodic descriptions such as digit-sum parity (Thue–Morse), so the result goes beyond the periodic baseline [`periodic-invariant-colourings-classification`](../periodic-invariant-colourings-classification/README.md). Positional and pattern information in the bits remains outside this theorem. No hypothetical nonabsorbing indicator is assumed to belong to the class.

## Proof

From [`digit_sum.md`](digit_sum.md). For every integer `k ≥ 2` put

```
n_k = 32(2^k − 1) + 9.
```

The binary blocks above and below bit 5 are disjoint, so

```
s_2(n_k) = k + 2,
3n_k + 1 = 32(3·2^k − 3) + 28.
```

For `k ≥ 2`, `3·2^k − 3 = 2^(k+1) + (2^k − 3)` has `k` one-bits: the second summand has `k − 1` one-bits and no overlap with the first. Since `28 < 32` has three one-bits, the second block decomposition gives `s_2(3n_k + 1) = k + 3`. Every `n_k` is positive, odd and greater than 1, so `F(k+2) = F(k+3)` for all `k ≥ 2`: all values at weights 4, 5, … agree. Three odd source identities connect the remaining weights:

| Source `n` | `3n+1` | `s_2(n)` | `s_2(3n+1)` |
|---|---:|---:|---:|
| 5 | 16 | 2 | 1 |
| 13 | 40 | 3 | 2 |
| 23 | 70 | 4 | 3 |

Thus `F(1) = F(2) = F(3) = F(4) = …`. Weight 0 never occurs on positive integers and is not constrained. ∎

**Thue–Morse is not eventually periodic** (so the class is genuinely beyond periodic colourings): an eventual period `M` would be global by doubling, but for `2^L > M`, `s_2(2^L − M) = L − s_2(M − 1)` has alternating parity as `L` grows, while adding `M` gives the constant weight `s_2(2^L) = 1`. Its failure of invariance is witnessed by 5: `s_2(5) = 2` but `s_2(16) = 1`.

## Certificates

- [`verify_examples.py`](verify_examples.py) (under a second): main-lane bounded replay of V003's digit, cylinder, kernel, scaling, carry and cycle examples, compared with [`verification.json`](verification.json). Finite checks only; the all-weight statement is the written proof.
- [`v003_digit_count_check.py`](v003_digit_count_check.py) (under a second; side lane, independent code): `s_2(n_k) = k + 2` and `s_2(3n_k + 1) = k + 3` for `k = 2..3000`; the sources 5, 13, 23; a union-find over every odd `n < 2·10^5` putting all binary weights in one class; the controls `1_(5|n)` (3 vs 5), `1_(61|n)` (31 vs 61) and Thue–Morse (`5 → 16`). It rewrites [`v003_digit_count_check.json`](v003_digit_count_check.json) identically.

## Remarks

**Controls.** The invariant `1_{5|n}` for `d = 5` does not factor through `s_2`: 3 and 5 both have weight 2 and different colours. For `d = 61`, 31 and 61 both have weight 5 and different divisibility colours. The `+1` identities above must not be replaced by `+d`; the controls are excluded at a named hypothesis.

**The V003 batch.** The legacy V003 report ("What arithmetic regularity has gained", 2026-10-18) delivered, besides this theorem:
- [`binary-kernel-first-ternary-image`](../binary-kernel-first-ternary-image.md): the first ternary image of a finite binary kernel adds at most the one function `h(3n)`, and the pure-zero ternary orbit is finite;
- [`scaling-invariant-character-not-eventually-periodic`](../scaling-invariant-character-not-eventually-periodic.md): an exact obstruction to dropping the guards (a binary-automatic character invariant under doubling and tripling with infinitely many mixed ternary sections, failing the full guard at 3);
- [`monochromatic-cylinder-forces-constancy`](../monochromatic-cylinder-forces-constancy.md): a known consequence, at `d = 1`, of published progression sufficiency;
- the closed carry-frontier test [`binary-ternary-carry-frontier`](../../attempts/binary-ternary-carry-frontier/README.md).

Its recommendation was to deepen V13 through the mixed ternary sections, or alternatively to seek a finite 3-Mahler relation for each colour indicator. The full binary-automatic classification was then proved in [`binary-automatic-invariant-colourings-constant`](../binary-automatic-invariant-colourings-constant/README.md) (V004), which subsumes the automatic subclass `G(s_2(n) mod m)` of this theorem (conditionally on Cobham's theorem); the general `F` here, which need not be automatic, is not subsumed. The Lean lane queued this theorem (unit 2) at low priority as subsumed by V004 and did not formalise it.

**Primary literature** ([`literature.md`](literature.md)): fixed-depth predecessor languages are regular, but the whole basin is not covered; Cobham requires two actual base descriptions; a characteristic-zero 3-Mahler equation would be another sufficient input. No exact single-base classification was located in this bounded search. Novelty undetermined.

**Side-lane calibration** (feed 18:43–18:46): by the computational verification that every `n < 2^68` reaches 1 (the side lane cites Barina; see [`barina-2025-convergence-2-71`](../../../../sources/barina-2025-convergence-2-71.md)), a `k`-state recogniser of a nonempty colour class accepts a word of length below `k`, so any nonconstant 2-automatic invariant colouring of `3x+1` needs at least 70 states; progress therefore needs structural arguments, not enumeration of small automata. (A remark, not a node.)

## History

- Migrated from `experiments/viewpoints/V003/REPORT.md` (legacy ID V003) at commit `be73a66`, by the B16 migration (Claude, Opus 5.5); the theorem and proof are from `V003/digit_sum.md`, kept here. The report's sections on the kernel lemma, the scaling obstruction, the literature and the carry test are condensed into Remarks and the linked nodes; `kernel_probe.md` and `cylinder_rigidity.md` became their own nodes and `carry_boundary.md` the attempt [`binary-ternary-carry-frontier`](../../attempts/binary-ternary-carry-frontier/README.md). The side-lane check `reviews/side_lane/v003_digit_count_check.*` moved here.
- Main lane (ChatGPT/Codex), 2026-10-18, main commit `2ac44ef`. The legacy report carried the historical note that the open classification it described was later proved in V004; its "independently agent-reviewed" label referred to main-lane review agents (`PROOF_REVIEW.md`).
- **Link repair in kept notes (B16 migration, 2026-10-20).** In `GOAL_REVIEW.md`, `PROOF_REVIEW.md`, `digit_sum.md`, `literature.md`, `side_review.md`, only link targets were changed: relative links to legacy paths now point to the corresponding nodes or to `archive/invariants-viewpoints/`. No text changed. Any `delivery_checks.json` hashes describe historical versions of these notes; no script in the repository checks them.
