---
id: mixed-exit-growing-reentry
kind: result
title: "Complete exits of the mixed growing block, and a natural continuation that re-enters at greater height"
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; T = nu S, rho(w) = nu(3w), Y(w) = 7153 w + 311195. At the end of the maximal
  guarded block of R67 (exit valuation e = 7..25 of Y), the next R26 first exponent is always 5 and its second depth
  is 2 at e = 7, 3 + v2(243 z - 294023) >= 4 at e = 8, and 3 at e = 9..25; the composed current keeps every signed
  helper, and its whole frontier at ranks >= the original 3 w0 is that of the raw endpoint. The exit-18-to-guard
  subdomain has an exact congruence at every old count m. On w = 8515171531530858421 mod 2^63 the block has exactly
  one copy and exit 18, and the natural continuation re-enters the guard at R(w) = (282429536481 w +
  328537586155)/2^37 > w, with full current D + J_R(w) - J_w, unique higher request R(w) (+1), all other requests
  below 3w, quotient clock 24 and ordinary common-tail clocks (30, 6); its returning R44 comparison is not
  rho-descending, so this is not an accepted rule. Every r >= 1 copies occur on w = -C/E mod 2^(63+37(r-1)), and a
  fixed positive seed makes exactly 1 + floor((v2(Ew+C) - 63)/37). No infinite positive path, failure of other exit
  comparisons or nonexistence of a richer rank is asserted.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [mixed-rank-growing-blocks, complementary-run-bridges, returning-forward-interface, critical-image-rank-composition]
certificates: [check_legacy_replay.py]
evidence:
  - "check_mixed_exit.py, mixed_exit.py, mixed_exit_audit.json: the legacy constructor and checker: 114 exit-parameter cases, 19 full signed next-block plans, eight general re-entry plans, eight full copies of (15), eight repeated currents through eight re-entries, 24 repetition families through 128 copies, 37 exact re-entry maxima and nine rejections; full current tables for the least single-copy and a two-copy example. Fails at its new path: mixed_exit.py loads ../mixed_rank_recursion/ (now ../mixed-rank-growing-blocks/) by its pre-migration folder name; it is loaded in turn by the later legacy integer_prefix/ code. Passed at be73a66 as experiments/residual_progress/mixed_exit/check_mixed_exit.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
  - "../native-height-inverse-obstruction/batch_r68_r70_check.py: side-lane probe of R68 and R70 (see reviewed_by), a certificate of that node"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: ../native-height-inverse-obstruction/batch_r68_r70_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 08:37, VERIFIED, main 9190ccf), with the lane's own S, nu and T, nothing imported from main: the guard w = 40529845 (mod 2^26) = -B/7153 with w = 5 (mod 8) and nu(3w) = 3w (200 samples); for m = 1..4 and every e = 7..25, 228 inputs with exact H, m = 1 + floor((H-26)/19), exit valuation e, 3w = 31 (mod 128), first R26 exponent 5 and the second-depth table; the re-entry theorem on 23 members of w = 8515171531530858421 (mod 2^63) (v2(Y) = 37, the two twelve-arrow words, R(w) odd, T^24(3w) = 3R(w), S^30(3w) = S^6(3R(w)), R(w) > w back in the guard); repetitions r = 1..6 (18 cases) with counts 1 + floor((h-63)/37) and the clocks. The signed currents and the non-descent of the continuation were not rebuilt; the status stays written"
aliases: [R70]
tags: [convergence, outer-residual, tripling-pairs, mixed-rank, exit-interface, negative-cycle-shadow]
---

# Complete exits of the mixed growing block, and a natural continuation that re-enters at greater height

## Statement

Odd-only clock, 1 absorbing; `T = νS` with its clock stated separately; `ρ(w) = ν(3w)`; `Y(w) = 7153w + 311195`; the guard `w ≡ 40529845 (mod 2^26)` of [`mixed-rank-growing-blocks`](../mixed-rank-growing-blocks/README.md).

