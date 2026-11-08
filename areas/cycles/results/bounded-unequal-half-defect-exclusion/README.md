---
id: bounded-unequal-half-defect-exclusion
kind: result
title: Unequal same-parity half defects of combined magnitude at most 24 exclude denominator one
status: written
claim: >
  Raw odd-only positive valuation words w=uv, with equal-length halves differing
  at exactly two positions. If the two absolute changes are unequal positive
  integers p<q of the same parity and p+q<=24, then D_w>0 implies den(w)>1.
  There is no restriction on the half-length, common letters, defect positions,
  signs, near-criticality or primitivity, and no external bound is used.
  More precisely, every full plus-factor cancellation has a canonical
  two-segment Mersenne representation among 74 base joins, with arbitrary
  repetitions of its at most two positive cycles. Exact affine convexity
  bounds show that its canonical normalized 3x+1 state is strictly below 1.
  Finite closed graphs certify all J=(p+q)/2 from 2 through 12 and all
  1<=r=(q-p)/2<J in both orders; the proof covers unbounded word lengths.
authors:
  - Codex cycle research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [two-half-defect-mersenne-normal-form, baseline-obligation-transfer-controls]
certificates: [check_bounded_halves.py]
evidence:
  - "check_bounded_halves.json: complete crossing graphs and traces, all 74 base joins and loop limits, exact reconstruction samples and actual-cycle controls"
tags: [cycles, denominators, half-defects, signed-orbits, finite-graphs, all-length]
---

# Unequal same-parity half defects of combined magnitude at most 24 exclude denominator one

## Statement

Let `w=uv` be a word of positive integer valuations for the raw
odd-only map, with `len(u)=len(v)=n`. Suppose the halves differ at
exactly two positions, and their absolute changes `p<q` satisfy

```
p and q have the same parity,       p+q <= 24.       (1)
```

Write `D_w=2^sum(w)-3^(2n)` and let `C_w` be the additive-one
intercept. Then

```
D_w>0  implies  den(w)=D_w/gcd(C_w,D_w)>1.           (2)
```

Thus no positive integer cycle of `3x+1` has such a half-period
four-mismatch pattern. The common letters and their number are
arbitrary. No near-critical, coprimality or primitive-word condition
is imposed. Equal-magnitude and opposite-parity defects, larger
combined magnitudes, and other shifts remain outside this statement.

The finite part certifies closed state graphs for 66 magnitude pairs,
in both segment orders. It is not a census up to a word length:
every admissible path is a listed base path with arbitrary cycle
repetitions, and an affine argument handles all repetitions at once.

The normalized rational `3x+1` state is `C_w/D_w`. For `3x+d`,
the actual state is `d*C_w/D_w`; conclusion (2) does not exclude
actual cycles for other addends.

## Proof

### 1. The signed normal form and its state criterion

Put `J=(p+q)/2`, `r=(q-p)/2`, so `2<=J<=12`, `1<=r<J`,
`p=J-r`, and `q=J+r`. Let

```
d_H=2^J-1,       d_L=2^r-1,
T_d(x)=(3x+d)/2^v_2(3x+d).
```

The valuation uses the absolute value for a negative numerator;
the map is undefined when that numerator is zero. Every state
in a segment below is a nonzero odd integer.

Since `sum(w)=2S` is even, its denominator factors as

```
D_w=(2^S-3^n)P,       P=2^S+3^n.
```

If `P` does not divide `C_w`, (2) follows immediately. If it does,
the [Mersenne normal form](../two-half-defect-mersenne-normal-form/README.md)
puts a cyclic rotation of the word into one of these forms.
Both nonempty segments join `-h -> z -> h`, for a positive odd `h`.
Here `A[t]` increases only the last letter of `A` by `t`.

| Order | Segment maps | Boundary conditions | Reconstructed halves | `s` |
|---|---|---|---|---:|
| HL | `T_(d_H)`, then `T_(d_L)` | `last(A)>J-r`, `last(B)>r` | `u=A[-(J-r)]B[-r]`, `v=AB[J]` | `J` |
| LH | `T_(d_L)`, then `T_(d_H)` | `last(B)>J` | `u=A[J-r]B[-J]`, `v=AB[r]` | `r` |

In each row, `S=sum(A)+sum(B)` and

```
C_v=2^s C_u-hP,
C_(uv)/D_(uv)=(C_u-h*beta)/(2^s*beta-alpha),
alpha=3^n,       beta=2^sum(u).                      (3)
```

