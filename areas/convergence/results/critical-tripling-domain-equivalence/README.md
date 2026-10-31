---
id: critical-tripling-domain-equivalence
kind: result
title: Tripling currents on the binary domain W = {5 mod 8} u {9 mod 16} biject onto the critical induction seeds and are already equivalent to Collatz convergence
status: reviewed
claim: >
  Odd-only 3x+1 map S on positive odd integers (state 1 killed); B, nu of elementary-bridge-quotient-normal-form;
  P(w) = [3w] - [w] a signed source. (Critical seeds) Every positive odd seed reduces to a smaller one by a proved
  elementary or ordinary step unless it lies in C = {q in B : q = 3 mod 4, q != 2 mod 3}. (Bijection) With
  W = {w odd : w = 5 mod 8 or w = 9 mod 16}, g(w) = nu(3w) is a bijection W -> C with w < g(w) and inverse q/3
  (q = 0 mod 3) or (2q+1)/3 (q = 1 mod 3). (Equivalence) The following are equivalent: every positive odd integer
  reaches 1; every w in W has a finite integer current with divergence P(w); every positive odd w has one (no
  uniform cost, height, clock or computability assumption). So restricted universal tripling is full-strength
  convergence, not a helper lemma. (Formal plans) Adjoining a formal edge 3w -- w for every odd w to the complete
  elementary identity graph makes it connected, with a terminating normaliser whose rows satisfy
  v - 1 <= (2/3)(q - 1), so the number of requested pair inputs is logarithmic in the start; these are conditional
  plans: an actual current is obtained only after every missing pair input is supplied and checked, and the bound
  says nothing about the cost of the inputs. The ordinary arrow identities use 3x+1 specifically.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [elementary-bridge-quotient-normal-form]
certificates: [check_tripling_recompute.py, check_legacy_replay.py]
evidence:
  - "check_tripling.py, tripling.py, tripling_audit.json: the legacy plan constructor (local steps with exact boundaries, static and critical decreasing plans, compile_plan accepting only checked supplied pair currents) and checker (16,384 local steps, 6,144 inputs of W, 2,731 critical inverse inputs, 2,048 formal plans, 40 compiled examples from 34 distinct supplied pair currents found by capped absorption searches on bounded sample inputs). Fails at its new path: tripling.py loads ../bridge_normal_form/normal_form.py (now ../elementary-bridge-quotient-normal-form/) by its pre-migration path. Passed at be73a66 as experiments/residual_progress/tripling_equivalence/check_tripling.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a). tripling.py is also loaded by its old path by the later legacy experiments/residual_progress/w9_closure/, finite_centres/ and by experiments/phase6/stopping_calibration/check_calibration.py. Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "batch_436f51f_check.py, batch_436f51f_check.json: side-lane probe (Claude side lane, 2026-10-17) of R37, R38 (odd-h-pair-interface-compiler), R39 (coupled-even-pair-recursion) and negative controls on W. Fails at its new path: it imports affine_controls from experiments/packet_currents/negative_controls/ by repository-relative path (now ../locally-collatz-like-control-barrier/) and fibre_count_check from its own folder (now ../absorbed-fibre-uniform-counts/). Passed at be73a66 as reviews/side_lane/batch_436f51f_check.py (archive/legacy-checker-run-be73a66.md, exit 0). The main lane's reproduction of it, with three W5 control witnesses, is ../tripling-doubling-pair-decomposition/side_lane_review_1a2dfc5.json (kept there because check_pair_domain_external.py reads it). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-17
    link: batch_436f51f_check.py
    scope: "Finite only (side-lane feed entry 2026-10-17 21:31, VERIFIED, main 436f51f; the R37 part): with the lane's own nu and Syracuse step, all 16,668 critical roots below 200,000 map back into W under the stated inverse (q/3 or (2q+1)/3), the inverse is always smaller than q, and nu(3w) = q recovers the root; all 16,668 images of W below 200,000 are critical and distinct. The entry also acknowledged that universal currents for P on W are equivalent to Collatz. The written equivalence and the plan termination were not re-derived; the status stays written"
  - by: Claude side lane (Opus)
    date: 2026-10-17
    link: ../critical-nine-elimination/batch_r40_r41_check.py
    scope: "Finite only (side-lane feed entry 2026-10-17 21:53, VERIFIED, main 4a45eb0; the R37 part, the planner as restated in R40), rebuilt with the lane's own nu and Syracuse step: normalize q = nu(x); if q = 1 (mod 8) step to S(q) < q; if q = 2 (mod 3) go to (2q-1)/3 < q; otherwise request u = q/3 or (2q+1)/3 and continue from u. Checked for all 99,999 odd x < 200000: it terminates, every request lies in W5 u W9, requests strictly decrease, and u <= (2x+1)/3. The equivalence and the compiler were not re-derived; the status stays written"
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Full argument re-derived (critical seeds, the bijection W to C, both directions of the Collatz equivalence including the finite-component lemma, the formal normaliser and its bound (5)); both certificates re-run (exit 0); bijection, counts and normaliser re-checked with the lane's own nu below 2^17 and the 3x+d control counts of the Remarks reproduced; verdict HOLDS (one imprecision noted: the claim's first sentence omits the seed 1)"
aliases: [R37]
tags: [convergence, outer-residual, tripling-pairs, critical-domain, collatz-equivalent, conditional-plans]
---

