---
id: native-critical-nine-continuation
kind: result
title: "Native critical-nine continuation at the original rank: complete native and next-A2 decisions"
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1, [1] = 0; P(w) = [3w] - [w], W5 = {w = 5 mod 8}, W9 = {w = 9 mod 16}, rho(w)
  = nu(3w), retained critical basis of R75 with formal plans [s] = div J_s + A_s.P. For every positive b = 905 mod
  8192 put t = (27b+13)/128, n = 3b, c = (27t-1)/4, m = 3c: the six ordinary arrows from n have valuations
  (1,2,1,1,1,2) and end at selected r = (81t-1)/2 with nu(r) = m, and the full signed plan C_b = G + N_r + L_c +
  J_c - J_b with requests l_c + A_c - A_b has every rank below the original n if and only if not (D = v2(9c-1) in
  {4,6} and 3z noncanonical); each failure keeps exactly one higher request with coefficient +1. In the D6 failure
  the k4 inverse plus the E conversion returns the request b (+1) with a possibly nonzero lower current, and the
  k8 inverse leaves the higher W9 input c. The next forward block gives the signed vector A_f + A_c - A_ell - A_b;
  on the whole next-initial-exponent A = 2 domain it is strict at the original n exactly when the next depth d is
  odd, or even d >= 6, or f is selected; other A are unclassified. The successful first-stage rows were already
  implicit in R52. Conditional on supplied currents for every signed request; no universal supply, new local orbit
  identity or dispatcher change.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [critical-nine-elimination, complementary-run-bridges, returning-second-forward-interface, selected-critical-five-forward-tables, two-selected-inverse-choices, common-critical-rank-basis]
certificates: [check_legacy_replay.py]
evidence:
  - "check_native_nine.py, native_nine.py, native_nine_audit.json: the legacy constructor, checker and receipt: 383 nonblocked local-bound cases, 226 native cases, 150 full two-ray substitutions, 134 next-A2 cells, 30 exact rational boundary checks, 13 rejections, 16 other-A cases recorded as unresolved, three supplied outputs P(905), P(517001), P(779145) with 43/97/102 rows and their 3/8/6 input tables; 36 reachable sources pinned. Fails at its new path: native_nine.py loads ../critical_basis/, ../returning_continuation/, ../selected_forward/ and ../selected_inverse/ (now ../common-critical-rank-basis/, ../returning-second-forward-interface/, ../selected-critical-five-forward-tables/, ../two-selected-inverse-choices/) by their pre-migration folder names. Passed at be73a66 as experiments/residual_progress/native_nine/check_native_nine.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
  - "../high-smaller-origin-history/batch_r78_r80_check.py: side-lane probe of R78-R80, replayed by this node's check_legacy_replay.py (see reviewed_by)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: ../high-smaller-origin-history/batch_r78_r80_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 03:31, VERIFIED, main 3b0c8a5), with the lane's own step, ν and selected: '**R78.** Take 2,000 random `b ≡ 905 (mod 8192)`. Then `t = (27b + 13)/128 ≡ 191 (mod 1728)`. From `3b` the six ordinary arrows have valuations `(1,2,1,1,1,2)` and end at `r = (81t − 1)/2`. This `r` is selected, with `ν(r) = 3c`, where `c = (27t − 1)/4 = U(b) = (729b + 223)/512`.' The signed plans and the decisions (6) and (18) were not rebuilt; reproduced by the main lane in side_lane_review_9849c53.md. The status stays written"
aliases: [R78]
tags: [convergence, outer-residual, critical-nine, critical-basis, original-rank, native-history]
---

# Native critical-nine continuation at the original rank: complete native and next-A2 decisions

## Statement

Odd-only clock, 1 absorbing, `[1] = 0`; `P(w) = [3w] − [w]`, `W5 = {w ≡ 5 mod 8}`, `W9 = {w ≡ 9 mod 16}`, `ρ(w) = ν(3w)`; `[s] = div J_s + Σ_v A_s(v)P(v)` the retained critical formal plans of [`common-critical-rank-basis`](../common-critical-rank-basis/README.md) (R75), `A_s(v) ≠ 0 ⇒ ρ(v) ≤ ν(s)`; `(L_c, l_c)` the local plan of [`critical-nine-elimination`](../critical-nine-elimination/README.md) (R40) without its recursive W9 elimination.

