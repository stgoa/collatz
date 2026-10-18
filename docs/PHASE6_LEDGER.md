# Phase 6 ledger

**Historical programme ledger.** The active goal is now
[viewpoint exploration](../VIEWPOINT_MAP.md). P6-004 is closed; its grading
and the former next-node choice below are retained as history.

The Phase6 plan is preserved in [ROUTE_MAP.md](../ROUTE_MAP.md). Collatz remains open.
R1–R94 and the seventeen-family dispatcher are frozen at main
`9190ccf2519acc56446dd027c6cbf8d45dcceeb6`.

Labels are proposed by main; confirmation or dispute comes from the side
lane's feed. A pending verdict does not block the next batch. No confirmation
is inferred from an earlier review of different work. Programme labels do
not replace written-proof / finite-certificate / open status.

## Batch register

| Batch | Node | Proposed label | Confirmation | Transfer status | Literature match |
|---|---|---|---|---|---|
| P6-000, 2026-10-18: map and controls | MAP; baseline controls attached to S.2, C.2, Y.2 | **none** — setup and existing-obligation counterexamples | **Confirmed none** by the side lane at `b1785fb2dcf121586e99be95c90b94afcf1e9733`, feed 15:38; cycle fixtures independently replayed there | Exact raw cycles refute ordinary universal descent / absorption / no-cycle analogues; quotient-specific transfer unestablished | [L1–L5 audit](PHASE6_LITERATURE.md); no published theorem re-derived in this batch |
| P6-001, 2026-10-18: explicit stopping calibration | S.1 | **calibration** — published half-descent corollary with explicit constants and W5 pullback | **Confirmed calibration** at side pin `0ed286c5e92f739f610f4aad2d460d0afc63eab6`, feed16:13, reviewing committed main546e891 | Ordinary estimate proved for each fixed positive odd d coprime to6; W5/nu/T pullback only at d=1 | Borovkov–Pfeifer Corollary2 finite-horizon half-descent limit, with conservative explicit errors; Korec fixed-half corollary; full power theorem not re-proved |
| P6-001, secondary preparation | S.2 | **none** — bounded-prefix obstruction already follows from frozen R25/R31 | **Confirmed none** in the same feed16:13 review | No new transfer claim | Frozen growth examples; no new exclusion mechanism |
| P6-002, 2026-10-18: first-half transport | S.2 | **barrier** — no uniform arbitrary-target constant-cardinality bound, even with sublinear error | **Confirmed barrier** at side pin `602386cac0070d673ff2d831102ae02ca2b0a439`, feed16:32, reviewing committedde32608 | Main obstruction transfers to every fixed supported d; sparse refinements proved for d=1 | Tao §1.1 concentration issue; exact named inequality and elementary construction specified here, no novelty claim |

| P6-003, 2026-10-18: power-growth norm | S.2 | **barrier** — no arbitrary-target contraction for any real0<alpha<1 | **Confirmed barrier** at side pin `e4f82311a804ecd1befaaa5e255e41c6d5d0c44c`, feed16:56, reviewing committed2e619a2; side probe independently reproduced | Full obstruction transfers to each supported fixed d; one-arrow upper bound proved only for d1 | Finite-cylinder stopping in Borovkov–Pfeifer; Tao valuation lemma and concentration issue; exact norm statement proved directly, no novelty claim |

| P6-004, 2026-10-18: linear predecessor-density audit | C.1a | **none** under the strict explicit-constant rederivation rubric; independent formal reproduction is recorded separately | Pending side review | Written qualitative lower theorem transfers to fixed positive d coprime to6; Lau's numerical constants are only audited at d1 | Mazur's weighted-history/counting argument rederived conditional on corrected Tao v7; pinned Lau formal source independently rebuilt with exact statement and axiom checks |
| P6-004, upper-bound attempt | C.2a | **none** — positive leading-density mode survives the specified residue relaxation | Pending side review | The proposed upper premise fails on the multiples-of-d controls; it remains unproved at d1 | Krasikov–Lagarias inverse inequalities supply lower counts, not this upper constraint; Tao almost-boundedness does not fill the gap |

