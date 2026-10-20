---
id: decreasing-inverse-ancestry
kind: result
title: Complete decreasing canonical inverse chains extend the run-bridge cutoff test to lower partners of unbounded-height returns
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; B, nu and the canonical predecessors are those of
  elementary-bridge-quotient-normal-form, and f is the return of complementary-run-bridges (R26). (Inverse
  chain) For canonical q, with h = v3(q+1) and eta(q) = 2^h (q+1)/3^h - 1, the states q_j = 2^j (q+1)/3^j - 1,
  0 <= j <= h, form the unique maximal strictly decreasing canonical inverse path, with S(q_j) = q_(j-1) by
  valuation-1 arrows; its nonpositive current has divergence delta_q - delta_eta(q). The canonical valuation-1
  components are finite paths with a unique minimum p, 3 not dividing p+1. This local minimum is not a global
  ancestor minimum: q = 91 + 419904j has the smaller ancestor 27 + 131072j although eta(q) = q.
  (Extension) For 8 | N and conditional on a supplied exact U_N current (absorption below N is an input), every
  complementary root x with eta(nu(f(x))) < N is certified with its full source weight. Even-d returns have
  h = 0 and are unchanged; for odd d = 2b+1 and elementary stratum k, h = min(b, v3(2k+1)) when the two
  differ, with an exact formula in the resonant case. (Families) Every x = 19199 mod 65536 has
  S^9(x) = S^2(p), p = (2187x - 117)/4096; for every h >= 2 an explicit complete binary cylinder modulo 2^K
  has p = lambda x + beta < 2x/3 while the old return q exceeds x with slope at least (3/2)^h 4/9, merger
  S^(a+b)(x) = S^(h+1)(p), and, for each fixed h, weighted R_N source count within 6 of 25N/(72 2^K); no
  uniform density for their union is asserted. (Count) The extended profile has an exact finite count with at
  most O(log^5 N) arithmetic operations; no leading coefficient is claimed. Recognized targets lie in the
  supplied-history saturation of supplied-path-saturation-core. Universal coverage, Collatz convergence and
  novelty are not claimed.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [elementary-bridge-quotient-normal-form, complementary-run-bridges, supplied-path-saturation-core]
certificates: [check_inverse_ancestry_recompute.py, check_legacy_replay.py]
evidence:
  - "check_inverse_ancestry.py, inverse_ancestry.py, inverse_ancestry_audit.json, root84735_current.csv, large_h2_weight2_current.csv: the legacy constructor (inverse chain, canonical components, extended bridge, exact cell count, large-return families, ray witnesses, full-profile and single-root conversions) and checker (4096 canonical targets below 16384, inverse depths 1 to 128, 2048 return branches, 32 members of the small cylinder, 12 required-ray witnesses for h = 2 to 7, eight exact profile counts through N = 65536, three full-profile conversions and two stored new-root currents with a 5000-step input cap, 33 counterfamily cases). Fails at its new path: inverse_ancestry.py loads ../complementary_bridge/run_bridge.py by its pre-migration path (now ../complementary-run-bridges/, which itself no longer runs). Passed at be73a66 as experiments/residual_progress/inverse_ancestry/check_inverse_ancestry.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-17
    link: ../mixed-shrinking-pair-rules/batch_r33_r36_check.py
    scope: "Finite only (side-lane feed entry 2026-10-17 21:06, VERIFIED, main 1603bf3; the R34 part): eta(q) = 2^h(q+1)/3^h - 1 with h = v3(q+1) satisfies S^h(eta(q)) = q for every odd q < 20000; on the cylinder x = 19199 (mod 65536) the numerators of q and p are exact, and S^9(x) = S^2(p); root 84735 gives q = 67865 > N and p = 45243 < N at N = 65536. The written arguments were not re-derived; the status stays written"
aliases: [R34]
tags: [convergence, outer-residual, complementary-family, inverse-ancestry, normal-form, conditional, constructive]
---

# Complete decreasing canonical inverse chains extend the run-bridge cutoff test to lower partners of unbounded-height returns

## Statement

Odd-only clock `S`, absorbing at 1 (algebraically `S(1) = 1`; current rows and measures at 1 are killed). `B`, the normal form `ν` and the canonical predecessors are those of [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md) (R25); `f` is the complementary return of [`complementary-run-bridges`](../complementary-run-bridges/README.md) (R26).