1. **Local bound.** For `c ∈ W9`, `M = 3c`, every request of `l_c` has `ρ(v) ≤ (27M + 23)/32`, unless `D = v2(9c − 1) = 4` and `3z` is noncanonical.
2. **Native interface.** For every positive `b ≡ 905 (mod 8192)`, with `t = (27b + 13)/128`, `n = 3b`, `c = (27t − 1)/4`, `m = 3c`, the six ordinary arrows from `n` have valuations `(1,2,1,1,1,2)` and end at selected `r = (81t − 1)/2`, `ν(r) = m`. The full plan `C_b = G + N_r + L_c + J_c − J_b`, requests `l_c + A_c − A_b`, has all ranks below the **original** `n` if and only if not (`D ∈ {4, 6}` and `3z` noncanonical). Each failure keeps exactly one higher request, coefficient `+1`. The successful rows were already implicit in R52 ([`returning-second-forward-interface`](../returning-second-forward-interface/README.md)).
3. **D6 inverse alternatives.** In the D6 failure, the k4 inverse and the E conversion give the full current `J_c − L_(c,ℓ) − J_ℓ` with requests `{b:1} + A_c − A_ℓ` (`ℓ = (Q + 2)/3`); the lower current need not vanish. The k8 inverse leaves the higher W9 input `c`. Neither is progress at the original rank.
4. **Next forward block.** It leaves the signed vector `A_f + A_c − A_ℓ − A_b`. On the whole next-initial-exponent `A = 2` domain it is strict at `n` exactly when the next depth `d` is odd, or even `d ≥ 6`, or `f` is selected; canonical `d = 2, 4` keep a genuine higher critical request. Other `A` are unclassified. At `b = 4187017` the locally accepted `d = 4` child has endpoint `12732427` above the original `n = 12561051`.

Every statement is conditional on supplied currents for all signed requests.

## Proof

The legacy note "A native-rank continuation for critical-nine inputs" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written proof, conditional finite compiler, and bounded executable
checks.** This composes existing R40/R52/R55/R56 comparisons in the retained
critical basis of R75, always against the **original** critical-nine rank.
It supplies no universal terminal currents and asserts no new local orbit
identity or novelty. Some initial successful cases were already implicit in
R52. The subsequent D6 continuation is a further original-rank composition;
its unhandled cases remain open.

Use the absorbed odd Syracuse map `S`, killed atoms `[1]=0`, and row
`div e_x=[x]-[S(x)]`. Set `P(w)=[3w]-[w]`,
`W5={w>0:w=5 mod8}`, `W9={w>0:w=9 mod16}`, and
`rho(w)=nu(3w)` on their union. The elementary current `N_s` has divergence
`[s]-[nu(s)]`. Write the retained critical formal absorption plan as

\[
 [s]=\operatorname{div}J_s+\sum_v A_s(v)P(v),
 \qquad A_s(v)\ne0\Longrightarrow\rho(v)\le\nu(s).       \tag{1}
\]

These are finite formal identities, not supplied absorption currents. Their
construction terminates by decreasing the canonical seed. All coefficients
and currents here are integers; negative requests require exact supplied
currents just as positive requests do. References are the
[critical basis](../common-critical-rank-basis/README.md),
[critical-nine local identity](../critical-nine-elimination/README.md),
[second returning block](../returning-second-forward-interface/README.md),
[selected forward interface](../selected-critical-five-forward-tables/README.md), and
[selected inverse interface](../two-selected-inverse-choices/README.md).

### 1. A bound for the retained local critical-nine plan

For `c in W9`, put `M=3c`, `D=v2(9c-1)`. Let `(L_c,l_c)` be R40's local
plan, **without** its recursive elimination of W9 requests:

\[
 \operatorname{div}L_c=P(c)-\sum_v l_c(v)P(v).
\]

For odd `D=2k+5` its normalized endpoint pair is `(3z,z)`, with
`z=3^k(9c-1)/2^D`. For even `D=2k+4` it is `(6z+1,2z+1)`, with the same
formula for `z`. If `3z` is noncanonical in the even case, the upper formal
plan starts with the unique request `4z+1` of rank `6z+1`, coefficient `+1`.
All other request ranks are at most `2z+1` or `z`.

