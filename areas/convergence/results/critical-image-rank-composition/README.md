---
id: critical-image-rank-composition
kind: result
title: The critical-image rank rho(w) = nu(3w) bounds every formal request and composes strict-rank rules
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; P(w) = [3w] - [w]; rho(w) = nu(3w) on W5 u W9 (W5 = {5 mod 8}, W9 = {9
  mod 16}). (W9 bound) Every W5 request u of the fully expanded critical-nine-elimination plan for w in W9
  satisfies 8 rho(u) <= 27w + 5; the exceptional d = 4, 6, 8 ranks are (27w+5)/8, (81w+23)/32, (243w+101)/128,
  and only d = 4 can increase rank. (Absorption bound) Every request of the W5-only formal absorption plan H_s
  has rho(u) <= (9s+5)/8; for a critical root p with pair index v every H_v input has rank at most (3p+4)/4 < p
  (p > 4). (Composition) If a rule on A in W5 supplies finite currents with div J_w = P(w) - sum c_w(u) P(u) and
  all requested ranks strictly below rho(w), then universal currents on W5 minus A suffice for Collatz (and
  conversely); finite unions under one fixed priority compose, pair indices may increase, and formal recursive
  substitution terminates with unhandled leaves retained. Neither termination of the formal expansion nor any
  finite sample supplies a leaf; the returning self-request of decreasing-w5-phase-inverse-barrier is not
  repaired by the rank.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [critical-nine-elimination, decreasing-w5-phase-inverse-barrier, critical-tripling-domain-equivalence, elementary-bridge-quotient-normal-form]
certificates: [check_legacy_replay.py]
evidence:
  - "check_rank_closure.py, rank_closure.py, critical_rank_audit.json, w749_inputs.json, w749_current.csv: the legacy rank bounds, generic signed closure compiler and checker: 2048 full W9 reductions, 4096 absorption bounds, the three exceptional affine rows, all 1024 W5 candidates below 8192 under the union (195 accepted, 58 expanding through more than one rule), seven actual substitutions (P1029 closes with no input; P749 has stored inputs and output) and the rejection cases. Fails at its new path: rank_closure.py loads ../critical_inverse/critical_inverse.py (now ../decreasing-w5-phase-inverse-barrier/) by its pre-migration folder name; rank_closure.py is itself imported by its old path by most later legacy rules and side-lane probes. Passed at be73a66 as experiments/residual_progress/critical_rank/check_rank_closure.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
  - "rules_union.py: the fixed-priority union of four strict-rank rules (R41 E_good, R45 base phase, accepted R44 interface, R46 inverse escape; returning-forward-interface, base-inverse-phases-increasing-pairs, variable-depth-inverse-escape-barrier), checked by check_rank_closure.py; it loads ../returning_phase/, ../nonselected_inverse/ and ../inverse_escape/ by their pre-migration names. It is the base of the later seven-, nine- and twelve-family dispatchers (two-inverse-phases-intermediate-increase, low-block-continuation-prescribed-growth, twelve-family-rho-dispatcher)"
  - "batch_r43_r46_check.py, batch_r43_r46_check.json: side-lane probe (Claude side lane, 2026-10-17) of the R46 escape identity and depth-4 law and of three R44/R45 rank values; recorded under reviewed_by in variable-depth-inverse-escape-barrier, returning-forward-interface and base-inverse-phases-increasing-pairs. It does not check this node's bounds or composition theorem. Fails at its new path: it imports affine_controls from experiments/packet_currents/negative_controls/ by repository-relative path (now ../locally-collatz-like-control-barrier/) and fibre_count_check from its own folder (now ../absorbed-fibre-uniform-counts/). Passed at be73a66 as reviews/side_lane/batch_r43_r46_check.py (archive/legacy-checker-run-be73a66.md, exit 0); its receipt is reproduced byte for byte by check_legacy_replay.py"
  - "side_lane_review_3d69784.json: the main lane's reproduction (2026-10-17) of the unmodified probe batch_r43_r46_check.py at side-lane commit 3d69784, PASS, with scope 'Finite external identity/depth4/rank checks reproduced; R43 composition and R44/R45 domain proofs not independently rebuilt by this probe'. A main-lane review of a side-lane probe, not a review of this node"
  - "union_acceptance_meter.py, union_acceptance_meter.json: side-lane measurement (2026-10-17 22:21) of the fixed-priority union in rules_union.py: random w = 5 (mod 8) at 10 to 80 bits, accepted share about 17 to 19% at every size (R41 about 11.9%, R44 3.0%, R45 1.8%, R46 2.2% at 48 bits). It measures the dispatcher; it does not check it, and gives no asymptotic coverage statement. Fails at its new path: it imports rules_union from experiments/residual_progress/critical_rank/ by repository-relative path (now this folder, which itself loads moved siblings by their old names). Passed at be73a66 as reviews/side_lane/union_acceptance_meter.py (archive/legacy-checker-run-be73a66.md, exit 0)"
  - "union_gap_map.py, union_gap_map.json: side-lane measurement (2026-10-17 22:44) of where the uncovered 81.6% of W5 sits under the four-rule union, by w mod 3 and selection of 3w (20,000 random 48-bit inputs). Measurement of the dispatcher, not a check. Fails at its new path: it imports union_acceptance_meter from its own folder, which loads rules_union by its pre-migration path. Passed at be73a66 as reviews/side_lane/union_gap_map.py (archive/legacy-checker-run-be73a66.md, exit 0)"