1. **Inverse chain.** For canonical `q` put `h = v₃(q+1)`, `η(q) = 2^h·(q+1)/3^h − 1`. The only canonical predecessor smaller than `q` is `L(q) = (2q−1)/3`, present exactly when `q ≡ 2 (mod 3)`, with `S(L(q)) = q`. Hence `q_j = 2^j·(q+1)/3^j − 1` (`0 ≤ j ≤ h`) is the unique maximal strictly decreasing canonical inverse path, `η` is idempotent, and `J_q = −Σ_(j=1..h) δ_(q_j)` has divergence `δ_q − δ_(η(q))`. The canonical valuation-1 components are finite paths `p_j = 3^j·(p+1)/2^j − 1`, `0 ≤ j < v₂(p+1)`, with unique minimum `p`, `3 ∤ p+1`. This is not a global ancestor minimum: `q = 91 + 419904j` has the ancestor `27 + 131072j < q` after eight canonical arrows although `η(q) = q`.
2. **Extension (conditional: a finite exact `U_N` current is supplied, `8 | N`).** For a complementary root `x` with `q = ν(f(x))` and `p = η(q) < N`, the bridge `D_x + J_q` and the supplied path of `p` give a nonnegative integral current certifying `x` with its full `R_N` weight. Since `η(q) ≤ q` the test contains R26's. Even `d` gives `h = 0` (no improvement). For odd `d = 2b+1` and elementary stratum `k`, `h = v₃(V) − 1` with `V` of (7), and `h = min(b, v₃(2k+1))` when `b ≠ v₃(2k+1)`.
3. **Small cylinder.** For `x ≡ 19199 (mod 65536)`: `q = (6561x+3745)/8192`, `p = (2187x−117)/4096`, `S^9(x) = S^2(p)`; every actual `R_N` source there has `p < N`. At `N = 65536`, root 84735 has `q = 67865 > N`, `p = 45243 < N`.
4. **Unbounded-return families.** For every `h ≥ 2`, `k = (3^h−1)/2`, `b = h+1`, `d = 2h+3` and the unique `a` with `4/9 ≤ λ = 3^a/2^(a+h+2+3^h) < 2/3`, the complete binary cylinder (14) modulo `2^K`, `K = a+d+2k+3`, has `p = λx + β` with `−5/9 < β < −7/192`, old return `q = Λx + Λ − 1/3 + c/4^k`, `Λ = (3/2)^h λ ≥ 1`, `c = 1/3 − 3^(h+1)/2^d > 0`, so `q > x`, and merger `S^(a+b)(x) = S^(h+1)(p)`. For each fixed `h` the weighted `R_N` mass in the cylinder is within 6 of `25N/(72·2^K)`; actual sources of both weights occur on infinitely many required cutoffs. No uniform density for the union over `h` is asserted.
5. **Count.** The whole extended profile has an exact finite count with at most `O(log⁵ N)` arithmetic operations (bit complexity not included); at `N = 65536` it certifies 1563 weighted units versus 1562 for R26. No leading coefficient is claimed.

Recognized targets lie in the supplied-history saturation of [`supplied-path-saturation-core`](../supplied-path-saturation-core/README.md); the originating seeds need not. Universal coverage, Collatz convergence and novelty are not claimed.

## Proof

The legacy note "Complete decreasing inverse ancestry and new lower-seed bridges" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

2026-10-17. **Written arithmetic proofs and finite certificates.** This is a
partial extension of the R26 complementary-return rule. It supplies complete
families whose old canonical returns have unbounded height ratios, and an
exact finite count for the extended rule. It leaves every even-d return
unchanged. Universal coverage, Collatz convergence, and novelty are not claimed.

Use the odd-only Syracuse map S, absorbing at1; current divergence is killed
at1. The [R25 canonical set B and normal form nu](../elementary-bridge-quotient-normal-form/README.md)
and [R26 return f](../complementary-run-bridges/README.md) are used without
changing their domains. Lower absorption currents are supplied. The independent
feed, unchanged at the parent's reviewed pin, is not a premise of this note.

### 1. Every strictly decreasing canonical inverse chain

For canonical q define

```
h=v_3(q+1),       eta(q)=2^h*(q+1)/3^h-1.                 (1)
```

**Complete inverse-chain theorem.** The only canonical T-predecessor smaller
than q exists exactly when q=2 modulo3, and is

```
L(q)=(2q-1)/3.
```

It is an actual valuation1 predecessor, S(L(q))=q. Consequently (1) is the
unique endpoint of the maximal strictly decreasing canonical inverse path.
Every intermediate state is canonical. Its explicit states are

