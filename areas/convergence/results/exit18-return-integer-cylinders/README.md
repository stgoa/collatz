---
id: exit18-return-integer-cylinders
kind: result
title: "Every finite mixed exit-18 return word has a complete integer cylinder; eventually periodic itineraries are negative"
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; rho(w) = nu(3w); G the R67 guard w = 40529845 mod 2^26, V(w) = (3^12 w +
  311195)/2^19, R(w) = (3^24 w + 328537586155)/2^37. Returning to G by V has complete domain 2218391138229 mod 2^45,
  by R the domain 8515171531530858421 mod 2^63; the domains are disjoint, and every maximal-count-m exit-18
  re-entry of R70 is exactly V^(m-1) R. For every finite word omega over {V, R} with e = 19 #V + 37 #R and ell = 12
  #V + 24 #R, the integers following omega with every state in G form exactly one residue class mod 2^(26+e);
  every member is a positive realisation, any extra odd-modulus congruence can be added by CRT, and the seed may
  depend on omega. The full currents telescope to D_(3w0,3wk) + J_wk - J_w0 with requests {wk: 1} + A_wk - A_w0
  (quotient clock ell; ordinary clocks (ell+1, 1) or (ell+6, 6) after V or R). Every eventually periodic infinite
  itinerary has a negative rational starting point, so a positive integer surviving forever needs an aperiodic
  itinerary; for fixed m the integers making at least m returns have density 2^(-26) s^m (s = 2^(-19) + 2^(-37)),
  and possible infinite survivors in [1, X] number at most 3 (X/2^26)^alpha. Neither sparsity nor the periodic
  exclusion proves that no survivor exists; no accepted rule is added.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [mixed-rank-growing-blocks, mixed-exit-growing-reentry]
certificates: [check_legacy_replay.py]
evidence:
  - "check_integer_prefix.py, integer_prefix.py, integer_prefix_audit.json: the legacy constructor and checker: 510 finite words with 1530 positive lifts, 20 long words through 256 symbols, 108 odd-CRT cases, nine maximal-count lists, 310 eventually periodic points, 32 density/count checks, 30 full signed compositions, two complete unfinished current tables, 30 missing-supply rejections, three cap/exit cases and ten invalid-input rejections; 47 imported sources pinned. Fails at its new path: integer_prefix.py loads ../mixed_exit/ (now ../mixed-exit-growing-reentry/) by its pre-migration folder name; it is loaded in turn by the later legacy itinerary_complexity/ code. Passed at be73a66 as experiments/residual_progress/integer_prefix/check_integer_prefix.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
  - "batch_r73_r74_check.py, batch_r73_r74_check.json: side-lane probe (Claude side lane, 2026-10-18 02:19) of R73's two pair identities and R74's word arithmetic; signed-pair-frontier-normalisation cites it from this folder. Fails at its new path: it imports affine_controls from experiments/packet_currents/negative_controls/ by repository-relative path (now ../locally-collatz-like-control-barrier/). Passed at be73a66 as reviews/side_lane/batch_r73_r74_check.py (archive/legacy-checker-run-be73a66.md, exit 0); its receipt is reproduced byte for byte by check_legacy_replay.py"
  - "side_lane_review_d3a91fe.md: the main lane's pinned review (2026-10-18) of side commit d3a91fe: byte-identical reproduction of batch_r73_r74_check under a 30 s cap, with its scope limits"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: batch_r73_r74_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 02:19, VERIFIED, main aefdf60), with the lane's own odd-only step: 600 random words in V and R of length at most 12, three lifts each: the composition (3^ell w + c)/2^e with e = 19 #V + 37 #R and ell = 12 #V + 24 #R; every intermediate image an integer in G on the stated full domain; each point in the next symbol's stated domain; strict growth; every word's periodic fixed point a negative rational. Per the main lane's review (side_lane_review_d3a91fe.md): finite independent arithmetic, not a proof that the aperiodic survivor set is empty; the eventually periodic conclusion rests on the written pullback argument. The status stays written"
aliases: [R74]
tags: [convergence, outer-residual, mixed-rank, integer-cylinders, two-adic-coding, negative-cycle-shadow]
---

# Every finite mixed exit-18 return word has a complete integer cylinder; eventually periodic itineraries are negative

