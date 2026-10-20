# Complete control of the guarded Phi exits

**Status: written arithmetic classification and conditional finite-current
construction. No universal current supply or whole-type termination is proved.**

This package merges the exact binary return with every maximal exit row. It
keeps the original threshold fixed, every signed premise, and both ordinary
clocks. The raw endpoint test is a complete arithmetic test for that endpoint;
it is not a test for all possible current constructions. The ancestor-cover
statement concerns unconditional absorption, not pair currents alone.

The inputs come from the [retained-history cell](../retained_history/RETAINED_HISTORY.md).
Use the odd-only Syracuse map S with absorption at1, elementary normal form nu,
and quotient T=nu composed with S on canonical states. Write P(w)=[3w]-[w].
The native critical-basis plan is [s]=div J_s+A_s.P, with nonnegative integral
coefficients A_s and every request rank rho(u)=nu(3u) at most nu(s). Both W5 and
W9 input types remain available. A finite formal current becomes an actual
pair current only after every remaining signed pair premise is supplied.

## Exact return and its guards

Put

    A = 3^12 = 531441, M = 2^19 = 524288,
    B = 299947, D = A-M = 7153,
    Phi(v) = (A v+B)/M, L(v)=D v+B.

The broader binary version of the coupled R89 input condition is

    v = 133797 (mod 2^18).

Equivalently, beta=(729v+35)/4096 is an integer congruent to 5 modulo 64.
This is exactly one progression with minimal modulus 2^18; it does not contain
the original retained-cell ternary condition.

The two exact ordinary Syracuse valuation words

    raw start 6v+1: (1,1,1,1,3,1,4,1,2,1,1,2),
    start 3v:      (1,1,1,2,1,1,4,1,2,1,1,2)

both end at 6Phi(v)+1. Both words have length12; their
valuation sums are respectively 19 and 18. Their common complete v-cylinder is
v=133797 modulo 2^19. To check completeness, a fixed odd valuation word of sum
E has exact starting cylinder modulo 2^(E+1). Substitution of 6v+1 removes one
binary bit for the raw word; substitution of 3v preserves all bits for the
second word. The representative 133797 has the displayed words, and the
opposite lift 395941 has last valuation 3 instead of 2. The affine endpoints
of both words are

    (1594323 v+1161985)/262144 = 6Phi(v)+1.

In particular, re-entry into the broader guard implies both words are valid.
Indeed, the guard is L(v)=0 modulo 2^18, and

    L(Phi(v)) = (3^12/2^19)L(v).

Thus the exact single re-entry cylinder is

    v = -B D^(-1) (mod 2^37),

whose least residue is 102642092709. It implies the complete word cylinder.
The quotient identity on this re-entry cylinder is T^12(3v)=3Phi(v).
For an explicit check, put C=(81v+11)/64, beta=(729v+35)/4096,
X=18beta+1 and Z=(81beta+7)/4. The elementary normalization formulas give
T^4(3v)=3C, T^7(3v)=X, T^9(3v)=Z and T^12(3v)=3Phi(v).
The guard fixes the required selection bits. In the first intermediate segment,
the selected sibling's negative three-row tail cancels the three-row upper
prefix, as in the retained-history construction. This verifies the quotient
clock separately from the ordinary words. The ordinary twelve-step endpoint
is 6Phi(v)+1.

## Maximal repetitions, growth, and original-cell intersection

For a positive guarded v, let h=v2(L(v)). Since L(v)>0, h is finite. The exact
maximum number of consecutive guarded re-entries is

    floor((h-18)/19).

Each such return reduces h by 19, increases v3(L) by 12, and increases v:
Phi(v)-v=L(v)/M>0. The prime-to-6 part of L is conserved. This is a genuine
finite countdown for this one subsystem. No bound on later exits or subsequent
return mechanisms follows from it.

For every r>=0, all starts with at least r re-entries form the complete cylinder

    v = -B D^(-1) (mod 2^(19r+18)).

These cylinders intersect the original coupled R89 cell for every r. Write

    V0=67839005952677, P0=2^18*3^18,
    v=V0+P0*l, m=2736+4096*l.

