# V009 — Every nonconstant invariant has unbounded additive excess

**Status: written theorem; independent agent review passed.** The
[review](ADDITIVE_REVIEW.md) covers the complete return argument.
This note assumes, for contradiction analysis, a nonconstant
finite-valued Collatz invariant satisfying

```
kappa_h(D)=D+O(1).
```

It derives a fixed maximal ternary depth increment in {3,4} and exactly
two possible periodic escape patterns, up to phase, then excludes both
by controlling every return to an earlier state. Thus a nonconstant
invariant cannot satisfy this additive-error bound. Equivalently its
nondecreasing excess kappa_h(D)-(D+1) tends to infinity. This diagnostic
theorem is weaker than the active unbounded-ratio goal and does not
complete that goal.

## 1. Exact setup and dependencies

Use the whole binary sections of h, with h(0)=h(1), and let rho(f) be
the minimum binary depth at which f occurs. Since h is nonconstant,
V004 makes its binary kernel infinite. Every binary layer is nonempty;
therefore kappa_h(D)-(D+1) is a nonnegative nondecreasing integer.
The assumed bound implies that, from some depth N onward, each binary
layer contains exactly one entire sequence, denoted q_n at depth n.

Work in S=K_2(b), where b(n)=h(2n+1). Removing the common power of two
from a positive offset shows that S is exactly the family of positive
binary h-sections. It consists of a finite initial set and all q_n for
n sufficiently large. It is closed under both section bases by V004.
Every state of S has infinite pure kernels in both bases by V005 and
the reverse-closure lemma in V007. These constancy dependencies include
V004's published Cobham input; no new external theorem is imported here.

Every q_(n+1) has a binary parent of minimum depth n, hence must be a
child of q_n. Thus the binary escape set

```
C_n={i in {0,1}: E_i(q_n)=q_(n+1)}
```

is nonempty. All other binary children have depth at most n. There is
no bound on how far they may return. For n>0, a minimal binary
representation of q_n has positive offset, so V004 gives

```
rho(T_j(q_n)) <= n+4,              j=0,1,2.                 (1)
```

This is a bound measured from h. It is not a four-step binary path
from q_n to T_j(q_n).

## 2. The maximal ternary increment stabilizes

Put

```
tau(n)=max_j rho(T_j(q_n)),
delta_n=tau(n)-n.
```

Choose i in C_n. For each j, the radix swap writes

```
T_j(q_(n+1)) = T_j(E_i(q_n)) = E_l(T_k(q_n)).
```

Since a binary child increases minimum depth by at most one,

```
tau(n+1)<=tau(n)+1,
delta_(n+1)<=delta_n.                                      (2)
```

If some delta_n<=0, (2) gives tau(m)<=m for all m>=n.
The finitely many states of S below depth n have finitely many ternary
children, all in S. Choose M>=n above their depths. The finite set
S intersect K_M(h) is then ternary-closed: tail states do not increase
depth, and the finite initial states have all their children within M.
This contradicts infinite ternary kernels. Thus delta_n>=1.

Together with (1), the integer monotonicity in (2) implies eventual
stabilization

```
tau(n)=n+delta,                  delta in {1,2,3,4}.         (3)
```

The value delta=1 is impossible. Once the finite initial states and
their ternary children are inside a sufficiently large binary ball,
every transition from its positive-section part lands in that part
or at its unique next binary state. A binary edge actually reaches that
state. This would be a finite forward interior with one joint exit,
contradicting V007's singleton-exit theorem. Consequently

```
delta in {2,3,4}.                                          (4)
```

## 3. The maximal-height boundary equation

Increase N so that (3) holds and the ternary children of every earlier
state have depth below the levels considered. Define the nonempty set

```
D_n={j in {0,1,2}: T_j(q_n)=q_(n+delta)},
X_n(z)=sum_(i in C_n) z^i,
Y_n(z)=sum_(j in D_n) z^j.
```

At q_n, a binary-then-ternary path has the largest possible final
depth n+delta+1 exactly when its first digit lies in C_n and its second
lies in D_(n+1). A nonescaping binary child has depth at most n and
cannot reach this level in one ternary step. In the other ordering the
same largest depth is reached exactly through D_n and C_(n+delta).
All earlier-state returns have thus been retained and excluded from
this particular coefficient comparison by their actual depth bounds.

The six radix identities give

```
X_n(z) Y_(n+1)(z^2) = Y_n(z) X_(n+delta)(z^3).              (5)
```

