# Literature

This is an index of the prior work the repository relies on or compares against. Detailed audits live next to the results that use them:
- [`experiments/phase6/LITERATURE.md`](../experiments/phase6/LITERATURE.md): audits L1–L5 (stopping times, Tao, Krasikov–Lagarias, cycle minima, analytic encodings);
- the per-batch notes `experiments/cycle_spectrum/C0xx/LITERATURE.md` (C001, C005, C006, C008–C014);
- [`experiments/viewpoints/V003/LITERATURE.md`](../experiments/viewpoints/V003/LITERATURE.md) and [`V005/LITERATURE.md`](../experiments/viewpoints/V005/LITERATURE.md).

## Works cited in the repository

| Work | Topic | Used in |
|---|---|---|
| Terras (1976); Everett (1977) | Stopping times; density of integers with finite stopping time | `experiments/phase6/` (L1) |
| Lagarias (1985) | Survey of the `3x+1` problem | throughout |
| Steiner (1977); Simons–de Weger (2005); Hercher (2023) | Exclusion of cycles with few circuits (local minima); Hercher's Corollary 29 gives the period bound `m > 1.375·10^11` | `experiments/phase6/` (L4); `experiments/cycle_spectrum/C011/` |
| Eliahou (1993) | Lower bound on the total length of a nontrivial cycle (`A ≥ 17,087,915`) | `experiments/cycle_spectrum/S06/`, `S07/` |
| Barina (2025) | Convergence verified for every integer below `2^71` | `experiments/cycle_spectrum/C011/EXCLUSION.md`; S-series |
| Halbeisen–Hungerbühler (1997) | A cycle's minimum compared with its Christoffel word (Theorem 3) | `lean/receipts/mmusson_gap_all.txt` (addendum); `archive/side_lane/FEED.md` |
| Knight (2026), "Collatz high cycles do not exist" | Exclusion of high (Christoffel) cycles | `experiments/cycle_spectrum/C004/`; R71 |
| Krasikov–Lagarias (2003) | Lower bound on the number of predecessors | `experiments/phase6/` (L3) |
| Tao (2019) | Almost all orbits attain almost bounded values | `experiments/phase6/` (L2); `experiments/explicit_tao/` |
| Matveev | Explicit lower bounds for linear forms in logarithms (the exact theorem and constant are cited in `experiments/cycle_spectrum/C011/EXCLUSION.md`) | C011, C013 (replaced by EXT-1 in S06 and S11) |
| Cobham; Eilenberg (via Allouche–Shallit, Adamczewski–Bell) | Automatic sequences | `experiments/viewpoints/V004/` |
| Monks (2006); Monks et al. (2013) | Sufficiency of arithmetic progressions; strongly sufficient sets | `experiments/residual_progress/sufficient_sets/` |
| Berg–Meinardus (1994) | Analytic encodings of the Collatz problem | `experiments/phase6/` (L5) |
| `mmusson/collatz` (Lean) | `Collatz.gap_all`, the effective gap (EXT-1) | `lean/receipts/mmusson_gap_all.txt` |
| `AxiomMath/CollatzPositiveDensity` (Lean) | Positive density of predecessors (route node C.1a) | `lean/audit/`; `experiments/phase6/linear_density_audit/` |

The years and titles above are as cited in the linked files. Check the primary source before relying on a detail.

## Adding a reference

When a result builds on or is anticipated by prior work, cite it in the result's folder (author, year, title, exact theorem used). If it is broadly relevant, add a row here. Never cite a paper you have not checked. Write "not verified" when you rely on a secondary citation.
