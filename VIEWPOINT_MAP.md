# Find a better language for Collatz

**Language-selection recommendation, 2026-10-18. Collatz remains open.**
The [user-approved brief](docs/VIEWPOINT_BRIEF.md) governs this exploration.
The [batch log](docs/VIEWPOINT_LOG.md) records decisions and checks. The former
[route map](ROUTE_MAP.md) supplies evidence, without restricting the search.

## Recommendation after two rounds

We compared **fourteen viewpoints**, tested the initial shortlist, and expanded
the search when both shortlisted approaches reproduced existing obligations.
The preferred working language for the next bounded investigation is
**V13: arithmetic regularity of orbit-component colorings**. Its question is:

> If some integers never reach 1, how complicated must the arithmetic
> description separating their components from the component of 1 be?

This shifts attention to the representation of an obstruction. It already
has a checkable consequence: every eventually periodic invariant coloring
for `3x+1` is constant. For `3x+5` and `3x+61`, explicit nonconstant periodic
colorings survive. The [complete elementary argument](experiments/viewpoints/V002/invariant_colors.md)
identifies the exact role of the additive parameter. It is independently
reviewed here, with no novelty or formal-verification claim.

The proposed intermediate target is to classify invariant colorings recognized
by a finite automaton in **base 2 alone**. We have no reason to assume an actual
nonabsorbing set has that regularity. The two-base version follows from a
published theorem; the one-base closure question remains unproved here and
needs a prior-work check. This is a recommendation of a working language,
not evidence that it is a superior convergence method.

Use **V14: binary/ternary carry diagrams** for one complementary boundary test.
Retain **V12: laws of actual integer ensembles** as a distinct alternative.
V14 has not supplied finite-kernel closure, and V12 has not supplied a new
first-passage estimate. Their next tests are specified below.

The first round's information-loss lesson remains: simplifying a representation
can discard exactly what is needed to recover an actual positive-integer path.
Guarded affine histories preserve that information well, but the proposed
relational extension was already present in the frozen programme. Graph
geometry controlled local boundary errors without giving an average estimate.

The frozen results remain useful: they identify which quantities cannot serve
as progress measures and provide exact difficult examples. We preserve them
while changing the questions asked of them.

## Comparison

Each linked card records objects, structural gain, translated gap, example,
cycle controls, cheapest test and a genuinely partial milestone.

