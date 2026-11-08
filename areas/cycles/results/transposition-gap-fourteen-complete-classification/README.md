---
id: transposition-gap-fourteen-complete-classification
kind: result
title: Gap-fourteen full plus cancellation has a unique transposition word
status: written
claim: >
  Raw odd-only valuation-word setting. Let u be any positive word of length n and total B,
  and let v transpose two letters of u whose absolute difference is 14. Then
  2^B+3^n divides C_(uv) if and only if, up to exchanging u and v,
  u=(1,z,15) and v=(15,z,1), where z is the valuation word of the first 187
  signed odd-only 3x+16383 steps from -63. In particular n=189, B=336,
  gcd(B,n)=21 and 2^(2B)>2*3^(2n). Thus no near-critical gap-fourteen
  transposition word cancels the whole plus factor, and none with gcd(B,n)=1
  does so at any distance from criticality. For 2^B>3^n and gcd(B,n)=1,
  its primitive cancellation at index 2 is strictly less than 2^B.
  The unrestricted classification is proved by a finite forward-closed positive crossing
  basin with 5472 states and a complete signed orbit with 659 distinct states;
  no bound on the input word length or its other letters is imposed.
authors:
  - Codex crossing research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [antiperiodic-intercept-nondivisibility, transposition-gap-fourteen-full-plus-cancellation]
certificates: [check_classification.py]
evidence:
  - "check_classification.json: all crossing seeds, complete finite positive closure, candidate last arrows, complete signed orbit, and the unique half-words"
tags: [cycles, denominators, transpositions, cancellation, near-critical, signed-orbits, classification]
---

# Gap-fourteen full plus cancellation has a unique transposition word

## Statement

Let `u` be a word of positive valuations, of length `n` and total `B`,
and let `v` be obtained by transposing two letters of `u` whose absolute
difference is 14. Set `w=uv`, `P=2^B+3^n`, and use the usual intercept
`C_w=sum_(i<2n) 3^(2n-1-i) 2^(sum_(j<i) w_j)`.

**Theorem.** `P` divides `C_w` if and only if the ordered pair `(u,v)`
is one of

```
((1,z,15),(15,z,1)),       ((15,z,1),(1,z,15)),
```

where `z` is the valuation word of the first 187 signed odd-only
`3x+16383` steps from `-63`. This is the word constructed in
[`transposition-gap-fourteen-full-plus-cancellation`](../transposition-gap-fourteen-full-plus-cancellation/README.md).
In particular every such cancellation has

```
n=189,     B=336,     gcd(B,n)=21,     2^(2B)>2*3^(2n).
```

The classification concerns the specified cut `w=uv`. Exchanging the
halves rotates `w` by `n`; arbitrary rotations need not retain a
transposition relation between the new halves.

**Consequences.** Complete plus-factor cancellation is impossible for
every near-critical gap-fourteen transposition word, namely those with
`3^(2n)<2^(2B)<2*3^(2n)`. It is also impossible whenever `gcd(B,n)=1`,
even without the near-critical restriction. In the latter case, when
`2^B>3^n`,

```
gcd(C_w,2^B+3^n) < 2^B;
```

this is the primitive half-cancellation bound at `gcd(2B,2n)=2`.
The theorem does not bound the complete cancellation `gcd(C_w,2^(2B)-3^(2n))`
for other near-critical words, and it does not settle the general
four-mismatch question.

## Proof

### 1. Every possible cancellation gives a forced signed segment

Write `k=14`, `d=2^k-1=16383`, and let the changed positions be `i<h`.
Let `z'` be the word strictly between them, `l=|z'|`, `b=sum(z')`, and
`r=n-l-1>=1`. Define

```
F(z') = sum_(t=0)^l 3^(l-t) 2^(sum of the first t letters of z').
```

The transposition identity of
[`antiperiodic-intercept-nondivisibility`](../antiperiodic-intercept-nondivisibility/README.md)
gives

```
gcd(C_w,P) = gcd(d F(z'),P).                             (1)
```

Assume `P | C_w` and put `q=d F(z')/P`. This is a positive odd integer:
`d`, `P`, and `F(z')` are odd. Append the letter `c=B-b` to `z'`.
Its intercept is `F(z')`, its total is `B`, and its length is `l+1`.
The equality `d F(z')=Pq` is exactly its signed endpoint identity

```
2^B q = 3^(l+1)(-3^r q)+d F(z').                       (2)
```

Every intermediate cut is integral: in the proof of the cited signed
endpoint lemma, replacing every prefix intercept by `d` times that
intercept leaves the odd suffix multiplier invertible modulo powers
of 2. Since `d` and the endpoint `q` are odd, every state is odd and
every division is exact. Thus `(z',c)` is a genuine signed odd-only
`3x+d` segment from `-3^r q` to `q`. The zero state cannot occur in
this segment because every state is odd.

The two swapped letters sum to at least `k+2`; there are `n-l-2`
other letters outside `z'`, each at least 1. Hence

```
c >= k+2+(n-l-2) = k+r+1 >= 16.                        (3)
```

### 2. A finite positive closure contains every possible last source

For the signed map

```
S_d(x)=(3x+d)/2^v_2(3x+d),
```

use the valuation of the absolute value for negative numerators.
A negative-to-positive crossing has predecessor `-a`, where `a` is
positive and odd and `3a<d`; its positive output is

```
(d-3a)/2^v_2(d-3a).                                    (4)
```

Its valuation is less than 14 because `0<d-3a<2^14`.
By (3), the crossing in (2) occurs before the last step.

The certificate enumerates all states (4), obtaining 1,365 distinct
positive seeds. It supplies a set `H` of 5,472 positive odd states
which contains all those seeds and is forward closed under `S_d`.
Every row is verified by exact arithmetic, including its exact
valuation and successor in `H`. Therefore, after the first crossing,
every state of (2), in particular its last source, belongs to `H`.

