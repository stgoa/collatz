---
id: growing-prefix-unhandled-leading-input
kind: result
title: Arbitrarily long growing prefixes keep an unhandled leading input for the seven direct rules
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; rho(w) = nu(3w); the seven direct rules are the fixed dispatcher of
  two-inverse-phases-intermediate-increase (R41, R45, R44, R46, R47, R48, R50). The whole phase w = 3445 mod
  3456 has selected 3w, w = 1 mod 3 and q = rho(w) = -17 mod 5184, and all seven direct predicates fail on it.
  For r >= 1, s >= 1 and q = 81*2^(11r+6) s - 17, the first 7r quotient steps repeat a complete affine word with
  return Psi(q) = (2187q + 2363)/2048, Psi(q) + 17 = (2187/2048)(q + 17); all states are positive and every
  noninitial prefix exceeds q (the negative shadow only records congruences; the seed changes with r). Each
  cycle's critical states are two W5 endpoints and an intermediate W9 input whose complete d = 6 elimination
  keeps the next W5 endpoint at coefficient +1. For every prefix length n <= 7r, appending the deterministic H
  gives a unique largest-rank unaccepted request, so strict-rho expansion with those rules (and with R52, R53)
  cannot cancel the leading coefficient; the same holds in sigma, without licensing mixed ranks. This rules out
  a fixed lookahead guarantee for the stated procedure only; it gives no forever-growing positive orbit and does
  not exclude other currents, supplied history, input-dependent depth or other comparisons (later rules resolve
  parts of the phase).
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [two-inverse-phases-intermediate-increase, critical-image-rank-composition, critical-nine-elimination, variable-depth-inverse-escape-barrier, sigma-rank-removes-absorption-overhead, returning-second-forward-interface, low-block-continuation-prescribed-growth]
certificates: [check_legacy_replay.py]
evidence:
  - "check_rule_avoidance.py, rule_avoidance.py, rule_avoidance_audit.json: the legacy constructor and checker: 256 phase inputs, 48 positive families through 128 cycles, 148 lookahead positions, 20 full W9 plans and two separately ranked auxiliary expansions; three unfinished currents are stored. Fails at its new path: rule_avoidance.py puts ../double_inverse/ (now ../two-inverse-phases-intermediate-increase/) on sys.path and the checker loads further siblings by their pre-migration folder names. Passed at be73a66 as experiments/residual_progress/rule_avoidance/check_rule_avoidance.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
  - "negative_cycle_shadows.py, negative_cycle_shadows.json: side-lane FINDING probe (2026-10-17 23:32, the same feed entry as negative-cycle-backward-word): extending nu to negative odd integers, T = nu S has exactly the cycles {-1}, {-5, -7} and {-17, -25, -37, -55, -21, -31, -23} on |x| <= 4000; Psi here and G of low-block-continuation-prescribed-growth are the return maps of the last two; and on the returning row the deep 2-adic shadows of -3 and -11 are accepted by neither dispatcher at the sampled depths. Finite enumeration and measurement only: it does not prove that no other negative cycle exists (main-lane review side_lane_review_bae3969.md in ../negative-cycle-backward-word/). Fails at its new path: it imports sigma_rank and continued_rules from experiments/residual_progress/ by repository-relative path and fibre_count_check from its own folder (now ../absorbed-fibre-uniform-counts/). Passed at be73a66 as reviews/side_lane/negative_cycle_shadows.py (archive/legacy-checker-run-be73a66.md, exit 0)"
  - "The side-lane probe checking this node is ../sigma-rank-removes-absorption-overhead/batch_r51_r54_check.py (recorded under reviewed_by)."
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-17
    link: ../sigma-rank-removes-absorption-overhead/batch_r51_r54_check.py
    scope: "Finite only (side-lane feed entry 2026-10-17 23:32, VERIFIED, main 8764158; the R54 part), with the lane's own nu and step: for 400 consecutive w = 3445 (mod 3456), w is in W5, 3w is selected, w = 1 (mod 3) and nu(3w) = -17 (mod 5184); for q0 = 81*2^(11r+6) s - 17, r = 1..5, s in {1, 2, 3, 7}, each of the r seven-step T blocks ends at Psi(q) = (2187q + 2363)/2048 and every intermediate state exceeds q0. The leading-request argument and the W9 accounting were not rebuilt; the status stays written"
