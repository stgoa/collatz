---
id: fixed-ternary-order-unbounded-depth
kind: result
title: With the ternary order fixed at h = 2, every exposure depth still has complete positive components on the required ladder
status: written
claim: >
  Odd-only 3x+1 map, absorbing at 1; A_N the six-band annulus; G_D(N) the first D arrows exposed from every
  nonzero source. For every integer D >= 1 and every positive integer X with 2^max(D+4,10) | X and
  X = 10 mod 3^(D+2), N = 3X/128 is divisible by 8, h = v_3(X-1) = 2 exactly, and the whole component of
  144N - 1 in G_D(N) is the chain y_1 -> ... -> y_(D+3), y_j = 3^j X/2^j - 1, with only the sources
  A_N(y_1) = -2, A_N(y_2) = A_N(y_3) = 2; it has mass 2 and does not contain 1. For each D infinitely many such
  N lie on N = 96 64^k. So no finite-valued function of h alone bounds the necessary exposure depth, for the
  whole annulus or for completing the (-2, +2, +2) block. The proof uses a finite barrier lemma (every positive
  odd Syracuse ancestor of z_0 = 10u_0 - c_0 is at least 35, by a 22-case enumeration and the nontrivial cycles
  of the auxiliary map 3c - 1). X varies with D: no permanent positive component, cutoff without eventual
  certificate, or Collatz counterexample is asserted.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [unbounded-exposure-depth-necessary, delayed-release-cancellation, disjoint-annular-recursion]
certificates: [check_barrier_recompute.py]
evidence:
  - "check_fixed_h.py, fixed_h_audit.json: the legacy checker (regenerates the complete finite barrier certificate, recovers the full exposed components at five CRT cutoffs with D = 1, 2, 5, 8, 12 and three required-ladder examples with the inverse oracle, and checks the ladder exponents by digit lifting through D = 64; about 0.1 s). Fails at its new path: it imports inverse_exposure_probe from ../templates/ (now ../unbounded-exposure-depth-necessary/). Passed at be73a66 as experiments/residual_progress/phase_depth/check_fixed_h.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a)"
  - "fixed_h_check.py, fixed_h_check.json: side-lane probe (Claude side lane, 2026-10-17): rebuilds the barrier data and the theorem with independent code. Fails at its new path: it imports affine_controls from experiments/packet_currents/negative_controls/ by repository-relative path (now ../locally-collatz-like-control-barrier/) and delayed_release_check, depth_probe from its own folder (now ../delayed-release-cancellation/, ../unbounded-exposure-depth-necessary/). Passed at be73a66 as reviews/side_lane/fixed_h_check.py (archive/legacy-checker-run-be73a66.md, exit 0)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-17
    link: fixed_h_check.py
    scope: "Finite only (side-lane feed entry 2026-10-17 19:44, VERIFIED, main 8e2b5eb): the 54-element orbit union of the odd integers 1..33, the 22-row (z0, u0, c0) table, every c0 > 1 in a 3x-1 basin cycling away from 1; the whole depth-D component by full brute force at the least admissible X for D = 1..4 (N = 528, 528, 2472, 8304); ladder exponents for D <= 12. The inverse-history propagation was not re-derived, and the main lane's review (../outer-residual-strong-induction-support/side_lane_review_20261017_latest.md §5) corrects the probe's narrative about the role of the 3x-1 cycles. The status stays written"
aliases: [R22]
tags: [convergence, packet-currents, annular, exposure-depth, obstruction, negative-cycles]
---

# With the ternary order fixed at h = 2, every exposure depth still has complete positive components on the required ladder

## Statement

Odd-only Syracuse `S`, absorbing at 1; `A_N` the six-band annulus; `G_D(N)` exposes the first `D` arrows from every nonzero source, keeping historical intersections ([`unbounded-exposure-depth-necessary`](../unbounded-exposure-depth-necessary/README.md)).

**Theorem.** For every integer `D ≥ 1` and every positive integer `X` with `2^max(D+4,10) | X` and `X ≡ 10 (mod 3^(D+2))`, put `N = 3X/128`. Then `8 | N`, `h = v_3(X − 1) = 2` exactly, and the whole component of `144N − 1` in `G_D(N)` is `y_1 → ⋯ → y_(D+3)`, `y_j = 3^j X/2^j − 1`, with only the sources `A_N(y_1) = −2`, `A_N(y_2) = A_N(y_3) = 2`; it has mass 2, does not contain 1, and blocks every current on `G_D(N)` (signed or rational, any packing) from leaving a nonpositive residual. For each `D`, `X = 2^(e_D + 2·3^(D+1)·t)`, `N = 96·64^(k_D + 3^D·t)`, `t ≥ 0`, realizes the hypotheses on the required ladder.

