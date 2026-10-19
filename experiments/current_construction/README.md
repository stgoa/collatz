# Current construction (R5–R7)

**Status: frozen** (2026-10-17).

**Rounds.**
- R5: finite current certificates suffice on five rays `N = a·2^b` (`a ∈ {12, 14, 16, 18, 21}`, `b ≥ 3`).
- R6: an exact annular recursion `Π_right(64N) = Π_right(N) + A_N`.
- R7: a current-existence criterion, and an obstruction ruling out uniformly bounded per-packet certificates.

A universal construction remains open.

- [`REPORT.md`](REPORT.md): the investigation and its results.
- Subfolders:
  - [`frontier/`](frontier/): the five-ray criterion;
  - [`recursive/`](recursive/): the annular recursion;
  - [`obstructions/`](obstructions/): the per-packet obstruction.

  Each has a note, a checker and receipts.

Verify: `python3 scripts/verify_all.py`. Continued in [`annular_construction`](../annular_construction/).