**Consecutive none counts:** MAP 1 (setup), S.1 0, S.2 0, C.1 0, C.2 0,
C.1a 1, C.2a 1, C.3 0, Y.1 0, Y.2 0, H.1 0, H.2 0. A later mathematical attempt on a node
must be counted even if it produces useful code or a clearer formulation.
Three none batches trigger a written post-mortem and an autonomous pivot.
S.2 has two retained redundant attempts across P6-001/002; P6-002's primary
proposed barrier resets its consecutive-none batch count, subject to the
recorded side-lane grading process.

## P6-000 — Decision and exact scope

**Reviewed side commit:** `f244b7a5b77a51f8dd7e6bccf2c6d5f18932df88`.
Both DIRECTIONS and FEED were read after fetching. The first four open
directions are answered below. New feed arithmetic checks and Q1/Q2 finite
exposure observations were read as context, not imported as asymptotic
theorems or rerun in this setup. Earlier reviewed reductions remain frozen.

| Open direction | Decision | Reason and implementation |
|---|---|---|
| D1 — seed the route map with R/S/C/Y/H | **accept** with explicit scope corrections | All five routes are represented. R.2 retains q>=7 and is an existence equivalence, not algorithmic necessity. C.2 counts all positive seeds with a stated odd clock and remains Collatz-equivalent with C.1. H.2 specifies the coefficient space instead of importing an unspecified analytic theorem. The map is living and main selects nodes autonomously under the user's updated goal. |
| D2 — transfer harness before outcome (a) | **accept** | Every registered test names its predicate, domain and failed step. Eleven supplied raw cycle minima are independently replayed; only eight are nonprincipal negative controls. The three cycles through 1 are terminal baselines. New mechanisms must register their own step; passing this baseline does not grant label (a). |
| D3 — almost-all results count as calibration, with blanket density transfer | **reject** the blanket proposal; retain its scoped calibration principle | Re-deriving published density results with explicit constants is calibration. But almost-all absorption at 1 does not transfer to d>1: multiples of d have positive density and never hit 1. Fixed-factor stopping needs its own proof and d-dependent constants. A genuinely non-transferable step is judged by the actual harness and proof, not by whether its statement includes a density. |
| D4 — tag all R1–R94 by transfer | **defer** | Ninety-four individual domain/proof audits would delay the first live node. Tag frozen inputs when a selected node uses them. Rational covariance changes the integer lattice, so no blanket “all transfer” conclusion is adopted. R71's denominator criterion remains a possible Y.2 input; hypothetical divergence is not testable by cycle fixtures alone. |

**Research choice:** next pursue S.1 calibration, with explicit finite
counts, odd-arrow clock and W5 pullback. This is chosen for a checkable
benchmark and a precise account of the exceptional set. It is not advertised
as a likely proof of S.2. The stronger C.2 target and the separate cycle and
harmonic routes remain available for later evidence-driven pivots.

**Durable evidence:** [control specification](../experiments/phase6/README.md),
[checker](../experiments/phase6/transfer_controls.py),
[cycles](../experiments/phase6/cycle_fixtures.json), and
[receipt](../experiments/phase6/transfer_controls_audit.json).
The new harness distinguishes raw S_d from absorption at 1, rejects missing
or malformed fixtures and capped results, and preserves finite d=1 positive
controls. The old packet controls use their own `{1,d}` absorber convention;
their frozen conclusions are unchanged.

**Verification:** focused replay, fifteen rejection checks and the full
`python3 scripts/verify_all.py --cpp --transfer-controls` gate passed with
exit 0. The [stored verification record](../experiments/phase6/setup_verification.json)
contains the complete gate report and pinned input/code hashes. Independent
arithmetic replay verified all eleven cycles and87 observation paths without
importing the harness. The review found and corrected C.1's target-domain
ambiguity. No frozen mathematical source or dispatcher changed. Delivery is
recorded in the accompanying Git history. No new proof of convergence,
universal current supply, or novelty claim is made.

## P6-001 — S.1 fixed-factor stopping calibration

