# Collatz research

This repository is the persistent record of the Collatz programme: definitions, proofs, failed approaches, finite certificates, and executable checks. Future work should start here rather than reconstructing the programme from chat memory.

**Current standing (2026-10-17): Collatz remains unproved.** A complete arithmetic rule now certifies asymptotically **55.3% of the residual mass left by the previous halving identity**. Combined with the earlier constructions, this conditionally covers asymptotically **92.24% of the next outer shell** from supplied absorption through N. The remaining profile is explicit, with infinite families that defeat the new rule's height decrease. We also have an exact reduced map and infinitely many certifiable targets at every height. The next task is a termination argument covering those remaining branches. The arguments have computational and model-assisted checks; they have not received human peer review or formal verification.

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

- **The complementary family has a complete run formula.** Process its initial rising run and following valuation2 run, then apply every elementary sibling and halving identity before testing the known cutoff. The [normalized construction](experiments/residual_progress/complementary_bridge/RUN_BLOCK_BRIDGES.md) removes about55.2788% of R23's complementary leading mass and leaves `0.01941025959382034 N+O(log^4 N)`. At N6144 it certifies146 of269 weighted units. Both coefficient2 roots and signed bridge rows are retained. This is one partial extension; its remaining profile has no proved closure.
- **The elementary identities are completely classified.** Every component is exactly `{F^k(q),F^k(2q+1): k>=0}`, where `F(x)=4x+1` and q is its canonical minimum. The [normal form](experiments/residual_progress/bridge_normal_form/BRIDGE_NORMAL_FORM.md) gives an exact induced map `T=nu S`, with `T nu=nu S`, and all inverse branches. Old identities alone cannot lower an already canonical root. Greedy inverse minimization fails, and canonical roots still have unbounded increasing runs.
- **Known targets extend to arbitrary heights.** If absorption through N is supplied, every x with `nu(x)<=N` has an explicit finite certificate. This infinite set contains `N/4+O(log N)` states in every band `[X,2X)`, uniformly for integer X>=N>=8. The [count and construction](experiments/residual_progress/absorbed_fibers/ABSORBED_FIBERS.md) show why the finite union of known forward orbits undercounts available targets. Spatial density alone does not prove that every unresolved orbit meets them.
- **The finite-prefix barrier now has precise scope.** For the specified D/M/H slope rules, the [elementary rate proof](experiments/residual_progress/cylinder_barrier/CYLINDER_RATES.md) gives survival factors0.9465045768 per odd step and0.9659065532 per bit. We reproduced the external receipts and corrected an omitted partially known closing valuation. Equal exponential rates do not imply constant-factor equivalence, a finite-integer counting theorem, or a barrier to arbitrary bridges.
- **A complete family reduces to half-size seeds.** For `x=2^a*t-1`, `a>=2`, odd t with `t=3^a mod4`, the exact identity `S^a(x)=S^a((x-1)/2)` gives a finite bridge to a smaller seed. The [construction](experiments/residual_progress/residual_return/SHRINKING_COALESCENCE.md) preserves every residual coefficient, including weight2. It leaves mass `25N/576+O(log N)`, half the previous leading term, and works through unbounded excursions. This is one partial extension; the halving fraction cannot be iterated without a new closure theorem.
- **The next induction target is precise.** The remaining roots have `t=-3^a mod4`. A universal rule certifying them from absorption through N would extend that absorption to `3N/2`. The five rays interleave with consecutive ratio at most7/6, so a checked base through6144 supplies the entire induction if that rule is proved. The [quantifier and literature audit](experiments/residual_progress/sufficient_sets/SUFFICIENT_SETS_AUDIT.md) states this conditional implication and explains why general sufficient-set results do not yet supply the missing rule.
- **From one finite tree to infinitely many identities.** Exact affine lifts preserve every branch of a checked common-tail tree. A five-source example can be packed into every sufficiently large allowed annulus, with a proof that no source coefficient is reused.
- **A combined partial constructor.** Five short-chain families, the packed tree, and two new cancellation families have disjoint sources. The [extended constructor](experiments/residual_progress/release_packing/RELEASE_PACKING.md) removes positive mass `1073N/432+O(1)` from an initial `99N/4`, improving the earlier `73N/48+O(1)`. It returns the full current and exact remaining measure; positive coefficients are retained.
- **Exact compression.** Merging states with the same successor gives `||P A_N||_1 = 171N/4 - |c_N|`, with `|c_N| <= 3`. This yields the `19/22` bound. The compressed measure is a different family, so repeating that bound is not justified.
- **Unbounded depth is necessary.** For every depth D>=1, the complete exposed component at `N=96*64^(3^D*t-2)`, `t>=1`, has source mass +2 and cannot be certified at depth D. The proof excludes every extra incoming history. On the ladder `N=96*64^k`, the refined least sufficient depth is at least `v_3(k+2)+4`. This rules out every finite catalogue with bounded source-to-anchor depth; recursive constructions with growing depth remain possible.
- **Selected long delays can now be resolved.** A [five-source construction](experiments/residual_progress/release/DELAYED_RELEASE.md) attaches two actual negative sources to the obstructing `(-2,+2,+2)` chain. Its current is everywhere nonpositive and works for infinitely many ternary depths, including cutoffs on the required ladder. It certifies that submeasure. A complete finite example changes from component mass2 to0 at its first attachment; a second example shows that the first attachment can instead be neutral.
- **The delay parameter does not settle coverage.** A [complete phase analysis](experiments/residual_progress/release_coverage/PHASE_COVERAGE.md) refutes completion by depth `2h+1` for all phases. At `N=96*64^k`, every `k=2 mod27` has h=2 yet retains a complete mass2 component at depth5. Symbolic proofs also isolate17 of18 coarse phases at h2 and53 of54 at h3 under stated binary and size conditions. Deeper cancellation remains possible.
- **No function of that parameter alone can work.** The [fixed-h theorem](experiments/residual_progress/phase_depth/FIXED_H_DEPTH.md) gives complete mass2 components at every prescribed depth while keeping `h=2`, including infinitely many required-ladder cutoffs per depth. Its incoming-history proof uses a finite22-case arithmetic barrier involving the auxiliary `3x-1` map. This rules out depth bounds depending only on h; it does not exhibit a cutoff without an eventual certificate.
- **A finite certificate compiler.** Exact rational weights combine finitely many packet certificates and all boundary terms. If the positive residual mass is below 1, integer component masses force an exact integer certificate. An actual demonstration combines 30 packet inputs into a 95-row certificate for every odd seed through 111, without exposing new arrows during extraction. For a target m, an explicit sufficient set uses O(log m) cutoffs, the largest O(m^2.14682); this bounds the required inputs, not the cost of constructing them.
- **The input dependency is now explicit.** Absorption on the inner interval `(N/4,N]` supplies an automatic one-sided packet certificate. Feeding that same certificate back to extend the absorbed range leaves the unknown mass unchanged. An independently supplied exact packet current does extend absorption to `(N,3N/2]`; a one-sided current retains an exact residual budget. A positive scale cone cannot bypass a new seed using only these automatic smaller inputs.
- **Retained arrows give a partial extension.** The [input graph construction](experiments/residual_progress/complement/RETAINED_GRAPH_EXTENSION.md) supplies every arrow below `3N/2`. From the supplied inner absorption it certifies all seeds through N and asymptotically `47/72` of the next outer shell, without exposing new arrows. The improved packet residual is an explicit profile of mass `25N/288+O(1)`. The inner input and remaining outer components are still required.
- **Cancellation can certify new outer seeds.** The [annular-to-complement transfer](experiments/residual_progress/complement_recursion/ANNULAR_COMPLEMENT_TRANSFER.md) takes known absorption through N and a checked partial current for `A_(N/64)`. Its positive sources already have smaller ancestors, so the identity certifies selected negative sources and their unresolved outer predecessors. The old packed trees cover `N/9216+O(1)` residual roots; the delayed family supplies explicit first descents to `N-1` in `h+r+2` steps, with no assumed absorption above N. Every uncovered residual coefficient remains present.
- **A terminating partial normalization.** Exact backward substitutions move positive mass downward with a strictly decreasing integer potential and give a unique residual. For every annulus the positive support ends below `64N`, but at least `21N/4` positive mass remains at multiples of 3. Continuing from this residual requires positive current; the normalization does not finish the proof.
- **Intermediate coefficients improve cancellation.** The [path construction](experiments/residual_progress/alternating/ALTERNATING_PATHS.md) retains the negative source capacity skipped by two-edge substitutions. A finite backward ancestry proof supplies both a nonpositive-current normalization and a linear signed collapse. Their positive roots remain unresolved. Keeping each exposed frontier avoids immediately undoing a forward move; explicit component exits can increase height, so height alone does not give termination.
- **Complete local source clusters are bounded.** Within that restricted path graph, all nonzero sources of one annulus on a component span at most **63 arrows**, sharply. A [bounded constructor](experiments/residual_progress/window_components/WINDOW_COMPONENTS.md) finds the entire source cluster and its exact frontier residual. Future exits can be arbitrarily distant and can enter components containing no original annular sources, so this is finite preprocessing, not termination.
- **A rejected shortcut.** Alternating root collapse and transport is conjugate to ordinary Syracuse evolution. Explicit positive atoms survive any fixed number of these operations, and their heights exceed every fixed multiple of N along the rays. This rules out that proposed closure mechanism while permitting other arithmetic rewrites and unequal-time cancellation.

