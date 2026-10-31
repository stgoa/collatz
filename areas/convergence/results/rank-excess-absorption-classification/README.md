---
id: rank-excess-absorption-classification
kind: result
title: "The unique rank excess in formal absorption, and a complete strict-rank domain in the fifth-exponent family"
status: reviewed
claim: >
  Odd-only 3x+1 map S, absorbing at 1; rho(w) = nu(3w); H_s the unchanged formal absorption plan with full W9
  elimination, n = nu(s). Every requested W5 rank is at most n, except precisely when canonical n = 27 mod 48,
  v2(3n-1) = 4 and 3z is noncanonical for z = (3n-1)/16; then exactly one request lies above n, u = 4z+1, with
  coefficient +1 and rho(u) = (9n+5)/8, and all others lie below n. At n = 1 there are no requests; for
  noncanonical s even the exceptional rank is below s. The proof covers every recursive W9 branch and the small
  v = 9 case. For the full fifth-exponent family w = 437 + 512m of sigma-rank-removes-absorption-overhead, the
  unchanged forward current is strict in the original rho exactly unless m = 7 mod 16 and 3(2147 + 4374j) is
  noncanonical, j = (m-7)/16 (ordinary clocks (6, 1), quotient clock 5); the full progression w = 4021 mod
  294912 passes and is outside all twelve earlier direct domains. The retained failure w = 44981 still requests
  96069 with rank 144103 > 134943; rho and sigma remain distinct. Missing currents are not supplied and no
  universal coverage is claimed.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [critical-image-rank-composition, critical-nine-elimination, sigma-rank-removes-absorption-overhead, twelve-family-rho-dispatcher, forward-blocks-low-exponent-tests]
certificates: [check_legacy_replay.py]
evidence:
  - "check_exact_bound.py, exact_bound.py, exact_bound_audit.json: the legacy classifier and checker: 16384 odd seeds, 2048 W9 plans, 2048 fifth-family inputs (1983 descending, 65 unresolved), 69 new-progression examples through index 2^128, three complete supplied-current outputs with 12 distinct supplied pairs and seven rejection checks. Fails at its new path: exact_bound.py loads ../critical_rank/, ../nonselected_forward/ and ../selected_rules/ by their pre-migration folder names. Passed at be73a66 as experiments/residual_progress/exact_absorption_bound/check_exact_bound.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
  - "r58_excess_check.py, r58_excess_check.json: side-lane probe (Claude side lane, 2026-10-18) testing the classification against main's committed R43 plans (critical_rank/rank_closure.absorption_plan at 7206f9c), not this node's module. Fails at its new path: it imports rank_closure from experiments/residual_progress/critical_rank/ by repository-relative path (now ../critical-image-rank-composition/). Passed at be73a66 as reviews/side_lane/r58_excess_check.py (archive/legacy-checker-run-be73a66.md, exit 0); its receipt is reproduced byte for byte by check_legacy_replay.py"
  - "side_lane_review_c2319c9.json: the main lane's reproduction (2026-10-18) of the unmodified probe r58_excess_check.py at side-lane commit c2319c9 (main d265d94), PASS, scope 'Independent finite R58 probe reproduced unchanged; no universal proof inferred'. A main-lane review of a side-lane probe"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: r58_excess_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 00:16, VERIFIED, main working copy), tested against main's committed R43 plans, not this node's module: 112,000 seeds (every odd s in [3, 200001]; 3,000 random odd s at each of 40 and 64 bits; 3,000 random canonical exceptional n at each of those sizes) all match the classification: 103,773 ordinary cases, 8,227 exceptional cases with exactly the stated single u*, and 53,006 noncanonical seeds, all with requests below s. The fifth-family forward classification was not rebuilt; the status stays written"
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Full re-derivation of the classification theorem (every case of the normalised seed, the W9 elimination bound and the v = 9 case), the fifth-family decision theorem with identities (8) and (11), and the progression (12) with the rule exclusions re-derived from the rules' stated domains; independent implementation on all 65,536 odd seeds below 2^17, all 16,384 W9 inputs below 2^18 and the fifth family through m < 4096, reproducing the receipt's counts; certificate re-run (PASS, exit 0, 134.5 s). HOLDS; imprecisions only, no correction"
aliases: [R58]
tags: [convergence, outer-residual, tripling-pairs, critical-rank, forward-blocks]
---