1. **Exit interface.** After the maximal guarded block (exit valuation `e = v2(Y(w)) ∈ 7..25`), the next R26 block ([`complementary-run-bridges`](../complementary-run-bridges/README.md)) has first exponent 5, and second depth 2 at `e = 7`, `3 + v2(243z − 294023) ≥ 4` at `e = 8`, 3 at `e = 9..25`. The composed current keeps every signed helper; its whole frontier at ranks `≥` the original `3w0` is exactly that of the raw endpoint.
2. **Exit-18 re-entry.** The exit-18-to-guard subdomain has an exact congruence at every old count `m`. On `w ≡ 8515171531530858421 (mod 2^63)` the block has exactly one copy and exit 18, and the natural twelve-quotient-step continuation re-enters the guard at `R(w) = (282429536481w + 328537586155)/2^37 > w`, with current `D_w + J_R(w) − J_w`, unique higher request `R(w)` (`+1`), every other request below `3w`, quotient clock 24 and ordinary common-tail clocks `(30, 6)`. Its returning R44 comparison is **not** `ρ`-descending, so this is a failed natural extension, not an accepted rule.
3. **Repetition.** Every `r ≥ 1` copies occur on `w ≡ −C/E (mod 2^(63+37(r−1)))` (`E = 3^24 − 2^37`, `C = 328537586155`); a fixed positive seed makes exactly `1 + ⌊(v2(Ew + C) − 63)/37⌋` copies.

Maximality of the old guard followed by this continuation does not ensure progress. No infinite positive path, failure of other exit comparisons, failure of the current dispatcher or nonexistence of a richer well-founded rank is asserted.

## Proof

The legacy note "Complete mixed-block exits and a growing natural re-entry" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written proof and finite exact replay.** This is a complete exit
interface and a scoped obstruction to treating a maximal guarded block as
progress. It supplies no missing pair current and adds no accepted dispatcher
rule. In particular, the returning comparison used at the re-entry is **not
rho-descending**. Collatz convergence and universal closure remain open.

The inputs are the exact constructions in
[R67](../mixed-rank-growing-blocks/README.md), the
[R26 run bridge](../complementary-run-bridges/README.md), and the existing
formal absorption compiler. All clocks below use the odd Syracuse map
`S(x)=(3x+1)/2^v2(3x+1)`, absorbed at1. Write `T=nu S` for the canonical
quotient map. Its clock is stated separately.

### 1. Notation and the complete nineteen-row exit interface

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

### 2. The exact original-rank frontier after that block

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

### 3. Complete exit18 re-entry condition

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

### 4. A full re-entry block with every helper below its original parent

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

#### Why this is not another accepted mixed-rank rule

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

### 5. Arbitrarily many full exit-and-re-entry repetitions

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

### 6. Reproduction and scope of the stored evidence

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

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B12 migration; standard library). The legacy scripts of this folder load sibling modules by their pre-migration paths, so they no longer run here. This certificate calls `tools/legacy_replay.py`, which rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, runs the unmodified legacy scripts there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied file unchanged. It writes nothing in the repository. It replays: the legacy checker `check_mixed_exit.py` (about 7 s; the counts of section 6 of the note and the stored current tables, compared with `mixed_exit_audit.json`). The side-lane probe of this result is a certificate of [`native-height-inverse-obstruction`](../native-height-inverse-obstruction/README.md). The commands in the legacy text name `experiments/residual_progress/mixed_exit/`.

## Remarks

- `−C/E` is the negative rational fixed point of `R`; the growing re-entries are its 2-adic shadow (side lane, feed 08:37). The integer realisation of every finite word in the two returns `V`, `R` is [`exit18-return-integer-cylinders`](../exit18-return-integer-cylinders/README.md) (R74).
- Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/mixed_exit/MIXED_EXIT_REENTRY.md` (legacy ID R70) at commit `be73a66`, by the B12 migration (Claude, Opus 5.5). Note, scripts and receipt moved byte-identical; `check_legacy_replay.py` was added at the migration. Legacy status: "written full exit interface and scoped failure of a natural continuation; no new accepted rule".
- Main lane (ChatGPT, Codex), 2026-10-18, from commit `ea3278e`. The batch's "independent model" proof and code reviews (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents, not a different lane.
