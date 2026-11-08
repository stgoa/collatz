---
id: unequal-one-three-half-defect-exclusion
kind: result
title: Half defects of amplitudes one and three cannot cancel the plus factor
status: written
claim: >
  Raw odd-only 3x+1 valuation words. Let u,v be positive words of the same
  length n, differing at exactly two positions whose absolute changes
  are 1 and 3, in either order and with arbitrary signs. Write
  sum(u)+sum(v)=2S and P=2^S+3^n. Then P does not divide C_(uv), for
  every length, total, position and remaining positive letters. If
  2^S>3^n, then gcd(C_(uv),P)<2^S; when gcd(S,n)=1, this is the
  primitive half-cancellation bound at index 2. The proof converts a
  hypothetical divisibility to an integral signed segment with additive
  coefficients consisting of a block of 2 followed by 3, or 3 followed
  by 2; its endpoint and last-valuation conditions are impossible.
authors:
  - Codex cycle research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex formalisation lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [antiperiodic-intercept-nondivisibility]
lean:
  - LeanLane.WeightedCrossing.trace_of_endpoint
  - LeanLane.WeightedCrossing.no_crossing_two_three
  - LeanLane.WeightedCrossing.no_crossing_three_two
  - LeanLane.WeightedCrossing.zero_interface_control
certificates: [check_one_three.py]
evidence:
  - "check_one_three.json: sign/order normalization, weighted-intercept identities, signed cuts, zero-interface control and near-critical examples"
tags: [cycles, denominators, unequal-amplitudes, near-doubled, signed-orbits]
---

# Half defects of amplitudes one and three cannot cancel the plus factor

## Statement

Let `u,v` be positive valuation words of equal length `n>=2`, differing
at exactly two positions. Suppose their two absolute changes are 1
and 3. Their combined total is even; write it as `2S`, and put
`w=uv`, `P=2^S+3^n`.

Then `P` does not divide `C_w`, for every length, other letters,
sign pattern and order of the changes. No coprimality or near-critical
restriction is needed. If `2^S>3^n`, then `gcd(C_w,P)<2^S`. If also
`gcd(S,n)=1`, `P` is the primitive homogeneous cyclotomic factor at
index `gcd(2S,2n)=2`, giving the primitive half bound.

This concerns the stated two-half family, not every four-mismatch
rotation. For example, the pairs

```
u=(1,1,1,1,2),  v=(2,1,1,4,2),
u=(2,1,1,1,2),  v=(1,1,1,4,2)
```

both have `n=5`, `S=8`, index 2, and exact near-critical inequality
`3^10<2^16<2*3^10`. They illustrate the two sign cases below.

## Proof

### 1. Normalize the changes to `(epsilon,3)`

The one-step rotation identity

```
2^w_0 C_(R_1 w) = 3 C_w + (2^(2S)-3^(2n))
```

preserves `gcd(C_w,P)`: `P` divides the parenthesized term and
both 2 and 3 are units modulo `P`.

If the half differences at positions `i<h` are `(delta_1,delta_2)`,
cutting after `i` gives halves `u[i+1:n] ++ v[0:i+1]` and
`v[i+1:n] ++ u[0:i+1]`, whose ordered differences are
`(delta_2,-delta_1)`. Repeating gives the four patterns

```
(delta_1,delta_2), (delta_2,-delta_1),
(-delta_1,-delta_2), (-delta_2,delta_1).
```

Exactly one has second change `+3` and first change of magnitude 1.
Thus, preserving positivity and the gcd, arrange
`v_i=u_i+epsilon`, `v_h=u_h+3`, where `epsilon` is -1 or 1.
Write `B=sum(u)`, `j=(epsilon+3)/2`, so `j=1` or 2 and `S=B+j`.

### 2. The weighted intercept has two constant blocks

Split `C_u=X+Y+Z` at indices `t<=i`, `i<t<=h`, and `t>h`.
Each term retains its original weight
`3^(n-1-t)2^(sum_(a<t)u_a)`. Changes of the prefix exponents give

