---
id: equal-amplitude-half-defect-exclusion
kind: result
title: Equal-amplitude half defects exclude denominator one at every amplitude
status: written
claim: >
  Raw odd-only positive valuation words. Let u,v have equal length n>=2,
  differ in exactly two positions, and have the same positive absolute
  change p at both positions. If D_(uv)>0, then under EXT-1 den(uv)>1,
  for every amplitude, length, total and sign pattern. No primitivity,
  coprimality, near-critical or imported convergence assumption is used.
  Cyclic normalization gives W=A B A[p] B[p], where the bracket raises
  only the final letter. For a hypothetical integer 3x+1 cycle, retaining
  both half factors gives n<40 log2(1/eta), with the half gap
  eta=1-3^n/2^(sum(A)+sum(B)+p). EXT-1 and exact powers reduce n to at
  most 959; exact minimum bounds and local descent below 2^17 contradict
  that possibility. Actual 3x+d controls retain their additive parameter,
  including complete plus-factor cancellation at amplitude 14.
authors:
  - Codex cycle research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex root research lane (GPT-6; directed by Santiago Armstrong)
created: 2026-11-08
assumes: [musson-collatz-gap-all]
certificates: [check_equal_halves.py]
evidence:
  - "check_equal_halves.json: exact two-factor identities, sign normalization, complete power-gap and minimum comparisons, local descent and actual cycle controls"
tags: [cycles, denominators, half-defects, equal-amplitudes, exact-arithmetic]
---

# Equal-amplitude half defects exclude denominator one at every amplitude

## Statement

For a positive valuation word w, let C_w be its additive-one intercept,
D_w=2^sum(w)-3^len(w), and den(w)=D_w/gcd(C_w,D_w) when D_w>0.

Let u,v have the same length n>=2 and differ at exactly two positions
i<j, with

~~~
|v_i-u_i|=|v_j-u_j|=p>=1.                              (1)
~~~

If D_(uv)>0, then under
[EXT-1](../../../../sources/musson-collatz-gap-all.md),

~~~
den(uv)>1.                                            (2)
~~~

All sign patterns and all positive amplitudes are covered. No
primitivity, coprimality, near-critical or imported convergence
hypothesis is imposed. EXT-1 is the sole external input: the finite
convergence range used below is replayed here, without a published
period bound.

The earlier [equal-amplitude normal form](../equal-amplitude-half-defect-normal-form/README.md)
excludes full plus-factor cancellation unconditionally through
amplitude 12. That stronger cancellation statement fails in general:
the [gap-fourteen control](../transposition-gap-fourteen-full-plus-cancellation/README.md)
cancels the entire plus factor. The present proof retains the
remaining minus-factor equation and excludes denominator one at every
amplitude under EXT-1. It does not assert that the plus factor survives.

## Proof

### 1. A double-increase cyclic normal form

Write A[p] for A with its final letter increased by p. A cyclic
rotation of uv, allowing exchange of its halves, has the form

~~~
W=A B A[p] B[p],                                      (3)
~~~

where A,B are nonempty positive words.

If the changes in (1) have the same sign, exchange the halves if needed
to make both positive. If they have opposite signs, cut between their
positions. Exactly one changed position crosses the half boundary, so
exactly one sign reverses. Exchanging halves then makes both positive.
Finally cut immediately after the second changed position and exchange
halves once more. The second positive change is now the final letter;
the first separates A from B. Distinct changed positions make both
blocks nonempty.

All operations are rotations of the complete word. The identity

~~~
2^w_0 C_(rotate(w,1))=3C_w+D_w
~~~

preserves gcd(C_w,D_w), since D_w is coprime to both 2 and 3.
Equivalently, rotation changes only the starting state of an actual
cycle. It suffices to exclude denominator one for (3).

For completeness, den(W)=1 means D_W divides C_W. The rotation
identity and gcd(D_W,2)=1 propagate this divisibility to every rotated
intercept. Positive letters make each such intercept positive and odd,
as is D_W. Thus the quotients C_(rotate(W,i))/D_W are positive odd
integers. The same identity gives their exact 3x+1 arrows, with precisely
the prescribed valuations because the successor is odd. No separate
word-to-cycle correspondence is assumed.

### 2. Retaining both factor equations

Put

