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

Subsequent entries should name the result changed, proof status, actual validation, and outstanding obligation. Do not record prospective checks as completed.