**Barrier lemma (finite).** If `u_0 = 2^s 3^r ≥ 4`, `c_0` is odd with `1 < c_0 < u_0`, and some iterate of `T_−(c) = (3c − 1)/2^(v_2(3c − 1))` sends `c_0` to 1, then every positive odd Syracuse ancestor of `z_0 = 10u_0 − c_0` is at least 35. Proof by enumeration: the orbits of the odd integers 1..33 form a 54-element set; only 22 triples `(z_0, u_0, c_0)` have `z_0` in it with `9u_0 < z_0 < 10u_0`; six have `c_0 = 1`, and the other twelve values of `c_0` fall into the `T_−` cycles `5 → 7 → 5` or `17 → 25 → 37 → 55 → 41 → 61 → 91 → 17`, never reaching 1.

**Consequence.** No finite-valued function of `h` alone bounds the necessary exposure depth, even at `h = 2`; this strengthens [`short-delay-all-phase-obstruction`](../short-delay-all-phase-obstruction/README.md). The cutoffs vary with `D`; each fixed `X` has only finite ternary precision around 10. Not human peer-reviewed or formally verified; no Collatz convergence, counterexample or novelty claim.

## Proof

The legacy note "The initial ternary depth cannot bound annular cancellation depth" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

Date: 2026-10-17. Status: written proof using an explicit finite arithmetic
barrier, with exact certificate and independent finite component checks.
Not human peer-reviewed or formally verified. No Collatz convergence,
counterexample, or novelty claim is supplied.

### 1. The theorem

Use the positive odd Syracuse map `S`, with absorption at 1. Let `A_N`
be the actual six-band annular measure, and let `G_D(N)` expose the first
`D` arrows from every nonzero source, retaining historical intersections.

For **every integer `D>=1`**, choose any positive integer `X` such that

\[
\boxed{\qquad 2^{\max(D+4,10)}\mid X,
\qquad X\equiv10\pmod{3^{D+2}}.\qquad}
\tag{1}
\]

Put `N=3X/128`. Then `8|N` and **`h=v_3(X-1)=2` exactly**. The whole
component of `144N-1` in `G_D(N)` is

\[
y_1\longrightarrow y_2\longrightarrow\cdots\longrightarrow y_{D+3},
\qquad y_j=3^jX/2^j-1.
\tag{2}
\]

Its only annular source coefficients are

\[
A_N(y_1)=-2,\qquad A_N(y_2)=A_N(y_3)=2.
\tag{3}
\]

Consequently it has signed source mass 2, does not contain 1, and
prevents a current on `G_D(N)` from leaving an everywhere nonpositive
residual. This is a complete-component obstruction, not a selected
positive path with unexamined incoming histories.

For each `D`, infinitely many such cutoffs lie on the required ladder
`N=96*64^k`. Therefore **no finite-valued function of `h` alone can bound
the necessary exposure depth**, even at the fixed value `h=2`. This
strengthens the earlier [failure of the bound `2h+1`](../short-delay-all-phase-obstruction/README.md).

The theorem does not exhibit a cutoff with no eventual certificate.
The congruence and the cutoff vary with `D`; each fixed integer `X` has
only finite ternary precision around 10. Recursive constructions with
growing depth and additional arithmetic information remain possible.

### 2. The finite arithmetic barrier

This lemma is independent of `X`, `N`, and `D`. Write

\[
T_-(c)=\frac{3c-1}{2^{v_2(3c-1)}}\qquad(c\text{ positive and odd}).
\]

The use of this auxiliary map is an exact arithmetic test on a finite
list; no convergence statement about that map is assumed.

#### Barrier lemma

Let `u_0=2^s3^r>=4`, with integers `r,s>=0`. Let `c_0` be odd with
`1<c_0<u_0`, and suppose some finite iterate of `T_-` sends `c_0` to 1.
Set

\[
z_0=10u_0-c_0.
\]

Then every positive odd Syracuse ancestor of `z_0` is at least 35.
Equivalently, no positive odd integer at most 33 reaches `z_0`.

