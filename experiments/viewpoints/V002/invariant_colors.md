# V13 — Arithmetic regularity of component colorings

**Status: exploratory language, with an elementary written finite-period
classification below. No novelty or convergence claim.** This changes the
question from constructing each merger to classifying how an obstruction
could be represented. Its unrestricted version is still Collatz-equivalent;
only restricted regularity classes are investigated here.

## 1. Objects

Let h assign a color to every positive integer and be constant on each
Collatz orbit component. Extend an odd-state coloring by
`h(n)=h(oddpart(n))`. For fixed positive odd d with `3∤d`, invariance means

```
h(2n)=h(n)                       for n>=1,
h(3n+d)=h(n)                     for odd n>1.                 (1)
```

The target1 is absorbing; no second identity is imposed at n=1. These
equations express ordinary-arrow invariance, not a change in the default
odd-only clock. The shortcut form of the second equation is equivalent
by the first. A nonabsorbing-set indicator is one such two-color function.
Ask which regularity classes can contain a nonconstant solution.

## 2. Structural gain

The component obstruction from R7 becomes a function with exact arithmetic
symmetries. The new question is its **regularity**, rather than merely the
existence of an invariant function. Finite periods can be classified uniformly
over every modulus, without inspecting long trajectories. At d=1 the
classification collapses to constants; at d=5 and61 explicit nonconstant
periodic controls survive. The additive parameter is visible in the result.

