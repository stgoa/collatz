# Research log

## 2026-10-17 — Right-aligned reduction and repository baseline

- Reviewed the master handoff and original current archive. Matched the archive SHA-256 and all 31 manifest entries; reran the stored Python checks and freshly compiled independent C++ checks for N=4096 and N=262144.
- Derived the right-aligned depth-one packet decomposition with residual support `{5,7,11,13}`. Saved the argument in `collatz_research_20261017/right_aligned_reduction.tex` and the finite construction in `right_aligned_packets.py`.
- Proved a qualitative equivalence: per-cutoff all-horizon upper boundedness, or finite current certificates with nonpositive residual, for every integer cutoff implies Collatz. No N-uniform cost estimate is needed. Universal construction remains open.
- Recorded the exact dyadic core period and transfer bounds, plus the positive-work witness at N=32. The audit passed for all N=8..2048, selected larger cutoffs, and dyadic exponents b=3..1000. The proof note compiled successfully in the built-in editor.
- Established top-level README, result ledger, agent ground rules, and a unified verification runner. Preserved the original archive and extracted certificate sources/data; excluded generated binaries and caches.
- Ran `python3 scripts/verify_all.py --cpp`: PASS for archive/manifest integrity, both stored Python certificates, the reproduced right-aligned receipt, and both independent C++ receipts. Checked local documentation links successfully. The repository setup did not change the open LaTeX source.

## 2026-10-17 — Five-ray reduction, disjoint annuli, and current obstructions

- Sharpened the universal criterion to five dyadic rays with mantissas `{12,14,16,18,21}` and exponents at least 3. The ray-dependent comparison contracts strictly below `89/90`. Earlier 30-ray and 21-ray arguments remain as alternatives in the investigation notes.
- Proved `Pi_right_(64N)=Pi_right_N+A_N` for `8|N`, with disjoint supports and an explicit six-band table modulo 18. The core is unchanged. The current quotient still contains an expanding source scale; the recurrence supplies no terminating constructor.
- Discharged the 30 initial measures for the annular sequences: all endpoint seeds below 12096 reach 1 within 98 odd steps. Their currents exist as finite sums of iterates; full tables for these 30 bases were not stored.
- Proved the orbit-component characterization of exact and nonpositive-residual currents and a complete historical-intersection semidecision search. Distinguished fixed-measure bounded work from componentwise current feasibility.
- Proved actual individual packets require arbitrarily many current rows, even with arbitrary auxiliary states. This rules out uniformly bounded per-packet catalogues without excluding cancellation between packets.
- Stored revised-family tables at 65536 (exact) and 2053 (nonpositive residual). At 2053, balanced components cancel before being linked to 1; the exact 65536 example already exposes absorption of all its sources.
- Updated the existing LaTeX source, README, ledger, agent rules, and investigation report. The document compiled successfully. Independent model reviews found no substantive gap; human review and formal verification remain outstanding.
- Ran `python3 scripts/verify_all.py --cpp`: PASS for original integrity/certificates and all new integrated audits: sparse constants and finite bases, 66 annular identities, 1728 finite graph/measure cases in both modes, ten whole-packet examples, and stored revised currents.

The remaining obligation is universal construction and termination on the five rays, or a sufficient construction for all annular increments on the 30 sequences with verified bases. Collatz remains open in this repository.

## 2026-10-17 — Universal partial currents, exact compression, and finite component progress

