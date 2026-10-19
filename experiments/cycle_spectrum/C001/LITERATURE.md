# C001 — Primary literature and scope of the denominator mechanism

**Status: bounded primary-source audit, 2026-10-18.** The selected mechanism
is cancellation for a repeated fixed valuation block followed by a fixed
perturbation. This note positions that mechanism, checks the proposed
unbalanced family, and identifies a concrete next extension. It does not
claim novelty or import an unchecked cycle exclusion. Historical R71 is
preserved unchanged.

## 1. Conventions and the existing baseline

For a positive valuation word w=(a_0,...,a_(r-1)), write

```
P_w=2^(sum a_i),   Q_w=3^r,
C_w=sum_(j=0)^(r-1) 3^(r-1-j) 2^(a_0+...+a_(j-1)),
D_w=P_w-Q_w.
```

The word acts by (Q_w*x+C_w)/P_w. When D_w>0 its fixed point
C_w/D_w is a genuine positive odd rational Syracuse cycle, with exact
valuations and common reduced denominator

```
d_w=D_w/gcd(C_w,D_w).
```

These facts are classical; the repository independently derives them in
[R71](../../residual_progress/lattice_cycles/BALANCED_DENOMINATORS.md).
R71 also gives the exact reduced denominator of mechanical words,
including reduction of repeated words. Repeating an existing cycle does
not create a new denominator. For every denominator comparison below,
least period and scaling to a primitive integer 3x+d cycle must be kept
distinct from the displayed word length.

The shortcut clock has one step per parity bit, so its displayed cycle
length is sum a_i, while the odd-only clock has r steps. Standard
Simons–de Weger/Hercher local-minimum counts use the shortcut clock.

## 2. Primary sources actually checked

### Böhm–Sontacchi and Lagarias