Each exponent 0,...,5 has one digit pair in either ordering. Equation
(5) is therefore coefficient-exact, not just a cardinality inequality.

## 4. Eventually each radix has exactly one maximal-height digit

There are only three possible X polynomials and seven possible Y
polynomials. The relevant factorizations, after removing powers of z,
are

```
X: 1 or 1+z;
Y: 1, 1+z, 1+z^2, or 1+z+z^2.
```

The following comparisons in (5) are exact; they can be read either
as polynomial factor comparisons or as zeros at the stated primitive
roots of unity.

1. A factor 1+z^4, with a primitive eighth root as a zero, can occur
   only from Y_(n+1)(z^2) when D_(n+1)={0,2}. No factor on the right
   has such a zero. Hence this gap pair is eventually absent.
2. With gap pairs absent, a primitive fourth root can occur only when
   Y_(n+1) is an adjacent pair, z^d(1+z). Thus adjacent pairs are
   eventually absent as well.
3. A primitive third root shows that the indicator of D_n={0,1,2}
   is the same at n and n+1. It is eventually constant.
4. A primitive sixth root shows that this same indicator equals the
   indicator of C_(n+delta)={0,1}.

Thus eventually either all binary and all ternary digits reach their
respective largest-height states, or each radix has one such digit.

The all-digits case is impossible. If E_0(q_n)=E_1(q_n)=q_(n+1)
throughout the tail, reading sufficiently many binary digits sends any
fixed input to the output at zero of a later q-state. All these outputs
agree because E_0 preserves output at zero. Each q_n would be a
constant sequence, contrary to the infinite-kernel hypothesis.

We therefore have, for all sufficiently large n,

```
C_n={c_n},        D_n={d_n},
c_n in {0,1},     d_n in {0,1,2},
c_n+2d_(n+1)=d_n+3c_(n+delta).                            (6)
```

## 5. The escape digits are eventually periodic

This conclusion does not assume a finite-state decoration of the ray.
It follows from (6). For L>=1, put

```
R_(n,L)=sum_(j=0)^(L-1) 2^j c_(n+j),
P_n=R_(n,delta).
```

Multiply (6), rearranged as
`d_n-2d_(n+1)=c_n-3c_(n+delta)`, by successive powers of two and
sum L terms. Reduction modulo 2^L gives

```
(2^delta-3) R_(n,L) = 2^delta d_n-3P_n (mod 2^L).          (7)
```

The coefficient 2^delta-3 is odd, so (7) uniquely determines R_(n,L)
in [0,2^L) from the pair (P_n,d_n). This holds for every L: the pair
determines the entire future binary escape word, not merely its first
delta digits.

There are at most 3*2^delta such pairs. Two indices n_0<n_1 in a
block of 3*2^delta+1 consecutive tail indices therefore have the same
pair. Equation (7) makes their entire future c-words identical, proving
eventual periodicity with period p=n_1-n_0<=3*2^delta.

Once c has period p, subtract (6) at indices n and n+p. The differences
e_n=d_(n+p)-d_n satisfy e_n=2e_(n+1). Consequently the integer e_n is
divisible by every power of two and must be zero. The d-word has the
same eventual period.

For delta=2 this is stronger: (7) has coefficient one, so every prefix
R_(n,L) is the residue of the fixed integer 4d_n-3P_n modulo 2^L.
Its high binary digits are eventually all zero if that integer is
nonnegative, and all one if it is negative. Thus c_n is eventually
constant. Equation (6) then forces d_n=2c_n eventually. The two tails
are (c,d)=(0,0) or (1,2).

## 6. Constant escape patterns are impossible

For any delta in {2,3,4}, if c_n is eventually constant c, equation
(6) forces d_n=2c eventually: the bounded integers d_n-2c satisfy
`d_n-2c=2(d_(n+1)-2c)`. In either constant escape tail put

```
A_n=E_(1-c)(q_n),                 rho(A_n)<=n.
```

If (c,d)=(0,0), the residue-3 swap gives

```
A_(n+delta)=E_1(T_0(q_n))=T_1(E_1(q_n))=T_1(A_n).
```

For (c,d)=(1,2), the residue-2 swap gives the same identity with E_0.
Since T_1 is not the maximal-height digit, it sends a sufficiently
late state q_m to depth at most m+delta-1. Its values on the finite earlier
set have some fixed depth bound H. Hence, for every s in S,

