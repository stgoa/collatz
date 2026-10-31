---
id: returning-forward-interface
kind: result
title: "A complete forward interface on the returning W5 row, with strict-rank subdomains and arbitrarily long runs"
status: reviewed
claim: >
  Odd-only 3x+1 map S, absorbing at 1; rho(w) = nu(3w). On the whole returning row E_return = {w in W5 : w = 3
  mod 9, 3w selected}, 3w = 2^a t - 1 (a >= 3, t = 3^a mod 4, 2^a t = 10 mod 27), q = rho(w) = 2^(a-1) t - 1
  reaches r = (3^(a-1) t - 1)/2 by the exact word 1^(a-2),2, and with z = nu(w) the current N_(3w) + prefix -
  N_w + H_r - H_z has boundary P(w) minus the signed difference of the two request vectors. Every lower request
  has smaller rank; a complete canonical endpoint table bounds the upper ranks and gives a decidable sufficient
  strict-rank test. The test holds on every a = 3 input with r noncanonical or r = 1 mod 8, and every a = 4
  input with r noncanonical; for every a >= 3 and k >= 1 with 4^k (2^(a+3) - 20) > 3^(a+1) - 3, r = F^k(s) gives
  complete nonempty CRT families with arbitrarily long rising runs. Prescribed absorption undoes only prefixes
  through a-3, and the full R41 inverse at r undoes the whole run (failures of specified compositions, not of
  all forward comparisons). Index decrease alone is insufficient: w = 6645 requests 4205 < w with rho(4205) =
  12615 > 9967 = rho(6645), left unresolved.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [critical-image-rank-composition, decreasing-w5-phase-inverse-barrier, critical-nine-elimination, critical-tripling-domain-equivalence, elementary-bridge-quotient-normal-form]
certificates: [check_legacy_replay.py]
evidence:
  - "check_returning_phase.py, returning_phase.py, returning_phase_audit.json: the legacy constructor (forward_plan, compile_forward_plan, sibling_family) and checker: 2048 bounds, 228 returning inputs (126 rank-descending), 456 undo checks, 96 CRT examples through a = 128 and 12 actual substitutions. Fails at its new path: returning_phase.py loads ../critical_inverse/critical_inverse.py (now ../decreasing-w5-phase-inverse-barrier/) by its pre-migration folder name; returning_phase.py is itself loaded by its old path by later legacy rules. Passed at be73a66 as experiments/residual_progress/returning_phase/check_returning_phase.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
  - "The side-lane probe touching this node is ../critical-image-rank-composition/batch_r43_r46_check.py (recorded under reviewed_by)."
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-17
    link: ../critical-image-rank-composition/batch_r43_r46_check.py
    scope: "Finite only (side-lane feed entry 2026-10-17 22:16, VERIFIED, main a06ef3c), with the lane's own nu and Syracuse step. Only the rank values rho(6645) = 9967 and rho(4205) = 12615 of the index-versus-rank example were checked. The entry says: The R43 composition theorem and the R44/R45 accepted-domain classifications were not rebuilt here. The status stays written"
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Full re-derivation of the parametrisation, the exact word, the interface identity, the endpoint table, the two complete subdomains, the stratum thresholds, the CRT families and both undo loops, with an independent implementation reproducing the receipt's 228 plans and 456 undo checks and extending the subdomain and family checks; certificate re-run (PASS, 6 s); 3x+d analogues of the identities checked. HOLDS"
aliases: [R44]
tags: [convergence, outer-residual, tripling-pairs, critical-rank, returning-row, conditional-compiler]
---

# A complete forward interface on the returning W5 row, with strict-rank subdomains and arbitrarily long runs

## Statement

Odd-only clock, 1 absorbing; `ρ(w) = ν(3w)`; `H_s` the formal absorption plan with request ranks at most `(9s+5)/8` ([`critical-image-rank-composition`](../critical-image-rank-composition/README.md)).

