# V008 — Two exits introduce a real obstruction to the separator route

**Status: written derivation and exact scoped counterexample;
[independent review passed](INDEPENDENT_REVIEW.md).** The active target remains
`sup_D kappa_h(D)/(D+1)=infinity` for every nonconstant finite-valued
Collatz invariant. This note does not complete it or propose a different
completion standard.

## 1. The boundary equations with destinations retained

Keep the whole-sequence graph and notation from
[V007/separator.md](../V007/separator.md):

```
E_i(f)(n)=f(2n+i),   i=0,1,
T_j(f)(n)=f(3n+j),   j=0,1,2,
T_j(E_i(f))=E_l(T_k(f)) when 2j+i=3l+k.
```

Let U be a finite nonempty set of reachable states. Suppose every
transition from U lands in `V=U union Q`, where
`Q={q_0,q_1}` consists of two distinct states outside U and each is
actually reached from U. Let R be the finite set of children of Q that
lie outside V. Distinct members of R remain distinct entire sequences.

Use the free abelian group with basis vectors e_p, p in R, and put
`pi(p)=e_p` outside V and `pi(p)=0` inside V. For s in U define scalar
polynomials

```
X_(s,alpha)(z)=sum_{i:E_i(s)=q_alpha} z^i,
Y_(s,alpha)(z)=sum_{j:T_j(s)=q_alpha} z^j,
```

and define destination-valued polynomials

```
A_alpha(z)=sum_{i=0}^1 pi(E_i(q_alpha)) z^i,
B_alpha(z)=sum_{j=0}^2 pi(T_j(q_alpha)) z^j.
```

The exact two-exit analogue of the singleton identity is

```
sum_alpha X_(s,alpha)(z) B_alpha(z^2)
  = sum_alpha Y_(s,alpha)(z) A_alpha(z^3),       s in U.       (1)
```

This is an equality of polynomials with coefficients in the free abelian
group, not just an equality of their supports or total counts. At exponent
`2j+i=3l+k`, the six radix identities identify the actual destination.
A first step into U has its second step in V and contributes zero. A
first step into Q contributes the indicated pi of its second step.
Each mixed-radix representation of an exponent is unique, so the equation
does not conceal coefficient multiplicities.

The same derivation works for any finite Q. At width two, however, the
sum over alpha is essential: polynomial factors associated with different
boundary vertices can compensate without forcing their children equal.

Even assuming every vertex has infinite kernels in both bases does not
make each A_alpha and B_alpha nonzero. A boundary vertex may first move
to the other boundary vertex before escaping. Only the assertion that
**all** A_alpha vanish would make V binary-closed, and similarly for B.
Thus the first singleton reduction already needs a replacement.

## 2. An exact two-exit graph satisfying both-base infinitude

Fix any irrational `0<alpha<1`, and define binary-valued sequences

```
p(n)=1 if {n alpha}<alpha, and 0 otherwise,
s(n)=p(floor(n/6)),
u(n)=p(floor(n/3)),
v(n)=p(floor(n/2)),                          n>=0.
```

Here braces denote fractional part. In particular `p(0)=1` and `p(1)=0`;
the strict inequality at the endpoint is intentional.

The five root children are exactly

```
E_0(s)=E_1(s)=u,
T_0(s)=T_1(s)=T_2(s)=v.                              (2)
```

For example, write n=3k+r, 0<=r<3. Then
`floor((2n+i)/6)=k=floor(n/3)` for i=0,1. The ternary identity is checked
by writing n=2k+r, 0<=r<2. The vertices s,u,v are distinct:

```
u(2)=1, v(2)=0;
s(3)=1, u(3)=0;
s(2)=1, v(2)=0.
```

Consequently `U={s}` has exactly the two exits `Q={u,v}`.
These are actual entire sequences, so all six radix identities and both
zero-output identities hold everywhere in the reachable graph.

Moreover,

```
T_0(u)=T_1(u)=T_2(u)=p,
E_0(v)=E_1(v)=p.                                    (3)
```

The state p is distinct from s,u,v, since it has value 0 at n=1 while
all three of those states have value 1 there.

### 2.1. Every reachable state has the same irrational frequency

In fact every affine section

```
f_(m,r)(n)=s(mn+r)=p(floor((mn+r)/6)),
```

for integers m>=1,r>=0 has a natural density of ones equal to alpha.
Split n into its six residue classes, n=6l+t. Then