**Main baseline:** pushed `b901e11`. **Reviewed side commit:**
`b1785fb2dcf121586e99be95c90b94afcf1e9733`, fetched and DIRECTIONS/FEED read
at the start of this batch. The feed confirms P6-000's label none and eleven
cycle fixtures, accepts the D3 correction and records D1–D4 as answered.
No new open mathematical direction appears in DIRECTIONS.

| Direction follow-up | Decision | Reason |
|---|---|---|
| D1/D2, now accepted | **accept**, unchanged | The living map and exact harness are in pushed b901e11. |
| D3, correction accepted by side lane | **reject** the historical blanket assertion, unchanged | Fixed-factor stopping and absorption at 1 have different transfer behavior. The retained old paragraph in DIRECTIONS is not reinstated as a premise. |
| D4, still deferred | **defer**, unchanged | This batch audits exactly the frozen R25/R37 interfaces used by S.1. |
| D5, moot no-waiting change | **accept**, already implemented | b901e11 removed approval gates under the user's updated goal. Side-lane proposals do not restrict the user's ability to steer the programme. |

**Attempted result and proposed label:** calibration of the published
half-descent corollary, with explicit finite horizon, integer cutoffs and
W5 pullback. It does not re-prove Korec's stronger power theorem. The ordinary
argument is parameterized by each fixed positive odd d; the W5 conclusion
uses only the frozen d=1 quotient. The [written proof](../experiments/phase6/stopping_calibration/STOPPING_CALIBRATION.md),
[constructor](../experiments/phase6/stopping_calibration/calibration.py),
[checker](../experiments/phase6/stopping_calibration/check_calibration.py) and
[exact receipt](../experiments/phase6/stopping_calibration/calibration_audit.json)
persist the result. Independent proof and integer-only parameter reviews
passed. The full gate passed with exit0 and116 report fields; its
[verification record](../experiments/phase6/stopping_calibration/verification.json)
retains the report and checked source hashes. The side lane subsequently
confirmed calibration at0ed286c5, feed16:13, reviewing committed546e891.
Its independent arithmetic agrees; this is external confirmation, not formal
verification or a new theorem imported into main.

For tolerances 1/2,1/10,1/100, the explicit ordinary odd-arrow horizons are
85,170,295; the W5 quotient horizons are240,330,455. Every cutoff is stored
as an exact integer. They are large conservative thresholds, not small-seed
performance claims. For each tolerance the assertion is uniform over all
integer cutoffs above its threshold. Choosing increasingly small tolerances
does not remove every exceptional input or give a single universal horizon.

Focused checks cover24,570 complete parity words,49,140 lifts,504 integer
cutoffs,200 tail bounds,18 direct parameter records and3 W5 records,
4,608 clock identities,1,024 W5 inputs and12 rejected invalid/capped calls.
Independent review reconstructed all21 parameter records with integer-only
cross products, and verified the proof separately from these finite tests.
R25/R37 source hashes are pinned; no frozen mathematical files changed.

**Next node:** S.2, whose exceptional-input obligation remains unproved.
C.2's absorption count is not inferred from this stopping calibration.

**Secondary S.2 attempt, none:** a proposed proof that finitely many
bounded-prefix stopping tests cannot cover W5 was independently checked,
then rejected as a new advance: the exclusion already follows from frozen
R25/R31. The proposed positive-density cylinder does not change that
mechanism. Count this conservatively as the first none batch at S.2.
The next attempt must allow input-dependent unbounded histories; another
finite dispatcher catalogue would not address the missing obligation.

## P6-002 — First-half transport and the exceptional basin

**Main baseline:** pushed `546e891`. **Reviewed side commit:**
`ade50f97bf187003f25fbc4d9e5430b53d2f2527`; fetched and both DIRECTIONS/FEED
read at the start of this batch. The new feed entry confirms P6-000 at its
committed pin and closes D5. It has no verdict on P6-001. No new open
mathematical direction appears.

