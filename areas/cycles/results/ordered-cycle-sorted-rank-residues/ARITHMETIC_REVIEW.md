# C008 independent arithmetic review

**Status: PASS for the stated partial theorems and exact controls.** The
all-height Hall proposal and the exclusion of ordered denominator-one
cycles remain open. This review independently inspected
[MATCHING_ARITHMETIC.md](MATCHING_ARITHMETIC.md) (SHA-256
`aefff8c4a83e236c341ecbd2c37e7b6d7cb41d2aa87c3459a44f9d722a2a53ad`),
[INDEPENDENT_MATCHING.md](INDEPENDENT_MATCHING.md) (SHA-256
`21b37af7f124364e57b041a18cd8b96fec818a14a55451e7528d74aff1c3931e`),
and the saved C008 arithmetic checker. The review uses positive raw
odd-only cycles with exact valuations, no absorber at 1, and reduced
numerator coordinates.

## 1. Proof audit

The main note's small-band Hall proof is sound. For `q>1`, a normalized
arrow with `c∈{1,2}` cannot preserve a unit residue, because
`2^c−3=−1` or `1`. If only two normalized residues occurred, they would
alternate; the two different digit multipliers cannot leave the same
source residue with the same successor. Hence `c` would be period two,
contradicting `gcd(A,m)=1` unless `m=2`, whose mixed word has
`2^3−3^2<0`. The rank-zero minimum has a `c=1` arrow within height
zero, giving two distinct residues there. Every adjacent height pair
has an upward arrow and cannot consist of the same singleton residue.
The resulting Hall check for `B<=2` is complete; the raw `B<=1`
argument uses the same exact minimum arrow. Every step requires
`q>1`; none silently transfers to `q=1`.

The minimal Hall-deficiency lemma also checks: inclusion minimality
forces `|N(I)|=|I|−1` and every neighbor to occur in at least two levels
of `I`. The final roadmap correctly retains deficient *pairs of
nonadjacent bands* when `B>=3`.

The denominator-spectrum theorem checks algebraically. From
`2^A=3^m mod q` and `gcd(A,m)=1`, Bezout coefficients `um+vA=1`
give `t=2^u3^v`, with `t^m=2` and `t^A=3`; thus `<2,3> mod q` is
cyclic. For any divisor `d|q`, the relation lattice has basis
`(ord_d2,0),(a,b)`, where `b` is the order of the image of 3 modulo
`<2>` and `2^a=3^b`. Its first Smith factor is
`e(d)=gcd(ord_d2,a,b)`. If `e(d)>1`, every relation has both totals
divisible by `e(d)`, contradicting coprimality. The explicit entries
for `d=35,65,91` are respectively `(12,10,2,2)`, `(12,4,4,4)`, and
`(12,0,6,6)`. The direct congruence proofs in the note agree with this
lattice computation. The q35 cycle `(13,37,73,127)` is correctly
outside the ordered `q<=L` domain.

The sorted-rank proof in the independent note is also sound and adds
an exact structural formula. Starting at rank zero, the normalized
phase `i` has residue `L3^i2^(−P_i)=Lt^(Ai−mP_i)`. Mechanicality and
the rank shift give `Ai−mP_i≡is` modulo `m`, exactly its sorted rank.
Thus `z_[j]≡Lt^j` and the raw residue is
`n_[j]≡Lt^(j+mH_j)` modulo any `Q>1` dividing `q`. The first `m`
normalized ranks therefore have exactly `min(m,ord_Q(t))` distinct
residues. This proves the note's rank-collision description; it does
not prescribe which ranks belong to a height band. For `Q>1`, the
order of `t` cannot be 1, 2, or 3, because each would make `Q` divide
`gcd(2^T−1,3^T−1)=1`. Its separate geometric proof of normalized
Hall through `B=2` and raw Hall through `B=1` is valid. The `Q=1`
case is explicitly excluded from those arguments.

## 2. Exact controls and replay

I independently reconstructed both period-17 proper-divisor controls
from their displayed valuation words. The raw arrows close with exact
valuations, `D=q=5,077,565`, primitive numerator gcd 1, and ordered
normalized images. At `L=446400719,B=3`, reduction modulo the *proper*
divisor 5 gives normalized Hall deficit `{1,3}→{4}` and raw deficit
`{1,2,3}→{2,3}`. At `L=365289811,B=2`, all three raw height sets
reduce to `{1,4}` modulo 5, while normalized matching survives.
The displayed full-`q` raw and normalized matching certificates were
checked independently for membership and distinctness. Thus these
controls refute primewise/proper-divisor matching, **not** matching at
the actual reduced denominator.

I also replayed [check_residue_spectrum.py](check_residue_spectrum.py)
without writing files. It returned PASS for 332 moduli through 1000,
477,552 finite relation cells, 1,185 distinct normalized cycles, and
51 ordered nonfixed cycles. Its independent relation-grid tests and
all sorted-residue equalities passed. The 28,830 `q>1` states include
seven fixed-point states; the separate nonfixed count is 28,823.
These counts corroborate exact statements on the declared finite
inputs; they are not evidence of universal Hall or `q=1` exclusion.

## 3. Scope conclusion

The established gain is a small-band Hall theorem plus an all-period
denominator-spectrum exclusion for moduli whose `<2,3>` subgroup is
noncyclic. The sorted-rank progression identifies residue collisions
exactly, while the proper-divisor controls show why reduced-denominator
matching cannot be checked prime by prime. No argument here excludes
a hypothetical wide ordered integer cycle. A future full Hall proof
must use additional global information linking height placement to
`q=D/gcd(C_h,D)`; the finite receipts and cyclicity alone do not supply it.
