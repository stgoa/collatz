# C.2a bounded attempt: actual-B invariance at two ternary levels

**P6-004 preparatory attempt. Outcome: none.** The proposed actual-B
transport inequality in `experiments/phase6/NEXT_ATTEMPT.md` remains
unproved. This note records an exact necessary system and the failure of
its leading-coefficient relaxation to prove that inequality. It does not
refute the actual-B premise or every finite-state method. No new
non-transfer theorem or Collatz proof is claimed.

## 1. The exact finite-level interface

Use ordinary odd-only Syracuse S(n)=(3n+1)/2^v2(3n+1), absorbed at1.
Let B be the actual positive odd nonabsorbing set. Thus1 is not in B and
1_B(n)=1_B(S(n)). For integer cutoffs X>=0 define

```
B_u^j(X) = #{n in B:n<=X, n=u mod3^j},  0<=u<3^j.
```

At j=0 this is the total odd bad count. A noninteger argument means its
integer floor. The following conditions are necessary, with no hypothesis
that B has a finite power-growth norm:

1. Counts are nonnegative and nondecreasing; increments are0 or1, occur
   only at the specified odd residue, and satisfy the exact residue
   capacity bound. The count at1 is zero. A supplied finite verified
   absorption interval supplies the corresponding additional zero values.
2. The lift identities retain every finer residue:
   `B_u^j(X)=sum_(t=0,1,2) B_(u+t3^j)^(j+1)(X)`.
3. Full inverse invariance gives

```
B_u^j(X) = sum_(a>=1)
 B_((3u+1)2^(-a) mod3^(j+1))^(j+1)((3X+1)/2^a).    (1)
```

Indeed n=(2^a y-1)/3 is an odd positive source, of exact valuation a,
when y is an odd target in the stated class. The residue condition is
exactly n=u mod3^j, and n<=X is exactly2^a y<=3X+1. Each source has one
valuation, so this is a disjoint count. Target1 contributes zero. There
is no raw-versus-absorbed correction for ordinary d=1.

The first two nontrivial source levels are j=1,2, and require target
levels2,3. Thus a system retaining sources modulo3 and9 must carry
auxiliary counts modulo27, or replace them by explicitly justified
inequalities. It is not a closed linear system on just the nine coarse
counts.

## 2. The first two levels, including advanced cutoffs

At source level j=1 the target residue modulo9 has period6 in a:

| Source u mod3 | a=1 | a=2 | a=3 | a=4 | a=5 | a=6 |
|---|---:|---:|---:|---:|---:|---:|
|0|5|7|8|4|2|1|
|1|2|1|5|7|8|4|
|2|8|4|2|1|5|7|

Consequently (1) is exactly the sum over s=1,...,6 and t>=0 of the
indicated target count at `(3X+1)/2^(s+6t)`. At source level j=2, the
complete formula is

```
v_s(u)=(3u+1)2^(-s) mod27,  s=1,...,18,
B_u^2(X)=sum_(s=1,...,18) sum_(t>=0)
                 B_(v_s(u))^3((3X+1)/2^(s+18t)).    (2)
```

Its first two columns are:

| Source u mod9 | a=1 target mod27 | a=2 target mod27 |
|---|---:|---:|
|0|14|7|
|1|2|1|
|2|17|22|
|3|5|16|
|4|20|10|
|5|8|4|
|6|23|25|
|7|11|19|
|8|26|13|

In both levels the a=1 cutoff `(3X+1)/2` is larger than X. It is an
advanced argument and cannot be replaced by a count at X or X/2. The
a=2 cutoff is `(3X+1)/4`; only a>=3 is a one-arrow half descent for a
bad target greater than1. These distinctions prevent silently treating
the full inverse identity as the one-arrow Q operator.

## 3. A complete valuation tail, with a uniform bound

For any fixed integer A>=2, truncate (1) only by introducing the exact
remainder

```
R_(u,j,A)(X)
 = #{n in B:n<=X, n=u mod3^j, 2^(A+1) divides3n+1}.
```

Then (1) is the sum of a=1,...,A plus R. By the Chinese remainder
theorem the remainder's sources lie in one residue class r modulo
`m=3^j*2^(A+1)`. Hence

```
0 <= R_(u,j,A)(X)
  <= max(0, floor((X-r)/m)+1)
  <= X/(3^j*2^(A+1))+1.                            (3)
```

Here r is its positive representative; source1 cannot occur because
A>=2. The tail contains all exact valuations greater than A. It is
neither zero nor an unresolved search. Formula (3), the lift sums, the
capacity conditions and (1) form an honest finite-level necessary
inequality system, still with count functions at shifted cutoffs and
auxiliary ternary lifts.