#### Complete finite proof of the lemma

The ordinary Syracuse orbits of the 17 odd integers from 1 through 33
all terminate at 1. Their full union is the following 54-element set:

```text
1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,
41,47,53,61,71,91,103,107,121,137,155,161,167,175,
233,251,263,283,319,325,377,395,425,433,445,479,577,
593,719,911,1079,1367,1619,2051,2429,3077
```

The receipt stores each full path; its checker verifies every arrow and
termination at 1 directly. Hence an ancestor at most 33 would force
`z_0` into this set. Since `0<c_0<u_0`, we must have

\[
9u_0<z_0<10u_0.
\]

Enumerating every integer `u_0=2^s3^r` in this strict interval, for all
54 values of `z_0`, gives **exactly** the following 22 candidates:

| `z_0` | `u_0` | `c_0` |
|---:|---:|---:|
| 155 | 16 | 5 |
| 167 | 18 | 13 |
| 175 | 18 | 5 |
| 233 | 24 | 7 |
| 251 | 27 | 19 |
| 263 | 27 | 7 |
| 319 | 32 | 1 |
| 325 | 36 | 35 |
| 433 | 48 | 47 |
| 445 | 48 | 35 |
| 479 | 48 | 1 |
| 577 | 64 | 63 |
| 593 | 64 | 47 |
| 719 | 72 | 1 |
| 911 | 96 | 49 |
| 1079 | 108 | 1 |
| 1367 | 144 | 73 |
| 1619 | 162 | 1 |
| 2051 | 216 | 109 |
| 2429 | 243 | 1 |
| 2429 | 256 | 131 |
| 3077 | 324 | 163 |

The six rows with `c_0=1` are excluded by the lemma's hypothesis. The
other rows have only 12 distinct values of `c_0`. Each enters one of
the following explicitly checked cycles under `T_-`, neither containing 1:

\[
5\to7\to5,
\]

\[
17\to25\to37\to55\to41\to61\to91\to17.
\]

Their connecting paths are

```text
13 -> 19 -> 7
35 -> 13
47 -> 35
63 -> 47
131 -> 49 -> 73 -> 109 -> 163 -> 61.
```

Together with starts at 5, 7, 19, 49, 73, 109, and 163, these exhaust
all 12 distinct values. Thus none can reach 1 under the deterministic
map `T_-`. This excludes every candidate and proves the lemma.

The bounded enumeration is the proof's finite certificate. It does not
extrapolate a finite range to all positive integers: a hypothetical
counterexample must belong to this explicitly bounded list.

### 3. Every off-chain inverse history satisfies the barrier

Fix a chain point `y_k`, and consider an admissible inverse history of
length `l<=D`. Let its inverse valuations be `a_1,...,a_l>=1`, and
`A=a_1+...+a_l`. Every state has the affine form

\[
x=uX-c,\qquad u=3^{k-l}2^{A-k},\qquad c>0,
\tag{4}
\]

with updates

\[
u'=2^a u/3,\qquad c'=(2^a c+1)/3.
\tag{5}
\]

Initially `c=1`. Each chain point is `-1 modulo3`, so its first inverse
valuation is odd. Valuation 1 stays on the chain; an off-chain branch
starts with an odd valuation at least 3. It suffices to treat histories
whose first inverse step is such a departure, since any earlier chain
steps can be removed. Then

\[
E=A-l=\sum_i(a_i-1)\ge2.
\]

#### Before the first integral slope

As long as `A<k`, also `l<k`. The coefficient `u` has a binary
denominator supplied by `X`, and a positive factor of 3. The actual
inverse admissibility condition is therefore
`3 divides 2^a c+1`. It follows inductively that `c` remains a positive
odd integer, including the first step with `A>=k`.

We also have `c<u` through that step. Evaluate the inverse maps at
`X=1`: the resulting number is `u-c`. Had every valuation been 1,
its value after `l` steps would be `(3/2)^(k-l)-1>=0` while `l<=k`.
The first valuation at least 3 increases this strictly, and every
subsequent inverse map preserves strict domination while that comparison
is nonnegative. At the first crossing `A>=k` we still have `l<=k`,
because `A` increases by at least 1 each step. This proves `u-c>0`.

Before that crossing, set `s=k-A>0` and `r=k-l`. Then `r-s=E>=2`, giving

\[
u=3^r/2^s=3^E(3/2)^s\ge9.
\]