1. **Whole-row interface.** On `E_return = {w ∈ W5 : w ≡ 3 (mod 9), 3w selected}` write `3w = 2^a t − 1`, `a ≥ 3`, `t ≡ 3^a (mod 4)`, `2^a t ≡ 10 (mod 27)`. Then `q = ρ(w) = 2^(a−1)t − 1` reaches `r = (3^(a−1)t − 1)/2 ≡ 4 (mod 9)` by the exact word `1^(a−2), 2`, and with `z = ν(w)` the current `L_w = N_(3w) + G − N_w + H_r − H_z` has `div L_w = P(w) − Σ (A_r(u) − A_z(u)) P(u)`. Every lower request has rank below `q`; a complete canonical endpoint table bounds the upper ranks and gives a decidable sufficient strict-rank test.
2. **Subdomains.** The test holds on every `a = 3` input with `r` noncanonical or `r ≡ 1 (mod 8)`, and on every `a = 4` input with `r` noncanonical, with no size cap.
3. **Long runs.** For every `a ≥ 3` and `k ≥ 1` with `4^k(2^(a+3) − 20) > 3^(a+1) − 3`, endpoints `r = F^k(s)` give complete nonempty CRT families (10)–(11) that pass; the initial path length `a − 1` and the ratio `r/w` are unbounded.
4. **Undo loops.** Appending prescribed absorption undoes only the prefixes through `a − 3`; at `a − 2` the endpoint is `1 (mod 8)` and takes its forward step. The full R41 inverse at `r` undoes the entire run. These delimit failed recipes, not all forward comparisons.

Index decrease alone does not give the common rank: `w = 6645` requests `4205 < w`, but `ρ(4205) = 12615 > 9967 = ρ(6645)`; that plan stays unresolved. Universal coverage of the returning row is open.

## Proof

The legacy note "A forward interface for the complete returning phase" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written conditional reduction and finite certificates.** The interface
below is defined on the entire returning row of R41. Two complete subdomains,
and nonempty families with arbitrarily long initial runs, have strictly
decreasing critical-image rank. The other inputs remain explicit obligations.
No universal current or convergence theorem is supplied.

Use the odd-only Syracuse map `S`, killed atoms `[1]=0`, and
`P(w)=[3w]-[w]`. Let `nu` be the elementary minimum from R25 and
`rho(w)=nu(3w)` for a critical pair. Let `W5={w>0:w=5 mod8}`.
An elementary current `N_x` has divergence `[x]-[nu(x)]`.
All currents and requests below are signed integer objects.

Dependencies are the [elementary normal form](../elementary-bridge-quotient-normal-form/README.md),
[R37 formal absorption](../critical-tripling-domain-equivalence/README.md),
[R40 W9 elimination](../critical-nine-elimination/README.md),
[R41 returning phase](../decreasing-w5-phase-inverse-barrier/README.md), and
[critical-image rank bound](../critical-image-rank-composition/README.md).

### 1. Exact whole-domain parameters and two undo loops

The domain is exactly

```
E_return={w in W5: w=3 mod9 and 3w is selected}.
```

Here selected means `x=2^a t-1`, with `t` odd and `t=3^a mod4`.
Every member, and conversely every positive parameter choice below, has

```
3w=2^a t-1,   a>=3,
t=3^a mod4,   2^a t=10 mod27.                         (1)
q=rho(w)=(3w-1)/2=2^(a-1)t-1,
r=(3^(a-1)t-1)/2=4 mod9.
```

The binary congruence makes `w=5 mod8` and selected `3w`; the ternary
congruence is precisely `w=3 mod9`. Both fix exact valuations, including
the binary phase beyond the divisibility bit. The ordinary path from `q`
to `r` has the exact valuation word

```
1^(a-2),2,     length a-1.                             (2)
```

For `0<=j<=a-3` its intermediate values are
`q_j=3^j 2^(a-1-j)t-1`. Each is complementary canonical; for `j>=1`
it is `2 mod3`. Consequently R37's first inverse step at `q_j` is exactly
`(2q_j-1)/3=q_(j-1)`. Appending the old absorption plan after any such
prefix cancels that prefix, including its formal coefficients. This is
the first complete undo loop. At the next state `q_(a-2)`, the binary
phase is instead canonical `1 mod8`; R37 takes its forward arrow to `r`.
The undo claim stops before that state. For example `w=93` has `q=139`
and `S(q)=209=1 mod8`; appending `H_209` need not cancel the first arrow.

At the endpoint, `v3(2r+1)=a-1`, because (1) makes `3` coprime to `t`.
The complete R41 inverse phase at `r` has lower endpoint
`2^(a-1)(2r+1)/3^(a-1)-1=q` and uses precisely the reverse of (2).
Appending this inverse current cancels the entire forward current. This is
the second complete undo loop. Neither observation rules out a different
forward comparison; both delimit a failed recipe exactly.

