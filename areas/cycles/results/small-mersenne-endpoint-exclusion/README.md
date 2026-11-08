---
id: small-mersenne-endpoint-exclusion
kind: result
title: A small signed Mersenne endpoint excludes denominator one at every amplitude
status: written
claim: >
  Raw odd-only positive valuation words reconstructed from either order of
  the two-half-defect Mersenne normal form, with exact nonzero odd signed
  segments -h to z to h and all required boundary valuations. Let M be
  2^J in high-to-low order or 2^r in low-to-high order, where J>r>=1
  and h is positive odd. If M^2-M-6Mh-h-3h^2>=0, the reconstructed
  half u satisfies F_u(1)<M+h. Consequently D_(uv)>0 implies den(uv)>1.
  The simpler sufficient condition is M>=7h+1; any denominator-one
  normal-form join must therefore have h>(M-1)/7. Its canonical
  normalized state x>=1 would also satisfy x*M*(M-1-6h)<h*(1+3h).
  There is no bound
  on J, r, segment lengths, valuations or intermediate states, and
  no near-critical hypothesis or external input.
authors:
  - Codex cycle research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [two-half-defect-mersenne-normal-form, baseline-obligation-transfer-controls]
certificates: [check_small_endpoint.py]
evidence:
  - "check_small_endpoint.json: exact polynomial identities, first-crossing comparison samples, both reconstruction orders and actual-cycle controls"
tags: [cycles, denominators, half-defects, signed-orbits, endpoint-bounds]
---

# A small signed Mersenne endpoint excludes denominator one at every amplitude

## Statement

Use the raw odd-only signed maps
`T_d(x)=(3x+d)/2^v_2(3x+d)` on nonzero odd integers, excluding
zero numerators. The valuation uses the absolute value for negative
numerators. Fix `J>r>=1` and put `p=J-r`. Suppose two nonempty
segments, with positive valuation words `A,B`, join `-h -> z -> h`,
where `h` is positive odd, in one of the following exact normal forms.
The notation `A[t]` changes only the final letter by `t`.

| Order | Addends in `A,B` | Required valuations | Reconstructed halves | `M,N` |
|---|---|---|---|---|
| High to low | `2^J-1, 2^r-1` | `last(A)>p`, `last(B)>r` | `u=A[-p]B[-r]`, `v=AB[J]` | `2^J,2^r` |
| Low to high | `2^r-1, 2^J-1` | `last(B)>J` | `u=A[p]B[-J]`, `v=AB[r]` | `2^r,2^J` |

Thus `M-1` is always the first addend and `N-1` the second.
Write `F_u(x)=(3^n x+C_u)/2^sum(u)` for the additive-one affine
composition, where `n=len(u)`. Define

```
Delta(M,h)=M^2-M-6Mh-h-3h^2.                        (1)
```

Then

```
Delta(M,h)>=0  implies  F_u(1)<M+h.                (2)
```

If the reconstructed word has `D_(uv)>0`, its normalized rational
`3x+1` state at this cut is strictly between 0 and 1, so
`den(uv)>1`. In particular, (2) holds whenever `M>=7h+1`.

Every unequal same-parity half-defect word with full plus-factor
cancellation has one of these normal forms, up to cyclic rotation,
by [the normal-form theorem](../two-half-defect-mersenne-normal-form/README.md).
Therefore a denominator-one word in that class would necessarily
satisfy

```
Delta(M,h)<0,       and in particular h>(M-1)/7.    (3)
```

More quantitatively, if a denominator-one candidate has canonical
normalized state `x=C_(uv)/D_(uv)>=1`, it necessarily satisfies

```
x*M*(M-1-6h)<h*(1+3h).                            (4)
```

When `M>6h+1`, this gives the explicit bound
`x<h*(1+3h)/(M*(M-1-6h))`. A lower bound on the candidate's
cycle states can therefore be inserted directly in (4).

This bounds the auxiliary endpoint, not an actual positive cycle
minimum. There is no upper bound on either Mersenne level or on
the word length. The larger-endpoint cases remain open. Actual
`3x+d` states are `d` times the normalized rational states; the
theorem does not exclude those other maps' cycles.

## Proof

**The first arrow crosses immediately.** Rewrite (1) as

```
Delta=M*(M-6h-1)-h*(3h+1).
```

Its nonnegativity forces `M>6h+1`, hence `M-1-3h>0`. If `a` is the
first valuation, the signed first output and the ordinary affine
output from 1 are

```
z_1=(M-1-3h)/2^a>0,       y_1=4/2^a.
```

