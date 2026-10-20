# V004 — Independent adversarial review

**Scope:** the complete argument in [kernel_route.md](kernel_route.md), with
particular attention to the elementary finish after Cobham. This is a
written mathematical review by a separate agent, not independent human
review or formal kernel verification. No novelty judgment is supplied.

**Outcome:** no mathematical gap found. The argument proves the full stated
finite-valued binary-automatic classification using Cobham as its sole
external theorem. The following are explicit checks, not agreement inferred
from finite trajectory samples.

## 1. Domain and automaticity

- A positive-integer automatic sequence can be extended by any prescribed
  value at0 while preserving automaticity: the exceptional representation
  for0 is a finite-language modification. The ordinary finite-kernel
  characterization then applies on nonnegative indices.
- Assigning h(0)=h(1) supplies no new positive-integer dynamical hypothesis.
  Every member of K+ evaluates h only at positive arguments, including at
  section index0.
- The omitted odd-source identity at1 is a value equality already forced
  by h(4)=h(2)=h(1). Its use in algebra does not restore a dynamical outgoing
  edge from the absorber or make the raw cycle through1 a counterexample.
- Every color fiber of a K+ member has both finite binary and ternary
  kernels. Cobham applies because bases2 and3 are multiplicatively
  independent. Finiteness of the output alphabet permits a common eventual
  cutoff and period for all fibers.

The positive-offset closure itself was independently checked in
[automaton_route.md](automaton_route.md). In particular the divisible-by3
case has ell<a, so its odd argument and its strict upper offset bound hold
also at n=0. No zero-offset state is silently inserted.

## 2. Eventual period becomes a global odd period

For b(n)=h(2n+1), the identity b(4n+2)=b(n) holds for every n>=0.
Let M=2^e L be an eventual period, with L odd, and G(n)=4n+2.
For fixed n>=0, choose k so both G^k(n) and G^k(n+L) are past the cutoff
and 2^e divides4^k. Both requirements can be met: G^k(n) tends to infinity
even when n=0. Their positive difference is4^k L, a multiple of M.
Repeated application of eventual periodicity therefore equates their
values. Repeated G-invariance gives b(n+L)=b(n).

This is a global period for b, including its early values. It does not
incorrectly assert that h itself is periodic before the later argument.

## 3. The residue coloring is well defined

If positive odd x,y are congruent modulo the odd L, then x-y is divisible
by2L. Hence (x-1)/2 and (y-1)/2 differ by a multiple of L. The global
period just proved defines a single q on Z/LZ with h(x)=q(x) for positive
odd x. Every residue modulo odd L has arbitrarily large positive odd
representatives.

The identities in the proof give, on all residue classes,

```
q(4x+1)=q(x),
q(3x)=q(16x+1)=q(4x).
```

The last equality is the first identity evaluated at residue4x. Although
4 times an odd integer is even, q is a residue coloring: one may use an
odd representative of residue4x. There is no application of an odd-source
dynamical identity at an even integer here.

## 4. Removing the 3-primary part

With L=3^e3 m, define H(x)=3*4^(-1)*x modulo L. The inverse of4 exists
because L is odd. The second residue identity gives q(Hx)=q(x), including
when H is not invertible.

If x=y modulo m, then

```
H^e3(x)-H^e3(y)=3^e3*4^(-e3)*(x-y)=0 modulo L.
```

Applying forward H-invariance e3 times shows q(x)=q(y). Thus q really
factors through Z/mZ. This does not assume that the multiplication-by3
map was invertible before removing its primary factor. If e3=0 the
statement is tautological, and if m=1 the proof has already finished.

## 5. The affine commutator finishes the quotient

On Z/mZ, both3 and4 are units. Let J(x)=4x+1. The descended color is
preserved by H and J, so

```
q(H(J(x)))=q(x)=q(J(H(x))),
H(J(x))=3x+3/4,
J(H(x))=3x+1.
```

Because3 is a unit, y=3x+3/4 ranges over every residue. Therefore
q(y)=q(y+1/4) everywhere. The increment1/4 is a unit modulo m, so its
additive translates exhaust Z/mZ. The color is constant. Doubling then
extends odd-input constancy to every positive integer.

No progression sufficiency theorem is needed for this elementary finish.
The earlier Monks-based finish remains a separately checked alternative.

## 6. Controls and exact consequence for actual components

For d=5 and61, h_d(n)=1_(d divides n) is a nonconstant binary-automatic
color preserved by doubling and3n+d. It fails the proof's +1 identity at
u=d: h_d(3d)=1 but h_d(16d+1)=0. At the residue-commutator stage the
corresponding increment would be d/4, which is zero modulo d. Thus the
argument exercises the relevant arithmetic distinction and does not
incorrectly exclude these control colors.

For the original map, the indicator of a union of full orbit components
obeys the stated value identities. Consequently **every nonempty proper
union of components has a nonautomatic binary indicator**. In particular,
if the nonabsorbing set is nonempty, its indicator is not binary automatic;
its complement, the basin of1, is not binary automatic either.

This neither proves the nonabsorbing set empty nor shows that its indicator
has any finite-state description. Proving automaticity of that actual
indicator would be a separate premise strong enough, together with this
theorem, to imply Collatz. It must not be presented as a routine bridge or
as a consequence of finite-depth predecessor recognition.

## 7. Recommended next objective: quantitative section complexity

An ambitious intermediate objective is to strengthen infinite-state
rigidity into a quantitative lower bound. For any finite-valued invariant
h, define

```
kappa_h(D) = #{n -> h(2^a*n+r): 0<=a<=D, 0<=r<2^a}.
```

The theorem already implies an infinite binary kernel for every
nonconstant h. An infinite kernel necessarily has kappa_h(D)>=D+1:
if the cumulative family ever stopped growing at a depth, it would be
closed under binary sections and hence finite. That elementary linear
bound should not be advertised as the next achievement.

**Proposed target:** prove that kappa_h(D)/D is unbounded for every
nonconstant Collatz-invariant finite-valued h. This would rule out even
linearly growing kernel descriptions, a strict increase in scope over
finite automata, while using the explicit bounded changes of section depth
in the new closure algebra. It is a proposed research target, not a proved
bound or an assertion about the actual bad set's growth.

The proposed objective assumes no regularity of an actual component
indicator. Its conditional consequence would be a stronger complexity
requirement on any hypothetical separation of components. No investigation
or implementation of this next objective was performed for this review.
