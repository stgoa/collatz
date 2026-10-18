# Phase 6 route map

**Historical route map.** The user replaced route-first proof search with
[breadth-first viewpoint exploration](VIEWPOINT_MAP.md) on2026-10-18.
The decisions below describe the completed Phase6 programme; they do not
constrain the new survey or instruct continued C.2a work.

**2026-10-18. Collatz remains open.** This is the preserved Phase6 research map.
S.1 now has a written quantitative calibration; universal stopping is open. The user has authorized
autonomous node selection and revision. R1–R94 and the seventeen-family
dispatcher are frozen at main `9190ccf2519acc56446dd027c6cbf8d45dcceeb6`.

The seed proposals are D1–D4 in the read-only side lane at
`f244b7a5b77a51f8dd7e6bccf2c6d5f18932df88`. The
[ledger](docs/PHASE6_LEDGER.md) answers every proposal and records grading.
The [literature audit](docs/PHASE6_LITERATURE.md) distinguishes published
theorems from the additional work required here.

## Last Phase6 research decision (superseded as active priority)

P6-004 supplies **C.1a's external lower theorem through an independent
source build, exact statement comparison and axiom audit**. Continue at
**C.2a's actual-nonabsorbing-set upper estimate**. The separate written
reconstruction retains Tao's mixing input. P6-004's finite residue attempt
did not establish the upper estimate; it is recorded as none. S.1 was pushed as546e891 and is independently
confirmed. P6-002's cardinality obstruction was pushed asde32608. P6-003
now excludes arbitrary-target contraction in every power-growth norm with
0<alpha<1; its full gate passed. This closes the current uniform-norm
method. S.1 supplies its finite first-crossing code directly. The audited
2026 formal theorem lowers the sufficient counting requirement from a
power saving to C.2a's statistical condition. That condition remains
equivalent to convergence. See the [audit and evidence](experiments/phase6/linear_density_audit/README.md).
Do not add dispatcher families or collect exponent variants of this barrier.

Each calibration must name the open-node step it feeds. Under accepted D6,
a route gets at most one calibration before an attempt on S.2, C.2, Y.2 or
H.2, respectively; a barrier counts. A second calibration without that
intervening attempt is none. S.1 has already fed the S.2 transport attempt.

Routes S, C and H each have a stated path to full convergence. Route Y
addresses cycles only; a separate divergence argument would still be needed.
Inclusion in the map does not certify any open node.

## Definitions and transfer conventions

- `S(n)=(3n+1)/2^v2(3n+1)` on positive odd integers, absorbed at 1.
  All unnamed times count these odd arrows. For a general positive integer
  seed, first take its odd part; those initial halvings are not charged.
- `nu` and `T` are the frozen R25 elementary normal form and quotient map,
  with `T nu = nu S`. `W5={w>0: w=5 mod8}`, `P(w)=[3w]-[w]`,
  and `rho(w)=nu(3w)`. Currents are finite signed integer edge functions;
  `[1]=0` is the killed absorber convention. Missing currents are premises.
- For transfer controls, `S_d(n)=(3n+d)/2^v2(3n+d)`, with positive odd
  `d` coprime to 6. Raw cycles and the version killed at 1 are distinguished.
  No `nu_d`, `T_d`, or `rho_d` is silently imported from `d=1`.
- **Transfers** means the same assertion on the specified domain, with the
  displayed parameter replacement, has an argument. **Fails** means an exact
  counterexample to that assertion. **Unestablished** means neither is supplied.
  A control for ordinary descent does not test a quotient-specific formula.
  Scaling by `d` changes the integer lattice; rational covariance is insufficient.
- Every proposed Phase 6 result must name a node and a proposed label:
  **(a) non-transfer step**, **calibration**, **barrier**, or **none**.
  The first requires an implemented named failing step in
  `python3 scripts/verify_all.py --transfer-controls`; the second requires a
  re-derived published theorem with explicit constants; the third requires
  a proof excluding a named method for the node. Finite success rates and
  new conditional interfaces alone receive **none**.

## R — frozen reduction interfaces

### R.1 — Universal pair supply

**Statement.** Collatz holds iff every `w in W5` has a finite exact current
for `P(w)`. Equivalently, for every positive odd `u`, the ordinary orbits of
`u` and `18u+5` meet, at possibly unequal finite times.