Set `kappa=4/(M-1-3h)`. Then `y_1=kappa*z_1`, and
`kappa*(M-1)>1`. Every remaining auxiliary state of the first
segment is positive. If `y<=kappa*x` at one cut, its next arrow
of valuation `b` satisfies

```
(3y+1)/2^b <= kappa*(3x+M-1)/2^b.                 (5)
```

Induction along the rest of `A` gives

```
F_A(1)<=kappa*z.                                   (6)
```

This comparison needs no upper bound on the positive states or
on the number of arrows.

**Both boundary reconstructions give the same inequality.** Write
the ordinary additive-one map of the nonempty second block as
`F_B(x)=c*x+b`, with `c,b>0`. Its auxiliary addend is `N-1`, so

```
h=c*z+(N-1)*b.                                     (7)
```

Changing a word's last valuation by `t` multiplies its affine
output by `2^(-t)`. In high-to-low order, the first boundary
multiplies by `2^p` and the last by `2^r`; their product is `M`.
In low-to-high order, the first divides by `2^p` and the last
multiplies by `2^J`; their product is again `M`. Thus in both cases

```
F_u(1)=M*c*F_A(1)+N*b
      <=M*kappa*c*z+N*b.                            (8)
```

Now `M*kappa>4`, whereas `N/(N-1)<=2`. The two positive terms
`c*z` and `(N-1)*b` sum to `h` by (7). Consequently (8) gives
the strict bound

```
F_u(1)<M*kappa*h=4Mh/(M-1-3h).                     (9)
```

Finally,

```
(M+h)*(M-1-3h)-4Mh=Delta(M,h)>=0,
```

so the strict bound (9) proves (2), including equality in the
quadratic condition. The normal-form state criterion converts (2)
to a state in `(0,1)` whenever `D_(uv)>0`. Such a state excludes
denominator one, including all cyclic rotations of the word.

**The simpler threshold.** Substitute `M=7h+1+t`, where `t>=0`:

```
Delta=4h^2+(8h+1)*t+t^2>0.                        (10)
```

This proves the sufficient condition `M>=7h+1` and the necessary
endpoint bound (3).

**The state-dependent necessary condition.** For a hypothetical
canonical state `x>=1`, the normal-form identity is
`F_u(x)=M*x+h`. If `M<=6h+1`, inequality (4) is automatic.
Otherwise the first arrow crosses immediately as above. Replace
`kappa` by `kappa_x=(3x+1)/(M-1-3h)` and start the ordinary
composition at `x`. Its first-step ratio is exactly `kappa_x`;
`kappa_x*(M-1)>1` propagates the comparison, and
`M*kappa_x>4>N/(N-1)` makes the second-block bound strict. Hence

```
M*x+h=F_u(x)<M*h*(3x+1)/(M-1-3h).
```

Multiplication by the positive denominator and rearrangement give
(4). This is a condition on the normalized state; an actual
`3x+d` state is `d*x`.

## Certificates

Run from the repository root:

```
python3 areas/cycles/results/small-mersenne-endpoint-exclusion/check_small_endpoint.py
python3 -O areas/cycles/results/small-mersenne-endpoint-exclusion/check_small_endpoint.py
```

The [certificate](check_small_endpoint.py) generates
[an exact receipt](check_small_endpoint.json). It verifies the
polynomial identities in the proof, samples the first-arrow
comparison and its propagation, and reconstructs explicit joins
in both orders, including `h>1` and repeated positive cycles.
These checks audit the formulas; the argument above proves the
unbounded statement, with no state graph or search cutoff used
as a theorem hypothesis.

The eleven shared actual `3x+d` fixtures are replayed. An actual
`3x+361` control satisfies the endpoint condition, but its
normalized state is `17/361`, so it is preserved. The actual
`3x+893` base has `M=8,h=3`, fails the endpoint condition and
has normalized state `367/893`; it confirms that the sufficient
condition is not necessary for denominator greater than one.

## Remarks

The theorem separates a uniform small-endpoint region from the
remaining normal-form problem. It does not assert that endpoints
of arbitrary joins are small. In particular, a long negative
initial path is outside the immediate-crossing argument, and
positive crossings with larger endpoints also need another bound.

The comparison is elementary and uses no imported period, minimum,
  gap or near-critical estimate. Repository and targeted literature
searches did not locate this particular endpoint criterion; that
limited check does not establish novelty. Novelty is undetermined.
The general [four-mismatch question](../../questions/rotation-distance-at-least-5.md)
remains open.

## History

- 2026-11-08: derived the uniform endpoint criterion from the first
  signed crossing and a positive affine comparison. Same-session
  scrutiny does not change the `written` status (Codex cycle
  research lane, GPT-6 Astra; directed by Santiago Armstrong).