| Direction | Decision | Reason |
|---|---|---|
| D1/D2 | **accept**, unchanged | The living route map and controls remain the active interfaces. |
| D3 | **reject** the historical blanket paragraph, unchanged | The correction above that retained paragraph remains valid; no blanket density transfer is imported. |
| D4 | **defer**, unchanged | Use frozen results only with a targeted audit; no blanket94-result transfer claim. |
| D5 | **accept**, closed | Main continues without waiting for side confirmation or user approval. |

**Attempted S.2 lemma:** test whether first-half descent can be iterated by
an arbitrary-target unweighted counting inequality. For its exact endpoint
multiplicities M_X(y), ask for a finite constant kappa and a uniform error
o(X) satisfying sum over A of M_X(y) <= kappa times |A| plus the error,
for every subset of odd endpoints through X/2. Independent algebra review
strengthened the initial kappa>=2 obstruction: **no finite kappa works**.
An explicit collection of one-arrow inverse branches gives endpoint/source
ratios growing with the number of allowed valuation exponents. Any fixed
finite target set, including1, can be excluded. The proof transfers to each
fixed positive odd d coprime to6. Proposed label: **barrier**, not (a).
The written proof and exact checker also refute cardinality-proportional
bounds with o(X^alpha) error on sparse targets, including a fixed target
sequence with a hereditary power count. This does not refute a bound in a
global growth norm C*X^alpha or one exploiting the actual bad set. Full verification passed with exit0.

**Secondary attempt, none/redundant:** full backward components meet every
finite binary/ternary residue cylinder. A proposed congruence-closure
separation argument therefore supplies no new result: frozen
[SUFFICIENT_SETS_AUDIT.md](../experiments/residual_progress/sufficient_sets/SUFFICIENT_SETS_AUDIT.md)
already audits the stronger Monks arithmetic-progression sufficiency.
Retain the real height and source-capacity gap rather than repackage this
fact as a new barrier. This is the second retained redundant attempt at S.2; P6-002's primary
transport result has a separate proposed barrier label.

**Other directions considered:** Lagarias's stronger stopping-tail count
will be recorded as a published benchmark, not silently converted into a
count of nonabsorbing seeds. The total-variation/single-atom route is
deferred while this concrete transport premise is audited.

**Written result and evidence:** [proof](../experiments/phase6/stopping_transport/STOPPING_TRANSPORT.md),
[checker](../experiments/phase6/stopping_transport/check_transport.py) and
[receipt](../experiments/phase6/stopping_transport/transport_audit.json).
The exact identity B=E disjoint-union L^(-1)(B) exposes the needed inverse
count. The main obstruction uses finitely many one-arrow valuation levels
at each cutoff, with all multiplicities disjoint. The sparse refinements
also retain every lower-cutoff count. They do not establish B nonempty at
d=1. They reject the universal cardinality premise rather than every
possible recurrence for B.

Three independent model reviews of proof and code passed. One final scope
correction confines the sparse refinements to d=1; only the main o(X)
obstruction is asserted uniformly for supported fixed d. Focused replay
passed150 general cases/2640 arrows,12 exact linear gaps,9 sparse cases,
227 hereditary counts/864 arrows, two finite basin classifications and11
rejection checks. No frozen source/proof/receipt changed. The full
`python3 scripts/verify_all.py --cpp --transfer-controls` gate passed with exit0
and117 report fields, including the independent C++ checks. The
[verification record](../experiments/phase6/stopping_transport/verification.json)
retains the complete report and checked source hashes. Remote main remained
546e891 before delivery; the accompanying Git history records commit/push.

**Next-node decision prepared:** continue at S.2 with its global power-growth
norm, after the next side refresh. Four concrete first-half words give a
candidate expansion that differs from the cardinality barrier just proved;
the [report](../experiments/phase6/REPORT.md) retains its exact formula and
candidate status. Defer C.1's large certificate reconstruction and H.2's
currently missing regularity premise. Neither alternative supplies an
extra hypothesis for this batch.

## P6-003 — Global power-growth norm transport