**Status:** written reduction, frozen R40/R43. With `w=4u+1`,
`S(w)=S(u)` and `S(3w)=18u+5`. The current/meeting equivalence is for finite
signed currents and actual integer states. The
[reviewed derivation](experiments/residual_progress/side_lane_review_678e565.md)
contains the exact scope. Universal supply remains the missing premise.

**Transfer:** graph-current/meeting equivalence transfers to deterministic
graphs. The displayed W5 and `18u+5` arithmetic is specific to `d=1`;
universal supply is not obtained by scaling. Its full `d` analogue is
unestablished in this map.

**Closest published result:** the classical orbit/convergence problem and
functional formulations surveyed in L5; no published identification with
this exact repository W5 compiler is claimed.

### R.2 — Sufficient stopping threshold, universally equivalent target

**Statement.** For every `w in W5`, put `q=rho(w)>=7`. There exists a finite
quotient time `k>=0` such that

`9 T^k(q)+5 < 8q`.

**Status:** the universal assertion is open and Collatz-equivalent by the
[existing argument](experiments/residual_progress/side_lane_review_33c3829.md).
The bound supplies a strict-rho plan, and strong induction supplies its
smaller inputs. Conversely convergence reaches 1, satisfying the bound.
This is not a necessary local test for every possible current construction,
nor an equivalence between finite search algorithms. Root 1 is excluded
from the quantified starting domain.

**Transfer:** unestablished for this exact quotient/rank interface.
Ordinary descent at nonprincipal `3x+d` cycle minima fails, as S.2 controls
show; this is not a fabricated test of an undefined `T_d`.

**Closest published result:** stopping-time formulations and the
Terras/Everett density theorems, L1. Their exceptional set is the remaining
difficulty, not a supplied proof of this universal assertion.

## S — stopping route

### S.1 — Calibrate fixed-factor stopping and its W5 pullback

**Status:** written calibration in [P6-001](experiments/phase6/stopping_calibration/STOPPING_CALIBRATION.md),
with exact executable checks; final verification is recorded in the ledger.

**Statement:** the following published-result corollary now has explicit errors: for each rational `0<epsilon<1`, exhibit an odd-arrow
horizon `K(epsilon)` and cutoff `X0(epsilon)` such that for all
`X>=X0(epsilon)`, at most `epsilon` times the number of odd seeds through X
have no `k<=K(epsilon)` with `S^k(n)<=n/2`. State finite small-seed exceptions
explicitly. Then justify the separate passage to density-one W5 inputs
satisfying R.2, controlling normal-form fibres and every cutoff error.

**Proof interface:** with k=5m, the bad raw shortcut parity fraction is at
most `(8/7)(16807/18432)^m`. The proof retains the affine intercept and
integer residue-counting error at every cutoff. It uses modulus `2^k` for
shortcut parity words; exact odd-valuation cylinders still require their
extra bit. R37 makes `w -> rho(w)` injective on W5, and R25 supplies the
same-index semiconjugacy. No general density-preservation assumption is used.

**Transfer:** the ordinary theorem is proved for every fixed positive odd
d coprime to 6, with the same horizon and d-dependent cutoff. The W5/nu
pullback still has no supplied verbatim d analogue. The result is not
almost-all absorption at 1 and coexists with the control cycles.

**Closest published result:** Borovkov–Pfeifer Corollary2, equation(11),
whose finite-horizon half-descent densities tend to1; see L1. Korec's
Theorem1 also gives eventual half-descent by taking exponent4/5 and n>=32.
Tao's logarithmic-density
almost-bounded theorem, L2, is a stronger but differently quantified
benchmark; it cannot be substituted for a natural-density power bound.

**Label:** calibration, confirmed by the side lane at0ed286c5. The
initial setup remains none. S.2 remains open; there is no iteration of this
density estimate or conclusion that its exceptional set is empty.

### S.2 — Remove every exceptional input

**Open obligation:** prove R.2 for every positive `w in W5`, or give an
alternative universal finite-current supply with a proved termination
argument. State any replacement interface before relying on it.

**Transfer:** the ordinary universal descent analogue
`for all odd n>1, some S_d^k(n)<n` fails at nonprincipal cycle minima.
The harness tests precisely that analogue on certified cycles, including
`19 -> 31 -> 49 -> 19` for `d=5`, and tests finite d=1 baselines.
The exact quotient statement remains untested for d other than 1.

