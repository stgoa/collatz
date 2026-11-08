---
id: expanding-background-defect-growth
kind: result
title: A fixed expanding background needs a growing number of changed letters
status: written
claim: >
  Raw odd-only 3x+1 clock, conditional only on the replayed gap EXT-1.
  Fix a nonempty positive word U of length t, total a and intercept C,
  with P=3^t>Q=2^a. Replace arbitrary s positions of U^N by any
  different positive letters, allowing increases and decreases.
  For D_W>0, put q=den(W). Then s>=1 and, with gamma=log_Q(P),
  H_s=sum_(j<s) gamma^j and explicitly defined background constants
  Z,Cmax,B,S, Q^(N/H_s)<q*Z(Cmax+BSs/3)*2^172*(tN)^341.
  This gives effective bounded-denominator finiteness for fixed U,s.
  At q=1 it gives an explicit growing lower bound on s; for fixed U,
  s>=log_gamma(N)-log_gamma(ln N)-O_U(1). If only final letters
  of blocks are increased, the sharper coefficient is q*C(s+1).
  In the final-letter-increase setting, for U=(2,1), s<=4 and
  D_W>0, den(W)=1 if and only if every
  block is (2,2), namely W=(2,2)^N with N<=4.
  The special exclusion uses an exact N<7120 bound, descent through
  2^25 and product inequalities for all odd-step lengths through 14238.
  No near-critical, parity or primitivity hypothesis is used, and
  the corollary does not restrict which copies are modified.
  This does not exclude arbitrary positive cycles.
authors:
  - Codex four-arc research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [baseline-obligation-transfer-controls]
assumes: [musson-collatz-gap-all]
certificates: [check_growth.py]
evidence:
  - "check_growth.json: exact affine identities, general-background controls, cutoff constants, all odd descents below 2^25, all 14238 product inequalities and eleven standard actual-cycle fixtures"
tags: [cycles, repeated-backgrounds, defects, effective-exclusion, growth]
---

# A fixed expanding background needs a growing number of changed letters

## Statement

Fix a nonempty positive valuation word `U`, with length `t`,
total `a`, and additive-one intercept `C=C_U`. Assume it is
**expanding**:

```
P=3^t > Q=2^a,      B=P-Q>0,      gamma=ln(P)/ln(Q)>1.
```

Form `W` by replacing `s` arbitrary positions of `U^N`
by different positive letters. Replacements may increase
or decrease their original letter. The raw odd-step length
is `m=tN`. Define, for phases `0<=j<t` and `0<=r<t`,

```
A_(j,r)=sum of the first r letters of the phase-j rotation of U,
C_j=intercept of that rotation,       Cmax=max_j C_j,
K=2^(max(U)-1),
R=max_(j,r) 3^r/2^(gamma*A_(j,r)),
Z=(R*K^gamma)^(1/(gamma-1)),
S=max_j [sum_(0<=r<t) 2^A_(j,r)/3^r]/(1-Q/P),
H_s=sum_(j=0)^(s-1) gamma^j.
```

All these constants are determined by the fixed background.
Empty prefixes ensure `R>=1`, hence `Z>=K>=1`.

**Denominator law.** Conditional on the replayed
[effective gap EXT-1](../../../../sources/musson-collatz-gap-all.md),
for every `W` with `D_W>0`, put `q=den(W)`. Then `s>=1` and

```
q > Q^(N/H_s)/[Z*(Cmax+B*S*s/3)*2^172*(tN)^341].         (D1)
```

In particular, `q=1` implies

```
Q^(N/H_s) < Z*(Cmax+B*S*s/3)*2^172*(tN)^341.              (G1)
```

Consequently, for every fixed `U,s` and denominator bound
`q<=q_*`, only finitely many such words exist, with an
effective bound. At `q=1`, an explicit growing restriction is

```
gamma^s > 1 + N*ln(P/Q)
 /[172ln2+341ln(t)+ln(Z*(Cmax+B*S*t/3))+342ln(N)].         (G2)
```

In particular, for fixed `U`,
`s>=log_gamma(N)-log_gamma(ln N)-O_U(1)`.
The dependence on `U` matters; no uniform asymptotic claim
is made when the background itself varies.

**Sharper final-letter form.** Let `U[e]` increase only the final letter of `U` by the
nonnegative integer `e`. For arbitrary `N>=1`, form

