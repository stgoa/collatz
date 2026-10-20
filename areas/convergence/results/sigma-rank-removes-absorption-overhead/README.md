---
id: sigma-rank-removes-absorption-overhead
kind: result
title: A separate rank sigma removes the absorption-bound overhead and certifies a further forward domain
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; rho(w) = nu(3w); E_return = {w in W5 : w = 3 mod 9, 3w selected}. Define
  sigma(w) = 4w/3 - 1 = (8 rho(w) - 5)/9 on E_return and sigma(w) = rho(w) otherwise. Every W5 request u in the
  unchanged formal absorption plan H_s has sigma(u) <= nu(s) <= s (in the only rank-expanding d = 4 row of the
  W9 elimination the exceptional index is returning with sigma = 3b, all others below). Every nonselected W5
  input with first exponent a = 5 and odd d >= 3 has an accepted sigma forward plan; the exact a = 5, d = 3
  domain is w = 437 mod 512 (q = 32t - 1, f = (243t-3)/8 < q). The two inductions cannot be mixed automatically:
  at w = 44981 the child 96069 increases rho (134943 -> 144103) but decreases sigma (134943 -> 128091), while
  the valid old-rho R44 plan at 4629 requests 2197, increasing sigma (6171 -> 6591). Any fixed family of exact
  signed rules each decreasing sigma gives the same conditional composition theorem as for rho; the separate
  sigma dispatcher keeps the nonreturning old rules and retests returning inputs. Universal supply of the
  remaining inputs is open.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [critical-image-rank-composition, decreasing-w5-phase-inverse-barrier, returning-forward-interface, forward-blocks-low-exponent-tests, critical-nine-elimination, complementary-run-bridges]
certificates: [check_legacy_replay.py]
evidence:
  - "check_sigma_rank.py, sigma_rank.py, sigma_rank_audit.json, w44981_certificate.json: the legacy sigma dispatcher, compiler and checker: 1024 W9 eliminations, 4096 absorption plans, 132 exact progression examples through index 2^128, both rank-comparison counterexamples and five actual substitutions; the w = 44981 certificate is stored. On 1024 W5 inputs below 8192 the old dispatcher accepts 442 and the sigma dispatcher 459, 441 shared (finite conditional rule domains, illustrating incomparability). Fails at its new path: sigma_rank.py puts ../double_inverse/ (now ../two-inverse-phases-intermediate-increase/) on sys.path by its pre-migration folder name and loads further siblings the same way. Passed at be73a66 as experiments/residual_progress/phase_rank/check_sigma_rank.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
  - "batch_r51_r54_check.py, batch_r51_r54_check.json: side-lane probe (Claude side lane, 2026-10-17) of the R51 rank values and of the R54 phase and seven-step family (growing-prefix-unhandled-leading-input). Fails at its new path: it imports affine_controls from experiments/packet_currents/negative_controls/ by repository-relative path (now ../locally-collatz-like-control-barrier/) and fibre_count_check from its own folder (now ../absorbed-fibre-uniform-counts/). Passed at be73a66 as reviews/side_lane/batch_r51_r54_check.py (archive/legacy-checker-run-be73a66.md, exit 0); its receipt is reproduced byte for byte by check_legacy_replay.py"
  - "sigma_stopping_plans.py, sigma_stopping_plans.json: side-lane FINDING (2026-10-17 23:43): plain quotient-orbit prefixes from q = nu(3w) to the first state below sigma(w) give plans that main's sigma validator accepts on all 3,600 sampled W5 inputs (24, 40, 64 bits, every class), with the lookahead needed tabulated by class (98.4% need at most 32 quotient steps; largest observed 89). A measurement with validated plans, not a theorem: it covers sampled inputs only, and the general strict-rho version (with target (8 rho(w) - 5)/9) is the side lane's later written argument, now ../quotient-prefix-plans-rho-decreasing/ (R62-b). Fails at its new path: it imports backward_word_rule from its own folder (now ../negative-cycle-backward-word/), which loads sigma_rank and continued_rules from experiments/residual_progress/ by repository-relative path. Passed at be73a66 as reviews/side_lane/sigma_stopping_plans.py (archive/legacy-checker-run-be73a66.md, exit 0)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-17
    link: batch_r51_r54_check.py
    scope: "Finite only (side-lane feed entry 2026-10-17 23:32, VERIFIED, main 8764158; the R51 part), with the lane's own nu and step: the rank values rho(44981) = 134943, rho(96069) = 144103, sigma(96069) = 128091, sigma(4629) = 6171 and rho(2197) = sigma(2197) = 6591. The uniform bound, the endpoint table and the a = 5 forward domain were not rebuilt; the status stays written"
aliases: [R51]
tags: [convergence, outer-residual, tripling-pairs, critical-rank, sigma-rank, returning-row]
---

# A separate rank sigma removes the absorption-bound overhead and certifies a further forward domain

## Statement

Odd-only clock, 1 absorbing; notation of [`critical-image-rank-composition`](../critical-image-rank-composition/README.md); `E_return = {w ∈ W5 : w ≡ 3 (mod 9), 3w selected}` as in [`returning-forward-interface`](../returning-forward-interface/README.md). Define `σ(w) = 4w/3 − 1 = (8ρ(w) − 5)/9` on `E_return` and `σ(w) = ρ(w)` otherwise; `w < σ(w) ≤ ρ(w)`.

