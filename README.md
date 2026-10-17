# Collatz research

This repository is the persistent record of the Collatz programme: definitions, proofs, failed approaches, finite certificates, and executable checks. Future work should start here rather than reconstructing the programme from chat memory.

**Current standing (2026-10-17): Collatz remains unproved.** Finite currents along **five dyadic rays** would suffice, with no uniform cost bound. We now prove that **every fixed exposure depth fails**, already on the single annular ladder `N=96*64^k`. Explicit partial currents, a terminating partial normalization, and a finite certificate compiler are available; a complete construction with proved termination remains open. The arguments have computational and model-assisted checks; they have not received human peer review or formal verification.

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

## Constructive progress

- **From one finite tree to infinitely many identities.** Exact affine lifts preserve every branch of a checked common-tail tree. A five-source example can be packed into every sufficiently large allowed annulus, with a proof that no source coefficient is reused.
- **A combined partial constructor.** Five short-chain families and the packed tree have disjoint sources. Their currents remove positive mass `D(N)+3C(N) = 73N/48+O(1)` from an initial `99N/4`. The code returns the full current and the exact remaining measure; its positive coefficients are retained.
- **Exact compression.** Merging states with the same successor gives `||P A_N||_1 = 171N/4 - |c_N|`, with `|c_N| <= 3`. This yields the `19/22` bound. The compressed measure is a different family, so repeating that bound is not justified.
- **Unbounded depth is necessary.** For every depth D>=1, the complete exposed component at `N=96*64^(3^D*t-2)`, `t>=1`, has source mass +2 and cannot be certified at depth D. The proof excludes every extra incoming history. On the ladder `N=96*64^k`, the least sufficient depth is at least `v_3(k+2)+1`. This rules out every finite catalogue with bounded source-to-anchor depth; recursive constructions with growing depth remain possible.
- **A finite certificate compiler.** Exact rational weights combine finitely many packet certificates and all boundary terms. If the positive residual mass is below 1, integer component masses force an exact integer certificate. An actual demonstration combines 30 packet inputs into a 95-row certificate for every odd seed through 111, without exposing new arrows during extraction. For a target m, an explicit sufficient set uses O(log m) cutoffs, the largest O(m^2.14682); this bounds the required inputs, not the cost of constructing them.
- **The input dependency is now explicit.** Absorption on the inner interval `(N/4,N]` supplies an automatic one-sided packet certificate. Feeding that same certificate back to extend the absorbed range leaves the unknown mass unchanged. An independently supplied exact packet current does extend absorption to `(N,3N/2]`; a one-sided current retains an exact residual budget. A positive scale cone cannot bypass a new seed using only these automatic smaller inputs.
- **A terminating partial normalization.** Exact backward substitutions move positive mass downward with a strictly decreasing integer potential and give a unique residual. For every annulus the positive support ends below `64N`, but at least `21N/4` positive mass remains at multiples of 3. Continuing from this residual requires positive current; the normalization does not finish the proof.
- **A rejected shortcut.** Alternating root collapse and transport is conjugate to ordinary Syracuse evolution. Explicit positive atoms survive any fixed number of these operations, and their heights exceed every fixed multiple of N along the rays. This rules out that proposed closure mechanism while permitting other arithmetic rewrites and unequal-time cancellation.

Full proofs and failed candidates are in the [annular construction report](experiments/annular_construction/REPORT.md) and the newer [residual progress report](experiments/residual_progress/REPORT.md).

## Where to start

1. Read [AGENTS.md](AGENTS.md) for working rules and claim standards.
2. Read the [result ledger](docs/RESULTS.md) for exact scope, evidence, and unresolved obligations.
3. Read the [current proof note](collatz_research_20261017/right_aligned_reduction.tex). Open this source in the document editor for its PDF preview.
4. Consult the [master handoff](COLLATZ_PROGRAMME_MASTER_HANDOFF.md) for the wider programme and historical counterexamples. Its old active target is superseded only for the revised right-aligned family.

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

Find an arithmetic construction that produces a finite current, possibly with an everywhere nonpositive residual, along **all five rays**. The annular formulation reduces this to six-band increments on the 30 sequences above. Prove termination; arbitrarily large finite certificates are allowed.

Retain historical orbit intersections: equal futures may cancel at unequal times. A complete capped search is implemented, but universal termination is open. The source recurrence still contains an expanding `3N/2` term, so the measure identity alone does not give a decreasing induction. Larger scans and a small unresolved positive residual do not discharge this obligation.

The next concrete lemma is **finite progress for every positive component plateau**. One route would close the residuals of the proved partial currents in a family with a decreasing integer parameter. Another would prove that a finite arithmetic extension must connect an unresolved positive component to enough negative source mass or to 1. Repeating the same root compression, dropping a boundary flux, or treating a zero residue projection as an integer certificate does not supply that lemma.

The finite compiler resolves the boundary terms conditionally across a finite set of scales. Its automatic input construction requires absorption of inner intervals that include the seed being sought. The explicit local conversion shows why feeding those inputs back makes no progress. A successful construction must supply independent cancellation or establish a different closed recursion; the raw outermost packet-source height alone is not an intrinsic obstacle.

The merged independent audit adds useful negative controls: `3x+61` exhibits similar early compression but has a permanent positive cycle component. A universal progress proof must use assumptions that this control does not satisfy. Its conditional minimality lemma is also valid, but one-sided certificates can differ while attaining the same minimum cost; structural certificate searches remain legitimate.

**Current direction:** pursue arithmetic specific to `3x+1` with unbounded historical depth, and prove that every positive component eventually connects to enough negative mass or to 1. The new depth theorem rules out a fixed catalogue. The controls rule out treating early compression as a termination argument.

Update this README and the result ledger whenever the standing changes. Preserve counterexamples and explain which earlier claim a new result supersedes.
