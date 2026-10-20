# V005 — Whole-section growth: source audit and a rejected shortcut

**Status: written arguments and bounded primary-source audit, 2026-10-18.**
The counterexample below concerns general sequences. It does not refute the
active Collatz-specific goal. No novelty claim is made.

## 1. The exact literature quantity

For a sequence f on the nonnegative integers define

```
G_k(f;D) = #{ n -> f(k^a n+r) : 0<=a<=D, 0<=r<k^a }.
```

Equality here means equality on **all** n>=0. This is exactly the
`k-growth` of Definition 4 in Jason P. Bell,
[*Cobham's theorem and its extensions*](https://numdam.org/item/10.5802/acirm.3.pdf),
Actes des rencontres du CIRM 1 (2009), 11–16, p.14. Definition 5 takes
the limsup of `log G_k(f;D)/log D`. Conjecture 3.4 asserts eventual
periodicity for a finite-valued sequence whose dimensions in two independent
bases are finite. That passage is explicitly a **conjecture**, not a theorem
available for import. The elementary construction in Section 2 contradicts
the conjecture as printed, even with linear bounds in bases 2 and 3.

The source was inspected directly on 2026-10-18. A bounded search for an
existing discussion or correction did not locate one. That search establishes
neither novelty of the example nor the absence of a later correction.

## 2. Separately linear growth in two bases does not force periodicity

**Proposition (written proof).** Put

```
E = {2^j : j>=0},
A = {6^e : e in E},
f(n) = 1_A(n), n>=0.
```

Then f is not eventually periodic, but for every integer D>=0,

```
G_2(f;D) <= 5D+3,
G_3(f;D) <= 3D+3.
```

**Proof.** Fix p=2 or 3 and a section depth a. The support points 6^e
have p-adic valuation exactly e. Those with e>=a lie in the zero residue
class modulo p^a. Those with e<a have nonzero residues, with distinct
p-adic valuations; therefore distinct such support points cannot occupy
the same nonzero residue class modulo p^a.

Consequently every section with r>0 is either the zero sequence or a
singleton indicator

```
delta_q(n) = 1_(n=q),     q = floor(6^e/p^a), e<a.
```

Across depths 0 through D, the zero-offset sections contribute at most
D+1 sequences. The zero sequence and delta_0 contribute at most two more.
For p=2, the inequality `6^e<2^(3e)` shows that q>0 requires a<3e.
For a fixed e<D there are fewer than 2e eligible depths e<a<3e. Thus

```
G_2(f;D) <= D+3 + 2 sum_{e in E, e<D} e < 5D+3  (D>=1).
```

For p=3, use `6^e<3^(2e)` and fewer than e eligible depths to obtain
`G_3(f;D)<3D+3` for D>=1. The displayed non-strict bounds include D=0.
The geometric sum used in both estimates satisfies
`sum_{2^j<D}2^j<2D`.

The support is infinite and the gaps between successive support points tend
to infinity. An eventually periodic indicator with infinitely many ones
has bounded gaps beyond its cutoff. Hence f is not eventually periodic.
This proves the proposition.

### Why this is not a Collatz counterexample

The example fails doubling invariance already at n=3:
`f(6)=1`, whereas `f(3)=0`. It satisfies neither the full hypotheses of
V004 nor the active goal's invariant-coloring premise. All of its support
is even and divisible by 3, so its failure is especially transparent.

### Why the stronger joint-section mechanism survives this test

Let J_f(D) count distinct whole sequences obtained by at most D section
operations, where each operation may use either base 2 or base 3. Among
these are the zero-offset mixed sections

```
F_(a,b)(n) = f(2^a 3^b n),       a,b>=0, a+b<=D.
```

These `(D+1)(D+2)/2` sequences are pairwise distinct. Their supports are

```
{ 2^(e-a) 3^(e-b) : e in E, e>=max(a,b) }.
```

Indeed, equality of the supports for (a,b) and (a',b') would imply that
their valuation pairs agree. Matching any support point gives
`a'-a=b'-b=c` and maps its exponent e to e+c. Thus the tails of E would
be invariant under the fixed translation c. If c is nonzero, choose e
beyond the absolute value of c: two sufficiently large powers of 2 cannot
differ by c. Hence c=0, a=a', and b=b'. Therefore

```
J_f(D) >= (D+1)(D+2)/2.
```

The example refutes **separate** linear bounds as a periodicity criterion.
It does not refute a theorem assuming linear growth of the **joint**
section family. V004's depth-controlled closure has the potential to
give the stronger joint bound for a hypothetical low-complexity Collatz
invariant. Those premises must not be conflated.

## 3. Other primary sources and why they do not finish the goal

### Truncated automaticity

Jeffrey Shallit,
[*Automaticity IV: Sequences, Sets, and Diversity*](https://cs.uwaterloo.ca/~shallit/Papers/auto4.pdf)
(author manuscript dated 1996), Section 1 defines automaticity by the
smallest automaton agreeing up to a numeric cutoff. Its equivalent
description uses pairwise distinguishable **truncated** kernel sequences.
Proposition 1 gives a logarithmic lower bound infinitely often for
nonautomatic sequences. Theorem 10 constructs a set with logarithmic
automaticity in every base and without automaticity in any base.

This source's cutoff is the original input value, whereas our depth
cutoff leaves each resulting sequence infinite. It cannot justify a
superlinear bound in D for whole sections. Nor may the logarithmic
lower bound be renamed a superlinear whole-section bound.

### Quantitative intersections of sparse automatic sets

Seda Albayrak and Jason Bell,
[*Quantitative estimates for the size of an intersection of sparse automatic sets*](https://arxiv.org/abs/2304.09223)
(2023), assumes actual finite automata in independent bases and bounds
intersections using their automaton data. Sparse support and small
whole-section growth are different conditions. Neither finite
recognizability nor the required sparse description has been supplied
for a hypothetical Collatz component. The abstract was inspected;
no theorem from this paper is imported.

### Finite-rank Mahler and regular-sequence results

Adamczewski and Bell,
[*A problem about Mahler functions*](https://arxiv.org/html/1303.2019),
proves rationality under simultaneous finite-order Mahler equations
in independent bases. This is the finite-system input available to V004.
A growing count of sections, even O(D), does not supply finite rank or
a fixed finite Mahler system. Applying that theorem here would require
a new rank-reduction argument. No such argument is supplied by the
source's theorem statement.

## 4. Candidate records

### A. Independent-base growth transfer

1. **Objects:** the separate whole kernels in bases 2 and 3, with their
   cumulative depth counts.
2. **Structural gain:** V004 transfers an O(D) binary bound for a positive
   section into an O(D) ternary bound.
3. **Translated unresolved gap:** separate linear growth does not imply
   eventual periodicity, as Section 2 proves.
4. **Worked example:** the exact sparse support `{6^(2^j)}` has the two
   displayed linear bounds and unbounded support gaps.
5. **Known-cycle controls:** at d=5 or 61, the periodic invariant
   `1_(d divides n)` has bounded kernels and must remain permitted when
   the +1 identities are replaced by +d identities.
6. **Cheapest meaningful next test:** already decisive; any proposed
   generic separate-growth theorem must be checked against Section 2.
7. **Intermediate milestone:** a Collatz-specific extra hypothesis that
   excludes the sparse example; repeating Bell's printed conjecture is
   not an available milestone or proof input.

**Decision:** reject the generic two-separate-bounds shortcut. Retain the
depth transfer as one part of the stronger joint approach.

### B. Joint mixed-base growth

1. **Objects:** the orbit of a whole sequence under all binary and ternary
   section operators, with total operator length charged.
2. **Structural gain:** V004's explicit formulas bound the increase of a
   binary representation depth per operator. A hypothetical O(D) binary
   kernel would therefore constrain the full mixed orbit, not only its
   coordinate directions.
3. **Translated unresolved gap:** prove a rigidity theorem for a joint
   affine-section orbit of linear growth, or exploit additional Collatz
   identities to obtain one. No applicable published theorem was found
   in this bounded pass.
4. **Worked example:** Section 2 has linear coordinate growth but at least
   triangular joint growth. It discriminates the two objects exactly.
5. **Known-cycle controls:** periodic divisibility indicators at d=5/61
   have bounded joint section families; a conclusion must allow periodic
   patterns before using the specific d=1 affine identities.
6. **Cheapest meaningful next test:** inspect whether mixed commutation
   and affine translation relations turn linear orbit growth into a
   finite section family or a periodic section.
7. **Intermediate milestone:** a proved joint-growth rigidity lemma with
   explicit hypotheses, sufficient for the active superlinear exclusion
   while imposing no regularity on the actual nonabsorbing set.

**Decision:** viable, but open here. The sparse counterexample does not
settle it.

### C. Finite-rank extraction

1. **Objects:** the linear span of all positive section sequences and
   the binary/ternary Cartier operators acting on it.
2. **Structural gain:** actual finite rank would unlock established
   regular-sequence or Mahler rigidity.
3. **Translated unresolved gap:** the number of states in a ball being
   linear does not make their span finite-dimensional.
4. **Worked example:** zero-offset sections of the sparse sequence have
   infinitely varying supports; a linear ball bound alone does not make
   a fixed finite-state system.
5. **Known-cycle controls:** d=5/61 divisibility indicators have finite
   rank and remain nonconstant; the final +1 arithmetic argument is still
   required.
6. **Cheapest meaningful next test:** look for a specific operator
   identity forcing bounded rank under the joint-growth hypothesis.
7. **Intermediate milestone:** prove that identity and its rank bound,
   without assuming finite rank as an extra premise.

**Decision:** a possible algebraic route, with the missing hypothesis
made explicit; no import currently closes it.