**Lemma.** Unless `D=4` and `3z` is noncanonical, every nonzero request obeys

\[
                 \rho(v)\le {27M+23\over32}.             \tag{2}
\]

For odd D, (1) gives a maximum at most `3z`; its largest possible bound is
`(9M-3)/32` at D5. For even D with canonical `3z`, the upper endpoint
normalizes to `3z`, so the largest possible bound is `(9M-3)/16` at D4;
the lower endpoint is smaller. For even D with noncanonical `3z`, the high
rank at D6 is `(27M+23)/32`, and at D8 is `(81M+101)/128`. The difference
between these two bounds is `(27M-9)/128>0`. Increasing D by two sends this
high bound `L` to `(3L+1)/4`, which decreases it. These facts prove (2),
including all lower requests. The finite receipt includes equality cases;
no sharpness assumption is needed later.

### 2. The whole native a5 interface

Fix any positive

\[
 b\equiv905\pmod{8192},\qquad
 t={27b+13\over128}\equiv191\pmod{1728},\quad t\ge191.
\]

Define

\[
\begin{split}
 n&=3b={128t-13\over9},& u&={32t-1\over3},&q&=16t-1,\\
 r&={81t-1\over2},&m&={81t-3\over4},&c&={27t-1\over4}.
\end{split}                                                   \tag{3}
\]

Here `u` is in the returning E phase, `rho(u)=q`, `r` is selected,
`nu(r)=m=3c`, `c in W9`, and `b<c<n<m`. Conversely the returning-a5 phase
`t=83 mod108` together with selected `r` whose canonical minimum is a W9
critical root gives `t=63 mod64`; their exact CRT intersection is precisely
`t=191 mod1728`. Thus (3) describes the entire stated native subdomain.

The actual ordinary prefix from `n` to `r` has six valuations

\[
                         (1,2,1,1,1,2).                      \tag{4}
\]

The first two reach q. The last four are the existing returning-a5 prefix.
Let G be its current. Substitution of the local plan of c gives

\[
\begin{split}
 C_b&=G+N_r+L_c+J_c-J_b,\\
 a_b&=l_c+A_c-A_b,\\
 \operatorname{div}C_b&=P(b)-\sum_v a_b(v)P(v).             \tag{5}
\end{split}
\]

All requests in `A_c` and `A_b` have rank below n. The following is a
**complete decision for the full signed plan (5)**:

\[
 \text{all nonzero request ranks are below }n
 \quad\Longleftrightarrow\quad
 \neg\bigl(D\in\{4,6\}\text{ and }3z\text{ noncanonical}\bigr).  \tag{6}
\]

In either failed case there is exactly one request above n, with coefficient
`+1`; every other signed request has rank below n. It cannot cancel against
any helper. To verify (6), the only relevant boundary differences are

\[
\begin{array}{ll}
n-(9m+5)/8=(-2465t-353)/288<0,&D4\text{ noncanonical},\\
n-(27m+23)/32=(-3299t-1763)/1152<0,&D6\text{ noncanonical},\\
n-(81m+101)/128=(6487t-8105)/4608>0,&D8\text{ noncanonical},\\
n-(9m-3)/16=(1631t-481)/576>0,&D4\text{ canonical}.
\end{array}                                                   \tag{7}
\]

The odd-D bounds are smaller; later even-D bounds decrease by the recurrence
in Section1. All strict positive signs hold for t at its stated minimum191.
This proves the full-domain statement, without sampling assumptions.

#### Relation to existing successful rules

The old first R44 test fails throughout (3), since m is a W9 critical root
and `(9m+5)/8>q`; the first sigma endpoint test also fails since m>n. The
successful rows in (6), however, are already implicit in the old R52 second
block: its second initial exponent is2 and its next depth is `D-2`, with
the same upper endpoint. Its lower helpers also have rank below n. Even its
largest canonical-upper all-W5 bound obeys

\[
 n-{81m+53\over128}={6487t-6377\over4608}>0.                \tag{8}
\]

Thus this first stage is an exact native-rank interpretation and complete
interface, not newly discovered W5 dispatcher coverage. The original-parent
rank discipline is the same as R62, but R62's published low-exponent tables
concern a different restricted initial-a3 family.

#### The D4 higher-nine request

In the failed D4 case, applying R75's E conversion to its high request
leaves a unique higher W9 input

