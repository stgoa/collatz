> **Work in progress (committed 2026-10-19 at the owner's request).** This is ChatGPT's uncommitted C014 draft, preserved as it was left in the working copy when that lane paused (files dated 05:06–05:11). It has no REPORT.md and was not reviewed or verified, so treat every claim in it as unverified.

# C014 — Exact limits of a common partition for compatible arcs

**Status: written elementary structural obstruction, with an infinite
family of actual positive generalized cycles.** This note tests two
specific ways of extending C013's shared-background representation.
It proves neither a new denominator exclusion nor an impossibility
theorem for overlapping-arc methods. The clock is raw positive odd-only,
without an absorber. No novelty or formal-verification claim is made.

## 1. A partition preserved by the rotation can require every cut

Let `w=(a_0,...,a_(m-1))` be a cyclic word, and compare it with its
rotation by h positions. Assume the mismatch set

```text
S={i mod m : a_i != a_(i+h)}
```

is nonempty, with size s. Let `C=S+1` be the cuts immediately after
the mismatches, as in C012. Suppose we refine these cuts to one common
partition into chronological cyclic intervals, and require translation
by h to permute the resulting intervals. Its cut set F must satisfy

```text
C subset F,                 F+h=F.
```

Conversely these two conditions give such a partition: translation
preserves cyclic order and takes consecutive cut points to consecutive
cut points. Put `d=gcd(m,h)`, and let k be the number of residue classes
modulo d met by C. The unique smallest possible refinement is

```text
F_min = union_(j in Z) (C+jh),
|F_min| = (m/d) k.                                      (1)
```

Indeed the orbits of addition by h are exactly the residue classes
modulo d, each containing m/d points. Formula (1) follows by taking
the union of all orbits meeting C. Each corresponding orbit meeting S
has at least two letter transitions, so `2k<=s`; this upper bound on
k does not bound m/d.

In particular, if h is coprime to m, every nonempty mismatch set forces

```text
F_min=Z/mZ.
```

The aligned partition then consists of m singleton intervals, regardless
of how small s is. Thus there is no bound in s alone on the size of this
literal partition model. The result allows arbitrary alphabets, periods,
and mismatch counts; it does not require positivity or primitivity.

**Scope.** This obstructs the proposed refinement into a disjoint interval
partition permuted by the rotation. A method can instead retain
overlapping intervals, use compressed runs, or use identities without
such a partition. Equation (1) supplies no lower bound on the size or
cost of every possible arithmetic representation.

## 2. Repetition cannot manufacture a nonempty C013 background

Here is an intrinsic criterion for the specific C013 representation.
Let w be a nonconstant word of primitive period m. Allow an arbitrary
cyclic cut and an arbitrary positive repetition of w. Suppose that
displayed word has the form

```text
(U,a_0,U,a_1,...,U,a_(r-1)),
b=length(U)+1,             r>=2,
```

with U nonempty and the one-letter marker word nonconstant.

**Theorem.** Necessarily b is a proper divisor of m. At a suitable cut,
each of the residue columns `0,...,b-2 mod b` is constant; only the
marker column `b-1 mod b` may vary. The primitive marker period is m/b.
Conversely, these column conditions at a proper divisor b of m produce
the representation. Repeating the full word adds no new admissible b.

**Proof.** Let `d=gcd(m,b)`. The length condition `m | rb` gives
`m/d | r`, so the block starts visit every position in their residue
class modulo d. For every offset `0<=i<b-1`, the shared U therefore
forces the letters at positions congruent to that offset modulo d to
be equal.

If d=m, every marker is at the same phase of w, contradicting
nonconstant markers. If d<m and b>d, the b-1 interior offsets contain
a representative of every residue class modulo d. Hence all letters
depend only on their residue modulo d; w would have period d<m.
Primitivity excludes this. The only remaining possibility is
`b=d<m`, proving that b is a proper divisor of m. The common-U
condition is then exactly the stated column condition.

If the marker sequence had a proper period shorter than m/b, the
full word would have a correspondingly shorter period. Conversely
the column condition assembles identical interiors U separated by the
marker letters. The argument already allowed every repetition and cut.
QED.

**Prime-period corollary.** A nonconstant word of prime primitive period
p has no C013 representation with nonempty U and nonconstant markers,
even after repetition and a change of cut. Only the empty-U boundary
representation can apply. Constant markers would instead repeat a
single whole block and are outside C013's finiteness theorem.

This is a coverage obstruction, not a failure of C013's theorem.
It shows why the C013 block-count result cannot be transferred to
arbitrary sparse rotations by merely looking for a different cut or
repeating the word.

## 3. Actual sparse-rotation cycles of every prime period p>=5

The preceding obstructions occur on positive rational cycles with
arbitrarily large normalized minimum, not just on abstract strings.
For each prime `p>=5`, set

```text
A=ceil(p log_2 3)=bit_length(3^p),
u_i=floor((i+1)A/p)-floor(iA/p),      0<=i<p.
```

Then `p<A<2p`, and every u_i is 1 or 2. In fact
`A<=2p-2`, since `(4/3)^p>4` for p>=5, and `A>=p+2`.
Thus both letters remain after replacing the last letter 2 by 3.
Define

```text
w=(u_0,...,u_(p-2),3),
m=p,             A_w=A+1<2p,
D_w=2^(A+1)-3^p>0.                                  (2)
```

The last letter of u is 2 because `floor(A-A/p)=A-2`.
The word w contains the three letters 1,2,3, with a unique 3, and is
primitive. Its intercept at the displayed cut is unchanged:
`C_w=C_u`, since an intercept omits its word's last valuation.

### The minimum rotation distance is exactly three

As p is prime, `gcd(A,p)=1`. Compare the mechanical phases 0 and 1.
Exactly one internal prefix floor changes: its index j satisfies
`jA=-1 mod p`. Hence their valuation words differ at exactly the two
adjacent positions `j-1,j`. Phase 1 is a rotation of phase 0 by the
nonzero h satisfying `hA=1 mod p`.

In fact `j=p-h`. Since `p+2<=A<=2p-2`, its inverse h modulo p is
neither 1 nor p-1, so `2<=j<=p-2`. At j-1, the phase change raises
the original letter 1 to 2; at j it lowers 2 to 1. The edited last
letter of the rotated copy lies at `p-1-h=j-1`, changing that 2 to 3
and retaining the first mismatch. The original edited last position
p-1 is distinct from both existing mismatches and supplies exactly one
new mismatch. The selected rotation of w therefore has mismatch set
`{j-1,j,p-1}`.

For any nonidentity rotation of w, addition by its shift
visits all p positions. Reading the letters along that orbit encounters
all three symbols. A circular list containing three symbols has at
least three transitions. Consequently

```text
rho(w)=3.                                           (3)
```

Here rho is the minimum nonzero rotation Hamming distance. This avoids
using an already excluded two-defect family as the only control.

### Every normalized state exceeds p/18

For any rotation of the original mechanical word u, its j-letter
prefix sum satisfies

```text
P_j > j A/p - 1.
```

Thus every summand in its intercept satisfies

```text
3^(p-1-j) 2^P_j
  > (3^(p-1)/2) (2^(A/p)/3)^j
  >= 3^(p-1)/2.
```

Increasing one valuation cannot decrease any rotated intercept. On the
other hand, `2^A<2*3^p` gives `D_w<3*3^p`. At every phase of w,

```text
C_(rotation(w))/D_w > p/18.                          (4)
```

Put `g=gcd(C_w,D_w)` and `q=D_w/g`. All rotated intercepts have the
same gcd g with D_w, by the one-letter cyclic identity and the fact
that D_w is coprime to 6. Their quotients by g are positive odd integers
and satisfy

```text
3 n_i+q=2^w_i n_(i+1).
```

The oddness of the successor makes each displayed valuation exact.
The resulting raw generalized cycle is primitive because w is
primitive. With L its least odd numerator, (4) says `L/q>p/18`.
In particular q<=L for every prime p>=19. Its total also lies in the
necessary integer-cycle range `A_w<2m`.

At every prime in this family, every nonidentity rotation has coprime
shift, so the partition in section 1 has p singleton blocks. Section 2
excludes every nonempty shared-background representation, including
representations of repeated displays. The simultaneous bounded rho,
unbounded period and unbounded L/q are therefore actual cycle controls
for both coverage failures.

**Denominator scope.** This construction imposes no bound on q. It does
not supply a fixed-q or integer-cycle counterexample, refute the
proposed denominator law in terms of m/rho, or claim a new all-size
q1 exclusion for this family. Its role is to test proposed coverage
and compression steps before any such arithmetic conclusion.

### Small exact example

At p=5, A=8 and

```text
u=(1,2,1,2,2),       w=(1,2,1,2,3),
C_w=319, D_w=q=269, g=1,
states=(319,613,527,925,761).
```

Every arrow has additive parameter 269 and the exact valuation in w.
Rotation by two has mismatch positions 2,3,4, so rho=3. Every
rotation-preserved mismatch-cut refinement has five singleton blocks.
No repetition or cut gives a nonempty C013 background with nonconstant
markers. Larger finite controls are recorded separately by the batch
checker; these finite examples are not the proof of (1)--(4).

## 4. What survives this bounded test

The actual q5, q7 and q13 cycles remain legal: neither theorem is an
assertion that sparse rotations cannot occur. Repeated `(2)` has no
mismatches, is constant, and lies outside both nonempty hypotheses.
C011's two-defect exclusion and C013's shared-background finiteness
remain unchanged.

| Required field | Outcome |
| --- | --- |
| Objects | Actual cyclic words, mismatch cuts, a rotation acting on chronological interval partitions, and the C013 representation under all cuts and repetitions. |
| Structural gain | Exact minimal invariant refinement size, intrinsic divisor/column classification of nonempty common backgrounds, and a positive prime-period family with bounded rotation distance and growing normalized minimum. |
| Translated unresolved gap | General compatible arcs may overlap without forming a small invariant partition, and need not contain one identical nonempty background. Their arithmetic correlations remain to be estimated directly. |
| Worked example | The primitive q269 five-cycle and the prime-period family (2). |
| Known-cycle controls | All positive generalized cycles remain allowed; the family itself consists of actual raw odd cycles, with q<=L for p>=19. Trivial repetitions have zero mismatch count. |
| Cheapest meaningful next test | Test an explicitly overlapping representation or identity on this family before charging its complexity only to mismatch count. Retain its numerical gcd at the true reduced q. |
| Intermediate milestone | A relative cancellation bound for compatible overlapping arcs whose cost is controlled by mismatch count, without assuming the partition or common-background reductions refuted here. This note does not establish that bound. |

No new numerical cycle record or comparison win over published cycle
exclusions follows. The mechanical prefix estimates are elementary
instances of the already persisted R71/C004 construction; the novelty
of the structural corollaries is not claimed. This batch lane rejects
two concrete reduction steps while leaving quantitative methods using
the full overlap information open.
