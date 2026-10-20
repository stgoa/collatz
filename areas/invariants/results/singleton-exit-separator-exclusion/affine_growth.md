# V007 — Exact affine growth, finite cuts, and the literature boundary

**Status: bounded source audit and independent algebra check. The full
quantitative goal remains open.** This pass found neither a published
theorem covering linear growth of the entire joint section orbit nor an
exact joint affine-section counterexample with linear growth and every
binary section nonautomatic. This is a bounded search result, not a claim
that no such theorem or example exists.

**Subsequent written result.** [separator.md](separator.md) now excludes
a finite forward interior with one exit when every reachable vertex has
infinite kernels in both bases. Its elementary proof passed the separate
[source-level audit](INDEPENDENT_REVIEW.md). The singleton case is settled
under that hypothesis; arbitrary finite separator size remains open.

The object is the graph in [V006's interface](../quadratic-separation-digit-count-sections/graph_interface.md):
vertices are entire finite-valued sequences; its two binary and three
ternary transitions satisfy all six radix identities and the leading-zero
output conditions. The Collatz root has the additional three scalar
identities. A rooted ball counts states, not distinct transformations,
finite prefixes, or translated patterns.

## 1. A small cut is a finite interface to unknown sequences

Let I be a finite set of vertices containing the root and let C be the
finite set of all immediate successors outside I, for the transitions
under consideration. Reading digits until the first exit from I is a
finite automaton with boundary states C. This does not specify the
continuations from C.

Here is the exact closure statement for either base k=2 or k=3.

**Finite-cut closure lemma (written proof).** If every vertex of C has a
finite k-kernel and every k-transition out of I lands in I or C, then
every vertex of I has a finite k-kernel.

Indeed, the union of I and the k-kernels of the finitely many members of C
is a finite k-closed set. It contains every k-descendant of every member
of I. If C={q} and q is a k-descendant of the root, root automaticity and
q automaticity are therefore equivalent. This closure lemma alone
transfers the unknown automaticity question to q. The stronger argument
in [separator.md](separator.md) uses all six radix identities and
infinitude in both bases to exclude such a singleton cut altogether.

If every vertex of I has infinitely many k-descendants, each has some
pure k-path to C. A shortest such path has length at most |I|, since its
interior vertices cannot repeat. Arbitrary paths may still loop inside I
for an unbounded time. In particular there is no justified uniform bound
on the length of every first-exit word.

The same issue appears if the finite interior is written as a Mahler
system with boundary series. The system still contains the unspecified
boundary continuations. Finiteness of the interior alone supplies no
closed finite-order Mahler system for those boundary sequences.

### Candidate record: bounded separating layers

1. **Objects.** The exact joint 2/3 section graph and arbitrarily distant
   finite cuts supplied by a linear rooted-ball bound.
2. **Structural gain.** Each cut yields finite exit automata in both
   bases, while radix compatibility identifies the two representations
   of every mixed affine section.
3. **Translated unresolved gap.** For every fixed finite boundary size
   K>=2, prove that the simultaneous exit descriptions and radix
   identities force some reachable sequence to have a finite kernel,
   or otherwise force growth beyond every linear bound. The singleton
   theorem does not provide that extension.
4. **Worked example.** For a singleton boundary q, both root and q are
   automatic together in each base, provided q is reachable in that
   base. The additional two-base infinitude hypothesis now rules out
   this exact joint configuration by the singleton theorem.
5. **Known-cycle controls.** The d=5 and d=61 divisibility colorings obey
   the universal radix identities but need not obey the d=1 root scalar
   identities. A general joint-growth theorem could allow their finite
   graphs. A Collatz constancy conclusion must use the d=1 equations.
6. **Cheapest meaningful next test.** Retain the two boundary-state
   labels in the two-exit analogue of the singleton boundary polynomial.
   Failure to derive closure is not itself a counterexample; a
   refutation requires an actual compatible graph or sequence.
7. **Genuinely intermediate milestone.** Exclude all linear binary
   whole-section bounds for a nonconstant invariant, with every possible
   coefficient C. This permits an unrestricted hypothetical invariant
   with larger complexity and makes no regularity assumption about an
   actual component indicator. The proved singleton-cut exclusion is
   a successful structural test, not completion of that milestone.

## 2. Primary sources checked in this pass

### Rational-base decorated trees

Michel Rigo and Manon Stipulanti, *Automatic sequences: from rational bases
to trees*, DMTCS 24:1 (2022), paper 25,
[primary PDF](https://dmtcs.episciences.org/9725/pdf), Theorems 27, 36, 41.
Theorem 41 assumes that, at some fixed height, every infinitely recurring
decorated factor of the rational-base numeration tree has at most one
extension in each specified domain class. It concludes p/q-automaticity.
Theorem 36 gives a converse with an additional finite-depth
distinguishability hypothesis. Theorem 27 characterizes ordinary
k-automaticity by finitely many infinite decorated subtrees.

These are global factor/extension conditions on numeration trees. A
small cut in the graph of whole affine sections does not give them.
Moreover, p/q-automaticity is a different input representation from
simultaneous binary and ternary automaticity. The paper's adaptation of
“Cobham's theorem” in Section 4 concerns the 1972 morphism
characterization, not the multiplicatively independent bases theorem.
No separator theorem can be imported from these statements.

### Asymptotic Cobham

Jakub Konieczny, *An asymptotic version of Cobham's theorem*,
[primary manuscript](https://arxiv.org/pdf/2209.09588), Theorems A and B,
Section 4. Here equality is weakened to agreement outside a set of
natural density zero, and automaticity means finitely many kernel
classes under that equivalence. Theorem A gives almost-everywhere
invariance under a nonzero shift from asymptotic automaticity in two
multiplicatively independent bases. Theorem B assumes exact automaticity
in one base and asymptotic automaticity in the other; it yields agreement
almost everywhere with a periodic sequence. Section 4 constructs a
sequence asymptotically 2- and 3-automatic which does not agree almost
everywhere with any periodic sequence.

Neither an O(D) exact kernel bound nor bounded separating layers has
been shown here to give finite kernels modulo density-zero errors.
Even supplying that premise would not yield exact periodicity through
Theorem A. This is not a counterexample to the exact joint-growth
route: no linear bound on the example's entire joint orbit was checked.

### Previously audited imports remain unavailable

[V006's source audit](../quadratic-separation-digit-count-sections/joint_literature.md) already explains why
linear-growth semigroup structure theorems do not directly apply to a
single rooted orbit. Equality of two states provides a one-sided action
congruence, not the two-sided congruence needed for a semigroup quotient.
The separate-base counterexample in
[V005](../automatic-section-forces-constancy/literature.md) has at least quadratic mixed growth. Neither
gap is repaired by calling the action rational or affine.

## 3. Independent audit: reverse closure gives two-base infinitude

This section checks the new elementary reverse-closure lemma independently
against [the scalar interface](../scalar-interface-three-identities.md). Put

```
c(n)=b(2n),
b(3n)=b(4n),
b(3n+2)=b(2n+1),
b(4n+2)=b(n),                     n>=0.
```

For a>=0, set m=3^a, take 0<=r<m and i in {0,1}, and let v=mi+r.
Then 0<=v<=2m-1. Write v=2w or v=2w+1. Direct substitution gives:

| Section to take | v=2w | v=2w+1 |
| --- | --- | --- |
| E_i of n -> b(mn+r) | n -> c(mn+w) | n -> b(3mn+3w+2) |
| E_i of n -> c(mn+r) | n -> b(3mn+3w) | n -> b(mn+w) |

The first row follows from b(2x+1)=b(3x+2); the second follows from
b(4x)=b(3x) and b(4x+2)=b(x). In both parity cases 0<=w<m.
The offsets w, 3w and 3w+2 lie respectively below m, 3m and 3m.
Thus these are genuine ternary sections, including a=0, r=0.

**Audit result: PASS as a written algebraic argument.** The union of the
ternary kernels of b and c is binary-closed. If b is ternary-automatic,
then so is c by closure under fixed affine extraction. This union is
finite, hence b is binary-automatic. The reconstruction of h from its
odd section and V004 then force h to be constant.

The [V005 local reconstruction](../automatic-section-forces-constancy/direct_sections.md#2-a-local-automaticity-lemma)
also works if its positive-offset binary section
g(n)=h(2^K n+r) is ternary-automatic. Its exact color identities are
unchanged. Fixed affine extraction and fixed-modulus interleaving preserve
automaticity in base 3 just as in base 2, so the reconstruction makes b
ternary-automatic, and the preceding paragraph applies. This assertion
concerns a positive-offset **binary** section that is ternary-automatic;
it does not assume an unproved reconstruction from an arbitrary ternary
cylinder of h.

By V004, every joint state reached from b is representable as such a
positive binary section. Consequently, a hypothetical nonconstant
invariant has an infinite pure binary kernel and an infinite pure
ternary kernel at every joint vertex. The algebra uses the d=1 scalar
identities, so it does not falsely exclude the generalized-map controls.
This supplies the infinitude hypothesis for the singleton theorem.
An exclusion of arbitrary fixed finite cut size is still missing.

## 4. Decision

Retain the full quantitative obstruction as the high-level target. The
new reverse closure removes one asymmetry from its exact graph model,
and the singleton theorem excludes its smallest finite bottleneck.
The central missing theorem remains growth amplification or a bound on
overlap across arbitrary finite cuts of size at least two. This pass does not
justify replacing that target by more digit-statistic subclasses or
claiming that a named extension of Cobham already solves it. No novelty,
formal verification, or convergence claim is made.
