# R53: carry expanding forward blocks before requesting absorption

**Status: written conditional construction, complete low-phase table, and
finite certificates.** All ranks here are the original R43 rank
ρ(w)=ν(3w), not the alternative rank in R51. The new infinite families
are outside all seven earlier direct rule domains. They do not cover all
remaining W5 inputs or prove Collatz.

Use killed odd atoms [1]=0, P(w)=[3w]−[w], elementary bridge N_x with
divergence [x]−[ν(x)], and ordinary Syracuse S absorbed at1. The canonical
quotient is T=νS. Dependencies: [R26 complete blocks](../complementary_bridge/RUN_BLOCK_BRIDGES.md),
[R43 rank](../critical_rank/CRITICAL_IMAGE_RANK.md),
[R48 first forward block](../nonselected_forward/NONSELECTED_FORWARD.md), and
[R47 inverse multiples](../nonselected_multiples/NONSELECTED_MULTIPLES.md).

## 1. Compose before requesting H

Let w∈W5 with3w nonselected and q=3w. An R26 block at a complementary
canonical x=2^a t−1 has parameters

    d=v2(3^(a−1)t−1)>=2, u=(3^(a−1)t−1)/2^d, b=floor(d/2),
    f=3^b u (d odd), or 2·3^b u+1 (d even).

Its explicit current D_x has boundary [x]−[f], and
T^(a+b−1)(x)=ν(f). Ordinary two-clock lengths are (a+b,1) when d is
odd and (a+b−1,0) when d is even. Adding its normalizer N_f changes the
endpoint from f to ν(f): div(D_x+N_f)=[x]−[ν(f)]. The ordinary prefixes
inside N_f are retained; their clocks are not quotient clocks.

For any finite prescribed sequence of such blocks, add all block currents
and intervening normalizers. If the last raw endpoint is y, the sum D has
boundary [q]−[y]. There is no H request at an intermediate endpoint.
The single final conditional plan is

    J=D−N_w+H_y−H_z, z=ν(w)<w/4,                       (1)
    div J=P(w)−Σ_v (A_y(v)−A_z(v))P(v),

where H is the deterministic R43 formal absorption plan. Every signed
coefficient remains explicit. The lower requests have rank below q.
Let B(ν(y)) be R44/R48's endpoint bound on all upper ranks. Whenever
B(ν(y))<q, (1) is a strict-rank rule. Supplied exact currents for the
remaining inputs give the requested P(w) current. No intermediate state
has been assumed absorbed, and no universal termination is inferred from
allowing an arbitrary finite number of blocks.

## 2. Complete two-block table after a failed low first block

Take the entire R48 domain with first exponent a=3 or4, assume its first
endpoint test fails, and assume its canonical endpoint n has first
exponent2. Apply one more complete R26 block at n. These assumptions
exhaust exactly the eight first rows below. The flag p says whether the
first raw endpoint is selected. Write e for the second block's d,
y for its raw endpoint, m=ν(y), and E for “y selected”.

All **odd e** succeed. For even e the exact endpoint-bound classification is:

| First (a,d,p) | n in terms of original q | Acceptance for even e |
|---|---|---|
| (3,2,0) | (27q+19)/16 | e>=8, or E and [e>=4 or m≠3mod8] |
| (3,4,0) | (81q+73)/64 | e>=6 or E |
| (4,2,0) | (81q+65)/32 | e>=10, or E and [e>=6 or (e4 and m1mod8)] |
| (4,2,1) | (81q+33)/64 | e>=6 or E |
| (4,4,0) | (243q+227)/128 | e>=8, or E and [e>=4 or m1mod8] |
| (4,4,1) | (243q+99)/256 | e>=4 or E |
| (4,6,0) | (729q+809)/512 | e>=6 or E |
| (4,8,0) | (2187q+2939)/2048 | e>=4 or E |

This is an iff for the stated endpoint-bound test, not for current existence.
It includes complete domains with unbounded second depth e.