## Statement

Odd-only clock, 1 absorbing; `ρ(w) = ν(3w)`. `G = {w > 0 : w ≡ 40529845 (mod 2^26)}` is the guard of [`mixed-rank-growing-blocks`](../mixed-rank-growing-blocks/README.md); `V(w) = (3^12 w + 311195)/2^19` and `R(w) = (3^24 w + 328537586155)/2^37` are its two returns (R67 and [`mixed-exit-growing-reentry`](../mixed-exit-growing-reentry/README.md)).

1. **Two disjoint returns.** Returning to `G` by `V` has complete domain `2218391138229 mod 2^45`; by `R`, `8515171531530858421 mod 2^63`. The domains are disjoint, and every maximal-count-`m` exit-18 re-entry is exactly the word `V^(m−1)R`.
2. **Complete cylinders.** For every finite word `ω` over `{V, R}` with `e = 19#V + 37#R`, `ℓ = 12#V + 24#R`, the positive integers following `ω` with every listed state in `G` form exactly one residue class mod `2^(26+e)`; all its members are realisations, and any extra congruence to an odd modulus can be added by CRT. So every finite list of maximal re-entry counts occurs; the seed may depend on the word.
3. **Currents and clocks.** The full currents telescope to `D_(3w0,3wk) + J_wk − J_w0` with requests `{wk: 1} + A_wk − A_w0`; the leading request is larger than the original, and helpers can exceed the original rank. Quotient clock `ℓ`; ordinary common-tail clocks `(ℓ+1, 1)` or `(ℓ+6, 6)` when the last symbol is `V` or `R`.
4. **Periodic words and density.** Every infinite word determines one 2-adic point; every eventually periodic one has a negative rational starting point, so a positive integer surviving forever needs an aperiodic itinerary. For fixed `m` the integers making at least `m` returns have natural density `2^(−26)·s^m`, `s = 2^(−19) + 2^(−37)`, with counting error below `2^m`; possible infinite survivors in `[1, X]` number at most `3(X/2^26)^α`, `α = log 2/log(2/s)`, for `X ≥ 2^26`.

Neither the sparsity bound nor the periodic exclusion proves that no survivor exists: that is the open question [`aperiodic-exit18-return-survivors`](../../questions/aperiodic-exit18-return-survivors.md). No accepted rule is added.

## Proof

The legacy note "Integer realization of every mixed exit18 return word" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written whole-class prefix theorem, exact conditional-current
constructor, and bounded replay.** Every finite sequence of the existing
exit18 re-entries has infinitely many positive integer realizations. Every
eventually periodic infinite return itinerary has a negative rational
starting point, so a hypothetical positive integer that survives forever
must have an aperiodic itinerary. This does **not** exclude such an integer,
prove termination of the return system, or supply its larger requested pair.

The inputs are the proved [R67 growing comparison](../mixed-rank-growing-blocks/README.md)
and [R70 exit and re-entry interface](../mixed-exit-growing-reentry/README.md).
No external theorem or empirical feed assertion is used. The optional feed
was read at `7150f312e0b9bd1099fb617ee680acb22cf1187e`; its corrected transfer
scope agrees with the distinction here. The [R71 denominator result](../../../cycles/results/mechanical-word-exact-denominator/README.md)
concerns periodic cycle closure. Its integrality obstruction cannot simply
be applied to a finite prefix without the closure equation.