```
rho(T_1(s)) <= max(H,rho(s)+delta-1).
```

Iterating separately on the delta residue classes of n proves

```
rho(A_n) <= lambda*n+O(1),       lambda=(delta-1)/delta<1.  (8)
```

Equation (8) alone is a growing bound. The remaining radix identities
turn it into a fixed finite bound, as follows.

Put B_n=T_1(q_n). In both escape cases there is the exact identity

```
E_c(B_n)=T_(2c)(A_n).                                    (9)
```

For c=0 this is `E_0 T_1=T_0 E_1`; for c=1 it is
`E_1 T_1=T_2 E_0`. If B_n=q_m and A_n=q_a are both in the
stable tail, the two sides of (9) are q_(m+1) and q_(a+delta).
Their minimum depths give m=a+delta-1. If A_n belongs to the finite
earlier set, its T_(2c)-image has bounded depth; then a tail B_n
also has bounded depth by the left side of (9). A B_n in the earlier
set already has bounded depth. Consequently a fixed H_1 satisfies

```
rho(B_n)<=max(H_1,rho(A_n)+delta-1)<=lambda*n+O(1).
```

The finitely many earlier states can be absorbed in a constant C, giving
the global inequality on the entire positive-section family

```
rho(T_1(s))<=lambda*rho(s)+C,             s in S.           (10)
```

Apply (10) to the exact recurrence A_(n+delta)=T_1(A_n). Separately
on the delta residue classes, the depths satisfy x_(k+1)<=lambda*x_k+C.
Thus all A_n belong to one fixed finite subset of S. The recurrence
is iteration of one deterministic map on this finite orbit, so the
delta A-subsequences are eventually periodic. There is an integer p>=1,
which may be chosen divisible by delta, such that A_(n+p)=A_n for
every sufficiently large n.

These are equalities of entire sequences. They force
q_(n+p)=q_n, also as entire sequences. Indeed

```
q_n(2m+c)=q_(n+1)(m),
q_n(2m+1-c)=A_n(m).
```

For c=0, all q_n(0) agree because their E_0-child is q_(n+1).
For c=1, q_n(0)=A_n(0), so those outputs have period p. Induction
on the input integer, simultaneously for all sufficiently large n,
now proves q_(n+p)(m)=q_n(m): the nonescaping digit uses equality
of A_n, and the escaping digit reduces a positive input to its
integer half. This contradicts the distinct minimum depths n and n+p.

All eventually constant escape patterns are therefore impossible.
Section 5 makes every delta=2 escape pattern eventually constant,
so that increment is excluded. The only surviving increments are

```
delta in {3,4}.                                          (11)
```

## 7. Exactly two periodic escape patterns remain

For completeness the periodic escape words can be classified without
a catalogue search. Let p be a common eventual period, put
M=2^delta-3, and define the rational numbers

```
x_n=R_(n,p)/(1-2^p),              -1<=x_n<=0.
```

Their defining periodic words give x_n=c_n+2x_(n+1). Equation (6)
also gives

```
x_n=d_n+3x_(n+delta).
```

One direct verification is to put y_n=x_n-d_n-3x_(n+delta).
Then (6) implies y_n=2y_(n+1); since y is periodic, it vanishes.
Combining the two x-identities and using P_n=R_(n,delta) yields

```
v_n=-M*x_n=3P_n-2^delta*d_n in {0,...,M},
v_(n+1)=(v_n+M*c_n)/2,
c_n = v_n mod 2.                                       (12)
```

The endpoints v=0,M are fixed and give exactly the constant escape
patterns excluded in Section 6. On the interior residues the map is
multiplication by the inverse of 2 modulo M. For delta=3, M=5 and
there is one four-cycle. For delta=4, M=13 and there is one
twelve-cycle. The following explicit cycles exhaust all interior
residues, so no multiplicative-order theorem is being imported.

| delta | v-cycle, starting at 1 | binary escape word c | ternary escape word d |
| --- | --- | --- | --- |
| 3 | 1,3,4,2 | 1100 | 1012 |
| 4 | 1,7,10,5,9,11,12,6,3,8,4,2 | 110111001000 | 222101000121 |

The words repeat, with an arbitrary common cyclic phase. The d-digits
are obtained from `d_n=(3v_(n+delta)-v_n)/M`; each lies in {0,1,2}.
Thus these are exactly the remaining possibilities for the maximal
transition labels. They are **not** constructions of section graphs:
the other children and the actual sequence values still have to satisfy
all radix identities and the Collatz root equations.

