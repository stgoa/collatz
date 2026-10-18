# Collatz research

This repository is the persistent record of the Collatz programme: definitions, proofs, failed approaches, finite certificates, and executable checks. Future work should start here rather than reconstructing the programme from chat memory.

**Current standing (2026-10-18): Collatz remains unproved.** Universal finite tripling-pair currents on `w=5 mod8` suffice. Our conditional compiler retains auxiliary `w=9 mod16` pairs and keeps every missing input explicit. We now retain both actual source histories and classify the lower path's first departure across every repetition count of the upper growth pattern. The resulting comparison still has an unresolved positive source. A proposed recursion to `Q(floor(ell/3))` provably requires unbounded ordinary clocks. The priority remains a comparison that covers a whole remaining family, preserves the original rank and supplies every terminal input. These results have no human peer review or formal verification.

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

## Current research frontier

- **Both actual source histories now have an exact exit interface.** The [two-source construction](experiments/residual_progress/two_source_history/TWO_SOURCE_HISTORY.md) reduces the original pair to `[864z-257]-[z]` after18 upper and16 lower ordinary arrows. A complete448-state rational certificate controls the lower path until its first departure, with exact cylinders for every upper repetition count. It stays below the original rank through that departure and eleven further arrows. The positive source remains above rank; this is an unfinished comparison, not terminal supply.
- **The proposed ternary child needs genuinely unbounded clocks.** For every digit and every fixed bound on both ordinary clocks, the [child-history theorem](experiments/residual_progress/child_history_scope/CHILD_HISTORY_SCOPE.md) constructs a whole positive progression where `Q(ell)` and `Q(floor(ell/3))` cannot meet within that bound, even after any prescribed initial growth count. This excludes finite word catalogues for that particular child. Other children, unbounded histories and general signed currents remain available.
- **Later-target controls preserve the distinction between methods.** The [complete ray/point probe](experiments/residual_progress/later_target_probe/LATER_TARGET_PROBE.md) gives exact failures at two later targets. The older forward rule already repairs one of them at the original rank. A failed inverse method must not be mistaken for absence of a current comparison.
- **Fourteen further steps still return only the original source.** The [deeper-window theorem](experiments/residual_progress/deeper_window/DEEPER_WINDOW.md) classifies all canonical origins p<=Q reaching the repeated target through12r+19 quotient steps, for every eligible source and every return count r. The sole solution is p=Q at12r+18. An exact congruence reduces the proof to33,995 rational origins and16 boundary tails; a separate C++ enumeration of176,754,119 origins agrees. This closes the saved next-window candidate. Longer histories, later targets and other signed comparisons remain open.
- **Leaving a growth pattern is not yet descent.** The [complete exit control](experiments/residual_progress/phi_exit_control/PHI_EXIT_CONTROL.md) gives the exact binary countdown, all 19 exit rows, every next-valuation cylinder, and the full signed plan at the original Q. All high requests in the fresh forward plan are positive. Fixed exit templates eventually fail the raw-height test as the initial repetition count grows; native normalization can still help in some cases. This is complete arithmetic control of the exit interface, with terminal supply still missing.
- **Smaller histories can meet above the original target.** The [first construction](experiments/residual_progress/native_history/HIGH_HISTORY.md) works where inverse-only searches fail. We now know its [complete fixed-word arithmetic cell](experiments/residual_progress/history_lifting/HISTORY_LIFTING.md), can [classify every smaller history within supplied ternary precision](experiments/residual_progress/history_frontier/HISTORY_FRONTIER.md), and have [successful subfamilies beyond any prescribed number of native growing returns](experiments/residual_progress/native_growth_escape/NATIVE_GROWTH_ESCAPE.md). Coverage of the entire exit type remains missing.
- **The recursion uses one consistent rank.** The [critical-basis compiler](experiments/residual_progress/critical_basis/CRITICAL_BASIS.md) retains W5 and W9 pairs and translates the older rank rules before combining them. Every signed dependency is explicit. Each accepted expansion strictly lowers the positive integer rank. A finite conditional plan becomes an actual current only after every remaining signed input is supplied; universal supply is still open. The older seventeen-family W5 dispatcher remains unchanged.
- **The parallel lane is useful independent scrutiny.** PR1's negative controls are incorporated. Its broad claim that alternative certificates cannot help has explicit counterexamples in our [review](collatz_research_20261017/negative_controls/PR1_REVIEW.md). The [latest pinned reproduction](experiments/residual_progress/side_lane_review_8ed32bc.md) now independently agrees with both R91's1,732,883-origin basin and R92's176,754,119-origin basin, including the16 boundary tails. It does not verify R92's suffix proof or supply a new current. The [previous review](experiments/residual_progress/side_lane_review_86ead16.md) covers the merged PR and older arithmetic probes. These checks support the tactical pivot toward whole-family supply and termination.

