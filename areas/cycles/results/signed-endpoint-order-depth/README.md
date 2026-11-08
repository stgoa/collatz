---
id: signed-endpoint-order-depth
kind: result
title: Residue order depths force complementary factors into signed endpoints
status: written
claim: >
  Exact signed odd-only arrows 2^a_i*x_(i+1)=3*x_i+d_i,
  a_i>=1 and positive odd d_i, join -h to h in n>=1 arrows,
  with h positive odd. Let Q>1 be coprime to 6, divide every d_i,
  and have odd ord_p(2) for every prime p dividing Q. Let D_v
  be the product of the full p^v_p(Q) components for which
  v_2(ord_p(3))=v, with empty products equal to 1.
  Then Q/D_(v_2(n)+1) divides h. Moreover, writing
  q0=Q/gcd(Q,h), a congruence Q|h(2^S+3^n) with integers
  S>=n>=1 exists exactly when q0=1 or every prime of q0 has
  the same positive order depth. This characterizes the
  common-addend residue obstruction, not actual signed paths.
  For odd J, no constant-addend 3x+(2^J-1) path joins -1 to 1
  if 9 divides J or 21 divides J. At J=21 every signed return
  forces 337|h or 6223|h, with the sharper length-dependent
  alternatives proved below. J=15 passes the residue test but
  its exact orbit from -1 closes away from 1. No claim of a
  complete signed-orbit or half-defect classification is made.
authors:
  - Codex signed-endpoint research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [odd-order-residue-signed-endpoint-divisibility, two-half-defect-mersenne-normal-form]
certificates: [check_order_depth.py]
evidence:
  - "check_order_depth.json: exact residue orders and complete tables, prime-power cancellation cases, genuine signed traces, Mersenne reconstructions, J=15 orbit closure and eleven actual-cycle controls"
tags: [cycles, signed-orbits, residues, prime-powers, half-defects, order-depth]
---

# Residue order depths force complementary factors into signed endpoints

## Statement

Work in the raw signed odd-only clock. Let

```
2^a_i*x_(i+1)=3*x_i+d_i,       a_i>=1,       0<=i<n,
x_0=-h,       x_n=h,          n>=1,
```

where all states are nonzero odd integers, every addend `d_i` is
positive odd, and `h` is positive odd. These are exact arrows:
the displayed exponent is the full valuation of the nonzero
numerator, using its absolute value when negative. Addends may
vary; a constant addend is the signed `3x+d` map. There is no
bound on the length, valuations, states or addends.

Let `Q>1` be coprime to 6, divide every addend, and satisfy
`ord_p(2)` odd for every prime `p|Q`. Define the **order depth**
and the corresponding full prime-power components by

```
v(p)=v_2(ord_p(3)),
D_v=product_(p|Q, v(p)=v) p^v_p(Q),       v>=0.
```

The empty product is 1. Only finitely many components are nontrivial;
they are pairwise coprime and their product is `Q`.

**Length-dependent endpoint law.** Every such signed return satisfies

```
Q/D_(v_2(n)+1) | h.                                    (1)
```

Thus all full prime-power components outside one permitted depth
must divide the endpoint. In particular `D_0|h`, recovering the
[odd-order obstruction](../odd-order-residue-signed-endpoint-divisibility/README.md).
When the indicated component is absent, (1) forces `Q|h`.

**Exact scope of the residue test.** Put `q0=Q/gcd(Q,h)`. There
exist integers `S>=n>=1` satisfying

```
Q | h*(2^S+3^n)                                        (2)
```

if and only if either `q0=1`, or every prime divisor of `q0`
has the same strictly positive order depth. This is an existence
classification for the composition congruence alone. It asserts
neither a constant-addend orbit nor a normal-form join.

**Mersenne applications.** For every odd `J>=3`, the full modulus
`Q=2^J-1` meets the order-of-2 hypothesis. A constant-addend
`3x+(2^J-1)` path from `-1` to `1` is impossible whenever

```
9 | J   or   21 | J.                                   (3)
```

The same exclusions apply to the endpoint-one, low-to-high `r=1`
subclass of the [two-segment Mersenne normal form](../two-half-defect-mersenne-normal-form/README.md).
They use no final-valuation bound and do not exclude every endpoint
at those levels.