Let c_r be the least nonnegative residue -B D^(-1) modulo 2^(19r+18), and set

    l_r = ((c_r-V0)/2^18)*(3^18)^(-1) modulo 2^(19r).

Then precisely l=l_r+2^(19r)j, j>=0, gives the required original-cell starts.
All inverses are of odd integers, and c_r-V0 is divisible by 2^18.

Only the START is asserted to lie in the original retained ternary cell. On
that original cell v3(L(v))=4, so for its raw r0=6v+1 and first return g,

    v3(g-r0)=v3(6L(v)/2^19)=5.

The original raw cell has period 128*3^19, so it is not invariant under this
return. Arbitrarily long repetitions use different starting
integers and the broader binary guard, not invariance of the original cell.

## Full signed comparison at the fixed original threshold

For the original m and Q=133704987+3*2^33*m, set b=Q/3. Let v_i=Phi^i(v_0).
The original ordinary 18-prefix ends at 6v_0+1. Concatenating the exact raw words
therefore gives an actual ordinary prefix of length 18+12i ending at 6v_i+1.
Every v_i in the guard is 37 modulo 64. Its selected terminal sibling has the
same five-step tail as 3v_i. Consequently

    S^(23+12i)(Q) = S^5(3v_i),
    T^(18+12i)(Q) = 3v_i.

Keep both clocks. If K_i is the difference of these two finite ordinary path
currents, then div K_i=[Q]-[3v_i]. With native critical-basis absorption plans
[s]=div J_s + A_s.P, the complete conditional pair identity is

    P(b) = div(K_i+J_(v_i)-J_b)
           + ({v_i:+1}+A_(v_i)-A_b).P.

No coefficient is dropped. Its request v_i has coefficient +1 and is the
unique highest-rank request, with rho(v_i)=3v_i>Q. The other positive requests
have rank at most (3v_i+1)/16 because the first elementary reduction and free
arrow of v_i supply that bound. Negative A_b requests have rank below Q.
All remaining ranks are below 3v_i, but they are NOT claimed below the fixed
original Q for arbitrary i. This is why an increasing raw return does not by
itself establish a repeated admissible R89 original-Q plan or a supply theorem.

## Maximal-exit parameters and the fixed original threshold

Put V0=67839005952677, VP=2^18*3^18. The original coupled sources are

    v0=V0+VP*l,
    Q=70506316836123+3*2^45*l
     =(2^27*v0-213949807)/3^17, l>=0.

At the maximal return count r the exit v=Phi^r(v0) has
h=v2(Dv+B) in {18,...,36}. Its complete exit cylinder is

    v=c_h+2^(h+1)*t,
    c_h=(2^h-B)*D^(-1) modulo 2^(h+1).

Every prescribed r,h occurs in the original cell. The next section refines
this cylinder by the exact first variable valuation, including its extra bit.

## Nineteen complete prefixes, followed by one arbitrary valuation

Let W=(1,1,1,1,3,1,4,1,2,1,1,2), the twelve-arrow raw return word.
The table gives the maximal fixed ordinary prefix from 6v+1 on the entire
h-cylinder. At its end the next valuation a is any integer a>=p. E is the
sum of the fixed prefix valuations, and ell its length.

|h|fixed prefix|ell|E|p|
|--|--|--:|--:|--:|
|18|W without its final 2|11|17|3|
|19|W|12|19|2|
|20|W,1|13|20|2|
|21|W,1,1|14|21|2|
|22|W,1,1,1|15|22|2|
|23|W,1,1,1,1,1|17|24|1|
|24|W,1,1,1,1,2|17|25|1|
|25|W,1,1,1,1|16|23|4|
|26|W,1,1,1,1,3|17|26|2|
|27|W,1,1,1,1,3,1,1|19|28|1|
|28|W,1,1,1,1,3,1,2|19|29|1|
|29|W,1,1,1,1,3,1,3|19|30|1|
|30|W,1,1,1,1,3,1|18|27|5|
|31|W,1,1,1,1,3,1,4|19|31|2|
|32|W,1,1,1,1,3,1,4,1,1|21|33|1|
|33|W,1,1,1,1,3,1,4,1|20|32|3|
|34|W,1,1,1,1,3,1,4,1,2|21|34|2|
|35|W,1,1,1,1,3,1,4,1,2,1|22|35|2|
|36|W,1,1,1,1,3,1,4,1,2,1,1,1|24|37|1|