\[
                 c={729b+223\over512},\qquad\rho(c)=m>n,   \tag{9}
\]

with coefficient `+1` and every other request below n. This statement
requires both D4 and noncanonical `3z`; `b=905 mod8192` alone does not imply
those guards. `d4_return` retains the entire current and lower signed list.
No universal zero-current cancellation is asserted.

### 3. The full D6 failure and the two prescribed inverse alternatives

Retain (3) and assume D6 with noncanonical `3z`. Define

\[
 p={729t+25\over64}={19683b+12677\over8192},\qquad
 Q=\rho(p)={2187t+11\over128}={59049b+29839\over16384}.
                                                               \tag{10}
\]

Then `p=4z+1 in W5`, `3p` is selected, `Q>n`,
`p=2176 mod19683`, and

\[
 c={16p-13\over27},\quad c\equiv2\pmod3,\quad
 n={16384Q-29839\over19683}.                               \tag{11}
\]

The exact D6 residue is `b=58249 mod65536`, **together with** the required
noncanonical-upper condition, equivalently selected `3p`. The residue alone
is insufficient: b58249 has canonical upper endpoint. It implies the valid
lower bound Q>=209935, including the additional guard when imposed.

For R56's two choices the valuations are fixed throughout this domain:

\[
                  v_3(4c+1)=3,\qquad v_3(8c+1)=0.           \tag{12}
\]

Indeed `4c+1=27t` and t=2 mod3, whereas `8c+1=2 mod3`.

#### Choice k4: a full signed return to the original request

The k4 inverse endpoint is `q=16t-1`; the actual q-to-Q word is

\[
                          (1,1,1,2,1,1,4).                 \tag{13}
\]

It obeys `Q+17=(2187/2048)(q+17)`, the existing shifted negative-cycle
block. This is a historical undo mechanism, not a new local identity.
The selected bridge at r, the four-arrow q-to-r prefix and the three-arrow
m-to-Q prefix `(1,2,2)` equal the seven-arrow path (13) **row for row**.

Let I be the negative of that ordinary path, so `div I=[Q]-[q]`. The
critical-basis P(p) inverse plan is

\[
 N_{3p}+I-N_p+J_q-J_{\nu(p)},\qquad
                   A_q-A_{\nu(p)}.                        \tag{14}
\]

Its unique request above n is u from (3), with coefficient `+1`; the others
are below n. Substituting (14) into (5), and then the exact R75 E conversion
of P(u), gives the **complete** current and request vector

\[
\begin{split}
 K&=J_c-L-J_\ell,\\
 a&=\{b:1\}+A_c-A_\ell,\qquad
 \ell={Q+2\over3}={27c+29\over32},                         \tag{15}
\end{split}
\]

where L is the ordinary c-to-ell word `(2,1,2)`. Since c,ell<n, every
remaining helper is below n. The request b survives with coefficient `+1`.
It is therefore not a strict original-rank plan.

For completeness, the exact cancellation uses
`J_Q=J_p-N_(3p)`, `J_q=J_u-N_(3u)`,
`J_p=N_p+J_nu(p)`, and the actual prefix equality after (13). The source of
K is `sum_v(A_ell(v)-A_c(v))P(v)`, exactly as (15) requires after the
P(b) self-request cancels. K need not be zero: a nonzero lower identity
must not be discarded or described as a zero-current tautology.

#### Choice k8: a higher-nine request

The k8 inverse endpoint is `eta=16c+1`. Its formal critical plan begins by
reaching and normalizing to m=3c, so its request vector is
`{c:1}+A_c`. Substitution in (5) leaves c with coefficient `+1`, rank m>n,
and all other requests below n. Forcing W5 elimination of c can hide this
as a return to p; retaining the critical basis exposes the higher-nine
request directly. Neither of these two inverse choices certifies b at its
original rank. No assertion is made about every other comparison at p.

### 4. A descending next forward block, at the original rank

For the same full D6 failure, write its canonical Q as
`Q=2^A s-1`, with s odd and A>=2, and put
`d=v2(3^(A-1)s-1)>=2`. Apply the existing R26/R55 block to Q, with raw
endpoint f and current D_Q:

