---
id: two-inverse-phases-intermediate-increase
kind: result
title: Two inverse phases cross an intermediate increase and reach strict rank decrease
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; rho(w) = nu(3w). For W5 inputs with 3w nonselected and 3 not dividing w,
  choose k = 4 when w = 2 mod 3 and k = 8 otherwise; set h = v3(kw+1) >= 1, C = (kw+1)/3^h, r = 2^(h+1) C - 1, L
  = v3(2r+1) >= 3, p = 2^L (2r+1)/3^L - 1. The base inverse phase gives a current with boundary [3w] - [r] and
  the 4-mod-9 inverse phase one with boundary [r] - [p], combined before any request. Exactly p < 3w iff h + L
  >= 5 (k = 4) or >= 6 (k = 8), with four explicit below-threshold cases and no small-input exceptions; then p =
  7 mod 8, the critical child is W5 and all final requests decrease rho. The accepted domains (k = 4: h = 1, L
  >= 4 or h = 2, L >= 3; k = 8: h = 1, L >= 5; h = 2, L >= 4; h = 3 or 4, L >= 3) each have r > 3w, p < 3w and a
  complete nonempty CRT family. Inputs with L < 3 and failed tests remain unhandled by this result.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [base-inverse-phases-increasing-pairs, decreasing-w5-phase-inverse-barrier, critical-image-rank-composition, elementary-bridge-quotient-normal-form]
certificates: [check_legacy_replay.py]
evidence:
  - "check_double_inverse.py, double_inverse.py, double_inverse_audit.json, w53_inputs.json, w53_current.csv: the legacy constructor and checker: 153 two-phase inputs, 65 strict plans, 408 exact CRT cases through h = 128 and L = 128, four actual substitutions; the w = 53 input and output are stored. Fails at its new path: double_inverse.py loads ../nonselected_inverse/inverse_phases.py (now ../base-inverse-phases-increasing-pairs/) by its pre-migration folder name; double_inverse/ is put on sys.path by the later legacy continued_rules/, phase_rank/, forward_continuation/ and rule_avoidance/ code. Passed at be73a66 as experiments/residual_progress/double_inverse/check_double_inverse.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
  - "check_expanded_union.py, expanded_union.py, expanded_union_audit.json: the seven-rule strict-rho dispatcher (the four rules of rules_union.py, then nonselected-multiples-inverse-interface, forward-blocks-low-exponent-tests and this rule) and its checker: all 1024 W5 candidates below 8192, 442 accepted (including all 195 accepted before), 258 mixed closures, eight actual substitutions, three full stored outputs including P1821, where all requests cancel. Fails at its new path: expanded_union.py loads ../critical_rank/ and further siblings by their pre-migration folder names. Passed at be73a66 as experiments/residual_progress/double_inverse/check_expanded_union.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
  - "expanded_union_meter.py, expanded_union_meter.json: side-lane measurement (2026-10-17 22:46) of expanded_union.py: random w = 5 (mod 8) at 10 to 64 bits, accepted share about 41 to 44% at every size, with the class w = 2 (mod 3), 3w selected 100% uncovered at 48 bits. It measures the dispatcher; it does not check it, and gives no coverage theorem. Fails at its new path: it imports expanded_union from experiments/residual_progress/double_inverse/ by repository-relative path and fibre_count_check from its own folder (now ../absorbed-fibre-uniform-counts/). Passed at be73a66 as reviews/side_lane/expanded_union_meter.py (archive/legacy-checker-run-be73a66.md, exit 0)"
aliases: [R50]
tags: [convergence, outer-residual, tripling-pairs, critical-rank, inverse-rays, dispatcher]
---

# Two inverse phases cross an intermediate increase and reach strict rank decrease

## Statement

Odd-only clock, 1 absorbing; `ρ(w) = ν(3w)`; `H_s` the formal absorption plan with requests of rank at most `(9s+5)/8`. Domain: `w ∈ W5`, `3w` nonselected, `3 ∤ w`.

1. **Two phases.** Take `k = 4` if `w ≡ 2 (mod 3)`, `k = 8` otherwise; `h = v3(kw+1) ≥ 1`, `C = (kw+1)/3^h`, `r = 2^(h+1)C − 1`, `L = v3(2r+1)`, and impose `L ≥ 3`, `p = 2^L(2r+1)/3^L − 1`. The base phase of [`base-inverse-phases-increasing-pairs`](../base-inverse-phases-increasing-pairs/README.md) gives a current with boundary `[3w] − [r]`, the phase of [`decreasing-w5-phase-inverse-barrier`](../decreasing-w5-phase-inverse-barrier/README.md) one with boundary `[r] − [p]`; the combined bridge precedes every missing-current request.
2. **Exact test.** `p < 3w` iff `h + L ≥ 5` (`k = 4`) or `≥ 6` (`k = 8`); four explicit below-threshold cases prove necessity without small-input exceptions. Then `p ≡ 7 (mod 8)`, its critical child is `W5`, and all final requests decrease `ρ`.
3. **Domains.** `k = 4`: `h = 1, L ≥ 4` or `h = 2, L ≥ 3`; `k = 8`: `h = 1, L ≥ 5`, `h = 2, L ≥ 4`, or `h ∈ {3, 4}, L ≥ 3`. Every one has `r > 3w` but `p < 3w` and a complete nonempty CRT family. Example: `w = 53` compares 159 with 283 and then 111 through inverse phases; this order is not the forward orbit.
4. **Seven-family dispatcher.** `expanded_union.py` keeps the earlier four-rule priority, then tries [`nonselected-multiples-inverse-interface`](../nonselected-multiples-inverse-interface/README.md), [`forward-blocks-low-exponent-tests`](../forward-blocks-low-exponent-tests/README.md) and this rule, each checked for exact divergence and strict `ρ`. Universal currents on the complement of its domain suffice; the complement remains unresolved.

