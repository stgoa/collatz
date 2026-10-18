# Two inverse phases permit an intermediate increase

**Status: written exact interface and complete strict-rank classification
within the stated two-phase domain.** A first inverse phase may increase
its canonical state; a second can bring it below the original rank.
The construction retains all missing pair inputs and does not prove Collatz.

Use killed odd atoms [1]=0 and P(w)=[3w]-[w]. The definitions of canonical,
selected, nu and T are those of R25. Let rho(w)=nu(3w), and let H_s be the
R43 formal absorption plan, with every missing rank at most(9s+5)/8.

## 1. Exact parameters and current

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

## 2. Complete endpoint descent test

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

## 3. Strict-rank pair construction and new complete domains

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

## 4. Every pair of phase lengths has a full congruence family

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

## 5. Implementation, evidence and limits

[double_inverse.py](double_inverse.py) constructs the exact bridges and
strict-rank pair plans. `parameters` retains accepted and failed endpoint
cases with L>=3; `recognized` is the accepted-domain predicate. No unknown
orbit search occurs. `compile_plan` substitutes only supplied exact inputs.

Run `python3 experiments/residual_progress/double_inverse/check_double_inverse.py`.
The deterministic receipt covers complete bounded parameter decisions,
exact ordinary/quotient words, long CRT families, strict-rank boundaries,
and capped actual input substitutions. The finite examples audit the
implementation; equations(1)–(3) prove the full classification.

Dependencies: [R45 first phase](../nonselected_inverse/NONSELECTED_INVERSE_PHASES.md),
[R41 second phase](../critical_inverse/CRITICAL_INVERSE.md),
[R43 common rank](../critical_rank/CRITICAL_IMAGE_RANK.md).
Permanent inverse-only failures in [R49](../inverse_scope/INVERSE_SCOPE.md)
will still require forward or other comparisons. This two-phase rule is
partial and does not bypass those failures or establish a novelty claim.

## 6. Integration with the earlier rules

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