aliases: [R54]
tags: [convergence, outer-residual, tripling-pairs, critical-rank, scoped-obstruction, negative-cycle-shadow]
---

# Arbitrarily long growing prefixes keep an unhandled leading input for the seven direct rules

## Statement

Odd-only clock, 1 absorbing; `ν`, `T = νS`; `ρ(w) = ν(3w)`; "the seven rules" are the fixed dispatcher of [`two-inverse-phases-intermediate-increase`](../two-inverse-phases-intermediate-increase/README.md) (R41, R45, R44, R46, R47, R48, R50), and `H` is the deterministic formal absorption plan with full `W9` elimination.

1. **Unhandled phase.** Every `w ≡ 3445 (mod 3456)` is in `W5`, has selected `3w`, `w ≡ 1 (mod 3)` and `q = ρ(w) ≡ −17 (mod 5184)`. Its inverse parameters `D = 2`, `j = 1` exclude R46, and the other six predicates fail too, on the whole phase. This concerns the named recognisers, not existence of `P(w)` currents.
2. **Growing cycles.** For `r ≥ 1`, `s ≥ 1` and `q = 81·2^(11r+6)·s − 17`, the first `7r` quotient steps repeat a complete affine word with return `Ψ(q) = (2187q + 2363)/2048`, `Ψ(q) + 17 = (2187/2048)(q + 17)`. All actual states are positive and every noninitial prefix exceeds `q`. The negative shadow only records congruences; the seed changes with `r`.
3. **Leading request.** Each cycle's critical states are two `W5` endpoints and an intermediate `W9` input; the complete `d = 6` elimination of the latter keeps the next `W5` endpoint at coefficient `+1`. For every prefix length `n ≤ 7r`, appending the deterministic `H` gives a unique largest-rank unaccepted request (the current cycle's input at positions 0–2, the next cycle's at 3–6). Further strict-`ρ` expansion with these rules cannot cancel it; R52 and R53 do not apply at the lead. The same holds in `σ`, since `σ = ρ` on the lead and every other `σ` rank is smaller; arbitrary mixing of the ranks remains invalid.

This rules out a fixed lookahead guarantee for the stated procedure. It does not rule out another current representation, a supplied-history argument, input-dependent unbounded depth or another comparison, and gives no forever-growing positive orbit. Later rules (R55–R57) resolve whole parts of the phase.

## Proof

The legacy note "Arbitrarily long avoidance of the seven direct rules" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written infinite-family theorem and scoped compiler obstruction.**
For every prescribed finite lookahead, a full positive integer family
avoids all seven direct W5 rules. Its complete W9 elimination is accounted
for. The result does not give one indefinitely avoiding positive orbit,
exclude other currents, or prove or disprove Collatz. No novelty claim is
made.

**Subsequent scope update (R55–R57).** The named old rules below remain
fixed, including the R52/R53 extension in Section7. The new
[selected forward](../selected-critical-five-forward-tables/README.md),
[selected inverse](../two-selected-inverse-choices/README.md), and
[cycle-exit](../guarded-cycle-exit-phases/README.md) comparisons
resolve whole parts of this phase outside that procedure. Thus the phase
is no longer wholly unrecognized by the enlarged twelve-family dispatcher.
R57 also proves, by cancellation across the normalization bridge, that
the full seven-step quotient current equals a seven-arrow ordinary path
with a different list of intermediate states. The quotient prefixes below
are unchanged.

Use positive odd Syracuse S, absorbed at 1, the elementary minimum nu,
canonical quotient T=nu S, P(w)=[3w]-[w], and rho(w)=nu(3w).
The seven rules are exactly the fixed dispatcher in
[R50](../two-inverse-phases-intermediate-increase/README.md):
R41/R45/R44/R46/R47/R48/R50. Formal absorption H means the deterministic
R43 plan, including full R40 elimination of every W9 request. It has not
been supplied with unknown input currents.

### 1. An entire unhandled critical phase

Every positive integer

```
w=3445 mod3456
```

is in W5, has selected3w, and has critical image