At `J=21`, `Q=7^2*127*337=2,097,151`, and the only nontrivial
components are `D_1=6223` and `D_3=337`. Hence

| Odd-arrow length `n` | Necessary endpoint divisor |
|---|---:|
| `n` odd | 337 divides `h` |
| `n=4 mod 8` | 6223 divides `h` |
| `n=2 mod 4` or `n=0 mod 8` | 2,097,151 divides `h` |

In particular `337|h` or `6223|h` is necessary at every length.
These divisibilities alone are not asserted sufficient.

## Proof

### 1. Composition and cancellation retain full prime powers

Put `S=sum_i a_i`. Iterating the arrow equations modulo `Q`
eliminates every additive term and gives

```
2^S*x_n = 3^n*x_0 (mod Q),
Q | h*(2^S+3^n).                                      (4)
```

Fix a full prime power `p^e|Q`, with `e=v_p(Q)`. If
`v_p(h)>=e`, this component already divides `h`. Otherwise write
`h=p^c h0`, where `c<e` and `p` does not divide `h0`. Cancelling
exactly `p^c` from (4) shows

```
p^(e-c) | 2^S+3^n,       so       2^S=-3^n (mod p).     (5)
```

No inverse of `h` modulo the original modulus has been assumed.

Write `ord_p(2)=a` and `ord_p(3)=2^v*b`, with `a,b` odd.
The exponent `L=lcm(a,b)` is odd. Raise (5) to `L` to obtain

```
3^(nL)=-1 (mod p).
```

This element has order exactly 2. Since `b|L` and `L` is odd,
the order of `3^(nL)` is

```
2^v / gcd(2^v,n) = 2^max(v-v_2(n),0).
```

It equals 2 only when `v>0` and `v=v_2(n)+1`. Therefore every
component at any other depth must have `v_p(h)>=e`. Multiplying
these coprime full components proves (1).

The argument requires only the integer arrow equations. Oddness,
exact valuations and positive addends specify the intended signed
map; the residue implication does not rely on intermediate signs.

### 2. The converse at the congruence-existence level

First, orders preserve their 2-adic depth on lifting to an odd
prime power. If `b` is coprime to `p`, reduction modulo `p` shows
that `ord_p(b)` divides `ord_(p^e)(b)`. The elementary binomial
lifting argument gives

```
b^(ord_p(b)*p^(e-1))=1 (mod p^e).
```

Indeed, raising `1+p^k u` to the `p`th power gives 1 modulo
`p^(k+1)`. Thus the quotient of the two orders divides `p^(e-1)`,
an odd number, and their 2-adic depths agree.

If (2) has a solution, cancel `gcd(Q,h)` to get
`q0 | 2^S+3^n`. Part 1 forces every residual prime's depth to
equal the same positive value `v_2(n)+1`. This proves necessity.

Conversely, suppose all primes in `q0>1` have one positive depth
`v`. For each full prime power dividing `q0`, write

```
ord_(p^e)(3)=2^v*b_p,       b_p odd.
```

Let `O=lcm_(p^e||q0) ord_(p^e)(3)=2^v*b`, with `b` odd.
Modulo `p^e`, the element `3^(ord_(p^e)(3)/2)` is `-1`:
it has order 2, and `-1` is the unique element of order 2 modulo
an odd prime power. The latter fact follows because
`p^e|(x-1)(x+1)` and the two factors have gcd dividing 2.
Since `b/b_p` is odd,

```
3^(O/2)=-1 (mod p^e),       hence 3^(O/2)=-1 (mod q0).
```

Take `n=O/2` and let `S` be any sufficiently large multiple of
`ord_q0(2)`, so that `S>=n`. Then `2^S=1 (mod q0)`, proving
(2). If `q0=1`, any `S>=n>=1` works. This completes the exact
classification of what the common-addend congruence can exclude.

### 3. Distinct depths exclude entire Mersenne level families

For odd `J`, `2^J-1` is coprime to 6. Every prime divisor has
`ord_p(2)|J`, so that order is odd. The certificate checks the
primes and exact orders below.