Inputs with `L < 3` and failed tests remain unhandled by this result.

## Proof

The legacy note "Two inverse phases permit an intermediate increase" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written exact interface and complete strict-rank classification
within the stated two-phase domain.** A first inverse phase may increase
its canonical state; a second can bring it below the original rank.
The construction retains all missing pair inputs and does not prove Collatz.

Use killed odd atoms [1]=0 and P(w)=[3w]-[w]. The definitions of canonical,
selected, nu and T are those of R25. Let rho(w)=nu(3w), and let H_s be the
R43 formal absorption plan, with every missing rank at most(9s+5)/8.

### 1. Exact parameters and current

Take w in W5 with3w nonselected and3 not dividing w. Choose k=4 when
w2 modulo3 and k=8 when w1 modulo3. Put

```
h=v3(kw+1)>=1,   C=(kw+1)/3^h,
b=2kw+1,        r=2^(h+1)C-1,
L=v3(2r+1).
```

R45 gives h ordinary valuation1 arrows from r to b and a quotient bridge
from b to q=3w. Its negative current A has divergence[q]-[r]. Impose
**L>=3**, and put

```
p=2^L(2r+1)/3^L-1.
```

Since r4 modulo9, R41 supplies the exact ordinary word1^(L-1),2 from
p to r. Its negative current B has divergence[r]-[p]. Consequently
A+B has divergence[q]-[p]. Every state of these prescribed quotient paths
is canonical, and T^(h+L+1)(p)=q. The last quotient bridge need not count
as one ordinary arrow. No future beyond these displayed words is used.

The maximal choice of L makes p0 or1 modulo3; moreover v2(p+1)=L.
Thus p is complementary7 modulo8 and its critical pair index v is in W5,
with rho(v)=p. This avoids an expanding W9 replacement at the final child.

### 2. Complete endpoint descent test

Throughout this domain L>=3,

```
p<3w  iff  h+L>=5 for k=4,
p<3w  iff  h+L>=6 for k=8.                          (1)
```

Indeed

```
k*3^L*(p-3w)
 = (k*2^(h+L+2)-3^(h+L+1))*C +(3-k)*3^L-k*2^L.     (2)
```

The constant term is negative. The coefficient of C is negative exactly
at the thresholds in(1), proving sufficiency. For necessity only the
following cases exist below threshold, since h>=1,L>=3:

| k,h,L | right side of(2) |
|---|---|
|4,1,3|13C-59|
|8,1,3|269C-199|
|8,1,4|295C-533|
|8,2,3|295C-199|

In the first row L=3 forces8C=1 modulo27, so C>=17. In the third,
L=4 forces8C=1 modulo81, so C>=71. In the other two rows C>=1 already
makes the expression positive. Thus there are no small-C exceptions,
and equality p=3w never occurs. This proves the exact test, including
all positive integer endpoints in the specified domain.

### 3. Strict-rank pair construction and new complete domains

Let z=nu(w)<w/4. Apply one R37 critical step to p; it gives current K
with divergence[p]-[v]-P(v). The full explicit current

```
J=A+B+K-N_w+H_v-H_z
```

has divergence P(w) minus its signed W5 requests. The leading request
v has rank p<q. By R43, every H_v request has rank at most
(9v+5)/8<=(3p+4)/4<p; every H_z request has rank below q=3w.
Thus all requests strictly decrease rho. Their indices need not decrease.
Every coefficient, including negative lower-side requests, is retained.

R45's first stage alone decreases exactly at h>=3 for k4 and h>=5 for k8.
Consequently the complete **additional** domains supplied here are:

| first branch | failed first-phase h | sufficient and necessary L in L>=3 |
|---|---|---|
|k4|1|L>=4|
|k4|2|L>=3|
|k8|1|L>=5|
|k8|2|L>=4|
|k8|3 or4|L>=3|

Every listed domain has r>q but p<q. Example w53 has q159,r283,p111;
example w37 has q111,r175,p103. These are inverse comparisons in the
quotient graph, not an assertion that the forward orbit follows the
same numerical order. The signed ordinary currents certify the comparisons.

