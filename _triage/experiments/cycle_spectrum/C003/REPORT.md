# C003 — Denominator restrictions uniform over changing blocks

**2026-10-19. Progress: written theorems, independently agent-reviewed,
with exact finite checks. The all-cycle headline remains open.**

This batch asks whether C002's denominator restriction survives when
the two valuation blocks have different lengths, totals and slopes.
It does: the blocks may vary freely in both results below. Neither
result asserts that arbitrary cycle words have the required repetition.
No novelty or formal-verification claim is made.

## 1. A uniform finiteness theorem for two repeated blocks

Let u,v be nonempty words of positive odd-step valuations and
`w=u^k v^ell`, with k,ell>=2. Write

```
A=sum(w), M=len(w), D_z=2^sum(z)-3^len(z),
C_z=sum_j 3^(len(z)-1-j)*2^(sum of entries before j),
K=D_u*C_v-D_v*C_u,
den(w)=(2^A-3^M)/gcd(C_w,2^A-3^M).
```

Assume `2^A>3^M` and K!=0. For every epsilon>0 there is a threshold,
**independent of u,v,k,ell**, above which

```
den(w) >= 2^((eta-epsilon)*A),
eta=(5*log_3(2)-3)/14=0.0110463406...>0.
```

Consequently, every bounded denominator layer contains only finitely
many such representations, even when both words vary. The threshold
is ineffective: this argument does not identify or eliminate all the
possible denominator-1 exceptions below it.

The [proof](UNEQUAL_PROBE.md) has two branches. Unequal block slopes
give the stronger lower rate `log_3(2)/2=0.3154648768...`. One fixed
group of rational 2/3-units permits the Corvaja–Zannier gcd estimate
uniformly over all blocks. A global power-gap estimate controls
`2^A-3^M`, even near the positivity boundary. For proportional slopes,
the exact shared factor is retained, and the elementary inequality

```
5*(R*k+S*ell-gcd(R*k,S*ell)+1) >= 7*(R+S)
```

for coprime R,S and k,ell>=2 gives the positive rate above. All imported
estimates, local terms and exceptional sets are explicit in the proof.

K=0 is essential: powers of a common primitive cycle retain their
denominator indefinitely. This includes the actual denominator-1, 5,
7 and 13 controls. The theorem cannot exclude that branch by assumption.

## 2. An effective exclusion at every size for contracting blocks

Suppose K!=0 and both blocks contract: D_u,D_v>0. Let
`Q_*=max(2^sum(u),2^sum(v))`, `m_*=max(len(u),len(v))`.
If a block attaining Q_* occurs t_*>=3 times, and the other occurs
at least once, then

```
den(u^k v^ell) > 2^m_* * Q_*^(t_*-3) >= 2^m_* > 1.
```

This [elementary proof](PROPORTIONAL_UNIFORM.md) has no ineffective
cutoff. Its two ingredients are real interval trapping of block starts
and integer lattice spacing after scaling by the cycle denominator.
It also gives an effective enumeration bound for each bounded
denominator layer within its hypotheses. Lengths, totals and slopes
need not agree; the other repetition count can be one.

For example, `(1,2,2)^3(2)` has C=213341, D=72023, gcd 1. Both
blocks contract, and the uniform lower bound is 8.

## 3. The expanding-block obstruction is real

The stored d499 cycle admits the representation
`u=(1), k=4, v=(1,3), ell=3`. Here

```
D_u=-1, C_u=1, D_v=7, C_v=5, K=-12,
C_w=85865, D_w=6487, gcd(C_w,D_w)=13,
den(w)=499, starting integer state=6605.
```

The pure block fixed points are -1 and 5/7. The mixed rational cycle
starts at 6605/499, outside their interval. Thus the positive interval
trapping used in Section 2 fails for this actual cycle. This refutes
that extension of the proof mechanism; it does not refute a possible
denominator inequality with a different proof. Section 1 still applies
asymptotically to this structural class.

A separate draft example `(1)^3(2)^5` was corrected before delivery:
C=10865, D=1631, gcd 1. The incorrect draft arithmetic was reported
and is documented in the [independent review](INDEPENDENT_REVIEW.md).
No historical result was changed.

