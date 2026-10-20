# Residual progress (R10–R94)

**Status: frozen. The objective, universal current supply, was not reached.**

This line holds the long middle of the packet-currents programme. Its R-numbered rounds are many partial constructions (forcing, recursion, inverse histories, pair compilers) and exact obstructions. It ends at R94.

- [`REPORT.md`](REPORT.md): the round-by-round record, oldest first. It is the only place where folder names map to R-numbers.
- [`archive/docs/RESULTS.md`](../../archive/docs/RESULTS.md): the archived results ledger for R1–R94.
- The 93 topic folders each hold a note, a generator or library, a `check_<topic>.py` and its audit receipt.
- `side_lane_review_*` files: independent reviews of R-rounds by the side lane. The scripts they cite are in [`reviews/side_lane/`](../../reviews/side_lane/).

**Where it stopped.** Universal tripling currents on `W5 = {w ≡ 5 (mod 8)}` would suffice. R93 reduces the coupled pair to `[864z−257]−[z]`. R94 shows that the proposed ternary child needs unbounded clocks.

Verify: `python3 scripts/verify_all.py`. It runs the checkers in a temporary copy. New attempts should start a new folder and cite R94.
