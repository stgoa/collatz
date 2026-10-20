# C008 independent arithmetic review: sorted residues and height matching

**Status:** exact elementary theorem and exact proper-divisor obstructions. The
full matching proposal modulo the *reduced* denominator remains open, in
particular at denominator one. This note uses primitive positive odd numerator
cycles for the raw map, without an absorber at 1. It independently reviews
[MATCHING_ARITHMETIC.md](MATCHING_ARITHMETIC.md); no novelty is asserted.

Let `3n_i+q=2^{a_i}n_(i+1)`, with `a_i>=1`, reduced odd `q` coprime to 6,
`gcd_i n_i=1`, `L=min_i n_i`, and `h_i=floor(log_2(n_i/L))`. Put
`z_i=n_i/2^{h_i}`, `B=max h_i`. In the ordered `q<=L`, `m>1` domain, let
the normalized successor shift sorted ranks by `s` modulo `m`. Then
`gcd(s,m)=1`, `A=m+s`, `D=2^A-3^m>0`, and the chronological normalized
valuation word is `c_i=a_i+h_(i+1)-h_i` with mechanical prefix sum
`P_i=floor(iA/m)`. All residue calculations below are in `Z/QZ` for a
divisor `Q>1` of `q`; `2,3,L` are units modulo `Q`.

## 1. Geometric residues in sorted rank

**Theorem (written proof).** Choose integers `u,v` with `um+vA=1`, and set

```text
t = 2^u 3^v (mod Q).
```

Then `t^m=2` and `t^A=3` modulo `Q`. If rank `j=0` is the minimum `L`,
the complete sorted normalized residue sequence is

```text
z_[j] = L t^j (mod Q),                  0<=j<m.             (R1)
```

In particular, with `T=ord_Q(t)`, two normalized residues at sorted
rank distance `d` agree exactly when `T|d`. The normalized Hall problem
is a matching between height levels and the occupied rank classes modulo
`T`. The raw residue at sorted rank `j`, whose height is `H_j`, is
`L 2^{H_j}t^j` modulo `Q`; it does not have a height-free geometric
progression.

**Proof.** Since `Q|D`, `2^A=3^m (mod Q)`. Thus
`t^m=2^{um}3^{vm}=2^{um+vA}=2`, and similarly `t^A=3`. The normalized
arrow gives `z_i=L 3^i2^{-P_i} (mod Q)` from the phase starting at `L`.
Substitute `3=t^A`, `2=t^m` to get
`z_i=L t^{Ai-mP_i}`. Mechanicality gives
`Ai-mP_i = Ai-m floor(iA/m) = is mod m`, the actual sorted rank of
phase `i`. Primitivity makes these ranks a permutation. This proves
(R1). All multipliers are units, so equality is equivalent to `t^d=1`.
QED.

The existence of `t` and cyclicity `<2,3>=<t>` require only `Q|D` and
`gcd(A,m)=1`; in particular
`T=lcm(ord_Q(2),ord_Q(3))` depends only on `Q`, not on the cycle.
**Order adds the placement** `z_[j]=Lt^j` in sorted rank.
Consequently the cyclic-subgroup obstruction in the main C008 note is an
algebraic consequence of coprime totals, not extra evidence for Hall.
The low orders `T=1,2,3` are impossible for `Q>1`: each would make
`Q` divide `gcd(2^T-1,3^T-1)=1`. Thus `T>=4`. For the known ordered
`q=5`, period-17 example, `s=10`, `A=27`, `t=2 (mod 5)`, and the
sorted normalized residues repeat every four ranks.

## 2. An all-period small-band result and its limit

**Corollary (written proof).** For any `Q>1` dividing the reduced
denominator of an ordered primitive cycle, the normalized height-residue
sets have a system of distinct representatives whenever `B<=2`. The raw
sets have one whenever `B<=1`.

For the normalized assertion, `B=0` is immediate. The minimum at rank
zero has height zero and `c=1`. Since `a>=1`, its successor at rank `s`
also has height zero. Their normalized residues differ: the arrow is
`2z_s=3L+q`, so modulo `Q` the difference is `L/2`, a unit. Thus height
zero has at least two colors. An upward chronological edge
`h -> h+1` must have `c=2`, `a=1`; its normalized endpoint residues
are distinct because equality would imply `Q|(3-4)`. Every adjacent
pair of levels has such an edge, since the cycle starts at height zero
and rises by at most one per arrow. When `B=2`, `m>=4` (the first arrow
stays in height zero and levels one and two also occur). By (R1) and
`T>=4`, the first four sorted ranks have four distinct normalized
colors. Hall's condition follows: height zero already has two colors,
levels one and two cannot share the same singleton color, and the union
of all three levels has at least four colors. The same argument covers
`B=1`. For raw residues at `B=1`, the two height-zero states are also
distinct modulo `Q`, since their first arrow has `a=1`; that alone
gives Hall for two nonempty levels. QED.

