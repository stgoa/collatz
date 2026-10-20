# A complete shrinking interface for high odd h, and the exact remaining domain

2026-10-17. **Written arithmetic interface, finite conditional compiler,
and scoped obstruction.** Every odd-h paired run now has one exact tripling
child. All branches with h>=7 strictly shrink, including the formerly
unhandled residues. Some children belong to pair domains whose currents
are still unproved. Low h=3 or5 can expand. This is not a universal pair
constructor or a proof of Collatz. No novelty or human/formal verification
is claimed.

Use the odd-only Syracuse map S, absorbing at1, and killed divergence
`div=I-P`. Write `[x]` for the killed point mass, and

```
P(w)=[3w]-[w],             Q(z)=[6z+1]-[z],
F(z)=4z+1.
```

The elementary canonical set B and normal form nu are those of
[R25](../bridge_normal_form/BRIDGE_NORMAL_FORM.md). All currents below are
finite signed integer currents. A bridge does not assume absorption of its
endpoints. The [R33 rule](../paired_completion/MIXED_SHRINKING_RULES.md)
already handles the special odd-h residue z=3 modulo8. The present result
gives the complete interface, including its failures of decrease.

## 1. Every Q pair has one elementary tripling child

For every positive odd z define

```
u=z       if 3z is canonical;
u=4z+1    if 3z is noncanonical.                       (1)
```

There is an explicit current E_z with

```
div E_z=Q(z)-P(u).                                    (2)
```

**Proof and signs.** For any odd r, exactly one of the following holds:
r is canonical and2r+1 is its selected elementary partner, or r is
noncanonical and2r+1 is itself complementary canonical. This follows
directly from the selected congruence: if r=1 mod8 it is the first case;
if r=5 mod8 it is the second; and for r=2^a t-1 the selected condition
on2r+1 is the opposite of the selected condition on r.

Consequently, if3z is canonical, the elementary current B from6z+1
to3z has divergence `[6z+1]-[3z]`. Set E_z=B. If3z is noncanonical,
the integer q=6z+1 is canonical and3u=12z+3=2q+1 is its selected
partner. Let B bridge3u to q, and let C be the sibling current
`[u]-[z]`, whose divergence is `[u]-[z]`. Then

```
E_z=C-B,
div E_z=[u]-[z]-[3u]+[6z+1]=Q(z)-P(u).
```

Both branches therefore **add** a supplied child current. No sign is
discarded, and every source coefficient can multiply the whole identity.
For z not3 modulo8 the child lies in

```
W={u=5 modulo8} union {u=9 modulo16}.                 (3)
```

Indeed a direct child has3z complementary canonical; then z=1 modulo4,
and its1-mod8 case must be9 modulo16. A nondirect child is always5
modulo8. For z=3 modulo8 the direct child is z itself. The separate
[tripling-domain theorem](../tripling_equivalence/TRIPLING_EQUIVALENCE.md)
classifies W; (2) does not assume any of its unproved universal currents.

## 2. Complete actual odd-h reduction and its exact decrease threshold

Let w>0, w=3 modulo8, and

```
h=v2(3w-1)=2k+3,     k>=0,
C=(3w-1)/2^h,       z=3^k C.
```

The complete R33 prefixes give

```
S^k(3w)=8z+1,       S^(k+1)(w)=4z+1,
S^(k+1)(3w)=6z+1.
```

Append the sibling bridge from4z+1 to z to the right prefix. The
left prefix minus the resulting right current has divergence P(w)-Q(z).
Add (2). The resulting explicit current L_w satisfies

```
div L_w=P(w)-P(u),                                  (4)
```

with the single child (1). Thus J_w=L_w+J_u whenever a child current
is supplied. Formula (4) covers **every** odd h and **every** allowed z.

**Complete decrease classification.**

- The direct child u=z is below w/2 for every k>=0.
- If h>=7 (k>=2), the nondirect child u=4z+1 satisfies u<7w/8.
- For h=3, every nondirect child is `(3w+1)/2>w`.
- For h=5, every nondirect child is `(9w+5)/8>w`.

For the first bound use `z/w<(3/8)(3/4)^k`. For the second, substitute
`w=(2^(2k+3)C+1)/3` and z=3^k C. The inequality8u<7w is exactly

```
17 < [7*2^(2k+3)-96*3^k] C.                         (5)
```

At k=2 the bracket is32, and C>=1. If the bracket at k is D_k,
then D_(k+1)=4D_k+96*3^k, so it increases and (5) holds at every
k>=2. This includes the intercept; it is not merely a slope estimate.
The low-h formulas follow by substituting k=0 or1 into4z+1.

The expanding branches are nonempty infinite actual parameter families:

```
w=64j+19,    h=3, z=24j+7,   u=96j+29;
w=256j+139,  h=5, z=72j+39,  u=288j+157;    j>=0.    (6)
```

In both rows z=7 modulo8, so3z=5 modulo8 is noncanonical. Therefore
applying (4) indiscriminately is not a decreasing recursion. The proved
positive result is the entire high odd-h interface and the direct low-h
branch, with a precise remaining low-h expansion domain. Entering W still
requires a valid constructor there; the new interface does not supply it.