The certificate checks all rows in `H`. Its largest valuation is 16,
and its only arrow with valuation at least 16 is

```
453291 -> 21,       3*453291+16383 = 2^16*21.             (5)
```

Equations (2), (3), and (5) force

```
c=16,       q=21,       r=1,       initial state=-63.    (6)
```

The set `H` is used as a finite closed certificate. No convergence
claim about arbitrary positive or negative `3x+d` orbits is used.

### 3. The forced signed orbit reaches the last source exactly once

The certificate gives the complete signed orbit from `-63` until its
first repeated state. There are 659 distinct states. Numbering the
initial state by 0, the repeated cycle begins at index 407 with state
4155 and has length 252. Every arrow is checked, the 659 listed states
are pairwise distinct, and the last successor equals the state at
index 407. Thus the list describes the entire future orbit.

The state 453291 appears exactly once, at index 187, before that
cycle. The first 187 valuations sum to 320 and are exactly the word
`z` in the statement. Consequently the segment in (2) has

```
z'=z,       l=187,       b=320,       n=l+r+1=189,
B=b+c=336.                                             (7)
```

Because `r=1`, there are no other letters outside `z'`: the swapped
letters must be the first and last letters of `u`. Their sum is
`c=16` and their absolute difference is 14, so they are 1 and 15.
This proves the necessary form of the ordered pair `(u,v)`.

For sufficiency, the witness node proves that its pair cancels `P`;
the present certificate independently checks the identity

```
16383 F(z) = 21*(2^336+3^189)
```

and the resulting divisibility in (1). Exchanging `u` and `v` changes
the sign of their intercept difference modulo `P`, so it preserves
the divisibility. The two pairs in the statement therefore both work.

### 4. Near-critical and primitive-factor consequences

The exact integer computations give `gcd(336,189)=21` and
`2^672>2*3^378`. Hence none of the classified pairs is near critical,
and none has `gcd(B,n)=1`.

For any gap-fourteen transposition with `gcd(B,n)=1`, `P` consequently
fails to divide `C_w`. Its gcd with `C_w` is a proper divisor of the
odd integer `P`, hence at most `P/3`. When `2^B>3^n`, this is less
than `2^B`. Under `gcd(B,n)=1`, the cyclotomic index is
`gcd(2B,2n)=2`, whose homogeneous factor is exactly `P`.

## Certificates

[`check_classification.py`](check_classification.py) uses only standard
Python and exact integers. It constructs the crossing closure and then
checks every seed, state, successor, and valuation. It enumerates every
candidate last arrow and every `r` allowed by (3). For the single
candidate it certifies the entire signed orbit, including its cycle
closure, its distinct states, and the unique hit on 453291.

It also reconstructs the unique half-words, checks the endpoint and
intercept identities, verifies the exact total cancellation of the
witness, and checks the stated gcd and near-critical comparisons.
The receipt [`check_classification.json`](check_classification.json)
contains all finite sets and the complete signed orbit; its size is
below 1 MB. Fixed resource guards fail if a finite certificate cannot
be obtained. No truncated trajectory is accepted as proof.

```
python3 areas/cycles/results/transposition-gap-fourteen-complete-classification/check_classification.py
```

By default the script compares its deterministic output byte for byte
with the receipt; `--write-receipt` regenerates it. It uses explicit
exceptions rather than `assert`, so checks also hold under `python3 -O`.

## Remarks

**What is classified.** The prior node supplied one far-from-critical
counterexample. The finite closure here proves that every gap-fourteen
transposition with complete plus-factor cancellation is that same
specified pair, up to exchanging halves. The result covers arbitrary
input word length and arbitrary other letters; no word census cutoff
is involved.

**Why a complete signed orbit matters.** A first-hit search would leave
open whether the required last source is reached again after a cycle.
The complete orbit certificate places 453291 strictly before the cycle,
so it can never recur. This is what fixes the word length rather than
just finding its smallest value.

**The finite reduction in general.** For a fixed `k`, a certified finite
crossing basin gives finitely many possible last arrows. Each arrow
gives finitely many `r` through `c>=k+r+1`, hence finitely many forced
signed starts. If those signed trajectories have finite closure, hits
on a required last source are either a single transient hit or occur
periodically on a positive cycle. In the periodic case, each cycle
repetition adds its length `p` and valuation total `A_c`, multiplying
`2^B/3^n` by `2^A_c/3^p>1`: positivity of the cycle and its composition
identity give `(2^A_c-3^p)x=d C_cycle>0`.

Thus each periodic candidate admits an exact finite test for the
near-critical interval `1<2^B/3^n<sqrt(2)`: check its first admissible
value above 1, reached after finitely many repetitions, and compare
its square with 2. Later values are larger. This reduction is
conditional on supplying the relevant finite closures; it does not
assume their existence for every `k`. Here the unique last source is
transient, so no periodic family remains.

**Controls and scope.** The proof allows signed crossings in `3x+d`
and uses their actual forward dynamics. The certificate also checks
crossings for `d in {5,7,13,61}`. The classified witness itself is a
positive cycle for a different parameter as verified in its node.
Nothing excludes those controls or proves uniqueness of the positive
`3x+1` orbit component.

**Novelty and status.** Novelty undetermined. This is a written
classification with exact finite certificates; no Lean formalisation
or independent-session review is claimed.

## History

- 2026-11-08: Written by the Codex crossing research lane (GPT-6 Astra;
  directed by Santiago Armstrong), strengthening the gap-fourteen
  witness into a complete classification through the crossing basin
  and the entire forced signed orbit.