# Tripling currents on the binary domain W = {5 mod 8} u {9 mod 16} biject onto the critical induction seeds and are already equivalent to Collatz convergence

## Statement

Odd-only clock on positive odd integers, `S(1) = 1` for path algebra, state 1 killed, `[x]` the killed point mass; `B`, `ν` and the elementary currents `N_x` (`div N_x = [x] − [ν(x)]`) from [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md); `P(w) = [3w] − [w]` is a source, not a supplied current.

1. **Critical seeds.** A noncanonical `x` reduces to `ν(x) < x`; a canonical `q ≡ 1 (mod 8)`, `q > 1`, has `S(q) < q`; a canonical `q ≡ 2 (mod 3)` has the smaller predecessor `(2q − 1)/3`. The only remaining least-counterexample seeds are `C = {q ∈ B : q ≡ 3 (mod 4), q ≢ 2 (mod 3)}`.
2. **Bijection.** With `W = {w odd : w ≡ 5 (mod 8) or w ≡ 9 (mod 16)}`, `g(w) = ν(3w)` is a bijection `W → C`, `w < g(w)`, with inverse `q/3` (`q ≡ 0 mod 3`) or `(2q + 1)/3` (`q ≡ 1 mod 3`).
3. **Equivalence.** These are equivalent: (i) every positive odd integer reaches 1; (ii) every `w ∈ W` has a finite integer current with divergence `P(w)`; (iii) every positive odd `w` has one. No uniform cost, height, clock or computability is assumed in (ii). Completing (ii) is therefore a full-strength convergence problem, not a helper lemma.
4. **Conditional formal plans.** In the complete elementary identity graph with a formal edge `3w — w` for every odd `w`, a terminating normaliser connects every vertex, each row satisfying `v − 1 ≤ (2/3)(q − 1)`, so a plan requests at most logarithmically many pair inputs. A plan yields an actual current only once every missing pair input is supplied and checked; the bound concerns neither the cost of `J_w` nor the work to find it. This does not contradict the disconnected graph of [`tripling-doubling-pair-decomposition`](../tripling-doubling-pair-decomposition/README.md), which grants tripling only at `w ≡ 3 (mod 8)`.

Neither universal pair existence nor convergence is proved; the identities use `3x+1` specifically. No novelty or formal verification is claimed.

## Proof

The legacy note "The exact critical domain for tripling-pair currents" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

2026-10-17. **Written equivalence and conditional finite compiler; bounded
checks.** Neither universal pair existence nor Collatz convergence is proved.
No novelty or formal verification is claimed. This note uses only the proved
[elementary normal form](../elementary-bridge-quotient-normal-form/README.md) and
ordinary Syracuse arrows. It sharpens the scope discussion in
[the general pair decomposition](../tripling-doubling-pair-decomposition/README.md).

Write `S(x)=(3x+1)/2^v2(3x+1)` on positive odd integers, with S(1)=1 for
path algebra. Kill state1 in measures and currents. For a finite integer
current J, `div J=(I-S_*)J`. Write `[x]` for the killed point mass and

```
P(w)=[3w]-[w],       F(x)=4x+1.
```

