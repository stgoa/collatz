# Delay the original-rank test until exact signed expansion

**Status: written finite-composition theorem and two complete arithmetic
domains, with conditional integer-current constructors.** The fixed twelve
old-rank families may resolve a larger intermediate request before the
original rank is tested. This does not prove that every resulting frontier
is decreasing, or supply the remaining pair currents. No sigma rule is used.

Use absorbed odd Syracuse `S`, the canonical minimum `nu`, `T=nu S`,
`P(w)=[3w]-[w]`, and `rho(w)=nu(3w)` on W5. The fixed resolver is exactly
[the twelve-family dispatcher](../selected_rules/SELECTED_RULES.md) from
the preceding batch. It does not call the new constructor recursively.

## 1. A safe finite signed expansion

Suppose an explicit finite integer current and signed W5 coefficients obey

\[
 \operatorname{div}J=P(w)-\sum_u c(u)P(u).               \tag{1}
\]

There is initially no requirement that `rho(u)<rho(w)`. Keep `w` protected:
an occurrence of the original request is not a new proof input. Repeatedly
choose a remaining, unprocessed request of largest rank at least `rho(w)`.
If it is the protected source or the fixed resolver has no accepted rule,
retain it explicitly. Otherwise substitute its accepted exact rule

\[
 \operatorname{div}J_u=P(u)-\sum_v a_u(v)P(v),\qquad
 \rho(v)<\rho(u),
\]

by replacing `J` with `J+c(u)J_u`, removing `c(u)P(u)` from the request
list, and adding `c(u)a_u(v)` at each child. Combine equal coefficients
exactly, including opposite signs. Formula (1) is unchanged.

**Finite-composition theorem.** This process terminates for every supplied
finite initial plan when the resource cap is omitted. If `M` is the largest
initial request rank, at most `max(0,M-rho(w)+1)` high-rank vertices need
be examined. Indeed the W5 rank is injective by R37. A processed rank cannot
reappear from any lower-ranked accepted rule. Largest-first processing
therefore strictly decreases the next unprocessed rank. Blocked vertices
cannot subsequently acquire another contribution from a lower vertex.
This bound concerns attempts, not their bit complexity or the discovery of
actual absorption currents.

The final plan is a new strict-rho rule precisely when every remaining
request has smaller original rank. Otherwise the larger, equal, or protected
requests remain explicit missing premises. A resource cap returns an exact
unfinished plan labelled `capped`; it does not certify or discard its
frontier. This is finite termination of formal rewriting, not universal
success of the rank test. In particular R56's h0 self-request cannot be
removed by invoking the same proposed construction on itself.

`defer` implements this theorem. `one_step` tries the existing R55 first
and permitted second plans, the two R56 plans, and the R57 exit plan, in
that order. It returns only a final strict-rho result. Each expanded rule,
its signed multiplier, original requests and blocked vertices are retained
in the result. `compile_plan` requires exact supplied currents for all
remaining nonzero requests.

## 2. Exact requests improve a rejected endpoint bound

For every integer `n>=0`, put

\[
 \begin{aligned}
 w&=245+1024n,&q&=367+1536n,\\
 f&=931+3888n,&m&=465+1944n,&s&=349+1458n.
 \end{aligned}                                         \tag{2}
\]

Then `3w` is selected, `q=rho(w)`, the first R55 parameters are A4d2,
and its raw endpoint is selected `f`, with `nu(f)=m=1 mod8`. The old
piecewise endpoint bound rejects the entire A4d2 row. Nevertheless the
actual signed request list of that same formal current is already strict
below `q`, for **every** n.

**Proof.** `q=16t-1` with `t=23+96n`. Exact substitution gives the A4d2
parameters and `f=2m+1`. Since m is canonical1 mod8, `f` is its selected
partner. The formal plan for `m` first uses its ordinary valuation2 arrow
to `s=(3m+1)/4`, which is1 mod3 and satisfies