1. **Uniform bound.** Every `W5` request `u` of the unchanged formal plan `H_s` has `σ(u) ≤ ν(s) ≤ s`. In the only rank-expanding `d = 4` row of [`critical-nine-elimination`](../critical-nine-elimination/README.md) the exceptional index `u = (9b+3)/4` is returning with `σ(u) = 3b`, and all other requests have `σ < 3b`. A complete first-step endpoint table sharpens the bound.
2. **New forward domain.** Every nonselected `W5` input with first exponent `a = 5` and odd `d ≥ 3` has an accepted `σ` forward plan; the exact `a = 5`, `d = 3` domain is `w ≡ 437 (mod 512)`, `q = 32t − 1`, `f = (243t − 3)/8 < q`.
3. **Incompatibility.** At `w = 44981` the child 96069 increases `ρ` (134943 → 144103) but decreases `σ` (134943 → 128091); the valid old-`ρ` plan of R44 at `w = 4629` requests 2197, increasing `σ` (6171 → 6591). The two inductions cannot be mixed automatically.
4. **Composition.** Any fixed family of exact signed rules whose every edge decreases `σ` gives the conditional composition theorem of R43 in `σ`; old strict-`ρ` rules at parents outside `E_return` also decrease `σ`. The separate `σ` dispatcher keeps those rules and retests returning inputs; it does not modify the old dispatcher.

Universal supply of the remaining inputs is open; no asymptotic coverage is claimed.

## Proof

The legacy note "A separate rank absorbs the critical-nine expansion" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written uniform bound and conditional construction.** The rank
below changes how the returning W5 inputs are ordered. It removes the
factor9/8 from formal absorption bounds and certifies a complete further
forward domain. It cannot be substituted silently into the earlier rule
union. Universal supply of the remaining inputs is still open.

Use the notation of [R43](../critical-image-rank-composition/README.md).
All currents are finite signed integer currents; H_s is the unchanged
R41 formal absorption plan with divergence[s] minus its signed W5 requests.
Let E_return={w in W5:w=3 modulo9 and3w selected}, as in
[R44](../returning-forward-interface/README.md). Define

```
sigma(w) = 4w/3−1 = (8rho(w)−5)/9, if w in E_return;
           rho(w),                  otherwise.                 (1)
```

Every w in W5 satisfies w<sigma(w)<=rho(w). The exceptional value is
the canonical W9 ancestor in the R41 returning phase. This is a specified
integer rank, not a claim that it is the minimum of all inverse ancestors.

### 1. Uniform absorption bound

**Theorem.** Every W5 request u in H_s satisfies

```
sigma(u) <= nu(s) <= s.                                      (2)
```

First consider the complete R40 elimination of a W9 request b. Every
resulting request u has sigma(u)<=3b. In its local proof, all ordinary
smaller-index requests satisfy rho(u)<=3u<3b. The only larger indices
occur in the three rows d=4,6,8 listed in R43. The d6 and d8 exceptional
rho values are already strictly below3b. In the d4 row the exceptional
index is u=(9b+3)/4, with selected3u and u=3 modulo9. Consequently

```
sigma(u)=4u/3−1=3b.                                        (3)
```

All auxiliary requests in this row have smaller index than b. Every
recursive W9 request c is also smaller than b; induction bounds its
descendants by3c<3b. This proves the asserted bound for the full signed
elimination. Cancellation can remove requests and cannot introduce a
larger one.

Now the original R37 absorption plan first normalizes s and strictly
decreases its seed thereafter. A direct W5 request has rho<=nu(s), hence
sigma<=nu(s). A W9 request b comes from a critical root3b<=nu(s), and
the preceding argument handles its elimination. This proves(2).
The bound can be attained: H_27 requests21, with sigma(21)=27.

### 2. Complete first-step endpoint bounds

The following integer bounds B_sigma(n) apply to every request in H_s,
where n=nu(s):

| Canonical n | Bound |
|---|---|
|n=1|0|
|n>1,n=1 modulo8|(3n+1)/4|
|n=3 modulo4,n=2 modulo3|(2n−1)/3|
|critical n with W5 index v|sigma(v)|
|critical n with W9 index|n|

The first two nontrivial rows apply(2) after the prescribed forward or
inverse step. In the W5 row the leading request is v and all other
requests have sigma<=v<sigma(v). The W9 row uses(2). Thus the table is
a proved upper bound; it is not asserted to equal the actual maximum in
every case. Each row includes its integer offset.

The R44 returning and R48 nonselected full forward interfaces remain exact
signed identities. Reuse their currents and accept an interface when

```
B_sigma(nu(endpoint)) < sigma(w).                            (4)
```

The lower absorption input z=nu(w)<w/4 always has sigma ranks<=z<sigma(w).
Hence every final request in an accepted interface strictly decreases(1).
The ordinary and quotient clocks remain precisely those of R44/R48.

### 3. A complete additional forward domain