Thus every such state satisfies

\[
x>9(X-1)>27X/8-1=144N-1
\tag{6}
\]

for `X>=1024`. Histories that end before the crossing are already excluded
from the annular source support.

#### The first integral slope and its negative-map history

At the crossing set `r=k-l>=0` and `s=A-k>=0`. Then

\[
u_0=3^r2^s\ge4,
\]

since `r+s=E>=2`. The integer `c_0` is positive, odd, and less than
`u_0`. It is strictly greater than 1: an update `(2^a c+1)/3=1` with
positive odd integer `c` forces `c=1,a=1`. Hence reaching `c_0=1` would
force all preceding valuations to be 1, contradicting the off-chain
departure.

Every previous update in (5) is exact in the form
`3c'-1=2^a c`, with `c` odd. Reversing these updates shows that
`T_-^l(c_0)=1`. Therefore the first integer shadow at `X=10`,

\[
z_0=10u_0-c_0,
\]

satisfies every hypothesis of the finite barrier lemma. This is where
the restrictions on possible first integer shadows enter; an arbitrary
positive shadow would not be sufficient.

#### Later shadows stay positive, odd, and above 33

At every later step define the auxiliary rational expression

\[
z=10u-c,
\qquad x-z=u(X-10),\qquad
z'=(2^a z-1)/3.
\tag{7}
\]

After the crossing, `u` has only powers of3 in its denominator. At a
history length `l<=D`, the difference in (7) is an even integer divisible
by3: (1) gives ternary valuation at least `D+2+k-l>=3`, and `X-10` is
even. Therefore every admissible inverse branch at the actual integer
`x` is also admissible at `z`. Starting from the positive odd integer
`z_0`, the updates preserve positive odd integrality, and each is an
exact inverse Syracuse step.

Every later `z` is consequently a positive odd ancestor of `z_0`.
The barrier lemma gives `z>=35`. Since `c>0`, we have `u>z/10`.
For `X>=1024>10`,

\[
x=u(X-10)+z>
\frac{z}{10}(X-10)+z
=\frac{zX}{10}\ge\frac72X
>\frac{27}{8}X-1.
\tag{8}
\]

Equations (6) and (8) exclude **every** source on every off-chain inverse
history of length at most `D`, regardless of its valuation word.

### 4. Complete historical closure

The binary hypothesis makes every `y_k` odd and every displayed arrow
an exact valuation-one Syracuse arrow. The first three are the sources
in (3), by the six-band coefficient table and `X=1 modulo9`; all later
vertices exceed the annular support. Every arrow in (2) is exposed:
the first three origins are sources, and later origins are fewer than
`D` steps from `y_3`.

An off-chain incoming exposed arrow at a chain vertex would have an
actual annular source ancestor within at most `D` inverse steps. Section 3
excludes that possibility. The valuation-one predecessor at the bottom
is `X-1`, which is divisible by 3, has zero annular coefficient, and has
no odd Syracuse predecessor. It is therefore not an exposed origin.

Finally, every source after at most `D-1` steps has height at most

\[
(3/2)^{D-1}144N-1=y_{D+2}<y_{D+3}.
\]

The terminal vertex has no exposed outgoing arrow. These statements
exhaust all incident arrows and prove that (2) is the entire component,
with only the source mass in (3). It contains no absorber.

Summing `(I-P)J` over this finite exposed component gives zero for every
current supported on the graph. Its source mass 2 therefore cannot be
represented with a nonpositive residual. Sources in other components
cannot change that sum. This conclusion allows arbitrary signed or
rational coefficients, cross-packet packing, and unequal-time meetings
within `G_D`; it is not a restriction to a particular current template.

### 5. Infinitely many examples on a required ladder

The elementary order proof in the earlier
[delayed-release note](../delayed-release-cancellation/README.md) shows that 2
generates the units modulo `3^m`, with order `2*3^(m-1)`. Hence there is
an exponent `e_D` such that

\[
2^{e_D}\equiv10\pmod{3^{D+2}},
\]

unique modulo `2*3^(D+1)`. Since 10 is 1 modulo9, every such exponent
is divisible by 6. Add sufficiently many periods to make
`e_D>=max(D+4,12)`. For all integers `t>=0`,

\[
X=2^{e_D+2\cdot3^{D+1}t},\qquad
N=96\cdot64^{k_D+3^Dt},\qquad k_D=e_D/6-2,
\tag{9}
\]