**Main baseline:** pushed `de32608`. **Reviewed side commit:**
`0ed286c5e92f739f610f4aad2d460d0afc63eab6`; fetched and DIRECTIONS/FEED
read at batch start. The new feed independently confirms P6-001's
calibration and secondary none labels at committed546e891. It contains no
P6-002 verdict. Its finite arithmetic agrees with main's independent proof
and gate. The qualitative comment about logarithmic horizons is not adopted
as a universal barrier to other counting methods.

| Direction | Decision | Reason |
|---|---|---|
| D1/D2 | **accept**, unchanged | Living routes and exact controls remain active. |
| D3 | **reject** the historical blanket paragraph, unchanged | Stopping and absorption at1 retain distinct transfer behavior. |
| D4 | **defer**, unchanged | Audit frozen inputs when actually used. |
| D5 | **accept**, closed | Continue without approval waits; the user retains steering authority. |
| D6 | **accept** | At most one calibration per route before an attempt on its open node; each calibration names the step it feeds. A second calibration without an intervening attempt is none. S.1's explicit stopping counts already feed P6-002's S.2 transport attempt, followed here by the remaining growth-norm test. A scoped barrier counts as an attempt. |

**Written attempt:** the [proof](../experiments/phase6/growth_norm_transport/GROWTH_NORM_TRANSPORT.md)
and exact checker separate a contracting one-arrow operator from its full
first-half transport. The all-exponent scope is now proved; full verification passed.
The proposed label is barrier, not(a); arbitrary targets and the actual
nonabsorbing set must remain distinct.

Theorem3 strengthens the initial four-word obstruction to every real
0<alpha<1. A finite prefix-free homogeneous first-crossing code has mass
arbitrarily close to1 by S.1. Averaging its weights over exact inverse
residues gives a class with expansion above1. A fixed positive offset makes
every compatible path an actual first-half descent, retaining intercepts
and all source multiplicities. The fixed sparse target sequence has an
exact global norm. Thus arbitrary-target power norms cannot supply the
proposed contraction, even allowing a target-dependent o(X^alpha) error.
The constructed target need not be the nonabsorbing set. The norm of its
full inverse image may be infinite; the proof does not decide this.

**Next decision:** close this uniform power-norm method and attempt a
B-specific estimate using exact invariance, with explicit transfer controls.
Do not add more exponent variants or repackage the obstruction as universal
impossibility. C.1 and H.2 remain alternatives with the costs recorded in
the report. Side-lane confirmation of P6-002/003 remains pending.

**Independent review:** the base proof/checker and the all-exponent extension
passed independent model review. One convention clarification was applied:
parity cylinders use the raw map; the finite target threshold then ensures
selected actual paths avoid1 and follow the absorbed map. Focused replay
covers1920 four-word paths,10752 one-arrow norm checks,276 independently
enumerated small code words,1752 raw residue seeds,390 inverse paths and
residue counts, two exact large code masses, two S.1 feed records, and29
rejections across the two checkers. The two large masses were independently
recomputed with a separate dynamic program. The full gate passed with exit0
and118 report fields, including all historical/C++ and transfer controls.
The [verification record](../experiments/phase6/growth_norm_transport/verification.json)
pins its report and checked sources. Remote main remainedde32608 before
delivery; the accompanying Git history records the commit and push.

**Next-choice revision during verification:** a fresh primary-literature
search found the2026 linear predecessor-density claims pinned in L3a.
They are not mathematical premises of this batch. Preliminary local proof
reading supports auditing their inherited analytic input; no independent
formal build is claimed. Select C.1a's input audit next, feeding a C.2a
attempt if verified. This supersedes the provisional S.2-only next choice
above and defers reconstruction of the older0.84 certificate. C.2a's upper
condition remains open; no extra calibration label is earned by this find.

The preliminary source audit also checked the newer endpoint implementation
and the companion's stated mixing-to-counting chain. No hidden convergence
hypothesis was found in the inspected steps. Its reported full local import
rebuild still reuses third-party dependencies and has not been independently
replayed here. C.1a remains an audit obligation rather than a supplied premise.

**Retained next-attempt preparation, no additional result label:**
[NEXT_ATTEMPT.md](../experiments/phase6/NEXT_ATTEMPT.md) records the proposed
actual-B truncated-norm inequality, conditional consequences and its d>1
negative control. The inequality is unproved. Its finite maxima avoid
assuming the desired global growth bound; none of this supplies C.2a.

