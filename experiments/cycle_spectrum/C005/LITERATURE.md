# C005 — Comparison with scoped cycle results

**2026-10-19. Bounded primary-source comparison; no novelty claim.**
The mathematical proofs in [ORDER_THEORY.md](ORDER_THEORY.md) are
elementary written arguments. They do not import a new external theorem.

## What the new class permits

Fix any primitive positive mechanical valuation word with coprime totals
`(A0,m0)`. C005 allows an arbitrary finite sequence of its cyclic rotations
as full blocks. The number, order and multiplicities of those blocks are
unrestricted. The reduced denominator is greater than one unless the
base is `(2)`, which only generates the trivial cycle.

This removes the prescribed two-block order within this rotation class.
It does not contain all C002/C003 cases: those allow nonmechanical blocks.
Conversely, C005 supplies no lower bound tending to infinity with the
number of blocks, and no general bounded-denominator finiteness theorem.
The surviving condition that every block is a rotation of one common
base remains a serious coverage gap.

## A primitive family beyond fixed cutoffs

For each prime `m0>=13`, set `A0=bit_length(3^m0)` and take the lower
mechanical base. Then `m0<A0<2m0`, so the totals are coprime. Use the
six phase labels `(0,0,1,0,1,1)`, where label 1 means a one-position
cyclic rotation of the base. This phase word has no period 1, 2 or 3.
Any period of the valuation word must have length divisible by `m0`,
because its valuation/length ratio is the reduced fraction `A0/m0`.
Consequently the full word is primitive, with totals `(6A0,6m0)`.

R71 gives base minimum greater than `m0/6` and ratio less than two.
C005's prefix comparison gives every mixed-cycle state greater than
`m0/12`, without a further repetition-size condition. The primitive
totals have gcd 6, so this is not a primitive mechanical word. Its
denominator is nevertheless greater than one by the new theorem.

Its entries are 1 and 2. In the shortcut clock, every valuation 2
ends one odd run with one even step, so the number of local minima is
exactly `6(A0-m0)`. This count and the cycle minimum grow without bound
as the prime base length grows. This is a statement about primitive
cycles, not repeated displays of a shorter cycle. Odd-only local-minimum
counts are not substituted for the shortcut count.

## Primary records checked

- [Simons–de Weger, author-hosted version 1.43 (2007)](https://www.deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.43%5B2007%5D.pdf):
  the abstract and Theorem 3 exclude nontrivial cycles with at most 75
  shortcut local minima. The paper also gives bounds for larger counts;
  C005 does not claim those broader methods are inapplicable.
- [Hercher, Journal of Integer Sequences (2023)](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html):
  the official record states exclusion through 91 local minima and
  links the June 2026 corrigendum. The earlier
  [C001 audit](../C001/LITERATURE.md) records that correction's scope.
  No independent replay of the paper's computational proof is claimed.
- [Knight, publisher abstract/preview](https://www.sciencedirect.com/science/article/pii/S0012365X25004200):
  the stated nonintegrality theorem concerns extremal high cycles,
  represented by Christoffel words. Search-visible primary preview
  material was available; this turn's full-page open failed. C005 does
  not identify a large absolute minimum with that extremal hypothesis.
- [Fernandez–Ibanez, 2026 preprint](https://arxiv.org/html/2607.24844v1):
  the stated optimization concerns minimum rotation numerators at fixed
  totals, with Christoffel extremizers. No arbitrary rotation-block
  concatenation exclusion was located in this bounded comparison.
- [Halbeisen–Hungerbuehler, 1997](https://people.math.ethz.ch/~halorenz/publications/pdf/collatz.pdf):
  the affine composition and extremal mechanical background remain
  established inputs, with the precise prior review in C001/C004.

## Exact claim scope

The six-block family eventually exceeds every fixed minimum-size and
local-minimum-count cutoff, and is nonmechanical. Therefore C005's
exclusion applies outside the direct hypotheses of the named fixed-count
exclusions and the mechanical/high-cycle exclusion. This does not improve
the universal numerical record, prove independence from every consequence
of those papers, or establish priority against all literature. Searches
for concatenations of Christoffel/mechanical rotations did not establish
novelty. The headline and divergence remain open.