```
q=(3w-1)/2=-17 mod5184,       5184=64*81.              (1)
```

Conversely (1) gives exactly that w progression. Here q is canonical
complementary, with binary first exponent 4, and w=1 modulo3. Write
q=-17+81h. Then

```
D=v3(q-1)=2,
u=(q-1)/9=-2+9h,
j=v3(16u+2)=v3(-30+144h)=1.                          (2)
```

Thus R46 does not recognize the input, since it requires j>=2. R41 and
R44 require divisibility of w by3; R45/R47/R48/R50 require nonselected3w.
All seven direct rules fail on this **whole phase**, not merely the
examples below. This statement concerns the named recognizers, not
existence of P(w) currents. For example, it does not exclude a separate
finite supplied history from certifying an individual input.

### 2. A full seven-step canonical cycle of affine formulas

For every positive q=-17 modulo2^17, the following are the exact T
prefixes. The last column is a convenient negative shadow for arithmetic;
the actual q and every actual state are positive.

| i | T^i(q) | shadow at q=-17 |
|---|---|---:|
|0|q|-17|
|1|(3q+1)/2|-25|
|2|(9q+5)/4|-37|
|3|(27q+19)/8|-55|
|4|(81q+33)/64|-21|
|5|(243q+163)/128|-31|
|6|(729q+617)/512|-23|
|7|(2187q+2363)/2048|-17|

The ordinary valuation at steps0,1,2 is1. At step3 the ordinary successor
is y=(81q+65)/32, with valuation2. It is in the selected class of -41:
v2(y+1)=3 and its odd unit is3 modulo4. Normalization sends it to
(y-1)/2, giving row4. The subsequent ordinary valuations are1,2,2;
these successors are canonical already. Every entry's exact binary
class follows by substituting q=-17+2^17h: the prefix differences are
the corresponding positive power-of-three multiple of2^(17-B), where
B is its displayed denominator exponent. All divisions are exact, and
the extra bits needed for the valuations and selected normalization are
retained. The last state is -17 modulo64 and canonical.

Every noninitial prefix has numerator slope exceeding its denominator
and positive offset. It is therefore strictly above q. The complete
return is

```
Psi(q)=(2187q+2363)/2048,
Psi(q)+17=(2187/2048)*(q+17),       Psi(q)>q.           (3)
```

These are seven **quotient** steps. At step3 the current implementing
normalization contains its full signed ordinary bridge. This is not
silently counted as one ordinary Syracuse arrow. The two R26 run labels
are (4,2) and (2,4): the second return decreases from row4 while remaining
above the cycle's original q.

### 3. Arbitrarily many repetitions, with complete critical-state accounting

For all integers r>=1 and s>=1 put

```
K=11r+6,       q_0=81*2^K*s-17.                      (4)
```

Its first7r quotient steps repeat the table r times. At the i-th cycle
start,

```
q_i+17=3^(7i)*2^(K-11i)*81s.                         (5)
```

For i<r the binary exponent in (5) is at least17, so Section2 applies
inductively. For i=r it is at least6, leaving the endpoint canonical.
Every cycle start stays -17 modulo81. Every noninitial quotient state
in this entire prefix exceeds q_0, and q_0<q_1<...<q_r.

The critical states in each cycle are exactly rows0,4,7:

- Rows0 and7 are1 modulo3, hence correspond to W5 indices
  w_i=(2q_i+1)/3 in (1). All seven direct rules fail there.
- Row4 is0 modulo3 and11 modulo16, hence its index
  v=(27q_i+11)/64 belongs to W9.
- Rows1 and2 are complementary2 modulo3. Rows3,5,6 are1 modulo8.
  These are noncritical states with their usual elementary induction
  steps; they must not be mislabeled W5 events.

Consequently no fixed quotient lookahead guarantees a directly accepted
W5 event. The starting positive integer varies with r; no positive seed
is claimed to realize infinitely many repetitions. For any **fixed finite**
supplied canonical history Q, taking s large enough makes q_0>max Q;
then the entire displayed prefix lies outside nu^(-1)(Q). This does not
exclude the seed-dependent complete smaller-origin history Q_<q_0.

### 4. Full W9 elimination retains the next unhandled frontier

