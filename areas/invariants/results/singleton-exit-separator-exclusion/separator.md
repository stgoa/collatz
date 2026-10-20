# V007 — A singleton separator cannot support the full invariant

**Status: written elementary proof; [independent review passed](INDEPENDENT_REVIEW.md).** This is a
bounded special case of the section-graph question. It does not prove the
active unbounded-linear-ratio target. Its main theorem is generic for exact
binary/ternary section graphs under an explicit infinitude hypothesis; the
full Collatz identities supply that hypothesis, rather than being replaced
by a weaker return loop.

**Dependency clarification (V008):** the generic theorem under (I) is
elementary. Its Collatz application derives (I) through V005/V004 and
therefore uses the published Cobham theorem. The written application is
distinct from the Lean lane's assembly with Cobham as an explicit input.

## 1. Objects, hypotheses, and claim

Use the five transitions and six identities of
[V006/graph_interface.md](../quadratic-separation-digit-count-sections/graph_interface.md):

```
E_i(s)(n)=s(2n+i),     i=0,1,
T_j(s)(n)=s(3n+j),     j=0,1,2,
T_j(E_i(s))=E_l(T_k(s)) whenever 2j+i=3l+k.
```

Vertices are entire sequences. Thus unequal vertices must differ at some
integer; two differently named but identical sequences are one vertex.
In particular, `o(E_0(s))=o(T_0(s))=o(s)`, with `o(s)=s(0)`.

**Infinitude hypothesis (I).** Every reachable vertex has infinitely many
distinct binary descendants and infinitely many distinct ternary descendants.
Descendants include the vertex itself and use only the indicated radix.

**Theorem.** Under (I), there is no finite nonempty set U of reachable
vertices and vertex q outside U such that every transition from U lands in
`U union {q}` and some transition from U lands at q.

This is a finite forward interior with a single exit. It includes a
singleton distance layer: if `B_d` is the ball of radius d and
`B_(d+1) minus B_d={q}`, take `U=B_d`.

For a nonconstant finite-valued Collatz invariant, V005 excludes automaticity
of every positive binary section. Section 1.1 below excludes ternary
automaticity of every such section, using the full three scalar identities
and V005 reconstruction. V004 represents every joint section as a positive
binary section. Therefore (I) applies to the whole joint graph of
`b(n)=h(2n+1)`.

This dependence is substantive: the proof below does **not** derive (I)
from an arbitrary graph, infinitude of its total vertex set, or a reduced
Collatz loop. In particular, it does not silently assume every vertex can
return to the root.

### 1.1. Reverse closure: ternary automaticity also forces constancy

The three full scalar identities are, for every n>=0,

```
b(3n)=b(4n),   b(3n+2)=b(2n+1),   b(4n+2)=b(n).
```

Put `c(n)=b(2n)`. If b has finite ternary kernel, c does too: write
`2r=q*3^a+s`, with q in {0,1} and `0<=s<3^a`; then
`c(3^a n+r)=f(2n+q)` for the ternary section
`f(n)=b(3^a n+s)`. There are only finitely many such functions.

The union of the ternary kernels of b and c is binary-closed. To verify
this, let a>=0, `0<=r<3^a`, i in {0,1}, and `v=3^a i+r`, so
`0<=v<2*3^a`. Its four cases are

```
E_i[b(3^a n+r)] = c(3^a n+v/2),                       v even,
E_i[b(3^a n+r)] = b(3^(a+1)n+(3v+1)/2),               v odd,
E_i[c(3^a n+r)] = b(3^a n+(v-1)/2),                   v odd,
E_i[c(3^a n+r)] = b(3^(a+1)n+3v/2),                   v even.
```

The first line is the definition of c; the other three use respectively
the second, third, and first scalar identities. Every offset is
nonnegative and strictly smaller than its displayed power of 3.
Consequently finite ternary kernel for b implies finite binary kernel
for b. The odd-part extension then has finite binary kernel, and V004
makes h constant.