## 8. A strict depth gain for the nonescaping binary children

The periodic patterns of Section 7 also force bounded returns. The
proof below retains the entire finite initial set and all jumps into it.
Take a common period p and a stable starting depth N. Write

```
A_n=E_(1-c_n)(q_n),
y_n=(x_n-(1-c_n))/2,
j_n=(d_n+2+c_n-3c_(n+delta))/2.
```

The six radix identities, applied to the nonescaping binary child of
T_(d_n)(q_n)=q_(n+delta), give

```
A_(n+delta)=T_(j_n)(A_n),
y_n=j_n+3y_(n+delta),             j_n in {0,1,2}.          (13)
```

For the first equality, the affine residue is
`d_n+3(1-c_(n+delta))`. Its parity is 1-c_n by (6); its quotient
after removing that parity bit is precisely j_n. The second equality
follows by substituting x_n=d_n+3x_(n+delta).

Every y_n is an odd integer divided by 2M: its numerator, up to sign,
is v_n+M(1-c_n), which is odd because M is odd and c_n=v_n mod 2.
Every x_a has denominator dividing the odd integer M. Therefore

```
y_n != x_a                     for all stable n,a.       (14)
```

Consider a block of p successive ternary digits
j_n,j_(n+delta),...,j_(n+(p-1)delta), applied to an arbitrary
tail state q_a. It cannot follow maximal-height ternary edges at all
p steps. If it did, the state indices would be a,a+delta,...,
a+p*delta, and j_(n+t*delta)=d_(a+t*delta) at every step.
Iteration of (13) and of the corresponding x-identities, together
with periodicity, would then give

```
y_n-x_a=3^p*(y_n-x_a),
```

contradicting (14).

Let U_n denote this p-step ternary operator and put Q=p*delta.
If its trajectory stays in the stable tail, one step increases depth
by at most delta-1 and all others by at most delta. If it enters the
finite earlier set, all its remaining at most p transitions have
uniformly bounded depth: there are finitely many such states and words.
The same finite bound covers a starting state in that set. Hence one
constant H gives, for every s in S and stable n,

```
rho(U_n(s)) <= max(H,rho(s)+Q-1).
```

Since A_(n+Q)=U_n(A_n), iteration in the Q residue classes yields

```
rho(A_n)<=lambda*n+B,           lambda=(Q-1)/Q<1,         (15)
```

with one constant B. This is still a growing bound; the next step
converts it into an actual contraction on the return operators.

## 9. Every nonmaximal ternary edge contracts depth

Fix stable n and j!=d_n, and suppose T_j(q_n)=q_m is in the stable
tail; a child in the finite earlier set already has bounded depth.
There is no alignment of its rational binary escape centers:

```
x_n != j+3x_m.                                          (16)
```

Indeed equality would imply v_n=3v_m-Mj. The critical equality
gives v_n=3v_(n+delta)-M d_n. Since 3 is invertible modulo M=5
or 13 and all v-values lie in {1,...,M-1}, it follows that
v_m=v_(n+delta), then j=d_n, a contradiction.

All x-values have odd denominator and satisfy
`x_a=R_(a,k) mod 2^k` for every k: this means that the numerator
of x_a-R_(a,k), after an odd common denominator is chosen, is
divisible by 2^k. A nonzero rational with odd denominator cannot be
divisible by every power of two. Thus (16) implies that for some k,

```
u=(3R_(m,k)+j) mod 2^k != R_(n,k).
```

Follow the k critical binary edges from q_m. Commuting these actual
affine substitutions back through T_j gives

```
q_(m+k)=T_t(E_[u,k](q_n)),
t=floor((3R_(m,k)+j)/2^k) in {0,1,2},
E_[u,k](f)(z)=f(2^k*z+u).
```

Let ell<k be the first binary digit at which u differs from the
critical word at q_n. Its binary path follows ell critical edges,
then reaches A_(n+ell), then makes k-ell-1 further binary steps.
There is a global finite C_0 such that
rho(T_t(s))<=rho(s)+C_0 for every s in S and t: use delta on the
stable tail and absorb the finite earlier set. Consequently

```
m+k <= rho(A_(n+ell))+(k-ell-1)+C_0,
m <= lambda*(n+ell)+B-ell-1+C_0
  <= lambda*n+B+C_0.
```

