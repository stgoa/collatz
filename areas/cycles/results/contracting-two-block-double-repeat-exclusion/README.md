---
id: contracting-two-block-double-repeat-exclusion
kind: result
title: Two copies of a sufficiently large contracting block exclude denominator one
status: written
claim: >
  Raw odd-only valuation words. Let U,V be nonempty positive words with
  D_U,D_V>0 and D_U*C_V-D_V*C_U nonzero. Put M=max(len(U),len(V)),
  Q=2^sum(U), S=2^sum(V), and w=U^k V^ell with k,ell>=1. Under EXT-1,
  den(w)>max(Q^(k-1),S^(ell-1))/3^M.
  Therefore either repetition budget at least 3^M excludes denominator one. In particular,
  two copies suffice if Q>=3^M, including every pair of distinct
  equal-length contracting blocks with U repeated at least twice.
  Lengths, totals and repetition counts are unbounded; no primitivity,
  minimum-state or imported period assumption is used. The denominator
  bound for M<8192 is an exact finite consequence without EXT-1.
authors:
  - Codex residue research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [contracting-two-block-effective-exclusion]
assumes: [musson-collatz-gap-all]
certificates: [check_double_repeat.py]
evidence:
  - "check_double_repeat.json: exact gap comparisons, contracting interval and lattice checks, and genuine cycle controls"
tags: [cycles, denominators, contracting-blocks, repetition, third-period]
---

# Two copies of a sufficiently large contracting block exclude denominator one

## Statement

For a nonempty positive valuation word `W`, write

```
P_W=3^len(W),   Q_W=2^sum(W),   D_W=Q_W-P_W,
C_W=sum_(j=0)^(len(W)-1) 3^(len(W)-1-j) 2^(W_0+...+W_(j-1)).
```

Its affine action is `(P_W x+C_W)/Q_W`. The block is **contracting**
when `D_W>0`. The clock throughout is raw odd-only, with exact positive
valuation letters.

Let `U,V` be contracting blocks with distinct fixed points, equivalently

```
K=D_U C_V-D_V C_U !=0.
```

Set `M=max(len(U),len(V))`, `Q=Q_U`, `S=Q_V`, and consider `w=U^k V^ell`,
where `k,ell>=1`. Put `q=den(w)` and `F=Q^(k-1)`. Under the
replayed gap [EXT-1](../../../../sources/musson-collatz-gap-all.md),

```
q > max(Q^(k-1),S^(ell-1))/3^M.                      (1)
```

Thus either repetition budget at least `3^M` excludes `q=1`.
Two repetitions already suffice when
`Q>=3^M`. This includes a repeated block of maximal length, and also
a repeated block of maximal total, since every block is contracting.
The symmetric statement holds after exchanging `U,V` and rotating.

In particular, **distinct contracting blocks of the same length cannot
give denominator one in `U^k V^ell` when either repetition count is at
least two**. For equal lengths, distinct words imply `K!=0`, as proved
below. No equal-total hypothesis is imposed.

For `M<8192`, inequality (1) and its exclusion consequence use only the
exact finite comparisons in the certificate. The all-length form uses
EXT-1, applied to individual block lengths. No minimum-state computation,
published period lower bound or primitivity assumption is used. These
are denominator laws for actual reduced `3x+q` cycles; they do not
exclude genuine controls with `q>1`.

## Proof

### 1. Contracting intervals and the even lattice

This uses the interval and spacing mechanism of
[the contracting two-block theorem](../contracting-two-block-effective-exclusion/README.md).
For completeness, let

```
a=C_U/D_U,   b=C_V/D_V,   alpha=P_U/Q_U,   beta=P_V/Q_V,
t=alpha^k,  z=beta^ell.
```

Both slopes lie strictly between zero and one. If `x` is the normalized
cycle state before the first `U`, direct composition gives

```
x=a+(b-a)(1-z)/(1-tz).                              (2)
```

The coefficient in (2) is strictly between zero and one. Every state
at a block boundary therefore lies strictly between `a` and `b`.
These are normalized rational states; multiplication by `q=den(w)`
gives positive odd integers of the actual raw `3x+q` cycle.

Let `n_i` be those integer states before the `i`th consecutive copy
of `U`, for `0<=i<=k`, and let `Delta_i=n_(i+1)-n_i`. Then

```
Delta_i=(P_U/Q_U)^i Delta_0.
```

The initial difference is nonzero: otherwise `x=a`, contrary to (2)
and `a!=b`. Since `Delta_(k-1)` is even and `P_U` is odd, the exact
integer identity

```
P_U^(k-1) Delta_0=Q_U^(k-1) Delta_(k-1)
```

implies `2Q_U^(k-1)` divides `Delta_0`. Consequently

```
2F <= abs(Delta_0) < q abs(a-b) < q max(a,b).         (3)
```

The extra factor `2` here comes from the odd states; it is retained in
both the finite and large-length estimates. For `k=1`, the same conclusion
holds with `F=1` because `Delta_0` is a nonzero even integer.

### 2. A uniform bound on contracting fixed points

For any positive block of length `n`, total `A`, binary power `B=2^A`
and ternary power `P=3^n`, positivity bounds each prefix total by
`A-(n-j)`. Hence

```
0<C <= (B/2^n)(P-2^n) < BP/2^n.
```