**Proof.** R48's complete first table leaves precisely these rows when its
canonical endpoint has exponent2. Direct substitution gives the displayed
affine n. Its second raw endpoint is

    y=3^b(3n−1)/2^(e+2)                 (e odd),
    y=3^b(3n−1)/2^(e+1)+1               (e even).       (2)

For odd e the largest generic bound (9y+5)/8 occurs at e3 and equals
(81n+133)/256. Substituting each displayed n makes it strictly below q
for all q>=39 in the a3 rows and q>=111 in the a4 rows. These are the
minimum q permitted by the initial complementary and ternary conditions.
Larger odd e replace y by3y/4 and preserve the strict inequality.

For even e, y is1mod3 and3mod4. If nonselected, m=y and B(m)=y.
If selected, m=(y−1)/2 is canonical and divisible by3. Its three possible
residues give the exact bounds

    B=(27m+29)/32 if m1mod8,
    B=(9m+5)/8   if m3mod8,
    B=m         if m7mod8.                              (3)

Substitute (2) and the displayed n in q−B. At each even e in{2,4,6,8,10},
the sign of its slope and its value at q39 or111 agree strictly. Thus no
positive endpoint exception occurs. The passing cases are exactly the
table; when e increases by2, y−1 and m are multiplied by3/4. All four
bounds therefore decrease, so checking through10 exhausts all even e.
These are finite rational algebra comparisons, not an interpolation of
sample integers. The checker independently verifies this complete finite
algebra table in addition to actual integer paths.

Every accepted row uses (1) with two complete blocks. The exact quotient
length is a+floor(d/2)−1+1+floor(e/2). Each block's ordinary clocks remain
those in Section1; an intervening selected normalizer is a signed bridge,
not a claim of zero ordinary elapsed time.

## 3. A complete recurring low-block interface

The whole (a,d)=(2,2) domain is exactly x27mod32. Its raw endpoint is

    G(x)=(9x+5)/8,    G(x)+5=9(x+5)/8.                 (4)

Let E=v2(x+5)>=5. The maximal number of consecutive raw (2,2) blocks is

    r=floor((E−2)/3),
    G^r(x)=9^r(x+5)/8^r−5.                             (5)

Indeed at step j the exponent v2(G^j(x)+5)=E−3j; the exact (2,2)
condition holds iff that exponent is at least5. The remainder E−3r is
one of2,3,4, giving a complete exit interface:

| Remainder | Raw exit |
|---|---|
|2|7mod8; apply its ordinary elementary normalization |
|3|selected3mod16; its minimum is1mod8 |
|4|canonical11mod32, with a2 and next d>=3 |

All r blocks use the ordinary word (1,2)^r, with exact quotient length2r
after normalizing the last endpoint. The finite inverse-free formula (5)
does not make these blocks contract: each grows, and r is unbounded.
It gives a complete arithmetic stopping rule for this repeated pattern,
not for an arbitrary succession of different patterns.

## 4. Arbitrarily long expanding prefixes followed by a decreasing exit

The remainder4 row gives a useful entire parameterized comparison. For
r>=1 and positive odd s satisfying 2^(3r+8)s=11mod9, define

    w=(2^(3r+8)s−11)/9, q=3w,
    x0=9·2^(3r+4)s−5,
    xr=16·9^(r+1)s−5.                                  (6)

Every such w is13mod32. Its first block is exactly (a,d)=(3,2), and its
raw canonical endpoint is x0. It then takes exactly r successive (2,2)
blocks to xr. The complete ordinary prefix is (1,1,2),(1,2)^r, of length
3+2r; it is also a canonical quotient prefix. All these block boundaries
are canonical. Its first R48 test fails, since x0>q and x0=1mod3.
Likewise every later raw boundary is1mod3 and exceeds q. The final ratio
xr/q grows asymptotically like (27/16)(9/8)^r as r grows (the harmless
additive constants are explicit in(6)). Thus preserving these intermediate
comparisons is essential; none can be prematurely discharged by its
direct H endpoint bound.

At xr the next block has a2 and

    d=2+v2(3^(2r+3)s−1)>=3.                            (7)

For odd d, put b=floor(d/2). The final raw endpoint is

    y=3^b(3^(2r+3)s−1)/2^(d−2).                        (8)

