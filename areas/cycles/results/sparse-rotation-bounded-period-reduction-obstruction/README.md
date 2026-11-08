---
id: sparse-rotation-bounded-period-reduction-obstruction
kind: result
title: Sparse rotations do not force a bounded number of short-period pieces
status: written
claim: >
  A purely combinatorial bounded-period, bounded-piece reduction from
  four-mismatch rotations fails even for primitive positive valuation words
  of prime length m, near-critical total 3^m<2^A<2*3^m, rho=4,
  and a unique largest letter equal to (m+5)/2 or (m+7)/2.
  An explicit family exists for every prime m>=61. For any T>=1,
  every decomposition after any cyclic cut into J contiguous pieces
  of period at most T satisfies m<J*T*(2^(5T+2)+1).
  Periods and templates may vary between pieces and with m.
  These are word-level coverage obstructions in the raw odd-only
  setting, not denominator-one counterexamples or cycle exclusions.
authors:
  - Codex four-arc research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [two-arc-word-rotation-structure]
certificates: [check_obstruction.py]
evidence:
  - "check_obstruction.json: exact finite word, rotation, periodic-factor and actual-cycle checks"
tags: [cycles, rotation-distance, periodic-dictionaries, coverage, obstruction]
---

# Sparse rotations do not force a bounded number of short-period pieces

## Statement

The [fixed expanding-background denominator law](../expanding-background-defect-growth/README.md)
controls changes to repetitions of a fixed word. A possible route to
[four-mismatch exclusion](../../questions/rotation-distance-at-least-5.md)
would first express every sparse-rotation word as a bounded number of
pieces with bounded periods, then apply arithmetic to those pieces.
This note records why rotation sparsity, a near-critical total and a
linear-size largest letter do not supply that representation.

A finite word `v` has **period b** if `v_i=v_(i+b)` whenever both
positions exist. Pieces may start at any phase and end partway through
a period. The bounds below allow arbitrary positive templates, not
just expanding ones.

Put `alpha=log_2(3)` and `theta=alpha-1/2`. For every prime `m>=61`,
define

```
F=floor(m*theta),       k=F-m,       A=ceil(m*alpha),
u_i=floor((i+1)*F/m)-floor(i*F/m),       0<=i<m,
h=k^(-1) mod m,         E={i:u_i != u_(i+h)}.
```

All positions are read modulo `m`. Choose the least position `p` with
`u_p=2` outside `E union (E+h)`. Replace this one letter by

```
M=A-F+2,
w_i=u_i for i!=p,       w_p=M.                            (1)
```

The choice exists. The word `w` is primitive, has `rho(w)=4`,
`3^m<2^A<2*3^m`, and

```
M is either (m+5)/2 or (m+7)/2.                           (2)
```

Along the coprime `h`-track, the edited 2-arc splits into a singleton
`M` and two nonempty 2-arcs, separated by the original 1-arc. Thus
these are four-arc words with one large label, not an arbitrary
high-complexity word inserted without a rotation constraint.

For every integer `T>=1`, put

```
L_T=T*(2^(5T+2)+1).
```

Every decomposition of any cyclic cut of `w` into `J` nonempty
contiguous pieces of period at most `T` satisfies

```
m < J*L_T.                                              (3)
```

Consequently, at fixed `T` the number of pieces grows at least
linearly with `m`. The permitted templates need not belong to a fixed
dictionary: they may depend on `m` and on the piece.


## Proof

### The construction has exactly four mismatches

The integer inequalities `3^12>2^19` and `3^3<2^5` give
`13/12<theta<7/6`. Hence

```
k > m/12-1 > 4,        k < m/6,        5<=k<m-2.
```

The mechanical word `u` has exactly `k` twos and `m-k` ones.
Since `m` is prime, `k` is invertible modulo `m`. Its 2-positions
are the inverse image of a cyclic interval of length `k` under
`i -> ik mod m`. The
[two-arc spectrum](../two-arc-word-rotation-structure/README.md)
therefore gives, with `||x||_m=min(x mod m,(-x) mod m)`,

```
s_u(r)=2*min(||rk||_m,k,m-k).                            (4)
```

In particular, `E` has size two, and only the shifts `h,-h` have two
mismatches. Every other nonidentity shift has at least four.
At most four positions lie in `E union (E+h)`, whereas at least five
positions carry 2. This proves that `p` exists. It also makes both
`p` and `p-h` agreeing positions before the edit, with neighboring
letters 2 on the `h`-track.

The fresh letter `M>2` cannot remove an old mismatch at any nonzero
shift: any comparison involving the edited position is now unequal.
At shift `h` the two new mismatch positions are precisely `p,p-h`,
disjoint from `E`; hence `s_w(h)=4`. Symmetry gives the same count
at `-h`, and (4) supplies the lower bound for all other shifts.
Therefore `rho(w)=4`. A unique `M` prevents a nontrivial repetition.

The total of `w` is `F+M-2=A`. Irrationality of `alpha` gives the
strict near-critical inequalities. To check (2), write `m=2j+1` and
`m*alpha=l+f`, where `0<f<1`. If `f<1/2`, then `F=l-j-1` and
`M=j+4`; if `f>1/2`, then `F=l-j` and `M=j+3`.
Equality `f=1/2` is impossible since it would make `3^(2m)` a
power of two. In particular the largest letter is asymptotic to
`m/2`; the construction does not evade a linear largest-letter
condition by keeping every letter bounded.

### Every bounded-period factor is short