~~~
a=len(A), b=len(B), n=a+b,
P=3^a, R=3^b, Q=2^sum(A), S=2^sum(B), k=2^p,
alpha=PR=3^n, beta=kQS,
Pplus=beta+alpha, Pminus=beta-alpha,
eta=Pminus/beta=1-alpha/beta, G=log2(1/eta).             (4)
~~~

The full length is 2n, the total valuation is
2(sum(A)+sum(B)+p), and the discriminant is Pplus*Pminus.
Thus D_W>0 is equivalent to beta>alpha, so 0<eta<1.

For the algebra, retain a general positive odd additive parameter d.
Let the actual positive odd boundary states be

~~~
x --A--> z --B--> y --A[p]--> t --B[p]--> x.
~~~

They satisfy

~~~
Qz=Px+dC_A,       Sy=Rz+dC_B,
kQt=Py+dC_A,      kSx=Rt+dC_B.                         (5)
~~~

The positive affine maps are increasing and
F_(A[p]B[p])(s)<F_(AB)(s) for s>0. If x>=y, then
y=F_(AB)(x)>=F_(AB)(y)>F_(A[p]B[p])(y)=x, a contradiction.
Hence y>x.

Subtracting corresponding equations shows that

~~~
H=(y-x)/Q,             J=(z-t)/S                       (6)
~~~

are odd integers, with H>0. Indeed, PH=kt-z and RJ=y-kx
are odd, and integrality follows first from the coprimality of the
powers P,Q and R,S. Solving gives

~~~
x=(QH-RJ)/(k-1),       t=(PH+SJ)/(k-1).
~~~

Substitute these expressions into (5) to obtain

~~~
Pplus J = d(k-1)C_A,
Pminus H = d(k-1)C_B+(k+1)RS J.                        (7)
~~~

The first identity forces J>0. Thus H,J are positive odd integers.
Both factors and the actual additive parameter remain present; no
coprimality cancellation of k-1 is made. H,J are auxiliary differences,
not the cycle extrema.

### 3. The plus equation makes the first block long

Assume now d=1. Positive letters give the strict intercept bounds

~~~
C_A<PQ/2^a,             C_B<RS/2^b.                   (8)
~~~

For example, if s_i is the first i letters' sum in A, then
sum(A)-s_i>=a-i. Summing the resulting geometric series gives
C_A/Q <= (3/2)^a-1 < (3/2)^a.

By the first equation of (7), J>=1, and (8),

~~~
(k-1)PQ/2^a > (k-1)C_A=Pplus J>kQS.
~~~

Consequently

~~~
P>2^a S>=2^(a+b)=2^n.
~~~

Since 3^5<2^8, this implies

~~~
a>5n/8.                                              (9)
~~~

### 4. The minus equation limits that block by the amplitude

Divide the second equation of (7) by beta and substitute its first:

~~~
eta H = (k-1)C_B/beta
        +(k+1)RS(k-1)C_A/(beta Pplus).                 (10)
~~~

For the first term, (8), alpha/beta<1 and P>2^a S give

~~~
(k-1)C_B/beta
  < (k-1)R/(kQ 2^b)
   = (k-1)(alpha/beta) S/(P 2^b)
  < (k-1)/2^n.                                       (11)
~~~

For the second term, (8) and alpha/Pplus<1/2 give

~~~
(k+1)RS(k-1)C_A/(beta Pplus)
  < ((k^2-1)/k) alpha/(2^a Pplus)
  < k/2^(a+1).                                       (12)
~~~

As H>=1 and b>=1, equations (10)--(12) yield

~~~
eta < (k-1)/2^n+k/2^(a+1) < k/2^a,
a<p+G.                                               (13)
~~~

The bound (13) is what the remaining minus-factor equation supplies.

### 5. Product and minimum bounds on the half clock

Let L denote the minimum of the hypothetical integer cycle.
The certificate follows every odd seed 3<=s<2^17 until it reaches a
smaller positive odd value. Such a seed cannot be a nontrivial cycle's
minimum. The word (3) is nontrivial because corresponding letters
differ by p>=1, so

~~~
L>=2^17.                                             (14)
~~~

In particular L>=129. The exact comparison
388^5<2^8*129^5 and the product of the full 2n arrows give,
for T=sum(A)+sum(B)+p,

