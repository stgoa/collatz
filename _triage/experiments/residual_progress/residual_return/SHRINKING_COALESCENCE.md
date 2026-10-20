# A complete halving family for the outer residual

2026-10-17. **Written conditional construction, exact source profile, and finite
checks.** The smaller absorption current is an input. Universal residual closure
and Collatz remain open. No novelty claim is made. The clock is odd-only
Syracuse, with absorption at1; algebraically write S(1)=1 and omit its current row.

## 1. A halving identity with unbounded arithmetic prefix length

Every positive odd x=3 modulo4 has a unique representation

```
x=2^a t-1,       a=v_2(x+1)>=2,       t odd.
```

Call x **selected** when `t=3^a modulo4`. Then, with `q=(x-1)/2<x/2`,

```
S^a(x)=S^a(q).                                            (1)
```

This is an exact statement about all parameters a and t. It does not assume
that either orbit terminates. Its finite current version is

```
D_x = sum_(j=0)^(a-1) delta_(S^j x)
      -sum_(j=0)^(a-1) delta_(S^j q),
div D_x = delta_x-delta_q.                                (2)
```

The measure delta_1 and current rows at1 are killed. Repeated rows in these
sums have their full multiplicities. Thus (2) remains valid if a prefix
already reaches1, including x=3,q=1.

**Proof.** The first a-1 valuations of x are1, with

```
S^j(x)=3^j 2^(a-j)t-1,       0<=j<=a-1.
```

The first a-2 valuations of q are1, with

```
S^j(q)=3^j 2^(a-1-j)t-1,     0<=j<=a-2.
```

Put z=3^(a-1)t. The selection condition gives z=3 modulo4, so at the
next q state the valuation is exactly2, and

```
S^(a-1)(q)=(z-1)/2,
S^(a-1)(x)=2z-1=4 S^(a-1)(q)+1.
```

The identity S(4u+1)=S(u) for positive odd u now proves (1).
Telescoping proves (2). No final exact valuation is assumed: its value may
grow with the parameters. In particular, these are complete binary residue
classes, not valuation cylinders with an omitted extra bit. The classes are

```
a even: x=2^a-1       modulo 2^(a+2),
a odd:  x=3*2^a-1     modulo 2^(a+2).                    (3)
```

They are disjoint because each fixes v_2(x+1)=a.

For x>3, neither prefix reaches1 before step a. The x prefix increases
through step a-1. The q prefix increases through step a-2, and its next
state `(3^(a-1)t-1)/2` exceeds1; equality occurs only for a=2,t=1,x=3.
Consequently selected x>3 and q have equal odd-only hitting times when
finite (and either both terminate or neither does).

This is a strictly decreasing recurrence for the selected seed: substitute
the smaller seed q, and retain the explicit finite bridge D_x. It is not a
recurrence covering every odd seed. The smaller seed need not itself belong
to the selected family; absorption through the stated lower cutoff is supplied.

## 2. Apply the rule to the exact residual, retaining all coefficients

Fix `8|N`, N>=8. The [retained-graph construction](../complement/RETAINED_GRAPH_EXTENSION.md)
leaves the following nonnegative R_N:

```
weight1: x=3 mod12,               N<x<3N/2;
weight1: x=7 mod12,               9N/8<x<3N/2;
weight2: x=7 or19 mod36,          N<x<9N/8.
```

All roots are3 modulo4. Let G_N be R_N restricted to the selected classes
(3), and let `R'_N=R_N-G_N`. Assume a finite exact current H for U_N is
supplied. Every selected root has `q=(x-1)/2<3N/4<N`. Let

```
Q_N = sum_(x in supp G_N) G_N(x) delta_((x-1)/2),
B_N = sum_(x in supp G_N) G_N(x) D_x.
```

These are new local symbols, unrelated to annular scale combinations.
Then `div B_N=G_N-Q_N`. Extract from the nonzero-row graph of H an exact
nonnegative integral current H_Q for Q_N. Consequently

```
T_signed=B_N+H_Q,            div T_signed=G_N.             (4)
R_N=div T_signed+R'_N.                                    (5)
```

In fact, if H_Q is extracted as the sum of the actual absorbing paths,
T_signed is already nonnegative: for each q, remove its first a arrows
and insert the x prefix of the same length. Their common suffix remains.
For these residual roots x>N>=8, both prefixes have exactly a nonabsorbed
origins, so the total current mass is unchanged by this replacement.

An exact nonnegative integral current T for G_N can also be extracted from
the nonzero-row graph of T_signed. To justify this without a global cycle
hypothesis: summing divergence in a finite weak component not containing1
gives zero, so it cannot contain positive G_N mass. A finite functional
component containing1 has1 as its unique terminal vertex, and therefore its
vertices have directed paths to1. This reasoning allows any signs in H or
T_signed. It requires no absorption of any new larger seed.

Every q prefix in (2) is already present in H's graph, since H certifies q.
The only additional arrows needed are the first a arrows of each x prefix.
Neither (4) nor the graph extraction searches for an unknown outer future.
The code checks that the extracted current uses only these supplied and
explicit prefix rows. Currents at coincident rows are added; source capacity
is accounted for by restricting G_N coefficientwise to R_N. A coefficient2
root contributes twice throughout, including to Q_N and D_x.

If the previous packet identity is `Pi_N=div J_0-R_N`, the upgraded one is

```
Pi_N=div(J_0-T)-R'_N.                                    (6)
```

The minus sign on T is required. This is a conditional partial extension;
G_N is certified entirely, while R'_N is returned with all its positive mass.

For example, at N=72 the root79 has coefficient2. Its two prefixes are