The [1978 original bibliographic record](https://www.bdim.eu/item?id=RLINA_1978_8_64_3_260_0)
describes an effective fixed-length cycle procedure for rational affine
branches. The full scan did not load in this pass. Lagarias's
[1990 publisher record](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/en/publishing-house/journals-and-series/acta-arithmetica/all/56/1/106574/the-set-of-rational-cycles-for-the-3x-1-problem)
confirms *The set of rational cycles for the 3x+1 problem*, Acta Arithmetica
56, 33–53. Its full primary PDF also failed to load. Consequently no
unread numbered theorem from that article is being adopted.

Barry Brent's [primary 2002 paper, Sections 2–4](https://arxiv.org/pdf/math/0204170)
explicitly states the parity-vector rational fixed-point theorem,
attributes it to Böhm–Sontacchi/Lagarias, and writes the reduced
denominator using the numerator gcd. It studies fixed-denominator
attractors and reports empirical length/odd-count scaling and covariance,
with exceptions. This supplies useful controls, not a general
classification or a theorem that every denominator has one positive
cycle. Its shortcut length is our sum a_i; its odd count is our r.

### Concatenation and repetition are established algebra

[Trümper 2014, Section 4, Eq. (75) and Lemmas 2–3](https://onlinelibrary.wiley.com/doi/pdf/10.1155/2014/756917)
already gives the commutator identity
`C_uv-C_vu=D_u*C_v-D_v*C_u` and the formula for C_(u^k), with
unchanged rational fixed point under repetition. The composition laws
are in Section 3. No explicit bounded-gcd or periodic-cancellation
corollary for u^k v was located in the inspected text. This limited
negative search is not a priority claim.

[Halbeisen–Hungerbühler 1997, Eq. (4) and Lemma 2](https://people.math.ethz.ch/~halorenz/publications/pdf/collatz.pdf)
also supplies the affine concatenation formula and rational-cycle
interpretation. Its main subject is optimal cycle-length/minimum
estimates. Thus affine encoding, rational legality, and concatenation
should all be attributed as background, not presented as newly found
structure.

### Knight's term “high cycle” has a specific extremal meaning

The [publisher abstract and Section 4 preview](https://www.sciencedirect.com/science/article/pii/S0012365X25004200)
define a high cycle by maximizing the cycle minimum at fixed shortcut
length and odd count, and identify its parity word as Christoffel.
The nonintegrality theorem concerns that class. Large absolute minimum
alone is not its hypothesis. The publisher preview was inspected;
the full journal text and HAL PDF were inaccessible in this pass.
The bibliographic record is Discrete Mathematics 349(3), 2026, 114812,
DOI 10.1016/j.disc.2025.114812.

### Current integer-cycle records need their clocks and versions

[Simons–de Weger's author-hosted 2007 update](https://www.deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.43%5B2007%5D.pdf)
defines m by shortcut local minima and excludes nontrivial m-cycles
for 1<=m<=75. Its header distinguishes that update from the 2005
journal version. These integer-cycle bounds are not uniform assertions
over rational denominator layers.

[Hercher's official journal page](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html)
states exclusion for m<=91 and links a
[2026 corrigendum](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/corrigendum.pdf)
repairing a step in Theorem 21. The corrigendum was inspected; an
independent replay of the entire computational proof was not performed.
The bound concerns the number of shortcut local minima, not odd-only
cycle length or the number of odd-only local minima.

A [June 2026 author-uploaded preprint by Xinjun Wang](https://www.researchgate.net/publication/408180567_NON-EXISTENCE_OF_COLLATZ_m-CYCLES_FOR_m_95)
claims exclusion through 95 under stated external inputs. The inspected
copy has a placeholder journal article number and blank acceptance
fields. This pass did not verify publication or replay its certificates;
it is not promoted to an established replacement record.

## 3. Selected mechanism: one repeated block and one fixed perturbation

For fixed nonempty words u,v, put

```
K=D_u*C_v-D_v*C_u,
w=u^k v.
```

The root lane's elementary elimination identity is

```
D_u*C_w-C_u*D_w=P_u^k*K.
```

Since D_w is coprime to 6, cancellation g_w=gcd(C_w,D_w) divides
K whenever K!=0. This bounds cancellation uniformly in k and gives
an explicit denominator lower bound when D_w>0. The mathematical
gain over a raw fixed-point formula is the fixed finite set of possible
cancellation divisors. The associated finite modular dynamics can
decide which of them occurs.

The exceptional case K=0 is essential: the two affine maps share a
fixed point, so repetition can preserve a small denominator. Neither
the identity nor a finite modular scan warrants dropping this case.
The relation is an elementary consequence of the established algebra
above. Its exact presentation as a denominator theorem was not found
in this bounded pass; novelty remains unassessed.

This mechanism is a better current batch than collecting more balanced
examples: R71 already solves the mechanical family. It also supplies a
concrete theorem to test against unbalanced words and large cancellations.

## 4. Audit of the strengthened unbalanced family

Let m>=13, A=ceil(m log_2 3), and choose the lower mechanical valuation
word u_m with entries

```
a_i=floor((i+1)A/m)-floor(iA/m).
```

Let w=u_m^k 2, with k>=2. The following checks are independent
calculations for the proposed family; they are not attributed to the
external articles.

### 4.1. Nonintegrality from the bounded divisor

Write C=C_(u_m), D=D_(u_m), x_0=C/D and q=3^m/2^A. R71 gives
every base-cycle state greater than m/6, so C>D and K=D-C!=0.
For every j<m,

```
3^(m-1-j)*2^floor(jA/m) < 2*3^(m-1),
```

because 3^m<2^A<2*3^m. Hence

```
|K|<C<(2m/3)*3^m,
D_w=4*2^(kA)-3^(km+1)>3^(km).
```

The cancellation bound therefore gives d_w>1 for m>=13,k>=2.
This is an all-parameter exclusion for this specified family, not a
finite verification claim.

### 4.2. Large minimum requires its extra exponent condition

The fixed point before the first copy of u_m is

```
x=[3*x_0*(1-q^k)+1]/[4-3q^k].
```

If q^k<=1/2, then x>=(3/5)x_0. Iterating whole u_m blocks moves
x toward x_0 and preserves this lower bound. Each partial block is
an affine map with positive multiplier and positive intercept, so its
value is at least 3/5 of the corresponding base-cycle state. Thus
every odd rational state is greater than m/10. Shortcut even states
are no smaller than the following odd state. For each fixed m, a
sufficiently large k satisfies q^k<=1/2; k>=2 alone is not asserted
to imply that condition.

### 4.3. It lies outside the mechanical/Christoffel class

For m>=13,

```
3/2<A/m<5/3.
```

Therefore u_m starts with 121 and ends with 122. Its entries are 1
or 2, and it has no cyclic factor 222: any three consecutive entries
have sum at most ceil(3A/m)<=5. Appending the extra 2 creates exactly
one cyclic 222. The unique occurrence also proves that w is primitive.

The factors 121 and 222 have sums 4 and 6, so w is not a mechanical
valuation word. More directly for Knight's shortcut parity convention,
the three gaps 121 give the length-five factor 11011, containing four
ones, while gaps 222 give 01010, containing two. This violates binary
balance. Thus the parity word is not Christoffel, independently of
any informal use of the word “high”.

### 4.4. The two minimum counts are different

Under the height condition all odd states exceed 1. A valuation-1
odd-only arrow increases, and a valuation-2 arrow decreases. The ones
are isolated, so the **odd-only** cycle has

```
k*(2m-A)
```

local minima. In the **shortcut** clock every valuation at least 2
ends an odd run and introduces an even run. The count used by
Simons–de Weger and Hercher is therefore

```
k*(A-m)+1.
```

Both are unbounded. The latter is the correct count when comparing
with a fixed cutoff such as 91. A claim equating those counts would
be a clock error.

### 4.5. What the comparison establishes

The family has a proved exact cancellation mechanism, is unbalanced,
and can simultaneously exceed any fixed absolute minimum and any
fixed local-minimum-count cutoff. It therefore goes outside R71's
mechanical class, Knight's stated Christoffel class, and the direct
hypotheses of fixed-count exclusions. No assertion is made that it
escapes every consequence of all published cycle methods, or that
this particular family has not appeared elsewhere.

## 5. Next extension: two growing blocks, with a published bridge

For w=u^k v^ell define the geometric sums

```
S_u(k)=(P_u^k-Q_u^k)/(P_u-Q_u),
S_v(ell)=(P_v^ell-Q_v^ell)/(P_v-Q_v).
```

The same elimination in both directions gives

```
D_u*C_w-C_u*D_w=P_u^k*K*S_v(ell),
D_v*C_w-C_v*D_w=-Q_v^ell*K*S_u(k).
```

Thus, when K!=0,

```
gcd(C_w,D_w) divides |K|*gcd(S_u(k),S_v(ell)).
```

This identifies a concrete next experiment: measure cancellation as
both exponents grow, splitting proportional and nonproportional pairs
of (total valuation, odd count). Do not propose bounded cancellation
in full generality. If u=(1,1,3), v=(1,2,2), and k=ell, both
blocks have (P,Q)=(32,27); their common geometric sum divides C_w
and D_w and grows exponentially.

There is a primary theorem to examine before calling the
nonproportional case a new conjecture:
[Corvaja–Zannier, Corollary 1 and Eq. (1.3)](https://arxiv.org/pdf/math/0311030).
For multiplicatively independent pairs in a fixed finitely generated
group, their generalized gcd is subexponential in the maximum height,
apart from finitely many exceptions for each epsilon. Apply this to
(P_u/Q_u)^k and (P_v/Q_v)^ell: independence follows from unequal
valuation/odd-count ratios. The displayed algebra suggests
subexponential cancellation in k+ell. An explicit numerical cutoff
does not follow from this citation. A full imported-theorem application,
including all local valuations, belongs in a subsequent batch; it is
not needed for C001's fixed-perturbation proof.

## 6. Seven-field decision record

1. **Objects.** Exact rational cycles indexed by positive valuation
   words, their reduced denominators, and affine block data.
2. **Structural gain.** A fixed perturbation of a repeated block has
   cancellation supported on one fixed nonzero integer K. This turns
   growing words into a finite divisor problem.
3. **Translated unresolved gap.** Several independently growing
   perturbations introduce common geometric factors; arbitrary words
   have no supplied bounded cancellation constant.
4. **Worked example.** u_m^k 2 gives primitive unbalanced cycles with
   growing minima and minimum counts, while its denominator remains
   greater than one by an explicit all-parameter bound.
5. **Known-cycle controls.** K=0 preserves common fixed points and
   repeated cycles. The trivial all-2 family must survive there.
   Reduced-denominator layers with d>1 are genuine cycles, not failures
   of rational legality.
6. **Cheapest meaningful next test.** Complete exact replay of the
   fixed-perturbation theorem, including its modular cancellation
   periods and degenerate cases. Then test the two-block gcd reduction
   against equal-slope controls before importing an asymptotic theorem.
7. **Intermediate milestone.** An explicit infinite unbalanced class
   with certified denominator spectrum and no denominator-one member.
   This neither excludes all integer cycles nor addresses divergence.

**Decision:** retain the bounded-cancellation mechanism as this batch's
main result, with classical algebra attributed and novelty unclaimed.
Do not replace it with another catalogue of mechanical examples or an
unverified claim to improve the general integer-cycle record.