```
W=U[e_0] U[e_1] ... U[e_(N-1)],
s=#{j:e_j>0},      m=tN,      A=aN+sum(e_j).
```

Here `N` counts blocks, `m` counts raw odd-only steps, and
`s` counts modified blocks. These are different clocks and
counts. There is no bound on the increases or on their
positions, and the word need not be primitive.

Assume the replayed [effective gap EXT-1](../../../../sources/musson-collatz-gap-all.md):
`2^A <= 2^172*m^341*(2^A-3^m)` for `m>0`, `D_W>0`.
It is the only external proof input.

For this more restrictive construction, if `den(W)=1`, then `s>=1` and

```
H_s=sum_(j=0)^(s-1) gamma^j,
Q^(N/H_s) < C(s+1)*2^172*(tN)^341.                         (1)
```

More generally, its denominator obeys
`q>Q^(N/H_s)/[C(s+1)*2^172*(tN)^341]` whenever `D_W>0`.

For every fixed `U,s`, (1) bounds `N` effectively. The
number of such denominator-one words is therefore finite,
even with all increases allowed to vary. More explicitly,

```
gamma^s > 1 + N*ln(P/Q)
                /[172ln2+341ln(t)+ln(2C)+342ln(N)].        (2)
```

In particular, for fixed `U` and `N` tending to infinity,

```
s >= log_gamma(N)-log_gamma(ln N)-O_U(1).
```

The dependence on `U` matters: this is not a uniform
asymptotic bound when the background itself varies.

**Explicit exclusion.** Take `U=(2,1)`, so `W` has the form
`(2,d_0,2,d_1,...,2,d_(N-1))`, where `d_j>=1` and
`s=#{j:d_j>1}`. If `s<=4` and `D_W>0`, then

```
den(W)=1  iff  all d_j=2.
```

The right side is just `W=(2,2)^N`, with `N=s<=4`,
representing repeated traversals of the trivial cycle.
Every other word in this class, under every cyclic cut,
has denominator greater than 1. The proof imposes no
near-critical or total-parity hypothesis.

## Proof

Sections 1-3 prove the sharper final-letter-increase
statement. Section 4 treats arbitrary substitutions and
the general denominator law.

### 1. Exact integral runs in a shifted coordinate

If `s=0`, the word is `U^N`, with denominator expression
`Q^N-P^N<0`. Thus `D_W>0` implies `s>=1`.

Suppose `den(W)=1`. The word-cycle correspondence gives
positive odd integer states following the specified exact
valuations. At the start of a block, its affine map is

```
x -> (P*x+C)/(Q*2^e).
```

Read cyclically from just after a modified block. Split
the `N` blocks into `s` groups of lengths `k_i>=1`,
`sum k_i=N`: the first `k_i-1` blocks have no increase,
and the last has increase `e_i>0`. This allows adjacent
modified blocks, in which case `k_i=1`.

Let `x_i` be the integer state at the beginning of group
`i`, and set `y_i=B*x_i+C`. The unmodified block acts by
`y -> (P/Q)y`, since `B=P-Q`. The exact group equation is

```
P^k_i*y_i = Q^k_i*(B*2^e_i*x_(i+1)+C).                   (3)
```

Because `P` and `Q` are coprime, `Q^k_i` divides the
positive integer `y_i`. Consequently

```
y_i >= Q^k_i,      product_i y_i >= Q^N.                  (4)
```

This is an integrality argument. Rational word states
cannot be substituted here without clearing their actual
denominator.

The same equation gives

```
y_(i+1) = C + [(P/Q)^k_i*y_i-C]/2^e_i
        <= (P/Q)^k_i*y_i
        <= y_i^gamma.                                   (5)
```

The first inequality uses `(P/Q)^k_i*y_i>C` and `e_i>0`.
The second uses (4) and `gamma-1=ln(P/Q)/ln(Q)>0`.
Index the groups so that `y_0=y_min`. Iterating (5) gives
`y_j<=y_min^(gamma^j)` for `0<=j<s`. Combining with (4),

```
Q^N <= product_i y_i <= y_min^H_s,
Q^(N/H_s) <= y_min.                                      (6)
```

### 2. The reciprocal sum across an entire group

Within group `i`, before its final increased division,
the block-start states are exactly

```
x_(i,j)=[(P/Q)^j*(B*x_i+C)-C]/B,
                         0<=j<k_i.
```

Thus `x_(i,j)>=(P/Q)^j*x_i`, and the finite geometric
sum gives