aliases: [R43]
tags: [convergence, outer-residual, tripling-pairs, critical-rank, sufficient-set, conditional-compiler]
---

# The critical-image rank rho(w) = nu(3w) bounds every formal request and composes strict-rank rules

## Statement

Odd-only clock, 1 absorbing, `[1] = 0`; `P(w) = [3w] − [w]`, `ρ(w) = ν(3w)` on `W5 ∪ W9`. By [`critical-tripling-domain-equivalence`](../critical-tripling-domain-equivalence/README.md) `ρ` bijects `W5 ∪ W9` onto the complementary canonical roots `≢ 2 (mod 3)`; `ρ(w) = 3w` on `W9` and on `W5` with `3w` canonical, `(3w−1)/2` when `3w` is selected.

1. **`W9` bound.** Every `W5` request `u` of the fully expanded plan of [`critical-nine-elimination`](../critical-nine-elimination/README.md) for `w ∈ W9` has `8ρ(u) ≤ 27w + 5`. The exceptional ranks at `d = 4, 6, 8` are `(27w+5)/8`, `(81w+23)/32`, `(243w+101)/128`; only `d = 4` can increase rank.
2. **Absorption bound.** Every request of the `W5`-only formal plan `H_s` of [`decreasing-w5-phase-inverse-barrier`](../decreasing-w5-phase-inverse-barrier/README.md) has `ρ(u) ≤ (9s+5)/8`. For a complementary canonical root `p > 4` with pair index `v`, every `H_v` input has `ρ(u) ≤ (3p+4)/4 < p`.
3. **Composition.** If a rule on `A ⊆ W5` supplies finite integer currents with `div J_w = P(w) − Σ c_w(u) P(u)` and `c_w(u) ≠ 0 ⇒ u ∈ W5, ρ(u) < ρ(w)`, universal exact currents on `W5 ∖ A` suffice for Collatz (and conversely). Finite unions under any fixed priority compose in the same rank, whether or not pair indices grow. Formal recursive substitution from one start terminates; unhandled inputs remain leaves with exact signed coefficients.

Neither termination of the formal expansion nor any finite sample proves that every leaf can be supplied. The returning self-request is still a loop; renaming the rank does not repair it.

## Proof

The legacy note "Critical-image rank permits larger pair indices" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written bound and conditional composition theorem.** A larger pair
index need not block induction. The useful rank is the associated canonical
critical root. This does not supply a rule on every root or prove Collatz.

Use killed atoms at1 and odd-only Syracuse S. Write

```
P(w)=[3w]-[w],     rho(w)=nu(3w),
W5={positive w: w=5 mod8},     W9={positive w: w=9 mod16}.
```

R37 proves that rho bijects W5 union W9 onto the complementary canonical
roots not2 modulo3. For W9, rho(w)=3w. For W5 it is3w when3w is
canonical, and(3w-1)/2 when3w is selected. Thus w and rho(w) can order
two inputs differently.

### 1. Rank bound for complete W9 elimination