The main [C008 note](MATCHING_ARITHMETIC.md) proves these claims by a
separate chronological two-color argument. Its Hall and cyclicity
proofs, including the explicit forbidden factors `35,65,91` and the
relation lattice, check out under their stated hypotheses. The rank
formula (R1) makes the order-specific content and the three-color
lower bound more explicit. Neither proof applies at `Q=1`: the residue
ring then has one class, and full matching would force `B=0`.

**Retracted scoped trial:** raw matching through `B=2` does *not* follow
for every divisor `Q` of the reduced denominator. The exact ordered
cycle below has `B=2` and a raw Hall failure modulo a proper divisor.
This does not refute the full-reduced-denominator proposal.

## 3. Exact proper-divisor obstructions

The following two cycles use the same `m=17`, `A=27`,
`D=q=2^27-3^17=5,077,565`, and sorted shift `s=10`. In each, the
displayed `L=C_h` is coprime to `D`, so `q=D` is the **reduced**
denominator, not just a chosen parameter. All arrows and height labels
are exact; the sorted normalized coordinates are strictly increasing.
In both, `q<=L`. The offending modulus is the proper divisor `Q=5`.

### Four heights: both projected variants fail

```text
L = 446400719, B = 3
a = (1,2,1,2,1,2,2,1,2,1,1,1,1,1,4,2,2)
h = (0,0,0,0,0,0,0,0,0,0,0,1,2,2,3,0,0)
sorted H = (0,2,0,0,3,0,0,0,1,0,0,2,0,0,0,0,0)
n = (446400719,672139861,505374287,760600213,571719551,
     860118109,646357973,486037871,731595589,549966083,
     827487907,1243770643,1868194747,2804830903,4209785137,
     789652061,593508437)
```

Here `gcd(L,D)=gcd_i n_i=1`, `max z=860118109<2L=892801438`,
and the minimum of the 17 cyclic adjacent normalized gaps multiplied
by `2^B=8` is `151913474>0`. Modulo 5 the height neighborhoods are

```text
            h=0       h=1    h=2      h=3
normalized  {1,2,3,4} {4}    {2,3}    {4}
raw         {1,2,3,4} {3}    {2,3}    {2}
```

Normalized levels `{1,3}` have only neighbor `{4}`; raw levels
`{1,2,3}` have only neighbors `{2,3}`. Both have Hall deficit one.
This is sharper than mere shortage of units, because four levels have
four available units modulo 5. Modulo the actual reduced denominator
`q`, the first 17 normalized rank residues are distinct. Separate
full-`q` matching certificates, listed in height order `0,1,2,3`, are
`(426229,4961174,1182098,60469)` for normalized residues and
`(426229,4844783,2015023,483752)` for raw residues.

### Three heights: projected raw matching already fails

```text
L = 365289811, B = 2
a = (1,1,1,3,1,1,1,3,1,1,1,3,1,3,1,1,3)
h = (0,0,1,1,0,0,1,2,0,1,1,2,1,1,0,0,1)
sorted H = (0,1,2,1,0,1,0,1,2,1,0,1,0,1,0,1,0)
n = (365289811,550473499,828249031,1244912329,467476819,
     703754011,1058169799,1589793481,596807251,897749659,
     1349163271,2026283689,760491079,1143275401,429362971,
     646583239,972413641)
```

Again `gcd(L,D)=gcd_i n_i=1`; `max z=703754011<2L=730579622`,
and the minimum cyclic adjacent gap multiplied by `2^B=4` is
`59822914>0`. Modulo 5, all three raw height neighborhoods are
`{1,4}`, so `{0,1,2}` is Hall deficient. The normalized neighborhoods
still match, as the corollary requires. Modulo the actual reduced
denominator `q`, matching certificates in height order are
`(340839,605936,335254)` for raw and `(340839,302968,128909)` for
normalized residues.

These examples prove a precise obstruction: **a matching theorem modulo
every prime or proper divisor of `q` is false, even for exact ordered
primitive integer cycles.** A proof of full-`q` matching cannot glue
arbitrary local matchings or rely on local order and height legality
alone; it must retain the full reduced denominator, including the
weighted intercept cancellation. They leave the full-`q` proposal and
the `q=1` case open.

## 4. Scope and next test

The sorted-rank geometric law is a useful language: it converts
normalized residue collisions into congruent rank positions, with
period `T=ord_q(t)`. A full Hall proof still requires a global
restriction on which heights can occupy those positions when
`q=D/gcd(C_h,D)`. Bounded diagnostics could test full normalized Hall
at `B=3` or full raw Hall at `B=2`, always modulo the *reduced* `q` and
at every period. Neither would settle `q=1`; the principal next goal
remains all-period exclusion of nontrivial ordered `q=1` cycles. The
exact proper-divisor controls above rule out a tempting but
insufficient primewise route to that goal.
