# R71 — Exact denominators for mechanical valuation words

**Status:** written elementary derivation and exact finite replay. This is a
restricted cycle result and a control family, not a Collatz convergence proof.
Related nonintegrality results are already published; no novelty is claimed.

## Why this matters for the side-lane transfer

For odd d coprime to3, the odd-only maps obey `S_d(dy)=d S_1(y)` on positive
odd rationals with denominator coprime to6. This correctly transports local
valuation identities. It sends the positive integer domain for S_d to
positive rationals in `d^(-1) Z`, not necessarily to integers for S_1.
Exact integrality can therefore distinguish whole words, at any height.
Covariance alone does not show that d can matter only in a finite base check.

Conversely, a proof intended to work on this entire rational domain must
cope with genuine positive cycles. Below we give controls with every state
above any prescribed constant, as well as the exact reason why this
particular family cannot be a nontrivial integer Collatz cycle.

## 1. General word identity and exact legality

Take k>=1 and a word of positive valuations `(a_0,...,a_(k-1))`. Let

```
A_j = a_0+...+a_(j-1), A_0=0, A=A_k,
B = sum_(j=0)^(k-1) 3^(k-1-j) 2^A_j,
D = 2^A-3^k.
```

The affine composition is `(3^k x+B)/2^A`. Suppose D>0. Its unique fixed
point is x=B/D>0. For the cyclic rotation starting at i, denote its
intercept by B_i; all rotations have the same D. Direct expansion gives

```
3B_i + D = 2^a_i B_(i+1),                (1)
```

with cyclic indices. Every B_i is odd, because its first summand is odd
and the others are even. D is odd and prime to3. Thus (1) proves the
**exact** valuation a_i, not merely divisibility by 2^a_i. The numbers
B_i/D form a genuine positive odd rational Syracuse cycle.

Since 2 and3 are units modulo D, (1) also proves that
`gcd(B_i,D)` is independent of i. The common reduced denominator is

```
d = D/gcd(B,D),                         (2)
```

which is coprime to6. Multiplication by d gives an integer S_d cycle.
The reduced denominator of any positive odd rational with denominator
coprime to6 is invariant under S_1: if gcd(p,q)=1 and gcd(q,6)=1, then
gcd(3p+q,q)=1, and division by powers of2 cannot cancel any factor of q.
This does not supply a nontrivial cycle at d=1.

## 2. The mechanical family

Fix integers A>=k>=1 with2^A>3^k. For `0<=l<k`, define

```
a_i(l) = floor(((i+1)A+l)/k)-floor((iA+l)/k),
B_l = sum_(j=0)^(k-1) 3^(k-1-j) 2^floor((jA+l)/k).
```

These are the specified evenly spaced, or mechanical, valuation words.
All entries are positive and their total is A. The argument below needs
only these formulas; it assumes no classification of arbitrary balanced
words and no extremal theorem about other cycles.

**Theorem.** Put `g=gcd(A,k)`, `A_0=A/g`, `k_0=k/g`. Every state in any
of these mechanical cycles has reduced denominator

```
d = 2^A_0-3^k_0.                       (3)
```

Their only positive integer case is the word consisting entirely of2s,
whose cycle is the fixed point1.

### Primitive case

First suppose gcd(A,k)=1. Shifting the word by s places replaces its
intercept l by `l+sA mod k`: expand the floor functions and subtract the
integer `floor((sA+l)/k)`. Every l is therefore a cyclic rotation of l0.
By (1), all `gcd(B_l,D)` agree.

For k>=2, passing from l0 to l1 increases precisely one prefix floor.
Indeed, among j=0,...,k-1 there is exactly one j with
`jA=k-1 mod k`, and this j is nonzero. Hence

```
B_1-B_0 = 3^(k-1-j) 2^floor(jA/k).     (4)
```

The common gcd divides (4). Because gcd(D,6)=1, that gcd is1. For k1
we have B0=1 directly. This proves (3) in the primitive case.

### Repeated words

For g>1, the l0 word is g repeats of the word with parameters(k_0,A_0).
More generally, writing `l=g h+r`, 0<=r<g, gives

