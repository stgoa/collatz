# An infinite known set from a finite supplied current

**Status: written conditional construction and uniform arithmetic count.**
The input is a finite exact current for absorption through a specified cutoff
N. The construction certifies any requested member of an explicit infinite
set, including arbitrarily large members. It does not prove that an unknown
orbit enters this set, and it does not imply universal Collatz convergence.
No novelty, formal verification, or human review is claimed.

Use positive odd integers, the odd-only Syracuse clock, and absorption at1.
The measure delta1 and current row at1 are killed. Let U_N assign weight1 to
each odd integer3<=q<=N. The count theorem below holds for every pair of
integers X>=N>=8; divisibility of N by8 is unnecessary for this local result.

## 1. The known elementary closure is infinite

The [complete elementary-bridge normal form](../bridge_normal_form/BRIDGE_NORMAL_FORM.md)
defines the canonical set B and the map nu. Its components are exactly

```
C_q={F^k(q),F^k(2q+1): k>=0},    q in B,
F(x)=4x+1,
B={q=1 mod8} union {q=2^a t-1: a>=2, t=-3^a mod4}.
```

All integers here are positive and odd. Every q in B is the unique smallest
element of its component. For every odd x the normal-form constructor returns
a finite integer current J_x with

```
div J_x=delta_x-delta_nu(x).                            (1)
```

Define

```
I_N={x>0 odd: nu(x)<=N}
   = union_(q in B, q<=N) C_q.                         (2)
```

The equality follows from the complete component classification, so the
display includes every member of this elementary closure. It contains all
positive odd integers at most N because nu(x)<=x. It is infinite because
even the component C_1 contains two infinite F-rays.

Suppose a finite integer current H satisfying `div H=U_N` is supplied.
H may have either sign. For any requested x in I_N, put q=nu(x). The
finite nonzero-row graph of H contains an absorbing path from q when q>1.
Indeed a finite weak component disjoint from1 has total divergence zero;
it cannot contain any of the positive U_N sources. A finite functional
component containing the absorbing vertex1 has a directed path to1 from
each of its vertices. This argument needs no global exclusion of cycles.

Let H_q be the nonnegative path current from q, or zero if q=1. Then

```
div(J_x+H_q)=delta_x.                                  (3)
```

Although this summed current can be signed, the same finite-component
argument extracts an actual nonnegative absorption path for x from its
nonzero-row graph. Its edges are a subset of the supplied graph together
with the explicitly constructed bridge edges. The constructor therefore
follows no unknown outer future. All boundary terms, including target1,
are handled exactly.

This gives a finite certificate for each requested member of an infinite
set; it is not one finite current whose divergence is an infinite measure.
Any finite nonnegative integer source supported on I_N can be certified
by summing its individual currents, with all source multiplicities retained.
Already supplied absorption paths can be reused as proof inputs.

The bridge size depends on N, not on how high x lies in its F-ray. Its
F-root is q or2q+1, at most2N+1. An F-sibling comparison uses at most two
current rows; the possible R23 bridge uses two explicit prefixes of length
`a<=floor(log2(2N+2))`. Thus at most

```
2*floor(log2(2N+2))+2                                  (4)
```

bridge rows suffice, before cancellations, independently of x. Integer
bit length and the size of the supplied current still affect computation.

## 2. A single affine sequence for each canonical base

Interleave the two F-rays by defining, for s>=0,

```
f_s(q)=2^s q+beta_s,
beta_s=(2^s-1)/3          when s is even,
beta_s=(2^(s+1)-1)/3      when s is odd.                (5)
```

The offsets are integers. For s=2k this is F^k(q), and for s=2k+1 it is
F^k(2q+1). The complete normal-form theorem ensures that every pair (q,s),
q canonical, represents a distinct integer. Consequently the desired band
count is

```
B_N(X)=#{odd x in [X,2X): nu(x)<=N}
      =sum_(s>=0) #{q in B: 1<=q<=N, X<=f_s(q)<2X}.    (6)
```

Only O(log N) levels can contribute, uniformly in X>=N. If a level has a
member, then beta_s/2^s is between0 and2/3, so

```
X/(N+2/3) <= 2^s < 2X.
```

Their exponent range has length O(log(N+1)). `band_count` evaluates (6)
by exact canonical progression counts, with inclusive and strict endpoints
implemented using `(X-1-beta_s)//2^s` and `(2X-1-beta_s)//2^s`.
It has O(log^2 N) arithmetic-count complexity independent of X; the bit
cost of those arithmetic operations does depend on X.

