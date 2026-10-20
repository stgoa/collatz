---
id: coupled-even-pair-recursion
kind: result
title: A coupled source C(v) = delta_(18v+3) - delta_v recurses where the split pair catalogue provably fails, closing two d = 4 entry domains of the even-return obligation
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; P(u) = delta_(3u) - delta_u, D(u) = delta_(2u+1) - delta_u. (Obligation) For
  a complementary root with even d = 2k, the remaining obligation after the run bridge is
  Q_k(w) = D(3^k w) + sum_(j<k) P(3^j w), an identity of sources only. (Split obstruction) The split catalogue at
  d = 4 (elementary D(9w), then separate calls for P(w) and P(3w) by the mixed-shrinking-pair-rules recognizer, with
  the missing-one-mod-8-pair-domain entries for 1-mod-8 inputs) accepts exactly when w = 105 mod 256 and R33 accepts
  (9w-1)/16; R33 never accepts both P(v) and P(6v+1) (infinite descent). This is an algorithm-specific
  obstruction. (Coupled recursion) For v = 19 mod 32, t = (3v-1)/8 < 3v/8, an explicit local current has divergence
  C(v) - C(t) (child added); every positive v = 39 mod 8192 has S^5(18v+3) = S^7(v); the cylinders c_r mod
  2^(13+3r) give exactly r coupled rewrites then the terminal rule, with S^(r+5)(18v+3) = S^(r+7)(v); the
  recognizer terminates on every input. (Entries) Two complete d = 4 entry domains (B: w = 105 mod 256 with R33
  accepting v; A: w = 17 mod 128 with the coupled C(v) accepted) give J_x with div J_x = delta_x - delta_q and
  S^(a+l+2)(x) = S^(a+l+2)(q) for complementary x, q = (x-1)/2, with complete original cylinders for every a, old
  return 9w > x for a >= 5, and fixed-cylinder weighted R_N counts within 6 of 25N/(72 L_a); with a supplied current
  for q (absorption below N is an input) x is certified at weight 1 or 2. The joint recognizer remains partial.
  This does not close all d4, all even d, or R37's critical domain.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [elementary-bridge-quotient-normal-form, complementary-run-bridges, mixed-shrinking-pair-rules, tripling-doubling-pair-decomposition, missing-one-mod-8-pair-domain]
certificates: [check_even_pairs_recompute.py, check_legacy_replay.py]
evidence:
  - "check_even_pairs.py, even_pairs.py, even_pair_audit.json, branch_A_weight2_current.csv, branch_B_weight2_current.csv: the legacy constructor and checker (57 joint cylinders through depth 64, 8192 split-catalogue inputs and 8192 simultaneous-child failures, 384 original cylinders, 12 actual required-ray sources with both weights, 24 exact weighted counts, two supplied-current conversions with a 10000-arrow cap on the lower inputs). Fails at its new path: even_pairs.py loads ../pair_one/pair_one.py (now ../missing-one-mod-8-pair-domain/, which itself no longer runs) by its pre-migration path. Passed at be73a66 as experiments/residual_progress/even_pair_closure/check_even_pairs.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a). The later legacy experiments/residual_progress/joint_frontier/ loads even_pairs.py by its old path. Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-17
    link: ../critical-tripling-domain-equivalence/batch_436f51f_check.py
    scope: "Finite only (side-lane feed entry 2026-10-17 21:31, VERIFIED, main 436f51f; the R39 part): for all 6,250 v = 19 mod 32 below 200,000, with t = (3v-1)/8 < 3v/8, the pairs 18v+3 ~ 18t+3 and v ~ t each meet at a state other than 1 within 3 steps; the terminal cylinder v = 39 mod 8192 satisfies S^5(18v+3) = S^7(v). The split-catalogue proposition, the entry constructions and the counts were not re-derived; the status stays written"
aliases: [R39]
tags: [convergence, outer-residual, pair-recursion, doubling-pairs, coupled-sources, cylinders, conditional, constructive]
---

