---
id: baseline-obligation-transfer-controls
kind: result
title: Exact 3x+d cycles refute the ordinary descent, absorption and no-cycle analogues of three Phase 6 route nodes
status: written
claim: >
  For positive odd d coprime to 6, raw odd-only map T_d(x) = (3x+d)/2^v2(3x+d) (absorbed only at 1 where
  stated). (Fixtures) The eleven listed raw cycles are exact: for d = 5 minima 1, 19, 23, 187, 347 (odd-only
  lengths 1, 3, 3, 17, 17); d = 7 minimum 5 (length 2); d = 13 minima 1, 131, 211 (lengths 1, 15, 5); d = 61
  minima 1, 235 (lengths 1, 41); every arrow, exact valuation, distinctness before closure and minimum checked.
  The eight with minimum > 1 are nonprincipal; the three through 1 are terminal baselines. (Controls) On them
  the ordinary analogues of three baseline obligations fail exactly: strict descent from an odd start x > 1
  (S.2), absorption at 1 (C.2) and exclusion of nonprincipal cycles (Y.2). (Invariant) For every positive odd
  k and odd d, T_d(dk) = d T_1(k); hence for d > 1 every positive odd multiple of d avoids 1 at every horizon,
  there are floor((floor(X/d)+1)/2) of them through X, and no bound X^alpha with alpha < 1 on unabsorbed odd
  seeds can hold for 3x+d. Setup and finite controls only: no d = 1 theorem, quotient or rank, and no
  statement about all cycles of these maps.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
