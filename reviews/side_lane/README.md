# Side-lane scripts

The scripts and receipts of the side lane, a Claude session on `claude/sidekick` from 2026-10-17 to 2026-10-19. The lane was first an independent reviewer of the main lane, then the producer of the S-series cycle results. Each `<name>.py` writes its receipt `<name>.json` next to itself when run from the repository root:

```sh
python3 reviews/side_lane/<name>.py
python3 scripts/run_checks.py --line reviews --fast    # all of them, skipping the slow ones
```

| Prefix | What it checks | Count |
|---|---|---|
| `batch_*`, `rNN_*` | Re-checks of the main lane's packet-currents rounds, R15–R94 | 16 + 15 |
| `c0NN_*` | Referee checks of the cycle-spectrum batches C001–C013 | 12 |
| `c004c_`, `c005d…h_`, `c006b…f_`, `c010b/c_`, `c013b_`, `r71a…c_`, `s1a_`, `s1b_`, `s1cd_`, `s2c_`, `s3a_` | Independent numerical checks of Lean units, by unit ID | 22 |
| `s2_` … `s13_`, `jterm_gap_check` | **S-series producer scripts**: the computations behind `experiments/cycle_spectrum/S02`–`S13` (and S1) | about 25 |
| `v00x_*`, `v13_*`, `viewpoint_*` | Checks of the viewpoint batches | 7 |
| `p6_*` | Checks of the Phase 6 batches | 3 |
| `fable_*` | Checks of the explicit-Tao lane | 2 |
| other names (`*_meter`, `*_probe`, `q1_*`, `q2_*`) | Exploratory measurements from the packet-currents era | about 25 |

Notes:
- **Arguments.** `c004_narrow_check`, `c005_c006_order_check`, `c007_height_check`, `c008_residue_check` and `s7_stress_rational` take command-line arguments; see their docstrings.
- **Nondeterministic receipts.** Three receipts record timing or environment details and can change on re-run: `c001_spectrum_check.json`, `q1_giant_component.json` and `selected_rules_meter.json`.
- **Shared helpers.** `s1a_integer_cycle_check.py` enumerates all cycles of `3x+q` for odd `q < 2000`, and later scripts import it. Keep sibling imports working if you move anything.
- **The C programs.** `c0_basin_classify.c` (wrapped by `c0_basin_receipt.py`) and `r88_anchor_exhaustive.c` are C programs; build instructions are in their headers. In these names, "c0" means a rational point, not the C-series.

**Status: frozen.** Add new reviews in a new folder under [`reviews/`](../).
