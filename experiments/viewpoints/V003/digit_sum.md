# V003 — No component invariant can depend only on binary digit count

**Status: elementary written proof; no novelty or convergence claim.**
This is a partial classification over an explicitly defined infinite class.
It is independent of the finite-period argument and of any second-base
automaticity theorem. A bounded literature check found no exact precedent;
that does not establish novelty.

## Statement

Let s_2(n) be the number of 1s in the binary expansion of a positive integer.
Let C be any set and F:{1,2,...}->C any function. Suppose h(n)=F(s_2(n))
and h(3n+1)=h(n) for every positive odd n>1. Then F, and hence h, is
constant. No finiteness or periodicity assumption on F is required.

Doubling invariance is automatic because multiplying by2 appends a zero bit.
Thus this applies to absorbed odd-only component invariants. The displayed
3n+1 is a color identity, not a declaration of a new clock.

## Proof

For every integer k>=2 put

```
n_k=32(2^k-1)+9.
```

The binary blocks above and below bit5 are disjoint, so

```
s_2(n_k)=k+2,
3n_k+1=32(3*2^k-3)+28.
```

For k>=2, 3*2^k-3=2^(k+1)+(2^k-3) has k one-bits: the second summand
has k-1 one-bits and no overlap with the first. Since28<32 has three
one-bits, the second block decomposition gives s_2(3n_k+1)=k+3.
Every n_k is positive odd and exceeds1, so F(k+2)=F(k+3) for all k>=2.
All values at weights4,5,... agree. Three odd source identities connect
the remaining weights:

| Source n | 3n+1 | s_2(n) | s_2(3n+1) |
|---|---:|---:|---:|
| 5 | 16 | 2 | 1 |
| 13 | 40 | 3 | 2 |
| 23 | 70 | 4 | 3 |

Thus F(1)=F(2)=F(3)=F(4)=.... Weight0 never occurs on positive integers
and has not been constrained. This completes the proof.

## Automatic subclass and a worked exclusion

For every m>=1, each coloring h(n)=G(s_2(n) mod m) is binary-automatic:
retain the digit count modulo m while reading bits. The theorem classifies
all invariant colorings in this family, simultaneously over all m and output
maps G. It does not enumerate a bounded number of states.

At m=2 this includes the nonperiodic Thue–Morse coloring. Its failure of
invariance is witnessed by5: s_2(5)=2 but s_2(16)=1. The infinite family
above connects every adjacent weight, so recoloring digit counts cannot
repair this failure.

This class goes beyond periodic sequences. Thue–Morse cannot have an eventual
period M: doubling would make it a global period, but for 2^L>M,
s_2(2^L-M)=L-s_2(M-1) has alternating parity as L grows, while adding M
gives the constant weight s_2(2^L)=1. This contradicts that period.

## Controls and remaining scope

The invariant 1_{5|n} for d=5 does not factor through s_2: 3 and5 both
have weight2 and different colors. For d=61, 31 and61 both have weight5
and different divisibility colors. The +1 identities above must not be
silently replaced by +d. These controls are excluded at a named hypothesis.

Order, positions and patterns of bits can carry information beyond their
count. No actual hypothetical bad-set indicator has been shown to factor
through s_2. The mixed-section problem in [kernel_probe.md](kernel_probe.md)
remains the main target; this theorem supplies one rigorous partial answer.
