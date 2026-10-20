# C008 — Height-residue matching and a denominator-spectrum obstruction

**Status:** two elementary written partial theorems; the full Hall-matching
proposal is open. This note uses raw positive odd-only cycles, without
absorbing at 1. Let a primitive positive cycle have odd reduced denominator
`q` and reduced odd numerator states `n_i`, so

```
3n_i+q=2^a_i n_(i+1),  a_i>=1,
gcd(n_0,...,n_(m−1))=1.
```

Write `L=min n_i`, `h_i=floor(log_2(n_i/L))`, `B=max h_i`, and
`z_i=n_i/2^h_i`. The **ordered domain** means `q<=L`, `m>1`, and strictly
increasing `F_i=3z_i+q2^(−h_i)` in sorted `z` order. By
[C005–C006](../ordered-cycle-sparse-forcing/ORDER_RIGIDITY.md), the normalized word
`c_i=a_i+h_(i+1)−h_i` then belongs to `{1,2}`, is the lower mechanical
word with totals `(A,m)`, and satisfies `gcd(A,m)=1`. All height labels
`0,...,B` occur.

For each height `h`, define the raw and normalized unit-residue sets

```
R_h={n_i mod q : h_i=h},
Z_h={2^(−h)n_i mod q : h_i=h}.                 (1)
```

For `q=1`, take the sole residue class `0`. The **full Hall proposal** says
that both families admit distinct representatives for all levels `0,...,B`.
At `q=1`, this would force `B=0`; C004 would then exclude every
nontrivial ordered integer cycle. This sufficient mechanism is not proved.
The finite matching receipts in [C007](../../questions/height-denominator-candidate/RESIDUE_MATCHING.md) cover
only their stated cycles with `q>1`.

## 1. Exact small-band matching theorem

**Theorem (written proof).** In every ordered nonfixed cycle with `q>1`,
the normalized residue graph has a full matching when `B<=2`; the raw
residue graph has a full matching when `B<=1`.

First, every numerator is a unit modulo `q`, by the propagation argument
in [C007](../../questions/height-denominator-candidate/HEIGHT_DENOMINATOR.md). The normalized arrow gives

```
2^c_i Z_(i+1) = 3 Z_i (mod q),  c_i in {1,2}.    (2)
```

Here `Z_i` denotes one chronological normalized residue. Equal residues
at the ends of an arrow would force `q | 2^c_i−3=±1`, impossible for
`q>1`. Thus consecutive normalized residues differ. The two possible
successors `3·2^(−1)r` and `3·2^(−2)r` of the same unit `r` also differ
modulo `q`.

In fact the whole chronological normalized residue orbit has at least
**three** values. If it had exactly two, consecutive residues would
alternate, so `m` would be even. At each of the two alternating source
residues, the required successor is fixed; since its `c=1` and `c=2`
successors differ, `c_i` must be constant on each parity class. The
normalized word would have period at most two. Its `gcd(A,m)=1` then
forces `m=2`; the only mixed two-letter word has `A=3` and
`2^A−3^m=−1<0`. Constant words also contradict `gcd(A,m)=1` for
`m>1`. Hence two residues are impossible.

The minimum state lies at sorted rank zero, so its first normalized digit
is `c_0=1`. Since `h_0=0` and `a_0>=1`, the next height is also zero.
Equation (2) makes their normalized residues distinct. Therefore
`|Z_0|>=2`. If a chronological arrow rises from height `h` to `h+1`,
then `a_i=c_i−1>=1`, so `c_i=2`; its endpoint residues differ by (2).
Every adjacent pair of observed height levels has such a rising arrow,
because the cycle starts at height zero and upward steps are at most one.
Consequently `Z_h` and `Z_(h+1)` cannot both equal the same singleton.

For `B=2`, a Hall-deficient pair of levels must have a one-element
union. The pairs `{0,1}` and `{1,2}` are ruled out by the rising arrows,
and `{0,2}` by `|Z_0|>=2`. A deficient triple would have a union of at
most two residues, ruled out by the three-value result. Singletons are
nonempty. This proves normalized Hall for `B=2`; `B=0,1` follow as
subcases.

For raw residues, the minimum and its successor are both at height zero
and have distinct residues: their exact valuation is `a_0=1`, so equality
would again force `q|2−3=−1`. If `B=1`, a deficient pair would mean that
every raw numerator in both bands had the same residue; this contradicts
those two height-zero states. This proves the raw assertion. QED.

The theorem has **no** `q=1` conclusion: modulo 1 all residues coincide,
and the ±1 argument is vacuous. It does not establish the all-height
proposal even for `q>1`.

## 2. What a minimal Hall failure must look like

**Lemma (elementary).** In either residue graph, let a nonempty set of
height labels `I` be inclusion-minimal with `|N(I)|<|I|`, where `N(I)`
is its residue neighborhood. Then

```
|N(I)|=|I|−1,
```

and every residue in `N(I)` occurs in at least two of the levels in `I`.

Indeed, removing any one level leaves a Hall-satisfying proper subset,
whose neighborhood has at least `|I|−1` elements and is contained in
`N(I)`. This forces equality. If a residue belonged to only one level,
removing that level would reduce the neighborhood to at most `|I|−2`,
a contradiction. QED.

For the normalized graph, Section 1 rules out failures with `B<=2`.
The lemma does not propagate a larger deficient set to a forbidden
arrow: the ordered `q=5`, period-17 control has repeated raw residue 2
across heights 0,1,2,3, and its height-band maxima all have raw
residue 3. It nevertheless has full raw and normalized matchings.
Selecting one canonical extremal state per band therefore cannot prove
the proposal. A proof must coordinate representatives and retain the
weighted integer-cycle divisibility, not just the local residue rule.