## 4. Exact finite evidence and its limits

The [checker](check_variable_blocks.py) recomputes the saved
[receipt](variable_blocks_audit.json) by default; `--write` is the
explicit regeneration mode. It rejects optimized Python and unknown
arguments. The checks use raw odd-only cycles, without absorbing at 1.

| Check | Scope |
| --- | --- |
| Actual cycle source | 2,459 stored cycles over 333 parameters from C001; every raw arrow replayed. |
| Rotations and decompositions | All 36,912 rotations; 1,694,160 exact power decompositions. Rotations are not additional primitive cycles. |
| Contracting inequalities on actual data | 1,256,140 exact commutator checks and 2,512,280 lattice-height checks. |
| Strong all-size theorem on actual data | **Zero eligible decompositions.** This part of the actual sample is vacuous. |
| Generated grid | 84 words of lengths 1–3 and entries 1–4; all ordered pairs and counts 1–6: 254,016 cases. |
| Positive generated realizations | 243,878 at 2,741 reduced denominators; 4,650,456 exact odd arrows. These are not all distinct primitive cycles. |
| Strong contracting bound | 153,696 eligible checks; 90,912 checks of the both-counts-at-least-three maximum-length bound. |
| Proportional refinement | 23,696 actual and 25,056 generated exact checks. |
| Coprime integer lemma | 78,287 cases with R,S<=32 and k,ell<=12; the sharp equality is retained. |
| Common-cycle controls | 3,384 positive generated K=0 cases retained. |

No finite test verifies the imported asymptotic estimates. A deliberately
stronger all-size exponent diagnostic, testing for `den^16<2^(5A)`,
found no failures in 154 actual
and 150,622 generated unequal-slope decompositions. Its absence of
counterexamples does not remove the ineffective cutoff. The actual
mixed-direction cases with both counts at least three are four
representations of the same d499 cycle described above.

The fresh root replay, historical gate and preservation checks are
recorded in [delivery_checks.json](delivery_checks.json) and
[full_gate.json](full_gate.json). The [root review](ROOT_REVIEW.md)
distinguishes code checks, written proof and published inputs.

## 5. What this changes, and what to aim for next

C003 removes the fixed-catalogue limitation for this two-block class.
It achieves a scoped denominator theorem under the existing success
ladder. The all-size contracting theorem covers additional unequal-total
classes beyond C002's equal-total exclusion; C002 also covers repetition
counts (1,2), outside this new theorem. These classes can have unbounded internal word
complexity and unbounded numbers of local minima; that is distinct from
improving a published bound for *every* cycle with a given minima count.
The limited literature comparison in C001–C002 establishes no general
record or novelty claim.

The next mechanism should target a restriction intrinsic to arbitrary
cycle words, connecting their denominator to the sizes of their rotated
cycle points. Merely increasing the number of repeated motifs would
leave the structural gap. An effective treatment of the mixed-block
finite exceptions is a useful secondary target, but would still be a
subclass result. The [side review](SIDE_REVIEW.md) audits the new size
proposal and the reported Lean work. Neither is an assumed premise.

| Required field | Outcome |
| --- | --- |
| Objects | Positive rational cycle words, their reduced denominators, repeated blocks and all rotated cycle states. |
| Structural gain | Uniform finite bounded-denominator layers for nondegenerate two-square representations; effective nonintegrality under the contracting repetition condition. |
| Translated unresolved gap | Arbitrary words need not have these repetitions; general thresholds are ineffective; K=0 remains essential. |
| Worked examples | Unequal contracting blocks give denominator 72023; the actual d499 mixed pair breaks interval trapping. |
| Known-cycle controls | Actual d5/7/13 cycles, K=0 repetitions, and the raw state-1 convention are retained. |
| Cheapest meaningful next test | Test a rotation-invariant size/residue constraint on every actual cycle, requiring an explicit inequality or exact obstruction. |
| Intermediate milestone | A denominator restriction for words with unrestricted internal structure, with a stated conclusion stronger than the defining cycle identity. |

The headline remains exclusion of all nontrivial integer cycles.
Divergence remains a separate unresolved part of Collatz.