If `B>P` and `eta=(B-P)/B`, its positive fixed point satisfies

```
C/(B-P) < (3/2)^n/eta.                              (4)
```

EXT-1 states `eta>=1/(2^172 n^341)`, with a weak inequality. The strict
intercept bound in (4) therefore gives

```
C/(B-P) < (3/2)^n 2^172 n^341.                     (5)
```

We prove the convenient uniform ceiling

```
C/(B-P) < 2*3^n                                    (6)
```

at every positive length. For `1<=n<8192`, let
`A_min=bit_length(3^n)`, the least integer with `2^A_min>3^n`.
The certificate checks every exact integer comparison

```
2^(n+1)(2^A_min-3^n) >= 2^A_min.                   (7)
```

The minimum ratio is exactly `1`, at `n=1`. The quantity `eta` increases
with `A`, so (7) implies `eta>=2^(-n-1)` for every contracting total.
Now (4) proves the strict inequality (6).

For `n>=8192`, choose the integer `j>=13` with `2^j<=n<2^(j+1)`.
Then

```
n-171-341 log2(n) > 2^j-171-341(j+1) >= 3247 >0.     (8)
```

The final expression equals `3247` at `j=13`; its increment is
`2^j-341>0`. Thus `2^172 n^341<2^(n+1)`. Combining with (5) again
proves (6). This step uses EXT-1; (7) is a local finite replay, not
an imported convergence computation.

### 3. The denominator law and equal-length corollary

By (6), `max(a,b)<2*3^M`. Equation (3) gives

```
2F < 2q*3^M,
```

which proves the `U` bound in (1). Rotate to start with `V` to obtain
the other bound. Either repetition budget at least `3^M` then excludes
denominator one.

If `U,V` have the same length and fixed point, that fixed point is a
positive rational whose reduced numerator and denominator are odd.
Each word's rotated-intercept identities show that scaling by this
denominator gives an actual positive odd cycle from the same state.
The raw `3x+q` map determines its valuation and successor uniquely.
The two equal-length valuation histories are therefore identical,
so `U=V`. Hence distinct equal-length blocks have `K!=0`. Their
contraction gives `Q_U>3^M`, proving the stated equal-length corollary.

### 4. An aligned third-period consequence

Suppose a word differs from `U^3` in two positions lying in one
length-`g` block after a cyclic cut. Write it as `V U U`.
The changes may have unequal magnitudes or the same sign. If both
`U` and `V` contract and they are distinct, they have the same length,
so the corollary excludes denominator one under EXT-1.

For a third-period four-mismatch word, this is the aligned placement
of its two exceptional majority-track entries. Their changes need not
balance. The unaligned placement has three distinct blocks and is not
covered by this theorem. If one of the aligned blocks expands, the
positive fixed-point interval argument also does not apply.

## Certificates

[`check_double_repeat.py`](check_double_repeat.py) checks all `8191`
integer comparisons in (7), the exact dyadic cutoff in (8), contracting
intervals, even lattice divisibility, and actual reduced `3x+q` arrows
on a declared finite grid. It tests the quantitative law (1), retaining
the actual denominator. Its receipt is
[`check_double_repeat.json`](check_double_repeat.json).

All eleven shared `3x+5`, `3x+7`, `3x+13` and `3x+61` cycles are replayed
as common-fixed-point controls; these have `K=0` and remain outside the
exclusion. The trivial all-`2` `3x+1` cycle is likewise retained. The
existing actual `3x+499` mixed-direction example is also replayed to
show why contraction cannot be omitted. These controls are not rescaled
into spurious integer `3x+1` cycles.

The finite grid tests the proof identities, not an absence-based
all-length exclusion. The only all-length outside input is EXT-1;
its proof is not re-run by this certificate. Commands from the repository
root:

```
python3 areas/cycles/results/contracting-two-block-double-repeat-exclusion/check_double_repeat.py
python3 -O areas/cycles/results/contracting-two-block-double-repeat-exclusion/check_double_repeat.py
```

The default verifies the committed receipt. `--write-receipt` regenerates
it deterministically.

## Remarks

The predecessor's unconditional formal theorem requires a block of
maximal total to occur at least three times, and gives `den(w)>2^M`.
Here the effective gap reduces the repetition threshold to two under
the explicit binary-size condition, at the cost of the EXT-1 assumption.
The old result and its proof remain unchanged. No novelty claim is made.

The [equal-total theorem](../equal-total-two-block-exclusion/README.md)
already excludes distinct equal-length, equal-total blocks with at least
three occurrences in total, unconditionally. The equal-length corollary
here allows unequal totals but requires both blocks to contract.
The [shared-background law](../shared-background-denominator-law/README.md)
and its fixed-marker resultant estimates are different restrictions.

The commutator hypothesis is essential: common-fixed-point words can
repeat genuine cycles indefinitely. Contraction is also essential to
this proof, as the
[mixed-direction obstruction](../../attempts/interval-trapping-expanding-blocks.md)
shows. No conclusion about arbitrary third-period words or general
four-mismatch rotations follows.

## History

- 2026-11-08: derived the two-copy extension while studying aligned
  unbalanced third-period changes. Retained the predecessor's interval
  mechanism, used even state differences, and replaced its coarse
  fixed-point ceiling by an EXT-1 estimate plus exact short-length
  comparisons. Same-session checks do not promote the `written` status.