Now suppose a positive binary h-section g has finite ternary kernel.
V005's exact reconstruction provides a power `M=3^j` and, for each
`0<=t<M`, fixed positive integers A_t,B_t with

```
b(Ml+t)=g(A_t l+B_t),        l>=0.
```

Fixed affine sampling preserves finite ternary kernel directly: for
`f(n)=g(An+B)`, write `Ar+B=q*3^a+s`, `0<=s<3^a`; then
`f(3^a n+r)=g_s(An+q)` where g_s is a ternary section of g and
`0<=q<=A+B`. These choices range over a finite set. Interleaving the
finitely many displayed sequences modulo `M=3^j` also preserves finite
ternary kernel: after j ternary digits one of them is selected, and
there are only finitely many shorter sections. Thus b has finite
ternary kernel, which we have just shown forces h constant.

For a nonconstant invariant every positive binary section therefore has
infinite kernels in **both** bases. This proves the full hypothesis (I)
used below, without assuming regularity of the actual component coloring.

## 2. A single exit propagates, unless one radix already closes

Suppose U,q are as above and put `V=U union {q}`. If both binary children
of q are in V, then V is binary-closed, so q has finite binary kernel.
Likewise, if all ternary children are in V, q has finite ternary kernel.
Both alternatives contradict (I).

Choose s in U with an edge to q. Define indicator polynomials

```
X(z)=x_0+x_1 z,             x_i=1 iff E_i(s)=q,
Y(z)=y_0+y_1 z+y_2 z^2,     y_j=1 iff T_j(s)=q,
A(z)=a_0+a_1 z,             a_i=1 iff E_i(q) is outside V,
B(z)=b_0+b_1 z+b_2 z^2,     b_j=1 iff T_j(q) is outside V.
```

A and B are nonzero by the previous paragraph. At least one of X,Y is
nonzero by the choice of s. The six radix identities imply

```
X(z) B(z^2) = Y(z) A(z^3).                         (1)
```

For the coefficient at `z^(2j+i)=z^(3l+k)`, both sides say that the
common two-step vertex is outside V. A first step into U cannot leave V
on its second step. A first step to q leaves V precisely when the second
step is marked by A or B. There is one digit pair for each exponent, so
no coefficient multiplicities are suppressed. Since the polynomials have
nonnegative coefficients, (1) also proves X and Y are both nonzero.

We claim A has exactly one nonzero coefficient. If A has two, then
`A=1+z`. If X has one nonzero coefficient, the support of the left side
of (1) has one parity, whereas every nonzero term of Y contributes
opposite parities at exponents k and k+3 on the right. This is impossible.
Thus X also has two and equals `1+z`. Divide (1) by `1+z` to obtain

```
B(z^2)=Y(z)(1-z+z^2).
```

The coefficients at z and z^3 give `y_1=y_0` and `y_1=y_2`.
Nonzero Y therefore equals `1+z+z^2`, and B has all three coefficients
equal to 1. At s, every first transition then lands at q; the six radix
identities identify all five children of q with one common vertex p.
For example they connect T_0(q) to E_0(q), T_1(q) to both E_0(q) and
E_1(q), and T_2(q) to E_1(q).

But if all five children of q equal p, then for every m>=0,

```
p(m)=q(2m)=p(floor(2m/3)).
```

The first equality uses E_0(q)=p; the second reads 2m by its ternary
quotient and uses all three T-children equal to p. For m>0 its new index
is strictly smaller. Induction makes p, and hence q, constant, again
contradicting (I). This proves the claim.

Let c be the unique escaping binary digit and `p=E_c(q)` its target.
Every escaping ternary child also equals p: choose any marked x_i=1
and any marked b_j=1 in (1). The corresponding right pair must have
`y_k=1,a_l=1`, so l=c and the actual radix identity reads
`T_j(q)=E_c(q)=p`.

Consequently every transition from V lands in `V union {p}`, with p
outside V, exactly one binary digit at q escapes to p, and at least one
ternary digit at q escapes to p. This proves propagation. It carefully
distinguishes a unique new vertex from a unique escaping binary digit;
the latter needed the preceding polynomial argument.

