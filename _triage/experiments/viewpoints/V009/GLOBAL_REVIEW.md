# V009 — Independent review of the first-nonzero growth argument

**Status: independent written-argument audit passed.** This review inspected
the actual `global_growth.md`, Sections 1–8. It checks the generic affine
theorem and its calibration. It is not formal verification, a novelty
claim, or a proof of the active Collatz growth goal. No executable evidence
or historical result was changed.

## 1. Main lemma: quantifiers, endpoints, and independence

The claim is valid for every real-valued sequence s, integers A,L>=0,
and nonzero entire sequence g in W_A(s), provided its first nonzero
index N satisfies N>=9^L. No finite alphabet, invariance, or infinite
kernel is needed here.

For each multiplier m=2^a 3^b with a+b<=L, the selected residue
r_m=N mod m lies in the declared residue range. The section
g(mn+r_m) is zero at every index below floor(N/m) and nonzero at
that index. Thus its first nonzero index is exactly floor(N/m).

Distinct pairs give distinct multipliers by unique factorization. For
two distinct multipliers m,m'<=3^L, their product is strictly less
than 9^L, including when one is the largest multiplier. Therefore
N|m-m'|/(mm')>1 even at the endpoint N=9^L. Their integer-part
pivots are distinct. At L=0 only one multiplier occurs, so no pairwise
estimate is needed.

Sectioning a state s(Mn+t) by this residue gives
s(Mm n+M r_m+t), with 0<=M r_m+t<Mm and total exponent depth
at most A+L. Hence all selected sequences belong to W_(A+L).
Sorting their distinct first nonzero indices makes the evaluation
matrix triangular with nonzero diagonal. The asserted lower rank
(L+1)(L+2)/2 follows for entire sequences.

## 2. The linear-growth consequence and explicit constants

The hypothesis is one constant C>=1 bounding |J_D(s)| by C(D+1)
for **every** integer D>=0. Applying it at the shifted depth A+L
is essential and is done explicitly. The least integer L_C(A) with
Q_L>C(A+L+1) exists, and contradiction with the lemma proves
nu(g)<9^L_C(A) for every nonzero g in W_A(s).

Consequently evaluations at inputs 0 through 9^L_C(A)-1 are
jointly injective on the whole vector space. The strict cutoff, the
number of coordinates, and the difference-of-states application agree.
This is stronger than a pairwise state test and does not infer equality
from an unproved finite-prefix heuristic.

The explicit integer

```
Lhat=ceil(2C+sqrt(2C(A+1))+1)
```

satisfies the needed strict quadratic inequality. All factors in the
displayed estimate are positive, and Q_L>=L^2/2 suffices. It follows
that the detecting input has at most 2Lhat ternary digits or
ceil(Lhat log_2 9) binary digits. The zero input is correctly treated
by the empty word; extra most-significant zero digits preserve output
in an actual section graph. The constant implicit in the square-root
word bound may depend on C and does not remain fixed as C varies.

## 3. Sufficient contradiction criterion and Collatz transfer

Without any growth assumption, a nonzero g_j in W_(A_j) with
N_j=nu(g_j)>=1 permits L_j=floor(log_9 N_j). The triangular
bound at A_j+L_j gives the displayed ratio estimate. Unbounded
L_j^2/(A_j+L_j+1) is therefore a sufficient condition for unbounded
joint growth ratio. The stated simpler condition
log(N_j)/sqrt(A_j+1) unbounded does imply it: either L_j<=A_j+1,
when the denominator is at most 2(A_j+1), or L_j>A_j+1,
when it is less than 2L_j.

The existing inclusion J_D(b) in K^+_(1+4D)(h) yields
kappa_h(1+4D)/(4D+2)>=|J_D(b)|/(4(D+1)), as written. Thus
an unbounded joint ratio would establish the requested unbounded
binary ratio. The document correctly does not claim to construct the
necessary nonzero delayed combinations from arbitrary invariant h.

## 4. Finite alphabet, rank, and the dimension-count limitation

For a d-dimensional space of entire sequences, the coordinate
evaluations span its dual: otherwise a nonzero vector annihilated by
every coordinate would exist. Selecting d independent evaluations
therefore embeds its sequences into R^d. A fixed q-element alphabet
permits at most q^d such sequences in that space.

If W_(D+1)=W_D, each of the five section maps preserves W_D, so
all future sections remain in this finite-dimensional space. The
finite-alphabet count then makes the whole kernel finite. Consequently
an infinite finite-alphabet joint kernel has strictly increasing rank
at every depth, starting at one, and d_A>=A+1.

The nullspace argument supplies a nonzero g vanishing at the first
d_A-1 coordinates. It guarantees only nu(g)>=d_A-1, not a delay
exponential in sqrt(A). The document preserves that gap. It also
correctly distinguishes this cyclic space from a full operator algebra
or transformation semigroup.

## 5. Calibration and controls

- **Pairwise tests versus span tests.** For N>=2, delta_0, delta_1,
  and delta_0+delta_1+delta_N are binary-valued and pairwise separated
  at inputs 0 or 1; their displayed linear combination is delta_N.
  Interleaving them and zero in the four classes modulo 4 realizes
  them as actual binary sections. The sequences have finite support;
  no uniform growth constant in N or invariant status is asserted.
- **Digit-count calibration.** A linear dependence among
  F(t+s_2(n)), 0<=t<=A, would yield a fixed linear recurrence for F,
  since s_2 attains every nonnegative integer. Solving for its last
  nonzero coefficient makes finite output blocks evolve
  deterministically, so F would be eventually periodic. Thus the
  independence claim is valid. Imposing A homogeneous conditions at
  weights 0,...,A-1 leaves a nonzero combination; its first nonzero
  integer is at least 2^A-1. This gives the claimed quadratic joint
  lower bound at depths of order A. At A=1 the allowed L_A is zero,
  which is consistent with the lemma; the quadratic conclusion is
  asymptotic as A grows.
- **Scope.** Periodic generalized-map colorings have finite kernel
  and admit no unbounded-delay sequence inside a fixed finite span.
  The V008 two-exit example already has quadratic joint growth. These
  controls do not challenge the theorem or establish a contradiction
  for an arbitrary nonconstant Collatz invariant.

## 6. Outcome

No mathematical gap was found in the inspected argument. Its precise
gain is a proved necessary detection bound under any cumulative linear
joint-growth constant. The missing full-class step is still the
construction of nonzero low-depth combinations whose first nonzero
inputs exceed that bound. The active unbounded-ratio goal remains open.
