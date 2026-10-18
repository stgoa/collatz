# Collatz research

This repository is the persistent record of the Collatz programme: definitions, proofs, failed approaches, finite certificates, and executable checks. Future work should start here rather than reconstructing the programme from chat memory.

**Current standing (2026-10-18): Collatz remains unproved.** Universal finite tripling-pair currents on `w=5 mod8` suffice. Our conditional compiler retains auxiliary `w=9 mod16` pairs and uses one consistent decreasing rank, with missing inputs explicit. We have exact arithmetic constructions for prescribed histories and a finite-anchor theorem covering every inverse ray within a stated depth. A new finite decision procedure classifies the later continuation of an entire progression, including successful classes beyond the earlier history cell. A separate theorem proves that no fixed budget for future and partner clocks can cover all critical inputs, even using every inverse branch. The priority is therefore a history procedure whose depth can depend on the input, with a proof that it finishes and supplies every terminal current. The proofs have finite and independent model checks, without human peer review or formal verification.

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

- **A later continuation has a complete finite decision rule.** The [thirteenth-target analysis](experiments/residual_progress/history_transition/HISTORY_TRANSITION.md) treats every `q=11547+3*2^19*k`, `k>=0`. Fourteen possible above-target patterns decide whether this comparison requests only smaller original ranks or retains a specific higher input. Whole successful classes extend beyond the earlier history cell. A sharp family first drops below q at quotient step20; its ordinary clock is recorded separately.
- **Every fixed history budget misses some critical inputs.** The [clock-barrier theorem](experiments/residual_progress/history_cover_scope/HISTORY_CLOCK_BARRIER.md) excludes every smaller origin reaching target a of a canonical valuation-one prefix within `D+a` partner steps when `3^D` divides the source. It includes all inverse rays and all words in that horizon. The source varies with the prescribed bounds; unrestricted histories at a fixed source remain available.
- **Smaller histories can meet above the original target.** The [first construction](experiments/residual_progress/native_history/HIGH_HISTORY.md) works where inverse-only searches fail. We now know its [complete fixed-word arithmetic cell](experiments/residual_progress/history_lifting/HISTORY_LIFTING.md), can [classify every smaller history within supplied ternary precision](experiments/residual_progress/history_frontier/HISTORY_FRONTIER.md), and have [successful subfamilies beyond any prescribed number of native growing returns](experiments/residual_progress/native_growth_escape/NATIVE_GROWTH_ESCAPE.md). Coverage of the entire exit type remains missing.
- **The recursion uses one consistent rank.** The [critical-basis compiler](experiments/residual_progress/critical_basis/CRITICAL_BASIS.md) retains W5 and W9 pairs and translates the older rank rules before combining them. Every signed dependency is explicit. Each accepted expansion strictly lowers the positive integer rank. A finite conditional plan becomes an actual current only after every remaining signed input is supplied; universal supply is still open. The older seventeen-family W5 dispatcher remains unchanged.
- **Whole signed expressions can simplify.** The [two-identity normalizer](experiments/residual_progress/frontier_progress/SIGNED_FRONTIER_NORMAL_FORM.md) terminates and preserves every sign and multiplicity. Some helpers cancel exactly, while the important growing leader survives. This gives a useful tool without completing the recursion.
- **The parallel lane is useful independent scrutiny.** PR1's negative controls are incorporated. Its broad claim that alternative certificates cannot help has explicit counterexamples in our [review](collatz_research_20261017/negative_controls/PR1_REVIEW.md). The [latest reproduced probe](experiments/residual_progress/side_lane_review_9849c53.md) checks native prefixes, return counts and a high-history anchor. The newer side pin `dc4976d` updates its synthesis and adds no new premise. These findings support a focused change in search strategy while retaining the current framework.

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

The checks establish finite arithmetic identities. They do not establish universal current existence or replace the written proof. Never use Python optimization flags for these assertion-based verifiers.

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

The active route supplies retained W9 and remaining W5 inputs through smaller-origin histories, including meetings above the original target. R84 gives a complete later-target decision but leaves explicit failed leaders. R85 shows why a fixed future/partner clock budget cannot cover every input. Resolve a complete remaining type using input-dependent depth and strictly smaller signed premises, or prove a different terminating closure. Universal existence and termination remain unproved.

Preserve the merged lane's `3x+61` negative controls: early compression alone cannot prove progress. Keep every source coefficient and boundary term. Finite scans, a smaller positive residual, and the measure recurrence alone do not supply the missing construction. The [ledger's open obligations](docs/RESULTS.md#open-obligations-and-priorities) and [latest research report](experiments/residual_progress/REPORT.md) retain the exact scopes and alternatives.