Here P(w) is a signed **source**, not an already supplied current. An exact
pair current must have precisely that divergence. No synchronised merger
clock is required by this note.

### 1. Elementary components and the remaining induction seeds

Recall the canonical set B:

* q=1 modulo8;
* q=2^a t-1 with a>=2, t positive odd, and t=-3^a modulo4.

The second class consists of the complementary roots. The complete proved
elementary component of q is the pair of F-rays

```
C_q={F^j(q), F^j(2q+1): j>=0}.
```

Its least member is q. Write nu(x) for this canonical minimum, and N_x for
the proved finite elementary current with
`div N_x=[x]-[nu(x)]`. The partner 2q+1 is selected, so
`nu(2q+1)=q`. In general a root `x=2^a t-1`, a>=2, is selected when
`t=3^a modulo4`; its half `(x-1)/2` is canonical and is its minimum.
These facts are proved in the linked normal-form note, not premises about
unproved tripling pairs.

Three kinds of seed already admit a reduction to a smaller positive odd
integer:

1. A noncanonical x has `nu(x)<x` through N_x.
2. A canonical q=1 modulo8, q>1, has `S(q)<= (3q+1)/4<q`.
3. A canonical q=2 modulo3 has the positive odd predecessor
   `p=(2q-1)/3<q`, with `3p+1=2q`, hence `S(p)=q` exactly.
   Its reverse arrow is the signed current `-delta_p` with divergence
   `[q]-[p]`.

Consequently the only remaining least-counterexample seeds are

```
C={q in B: q=3 modulo4 and q is not2 modulo3}.          (1)
```

This is a reduction of the possible least counterexample, not a claim that
each earlier operation decreases on every unrestricted orbit.

### 2. A bijection with two binary tripling domains

Define

```
W={w>0 odd: w=5 modulo8 or w=9 modulo16},
g(w)=nu(3w).                                          (2)
```

**Theorem.** The map g is a bijection from W onto C. Every w in W satisfies
`w<g(w)`. Its inverse is

```
w=q/3,          q in C and q=0 modulo3;
w=(2q+1)/3,     q in C and q=1 modulo3.                 (3)
```

**Proof.** If w=9 modulo16 then 3w=11 modulo16. This is complementary
with a=2, so `g(w)=3w`, a member of C divisible by3.

If w=5 modulo8 then 3w=7 modulo8, an F-root with a>=3. If it is
complementary, `g(w)=3w` belongs to C and is0 modulo3. Otherwise it is
selected; its canonical half `(3w-1)/2` has exponent a-1>=2 and therefore
is complementary rather than1 modulo8. This half is1 modulo3. Both
possible images are strictly larger than w, since w>=5.

Conversely, take q in C. When q=0 modulo3, put w=q/3. If q has a=2,
complementarity says q=11 modulo16, hence w=9 modulo16. If a>=3,
q=7 modulo8 gives w=5 modulo8. In both cases `nu(3w)=q`.
When q=1 modulo3, put w=(2q+1)/3. Because q=3 modulo4,
`2q+1=7 modulo8`, hence w=5 modulo8. Its triple is the selected partner
2q+1 and has minimum q. The image's residue modulo3 distinguishes the
two formulas, proving uniqueness. Every operation is on positive odd
integers, and both formulas in (3) give w<q. This proves the theorem.

The apparent binary simplicity of W does not mean that its tripling
currents are known. For instance its first inputs include5,9,13,21,25.

### 3. Restricted universal tripling is already Collatz-equivalent

The following statements are equivalent:

1. Every positive odd integer reaches1 under S.
2. For every w in W there is a finite integer current J_w with
   `div J_w=P(w)`.
3. For every positive odd w there is such a current J_w.

There is no uniform cost, support-height, clock, or computability assumption
in statement2. Each current is finite; its size may depend arbitrarily on w.

**Proof.** Statement1 supplies finite absorption path currents H_x, and
`J_w=H_(3w)-H_w` proves statement3. Statement3 implies statement2.

Assume statement2. Use strong induction on the positive odd source x.
Apply the smaller-seed reductions in Section1 whenever possible. In the
remaining case x=q in C, the unique w from (3) is smaller than q. The
supplied pair current and the elementary current at its upper endpoint give

```
div (J_w-N_(3w)) = [q]-[w].                           (4)
```