```
epsilon=-1, j=1:  2*(2 C_u-C_v) = 2X+3Y-4Z;
epsilon=+1, j=2:      4 C_u-C_v  = 3X+2Y-12Z.          (1)
```

The first identity clears the factor `1/2` in the changed middle
weights; the decreased letter was at least 2. Set `(a,b)=(2,3)`
in that case, and `(3,2)` in the other. Both right sides are
`aX+bY-2^j aZ`.

Rotate `u` to begin after `h`. Give coefficient `a` to terms
originally outside `i<t<=h`, and coefficient `b` to those inside.
For the rotated letters `r_t` and coefficients `b_t`, define

```
M = sum_(t<n) b_t 3^(n-1-t) 2^(sum_(q<t)r_q).
```

Its coefficient sequence is a nonempty block of `a` followed by
a nonempty block of `b`, of lengths `n-h+i` and `h-i`. With
`p=sum_(t<=h)u_t`, direct rotation of the sums gives

```
3^(n-1-h) 2^p M = 3^n aZ + 2^B(aX+bY)
                = 2^B(aX+bY-2^j aZ) (mod P).         (2)
```

Concatenation gives
`C_w=3^n C_u+2^B C_v=-2^B(2^j C_u-C_v) (mod P)`.
All powers of 2 and 3 in these identities are units modulo `P`, so

```
gcd(C_w,P)=gcd(M,P).                                 (3)
```

### 3. The integer segment cannot pass through zero as required

Increase the last rotated letter by `j`. Its total becomes `S`,
while its weighted intercept remains `M`, since the last letter
occurs in no prefix sum. Its last valuation is at least `j+1`.

If `P | M`, the quotient `H=M/P` is a positive integer, and

```
2^S H = 3^n(-H)+M.
```

Every intermediate cut is integral: reducing the endpoint equation
modulo each prefix denominator and cancelling the odd suffix
multiplier proves this, exactly as in
[`antiperiodic-intercept-nondivisibility`](../antiperiodic-intercept-nondivisibility/README.md).
This argument allows arbitrary integer additive coefficients.
Thus integer states from `-H` to `H` satisfy

```
2^r_t x_(t+1)=3x_t+b_t,
```

with every `r_t>=1`, last `r_t>=j+1`, and the two coefficient
blocks above. No oddness of `H` or of every cut is assumed.

**Coefficients 2 then 3.** A negative integer remains negative
under every integral `+2` step, since `3x+2<=-1`. In the `+3`
block it remains nonpositive. It can reach zero only from `-1`;
a further `+3` step from zero would divide 3 by a positive power
of 2, which is not integral. A positive endpoint is impossible.

**Coefficients 3 then 2.** The `+3` block cannot produce a
positive state but might end at zero. The `+2` block preserves
negative integers. From zero its first positive integer output
can only be 1, using valuation 1. A further `+2` step at 1
would divide 5 by a positive power of 2, impossible. Therefore
any positive endpoint would require `0 -> 1` to be the last
arrow, with last valuation 1. Here `j=2`, so the actual last
valuation is at least 3. Again this is impossible.

Both cases contradict divisibility. Equation (3) proves `P` does
not divide `C_w`. If `2^S>3^n`, its gcd with `C_w` is a proper
divisor of the odd number `P`, hence at most `P/3<2^S`.
At `gcd(S,n)=1`, the primitive factor is exactly `P`.

## Certificates

[`check_one_three.py`](check_one_three.py) checks all base halves
of length 2 through 5 with letters in `{1,2,3,4}`, all position
pairs, both amplitude orders and all signs retaining positivity.
It verifies normalization, the weighted identities, coefficient
order, gcd identity (3), and nondivisibility with exact integers.

Separate small weighted-word checks verify all cuts whenever
the endpoints are integral, and exclude a negative-to-positive
segment under the stated last-valuation condition. The explicit
affine control `-1 -> 0 -> 1`, with coefficients `(3,2)` and
valuations `(1,1)`, checks why that last condition is necessary.
The certificate also checks the displayed near-critical pairs
and `3x+d` sign-crossing controls.

```
python3 areas/cycles/results/unequal-one-three-half-defect-exclusion/check_one_three.py
```