### 2. A complete signed interface with a different endpoint comparison

Write the finite formal W5 absorption plan of R41 as

```
div H_s=[s]-sum_u A_s(u)P(u).                         (3)
```

It is available arithmetically for every positive odd `s`, but its missing
pair currents are not supplied. Let `G` be the ordinary current along (2),
and put `z=nu(w)`. Since `w=5 mod8`, `z<=(w-1)/4`. Then

```
L_w=N_(3w)+G-N_w+H_r-H_z,
div L_w=P(w)-sum_u (A_r(u)-A_z(u))P(u).               (4)
```

Indeed the first three terms have divergence `P(w)-[r]+[z]`.
Adding (3) proves (4), with full multiplicities and both signs. Formula
(4) is the promised finite interface on every member of (1). It makes
no unknown orbit search. Opposite requests are combined before use.

The generic R43 bound is

```
A_s(u) nonzero => rho(u)<=(9s+5)/8.                  (5)
```

The lower plan `H_z` always has rank strictly below `q`, since
`z<=(w-1)/4` and `(9z+5)/8<q`. Only the upper plan needs a new test.
An exact current for every remaining requested pair, substituted with its
signed coefficient, produces an exact current of divergence `P(w)`.
The compiler rejects missing or incorrect currents and does not search
for them.

#### A sharper complete endpoint bound

Put `n=nu(r)`. Applying (5) after the first prescribed R37 step gives the
following rational upper bounds on **every** rank requested by `H_r`:

| Canonical minimum `n` | Rank bound |
|---|---|
|`n=1`|`0`|
|`n=1 mod8`, `n>1`|`(27n+29)/32`|
|`n=3 mod4`, `n=2 mod3`|`(3n+1)/4`|
|`n=3 mod4`, `n=1 mod3`|`n`|
|`n=3 mod4`, `n=0 mod3`, `n/3 in W5`|`n`|
|`n=3 mod4`, `n=0 mod3`, `n/3 in W9`|`(9n+5)/8`|

For the first nontrivial row, `S(n)=(3n+1)/4`, giving (5). For the next,
the free inverse seed is `(2n-1)/3`. In the direct W5 rows, the first
request has rank exactly `n`; subsequent absorption of the smaller pair
index has rank below `n` by (5). The W9 row uses R43's complete W9 bound.
These are all possible canonical minima. If the applicable bound is below
`q`, (4) is a strictly rank-decreasing rule. This test is sufficient; an
unresolved result is not a proof of impossibility or of nonconvergence.

### 3. Two complete low-valuation subdomains

The rank test always succeeds on:

1. Every returning input with `a=3` for which `r` is **not** complementary
   canonical: `r` is noncanonical or `r=1 mod8`.
2. Every returning input with `a=4` for which `r` is noncanonical.

If `r` is noncanonical, `nu(r)<=(r-1)/2`; hence (5) improves to
`rho(u)<=(9r+1)/16`. If `r=1 mod8`, the first forward step instead gives
`rho(u)<=(27r+29)/32`.

For `a=3`, (1) is exactly `t=35 mod108`, so `t>=35`.
The noncanonical bound is smaller than `q=4t-1`; the `1 mod8` bound is
smaller precisely when `13t>95`, which always holds here.
For `a=4`, (1) is exactly `t=85 mod108`; the noncanonical bound is
smaller than `q=8t-1` precisely when `13t>25`, again always true.
The corresponding pair indices are also strictly below `w`.
These assertions cover their entire parameter domains, without a size cap.

### 4. Exact stratum thresholds and arbitrarily long successful runs

Every endpoint has a unique elementary stratum

```
r=lambda*n+beta,    n=nu(r),
(lambda,beta)=(4^k,(4^k-1)/3), or
              (2*4^k,(4^(k+1)-1)/3).                 (6)
```

The generic sufficient test `(9n+5)/8<q` is exactly

```
(2^(a+3)lambda-3^(a+1))*t >26lambda-18beta-9.        (7)
```

If `n>1` and `n=1 mod8`, the sharper forward test is exactly

```
(2^(a+5)lambda-3^(a+2))*t >122lambda-54beta-27.       (8)
```