**Literature context, not a proof premise.** Bernstein and Lagarias,
[*The 3x+1 Conjugacy Map*, Canadian Journal of Mathematics 48(6), 1996](https://doi.org/10.4153/CJM-1996-060-x),
describe a full 2-adic shift conjugacy for the shortcut clock. The coding
argument below is an explicit scoped instance for these two returns, with
their guards, signed currents and separate odd/quotient clocks. No novelty
is claimed for 2-adic itinerary coding or finite-prefix realization.

### 1. Two disjoint returns to the same guard

Use the positive pair indices and constants

```
A=531441=3^12, M=2^19, B=311195, D=A−M=7153,
G={w>0 : w=40529845 mod2^26}, b=40529845,
V(w)=(Aw+B)/M,
P=A^2, C=B(A+M), L=M^2/2=2^37,
R(w)=(Pw+C)/L=2V^2(w).
```

Here `R` denotes this re-entry map, not the older root-collapse operator.
Every `w` in `G` is in W5, has canonical `3w`, and has `rho(w)=3w`.
The ordinary and quotient clocks retain the meanings in R67 and R70.

Consider **returns to G**, rather than the unconditioned affine maps.
Their complete positive domains are

| Symbol | Domain | Target | Consumed precision | Quotient steps | Ordinary common-tail clocks |
|---|---|---|---:|---:|---|
| V | `w=2218391138229 mod2^45` | `V(w) in G` | 19 | 12 | (13,1) |
| R | `w=8515171531530858421 mod2^63` | `R(w) in G` | 37 | 24 | (30,6) |

For either row, solving `a w+c=2^e b mod2^(e+26)` gives the displayed
single residue, since `a` is odd. That residue reduces to `b mod2^26`.
Thus these are necessary and sufficient return domains, including every
intermediate integrality and valuation condition already proved in R67/R70.

They are disjoint for a structural reason. Put `Y(w)=Dw+B`. Then

```
Y(V(w))=(A/M)Y(w),
Y(R(w))+B=(P/L)Y(w).                                  (1)
```

A V return requires `v2(Y(w))>=45`. An R return has
`v2(Y(w))=37` exactly, because its target has `2^26|Y(R(w))` and `B` is odd.
Both return maps strictly increase every positive input in their domains.
Their real affine slopes are greater than1 and their offsets are positive.

#### This exhausts the existing exit18 re-entries

The R70 return with maximal old-guard count `m>=1` is precisely

```
V^(m−1) followed by R.                                (2)
```

Indeed the first `m−1` V arrows remain in G. At the next parent the exact
Y-order is37, so there is exactly one old R67 block left; its exit order
is18. The additional R70 continuation returns to G. Conversely every R70
exit18 re-entry has this decomposition. Its affine map is `2V^(m+1)`,
exactly R70's general formula. This covers every maximal depth m, but does
not claim that other exit valuations return or that this subsystem exhausts
all available Collatz comparisons.

### 2. Every finite mixed word has a complete integer cylinder

Let `omega` be any nonempty finite word over `{V,R}`. Set

```
e=19 #V +37 #R, ell=12 #V +24 #R, a=3^ell,
F_omega(w)=(a w+c)/2^e.
```

The positive odd offset c is computed in chronological order, starting
with `(a,c,e)=(1,0,0)` and appending a row `(alpha,beta,f)` by

```
(a,c,e) -> (alpha a, alpha c+beta 2^e, e+f).            (3)
```

**Complete-cylinder theorem.** An integer `w>0` follows all symbols in
omega, with every listed intermediate state and its terminal state in G,
if and only if

```
w = r_omega mod2^(26+e),
r_omega=(2^e b−c)a^(-1) mod2^(26+e).                  (4)
```

The least residue is positive and odd. Every member
`r_omega+j2^(26+e)`, `j>=0`, is a positive integer realization. All its
successive states strictly increase.

**Proof.** Following a legal word gives the terminal congruence in(4), so
necessity is immediate. Conversely the terminal congruence makes the full
affine output an integer in G. For every earlier prefix, its numerator
multiplied by the odd suffix multiplier differs from the full numerator by
a multiple of that prefix's denominator. Thus the full divisibility implies
every intermediate denominator divides its numerator. All intermediate
states are integers. Starting at the terminal G state and working backwards,
the single-return calculation in §1 puts each predecessor in the appropriate
complete return domain, hence in G. Positivity follows instead in the forward
direction from the positive initial value and both positive affine maps.
The start is in G and therefore odd and nonzero. ∎

Equivalently, pulling a cylinder of precision p back through V or R produces
one cylinder of precision `p+19` or `p+37`, respectively. The extra precision
already contains every exact valuation bit; this theorem does not replace
an exact valuation cylinder by the insufficient modulus `2^sum(a_i)`.

For any positive odd integer h and any residue t, CRT appends `w=t mod h`
to(4), giving a complete positive progression of period `h2^(26+e)`.
No condition on an initial odd modulus, by itself, eliminates any finite
word. Conditions on later states are induced by the same formulas and must
not be assumed independent.

In particular every prescribed finite list `m1,...,mk` of positive maximal
old counts occurs: apply(4) to
`V^(m1−1) R ... V^(mk−1) R`.

### 3. Full signed currents and both clocks

Write the fixed formal absorption plan as

```
[x]=div J_x + sum_v A_x(v) P(v),  P(v)=[3v]−[v].
```

These are identities with supplied pair-current premises; they do not
assert that `x` has been absorbed. Let `w0,...,wk` be the state sequence of
a legal word. Summing the existing complete R67/R70 comparisons gives

```
K_omega = D_(3w0,3wk)+J_wk−J_w0,
c_omega = {wk:+1}+A_wk−A_w0,
div K_omega = P(w0)−sum_v c_omega(v)P(v).              (5)
```

Every source multiplicity and sign is retained. All intermediate J terms
and their request vectors cancel exactly. This identity comes from actual
comparison rows, not just the affine endpoint equation.

The leading coefficient is+1. Every other nonzero request has
`rho(v)<3w_(k−1)<3wk`, using the existing single-return helper bound on the
last edge and the monotone heights. For k=1 the first strict bound reads
`rho(v)<3w0`; for longer words those helpers can exceed the **original**
rank `3w0`. In every case the leading request has `3wk>3w0` and remains
unresolved. Expanding only nonleading requests by strict-rho plans cannot
cancel it. Another representation or comparison at wk is not excluded.

The quotient clock is exactly ell. The ordinary common-tail clocks are

```
(ell+1,1) if omega ends in V,
(ell+6,6) if omega ends in R.                         (6)
```

To check composition, each local comparison is the ordinary path of length
`ell_i+c_i` from `3w_i` minus the length-`c_i` path from `3w_(i+1)`, with
`c_i` equal to1 or6. Every subsequent macro has at least12 quotient steps.
Those common tails therefore compose: its remaining ordinary prefix is long
enough to pass each preceding bridge. Equivalently, cancel the negative
length-`c_i` prefix against the next local path, then continue from their
equal states. The result is exactly the path of length `ell+c_last` from
`3w0` minus the path of length `c_last` from `3wk`. This proves both the
current identity and the clocks. No clock is assigned to the extra formal
absorption terms in(5).

### 4. Periodic closure and the remaining aperiodic question

Every infinite symbolic word has nested cylinders(4), with precision tending
to infinity. Consequently it determines exactly one odd 2-adic integer.
Every finite prefix still has arbitrarily large positive integer lifts.
The disjoint return domains make this coding injective.

For a nonempty finite cycle word, `a>2^e` and `c>0`. Its unique fixed point is

```
x_cycle=−c/(a−2^e)<0.                                (7)
```

Its denominator after reduction is odd. Nested cylinders for repeated
copies show that it is exactly the 2-adic point of that periodic itinerary.
For an eventually periodic word with preceding affine prefix
`(a0 w+c0)/2^e0`, its unique starting point is

```
x_start=(2^e0 x_cycle−c0)/a0 <0.                      (8)
```

Thus **no positive integer can have an eventually periodic infinite
itinerary in this return system**. This is a sign obstruction after imposing
cycle closure; it is not a proof that every itinerary is eventually periodic.
Any positive infinite survivor would have a genuinely aperiodic word and
strictly growing states. No such survivor is constructed here, and no claim
that none exists is proved.

The distinction is exact: for each finite word there is a different complete
positive progression, whereas one positive integer satisfying all prefixes
would have to equal the single 2-adic limit. Inferring the latter from the
former, or excluding it merely by testing periodic words, is invalid.

### 5. Exact prefix density, with a uniform counting error

Distinct words of the same symbol length m have disjoint cylinders: at
their first differing symbol the return domains are disjoint, and each
preceding affine map is injective. Let E_m be the positive integers making
at least m returns in this subsystem, define E_0=G, and put

```
s=2^(-19)+2^(-37)=262145/137438953472.
```

There are `2^m` cylinders, each with density `2^(-26-e)`. Therefore

```
density(E_m)=2^(-26) s^m,
| #(E_m intersect[1,X]) − X 2^(-26) s^m | < 2^m.       (9)
```

The first identity is an exact natural density for each **fixed** m. The
second is a uniform real-X counting bound from one interval-floor error
per cylinder. This is not an independence hypothesis.

The possible infinite-positive-survivor set is contained in every E_m, so
it has natural density zero. More quantitatively, for `X>=2^26`, write
`alpha=log(2)/log(2/s)`. Choosing
`m=ceil(log_(2/s)(X/2^26))` in(9) gives

```
#(possible infinite survivors intersect[1,X])
    <= 3 (X/2^26)^alpha.                              (10)
```

Indeed the two terms on the right of the counting bound are at most
`(X/2^26)^alpha` and `2(X/2^26)^alpha`. This sparsity bound permits a
nonempty exceptional set. It does not prove termination on any untested
integer and does not justify a probabilistic assertion about a fixed orbit.

### 6. What the theorem changes

The entire existing exit18 re-entry class supports arbitrary finite mixed
return words on the ordinary positive integer lattice. Exact finite-word
integrality, even with an additional starting congruence at any odd modulus,
cannot exclude those words. Periodic closure does exclude their positive
periodic points, but leaves a precise aperiodic survivor question.

A termination argument for this class must add a constraint on the **same
integer across unbounded prefixes**, a well-founded state that survives both
return branches, or a different signed-current construction. Neither this
statement nor R71 implies that such a constraint is unavailable. No new
accepted family is added to the seventeen-rule dispatcher.

### 7. Executable interface and bounded verification

`integer_prefix.py` supplies `cylinder`, `family`, `odd_lift`,
`maximal_counts`, `rational_point`, the complete signed `plan`, and a capped
trace. `compile_plan` requires every pair current, including the larger
leading one; an empty supply is rejected. A trace cap is unresolved, and
leaving this return system is not asserted to be Syracuse descent.

Run `python3 experiments/residual_progress/integer_prefix/check_integer_prefix.py`.
The adjacent receipt records exact ranges, source hashes, full signed
examples, and checks of the ordinary and quotient clocks. The default test
replays the saved receipt; `--write-receipt` refreshes it. Mathematical
quantifiers rest on the proofs above, not the bounded examples.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B12 migration; standard library). The legacy scripts of this folder load sibling modules by their pre-migration paths, so they no longer run here. This certificate calls `tools/legacy_replay.py`, which rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, runs the unmodified legacy scripts there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied file unchanged. It writes nothing in the repository. It replays: the legacy checker `check_integer_prefix.py` (about 45 s; the counts of section 7 of the note and the stored current tables, compared with `integer_prefix_audit.json`) and the side-lane probe `batch_r73_r74_check.py` (under 1 s, receipt reproduced byte for byte). The commands in the legacy text name `experiments/residual_progress/integer_prefix/`.