**Prescribed clocks.** Put r=v2(3z+1) and let A=r+1 for a direct
child, A=r+2 otherwise. These are the selected partner lengths used
in (2). If a child merger has clock ell,
`S^ell(3u)=S^(ell+1)(u)`, let L=max(ell,A). After extending the child
equality by L-ell arrows, the elementary identities give
`S^L(6z+1)=S^(L+1)(z)`. Consequently the parent clock is

```
ell_parent=k+1+max(ell,A).                           (7)
```

The maximum cannot be omitted for general residues. Finite signed-current
composition (4) itself does not require a merger clock or future search.

## 3. What the static catalogue can and cannot do

Grant the entire formal R35 catalogue: all elementary identities and
every hypothetical P(v) for v=3 modulo8, in both directions. It includes
no arbitrary forward S arrows. Its complete component label chi is
obtained from nu by the decreasing parents

```
q ->(q-3)/6, q=9 modulo48;
q ->q/3,    q=33 modulo48.
```

**Exact odd-pair scope:** Q(z)'s two endpoints lie in the same component
if and only if z=3 modulo8.

If z=3 modulo8, its left endpoint normalizes to3z and the granted
P(z) connects it to z. Conversely, if z is not3 modulo8 and3z is
canonical, it is complementary canonical. It cannot be an upper vertex
of either displayed parent rule, both of which are1 modulo8. Its
terminal label is3z. If3z is noncanonical,6z+1 is canonical and1
modulo3, hence also a terminal label. In either case the label exceeds
chi(z)<=z. Thus no additional missing residue can be closed by that
whole static catalogue, even using larger intermediate vertices.
This is an operation-set statement, not a nonconvergence theorem.

## 4. A complete critical-seed bijection and finite input compiler

Define the critical set

```
Ccrit={q in B: q=3 modulo4 and q!=2 modulo3}.
```

For every odd z not3 modulo8 put g(z)=nu(6z+1). Then

```
g(z)=3z      if3z is canonical;
g(z)=6z+1    otherwise.                              (8)
```

This is a bijection from the entire missing z domain to Ccrit. Its inverse
is z=q/3 when q=0 modulo3, and z=(q-1)/6 when q=1 modulo3. In the
first case canonical q=3 modulo4 forces z odd and not3 modulo8. In the
second, q=7 modulo12, so z is odd, and q's being canonical forces3z
noncanonical. These observations prove both the inverse formulas and
all domain claims. In all cases z<g(z), indeed z<=g(z)/3.

The elementary current B_z from6z+1 to g(z) gives the exact interface

```
Q(z)=div B_z + [g(z)]-[z].                           (9)
```

For an integer M>=1 define the finite input set

```
I_M={z odd, z!=3 modulo8: g(z)<=M}.                  (10)
```

**Finite compiler theorem.** Supplied finite currents J_z satisfying
`Q(z)=div J_z+rho_z`, rho_z<=0 pointwise, for every z in I_M suffice
to construct an exact nonnegative integer current for U_M. All lower
inputs in the induction are strictly smaller than the seed being certified;
the construction searches no unknown future. Conversely, a supplied
exact U_M current constructs exact Q(z) currents for every z in I_M.

**Proof.** Induct on the positive odd seed x<=M, starting with1.
If x is noncanonical, bridge to nu(x)<x. If canonical x=1 modulo8
and x>1, S(x)<x. If canonical x=3 modulo4 and x=2 modulo3, its
actual predecessor p=(2x-1)/3<x has S(p)=x; subtract its first row
from a supplied absorbing p path. The remaining case is critical:
put z=g^(-1)(x), and combine J_z-B_z with the previously constructed
current for z. Its divergence is `[x]-rho_z`, a nonnegative measure
with positive coefficient at x. Every finite weak component disjoint
from1 has divergence sum zero, so x must lie in the absorbing component.
Its actual forward path uses only existing nonzero current rows and can
be extracted in at most their number of steps. This proves the induction
without a global no-cycle assumption.

Conversely extract the supplied absorbing currents H_g and H_z, and set
J_z=B_z+H_g-H_z. Equation (9) proves its exact divergence Q(z).
Each needed z is at most M/3. Separate root proofs may reuse lower
absorbing paths; this is not simultaneous use of signed annular capacity.
All integer multiplicities are retained under scaling or summation.

It follows that universal Q certificates restricted to z not3 modulo8
are already equivalent to Collatz. This calibrates the unrestricted
missing domain, not the narrower actual odd-h restriction below. The
compiler proves no method for supplying its Q inputs. Its finite input
list is exact for this stated induction, not a claim that every input is
logically indispensable under all possible additional arguments.

## 5. The actual odd-h restriction covers a specified ternary half

Put

```
Zplus={z>0 odd: z=3^k C, k=v3(z), C=1 modulo3}.
```

The actual odd-h P3 branches are in bijection with **exactly Zplus**.
The forward map is the z in Section2. Conversely, for every z=3^k C
in Zplus,