This is a finite affine verification, not a sampled classification. Start
x=alpha*t+beta with alpha=6*2^(h+1), beta=6*c_h+1. At each fixed step,
v2(3*beta+1)<v2(3*alpha), so that valuation is constant for all t. At the
listed stopping point, p=v2(3*alpha) and v2(3*beta+1)>=p. Define the odd
integer u=3*alpha/2^p and the integer z=(3*beta+1)/2^p. The exact next-a
cell, with j=a-p>=0, is

    t=(2^j-z)*u^(-1) modulo 2^(j+1).

Every such cell is nonempty and includes the required extra bit. In particular
p=h+2-E. The constructor computes all integer affine states; the checker independently
verifies each fixed valuation and the first variable one.

The resulting exact exit-v residue has modulus 2^(E+a). Writing
C_r=B*(A^r-M^r)/D, its pullback to v0 has modulus 2^(19r+E+a), with residue

    v0=(M^r*c_exit-C_r)*(A^r)^(-1) modulo 2^(19r+E+a).

Divide the difference from the original v0 base by 2^18, then invert 3^18,
to obtain the exact original l progression. This determines *exactly* r
re-entries, exit h, and next valuation a, not just lower bounds.

## Complete raw-target test, keeping original Q

For the listed fixed prefix, define its affine constant c by
x=(6*3^ell*v+c)/2^E. Initialize c=1,E=0; an arrow of valuation e changes
c to 3c+2^E and E to E+e. After the variable arrow let t0=ell+1 and
c_star=3c+2^E. Its actual endpoint is

    y=[6*3^t0*(A^r*v0+C_r)+M^r*c_star]/[M^r*2^(E+a)].

Exactly y<Q if and only if

    [2^27*M^r*2^(E+a)-6*3^(t0+17)*A^r]*v0
      > 3^17*[6*3^t0*C_r+M^r*c_star]
        +213949807*M^r*2^(E+a).

The right side is positive. Thus a nonpositive bracket excludes the raw-target
stop on the entire fixed (r,h,a) cell. A positive bracket gives an exact lower
bound on v0; intersecting it with the complete progression handles any finite
initial exceptions. This is only the raw-target test. Native normalization can
succeed above Q, so its failure is not a missing-current claim.

Any fixed h,a has a positive fixed terminal slope multiplied by (A/M)^r.
Therefore the raw-target stop cannot work on that fixed exit template for
arbitrarily large r. A variable exit valuation can compensate; no argument
here forces it to be large enough.

## Signed inputs: forward history creates no negative high cancellation

The concatenated ordinary path from the original Q to y has length

    L=18+12r+ell+1.

For b=Q/3, its complete native formal pair plan is

    P(b)=div(prefix(Q,L)+J_y-J_b)+(A_y-A_b).P.

All requests of A_b have rank<Q, while the native absorption coefficients in
A_y are nonnegative. Consequently every request with rank>=Q in this fresh
plan is positive. No high negative request can be cancelled merely by
retaining more of this one forward history. The original inherited D+E+F
relations stay below the original Q and likewise cannot cancel those high
requests. A new cancellation needs another comparison or a separate retained
history. This does not exclude progress by a potential on positive vectors.

## A scope fact: each fixed exit cell is an unconditional ancestor cover

For fixed r,h,a, let L be the total ordinary word length above, and E_total
its total valuation sum. The original Q step is 3*2^45. The exact word fixes
l modulo 2^(E_total+1-45), because its complete cylinder has modulus
2^(E_total+1). Here E_total=26+19r+E+a>=46. Therefore the complete cell's
terminal image is exactly

    y=y_min+2*3^(L+1)*j, j>=0.

It is a tail of all odd integers in one residue class modulo 3^(L+1), with
no remaining binary restriction. This supplies an explicit ancestor-cover
property. Given any positive odd z not divisible by3, choose e with

    2^e*z=3*y_min+1 modulo 3^(L+2).