## Remarks

- **Literature context, not a premise:** Bernstein and Lagarias's 2-adic conjugacy for the shortcut clock; no novelty is claimed for itinerary coding or finite-prefix realisation.
- The mechanical-word denominators of [`mechanical-word-exact-denominator`](../../../cycles/results/mechanical-word-exact-denominator/README.md) (R71) concern periodic cycle closure; their integrality obstruction cannot be applied to a finite prefix without the closure equation.
- The first same-seed constraint across unbounded prefixes is [`same-seed-factor-complexity-bound`](../same-seed-factor-complexity-bound/README.md) (R77).

## History

- Migrated from `experiments/residual_progress/integer_prefix/INTEGER_PREFIXES.md` (legacy ID R74) at commit `be73a66`, by the B12 migration (Claude, Opus 5.5). Note, scripts and receipt moved byte-identical; `check_legacy_replay.py` was added at the migration. The side-lane probe `reviews/side_lane/batch_r73_r74_check.*` and the main lane's review `experiments/residual_progress/side_lane_review_d3a91fe.md` moved here. The open aperiodic case became the question [`aperiodic-exit18-return-survivors`](../../questions/aperiodic-exit18-return-survivors.md). The legacy checker of R77 pinned this note's hash, so editing it makes that checker fail (see [`same-seed-factor-complexity-bound`](../same-seed-factor-complexity-bound/README.md)). Legacy status: "written complete prefix and counting theorem for the specified return subsystem; aperiodic integer survival remains open".
- Main lane (ChatGPT, Codex), 2026-10-18, from commit `aefdf60`. The batch's "independent model" proof and code reviews (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents, not a different lane.
