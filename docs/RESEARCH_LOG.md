# Research log

## 2026-10-17 — Right-aligned reduction and repository baseline

- Reviewed the master handoff and original current archive. Matched the archive SHA-256 and all 31 manifest entries; reran the stored Python checks and freshly compiled independent C++ checks for N=4096 and N=262144.
- Derived the right-aligned depth-one packet decomposition with residual support `{5,7,11,13}`. Saved the argument in `collatz_research_20261017/right_aligned_reduction.tex` and the finite construction in `right_aligned_packets.py`.
- Proved a qualitative equivalence: per-cutoff all-horizon upper boundedness, or finite current certificates with nonpositive residual, for every integer cutoff implies Collatz. No N-uniform cost estimate is needed. Universal construction remains open.
- Recorded the exact dyadic core period and transfer bounds, plus the positive-work witness at N=32. The audit passed for all N=8..2048, selected larger cutoffs, and dyadic exponents b=3..1000. The proof note compiled successfully in the built-in editor.
- Established top-level README, result ledger, agent ground rules, and a unified verification runner. Preserved the original archive and extracted certificate sources/data; excluded generated binaries and caches.
- Ran `python3 scripts/verify_all.py --cpp`: PASS for archive/manifest integrity, both stored Python certificates, the reproduced right-aligned receipt, and both independent C++ receipts. Checked local documentation links successfully. The repository setup did not change the open LaTeX source.

## 2026-10-17 — Independent audit, negative controls, certificate minimality

These entries come from a parallel lane on branch `claude/claude-vs-chatgpt-perf-8230f6`.

- **Audit.** Added `collatz_research_20261017/negative_controls/`. Its independent implementation of right-aligned packets matches the repository construction exactly at `d=1`. `reduction_audit.py` rechecks R2–R4 from their definitions; see the ranges in RESULTS R5. No discrepancy was found. Lemma 3 shows why the maximum principle is necessary. `main_claims_audit.py` cross-checks the five-ray arithmetic and annular identities from main commit `8d62dcc`: PASS. The controls also fail on the five-ray grid, first at N=96 for d=-1 and N=224 for d=61. These results are recorded as C1.
- **Negative controls.** `affine_controls.py` extends the construction to `T_d`, for `d in {-1,5,13,29,61,125,253,509}`. On every one of these maps, the criterion fails at some cutoff. Failures were certified with explicit orbit certificates and exact linear work slopes at `d=-1` and `d=61`. The locally Collatz-like `d=13` and `d=61` first fail at `ceil((4r-d)/3)`; this is an observation, asserted in the script. These results are recorded as C2.
- **Certificate minimality.** Proved minimality and uniqueness of the exact current as C3. Checked that the archive's stored currents at `N=4096` and `N=262144` equal the forward aggregates row for row. Measured the true all-horizon work `W(N)` against the forced cost `||J_N^+||_1` for 255 cutoffs. In every case the extinction time equals the slowest atom's stopping time.
- **Verification.** Ran `python3 scripts/verify_all.py --cpp`: PASS, including all four new receipts, reproduced in temporary storage, in about 41 s total. No LaTeX source was changed, and no compiler was available locally.
- **Progress measures (C4).** `progress_measures_audit.py` reproduces main commit `ce56699`'s R9 norm formula for 68 cutoffs, `c_80000=0`, and R10's `Phi(A_96)` trace, using independent code. On `T_61` increments, the same measures show the same one-pass ratio and early `Phi` decay. There, though, a positive component containing the 41-cycle is permanent. Main's uncommitted transport numbers for `A_96` were also reproduced, as a working-copy observation outside the receipt.

Subsequent entries should name the result changed, its proof status, actual validation performed, and any outstanding obligation. Do not record prospective tests as completed.