No assumed bound on a backward jump was used. The first differing
digit ell may depend on the phases; its contribution has the favorable
coefficient lambda-1. Including the bounded earlier-set cases gives
one constant C_1 such that

```
rho(T_j(q_n))<=lambda*n+C_1       whenever j!=d_n.        (17)
```

## 10. Bounded returns force equality of whole sections

Revisit U_n from Section 8. A trajectory staying in the stable tail
must include a nonmaximal ternary edge. Before its first such edge,
depth grows by at most delta per step; that edge obeys (17); the
remaining at most p-1 steps have bounded additive depth increase.
If a trajectory enters the finite earlier set, its remaining depth
is uniformly bounded as before. Enlarging one constant C_2 therefore
gives the genuine contraction

```
rho(U_n(s))<=lambda*rho(s)+C_2       for every s in S.    (18)
```

Iterate A_(n+Q)=U_n(A_n). The depths remain bounded because
lambda<1. Thus all sufficiently late A_n belong to a fixed finite
subset of S. Moreover U_n depends only on n modulo p, and Q is a
multiple of p. In each residue class modulo Q this is iteration of
one deterministic operator on a finite orbit. The A_n sequence is
therefore eventually periodic. Choose an eventual period P that is
also a multiple of p.

Both remaining binary escape patterns contain a one. Hence q_n(0)
can be evaluated by following its initial zero escape digits until
the next c_(n+t)=1, within fewer than p steps, when it equals
A_(n+t)(0). These zero outputs consequently also have period P.
Finally the exact recursion

```
q_n(2z+c_n)=q_(n+1)(z),
q_n(2z+1-c_n)=A_n(z)
```

proves q_(n+P)(z)=q_n(z) by induction on z, simultaneously for all
sufficiently large n. The case z=0 was just checked; an escaping
digit reduces every positive input to a smaller integer, and a
nonescaping digit uses the equality of entire A-sequences.

This contradicts the distinct minimum depths n and n+P. Neither
periodic pattern is possible. Therefore no nonconstant invariant has
kappa_h(D)=D+O(1).

## 11. Scope and the remaining full-goal obligation

For a nonconstant invariant, every binary layer is nonempty, so
kappa_h(D)-(D+1) is a nonnegative nondecreasing integer. Excluding
a bounded excess proves that this excess tends to infinity. It does
not supply a fixed positive fractional improvement over D, let alone
an unbounded ratio kappa_h(D)/(D+1). In particular growth such as
D+sqrt(D) is not excluded by this conclusion alone.

The proof uses the full invariant interface through positive-section
closure, the depth-four ternary bound, and infinitude of both pure
kernels. The Collatz root equations are retained in those prior
theorems. It does not assert that periodic escape labels by themselves
make a sequence automatic: the explicit return control in Sections
8–10 is the required additional argument.

### Seven-field assessment

1. **Objects.** The minimum-depth binary kernel graph of a hypothetical
   invariant with additive-error minimal growth, its exact joint section
   action, and every return to an older state.
2. **Structural gain.** An eventual binary ray is impossible. Its
   maximal transitions first reduce to finitely many periodic phases;
   exact radix swaps then force a contracting depth bound on every
   return block and equality of entire sections.
3. **Translated unresolved gap.** Extend beyond an eventual single
   new binary state per layer. Unbounded additive excess is weaker than
   the full unbounded-ratio goal; recurrent layers with several states
   have not been controlled by this argument.
4. **Worked example.** Section 6 excludes constant extreme tails
   using A_(n+delta)=T_1(A_n), the second radix identity (9), and
   whole-sequence equality. This is a conditional structural calculation,
   not an exhibited invariant.
5. **Known-cycle controls.** Generalized-map periodic colorings fail the
   two-base infinitude hypothesis. The binary-only V005 and V006 controls
   have no supplied ternary closure with the required depth bound.
6. **Cheapest meaningful next test.** Independently audit the finite
   phase argument in Sections 8–10, then identify which step admits
   several new states per layer without assuming bounded backward jumps.
7. **Genuinely intermediate milestone.** Excluding kappa_h(D)=D+O(1)
   proves an unbounded additive excess. This remains weaker
   than the active requirement that kappa_h(D)/(D+1) be unbounded.

The eventual-ray constancy implication has written independent review,
including its last phase. Full quantitative completion, novelty, and
formal verification are not claimed.