## 3. Exact telescoping improves the uniform error to O(log N)

Let K(Y) count canonical positive integers at most Y. For any real t, define

```
K_N(t)=#{q in B: 1<=q<=N, q<=t},
A_s(t)=K_N((t-1-beta_s)/2^s),                          (7)
```

where t will be an integer X or2X. Thus A_s(t) counts the level-s members
strictly below t. Every sum below is finite because A_s(t)=0 for all
sufficiently large s.

Reindexing (6), and using X>=N, gives the exact identity

```
B_N(X)=K(N)+sum_(s>=1) [A_s(2X)-A_(s-1)(X)].         (8)
```

Indeed the first unsummed term is `A_0(2X)=K_N(2X-1)=K(N)`.
Crucially, (8) telescopes the exact count before any replacement by a
leading density.

The two real arguments in the s-th correction differ by

```
d_s=(1+2 beta_(s-1)-beta_s)/2^s
   = 1/3+2/(3*2^s),        s even;
   =-1/3+2/(3*2^s),        s odd.                    (9)
```

For s>=1, `|d_s|<=1/2`; at s=1 the difference is zero. An interval of
length at most1/2 contains at most one integer, so every correction in
(8) has magnitude at most1.

It remains to bound the number of potentially nonzero corrections without
introducing a dependence on log X. Put

```
c_s=(1+beta_s)/2^s,      1/3<c_s<=1.
```

The two arguments in (8) are `2X/2^s-c_s` and
`2X/2^s-c_(s-1)`. If their counts differ, the interval between them contains
some canonical integer q with1<=q<=N, with the lower endpoint excluded.
Since both c's are positive and at most1, this forces

```
2X/(N+1) < 2^s < 2X.                                 (10)
```

Let L=floor(log2 N). The ratio between the endpoints in (10) is N+1,
which is at most2^(L+1). An open interval with this ratio contains at most
L+1 distinct powers of2. Therefore

```
|B_N(X)-K(N)| <= L+1.                                 (11)
```

The normal-form count theorem gives

```
|K(N)-N/4| <= floor(log2(N+1))+1/2 <= L+3/2.
```

Combining this with (11) proves the explicit, uniform bound

```
|B_N(X)-N/4| <= 2*floor(log2 N)+3,
for every integer X>=N>=8.                            (12)
```

The extra half unit in this displayed bound is harmless rounding. The
argument establishes O(log N), stronger than separately replacing each
level count by its density, which would only yield O(log^2 N).
`telescope_count` implements (8), checks the active range (10), and returns
all nonzero signed corrections for inspection.

## 4. Interpretation and limits

There are ceil(X/2) odd integers in the integer band [X,2X). Equations
(11)-(12) therefore imply the uniform counting proportion

```
B_N(X)/ceil(X/2)=N/(2X)+O(log N/X).                    (13)
```

At X=HN this has leading term1/(2H). This is the density of the explicitly
certified elementary closure in a band, conditional on the supplied lower
current. It describes actual integer membership. It is not an independent
trial probability for an orbit, a proof that every orbit hits I_N, or an
iteration rule for the complementary residual. It also does not describe
the different set obtained by taking a finite forward union of known seeds.

For each fixed N, the set I_N even has bounded absorption times once the
finite input is supplied. In a component C_q with q>1, the F identities
preserve hitting time, and the selected-partner R23 identity compares two
equal-length prefixes neither of which reaches1 early. All its members
therefore have the same hitting time as q. Every member of C_1 reaches1
within two steps. The bound is the maximum of2 and the finitely many known
canonical hitting times through N. This strengthens the individual
certificate interpretation; it supplies no information about a seed outside
I_N entering that set.

## 5. Reproduction and finite evidence

Run from the repository root:

```
python3 experiments/residual_progress/absorbed_fibers/check_fibers.py
```

The default run is read-only and compares against `fiber_audit.json`.
`--write-receipt` regenerates that receipt. The checks compare three exact
counts: direct band membership for small bands, the level formula, and the
telescope. A fourth independent calculation enumerates canonical bases and
locates the first F-power in the band, without scanning very high intervals.

The receipt covers912 small bands,42 additional boundary bands at odd
cutoffs,18 high bands with multipliers through2^512, and56 actual conditional
current conversions, including F-exponents
128. Supplied absorption through96 is discovered solely for these finite
tests, with a1000-step cap per seed; it is an input assumption in the theorem.
No universal absorption search, orbit-hitting heuristic, or convergence
claim is used.