\[
                       q-s=18+78n>0.                  \tag{3}
\]

The already proved R44 branchwise bound obeys `B(s)<=s` for every positive
odd `s=1 mod3`. For canonical s3 mod4 it equals s; for canonical s1 mod8
it is `(27s+29)/32<=s`, with s1 absorbed separately. If s is noncanonical,
`nu(s)<=(s-1)/2` and the generic bound `(9nu(s)+5)/8<s` suffices. Thus
all requests of the exact `H_m` are below q. The other absorption input
is `nu(w)<w/4` and already has smaller request ranks. This proves the
complete claim without expanding any high request. ∎

The subprogression

\[
                         w=245\pmod{3072}              \tag{4}
\]

is genuinely outside all twelve earlier direct domains. It is selected
w2 mod3, which excludes all nine old predicates by R55's whole-unit-class
proof. R55 rejects A4d2 and has no second-block option at A4. R56 requires
w1 mod3, and R57's phase also has w1 mod3. Consequently (4) adds complete
new coverage; it is not an extrapolation from a finite acceptance count.

## 3. A complete branch with a genuinely larger intermediate request

For every integer `l>=0`, define

\[
 \begin{aligned}
 w&=1301+32768l,&q&=1951+49152l,\\
 f&=7411+186624l,&m&=3705+93312l,\\
 s&=2779+69984l,&u&=1853+46656l,\\
 g&=3127+78732l,&r&=(g-1)/2=1563+39366l.
 \end{aligned}                                         \tag{5}
\]

Assume **g is selected** in the exact R25 sense. This is the entire stated
branch, allowing every selected exponent; it is not a fixed-depth scan.
The resulting deferred plan is strict below the original q. It expands
exactly one larger request, `P(u)`, with coefficient+1.

### Arithmetic and the larger request

Here `q=rho(w)=32t-1`, `t=61+1536l`; its first R55 block has A5d2.
Its selected raw endpoint f has `nu(f)=m=1 mod8`. The R44 bound used by
the old parent rule equals g exactly:

\[
 B(f)=(27m+29)/32=g>q.                                 \tag{6}
\]

Hence the old R55 parent test rejects every member. But `S(m)=s`, and s
is a complementary canonical root1 mod3 with critical W5 input
`u=(2s+1)/3`. Its rank s is larger than q. Moreover `u=2 mod3` and its
R55 block is A2d2, with raw endpoint g. By the selected-g hypothesis,
that child is accepted by R55; all earlier nine predicates exclude it.
Thus the fixed twelve-rule resolver chooses exactly this R55 child.

The exact `H_s` requests `P(u)` once and then the formal `H_u`. Since
u is W5, `nu(u)<=(u-1)/4`, so all H_u request ranks are at most
`(9u+11)/32<q`. The lower H_(nu(w)) requests are also below q. Thus u
is the only initial request at or above the original rank, with multiplier1.

### Current cancellation, ordinary clock, and quotient clock

Write `N_x` for the exact elementary current `[x]-[nu(x)]`. The parent
current is

\[
 N_{3w}+D_q+N_f-N_w+H_m-H_{\nu(w)},                    \tag{7}
\]

where D_q is its five-arrow R26 prefix. The deterministic formal plans
satisfy the exact current/request identities

\[
 H_m=\delta_m+H_s,\qquad
 H_s=-N_{3u}+P(u)+H_u,\qquad H_u=N_u+H_{\nu(u)}.       \tag{8}
\]

The notation `P(u)` in (8) denotes a missing source input; `delta_m` is the
unit current row on `m -> s`. Substituting the child current

\[
 N_{3u}+D_s+N_g-N_u+H_r-H_{\nu(u)}
\]

therefore cancels all intermediate H_u terms and both normalizers at u.
Only the final H_r and original lower input remain. This is signed
linearity of actual finite current rows, not an assumption that u absorbs.

More precisely the combined q-to-g current is exactly the eight ordinary
arrows with valuation word

