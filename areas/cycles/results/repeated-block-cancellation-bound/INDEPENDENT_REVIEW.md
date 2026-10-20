# C001 — Independent algebra, domain and executable review

**Status: written mathematics and corrected independent finite replay
PASS, 2026-10-19.** The initial research activation was 2026-10-18.
This review concerns [REPETITION_SPECTRUM.md](REPETITION_SPECTRUM.md),
[repetition_spectrum.py](repetition_spectrum.py) and
[check_spectrum.py](check_spectrum.py). Their algebra was rederived
independently of the proof author. This is agent review, not human peer
review, formal verification, an exhaustive literature review or a novelty
claim.

The actual-cycle scanner was written by this reviewer and separately
reviewed by the coordinating agent. Its discovery and certificate counts
are distinct from the word-family checks reviewed here.

## 1. Quantifiers and exact cancellation

For fixed nonempty positive valuation words u,v and k>=1, the universal
positive-cycle statements retain **D_k>0**. No assumption about absorption
at 1 is made: the experiment uses the raw odd recurrence, including at 1.

Independently expanding the affine compositions gives

```
C_k = R C_u (Q^k-P^k)/(Q-P) + Q^k C_v,
D_k = S Q^k - R P^k,
(Q-P) C_k - C_u D_k = Q^k K,
K = (Q-P) C_v - (S-R) C_u.
```

Since D_k is odd and prime to3, its gcd with C_k is also prime to6.
It therefore divides K, without a coprimality premise on the two block
differences. For K!=0 this gives den(w_k)>=D_k/|K|. If Q>P, D_k tends
to positive infinity; every fixed reduced denominator then occurs only
finitely often in this particular family.

The sharper equality gcd(C_k,D_k)=gcd(D_k,K) requires the stated
gcd(D_u,D_v)=1 premise. A prime dividing D_k and D_u would divide D_v,
because D_k=P^k D_v modulo that prime. Thus the relevant divisor of
D_k is invertible against D_u, and the elimination identity proves the
reverse divisibility. Without that premise, the written two-sided bound
H/gcd(H,D_u) | gcd(C_k,D_k) | H is valid. The example
u=(3), v=(1,5), k=1 has C=49,D=485,K=-30 and actual gcd 1, while
gcd(D,K)=5. The shared-prime exception is exercised, not discarded.

The K=0 case is also correctly separated. Positivity of D_k forces both
block differences positive. The blocks have the same positive fixed point,
so their exact deterministic valuation itineraries repeat one common
primitive word. This gives repetition of an existing cycle, rather than
the nonzero-K cancellation bound.

## 2. Period and exact raw realizations

Removing the factors 2 and 3 from |K| gives a modulus K_0 containing every
possible cancellation divisor. The proof's period obtained modulo
K_0|D_u| is valid, because both Q and P are units there and division of
the power difference by D_u preserves divisibility by K_0.

The implementation uses a separate valid finite construction: track
(Q^k,P^k,G_k) modulo K_0 with update

```
(x,y,z) -> (Qx, Py, Pz+x).
```

Its determinant QP^2 is a unit modulo K_0. A return to the initial
state is consequently a certified period from k=0, not an assumed
eventual period. The returned period need not be least; a capped search
returns None. K_0=1 is handled separately.

For any nonempty word with D>0, each cyclic coefficient C_i is odd and
3C_i+D=2^a_i C_(i+1). Reduction removes only a common odd divisor.
Thus the primitive-denominator integer realization has exactly the
specified valuations. The code checks every arrow, closure and preservation
of the reduced denominator. The constructor deliberately retains repeated
states when the input word is a proper power; its finite counts are word
realizations, not counts of distinct primitive cycles.

## 3. Growing-height family and the two minimum counts

For m>=13, A=ceil(m log_2 3), V=3^m and U=2^A satisfy V<U<2V.
An independent mechanical-word estimate verifies the used R71 bound:
every cyclic prefix exponent differs from its ideal linear exponent by
less than 1, so every cyclic coefficient exceeds mV/6. Dividing by
Delta=U-V<V gives every pure-block state greater than m/6.