# The unique rank excess in formal absorption, and a complete strict-rank domain in the fifth-exponent family

## Statement

Odd-only clock, 1 absorbing; `W5`, `W9` from [`critical-nine-elimination`](../critical-nine-elimination/README.md); `ρ(w) = ν(3w)`; `H_s` the unchanged formal absorption plan with boundary `[s] − Σ h_s(u) P(u)` after complete `W9` elimination; `n = ν(s)`.

1. **Unique excess.** Every requested `W5` rank is at most `n`, except precisely when canonical `n ≡ 27 (mod 48)`, `v2(3n − 1) = 4` and `3z` is noncanonical for `z = (3n − 1)/16`. Then exactly one request lies above `n`: `u = 4z + 1`, with coefficient `+1` and `ρ(u) = (9n+5)/8`; all others lie below `n`. At `n = 1` there are no requests. If `s` is noncanonical, even the exceptional rank is strictly below `s`. The proof includes every recursive `W9` branch and the small `v = 9` case. This refines the bound `(9ν(s)+5)/8` of [`critical-image-rank-composition`](../critical-image-rank-composition/README.md) in the same rank `ρ`.
2. **Fifth-exponent family.** For the full family `w = 437 + 512m` of [`sigma-rank-removes-absorption-overhead`](../sigma-rank-removes-absorption-overhead/README.md), the unchanged forward current is strict in the original `ρ` exactly unless `m ≡ 7 (mod 16)` and `3(2147 + 4374j)` is noncanonical, `j = (m − 7)/16`. Ordinary clocks stay `(6, 1)`, the quotient clock 5.
3. **New domain.** The full progression `w ≡ 4021 (mod 294912)` passes and is outside all twelve earlier direct domains ([`twelve-family-rho-dispatcher`](../twelve-family-rho-dispatcher/README.md)). The retained failure `w = 44981` still requests 96069 with rank `144103 > 134943`; `ρ` and `σ` remain distinct.

It does not mix `ρ` with `σ`, supply missing currents or establish universal coverage.

## Proof

The legacy note "The unique rank excess in formal absorption" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written complete classification of above-seed requests, with a
conditional forward rule on a complete arithmetic domain.** This refines
the R43 absorption bound while keeping the same rank rho. It does not mix
rho with sigma, supply missing currents, or establish universal coverage.

Use the absorbed odd Syracuse map S, the elementary minimum nu, W5 and W9
from [R40](../critical-nine-elimination/README.md), and
rho(w)=nu(3w). The unchanged formal plan H_s has boundary

    [s] = div H_s + sum_u h_s(u) P(u),    P(u)=[3u]-[u].       (1)

All h_s(u) are signed integers after complete W9 elimination. The
requests in (1) are premises. The existing general bound is
rho(u)<=(9nu(s)+5)/8. Here we characterize exactly when a request can
exceed nu(s), and use the characterization in the original rho order.

### 1. Complete classification of the excess

For a canonical n define the exceptional condition

    n=27 mod48,
    v2(3n-1)=4,
    z=(3n-1)/16, and 3z is noncanonical.                     (2)

**Theorem.** Put n=nu(s). If (2) fails, every request of H_s has rho<=n.
If (2) holds, H_s has exactly one request above n:

    u*=4z+1,  h_s(u*)=+1,  rho(u*)=(9n+5)/8.                (3)

Every other request then has rho<n. In particular, if s is noncanonical,
every request has rho<s even when its minimum is exceptional. At n=1
there are no requests. The bound n outside (2) is an upper bound, not an
assertion that some request always attains n.

#### Complete W9 elimination

First take a W9 input v. Its local R40 formulas have one possible
exceptional W5 request u*=4z+1 in the even-depth upper-noncanonical row.
All other local indices are at most

    (27v+13)/32.                                           (4)

For odd depth they are below v/2. For the upper-canonical even case,
(4) is R40's bound (9). In the upper-noncanonical case its lower bound
(9v+11)/12 is at most (4) for every v>=9; the other upper inputs are
smaller still. Thus (4) also applies to every recursive W9 input c.

