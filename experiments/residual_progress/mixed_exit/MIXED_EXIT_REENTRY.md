# Complete mixed-block exits and a growing natural re-entry

**Status: written proof and finite exact replay.** This is a complete exit
interface and a scoped obstruction to treating a maximal guarded block as
progress. It supplies no missing pair current and adds no accepted dispatcher
rule. In particular, the returning comparison used at the re-entry is **not
rho-descending**. Collatz convergence and universal closure remain open.

The inputs are the exact constructions in
[R67](../mixed_rank_recursion/MIXED_GROWING_BLOCK.md), the
[R26 run bridge](../complementary_bridge/RUN_BLOCK_BRIDGES.md), and the existing
formal absorption compiler. All clocks below use the odd Syracuse map
`S(x)=(3x+1)/2^v2(3x+1)`, absorbed at1. Write `T=nu S` for the canonical
quotient map. Its clock is stated separately.

## 1. Notation and the complete nineteen-row exit interface

Put

```
A=531441=3^12, M=524288=2^19, B=311195, D=7153=A−M,
V(w)=(Aw+B)/M, Y(w)=Dw+B.
```

The R67 guard is `w>0, w=40529845 mod2^26`, equivalently
`v2(Y(w))>=26`. Every guarded input is in W5 (`w=5 mod8`), with canonical
`3w` and `rho(w)=3w`. If `H=v2(Y(w0))`, the exact maximal number of guarded
R67 copies is

```
m=1+floor((H−26)/19),  w=V^m(w0),  e=H−19m in{7,...,25}.       (1)
```

Indeed `Y(V(w))=(A/M)Y(w)`, so every copy consumes exactly19 binary
valuation units. The next state fails this particular guard. All nineteen
exit valuations occur at every prescribed `m>=1`. The **complete** positive
initial progression for given `m,e` is

```
H=19m+e,
w0 = (2^H−B)D^(-1) mod2^(H+1), plus nonnegative multiples2^(H+1). (2)
```

The least residue is positive and odd. The extra bit makes the valuation
exact. Equivalently, if `Y(w)=2^e z`, then `z` is odd and
`z=A^m Z`, where `Z=Y(w0)/2^H` is odd. This last ternary condition must not
be dropped when the exit is required to come from an actual guarded prefix.

Every exit has `3w=31 mod128`. Consequently its next R26 block starts with
the same first exponent

```
a=5, t=(3w+1)/32, d=v2(81t−1).
```

The complete second-exponent table is

| Exact exit valuation e | Next second exponent d | Raw R26 endpoint f |
|---|---|---|
| 7 | 2 | `(729w+211)/64` |
| 8 | `3+v2(243z−294023)>=4` | the general formula below |
| 9 through25 | 3 | `(729w+147)/256` |

For the variable row, set `b=floor(d/2)` and
`c=(81t−1)/2^d`. The general endpoint formula is

```
f=3^b c                 if d is odd,
f=2·3^b c+1             if d is even.                         (3)
```

To prove the table, use the exact identity

```
243w+49 = (243·2^e z−2^8·294023)/D.                           (4)
```

The odd denominator does not change valuations. At `e=7` the numerator
has valuation7; at `e>=9` it has valuation8; at `e=8` extract `2^8`.
Subtracting the five powers in `81t−1=(243w+49)/32` gives the table.
Here `z>=A`, so the argument `243z−294023` is positive.

This is a complete parameterized interface, not a claim that all nineteen
rows descend after one block.

## 2. The exact original-rank frontier after that block

Use killed atoms `[1]=0`, pair sources `P(v)=[3v]−[v]`, and the fixed
formal absorption plan

```
div J_x = [x]−sum_v a_x(v)P(v).                               (5)
```

All coefficients are signed integers. A missing `P(v)` current remains an
input; (5) does not assert absorption of `x`. The uniform existing bound is
`rho(v)<=(9x+5)/8` on requests of `H_x=(J_x,a_x)`.

R67's full prefix has a comparison current from `[3w0]` to `[3w]` and pair
requests `1_w+a_w−a_w0`. Substitute the whole R26 forward comparison for
`P(w)`, including both absorption components. The result is

```
div C = P(w0)−sum_v (a_f(v)−a_w0(v))P(v).                     (6)
```

Every request of `H_w0` has rank below `Q0=3w0`. Thus the complete signed
frontier at or above the **original** rank is exactly

```
{(v,a_f(v)): rho(v)>=Q0, a_f(v)!=0}.                           (7)
```

No lower-source cancellation can remove or alter these coefficients.
Formula (7), not a comparison with the grown exit rank `3w`, is the correct
test for a composed original-rank argument.

The raw common-tail clocks from `3w0` to `f` are

```
(12m+5+(d−1)/2, 1)       if d is odd,
(12m+4+d/2, 0)           if d is even.                         (8)
```