The deterministic receipt is [`check_one_three.json`](check_one_three.json).
Use `--write-receipt` to regenerate it. The script uses the standard
library and explicit exceptions that remain active under `python3 -O`.

## Lean

The integer-cut lemma and the two weighted endpoint obstructions in
proof step 3 are formalised in
[`LeanLane/WeightedCrossing.lean`](../../../../lean/LeanLane/WeightedCrossing.lean).
A weighted letter is a pair `(a,c)` of a natural valuation and an
integer additive coefficient. The module defines the total valuation
and the weighted intercept recursively:

```
intercept([]) = 0;
intercept((a,c)::w) = 3^length(w)*c + 2^a*intercept(w).
```

This is the intercept `M` in step 2, with the same prefix weights.
`Endpoint w x y` means the integer equation
`2^total(w)*y = 3^length(w)*x + intercept(w)`.
`Trace w x y` supplies an integer at every cut satisfying
`2^a*x_next = 3*x+c`. A block assigns one constant coefficient to
every valuation in a list.

- `trace_of_endpoint` proves that every such integer endpoint equation
  supplies an integral trace, for arbitrary integer coefficients and
  natural valuations, including zero valuations.
- `no_crossing_two_three` excludes an endpoint with `x<0<y` for
  a block of coefficient 2 followed by a block of coefficient 3.
  It requires positive valuations in the coefficient-3 block;
  the coefficient-2 block may even have zero valuations.
- `no_crossing_three_two` excludes an endpoint with `x<0<y` for
  a block of coefficient 3 followed by a nonempty block of
  coefficient 2, all valuations positive and the final valuation
  at least 2. The application above supplies the stronger final
  bound of 3. Neither theorem assumes odd intermediate values.
- `zero_interface_control` verifies the trace `-1 -> 0 -> 1`
  and its endpoint equation for coefficients `(3,2)` and valuations
  `(1,1)`, showing why the final bound cannot be dropped.

The sign/order normalization, weighted-intercept and gcd identities,
and passage to the primitive half-cancellation bound remain written
proofs. The full node therefore remains `written`.

Build and axiom evidence is in
[`WeightedCrossing.build.txt`](../../../../lean/receipts/WeightedCrossing.build.txt),
[`WeightedCrossing.axioms.txt`](../../../../lean/receipts/WeightedCrossing.axioms.txt),
and [`WeightedCrossing.sha256.txt`](../../../../lean/receipts/WeightedCrossing.sha256.txt).
Only `propext`, `Classical.choice` and `Quot.sound` occur. The module is
included in `LeanLane.lean` and built by `lake build LeanLane`.

## Remarks

- **New scope.** The unequal amplitudes 1 and 3 lie outside
  the one-letter, transposition and equal-amplitude families.
  Their full plus cancellation is excluded for every length
  without a finite basin search or an external theorem.
- **Next target.** Other unequal amplitudes produce different
  coefficient blocks. Their possible signed integer crossings
  require the endpoint and last-valuation constraints, especially
  in the near-critical range, to be kept together.
- **Controls.** The coefficients 2 and 3 are auxiliary terms
  in a divisibility argument. The proof permits an intermediate
  zero and checks its possible exit. It makes no claim that
  general `3x+d` maps preserve sign or that their positive cycles
  are excluded; the certificate verifies crossings for
  `d=5,7,13,61`.
- **Novelty and status.** Novelty undetermined. The weighted endpoint
  obstruction is formalised as described above; the full family
  reduction remains written. No independent-session review is claimed.

## History

- 2026-11-08: Derived by the Codex cycle research lane (GPT-6 Astra;
  directed by Santiago Armstrong). The unequal amplitudes 1 and 3
  reduce to coefficient blocks `(2,3)` or `(3,2)`; their only
  possible exit from zero violates the required endpoint or
  last valuation.
- 2026-11-08: The integer-cut lemma, the two weighted block endpoint
  obstructions and the zero-interface control were formalised in Lean
  by the Codex formalisation lane (GPT-6 Astra; directed by Santiago
  Armstrong). The full node remains `written` because its normalization,
  weighted-intercept identities and gcd consequences are not formalised.