An ordinary W5 request below v has rho<=3u<3v. Applying R43's already
proved W9 bound to a recursive c gives

    rho <= (27c+5)/8 <= (729v+511)/256 < 3v,                (5)

where the last inequality holds for v>=25. The only smaller W9 input
is v=9. Its exact elimination is P(9) -> P(21)-P(5); the former has
rho31>27 and the latter rho7<27, so it has precisely the stated exception.

The remaining possible large W5 index is the explicitly retained u*.
At depths d=4,6,8 its ranks are respectively

    (27v+5)/8,   (81v+23)/32,   (243v+101)/128.             (6)

Only the first exceeds3v. The latter two are strictly below3v for every
v>=9. At even depths d>=10 the exceptional index itself is below v and
therefore has rho<3v. This proves: in the full W9 plan, an excess over3v
occurs exactly at d4 with 3z noncanonical. Its coefficient remains+1,
since all other contributions have smaller rank. All signs and all
recursive W9 branches have been retained.

#### Formal absorption from an arbitrary seed

Normalize to n. For canonical n=1 mod8, the first arrow reaches
(3n+1)/4, so R43 bounds all its requests by(27n+29)/32<n (n>=9).
For a canonical n=2 mod3 outside that row, the prescribed free inverse
reaches(2n-1)/3, giving bound(3n+1)/4<n.

Otherwise n is a critical root. A W5 critical index gives its leading
request with rank n and auxiliary H inputs strictly below n. A W9
critical index can occur only when n=3v with v=9 mod16, equivalently
n=27 mod48. Indeed the alternative index v=(2n+1)/3 in W9 would force
n=5 mod8, contradicting canonicality. The preceding W9 classification
gives (2) and (3). The additional H_v requests have rank at most
(9v+5)/8<3v, so they cannot cancel or add a high request.

For noncanonical s, n<=(s-1)/2. Even the exceptional bound is at most
(9s+1)/16<s for s>1. This completes the theorem. Normalization adds only
its exact current and does not change the request vector.

### 2. Complete original-rho classification on the fifth-exponent family

R51 proved a whole sigma domain. Here the same current is tested in rho.
For every m>=0 set

    w=437+512m,  t=41+48m,  q=3w=32t-1,
    f=(243t-3)/8=3v,  v=415+486m.                         (7)

The full R26 block has exact first parameters a5,d3, ordinary common-tail
clocks(6,1) and quotient clock5 to nu(f). It obeys

    q-f=(13t-5)/8>0.                                    (8)

Let N_w be the normalizer current. The full signed comparison is

    J=D_q-N_w+H_f-H_nu(w).                               (9)

**Complete decision theorem for (9).** Every remaining request strictly
decreases rho if and only if the following failure condition is false:

    m=7 mod16,  j=(m-7)/16,
    z=2147+4374j, and 3z is noncanonical.                 (10)

When (10) holds, the sole request of rank at least q is u*=4z+1 with
coefficient+1. It has rank(9f+5)/8>q. This is an exact classification of
this signed plan, not a claim that failing inputs lack other currents.

**Proof.** By Section1 and f<q, a failure can occur only if f itself is
canonical and exceptional. A noncanonical f has all requests below f.
The condition v=9 mod16 in (7) is m=7 mod8. Write m=7+8l. Then

    v=3817+3888l,  9v-1=16(2147+2187l).

The depth is exactly4 iff l is even, giving m=7+16j and the z in (10).
This proves equivalence to the exceptional condition. At such a point,

    (9f+5)/8-q=(139t+77)/64>0.                           (11)

All other H_f requests have rank<f<q. Also nu(w)<w/4, so every lower
H_nu(w) request is below q. Hence the unique excess cannot cancel,
and the theorem follows including both implications.

#### A complete new subdomain of the twelve-rule complement

Every member of

    w=4021+294912k,   k>=0                              (12)

passes (9) and is outside all twelve previous direct predicates.
Here m=7+576k, j=36k, z=2147+157464k, and3z=1 mod8, hence3z is
canonical and (10) fails.

