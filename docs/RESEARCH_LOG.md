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

Subsequent entries should name the result changed, proof status, actual validation, and outstanding obligation. Do not record prospective checks as completed.