Full proofs and failed candidates are in the [annular construction report](experiments/annular_construction/REPORT.md) and the newer [residual progress report](experiments/residual_progress/REPORT.md).

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

Find an arithmetic construction that produces a finite current, possibly with an everywhere nonpositive residual, along **all five rays**. The annular formulation reduces this to six-band increments on the 30 sequences above. Prove termination; arbitrarily large finite certificates are allowed.

Retain historical orbit intersections: equal futures may cancel at unequal times. A complete capped search is implemented, but universal termination is open. The source recurrence still contains an expanding `3N/2` term, so the measure identity alone does not give a decreasing induction. Larger scans and a small unresolved positive residual do not discharge this obligation.

The next concrete lemma is **finite progress for every positive component plateau**. One route would close the residuals of the proved partial currents in a family with a decreasing integer parameter. Another would prove that a finite arithmetic extension must connect an unresolved positive component to enough negative source mass or to 1. Repeating the same root compression, dropping a boundary flux, or treating a zero residue projection as an integer certificate does not supply that lemma.

The finite compiler resolves the boundary terms conditionally across a finite set of scales. Its automatic input construction requires absorption of inner intervals that include the seed being sought. Scalar feedback makes no progress, but the retained-graph theorem now supplies a partial extension with a precise outer residue profile. That profile still needs a construction; its smaller mass is not a proved repeatable contraction.

The merged independent audit adds useful negative controls: `3x+61` exhibits similar early compression but has a permanent positive cycle component. A universal progress proof must use assumptions that this control does not satisfy. Its conditional minimality lemma is also valid, but one-sided certificates can differ while attaining the same minimum cost; structural certificate searches remain legitimate.

**Current direction:** close the profile left by the normalized run construction. Use the exact quotient and its full inverse branches to find finite bridges into the infinite known set, or establish a decreasing quantity with enough arithmetic information to survive every branch. A rank depending only on the two run lengths fails on27→31→91; canonical return heights are unbounded even on required rays. The annular transfer remains available. Claude's merged controls support this focused pivot, while the latest [feed audit](experiments/residual_progress/cylinder_barrier/CYLINDER_RATES.md) narrows its proposed merger barrier to the rules actually tested. The [PR assessment](collatz_research_20261017/negative_controls/PR1_REVIEW.md) preserves both the useful controls and the corrected minimality scope.

Update this README and the result ledger whenever the standing changes. Preserve counterexamples and explain which earlier claim a new result supersedes.
