# V009 — Linear joint growth forces short distinguishing inputs

**Status: written generic affine theorem and scoped reductions; independent
[review passed](GLOBAL_REVIEW.md).** The theorem below uses the cumulative growth hypothesis
at its actual strength and preserves entire affine sections. It supplies
a quantitative restriction on any proposed linear-growth invariant, but
does not prove that such an invariant cannot exist. The active target
remains the full unbounded ratio in
[the quantitative brief](../../../../archive/invariants-viewpoints/briefs/QUANTITATIVE_RIGIDITY_BRIEF.md).

## 1. Setup and the new restriction

For a real-valued sequence s on the nonnegative integers define

```
J_D(s)={n -> s(2^a 3^b n+r):
        a,b>=0, a+b<=D, 0<=r<2^a 3^b},
W_D(s)=span_R J_D(s),
d_D(s)=dim_R W_D(s).
```

The span is a space of entire sequences. It is not a span of a finite
sample matrix. Any finite set of output colors may be injectively encoded
as real numbers when applying this to an invariant. That encoding
preserves which entire section functions are equal.

For a nonzero sequence g write

```
nu(g)=min{n>=0:g(n)!=0}.
```

**Main consequence.** Suppose, for one constant C>=1,

```
|J_D(s)| <= C(D+1)            for every integer D>=0.          (1)
```

For every A>=0, evaluation at an explicitly bounded finite prefix is
injective on the entire space W_A(s). The required inputs have at most
`O_C(sqrt(A+1))` digits in either base 2 or base 3. This applies to linear
combinations of states, which is stronger than just distinguishing pairs
of states. The exact constants follow below.

The argument is generic for actual affine sections. Neither the three
Collatz root equations nor two-base infinitude is assumed in its proof.
Those additional hypotheses must supply a contradiction with this
restriction if it is to complete the active goal.

## 2. Transporting the first nonzero value

**Lemma.** Let A,L>=0 be integers and let `0!=g in W_A(s)`. If

```
nu(g) >= 9^L,
```

then

```
d_(A+L)(s) >= (L+1)(L+2)/2.                            (2)
```

**Proof.** Put N=nu(g). For every pair a,b>=0 with a+b<=L, let

```
m=2^a3^b,     r_m=N mod m,
g_m(n)=g(mn+r_m).
```

All multipliers m are distinct, by unique factorization, and m<=3^L.
The first nonzero value of g_m occurs exactly at

```
nu(g_m)=floor(N/m).                                    (3)
```

Indeed the argument is N at that index and is strictly smaller at every
earlier nonnegative index. Thus g_m is nonzero.

For distinct m,m'<=3^L, their product is strictly smaller than 9^L.
Consequently

```
|N/m-N/m'| = N |m-m'|/(mm') > 1.
```

The integer parts in (3) are therefore distinct. When L=0 there is only
one multiplier and no pairwise comparison is needed. The strict product
inequality handles the endpoint N=9^L without a lost unit.

Each g_m belongs to W_(A+L)(s). To check this directly, write g as a
linear combination of states `s(Mn+t)` from J_A(s), where
`M=2^i3^j`, i+j<=A, 0<=t<M. Its corresponding m-section is

```
s(Mm n+M r_m+t),
```

where `0<=M r_m+t<Mm` and the total exponent depth is at most A+L.
No coefficient, residue, or shift outside the declared section family
is being suppressed.

Finally, sequences with distinct first nonzero indices are linearly
independent. Sort them by those indices. In a vanishing linear
combination, evaluation at the smallest first nonzero index kills all
later terms and forces the earliest coefficient to vanish. Continue
inductively. There are `(L+1)(L+2)/2` multiplier pairs, proving (2).

## 3. Exact prefix and word-length bounds under linear growth

Write `Q_L=(L+1)(L+2)/2` and define the integer cutoff

```
L_C(A)=min{L>=0: Q_L > C(A+L+1)}.                     (4)
```

This finite minimum is well defined because Q_L is quadratic in L.
Assumption (1) and Lemma (2) imply that every nonzero g in W_A(s)
satisfies

```
nu(g)<9^(L_C(A)).                                    (5)
```

Otherwise (2) would give
`Q_L<=d_(A+L)<=|J_(A+L)|<=C(A+L+1)`, contrary to (4).

Equivalently, the linear evaluation map

```
W_A(s) -> R^(9^(L_C(A))),
g -> (g(0),...,g(9^(L_C(A))-1))                       (6)
```

is injective. This is a theorem about whole functions: the prefix is
proved sufficient under the all-depth hypothesis (1), rather than taken
as an empirical equality test.