**Closest published result:** L1 and L2, with their exceptional-set
qualifiers. Neither removes every exception.

**Potential outcomes:** (a) only for a new proved step whose stated
`d` analogue actually fails in the harness; barrier for a named proposed
method with a proof. Repackaging R.2 or adding finite accepted cases is none.

**Current named-method test (P6-002):** define L(n) as the first odd iterate
at most n/2 and M_X(y) as the number of odd n<=X whose L endpoint is y.
Test whether one finite kappa and one remainder r(X)=o(X) can satisfy
`sum_(y in A) M_X(y) <= kappa |A| + r(X)` uniformly over every eligible
A subset of odd (1,X/2]. The [written one-arrow obstruction](experiments/phase6/stopping_transport/STOPPING_TRANSPORT.md)
excludes every finite kappa, even after discarding any fixed finite target
set; it transfers to all supported fixed d. At d=1 the sparse refinements
also reject cardinality-proportional bounds with o(X^alpha) errors, even
under hereditary sparse counts. This barrier concerns the stated premise.
P6-002 alone leaves global growth norms open; P6-003 addresses them next.
Full verification is recorded in the ledger.

**Global norm test (P6-003):** define `||A||_alpha=sup_X A(X)/X^alpha` and
G_d(A) as the first-half preimage set. The [written proof](experiments/phase6/growth_norm_transport/GROWTH_NORM_TRANSPORT.md)
shows that for every fixed supported d and every real0<alpha<1 there is a
fixed infinite finite-norm A with `||G_d(A)||_alpha>||A||_alpha`. It also
rejects coefficients<=1 with o(X^alpha) error, even depending on A. Finite
homogeneous crossing words, exact inverse residue classes and a large
fixed target offset retain all affine terms. Only the four-word subtheorem
has the explicit241/240 factor through alpha7/8. At d=1 the one-arrow
operator contracts by10/13 for4/5<=alpha<1; that bound cannot be iterated
as a bound for G. The full norm's finiteness remains undecided.

**Next attempt:** exploit the actual nonabsorbing set B, which satisfies
B=E disjoint-union L^(-1)(B), rather than arbitrary targets. Any proposed
bound must state exactly how B-invariance changes the estimate and why its
claimed discriminating step fails on a certified d-cycle. No such bound is
currently supplied. Other norms, signed currents and the other routes
remain available. Closest sources are L1's finite-cylinder stopping
estimates and L2's concentration issue; no novelty claim is made.

## C — predecessor counting route

### C.1 — Calibrate a lower bound for every non-ternary target

**Published statement, in the subcase needed here:** for each fixed positive
odd integer `a` not divisible by 3, the number of positive integers `n<=X`
whose odd-only orbit from `oddpart(n)` visits a is
at least `X^0.84` for all sufficiently large X, with the threshold depending
on a. Krasikov–Lagarias prove the stronger all-positive-target statement
in the shortcut clock; odd targets have the same reachability in our clock.
See L3 for the precise published domain and clock.

**Open calibration obligation:** independently reproduce the relevant
certified inequality system and make the threshold/constants needed for
C.3 explicit. Published existence of an a-dependent threshold is enough
for the logical C.3 contradiction; it is not an already reproduced explicit
calibration. Use all positive integer predecessors, not just odd ones.

**Transfer:** unestablished for the exponent and quantifiers stated here.
The inverse-tree arithmetic must be checked; neither generic covariance
nor the presence of a cycle settles this lower-bound statement.

**Closest published result:** Krasikov–Lagarias (2003), L3, directly.

### C.1a — Audit the new linear predecessor-density input

**Supplied external theorem, with recorded trust boundaries.** Put
`L=2^(2^(2^87640))`. For each positive target a with3 not dividing a,
every integer `X>=2^(a^3 L)` has at least `X/(a^4 L)` distinct odd
predecessors below X. For odd a the accelerated endpoint is a; for even a
it is oddpart(a), while the ordinary path reaches a. No convergence or
nonperiodicity assumption on a is used.

**Source and scope:** the pinned Lau formal development in L3a was rebuilt
independently. Four public statements matched an independently named copy
of the challenge; all eight axiom reports contain only propext,
Classical.choice and Quot.sound. The [evidence](experiments/phase6/linear_density_audit/README.md)
separates source compilation, cached dependencies and fresh-kernel replay.
The full Hexagon article was unavailable, so the adopted exact statement
is the accessible formal challenge. Our separate written qualitative
derivation is conditional on Tao's mixing theorem; it does not rederive
Lau's numerical analytic chain. Programme label: none under the strict
rederivation requirement.