## 3. An infinite one-vertex extension has only two possible tails

Apply Section 2 repeatedly. It produces pairwise distinct vertices
`q_0=q,q_1,q_2,...`, where, on putting

```
V_n=U union {q_0,...,q_n},
```

all transitions from V_n land in `V_n union {q_(n+1)}`. There is one
binary escape digit `c_n in {0,1}` at q_n and a nonempty ternary escape
set `D_n subset {0,1,2}`; all those escaping transitions land at q_(n+1).
Other transitions at q_n land in V_n.

At q_(n-1), n>=1, consider which two-step radix words land outside V_n.
Their first step must land at q_n and their second must escape from q_n.
The six identities give the equality of integer residue sets

```
c_(n-1) + 2 D_n = D_(n-1) + 3 c_n.                (2)
```

In particular, all |D_n| equal a fixed positive integer m. The left side
of (2) has one parity, so every D_(n-1) has one parity. This holds for
every index n-1>=0. A subset of {0,1,2} of size at least two and one
parity must be {0,2}. Thus m>=2 would force every D_n={0,2}; then the
left side of (2) has width 4 and the right side width 2, impossible.
Therefore `D_n={d_n}` for one digit d_n at each n.

Equation (2) now reads

```
c_(n-1)+2d_n=d_(n-1)+3c_n.                        (3)
```

Set `t_n=d_n-c_n`, initially in {-1,0,1,2}. Then
`t_(n-1)=2t_n-c_n`. For n>=1, the cases t_n=-1 and t_n=2
would give respectively t_(n-1)=-3 or 4, impossible. Thus
`t_n in {0,1}` for n>=1. For n>=2, this recurrence forces either

```
(c_n,d_n)=(0,0) at every n>=2,
```

or

```
(c_n,d_n)=(1,2) at every n>=2.
```

Indeed t_(n-1)=0 forces t_n=0,c_n=0,d_n=0; t_(n-1)=1
forces t_n=1,c_n=1,d_n=2. The choice then persists.

## 4. Both tails collapse to finitely many entire sequences

Fix N=2, so one of the two descriptions above holds for every n>=N.
In either case T_1 is a nonescaping transition at every tail vertex.
In particular, `V_N` is T_1-closed: each vertex in V_(N-1) sends every
transition into V_N, and `T_1(q_N)` lies in V_N. This is the finite
closure actually used below. It does not assert reverse closure of V_N,
closure under the other four transitions, or impossibility of leaving
after a later change of digit.

### Zero escape tail

Here `E_0(q_n)=T_0(q_n)=q_(n+1)`. Put `A_n=E_1(q_n)`, which lies in V_n.
The radix identity for residue 3 gives

```
A_(n+1)=E_1(T_0(q_n))=T_1(E_1(q_n))=T_1(A_n).
```

Since A_N is in the finite T_1-closed set V_N, the sequence of vertices
A_n is eventually periodic: there exist M>=N and p>=1 with
`A_(n+p)=A_n` for every n>=M. The outputs o(q_n) are all the same for
n>=N, because E_0 preserves the output at zero.

For m>0 write `m=2^v(2u+1)`. Reading its first v zero digits and then
one digit gives

```
q_n(m)=A_(n+v)(u).
```

For n>=M, this and the equality at m=0 show
`q_(n+p)(m)=q_n(m)` for every integer m>=0. These entire sequences are
equal, contradicting the pairwise distinct q vertices.

### Maximal-digit escape tail

Here `E_1(q_n)=T_2(q_n)=q_(n+1)`. Put `A_n=E_0(q_n)`. The radix
identity for residue 2 gives

```
A_(n+1)=E_0(T_2(q_n))=T_1(E_0(q_n))=T_1(A_n).
```

The same finite T_1-closure makes A_n eventually periodic with parameters
M,p as above. For any m>=0, put `v=v_2(m+1)` and write
`m=2^(v+1)u+2^v-1`, u>=0. Reading v one digits followed by a zero gives

```
q_n(m)=A_(n+v)(u).
```