```
w=(2^(2k+3)C+1)/3                                  (11)
```

is a positive integer3 modulo8, w>z, with exact h=2k+3 and the
prescribed z. Integrality follows because2^(2k+3)=2 modulo3 and
C=1 modulo3; the odd numerator factor C gives the exact binary valuation.
For an actual w,3w-1=-1 modulo3 proves C=1 modulo3 and v3(z)=k.
This proves surjectivity and uniqueness without an orbit assumption.

Under (8), the missing part Zplus\{3 modulo8} has precisely the image

```
q in Ccrit, q=0 modulo3, unit3(q)=1;
q in Ccrit, q=1 modulo3, unit3(q-1)=2.               (12)
```

Here unit3(n)=n/3^v3(n) modulo3, for n>0. In the first case z=q/3
has the same ternary unit. In the second write q-1=3^s D, s>=1;
then z=3^(s-1)D/2, whose unit is2D modulo3. This gives (12) exactly.
The complementary critical phases are therefore

```
q=0 modulo3, unit3(q)=2;
q=1 modulo3, unit3(q-1)=1.                           (13)
```

The finite compiler of Section4 cannot simply assume Q inputs for (13)
from the actual odd-h construction. Whether universal existence only on
Zplus, combined with unrestricted valid dynamical arguments, already
suffices for Collatz is not settled here. Nor does classifying (13) imply
its seeds are unabsorbed: for example31 is an omitted critical phase but
is reached from27, a covered critical phase. Full supplied-history reuse
can certify it. The following result scopes a bounded phase-driven test.

## 6. Arbitrarily long growing returns avoid the covered phase

For every r>=1 let

```
K=11r+6,
x=-9221*4513^(-1) modulo2^K,
x=10 modulo27.                                      (14)
```

CRT supplies a complete nonempty class modulo27*2^K. R31 proves that
its first8r ordinary arrows repeat `(1,2,1,1,1,1,2,2)`, all states
are canonical, every noninitial state exceeds x, and its2r run returns
strictly increase with alternating labels(2,2),(5,4).

Every critical run endpoint in this prefix lies in the **omitted** phase
(13). To prove this additional assertion, write the two-return map and
the middle return as

```
Psi(x)=(6561x+9221)/2048,
y=(9x+5)/8.
```

For any integer admissible x, Psi(x)=10 modulo27 and y=4 modulo9.
Thus all pair starts have v3(x-1)=2 and unit3(x-1)=1, and all
middle returns have v3(y-1)=1 and unit3(y-1)=1. They are critical
by their fixed canonical phases. During each pair, the other states are
valuation-one descendants of its start or its middle return, except
the seventh state, which is1 modulo8 and1 modulo3. Their decreasing
inverse-chain minima are respectively those two starts or that seventh
state. They too exceed the initial x. In particular none of the visited
canonical states is an upper image of a Zplus Q rule: the noncritical
states are2 modulo3 or1 modulo8 and1 modulo3, while noncritical upper
images of Q can only be1 modulo8 and0 modulo3.

This gives actual full-weight residual examples on the required rays.
Let e be the CRT residue in (14), put P=27*2^K, and for any B>=K+5
set N=12*2^B. Choose the first x=e modulo P strictly above N. Then

```
N<x<=N+P<=137N/128<9N/8,    x=19 modulo36.           (15)
```

It is an actual coefficient2 complementary R_N root. Every state in its
8r-step prefix remains canonical and above N; even its complete decreasing
valuation-one inverse minimum is above N. No visited state supplies the
covered descending Q substitution.

Thus no fixed number of these forward returns, elementary normalization,
decreasing valuation-one inversion and **descending** covered-phase tests
guarantees closure. The seed changes with r. This does not rule out full
known-history saturation, an upward inverse excursion, cross-pair currents,
other branches, or a construction whose depth depends on the seed. It
does not prove logical insufficiency of universal Zplus certificates.

## 7. Reproduction and next obligation

```
python3 experiments/residual_progress/odd_pair_closure/check_odd_interface.py
```

The default checker is read-only; `--write-receipt` regenerates the receipt
and finite data. It verifies8192 Q interfaces and static labels,2731 actual
odd-h reductions below32768,528 exact Zplus parameter cases through k32,
171 prescribed parent clocks,14 expanding-family examples, and16 actual
weight2 ray witnesses through128 repeated word pairs. It compiles supplied
currents through M64,128,512 in both exact and one-sided modes. Only the
finite test inputs use capped absorption discovery, with a2000-step cap;
the interface and compiler never search an unknown future.

The full M128 Q input currents are stored in `compiler128_inputs.json`;
the extracted exact U128 current is `compiler128_current.csv`.
`odd_interface_audit.json` stores exact counts and hashes. Source-weight2
scaling, finite graph extraction, and all current signs are checked.
These computations test the implementations; the general claims rest on
the arguments above. The parent runs the full repository verification gate.

The next constructive target is the W-domain child currents needed by the
complete high-h interface, together with the low-h expanding interfaces.
The critical bijections locate the remaining inputs exactly. They provide
neither those currents nor a universally decreasing recursion on them.