Such e exists because 2 generates the units modulo powers of3. Adding the
period 2*3^(L+1) makes e arbitrarily large. Then p=(2^e*z-1)/3 is an odd
member of the terminal progression once large enough, and S(p)=z. Its unique
preimage Q in the fixed cell is positive and reaches z after L+1 arrows.
For a seed divisible by3, its next Syracuse state is not divisible by3.

Thus unconditional absorption of *one complete fixed exit cell* already
implies Collatz. This is NOT an equivalence for the pair currents P(Q/3)
alone, and NOT an obstruction to a useful conditional repair with strictly
smaller original-Q premises. Those must remain distinguished. The statement
also does not assume a uniform bound on the exponent e; it may be very large.

Elementary justification of the unit generator: v3(4^(3^j)-1)=j+1 by the
binomial induction. Hence 2 has order 2*3^(K-1) modulo3^K, the entire number
of units.

## Why the gained ternary order does not automatically make a long point chain

The rational centre of the raw word is -1792529/7153. Every finite ordinary
word applied to that centre remains a rational with reduced denominator
7153 times a power of2: multiplication by3 is invertible modulo7153.
It can never equal -1. Therefore, after any fixed exit word, the exact finite
value v3(y_shadow+1) stabilizes the maximal point-chain length once the gained
ternary precision exceeds it. The latter grows with r, but the former does
not. With variable a, high point depth is a separate congruence in 2^a; it is
not a consequence of r alone. Multi-ray inverse words are outside this claim.

## Consequences and unresolved obligation

The binary budget is a well-founded countdown for consecutive Phi re-entries.
It does not control how another branch changes the affine centre or replenishes
precision. The original ternary cell is not closed, the raw return grows, and
all high requests in a fresh forward comparison are positive. These statements
rule out treating the countdown or the endpoint table as terminal supply.

The exact whole-exit obligation remains: supply every remaining pair current
at the original rank, or prove a recurrence which terminates across all exits.
The interface permits parameter-dependent histories and additional signed
comparisons. It does not exclude multi-ray inverse words, later targets,
nonlocal histories, or richer progress measures. The separate first-ray/point
scratch obstruction is intentionally not part of this result.

## Executable interface and verification

`phi_exit_control.py` exports:

- `repeat_parameters(count,index)` and `repeat_comparison(...)`: complete
  at-least-count cylinders and full signed original-Q comparisons;
- `exit_row(h)`: the exact row and its maximal fixed affine prefix;
- `exit_parameters(count,h,a,index)`: complete exact-count/exit/valuation cells;
- `exit_comparison(...)`: actual forward current plus every native signed
  request, explicit high frontier and exact raw inequality;
- `ancestor_exponent(target,anchor,power)`: a modular exponent certificate for
  the ancestor-cover argument, without materializing enormous powers of2.

Both comparison constructors have an explicit ordinary-prefix cap, default
10000. They reject invalid integer domains and incomplete capped comparisons.
No absorption search or dispatcher extension is performed. A returned
`descending` status means every retained premise is strictly below the
original threshold; it does not mean those premises have been supplied.

Replay with:

    python3 experiments/residual_progress/phi_exit_control/check_phi_exit_control.py

The checker independently recomputes ordinary arrows and current boundaries,
replays complete cells and exact progression increments, and pins reachable
local source dependencies. The finite receipt is
[phi_exit_control_audit.json](phi_exit_control_audit.json). Its finite samples
support the written arguments; they do not establish their universal scope by
sampling. No terminal absorption current is assumed or searched for.


The frozen focused receipt covers10 full return comparisons (two indices for
r=1,2,4,8,16), all19 exact rows, and171 full signed exit comparisons
(r=0,1,4; every h; a=p,p+1,p+3). Every exit also checks the next progression
member and its exact image increment. All ten return plans and three exit
plans are stored in full; the latter have156/283/498 current rows. Fifteen
modular ancestor certificates and29 explicit invalid-premise/cap controls are
retained. Sixty-five tested cases have raw y>=Q while their native formal plan
is descending, preserving the non-necessity of the raw stop. Reachable source
pinning covers37 local files. Generation and default replay each took about
1.5 seconds. These are conditional comparisons; no terminal inputs were
supplied or silently discarded.
