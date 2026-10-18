# Phase 6 route map

**2026-10-18. Collatz remains open.** This is the first Phase 6 batch: a
living research map, not a new convergence result. The user has authorized
autonomous node selection and revision. R1–R94 and the seventeen-family
dispatcher are frozen at main `9190ccf2519acc56446dd027c6cbf8d45dcceeb6`.

The seed proposals are D1–D4 in the read-only side lane at
`f244b7a5b77a51f8dd7e6bccf2c6d5f18932df88`. The
[ledger](docs/PHASE6_LEDGER.md) answers every proposal and records grading.
The [literature audit](docs/PHASE6_LITERATURE.md) distinguishes published
theorems from the additional work required here.

## Current research decision

Start with **S.1, a calibration of fixed-factor
stopping**, including explicit finite error terms and the separate pullback
to W5. Its purpose is to establish exactly what the density machinery gives
before attempting S.2 or the stronger counting obligation C.2. Reproducing
a published result is calibration, even when useful to the programme.
Do not add more dispatcher families during this phase.

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

**Open obligations.** Re-derive the following published-result corollary
with explicit errors: for each rational `0<epsilon<1`, exhibit an odd-arrow
horizon `K(epsilon)` and cutoff `X0(epsilon)` such that for all
`X>=X0(epsilon)`, at most `epsilon` times the number of odd seeds through X
have no `k<=K(epsilon)` with `S^k(n)<=n/2`. State finite small-seed exceptions
explicitly. Then justify the separate passage to density-one W5 inputs
satisfying R.2, controlling normal-form fibres and every cutoff error.

**Dependencies:** exact parity/valuation cylinders, including their extra
bit; clock conversion; an integer counting estimate for the pullback.
An asymptotic cylinder rate with a modulus growing with X is insufficient.

**Transfer:** ordinary fixed-factor stopping for each fixed `d` is a
candidate for transfer of the parity argument, with `d`-dependent additive
constants; the complete quantitative version must be checked. The W5/nu
pullback has no supplied verbatim `d` analogue. This is not a statement of
almost-all absorption at 1.

**Closest published result:** the half-descent corollary of Korec's Theorem 1
(take exponent 4/5 and n>=32), using the Terras/Everett method, L1.
Tao's logarithmic-density
almost-bounded theorem, L2, is a stronger but differently quantified
benchmark; it cannot be substituted for a natural-density power bound.

**Expected label:** calibration only after the proof and explicit constants
are written and verified. This setup batch is none. Even successful
calibration leaves S.2 open.

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
and push each batch to origin/main, then begin the next. This first batch
builds the map, ledger, transfer harness and rules. Setup is none at node
MAP and does not consume an attempted S/C/Y/H-node batch. S.1 is selected
for the next batch after the verified setup is pushed.