A convenient explicit, slightly larger cutoff is

```
Lhat_C(A)=ceil(2C+sqrt(2C(A+1))+1).                   (7)
```

It satisfies the strict inequality in (4). To verify it, put
`x=sqrt(2C(A+1))`; then Lhat>=2C+x+1, so

```
Lhat^2/2-C*Lhat = Lhat(Lhat-2C)/2
              >= (2C+x+1)(x+1)/2
               > x^2/2 = C(A+1).
```

Since Q_L>=L^2/2, this proves `L_C(A)<=Lhat_C(A)`.
In particular Lhat is at most `2C+sqrt(2C(A+1))+2`.

For distinct states f,g in J_A(s), their difference belongs to W_A(s).
By (5) some input n with `0<=n<9^L` distinguishes them, where
L=L_C(A), or the explicit Lhat may be used. This n has at most

```
2L ternary digits,
ceil(L log_2 9) binary digits.                       (8)
```

The input n=0 is read by the empty word. Leading zeros may be appended
because the true section graph preserves the output at zero. The same
word-length conclusion applies to detecting a nonzero linear combination,
not merely to distinguishing two individual vertices.

## 4. What would turn this into the full growth contradiction

Lemma (2) can be used without assuming (1). Suppose there is a sequence
of nonzero functions g_j in W_(A_j)(s), with first nonzero inputs N_j,
and let

```
L_j=floor(log_9 N_j),          N_j>=1.
```

Then

```
|J_(A_j+L_j)(s)|/(A_j+L_j+1)
 >= (L_j+1)(L_j+2)/(2(A_j+L_j+1)).                   (9)
```

Thus it would suffice to produce such functions with

```
sup_j L_j^2/(A_j+L_j+1)=infinity.                   (10)
```

For example, delayed nonzero values with
`log(N_j)/sqrt(A_j+1)` unbounded would suffice. If A_j stays bounded
while the delay becomes arbitrarily large, the same displayed criterion
applies, although a fixed finite-dimensional W_A in fact precludes such
an unbounded delay.

For an invariant, take s=b, where b(n)=h(2n+1). The existing exact depth
bound is `|J_D(b)|<=kappa_h(1+4D)`. Consequently an unbounded ratio in
(9) would imply the active unbounded binary ratio, since

```
kappa_h(1+4D)/(4D+2) >= |J_D(b)|/(4(D+1)).           (11)
```

The unresolved step is to construct the delayed differences or linear
combinations in (10) from the **full** Collatz identities and
nonconstancy. No such construction is provided here. Two-base infinitude
alone has not supplied it in this bounded pass. Criterion (10) is a
sufficient route to the existing target, not a substitute goal or a
regularity assumption on the actual nonabsorbing set.

## 5. Why a dimension count does not already supply the delay

There is a useful exact preliminary reduction. A d-dimensional space
of entire sequences admits d coordinate evaluations that are jointly
injective: coordinate evaluations separate vectors, so they span the
dual of the space, from which a basis can be selected. Therefore it
contains at most `q^d` distinct sequences taking values in a fixed
q-element alphabet.

It follows that a finite-dimensional span of the whole joint kernel
would make that kernel finite. Moreover, if
`W_(D+1)(s)=W_D(s)` at some depth D, then W_D is preserved by all five
section maps. Every later section lies in this same finite-dimensional
space, and the finite-alphabet observation again makes the whole kernel
finite. For an infinite finite-alphabet joint kernel, therefore,

```
d_A(s)>=A+1.                                        (12)
```

The starting rank is one, since an infinite kernel cannot start with the
identically zero sequence. At each depth the rank must strictly increase.

Pure linear algebra then supplies a nonzero member of W_A vanishing at
the first `d_A-1` coordinates, by solving that many homogeneous equations
in d_A unknown coefficients. But this only guarantees

```
nu(g)>=d_A-1>=A,
```

which is far below the forbidden threshold in (5). A linear dimension
and the existence of an irrational or absent density do not upgrade
this to an exponential delay. Under (1), (12) merely places d_A between
two linear bounds. Importing a theorem about the growth of a full
transformation semigroup or operator algebra would again change the
object: W_A is a cyclic space generated from one sequence.

Likewise the word bound (8) grows with A. It does not give one fixed
finite collection of tests for all reachable states, and hence does not
give an automatic section. Finite-alphabet counting is consistent with
O(A) states distinguished by `O(sqrt A)` digits; the number of possible
output patterns on those tests is vastly larger than A. Whole-function
equality is not replaced by a graph-limit or prefix-compactness argument.

## 6. Checks on the mechanism

### 6.1. Pairs of states are not the whole span

