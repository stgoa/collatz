# Finite current construction: investigation

Started 2026-10-17. Status: research pass completed and checked; universal construction remains open. The established baseline is the right-aligned reduction in the existing proof note.

## Question and completion criterion

Can the qualitative current criterion be turned into an arithmetic construction that terminates for every required cutoff? This investigation will persist any new proved construction, a precisely scoped obstruction, and reproducible evidence. A finite scan alone will not count as progress on the universal claim.

## Falsifiable directions

1. Source-scale or affine identities generate a recursive current from smaller cutoffs, with a well-founded termination argument.
2. A finite local coalescence rule set can eliminate all positive residuals. Test this against exceptional residue classes and distinguish this restricted scheme from general signed currents.
3. The qualitative criterion can be narrowed or its obstruction characterized exactly, exposing what a successful constructor must establish.

## Work plan

- [x] Read repository standing, invariants, and existing proof.
- [x] Investigate recursive arithmetic construction; identify the remaining expanding term.
- [x] Characterize finite-current feasibility and local-template obstructions.
- [x] Audit and sharpen the qualitative criterion.
- [x] Implement reproducible finite checks for new claims.
- [x] Incorporate accepted results into the existing proof note and result ledger.
- [x] Run verification, compile the note, review changes, and persist the handoff.

## Findings

### Accepted written results in this research pass

- **Five rays suffice:** `N=a*2^b`, `a in {12,14,16,18,21}`, `b>=3`. A comparison weight depending on the ray gives strict contraction below `89/90`. The required odd seeds below 96 are verified. Earlier 21-ray and 30-ray arguments remain in the scoped frontier note, superseded as the primary target.
- For `8 | N`, `Pi_right_(64N) = Pi_right_N + A_N`, with disjoint supports. `A_N` consists of six annular bands with explicit coefficients periodic modulo 18. This is a recurrence for measures; currents for its increments remain to be constructed.
- A finite signed current exists exactly when every nonabsorbing orbit component has zero source mass. A current with nonpositive residual exists exactly when each such component has nonpositive mass. Bounded work for one measure only tests their combined mass.
- A complete semidecision search can retain historical orbit intersections. Its finite cap reports unresolved; completeness does not prove universal termination.
- For every `H`, an explicit actual individual packet requires more than `H` current rows, even allowing arbitrary auxiliary states and a nonpositive residual. This rules out uniformly bounded per-packet catalogues.
- The five rays split into 30 sequences under multiplication by 64. Their initial packet endpoints lie below 12096 and reach 1 within 98 odd steps. Thus initial currents are finite sums of 98 iterates; full tables for those 30 bases are not stored.

### Finite construction evidence

- Stored and verified an exact revised-family current at `N=65536` (53621 rows) and a nonpositive-residual current at `N=2053` (1532 rows, residual mass -5).
- At 2053 the exact historical search cancels 27 source atoms in two balanced components before those components are linked to 1. The one-sided search stops earlier with 32 unlinked atoms. This demonstrates cancellation of unresolved common futures in a finite case.
- At 65536, the exposed graph already proves absorption of every source. Its smaller discovery depth is shared-path compression. These are distinct mechanisms; neither finite example proves universal termination.

### Directions changed after evidence

1. A finite catalogue of bounded per-packet certificates is ruled out by the delayed-separation family. Work shifted to aggregated measures and recursions with unbounded expansion.
2. The source-scale identity alone reproduces the original current quotient equation and supplies no decreasing induction parameter. Work shifted to the stronger disjoint annular identity and the sparse sampling theorem.
3. Faster historical searches can still expose the complete terminating graph of every source. Computational work now distinguishes cancellation of unresolved futures from shared-path compression.

### Open obligation

Prove an arithmetic current construction terminates on all five rays, or construct currents with nonpositive residual for every annular increment on their 30 sequences. None of the reductions or finite searches establishes this.

For the annular route, the unresolved input is fully explicit: the six rows of the modulo-18 coefficient table in `recursive/annular_recursion.md`. Prove that every positive exposed component eventually merges with enough negative source mass or reaches a verified absorbing component. A source-scale induction must address its `3N/2` expanding term. Zero total mass in a band alone does not imply finite current existence.

A uniform exposure depth for aggregated packets is a separate candidate, not a theorem. Depths at most 71 already fail at 65536 for this search. The per-packet obstruction does not exclude larger aggregate depth bounds; further finite successes alone would not prove one.

## Verification performed

- `python3 scripts/verify_all.py --cpp`: PASS, including original archive and 31 manifest entries; original Python and independent C++ certificates; right-aligned audit; sparse-ray constants and finite bases; 66 annular identities; 1728 finite map/measure cases in both modes; delayed-separation examples; ten whole-packet experiments; and both new stored tables.
- The existing `right_aligned_reduction.tex` compiled successfully in the built-in document editor after the additions.
- Independent model reviews checked the five-ray proof, annular recursion, finite-base corollary, component criterion, and arbitrary-auxiliary-state version of the packet obstruction. No substantive gap was found. This is not human peer review or formal verification; no novelty claim is made.

## Navigation

- Current overall standing: `../../README.md` and `../../docs/RESULTS.md`.
- Main proof: `../../collatz_research_20261017/right_aligned_reduction.tex`.
- Sampling proof and exact base checks: `frontier/`.
- Annular proof and failed scale-closing attempt: `recursive/`.
- Current existence, capped search, obstruction, and new certificates: `obstructions/`.
