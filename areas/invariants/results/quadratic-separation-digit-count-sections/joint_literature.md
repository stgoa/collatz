# V006 — Joint affine sections and the semigroup-growth boundary

**Status: bounded primary-source audit and written controls, 2026-10-18.**
No theorem here proves the active superlinear Collatz-complexity goal.
The genuinely joint question remains open in this investigation.

## 1. Exact question

For a finite-valued sequence f on n>=0, let

```
J_f(D) = {n -> f(2^a 3^b n+r): a,b>=0, a+b<=D,
                                  0<=r<2^a 3^b}.
```

The desired general statement would be one of:

- `|J_f(D)|=O(D)` implies eventual periodicity of f;
- the same hypothesis guarantees a binary-automatic section of f.

The second statement would suffice for the present Collatz application
when applied to a positive section: V005 proves that any such automatic
section forces the invariant coloring to be constant. Neither statement
was proved or found as an applicable published theorem in this bounded pass.

The [V005 sparse example](../V005/literature.md) refutes the corresponding
claim with **separate** base counts. It has quadratic joint growth and
does not refute the question above.

## 2. A real semigroup theorem with a missing hypothesis

Holt, Owens and Thomas,
[*Groups and semigroups with a one-counter word problem*](https://wrap.warwick.ac.uk/id/eprint/861/1/WRAP_Holt_Group_semigroups.pdf),
J. Aust. Math. Soc. 85 (2008), Theorem 4.2, shows that a finitely generated
semigroup with linear cumulative growth is covered by finitely many
families `a_i b_i^n c_i`. Its proof uses shortlex normal forms: every
contiguous subword of a semigroup normal form is again a normal form.
The statement and that proof step were inspected directly.

Our growth count concerns the orbit of **one** sequence under operators,
not the number of distinct operators. For affine maps A and B, equality

```
f composed with A = f composed with B
```

survives precomposition by a further affine C on the right:
`f composed with A composed with C = f composed with B composed with C`.
It does not automatically survive inserting C immediately after f.
Thus the equivalence on words is only one-sided. It does not define a
semigroup quotient to which Theorem 4.2 applies. Shortlex representatives
of an orbit have the appropriate prefix closure, but arbitrary contiguous
subword closure has not been supplied.

### Exact control: linear orbit, exponential transformation semigroup

This distinction is essential even for two simple maps on nonnegative
integers. Define

```
T(n)=n+1,
U(n)=n+1+1_(n is a positive power of 2).
```

Starting from 0, a word of length at most D reaches only integers in
`[0,2D]`. Thus this orbit has at most 2D+1 states through depth D, and
at least D+1 by applying T repeatedly.

Nevertheless all `2^D` words of length D give distinct transformations
of the entire set of nonnegative integers. To distinguish two such words,
let k be their first differing position, numbered from 0. Choose a power
of 2, p>4D, and start both words at n=p-k. Up to position k both maps
increase by 1, reaching p. At p one word applies T and the other U, so
their states differ by 1. All later visited positions are strictly between
p and 2p; every subsequent map therefore increases by exactly 1. The
final states remain different. This proves the exponential lower bound.

This is a control on a proposed general inference about actions, not a
joint affine-section counterexample. The maps T,U are not asserted to
realize a binary/ternary kernel. A valid proof must use those additional
affine relations explicitly.

## 3. What linear joint growth does force without an imported theorem

The zero-digit operators commute. If `|J_f(D)|<=C(D+1)` for every D,
then the `(D+1)(D+2)/2` pairs `(a,b)` with a+b<=D cannot all give
different whole sequences once D+2>2C. Thus some distinct pairs give

```
f(2^a 3^b n)=f(2^c 3^d n), every n>=0.
```

Multiplicative independence ensures that the two affine dilations are
different maps. The same argument applies at any fixed descendant g,
with the original growth bound shifted by its finite access depth.

This supplies an exact dilation relation at every state. It does not
supply an additive period or an automatic section. In particular,
relations involving only dilations lose the positive offsets responsible
for V004's rigidity. The previously retained scaling-only control has
`g(2n)=g(3n)=g(n)` and remains nonperiodic; it already defeats any attempt
to infer additive periodicity from this collision alone.

## 4. Why low word-pattern complexity is a different hypothesis

Morse–Hedlund and multidimensional pattern-complexity methods count
distinct finite patterns over **all** possible starting positions.
The count J_f(D) restricts the access cost of each starting state from
one root. A bound on one does not presently bound the other.

An elementary control is a ray of states 0,1,2,... with the shift
transition t->t+1 and arbitrary finite-valued outputs on its vertices.
Its cumulative orbit has D+1 states, while the output word can have
every possible finite binary block. Such a word can be obtained by
concatenating the finite binary words in length order. Hence linear
orbit growth alone does not imply low factor complexity.

For a proposed two-dimensional coloring
`(a,b) -> f(2^a 3^b n)`, rectangular patterns may begin at arbitrarily
distant exponent pairs. Their uniform count is not bounded by J_f(D)
at a fixed D. An applicability proof would need an additional bound
linking access depth to the size of a distinguishing pattern. No such
bound is assumed or proved here.

## 5. The algebra route has the same distinction

Taking the vector space with basis the section states turns the orbit
into a cyclic module under the section operators. Linear growth of its
cyclic filtration bounds the **module**, not the algebra generated by
the operators. The T,U example shows that the latter can contain
exponentially many transformations while the former has linear growth.

A further caution comes from Piontkovski,
[*Algebras of linear growth and the dynamical Mordell–Lang conjecture*](https://arxiv.org/abs/1706.06470)
(2017). The paper studies when finitely presented algebras of linear
growth have regular normal-word languages, and identifies dependencies
on the coefficient field. Its abstract was inspected. It does not state
that a cyclic module of linear growth has finite rank, nor does it
provide a binary/ternary automatic-section theorem. No result from it
is imported here.

Finite-state Cobham and finite-order Mahler theorems still require the
finiteness premise supplied in V004. Merely replacing the finite space
by one whose ball dimensions are O(D) leaves an unproved step.

## 6. Focused candidate record

1. **Objects:** the cumulative joint 2/3 affine-section orbit, together
   with its action by the five digit operators and its cyclic module.
2. **Structural gain:** the Collatz identities control every mixed
   section by a binary section with at most four extra binary levels per
   ternary step. Hypothetical linear binary growth therefore controls
   the whole joint orbit. Joint zero-digit collisions follow by an exact
   quadratic-versus-linear count.
3. **Translated unresolved gap:** turn that orbit constraint into an
   automatic section while respecting all positive offsets. A theorem
   about semigroup products, or global rectangular patterns, does not
   apply without an additional argument.
4. **Worked examples:** the V005 sparse sequence separates coordinate
   growth from joint growth; the explicit T,U action above separates
   orbit growth from transformation growth.
5. **Known-cycle controls:** periodic divisibility invariants at d=5 and
   d=61 have finite joint orbits. A general conclusion should permit
   eventual periodicity; the later exclusion of nonconstant colorings
   must use the particular d=1 identities.
6. **Cheapest meaningful next test:** prove that the affine digit
   relations add enough congruence stability to the section orbit to
   produce a finite binary descendant family, or identify exactly where
   a proposed adaptation of shortlex normal forms needs a stronger
   hypothesis. Test every claimed action theorem against T,U.
7. **Genuinely intermediate milestone:** a proved automatic-section
   theorem under the joint O(D) hypothesis, sufficient for the activated
   superlinear exclusion without assuming regularity of an actual
   nonabsorbing set.

**Decision:** retain the joint action as an open mechanism. Reject the
direct semigroup-growth and factor-complexity imports. The new exact
controls specify missing hypotheses; they are not completion of the
active mathematical goal.
