# V008 — Boundary size alone cannot prove the growth theorem

**Progress; the full unbounded-ratio goal remains active and unresolved.**
The preceding batch V007 was delivered at
`b24020f8c64aab28a11326bf542e5a05530aa022` and made progress by excluding
singleton exits. V008 compares its proposed two-exit extension with an
investigation using the full cumulative growth hypothesis. No universal
asymptotic rate improvement is claimed.

## 1. The generic two-exit extension is refuted

The [exact construction](two_exit.md) takes an irrational rotation
coloring p and repeats each value six times:

```
p(n)=1_{{n alpha}<alpha},      0<alpha<1 irrational,
s(n)=p(floor(n/6)).
```

Both binary children of s equal `u(n)=p(floor(n/3))`; all three ternary
children equal `v(n)=p(floor(n/2))`. The states s,u,v are distinct, so
the finite interior {s} has exactly two exits. Every reachable section
has irrational natural frequency alpha. A finite kernel with an existing
frequency has rational frequency, by a rational stochastic-matrix
averaging argument. Thus every vertex has infinite kernels in both bases.

This is an actual graph of entire sequences obeying all six radix laws
and zero-output conditions. It refutes the generic two-exit analogue of
V007. Its binary and ternary incoming edges reach different boundary
states; collapsing those states loses precisely the relevant information.
The note derives the correct destination-valued boundary equation for
any finite number of exits.

The example fails the Collatz equation `s(4n+2)=s(n)` at n=1. Its zero
sections already supply at least `D(D-1)/2` distinct states through joint
depth D. It is therefore neither a Collatz invariant nor a linear-growth
counterexample, and it supplies no recurrent bounded-layer example.

## 2. The full root equations give an elementary finite-depth exclusion

Root derived the [first-shell theorem](ROOT_REVIEW.md): for any output
alphabet, the three scalar equations

```
b(3n)=b(4n),  b(3n+2)=b(2n+1),  b(4n+2)=b(n),   n>=0,
```

together with `|J_1(b)|<=3`, force b constant. An exhaustive case split
exhibits a binary-closed family of at most four entire sequences. All
their outputs at zero agree, so binary reading gives constancy directly.
This theorem does not need Cobham or a finite output alphabet.

For a nonconstant invariant it implies `|J_1(b)|>=4`. This rules out the
generic example at the actual Collatz root, and confirms that the extra
equations matter. It does not move those root equations to arbitrary
boundary states or rule out later two-exit interiors. The resulting
finite-depth constraint gives no improved universal asymptotic bound.

During review, one unpublished draft row used an incomplete subset of
the radix equations. The omitted equation makes that row inconsistent.
It was removed before acceptance; seven surviving rows give the theorem.
The [root review](ROOT_REVIEW.md) records the correction explicitly, and
a second review independently checks the final table and constant-output
finish. No historical theorem was found false or altered.

## 3. Use the growth assumption in its actual strength

The parallel [growth analysis](linear_joint.md) proves a useful uniform
version of the small-layer observation. If `|B_D|<=C(D+1)`, then for every
C'>C there are arbitrarily late r with

```
|B_(r+t) minus B_r| <= C't     for every t>=0.
```

This follows by maximizing `|B_D|-C'D` over a tail. It retains the future
cumulative bound after selected cuts, including every return through the
finite interior.

A separate explicit abstract graph control has cumulative size O(D),
outdegree at most two and infinite descendants at every vertex, but
recurrent layer peaks of every height. It admits no arbitrarily long
intervals with one fixed bound on every layer. Its exact profile obeys
`sum_(n=1)^N a_n<=13N`. This control is not an affine section graph; it
refutes only a deduction from cumulative counting and finite branching.

The source audit checks one finitary S-adic rigidity result. Its symbolic
presentation and recognizability hypotheses have not been supplied by
our rooted count, so it is not imported as a growth theorem.

## 4. Comparison and next action

| Proposed mechanism | Outcome | Decision |
|---|---|---|
| Exclude every finite boundary of size two using radix laws and two-base infinitude | Exact affine counterexample | Reject at that generic scope |
| Use all three root equations when the first joint shell has at most three states | Elementary constancy theorem | Retain as a finite-depth distinction, with no rate claim |
| Replace cumulative linear growth by long stretches of uniformly bounded layer width | Explicit bounded-degree counterexample | Reject without an additional affine argument |
| Retain the uniform future cumulative bound after selected cuts | Proved necessary condition for each C'>C | Use this actual growth hypothesis in the next global overlap test |

Do not proceed by mechanically excluding successive fixed boundary sizes.
The next investigation must use the global bound or derive additional
equations from the full Collatz root. One bounded discrimination within
that investigation is exact near-minimal binary growth:
`kappa_h(D)=D+O(1)` is equivalent to one new binary state per sufficiently
late depth. Ternary children have a bounded forward depth cost but can
return arbitrarily far into the old graph. V007 cannot be applied to such
a binary layer as if it were a joint singleton exit.

Resolving that diagnostic would still be partial. The main completion
condition remains every possible linear coefficient, and no regularity
of the actual nonabsorbing set is assumed. Future graph limits or finite
presentations must retain whole-sequence distinctions; finite-prefix
convergence alone cannot provide an automatic actual section.

## 5. Verification and dependency scope

Root checked the two-exit construction, the irrational-frequency proof,
all multiplier witnesses and the layer-profile and envelope calculations.
The [independent review](INDEPENDENT_REVIEW.md) checks the counterexample
and the corrected first-shell theorem. The cases are equations of entire
sequences, not finite matching experiments. No formal verification or
novelty claim is made. The actual d5/d61 controls remain valid and fail
the named d1 root equations; they have finite kernels.

The [side review](side_review.md) records fetched pin
`b567f2bfc9ec581d42bbd35c5231324f7865a01e` and accepts an attribution
clarification: the Collatz applications in V005–V007 inherit the published
Cobham theorem through V004. Their elementary generic arguments are
separate. Dated notes now make this explicit in the standalone reports
and ledger. The written proof's use of a published theorem is distinct
from the Lean lane's conditional assembly and its replay status.

D8's proposed fixed-epsilon improvement is retained as a progress
diagnostic, not a new success condition. V008 does not achieve it. Its
automatic two-batch abandonment rule is rejected under the user's active
goal. Reconsidering methods remains appropriate; changing the objective
or treating fixed-width lemmas as completion does not.

This is a prose-only mathematical batch. Existing executable evidence,
the frozen R-series body, dispatcher and open LaTeX source remain
unchanged. The historical Phase6 finite gate was not rerun; mathematical
reviews, local links and exact frozen comparisons are recorded separately.
