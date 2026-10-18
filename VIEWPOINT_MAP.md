# Find a better language for Collatz

**Active goal, 2026-10-18: breadth before depth. Collatz remains open.**
The [user-approved brief](docs/VIEWPOINT_BRIEF.md) governs this exploration.
The [batch log](docs/VIEWPOINT_LOG.md) records decisions and checks. The former
[route map](ROUTE_MAP.md) supplies evidence, without restricting the search.

## What the first pass changed

We compared ten viewpoints and made three short discrimination probes. The
strongest conclusion concerns **information loss**: a representation may make
Collatz look simpler by discarding exactly what is needed to recover an actual
positive-integer path. Restoring that information often returns us to a known
unresolved obligation.

No candidate has yet earned an extended proof investigation. Guarded affine
histories are the most faithful common representation in this comparison,
but they are already present in the programme. Calling them adelic, categorical
or abstract interpretation does not supply a new estimate. The present
shortlist is for further tests, not a claim that we have found the right language.

The frozen results remain useful: they identify which quantities cannot serve
as progress measures and provide exact difficult examples. We preserve them
while changing the questions asked of them.

## Comparison

Each linked card records objects, structural gain, translated gap, example,
cycle controls, cheapest test and a genuinely partial milestone.

| View | What becomes clearer | What remains difficult | Decision after first pass |
|---|---|---|---|
| V1. [Parity coding](experiments/viewpoints/V001/symbolic_arithmetic.md#v1-parity-coding-a-shift-with-a-difficult-arithmetic-subset) | Dynamics becomes a shift; prefixes and tails are explicit | Which infinite codes come from positive integers | Supporting language; substantial overlap with frozen prefix results |
| V2. [Mixed-place affine cocycles](experiments/viewpoints/V001/symbolic_arithmetic.md#v2-a-mixed-real2-adic3-adic-affine-cocycle) | Real size, exact binary legality, ternary endpoint conditions and offsets can be retained together | A bound coupling these data that does more than separate estimates | Keep as common arithmetic representation; the probe found no new inequality |
| V3. [Multiplicative semigroups](experiments/viewpoints/V001/symbolic_arithmetic.md#v3-multiplicative-semigroup-completion-versus-legal-path-lifting) | A relaxed factorization problem is already solved | Legal ordering and state-dependent realization | Defer: inspected induction uses an additional multiplication with an unsupplied bridge |
| V4. [Absorbing operators](experiments/viewpoints/V001/operators_geometry.md#a-absorbing-transfer-operators-and-function-spaces) | Survival of a specified input ensemble is one observable | A uniform estimate on that ensemble, without arbitrary-target contraction | Keep as measurement language; no spectral-gap claim |
| V5. [Orbit groupoids and currents](experiments/viewpoints/V001/operators_geometry.md#b-graph-currents-cohomology-and-orbit-groupoids) | Meeting lags, cycles and arithmetic labels remain visible | A useful invariant beyond existing component and current algebra | Defer bare homology or categorical reformulations |
| V6. [Dirichlet energy and potentials](experiments/viewpoints/V001/operators_geometry.md#c-potential-theory-dirichlet-energy-and-possible-boundaries) | Finite access-to-1 probabilities have comparison principles and explicit boundary flux | Quantitative arithmetic control as domains grow | Retain one bounded geometric test; no claim of superiority |
| V7. [Proof rewriting](experiments/viewpoints/V001/rewriting_renormalization.md#1-rewriting-confluence-of-proofs-versus-termination-of-dynamics) | Compatibility of certificate transformations can be checked separately | Universal discharge of the remaining leaves | Supporting tool only; confluence does not imply termination |
| V8. [Induced maps](experiments/viewpoints/V001/rewriting_renormalization.md#2-induced-maps-return-times-and-affine-cocycles) | An arbitrarily long excursion can become one parameterized branch | Exiting a guard need not reduce height or enter known history | Defer unary inducing as a separate direction; much is already done |
| V9. [Relational abstraction](experiments/viewpoints/V001/rewriting_renormalization.md#3-abstract-interpretation-and-independently-checked-summaries) | Soundness, precision and unbounded counters are explicit | A useful relation between unequal-time histories that survives composition | Retain only a test with a new compression or closure target |
| V10. [Rational denominator layers](experiments/viewpoints/V001/rational_layers.md) | Related maps become layers of one rational system; target and lattice changes are explicit | A property of the denominator-one layer that forces useful progress | Control bookkeeping; defer as an independent route |

These are related lenses, not ten independent possible proofs. In particular,
V2, V8 and V9 share affine data. V4 addresses absorption through an exact
survival observable; V6 supplies auxiliary lower bounds for absorption. Their value must be demonstrated by different
estimates or proof organization, not by counting names.

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

## Shortlist and next tests

Retain two complementary experimental portfolios, with V4 as their common
measurement language. Neither is selected for deep development.

**A. Arithmetic relational histories — V2 + V9, using V8 when useful.**
Specify one relation between two source histories, an exact concretization,
and its behavior under unequal numbers of odd arrows. Test it on one frozen
successful merger and one unresolved family. The output should be a short
closure/compression proposition, or an explicit lost relation. Stop if it
only restates an existing affine block, current identity or dispatcher case.
A credible intermediate milestone is a compositional summary valid at
arbitrary repetition count for one explicit family; other families may
remain unresolved. Do not assume all its leaves have currents.

**B. Arithmetic graph geometry — V6, audited through V4.**
First derive a uniform bound for omitted inverse-edge conductance and decide
whether it can control a growing-domain average without assuming membership
in the absorbing component. Compare two domain constructions on a small
exact example. Stop if the proposed lower bound merely enumerates already
certified histories, wires unknown exits to1, or discards escape flux.
A longer-term intermediate milestone is an explicit50% logarithmic
absorption bound for all sufficiently large integer cutoffs, allowing an
exceptional set. The audited lower theorem already supplies a tiny explicit
positive fraction; merely proving some positive fraction again is not this
quantitative target. No50% bound or all-input convergence is asserted here.

V10 is a challenge to both portfolios: identify what specifically concerns
the denominator-one integer layer. It is not permission to assume that
general rational cycles rule out, or predict, integer convergence.

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
- If both portfolios only reproduce existing results, expand the survey
  again before starting a deeper investigation. No framework has won yet.

## Evidence and scope

Primary references are beside the imported claims in the cards. The
[exploration log](docs/VIEWPOINT_LOG.md) records actual checks, the reviewed
side commit and the frozen-code boundary. These notes are exploratory
comparisons and elementary worked calculations, not additions to R1–R94.
The open LaTeX document and existing dispatcher remain unchanged.