```
f_(m,r)(6l+t)=p(ml+floor((mt+r)/6)).                   (4)
```

For each fixed t this is the indicator of a length-alpha interval under
an irrational rotation with increment m alpha, so its frequency is alpha.
Interleaving six subsequences with the same limiting frequency leaves
that frequency unchanged.

The elementary equidistribution input here can be seen directly. For
irrational beta and every nonzero integer k, the average of
`exp(2*pi*i*k*(l beta+gamma))` over 0<=l<L tends to zero by the finite
geometric-sum formula: its denominator `1-exp(2*pi*i*k*beta)` is nonzero
and independent of L. Approximation of an interval from above and below
by trigonometric polynomials then gives frequency equal to its length;
the endpoints have zero length. Apply this with beta=m alpha and the
fixed shift gamma from (4).

Every reachable joint section has the form f_(m,r), with
`m=2^a3^b`, `0<=r<m`. The same argument also covers every further
binary or ternary descendant.

### 2.2. Finite kernels cannot have an irrational existing frequency

Here is the required finite-kernel fact with its justification. Let f be
a binary-valued sequence with finite k-kernel, k>=2. List its kernel states
and let P be the rational stochastic matrix whose entry P_ab is 1/k times
the number of digit transitions from state a to state b. Let w be the
0/1 vector of outputs at zero. For the state f,

```
(P^j w)_f = k^(-j) sum_{0<=n<k^j} f(n).              (5)
```

Suppose the natural frequency of ones in f exists and equals rho. The
right side of (5) then tends to rho, and so does its Cesaro mean in j.

For completeness, the Cesaro limit of the powers of a rational finite
stochastic matrix is a rational matrix. All P^j are bounded. Hence its
eigenvalues have modulus at most 1 and its Jordan blocks at eigenvalues
of modulus 1 have size one. The Cesaro average kills every eigenvalue
other than 1 and retains the eigenspace at 1. Its limit is the projection
onto `ker(I-P)` along `im(I-P)`. Those spaces are complementary because
the eigenvalue 1 is semisimple; they have bases obtained from rational
linear equations. The projection therefore has rational entries.
Thus the limit of the Cesaro mean in (5), rho, is rational.

This proves the needed statement even if frequencies for other kernel
states do not exist. It does not assume that every automatic sequence
has a frequency.

Since each f_(m,r) above has the irrational frequency alpha, none has
finite binary kernel and none has finite ternary kernel. Thus the entire
reachable graph satisfies V007's hypothesis (I).

**Conclusion.** A finite interior with exactly two exits is compatible
with (I), the full six radix identities, zero-output compatibility, and
whole-sequence distinguishability. Therefore the statement obtained by
replacing “single exit” by “two exits” in V007 is false at that generic
hypothesis scope.

## 3. Where the singleton polynomial argument fails

For this example, in the order Q=(u,v), the root rows in (1) are

```
X_s(z)=(1+z, 0),
Y_s(z)=(0, 1+z+z^2).
```

Using (3), the two relevant boundary rows are

```
B_u(z)=(1+z+z^2)e_p,
A_v(z)=(1+z)e_p.
```

Thus the complete destination-valued equality at s is

```
(1+z)(1+z^2+z^4)e_p
  = (1+z+z^2)(1+z^3)e_p
  = (1+z+z^2+z^3+z^4+z^5)e_p.                       (6)
```

All six two-step swaps lead to the same p. But the binary children of u
and the ternary children of v do not appear in (6). They are

```
E_i(u)(n)=p(floor((2n+i)/3)),
T_j(v)(n)=p(floor((3n+j)/2)).
```

They are actual retained states of the graph, not missing boundary data.
The root equations simply place no constraint on them through the one
mixed-radix swap in (6). In the singleton proof the one boundary state
was necessarily entered through both radices, allowing these constraints
to meet at the same state. With two exits, incoming binary and ternary
edges can land at different states. Collapsing u and v in an unlabeled
support calculation would incorrectly recover the singleton conclusion.

## 4. Why this does not refute the active target

### 4.1. A named full Collatz root identity fails

The scalar interface for a genuine invariant requires

```
b(3n)=b(4n),
b(3n+2)=b(2n+1),
b(4n+2)=b(n),                                  every n>=0.
```

For b=s, the third identity already fails at n=1:

```
s(6)=p(1)=0,       s(1)=p(0)=1.                       (7)
```