**Transfer:** the qualitative lower-density assertion is proved in the
written reconstruction for every fixed positive d coprime to6 and every
positive target a with3 not dividing a. Lau's numerical constants and
clocks are not claimed to transfer. Thus this lower premise is not(a).

**Feeds:** C.2a, whose first residue-counting attempt is persisted in
P6-004. A positive leading-density mode survives that stated relaxation.

### C.2a — Eliminate a positive-density nonabsorbing basin

**Open candidate obligation:** for every rational epsilon>0 and every
integer M>=1, find finite integers X>=M and H>=0 such that at most epsilon*X
of the positive integers n<X have tau_1(oddpart(n))>H. Times count absorbed
odd arrows. There is no claimed uniform logarithmic bound on H.

**Implication using C.1a:** a nonabsorbing target would force
at least cX bad starts at every sufficiently large X. Choosing epsilon<c
contradicts the obligation. Conversely Collatz supplies a finite H for every
finite cutoff; choose X large enough to handle the excluded0. Thus this is
an alternative universal obligation, not a consequence of positive density
of absorbed starts or of stopping below the initial value.

**Transfer:** the upper premise fails at supported d>1 because multiples of
d never reach1. Exact controls must exercise any new claimed proof step.
The qualitative C.1a lower premise transfers under its stated mixing input;
its explicit numerical strengthening has only been replayed at d=1.

**Closest source:** L3a for the conditional density criterion. No proof of
this upper condition is supplied. A possible first test uses a truncated
counting norm of the actual invariant set B, without assuming a finite
global norm; that test is still only a candidate. The exact two-level
residue system retains advanced cutoffs and valuation tails but admits a
positive-density leading profile. See the [failed bounded attempt](experiments/phase6/linear_density_audit/c2a_attempt.md).

### C.2 — A power bound for the remaining seeds

**Open obligation:** produce constants `0<epsilon<0.84`, `C>0`, `X0`, and
a finite computable integer horizon `H(X)` such that for every integer
`X>=X0`,

`#{1<=n<=X : tau_1(oddpart(n))>H(X)} <= C X^(0.84-epsilon)`.

Here `tau_1` is the absorbed odd-arrow hitting time, equal to infinity for
a nonconvergent orbit. No monotonicity of H is needed; its clock and any
growth bound must be stated. This is much stronger than density zero.

**Transfer:** fails for every fixed `d>1` in the control domain: positive
multiples of d remain multiples of d and never hit 1. There are exactly
`floor(X/d)` such integer seeds. The harness verifies the invariant's
arithmetic and fixed-d cycle witnesses; it does not test every hypothetical
proof of the power bound. The obstruction does not require an extra cycle.

**Closest published result:** Tao's almost-bounded theorem, L2, and the
stopping-time results L1 are benchmarks with substantially weaker/different
conclusions. No published C.2 bound is being imported.

With C.1, C.2 is already Collatz-equivalent: convergence would permit the
computable maximum of the finite stopping times of seeds through X as H(X).
Calling it a counting target does not weaken its universal difficulty.

### C.3 — Turn the two bounds into a contradiction

**Interface:** C.1 plus C.2 implies convergence. On a hypothetical
nonabsorbing odd orbit choose `a=S(n)`. Then `3` does not divide a, since
`3n+1` is a ternary unit. Every positive integer predecessor of a is
nonabsorbing. Thus `X^0.84 <= C X^(0.84-epsilon)` for all sufficiently
large X, impossible once `X^epsilon>C`.

**Status:** elementary conditional argument; C.2 is not supplied. Counting
all integers avoids confusing published inverse counts with odd-only seed
counts. Initial removal of powers of 2 changes clocks but not membership.

**Transfer:** the abstract incompatible-counts implication transfers when
its hypotheses hold; the concrete C.2 hypothesis fails in the controls.

**Closest published result:** L3 supplies the lower-bound side only.
This setup writes the dependency, with label none, not a new breakthrough.

## Y — cycle route, insufficient by itself for Collatz

### Y.1 — Audit the published finite-minimum exclusions

