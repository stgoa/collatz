# Phase 6 ledger

The active plan is [ROUTE_MAP.md](../ROUTE_MAP.md). Collatz remains open.
R1–R94 and the seventeen-family dispatcher are frozen at main
`9190ccf2519acc56446dd027c6cbf8d45dcceeb6`.

Labels are proposed by main; confirmation or dispute comes from the side
lane's feed. A pending verdict does not block the next batch. No confirmation
is inferred from an earlier review of different work. Programme labels do
not replace written-proof / finite-certificate / open status.

## Batch register

| Batch | Node | Proposed label | Confirmation | Transfer status | Literature match |
|---|---|---|---|---|---|
| P6-000, 2026-10-18: map and controls | MAP; baseline controls attached to S.2, C.2, Y.2 | **none** — setup and existing-obligation counterexamples | Pending; pinned feed predates these artifacts | Exact raw cycles refute ordinary universal descent / absorption / no-cycle analogues; quotient-specific transfer unestablished | [L1–L5 audit](PHASE6_LITERATURE.md); no published theorem re-derived in this batch |

**Consecutive none counts:** MAP 1 (setup), S.1 0, S.2 0, C.1 0, C.2 0,
C.3 0, Y.1 0, Y.2 0, H.1 0, H.2 0. A later mathematical attempt on a node
must be counted even if it produces useful code or a clearer formulation.
Three none batches trigger a written post-mortem and an autonomous pivot.

## P6-000 — Decision and exact scope

**Reviewed side commit:** `f244b7a5b77a51f8dd7e6bccf2c6d5f18932df88`.
Both DIRECTIONS and FEED were read after fetching. The first four open
directions are answered below. New feed arithmetic checks and Q1/Q2 finite
exposure observations were read as context, not imported as asymptotic
theorems or rerun in this setup. Earlier reviewed reductions remain frozen.

| Open direction | Decision | Reason and implementation |
|---|---|---|
| D1 — seed the route map with R/S/C/Y/H | **accept** with explicit scope corrections | All five routes are represented. R.2 retains q>=7 and is an existence equivalence, not algorithmic necessity. C.2 counts all positive seeds with a stated odd clock and remains Collatz-equivalent with C.1. H.2 specifies the coefficient space instead of importing an unspecified analytic theorem. The map is living and main selects nodes autonomously under the user's updated goal. |
| D2 — transfer harness before outcome (a) | **accept** | Every registered test names its predicate, domain and failed step. Eleven supplied raw cycle minima are independently replayed; only eight are nonprincipal negative controls. The three cycles through 1 are terminal baselines. New mechanisms must register their own step; passing this baseline does not grant label (a). |
| D3 — almost-all results count as calibration, with blanket density transfer | **reject** the blanket proposal; retain its scoped calibration principle | Re-deriving published density results with explicit constants is calibration. But almost-all absorption at 1 does not transfer to d>1: multiples of d have positive density and never hit 1. Fixed-factor stopping needs its own proof and d-dependent constants. A genuinely non-transferable step is judged by the actual harness and proof, not by whether its statement includes a density. |
| D4 — tag all R1–R94 by transfer | **defer** | Ninety-four individual domain/proof audits would delay the first live node. Tag frozen inputs when a selected node uses them. Rational covariance changes the integer lattice, so no blanket “all transfer” conclusion is adopted. R71's denominator criterion remains a possible Y.2 input; hypothetical divergence is not testable by cycle fixtures alone. |

**Research choice:** next pursue S.1 calibration, with explicit finite
counts, odd-arrow clock and W5 pullback. This is chosen for a checkable
benchmark and a precise account of the exceptional set. It is not advertised
as a likely proof of S.2. The stronger C.2 target and the separate cycle and
harmonic routes remain available for later evidence-driven pivots.

**Durable evidence:** [control specification](../experiments/phase6/README.md),
[checker](../experiments/phase6/transfer_controls.py),
[cycles](../experiments/phase6/cycle_fixtures.json), and
[receipt](../experiments/phase6/transfer_controls_audit.json).
The new harness distinguishes raw S_d from absorption at 1, rejects missing
or malformed fixtures and capped results, and preserves finite d=1 positive
controls. The old packet controls use their own `{1,d}` absorber convention;
their frozen conclusions are unchanged.

**Verification:** focused replay, fifteen rejection checks and the full
`python3 scripts/verify_all.py --cpp --transfer-controls` gate passed with
exit 0. The [stored verification record](../experiments/phase6/setup_verification.json)
contains the complete gate report and pinned input/code hashes. Independent
arithmetic replay verified all eleven cycles and87 observation paths without
importing the harness. The review found and corrected C.1's target-domain
ambiguity. No frozen mathematical source or dispatcher changed. Delivery is
recorded in the accompanying Git history. No new proof of convergence,
universal current supply, or novelty claim is made.