## What would count as the next breakthrough

Construct a procedure that covers a complete remaining type, prove that it finishes for every input of that type, and supply every terminal current it requests. Its depth may grow with the input. Preserve the original rank and all signed coefficients throughout.

A list of successful arithmetic progressions, a high finite acceptance rate, or a recursion conditional on unknown inputs does not establish that coverage. The [result ledger](docs/RESULTS.md) gives the full sequence of proofs, counterexamples and open obligations. The [residual progress report](experiments/residual_progress/REPORT.md) records the latest research decisions; the [annular report](experiments/annular_construction/REPORT.md) retains the earlier construction work.

## Where to start

1. Read [AGENTS.md](AGENTS.md) for working rules and claim standards.
2. Read the [result ledger](docs/RESULTS.md) for exact scope, evidence, and unresolved obligations.
3. Read the [current proof note](collatz_research_20261017/right_aligned_reduction.tex). Open this source in the document editor for its PDF preview.
4. Consult the [master handoff](COLLATZ_PROGRAMME_MASTER_HANDOFF.md) for the wider programme and historical counterexamples. Its old active target is superseded only for the revised right-aligned family.

At the start of each batch, also skim the independent `claude/sidekick`
feed by fetching that branch and reading `sidekick/FEED.md` from its remote
reference. It supplies optional checks, counterexamples, and questions.
Verify findings before using them and leave that branch unchanged.

## Reproduce the finite checks

Requires Python 3.10+ and its standard library. The independent check additionally requires a C++17 compiler (`c++`, or set `CXX` to a compiler executable).

```sh
python3 scripts/verify_all.py --cpp
```

Without a compiler, omit `--cpp`; the report explicitly records that the independent C++ check was not run. The runner verifies the archive and all 31 manifest entries, stored certificates, the right-aligned and five-ray audits, annular identities, partial constructions, norm formula, component diagnostics, and the independent lane's negative-control and audit receipts. It uses temporary storage so preserved inputs and receipts stay unchanged. With `--cpp`, it also builds and runs the independent verifier at both original stored cutoffs.

Most checks establish finite arithmetic identities. R91 and R92 additionally use complete finite rational-basin classifications inside their computer-assisted proofs. R92's default replay checks the smaller congruence-selected universe; `--cpp` independently classifies the entire larger interval as well as reproducing R91 and the original stored cutoffs. None of these checks establishes universal current existence. Never use Python optimization flags for these assertion-based verifiers.

## Repository map

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

The overall target remains a finite current, possibly with an everywhere nonpositive residual, at every cutoff on **all five rays**, with a proof of construction and termination. The annular formulation gives six-band increments on thirty sequences; arbitrarily large finite certificates are allowed.

The active target is the remaining positive W5 request for one complete family, tested at the original rank. Retain the entire signed history and allow comparison depth to depend on the input. The growth pattern has slope `3^12/2^19 > 1`; its exact finite countdown does not prove progress across subsequent exits. R91 and R92 rule out a smaller origin at its repeated target through `12r+19` quotient steps, including every inverse ray and word. Prioritize later common targets or a signed comparison using genuinely different retained history. Any proposed recursion needs a closed domain, a decreasing quantity and supplied terminal currents. Further isolated residue classes or higher finite acceptance counts alone will not meet that target.

The [saved next-window draft](experiments/residual_progress/deeper_window/CANDIDATE.md) is now resolved by R92. Its complete window yields only the known self-history and supplies no new terminal current. Increasing that same search budget is a lower priority than testing a different meeting target or comparison mechanism.

R93 now gives an exact starting interface for both retained histories, including the lower path's departure and its original-rank bound. Seek a comparison after that interface or a different smaller child whose complete family closes. R94 proves that the particular ternary child in the saved template needs unbounded clocks; a finite catalogue for that child cannot finish the task.

Preserve the merged lane's `3x+61` negative controls: early compression alone cannot prove progress. Keep every source coefficient and boundary term. Finite scans, a smaller positive residual, and the measure recurrence alone do not supply the missing construction. The [ledger's open obligations](docs/RESULTS.md#open-obligations-and-priorities) and [latest research report](experiments/residual_progress/REPORT.md) retain the exact scopes and alternatives.