For a rigorous upper estimate, finer lift counts cannot be replaced by
equal thirds without a new distribution lemma for B. A maximum over
lifts gives an upper relaxation, but loses the coupling one intended to
exploit. Conversely, a lower inverse-tree inequality does not become an
upper transport inequality when multiplied by positive weights.

## 4. Analytical test: a positive-density mode survives the relaxation

Consider the explicitly defined leading-coefficient relaxation obtained
by replacing count functions by `B_u^j(X)=b_u^j X+o(X)`, retaining the
lift identities, the leading terms of (1), and the complete tail bounds
(3). This is a relaxation, not an assertion that actual B has densities.

For any fixed0<lambda<=1, the positive profile

```
b_u^j = lambda/(2*3^j),  for every u and j,         (4)
```

satisfies every one of these constraints. The lift identity is immediate.
In (1), every target branch contributes
`3 b_v^(j+1)/2^a = lambda/(2*3^j*2^a)`. Since
`sum_(a>=1)2^(-a)=1`, their sum equals b_u^j. The leading remainder
after a=A is exactly

```
lambda/(3^j*2^(A+1)),                              (5)
```

which lies within (3). This verifies the profile at both tested ternary
levels and, algebraically, at every fixed level. Setting this tail to zero
would remove genuine mass and can manufacture a false strict decrease.

Fixed finite zero data, including exclusion of1 and any supplied finite
absorption interval, have no leading coefficient. Thus they do not remove
(4) from this particular relaxation. This observation does not mean that
they can be dropped from an exact proof. For example, all odd integers
above a fixed cutoff realize the same leading residue profile but fail
exact invariance at predecessors of the omitted seeds. They are not an
actual-B counterexample.

Let w_u be any strictly positive finite residue weights. Under (4),
their weighted total is `F(X)=c_w X+o(X)`, with c_w>0. The existing
S.1 bound on E is sublinear, so the necessary disjoint decomposition
`B=E disjoint-union G(B)` has the compatible leading profile
`g(X)=c_w X+o(X)`. For0<alpha<1,

```
C_alpha(X)=max_(1<=Y<=X) F(Y)/Y^alpha
           ~ c_w X^(1-alpha).
```

The candidate inequality (P) would therefore require

```
1 <= kappa*2^(alpha-1).                            (6)
```

This fails for kappa<1, including alpha=99/100. Changing positive weights
does not fix (6), because c_w cancels. Therefore no valid implication from
only this stated leading-coefficient system can establish (P).

**Scope:** this is a concrete obstruction to the specified relaxation.
It does not prove that (P) is false for actual B, that every finite
coefficient method is impossible, or that exact affine terms, supplied
absorption and finer constraints cannot exclude this profile. The present
attempt did not find such an exclusion. Its outcome is none, not a new
arbitrary-target barrier relabelled as B-specific progress.

## 5. Transfer control and the next missing ingredient

For supported d>1, all odd multiples of d are nonabsorbing, and d itself
is a fixed point of S_d. They give positive lower density to the actual
B_d. S.1 still gives E_d=o(X). The exact limsup argument in
`NEXT_ATTEMPT.md` therefore proves that the analogue of (P) fails on
actual B_d, without assuming a finite global alpha-norm.

At the residue-system level, the target class in (1) becomes
`(3u+d)2^(-a) mod3^(j+1)`; the upper cutoff is `(3X+d)/2^a` and any
small-source/absorber correction must be retained. For fixed d these
corrections have no linear leading term. Multiplication of ternary
residues by the unit d permutes the homogeneous residue equations.
Thus the positive-density mode is unsurprising in these controls.

The missing discriminating step is an actual-B upper constraint that
uses connection to the absorbing component and rules out (4), with all
advanced terms and valuation tails retained. Merely enforcing finite
ternary invariance, positivity, lift sums and the S.1 exceptional estimate
does not supply it in the tested relaxation.

Krasikov–Lagarias's finite residue difference inequalities yield lower
growth for inverse basins and treat advanced arguments explicitly. Their
direction does not provide this missing upper constraint. The separate
P6-004 audit of the stronger positive-density predecessor claim may
change what upper bound would suffice; it does not prove (P).
See [Krasikov–Lagarias, Sections2–6](https://arxiv.org/html/math/0205002v1).

## 6. Verification scope

Exact modular arithmetic checked the period6 table modulo9, the period18
formula modulo27 and its displayed first two columns. Rational arithmetic
checked that each leading branch sum plus the retained tail equals
`1/(2*3^j)` for j=1,2 and A=2,6,18. The proof above supplies all fixed
levels and all A. No orbit scan, LP feasibility extrapolation, full gate,
or frozen-source edit was performed for this attempt.