```
q_j=2^j*(q+1)/3^j-1,       0<=j<=h,
q_0=q, q_h=eta(q),          S(q_j)=q_(j-1), j>=1.        (2)
```

The terminal p=eta(q) satisfies `3 does not divide p+1`, and eta is
idempotent. If p>1, all its canonical predecessors are strictly larger.
At p=1 the self-loop is the sole equality exception.

**Proof.** R25's complete inverse list has two rays and, only at q=2 mod3,
the point L(q). The ray minima are

```
q=0 mod3: (8q+3)/3,   (16q+3)/3;
q=1 mod3: (4q-1)/3,   (32q+19)/3;
q=2 mod3: (64q+19)/3, (128q+83)/3.
```

All exceed q, except the first minimum at q=1. Every further ray term is
larger. The point L(q) is canonical by the same inverse classification,
and `3L(q)+1=2q` proves its exact valuation. Its positive odd value is
less than q. Formula (2) follows by iteration, and
`v_3(q_j+1)=h-j` proves precisely when the chain ends. No trajectory search
or assumption of absorption appears in this proof.

The finite nonpositive current

```
J_q=-sum_(j=1)^h delta_(q_j),
div J_q=delta_q-delta_eta(q)                            (3)
```

keeps the inverse orientation. There is no positive current cost for this
particular bridge; this says nothing about the cost after other currents
are added or cancelled.

#### The whole finite component, not just one chain

Consider only valuation1 arrows whose sources and targets are canonical.
Their undirected components are finite paths. Every component has a unique
minimum p in B with `3 not dividing p+1`. Put a=v_2(p+1). The complete path is

```
p_j=3^j*(p+1)/2^j-1,       0<=j<=a-1.                 (4)
```

Its a states strictly increase, except the singleton case a=1. The last
state is1 modulo8, hence has no outgoing valuation1 arrow; every previous
state is complementary3 modulo4. In the a>=2 case the defining complementary
congruence gives the last state1 modulo8. Formula (2) recovers p at every
state, since `v_3(p_j+1)=j`. This proves completeness in both directions.

This local minimum is not a minimum among arbitrary canonical ancestors.
For every j>=0 put

```
u=27+131072j,       q=91+419904j.
```

The repeated-word proof gives S^8(u)=q with all intermediate states canonical,
and q>u. Yet q=1 modulo3, so eta(q)=q. Already at j=0 the path is
`27,41,31,47,71,107,161,121,91`. Its inverse must initially increase.
Thus stopping at eta cannot replace complete inverse search. Also eta T is
not constant on these path components: eta(T(7))=7 whereas eta(T(17))=1,
although eta(7)=eta(17)=7. A later forward move must retain the exit position;
there is no one-step semiconjugacy analogous to R25's nu.

### 2. A complete arithmetic extension of the R26 cutoff test

Throughout the annular profile and counting interfaces, assume `8|N` and
N>=8. All targets are odd, so p<N and p<=N are equivalent here. For a
single-seed bridge with a general supplied U_N, the appropriate condition
is p<=N.

For any complementary root x, let q=nu(f(x)) be R26's canonical return and
p=eta(q). Its explicit R26 bridge D_x has divergence delta_x-delta_q.
Adding (3) gives

```
div(D_x+J_q)=delta_x-delta_p.                           (5)
```

If p<N and an exact U_N current is supplied, extract the actual absorption
path of p from that finite graph and add its current to (5). The signed sum
has divergence delta_x. Its finite nonzero-row graph contains an absorbing
path from x: any weak component disjoint from1 has divergence sum zero,
so it cannot contain the sole positive source. Extracting that path gives a
nonnegative integer current. No global cycle exclusion is assumed.

For a full selected profile, retain each R_N coefficient1 or2. Add its
weighted bridge, and request the corresponding total multiplicity at every
lower target. Different roots may reuse a supplied absorbing path as a proof
input. This is not reuse of annular source capacity. The resulting current
certifies exactly the selected weighted submeasure.

