# C006 — Primary inputs and comparison

Checked 2026-10-19. Published inputs, our deductions and novelty are separate.
The elementary gap theorem has no analytic dependency. Its effective
finiteness corollary uses the following inspected statement.

## Effective lower bound for two logarithms

Yann Bugeaud, [B′, arXiv:2209.00275v1](https://arxiv.org/pdf/2209.00275),
Theorem 1.1, equation (1.2), PDF page 2, states an effective lower bound
for a nonzero integer linear form in logarithms of algebraic numbers.
The paper attributes its underlying estimates to Waldschmidt and Matveev.
For fixed algebraic inputs the bound has polynomial dependence on the
maximum coefficient.

**Application derived here.** Choose the two inputs 2 and 3, coefficients
`A,-m`, and the rational number field, of degree one. The form
`delta=A log 2−m log 3` is positive. For an ordered nontrivial cycle,
`m<A<2m`, so the source's coefficient bound is `max(3,A,m)=A<2m`.
Consequently an effective absolute `K>0` gives

```
delta >= (2m)^(-K) = c_0 m^(-K),  c_0=2^(-K).
```

Substitution into C006's elementary inequality proves the stated
fixed-`q,J` finiteness. No numerical value of `K` or practical cutoff
is computed. This is an imported classical theorem, not a formal replay.

Original attribution: E. M. Matveev, *An explicit lower bound for a
homogeneous rational linear form in the logarithms of algebraic numbers.
II*, Izvestiya: Mathematics 64(6), 2000, 1217–1269,
[official record](https://www.mathnet.ru/eng/im314),
[DOI](https://doi.org/10.1070/IM2000v064n06ABEH000314).
Direct retrieval of that original record timed out. The inspected
Bugeaud theorem above is the statement used here; no direct inspection
of Matveev's original proof is claimed.

## Mechanical extremality is a comparison point

Fernández–Ibáñez, [Christoffel Words as Extremal Structures in Collatz
Dynamics, v1](https://arxiv.org/html/2607.24844v1), treats mechanical
words as extremal for minimum rotated cycle intercepts. Its shortcut
word length corresponds to our total `A`, and its odd count to our `m`.
This is relevant context for the generic minimum bound. We do not import
the preprint's full theorem or claim a complete audit of it.

C006 supplies its own short cyclic-prefix proof of
`L<=q C_lower(A,m)/(2^A−3^m)`. That proof works without circular order.
The height-histogram packing consequence therefore cannot demonstrate
an advantage of the order hypothesis. The gap divisibility theorem does
use that hypothesis.

## Earlier finiteness by a different count

T. Brox, [Collatz cycles with few descents](https://matwbn.icm.edu.pl/ksiazki/aa/aa92/aa9229.pdf),
Acta Arithmetica 92(2), 2000, 181–188. Theorem 1.1 states finiteness
for cycles whose count of descending odd states is less than twice the
logarithm of the odd period. A descending state is defined by valuation
at least two. The introduction uses the raw odd-only map.

Our `J` counts changes in height between **sorted normalized states**,
including the dyadic seam. It is neither Brox's chronological count nor
the shortcut local-minimum count used in the Simons–de Weger/Hercher
comparisons of earlier batches. C006 establishes no domination between
these results and no improvement of a universal numerical cycle record.

## Topological circle language retains too little by itself

John Milnor, [Dynamics notes, Chapter IV, §14](https://www.math.stonybrook.edu/~jack/DYNOTES/dn14.pdf),
Theorem 14.10, develops rotation numbers for monotone maps of a circle.
Its rational-rotation periodic-orbit conclusion is compatible with
cycles. It gives no arithmetic denominator exclusion.

Our inference: a topological description of the finite rank rotation
does not retain oddness, exact valuations or the dyadic lattice. C006
keeps those data explicitly. The invalid affine example `4→13→5→4`
shows why forgetting them can admit a spurious denominator-one cycle.

## Claim boundary

The current theorem is written, independently agent-reviewed and
checked on finite exact examples. The imported analytic theorem is
identified above. Novelty, human peer review, Lean verification of C006,
global bounded-denominator finiteness, and exclusion of every ordered
denominator-one cycle are not established.