The quotient statement is `T^(12m+4+floor(d/2))(3w0)=nu(f)`.
The clocks (8) compare the raw `f`; normalization to `nu(f)` retains its
own signed bridge. All are finite prescribed constructions.

## 3. Complete exit18 re-entry condition

The natural continuation used here is explicit: after reaching an exit
with `e=18`, perform the next twelve quotient steps, using the same
nonselected-to-returning comparison underlying R67, then normalize its
raw endpoint. It is not assumed that this comparison passes a rank test.

For any positive exit `v` with `v2(Y(v))=18`, the ordinary twelve-arrow
word from `3v` is

```
W=(1,1,1,1,2,3,2,1,1,1,1,2).                                (9)
```

Its endpoint is

```
12V(v)+1 = 6y+1,    y=2V(v)=(Av+B)/2^18,                     (10)
```

and `y` is an odd integer. The word needs only eighteen binary guard
bits, which exit18 retains. This can also be checked directly by the
twelve affine odd steps; their valuation sum is17 and their map is
`q -> (Aq+1064657)/2^17`.

The next normalized state is in the *original R67 guard* exactly when

```
y = 40529845 mod2^26.                                        (11)
```

Under (11), `3y=31 mod128` is canonical and `6y+1=63 mod256` is its
selected elementary partner. Therefore `nu(6y+1)=3y`. The normalization
uses equal six-arrow prefixes; it is not a zero-cost ordinary step.

This gives a complete congruence classification of the exit18-to-guard
subdomain. It does not say that every exit18 normalizes into that guard.

More explicitly, fix **any** maximal old count `m>=1` and put `k=m+1`,

```
P_k=A^k,
C_k=B(A^k−M^k)/(A−M),
L_k=M^k/2=2^(19k−1).
```

The quotient in `C_k` is an integer geometric sum. The entire positive
initial progression satisfying (11) after that old maximal prefix is

```
w0=(40529845 L_k−C_k)P_k^(-1) mod(2^26 L_k),
y=(P_k w0+C_k)/L_k.                                         (12)
```

Adding any nonnegative multiple of the modulus gives another input.
To see maximality without extrapolation, use

```
Y(y)=2(A/M)^k Y(w0)−B.
```

Condition (11) forces `v2(Y(w0))=19k−1=19m+18`, hence precisely `m`
old macros followed by exit18. Conversely, those conditions and (11)
give (12), since `P_k` is odd.

The whole current in this general re-entry case has requests

```
1_y+a_y−a_w0.                                                (13)
```

Its quotient clock is `12(m+1)`; raw normalization gives common-tail
clocks `(12(m+1)+6,6)` between `3w0` and `3y`. For large `m`, some helper
requests can exceed the original rank. They remain explicit in (13).
The leading request `y` always has coefficient `+1` and strictly larger
rank than every other request; no general original-rank descent follows.

## 4. A full re-entry block with every helper below its original parent

The particularly useful whole branch is `m=1`. Write

```
P=282429536481=A^2,
C=328537586155=B(A+M),
L=137438953472=2^37,
E=P−L=144990583009,
R(w)=(Pw+C)/L=2V^2(w).
```

**Theorem.** For every positive

```
w=8515171531530858421 mod2^63,                               (14)
```

the following assertions hold.

1. The R67 guarded prefix has exact length1 and exits at valuation18.
2. The continuation (9) re-enters the R67 guard at `R(w)>w`.
3. There is an explicit integer current `K_w` such that

   ```
   div K_w=P(w)−P(R(w))−sum_v (a_R(w)(v)−a_w(v))P(v).          (15)
   ```

   The leading input `R(w)` has coefficient `+1`. Every other request
   in (15) has `rho(v)<3w`.
4. The quotient identity is `T^24(3w)=3R(w)`. The ordinary common-tail
   identity is `S^30(3w)=S^6(3R(w))`.

**Proof.** The unique preimage of the original guard under `R` modulo
`2^63` is the residue (14). It also equals `−C E^(-1) mod2^63`.
The identity `E Y(w)=D(Ew+C)+BL` forces `v2(Y(w))=37`, so (1) gives
exactly one old macro and exit18. The endpoint (10) is `6R(w)+1`, whose elementary minimum is
`3R(w)`. Both output and input have canonical tripled states and rank
three times the pair index. Positivity and `P>L, C>0` give strict growth.

The first twelve ordinary valuations are `W`. Because their endpoint
is `F(3V(w))=4·3V(w)+1`, the next twelve ordinary valuations are `W`
with its first entry changed from1 to3. After these twenty-four arrows
the actual state is `6R(w)+1`. Append its six/six elementary bridge;
call the resulting current `D_w`, with boundary `[3w]−[3R(w)]`.
Then

```
K_w = D_w + J_R(w)−J_w                                    (16)
```

proves (15) with all signs retained. It agrees row-for-row with the
old R67 macro followed by the complete two-comparison continuation at
the exit; no fresh absorption search is used.