The rule also applies when the first phase already decreases, but those
cases add no new R45 domain. Inputs with L<3 and failed rows in(1) remain
unresolved by this constructor. Other inverse words remain available.
Universal currents on the complement of this domain and any other
strict-rho rule domains suffice by R43. Their supply remains open.

### 4. Every pair of phase lengths has a full congruence family

For k4 or8,h>=1,L>=3 define C by the coprime congruences

```
C=(1+13k)*3^(-h) mod32k,
C=(1+3^L)*2^(-h-2) mod3^(L+1).                       (3)
```

Every positive member gives w=(3^h C-1)/k with w13 modulo32. Hence
q=3w has exact binary exponent3 and complementary phase, so3w is
nonselected. The second congruence makes C a ternary unit and forces
v3(2^(h+2)C-1)=L exactly. The first forces integrality and the W5 residue.
Thus(3) describes a nonempty full infinite family with exactly these h,L.
Every row of the additional-domain table is therefore populated, with
unbounded second-phase length available. These are complete arithmetic
families, not extrapolations from finite samples.

### 5. Implementation, evidence and limits

[double_inverse.py](double_inverse.py) constructs the exact bridges and
strict-rank pair plans. `parameters` retains accepted and failed endpoint
cases with L>=3; `recognized` is the accepted-domain predicate. No unknown
orbit search occurs. `compile_plan` substitutes only supplied exact inputs.

Run `python3 experiments/residual_progress/double_inverse/check_double_inverse.py`.
The deterministic receipt covers complete bounded parameter decisions,
exact ordinary/quotient words, long CRT families, strict-rank boundaries,
and capped actual input substitutions. The finite examples audit the
implementation; equations(1)–(3) prove the full classification.

Dependencies: [R45 first phase](../base-inverse-phases-increasing-pairs/README.md),
[R41 second phase](../decreasing-w5-phase-inverse-barrier/README.md),
[R43 common rank](../critical-image-rank-composition/README.md).
Permanent inverse-only failures in [R49](../inverse-only-exclusions-short-forward/README.md)
will still require forward or other comparisons. This two-phase rule is
partial and does not bypass those failures or establish a novelty claim.

### 6. Integration with the earlier rules

`expanded_union.py` preserves the earlier four-rule priority, then tries
R47's multiples-of-three rule, R48's accepted complete forward block,
and this two-inverse-phase rule. Each accepted current passes the same
R43 divergence and strict-rho checks. R49's forward witness cylinders
are contained in R48, so they are not counted as another independent rule.
Universal currents on the complement of this seven-rule domain suffice;
the complement remains unresolved.

Run `python3 experiments/residual_progress/double_inverse/check_expanded_union.py`.
Its [receipt](expanded_union_audit.json) checks all1024 W5 candidates below8192:
442 have an accepted rule, including all195 accepted before this batch;
258 expansions use multiple rule types. Eight actual substitutions retain
all signed coefficients. Three complete outputs and their inputs are stored,
including P1821, where all remaining requests cancel. These finite counts
and examples are not an asymptotic coverage or convergence theorem.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B11 migration; standard library). The legacy scripts in this folder load their sibling modules by pre-migration folder names, so they no longer run here. This certificate rebuilds the legacy directory layout in a temporary directory from the node folders that now hold those files, runs the unmodified legacy checks there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied receipt unchanged. It writes nothing in the repository. It replays: the legacy checkers `check_double_inverse.py` (about 6 s; the counts of section 5 and the `w = 53` fixture, against `double_inverse_audit.json`) and `check_expanded_union.py` (about 3 s; the seven-rule counts and stored outputs, against `expanded_union_audit.json`). The commands in the legacy text name `experiments/residual_progress/double_inverse/`.

## Remarks

- **Measurement (side lane, finite).** The meter in this folder reports the seven-rule union accepting a size-stable 41–44% of sampled `W5`, with `w ≡ 2 (mod 3)`, `3w` selected entirely uncovered at 48 bits; [`selected-critical-five-forward-tables`](../selected-critical-five-forward-tables/README.md) later addresses that class. These are samples of the dispatcher, not coverage theorems.
- The dispatcher is extended to nine families in [`low-block-continuation-prescribed-growth`](../low-block-continuation-prescribed-growth/README.md) and twelve in [`twelve-family-rho-dispatcher`](../twelve-family-rho-dispatcher/README.md). Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/double_inverse/DOUBLE_INVERSE_PHASES.md` (legacy ID R50) at commit `be73a66`, by the B11 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; `check_legacy_replay.py` was added at the migration. The side-lane probe `reviews/side_lane/expanded_union_meter.*` moved here (`expanded_union.py` lives here). Legacy status: "written complete endpoint test within the second-depth L>=3 domain and a strict-rank constructor".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `bcde58e`. The batch's "independent model" proof and code reviews (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents, not a different lane.