At row4 let v=T^4(q)/3=(27q+11)/64. Direct arithmetic gives

```
v2(9v-1)=6,
R40 upper endpoint = q'=Psi(q),
R40 lower endpoint = ell=(729q+2153)/2048,
q'=3ell-2.                                          (6)
```

Indeed the R40 parameter is z=3(9v-1)/64, and its endpoints are
6z+1 and2z+1. The complete W5 plan for P(v) is its prescribed prefix
current plus H_(q')-H_ell. The upper plan H_(q') has a leading request
P(w'), w'=(2q'+1)/3, with coefficient+1, followed by H_(w'). All its
other requests have ranks at most(3q'+4)/4<q'. The lower side has rank
at most(9ell+5)/8=(3q'+11)/8<q'. Thus full recursive W9 elimination
retains w' as its unique largest-rank request, with coefficient+1.

For the absorption H_(T^4(q)), also add H_v. Its requested ranks obey

```
(9v+5)/8=(243q+419)/512 < q'.                        (7)
```

The frontier q' is below T^4(q), but above the cycle's starting q.
The W9 stage really reduces its own rank; it does not reduce the rank
below the initial input. The leading w' is in (1) and remains outside
all seven direct rules. W9 requests have not been silently discarded.

### 5. Every lookahead length retains a nondecreasing input

Start with w_0 from (4), choose any n with0<=n<=7r, and denote the exact
quotient prefix current from q_0 to x=T^n(q_0) by D_n. Let N_a bridge
a to nu(a), and z=nu(w_0). Form the full deterministic lookahead plan

```
J_n=N_(3w_0)+D_n-N_(w_0)+H_x-H_z.                    (8)
```

Its divergence is P(w_0) minus every signed W5 request from H_x-H_z.
Write n=7i+j, 0<=j<=6, except the final endpoint n=7r. Its coefficient
vector has one unique largest-rank request, with coefficient+1:

```
w_i       if j=0,1,2;
w_(i+1)   if j=3,4,5,6;
w_r       at n=7r.                                  (9)
```

**Proof of the complete split.** At row0, H asks w_i and then H_(w_i),
whose other requests have smaller rank. At rows1 and2, the deterministic
inverse point step reverses the preceding ordinary valuation1 arrow;
this reaches row0 with no new pair. At row3, H prioritizes its forward
arrow because this state is1 modulo8, and normalization reaches row4.
Section4 gives the unique leading request there. At rows5 and6 the
canonical1-modulo8 forward steps reach row7, again with no intermediate
pair. Finally H_z has ranks below q_0, because z<=(w_0-1)/4. It cannot
cancel any of the displayed leading requests. This proves (9), including
the row3 boundary where forward priority matters.

Every displayed leading rank is at least q_0 and its direct recognizer
fails. Every other request has strictly smaller rank. Expanding any or
all of those other requests by the seven strict-rho rules cannot create
that leading request, regardless of coefficient signs. It therefore
cannot cancel its coefficient+1. The rules' finite conditional closure
still leaves a nondecreasing unproved input.

This is a **scoped no-go** for a specified procedure: bounded quotient
lookahead, deterministic H conversion including W9, and arbitrary further
seven-rule expansion. It does not prohibit another absorption representation,
an independently supplied leading current, an unknown-history query,
another inverse word, or a different joint comparison.

#### A whole-cycle signed comparison

For one cycle the equivalent explicit boundary is

```
P(w)=div J+P(w')+requests(H_(w'))-requests(H_(nu(w))).  (10)
```

All auxiliary ranks are below the **original** q, since
`3q'+4<4q` is equivalent to1631q>15281, true in (4).
Repeating (10) leaves the final unaccepted w_r at coefficient+1 and all
other ranks below q_r. The saved constructor retains these full currents
and coefficients, rather than treating the growing comparison as descent.

### 6. Why the previous growing-word obstruction is not enough here

For a full even R26 block with canonical raw endpoint f, first exponent
a>=3 and ternary-unit initial t, its maximal inverse parameters at f are
exactly D=d/2,j=a-1. If f exceeds the block's initial q, R46 accepts the
critical input corresponding to f: the inverse endpoint is precisely the
smaller q and j>=2. The forward path and that inverse path cancel exactly.
This is the same scoped undo identity as R48, now interpreted from the
growing endpoint. In particular the (5,4) block in R31's old growing word
is intercepted by R46. Acceptance at a later larger rank need not give
descent below the original input; it can merely return to that input.

The present family is different: its selected normalization creates the
intermediate W9 state, and its terminal inverse has j=1. Sections4–5
account for the resulting complete formal dependencies.

### 7. Additional-rule scope and reproducibility

Every leading w_i has selected3w_i and w_i=1 modulo3. Therefore any new
direct rule restricted to nonselected3w or to E_return (w=3 modulo9)
cannot recognize it. This applies to the checked domain predicates of
[R51 forward](../sigma-rank-removes-absorption-overhead/README.md),
[R52 returning continuation](../returning-second-forward-interface/README.md)
and [R53 nonselected continuation](../low-block-continuation-prescribed-growth/README.md).
Adding R52/R53 to the rho-decreasing closure therefore still cannot cancel
the largest request in (9).

The separate R51 sigma compiler uses the **same** H currents and
coefficients. It has sigma(u)<=rho(u) everywhere and equality on the
leading inputs w_i, since they are not E_return. Consequently (9) also
has a unique largest sigma request, and R51's direct dispatcher does not
recognize it. Any further strictly sigma-decreasing expansion preserves
this unhandled leading coefficient. This is a separate valid argument;
it does not license arbitrary mixing of rho-only and sigma-only rules.
New rules covering the selected, nondivisible-by3 phase require a fresh
audit.

```
python3 experiments/residual_progress/rule_avoidance/check_rule_avoidance.py
```

The checker validates the complete phase predicates, exact affine prefixes
and full signed boundaries, long prescribed repetitions, every short
lookahead position, W9 leading requests, and rejected invalid parameters.
The receipt stores an actual unfinished comparison and its coefficients.
All iteration counts are explicit and finite; no future orbit is searched.
The theorem's universal quantifiers come from (1)–(9), not the samples.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B11 migration; standard library). The legacy scripts in this folder load their sibling modules by pre-migration folder names, so they no longer run here. This certificate rebuilds the legacy directory layout in a temporary directory from the node folders that now hold those files, runs the unmodified legacy checks there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied receipt unchanged. It writes nothing in the repository. It replays: the legacy checker `check_rule_avoidance.py` (about 1 s; the counts of section 7 and the stored unfinished currents, compared with `rule_avoidance_audit.json`). The command in the legacy text names `experiments/residual_progress/rule_avoidance/`.

## Remarks

- **Negative cycles.** `Ψ` is the return map of the negative 7-cycle `{−17, −25, −37, −55, −21, −31, −23}` of `T` extended to negative integers (side-lane feed 2026-10-17 23:32, probe `negative_cycle_shadows` in this folder; a finite enumeration on `|x| ≤ 4000`). Its backward word gives [`negative-cycle-backward-word`](../negative-cycle-backward-word/README.md), whose domain is exactly the `k = 4` domain of [`two-selected-inverse-choices`](../two-selected-inverse-choices/README.md).
- **Later rules on this phase:** [`selected-critical-five-forward-tables`](../selected-critical-five-forward-tables/README.md), [`two-selected-inverse-choices`](../two-selected-inverse-choices/README.md), [`guarded-cycle-exit-phases`](../guarded-cycle-exit-phases/README.md) and [`maximal-inverse-cycle-continuation`](../maximal-inverse-cycle-continuation/README.md). The "subsequent scope update" paragraph of the note was added by the main lane at commit `7206f9c`.
- Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/rule_avoidance/RULE_AVOIDANCE.md` (legacy ID R54) at commit `be73a66`, by the B11 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; `check_legacy_replay.py` was added at the migration. The side-lane probe `reviews/side_lane/negative_cycle_shadows.*` moved here. Legacy status: "written arithmetic families and scoped obstruction to a specified lookahead/closure procedure".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `8764158`. The batch's "independent model" proof and code reviews (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents, not a different lane.
- 2026-10-17, commit `7206f9c`: the main lane added the "Subsequent scope update (R55–R57)" paragraph near the top of the note.
