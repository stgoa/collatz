# Collatz research

This repository is the persistent record of the Collatz programme: definitions, proofs, failed approaches, finite certificates, and executable checks. Future work should start here rather than reconstructing the programme from chat memory.

## Current programme: cycle denominators across 3x+d

**Current standing (2026-10-19): C002 gives a uniform cycle exclusion:
different valuation blocks with the same length m and total A, repeated
k and ell times with k+ell>=3, have reduced denominator greater than
2^m whenever 2^A>3^m. The blocks and their lengths may vary freely.
All-cycle exclusion and Collatz convergence remain open.**

The user replaced the quantitative-rigidity goal with the
[cycle-spectrum goal](docs/CYCLE_SPECTRUM_BRIEF.md). Integer cycles across
the positive `3x+d` family are organized by the reduced denominators of
rational `3x+1` cycles. The question is which word structures can make
that denominator equal 1. Rotations and repetitions must be distinguished
from new primitive cycles.

[C002's report](experiments/cycle_spectrum/C002/REPORT.md) gives the proof,
an explicit finite enumeration bound for every bounded denominator layer
within that class, and a complete fixed-pair growth result for two repeated
blocks. Proportional slopes have an elementary bound; unequal slopes use
published S-unit estimates and have no effective threshold here. The
common-cycle exception is retained. Arbitrary cycle words need not have
the covered structure, so the universal gap remains explicit.

The checker replays all 2,459 cycles over 333 parameters from
[C001](experiments/cycle_spectrum/C001/REPORT.md), then checks 433,074
positive word-cycle realizations at 5,003 parameters. Large cancellation
really occurs; thirteen failures of a proposed constant bound are saved.
Neither experiment is an exhaustive cycle census. A primitive nonbalanced
subfamily has unbounded minima and local-minimum counts; no general
published-record improvement, novelty or formal verification is claimed.

**Next:** seek a denominator restriction that survives changing the
blocks' totals, with a precise structural class and actual-cycle controls.
Increasing a fixed catalogue alone would not address that uniformity
gap. The [cycle log](docs/CYCLE_SPECTRUM_LOG.md) records the active work;
each batch must include actual-cycle tests and a theorem or an exact
obstruction. The separate Lean lane's reported checks strengthen the
validation record; they do not supply the missing cycle restriction.

## Previous language programme: arithmetic regularity

The following overview records the previous sequence of goals. Its
quantitative target is still unresolved and has been replaced as the
active objective. V004 excludes finite-state nonconstant invariants.
V009 proves an unbounded additive excess over the generic count D+1;
it does not exclude every linear bound.

The [quantitative brief](docs/QUANTITATIVE_RIGIDITY_BRIEF.md) asks for an
unbounded ratio of section count to binary depth for every nonconstant
invariant. [V005](experiments/viewpoints/V005/REPORT.md) proves local
reconstruction and rejects two growth shortcuts.
[V006](experiments/viewpoints/V006/REPORT.md) proves a quadratic bound if
even one positive section depends only on binary digit count. No argument
supplies such a section for an arbitrary invariant; an exact linear-growth
control shows why extraction from weaker premises fails.
[V007](experiments/viewpoints/V007/REPORT.md) now excludes a finite interior
with a single exit anywhere in the full section graph. It uses all radix
relations and proves infinitude in both bases at every section.
[V008](experiments/viewpoints/V008/REPORT.md) refutes the generic extension
to two exits with an actual sequence example. The full Collatz equations
do exclude that small configuration at the initial state, by an elementary
case argument, but no asymptotic rate improves. Future work must use the
global growth bound or propagate more of the root equations, rather than
exclude boundary sizes one by one. The complete all-invariant bound
remains the completion requirement. The Collatz applications in V005–V007
inherit the published Cobham theorem through V004; V008's first-shell
argument has a direct constant-output finish.

[V009](experiments/viewpoints/V009/REPORT.md) now excludes an eventual
single-state binary tail by controlling all returns to earlier states.
Thus `kappa_h(D)-(D+1)` tends to infinity for every nonconstant invariant.
This still allows `D+sqrt(D)` and does not prove an unbounded ratio.
A separate generic theorem uses the global linear-growth hypothesis:
every nonzero linear combination of depth-A mixed sections would have
to be detectable with `O_C(sqrt(A+1))` input digits. Producing longer
delays, or extending the return contraction beyond single-state layers,
are the next mechanisms to compare. Both written arguments have agent
review; no novelty or formal-verification claim is made.

We explored Grothendieck-style changes of viewpoint through **breadth before
depth**. Fourteen views and two rounds of bounded comparisons support a
provisional choice: ask how complicated an arithmetic description of a
nonabsorbing component would have to be. No language is being presented as
a proof or a promised breakthrough.

Start with the living [VIEWPOINT_MAP.md](VIEWPOINT_MAP.md) and
[exploration log](docs/VIEWPOINT_LOG.md). The survey spans symbolic arithmetic,
operators, geometry, rewriting, statistical laws, automata and base conversion.
Each card records seven evaluation fields; deferred cards may offer only a
milestone template. The [selection review](experiments/viewpoints/V002/SELECTION_REVIEW.md)
records the evidence and limitations of the final recommendation.

The [full-classification brief](docs/GLOBAL_RIGIDITY_BRIEF.md) raised the
completion threshold after V003's partial theorem. The
[V004 proof](experiments/viewpoints/V004/GLOBAL_RIGIDITY.md) now meets it:

1. Retain binary sections with **strictly positive offsets**. They form a
   finite family closed under both binary and ternary sections.
2. Cobham's published theorem makes the odd section eventually periodic.
3. An elementary residue argument removes the exceptional initial terms
   and forces every color to agree.

This rules out every finite-state binary description separating Collatz
components. No automaticity of the actual nonabsorbing set has been proved.
Proving that automaticity would now be equivalent to proving convergence;
it must not be presented as an intermediate next milestone.

The proof has independent agent review and reproducible finite checks.
The separate Lean lane reports a formal derivation conditional on Cobham;
main inspected its statement and matching source receipt but has not
independently replayed it. See the [scope assessment](experiments/viewpoints/V005/side_review.md).
Human peer review and novelty are unclaimed. The
[V003 results and counterexample](experiments/viewpoints/V003/REPORT.md)
remain valid historical evidence. The carry-boundary probe is closed;
integer-ensemble statistics remain an alternative language. See the
[goal review](experiments/viewpoints/V004/GOAL_REVIEW.md) for exact scope
and the distinction between completion of this theorem and the next goal.

**Preserved evidence:** R1–R94 and the seventeen-family dispatcher are frozen
at `9190ccf`. The earlier [route map](ROUTE_MAP.md) supplies obligations and
failures without restricting this exploration. Phase6 proved two scoped
obstructions to uniform transport estimates. Its final
[P6-004 audit](experiments/phase6/linear_density_audit/README.md) independently
reproduced the formal lower-density theorem, including exact statements,
axioms and fresh same-kernel replay. The required upper estimate remains
open. Those results and all counterexamples remain available.

The independent side lane remains read-only input. PR1 is already
incorporated with corrected minimality claims; it does not rule out all
alternative current constructions. Current source pins and decisions are
recorded in the exploration log.

## Frozen mathematical standing

Universal finite tripling-pair currents on `w=5 mod8` suffice. Our conditional compiler retains auxiliary `w=9 mod16` pairs and keeps every missing input explicit. We now retain both actual source histories and classify the lower path's first departure across every repetition count of the upper growth pattern. The resulting comparison still has an unresolved positive source. A proposed recursion to `Q(floor(ell/3))` provably requires unbounded ordinary clocks. Universal terminal supply remains unresolved; the new exploration compares languages for addressing such obligations. These results have no human peer review or formal verification.

## What the existing current framework captures

The programme converts an exact stopping-work discrepancy into a finite signed measure on actual Collatz states. Balanced source packets allow positive and negative contributions to cancel, including contributions that arrive at a common state at different times. A finite current certificate can be checked using one-step arithmetic without resolving the future of its exits.

Grouping **depth-one source triples from the right** leaves endpoints only in `{5, 7, 11, 13}`, all of which reach 1 within five odd-only steps. The remainder is therefore controlled at every time horizon.

For this revised family, a written maximum-principle proof shows:

> It suffices to give finite current certificates at every cutoff
> `N = a * 2^b`, where `a ∈ {12, 14, 16, 18, 21}` and `b >= 3`.
> Certificate size and positive cost may depend arbitrarily on N.
> A finite current with an everywhere nonpositive residual also suffices.

The proof compares the exceptional-seed count using a weight that depends on the ray and scale. Its contraction factor is strictly below `89/90`. This supersedes the earlier requirement to certify every integer cutoff; all five rays still contain infinitely many cutoffs.

For every multiple of 8, `Pi_right_(64N) = Pi_right_N + A_N`. The added measure occupies six bands above the old support, with known coefficients periodic modulo 18. The five rays split into **30 sequences under multiplication by 64**. Their finite starting cases have been discharged by verified absorption. Constructing currents for all their annular increments is therefore a concrete sufficient target.

These criteria are equivalent to Collatz; they do not prove the universal certificates exist. The original handoff's packets and current tables are a different family. A proved obstruction also rules out uniformly bounded certificates for individual raw packets, while allowing cancellation between packets and constructions of unbounded size.

## Frozen research frontier through R94

- **Both actual source histories now have an exact exit interface.** The [two-source construction](experiments/residual_progress/two_source_history/TWO_SOURCE_HISTORY.md) reduces the original pair to `[864z-257]-[z]` after18 upper and16 lower ordinary arrows. A complete448-state rational certificate controls the lower path until its first departure, with exact cylinders for every upper repetition count. It stays below the original rank through that departure and eleven further arrows. The positive source remains above rank; this is an unfinished comparison, not terminal supply.
- **The proposed ternary child needs genuinely unbounded clocks.** For every digit and every fixed bound on both ordinary clocks, the [child-history theorem](experiments/residual_progress/child_history_scope/CHILD_HISTORY_SCOPE.md) constructs a whole positive progression where `Q(ell)` and `Q(floor(ell/3))` cannot meet within that bound, even after any prescribed initial growth count. This excludes finite word catalogues for that particular child. Other children, unbounded histories and general signed currents remain available.
- **Later-target controls preserve the distinction between methods.** The [complete ray/point probe](experiments/residual_progress/later_target_probe/LATER_TARGET_PROBE.md) gives exact failures at two later targets. The older forward rule already repairs one of them at the original rank. A failed inverse method must not be mistaken for absence of a current comparison.
- **Fourteen further steps still return only the original source.** The [deeper-window theorem](experiments/residual_progress/deeper_window/DEEPER_WINDOW.md) classifies all canonical origins p<=Q reaching the repeated target through12r+19 quotient steps, for every eligible source and every return count r. The sole solution is p=Q at12r+18. An exact congruence reduces the proof to33,995 rational origins and16 boundary tails; a separate C++ enumeration of176,754,119 origins agrees. This closes the saved next-window candidate. Longer histories, later targets and other signed comparisons remain open.
- **Leaving a growth pattern is not yet descent.** The [complete exit control](experiments/residual_progress/phi_exit_control/PHI_EXIT_CONTROL.md) gives the exact binary countdown, all 19 exit rows, every next-valuation cylinder, and the full signed plan at the original Q. All high requests in the fresh forward plan are positive. Fixed exit templates eventually fail the raw-height test as the initial repetition count grows; native normalization can still help in some cases. This is complete arithmetic control of the exit interface, with terminal supply still missing.
- **Smaller histories can meet above the original target.** The [first construction](experiments/residual_progress/native_history/HIGH_HISTORY.md) works where inverse-only searches fail. We now know its [complete fixed-word arithmetic cell](experiments/residual_progress/history_lifting/HISTORY_LIFTING.md), can [classify every smaller history within supplied ternary precision](experiments/residual_progress/history_frontier/HISTORY_FRONTIER.md), and have [successful subfamilies beyond any prescribed number of native growing returns](experiments/residual_progress/native_growth_escape/NATIVE_GROWTH_ESCAPE.md). Coverage of the entire exit type remains missing.
- **The recursion uses one consistent rank.** The [critical-basis compiler](experiments/residual_progress/critical_basis/CRITICAL_BASIS.md) retains W5 and W9 pairs and translates the older rank rules before combining them. Every signed dependency is explicit. Each accepted expansion strictly lowers the positive integer rank. A finite conditional plan becomes an actual current only after every remaining signed input is supplied; universal supply is still open. The older seventeen-family W5 dispatcher remains unchanged.
- **The parallel lane is useful independent scrutiny.** PR1's negative controls are incorporated. Its broad claim that alternative certificates cannot help has explicit counterexamples in our [review](collatz_research_20261017/negative_controls/PR1_REVIEW.md). The [latest pinned reproduction](experiments/residual_progress/side_lane_review_8ed32bc.md) now independently agrees with both R91's1,732,883-origin basin and R92's176,754,119-origin basin, including the16 boundary tails. It does not verify R92's suffix proof or supply a new current. The [previous review](experiments/residual_progress/side_lane_review_86ead16.md) covers the merged PR and older arithmetic probes. These checks support the tactical pivot toward whole-family supply and termination.

## Historical Phase6 grading

This rubric records the previous programme; it does not grade or restrict
the current viewpoint exploration. Within Phase6, every attempted result must attach to a named route-map node with one of three labels:

- **(a) Non-transfer step:** a proved step whose stated `3x+d` analogue fails on a known cycle, exercised by the transfer harness.
- **Calibration:** a published result re-derived with explicit constants.
- **Barrier:** a proof that a named method cannot close the node.

Everything else is **none**. Finite acceptance rates and new conditional interfaces alone do not discharge a universal obligation. The side lane confirms or disputes proposed labels; main records the evidence and continues without waiting. After three none batches on one node, write a post-mortem and select another node. The stopping, counting and harmonic routes have stated paths to convergence; the cycle route alone does not.

## Where to start

1. Read [AGENTS.md](AGENTS.md) for working rules and claim standards.
2. Read [VIEWPOINT_MAP.md](VIEWPOINT_MAP.md) and the [exploration log](docs/VIEWPOINT_LOG.md), then the [result ledger](docs/RESULTS.md) for exact scope, evidence and unresolved obligations.
   For the active goal, read the [quantitative brief](docs/QUANTITATIVE_RIGIDITY_BRIEF.md) and [V009 report](experiments/viewpoints/V009/REPORT.md); its completed prerequisite is the [V004 proof](experiments/viewpoints/V004/GLOBAL_RIGIDITY.md).
3. Read the [current proof note](collatz_research_20261017/right_aligned_reduction.tex). Open this source in the document editor for its PDF preview.
4. Consult the [master handoff](COLLATZ_PROGRAMME_MASTER_HANDOFF.md) for the wider programme and historical counterexamples. Its old active target is superseded only for the revised right-aligned family.

Each batch fetches the read-only `claude/sidekick` branch and reads both `sidekick/DIRECTIONS.md` and `sidekick/FEED.md`. Assess open direction proposals in the exploration log with accept/defer/reject and a reason. Verify findings before using them; never write to that branch. Verified batches are committed and pushed to origin/main without an approval wait.

## Reproduce the finite checks

Requires Python 3.10+ and its standard library. The independent check additionally requires a C++17 compiler (`c++`, or set `CXX` to a compiler executable).

The latest viewpoint examples have a separate bounded verifier:

```sh
python3 -B experiments/viewpoints/V006/verify_examples.py
```

Its [receipt](experiments/viewpoints/V006/verification.json) records finite
mixed-state distinctions and counterexample checks; it does not prove the
full quantitative goal. V003–V005's separate verifiers and receipts remain
available. The historical mathematical gate is:

```sh
python3 scripts/verify_all.py --cpp --transfer-controls
```

Without a compiler, omit `--cpp`; the report explicitly records that the independent C++ check was not run. The runner verifies the archive and all 31 manifest entries, stored certificates, the right-aligned and five-ray audits, annular identities, partial constructions, norm formula, component diagnostics, and the independent lane's negative-control and audit receipts. It uses temporary storage so preserved inputs and receipts stay unchanged. With `--cpp`, it also builds and runs the independent verifier at both original stored cutoffs.

The added transfer flag replays [exact cycle controls](experiments/phase6/README.md), with declared domains, absorber conventions and fail-closed cap handling. It augments the historical gate. It does not automatically test an unregistered proof mechanism.

Most checks establish finite arithmetic identities. R91 and R92 additionally use complete finite rational-basin classifications inside their computer-assisted proofs. R92's default replay checks the smaller congruence-selected universe; `--cpp` independently classifies the entire larger interval as well as reproducing R91 and the original stored cutoffs. None of these checks establishes universal current existence. Never use Python optimization flags for these assertion-based verifiers.

## Repository map

- `VIEWPOINT_MAP.md`: active comparison, shortlist, tests and decision criteria.
- `docs/VIEWPOINT_LOG.md`: exploration batches, source pins, decisions and verification.
- `experiments/viewpoints/`: bounded surveys and discrimination probes.
- `ROUTE_MAP.md`: preserved Phase6 proof skeletons and unresolved nodes.
- `docs/PHASE6_LEDGER.md`: batch grading, transfer status and side-lane decisions.
- `docs/PHASE6_LITERATURE.md`: primary references and exact comparison scopes.
- `experiments/phase6/`: completed controls, audits, receipts and historical report.

- `COLLATZ_PROGRAMME_MASTER_HANDOFF.md`: inherited proof map and historical context.
- `collatz_packet_currents_bundle.zip`: original supplied archive, retained for provenance.
- `collatz_research_20261017/collatz_packet_currents/`: extracted original proofs, scripts, complete finite current tables, and audit receipts.
- `collatz_research_20261017/right_aligned_reduction.tex`: current written reduction; maintain this existing document in place.
- `collatz_research_20261017/right_aligned_packets.py`: construction and finite regression checks for the revised family.
- `collatz_research_20261017/right_aligned_audit.json`: reproducible finite audit receipt.
- `collatz_research_20261017/negative_controls/`: the independent lane. It contains:
  - audits of R2–R4 and of later main claims;
  - negative controls on `3x+d` maps with real cycles;
  - certificate minimality, and progress-measure controls;
  - a certificate checker (`affine_controls.py --check`).

  The ledger entries are C1–C5. The [PR review](collatz_research_20261017/negative_controls/PR1_REVIEW.md) records the retained conclusions and corrected scope.
- `docs/RESULTS.md`: claim ledger and next proof obligations.
- `docs/RESEARCH_LOG.md`: dated record of durable changes and validation.
- `scripts/verify_all.py`: unified verification entry point.
- `experiments/current_construction/REPORT.md`: investigation handoff, proved results, failed directions, and remaining obligations.
- `experiments/current_construction/frontier/`: five-ray proof and finite base checks.
- `experiments/current_construction/recursive/`: annular coefficient table, proof, and checker.
- `experiments/current_construction/obstructions/`: component criterion, capped search, packet obstruction, and new finite current tables.
- `experiments/annular_construction/REPORT.md`: constructive continuation, exact results, failed candidates, and next proof obligation.
- `experiments/annular_construction/components/`: affine current compiler, disjoint packing, incremental graph search, and annular certificates.
- `experiments/annular_construction/arithmetic/`: short-chain catalogue, norm proof, outer-profile obstruction, and reusable combined constructor.
- `experiments/annular_construction/duality/`: component potential, exact boundary flux, residue information loss, and scoped counterexamples.
- `experiments/residual_progress/`: finite rational cone and integer-gap compiler, actual certificate conversion, and scoped residual-transport obstructions.

## Recommended next research programme

The full binary-automatic goal has its proof in V004. Its
[mechanism comparison](experiments/viewpoints/V004/GLOBAL_RIGIDITY.md#8-comparison-of-the-three-requested-mechanisms)
records the positive-section proof, the direct-automaton limitations and
the supplied Mahler systems. Further searches for the same classification
are unnecessary. The [viewpoint map](VIEWPOINT_MAP.md#focused-subsequent-programme)
records the completed target and the remaining regularity gap.

A subsequent goal must add an independently meaningful complexity theorem
or a new estimate for actual integer ensembles. It cannot simply assume
that the nonabsorbing indicator is automatic. Verification and possible
formalization of V004 are separate tasks from extending its mathematical
scope. No subsequent research goal is activated by this recommendation.

The former C.2a upper-density target remains an unresolved historical route.
Its [matched density gap](experiments/phase6/linear_density_audit/next_upper_attempt.md)
is not supplied by the audited lower theorem or by an unspecified positive
upper fraction. The [route map](ROUTE_MAP.md) and [Phase6 report](experiments/phase6/REPORT.md)
retain that programme's results. Universal currents on all five rays remain
one possible proof route. No such supply, Collatz proof or novelty claim is
made by the viewpoint recommendation.
