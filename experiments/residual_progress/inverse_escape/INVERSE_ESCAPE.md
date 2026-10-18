# Variable-depth inverse escape with strictly smaller W5 inputs

**Status: written exact identities, a conditional constructor, and scoped
complete-inverse obstructions.** This supplies no universal family of input
currents and no proof of Collatz. The main result is the full arithmetic rule
in Sections 1–3, rather than the examples or supporting barriers.

Use ordinary odd Syracuse S, absorbed at1, for every current. Write `[x]` for
`delta_x`, with `[1]=0`, and `P(w)=[3w]-[w]`. The canonical normal form nu and
quotient T=nu S are those of
[R25](../bridge_normal_form/BRIDGE_NORMAL_FORM.md). `N_x` denotes its explicit
ordinary current `[x]-[nu(x)]`. Only Sections 4–6 count **quotient** steps.

The construction depends on the exact smaller-input absorption compiler in
[R41](../critical_inverse/CRITICAL_INVERSE.md), which in turn uses R37 and R40.
These are formal plans retaining their missing P inputs, not supplied currents.

## 1. A complete two-block inverse rule

Let q>1 be any canonical odd integer with q=1 modulo3. Define

```
D=v3(q-1)>=1,       u=(q-1)/3^D,
s=4^D*u+1,         j=v3(s+1),
p=2^j*(s+1)/3^j-1.                                      (1)
```

Here u is positive even and not divisible by3. The first D inverse steps
`y -> (4y-1)/3` are all legal: their states are
`4^i*3^(D-i)*u+1`, for1<=i<=D. Every such predecessor is canonical1 modulo8,
by R25's complete inverse table. They are ordinary valuation2 arrows in the
forward direction. For i<D the state is1 modulo3, so D is the maximal length
of this initial branch. The terminal state s is not1 modulo3.

Exactly j following inverse point steps `y -> (2y-1)/3` are legal. Their
states are `2^i*(s+1)/3^i-1`. Before each step the target is2 modulo3; afterward
the predecessor is canonical by R25. Thus

```
S^(D+j)(p)=q,
the exact ordinary valuation word is 1^j,2^D.             (2)
```

All states are positive odd. In fact s=1 modulo8, so v2(s+1)=1 and

```
v2(p+1)=j+1.                                             (3)
```

The negative of the finite p-to-q path gives an explicit integer current I
with `div I=[q]-[p]`. This is valid whether or not p<q.

### Exact descent criterion, including integer endpoints

Put `lambda=2^(2D+j)/3^(D+j)`. From (1),

```
p-q=(lambda-1)*(q-1)+2*(2/3)^j-2.                        (4)
```

Consequently

```
p<q  if and only if  2^(2D+j)<3^(D+j).                   (5)
```

If lambda<1, both terms in (4) are nonpositive and the first is negative.
If lambda>1, (4) is strictly greater than -2. The difference p-q is an even
integer, so it is nonnegative. Equality lambda=1 is impossible because D>=1.
Thus there are **no small-u exceptions** beyond the slope test. Equivalently,
the exact inequality before this parity argument is

```
(2^(2D+j)-3^(D+j))*u < 2*3^j-2^(j+1).
```

This classification is complete for the prescribed maximal two-block word.
Failure of (5) does not rule out another inverse word or a different current.

## 2. A new whole domain with strictly smaller W5 requests

Define W5 as the positive integers5 modulo8. Take w in W5 with3w selected,
so its critical canonical image is `q=(3w-1)/2`, and compute (1). The rule
accepts precisely when

```
j>=2 and 2^(2D+j)<3^(D+j).                               (6)
```

It produces a finite formal current plan

```
div J=P(w)-sum_v c(v)P(v),
every requested v is in W5 and v<w.                      (7)
```

**Proof.** By (3), p=7 modulo8. Apply exactly one R37 critical step to p:

| p modulo3 | lower seed l | missing pair v |
|---|---|---|
|0|p/3|p/3|
|1|(2p+1)/3|(2p+1)/3|
|2|(2p-1)/3|none|

For the maximal j in (1), p is never2 modulo3: the remaining unit in
(s+1)/3^j is not divisible by3. The third row records the valid free descent
when one instead stops an admissible point block early, as in (11).

Its exact current K has divergence `[p]-[l]-P(v)` when a pair is present,
and `[p]-[l]` otherwise. Every l is at most `(2p+1)/3`, which is strictly
below `w=(2q+1)/3` by (5). In the first row, p=7 modulo8 implies v=5 modulo8.
In the second, `3v=2p+1=15 modulo16`, hence again v=5 modulo8. **No W9 input
occurs at this step.** In particular there is no hidden expanding R40
replacement of its leading child.

Let z=nu(w)<w. The finite current

```
L=N_(3w)+I+K-N_w
```