These are also exactly the index tests `(3n+3)/4<w` and
`(9n+15)/16<w`, respectively. They are not assumed to hold for all
strata. In particular the new rank condition must not be replaced by an
index-only assertion on a direct critical request. For example `w=6645`
has parent rank `9967`; its formal request `u=4205<w` has rank `12615`.
The implementation retains this plan as unresolved for the common-rank
compiler, even though its pair-index bound decreases.

For each `a>=3`, choose any integer `k>=1` satisfying

```
4^k(2^(a+3)-20)>3^(a+1)-3.                          (9)
```

Such a `k` exists. Every returning member whose endpoint has at least `k`
sibling factors, `r=F^k(s)=4^k s+(4^k-1)/3` with `s` positive odd,
passes the generic bound using `s`. Substituting this scale and offset
in (7) makes its right side `20*4^k-3`; (9) makes the slope difference
larger than that already at `t=1`. Further elementary normalization only
reduces the generic bound.

This domain is nonempty and explicit for every `a,k`. Put
`lambda=4^k`, `beta=(lambda-1)/3`, `B=4lambda`, and choose the CRT progression

```
t=(2beta+2lambda+1)*3^(1-a) mod B,
t=10*2^(-a) mod27.                                  (10)
```

The moduli are coprime. The first congruence means exactly that
`(3^(a-1)t-1)/2=F^k(s)` for odd `s`; as `k>=1` it also implies the selected
phase `t=3^a mod4`. Every positive member of (10) gives (1), a positive
odd `s`, and strict descent. If `t0` is its least positive representative,
the pair indices are

```
w=(2^a t0-1)/3 + (9*2^a*B)j,   j>=0.               (11)
```

Thus the initial path length `a-1` is unbounded. Along these families,
`r/w` is unbounded as `a` grows: explicitly
`r/w=(3/2)(3^(a-1)t-1)/(2^a t-1)` has leading ratio
`(1/2)(3/2)^a`, and for `a>=3,t>=1` it exceeds
`(4/9)(3/2)^a`. A long or high first excursion therefore does not by
itself defeat this rule. This does not cover every endpoint of such a run.

### 5. Executable scope

`returning_phase.py` exports `forward_plan(w)` on the whole domain. Its
`seed`, `rank`, `current`, and signed `coefficients` satisfy (4).
`status='descending'` means the proved endpoint rank bound is strictly
below the parent rank. `index_status` is recorded separately. Unresolved
plans retain all requests. `compile_forward_plan` requires a descending
plan and exact supplied pair currents. `sibling_family` constructs (10).

Run:

```
python3 experiments/residual_progress/returning_phase/check_returning_phase.py
```

The deterministic receipt records exhaustive bounded interface checks,
both undo loops, the rational bounds, low-valuation classes, long CRT
families, capped discovery only for specified demonstration inputs, and
actual substituted currents. This finite evidence checks implementation;
the arguments above give the unbounded quantifiers. Universal coverage of
the remaining returning phase is open.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B11 migration; standard library). The legacy scripts in this folder load their sibling modules by pre-migration folder names, so they no longer run here. This certificate rebuilds the legacy directory layout in a temporary directory from the node folders that now hold those files, runs the unmodified legacy checks there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied receipt unchanged. It writes nothing in the repository. It replays: the legacy checker `check_returning_phase.py` (about 2 s; the counts of section 5 and the stored compiled currents, compared with `returning_phase_audit.json`). The command in the legacy text names `experiments/residual_progress/returning_phase/`.

## Remarks

- A second full run before requesting inputs is [`returning-second-forward-interface`](../returning-second-forward-interface/README.md); a separate rank on this row is [`sigma-rank-removes-absorption-overhead`](../sigma-rank-removes-absorption-overhead/README.md). The endpoint table is reused by [`forward-blocks-low-exponent-tests`](../forward-blocks-low-exponent-tests/README.md) and [`selected-critical-five-forward-tables`](../selected-critical-five-forward-tables/README.md).
- A main-lane model review corrected the first undo endpoint from `a − 2` to `a − 3` before the commit (archive/convergence-residual-progress/REPORT.md); the migrated text has the corrected value.
- Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/returning_phase/RETURNING_FORWARD_INTERFACE.md` (legacy ID R44) at commit `be73a66`, by the B11 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; `check_legacy_replay.py` was added at the migration. Legacy status: "written whole-domain conditional identity and strict-rank rules on specified subdomains".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `a06ef3c`. The batch's "independent model" proof and code reviews (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents, not a different lane.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No correction needed; see [`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md).