Add the already proved absorption current of w. This constructs a finite
integer current with divergence `[q]`. The same construction works in the
other three induction cases, and x=1 requires the zero current.

For completeness, a finite current with divergence `[x]` forces actual
absorption of x. In the finite graph of its nonzero current arrows and their
endpoints, summing divergence over a component not meeting1 gives zero.
Thus the component containing x must meet1. Every edge is an actual
deterministic S arrow; any finite undirected path to the absorbing state
implies that the forward orbit of x joins the orbit of1. Hence x reaches1.
This completes the implication to statement1.

The theorem identifies the precise missing comparison interface in this
induction. Completing it is a full-strength convergence problem, not a proved
helper lemma. Proved partial constructions on W can still be useful if they
leave a smaller, explicitly described unresolved family.

### 4. All tripling edges connect the complete elementary identity graph

For a separate operation-set statement, form an undirected **formal** graph
using all proved elementary identities and an added edge `3w--w` for every
positive odd w. Ordinary S arrows outside the elementary identities are
not needed in this paragraph. The graph is connected, and it has the
following terminating normalizer.

First reduce x to q=nu(x). Stop at q=1. For q>1 use the appropriate row:

| q modulo3 | formal path | smaller endpoint v | required pair base |
|---|---|---|---|
|0|q=3v -- v|q/3|v|
|1|q -- 2q+1=3v -- v|(2q+1)/3|v|
|2|q -- F(q)=3u -- u -- v|(2q-1)/3|u=(4q+1)/3|

The first and third moves in the final row are proved elementary moves.
To check the last move, it remains to prove u is selected. If q=1 modulo8
and q=2 modulo3, then q=17 modulo24 and u=23 modulo32. Thus u has a=3
and odd part3 modulo4, exactly the selected condition. Otherwise write
q=2^a t-1 complementary. Since q=2 modulo3, t is divisible by3, and

```
u+1=2^(a+2)(t/3),
t/3 = 3t = -3^(a+1) = 3^(a+2) modulo4.
```

So u is selected and its minimum is v=(u-1)/2. This also proves v is
canonical in that row. In every row v is positive odd and v<q.
Normalize v and repeat. This proves connectivity even when intermediate
vertices exceed the original input.

More quantitatively, every row has

```
v-1 <= (2/3)(q-1).                                    (5)
```

Thus the number of formal tripling invocations is logarithmic in the starting
height: if at least r invocations occur, then
`2 <= (2/3)^(r-1)(x-1)`. This bounds only the number of missing inputs
requested by a formal plan. It bounds neither the cost of J_w nor the work
needed to discover it. The algorithm terminates as a **conditional plan**;
its actual current is obtained only after all its missing pair inputs are
supplied and checked.

This statement includes selected-halving identities. No connectivity theorem
is asserted here for the smaller graph generated by F and tripling alone.
Nor does it contradict the earlier disconnected graph that grants tripling
only at w=3 modulo8: the operation sets differ.

### 5. Executable boundary checks and finite evidence

`tripling.py` implements both decreasing plans. For each local step from x
to v it returns an explicit elementary/ordinary current C and either no
missing input or a specified w, with the checked exact boundary

```
div C=[x]-[v]-P(w).
```

The plan retains every occurrence of a missing pair. Its total boundary is
`[x]-sum P(w)`. `compile_plan` accepts only explicitly supplied currents,
checks every pair divergence, and adds them with positive orientation.
Missing or incorrect inputs cause an error. Current-row cancellation is
performed exactly, with state1 killed.

The bounded checker verifies local boundaries, the finite portions of the
bijection in both directions, complete decreasing plans, and compiled
absorption examples. The demonstration input currents are obtained by capped
ordinary absorption searches on explicitly bounded sample inputs; those
searches prove only their finite examples. The stored receipt includes exact
final current tables for selected examples, hashes of all other checked
rows, input bounds, and caps.

The default receipt checks16,384 local steps,6,144 inputs of W,2,731
critical inverse inputs,2,048 formal plans, and40 actual compiled examples.
The examples use34 distinct supplied pair currents. These are bounded
verification counts, not a universal pair construction.

Reproduce from the repository root:

```
python3 experiments/residual_progress/tripling_equivalence/check_tripling.py
```