```
sum_(j<k_i) 1/x_(i,j) < [P/(P-Q)]/x_i = P/(B*x_i).       (7)
```

Multiplying all block arrows, the natural-log drift is

```
Lambda=ln(2^A/3^m)
      =sum_blocks ln(1+C/(P*x))
      < (C/P)*sum_blocks 1/x
      < C*sum_(i<s) 1/(y_i-C)
      <= Cs/(y_min-C).                                   (8)
```

All sums in (7)-(8) run over block starts, not all `m`
odd states. The factors `P/B` and `C/P` account for that
change of clock explicitly.

Put `G=2^172*(tN)^341`. EXT-1 and
`ln(z)>1-1/z` for `z>1` give

```
Lambda > D_W/2^A >= 1/G.
```

Together with (8), this implies

```
y_min < C+CsG <= C(s+1)G.
```

Combining with (6) proves (1).

### 3. Effective finiteness and growing defect count

For fixed `U,s`, the left side of (1) grows exponentially
in `N` and the right side polynomially. An entirely
effective cutoff can be found using any rational `g>gamma`:
replace `H_s` by `sum_(j<s)g^j`, take base-2 logarithms,
and use dyadic intervals `2^k<=N<2^(k+1)` until the
exponential-in-`k` left side exceeds the affine right side.
The strict rational bound on `gamma` can itself be checked
by an integer-power comparison `P^v<Q^u` for `g=u/v`.

Once `N` is bounded, so are the increases. Indeed, on a
positive integer `3x+1` cycle,
`2^A=product_(j<m)(3+1/n_j)<=4^m`, hence `A<=2tN` and
`sum e_j<=N(2t-a)`. There are finitely many choices.

For the explicit growth inequality, take natural logarithms
in (1), use `s<=N`, and write
`H_s=(gamma^s-1)/(gamma-1)`. Then

```
N*ln(Q)/H_s
  < 172ln2+341ln(t)+ln(2C)+342ln(N).
```

Since `(gamma-1)ln(Q)=ln(P/Q)`, this is (2), with the
stated fixed-background asymptotic consequence.

### 4. Arbitrary phases and decreases cost only fixed background constants

We now prove (G1)-(G2). Write the base periodic letters
as `b_j`, with phases modulo `t`. The rotation-intercept
identity gives

```
2^b_j*C_(j+1)=3C_j-B.
```

At phase `j`, use `y=B*x+C_j`. At an unchanged letter,
the next phase's coordinate is exactly `3y/2^b_j`.
Group the word into `s` nonempty stretches, each ending
at one changed letter and containing no other changes.
Let stretch `i` have length `ell_i`, base total `a_i`,
initial coordinate `y_i`, final phase intercept `C_next`,
and final-letter change `e_i!=0`. Put
`f_i=max(-e_i,0)`. Positivity of the substituted letter
gives `2^f_i<=K`, and exact composition gives

```
3^ell_i*y_i = 2^a_i*(B*2^e_i*x_(i+1)+C_next).             (13)
```

If `e_i<0`, clear its power-of-two denominator in (13).
In both signs, coprimality with 3 yields

```
2^(a_i-f_i) | y_i,
y_i >= 2^a_i/K,
product_i y_i >= Q^N/K^s.                                (14)
```

The exponent `a_i-f_i` is positive, since `a_i` includes
the original changed letter. The base, unmodified stretch
sends a positive state to a positive rational state, so
`mu_i*y_i>C_next`, where `mu_i=3^ell_i/2^a_i`. Hence

```
y_(i+1)=C_next+(mu_i*y_i-C_next)/2^e_i
       <=K*mu_i*y_i.
```

Write `ell_i=kt+r` with `0<=r<t`. Complete periods
cancel from `3^ell_i/2^(gamma*a_i)`, so it is at most `R`.
Using (14),

```
y_(i+1) <= R*K^gamma*y_i^gamma.
```

The normalized coordinates `z_i=Z*y_i` therefore satisfy
`z_(i+1)<=z_i^gamma`. Moreover (14) and `Z>=K` give
`product_i z_i>=Q^N`. The product-and-chain argument of
section 1 now proves

```
Q^(N/H_s) <= Z*y_min.                                    (15)
```

