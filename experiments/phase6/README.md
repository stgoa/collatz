# Phase 6 transfer controls

**Status: finite certificates and setup; proposed batch label `none`.** This
harness verifies baseline obligations on the three named route nodes. It does
not implement a proof of any node, the canonical quotient, a candidate rank,
or a new progress mechanism. Passing its negative controls does not make a
new argument specific to `3x+1`. A proposed argument must separately register
its own `d`-parametric step and demonstrate where that step fails.

## Declared dynamics

For positive odd `d` coprime to 6 and positive odd `x`, the raw map is
`T_d(x)=(3x+d)/2^v2(3x+d)`. All clocks here count odd-only arrows. The working
map absorbs at **1 only**: it sets `T_d(1)=1` even when the raw map does not.
Raw cycle certificates explicitly use the raw map at every state.

This distinction matters at `d=7`: the raw path is `1 -> 5 -> 11 -> 5`, while
the absorbed map fixes 1. The older packet control
[`affine_controls.py`](../../collatz_research_20261017/negative_controls/affine_controls.py)
uses absorbers `{1,d}` for work and currents. That convention is appropriate
to its stated certificate, but is **not** imported here. In this harness 61
remains a nonabsorbing fixed point of `T_61`.

## Exact fixtures

The candidate minima came from side-lane `DIRECTIONS.md` at commit
`f244b7a5b77a51f8dd7e6bccf2c6d5f18932df88`. Main independently reconstructs and
checks every arrow, its exact valuation, distinctness before closure, and the
minimum. The fixture is a list of specific cycles; it does not claim all
cycles or reproduce the side lane's starting-value scan.

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

The eight cycles whose minimum exceeds 1 are genuine negative controls for
the baseline obligations. The three minimum-1 cycles are terminal baselines,
and are never counted as failures of convergence to 1. Additional fixed
points `x=d` for each of the four `d` values check a separate invariant set.
Those fixed points are not primitive relative to `d` and are not in the
side lane's listed primitive cycle fixtures.

## Registered baseline obligations

| Node | Registered name and exact test | Named obstruction |
|---|---|---|
| [S.2](../../ROUTE_MAP.md) | `strict_descent`: from an odd start `x>1`, seek an odd iterate `<x` | `S.2.strict_orbit_descent`: a complete cycle at its minimum has no such iterate |
| [C.2](../../ROUTE_MAP.md) | `one_absorption`: seek 1 from the tested odd seed | `C.2.one_absorption`: a complete cycle disjoint from 1 never hits 1 |
| [Y.2](../../ROUTE_MAP.md) | `nonprincipal_cycle_exclusion`: seek either 1 or an exact nonprincipal cycle | `Y.2.nonprincipal_cycle_exclusion`: the listed nonprincipal cycle exists |

For S.2 this is the necessary ordinary height-drop control. It does not claim
to parameterize or test the stronger canonical-quotient threshold in the
route map. For C.2, checking one seed does not verify a density estimate. For
Y.2, the harness recovers actual cycles; it does not implement an unproved
cycle-exclusion inequality or a `d`-generalized canonical-word theorem.

For every `d`-control, each registered test is also run on `d=1` at the
explicit odd seeds `1,3,5,7,9,11,15,27,31,41,63,127,255,447`. These are finite
positive controls. Start 1 is an exempt terminal baseline, not an assertion
of strict descent below 1.

### The invariant behind the C.2 obstruction

For every positive odd `k` and every positive odd `d`, exact arithmetic gives

```
T_d(d*k) = d*T_1(k)
```

for the raw maps, since `v2(d*(3k+1))=v2(3k+1)`. If `d>1`, no positive
multiple of `d` equals 1. Thus the same equality persists under absorption
at 1 along these orbits, and all positive odd multiples of `d` avoid 1 for
every horizon. Their exact count through integer `X>=0` is
`floor((floor(X/d)+1)/2)`. In particular, a proposed bound `X^alpha` with
`alpha<1` cannot hold for the full odd domain of this generalized map for all
large `X`, whatever horizon is supplied. This argument needs no assumption
that the `T_1` orbit of `k` converges. The harness checks the fixed-point
instances and explicit scaling samples; the all-`k` identity is the written
algebra above. It is a baseline obstruction, not a new Phase 6 convergence
step. A domain restricted to numbers coprime to `d` would require a different
density argument; isolated primitive cycles alone do not establish linear
basin size on that restricted domain.

## Replay and failure behavior

Run the focused deterministic replay:

```
python3 -B experiments/phase6/transfer_controls.py
```

Run the integrated required gate:

```
python3 scripts/verify_all.py --cpp --transfer-controls
```

The integrated flag adds the new replay to the unchanged frozen mathematical
audits. It does not skip them. The focused command compares its complete
output to [`transfer_controls_audit.json`](transfer_controls_audit.json).
Fixtures are stored in [`cycle_fixtures.json`](cycle_fixtures.json); their
SHA-256 is in the receipt. To deliberately regenerate a reviewed receipt,
use `--write-receipt PATH`.

`evaluate(name,d,start,max_steps)` returns `SUCCESS`, `OBSTRUCTED`, or
`UNRESOLVED`. Only exact paths and complete repeated cycles justify the
first two results. An exhausted step cap always yields `UNRESOLVED` and
fails an expected-success or expected-obstruction audit. Unknown mechanism
names, unsupported domains, malformed fixtures, incorrect arrows or
valuations, missing/duplicate fixtures and unexpected receipt changes fail
closed. Built-in rejection checks exercise those distinctions. Running with
`--max-steps 0` is an intentional failing check.

No tested positive sample proves a universal statement. These cycle controls
also do not test the behavior of hypothetical divergent orbits.