Every W5 request u in R40's finite `five_plan(w)`, w in W9, satisfies

```
8*rho(u) <= 27w+5 = 9*rho(w)+5.                       (1)
```

To prove this, first use the complete local R40 classification. Every
nonexceptional request u<w has rho(u)<=3u<3w. The exceptional request is
u=4z+1 with3z noncanonical, so3u is selected and rho(u)=6z+1. The exact
three cases are:

| d=v2(9w-1) | u | rho(u) |
|---|---|---|
|4|(9w+3)/4|(27w+5)/8|
|6|(27w+13)/16|(81w+23)/32|
|8|(81w+55)/64|(243w+101)/128|

The d6 and d8 ranks are strictly below3w for every w>=9, even though
their pair indices exceed w. Only d4 increases the critical rank.
All W9 children have smaller index. Apply strong induction to these children;
their bounds(27u+5)/8 are smaller than the parent's bound. Retain all signed
coefficients and cancellations. This proves(1) for the fully expanded plan.

### 2. Rank bound for a formal absorption input

The finite W5-only absorption plan of R41 for any positive odd seed s has
current H_s and signed coefficients a_s(u) satisfying

```
div H_s=[s]-sum a_s(u)P(u),
a_s(u) nonzero  =>  rho(u)<=(9s+5)/8.                 (2)
```

Indeed each directly requested W5 index has critical root at most s,
because the R37 seed decreases at every step. Each W9 request b similarly
comes from a critical root3b<=s. Replacing it by(1) gives rho(u)<=
(27b+5)/8<=(9s+5)/8. Signed cancellation cannot introduce a larger index.
This is an input bound; H_s still requires its missing pair currents.

In particular, if p is a complementary canonical root and v its critical
pair index, then v<=(2p+1)/3 and every absorption input for v obeys

```
rho(u)<=(9v+5)/8<=(3p+4)/4<p                         (3)
```

for p>4. If p2 modulo3, its free inverse descent goes to(2p-1)/3 and
the same strict bound holds. This is why a bridge to a smaller canonical
root can be used even when its new pair index exceeds the old one.

### 3. A common induction and a finite conditional compiler

Let A be any subset of W5 for which a specified rule supplies a finite
integer current J_w and finitely many signed integer requests c_w(u), with

```
div J_w=P(w)-sum c_w(u)P(u),
c_w(u) nonzero  =>  u in W5 and rho(u)<rho(w).         (4)
```

Then universal exact currents on W5 minus A suffice for Collatz. Strong
induction on the positive integer rho(w) supplies each omitted input using
(4), after which R40 and R37 apply. The converse follows from absorption.
Finite unions of rule domains can use any fixed priority: every chosen rule
strictly decreases the same rank, regardless of whether its pair index grows.
This is a sufficient-set theorem with explicit missing premises.

For any one starting pair, recursively substituting(4) terminates: the
branching is finite and the positive integer rank strictly decreases on
each expanded edge. Unhandled inputs remain leaves. Opposite coefficients
are combined exactly; signs or multiplicities must not be dropped. Supplying
all remaining exact leaf currents yields an exact current for the start.
Neither mathematical termination of this formal expansion nor any finite
sample proves that every leaf can be supplied.

`rank_closure.py` implements the bounds and this generic compiler. It checks
every rule's exact divergence and strict rank. Nondecreasing or malformed
rules are rejected, including a tautological self-request. An optional
resource cap rejects the computation rather than turning a leaf into a
certificate. Missing or incorrect actual inputs are rejected on substitution.

The existing R41 E_good rule is compatible with this rank: its child has
critical image p<q=rho(w), (3) handles the child's absorption input, and
nu(w)<=(w-1)/4 gives a strictly smaller rank for the other absorption input.
The returning E row still fails(4). Its self-request cannot be made smaller
by renaming the rank.

### 4. Executable union of the proved rules

`rules_union.py` chooses, in order, R41 E_good, the R45 nonselected base
phase, the accepted R44 returning forward interface, and the R46 inverse
escape. Each selected rule is checked against (4). The accepted domains
are specified in their proof notes, with the R44 rational bound retained
as its sufficient test. Let A be this union. Universal currents on W5
minus A suffice by Section3; every other requested current remains an
explicit premise. A rejected sufficient test is not a nonexistence result.