**Calibration obligation:** reproduce a specified published exclusion of
nontrivial cycles with bounded numbers of local minima, with its explicit
constants, computational assumptions and original clock. The primary
reference audit must include corrections to the published proof.

**Transfer:** the `3x+1` numerical exclusions do not hold verbatim for the
certified `3x+d` cycles. The underlying inequalities may transfer after
changing constants; a named distinguishing step is still required.

**Closest published result:** Hercher's 2023 result excluding at most 91
local minima, read together with its 2026 corrigendum, and the earlier
Simons–de Weger 68-minimum result; precise scope in L4. These are published
benchmarks, not reproduced certificates of this Phase 6 batch.

### Y.2 — Exclude every nontrivial canonical periodic itinerary

**Open obligation:** show there is no finite positive T-cycle except `{1}`.
Any word-based proof must specify all admissible words, reconstruct exact
ordinary arrows, and establish the required integer-lattice condition.
The frozen R71 mechanical-word theorem addresses only its stated subclass.

**Transfer:** an unrestricted no-cycle assertion fails for the raw `S_d`
controls. The harness recognizes their full cycles and minima, including
all three cycles containing 1 as terminal baselines under absorption.
No generalized canonical normal form is assumed.

**Closest published result:** L4 and the restricted cycle literature;
the repository's R71 is frozen input, not a new Phase 6 result.

**Remaining obligation:** even a proof of Y.2 leaves unbounded positive
orbits. It must be combined with a separate no-divergence proof, for example
S.2, C.2 or H.2. A cycle-only result must never be called convergence.

## H — invariant functions and analytic rigidity

### H.1 — Retain the exact graph duality

**Interface:** a finite pair current exists iff every invariant function
on the killed deterministic graph has the same values on the two sources.
Equivalently their forward orbits meet. An invariant is constant on each
whole orbit component and zero at the absorber. Indicators of exposed
finite components are not automatically invariants of the full graph.

**Status:** frozen graph-current interface; the corresponding general-source
criterion tests component sums. Pair cancellation need not mean absorption.

**Transfer:** the graph statement transfers, including to graphs with
cycles. There, different-component indicators are genuine obstructions.

**Closest published result:** Berg–Meinardus and the functional-equation
discussion in L5. This finite-support graph statement is not an automatic
analytic rigidity theorem or an invocation of unspecified functional analysis.

### H.2 — A precisely stated canonical rigidity target

Let K be the positive canonical roots of R25. For a bounded real sequence
`(h_q)_(q in K)` with `h_1=0`, form
`F(z)=sum_(q in K) h_q z^q`, analytic for `|z|<1`.

**Open obligation:** show that the coefficient relations
`h_(T(q))=h_q` for every `q in K` force `F=0`.
Every hypothetical nonabsorbing component supplies a bounded 0/1 solution,
so this target is Collatz-equivalent. Analyticity inside the unit disk alone
is already automatic and gives no missing rigidity. Any additional
regularity assumption must be proved for these component indicators.

**Transfer:** the ordinary-graph analogue fails in the presence of a
nonprincipal cycle by its basin indicator. The quotient-specific `d`
version is unestablished; no analytic mechanism has yet been registered
in the harness. Do not infer failure or success of one from another.

**Closest published result:** L5, with its exact function space and
equivalence distinguished from this proposed quotient coefficient space.

**Potential barrier:** prove that a named proposed regularity condition
does not follow from the available coefficient relations. An equivalent
reformulation without such a result receives none.

## Batch contract

For the selected node, state the attempted lemma and label before assessing
it; persist the proof, exact tests, transfer assessment and literature match.
The side lane confirms or disputes the label in its feed. Until then the
ledger says **pending**, never independently confirmed by main itself.
Do not wait for its verdict. Resolve disagreements with evidence; if one
remains open, record both positions and continue using independent judgment.
After three none batches on one node, write a one-page post-mortem, weigh
the latest side-lane directions and switch to the most promising node. Run
that post-mortem immediately if the user says the work seems stuck.

Never wait for user approval between batches. Finish verification, commit
and push each batch to origin/main, then begin the next. The setup batch
built the map, ledger, transfer harness and rules and was pushed as b901e11.
It is confirmed none at MAP. P6-001 supplies the verified S.1 calibration; S.2 is the next selected node.
Its bounded-prefix preparation was redundant with frozen R25/R31 and is
recorded as none. Continue with input-dependent unbounded histories.