For `D>0`, the state in (3) lies in `(0,1)` precisely when

```
F_u(1)=(alpha+C_u)/beta < 2^s+h.                     (4)
```

An integral cycle would give positive integer states at every
rotation, so (4) rules it out. The normal-form theorem covers
every original ordering and sign choice by cyclic cuts. It remains
to prove (4) for all the segment pairs in the bounded parameter range.

### 2. Finite candidate endpoints, including negative interfaces

For an addend `d_j=2^j-1`, a negative-to-positive crossing starts
at `-a`, where `a` is positive odd and `3a<d_j`. These are finitely
many explicitly enumerated inputs. Its positive numerator is less
than `2^j`, so the crossing valuation is strictly less than `j`.

Let `G_j` be the forward closure under `T_(d_j)` of all their
positive outputs. The certificate constructs `G_j` for every
`1<=j<=12` and verifies that every successor stays in the graph.
Every positive state reached from a negative start therefore lies
in `G_j`. For `j=1,2`, there are no such crossings and the graph
is empty. No hypothesis about arbitrary starting states is used.

Fix a row of the normal-form table. Let `j_1,j_2` be its two
levels, and let `b_A,b_B` be the strict lower bounds on its final
valuations: `(J-r,r)` for HL and `(0,J)` for LH. In particular,
`b_B=j_2` in both rows.

If the interface `z` is positive, the first segment has already
crossed. Its last arrow is either a crossing arrow or an arrow
inside `G_(j_1)`, and has valuation greater than `b_A`. Let `Z`
be all outputs of these eligible arrows. Close `Z` forward under
the second map, obtaining a finite graph `H`. Then `h` is an
output of an arrow in `H` with valuation greater than `b_B`.

If `z` is negative, the second segment must cross. That crossing
cannot be its final arrow: a crossing valuation is below `j_2`,
whereas the final valuation is greater than `b_B=j_2`. Its final
arrow is therefore inside `G_(j_2)`. In this case `h` is an output
of an eligible arrow in that graph.

The union of these two finite endpoint sets contains every possible
`h`, without assuming the sign of the interface. The certificate
builds and checks every graph `H` as well as every `G_j`. A resource
guard raises an error; it never accepts a truncated graph.

### 3. Complete traces give a finite list of base paths

For each candidate `h`, trace the first map from `-h` until its
first repeated state or a zero numerator. Retain every eligible
arrow as a possible end of `A`. From its output trace the second
map the same way, retaining every eligible arrow into `h` as a
possible end of `B`. Every trace in this finite computation closes
or reaches a zero numerator. No open trace is accepted.

These traces cover every finite segment: a deterministic orbit
has a transient prefix followed by one cycle, or stops at an
undefined arrow. Any path ending on a cycle consists of its
recorded base path and a nonnegative number of whole repetitions
of that cycle, inserted at its entry. Each trace includes the
cycle-closing arrow. Thus both the first arrival at a cycle entry
and a later return to it are tested. In particular, when `z=h`,
a nonempty second segment returning to its start is included.

The exact result is:

| Quantity | Certified value |
|---|---:|
| Ordered parameter cases | 132 |
| Base joins | 74 |
| Base joins with negative interface | 0 |
| Bases with zero / one / two insertion cycles | 15 / 44 / 15 |
| Insertion cycles, counted by base | 74 |
| Completed traces | 1,057 |
| Maximum recorded trace length | 273 |
| Maximum base half-length | 164 |
| Maximum base endpoint `h` | 261 |

Every insertion cycle of every retained join is positive. The
certificate requires these facts, rather than merely reporting
them. Negative cycles would need a different argument; here the
complete enumeration excludes such joins.

The receipt lists every base pair `A,B`, its interface, endpoint,
cycle words and insertion sites. Bases can represent overlapping
families; uniqueness is not needed for the coverage argument.

### 4. Affine convexity handles every cycle repetition

Consider a positive cycle of a fixed auxiliary map `T_d`, of
valuation word `L`, returning to an entry state `z>0`. Its ordinary
additive-one affine map has the form

```
F_L(x)=c+lambda*(x-c),
c=z/d>0,       lambda=3^len(L)/2^sum(L).             (5)
```

