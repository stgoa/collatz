---
id: antiperiodic-intercept-nondivisibility
kind: result
title: Positive valuation words have no integral antiperiodic starting point
status: written
claim: >
  For the affine compositions of the raw odd-only 3x+1 map, let z be any nonempty
  word of positive valuations, of length n, total B and intercept C_z. For all
  positive integers s,t, 2^B*t + 3^n*s does not divide C_z. In particular
  2^(B+j) + 3^n does not divide C_z for every integer j >= 0, without a bound on
  n, B or the letters. Consequently, if v is obtained from u by raising one
  letter by 2j, j >= 1, and N = 2^(sum(u)+j) + 3^length(u) is coprime to
  2^j-1, then N does not divide C_(uv). This coprimality always holds for j=1,2.
  The analogous exclusion holds when v transposes two letters of u whose
  positive difference k satisfies gcd(2^k-1,2^sum(u)+3^length(u))=1, in particular
  k=1,2. For either family with even total 2S, D_(uv)>0 and
  gcd(S,length(u))=1, the primitive cancellation of uv is less than 2^S.
authors:
  - Codex cycle research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex formalisation lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
lean:
  - LeanLane.SignedIntercept.negative_endpoint
  - LeanLane.SignedIntercept.not_dvd_intercept
  - LeanLane.SignedIntercept.not_dvd_power_plus
certificates: [check_antiperiodic.py]
evidence:
  - "check_antiperiodic.json: deterministic finite checks of the nondivisibility, the signed cut argument, one-letter gcd identity and 3x+d controls"
tags: [cycles, denominators, antiperiodic, one-letter, signed-orbits]
---

# Positive valuation words have no integral antiperiodic starting point

## Statement

For a nonempty positive valuation word `z = (a_0,...,a_(n-1))`, set
`B = sum(z)`, `P_i = sum_(r<i) a_r` and
`C_z = sum_(i<n) 3^(n-1-i) 2^P_i`. Its affine composition is
`F_z(x) = (3^n x + C_z)/2^B`.

For every pair of integers `s,t >= 1`,

```
(2^B t + 3^n s) does not divide C_z.                (1)
```

The theorem concerns the raw odd-only `3x+1` affine word maps. It does not
assume that an arbitrary rational input realises the prescribed valuations.
The proof establishes the intermediate integrality needed for its hypothetical
integer input. Taking `s=1`, `t = 2^j` answers the clean-intercept target in
[`primitive-cancellation-below-half`](../../questions/primitive-cancellation-below-half.md)
and in the remarks of
[`near-doubled-words-primitive-factor-test`](../near-doubled-words-primitive-factor-test/README.md),
for every `j >= 0` and every positive word.

**One-letter consequence.** Let `u` have length `n >= 1` and total `B`, and let
`v` differ from `u` only at position `i`, where its letter is larger by `2j`,
`j >= 1`. Write `S = B+j`, `w = uv`, `N = 2^S+3^n` and
`u° = (u_(i+1),...,u_(n-1),u_0,...,u_i)`. If
`gcd(2^j-1,N)=1`, then `N` does not divide `C_w`. In particular this holds
for `j=1` and `j=2`, since `N` is coprime to 3.

If `2^S>3^n`, the cancellation `gcd(C_w,N)` is then a proper divisor of `N`,
so is at most `N/3 < 2^S`. When `gcd(S,n)=1`, the homogeneous cyclotomic
factor indexed by `gcd(2S,2n)=2` is precisely `N`; thus this is the primitive
half-cancellation bound for the stated one-letter family. No near-critical
assumption is needed. The general four-mismatch question remains open.

**Transposition consequence.** If `v` instead swaps two distinct letters
of `u`, of absolute difference `k`, then `P=2^B+3^n` does not divide `C_(uv)`
provided `gcd(2^k-1,P)=1`. Again `k=1,2` always satisfy this condition.
When `D_(uv)>0` and `gcd(B,n)=1`, the primitive cancellation is less than
`2^B`. This conclusion places no bound on the lengths, totals, other letters,
or the positions of the two swapped letters.

## Proof

**Integer endpoints force integer cuts, including negative inputs.** Suppose
`x,y` are integers and

```
2^B y = 3^n x + C_z.
```

For the prefix of length `i`, let its intercept be `C_i` and the suffix
intercept be `E_i`. Composition gives