For `1<=b<=T` and `b<=v<=2b`, irrationality of `theta` prevents
`v=b*theta`. There is also an elementary uniform separation:

```
2*ln(2)*|v-b*theta|=|ln(2^(2v+b)/3^(2b))|>2^(-5T),
|v-b*theta|>2^(-5T-1).                                  (5)
```

Indeed the two distinct positive integers inside the logarithm
are at most `2^(5T)`. If `a>b>0` are integers, then
`ln(a/b)>(a-b)/a>=1/a`. Finally `ln(2)<1` gives the second bound.
This uses no imported Diophantine estimate.

Suppose first that `m>=T*2^(5T+2)`. Since
`0<theta-F/m<1/m`, (5) implies

```
|v-b*F/m|>2^(-5T-2).                                   (6)
```

Consider a cyclic factor of `w` of length `ell<=m`, having period
`b<=T`. If it contains the unique `M` and `ell>=2b`, every position
has a second position in its residue class modulo `b`; periodicity
would repeat `M`. Therefore such a factor has `ell<2b<=2T<L_T`.

Otherwise it is a factor of the unedited mechanical word. Put
`r=floor(ell/b)`. When `r=0`, already `ell<b<L_T`. For `r>=1`, let
`v` be the sum of its first `b` letters. Its first `rb` letters have
sum `rv`. Mechanical balance, valid across the cyclic cut because
`F` is an integer, gives

```
|rv-rb*F/m|<1.
```

By (6), `r<2^(5T+2)`. Thus
`ell<(r+1)b<=T*(2^(5T+2)+1)=L_T`.
Every piece in the proposed decomposition is therefore shorter than
`L_T`, proving (3) in this case. If `m<T*2^(5T+2)`, then
`m<L_T<=J*L_T` already proves (3).

The same argument prevents a fixed short periodic background plus
only boundedly many substitutions. If a period-at-most-`T` word
differs from a cyclic cut of `w` at `s` positions, its at most `s+1`
agreeing runs each have period at most `T`. For the large-`m` case,
`m-s<(s+1)L_T`, so

```
s > m/(L_T+1)-1.                                       (7)
```

For the small-`m` case the right side is negative and the bound is
automatic. Thus neither a bounded number of pieces nor a bounded
number of edits at bounded period follows from these word conditions.

## Certificates

The deterministic [certificate](check_obstruction.py) checks every
prime `61<=m<=601`, all rotations, mechanical balance at every cyclic
start and length, and every maximal periodic factor with period
`1<=b<=12`. It also reconstructs the actual reduced `3x+den(w)` cycles
and replays the eleven standard `3x+d` fixtures, including
`d=5,7,13,61`. The [receipt](check_obstruction.json) reports the exact
finite counts. The proof above, not this finite range, establishes
the infinite family and (3).

## Remarks

The [expanding-background law](../expanding-background-defect-growth/README.md)
remains valid under its declared EXT-1 input. Its hypothesis must be
obtained using additional arithmetic or a restricted word class.
The family here makes no bounded-denominator assertion, gives no
denominator-one counterexample, and imposes no lower bound on its
normalized cycle minimum. Overlapping-arc identities, templates with
growing periods, and reductions using integer-cycle arithmetic remain
possible. The general four-mismatch question remains open.

There is a separate immediate limitation for the half-turn encoding.
In that law's notation, let `G=2^172*(tN)^341`. If `N<=s`, then
`H_s>=s`, `Q^(N/H_s)<=Q<P`, `Cmax>=P/3`, and `Z>=1`.
Its numerical lower bound (D1) for the denominator is consequently
less than `3/G<1`. If two halves differ at two positions, every
half-length template repeated twice needs at least two substitutions:
`N=2<=s`. An expanding choice of template therefore gives a vacuous
denominator-one test from (D1); a nonexpanding choice is outside that
theorem. This is an algebraic limitation of the displayed bound,
not a new use of EXT-1 or a failure of the theorem.

**Relation to earlier work.** The unreviewed C014
[common-partition draft](../compatible-arcs-common-partition-limits/README.md),
especially [its mechanical one-marker construction](../compatible-arcs-common-partition-limits/COMPATIBLE_ARCS.md),
is the direct precursor: it has prime length, `rho=3`, and an
unbounded normalized minimum. Its limiting irrational slope also
obstructs bounded-period factors. The present argument rederives the
needed construction and adds the simultaneous near-critical,
`rho=4`, and linear-largest-letter restrictions; it neither assumes
nor upgrades that draft. The
[arbitrary-background example](../three-defect-arbitrary-background.md)
already shows that sparse rotations need not control internal word
complexity, with a noncoprime shift. Here the shift is coprime and the
failure concerns every chronological cut and every short-period
template.

Rotation Hamming distance and mechanical words are established
objects; compare Gabrić's
[*Words that almost commute*](https://arxiv.org/html/2110.01120v2).
The [periodic-dictionary manuscript](../../../../sources/lyapunov-weaver-2026-periodic-dictionary-complexity.md)
is a scope comparison, not an assumed theorem: a complexity lower
bound is compatible with the high complexity exhibited here.
Novelty is undetermined. The standard actual `3x+5`, `3x+7`,
`3x+13`, and `3x+61` cycles remain untouched; no cycle is excluded.

## History

- 2026-11-08: recorded the failed attempt to obtain bounded short-period
  descriptions from four-mismatch word structure. The finite certificate
  and same-session scrutiny do not constitute an independent review.