\[
                       (1,1,1,1,2,1,3,2).              \tag{9}
\]

The successive states are

\[
\begin{array}{rcl}
q&=&1951+49152l,\\
S(q)&=&2927+73728l,\\
S^2(q)&=&4391+110592l,\\
S^3(q)&=&6587+165888l,\\
S^4(q)&=&9881+248832l,\\
S^5(q)&=&7411+186624l=f,\\
S^6(q)&=&11117+279936l,\\
S^7(q)&=&4169+104976l,\\
S^8(q)&=&3127+78732l=g.
\end{array}                                            \tag{10}
\]

Every displayed successor is odd, proving each exact valuation. The total
valuation12 uses the extra-bit modulus8192; the q step49152 is divisible
by8192. At f, the selected exponent is exactly2, so N_f is the difference
of two two-arrow prefixes from f and m. The subsequent three-arrow prefix
from m to g contains the negative prefix, which cancels. This proves the
row-for-row identity between (7) after substitution and the ordinary
eight-arrow path, not merely equality of endpoints. By R25's exact
semiconjugacy, `T^8(q)=nu(S^8(q))=r`. The upper normalizer N_(3w) retains
its two six-arrow prefixes; the g normalizer has its own selected clock.
Neither is counted as a zero-length ordinary arrow.
Writing `a_g=v2(g+1)`, the normalized comparison also gives the exact
ordinary equality `S^(8+a_g)(q)=S^a_g(r)`. Its current is the difference
of those two prefixes. The possibly varying `a_g` is retained in full.

### Original-rank decrease and a wholly new progression

The final upper requests obey

\[
 q-\frac{9r+5}{8}=\frac{1536+38922l}{8}>0.             \tag{11}
\]

All lower requests already lie below q. Therefore the exact composite
passes the original-rank test for every l with selected g, even though
the intermediate request u is larger in both index and rank.

For `l=24j`, g is selected with exponent exactly3:
`g+1=8(391+236196j)`, with the odd unit3 mod4. Also w2 mod3. Hence

\[
                         w=1301\pmod{786432}            \tag{12}
\]

is a complete new progression. The nine old predicates exclude selected
w2 mod3; R55 rejects its A5d2 parent by (6) and has no A5 second-block
option; R56 and R57 require w1 mod3. Thus every term of (12) was outside
all twelve direct domains. The selected-g hypothesis is retained for the
larger branch (5); nothing here asserts success for all unselected exits.

## 4. Implementation, evidence, and remaining obligation

`deferred_rank.py` exposes `defer`, the bounded candidate dispatcher
`one_step`, the two whole-family constructors, and checked substitution of
supplied currents. It reads only the fixed old twelve-family resolver.
An unresolved original request cannot call back into this new dispatcher.

Run `python3 experiments/residual_progress/deferred_rank/check_deferred_rank.py`.
The receipt audits the specified finite candidate window, complete-family
examples including large parameters, all signed boundary identities, the
eight-arrow word and exact composite current, protected self-requests,
negative request multipliers, caps and missing input rejection. Actual
supplied-current demonstrations remain separate from the symbolic rule
proofs and retain their full input/output tables under explicit search caps.

The stored default audit checks 127 initial plans from the unrecognized
inputs among 1024 W5 candidates below8192. It finds 23 new descending seeds
in that finite window and retains 101 protected-source cases. It also
checks 68 examples from each complete family, 72 whole-new-domain examples
through parameter powers2^128, a negative-multiplier identity, a retained
zero-budget frontier, and seven invalid-call rejections. Four actual
substitutions use 13 distinct supplied pair currents; full input and output
tables for245 and1301 are stored. These finite counts audit the code and
do not establish an asymptotic acceptance rate.

The two new domains can be appended to a common-rho rule collection.
The general deferred procedure may find more successes, but can terminate
with blocked high requests. Its finite termination does not establish
universal strict descent or the existence of all remaining input currents.