Since eta(q)<=q, the new test includes R26's old test. Its recognized
return targets are contained in
[R29's exact supplied-history saturation](../supplied-path-saturation-core/README.md):
S^h(p)=q and p<N make q a supplied forward-history state. This is an explicit
arithmetic way to recognize such history without constructing the whole
finite Q_N table. It does not enlarge that known target set. The originating
seed x is certified by the separate R26 bridge into that target; it is not
asserted that x already belongs to the supplied-history closure.

#### Exactly which return branches can improve

Write R26's complementary parameters as a>=2, odd t, d>=2,
`w=(3^(a-1)t-1)/2^d`, and b=floor(d/2).

**Even d is unchanged.** Here f=2*3^b w+1 is3 modulo4, so normalization
gives either q=f or q=(f-1)/2. In the first case q=1 modulo3; in the
second q=0 modulo3. Therefore h=0 in both cases. This entire branch
still requires another construction when R26's cutoff test fails.

**Odd d=2b+1.** Write the exact elementary stratum as

```
f=F^k(q) or F^k(2q+1),        q canonical.
```

In the two cases respectively,

```
3*4^k*(q+1) =3f+2*4^k+1,
6*4^k*(q+1) =3f+2*4^k+1.                              (6)
```

Thus the inverse depth is independent of the partner flag once the stratum
is fixed. Multiplying the common numerator by2^d gives

```
V=3^(a+b)t-3^(b+1)+2^d*(2^(2k+1)+1),
h=v_3(V)-1.                                           (7)
```

For odd n, `v_3(2^n+1)=1+v_3(n)`: factor out3 repeatedly in
`A^3+1=(A+1)(A^2-A+1)` with A=2 to an odd exponent; at A=-1 modulo3
the second factor has exact valuation1. The remaining odd exponent not
divisible by3 contributes no extra factor. This is the elementary lifting
identity needed here.

Put e=v_3(2k+1). If b differs from e, (7) has a unique term with least
ternary valuation, and hence

```
h=min(b,e).                                          (8)
```

If b=e, retain the exact formula (7); cancellation can increase the depth.
In particular k=0 always has h=0. These statements cover every elementary
stratum of every R26 return; no independence assumption between binary and
ternary conditions is used.

### 3. A small complete cylinder beyond the old cutoff rule

For every positive x in the binary cylinder

```
x=19199 modulo65536,
x=256t-1,       t=75 modulo256,
```

one has a=8, d=3 and raw f=F(q), with

```
q=(6561x+3745)/8192=1 modulo8,
v_3(q+1)=1,
p=(2q-1)/3=(2187x-117)/4096.                           (9)
```

Indeed `q+1=3(2187t+7)/32` has exact ternary valuation1. The complete
ordinary words are `(1,1,1,1,1,1,1,2,6)` from x and `(1,2)` from p,
and they prove

```
S^9(x)=S^2(p).                                        (10)
```

The first word has total valuation15, so its exact cylinder correctly
retains the extra bit, modulus2^16.

Whenever x is an actual R_N root, x<3N/2 gives
`p<(2187/4096)x<(6561/8192)N<N`. Hence every actual source in this
cylinder is certified. The new roots beyond R26 satisfy exactly

```
(8192N-3745)/6561 < x < 3N/2.                          (11)
```

For N>=8 the lower endpoint exceeds9N/8. Thus these are coefficient1
roots with x=3 or7 modulo12. Intersecting the binary class with those
two ternary classes gives an exact pair of progression counts. Their mass is

```
[3299/(13122*98304)] N + O(1),                         (12)
```

with absolute error less than3: each progression contributes error less
than1, and the constant endpoint displacement contributes less than1.
This is a count for the stated extra subfamily, not a new global residual
fraction. For example, at the required cutoff N=65536, root84735 has
q=67865>N and p=45243<N. Its exact certificate is stored.

### 4. Complete families with arbitrarily high old canonical returns

Fix any h>=2 and set

```
k=(3^h-1)/2,  b=h+1,  d=2h+3,  M=h+2+3^h.
```

Choose the unique integer a with

```
4/9 <= lambda=3^a/2^(a+M) < 2/3.                      (13)
```

Existence and uniqueness follow because successive values multiply by3/2;
neither boundary equality occurs for these M. A finite integer comparison
finds a without approximating logarithms. In particular a>=2.

Define the odd residue t_0 modulo `2^(d+2k+3)` by

```
3^(a+b)t_0 =3^(b+1)+2^d*(4^(k+1)-1)
                         modulo2^(d+2k+3),
x=2^a*t_0-1 modulo2^K,       K=a+d+2k+3.               (14)
```

This exactly imposes odd d and f=F^k(q) with q=1 modulo8. It has no
hidden ternary condition. From e=v_3(2k+1)=h<b, equation (8) proves
that the complete decreasing inverse depth is exactly h, uniformly over
the entire cylinder.

Put

```
c=1/3-3^(h+1)/2^d >0,
beta=lambda+(2/3)^h*(2/3+c/4^k)-1.
```

Direct substitution in (1) gives the exact affine lower seed

```
p=lambda*x+beta,      -5/9<beta<-7/192<0.              (15)
```

For the lower bound use c>0 and lambda>=4/9. For the upper bound use
h>=2, k>=4, c<1/3 and lambda<2/3:
`(2/3)^h*(2/3+c/4^k)<8/27+1/1728=19/64`.
Consequently p<(2/3)x<N whenever x<3N/2.

Meanwhile the old canonical return has the exact expression

```
q=Lambda*x+Lambda-1/3+c/4^k,
Lambda=(3/2)^h*lambda >= (3/2)^h*(4/9) >=1.            (16)
```

Thus q>x for every positive member of the cylinder. Every actual R_N
source in (14) is missed by R26's cutoff test and is certified by (5).
The guaranteed slope Lambda is unbounded as h grows. This deals with
unbounded old return heights by a complete arithmetic family, not by
assuming absorption at those larger heights.

The full prescribed merger is

```
S^(a+b)(x)=S^(h+1)(p).                               (17)
```

The x word is `1^(a-1),2^b,(2k+4)`; its total valuation is K-1, retaining
the required extra exact-valuation bit in (14). The p word is `1^h,2`.
No prefix can hit1 before the displayed common state, which exceeds1.
If the lower seed absorbs, the exact hitting-time difference is a, since
b=h+1. The bridge can be taken as the difference of these two prefix
currents. Replacing the known p prefix by the x prefix directly yields a
nonnegative absorption current, with source weight preserved.

#### Actual weighted sources and required rays

Intersect the binary residue r moduloP=2^K with the four original source
rows, retaining all their weights:

```
(N,3N/2),       x=3 mod12,       weight1;
(9N/8,3N/2),    x=7 mod12,       weight1;
(N,9N/8),      x=7 mod36,       weight2;
(N,9N/8),      x=19 mod36,      weight2.
```

For a row x=s modulo4m, the combined class is
`r+P*((s-r)P^(-1) mod m)` moduloPm. Count its strict interval by
`ceil((H-r')/(Pm))-floor((L-r')/(Pm))-1`, or zero for an empty interval.
The full weighted mass in (14) therefore has the exact finite formula
implemented by `source_count`, and

```
abs(mass - [25/(72*2^K)]N) <=6.                       (18)
```

The leading coefficient follows from the lower-shell weighted odd-modulus
density7/9 and upper-shell density2/3. The four progression errors have
total weight6. This is for each fixed h; its period and coefficient depend
on h. No uniform positive density for their union is asserted.

There are such actual sources on infinitely many required cutoffs. For
weight1 impose x=0 mod3, let N=12*2^B with B>=K, and take the first CRT
representative above N. It lies below N+3*2^K<=5N/4. For weight2 impose
x=7 mod36 and B>=K+3; the first representative lies below
N+9*2^K<=35N/32<9N/8. The endpoints are actual odd source states,
and both constructions stay below3N/2. The stored h=2 example retains
weight2, including both units in its resulting current.

### 5. Exact count of the whole extended rule

The implementation also counts every root certified by p<N, without
enumerating roots or following absorption. R26 already supplies for each
run cell (a,d), elementary stratum (k,partner), and source row a canonical
target interval and an arithmetic class

```
q_low<q<q_high,       q=r modulo3^E.                  (19)
```

For each possible h, replace the upper endpoint by

```
min(q_high, (3/2)^h*(N+1)-1),                         (20)
```

and intersect (19) with q=-1 modulo3^h, excluding q=-1 modulo3^(h+1).
The exclusion is a subtraction of counts in the same interval. Since all
odd moduli are powers of3, compatibility is exact divisibility, with no
coprime assumption. R25's `canonical_count` then gives each integer count.
For even-d nonpartner strata, subtract the canonical1-mod8 class as in R26.
All original source weights remain in the sum.

The sum is finite. One has a=O(log N), d=O(log N), k=O(log N), and
h<=floor(log_3(f_max+1))=O(log N), with R26's explicit f_max on each
cell. The canonical counter itself uses O(log N) progression terms.
Thus this is an exact finite formula using at most O(log^5 N) arithmetic
operations; bit complexity is not included in that statement. Usually r
already fixes h<E and there is only one depth to inspect. No leading
coefficient for the full extended profile is claimed in this batch.

### 6. Reproduction and remaining obligation

```
python3 experiments/residual_progress/inverse_ancestry/check_inverse_ancestry.py
```

The default runner compares the stored receipt and finite certificates.
`--write-receipt` regenerates them. Its finite input discovery is capped;
the arithmetic constructors never search an unknown orbit. The parent's
unified repository gate remains separate from this focused checker.

The focused checks cover4096 canonical targets below16384; inverse depths
1 through128;2048 complementary return branches;32 members of (9);12
required-ray witnesses from (14), with both weights and h=2 through7;
eight exact full-profile counts through N=65536; and three supplied
full-profile conversions. The two new-root certificates are:

| N | root x | lower seed p | old return q | weight | output rows |
|---:|---:|---:|---:|---:|---:|
|65536|84735|45243|67865|1|25|
|52776558133248|55862997549055|34013453716263|76530270861593|2|171|

Their rows are stored in `root84735_current.csv` and
`large_h2_weight2_current.csv`. Only their lower single-seed inputs are
discovered, with a5000-step cap; no full U_N table at the larger cutoff is
constructed. At N65536 the extended rule removes1563 weighted units,
versus1562 for R26; the sole extra root is84735. These are implementation
checks, while the universal cylinder claims rest on the written proofs.

This rule has a complete local inverse formula, exact full-profile count,
and infinite new lower-seed bridge families. Its recognized return targets
lie in known-history saturation; the originating seeds need not already be
represented there. It does not lower every global ancestor minimum and leaves all
even-d failed returns unresolved. Its decreasing inverse parameter proves
only termination of this recognizer. A universal complementary-root
construction still needs additional arithmetic information or mergers.

## Certificates

- [`check_inverse_ancestry_recompute.py`](check_inverse_ancestry_recompute.py) (written at the B10 migration, about 0.5 s, standard library). It rebuilds `S`, `ν`, the R26 return and `R_N` itself and checks: the inverse chain, the six ray minima and `L(q)` for all 4096 canonical `q < 16384`, and depths 1 to 128; formulas (7) and (8) on all 2048 complementary returns below 16384 (1364 with even `d`); the 32 stored members of cylinder (9) with their words and numerators; for `h = 2, …, 7` and both weights, the family parameters, `K`, the ray witness, its exact weighted source count against the receipt and against (18), `p = λx + β`, the order `p < N < x < q`, and the words of (17); the old and extended masses and the extra root at the eight receipt cutoffs, by explicit enumeration of `R_N`; the divergence and positivity of the two stored new-root currents; and the 33 counterfamily cases. It does not rebuild the full-profile conversions from supplied `U_N` currents or the bridge-current hashes (legacy checker, evidence only).
- The command in the legacy text names `experiments/residual_progress/inverse_ancestry/`.

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B18-replay-revival migration; standard library) replays the unmodified legacy check `check_inverse_ancestry.py` in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, requiring exit 0 and every file unchanged (about 15 s). It checks finite steps only; the status is unchanged.

