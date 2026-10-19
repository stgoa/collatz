# V006 — Independent review of the exact graph interface

**Status: PASS for the representation, converse and necessary layer
condition, 2026-10-18.** This review does not establish a new growth
theorem or complete the quantitative goal.

Reviewed [graph_interface.md](graph_interface.md), including composition
order, reconstruction from an abstract graph and the separating-layer
argument, against the [V005 scalar equivalence](../V005/scalar_interface.md).

## Radix identities and the root equations

The operator order is correct. Applying E_i first and T_j second gives
`s(6n+2j+i)`. The uniquely determined l,k with `2j+i=3l+k` give the same
sequence when T_k is applied first and E_l second. The six identities
therefore exchange adjacent binary and ternary digits while preserving
both the residue and the product of their radices. They do not assert
commutation of arbitrary digit operators.

The root relations are precisely the three scalar identities:
`T_0(b)=E_0(E_0(b))`, `T_2(b)=E_1(b)`, and
`E_1(E_0(b))=b`. In particular the last left side evaluates to b(4n+2),
not b(4n+1). The omitted dynamical arrow from absorber 1 remains covered
only by the valid color equality h(4)=h(1).

## Abstract graph converse

The converse correctly requires the six radix identities at **every**
vertex and requires all five transitions to be defined. A binary digit
word represents its integer in least-significant-first order. Appending
binary zeros preserves the output by `o(E_0(s))=o(s)`.

For a fixed n, choose n<2^a and n<3^b. The path consisting of its a
binary digits followed by b ternary zeros has residue n. Adjacent swaps
move all ternary digits to the front. Each swap is legal at the current
vertex and preserves the mixed-radix residue. In the resulting ternary-
then-binary representation, the upper binary block is zero because
n<3^b. Removing it preserves output. The lower ternary block is exactly
the padded ternary representation of n. This proves equality of the
binary and ternary evaluations for every vertex, including n=0.

Prepending a binary digit now gives the stated E_i extraction. Prepending
a ternary digit and using equality of the two evaluations gives the
stated T_j extraction. Thus the abstract transitions really act as the
five section operators on the reconstructed sequences.

The required merger of output-indistinguishable vertices is valid for
both sets of transitions. Once f_s=f_t as entire sequences, the extraction
identities imply equality for their E_i children and their T_j children.
The equivalence is therefore a transition congruence, and the quotient
retains all six identities. In that quotient, reachable vertices through
depth D correspond exactly to distinct joint sections accessible in at
most D operations. Root equations (3) then permit the V005 converse to
construct the actual invariant h.

## Separating layers

For a real coefficient C satisfying `|B_D|<=C(D+1)`, if all sufficiently
late increments were larger than floor(C), each would be at least
floor(C)+1>C. Summing gives a contradiction. Hence infinitely many layers
have size at most floor(C).

The separation claim is also valid for directed graphs with returns and
cycles. At the first exit from B_D, the predecessor has root distance at
most D, so the next vertex has distance at most D+1 and lies in
`B_(D+1) minus B_D`. In the nonconstant-invariant application the graph is
infinite, by the local automaticity lemma. The arbitrarily late layers
therefore give genuine bounded separating sets. No contradiction with
infinite descendants is inferred solely from their existence.

## Controls and disposition

The d5/d61 graphs satisfy the universal radix and zero-output conditions,
but the d1 root relation b(3n)=b(4n) fails on actual checked inputs:
n=3 for d=5 has colors (0,1), and n=10 for d=61 has colors (1,0).
The updated bounded verifier exercises these named failures directly.

Accept the graph interface as a faithful formulation and the bounded-layer
conclusion as a necessary condition. The proposed automatic-section
conclusion, even for restricted separating-layer patterns, remains an
open subsequent test. No correction was required.