~~~
2^(2T)=product_i(3+1/x_i)<2^(16n/5),
T<8n/5,             p=T-sum(A)-sum(B)<3n/5.            (15)
~~~

Combining (9), (13) and (15),

~~~
5n/8 < a < 3n/5+G,          hence n<40G.               (16)
~~~

The minimum estimate must retain the half clock. The full product
identity says

~~~
-ln(1-eta) = (1/2) sum_(i=0)^(2n-1) ln(1+1/(3x_i))
           < n/(3L).
~~~

Since eta<-ln(1-eta), this gives

~~~
L<n/(3eta).                                          (17)
~~~

Thus n is half the displayed period, and eta is its associated half
gap, not the full-word gap.

### 6. Complete exact finite closure

EXT-1 applies directly to 3^n<2^T:

~~~
eta>=2^(-172)n^(-341),       G<=172+341log2(n).         (18)
~~~

If n>=2^19, choose j>=19 with 2^j<=n<2^(j+1).
Equation (16) would require 2^j<40(172+341(j+1)).
The left side minus the right is 244608 at j=19; its next
increment is 2^j-13640, positive and increasing. Hence n<2^19.

For every integer 1<=n<2^19, the certificate computes

~~~
P_n=3^n, T_n=bit_length(P_n), B_n=2^T_n,
gap_n=B_n-P_n,
~~~

and checks

~~~
2^24 gap_n > B_n.                                    (19)
~~~

Here T_n is the smallest integer with 2^T_n>3^n.
Since 1-3^n/2^T increases with T, (19) implies eta>2^(-24)
for every possible total in that range. Thus G<24, and (16) gives

~~~
n<960,             n<=959.                           (20)
~~~

For all 1<=n<=959, the certificate also checks

~~~
3*2^17*gap_n > n*B_n.                                (21)
~~~

The maximum of n*B_n/(3gap_n) over this range has ceiling 99935,
at n=918 and T_n=1455. By (17) and monotonicity,
L<99935<2^17, contradicting (14).

This closes every length and amplitude under EXT-1 alone.
The power checks and local descent are complete computations over
their stated intervals. No extrapolation, convergence import,
continued-fraction source or least-period assumption is used.

## Certificates

[check_equal_halves.py](check_equal_halves.py) and its generated
[receipt](check_equal_halves.json) check the factor equations with the
actual positive additive parameter, cyclic sign normalization and
denominator invariance, all 524287 power-gap comparisons in (19),
all 959 comparisons in (21), and all 65535 odd nontrivial local seeds
below 2^17.

The word controls are genuine reduced 3x+d cycles. They cover all
sign patterns and large amplitudes, including the known amplitude-14
signed crossing. Its full plus-factor cancellation and denominator
2^336-3^189 remain intact: (7) retains that actual d. The eleven
shared 3x+5, 3x+7, 3x+13 and 3x+61 fixtures are replayed too.
Finite examples check the identities and scope; they do not prove
the all-amplitude result by absence from a census.

From the repository root:

~~~
python3 areas/cycles/results/equal-amplitude-half-defect-exclusion/check_equal_halves.py
python3 -O areas/cycles/results/equal-amplitude-half-defect-exclusion/check_equal_halves.py
~~~

The default verifies the committed receipt; --write-receipt regenerates
it. Checks use only exact standard-library arithmetic and remain active
under optimized execution. The external EXT-1 theorem is not rebuilt
by this certificate.

## Remarks

- The earlier finite signed-crossing results retain their stronger
  unconditional small-amplitude scope. This proof extends the
  denominator-one exclusion to every equal amplitude using both
  factor equations and EXT-1, without extending an orbit census.
- The [small-endpoint criterion](../small-mersenne-endpoint-exclusion/README.md)
  and [state enclosure](../mersenne-join-state-enclosure/README.md)
  assume two unequal positive Mersenne levels. They do not directly
  include this degeneration, and no extension of them is assumed.
- Unequal absolute half changes remain outside this result. No full
  four-mismatch exclusion or Collatz proof is claimed. Novelty is
  undetermined; same-session scrutiny does not upgrade written status
  to an independent review.

## History

- 2026-11-08: retained the two positive factor equations in the
  double-increase normal form, derived n<40log2(1/eta), and closed the
  finite range by exact powers and local descent. Earlier unconditional
  cancellation statements are preserved.