For any N>=2 let delta_j be the indicator sequence of the singleton {j}.
The three binary-valued sequences

```
f_0=delta_0,
f_1=delta_1,
f_2=delta_0+delta_1+delta_N
```

are pairwise distinguishable already at input 0 or 1. Yet
`f_2-f_0-f_1=delta_N` first becomes nonzero at the arbitrarily late
input N. These can even be actual sections of one binary-valued
finite-support sequence: interleave f_0,f_1,f_2,0 in the four residue
classes modulo 4. Thus a bound on pairwise distinguishing inputs is
strictly weaker than the injectivity-on-span assertion (6).

These finite-support sequences have finite kernels and fail the
two-base-infinitude hypothesis. They are a control for the linear-algebra
distinction only, not an invariant or a linear-growth counterexample.
Their finite growth constant is not asserted uniform in N.

### 6.2. Calibration against the persisted digit-count result

The new mechanism reproduces the already proved quadratic-growth
phenomenon for the digit-count family, by a different elementary route.
This is a check of the generic theorem, not a new subclass campaign.

Let F be finite-valued and not eventually periodic, with its values
encoded as real numbers, and set

```
G_t(n)=F(t+s_2(n)),      t>=0.
```

The functions G_0,...,G_A are linearly independent for every A. A
nontrivial linear relation would, because s_2 takes every nonnegative
integer value, give a fixed linear recurrence for F. Choose its largest
nonzero coefficient to solve for the last term from a fixed finite
preceding block. There are finitely many such blocks because F has a
finite range; the deterministic recurrence would make F eventually
periodic, a contradiction. A relation involving only one term has the
same conclusion immediately.

Each G_t with t<=A is a binary section of G_0 reached by t one-digits.
A nonzero linear combination of these A+1 functions can be chosen to
vanish at weights 0,...,A-1. Its first nonzero digit weight is at least
A, and the smallest nonnegative integer of weight k is `2^k-1`.
Therefore this combination lies in W_A(G_0) and has

```
nu(g)>=2^A-1.
```

For A>=1 put `L_A=floor(log_9(2^A-1))`. Lemma (2) gives
`|J_(A+L_A)(G_0)|>=Q_(L_A)`, a quadratic lower bound along depths of
order A. The sharper explicit state count in V006 remains available;
this argument checks that the new first-nonzero mechanism detects that
known obstruction without its special balanced ternary-block witnesses.

This calibration does not prove that an arbitrary invariant has a
digit-count section or comparable long vanishing combinations. The
missing full-class step remains exactly the one in Section 4.

## 7. Seven-field assessment and decision

1. **Objects.** Entire joint affine sections, their real linear spans,
   and the first integer at which a nonzero combination is detected.
2. **Structural gain.** A long initial zero interval yields a triangular
   number of linearly independent sections by distributing its first
   nonzero coordinate over distinct 2/3 multipliers. Cumulative linear
   growth therefore imposes the explicit prefix injectivity bound (6)
   and the square-root-depth word bound (8).
3. **Translated unresolved gap.** Force delays exceeding this bound
   from arbitrary nonconstant invariant colorings, retaining all three
   root identities. Neither local kernel infinitude nor a dimension
   count has done this.
4. **Worked example.** Section 6.2 recovers the persisted digit-count
   quadratic growth. Section 6.1 separates pairwise state tests from
   tests of their entire span.
5. **Known-cycle controls.** The d=5/d=61 periodic colorings have finite
   kernels and finite-dimensional invariant spans, so they satisfy no
   unbounded-delay premise. The generic V008 two-exit construction has
   at least quadratic joint growth and does not satisfy (1). None is
   falsely excluded or promoted to a Collatz counterexample.
6. **Cheapest meaningful next test.** Examine the exact scalar relations
   for a mechanism producing nonzero combinations of low-depth states
   with the delays in (10). Retain coefficient cancellation and actual
   nonzeroness; a formal expression that is identically zero has no first
   nonzero coordinate and supplies no growth witness.
7. **Genuinely intermediate milestone.** The explicit necessary bound
   on distinguishing word length under any proposed linear-growth
   constant. It uses every possible coefficient C but does not exclude
   any such constant for all invariants. The universal unbounded-ratio
   theorem remains the goal and is not marked achieved.

## 8. Verification scope

The argument uses only exact affine substitutions, strict integer
endpoints, triangular linear independence and finite-dimensional linear
algebra. No finite-prefix experiment certifies an equality, and no
external growth theorem is imported. It does not change historical
mathematics or executable evidence. Independent agent review passed;
novelty and formal Lean verification remain unclaimed.
