# V001: rewriting, induced dynamics, and abstract interpretation

**Bounded first pass; three proposed languages, no new convergence claim.**
Read against R25, R31, R49, the per-packet bounded-size obstruction, and
the complete aggregate obstruction at every fixed exposure depth. These
proposals preserve the frozen results. Their milestones are local structural
theorems, not universal certificate supply. Default dynamics are positive
odd Syracuse, absorbed at 1; alternative clocks are identified below.

## 1. Rewriting: confluence of proofs versus termination of dynamics

**Objects.** Use guarded rewrite rules on *proof obligations and their
signed currents*, retaining source, target, hypotheses, and exact boundary.
Keep two relations separate: elementary equivalence normalization, and
forward dynamical progress. R25 already completely normalizes the first:
each class is two F-rays, with F(x)=4x+1, meeting through their selected
base relation. Calling this existing normalizer a rewrite system adds no
coverage.

**Structural gain.** The useful new question is whether different orders
of applying valid certificate transformations have joinable residual
obligations. A critical overlap can expose a missing hypothesis or genuine
cancellation before choosing a strategy. This concerns coherence of proofs,
not termination of the original orbit. Newman's classical implication
requires both termination and local confluence; it does not obtain the
former from the latter. See the [original paper](https://doi.org/10.2307/1968867).

**Translated gap.** Normalization ends at an unresolved canonical atom.
R25's induced T still has Collatz-equivalent universal termination. A
completion procedure which keeps inventing larger comparison rules may
itself fail to terminate. Moreover, signed proof dependencies require a
rank valid for every remaining input; canonical state equality does not
establish that rank. The fixed-catalogue obstructions permit recursive
proofs of growing size and forbid treating a finite completed table as
universal source coverage.

**Worked example.** The direct odd arrow 21→1 has current J=δ21, with
the atom/row at 1 killed. Alternatively the sibling comparison 21∼5 has
current δ21−δ5, followed by 5→1 with current δ5. The sum is again δ21.
This is an exact proof diamond with cancellation. Its rewrite lengths are
not orbit lengths: the sibling comparison is an equality of successors,
not the orbit arrow 21→5. R25's selected comparison 3∼1 similarly has
two actual odd arrows behind one normalization move.

**Known-cycle controls.** Every deterministic forward relation is
confluent: two finite prefixes from one state can be extended to a common
later state. Thus even 19→31→49→19 for d=5 is confluent.
The raw sibling identity for F_d(x)=4x+d is S_d(F_d(x))=S_d(x), so terminating sibling
simplification persists with known d=5 and d=61 cycles. Neither property
separates absorption from periodicity.

**Cheapest test.** Select one proposed new bridge, enumerate its symbolic
overlaps with the two R25 normalization moves, and retain the exact current
difference in each case. Do this before expanding a dispatcher.

**Intermediate milestone.** Prove joinability and a terminating proof
normalization for that explicitly bounded rule extension, including every
arithmetic guard. Unhandled canonical atoms remain leaves. This would make
alternative certificate constructions interoperable without asserting that
all leaves can be discharged. It is a new lens only if it discovers or
controls proof overlaps; renaming the existing priority dispatcher is not.

## 2. Induced maps: return times and affine cocycles

**Objects.** Choose an actual-state section or guarded phase and define a
partial induced map R(n)=S^{τ(n)}(n), with τ explicitly a first-return or
first-exit time. Record the full affine data: τ odd arrows, A total binary
valuation, and C in S^{τ(n)}(n)=(3^τ n+C)/2^A. Their composition is a cocycle;
the affine intercept and the consumed binary precision are part of it.
For a quotient construction, retain T's separate clock and its signed
ordinary-current lift: a T endpoint need not be an actual S endpoint.

**Structural gain.** Long excursions become individual, parameterized
branches instead of many locally unsuccessful steps. The question becomes
whether the induced branches have a controlled exit distribution, domain
closure, or compatible comparison after the excursion. Tao's
[first-passage Proposition 1.11](https://arxiv.org/html/1909.03562v7)
is a primary example of specifying both a stopping rule and its input
ensemble; its distributional conclusion is not a statement for every seed.

**Translated gap.** Defining a return does not prove it exists everywhere,
and a negative average homogeneous log-slope does not pay for intercepts,
exceptional branches, or return-time tails. R31 rules out strict descent
at every normalized return for finite labels with height-monotone ranks.
An induced argument must permit increases or retain unbounded arithmetic
state. R49 also warns that return into supplied history can succeed where
every smaller inverse ancestor is absent.

**Worked example.** R31's eight actual odd valuations
(1,2,1,1,1,1,2,2) map 27 through 41,31,47,71,107,161,121 to91. Their
map Ψ(x)=(6561x+9221)/2048 obeys
`4513 Ψ(x)+9221=(6561/2048)(4513x+9221)`.
On the guard x=27 modulo2^17, the integer
b=v2(4513x+9221) drops by exactly11 per complete block. Hence the maximal
number of consecutive guarded blocks is floor((b−6)/11), leaving b in
{6,...,16}; the duration is eight times that number. This finite exit
counter coexists with growing height. Its negative rational affine fixed
point is not a positive orbit or a cycle.

**Known-cycle controls.** For d=5 the word (1,1,3) has return formula
`S_5^3(x)=(27x+95)/32`, fixing19. Its homogeneous slope27/32 is below1.
The d=61 cycle at 235 has 41 odd arrows and valuation sum 66; its affine
return also fixes a positive point despite homogeneous slope below1.
Any drift argument must retain these intercepts and recurrent branches.

**Cheapest test.** Derive the eleven R31 exit cells symbolically, including
the extra exact-valuation bit, and compare their affine/current outputs
with supplied-history membership. No long orbit survey is needed.

**Intermediate milestone.** Obtain a complete first-exit relation for this
one repeated phase, valid for every repetition count, and prove a useful
smaller-seed comparison on one specified exit subdomain. Other exits may
remain open. Merely restating R26's variable-clock return is insufficient;
the gain must be a proved exit relation or composition law across phases.

## 3. Abstract interpretation and independently checked summaries

**Objects.** Treat S and the certificate constructors as transition
relations. Abstract states can combine congruence cells, interval bounds,
symbolic valuation counters, and relational facts about two actual source
histories. Every abstract state has an explicit concretization, and every
abstract edge must contain all its concrete transitions. Finite valuation
words retain modulus2^(A+1), including the extra bit. A small checker
validates invariant or summary certificates independently of their search.

**Structural gain.** The framework separates soundness from precision:
an abstract loop can be an overapproximation without being an integer
cycle. Refinement must eliminate a concrete spurious behavior, rather than
increase the catalogue because samples failed. This is the methodological
contribution of [Cousot and Cousot's original abstract-interpretation
paper](https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml).
The potentially new object is a relational invariant over whole histories
or an unbounded counter, rather than another accepted-case predicate.

**Translated gap.** Sound overapproximation proves safety properties;
termination additionally needs a well-founded progress argument covering
the represented executions. R31 excludes the obvious finite-label,
height-monotone template. Fixed-depth source coverage is also impossible
on the persisted annular families. Therefore unknown/capped exits must
remain unknown, and the abstract domain must either retain growing state
or prove why a finite summary covers arbitrarily long concrete histories.
No claim about Collatz undecidability follows from general program-analysis
limitations or from the separate inverse-Syracuse/PCP project.

**Worked example.** R49's 43-state canonical table is a finite inductive
invariant Q: it contains every canonical origin below39, is T-forward
closed, and excludes39. Those three checks prove that no smaller canonical
origin reaches39 at *any* quotient depth. Nevertheless
39→59→89→33 enters Q in three quotient arrows. The last arrow includes
normalization, so this is not an ordinary three-arrow path to33. The
example separates a sound unreachability certificate from forward progress,
without attempting an infinite search.

**Known-cycle controls.** The d=5 cycle {19,31,49} and the 41-state d=61
cycle must survive as concrete recurrent witnesses. A sound analyzer may
classify them as nonabsorbing or unresolved; it may not discharge them by
merging their residue labels. A ranking cannot strictly decrease around
their complete exact cycles. Raw versus absorbed-at-1
semantics must be declared at the transition relation.

**Cheapest test.** Use the R49 table and R31's counter decrement as two
small fixtures: one finite invariant, one unbounded family compressed by
a parameter. Ask which proposed abstraction proves each, and exhibit a
specific lost relation whenever it cannot.

**Intermediate milestone.** Prove a sound, compositional summary rule for
one counter-parameterized history family and produce a finite certificate
that checks all counter values, including its exit. This is useful before
universal termination and need not decide other families. Repackaging the
existing dispatcher as an automaton would not meet this milestone; an
invariant discovered across its rule boundaries could.

## First-pass assessment

Rewriting primarily clarifies which proof transformations can safely be
combined. Inducing exposes long excursions and their exact costs. Abstract
interpretation supplies a discipline for compressing those excursions
without converting lost information into a proof. Their most plausible
combination is a checked relational summary of a variable-length exit,
followed by a proof-overlap audit. This remains a proposal for a bounded
next experiment, not a selection of a universal proof strategy.

Local anchors: [R25](../../../convergence/results/elementary-bridge-quotient-normal-form/README.md),
[R31](../../../convergence/results/bounded-runs-exclude-finite-label-potentials/README.md),
[R49](../../../convergence/results/inverse-only-exclusions-short-forward/README.md),
[packet obstruction](../../../convergence/results/orbit-component-current-criterion/README.md),
[aggregate depth obstruction](../../../convergence/results/unbounded-exposure-depth-necessary/README.md).