Every positive input

```
w=437+512m,   m>=0,                                        (5)
```

has nonselected q=3w=32t−1, with t=41+48m and exact first parameters
a=5,d=3. Conversely these conditions on nonselected W5 give(5): the
valuation condition is t=9 modulo16 and integrality is t=2 modulo3.
The full R26 endpoint is

```
f=(243t−3)/8,
q−f=(13t−5)/8>0.                                         (6)
```

By(2) every upper request has sigma<=nu(f)<=f<q=sigma(w).
The full forward current therefore gives a strict-sigma reduction on
every member of(5). More generally a=5 and any odd d>=3 satisfy f<q:
increasing d by2 multiplies f's positive affine numerator by3 and its
denominator by4, so its value decreases for fixed t. This comparison is
used only for parameter values having the stated exact valuation.

This need not decrease rho. At w44981 the current has a request96069:

```
parent: rho=sigma=134943;
child:  rho=144103, sigma=128091.
```

The parent is outside the earlier seven direct rule domains. The example
illustrates the different order; the proof of(5) does not depend on it.

### 4. Compatibility is a theorem obligation

Every old strict-rho rule at a parent outside E_return also decreases
sigma: its parent ranks agree, and every child's sigma is no larger than
its rho. Thus the six old rule families outside R44 remain valid.
The returning rule must be retested. A concrete failure is

```
w4629: rho=6943, sigma=6171;
R44 requests {5:−1,69:+1,2197:+1};
sigma(2197)=rho(2197)=6591>6171.
```

This is a valid old-rho rule and an invalid sigma step. It prevents claiming
that all previously accepted rules automatically compose with the new
ones. Neither rank invalidates the proofs using the other rank.

For any fixed family of exact signed rules whose every edge decreases
sigma, strong induction on its positive integer values supplies the same
conditional composition theorem as R43. Universal currents on its
unrecognized W5 complement suffice by R40/R37; the complement remains
missing. `sigma_rank.py` uses the old nonreturning rules and the retested
forward interfaces. It is a separate dispatcher and compiler, with
explicit rank validation and missing-input rejection. It does not modify
the old seven-rule dispatcher.

### 5. Reproduction

Run `python3 experiments/residual_progress/phase_rank/check_sigma_rank.py`.
The finite audit checks complete W9 and absorption samples, endpoint
bounds, all members of(5) within a declared range and large prescribed
examples, both rank-comparison counterexamples, signed mixed closure and
actual supplied-current substitution. The saved44981 fixture retains its
inputs and output. The infinite statements rest on the proof above.

The deterministic receipt contains1024 W9 eliminations,4096 absorption
plans,132 progression examples (including indices through2^128) and five
actual substitutions. On1024 W5 inputs below8192, the old dispatcher accepts
442 and this dispatcher459;441 are shared,18 occur only in the sigma
dispatcher and one only in the old dispatcher. These finite sets are
incomparable, consistent with the explicit4629 counterexample. They are
conditional rule domains, not counts of independently proved absorption.

No universal current constructor, asymptotic coverage or novelty claim is
supplied. In particular improving an input bound does not force every
forward block to satisfy(4).

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B11 migration; standard library). The legacy scripts in this folder load their sibling modules by pre-migration folder names, so they no longer run here. This certificate rebuilds the legacy directory layout in a temporary directory from the node folders that now hold those files, runs the unmodified legacy checks there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied receipt unchanged. It writes nothing in the repository. It replays: the legacy checker `check_sigma_rank.py` (about 4 s; the counts of section 5, compared with `sigma_rank_audit.json` and `w44981_certificate.json`) and the side-lane probe `batch_r51_r54_check.py` (under 1 s, receipt reproduced byte for byte). The command in the legacy text names `experiments/residual_progress/phase_rank/`.

## Remarks

- **Mixing.** A finite survey of combining the two dispatchers is [`rho-sigma-rank-mixing`](../../attempts/rho-sigma-rank-mixing/README.md); the exact excess of `ρ` over the seed is [`rank-excess-absorption-classification`](../rank-excess-absorption-classification/README.md), which also keeps `w = 44981` as a retained failure in `ρ`.
- **Side-lane measurement.** `sigma_stopping_plans` in this folder (finite, sampled) found validated `σ` quotient-prefix plans on every sampled input, including the selected classes no `ρ` rule then reached. The side lane's later written `ρ` version, with target `(8ρ(w) − 5)/9`, is [`quotient-prefix-plans-rho-decreasing`](../quotient-prefix-plans-rho-decreasing/README.md) (R62-b, reviewed), built on R62's compatibility theorem ([`absorption-defect-original-rank-resolution`](../absorption-defect-original-rank-resolution/README.md)).
- Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/phase_rank/PHASE_RANK.md` (legacy ID R51) at commit `be73a66`, by the B11 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; `check_legacy_replay.py` was added at the migration. The side-lane probes `reviews/side_lane/batch_r51_r54_check.*` and `sigma_stopping_plans.*` moved here. Legacy status: "written uniform rank bound, complete forward domain and conditional compiler".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `8764158`. The batch's "independent model" proof and code reviews (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents, not a different lane.
