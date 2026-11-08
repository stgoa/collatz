---
id: equal-amplitude-half-defect-normal-form
kind: result
title: Equal-amplitude half defects reduce to a balanced transfer
status: written
claim: >
  Raw odd-only 3x+1 valuation words. Let u,v be positive words of the same
  length n, differing at exactly two positions, with the absolute change
  equal to the same integer k at both positions. Write sum(u)+sum(v)=2S.
  For every k>=1, a cyclic rotation of uv has halves U,V of equal total S
  differing by a transfer +k,-k; the gcd of its intercept with
  P=2^S+3^n is unchanged. The balanced transfer has the same middle-intercept
  gcd and positive-letter fillability as a transposition. Consequently,
  for 1<=k<=12, P does not divide C_(uv), for every length, total and
  other positive letters. If 2^S>3^n then gcd(C_(uv),P)<2^S; if also
  gcd(S,n)=1, this is the primitive half-cancellation bound at index 2.
authors:
  - Codex cycle research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [near-doubled-crossing-orbit-exclusion]
certificates: [check_normal_form.py]
evidence:
  - "check_normal_form.json: exact checks of rotation invariance, balanced normalization, the middle-intercept identity, fillability and genuine non-swap near-critical examples"
tags: [cycles, denominators, near-doubled, balanced-transfer, normal-form, signed-orbits]
---

# Equal-amplitude half defects reduce to a balanced transfer

## Statement

Let `u,v` be positive valuation words of equal length `n>=2`, differing
at exactly two positions `i<h`. Suppose

```
|v_i-u_i| = |v_h-u_h| = k >= 1.
```

Each signed change is either `+k` or `-k`, so `sum(u)+sum(v)` is even;
write it as `2S`. Set `w=uv` and `P=2^S+3^n`.

**Normal form, for every `k`.** A cyclic rotation of `w`, allowing an
exchange of its halves, has the form `UV`, where `sum(U)=sum(V)=S`
and `V` is obtained from `U` by adding `k` at one position and
subtracting `k` at another. The gcd with `P` is invariant under this
rotation. A balanced transfer need not literally swap the two letters.

**Exclusion for `1<=k<=12`.** For every such pair, `P` does not divide
`C_w`. There is no bound on the length, total, positions, or other
letters, and no coprimality or near-critical hypothesis. If `2^S>3^n`,
then `gcd(C_w,P)<2^S`. If also `gcd(S,n)=1`, `P` is the primitive
homogeneous cyclotomic factor at index `gcd(2S,2n)=2`, so this is the
primitive half-cancellation bound.

This enlarges the transposition family of
[`near-doubled-crossing-orbit-exclusion`](../near-doubled-crossing-orbit-exclusion/README.md).
It includes balanced transfers between unequal endpoint letters and two
equal increases or decreases. For example, the near-critical half-pairs

```
u=(1,1,1,1,4),  v=(2,1,1,1,3),       a non-swap balanced transfer;
u=(1,1,1,1,3),  v=(2,1,1,2,3),       two equal increases,
```

both have `n=5`, `S=8`, `k=1` and `gcd(S,n)=1`. Their near-criticality
is the exact inequality `3^10 < 2^16 < 2*3^10`.

The theorem does not cover unequal absolute changes, arbitrary
non-half-period rotations, or all four-mismatch words.

## Proof

### 1. Rotation preserves the relevant gcd

For any positive word `a` of length `m` and total `A`, the intercept
identity for one left rotation is

```
2^a_0 C_(R_1 a) = 3 C_a + (2^A-3^m).                 (1)
```

This follows by moving the first term of the intercept sum to the
last position and shifting the remaining prefix sums. For `w`,
`2^A-3^m=(2^S-3^n)P`. Both 2 and 3 are units modulo `P`. Reducing
(1) modulo `P` proves `gcd(C_(R_1 w),P)=gcd(C_w,P)`, and iteration
proves invariance under every cyclic rotation. This works whether or
not `2^S>3^n`.

### 2. Two equal changes become opposite changes at another cut

If the changes have opposite signs, `sum(u)=sum(v)=S` already. If
they are both negative, exchange `u` and `v`, a rotation by `n`, to
make both positive. It remains to consider `v_i=u_i+k`, `v_h=u_h+k`.

Cut at `r=i+1`, between the changed positions, and rotate `w` left
by `r`. Its two new halves are

```
U = u[r:n] ++ v[0:r],
V = v[r:n] ++ u[0:r].                              (2)
```

Since exactly one changed position is in each part of the cut,
both new totals equal `sum(u)+k=S`. At the moved position `h-r`,
`V-U=+k`; at the moved position `i+n-r=n-1`, `V-U=-k`.
All other letters agree. Every letter remains positive. Equation
(1) ensures the normalization preserves the gcd with `P`.

### 3. A balanced transfer has the transposition intercept identity

Take positive `U,V` of equal total `S` with changes at positions
`a<b`. By exchanging halves if necessary, assume
`V_a=U_a+k`, `V_b=U_b-k`. Let `z` be the word between those positions,
with length `l=b-a-1` and total `b_z`. Define