has divergence `P(w)-P(v)-[l]+[z]` (omit P(v) in the third row).
R41 gives formal absorption plans H_l and H_z requesting only W5 inputs
strictly below l and z. Therefore `J=L+H_l-H_z`, with the missing P(v) added
to the coefficient list, has exactly (7). All signs and repeated coefficients
are retained. Shared current rows can cancel; missing premises cannot be
silently supplied.

### Compatibility with the common critical-image rank

The plan also strictly decreases `rho(w)=nu(3w)=q` on every request.
The leading child, when present, has rho(v)=p<q. The
[critical-image absorption bound](../critical_rank/CRITICAL_IMAGE_RANK.md)
gives `rho(H_l)<=(9l+5)/8<=(3p+4)/4<p`, since p>=7. For the other input,
z=nu(w)<=(w-1)/4 gives `rho(H_z)<=(9w+11)/32<q`. Thus this rule can be
combined with other strict-rho rules even if those other rules increase
their pair indices. The API records `rho` and checks both strict inequalities.

The new domain with D>=2 has w=1 modulo3, because
`D=1+v3(w-1)`. It is therefore disjoint from R41's eligible domain E, where
3 divides w. The D=1 accepted row recovers a previously handled part of E.

### Sufficient-set consequence

Let E_escape be the domain (6), restricted to D>=2. Universal finite exact
P currents on

```
W5 \ (E_good union E_escape)                             (8)
```

suffice for Collatz: strong induction on w supplies every omitted E_good
input by R41 and every omitted E_escape input by (7), always using strictly
smaller W5 inputs. R40 then supplies W9, and R37 applies. Conversely Collatz
supplies every current in (8). This removes a whole arithmetic domain from
the universal premise; it does not establish that premise.

## 3. Every block-length pair has a full exact congruence family

For any D>=1 and j>=1, impose

```
4^D*u+2 = 3^j modulo3^(j+1),
3^D*u = 6 modulo32.                                     (9)
```

CRT gives one full class of positive even u modulo `32*3^(j+1)`.
The first congruence forces v3(4^D*u+2)=j and u=1 modulo3; the second gives
q=1+3^D*u=7 modulo32. Thus q is complementary canonical, its critical index
w is5 modulo64, and3w is selected. Every positive member has the exact
parameters D,j. More generally the two nonzero choices of the terminal
ternary unit describe all phases of exact j; (9) picks one complete infinite
subfamily for reproducible witnesses.

For every D, choose any j>=2 satisfying (5). This gives infinitely many new
accepted inputs when D>=2, with arbitrarily large exact word length. It is
not an assumption that their later orbits converge. The rule constructs a
finite conditional plan from the displayed word and lower-input plans only.

### First sharp phase: exactly four quotient inverse steps

For **every** canonical q>1 with q=1 modulo9, a smaller canonical ancestor
under1 through3 quotient steps is impossible. At depth4, a smaller ancestor
exists **if and only if**

```
q=10 modulo81.                                          (10)
```

It is unique at these depths and equals

```
p_2=(64q-73)/81,
S^4(p_2)=q with exact word(1,1,2,2).                     (11)
```

To prove completeness, use R41 at depth2. Every off-spine state exceeds
4q+3. Any canonical inverse step is at least `(2y-1)/3`; two further steps
from an off-spine state therefore remain above q. The sole remaining
depth2 state is `s_2=(16q-7)/9`. One further step is at least
`(32q-23)/27>q`, since any canonical q>1 is at least7. A two-step continuation
containing a ray is at least `(8s_2-7)/9=(128q-119)/81>q`; here every ray is
at least `(4y-1)/3`. Thus only two consecutive point steps can descend.
They are legal exactly when `9|(s_2+1)`, namely (10), and give (11).

On the selected W5 domain, (10) is `w=7 modulo54`. It has D=2 and j>=2;
the maximal rule (6) therefore accepts it. If j>2, its maximal ancestor is
different from p_2, but the minimal sufficient inverse depth is still4.
The smallest critical example is w61, q91, p_2=71.

## 4. The old barrier persists one step beyond its stated precision

For every D>=2 and canonical q>1 with q=1 modulo3^D, all canonical ancestors
at depths1 through D+1 are greater than q. R41 covers depths<=D. At depthD,
an off-spine state exceeds4q+3 and remains greater after one inverse step.
For the spine state `s_D=4^D*u+1`, where q=1+3^D*u and u>=2, even the lower
bound `(2s_D-1)/3` exceeds q: its difference is

```
[u*(2*4^D-3^(D+1))-2]/3 > 0.
```

The coefficient is at least5 for D>=2. D=1 is different: its immediate
escape is exactly q4 modulo9, the phase already used in R41. Section 3
shows that D=2 can first escape at depth4, and classifies that whole case.

## 5. Fixed ternary precision does not bound inverse escape depth

