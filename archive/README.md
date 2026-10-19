# Archive

Frozen history. Nothing here is edited except to keep links working. The files are kept because results elsewhere cite them, and because the record of what was claimed, when and by whom is part of the research.

| Path | What it is |
|---|---|
| [`AGENTS_2026-10-19.md`](AGENTS_2026-10-19.md) | The previous agent rules (92 KB), mostly the main lane's working notes. The new rules are in [`../AGENTS.md`](../AGENTS.md). |
| [`README_2026-10-19.md`](README_2026-10-19.md) | The previous README, with stacked "current standing" notes for C003–C013 and the earlier programmes. |
| [`COLLATZ_PROGRAMME_MASTER_HANDOFF.md`](COLLATZ_PROGRAMME_MASTER_HANDOFF.md) | The hand-off from the original ChatGPT conversation that started the repository. Its §2 notation is still useful. It cites bundles that were never committed. |
| [`docs/RESULTS.md`](docs/RESULTS.md) | The previous results ledger: summaries of the C/V/Phase 6 work, then R1–R94 and C1–C5 in full. Some historical checkers pin its tail byte-for-byte. |
| [`docs/RESEARCH_LOG.md`](docs/RESEARCH_LOG.md) | The dated research log of every era. It is newest-first above its line 731 and oldest-first below. |
| [`side_lane/FEED.md`](side_lane/FEED.md) | The side lane's feed (146 entries). It holds its review verdicts on main-lane batches and Lean units, its S-series announcements, and the corrections. Labels are explained in [`docs/CONVENTIONS.md`](../docs/CONVENTIONS.md) §4. |
| [`side_lane/DIRECTIONS.md`](side_lane/DIRECTIONS.md), [`side_lane/VIEWPOINTS.md`](side_lane/VIEWPOINTS.md), [`side_lane/proposals/`](side_lane/proposals/), [`side_lane/writeup/`](side_lane/writeup/), [`side_lane/frameworks/`](side_lane/frameworks/) | The side lane's proposals D1–D8 (all resolved), its viewpoint verdicts, a Phase 6 proposal, surveys of the R-series as of 2026-10-18, and framework notes |

## Where did it go? (the 2026-10-19 restructure)

The research lines in `experiments/` did **not** move: frozen scripts load files by path, and receipts pin their hashes. Everything else moved as follows. Old paths may still appear in receipts, historical notes and commit history.

| Before | After |
|---|---|
| `collatz_research_20261017/` (the dated upload folder) | `experiments/packet_currents/` |
| `experiments/lean_lane/` | `lean/` |
| `experiments/lean_audit/` | `lean/audit/` |
| `collatz_research_20261017/right_aligned_reduction.tex` | `papers/right_aligned_reduction/right_aligned_reduction.tex` |
| `collatz_packet_currents_bundle.zip` | removed; byte-identical to `experiments/packet_currents/collatz_packet_currents/`, and in git history |
| `sidekick/research/S2` … `S13` (branch `claude/sidekick`) | `experiments/cycle_spectrum/S02` … `S13` |
| `sidekick/probes/` | `reviews/side_lane/` |
| `sidekick/writeup/D_UNIFORM_AUTOMATIC.md` | `experiments/viewpoints/V004/D_UNIFORM_AUTOMATIC.md` |
| `sidekick/` (`FEED.md`, `DIRECTIONS.md`, `VIEWPOINTS.md`, `proposals/`, `writeup/`, `frameworks/`) | `archive/side_lane/` |
| `docs/CYCLE_SPECTRUM_BRIEF.md`, `docs/CYCLE_SPECTRUM_LOG.md` | `experiments/cycle_spectrum/BRIEF.md`, `LOG.md` |
| `VIEWPOINT_MAP.md`, `docs/VIEWPOINT_LOG.md` | `experiments/viewpoints/MAP.md`, `LOG.md` |
| `docs/VIEWPOINT_BRIEF.md`, `ARITHMETIC_REGULARITY_BRIEF.md`, `GLOBAL_RIGIDITY_BRIEF.md`, `QUANTITATIVE_RIGIDITY_BRIEF.md`, `NEXT_GOAL_PROPOSAL.md` | `experiments/viewpoints/briefs/` |
| `ROUTE_MAP.md`, `docs/PHASE6_LEDGER.md`, `docs/PHASE6_LITERATURE.md` | `experiments/phase6/ROUTE_MAP.md`, `LEDGER.md`, `LITERATURE.md` |
| `docs/RESULTS.md`, `docs/RESEARCH_LOG.md` | `archive/docs/` |
| `AGENTS.md`, `README.md`, `COLLATZ_PROGRAMME_MASTER_HANDOFF.md` | `archive/` (new `AGENTS.md` and `README.md` written) |

Branches `claude/sidekick`, `claude/lean-lane` and `claude/explicit-tao` were merged into `main` with their full history and then deleted. `git log --follow <path>` traces any file through the move.