This formula includes m=0 and numbers whose written binary digits are all
ones: a final zero may always be appended because the output at zero is
preserved. Thus again `q_(n+p)=q_n` as entire sequences for n>=M,
a contradiction. This completes the theorem.

## 5. Exact gain and remaining finite-width problem

For a nonconstant invariant, every joint layer is nonempty: an empty
layer would make the finite preceding ball closed under all transitions,
contrary to (I). The theorem excludes a layer of size one. Therefore

```
|J_D(b)| >= 2D+1,       D>=0.                       (4)
```

Combining this with V004/V005 depth distortion gives only
`kappa_h(1+4D)>=2D+1`. This is a linear lower bound, and **does not**
prove that `kappa_h(D)/(D+1)` is unbounded. Linear growth with a larger
coefficient would give infinitely many layers of some bounded size K;
the present theorem handles K=1 only.
After the factor-four depth conversion this does not even improve the
generic binary lower bound `kappa_h(D)>=D+1` from an infinite binary
kernel. Its gain is the exclusion of a precise graph topology.

The precise gain is structural: the smallest possible recurring finite
bottleneck is excluded without assuming that the graph contains a
digit-count section. Larger separators can carry several escaping
states. The Boolean product in (1) then becomes a system retaining
which boundary state each digit reaches; equality of supports alone
does not identify the resulting whole sequences. No classification of
those multi-state systems is claimed here.

## 6. Seven-field assessment

1. **Objects.** The exact joint binary/ternary section graph, a finite
   forward interior U with one exit q, all five radix transitions, their
   six reorder identities, zero outputs, and whole-function equality.
2. **Structural gain.** Such a singleton exit is incompatible with
   infinite kernels in both bases at every reachable vertex. The proof
   retains all possible returns into the finite interior. It forces the
   escape digits and then a finite T_1 orbit, rather than postulating
   a ray classification for arbitrary linear graphs.
3. **Translated unresolved gap.** Excluding every fixed finite separator
   size K, or a different argument controlling all possible linear
   coefficients. The singleton proof does not supply that step.
4. **Worked example.** If every root child lies in {b,q}, U={b} is the
   simplest special case. Under the full Collatz root equations an even
   shorter argument works: if E_0b=b, then E_1b=b; otherwise q=E_0b,
   `E_1q=b`, and `E_0q=T_0b in {b,q}`, so {b,q} is binary-closed.
   The theorem above applies equally to a singleton exit at any depth.
5. **Known-cycle controls.** The d=5 and d=61 divisibility colorings
   satisfy the universal radix identities but have finite kernels, so
   they fail (I). Their named d=1 scalar identity failure was checked in
   V006. The present proof does not falsely remove those cycles. The
   reduced binary N11 control has no verified linear joint graph and
   cannot be imported as a counterexample to the five-transition theorem.
6. **Cheapest meaningful next test.** Retain boundary-state labels in
   the two-exit analogue of (1) and test whether its radix equations
   force a finite orbit, or exhibit an exact surviving boundary system.
   This is a bounded structural calculation, not a large automaton scan.
7. **Genuinely intermediate milestone.** The written arbitrary-depth
   singleton-exit exclusion. It is stronger than the first-layer lemma,
   weaker than the active all-coefficients growth target, and does not
   assume regularity of the hypothetical nonabsorbing set.

## 7. Claim and verification boundaries

All arguments above are symbolic and use finite sets of whole sequences.
No finite prefix comparison is substituted for their equality; no large
search, imported growth theorem, new historical verifier run, or formal
Lean verification is asserted. Correctness is separate from novelty.
The reverse-closure argument in Section 1.1 is part of the dependency
chain for the Collatz corollary and must accompany that use.

The main proof is a forward-closure argument. Having every interior
vertex reach q by some pure-radix path is compatible with it, but neither
that reachability nor a reverse-closed cone is assumed or used. In
Section 4 the single transition T_1 preserves V_N; trajectories using
other transitions may leave and return, and are retained in the exact
section identities and binary evaluations.