```
79 ->119 ->179 ->269 ->101,
39 -> 59 -> 89 -> 67 ->101.
```

Twice their difference has divergence `2 delta_79-2 delta_39`.
The full current for39 is available below N. The construction retains all
two units at79 and does not assume absorption through269.

## 3. Exact logarithmic floor formula and the remaining profile

Write C(L,H;r,m) for the number of integers strictly between rational L,H
that equal r modulo m. Thus

```
C(L,H;r,m)=ceil((H-r)/m)-floor((L-r)/m)-1.
```

Set `A=floor(log2(3N/2))`. For each `2<=a<=A`, let b_a be the residue in
(3) and p_a=2^(a+2). For an R_N residue r modulo m, m=12 or36, put

```
k_a(r,m)=(r-b_a) p_a^(-1) modulo (m/4),
r_a(r,m)=b_a+p_a k_a(r,m) modulo p_a(m/4),
ell_a(m)=p_a(m/4).
```

The inverse exists because m/4 is odd. Both residues are3 modulo4, so
this is the exact Chinese-remainder intersection. The removed mass is

```
|G_N| = sum_(a=2)^A [
 C(N,3N/2; r_a(3,12),ell_a(12))
+C(9N/8,3N/2; r_a(7,12),ell_a(12))
+2 C(N,9N/8; r_a(7,36),ell_a(36))
+2 C(N,9N/8; r_a(19,36),ell_a(36)) ].                  (7)
```

No a>A can occur, because x<3N/2 and x odd imply `2^a<=x+1<=3N/2`.
The four interval widths, with weights and odd moduli, sum to `25N/72`.
Since `sum_(a=2)^A 2^(-a-2)=1/8-2^(-A-2)`, replacing each progression
count by its interval length divided by its period gives

```
|G_N| = 25N/576 + epsilon_N,
|epsilon_N| <= 6(A-1)+25/216.                            (8)
```

Indeed each progression error has magnitude at most1, and its four weights
sum to6. The omitted tail is `25N/(72*2^(A+2))<25/216`, because
`3N/2<2^(A+1)`. Combining (8) with R17's exact formula and its bound
`-19/9<=|R_N|-25N/288<=5/4` yields, in particular,

```
|R'_N|=25N/576+O(log N),
abs(|R'_N|-25N/576) <= 6A.                               (9)
```

The code evaluates (7) using exact integer/Fraction arithmetic in O(log N)
terms and also compares it against every explicit weighted root in its finite
audit range. Equations (7)-(9) are written proofs for every allowed N, not
extrapolations from a numerical proportion.

Relative to the original outer mass N/4, the combined retained-graph and
halving construction certifies `119/144` asymptotically, leaving `25/144`.
This fraction is a one-pass statement. The remaining R'_N is a different
arithmetic profile, so repeatedly multiplying its mass by1/2 is unjustified.

## 4. Exact complementary branch and the next obligation

The entire remaining family has

```
x=2^a t-1,    t=-3^a modulo4,
q=(x-1)/2,    d=v_2(3^(a-1)t-1)>=2,
w=(3^(a-1)t-1)/2^d odd.
```

The explicit first-run exits are

```
S^(a-1)(q)=w,
S^a(x)=(3^a t-1)/2=3*2^(d-1)w+1.                       (10)
```

For a>=3, q itself satisfies the selected condition with parameter a-1.
That certifies q from a still smaller seed but does not connect x to q.
The relation in (10) is not the common-successor relation `4w+1` used in
Section1, and its larger term need not be below x or N. The simple attempt
to apply (1) to both binary classes is false: x=27 at N=24 is an actual
weight1 residual root, and

```
S^2(27)=31,        S^2(13)=1.
```

Thus the next construction must handle precisely the complementary branches
(10), or add a separate decreasing parameter that remains valid after them.
Knowing their smaller partners are already certified does not provide that
missing connection. This is the outstanding closure obligation, rather than
an appeal to iterate the observed half-mass reduction.

## 5. Arbitrarily long excursions already occur on a required ray

For every even a>=8, choose

```
x=2^a-1,       N=12*2^(a-4),       q=2^(a-1)-1.
```

Then N is a required five-ray cutoff, x=3 modulo12, `N<x<3N/2`, and
R_N(x)=G_N(x)=1. Its first a-1 states after the start are strictly greater
than x, and its last state before coalescence is

```
S^(a-1)(x)=2*3^(a-1)-1.
```

This height divided by N grows without bound. In particular the first return
to the absorbed interval cannot occur in fewer than a steps. The construction
still finishes its arithmetic bridge after exactly a arrows on each side,
because it compares with the supplied smaller seed q. It does not promise
that the common state itself is below N.

The old packed annular roots `x=9183+768j` satisfy x=223 modulo256 and
therefore belong to the a=5 selected class. The halving identity removes
the extra annular copy-index and band restrictions when the root lies in
R_N. Its applicability also covers both coefficient1 and coefficient2 roots.
This is why the present step is broader than adding another isolated block.

## 6. Reproduction and limits

Run from the repository root:

```
python3 experiments/residual_progress/residual_return/check_halving_return.py
```

The default runner is read-only and compares its exact output to
`halving_return_audit.json` and the stored coefficient2 current. Use
`--write-receipt` only to regenerate those files. Finite demonstration input
currents are discovered with a1000-step cap per supplied seed; the theorem
takes those currents as inputs and makes no universal search-termination claim.

`halving_return.py` provides the complete selected-class test, finite bridge,
exact logarithmic count, and source-capacity-preserving current conversion.
The receipt records the exact test ranges, current hashes, remaining mass,
large-parameter arithmetic cases, and the complementary-branch counterexample.
The written proof is not formal verification or human peer review.