```
F(z)=sum_(t=0)^l 3^(l-t) 2^(sum of the first t letters of z).
```

The prefix sums increase by `k` exactly at positions `a+1,...,b`.
Writing `p=sum_(t<=a) U_t` and factoring the changed intercept terms
gives

```
C_V-C_U = (2^k-1) 2^p 3^(n-1-b) F(z).
```

Concatenation gives `C_(UV)=3^n C_U+2^S C_V`. Since `3^n=-2^S`
modulo `P`, and powers of 2 and 3 are units there,

```
gcd(C_(UV),P)=gcd((2^k-1)F(z),P).                    (3)
```

The derivation uses a balanced transfer, not equality of the two
endpoint letters after exchange.

### 4. The same finite signed-crossing certificate applies

Set `d=2^k-1`, `r=n-l-1>=1`, and `c=S-b_z`. Positivity of both halves
forces `U_a>=1` and `U_b>=k+1`; the other `n-l-2` letters outside `z`
are at least 1. Hence

```
c >= (k+2)+(n-l-2) = k+r+1.                        (4)
```

Suppose `P | C_(UV)`. By (3), `H=d F(z)/P` is a positive odd integer.
Appending `c` to `z` gives a positive word of length `l+1`, total `S`,
and intercept `F(z)`. Its endpoint equation is

```
2^S H = 3^(l+1)(-3^r H)+d F(z).
```

The signed cut lemma in the preceding node forces this to be an
actual signed odd-only `3x+d` segment from `-3^r H` to `H`, with
last valuation `c>=k+r+1`.

For `k=1,2`, the coprime argument of the preceding node excludes
(3): the factor `2^k-1` is 1 or 3, a unit modulo `P`.

For `3<=k<=12`, use its certified positive crossing basins. The
only arrow of valuation at least `k+2` in those basins occurs at
`k=7`, with `299 -> 1` and valuation 10. Thus the only possibilities
for the last arrow have `H=1`, `c=10`, and by (4), `r=1` or `r=2`.
The required initial states would be `-3` or `-9`. The preceding
certificate gives finite forward-closed sets containing these
respective starts and omitting 299. Neither segment can reach its
required last source. This contradiction proves `P` does not divide
`C_(UV)`, hence does not divide `C_w`.

Every finite fact used here is already part of
[`check_crossing.py`](../near-doubled-crossing-orbit-exclusion/check_crossing.py)
and its committed receipt. The new part is that (3) and (4) require
only a balanced transfer, and (2) brings all equal-amplitude pairs
into that form.

Finally, if `2^S>3^n`, a proper divisor of the odd integer
`P=2^S+3^n` is at most `P/3<2^S`. For `gcd(S,n)=1`, the primitive
factor of `2^(2S)-3^(2n)` is `P`, giving the last assertion.

## Certificates

[`check_normal_form.py`](check_normal_form.py) checks normalization,
cyclic-rotation gcd invariance, identity (3), inequality (4), and the
claimed exclusion for all tested pairs. The finite family comprises
all base halves of length 2 through 5 with letters in `{1,2,3}`;
all two-position choices, signs and amplitudes 1 through 12 for
which the modified half stays positive; and additional balanced
families at every amplitude through 12. It verifies the two explicit
non-swap examples above. Its deterministic receipt is
[`check_normal_form.json`](check_normal_form.json).

The certificate uses exact integers, the Python standard library,
and explicit failures that remain active under `python3 -O`.

```
python3 areas/cycles/results/equal-amplitude-half-defect-normal-form/check_normal_form.py
```

By default the receipt must match; `--write-receipt` regenerates it.
These finite algebra checks complement the unrestricted normalization
argument and the preceding node's finite crossing certificates.

## Remarks

- **Research consequence.** In the half-period four-mismatch case,
  equal absolute changes through 12 are now covered even when the
  halves have different totals and do not swap letters. The remaining
  half-pairs have unequal amplitudes, or equal amplitudes above 12;
  general rotations need further arguments. The near-critical
  requirement may impose additional restrictions on their signed
  endpoint constructions.
- **Scope and controls.** The normal form is an algebraic statement
  about positive valuation words. The exclusion retains the exact
  auxiliary `3x+(2^k-1)` crossing analysis, which permits sign changes
  and actual positive cycles of those maps. No cycles of `3x+5`,
  `3x+7`, `3x+13` or `3x+61` are excluded.
- **Novelty and status.** Novelty undetermined. This is a written
  proof with finite certificates and explicit dependencies; no
  independent-session review or Lean formalisation is claimed.

## History

- 2026-11-08: Derived by the Codex cycle research lane (GPT-6 Astra;
  directed by Santiago Armstrong) while identifying which half-pair
  cases remained after the signed-crossing exclusion. Equal raises
  initially gave a masked-intercept proof, but the cyclic-cut normal
  form subsumes that argument and transfers the stronger exclusion
  through amplitude 12.