\[
 f=\begin{cases}
 3^{\lfloor d/2\rfloor}(3^{A-1}s-1)/2^d,&d\text{ odd},\\
 2\,3^{d/2}(3^{A-1}s-1)/2^d+1,&d\text{ even},
 \end{cases}
 \qquad \operatorname{div}D_Q=[Q]-[f].                    \tag{16}
\]

The retained critical-basis P(p) plan is
`N_(3p)+D_Q+J_f-J_p`, with request vector `A_f-A_p`.
Substituting into (5) and canceling exact rows yields

\[
\begin{split}
 C&=G_9+D_Q+J_f-L+J_c-J_\ell-J_b,\\
 a&=A_f+A_c-A_\ell-A_b,\\
 \operatorname{div}C&=P(b)-\sum_v a(v)P(v),                \tag{17}
\end{split}
\]

where `G_9` is the actual n-to-Q prefix with word
`(1,2,1,1,1,2,1,1,4)`, and L,ell are as in (15). All helpers outside A_f
have rank strictly below n. Formula (17) is valid for every A>=2; no
acceptance is inferred for unclassified A.

**Complete A2 theorem.** On the entire subdomain A=2, the full signed
plan (17) has only ranks below the original n **if and only if**

\[
           d\text{ is odd},\quad\text{or even }d\ge6,
           \quad\text{or }f\text{ is selected}.          \tag{18}
\]

In particular the failed rows are exactly d2/d4 with canonical f. The old
R55 local test at p accepts d4 canonical, but that local acceptance cannot
be substituted as original-rank progress here.

**Proof.** For odd d, the largest raw endpoint is `(9Q-3)/32` at d3.
For even d, f=1 mod3 and f=3 mod4. If selected, its canonical minimum is
`(f-1)/2`, whose worst value is `(9Q-3)/16` at d2. If not selected, f is
canonical, with values `(9Q+5)/8`, `(27Q+23)/32`, `(81Q+101)/128` at
d2,d4,d6. Increasing d by two multiplies f, or f-1 respectively, by3/4.
The exact boundary differences are

\[
\begin{array}{ll}
n-(9Q-3)/32=(347141Q-895799)/629856>0,&\text{odd worst},\\
n-(9Q-3)/16=(84997Q-418375)/314928>0,&\text{selected worst},\\
n-(9Q+5)/8=(-46075Q-337127)/157464<0,&d2\text{ canonical},\\
n-(27Q+23)/32=(-7153Q-1407557)/629856<0,&d4\text{ canonical},\\
n-(81Q+101)/128=(502829Q-5807375)/2519424>0,&d6\text{ canonical}.
\end{array}                                                   \tag{19}
\]

All displayed positive signs hold at Q>=209935. In the two failing rows,
f is not merely a raw large endpoint: being canonical, 3mod4 and1mod3,
it is a critical root with first input `v=(2f+1)/3 in W5`. That input has
rank exactly f and coefficient `+1`; all later H_f requests have smaller
rank. Every other term in (17) is below n<f, so it cannot cancel this
request. This proves necessity as well as sufficiency in (18).

The ordinary merger clocks of the **upper comparison** n-to-f are

\[
 \bigl(9+A+\lfloor d/2\rfloor,1\bigr)\ (d\text{ odd}),
 \qquad\bigl(9+A+d/2-1,0\bigr)\ (d\text{ even}).          \tag{20}
\]

For A2 these are `(floor(d/2)+11,1)` and `(d/2+10,0)`. They do not measure
the entire pair current: L and the formal normalizers/absorption currents
in (17) remain explicit with their own rows.

### 5. Exact parameter families, conditional compilation, and evidence

For any integer D>=4, solve

\[
 t\equiv2\pmod{27},\qquad
 t\equiv(13+2^{D+2})243^{-1}\pmod{2^{D+3}}.                \tag{21}
\]

Take the least t>=191, then add arbitrary nonnegative multiples of
`27*2^(D+3)`. Formula (3) gives every corresponding native cell of exact
local depth D, with b-period `2^(D+10)`. The extra binary bit ensures exact
valuation. Canonicality remains a separate tested arithmetic guard.

For any next depth d>=2, the complete next-A2 CRT cell is

\[
 Q\equiv32788\pmod{59049},\qquad
 Q\equiv(1+2^{d+2})3^{-1}\pmod{2^{d+3}}.                  \tag{22}
\]

