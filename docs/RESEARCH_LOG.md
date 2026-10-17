# Research log

## 2026-10-17 — Right-aligned reduction and repository baseline

- Reviewed the master handoff and original current archive. Matched the archive SHA-256 and all 31 manifest entries; reran the stored Python checks and freshly compiled independent C++ checks for N=4096 and N=262144.
- Derived the right-aligned depth-one packet decomposition with residual support `{5,7,11,13}`. Saved the argument in `collatz_research_20261017/right_aligned_reduction.tex` and the finite construction in `right_aligned_packets.py`.
- Proved a qualitative equivalence: per-cutoff all-horizon upper boundedness, or finite current certificates with nonpositive residual, for every integer cutoff implies Collatz. No N-uniform cost estimate is needed. Universal construction remains open.
- Recorded the exact dyadic core period and transfer bounds, plus the positive-work witness at N=32. The audit passed for all N=8..2048, selected larger cutoffs, and dyadic exponents b=3..1000. The proof note compiled successfully in the built-in editor.
- Established top-level README, result ledger, agent ground rules, and a unified verification runner. Preserved the original archive and extracted certificate sources/data; excluded generated binaries and caches.
- Ran `python3 scripts/verify_all.py --cpp`: PASS for archive/manifest integrity, both stored Python certificates, the reproduced right-aligned receipt, and both independent C++ receipts. Checked local documentation links successfully. The repository setup did not change the open LaTeX source.

Subsequent entries should name the result changed, its proof status, actual validation performed, and any outstanding obligation. Do not record prospective tests as completed.