Before the changed terminal letter, each raw state of a
stretch follows the unmodified periodic background.
Starting at `x_i` in phase `j`, the state after `r` such
letters is at least `3^r*x_i/2^A_(j,r)`. Summing over
complete periods and the final partial period gives a
strict reciprocal bound `sum 1/x < S/x_i`. Thus the
original raw-step drift satisfies

```
Lambda < (S/3)*sum_(i<s) 1/x_i.
```

If `y_min>Cmax`, then `x_i>=(y_min-Cmax)/B`, so EXT-1
forces `y_min<Cmax+B*S*s*G/3`, where
`G=2^172*(tN)^341`. If `y_min<=Cmax`, the bound
`y_min<(Cmax+B*S*s/3)*G` is immediate instead. In both
cases, this last bound and (15) prove (G1).

For (G2), use `s<=tN` and
`Cmax+B*S*s/3 <= (Cmax+B*S*t/3)*N`, then take logarithms
as in section 3. The same argument gives an effective
length bound for fixed `U,s`: all finite phase constants
can be bounded explicitly, and the right side of (G1)
is polynomial in `N`. The cycle product still gives
`A<=2tN`, so bounded length leaves finitely many positive
substituted words, including when some letters decrease.

To obtain (D1), let `q=den(W)` and use the actual positive
odd integer `3x+q` cycle supplied by the word-cycle
correspondence. Replace every phase intercept in the
coordinates by `qC_j`, so `y=B*x+qC_j`. Equations
(13)-(15) and the constants `K,R,Z,S` are unchanged.
The raw drift is now
`sum ln(1+q/(3x))<(qS/3)*sum 1/x_i`. Splitting at
`y_min=qCmax` as before yields

```
y_min < q*(Cmax+B*S*s/3)*G.
```

This proves (D1). The same scaling in sections 1-2 gives
the sharper final-letter denominator law. At any fixed
denominator bound `q<=q_*`, the exponential inequality
bounds `N`, and the actual-cycle product gives
`2^A<= (3+q_*)^(tN)`. Thus the positive letters are
bounded too, proving effective bounded-denominator
finiteness. No `q=1` convergence assertion is used in
these denominator laws.

### 5. For the background (2,1), four final-letter increases force N<7120

Now `P=9`, `Q=8`, `B=1`, `C=7`. With `s<=4`, exact
integer comparisons give

```
9^256 < 8^271,
gamma < 271/256,
H_s < 1+271/256+(271/256)^2+(271/256)^3
    = 73240879/16777216.
```

As `7(s+1)<=35<64`, (1) implies

```
c*N < 178+341*log_2(2N),    c=50331648/73240879.           (9)
```

Let `N_0=7120`. The integer comparison `7120^5<2^64`
gives `log_2(N_0)<64/5`, while

```
c*N_0-[178+341*(69/5)] = 3337644499/366204395 >0.          (10)
```

For `N>=N_0`, the elementary bounds `ln z<=z-1` and
`ln2>1/2` imply
`log_2(N/N_0)<=2(N/N_0-1)`. The right side of (9)
therefore increases by at most `682*(N-N_0)/N_0`, while
the left side increases by `c*(N-N_0)`, and `c>682/N_0`.
Thus (10) excludes every `N>=7120`:

```
N<=7119,      m=2N<=14238.                               (11)
```

### 6. A local exact replay excludes every remaining nontrivial cycle

Set `L=2^25=33554432`. The attached certificate verifies
that every odd seed `3<=n<L` reaches a smaller odd state
under the raw odd-only `3x+1` map. It checks all 16,777,215
seeds, using 58,580,426 odd steps in total. The largest
individual descent has 188 steps. A fixed per-seed guard
fails the certificate rather than allowing an unbounded run.
Induction on odd seeds proves that every positive odd
integer at most `L` reaches 1. Hence every state of a
nontrivial positive integer cycle exceeds `L`.

For every `1<=m<=14238`, the certificate also verifies
the exact integer inequality

```
(3L+1)^m < 2^bit_length(3^m)*L^m.                         (12)
```

An integer cycle of that length would satisfy

```
2^A=product_(j<m)(3+1/n_j)
   <=(3+1/L)^m < 2^bit_length(3^m).
```

But `2^A>3^m` requires `A>=bit_length(3^m)`, a
contradiction. This also excludes repeated traversals of
a nontrivial cycle. The only denominator-one words left
in (11) are repetitions of `(2)`, which in the specified
block format mean exactly `d_j=2` for every `j`.
The usual rotation identity preserves the denominator,
so all cyclic cuts have the same conclusion.