This is within the established functional-equation tradition, not a claim
to invent that tradition. A useful external comparison is
[Cobham's original base-dependence theorem](https://research.ibm.com/publications/on-the-base-dependence-of-sets-of-numbers-recognizable-by-finite-automata):
a finite-valued sequence automatic in both bases2 and3 is eventually periodic.
Here this theorem is a supplied published input, not a proof checked formally
in the repository. The elementary periodic argument below is independent of it.

## 3. Translation of the unresolved gap

All invariant colorings being constant is just convergence. There is no
reason supplied here for an actual hypothetical bad-set indicator to be
periodic, automatic, continuous on a compactification, or approximable at
a useful rate by such functions. A density result alone supplies none of
those regularity properties. Imposing one without proof would remove the
obstruction by assumption.

The narrower opportunity is to classify **restricted** invariant colorings
and discover precisely which arithmetic complexity a counterexample would
need. This can be useful short of proving that no counterexample exists.
It is different from assigning a height-decreasing rank to every trajectory.

## 4. Worked example and exact consequence

For every M>=1, every M-periodic solution of (1) factors through
`g=gcd(M,d)` and is constant on the orbits of multiplication by2 and3
in `Z/gZ`. The converse also holds. In particular, **every periodic or
eventually periodic d=1 invariant coloring is constant**.

For example, once the factors2 and3 have been removed from a hypothetical
period M, write A(n)=2n and B(n)=3n+1. Both preserve colors, so

```
h(6n+2)=h(A(B(n)))=h(n)=h(B(A(n)))=h(6n+1).
```

Since6 is invertible modulo the remaining period, neighboring residues
have the same color. The detailed argument handles even periods and the
absorber convention in the appendix. This is a statement about a regularity
class, not about all component indicators.

## 5. Known-cycle controls

For d=5, `h(n)=1_{5|n}` is a nonconstant invariant coloring of period5.
Multiplication by2 or3 preserves zero versus nonzero modulo5, and the +5
term preserves that distinction. Likewise `h(n)=1_{61|n}` works at d=61.
The fixed odd states5 and61 are outside the designated absorber1.
The commutator gives shift by d, not shift by1, so it cannot erase these
colors. This names exactly where the d=1 rigidity argument ceases to apply.

These colors do not classify all components: the d=5 cycle19→31→49 and
the d=61 nonprincipal cycle at235 lie outside their respective divisible
strata. Such basins can require less regular descriptions.

## 6. Cheapest next test

Compare finite **binary kernels**, rather than finite periods. A finite-valued
sequence is2-automatic when the family
`{n -> h(2^k n+r): k>=0, 0<=r<2^k}` is finite. Under d=1 invariance,

```
h(3n+2)=h(2n+1).                                        (2)
```

This controls one ternary section. It does not by itself bound the full
ternary kernel, including the `3n` and `3n+1` sections and every iterated
section. The next bounded test is to write these missing sections explicitly
and ask whether invariance supplies a finite closure. Do not confuse the
automaticity of a single affine subsequence with a uniform bound over all
ternary depths. Search the literature before treating the question as new.

Relevant prior work already gives regular languages of ancestors at **each
fixed number of odd shortcut branches**; see
[Stérin, Theorem 1](https://arxiv.org/html/1907.00775v4), crediting
Shallit–Wilson for regularity. This does not supply one finite automaton for
the whole basin. That basin takes a union over unbounded branch counts, and
regular languages are not closed under arbitrary countable unions. The next
test must address unbounded closure rather than rediscover a fixed-budget
recognizer. This is a checked source distinction, not an exhaustive novelty
search for the single-base invariant-coloring question.

## 7. Intermediate milestone and assessment

**Candidate milestone:** classify the2-automatic solutions of (1) at d=1,
without assuming arbitrary invariant colorings are automatic. A sufficient
route would derive a finite ternary kernel from a finite binary kernel and
(1); Cobham plus the appendix would then force constancy. That implication
is currently unproved here. The two-base-automatic case is already covered
by the supplied Cobham theorem and is not the new target.

The finite-period classification is a concrete useful diagnostic, and the
single-base question is a restricted obstruction problem, not universal
current supply. This earns a bounded comparison with the base-conversion
viewpoint. It does not yet justify a long automata search or an assumption
that every obstruction belongs to the chosen class.

## Appendix — Complete elementary classification of finite periods

Assume h has period M and satisfies (1); its color set may be arbitrary.
Write `M=2^a 3^b m`, with `(m,6)=1`.

**Remove the factor2.** If `n=n' mod3^b m`, then
`2^a n=2^a n' modM`. Iterating the first identity gives `h(n)=h(n')`.
Thus h factors through the odd modulus `M0=3^b m`.

**Extend the affine identity to every residue.** Every class modulo M0
has a sufficiently large positive odd representative greater than1.
The second identity therefore gives invariance of the induced coloring
under `B(r)=3r+d` on every residue of `Z/M0Z`. In particular the missing
ordinary arrow at the absorber causes no exception in this finite quotient.

**Remove the factor3.** The b-th iterate is
`B^b(r)=3^b r+d(3^b-1)/2`. Residues r,r' equal modulo m have the same
image under this iterate modulo M0. Hence h factors through m. This also
works at b=0, when there is no factor to remove.

**Use the affine commutator.** On `Z/mZ`, both A(r)=2r and B(r)=3r+d
preserve h. Thus `h(6r+2d)=h(6r+d)`. Since multiplication by6 permutes
these residues, h is invariant under translation by d. The subgroup
generated by d consists of the multiples of `gcd(m,d)`, so h factors
through `gcd(m,d)=gcd(M,d)=g`. At this modulus B is multiplication by3;
A is multiplication by2. Colors are exactly unions of their joint orbits.

**Converse.** If h factors through g and is invariant under those two
multiplications, then (1) holds because g divides d. Since g divides M,
the function is M-periodic. This proves the asserted classification.

**Eventual periods.** If a period M only holds for n>=N0, choose k so that
both `2^k n` and `2^k(n+M)` exceed N0. They differ by a multiple of M;
the first identity gives `h(n)=h(n+M)`. Thus eventual periodicity is already
global periodicity here. For d=1 the classification forces constancy.

The appendix is a written elementary argument, independently reviewed for
its exact domain. It is not a novelty claim, a formal verification, or a
regularity theorem for the actual nonabsorbing set.