Its generic sufficient comparison (9y+5)/8<q is exactly

    [2^(3r+d+9)−3^(2r+b+6)]s
        >103·2^(d−2)−3^(b+3).                          (9)

This retains every offset. A sufficient condition uniform over all s>=1 is

    2^(d−2)[2^(3r+11)−103]
        >3^(b+3)[3^(2r+3)−1].                         (10)

The right side in(9) is positive for odd d>=3 (it is125 at d3 and the
positive power of two grows faster thereafter). Thus(10) makes the slope
in(9) positive and proves (9) already at s1. For every
r>=1, the explicit choice **d=4r+3** satisfies(10). Indeed its left side
exceeds 2^(7r+11), while its right side is below3^(4r+7); and
2^(7r+11)>3^(4r+7) follows at r1 from262144>177147 and improves by128/81
per unit r. Larger odd d preserve(10), multiplying the two sides by4
and3 respectively.

The current in(1), for these three pieces, therefore has only requests
of rank below the **original q**. Its ordinary coalescence clocks, relative
to the raw y, are

    (2r+b+5, 1);                                       (11)

its exact quotient length to ν(y) is2r+b+4. Elementary normalization of y
inside H_y retains its own explicit signed prefixes. When d=4r+3 the
ordinary clocks are(4r+6,1). No unknown future has been exposed in deriving
these currents or clocks.

## 5. Whole new cylinders, outside all earlier seven direct rules

Fix r>=1 and any odd d satisfying(10). Impose the coprime congruences

    s=3^(−2r−3)(1+2^(d−2)) mod2^(d−1),
    2^(3r+8)s=416 mod729.                              (12)

They give one complete positive progression modulo729·2^(d−1). The
first congruence fixes the exact valuation in(7), including its extra bit;
it also makes s odd. The second gives both integrality of(6) and
w45mod81. The resulting w period is81·2^(3r+d+7). All positive members
are covered, not merely the first representatives.

Each such w is excluded by every earlier seven-rule direct recognizer:
R41/R44/R46 require selected3w; R45/R50 require3∤w; and R48 fails at the
first (3,2) block. For R47, w45mod81 means D2 and unit u5mod9, so the
active k4 branch has j=v3(64u+1)=1 and fails its exact slope test; its
other branch has j0. Thus(12) gives infinitely many new inputs at each r,
with no fixed bound on the exposed prefix length or its intermediate
height ratio. This is a direct-domain statement: it does not assert that
no earlier supplied graph or recursively composed certificate covered a
particular member.

## 6. Executable interface, evidence, and limits

`forward_continuation.py` supplies `two_plan`, the complete `low_first_table`,
`low_run`, `delayed_plan`, `delayed_family`, and `accepted_plan` for the old
ρ compiler. The ordinary w-based aliases `one_step(w)` and `recognized(w)`
need no explicit family parameters. The finite recognizer prioritizes the delayed arithmetic stratum,
then the complete low-first table. Unaccepted conditions return no rule;
they do not discard a missing source or assume an unavailable current.

Run `python3 experiments/residual_progress/forward_continuation/check_forward_continuation.py`.
The receipt records exact algebra comparisons, actual two-clock checks,
bounded whole-domain table decisions, all three low-run exit phases,
large exact CRT families, direct-domain exclusions, and supplied finite
input substitutions. The example input searches have explicit caps and
are used only to produce replayable finite fixtures. Full proofs are the
equations and tables above, not the bounded sample counts.

The stored receipt checks570 complete two-block cases among8192 W5
candidates below65536,224 maximal low runs covering all three exit
remainders, and56 exact CRT-family members, including r32 and64.
Three finite constructions are checked: w141 closes with no missing
inputs, w365 uses two supplied inputs, and w4258701 uses six. The latter
input currents, local current, and completed current table are stored.

The progress is a complete finite phase table and an unbounded-length
arithmetic family that crosses intermediate growth. It is still partial.
No closure theorem for arbitrary macro words, universal decrease, Collatz
proof, novelty claim, or human/formal verification is supplied.
