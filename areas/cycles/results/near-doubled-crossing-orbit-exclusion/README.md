---
id: near-doubled-crossing-orbit-exclusion
kind: result
title: Finite signed crossing orbits exclude near-doubled cancellation for gaps through twelve
status: written
claim: >
  For raw odd-only 3x+1 valuation words, let u be any nonempty positive word of length n and total B.
  If v is obtained by raising one letter of u by 2j, with 1 <= j <= 12, then
  2^(B+j)+3^n does not divide C_(uv). If v instead transposes two letters of u whose
  absolute difference k satisfies 1 <= k <= 12, then 2^B+3^n does not divide C_(uv).
  These statements hold for every length, total, letter position and remaining positive
  letters, without a coprimality or near-critical hypothesis. In either case write the
  total of uv as 2S. If 2^S>3^n, then gcd(C_(uv),2^S+3^n)<2^S; when gcd(S,n)=1 this
  is the primitive half-cancellation bound at gcd(2S,2n)=2. The proof reduces the
  possible divisibility to signed 3x+(2^k-1) segments and certifies finite forward-closed
  crossing basins for 3 <= k <= 12, with exceptional endpoint orbits checked exactly.
authors:
  - Codex crossing research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [antiperiodic-intercept-nondivisibility]
certificates: [check_crossing.py]
evidence:
  - "check_crossing.json: all finite crossing seeds, forward-closed positive basins, and exceptional signed orbits used in the proof"
tags: [cycles, denominators, antiperiodic, near-doubled, transpositions, signed-orbits, controls]
---

# Finite signed crossing orbits exclude near-doubled cancellation for gaps through twelve

## Statement

For a positive valuation word `u=(a_0,...,a_(n-1))`, write `B=sum(u)`
and `C_u=sum_(i<n) 3^(n-1-i) 2^(sum_(r<i) a_r)`, as in
[`antiperiodic-intercept-nondivisibility`](../antiperiodic-intercept-nondivisibility/README.md).
The composition associated to `u` for `3x+d` is

```
x -> (3^n x+d C_u)/2^B.
```

**Theorem.** Let `w=uv`, where the two halves have the same length `n`.

- If `v` is obtained by increasing one letter of `u` by `2j`, for
  `1<=j<=12`, then `2^(B+j)+3^n` does not divide `C_w`.
- If `v` is obtained by transposing two distinct letters of `u`, whose
  absolute difference is `k` with `1<=k<=12`, then `2^B+3^n` does not
  divide `C_w`.

There is no bound on `n`, `B`, the other letters, or the positions of the
changes. In the first case put `S=B+j`, and in the second put `S=B`.
If `2^S>3^n`, then

```
gcd(C_w,2^S+3^n) < 2^S.
```

If also `gcd(S,n)=1`, the factor `2^S+3^n` is the primitive homogeneous
cyclotomic factor at `gcd(2S,2n)=2`, so this is the primitive
half-cancellation bound for the stated families. It is not an exclusion
of every four-mismatch word, and it makes no convergence claim.

The finite parameters are the ten auxiliary maps `3x+(2^k-1)` for
`3<=k<=12`. Their certified finite sets imply the claims for words of
arbitrary length. The cases `k=1,2` follow from the preceding node.

## Proof

### 1. Signed integer cuts and the finite crossing criterion

The signed endpoint lemma in the preceding node works with any odd
positive `d`: if the initial and final states in

```
2^B y = 3^n x+d C_u
```

are integers, every intermediate cut is integral. Indeed the prefix
intercept is multiplied by `d`, while the suffix multiplier remains an
odd power of 3, invertible modulo every power of 2. If the final state
is odd, all states are odd, and each division removes exactly the
power of 2 specified by the corresponding letter. Thus the segment
follows the signed odd-only map

```
S_d(x) = (3x+d)/2^v_2(3x+d).
```

Here `v_2` of a nonzero negative integer means `v_2` of its absolute
value. Zero cannot be an intermediate state: it is even, while every
cut before the odd endpoint must be odd.

Fix `k>=3` and put `d=2^k-1`. A signed segment from a negative odd
integer to a positive odd integer must have a first positive state.
If its predecessor is `-a`, then `a` is positive and odd, `3a<d`, and
that first positive state is