```
C_z = 3^(n-i) C_i + 2^P_i E_i.
```

Reducing the endpoint equation modulo `2^P_i` shows
`2^P_i | 3^(n-i)(3^i x+C_i)`. Since 3 is odd, it follows that

```
x_i = (3^i x+C_i)/2^P_i
```

is an integer at every cut. These integers obey
`2^a_i x_(i+1) = 3x_i+1`, with `x_0=x` and `x_n=y`. This is the signed
integrality part of the endpoint argument; its proof is included because
the positive-state statement of
[`excursion-cut-lemma`](../excursion-cut-lemma.md) does not itself cover
negative initial states. For `i<n`, the relation also forces `x_i` odd.
The endpoint need not be odd, and the last division need not remove the
entire power of two.

**Sign preservation.** If `x_i` is a negative integer, then `3x_i+1 <= -2`.
Hence the next integer `x_(i+1)` is negative. Thus no integral word segment
of `3x+1` goes from a negative integer to a positive integer.

If (1) failed, put `k = C_z/(2^B t+3^n s)`. Since `C_z>0`, `k` is a positive
integer. The word equation would be

```
3^n (-s k) + C_z = 2^B (t k).
```

The integral cuts just proved would give a segment from `-sk<0` to `tk>0`,
contradicting sign preservation. This proves (1).

**The one-letter factor must be retained.** Split the intercept of `u` as
`C_u=P+Q`, with `P` the terms at positions at most `i`, and `Q` those at
positions greater than `i`. Then

```
C_v = P+2^(2j) Q,
2^j C_u-C_v = (2^j-1)(P-2^j Q).
```

The concatenation identity `C_w=3^n C_u+2^B C_v` and
`3^n = -2^(B+j) (mod N)` imply

```
gcd(C_w,N) = gcd((2^j-1)(P-2^j Q),N).
```

For `r = sum_(a<=i) u_a`, direct rotation of the two sums gives

```
3^(n-1-i) 2^r C_(u°) = 3^n Q + 2^B P
                       = 2^B(P-2^j Q) (mod N).
```

Both 2 and 3 are units modulo `N`; consequently

```
gcd(C_w,N) = gcd((2^j-1) C_(u°),N).                 (2)
```

This re-derives the identity in
[`doubled-words-periodic-and-antiperiodic-points`](../doubled-words-periodic-and-antiperiodic-points/README.md).
Under the stated coprimality, `N | C_w` would imply `N | C_(u°)`, contrary
to (1) with `t=2^j`. The proper-divisor bound follows because `N` is odd,
and `N<2^(S+1)` when `2^S>3^n`.

**Transpositions.** Suppose instead that `v` swaps distinct letters at
positions `i<h` of `u`, whose difference in absolute value is `k>=1`.
Both halves now have total `B`. Put `P=2^B+3^n`, let `z` be the word
strictly between those positions, of length `l=h-i-1` and total `b`, and
write

```
F(z) = sum_(r=0)^l 3^(l-r) 2^(sum of the first r letters of z).
```

Only prefix sums at positions `i+1,...,h` change in the intercept. Their
difference factors as a sign times a power of 2 times a power of 3 times
`(2^k-1)F(z)`. The equal-total concatenation identity therefore gives

```
gcd(C_(uv),P) = gcd((2^k-1)F(z),P).                (3)
```

Append the positive letter `c=B-b` to `z`; it is positive because `B`
also includes the two swapped letters. The resulting word has total `B`,
length `l+1<=n`, and intercept exactly `F(z)`, including when `z` is empty.
Applying (1) to this appended word with `s=3^(n-l-1)`, `t=1` proves
`P` does not divide `F(z)`.
Thus `P` does not divide `C_(uv)` whenever `gcd(2^k-1,P)=1`; in particular
for `k=1,2`. If `D_(uv)>0`, the same proper-divisor argument bounds
`gcd(C_(uv),P)<2^B`, and if `gcd(B,n)=1` this is the primitive factor.

This transposition consequence uses the same sign obstruction as (1).

## Certificates

[`check_antiperiodic.py`](check_antiperiodic.py) uses exact integer arithmetic
and the standard library. It checks all positive words of length at most 6
and total at most 14: (1) for `s,t=1,...,16`; signed endpoint integrality for
integer starts `-9,...,9`; and (2) for every letter position and `j=1,...,6`,
including the nondivisibility conclusion whenever its coprimality condition
holds; and (3) for every pair of distinct letters, including its coprime
exclusion. It also checks the `3x+d` countercontrols below. These finite checks
support the formulas; the unrestricted theorem is the proof above.