- Proved an affine lifting lemma for finite common-tail trees. Exact branch valuations and current coefficients survive at every nonnegative integer parameter. Separated generic identity validity from actual annular coverage.
- Compiled a balanced five-source component into two arithmetic parameter classes with exact cutoff intervals. Proved all admissible copies have disjoint source support using 45 gcd obstructions. The packing is available for every allowed N>=168, plus N=96..152.
- Proved five short-chain cancellation families with nonpositive currents, exact floor counts, and disjoint source support. Independently proved these families disjoint from the five-source packing. Their combined partial constructor returns full current/residual dictionaries and deletes positive mass `73N/48+O(1)`; the general residual remains unresolved.
- Proved `||P A_N||_1=171N/4-|c_N|`, `|c_N|<=3`, and the resulting one-pass `19/22` contraction. Supplied the finite root-collapse current. Proved its idempotence and a surviving positive mass of at least 4N, preventing an unsupported repeated-contraction argument.
- Proved a growing ternary-period obstruction to a fixed-modulus profile catalogue under literal forward transport. This is scoped to synchronous transport and does not exclude arithmetic rewrites or historical cancellation.
- Stored actual A_96 and A_168 current certificates and full component diagnostics. Cross-band cancellation can precede exposed absorption. Exact positive-work witnesses refute the stronger everywhere-nonpositive-current target.
- Proved the positive-component integer potential and an exact scale boundary-flux identity. Stored a positive A_96 component with source mass 17 and flux -7; exposing every boundary row still leaves positive mass 17. Identified finite termination of every positive plateau as the next constructive obligation.
- Proved eventual vanishing of each band's projections modulo fixed powers of two and three times those powers. Stored a separate negative-domain reflected-annulus certificate with component masses -20, -73, +93; this tests an overgeneralized inference and makes no positive Collatz counterexample claim.
- Updated the existing LaTeX note, README, ledger, agent guards, and investigation report. Independent model reviews checked the capacity proofs, norm proof, and main-note transcription. The source compiled successfully in the built-in editor; human review and formal verification remain outstanding.
- Ran `python3 scripts/verify_all.py --cpp`: PASS for all earlier checks and five new integrated checkers. New checks cover packing at every 8|N through 4096, 66 arithmetic cases, eight combined-constructor cases through 6144, six graph diagnostics, stored annular currents, exact boundary flux, projections, and the reflected certificate. All 31 checked local Markdown links resolved; `git diff --check` passed.

The universal goal remains open. The next step is a finite progress lemma for positive component plateaus, or a closed residual family with a proved decreasing parameter. The partial constructor and one-pass contraction do not establish either.

## 2026-10-17 — Finite certificate compiler and residual progress obstructions

- Proved the strict integer-component gap: a finite rational current for an integer source with total positive residual mass below 1 converts, on its existing graph, into an integer current with nonpositive residual. For a nonnegative source it supplies actual absorption paths. Recorded the strict threshold and general-graph scope of its counterexample.
- Made the five-ray implication finite and constructive. Exact rational comparison r=35/27 gives a nonnegative finite inverse; its weights combine supplied packet certificates with every source-scale current, rounding shell, and boundary measure. An explicit sufficient block has O(log m) input cutoffs and largest cutoff O(m^2.14682). This is an input-location bound, not a universal construction or complexity bound.
- Implemented the actual compiler. Thirty capped one-sided packet searches at cutoffs through 5376 supply a rational U_112 current with 6217 rows and positive residual `29145292346068/46422343855805 < 1`. Extracted and stored a 95-row nonnegative integer current without exposing any new arrow. Twenty inputs finish with some sources unlinked to 1 in their individual graphs. All input divergences and the full combined rational identity are checked exactly.
- Proved the root/transport normal form and conjugacy, including root-1 absorption. Explicit positive atoms survive every fixed number of P/R operations, and a required-ray source reaches height `324*a*3^b-1` after b+2 transports. This excludes fixed-depth and uniform linear-height closure for that process, while permitting historical cancellation and other rewrites.
- Preserved exact failures of repeated 19/22 contraction and of strict one-step norm decrease on every unresolved residual. No infinite plateau is inferred from the finite examples.
- Implemented a complete inverse exposure oracle with exact height bounds and explicit unresolved caps. At N=12*2^27 it verifies a 35-vertex component of the entire depth-32 graph with source mass +2, excluding one-sided currents supported on that graph. It avoids materializing 53,754,200,064 source atoms. The finite witness does not establish an arbitrary-depth aggregate obstruction.
- Refuted the naive always-positive top-chain candidate using the complete depth-2 component at N=10368: 27 sources balance to zero through historical intersections. Saved all vertices/arrows of both examples and validated the inverse oracle against 48 independent full graphs.
- Updated the existing LaTeX source, README, result ledger, agent guards, and new investigation report. Independent model reviews checked the transport proof, finite-cone positivity and signs, compiler implementation, and main-note transcription. Applied three clarification fixes concerning lower indices, least admissible block size, and the threshold counterexample's domain.
- Ran `python3 scripts/verify_all.py --cpp`: PASS, including all prior checks and four new default checkers. New evidence includes 216000 integer-gap cases, four rational-cone plans, four full boundary identities, seven exact tail bounds through target 10^30, actual certificate conversion, transport witnesses, and complete inverse components. The LaTeX source compiled successfully; all 44 checked local Markdown links resolved; `git diff --check` passed.

