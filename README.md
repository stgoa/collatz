# Collatz research

This repository is the persistent record of the Collatz programme: definitions, proofs, failed approaches, finite certificates, and executable checks. Future work should start here rather than reconstructing the programme from chat memory.

**Current standing (2026-10-18): Collatz remains unproved.** Universal finite tripling-pair currents on `w=5 mod8` suffice. Our conditional compiler retains auxiliary `w=9 mod16` pairs and keeps every missing input explicit. Retained lower histories remove one high negative request, but a positive request remains. We now classify all exits of its repeated growth pattern and prove that the ternary precision gained during those repetitions cannot supply a smaller original history at that repeated target within that precision. This last theorem uses a complete rational-state calculation, independently reproduced in Python and C++. The priority is a construction that reaches beyond this precise obstruction and supplies a whole remaining family. There is no human peer review or formal verification.

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

- **All inverse words within the gained precision are excluded.** The [rational-shadow theorem](experiments/residual_progress/shadow_precision/SHADOW_PRECISION.md) reduces an arbitrary-depth slope question to a finite universe. All 1,732,883 eligible origins were classified; only 19 reach the specified cycle, and none improves the required slope. For every original coupled source with at least r growing returns, no canonical origin p<=Q reaches the repeated target within12r+5 quotient steps. The known original Q arrives at18+12r. Longer histories, later targets and other signed comparisons remain open.
- **Leaving a growth pattern is not yet descent.** The [complete exit control](experiments/residual_progress/phi_exit_control/PHI_EXIT_CONTROL.md) gives the exact binary countdown, all 19 exit rows, every next-valuation cylinder, and the full signed plan at the original Q. All high requests in the fresh forward plan are positive. Fixed exit templates eventually fail the raw-height test as the initial repetition count grows; native normalization can still help in some cases. This is complete arithmetic control of the exit interface, with terminal supply still missing.
- **Retained history removes an avoidable obligation.** The [new construction](experiments/residual_progress/retained_history/RETAINED_HISTORY.md) uses a smaller lower history throughout a larger W9 window. Its three-substitution bound is sharp for that procedure. On a complete subfamily, it supplies a negative high pair through smaller premises and simplifies a fresh comparison to an actual 25-step ordinary path. One positive high W5 pair remains; the inherited comparison also retains explicit lower signed relations.
- **A uniform short history cannot close the retained cell.** The [four-target classification](experiments/residual_progress/history_cell_scope/HISTORY_CELL_SCOPE.md) exhausts every inverse ray through horizons19–22 on the whole parameter family. Among canonical origins no larger than the original source, only that source reaches those targets in those horizons. An integrality argument also excludes one fixed word of any length giving a smaller origin throughout the family. Parameter-dependent histories and later targets remain available.
- **Exact requests improve an earlier sufficient test.** The [even-exit comparison](experiments/residual_progress/even_exit_history/EVEN_EXIT_HISTORY.md) has a complete raw-target inequality for all its parameters. For every initial climb exponent H>=4, whole families cross a larger intermediate endpoint and then request only smaller original ranks. One full phase is outside all seventeen old direct predicates. The current identity was already available; its exact acceptance domain is larger than the old estimate recognized.
- **The current W9 failures have a bounded reduction.** The [W9 repair interface](experiments/residual_progress/w9_history_repair/W9_HISTORY_REPAIR.md) treats every W9 leader left by the [thirteenth-target decision](experiments/residual_progress/history_transition/HISTORY_TRANSITION.md). At most two substitutions remove all above-target W9 requests. The remaining high request, if present, is a single W5 input with coefficient +1. A natural inverse comparison can restore the original W9 request, so this is a reduction to a smaller unresolved class, not complete supply.
- **Every fixed history budget misses some critical inputs.** The [clock-barrier theorem](experiments/residual_progress/history_cover_scope/HISTORY_CLOCK_BARRIER.md) excludes every smaller origin reaching target a of a canonical valuation-one prefix within `D+a` partner steps when `3^D` divides the source. It includes all inverse rays and all words in that horizon. The source varies with the prescribed bounds; unrestricted histories at a fixed source remain available.
- **Smaller histories can meet above the original target.** The [first construction](experiments/residual_progress/native_history/HIGH_HISTORY.md) works where inverse-only searches fail. We now know its [complete fixed-word arithmetic cell](experiments/residual_progress/history_lifting/HISTORY_LIFTING.md), can [classify every smaller history within supplied ternary precision](experiments/residual_progress/history_frontier/HISTORY_FRONTIER.md), and have [successful subfamilies beyond any prescribed number of native growing returns](experiments/residual_progress/native_growth_escape/NATIVE_GROWTH_ESCAPE.md). Coverage of the entire exit type remains missing.
- **The recursion uses one consistent rank.** The [critical-basis compiler](experiments/residual_progress/critical_basis/CRITICAL_BASIS.md) retains W5 and W9 pairs and translates the older rank rules before combining them. Every signed dependency is explicit. Each accepted expansion strictly lowers the positive integer rank. A finite conditional plan becomes an actual current only after every remaining signed input is supplied; universal supply is still open. The older seventeen-family W5 dispatcher remains unchanged.
- **Whole signed expressions can simplify.** The [two-identity normalizer](experiments/residual_progress/frontier_progress/SIGNED_FRONTIER_NORMAL_FORM.md) terminates and preserves every sign and multiplicity. Some helpers cancel exactly, while the important growing leader survives. This gives a useful tool without completing the recursion.
- **The parallel lane is useful independent scrutiny.** PR1's negative controls are incorporated. Its broad claim that alternative certificates cannot help has explicit counterexamples in our [review](collatz_research_20261017/negative_controls/PR1_REVIEW.md). The [latest pinned review](experiments/residual_progress/side_lane_review_cbe77bc.md) reproduces 85 R64 boundary checks, with ordinary words as long as600 arrows. GitHub's latest PR read listed only the already integrated PR1; newer checks are on the separate side branch. Our response is a tactical pivot toward whole-family supply and termination, with local catalogues useful when they establish that mechanism or a decisive limitation.

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

Most checks establish finite arithmetic identities. R91 additionally uses a complete finite rational-basin classification inside its computer-assisted all-word proof; `--cpp` independently reproduces that classification as well as the original stored cutoffs. None of these checks establishes universal current existence. Never use Python optimization flags for these assertion-based verifiers.

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

The active target is the remaining positive W5 request for one complete family, tested at the original rank. Retain the entire signed history and allow comparison depth to depend on the input. The growth pattern has slope `3^12/2^19 > 1`; its exact finite countdown does not prove progress across subsequent exits. R91 rules out extracting a smaller origin at its repeated target from the accumulated ternary precision alone, even with arbitrary combinations of inverse rays. Investigate histories beyond that precision, later common targets, or a signed comparison using genuinely different retained history. Any proposed recursion needs a closed domain, a decreasing quantity and supplied terminal currents. Further isolated residue classes or higher finite acceptance counts alone will not meet that target.

Preserve the merged lane's `3x+61` negative controls: early compression alone cannot prove progress. Keep every source coefficient and boundary term. Finite scans, a smaller positive residual, and the measure recurrence alone do not supply the missing construction. The [ledger's open obligations](docs/RESULTS.md#open-obligations-and-priorities) and [latest research report](experiments/residual_progress/REPORT.md) retain the exact scopes and alternatives.
