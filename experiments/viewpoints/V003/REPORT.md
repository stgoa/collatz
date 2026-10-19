# V003 — What arithmetic regularity has gained

**Historical snapshot:** the open classification below was subsequently
proved in [V004](../V004/GLOBAL_RIGIDITY.md). The V003 results and scoped
counterexamples remain valid; its completion used the earlier partial-result
criterion, not the later strict full-classification goal.

**Standing, 2026-10-18:** a partial classification and two structural lemmas
have written, independently agent-reviewed proofs. Full classification of
binary-automatic invariant colorings remains open here. No novelty, human
peer review, formal verification or Collatz convergence is claimed.

The [active brief](../briefs/ARITHMETIC_REGULARITY_BRIEF.md) asks how
complicated a rule separating Collatz components must be. V002 supplied
periodic rigidity. This batch investigates the larger binary-automatic
class and delivers results beyond that periodic case.

## 1. A complete classification by binary digit count

Let s_2(n) count the 1s in the binary expansion of n. For **any** function
F on positive integer weights, with any output set, suppose

```
h(n)=F(s_2(n)),
h(3n+1)=h(n) for every positive odd n>1.
```

Then F is constant. Doubling invariance is automatic. The
[proof](digit_sum.md) constructs odd inputs joining every adjacent weight
from 4 onward, and three small inputs join weights 1 through 4.

This simultaneously classifies every binary-automatic coloring
`G(s_2(n) mod m)`, for every m and every output map G. That family includes
nonperiodic descriptions such as digit-sum parity, so the result goes beyond
the periodic baseline. Positional and pattern information in the bits remain
outside this theorem. No hypothetical nonabsorbing indicator is assumed to
belong to the class.

## 2. The first ternary image has only one possible new function

Now let h be finite-valued and satisfy both identities in the brief. Extend
h(0)=h(1) only for the standard kernel convention. Write

```
K = {n -> h(2^a*n+r): a>=0, 0<=r<2^a},
T_j f(n)=f(3n+j), j=0,1,2,
f_t(n)=h(3^t*n).
```

Assume K is finite, equivalently binary automaticity. The
[kernel proof](kernel_probe.md) establishes

```
T_1 h(n)=h(4n+1),       T_2 h(n)=h(2n+1),
T_j(K) subset K union {f_1} for all j,
|{f_t:t>=0}| <= |K|.
```

The first inclusion concerns **every binary-kernel state**, at every binary
depth. Its proof retains the affine offset and odd-source guard. The second
bound follows because the odd section of every f_t is a member of K and
doubling invariance determines the function from that section.

Thus the unknown first ternary images have been reduced to one function,
and repeated zero ternary sections form a finite family. This is a genuine
reduction of the closure obligation. It neither makes f_1 a member of K nor
bounds all iterated mixed ternary sections.

For `b_t(n)=f_t(2n+1)`, define `u_t=T_1 f_t`, `v_t=T_2 f_t`. Their binary
sections obey

```
u_t(2n)=T_0 b_t(n),    u_t(2n+1)=v_t(n),
v_t(2n)=u_t(n),        v_t(2n+1)=T_2 b_t(n).
```

The boundary functions belong to `K union {f_1}`. These relations provide
a finite binary presentation of each pair; closure under further ternary
sections is still missing. A proposed closure must supply one finite family
stable under all three T_j, with equality of entire sequences.

## 3. An exact obstruction to dropping the guards