# A coupled source C(v) = delta_(18v+3) - delta_v recurses where the split pair catalogue provably fails, closing two d = 4 entry domains of the even-return obligation

## Statement

Odd-only clock, absorbing at 1, `div = I − P`, `F(z) = 4z + 1`; `P(u) = δ_(3u) − δ_u`, `D(u) = δ_(2u+1) − δ_u`.

1. **Even-return obligation.** For complementary `x = 2^a t − 1` with `3^(a−1)t − 1 = 2^d w`, `d = 2k`, the run bridge of [`complementary-run-bridges`](../complementary-run-bridges/README.md) and the half prefix `q → w` leave exactly `Q_k(w) = D(3^k w) + Σ_(j<k) P(3^j w)` (an identity of sources). `D(u)` is elementary exactly when `u` is canonical ([`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md)); universal `D` is Collatz-equivalent ([`tripling-doubling-pair-decomposition`](../tripling-doubling-pair-decomposition/README.md)), and R34's decreasing inverse chain leaves the whole even domain unchanged.
2. **Split-catalogue obstruction (`d = 4`).** The split catalogue (elementary `D(9w)`, then separate calls for `P(w)` and `P(3w)` by the recognizer of [`mixed-shrinking-pair-rules`](../mixed-shrinking-pair-rules/README.md), with the entries of [`missing-one-mod-8-pair-domain`](../missing-one-mod-8-pair-domain/README.md) for `1 (mod 8)` inputs) accepts exactly when `w ≡ 105 (mod 256)` and R33 accepts `(9w − 1)/16`. R33 never accepts both `P(v)` and `P(6v + 1)` (simultaneous acceptance repeats at a strictly smaller parameter). This is an algorithm-specific obstruction, not one to exact currents.
3. **Coupled recursion.** For `v ≡ 3 (mod 4)` let `C(v) = δ_(18v+3) − δ_v`. For `v ≡ 19 (mod 32)`, `t = (3v − 1)/8` (`0 < t < 3v/8`, `t ≡ 3 mod 4`): `S(18v + 3) = 2(18t + 3) + 1`, `S(v) = F(t)`, and an explicit `L_v` has `div L_v = C(v) − C(t)`; the child current is added, and `t` may be `7 (mod 8)`, the class the split recognizers lose. Every positive `v ≡ 39 (mod 8192)` has words `(2,2,3,6)` and `(1,1,2,1,4,1)` and `S^5(18v + 3) = S^7(v)` (the modulus 4096 does not suffice). The cylinders `c_r mod 2^(13+3r)` of (5) perform exactly `r` rewrites then terminate, with `S^(r+5)(18v + 3) = S^(r+7)(v)`. The recognizer terminates on every input, returning a current or unresolved.
4. **Two `d = 4` entries.** **B:** `w ≡ 105 (mod 256)`, R33 accepting `v = (9w − 1)/16`. **A:** `w ≡ 17 (mod 128)`, the coupled recognizer accepting `C(v)`, `v = 3(w − 1)/16` (first class `w ≡ 932625 mod 1048576`). Both construct `δ_f − δ_w` with `f = 18w + 1`, and then `J_x` with `div J_x = δ_x − δ_q`, `S^(a+l+2)(x) = S^(a+l+2)(q)`, `q = (x − 1)/2 < N`. Each parent cylinder gives complete original cylinders (11) for every `a ≥ 2`; the old return `9w` exceeds `x` for `a ≥ 5`, unboundedly. For each fixed cylinder the weighted `R_N` mass is within 6 of `25N/(72 L_a)` (not a global asymptotic), with actual sources of both weights on the required ray. With a supplied current for `q` (absorption below `N` is the input), `x` is certified at weight `c = 1` or `2`.

The joint recognizer remains partial. This does not close all `d = 4`, all even `d`, or R37's critical domain ([`critical-tripling-domain-equivalence`](../critical-tripling-domain-equivalence/README.md)). No novelty is claimed.

## Proof

The legacy note "A coupled recursion for part of the missing even-return domain" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status:** written exact identities, a partial terminating constructor, complete
infinite cylinders, and checked finite currents. Collatz and universal completion
of the even-return domain remain open. No novelty claim is made.

This note uses the odd Syracuse map, absorbed at1, and killed atoms at1. Write
`div=(I-P)` and `F(z)=4z+1`. It builds on [R25's complete elementary
classification](../elementary-bridge-quotient-normal-form/README.md),
[R26's complete complementary run](../complementary-run-bridges/README.md),
[R33's mixed pair recursion](../mixed-shrinking-pair-rules/README.md), and
[R36's two entry branches](../missing-one-mod-8-pair-domain/README.md). The new mechanism
retains a **sum** of two pair obligations that the old separate recognizers can
never accept simultaneously.

### 1. The full even-return obligation and its helper gap

Every complementary root has unique parameters

```
x=2^a t−1, a≥2, t odd, t=−3^a mod4,
3^(a−1)t−1=2^d w, d≥2, w positive odd.
```

For even `d=2k`, put `u=3^k w` and `f=2u+1`. Actual integrality gives
`w=2 mod3`. R26 supplies the finite prefix `x→f` in `a+k−1` arrows; the
smaller half `q=(x−1)/2` reaches w in `a−1` arrows. Thus the additional
obligation is exactly

```
Q_k(w)=δ_(2*3^k*w+1)−δ_w
      =D(3^k w)+sum_(j=0)^(k−1) P(3^j w),
D(u)=δ_(2u+1)−δ_u,    P(u)=δ_(3u)−δ_u.                  (1)
```

This is an identity of sources; it does not supply any of their currents.
Although `Q_k(w)=Q_(k−1)(3w)+P(w)` lowers k, its other parameter increases.
The resulting helpers can exceed the original x, so assuming their absorption
would not be a decreasing induction.

R25 classifies D(u) as elementary **exactly when u is canonical**. Indeed,
`2u+1` is a3-modulo4 F-root; it is the selected partner of u precisely when u
is canonical. If u is noncanonical, `2u+1` is itself complementary and its
half is u. Consequently the missing D helper is another instance of the
unresolved half comparison. In the actual even domain u is divisible by3 and
its ternary unit `u/3^k` is2 modulo3. No equivalence between this narrower D
subdomain alone and all of Collatz is asserted. R35 proves equivalence for
universal D over all positive odd u, so that universal helper cannot be assumed.

Every normalized even return is either f, which is1 modulo3, or u, which is0
modulo3. Hence `v3(nu(f)+1)=0`: R34's strictly decreasing canonical inverse
chain leaves the whole even domain unchanged. The construction below addresses
part of that gap by explicit currents.

### 2. An exhaustive failure of the separate pair catalogue at d=4

Define a particular **split catalogue** as follows. It attempts to certify
`Q_2(w)` by elementary D(9w), a call for P(w), and a separate call for P(3w).
For a3-modulo8 input it uses exactly R33's mixed recognizer. For a1-modulo8
input it uses exactly R36's A/B entries followed by that recognizer. Other
input classes are rejected. This definition permits no extra forward arrows,
alternative aliases, or external current inputs.

**Proposition.** For every positive odd w, this split catalogue accepts exactly
when

```
w=105 mod256 and R33 accepts v=(9w−1)/16.                (2)
```

The key obstruction is stronger than a failed search:

> For no positive `v=3 mod8` does R33 accept both P(v) and P(6v+1).

For the second input, `v2(3(6v+1)−1)=3`. Its only possible R33 transition is
O with child `(9v+1)/4`, so acceptance forces `v=19 mod32`. The first input
then also has valuation3. Acceptance forces its child
`t=(3v−1)/8` to be3 modulo8, equivalently `v=51 mod64`. The two children are
exactly t and `6t+1`. Both calls would therefore again have to succeed at a
strictly smaller positive parameter. Infinite descent excludes such a pair.

To exhaust the split catalogue, if w is1 modulo8 it must enter A or B.
On A, `w=17 mod128`, the two child obligations are precisely P(v) and P(6v+1),
with `v=3(w−1)/16`; the obstruction applies. On B, (2), the second input3w
has even paired valuation4 and terminal z=3v, which is1 modulo8. Also9w is
canonical. Thus only the first child's acceptance is required.

If w is3 modulo8, then3w must enter A or B. Its A class requires
`w=91 mod128`; then `9w=3 mod16` is selected, not canonical, so the elementary
D call fails. Its B class requires `w=35 mod256`; then R33's first call has
valuation3 and child5 modulo8, so fails. Inputs5 and7 modulo8 are outside the
catalogue. This proves the proposition. It is an obstruction to the named
split algorithm, not to exact currents for those sources.

### 3. Retaining the coupled source escapes that obstruction

For every positive `v=3 mod4` define

```
C(v)=δ_(18v+3)−δ_v.                                    (3)
```

When v is3 modulo8, `3v` is canonical and `6v+1` is its selected partner.
Consequently the sum `P(v)+P(6v+1)` differs from C(v) by the negative of an
explicit elementary D(3v) current. Keeping this combined source permits a
larger child domain than the two separate P recognizers.

**Coupled rewrite.** If `v=19 mod32`, set `t=(3v−1)/8`. Then

```
0<t<3v/8<v,     t=3 mod4,
S(18v+3)=2(18t+3)+1,     S(v)=F(t).                     (4)
```

The source `18v+3` is1 modulo8, so its valuation is exactly2. The source v
is3 modulo4, so its valuation is1; these give (4) directly. Also `18t+3` is
1 modulo8, hence canonical. Let B be its elementary selected-partner current,

```
div B=δ_(2(18t+3)+1)−δ_(18t+3).
```

Then the explicit local current

```
L_v=δ_(18v+3)+B−δ_v−δ_(F(t))+δ_t
```

satisfies `div L_v=C(v)−C(t)`. **Add** the child current to finish C(v).
In particular t may be7 modulo8. This is precisely the child class lost by
the separate recognizers.

If the child has the prescribed merger

```
S^ell(18t+3)=S^(ell+2)(t),   ell≥2,
```

then the parent has the same relation with ell replaced by `ell+1`. The
selected partner in (4) agrees with `18t+3` after two arrows at equal clock;
F(t) agrees with t after one arrow at equal clock. No assumption that either
trajectory reaches1 is used.

#### A complete terminal cylinder

For every positive `v=39 mod8192`, the two exact prefix words are

```
18v+3: (2,2,3,6),          S^4(18v+3)=(729v+241)/4096=z,
v:     (1,1,2,1,4,1),      S^6(v)=(729v+1265)/1024=F(z).
```

Thus `S^5(18v+3)=S^7(v)`. These are affine identities throughout the
stated cylinder, not a trajectory extrapolation from v39.

The left word has total valuation13 and needs14 bits of its seed. Since the
seed is `18v+3`, with coefficient valuation1, parameter precision13 bits is
exactly sufficient. The left seed cylinder is `18v+3=705 mod16384`;
dividing its even coefficient gives exactly `v=39 mod8192`. The right word
has total valuation10 and full seed cylinder `v=39 mod2048`, which is implied.
The extra bit is therefore retained.
Replacing8192 by4096 changes the left closing valuation at v4135, so that
weaker cylinder would not preserve the stated words. The final shared
valuation after z/F(z) is not fixed and is not silently charged as one bit.

#### A closed recursive family

For each integer `r≥0`, let `(c_r,M_r)` be

```
c_0=39, M_0=8192,
M_(r+1)=8M_r,
c_(r+1)=(8c_r+1)*3^(-1) mod M_(r+1).                  (5)
```

Every positive `v=c_r mod M_r` performs exactly r coupled rewrites, then
the terminal rule. Thus `M_r=2^(13+3r)` and

```
S^(r+5)(18v+3)=S^(r+7)(v).                             (6)
```

Inverting `3v=8t+1` modulo `8M_r` proves the complete cylinder. Since each
child is3 modulo4, its parent is19 modulo32. Earlier termination is
impossible: all recursive states are19 modulo32, whereas the terminal class
is7 modulo32. The recursion decreases the positive integer parameter by a
factor below3/8. The recognizer therefore terminates on every input, returning
either an explicit finite current or **unresolved**; only the accepted family
(5) is claimed to receive a certificate.

The first recursive class is `v=43795 mod65536`. Its first child is7 modulo8,
so the split catalogue provably cannot reproduce it. The new constructor
uses its joint source instead.

### 4. Two complete d=4 entries into smaller-half comparisons

Keep the complementary x of Section1, now with `d=4`, and put

```
f=18w+1,     q=(x−1)/2,
S^(a+1)(x)=f,     S^(a−1)(q)=w.                        (7)
```

#### B: the complete successful split branch

Let `w=105 mod256` and `v=(9w−1)/16`. Then v is11 modulo16. Suppose R33
constructs P(v) with clock ell, so `S^ell(3v)=S^(ell+1)(v)` and `ell≥3`.
R36 B gives P(w) at clock `ell+2`. R33 applied to3w is automatically terminal:

```
v2(9w−1)=4,     z=3(9w−1)/16=3v=1 mod8,
S^3(9w)=S^4(3w).
```

Finally9w is canonical1 modulo8, so f is its selected partner. Adding these
three currents constructs `δ_f−δ_w`, with

```
S^(ell+1)(f)=S^(ell+3)(w).                             (8)
```

The elementary child-terminal cylinder `v=59 mod128` gives
`w=105 mod2048`, ell3. More generally every R33 mixed word ending in its
terminal cylinder gives a complete B parent provided its child residue is
11 modulo16. Arbitrary recursive depths occur, for example words beginning
with E1 or E2 and then any permitted continuation.

#### A: the joint recursion succeeds where separate P calls cannot

Let `w=17 mod128`, `v=3(w−1)/16`, and suppose the coupled C(v) constructor
accepts. Here v is3 modulo8, so its depth in (5) is at least1. Write
`L=18v+3`, which is canonical1 modulo8. Exact first arrows give

```
S(f)=F(2L+1),     S(w)=F(v).                           (9)
```

Normalize the first expression to L using its explicit F and selected-partner
bridges. For the second expression use only the explicit F bridge to v;
normalizing v further would alter the child source. Add the C(v) current.
This constructs `δ_f−δ_w`. If C(v)'s clock is ell, (9) implies exactly (8).
For a depth-r joint child, `ell=r+5`. The first w cylinder is
`w=932625 mod1048576`, with r1.

#### Exact original clock and lower input

In both entries, combine the R26 prefix in (7), the current `δ_f−δ_w`, and
the **negative** of the q-to-w prefix. The result J_x satisfies

```
div J_x=δ_x−δ_q,
S^(a+ell+2)(x)=S^(a+ell+2)(q).                         (10)
```

B's first terminal therefore has equal clock `a+5`. A's depth-r family has
equal clock `a+r+7`. Only q is an absorption input. For every actual R_N
source, `x<3N/2`, so `q<N`. No unknown larger return is used as an induction
input, irrespective of the heights of these prescribed prefixes.

### 5. Complete original cylinders and actual source multiplicities

Suppose either entry has a complete w cylinder `w=b mod m`, where m is a
power of2. For every integer `a≥2`, set

```
t_a=(16b+1)*3^(-(a−1)) mod16m,
x_a=2^a t_a−1,       L_a=2^a*16m.                     (11)
```

Every positive `x=x_a mod L_a` has exactly the stated a, exactly d4, and
w in the prescribed parent cylinder. Conversely the parent cylinder with
these a,d gives (11). This follows by multiplying the definition
`16w=3^(a−1)t−1`; t is odd and w is odd, retaining the exact closing
valuation. Integrality forces w2 modulo3 automatically. In particular there
are genuine positive integer instances for **every a**, not just an
unverified extension of a binary pattern.

The old normalized return in both families is9w, and

```
9w = [3^(a+1)/2^(a+4)]*(x+1)−9/16.                   (12)
```

For every `a≥5`, it already exceeds x. Its ratio to x grows without bound
as a grows. Thus neither R26's cutoff-only normalization nor R34's inverse
chain recognizes these actual upper roots via that return. This does not
assert that the roots are outside every supplied-history closure or every
other existing bridge rule.

For a fixed cylinder `(x_a,L_a)`, all four exact R_N source rows are retained:

| Open interval | Residue | Weight |
|---|---|---|
| `(N,3N/2)` | `3 mod12` | 1 |
| `(9N/8,3N/2)` | `7 mod12` | 1 |
| `(N,9N/8)` | `7 mod36` | 2 |
| `(N,9N/8)` | `19 mod36` | 2 |

Since `x_a=3 mod4` and L_a is a power of2, CRT combines the cylinder with
each odd modulus3 or9. Each row's open-interval count is a difference of
floors. For `8|N`, its total weighted mass is exactly the implementation's
`weighted_count` and obeys

```
mass = 25N/(72 L_a)+error,        |error|≤6.            (13)
```

Indeed the four weighted leading terms are `N/(6L_a)`, `N/(8L_a)`, and
twice `N/(36L_a)`. Each individual count differs from its interval length
divided by its CRT period by at most1; the weights sum to6. This is a
**fixed-cylinder** estimate, not a global mass asymptotic after summing all
words or all a. For every fixed cylinder and either weight, arbitrarily
large cutoffs on the required ray `N=12*2^b` contain actual sources. The
constructor gives explicit witnesses using `b=log2(L_a)+4`; larger b also
work by the same interval-length and CRT bounds.

### 6. Supplied-current interface and evidence

Given any checked finite signed current H for q, the exact signed expression
`c(J_x+H)` has divergence `cδ_x`. Existing finite-graph extraction converts
it to a nonnegative absorption current without exposing any unknown orbit.
It is valid for full residual multiplicity `c=1` or `c=2`. This uses the
same finite positive-source graph lemma as R20/R23/R30, and requires no
assumption excluding nontrivial cycles elsewhere. Independent root
certificates may reuse supplied lower paths as proof inputs; the claim here
does not consume the same annular source coefficient twice.

Files and reusable entry points:

- [even_pairs.py](even_pairs.py): `joint_plan`, `joint_current`,
  `joint_cylinder`; the A/B `pair_current`; original-root `bridge`,
  `cylinder`, `actual_source`, `weighted_count`, `from_supplied_lower`.
- [check_even_pairs.py](check_even_pairs.py): read-only default verifier.
- [even_pair_audit.json](even_pair_audit.json): exact deterministic receipt.
- [branch_A_weight2_current.csv](branch_A_weight2_current.csv) and
  [branch_B_weight2_current.csv](branch_B_weight2_current.csv): complete
  nonnegative weight2 currents for actual R_N sources.

Run:

```sh
python3 experiments/residual_progress/even_pair_closure/check_even_pairs.py
```

The checker validates57 joint cylinders through depth64;8192 split-catalogue
inputs and8192 simultaneous-child failures;384 original cylinders, including
long mixed words;12 actual required-ray sources with both weights;24 exact
weighted counts; and two supplied-current conversions. Discovery of the
two supplied lower currents alone uses a10000-arrow cap. The bridge
construction itself follows only its prescribed finite arithmetic rules.
No full-cutoff absorption scan is used for these high witnesses.

### 7. What remains open

This closes two explicit d4 entry domains, with unbounded recursive depth
and equal-clock bridges to smaller half seeds. It also fully characterizes
the success set of the named **split** catalogue at d4. The joint family is
new constructive information because that catalogue provably rejects its
A inputs. It does not complete all of A, all d4, or all even d.

The general D helper still needs a construction on its noncanonical actual
inputs. The joint C recognizer retains unresolved outcomes, and no repeated
fractional reduction is asserted. The critical tripling domains identified
elsewhere in this batch are not exhausted by these entries. A complete
recursion must prove progress for all remaining states while preserving
both the current signs and a valid smaller supplied-input dependency.

## Certificates

- [`check_even_pairs_recompute.py`](check_even_pairs_recompute.py) (written at the B10 migration, under 1 s, standard library). With its own `S` and `ν` it checks, against [`even_pair_audit.json`](even_pair_audit.json): the 57 joint cylinders (depths 0–16, 32, 64), with the recursion (5), the terminal words and clock, and the divergence `[18v + 3] − [v]` of the assembled current, plus bits, clock, rows and SHA-256 of every receipt row, and that modulus 4096 loses the left terminal word (`v = 4135`); the A-entry original cylinders (11) for `a = 2, 5, 8, 32` and joint depths 1, 2, 8, 32 with their equal clocks and old returns; the six A-entry actual sources, and for the six B-entry sources the stored root's weight, `d = 4`, `w ≡ 105 (mod 256)` and clock; the twelve A-entry fixed-cylinder counts against explicit enumeration and the bound (13); and both stored weight-2 currents [`branch_A_weight2_current.csv`](branch_A_weight2_current.csv) and [`branch_B_weight2_current.csv`](branch_B_weight2_current.csv) (positive, divergence exactly `2[root]`, rows and hash). It does not rebuild the B entry, the split-catalogue success set or the 8192 paired nonacceptances, which need the R33 recognizer (legacy checker, evidence only).
- The command in the legacy text names `experiments/residual_progress/even_pair_closure/`.

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B18-replay-revival migration; standard library) replays the unmodified legacy check `check_even_pairs.py` in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, requiring exit 0 and every file unchanged (about 9 s). It checks finite steps only; the status is unchanged.

## Remarks

- **What remains.** The general `D` helper on its noncanonical actual inputs, the unresolved outcomes of the joint recognizer, and the critical tripling domain of [`critical-tripling-domain-equivalence`](../critical-tripling-domain-equivalence/README.md). The next rounds continue from here: [`critical-nine-elimination`](../critical-nine-elimination/README.md) (R40), [`decreasing-w5-phase-inverse-barrier`](../decreasing-w5-phase-inverse-barrier/README.md) (R41) and [`joint-source-unbounded-frontier`](../joint-source-unbounded-frontier/README.md) (R42), which gives the complete interface of the joint source `C(v)` and an unbounded positive frontier for the prescribed joint block.
- **Controls.** The coupled rewrite uses exact `3x+1` valuation identities; the generic merger statement it would replace fails on the control maps ([`tripling-doubling-pair-decomposition`](../tripling-doubling-pair-decomposition/README.md), Remarks).
- No novelty is claimed.

## History

- Migrated from `experiments/residual_progress/even_pair_closure/EVEN_PAIR_CLOSURE.md` (legacy ID R39) at commit `be73a66`, by the B10 migration (Claude, Opus 5.5). Note, scripts, receipt and the two stored currents moved byte-identical; `check_even_pairs_recompute.py` was added at the migration. Legacy status: "written exact identities and partial constructor, complete cylinders and stored finite currents".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `436f51f`. The batch's "independent model audits" (R37–R39) were the main lane's own agents. The side lane's finite check is recorded under `reviewed_by`.