The proof, not these finite tests, supplies the universal equivalence and
the formal plan's termination. No universal pair current is generated. The
construction certifies individual roots; it makes no simultaneous source
capacity claim for an annular submeasure. Ordinary arrow identities and the
elementary bridges specifically use3x+1; generalized odd maps are not
automatically covered by this theorem.

## Certificates

- [`check_tripling_recompute.py`](check_tripling_recompute.py) (written at the B10 migration, about 1 s, standard library). With its own `S` and `ν` it checks, against [`tripling_audit.json`](tripling_audit.json): the bijection in both directions for every odd `w < 32768` in `W` (6144 images) and every critical `q < 32768` (2731 inverses), with the receipt's domain and inverse hashes; the 16,384 local steps (`div C = [x] − [v] − P(w)` exactly, `v < x`, the bound (5), critical requests in `W`) and their hash; the complete formal plans for odd `x < 2048` in both modes with the logarithmic bound and hash; and the 40 compiled examples (divergence exactly `[x]`), the 34 supplied pair inputs, the two stored final current tables (seeds 27 and 31) and the receipt hashes, and that a plan with absent or zero pair inputs is rejected.
- The command in the legacy text names `experiments/residual_progress/tripling_equivalence/`.

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B18-replay-revival migration; standard library) replays the unmodified legacy checks `check_tripling.py`, `batch_436f51f_check.py` in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, requiring exit 0 and every file unchanged (about 24 s). It checks finite steps only; the status is unchanged.

## Remarks

- **Controls on `W`.** The generic statement that `w` and `3w` share a future fails on `W` for every control map (feed 2026-10-17 21:31; counts below 4000): `3x−1`, 336 cases (e.g. `w = 5`, cycle `{5, 7}`, against 15, trivial); `3x+13`, 285 (e.g. `w = 41` against 123, cycle at 259); `3x+61`, 57 (e.g. `w = 133` against 399, the 41-cycle). The main lane's checker [`check_pair_domain_external.py`](../tripling-doubling-pair-decomposition/check_pair_domain_external.py) re-verifies three such `W5` witnesses. Restricting the input domain therefore does not remove the need for specific `3x+1` arithmetic.
- **Later checks.** The side lane later rebuilt the R37 planner as restated in R40 (feed 2026-10-17 21:53, probe [`batch_r40_r41_check.py`](../critical-nine-elimination/batch_r40_r41_check.py), in the folder of [`critical-nine-elimination`](../critical-nine-elimination/README.md)): for all odd `x < 200000` it terminates, every request lies in `W5 ∪ W9` and strictly decreases, and `u ≤ (2x + 1)/3`. It is recorded under `reviewed_by`.
- **What uses it.** [`odd-h-pair-interface-compiler`](../odd-h-pair-interface-compiler/README.md) connects the odd-`h` interface to the critical roots; [`critical-nine-elimination`](../critical-nine-elimination/README.md) (R40) eliminates the `W9` half, leaving the open premise [`universal-w5-tripling-currents`](../../questions/universal-w5-tripling-currents.md), and [`critical-image-rank-composition`](../critical-image-rank-composition/README.md) (R43) and the later rules rank and reduce the `W5` requests. The Collatz-equivalence agrees with the class-wise picture of [`class-wise-obligation-equivalence`](../class-wise-obligation-equivalence.md).
- Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/tripling_equivalence/TRIPLING_EQUIVALENCE.md` (legacy ID R37) at commit `be73a66`, by the B10 migration (Claude, Opus 5.5). Note, scripts and receipt moved byte-identical, with the side-lane probe `reviews/side_lane/batch_436f51f_check.*`. The plan placed the main lane's reproduction receipt `side_lane_review_1a2dfc5.json` here; it is in [`tripling-doubling-pair-decomposition`](../tripling-doubling-pair-decomposition/README.md) because the checker there reads it. `check_tripling_recompute.py` was added at the migration. Legacy status: "written equivalence and explicit conditional compiler; finite checks".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `436f51f`. The batch's "independent model" proof and code reviews of R37–R39 (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents. The side lane's finite check is recorded under `reviewed_by`.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No correction to the text; the review notes that the claim's first sentence should exclude the seed 1 (the absorbing state), as the body's Statement 1 does ([`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md)).
