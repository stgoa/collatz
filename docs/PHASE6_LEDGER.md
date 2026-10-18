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
| P6-000, 2026-10-18: map and controls | MAP; baseline controls attached to S.2, C.2, Y.2 | **none** — setup and existing-obligation counterexamples | **Confirmed none** by the side lane at `b1785fb2dcf121586e99be95c90b94afcf1e9733`, feed 15:38; cycle fixtures independently replayed there | Exact raw cycles refute ordinary universal descent / absorption / no-cycle analogues; quotient-specific transfer unestablished | [L1–L5 audit](PHASE6_LITERATURE.md); no published theorem re-derived in this batch |
| P6-001, 2026-10-18: explicit stopping calibration | S.1 | **calibration** — published half-descent corollary with explicit constants and W5 pullback | Pending; no verdict on this proof in the batch-start feed | Ordinary estimate proved for each fixed positive odd d coprime to6; W5/nu/T pullback only at d=1 | Borovkov–Pfeifer Corollary2 finite-horizon half-descent limit, with conservative explicit errors; Korec fixed-half corollary; full power theorem not re-proved |
| P6-001, secondary preparation | S.2 | **none** — bounded-prefix obstruction already follows from frozen R25/R31 | Pending | No new transfer claim | Frozen growth examples; no new exclusion mechanism |

**Consecutive none counts:** MAP 1 (setup), S.1 0, S.2 1, C.1 0, C.2 0,
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

## P6-001 — S.1 fixed-factor stopping calibration

**Main baseline:** pushed `b901e11`. **Reviewed side commit:**
`b1785fb2dcf121586e99be95c90b94afcf1e9733`, fetched and DIRECTIONS/FEED read
at the start of this batch. The feed confirms P6-000's label none and eleven
cycle fixtures, accepts the D3 correction and records D1–D4 as answered.
No new open mathematical direction appears in DIRECTIONS.

| Direction follow-up | Decision | Reason |
|---|---|---|
| D1/D2, now accepted | **accept**, unchanged | The living map and exact harness are in pushed b901e11. |
| D3, correction accepted by side lane | **reject** the historical blanket assertion, unchanged | Fixed-factor stopping and absorption at 1 have different transfer behavior. The retained old paragraph in DIRECTIONS is not reinstated as a premise. |
| D4, still deferred | **defer**, unchanged | This batch audits exactly the frozen R25/R37 interfaces used by S.1. |
| D5, moot no-waiting change | **accept**, already implemented | b901e11 removed approval gates under the user's updated goal. Side-lane proposals do not restrict the user's ability to steer the programme. |

**Attempted result and proposed label:** calibration of the published
half-descent corollary, with explicit finite horizon, integer cutoffs and
W5 pullback. It does not re-prove Korec's stronger power theorem. The ordinary
argument is parameterized by each fixed positive odd d; the W5 conclusion
uses only the frozen d=1 quotient. The [written proof](../experiments/phase6/stopping_calibration/STOPPING_CALIBRATION.md),
[constructor](../experiments/phase6/stopping_calibration/calibration.py),
[checker](../experiments/phase6/stopping_calibration/check_calibration.py) and
[exact receipt](../experiments/phase6/stopping_calibration/calibration_audit.json)
persist the result. Independent proof and integer-only parameter reviews
passed. The full gate passed with exit0 and116 report fields; its
[verification record](../experiments/phase6/stopping_calibration/verification.json)
retains the report and checked source hashes. The label remains proposed
until the side lane addresses this batch.

For tolerances 1/2,1/10,1/100, the explicit ordinary odd-arrow horizons are
85,170,295; the W5 quotient horizons are240,330,455. Every cutoff is stored
as an exact integer. They are large conservative thresholds, not small-seed
performance claims. For each tolerance the assertion is uniform over all
integer cutoffs above its threshold. Choosing increasingly small tolerances
does not remove every exceptional input or give a single universal horizon.

Focused checks cover24,570 complete parity words,49,140 lifts,504 integer
cutoffs,200 tail bounds,18 direct parameter records and3 W5 records,
4,608 clock identities,1,024 W5 inputs and12 rejected invalid/capped calls.
Independent review reconstructed all21 parameter records with integer-only
cross products, and verified the proof separately from these finite tests.
R25/R37 source hashes are pinned; no frozen mathematical files changed.

**Next node:** S.2, whose exceptional-input obligation remains unproved.
C.2's absorption count is not inferred from this stopping calibration.

**Secondary S.2 attempt, none:** a proposed proof that finitely many
bounded-prefix stopping tests cannot cover W5 was independently checked,
then rejected as a new advance: the exclusion already follows from frozen
R25/R31. The proposed positive-density cylinder does not change that
mechanism. Count this conservatively as the first none batch at S.2.
The next attempt must allow input-dependent unbounded histories; another
finite dispatcher catalogue would not address the missing obligation.