| `p` | `ord_p(2)` | `ord_p(3)` | `v(p)` |
|---:|---:|---:|---:|
| 7 | 3 | 6 | 1 |
| 73 | 9 | 12 | 2 |
| 127 | 7 | 126 | 1 |
| 337 | 21 | 168 | 3 |

If `9|J`, the primes 7 and 73 divide `2^J-1` and have distinct
positive depths. If `21|J`, the primes 7 and 337 do the same.
At `h=1` no component can be cancelled, so part 1 gives a
contradiction in either case. This proves (3). The exact
factorization at `J=21` gives the displayed length table.

For endpoint-one, low-to-high `r=1` normal forms, the first
segment uses `3x+1`. Its initial state `-1` stays fixed, with
valuation 1 at every arrow. The second segment would therefore
join `-1` to `1` with addend `2^J-1`, which (3) excludes. The
normal form's boundary conditions remain unchanged.

More generally, the theorem applies to either segment order
using any admissible `Q` dividing both addends. If
`g=gcd(J,r)>1` is odd, one may take the full common modulus
`Q=2^g-1>1` and use `n=len(A)+len(B)`. This is a constraint on
the combined signed join, not an assertion about each segment's
endpoints separately.

### 4. A residual level separates arithmetic from dynamics

At `J=15`, `Q=32767=7*31*151`. All three primes have depth 1.
The complete power-residue table has exactly the solutions

```
S=0 (mod 15),       n=75 (mod 150)                     (6)
```

to `2^S=-3^n (mod Q)`. For example `S=120,n=75` satisfies the
necessary congruence with positive valuation total.

Nevertheless the actual constant-addend odd-only orbit from
`-1` does not reach 1. The certificate follows the exact orbit
until a state repeats: after 75 arrows it enters a positive
150-arrow cycle at 98,303. The cycle has valuation total 315,
minimum 1229 and maximum 2,342,315. No state in the transient
or the closed cycle is 1. Exact closure therefore proves that
this orbit never reaches 1; this is not a timeout or an
extrapolation. The arithmetic equivalence above is not a
sufficient condition for a constant-addend signed return.

## Certificates

The standard-library [certificate](check_order_depth.py) checks
primality, exact multiplicative orders and prime-power depth
preservation. It enumerates complete power-residue tables for
the selected moduli and endpoint classes, including partial
prime-power cancellation, and verifies both the fixed-length
divisibility and the congruence-existence criterion. Its
[generated receipt](check_order_depth.json) states every range.

Genuine signed traces test surviving components. For example,
under the common modulus `Q=511`, `h=73` has the one-arrow
return `-73 -> 73` with addend 511 and valuation 2. Also,
`h=7` has `-7 -> 245 -> 7`, with addends 511 and 113953 and
valuations 1 and 14. Their lengths select different depths.
The second example has varying addends and is not asserted a
constant-addend orbit.

The certificate also checks exact weighted compositions,
Mersenne normal-form reconstructions, the complete `J=15`
finite orbit closure, and all eleven standard positive-cycle
fixtures for `d=5,7,13,61`. Positive cycles have equal rather
than opposite endpoints and are not excluded by this theorem.
All checks remain active under `python3 -O`.

Run `python3 areas/cycles/results/signed-endpoint-order-depth/check_order_depth.py`
from the repository root. Add `--write-receipt` to regenerate the
deterministic receipt after inspecting any intended change.

## Remarks

The predecessor result handles depth zero, where the orders of
both 2 and 3 are odd. This extension keeps the 2-adic part of
the order of 3 and the odd-arrow length. Its existence converse
states the precise limit of the common-addend congruence test;
unresolved actual trajectories require further information.

The argument is elementary multiplicative-order arithmetic,
with no external theorem or computation assumed. Novelty of the
combined signed-endpoint application is undetermined. It does
not classify all Mersenne returns, settle the general half-defect
affine-state criterion, or exclude arbitrary positive cycles.

## History

- 2026-11-08: extended the odd-order endpoint obstruction by
  retaining mixed positive order depths and full prime powers,
  and characterized existence of the composition congruence.
  The residual `J=15` orbit supplies a finite dynamics control.
  Same-session scrutiny does not upgrade the node to `reviewed`.