The [scaling counterexample](literature.md#l6-two-scaling-invariances-do-not-imply-periodicity)
is the binary-automatic function

```
g(n)=+1 if oddpart(n)=1 or3 mod8,
g(n)=-1 if oddpart(n)=5 or7 mod8.
```

It satisfies `g(2n)=g(3n)=g(n)`. Every pure-zero ternary section is therefore
the same function. Nevertheless it is not eventually periodic, and its
sections `g(3^t n+1)` for t>=1 are pairwise distinct. The note gives exact
integer witnesses separating every pair, without relying on a finite scan
or on Cobham's theorem.

The full Collatz guard excludes this example: g(3) differs from g(10).
Consequently the counterexample refutes only a scaling-based completion of
the argument. It identifies the information that must survive further work:
the guarded additive identity and its effect on mixed sections.

## 4. Literature and complementary test

| Investigation | Established outcome | Decision |
|---|---|---|
| [Primary literature](literature.md) | Fixed-depth predecessor languages are regular; the whole basin is not covered. Cobham requires two actual base descriptions. A characteristic-zero 3-Mahler equation would be another sufficient input. | Keep these as precisely conditional interfaces. No exact single-base classification was located in this bounded search; novelty is undetermined. |
| [Monochromatic cylinders](cylinder_rigidity.md) | One constant dyadic section forces an invariant coloring to be constant. At d=1 this is already covered by published arithmetic-progression sufficiency. | Use the known restriction; do not count its rederivation as a new result. |
| [Complete carry frontier](carry_boundary.md) | The conversion of ternary 12 to binary 101, with bootstrap and carries, yields 3*5+1=16. Removing the internal cells recovers existing affine/section data. | Stop this V14 test. Reopen only with an additional relation between entire frontier families. |

The source notes distinguish directly inspected theorem statements from
abstract-only leads. The new elementary arguments have no established
novelty claim. The carry example has three division sweeps, four shortcut
Collatz arrows, one odd-only arrow and five horizontal digit transitions;
none is substituted for a parallel-update count.

## 5. Known-cycle controls

Use the absorbed odd map `S_d(n)=(3n+d)/2^v2(3n+d)` for odd n>1 and
`S_d(1)=1`. For d=5 and61, `1_(d divides n)` is a nonconstant periodic
invariant: doubling preserves divisibility, and `d | (3n+d)` iff `d | n`
because gcd(d,6)=1. This remains true with absorption at 1.

| Claim | What the controls exercise |
|---|---|
| Digit-count classification | The +1 proof is map-specific. The d=5 invariant distinguishes 3 and5, both with two 1s; the d=61 invariant distinguishes 31 and61, both with five 1s. They fail the digit-count hypothesis. |
| First-image and pure-zero identities | The displayed offsets use +1. Replacing it by +d changes the equations. Even finite two-base closure would leave nonconstant periodic colors at these d. |
| Monochromatic-cylinder rigidity | The written proof transfers to positive odd d coprime to3. Each dyadic class contains both divisibility colors by CRT, so these controls obey its hypothesis restriction. |
| Scaling counterexample | It disproves the explicitly weaker hypotheses at d=1; it fails the full guarded Collatz identity at an exhibited source. |
| Carry picture | The d=5 arithmetic cycle is an external check on proposed convergence inferences. No d=5 tile system or generalized bootstrap has been verified. |

The standalone verifier replays actual absorber-avoiding cycles and checks
the claims' arithmetic fixtures. Cycle replays alone are not new theorems,
and these controls do not settle hypothetical divergence.

## 6. Recommendation

**Deepen V13 through a bounded mixed-section investigation.** It has supplied
an infinite-class theorem and reduced the closure problem. The next work
should preserve the full guarded relations while treating the families
`T_1 f_t`, `T_2 f_t` and their iterates. State a proposed finite closure
explicitly before testing it. Alternatively, seek a finite 3-Mahler relation
for each color indicator, retaining every auxiliary series.

The discrimination criterion is an additional relation or a rigorous bound
on these mixed families. Pure-zero periodicity, repeated affine-subsequence
automaticity, or finite-state catalogues cannot meet it. If the next bounded
probe adds no such relation, compare the separate V12 statistical target
before further depth. V14 has reached its stop condition.

This batch demonstrates a mathematical gain from the selected language.
The principal binary-automatic classification remains a subsequent research
target, and the regularity of an arbitrary component indicator remains an
entirely separate missing premise.

## Evidence

- [Independent proof review](PROOF_REVIEW.md).
- [Executable arithmetic checks](verify_examples.py) and [receipt](verification.json).
- [Read-only side-lane assessment](side_review.md).
- [Goal completion audit](GOAL_REVIEW.md), with delivery evidence in the
  [viewpoint log](../LOG.md).

The finite checks accompany the written proofs; they do not prove their
unbounded quantifiers. R1–R94 and all historical mathematical evidence are
preserved. The new results use a separate V003 record.