## 3. An independent all-period denominator-spectrum theorem

The matching problem led to a separate exact restriction. It concerns
which reduced denominators can occur in the ordered domain, and does
not resolve Hall or the denominator-one case.

**Theorem (written proof).** Let `q>1` be the reduced denominator of an
ordered nonfixed cycle. Then the subgroup `<2,3>` of `(Z/qZ)^×` is
cyclic. Consequently, no such `q` is divisible by `35`, `65`, or `91`.

Because `q` divides `D=2^A−3^m` and `gcd(A,m)=1`, choose integers
`u,v` with `um+vA=1` and set `t=2^u3^v mod q`. Negative exponents
exist since `q` is coprime to 6. The relation `2^A=3^m` modulo `q`
gives

```
t^m=2^(um)3^(vm)=2^(um+vA)=2,
t^A=2^(uA)3^(vA)=3^(um+vA)=3.                 (3)
```

Thus `<2,3>=<t>`.

For explicit forbidden divisors, if `35|q`, reduction modulo 7 uses
`2=3^2` and `ord_7(3)=6`, giving `m≡2A (mod 6)`, hence `m` even.
Modulo 5 uses `3=2^3` and `ord_5(2)=4`, giving
`A≡3m (mod 4)`, hence `A` even. This contradicts `gcd(A,m)=1`.
If `65|q`, modulo 13 uses `3=2^4` and `ord_13(2)=12`, so
`A≡4m (mod 12)` and `4|A`; modulo 5 then gives `4|m`.
If `91|q`, modulo 13 again gives `4|A` and `A≡m (mod 3)`;
modulo 7 gives `m` even and `m≡−A (mod 3)`. Hence both `A,m`
are divisible by 3, again a contradiction. QED.

There is a general exact test for such forbidden factors. For any
`d>1` coprime to 6, set `n=ord_d(2)`. Let `b` be the least positive
integer with `3^b∈<2> mod d`, and choose `0<=a<n` with
`2^a=3^b mod d`. The relation lattice

```
{(A,m) in Z^2 : 2^A=3^m mod d}
  = Z(n,0) + Z(a,b).                             (4)
```

Indeed, the image of 3 in `<2,3>/<2>` has order `b`, so any relation
has `m` divisible by `b`; then its `A` is congruent to `a(m/b)` modulo
`n`. Put `e(d)=gcd(n,a,b)`. Every relation in (4) has both coordinates
divisible by `e(d)`. Therefore

```
e(d)>1  and  d|q  =>  no ordered primitive cycle.  (5)
```

Equivalently, the finite group `<2,3> mod d`, presented by (4), has
Smith invariant factors `e(d)` and `nb/e(d)`; it is cyclic exactly when
`e(d)=1`. The three controls are

| `d` | `n=ord_d(2)` | `a` | `b` | `e(d)` |
| ---: | ---: | ---: | ---: | ---: |
| 35 | 12 | 10 | 2 | 2 |
| 65 | 12 | 4 | 4 | 4 |
| 91 | 12 | 0 | 6 | 6 |

This spectrum restriction is already implied by the coprime totals
of an ordered cycle; it is not additional evidence for Hall. In
particular it gives no denominator-one exclusion and does not rule
out prime reduced denominators, whose unit groups are cyclic. Its
ordered-domain qualification matters: the exact raw `q=35` cycle
`(13,37,73,127)` has valuation word `(1,1,1,5)`, total `(A,m)=(8,4)`,
and `L=13<q`; it is outside the theorem and has the expected shared
factor in its totals.

## 4. Seven-field decision record

| Field | C008 assessment |
| --- | --- |
| Objects | Height bands of primitive positive ordered odd-only cycles, with raw or normalized unit residues modulo the reduced denominator `q`; `q=1` has the sole residue 0. |
| Structural gain | Written normalized Hall theorem for `q>1,B<=2`, raw Hall for `q>1,B<=1`, minimal-deficiency lemma, and the all-period noncyclic-modulus denominator exclusion (3)–(5). |
| Translated unresolved gap | Prove full Hall for arbitrarily many height bands, especially `q=1,B>=1`, using the global weighted intercept and integer order; local modular arrows and the two-band theorem do not do it. |
| Worked example | The ordered `q=5` period-17 cycle has four bands and a full matching despite overlapping residue sets and identical residues on all band maxima. |
| Known-cycle controls | C007's finite matching receipt covers its 1,184 `q>1` cycles, of which 51 are ordered; the `q=1` fixed point has `B=0`. No finite receipt covers hypothetical longer periods. |
| Cheapest meaningful next test | For an inclusion-minimal deficient set in any wider cycle, including a pair of nonadjacent bands, combine its repeated-residue requirement with the full rank-gap inequalities and the reduced-denominator equality `q=D/gcd(C_h,D)`; a local propagation using only (2) is insufficient. |
| Genuinely intermediate milestone | Exclude every nontrivial ordered `q=1` cycle at all periods, by Hall or another exact denominator argument. This is strictly below the full cycle goal because unordered integer cycles remain. The next `q>1` height cases are bounded diagnostics, not completion milestones. |

**Decision:** retain full Hall as an open sufficient mechanism for ordered
integer-cycle exclusion. The two partial theorems above are exact but do
not close that target. No novelty claim is made.
