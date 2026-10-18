# The complete exponent-eleven exit and an exact continuation undo

**Status: written complete exit identity and scoped infinite-family
obstruction, with unfinished integer currents retained.** The exponent11
row has a sharp comparison with the original rank. On a full CRT family,
appending any prescribed finite number of complete forward blocks and
then applying the named inverse rules returns exactly the original
unfinished current. Its leading missing input lies outside all twelve
direct domains in the dispatcher at commit7206f9c. This does not exclude
other comparisons, newly proved rules, longer seed-dependent continuations,
or eventual absorption. It is not a positive divergent-orbit construction.

The point is to preserve the original rank after the growing cycles.
A decrease from their final endpoint alone need not be progress.

Use the absorbed odd Syracuse S, elementary minimum nu, quotient T=nu S,
P(w)=[3w]-[w], W5={w>0:w=5 mod8}, and rho(w)=nu(3w).
Killed atoms have[1]=0. Let H_x be the unchanged formal R43 absorption
plan after full W9 substitution, with integer current J_x and signed
request vector A_x:

    [x]=div J_x + sum_u A_x(u)P(u).

All requests remain premises. We use its exact elementary normalization
identity H_x=N_x+H_nu(x), where div N_x=[x]-[nu(x)].
Dependencies are [R41](../critical_inverse/CRITICAL_INVERSE.md),
[R43](../critical_rank/CRITICAL_IMAGE_RANK.md),
[R48](../nonselected_forward/NONSELECTED_FORWARD.md),
[R53](../forward_continuation/FORWARD_CONTINUATION.md),
[R57](../selected_cycle_exit/SELECTED_CYCLE_EXIT.md), and the fixed
[twelve-rule dispatcher](../selected_rules/SELECTED_RULES.md).

## 1. The entire exit-exponent11 stratum

For every integer r>=0 and every positive odd s, put

    q=81*2^(11r+11)s-17,   w=(2q+1)/3,
    f=3^(7r+10)s-6.                                    (1)

There are exactly r guarded R54 cycles before the R57 exit exponent11.
Its complete exit bridge has boundary[q]-[f], quotient clock7r+6 to
nu(f), and ordinary common-tail clocks

    S^(7r+7)(q)=S(f).                                  (2)

In particular this entire row is represented without searching an orbit.
The raw endpoint comparison is exactly

    f>q if and only if r>=16.                          (3)

This is a comparison of raw f with the **original** q; normalization may
still make a particular f useful. It is not a statement that all r>=16
inputs fail every possible current test.

To prove(1)–(2), the last cycle endpoint is
Q=2^11 U-17 with U=81*3^(7r)s. R57's first block has(a,d)=(4,2),
reaching selected Y=5184U-41. Its minimum is V=2592U-21, and
S^3(Y)=S^3(V). The second block has(a,d)=(2,3), with raw endpoint
729U-6=f and ordinary clocks(3,1). Add the four ordinary arrows to Y
and the7r preceding ordinary cycle arrows. The quotient lengths are
4+2+7r. The current is precisely the left path in(2) minus the single
row at f.

For(3),

    f-q=(3^(7r+10)-81*2^(11r+11))s+11.

The coefficient's ratio increases by2187/2048 with r. The two exact
integer comparisons

    3^111 < 2^176,             3^118 > 2^187

locate the transition between r15 and r16. The nonzero coefficient is
a multiple of81, so the intercept11 cannot reverse either sign for s>=1.

## 2. A full family with arbitrarily many further growing blocks

Fix **any** r>=16, A>=5, K>=0, and let M=7r+10. Take every positive
integer t satisfying the complete coprime CRT conditions

    t = -9*3^(-A)                         mod2^(3K+6),
    t = (3^M epsilon-5)*2^(-A)             mod3^(M+1),
    epsilon = 2^r mod3 in {1,2}.                        (4)

Define

    f=2^A t-1,   s=(2^A t+5)/3^M,
    q,w as in(1),   v=f/3,
    g=(3^A t-1)/2,   G(x)=(9x+5)/8,   g_j=G^j(g).     (5)

These are positive integers, s is odd, and s=epsilon mod3. The first
congruence makes f complementary canonical with exact run parameters
(a,d)=(A,2). Its complete raw return is g>f. It also gives

    g+5=0 mod2^(3K+5),
    g_j+5=9^j(g+5)/8^j.                                (6)

Thus every g_j,0<=j<=K, is27 mod32 and complementary canonical.
There are at least K further complete(a,d)=(2,2) blocks, with

    q < f < g_0 < ... < g_K.                           (7)

K counts a prescribed prefix, not necessarily the maximal low run.
The first complete block from f has A ordinary arrows, and every low
block has two. After adjoining the first block and j low blocks to(2),
the row at f cancels. The resulting current is an actual ordinary path
from q to g_j of length

    7r+A+6+2j.                                        (8)

This equals its quotient clock. No inference about later paths is made.

Every class in(4) is nonempty because the moduli are coprime. If t_0
is its least positive representative, t=t_0+i*2^(3K+6)*3^(M+1), i>=0.
The corresponding periods are

    Delta s=3*2^(A+3K+6),
    Delta w=81*2^(11r+A+3K+18).                        (9)

