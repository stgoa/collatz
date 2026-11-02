---
id: undecidable-collatz-family-threshold
kind: question
title: "How small can an undecidable family of Collatz-like maps be, if it contains 3x+1?"
status: open
claim: >
  Conway (1972) and Kurtz–Simon (2007) show that convergence questions are undecidable, respectively Π⁰₂-complete,
  for the class of generalized Collatz maps n ↦ a_r·n + b_r on n ≡ r (mod m), where the map is the input. Find the
  most restricted natural family containing 3x+1 for which a convergence problem is undecidable, measured by the
  modulus m, the number of branches, and the size of the coefficients; in particular decide whether the problem
  "given odd d, does every positive orbit of the odd-only 3x+d map enter a cycle?" or its variant for the two-branch
  maps n ↦ n/2, n ↦ (a·n + b)/2 is decidable, undecidable, or equivalent to a known open problem. Literature status
  not checked: the first task is a search of what is known for small moduli.
created: 2026-11-01
tags: [decidability, generalized-collatz, frontier]
---

# How small can an undecidable family of Collatz-like maps be, if it contains 3x+1?

## Question

As in the claim. The fixed `3x+1` map cannot itself be the input of a decision problem; the families meant here vary a parameter (the map, a coefficient, a modulus) while the question asked of each member is fixed.

## Why it matters

[`collatz-conjecture-logical-form`](../results/collatz-conjecture-logical-form/README.md) shows that any undecidability statement about Collatz must live in a family, and that simulating machines inside `3x+1` orbits with "reaches 1" as the halting signal would already refute the conjecture. The interesting boundary is therefore between the large programmable classes of [Conway](../../../sources/conway-1972-unpredictable-iterations.md) and [Kurtz–Simon](../../../sources/kurtz-simon-2007-generalized-collatz.md) and the one-parameter families that contain `3x+1` and look like it. Knowing where undecidability starts would say how much structure a proof of the conjecture must use that a programmable map lacks.

## Known progress

- [`synchronised-coding-pcp-reduction`](../results/synchronised-coding-pcp-reduction/README.md): a different kind of undecidable problem, phrased with the fixed branches of `3x+1` and with the word list as input. It shows that the inverse tree of `3x+1` carries a free binary monoid with a decidable codebook; it is not a convergence problem.
- Nothing else in the repository. The controls `3x+5`, `3x+7`, `3x+13`, `3x+61` show that "every orbit enters a cycle" and "there is one cycle" are different questions as `d` varies ([`actual-cycles-3x-d-corpus`](../../cycles/results/actual-cycles-3x-d-corpus/README.md)).

## Suggested attacks

Proposals, not results.

- **Literature first.** Collect what is known on the smallest moduli and numbers of branches for which Conway's construction (FRACTRAN) and the Kurtz–Simon reduction go through, and add the findings as source nodes.
- **Simulate a counter machine with few branches.** Conway's construction encodes register values as exponents of primes. Count the branches and the modulus it needs, and try to shrink them while keeping the map affine on residue classes.
- **The one-parameter family.** For `3x+d`, the parameter `d` enters only additively. Ask whether some uniform statement over `d` (for example, "the number of cycles is finite") can encode a halting problem, or whether everything about `3x+d` is controlled by `3x+1` through the scaling `S_d(dy) = d·S_1(y)` plus finitely many residue classes.

## History

- Posed 2026-11-01 by the Claude cycles lane (Opus 5.5), directed by Santiago Armstrong, when the decidability area was opened.