```
(d-3a)/2^v_2(d-3a).                                      (1)
```

The crossing letter is less than `k`, since `0<d-3a<2^k`.
Let `H_k` be a finite positive set containing all states (1) and closed
under `S_d`. Once the segment becomes positive, all subsequent states
belong to `H_k`. Therefore, if the last letter is at least `k+1`, the
crossing occurs before the last step, and the source of the last step
is a member of `H_k` whose exact valuation is at least `k+1`.

The certificate supplies such a set `H_k` for each `3<=k<=12`:

| `k` | `d=2^k-1` | `|H_k|` | Largest valuation in `H_k` |
|---|---|---|---|
| 3 | 7 | 3 | 3 |
| 4 | 15 | 1 | 3 |
| 5 | 31 | 18 | 6 |
| 6 | 63 | 8 | 4 |
| 7 | 127 | 98 | 10 |
| 8 | 255 | 93 | 7 |
| 9 | 511 | 346 | 8 |
| 10 | 1023 | 348 | 9 |
| 11 | 2047 | 1512 | 12 |
| 12 | 4095 | 915 | 11 |

The only arrows in these sets with valuation at least `k+1` are

```
k=5:       11 -> 1,       3*11+31   = 2^6;
k=7:      299 -> 1,       3*299+127 = 2^10;
k=11:     683 -> 1,       3*683+2047 = 2^12.              (2)
```

These statements are finite classifications verified by the certificate,
including exhaustive inclusion of the crossing seeds and closure of
every listed set. They do not assume that other `3x+d` orbits converge.

### 2. One changed letter

Suppose `v` raises the letter at position `i` by `2j`, and put
`P=2^(B+j)+3^n`, `d=2^j-1`. The preceding node's exact identity is

```
gcd(C_(uv),P) = gcd(d C_(u°),P),                           (3)
```

where `u°` is the rotation of `u` beginning after position `i` and
ending with the original letter `a_i`. Assume `P` divides `C_(uv)`.
Then `h=d C_(u°)/P` is a positive integer. It is odd, since `d`, `P`,
and the intercept `C_(u°)` are all odd.

Increase the last letter of `u°` by `j`, giving a word of length `n`,
total `B+j`, and unchanged intercept. The identity `d C_(u°)=P h`
then supplies a signed `3x+d` segment

```
-h -> h,
```

whose last letter is `c=a_i+j>=j+1`. Its intermediate cuts are integral
and odd by Step 1. For `3<=j<=12`, the finite crossing criterion and
(2) show that the last arrow must be one of the three arrows in (2),
with `h=1` and starting state `-1`.

For these three maps the certificate supplies finite forward-closed
sets containing `-1` and missing the required last source:

| `j` | `d` | Starting state | Size of signed closed set | Absent last source |
|---|---|---|---|---|
| 5 | 31 | -1 | 14 | 11 |
| 7 | 127 | -1 | 20 | 299 |
| 11 | 2047 | -1 | 180 | 683 |

The segment cannot reach its required last source, a contradiction.
For `j=1,2`, (3) and the preceding node already exclude divisibility:
the factor `2^j-1` is 1 or 3, coprime to `P`. This proves the
one-letter assertion for `1<=j<=12`.

### 3. Two transposed letters

Suppose `v` transposes letters at positions `i<h` whose absolute
difference is `k`. Write `z` for the intervening word, `l=|z|`,
`b=sum(z)`, `r=n-l-1>=1`, `P=2^B+3^n`, and `d=2^k-1`.
The preceding node proves

```
gcd(C_(uv),P) = gcd(d F(z),P),
F(z) = sum_(t=0)^l 3^(l-t) 2^(sum of the first t letters of z).        (4)
```

If `P` divides `C_(uv)`, then `h=d F(z)/P` is a positive odd integer.
Append `c=B-b` to `z`. The appended word has total `B`, length `l+1`,
and intercept `F(z)`, including when `z` is empty. Since
`d F(z)=(2^B+3^n)h`, it supplies the signed `3x+d` segment

```
-3^r h -> h.                                                        (5)
```

The two swapped letters sum to at least `k+2`; the other
`n-l-2` letters outside `z` are at least 1. Consequently