This construction permits r, A and K to be chosen independently in their
stated ranges. It is not a list of isolated examples.

## 3. Both the original input and the exit's leading input are unhandled

The original w is in R54's phase3445 mod3456, outside the original nine
direct domains. R55 sees first parameters(4,2) and rejects its bound;
its second-block option has domain(2,2). R56's parameter is

    (32q-23)/81=2^(11r+16)s-7=0 mod3

by epsilon in(4), so both its inverse depths are zero. R57 ends at the
canonical f in(5), which has v3(f)=1 and f/3=v in W5. Its bound is
therefore B(f)=f>q. The complete original twelve-rule dispatcher fails.

Now consider the leading pair input v=f/3. Its critical image is f,
and

    v=3^(M-1)s-2,  v=5 mod8,  v=1 mod3.                (10)

It too fails all twelve direct domains:

- It has nonselected3v=f and is not divisible by3. This excludes the
  selected rules R41/R44/R46/R52/R55/R56/R57 and the multiple rule R47.
- R45's k4 depth is0, while its k8 depth is1 with lower endpoint0 mod3,
  the exact returning-self-request row. Thus neither base ray descends.
- For R50, the k8 first lower endpoint is
  p=32*3^(M-2)s-21. Its next depth is v3(2p+1)=0, outside that rule.
- R48's first complete run is(A,2), with canonical endpoint g=1 mod3
  and B(g)=g>f. Its endpoint-bound test fails.
- R53 requires first exponent3 or4, whereas A>=5.

The equalities use M>=122; no large-r approximation is involved. This
classification concerns exactly the fixed twelve dispatchers. A later
rule could recognize v and defeat this particular obstruction.

Because f is critical with f/3 in W5, its full formal absorption vector
is

    A_f={v:1}+A_v.                                    (11)

All requests in A_v have rank at most(9v+5)/8=(3f+5)/8<f. The original
lower input z=nu(w)<w/4 has all request ranks below q<f. Consequently
the full original exit plan

    C_0=N_(3w)+D_(q,f)-N_w+J_f-J_z,
    c_0=A_f-A_z                                      (12)

has exactly one largest-rank request, namely v with coefficient+1 and
rank f>q. No lower-rank strict-rho expansion can create v or cancel it.

## 4. Complete inverse undo, including every current and auxiliary request

Convert any endpoint g_j to H_g_j after appending the blocks in Section2.
There is an explicit finite sequence of valid R41 leading substitutions
that restores exactly(12), **both its integer current and its signed
request vector**. Nothing is discarded as small or affordable.

For a canonical critical x=1 mod3, put a=(2x+1)/3. Its H step is

    J_x=-N_(3a)+J_a,     A_x={a:1}+A_a.                (13)

For x=g, R41 has h=v3(2g+1)=A and its maximal inverse endpoint is f.
For x=g_j,j>=1, one has

    2g_j+1=9(g_(j-1)+1)/4,

so h=2, with unit2 mod3, and its inverse endpoint is g_(j-1). These are
all descending R41 rows: the first index has v3(a)=A-1>=4, while later
indices have v3(a)=1 and unit2. The forbidden R41 returning phase is
never used. Their negative ordinary paths are precisely the negatives
of the just-appended full blocks.

For either predecessor y=f or y=g_(j-1), its critical index b is in W5.
The substituted R41 current for P(a) is

    L_a=N_(3a)+I_(x,y)-N_(3b)-N_a+J_b-J_nu(a),
    c_a={b:1}+A_b-A_nu(a),                            (14)

where I_(x,y) is the negative appended path. Add(14) to(13) after
removing its P(a) premise. Exact elementary normalization gives
J_a=N_a+J_nu(a), A_a=A_nu(a). The result is exactly

    I_(x,y)+J_y,       A_y.                           (15)

The appended forward path cancels I_(x,y) row for row. Applying this
identity j+1 times yields the original current and vector(12). This is
stronger than a height comparison or a check of one displayed source.

At every stage the critical request being replaced is the unique largest
rank with coefficient+1, because its remaining H_a requests have smaller
rank. After the prescribed undos the largest request is v from(11),
which the fixed twelve-rule dispatcher does not handle. Any further
strict-rho expansion of other requests cannot create that index.

Therefore no uniform number of these appended complete forward blocks,
followed by these exact leading inverses and lower-request expansions,
closes the entire exponent11 exit row. This does not rule out a successful
longer continuation for a given seed, a different inverse word, arbitrary
joint cancellation, a future broader direct rule, or any global Collatz
proof. The finite bound K and the actual seed vary together.

## 5. Executable evidence

`exit_continuation.py` implements the whole exit identity, the complete
CRT family, the appended currents, and the finite inverse-undo schedule.
It exposes the positive leading request rather than compiling it as a
supplied current. `check_exit_continuation.py` replays exact clocks,
both source boundaries, direct-rule exclusions and complete equality
of the current and request vector after undo. Resource bounds and a full
unfinished current fixture are retained in its receipt.

Run `python3 experiments/residual_progress/exit_continuation/check_exit_continuation.py`.
No absorption discovery is used. Finite checks audit the implementation;
the written argument supplies the infinite quantifiers. Universal supply
on the remaining domain stays open.