Take its least Q>=209935 and add arbitrary nonnegative multiples of
`59049*2^(d+3)`. Then set `t=(128Q-11)/2187` and `b=(128t-13)/27`.
These are positive integers in the D6 failed domain, Q is a canonical A2
climber, and its next depth is exactly d. The binary condition gives
Q3mod4, s odd with the complementary phase; the ternary condition gives
(10) and t191mod1728. It also forces selected3p, so no canonicality guard
is lost in (22). The resulting b-period is `2^(d+17)`. Every d has a
nonempty infinite cell; (18) applies to all of it, retaining its selected
versus canonical distinction where necessary.

`native_nine.py` constructs (5), (9), (15), both inverse alternatives, and
(17), keeping every signed request. `one_step` accepts only the proved
(6)/(18) domains. Other A values retain their formal interface but are
marked unresolved even if an individual computed list happens to pass.
`compile_plan` checks exact boundaries, strict original rank, and every
supplied terminal current. Missing, incorrect, boolean-valued, self- or
higher-request plans are rejected. This conditional compiler is not a
universal input supplier and is not registered in the frozen W5 dispatcher.

Reproduce the focused finite audit from the repository root:

```text
python3 experiments/residual_progress/native_nine/check_native_nine.py
```

The receipt `native_nine_audit.json` stores dependency hashes, complete input
and output current tables for three supplied demonstrations, and hashes of
larger finite case lists. The checker independently reconstructs Syracuse
divergence, validates full coefficient vectors and original-rank tests,
checks row-for-row inverse cancellation and ordinary merger clocks, tests
exact CRT periods including depths256, and rejects missing or invalid
premises. Its capped fixture-only absorption searches use at most10,000
arrows and4,096 bits; these finite searches are not used in any infinite
proof above. The proof makes no universal supply or convergence claim.

The stored finite receipt passes383 nonblocked local-bound cases,226 native
cases,150 full two-ray substitutions,134 complete next-A2 cells,30 exact
rational boundary checks, and13 general rejection checks. It records16
other-A cases as unresolved. Its three fully supplied outputs are P(905),
P(517001), and P(779145), with43,97,102 nonzero rows respectively; the
complete3,8,6 terminal-input tables are retained. The reachable-module hash
set contains36 source files. These counts describe the finite evidence,
not the scope of the written universal parameter statements.

A concrete local/original-rank distinction is retained: at b4187017, the
higher input is p10060189 with local rank15090283. Its next A2/d4 canonical
endpoint12732427 is below that local rank but above the original
n12561051. The old local R55 plan accepts p; the original-rank compiler
correctly rejects this substitution for b.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B13 migration; standard library). The legacy scripts load sibling modules by their pre-migration paths, so they no longer run here. This certificate calls `tools/legacy_replay.py`, which rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, runs the unmodified legacy scripts there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied file unchanged. It writes nothing in the repository. It replays: the legacy checker `check_native_nine.py` (about 20 s; the counts above, compared with `native_nine_audit.json`) and the side-lane probe `batch_r78_r80_check.py` from [`high-smaller-origin-history`](../high-smaller-origin-history/README.md) (under 1 s, receipt reproduced byte for byte). The commands in the legacy text name `experiments/residual_progress/native_nine/`.

## Remarks

- The supplement on the immediate self-loop of R75 is [`immediate-self-loop-lower-relations`](../immediate-self-loop-lower-relations/README.md) (R78-b); the guarded growth of the native interface and its exits are [`native-growth-original-rank-exit-obstruction`](../native-growth-original-rank-exit-obstruction/README.md) (R79).
- The W5 dispatcher [`seventeen-family-rho-dispatcher`](../seventeen-family-rho-dispatcher/README.md) is unchanged; `one_step` accepts only the proved domains (6) and (18).
- No novelty is claimed.

## History

- Migrated from `experiments/residual_progress/native_nine/NATIVE_NINE_CONTINUATION.md` (legacy ID R78) at commit `be73a66`, by the B13 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; the note became this README, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Legacy status: "written conditional composition theorem and complete decisions on the stated domains; universal supply remains open".
- Main lane (ChatGPT, Codex), 2026-10-18, first committed in `3b0c8a5`. The batch's "independent" proof, source and default-replay reviews recorded in archive/convergence-residual-progress/REPORT.md were the main lane's own agents, not a different lane.
