# V009 — Unbounded additive excess and a global detection bound

**Progress; the full quantitative goal remains active and unresolved.**
V008 was delivered at `9d66b69b1e9dc9413e73a0ff569972fd38feade7`.
This batch uses the hypothetical cumulative linear bound directly and
compares it with a separate diagnostic for near-minimal binary growth.
The return analysis proves an unbounded additive improvement over the
generic bound. This does not supply the unbounded ratio required by the
goal. Final independent audit of that argument is recorded separately.

## 1. Linear growth imposes a quantitative detection bound

Let J_D(s) be the whole mixed binary/ternary section family through total
depth D, and W_D its real linear span. The [new elementary theorem](global_growth.md)
proves the following implication, for every fixed C>=1:

```
|J_D(s)|<=C(D+1) for all D
    => every nonzero g in W_A is detected before input 9^L,

L=ceil(2C+sqrt(2C(A+1))+1).
```

Thus at most O_C(sqrt(A+1)) binary or ternary input digits detect every
nonzero linear combination of depth-A states. This is stronger than
pairwise distinguishability. It is a proved prefix test under a stated
all-depth hypothesis, not an inference of whole-function equality from
a finite sample.

The mechanism is exact. If g first becomes nonzero at N>=9^L, sectioning
along each multiplier m=2^a3^b with a+b<=L moves that first nonzero
coordinate to floor(N/m). The resulting indices are distinct. Their
triangular ordering gives (L+1)(L+2)/2 linearly independent functions
inside W_(A+L). This contradicts the assumed linear bound when L is
chosen as above. All offsets lie in their declared cylinders, and the
endpoint N=9^L is retained.

This gives a concrete route to the **full** goal: construct nonzero
combinations g_j in W_(A_j)(b), b(n)=h(2n+1), with

```
log(nu(g_j))/sqrt(A_j+1) unbounded,
```

where nu is the first nonzero input. Their independent mixed sections
would force an unbounded joint ratio and then an unbounded binary ratio
through the existing exact depth conversion. The missing step is to
produce these delays from arbitrary nonconstancy and the full Collatz
identities. No such construction is supplied here.

## 2. Why the new bound is not already a contradiction

An infinite finite-alphabet joint kernel has strictly increasing span
dimension: a rank plateau would make the finite-dimensional span closed
under all section maps, and only finitely many finite-alphabet sequences
can lie in that space. Hence dim W_A>=A+1.

That rank count alone gives a nonzero combination vanishing at only A
initial inputs. The detection bound permits much longer zero prefixes,
of size exponential in sqrt(A). An additional arithmetic mechanism is
essential. The calibration in the proof note recovers the existing
digit-count quadratic phenomenon by constructing exponentially delayed
combinations; it does not assume every invariant has such a section.

## 3. The smallest-growth diagnostic is excluded

The independent [binary-ray analysis](binary_tail.md) assumes the narrower
bound kappa_h(D)=D+O(1). It is equivalent to exactly one new binary state
q_n at each sufficiently large depth n. All returns to previous states
are retained.

The maximal ternary depth increment stabilizes, and the exact radix
equations make its reaching digit and the forward binary digit unique
and eventually periodic. A contraction argument excludes every constant
escape pattern, including the whole increment-two case. Rational
coordinates then leave only two maximal-transition patterns, up to phase:

| Ternary increment | Binary escape word | Ternary escape word |
| --- | --- | --- |
| 3 | 1100 | 1012 |
| 4 | 110111001000 | 222101000121 |

These words describe transitions reaching the largest possible depth.
The proof then controls all other transitions. The nonescaping binary
children obey an exact periodic sequence of ternary maps. Formal rational
coordinates for their digits have an even denominator; maximal transitions
have coordinates with odd denominator. This forces a nonmaximal move in
every fixed-length return block and gives a strict gain in depth.

Radix commutation upgrades that gain: every nonmaximal ternary edge
contracts depth by one fixed factor less than1, up to an additive constant.
Repeated return blocks then stay in a finite set. Including their phases
makes the return sequences periodic, and induction on actual integer
inputs forces two entire q_n states equal. This contradicts their distinct
minimum depths. Every jump into the finite earlier set is retained.

Consequently, for every nonconstant finite-valued Collatz invariant,

```
kappa_h(D)-(D+1) -> infinity.
```

This is a universal additive gain beyond the generic infinite-kernel
argument. It still permits growth such as D+sqrt(D), and therefore proves
neither a fixed fractional improvement nor the active unbounded ratio.

## 4. Comparison and next action

| Mechanism | What this batch proves | What must still be supplied |
| --- | --- | --- |
| Global count and linear combinations | Explicit short detection under every fixed linear coefficient | Nonzero combinations with delays exceeding that bound, from full Collatz invariance |
| Near-minimal binary graph | All eventual one-state binary tails excluded, giving unbounded additive excess | Extension to growth allowing recurrent layers with several states |
| Pure dimension counting | Rank increases at every depth in an infinite finite-alphabet kernel | A reason for long zero prefixes; rank alone supplies only a linear delay |

Compare the global detection route with the now proved return-contraction
mechanism. Test the scalar equations for delayed nonzero combinations,
and identify which contraction steps can handle several states per layer
without assuming bounded layer sizes from cumulative growth. A formally
cancelled expression that is identically zero is not a witness. Periodic
escape digits alone do not prove periodicity of entire states: the return
analysis is essential. No regularity is assumed for the actual nonabsorbing set.

## 5. Verification and preservation

The [global review](GLOBAL_REVIEW.md) checks the affine substitutions,
strict pivot separation, linear independence, explicit cutoff and
finite-alphabet rank argument. The [additive review](ADDITIVE_REVIEW.md) checks
the full radix constraints, finite earlier-state exceptions, contraction
and rational-coordinate classification, followed by the full return-block
contraction. Root independently checked these arguments and the two
displayed words. This is written proof with agent
review; novelty, human peer review and formal verification are unclaimed.

The generic detection theorem imports no external theorem. The tail's
Collatz application uses the existing two-base infinitude argument and
therefore imports Cobham through V004. The [side review](side_review.md)
records the newly fetched formalization report without claiming a main
replay. Known d5/d61 periodic controls fail the infinitude premises and
have no unbounded-delay witness.

This is a prose-only mathematical batch. Frozen R1–R94, dispatcher code
and evidence, and the open LaTeX document are preserved. Local links,
source hashes and frozen comparisons are recorded in the delivery checks;
the unrelated historical finite gate is not rerun.
