# The original upload (2026-10-17): packet currents R1–R4 and negative controls C1–C5

**Status: frozen.** Until 2026-10-19 this folder was the repository's top-level `collatz_research_20261017/`. Frozen scripts elsewhere load files from it by path, and receipts pin hashes. Do not move or edit anything here.

It is the starting point of the packet-currents programme, which continues in [`experiments/current_construction`](../current_construction/) (R5–R7), [`experiments/annular_construction`](../annular_construction/) (R8–R9) and [`experiments/residual_progress`](../residual_progress/) (R10–R94).

| Path | Contents |
|---|---|
| [`collatz_packet_currents/`](collatz_packet_currents/README.md) | The **inherited snapshot**, byte-for-byte as uploaded. Its `SHA256SUMS.txt` manifest is verified by `scripts/verify_all.py`, and `.gitattributes` preserves its CRLF line endings. The original zip (SHA-256 `025c8faf…5447`, recorded in `scripts/verify_all.py`) was byte-identical to it; it was removed from the tree on 2026-10-19 and remains in git history. |
| [`right_aligned_packets.py`](right_aligned_packets.py), [`right_aligned_audit.json`](right_aligned_audit.json) | The R2–R4 checks of the right-aligned reduction. The written proof note is [`papers/right_aligned_reduction`](../../papers/right_aligned_reduction/right_aligned_reduction.tex). |
| [`negative_controls/`](negative_controls/NOTE.md) | The independent PR1 lane's negative controls C1–C5, with [the review of its claims](negative_controls/PR1_REVIEW.md) |

**The idea.** Convert the stopping-work discrepancy into a finite signed measure (a "current") on actual Collatz states, then certify convergence by finite current certificates. Grouping depth-one source triples from the right leaves endpoints only in `{5, 7, 11, 13}`.

Verify: `python3 scripts/verify_all.py`. It runs everything here in a temporary copy, because some scripts rewrite receipts in place.