## Certificates

[`check_growth.py`](check_growth.py) checks the affine
coordinate identities and group equations by exact
arithmetic, with finite examples covering many expanding
backgrounds and nonzero additive parameters. The universal
argument is the written proof above, not that sample.

The certificate also checks the exact constants in
(9)-(10), replays all descents below `2^25`, and verifies
every one of the 14,238 inequalities (12) without floating
point. All powers are updated by integer multiplication;
the right side of (12) is a bit shift.

The eleven standard
[`3x+5,7,13,61` controls](../../../convergence/results/baseline-obligation-transfer-controls/README.md)
retain their exact arrows and denominators. For `3x+q`,
the corresponding shifted coordinate is `Bx+qC`, and
the right side of (1) contains `qC`; the `q=1` convergence
replay cannot be applied to those maps. A constructed
`3x+23` cycle with word `(2,3)` exercises the block format
directly and remains legal.

```
python3 areas/cycles/results/expanding-background-defect-growth/check_growth.py
```

The deterministic receipt is [`check_growth.json`](check_growth.json),
regenerated with `--write-receipt`. Checks use only the
standard library and remain active under `python3 -O`.
No external convergence verification or period bound is
imported.

## Remarks

- **Method and prior work.** This adapts the classical
  product-and-power-chain method for bounding cycles with
  few rising stretches, described in
  [Simons (2008), section 2.2 and section 4.2](../../../../sources/simons-2008-generalized-syracuse-cycles.md).
  The specific coordinate here groups an arbitrary fixed
  expanding valuation word. The proof is fully rederived;
  no theorem from that paper is assumed.
- **Direct precedent.** [Cerdá Bennassar (2026), theorems 8 and 10](../../../../sources/cerda-bennassar-2026-periodic-perturbations.md)
  uses the same `log_8(9)` integrality mechanism for `(1,2)`
  and states an exclusion for up to 19 increased positions,
  including both phases. The four-increase corollary here
  is an independently checked weaker case, not a new family
  exclusion. The arbitrary-background, arbitrary-substitution
  statement has broader template scope; novelty remains
  undetermined.
- **No asymptotic record claimed.** A
  [periodic-dictionary manuscript](../../../../sources/lyapunov-weaver-2026-periodic-dictionary-complexity.md)
  claims a stronger `log(N)*log(log(N))` lower order using
  Subspace Theorem inputs. That work has not been audited
  here. This node supplies explicit background constants
  under EXT-1 and a local finite replay, rather than claiming
  the strongest known asymptotic order.
- **What the count means.** In the general theorem, `s`
  counts changed letters; in the sharper corollary it
  counts increased block endings. It is
  neither rotation mismatch count nor the shortcut
  local-minimum count. For the final-letter construction
  with `U=(2,1)`, the ordinary shortcut
  local-minimum count is `N+s`, which can be unbounded even
  with `s<=4`. Thus the special exclusion is not simply a
  fixed-small-local-minimum theorem for the original map.
- **Relation to the previous lifted result.** The
  [lifted four-arc family](../lifted-four-arc-denominator-one-exclusion/README.md)
  has at most four `d_j>1` and contains a letter 1, so the
  explicit corollary excludes it. This result removes that
  node's arc lengths, marker equalities and total-parity
  structure; its separate resultant proof remains valid.
- **Why earlier background laws do not immediately give this.** The
  [fixed-defect theorem](../repeated-block-cancellation-bound/README.md)
  fixes one defect word and obtains its finiteness
  consequence for a contracting repeated block. Here the
  background expands and all substitutions and placements vary.
  In the natural [shared-background representation](../shared-background-denominator-law/README.md),
  there are `N` markers and their total is unrestricted;
  its fixed-marker-count/total finiteness statement is not
  this fixed-modification-count statement.
- **Limits and status.** The general four-mismatch question
  remains open: a sparse rotation need not have any such
  fixed expanding background. This is a written theorem
  conditional on EXT-1, with no independent-session review
  or Lean formalisation claimed.

## History

- 2026-11-08: Codex four-arc research lane (GPT-6 Astra;
  directed by Santiago Armstrong) derived the general
  shifted-coordinate bound for arbitrary positive substitutions
  and the arbitrary-placement
  `(2,1)` corollary. The classical cycle-bound strategy is
  credited explicitly; the finite closing calculation is
  reproduced locally.