The finite mixed example w749 expands five rule instances across R41,
R45 and R46 and retains two leaf currents. Both supplied currents and the
final table are stored. At w1029, R44 and R46 compose and their signed
requests cancel completely, giving an exact current with no supplied
inputs. These are finite examples of the compiler. The unresolved P21
self-request is still rejected; its rank has not changed.

Run `python3 experiments/residual_progress/critical_rank/check_rank_closure.py`.
The [receipt](critical_rank_audit.json) checks2048 full W9 reductions,
4096 absorption bounds, the three exceptional affine rows, and all1024
W5 candidates below8192. Of those,195 have an accepted rule and58 expand
using more than one rule. Seven actual substitutions, including an empty
input set, verify final divergence. Missing/bad inputs, incorrect boundaries,
non-W5 children, a self-request and a resource cap are rejected. Input
path discovery is confined to bounded demonstration fixtures; it is absent
from the constructors. These counts do not estimate asymptotic coverage.

### Dependencies and scope

- [R37 critical domain](../critical-tripling-domain-equivalence/README.md).
- [R40 complete W9 elimination](../critical-nine-elimination/README.md).
- [R41 absorption compiler and returning branch](../decreasing-w5-phase-inverse-barrier/README.md).

The common rank allows genuine intermediate increases in the pair parameter.
It does not repair every expanding branch: d4 exceptions in R40 still increase
rho, and the exact returning loop remains a loop. No universal construction,
new annular mass fraction, or novelty claim is supplied.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B11 migration; standard library). The legacy scripts in this folder load their sibling modules by pre-migration folder names, so they no longer run here. This certificate rebuilds the legacy directory layout in a temporary directory from the node folders that now hold those files, runs the unmodified legacy checks there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied receipt unchanged. It writes nothing in the repository. It replays: the legacy checker `check_rank_closure.py` (about 3 s; the counts of section 4 of the note and the stored `w = 749` fixture, compared with `critical_rank_audit.json`) and the side-lane probe `batch_r43_r46_check.py` (about 3 s, receipt reproduced byte for byte). The command in the legacy text names `experiments/residual_progress/critical_rank/`.

## Remarks

- **The union in `rules_union.py`** uses the later rules [`returning-forward-interface`](../returning-forward-interface/README.md) (R44), [`base-inverse-phases-increasing-pairs`](../base-inverse-phases-increasing-pairs/README.md) (R45) and [`variable-depth-inverse-escape-barrier`](../variable-depth-inverse-escape-barrier/README.md) (R46), which depend on the bounds proved here; they are not listed under `depends_on` to keep the dependency graph acyclic. Its enlargements are in [`two-inverse-phases-intermediate-increase`](../two-inverse-phases-intermediate-increase/README.md) (seven families), [`low-block-continuation-prescribed-growth`](../low-block-continuation-prescribed-growth/README.md) (nine) and [`twelve-family-rho-dispatcher`](../twelve-family-rho-dispatcher/README.md) (twelve).
- **The side lane's measurements** of the union (in this folder) report a size-stable accepted share of about 18% of `W5`, with an uncovered remainder concentrated in three of the six classes by `w mod 3` and selection of `3w`. These are finite samples of the dispatcher, not coverage theorems.
- The sharper classification of when a request exceeds the seed is [`rank-excess-absorption-classification`](../rank-excess-absorption-classification/README.md); a different rank that removes the factor `9/8` is [`sigma-rank-removes-absorption-overhead`](../sigma-rank-removes-absorption-overhead/README.md).
- The remaining premise is [`universal-w5-tripling-currents`](../../questions/universal-w5-tripling-currents.md). Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/critical_rank/CRITICAL_IMAGE_RANK.md` (legacy ID R43) at commit `be73a66`, by the B11 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; `check_legacy_replay.py` was added at the migration. The side-lane probes `reviews/side_lane/batch_r43_r46_check.*`, `union_acceptance_meter.*` and `union_gap_map.*`, and the main lane's reproduction receipt `experiments/residual_progress/side_lane_review_3d69784.json`, moved here (`rules_union.py` lives here). Legacy status: "written bounds, sufficient-set theorem and conditional compiler".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `a06ef3c`. The batch's "independent model" proof and code reviews (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents, not a different lane.