Run from the repository root:

```
python3 areas/cycles/results/antiperiodic-intercept-nondivisibility/check_antiperiodic.py
```

The script compares its output with
[`check_antiperiodic.json`](check_antiperiodic.json). Use `--write-receipt` to
regenerate that receipt.

## Lean

The central signed endpoint and nondivisibility theorems are formalised in
[`LeanLane/SignedIntercept.lean`](../../../../lean/LeanLane/SignedIntercept.lean),
using the shared integer intercept `LeanLane.Words.C`.

- `negative_endpoint` says that for any natural-number word `w` and integers
  `x,y`, if `x<0` and `2^sum(w)*y=3^length(w)*x+C(w)`, then `y<0`.
  Its induction obtains an integral cut by cancelling an odd power of 3
  from divisibility by a power of 2, and propagates the negative sign.
- `not_dvd_intercept` proves (1) for every nonempty `w` and positive
  integers `s,t`, with no bound on length or entries.
- `not_dvd_power_plus` is the stated clean-intercept corollary
  `2^(sum(w)+j)+3^length(w)` does not divide `C(w)` for every natural `j`.

The formal word entries may be zero, so these statements are stronger
than their restriction to positive valuation words in this node. They
use exactly the same `C(w)`, defined recursively by `C([])=0` and
`C(a::w)=3^length(w)+2^a*C(w)`, and no assumption of orbit convergence.
The one-letter and transposition gcd identities and their primitive-factor
corollaries remain written proofs; the status of this whole node therefore
remains `written`.

Build and axiom evidence is in
[`SignedIntercept.build.txt`](../../../../lean/receipts/SignedIntercept.build.txt),
[`SignedIntercept.axioms.txt`](../../../../lean/receipts/SignedIntercept.axioms.txt),
and [`SignedIntercept.sha256.txt`](../../../../lean/receipts/SignedIntercept.sha256.txt).
Only `propext`, `Classical.choice` and `Quot.sound` occur. The module is
included in `LeanLane.lean` and built by `lake build LeanLane`.

## Remarks

- **What is settled.** The clean-intercept divisibility target is impossible
  for every positive word, and the one-letter and transposition families
  are settled whenever their explicit factor `2^j-1` or `2^k-1` is a unit
  modulo the plus factor. This replaces bounded
  absence of hits by a proof on that family.
- **What is not inferred.** The older near-doubled node writes its one-letter
  reduction without the factor `2^j-1`; the later doubled-word identity (2)
  retains it. This proof does not cancel that factor without coprimality,
  and does not settle the nonunit cases of either family.
  For example `u=(1)`, `v=(9)`, `j=4` gives `N=35`,
  `gcd(C_(uv),N)=gcd(5,35)=5`, whereas `gcd(C_(u°),N)=1`.
  This demonstrates that the factor changes the gcd; it is not a
  counterexample to the full-divisibility equivalence as written there.
- **Controls and the role of `+1`.** For `3x+d`, negative integers need not
  stay negative. With the one-letter word `(1)`, for each
  `d in {5,7,13,61}` put `t=(d-3)/2`. Then
  `(3(-1)+d)/2=t>0`, and `2t+3=d` divides `d C_(1)=d`.
  Thus the proposed `3x+d` extension of (1) fails on all four controls.
  The theorem excludes no actual positive cycle of any of these maps.
- **Novelty.** Undetermined. The proof is elementary; its use here is to
  resolve a stated intercept subtarget and isolate the remaining factor.
- **Status.** The central theorem is formalised as described above; the
  additional family corollaries remain written. No independent-session
  review is claimed.

## History

- 2026-11-08: derived by the Codex cycle research lane (GPT-6 Astra; directed
  by Santiago Armstrong) while investigating the surviving near-critical
  cancellation question. The proof and certificate were prepared in the
  same authoring session.

- 2026-11-08: the signed endpoint theorem, central nondivisibility theorem,
  and clean-intercept corollary were formalised in Lean by the Codex
  formalisation lane (GPT-6 Astra; directed by Santiago Armstrong).
  The full node remains `written` because its family-specific gcd
  identities and primitive-factor corollaries are not yet formalised.