For the rank assertion, every request of `H_R(w)` is at most
`(9R(w)+5)/8`. The inequality `(9R(w)+5)/8<3w` is equivalent to

```
756669054999 w > 3644033042755.                               (17)
```

It holds for every integer `w>=5`, in particular all of (14). The
requests of `H_w` are also below `3w`. Therefore the leading term in
(15) cannot cancel. The clocks follow from the explicit arrows and
the six/six bridge. □

The least input is `8515171531530858421`; its re-entered input is
`17498212027614261173`. These large numbers are fixed by the exact
congruences, not found by an uncapped orbit search.

### Why this is not another accepted mixed-rank rule

At the exit `v`, the first sigma plan is accepted. Its returning input is

```
u=(2187v+1209)/1024,   rho(u)=(6561v+2603)/2048.
```

The full R44 comparison at `u` requests `y=2V(v)` with coefficient `+1`.
This request is **higher** than its parent:

```
rho(y)−rho(u)=(754515v+600401)/262144>0.                       (18)
```

All its other requests are smaller than `rho(u)`: the upper helpers obey
`(9y+5)/8<rho(u)`, equivalent to `1935495v>1446003`, and the lower
absorption input is `nu(u)<u`, whose bound is below `rho(u)` here (in
fact `nu(u)<=(u−1)/4`, since `u` is W5). The returned plan is
unresolved because of this one leading request. Thus (15) does not
establish incompatibility of additional individually accepted rules.
It establishes that this natural extension of the maximal-exit procedure
is not a descending rule. Silently declaring the intermediate returning
plan accepted would erase exactly the unresolved issue.

## 5. Arbitrarily many full exit-and-re-entry repetitions

For every integer `r>=1`, all positive inputs in the complete progression

```
w=−C E^(-1) mod2^(63+37(r−1))                               (19)
```

admit at least `r` successive copies of (15). Every copy has an old
R67 maximal length exactly1, then exit18, then re-entry. The pair
indices grow strictly throughout. This follows from the exact identity

```
E R(w)+C=(P/L)(Ew+C),                                      (20)
```

so one copy removes exactly37 binary valuation units. Conversely the
guard at each of the first `r` states forces (19).

For a fixed positive guarded input the number of these particular
copies is finite and known exactly:

```
h=v2(Ew+C),
r_max=1+floor((h−63)/37).
```

The terminal value of `v2(Ew+C)` is in26..62. The terminal state remains
in the original R67 guard, but fails the stronger re-entry guard. No
claim about subsequent choices follows from this finite countdown.

Write `w_j=R^j(w0)`. Adding the full currents gives

```
div K^(r)=P(w0)−P(w_r)−sum_v (a_w_r(v)−a_w0(v))P(v).          (21)
```

The intermediate absorption plans cancel exactly, including their
currents, signs, and integer multiplicities. The final leading input has
coefficient `+1`. Every other remaining request has rank below
`3w_(r−1)<3w_r`, by (17) applied at the last parent. They need not all
be below `3w0`; the implementation records the entire original-rank
frontier. Expanding nonleading requests only through strictly smaller
rho dependencies cannot cancel the leading request.

The quotient clock is `24r`. The ordinary common-tail clocks are
`(24r+6,6)`, obtained by composing the equal six-arrow right tails;
one must not call the quotient length an ordinary path to the normalized
endpoint.

The consequence is precise: **maximality of the old guard, followed by
this natural continuation, does not ensure progress.** There are
arbitrarily long finite increasing re-entry strings, with their higher
signed premise retained. These statements concern the specified
comparisons. They do not establish an infinite positive trajectory,
failure of other comparisons, failure of the current dispatcher, or
nonexistence of a richer well-founded rank.

## 6. Reproduction and scope of the stored evidence

Run from the repository root:

```
python3 experiments/residual_progress/mixed_exit/check_mixed_exit.py
```

The default command recomputes and matches the checked-in receipt. It
uses only prescribed finite paths and exact integer arithmetic. The
bounded audit covers:

- 114 exact exit-parameter cases: all nineteen valuations, old counts
  1,2,8, and two progression indices;
- 19 full signed next-block plans, one for every exit valuation;
- eight complete general re-entry plans at old counts1,2,4,8;
- eight full copies of (15), checked against the original macro and both
  complete exit comparison plans;
- eight full repeated currents through eight re-entries, with explicit
  intermediate-plan substitution through two copies;
- 24 arithmetic repetition families through128 copies and a65-bit index;
- 37 exact re-entry guard maxima, covering every terminal valuation26..62;
- nine rejection checks, including absent and invalid supplied currents.

The receipt stores full signed current and request tables for the least
single-copy example and a two-copy example, plus hashes for the other
finite cases. These are conditional comparison certificates; their
larger requested pair is not stored as an absorption certificate.
`compile_plan` rejects missing premises. The written proofs establish
the universal quantified statements; the finite audit checks their
implementation and recorded examples.