satisfy (1). Each has `h=2`, since its residue modulo27 is exactly 10.
This proves the infinite required-ladder quantifier without allocating
these enormous integers.

The checker computes `e_D` by lifting one ternary digit at a time: at
each step exactly one of `e,e+order,e+2*order` has residue 10 modulo the
next power of3. It verifies the resulting congruences at selected depths
through 64, using modular exponentiation only. The unbounded conclusion
is the elementary order argument, not that finite list.

### 6. Verification, scope, and the constructive implication

```sh
python3 experiments/residual_progress/phase_depth/check_fixed_h.py
```

The default checker regenerates the complete finite barrier certificate,
compares `fixed_h_audit.json`, and independently recovers full exposed
components at five CRT cutoffs with depths `1,2,5,8,12`, plus three actual
required-ladder examples. All eight graphs equal the predicted path;
the largest uses 156 inverse reachability queries. The recorded default
run takes about 0.1 seconds.

The complete-component checks have caps of 2,000 vertices and 100,000
queries. Every check finishes; a cap is an error, never an obstruction.
The finite barrier checks also have explicit orbit caps and assert actual
termination at 1 or an exact repeated cycle. The receipt stores all
paths, all 22 triples, and full finite component rows. No optimized Python
mode is used. The unchanged independent feed commit reviewed for this
batch is `f12da944dc68cfaff0884d874e11bc6c2cb98d34`; the present argument
is independently derived.

**What is ruled out:** any uniform exposure bound depending only on
`h=v_3(X-1)`, whether for the whole annulus or for capacity-safe completion
of the original `(-2,+2,+2)` block inside that graph.

**What remains open:** a constructor that uses the deeper ternary phase,
or another growing parameter, and proves eventual capacity-safe
completion. The obstruction is now driven by arbitrary proximity to
the fixed ternary reference 10, even though proximity to 1 stays fixed.
The finite interaction of the ordinary positive map and the auxiliary
`3c-1` map supplies a reusable barrier test; it does not establish
infinite isolation for any individual positive integer cutoff.

## Certificates

- [`check_barrier_recompute.py`](check_barrier_recompute.py) (written at the B09 migration, under 1 s, standard library). Recomputes the finite barrier certificate and compares it with `finite_barrier_certificate` in the legacy receipt `fixed_h_audit.json`: the 54-state orbit union (every orbit reaches 1), exactly the 22 candidate triples, and for each of the twelve `c_0 > 1` the full `T_−` orbit into one of the two cycles; and for every `D = 1..64` an exponent `e` with `2^e ≡ 10 (mod 3^(D+2))`, `6 | e`. It does not recompute the complete exposed components (they need the inverse oracle; legacy checker, evidence only).
- The command in the legacy text names `experiments/residual_progress/phase_depth/`.

## Remarks

- **The `3x − 1` controls.** The auxiliary map `T_−` is the `d = −1` member of the `3x + d` family (the negative-integer control of [`locally-collatz-like-control-barrier`](../locally-collatz-like-control-barrier/README.md)). Its two nontrivial cycles are used only as exclusion certificates: a hypothetical small positive shadow would force an actual `c_0` that reaches 1 under `T_−` into a cycle basin away from 1, which is impossible. The side lane first described the obstruction as lasting "while the auxiliary values sit in the `3x − 1` cycles"; the main lane's review reverses that reading (§5 of [`side_lane_review_20261017_latest.md`](../outer-residual-strong-induction-support/side_lane_review_20261017_latest.md)): the actual first-integer offsets lie in the basin of 1.
- **What remains.** A constructor using the deeper ternary phase, or another growing parameter, with a proof of eventual capacity-safe completion.

## History

- Migrated from `experiments/residual_progress/phase_depth/FIXED_H_DEPTH.md` (legacy ID R22) at commit `be73a66`, by the B09 migration (Claude, Opus 5.5). Note, checker and receipt moved byte-identical, with the side-lane probe `reviews/side_lane/fixed_h_check.*`; `check_barrier_recompute.py` was added at the migration. Legacy status: "written complete-component proof with a finite arithmetic certificate".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `46198fb`; the side feed reviewed for this batch was `f12da944`, and the note says the argument was derived independently of it. Its "independent model audits" were the main lane's own agents. The side lane's finite check is recorded under `reviewed_by`.