## P6-004 — C.1a input audit started

**Main baseline:** P6-003 verified and pushed as `2e619a2`.
**Reviewed side commit:** `602386cac0070d673ff2d831102ae02ca2b0a439`;
fetched and both DIRECTIONS/FEED read at batch start. New feed16:32 confirms
P6-002's barrier at committedde32608 with independent arithmetic. No P6-003
verdict appears. Its heuristic comment about logarithmic weighting is not
an additional uniform transport theorem and is not imported as one.

| Direction | Decision | Reason |
|---|---|---|
| D1/D2 | **accept**, unchanged | Named routes and exact controls remain active. |
| D3 | **reject** the historical blanket paragraph, unchanged | Stopping and fixed-target absorption have different transfer behavior. |
| D4 | **defer**, unchanged | Audit the inputs needed by the selected node. |
| D5 | **accept**, closed | Continue without waiting; the user retains steering authority. |
| D6, still shown open in side file | **accept**, reaffirmed | Persisted in P6-003; C.1a's audit must feed a C.2a attempt. A source inspection alone is not a calibration. |

**Work started:** audit the new linear predecessor-density premise and its
explicit refinement at the pinned sources in L3a. Status is in progress;
no result label is assigned yet. The route's next upper estimate is retained
in NEXT_ATTEMPT.md with its missing transport inequality explicit. No Lean
or Lake executable is presently on the command path; source inspection is
not a substitute for independent formal replay. No installation or external
source execution has occurred in this preparation.

### User-requested PR review and mid-batch side refresh