Next: supply the finite compiler's larger packet inputs without circular induction, or find a different residual family with proved finite progress. A parameterized aggregate obstruction would require lifting complete component closure, including every excluded incoming edge. Collatz and universal termination remain open.

Subsequent entries should name the result changed, proof status, actual validation, and outstanding obligation. Do not record prospective checks as completed.

## 2026-10-17 — Independent audit, negative controls, certificate minimality

These entries come from a parallel lane on branch `claude/claude-vs-chatgpt-perf-8230f6`.

- **Audit.** Added `collatz_research_20261017/negative_controls/`. Its independent implementation of right-aligned packets matches the repository construction exactly at `d=1`. `reduction_audit.py` rechecks R2–R4 from their definitions; see the ranges in RESULTS R5. No discrepancy was found. Lemma 3 shows why the maximum principle is necessary. `main_claims_audit.py` cross-checks the five-ray arithmetic and annular identities from main commit `8d62dcc`: PASS. The controls also fail on the five-ray grid, first at N=96 for d=-1 and N=224 for d=61. These results are recorded as C1.
- **Negative controls.** `affine_controls.py` extends the construction to `T_d`, for `d in {-1,5,13,29,61,125,253,509}`. On every one of these maps, the criterion fails at some cutoff. Failures were certified with explicit orbit certificates and exact linear work slopes at `d=-1` and `d=61`. The locally Collatz-like `d=13` and `d=61` first fail at `ceil((4r-d)/3)`; this is an observation, asserted in the script. These results are recorded as C2.
- **Certificate minimality.** Proved minimality and uniqueness of the exact current as C3. Checked that the archive's stored currents at `N=4096` and `N=262144` equal the forward aggregates row for row. Measured the true all-horizon work `W(N)` against the forced cost `||J_N^+||_1` for 255 cutoffs. In every case the extinction time equals the slowest atom's stopping time.
- **Verification.** Ran `python3 scripts/verify_all.py --cpp`: PASS, including all four new receipts, reproduced in temporary storage, in about 41 s total. No LaTeX source was changed, and no compiler was available locally.
- **Progress measures (C4).** `progress_measures_audit.py` reproduces main commit `ce56699`'s R9 norm formula for 68 cutoffs, `c_80000=0`, and R10's `Phi(A_96)` trace, using independent code. On `T_61` increments, the same measures show the same one-pass ratio and early `Phi` decay. There, though, a positive component containing the 41-cycle is permanent. Main's uncommitted transport numbers for `A_96` were also reproduced, as a working-copy observation outside the receipt.

Subsequent entries should name the result changed, its proof status, actual validation performed, and any outstanding obligation. Do not record prospective tests as completed.
- **Direct attempt (C5).** Tried to prove the annular obligation using main's R5–R13. No proof was found.
  - `attempt_probes.py` refutes high-level annihilation: forced currents reach 1, with growing signed entry traffic.
  - It also confirms on the controls that every nontrivial cycle class separately violates the criterion.
  - The written class-wise corollary shows the obligation is equivalent to excluding cycles and divergence, each separately and at full strength.