## Remarks

- **Scope.** The rule is partial: even-`d` returns are untouched, the decreasing inverse parameter proves only termination of this recognizer, and stopping at `η` cannot replace complete inverse search (the `27 + 131072j` family). The extended test certifies one more root than R26 at `N = 65536` and none at `N = 6144`.
- **Controls.** The arguments are exact arithmetic identities for the `3x+1` step together with a supplied absorption current; no statement about other `3x+d` maps is made, and the conditional application inherits whatever the supplied input asserts.
- **Novelty.** Novelty undetermined (none claimed).
- **Next obligation.** A universal complementary-root construction still needs additional arithmetic information or mergers: [`five-ray-complementary-profile-completion`](../../questions/five-ray-complementary-profile-completion.md).

## History

- Migrated from `experiments/residual_progress/inverse_ancestry/INVERSE_ANCESTRY.md` (legacy ID R34) at commit `be73a66`, by the B10 migration (Claude, Opus 5.5). Note, scripts, receipt and the two stored currents moved byte-identical; `check_inverse_ancestry_recompute.py` was added at the migration. Legacy status: "written arithmetic extension, exact full-profile counting formula and finite currents" (the note itself opens "Written arithmetic proofs and finite certificates").
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `1603bf3`. The legacy index's "independent proof/code/count audits" were the main lane's own agents. The side lane's finite check is recorded under `reviewed_by`.
