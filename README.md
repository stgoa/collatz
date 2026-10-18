# Collatz research

This repository is the persistent record of the Collatz programme: definitions, proofs, failed approaches, finite certificates, and executable checks. Future work should start here rather than reconstructing the programme from chat memory.

**Current standing (2026-10-18): Collatz remains unproved. Phase 6 is active.**

**Parallel-work review:** the remote currently lists PR1 as the only merged
PR; it is already incorporated with corrected minimality claims. The latest
side feed independently confirms P6-003's barrier, and its probe was reproduced
here. We are continuing the counting-route pivot: audit the stronger
predecessor-density input, then attack the actual nonabsorbing set. See the
[current decision](docs/PHASE6_LEDGER.md#user-requested-pr-review-and-mid-batch-side-refresh).

R1–R94 and the seventeen-family dispatcher are frozen at `9190ccf`. The living [route map](ROUTE_MAP.md) now controls research priorities. The [Phase 6 ledger](docs/PHASE6_LEDGER.md) records batch grades, side-lane decisions and disputes; the [literature audit](docs/PHASE6_LITERATURE.md) records primary references. The setup is confirmed **none**. **S.1 has a verified, independently confirmed calibration with explicit stopping constants and a W5 pullback.** S.2 now has a written barrier to uniform cardinality transport (P6-002, full gate passed) and a stronger written barrier to contraction in **every power-growth norm with exponent below 1** (P6-003, full gate passed). The latter uses the calibration directly: a finite family of first-descending paths concentrates on some sparse target set. Universal stopping remains open.

## Frozen mathematical standing

Universal finite tripling-pair currents on `w=5 mod8` suffice. Our conditional compiler retains auxiliary `w=9 mod16` pairs and keeps every missing input explicit. We now retain both actual source histories and classify the lower path's first departure across every repetition count of the upper growth pattern. The resulting comparison still has an unresolved positive source. A proposed recursion to `Q(floor(ell/3))` provably requires unbounded ordinary clocks. Universal terminal supply remains unresolved; the route map now determines which proof obligations to pursue. These results have no human peer review or formal verification.

## Our current understanding

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

## What counts in Phase 6

Every attempted result must attach to a named route-map node with one of three labels:

- **(a) Non-transfer step:** a proved step whose stated `3x+d` analogue fails on a known cycle, exercised by the transfer harness.
- **Calibration:** a published result re-derived with explicit constants.
- **Barrier:** a proof that a named method cannot close the node.

Everything else is **none**. Finite acceptance rates and new conditional interfaces alone do not discharge a universal obligation. The side lane confirms or disputes proposed labels; main records the evidence and continues without waiting. After three none batches on one node, write a post-mortem and select another node. The stopping, counting and harmonic routes have stated paths to convergence; the cycle route alone does not.

## Where to start

1. Read [AGENTS.md](AGENTS.md) for working rules and claim standards.
2. Read [ROUTE_MAP.md](ROUTE_MAP.md) and the [Phase 6 ledger](docs/PHASE6_LEDGER.md), then the [result ledger](docs/RESULTS.md) for exact scope, evidence, and unresolved obligations.
3. Read the [current proof note](collatz_research_20261017/right_aligned_reduction.tex). Open this source in the document editor for its PDF preview.
4. Consult the [master handoff](COLLATZ_PROGRAMME_MASTER_HANDOFF.md) for the wider programme and historical counterexamples. Its old active target is superseded only for the revised right-aligned family.

Each batch fetches the read-only `claude/sidekick` branch and reads both `sidekick/DIRECTIONS.md` and `sidekick/FEED.md`. Answer every open direction in the Phase 6 ledger with accept/defer/reject and a reason. Verify findings before using them; never write to that branch. Verified batches are committed and pushed to origin/main without an approval wait.

## Reproduce the finite checks

Requires Python 3.10+ and its standard library. The independent check additionally requires a C++17 compiler (`c++`, or set `CXX` to a compiler executable).

```sh
python3 scripts/verify_all.py --cpp --transfer-controls
```

Without a compiler, omit `--cpp`; the report explicitly records that the independent C++ check was not run. The runner verifies the archive and all 31 manifest entries, stored certificates, the right-aligned and five-ray audits, annular identities, partial constructions, norm formula, component diagnostics, and the independent lane's negative-control and audit receipts. It uses temporary storage so preserved inputs and receipts stay unchanged. With `--cpp`, it also builds and runs the independent verifier at both original stored cutoffs.

The added transfer flag replays [exact cycle controls](experiments/phase6/README.md), with declared domains, absorber conventions and fail-closed cap handling. It augments the historical gate. It does not automatically test an unregistered proof mechanism.

Most checks establish finite arithmetic identities. R91 and R92 additionally use complete finite rational-basin classifications inside their computer-assisted proofs. R92's default replay checks the smaller congruence-selected universe; `--cpp` independently classifies the entire larger interval as well as reproducing R91 and the original stored cutoffs. None of these checks establishes universal current existence. Never use Python optimization flags for these assertion-based verifiers.

## Repository map

- `ROUTE_MAP.md`: active living proof skeletons and selected node.
- `docs/PHASE6_LEDGER.md`: batch grading, transfer status and side-lane decisions.
- `docs/PHASE6_LITERATURE.md`: primary references and exact comparison scopes.
- `experiments/phase6/`: controls, receipts and current report.

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

## Next research target

The [S.1 calibration](experiments/phase6/stopping_calibration/STOPPING_CALIBRATION.md) feeds the [S.2 power-growth proof](experiments/phase6/growth_norm_transport/GROWTH_NORM_TRANSPORT.md): uniform contraction for arbitrary target sets fails at every exponent 0<alpha<1. One-arrow contraction alone therefore cannot justify iterating density descent. The next step audits newly found2026 claims of linear predecessor density ([L3a](docs/PHASE6_LITERATURE.md)), then targets an estimate for the actual nonabsorbing set. Those external proofs are not yet independently reproduced here. The route map records the resulting conditional counting target; Y.2 addresses cycles only and H.2 needs additional rigidity.

The overall goal remains a finite current, possibly with an everywhere nonpositive residual, at every cutoff on **all five rays**, or another proof of convergence. The [route map](ROUTE_MAP.md) supersedes old next-target paragraphs in historical reports. The [Phase 6 report](experiments/phase6/REPORT.md) records active work. No universal current construction, Collatz proof or novelty claim is supplied.