For the old predicates, 3w is nonselected with a5,d3, so every selected
rule and the first-a3/a4 R53 continuation is excluded. Also w=7 mod9,
so3 does not divide w. R45's k4 depth is0, while its k8 depth is1
and its endpoint r=4(8w+1)/3-1 is divisible3; that plan retains the
original request. R50's second depth v3(2r+1) is0. Thus R45, R47 and
R50 do not apply. The R48 endpoint is canonical f=3v with v in W9,
so its old sufficient bound is(9f+5)/8>q by (11), despite the actual
high request being absent. These exclusions exhaust the old twelve
families. No claim is made against later rules or supplied histories.

The former sigma example w44981 remains a failure here: its retained
child96069 has rho144103 above parent134943. The new classification
therefore does not silently make the two rank systems interchangeable.

### 3. Reproduction and exact supply

`exact_bound.py` returns the exceptional input explicitly and checks its
coefficient against the unchanged absorption implementation. It supplies
the complete fifth-family comparison and returns only strict-rho plans
from `one_step`. Missing or malformed supplied currents are rejected by
the existing R43 compiler. No unknown orbit is searched by these APIs.

Run:

```sh
python3 experiments/residual_progress/exact_absorption_bound/check_exact_bound.py
```

The adjacent receipt records bounded whole-seed checks, complete W9
eliminations, the fifth-family iff test, full new-progression samples,
the retained sigma incompatibility, and actual supplied-current conversions.
These finite checks verify the implementations; the universal quantifiers
and complete domain statements rest on the proofs above.

The focused replay checks16384 odd seeds below32768, including342 with
exceptional normalized minima,2048 complete W9 plans and2048 fifth-family
inputs (1983 decreasing,65 unresolved). It checks69 members of the new
progression through index2^128, the retained44981 failure and seven invalid
or missing-supply rejections. Three actual substitutions at4021,298933
and593845 store complete30-,105- and119-row outputs and all12 distinct
supplied pair currents. Fixture discovery is capped at10000 steps and1024
bits with cycle detection. Default replay reproduces the receipt and its
module/checker source hashes; these counts are finite evidence only.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B11 migration; standard library). The legacy scripts in this folder load their sibling modules by pre-migration folder names, so they no longer run here. This certificate rebuilds the legacy directory layout in a temporary directory from the node folders that now hold those files, runs the unmodified legacy checks there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied receipt unchanged. It writes nothing in the repository. It replays: the legacy checker `check_exact_bound.py` (about 12 s; the counts of section 3 and the three stored outputs, compared with `exact_bound_audit.json`) and the side-lane probe `r58_excess_check.py` (about 2 min, receipt reproduced byte for byte). The command in the legacy text names `experiments/residual_progress/exact_absorption_bound/`.

## Remarks

- The exceptional seeds are the later R65's adjacent-defect domain ([`adjacent-source-defect-equivalence`](../adjacent-source-defect-equivalence/README.md)), and R62 resolves the unique defect in the original rank ([`absorption-defect-original-rank-resolution`](../absorption-defect-original-rank-resolution/README.md)). The main lane's 2026-10-18 note `side_lane_review_767af32.md` (in [`two-selected-inverse-choices`](../two-selected-inverse-choices/README.md)) names this classification as structure for a complete recursion.
- Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/exact_absorption_bound/EXACT_ABSORPTION_BOUND.md` (legacy ID R58) at commit `be73a66`, by the B11 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; `check_legacy_replay.py` was added at the migration. The side-lane probe `reviews/side_lane/r58_excess_check.*` and the main lane's reproduction receipt `experiments/residual_progress/side_lane_review_c2319c9.json` moved here. Legacy status: "written classification and complete conditional forward domain".
- Main lane (ChatGPT, Codex), 2026-10-18, from commit `d265d94`. The batch's "independent model" proof and code reviews (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents, not a different lane.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No correction to the claim or proof; the review records that inequality (5) holds for every `W9` value except 9 (not only for `v ≥ 25`), that the bound `ρ ≤ n` outside (2) is attained by the leading request of every `W5`-critical seed, and that the certificate replays assert-based legacy checkers without `-O`. See [`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md).