```
floor((jA+l)/k) = floor((jA_0+h)/k_0).
```

Thus each intercept word repeats the corresponding primitive word. Its
positive fixed point is unchanged by repetition: an affine map with
slope3^k_0/2^A_0 strictly between0 and1 has the same unique fixed point
as every positive iterate. Applying the primitive case proves (3).
Using the unreduced D here would be wrong; for(k,A)=(6,10), D295 but d5.

### Excluding nontrivial integer cycles in this family

An integer state requires d1. If k_0>=2, positivity forces A_0>=4.
But `2^A_0=3^k_0+1` is impossible modulo8: the right-hand side is2
when k_0 is even and4 when it is odd. If k_0=1, d1 forces A_0=2.
Consequently A=2k, every valuation is2, and every state is1.

The theorem excludes this entire word family, at every length. It
neither excludes other periodic valuation patterns nor addresses
aperiodic positive divergence.

## 3. Rational cycles arbitrarily far above the absorber

For each k>=1, choose A as the bit length of3^k, equivalently
`A=ceil(k log_2 3)`. Exact integer arithmetic gives

```
3^k < 2^A < 2*3^k,      0<D<3^k.
```

The word entries are1 or2. For every intercept l and every j,

```
floor((jA+l)/k) > jA/k-1,
3^(k-1-j) 2^floor((jA+l)/k)
    > (3^(k-1)/2) (2^(A/k)/3)^j >= 3^(k-1)/2.
```

Summing k terms and dividing by D<3^k proves

```
every cycle state x > k/6.             (5)
```

Given any C>0, choose an integer k>6C. This yields a rational S_1 cycle
with all states>C. With d from(3), the corresponding integer S_d cycle
has every state>C d. For k>6, d>1 and the cycle avoids the fixed absorber d.
The denominator d varies with k; this is not a construction of arbitrarily
high cycles for one fixed d. In particular, there is no constant C
uniform over all d that bounds every cycle minimum by C d.

This is a control for arguments using only identities on rationals and
size inequalities. It does **not** show that these S_d maps pass any
proposed finite base test: smaller seeds may already fail to reach d.
It therefore does not, by itself, refute a method that separately checks
all required base cases and proves a genuinely applicable integer induction.

## 4. Reproduction and exact scope

Run from the repository root:

```
python3 experiments/residual_progress/lattice_cycles/check_balanced_cycles.py
```

The [module](balanced_cycles.py) constructs exact Fraction cycles and
the [receipt](balanced_cycles_audit.json) retains source hashes and full
integer cycle tables for selected controls. The replay checks:

- 1320 positive arbitrary words of lengths1..5 and valuations1..4,
  including each rotation, denominator invariance and exact scaled steps;
- 336 mechanical parameter pairs, k1..48 and seven consecutive totals
  beginning at `ceil(k log_2 3)`, including8232 intercepts, rotation
  identities, primitive gcds, repeated-word reduction and integer cases;
- 130 high controls, k1..128 and256/512, with exact bound(5), and11 invalid
  input rejections.

The finite checks support the implementation. The proofs above establish
the universal statements for this specified family. No dispatcher rule,
pair-current domain, universal stopping time or new Collatz proof is supplied.

## 5. Primary literature and positioning

Barry Brent's [2002 paper on rational dynamics](https://arxiv.org/abs/math/0204170)
discusses fixed denominators, cyclic parity formulas and scaling. Our
Section1 uses the odd-only clock and gives its full arithmetic derivation.

Kevin Knight's [*Collatz high cycles do not exist*](https://doi.org/10.1016/j.disc.2025.114812),
Discrete Mathematics349(3),2026,114812, already excludes integer high
cycles using Christoffel words. The journal abstract and section previews
were consulted; we do not assert priority for the nonintegrality conclusion.
The mechanical class is connected to that established direction, and its
exact denominator formula here is proved without importing an extremal
characterization or any claim about all parity words.

Fernández and Ibáñez's [2026 preprint](https://arxiv.org/abs/2607.24844)
studies extremal Christoffel parity patterns and explicitly relates its
results to Knight. Its shortcut clock differs from our k odd-only steps
with total valuation A. No theorem from that preprint is required above.