Its additive intercept is positive. Since `c=F_L(c)>0`, equation
(5) gives `0<lambda<1`. Repeating it `t>=0` times replaces its
slope by `rho=lambda^t`, with `0<rho<=1`.

Fix a base join, and keep its two altered boundary letters fixed.
An inserted whole cycle uses the ordinary `+1` affine maps: its
fixed point is the intrinsic `z/d`, with no boundary rescaling.
For each available insertion site, define its **limit value** by
starting at `c=z/d` there and applying the remaining base suffix
of `u`, with all later insertions omitted. Let these be `L_A,L_B`,
and let the base value be `F_0=F_u(1)`.

For repetition counts `t_A,t_B`, write `rho_A=lambda_A^t_A` and
`rho_B=lambda_B^t_B`. A missing cycle means `rho=1` and omits its
limit term. Affineness gives exactly

```
F(t_A,t_B) = rho_A*rho_B*F_0
           + (1-rho_A)*rho_B*L_A
           + (1-rho_B)*L_B.                         (6)
```

The three coefficients are nonnegative, sum to 1, and the
coefficient of `F_0` is strictly positive for all finite repetition
counts. Consequently

```
F_0 < 2^s+h,       L_A,L_B <= 2^s+h                 (7)
```

imply (4) for every pair of nonnegative repetition counts.

The certificate computes these fractions exactly for every base
and cycle. Every base passes the strict bound and every available
limit passes the weak bound. All bases have `D>0`, and positive
cycle insertions only decrease the half-composition slope, so
their repetitions retain `D>0`; the conclusion already needed
only the words with `D>0`. Equations (6) and (7) prove (4) for
all lengths. Together with (3) and the case `P` not dividing
`C_w`, this proves (2).

## Certificates

Run from the repository root:

```
python3 areas/cycles/results/bounded-unequal-half-defect-exclusion/check_bounded_halves.py
python3 -O areas/cycles/results/bounded-unequal-half-defect-exclusion/check_bounded_halves.py
```

The standard-library [certificate](check_bounded_halves.py) writes
[its deterministic receipt](check_bounded_halves.json). It checks
closed graph edges, all signed trace endings, all endpoint and
boundary tests, reconstruction identities, positivity and contraction
of every insertable cycle, and every exact base and limit inequality.
The receipt includes graph hashes and all base words. Resource guards
abort with failure; zero accepted truncations is required.

There are also 282 exact reconstruction checks with each available
cycle repeated 0, 1 or 2 times. These check the implementation of
(6); the mathematical proof above covers every repetition count.
The enumerated bases recover the prior amplitudes `(1,3)` exclusion,
the single `(1,5)` family, and the two `(2,4)` families.

All eleven shared actual `3x+d` fixtures are replayed. They lie
outside this half-defect class: the odd lengths have no half-period,
and the period-two fixture cannot have two changed half positions.
Two actual cycles inside the class are also replayed: the `(2,4)`
base with `d=361` and minimum 17, and the `(1,5)` base with `d=893`
and minimum 367. Their normalized states are below 1 and their
denominators exceed 1, so the theorem preserves both cycles.

## Remarks

This is an unconditional bound on a specified half-period pattern,
not an exclusion of all four-mismatch rotations. Its finite state
analysis classifies every full plus-factor cancellation in the
bounded amplitude range and controls arbitrary positive cycle
insertions. The common background is not fixed in advance.

The [largest-letter and mismatch-variation reduction](../largest-letter-rho-reduction.md),
together with its external gap and cycle-size inputs, already
excludes bounded mismatch variation in hypothetical `3x+1` cycles.
Here the half-turn variation is `2(p+q)`. The present contribution
is the explicit signed-orbit proof without those external inputs,
and its complete description by finitely many paths and loops;
it is not claimed to exclude a previously uncovered global cycle
class under the stronger imported theory. Novelty is undetermined.

For larger amplitudes, the remaining tasks are to control the
crossing graphs and transient paths, or to prove the affine
inequality without finite closure. Equal magnitudes, opposite
parities and shifts other than a half-period need their own
arguments. The general [four-mismatch question](../../questions/rotation-distance-at-least-5.md)
remains open.

## History

- 2026-11-08: proved the bounded-amplitude exclusion using complete
  signed crossing graphs and an affine convexity argument for
  unbounded repetitions. Same-session mathematical scrutiny does
  not change the node's `written` status (Codex cycle research lane,
  GPT-6 Astra; directed by Santiago Armstrong).
