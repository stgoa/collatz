# Research lines

Each folder is one research line (programme). Each has a `README.md` giving its goal, status and an index of its results. New results go into an existing line as `experiments/<line>/<YYYY-MM-DD>-<slug>/` ([`AGENTS.md`](../AGENTS.md) §2).

| Line | IDs | Status | Dates (2026) | Start at | Verify with |
|---|---|---|---|---|---|
| [`cycle_spectrum`](cycle_spectrum/) | C001–C014, S01–S13 | **active**; paused since Oct 19 | Oct 18–19 | [README](cycle_spectrum/README.md) | `python3 scripts/run_checks.py --line cycle_spectrum` |
| [`viewpoints`](viewpoints/) | V001–V009 | finished | Oct 18 | [README](viewpoints/README.md) | `python3 scripts/run_checks.py --line viewpoints` |
| [`phase6`](phase6/) | P6-000–P6-004 | finished | Oct 18 | [README](phase6/README.md) | `python3 scripts/verify_all.py --transfer-controls` |
| [`packet_currents`](packet_currents/) | R1–R4, C1–C5 | frozen | Oct 17 | [README](packet_currents/README.md) | `python3 scripts/verify_all.py` |
| [`current_construction`](current_construction/) | R5–R7 | frozen | Oct 17 | [README](current_construction/README.md) | `python3 scripts/verify_all.py` |
| [`annular_construction`](annular_construction/) | R8–R9 | frozen | Oct 17 | [README](annular_construction/README.md) | `python3 scripts/verify_all.py` |
| [`residual_progress`](residual_progress/) | R10–R94 | frozen; objective abandoned | Oct 17–18 | [README](residual_progress/README.md) | `python3 scripts/verify_all.py` |
| [`explicit_tao`](explicit_tao/) | L1–L6 | closed; Leg 1 is a scoped barrier | Oct 18 | [README](explicit_tao/README.md) | `python3 scripts/run_checks.py --line explicit_tao` |

**Status words.**
- *Active*: open to new results.
- *Finished*: the goal was met or retired with a written outcome.
- *Frozen*: kept as a reproducible record; build on it in a new folder rather than editing it.
- *Closed*: stopped at a documented barrier.

The formal development is in [`lean/`](../lean/), and independent checks are in [`reviews/`](../reviews/).