certificates: [transfer_controls.py]
evidence:
  - "transfer_controls_audit.json: the receipt of transfer_controls.py (complete output: eleven raw cycles, eight nonprincipal controls, four fixed-d controls x = d, fourteen d = 1 positive samples, scaling samples and fifteen fail-closed rejection checks); it pins the SHA-256 of cycle_fixtures.json"
  - "cycle_fixtures.json: the shared fixture of eleven exact raw 3x+d cycles (candidate minima from side-lane DIRECTIONS.md at f244b7a5, every arrow reconstructed by the main lane). Legacy cycle checkers load it by its legacy path experiments/phase6/cycle_fixtures.json and pin its hash: actual-cycles-3x-d-corpus (scan_cycles.py), narrow-cycles-are-mechanical (check_rotations.py), rotation-block-exclusion (check_mechanical_blocks.py, check_order.py), equal-total-two-block-exclusion (check_two_blocks.py), ordered-cycle-sparse-forcing (check_order_rigidity.py), ordered-cycle-sorted-rank-residues (check_height_matching.py), height-denominator-candidate (check_height_denominator.py), excursion-compression (check_excursions.py, check_delivery.py) and local-odd-rounding-exclusion (check_delivery.py); tools/legacy_replay.py maps the legacy path to this folder, byte-identical"
  - "setup_verification.json: the main lane's P6-000 verification record: the full gate python3 scripts/verify_all.py --cpp --transfer-controls passed with exit 0 at main 9190ccf, with pinned input and source hashes and its own model review (the main lane's own agents, not independent)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    scope: "Finite only (side-lane feed 2026-10-18 15:38 on main's working copy and 15:52 on committed b901e11, CONFIRMED setup label none): all 11 cycles in cycle_fixtures.json re-verified with the side lane's own 3x+d step, every arrow, every exact valuation, distinctness before closure and the stated minimum; they agree with the side lane's own scan of starts below 20,000, which also lists further d = 13 five-cycles with minima 227, 251, 259, 283, 287 and 319. The feed's 15:39 entry agrees that almost-all arrival at 1 does not transfer to d > 1 because the multiples of d have positive density and never reach 1. The harness code was not separately reviewed; the status stays written"
    link: ../../../../archive/side-lane/FEED.md
aliases: [P6-000]
tags: [convergence, phase6, transfer-controls, 3x-plus-d, negative-controls, fixture]
---

# Exact 3x+d cycles refute the ordinary descent, absorption and no-cycle analogues of three Phase 6 route nodes

## Statement

Phase 6 (2026-10-18) replaced open-ended exploration with named proof obligations ("route nodes") and graded every batch against them. Before any node was attempted, this setup batch built the exact negative controls that every claimed step had to survive. It is setup: it proves no node, and passing its controls does not make an argument specific to `3x+1`. A proposed argument must separately register its own `d`-parametric step and show where that step fails.

The three route nodes whose baseline analogues are tested are [`universal-w5-quotient-stopping`](../../questions/universal-w5-quotient-stopping.md) (S.2), [`unabsorbed-count-power-saving`](../../questions/unabsorbed-count-power-saving.md) (C.2) and [`canonical-quotient-cycle-exclusion`](../../../cycles/questions/canonical-quotient-cycle-exclusion.md) (Y.2).

**Declared dynamics.** For positive odd `d` coprime to 6 and positive odd `x`, the raw map is `T_d(x) = (3x+d)/2^v2(3x+d)`. All clocks count odd-only arrows. The working map absorbs at **1 only**: it sets `T_d(1) = 1` even when the raw map does not. Raw cycle certificates use the raw map at every state.

This matters at `d = 7`: the raw path is `1 → 5 → 11 → 5`, while the absorbed map fixes 1. The older packet control [`affine_controls.py`](../locally-collatz-like-control-barrier/affine_controls.py) uses absorbers `{1, d}` for work and currents. That convention suits its own certificate, but it is **not** imported here. Here 61 remains a nonabsorbing fixed point of `T_61`.

**Exact fixtures.** The candidate minima came from side-lane `DIRECTIONS.md` (now [`archive/side-lane/DIRECTIONS.md`](../../../../archive/side-lane/DIRECTIONS.md)) at commit `f244b7a5b77a51f8dd7e6bccf2c6d5f18932df88`. The main lane independently reconstructs and checks every arrow, its exact valuation, distinctness before closure, and the minimum. The fixture is a list of specific cycles; it does not claim all cycles or reproduce the side lane's starting-value scan.

| d | Raw cycle minimum | Odd-only length |
|---|---:|---:|
| 5 | 1 | 1 |
| 5 | 19 | 3 |
| 5 | 23 | 3 |
| 5 | 187 | 17 |
| 5 | 347 | 17 |
| 7 | 5 | 2 |
| 13 | 1 | 1 |
| 13 | 131 | 15 |
| 13 | 211 | 5 |
| 61 | 1 | 1 |
| 61 | 235 | 41 |

The eight cycles whose minimum exceeds 1 are genuine negative controls for the baseline obligations. The three minimum-1 cycles are terminal baselines and are never counted as failures of convergence to 1. The additional fixed points `x = d` for each of the four `d` values check a separate invariant set. They are not primitive relative to `d` and are not among the side lane's listed primitive cycle fixtures.

**Registered baseline obligations.**

| Node | Registered name and exact test | Named obstruction |
|---|---|---|
| S.2 | `strict_descent`: from an odd start `x > 1`, seek an odd iterate `< x` | `S.2.strict_orbit_descent`: a complete cycle at its minimum has no such iterate |
| C.2 | `one_absorption`: seek 1 from the tested odd seed | `C.2.one_absorption`: a complete cycle disjoint from 1 never hits 1 |
| Y.2 | `nonprincipal_cycle_exclusion`: seek either 1 or an exact nonprincipal cycle | `Y.2.nonprincipal_cycle_exclusion`: the listed nonprincipal cycle exists |

For S.2 this is the necessary ordinary height-drop control. It does not parameterise or test the stronger canonical-quotient threshold of the route map. For C.2, checking one seed does not verify a density estimate. For Y.2, the harness recovers actual cycles; it does not implement an unproved cycle-exclusion inequality or a `d`-generalised canonical-word theorem.

For every `d`-control, each registered test is also run on `d = 1` at the explicit odd seeds `1, 3, 5, 7, 9, 11, 15, 27, 31, 41, 63, 127, 255, 447`. These are finite positive controls. Start 1 is an exempt terminal baseline, not an assertion of strict descent below 1.

## Proof

**The fixtures and controls** are finite exact computations, checked by the certificate below.

**The invariant behind the C.2 obstruction.** For every positive odd `k` and every positive odd `d`, exact arithmetic gives

```
T_d(d*k) = d*T_1(k)
```

for the raw maps, since `v2(d*(3k+1)) = v2(3k+1)`. If `d > 1`, no positive multiple of `d` equals 1. So the same equality persists under absorption at 1 along these orbits, and all positive odd multiples of `d` avoid 1 at every horizon. Their exact count through integer `X ≥ 0` is `floor((floor(X/d)+1)/2)`. In particular, a proposed bound `X^alpha` with `alpha < 1` cannot hold for the full odd domain of this generalised map for all large `X`, whatever horizon is supplied. This argument needs no assumption that the `T_1` orbit of `k` converges. The harness checks the fixed-point instances and explicit scaling samples; the all-`k` identity is the written algebra above. It is a baseline obstruction, not a new convergence step. A domain restricted to numbers coprime to `d` would need a different density argument; isolated primitive cycles alone do not establish linear basin size on that restricted domain.

## Certificates

- [`transfer_controls.py`](transfer_controls.py) (under a second): run `python3 areas/convergence/results/baseline-obligation-transfer-controls/transfer_controls.py`. It recomputes every arrow and valuation of the eleven fixtures from [`cycle_fixtures.json`](cycle_fixtures.json), runs the three registered tests on the eight nonprincipal controls, the four fixed points `x = d` and the fourteen `d = 1` seeds, checks scaling samples of the invariant, and compares its complete output with [`transfer_controls_audit.json`](transfer_controls_audit.json), which pins the fixture's SHA-256. To regenerate a reviewed receipt deliberately, use `--write-receipt PATH`.

`evaluate(name, d, start, max_steps)` returns `SUCCESS`, `OBSTRUCTED` or `UNRESOLVED`. Only exact paths and complete repeated cycles justify the first two. An exhausted step cap always yields `UNRESOLVED` and fails an expected-success or expected-obstruction audit. Unknown mechanism names, unsupported domains, malformed fixtures, incorrect arrows or valuations, missing or duplicate fixtures and unexpected receipt changes fail closed; built-in rejection checks exercise those distinctions. Running with `--max-steps 0` is an intentional failing check.

No tested positive sample proves a universal statement. These cycle controls also do not test the behaviour of hypothetical divergent orbits.

## Remarks

- **Shared fixture.** [`cycle_fixtures.json`](cycle_fixtures.json) is also the fixture of the cycle-area checkers listed under `evidence`; they load it by its legacy path, which [`tools/legacy_replay.py`](../../../../tools/legacy_replay.py) maps here. The fuller corpus of actual `3x+d` cycles is [`actual-cycles-3x-d-corpus`](../../../cycles/results/actual-cycles-3x-d-corpus/README.md), which rediscovered all eleven fixtures.
- **Grading.** The main lane proposed the programme label **none** (setup and existing-obligation counterexamples); the side lane confirmed it. The setup batch also answered the side lane's directions D1–D4: D3's blanket claim that almost-all results transfer to `3x+d` was **rejected**, for the reason in the invariant above: fixed-factor stopping transfers, absorption at 1 does not ([`route-literature-transfer-audit`](../route-literature-transfer-audit.md)).
- The controls are consistent with [`conventions/NOTATION.md`](../../../../conventions/NOTATION.md) §3 by construction: they are the controls.

## History

Migrated from `experiments/phase6/README.md` (the transfer-control harness specification, below the line the 2026-10-19 restructure added; that added line overview is retold in [`areas/convergence/OVERVIEW.md`](../../OVERVIEW.md)), with `transfer_controls.py`, `transfer_controls_audit.json`, `cycle_fixtures.json` and `setup_verification.json`, at commit `be73a66`. Legacy batch `P6-000`, ChatGPT main lane, 2026-10-18, pushed as `b901e11`; confirmed **none** by the side lane at `b1785fb` (feed 15:38, 15:52). The route map, ledger and programme report of Phase 6 are in [`archive/convergence-phase6/`](../../../../archive/convergence-phase6/).