| View | What becomes clearer | What remains difficult | Current decision |
|---|---|---|---|
| V1. [Parity coding](experiments/viewpoints/V001/symbolic_arithmetic.md#v1-parity-coding-a-shift-with-a-difficult-arithmetic-subset) | Dynamics becomes a shift; prefixes and tails are explicit | Which infinite codes come from positive integers | Supporting language; substantial overlap with frozen prefix results |
| V2. [Mixed-place affine cocycles](experiments/viewpoints/V001/symbolic_arithmetic.md#v2-a-mixed-real2-adic3-adic-affine-cocycle) | Real size, exact binary legality, ternary endpoint conditions and offsets can be retained together | A bound coupling these data that does more than separate estimates | Keep as common arithmetic representation; the probe found no new inequality |
| V3. [Multiplicative semigroups](experiments/viewpoints/V001/symbolic_arithmetic.md#v3-multiplicative-semigroup-completion-versus-legal-path-lifting) | A relaxed factorization problem is already solved | Legal ordering and state-dependent realization | Defer: inspected induction uses an additional multiplication with an unsupplied bridge |
| V4. [Absorbing operators](experiments/viewpoints/V001/operators_geometry.md#a-absorbing-transfer-operators-and-function-spaces) | Survival of a specified input ensemble is one observable | A uniform estimate on that ensemble, without arbitrary-target contraction | Keep as measurement language; no spectral-gap claim |
| V5. [Orbit groupoids and currents](experiments/viewpoints/V001/operators_geometry.md#b-graph-currents-cohomology-and-orbit-groupoids) | Meeting lags, cycles and arithmetic labels remain visible | A useful invariant beyond existing component and current algebra | Defer bare homology or categorical reformulations |
| V6. [Dirichlet energy and potentials](experiments/viewpoints/V001/operators_geometry.md#c-potential-theory-dirichlet-energy-and-possible-boundaries) | Finite access-to-1 probabilities have comparison principles and explicit boundary flux | Quantitative arithmetic control as domains grow | Demoted after V002: local tail bounds do not control ensemble absorption |
| V7. [Proof rewriting](experiments/viewpoints/V001/rewriting_renormalization.md#1-rewriting-confluence-of-proofs-versus-termination-of-dynamics) | Compatibility of certificate transformations can be checked separately | Universal discharge of the remaining leaves | Supporting tool only; confluence does not imply termination |
| V8. [Induced maps](experiments/viewpoints/V001/rewriting_renormalization.md#2-induced-maps-return-times-and-affine-cocycles) | An arbitrarily long excursion can become one parameterized branch | Exiting a guard need not reduce height or enter known history | Defer unary inducing as a separate direction; much is already done |
| V9. [Relational abstraction](experiments/viewpoints/V001/rewriting_renormalization.md#3-abstract-interpretation-and-independently-checked-summaries) | Soundness, precision and unbounded counters are explicit | A useful relation between unequal-time histories that survives composition | Demoted after V002: tested relation already exists in R81/R93 |
| V10. [Rational denominator layers](experiments/viewpoints/V001/rational_layers.md) | Related maps become layers of one rational system; target and lattice changes are explicit | A property of the denominator-one layer that forces useful progress | Control bookkeeping; defer as an independent route |
| V11. [Occupation measures](experiments/viewpoints/V002/statistical_languages.md#v11-occupation-measures-recurrence-versus-escape-of-mass) | Cycle mass and escape of mass are different phenomena | Tightness uniform in the seed range; cycle identification remains separate | Diagnostic only until a quantitative mechanism is proposed |
| V12. [Information of actual integer ensembles](experiments/viewpoints/V002/statistical_languages.md#v12-conditional-information-of-realized-paths-rather-than-symbolic-entropy) | Merging, conditioning and endpoint concentration are separate | A quantitative first-passage law with integer endpoints | Retain as a separate statistical alternative; literature comparison first |
| V13. [Arithmetic regularity of component colorings](experiments/viewpoints/V002/invariant_colors.md) | Obstruction complexity and incompatible bases become explicit | Restricting one-base automatic solutions; no regularity of the actual bad set is known here | Preferred working language for the next bounded investigation |
| V14. [Two-dimensional base conversion](experiments/viewpoints/V002/base_conversion.md) | Binary and ternary data share one carry boundary | Growing frontier, finite integer support and nonlocal bootstrap | One complementary test; no kernel-closure implication established |

These are related lenses, not fourteen independent possible proofs. In particular,
V2, V8 and V9 share affine data. V4 addresses absorption through an exact
survival observable; V6 supplies auxiliary lower bounds for absorption. Their value must be demonstrated by different
estimates or proof organization, not by counting names. V13 asks about restricted
component invariants; V14 exposes arithmetic boundary data which might help
analyze such restrictions. This connection is a question, not a theorem.
Several deferred cards contain milestone templates rather than selected
targets; they are not ready research programmes. The selected portfolio below
has explicit targets and stopping conditions.

## Three discrimination probes

### 1. Which simplifications preserve legal paths?

The [lifting probe](experiments/viewpoints/V001/lifting_probe.md) compares V2
and V3. For the two odd arrows with valuations `(1,4)`, the exact map is
`(9x+5)/32` on `x=3 mod64`. Keeping only its slope loses the offset; reversing
the word changes the offset; using modulus32 wrongly admits35, whose actual
word is `(1,5)`. An integral rational-factor step can also be illegal:
`10*(3/5)=6`, but the shortcut image of6 is3, not10.

The inspected published semigroup step first multiplies `x=7 mod64` by5,
then reaches `(45x+5)/64<x` in six shortcut arrows. It is a valid step in
that relaxed problem. A Collatz comparison between x and5x is still missing.
**Decision:** keep guarded composition; defer semigroup lifting without a
new way to supply the bridge. No novelty is claimed for either calculation.

### 2. Does a finite exit counter supply progress?

The [summary probe](experiments/viewpoints/V001/summary_probe.md) tests V8/V9
on the frozen R31 growth pattern. An unbounded valuation counter decreases
by11 per guarded block, while the affine height grows. Its exact exhaustion
therefore proves exit from one specified guard. It does not prove descent,
and leaving that guard need not end the raw valuation word.

This reproduces structure already present in R31/R77; later frozen work
already retains asynchronous source histories. **Decision:** no new unary
return catalogue. A relational pilot needs an explicit invariant across
different histories or phases that simplifies an existing obligation.

### 3. Does a geometric potential add a usable bound?

The [potential probe](experiments/viewpoints/V001/potential_probe.md) uses
conductance1/n on actual odd arrows. On the finite domain `{1,3,5}`, the
voltage at3 and5 is less than1 because all omitted inverse edges lead to
the escape boundary. Deleting those edges gives a false finite-domain
value. On the d=5 nonabsorbing cycle, voltage is0.

Positive voltage certifies a finite path into the component of1, already
recognized by the current framework. **Decision:** the only possible new
benefit is a quantitative estimate across growing domains. Recurrence,
connectivity restatements or a favorable finite plot are insufficient.

## The initial shortlist reached its stop conditions

**A. Arithmetic relational histories — V2 + V9.** The
[two-family test](experiments/viewpoints/V002/relational_test.md) found that
R81 already supplies the proposed guarded merger relation and R93 already
supplies a compact asynchronous invariant. Dropping guards admits illegal
histories; treating a shifted coordinate as a path drops an actual residual.
No new closure implication was obtained. Keep this representation as a tool;
reopen the direction only with a specific additional consequence.

**B. Arithmetic graph geometry — V6 through V4.** The
[boundary test](experiments/viewpoints/V002/geometry_test.md) proves an inverse
conductance tail at most `4/(3n_0)` from its first omitted source. It holds on
the cycle controls too. A small height domain misses the excursion of 7;
a domain containing its supplied path gives positive voltage after membership
has already been supplied. Outgoing escapes and cumulative occupation remain
uncontrolled. Keep finite approximation tools, but no geometry-only follow-up
without a specified global estimate.

These are scoped demotions of the tested proposals, not impossibility theorems
for either mathematical field. They are why the second round added V11–V14.

## Focused subsequent programme

The language-selection deliverable ends with the following bounded programme.
It does not require executing that programme or starting an extended proof search.

| Priority | Bounded next investigation | Evidence needed to continue | Stop or redirect when |
|---|---|---|---|
| 1 — V13 | Check primary automata/functional-equation literature; write the ternary sections of an invariant sequence with finite binary kernel | A precise existing classification, a new finite closure implication, or a specific missing family of sections | Only the already-known two-base theorem is recovered, or regularity of the actual bad set is assumed |
| 2 — V14 with V13 | Trace one finite conversion rectangle and list its complete frontier, zero tail and bootstrap; compare with guarded affine data | A demonstrable relation between boundary data or sections that the endpoint description obscures | The diagram merely redraws the history or silently fixes an unknown/infinite boundary |
| Alternative — V12 | Compare the specified capped first-passage law with Tao's exact hypotheses, retaining failure mass and selection bias | A named estimate that can plausibly be obtained for actual integer seeds | Fresh independent bits, stationary input laws, or uniform residue counts are assumed after conditioning |

**V13 intermediate target.** Classify finite-valued, base-2-automatic solutions
of `h(2n)=h(n)` for `n>=1` and `h(3n+1)=h(n)` for odd `n>1`.
A sufficient approach would prove a finite ternary kernel from a finite binary
kernel and these identities. We currently have only the section identity
`h(3n+2)=h(2n+1)` for `n>=1`, not the required closure. Classifying this
restricted function class does not establish regularity of arbitrary component
indicators and therefore supplies no universal convergence inference.

**V14 intermediate target.** Assess the published small-cycle problem
`T^k(x)!=x` for `x>2`, `1<=k<=ceil(log_2 x)` in the **shortcut** clock.
This leaves divergence and longer cycles. First establish that a boundary
argument contributes something beyond the periodic affine equation. The
d=5 check on this card is an external arithmetic control; no generalized
d=5 tile construction has been tested.

**V12 intermediate target.** For logarithmic odd seeds in `[X,2X]`, retain
the first endpoint at most `X^(1/4)`, capped at `ceil(10 log X)` odd arrows.
Seek an explicit power bound for both the failure probability and the collision
mass of non-1 endpoints, for all sufficiently large integer X. Its card states
all constants and quantifiers as a candidate, not a proved estimate. It leaves
the fate of the endpoints and exceptional seeds unresolved.

After these bounded checks, compare their outputs before choosing deeper work.
If V13 yields only an unsupported regularity assumption and V14 no compression,
broaden again; do not grow an automata case catalogue to preserve the choice.
V2 remains the arithmetic bookkeeping layer, V4 the survival observable, V10
the control index, and V11 the check against losing mass at infinity.

## Decision rules

- A successful language must improve a checkable proof obligation or expose
  useful structure, not just carry the same missing premise under another name.
- Finite calculations test the translation. They do not establish uniform
  bounds, termination, integer realization of infinite words or novelty.
- Keep both real size and arithmetic legality when needed; preserve signs,
  source weights, exact endpoints, absorber conventions and all clocks.
- A claim must behave correctly on the d=5 and d=61 cycle controls. The
  failure of a general argument there must occur at a named hypothesis.
- Fixed-word periodic exclusions are partial cycle results. They say
  nothing by themselves about aperiodic divergence.
- A recommendation is provisional and revisable. Its evidence must distinguish
  useful organization from a claimed advance on convergence. No long proof
  campaign follows automatically from selecting a working language.

## Evidence and scope

Primary references are beside the imported claims in the cards. The
[exploration log](docs/VIEWPOINT_LOG.md) records actual checks, the reviewed
side commit and the frozen-code boundary. These notes are exploratory
comparisons and elementary worked calculations, not additions to R1–R94.
The open LaTeX document and existing dispatcher remain unchanged.
The [selection review](experiments/viewpoints/V002/SELECTION_REVIEW.md) maps the
goal requirements to the actual cards, comparisons and checks. The independently
reviewed finite-period argument is the main new diagnostic in this exploration;
the automatic-coloring theorem, boundary closure and statistical estimate remain
proposed subsequent work.