For u_m^k(2), **k>=2** suffices for the denominator conclusion. Here
K=Delta-C_u<0 and |K|<2mV/3, whereas D_k=4U^k-3V^k>V^k.
Therefore den(w)>3V^(k-1)/(2m)>1. The claim is about this family,
not all nonmechanical words or all d=1 cycles.

The stronger state and minimum claims additionally require U^k>=2V^k.
The sufficient choice k>=ceil(V/Delta) follows from Bernoulli's inequality.
Writing t=(V/U)^k and x_0=C_u/Delta, the defect-tail start is

```
x=[3x_0(1-t)+1]/(4-3t),
x/x_0 > 3(1-t)/(4-3t) >= 3/5.
```

Subsequent block starts move monotonically from x toward x_0. Every
prefix has positive slope and nonnegative intercept, so all corresponding
states exceed three-fifths of the pure-block states. Thus every normalized
rational state n/d exceeds m/10. This is a varying-denominator family;
it supplies no fixed-d counterexample.

The elementary bounds 3/2<A/m<5/3 imply digits 1/2, isolated 1s, no
cyclic 222 in u_m, and its stated end digits. The extra 2 creates exactly
one cyclic 222, proving that the new word is primitive. Its triple sums 4
and 6 also show it is not mechanical, even after rotation. The shortcut
factors 11011 and 01010 have respectively four and two 1s, so the shortcut
word is not balanced.

When all normalized states exceed 1, valuation 1 gives an increase and
valuation 2 a decrease. Cyclic pairs(2,1) therefore count the distinct
odd-only minima: k(2m-A). In the shortcut clock, each valuation 2 contributes
one descending halving run and a subsequent minimum, giving k(A-m)+1.
These counts refer to different clocks and are not interchangeable.

## 4. Corrections and finite evidence boundary

1. The draft said that D_u>0 made every k admissible. The counterexample
   u=(2), v=(1,1,1), k=1 gives D_u=1 but D_k=-49. The corrected proof
   retains D_k>0 and says only sufficiently large k are then admissible.
2. The final proof explicitly separates the all-k>=2 denominator/primitivity
   result from the extra height condition, and declares raw, nonabsorbed
   arithmetic at 1.
3. The first independent default executable replay failed: periodic-control
   words were tuples in memory and lists after JSON serialization. Writing
   the receipt could pass while exact default replay failed. The code now
   stores those words as lists. The coordinating agent regenerated the
   source-hashed receipt, and this reviewer reran the default command:
   **PASS**, without rewriting the receipt. The finite-box metadata now
   also explicitly records the Q>P restriction on u.

The declared finite box has u lengths 1..4, v lengths 1..3, valuations 1..4,
and the listed nine k values, **restricted to Q>P for u**. Negative-D_k
words are counted and skipped. It does not test every noncontracting u
covered by the general algebra. The reported counts are 239,345 positive
word realizations,6,264,270 exact odd arrows,238,328 nonzero-K bounds,
212,522 coprime exact-gcd cases,128 modular controls and 306 high-family
cases. These bounded tests support the implementation; the universal
quantifiers are supported by the written arguments above.

The accepted replay was `python3 experiments/cycle_spectrum/C001/check_spectrum.py`.
The entry point refuses optimized Python, which would remove its assertions.
Its successful default run recomputed the cases and compared the entire
result with [spectrum_audit.json](spectrum_audit.json), including both source
hashes. This is separate from the coordinator's full historical gate.

The actual d=5,7,13,61 fixtures and scan are separately retained in
[actual_cycles.json](../actual-cycles-3x-d-corpus/actual_cycles.json). No cycle search, fixed-family
denominator theorem, or successful raw-cycle constructor proves convergence
or excludes arbitrary changing-defect words.