The remote PR listing again returns only [PR1](https://github.com/stgoa/collatz/pull/1),
merged at `ba6b3371fabd7fcabebb442d7c89ea3ed5c02149` and already incorporated.
Remote main remains `2e619a2`. The latest independent work is on the separate
read-only side branch, now reviewed at
`e4f82311a804ecd1befaaa5e255e41c6d5d0c44c`. Both direction and feed changes
were read. Its feed confirms P6-003's barrier. The unmodified side probe
was reproduced in temporary storage with a 45-second cap: 27,773 target
cases and 120,000 exact count comparisons, with the stored JSON matching
byte for byte. The [replay receipt](../experiments/phase6/side_lane_review_e4f8231.json)
pins the source and receipt hashes. These finite checks support the separate
written proof; they do not supply a new convergence theorem.

**PR opinion:** retain C1/C2/C4's checks and negative controls, and C3's
minimality lemma with its finite exact comparison and cycle hypothesis.
The PR description's claim that alternative certificates cannot help is
too broad. The existing [scope review](../collatz_research_20261017/negative_controls/PR1_REVIEW.md)
has exact counterexamples; its bounded checker was rerun successfully.
At `A_768`, 56 distinct integer one-sided certificates have the same minimum
positive cost 53758. The working repository already contains this correction.

**Pivot decision:** keep the current C.1a-to-C.2a pivot. C2/C4 disqualify
early compression as a termination argument; the separately proved
P6-002/003 barriers close two particular uniform transport methods. They
do not exclude arbitrary signed-current constructions. Audit the claimed
linear predecessor lower bound, then seek a bound specific to the actual
nonabsorbing set. Both necessary inputs remain open in this repository.
No additional batch label is earned by this review.

| New direction | Decision | Reason |
|---|---|---|
| D7 — audit standard for external results | **accept** for promoting the C.1a formal result to a premise | Match the exact statement; independently build pinned sources in isolation; inspect theorem axioms and any native computation. Author/registry build reports and source reading alone do not satisfy independent replay. |

D1/D2/D5/D6 remain accepted, D3's blanket transfer claim remains rejected,
and D4 remains deferred for the reasons above. D6 is now marked accepted
in the side file. The new D7 decision does not pause the parallel C.2a
attempt, and no external theorem has been promoted to a verified premise.

### P6-004 outcome — lower input supplied; upper estimate remains open

**Working baseline after the PR review:** `44a2745`. The reviewed side pin
remains `e4f82311a804ecd1befaaa5e255e41c6d5d0c44c`; all direction decisions
above remain in force. No side-lane confirmation is inferred for this batch.

The [written audit](../experiments/phase6/linear_density_audit/README.md)
rederives the seed-uniform weighted histogram, summable central variation,
endpoint-dependent terminal shift, distinct-source count and coverage of
all sufficiently large cutoffs. Tao's corrected v7 Proposition1.14 is an
explicit input. The normalization factor is2/3, and its marginal identity
keeps the full1<=m<=q domain. Multiplicities, residue endpoint errors, both
terminal errors and the nonreturn seed selection are retained. Independent
model reviews of these arguments and their checker passed. The qualitative
argument extends to each fixed positive d coprime to6 and target a with
3 not dividing a; it is not a non-transfer step and does not carry over
Lau's numerical constants.

The Lau source pin is `3a38bfbb70379e051b51155def1423846fab3a90`. Its exact
public statement uses L=2^(2^(2^87640)), c(a)=1/(a^4 L), and
X0(a)=2^(a^3 L). Every sufficiently large integer cutoff counts distinct
odd predecessors, with ordinary and accelerated logarithmic clocks. The
formal challenge has been semantically reviewed and compared by compiling
an independently named copy of all four statements and definitions. It
imports Solution.Basic, not the challenge's placeholders. All eight actual
axiom reports contain exactly propext, Classical.choice and Quot.sound.
The explicit Solution.Basic build passed4102 jobs inside the reviewed
network-denying macOS sandbox. Every original archive file matched the
pinned archive; source files were unchanged during compilation.

D7 is satisfied for adopting this **formal-source statement**, under the
recorded compiler/dependency trust boundary. The full Hexagon article was
unavailable, so no full article-correspondence claim is made. Cached
Mathlib dependencies were not all rebuilt from source. Fresh-kernel replay
also completed with exit0 and PASS, as recorded in the
[formal replay record](../experiments/phase6/linear_density_audit/formal_replay.json). It uses the same Lean kernel implementation; it is
not a second-kernel check. The receipt runner preserves the initial build,
binds stage inputs and proof objects, and rejects missing predecessor
edges, altered logs and incomplete/nonstandard axiom reports. Eleven
focused integrity tests passed after one missing-edge validation defect
was corrected; the focused independent review passed.

**Grade:** none under the literal current rubric. Our written reconstruction
still imports Tao's unspecified analytic constants. Independently replaying
Lau's supplied numerical derivation is useful verification, but it is not
our independent rederivation of that numerical Fourier/renewal chain. The
new external premise can be used without awarding a new calibration label.

**C.2a attempt:** the complete two-level inverse identity requires finer
ternary lifts, an advanced a=1 cutoff, and a retained infinite valuation
tail. Its specified leading-coefficient relaxation admits the positive
profile b_u^j=lambda/(2*3^j), even after any finite base is removed at leading
order. That relaxation cannot prove the proposed strict contraction. This
is a failed attempt at the actual-B upper constraint, not a refutation of
that constraint or of all finite-state methods. The separate matched
lower/upper density comparison is only next-attempt preparation; its
required strict inequality remains missing.

**Verification:** the full `python3 scripts/verify_all.py --cpp --transfer-controls`
gate passed with exit0 and119 report fields. The [verification record](../experiments/phase6/linear_density_audit/verification.json)
pins the runner, checker and receipt bytes. An earlier run ended with143
and an empty log; its cause is unknown and it was not counted as PASS.
The new finite checker covers three central histories,64 histogram fibers,
10 marginal laws, eight signed transfer identities,108 branch/tail checks,
six density-mode cases, four d-controls and six rejections. These checks
support the written ingredients; they do not certify the external theorem
or supply the missing upper bound. No frozen result or LaTeX source changed.

**Next:** proceed at C.2a using the now supplied lower premise. Any new upper
argument must distinguish actual Collatz absorption from the positive-density
control sectors. Do not repeat the failed leading-profile relaxation or
infer the matched density comparison from Tao's qualitative tail limit.