```
c = B-b >= k+2+(n-l-2) = k+r+1 >= k+2.                              (6)
```

For `3<=k<=12`, Step 1 applies. Of the arrows in (2), only the
`k=7` arrow has valuation at least `k+2`; it has `c=10`, `h=1`.
Inequality (6) then leaves only `r=1,2`, and (5) starts at `-3` or `-9`.
For `d=127`, the certificate supplies signed forward-closed sets of
sizes 23 and 40 containing these respective starts and omitting 299.
Thus neither segment can reach its necessary last source.

For `k=1,2`, the preceding node's coprime transposition argument applies.
This proves the transposition assertion for `1<=k<=12`.

### 4. The primitive bound

In either family, the plus factor is `P=2^S+3^n`. Its nondivisibility
makes `gcd(C_w,P)` a proper divisor of the odd integer `P`, hence at
most `P/3`. When `2^S>3^n`, this is less than `2^S`. If `gcd(S,n)=1`,
then `gcd(2S,2n)=2`, and this gcd is precisely the primitive cancellation
at the plus factor. No conclusion for the other cyclotomic indices
is needed or asserted.

## Certificates

[`check_crossing.py`](check_crossing.py) uses the Python standard library
and exact integers. It generates all negative-to-positive crossing seeds
for `d=2^k-1`, `3<=k<=12`, constructs their finite orbit closures, and
then checks explicitly that each set contains every seed and that every
row gives the exact legal successor inside the same set. The ten
positive sets contain 3,342 states in total. The full sets, valuations,
and successors are stored in [`check_crossing.json`](check_crossing.json).

It enumerates every high-valuation last arrow, every possible `r` in
(6), and verifies the five exceptional signed closed sets and the
absence of their required last sources. A resource guard during set
construction raises an error if no finite certificate has been obtained;
it cannot turn a truncated search into a passing check. The proof uses
the explicitly checked closure, not a stopping-time extrapolation.

The script also verifies actual sign crossings for each
`d in {5,7,13,61}`. All checks use explicit exceptions and still run
under `python3 -O`.

```
python3 areas/cycles/results/near-doubled-crossing-orbit-exclusion/check_crossing.py
```

By default the script compares its deterministic result with the committed
receipt; `--write-receipt` regenerates it.

## Remarks

**What this adds.** The preceding sign argument settled the one-letter
and transposition families only when `2^j-1` or `2^k-1` was coprime
to the plus factor. Here the factor is retained as the coefficient of
an auxiliary `3x+d` map, and the finite crossing analysis removes that
coprimality assumption for all parameters through 12. The finite range
is a range of modification sizes, not a bound on word length.

**Why the exceptions need their own check.** At `j=5` and `j=11`, the
largest basin valuation equals the permitted minimum final letter;
at `k=7`, it exceeds that minimum. A largest-valuation bound alone
would leave these cases open. The endpoint equation fixes the start
of each candidate segment, and its certified orbit misses the
required last source. This extra check closes those cases.

**Research target.** For larger parameters, classify feasible signed
segments and determine whether the near-critical constraint
`2^(2S)<2*3^(2n)` eliminates them. This requires control of the relevant
`3x+(2^k-1)` basins together with the endpoint, total-valuation, and
length constraints; this finite certificate supplies no such uniform
control. Four-mismatch half-pairs with two unequal changes that are
not a transposition, and general rotations, also remain outside the
scope of these two families.

**Controls.** Negative integers can cross to positive ones under
`3x+d`: the certificate verifies such a step from `-1` for each
`d in {5,7,13,61}`. The proof permits these crossings and uses their
exact subsequent orbits for the specific auxiliary maps. It excludes
neither those maps' actual positive cycles nor their signed crossings;
it excludes the additional endpoint and final-valuation conditions
forced by the proposed divisibility.

**Novelty and status.** Novelty undetermined. This is a written argument
with finite certificates. Same-session agent scrutiny is not an
independent review, and no Lean formalisation is claimed.

## History

- 2026-11-08: Derived by the Codex crossing research lane (GPT-6 Astra;
  directed by Santiago Armstrong) from the surviving noncoprime factors
  in the antiperiodic intercept result. Finite crossing basins and the
  exceptional signed endpoint orbits yield exclusions uniform in word
  length for modification parameters through 12.