Thus this is not a Collatz invariant or a counterexample to the active
all-invariant theorem. The theorem at the generic graph level fails;
the corresponding statement with all three Collatz root relations is
not decided here.

### 4.2. Its joint section complexity is at least quadratic

There is also no linear-growth counterexample. For a,b>=1,

```
s(2^a3^b n)=p(2^(a-1)3^(b-1)n).                      (8)
```

For distinct positive integers m<M, the whole sequences p(mn) and p(Mn)
are distinct. Indeed take

```
alpha/M < x < min(1/M, alpha/m).
```

This is a nonempty open interval. On it `mx<alpha` and
`alpha<Mx<1`, so the two interval indicators have values 1 and 0.
The values `{n alpha}` are dense, by the same irrational-rotation
argument used above; some such n enters this interval. Because
`{mn alpha}={m {n alpha}}`, it witnesses p(mn)=1 and p(Mn)=0.

The multipliers `2^(a-1)3^(b-1)` in (8) are pairwise distinct for
different pairs (a,b), by unique factorization. At depth a+b they are
actual zero-offset joint sections. Hence, for D>=2,

```
|J_D(s)| >= D(D-1)/2.                                (9)
```

In particular, the example has a two-exit interior at the root while
its graph expands later. It does not show arbitrarily distant bounded
layers or even a second two-exit layer. Existence of one small separator
and repeated bounded separators are different statements.

## 5. Bounded comparison and decision

Three mechanisms were discriminated before deeper classification:

| Mechanism | Exact result of this probe | Consequence |
|---|---|---|
| Copy singleton support polynomial and ignore boundary labels | Equation (6) passes while u and v stay distinct | Reject this reduction |
| Exclude every finite two-exit interior using only radix laws and (I) | The actual sequences in Section 2 satisfy all these hypotheses | Refuted at the generic scope |
| Use repeated bounded layers, or propagate the three full root relations through a labeled boundary | Counterexample has quadratic growth and fails (7) | Remains a meaningful direction; no theorem supplied |

The next all-finite-width mechanism must retain more than one boundary
cardinality. Possibilities consistent with this bounded test are a
constraint on **repeated** bounded layers, or additional equations
propagated from the Collatz root identities that couple the two boundary
states. Neither follows merely from each vertex having infinite kernels
in both bases. The destination-valued equation (1) is a correct interface
for those tests; it is not itself a rigidity theorem.

## 6. Seven-field assessment

1. **Objects.** Finite forward interiors, two distinct exits, actual
   binary/ternary section transitions, destination-valued boundary
   polynomials, and an irrational-rotation sequence with repeated blocks.
2. **Structural gain.** An exact boundary equation valid for every finite
   width, together with a two-exit counterexample that satisfies all its
   generic hypotheses, including infinitude in each base at every state.
   It identifies the specific loss in dropping boundary-state labels.
3. **Translated unresolved gap.** Prove unbounded complexity ratios using
   repeated finite boundaries and/or the full three Collatz root
   identities. A universal exclusion of single finite boundaries is
   too strong under the generic radix-plus-infinitude hypotheses.
4. **Worked example.** Equations (2)-(6), with s,u,v,p explicitly given
   as entire binary-valued sequences for every irrational 0<alpha<1.
5. **Known-cycle controls.** The d=5/d=61 divisibility colorings still
   have finite kernels and do not satisfy (I). The new control instead
   satisfies (I) and fails a named full Collatz root identity in (7).
   Its quadratic lower bound (9) also prevents treating it as a
   counterexample to the growth target.
6. **Cheapest meaningful next test.** Track how a second distant
   two-exit layer could be reached from the first using (1), retaining
   state labels and the full root relations. Test a claimed repeated-cut
   implication against this finite-block-stretch construction before
   any wider finite-state search.
7. **Genuinely intermediate milestone.** The scoped generic obstruction
   and the exact labeled boundary interface. They prevent spending a
   research batch on a false width-two analogue; no positive
   all-invariant growth milestone is claimed in this note.

## 7. Verification boundary

These are symbolic arguments about entire functions. The frequency fact
is justified above by finite-matrix averaging and irrational rotation;
no numerical frequency fit or finite-prefix equality is used. The
counterexample has exact failures and exact growth witnesses. No change
to historical mathematical code/evidence, new large catalogue, novelty
claim, or formal Lean verification is included.