The constructive rule does not provide a depth bound depending only on
v3(q-1). Here is a complete all-ray obstruction with that valuation fixed1.

For every D>=2 and every t>=1, set

```
q=7+32*3^D*t,       w=(2q+1)/3=5+64*3^(D-1)*t.            (12)
```

Then q is critical complementary7 modulo32, w is5 modulo64,3w is selected,
and **v3(q-1)=1**. Nevertheless every canonical p with

```
T^d(p)=q, 1<=d<=D
```

satisfies p>q. Every inverse branch and every unbounded ray index is included.

**Proof.** Shadow the chosen inverse word at7. Actual and shadow states
have the form `p_i=lambda_i*(q-7)+c_i`, with a power-of2 slope over3^i.
The congruence in (12) ensures matching residues before each of the D steps,
so every actual branch is also a legal shadow branch. Every shadow is a
positive canonical ancestor of7. It cannot equal1, since T(1)=1; the least
canonical integer above1 is7. Hence c_i>=7.

Every affine inverse branch `y -> a*y+b`, including all ray iterates,
satisfies a-b>=1, with strict inequality on every ray (R41). Define
`G_i=lambda_i-(c_i+1)/8`. Then

```
G_i=a*G_(i-1)+(a-b-1)/8.
```

Initially G_0=0. The first inverse at7=1 modulo3 must be a ray, so G_1>0
and strict positivity persists. Thus lambda_i>(c_i+1)/8>=1, and
`p_i=lambda_i*(q-7)+c_i>q`. This proves the full quantifier without scanning
the tree. Taking t not divisible by3 additionally makes v3(q-7)=D exactly.

## 6. One or two forward steps do not repair this fixed-phase barrier

For (12), the first two actual and quotient steps coincide:

```
y_0=q,
y_1=(3q+1)/2,
y_2=(9q+5)/4.
```

They shadow `7 ->11 ->17`. For k=0,1,2, every canonical origin p satisfying

```
T^d(p)=y_k, 1<=d<=D+k
```

obeys **p>=q**. Equality occurs exactly for k>=1,d=k and the original
k inverse point steps returning to q. All other origins are larger.

Write c_0=7,11,17 respectively and `a_0=(3/2)^k`, so c_0+1=8a_0 and
`y_k-c_0=a_0*(q-7)` is divisible by3^(D+k). Every inverse shadow of c_0 is
at least7, for the same reason as in Section 5. With lambda the inverse
slope, the gap `lambda-(c+1)/(c_0+1)` starts0 and remains nonnegative by
the same recurrence. Therefore the effective slope is

```
a_0*lambda >= (c+1)/8 >=1,
p=a_0*lambda*(q-7)+c >=q.
```

Equality forces c=7 and zero gap, hence every branch must be a point.
At c_0=11 this occurs after exactly one point; at17 after exactly two.
At7 a ray is required immediately. The next shadow cannot be1, so these
are all equality cases.

The corresponding ordinary-S assertion follows from `T nu=nu S` and
nu(p)<=p: no ordinary source p<q can reach y_k in the stated number of
ordinary arrows. An equal ordinary source must be q. This comparison does
not bound the ordinary length of a general quotient bridge.

The result rules out a fixed inverse lookback after either of these two
forward arrows as a universal completion on this family. It does not cover
an arbitrary forward excursion, unbounded input-dependent lookback,
supplied-history reuse, unequal-time mergers, or general current inference.
The seed changes with D; no fixed seed is proved permanently unresolved.

## 7. Reproduction

Run from the repository root:

```
python3 experiments/residual_progress/inverse_escape/check_inverse_escape.py
```

The default checker is read-only and compares deterministic results with
`inverse_escape_audit.json`; `--write-receipt` regenerates that evidence.
The implementation is [inverse_escape.py](inverse_escape.py). Its public
`pair_plan` returns `seed,rho,current,coefficients`, with every missing index
strictly smaller and in W5, and every missing critical image strictly smaller
than rho. `compile_plan` validates the supplied exact
currents. Rejected arithmetic cases remain unresolved by this rule.

The evidence covers2731 exact phase/word cases,444 parameter-family examples
through D256 and j182, and317 signed strict-rank plans below32768. Of these,
89 have D>=2 and228 have D=1. Both possible maximal-block child residues
occur. There are16 bounded actual substitutions using30 distinct supplied
currents; complete current tables for P61,P277,P709 are retained in the
receipt. It also covers the
complete depth4 classification by independent forward enumeration, arbitrary
sampled inverse rays (3229 finite words and48 longer words with indices up
to1024), and15 independent small full-origin checks of the fixed-phase
barrier. The depth4 check includes227 targets and27 descending cases, with
every potential smaller canonical origin through8191 included. The unbounded
quantifiers rest on the arguments above.
