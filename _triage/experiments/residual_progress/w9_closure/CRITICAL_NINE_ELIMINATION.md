# Eliminating the complete critical-nine domain

**Status: written proof and finite executable conditional compiler.** This
eliminates one entire remaining pair domain. It does not construct the
critical-five input currents, prove their universal existence, or claim novelty.
All clocks below are odd-only Syracuse clocks, with 1 absorbing.

Write `S(x)=(3x+1)/2^v2(3x+1)`, `F(x)=4x+1`, and use killed atoms `[1]=0`.
The divergence of row `e_x` is `[x]-[S(x)]`. Set

\[
P(w)=[3w]-[w],\qquad
W_5=\{w>0:w\equiv5\pmod8\},\quad
W_9=\{w>0:w\equiv9\pmod{16}\}.
\]

The elementary normal form `nu` and its exact finite currents are from
[R25](../bridge_normal_form/BRIDGE_NORMAL_FORM.md). The finite decreasing
critical plans are from
[R37](../tripling_equivalence/TRIPLING_EQUIVALENCE.md). All input currents in
this note are finite signed **integer** currents with exact divergence.

## 1. Complete-domain elimination and its scope

**Theorem.** For every `w in W9`, there is an explicitly computed finite integer
current `J_w` and finitely supported integer coefficients `c_w(u)`, supported
on `W5`, such that

\[
\operatorname{div}J_w
  =P(w)-\sum_{u\in W_5}c_w(u)P(u),
\qquad c_w(u)\ne0\Longrightarrow u\le{9w+3\over4}. \tag{1}
\]

The algorithm producing this formal identity terminates without an absorption
search or any hypothetical current. If exact currents for all its nonzero
inputs are supplied, substitution produces an exact current for `P(w)`.
Missing or invalid inputs are rejected.

Consequently the following assertions are equivalent:

1. Every positive odd integer reaches 1.
2. For every `w in W5`, a finite exact current for `P(w)` exists.

For `2 => 1`, (1) supplies every `W9` input, and the R37 critical-domain theorem
applies to `W5 union W9`. Conversely, absorption currents for `3w` and `w`
give their difference. This is an existence equivalence with a finite
conditional compiler. It does **not** assert an algorithm supplying the
universal `W5` premises, or a decreasing induction within `W5` itself.

The proof is a local identity followed by strong induction on the unresolved
`W9` index. We give all bounds, including the possible larger `W5` request.

## 2. Finite formal critical plans and a sharper endpoint bound

For any positive odd `x`, R37 computes a finite current `H_x` and a list
`I_x` of missing critical indices, each in `W5 union W9`, satisfying

\[
\operatorname{div}H_x=[x]-\sum_{u\in I_x}P(u). \tag{2}
\]

At each step it first replaces `x` by its elementary minimum `q=nu(x)`.
If `q=1`, it stops. If `q=1 mod8`, it takes its strictly decreasing ordinary
arrow. If `q=2 mod3`, it uses the strictly smaller inverse predecessor
`(2q-1)/3`. Otherwise `q` is complementary canonical and the requested index
and next seed are both

\[
u=q/3\quad(q=0\bmod3),\qquad
u=(2q+1)/3\quad(q=1\bmod3).
\]

Each seed strictly decreases. Thus the process terminates and every requested
index satisfies `u <= (2x+1)/3`. Its requested list is strictly decreasing;
subtracting two lists nevertheless requires retaining both signs and any
equal-index cancellations.

**Sharper tripling bound.** Every index in `I_(3z) union I_z`, for any odd
positive `z`, is at most `(3z+1)/2`.

* If `3z` is complementary canonical, its first request is `z`, and all later
  requests are at most `(2z+1)/3`.
* If `3z` is noncanonical, `nu(3z) <= (3z-1)/2`, so all requests are at most `z`.
* If `3z=1 mod8`, its first ordinary arrow, with valuation exactly 2, reaches
  `(9z+1)/4`. The generic bound for that seed is `(3z+1)/2`.

These exhaust all cases. The generic bound for `I_z` is smaller as well.
This sharper estimate, rather than the generic estimate for `3z`, is needed
for the factor-one-half conclusion below.

## 3. The full `W9` run identity

Fix `w=9 mod16` and put `d=v2(9w-1) >= 4`. On `3w` the first two valuations
are `(1,2)`; on `w` they are `(2,1)`. Their endpoints are

\[
S^2(3w)=3v-2,\qquad S^2(w)=v,
\qquad v={9w+7\over8}. \tag{3}
\]

For `v=1 mod8`, both endpoints in this pair have valuation 2 and

\[
(3v-2,v)\longmapsto(3v'-2,v'),\qquad v'={3v+1\over4}. \tag{4}
\]

Since `v2(v-1)=d-3`, (4) can be iterated exactly until that valuation is 1 or 2.
Let `Gamma_w` be the difference of the two prefix currents of length `k+2`
specified below. Its divergence is `P(w)` minus the endpoint pair.

### 3.1 Odd `d=2k+5`, `k>=0`

Set

\[
C={9w-1\over2^{2k+5}},\qquad z=3^kC.
\]

After the prescribed `k+2` arrows the endpoints are `(F(3z),F(z))`.
The explicit sibling current

\[
E_z=e_{F(3z)}-e_{3z}-e_{F(z)}+e_z
\]

has divergence `[F(3z)]-[F(z)]-P(z)`, including the killed-1 convention.
Consequently

\[
\operatorname{div}(\Gamma_w+E_z+H_{3z}-H_z)
 =P(w)-\sum_{u\in I_{3z}}P(u)+\sum_{u\in I_z}P(u). \tag{5}
\]

Here `32z <= 9w-1`, so every requested index obeys

\[
u\le{3z+1\over2}\le{27w+29\over64}<{w\over2}; \tag{6}
\]

the last inequality holds for every `w>=9`. Thus **every odd-valuation
branch** has only smaller critical inputs, for all valuations and phases.

### 3.2 Even `d=2k+4`, `k>=0`

Set

\[
C={9w-1\over2^{2k+4}},\quad z=3^kC,\quad
J(z)=[6z+1]-[2z+1].
\]

The endpoints after `k+2` arrows are exactly `(6z+1,2z+1)`, so

\[
\operatorname{div}(\Gamma_w+H_{6z+1}-H_{2z+1})
 =P(w)-\sum_{u\in I_{6z+1}}P(u)+\sum_{u\in I_{2z+1}}P(u). \tag{7}
\]

The integer relation `2^(2k+4) C+1=9w` gives

\[
C\equiv-2^{-(2k+4)}\pmod9,\qquad C\equiv2\pmod3,
\quad v_3(z)=k. \tag{8}
\]

In particular `z>=5` and `16z <= 9w-1`. These ternary restrictions are part
of the actual domain; arbitrary `z` cannot be substituted.

#### The upper canonical case

If `3z` is canonical, `6z+1` is its elementary selected partner and its
missing list is `I_(3z)`. The sharper bound above applies to it.

For the lower endpoint, if `z` is canonical, its list is `I_z`. Otherwise
`2z+1` is complementary canonical. If `k=0`, (8) gives `z=2 mod3`; the first
inverse step goes to `(4z+1)/3` and all requests are at most `(8z+5)/9`.
If `k>=1`, then `z=0 mod3`, and the first request is `(4z+3)/3`, with all
later requests smaller. In either case every lower request is at most
`(3z+1)/2`, since `z>=5`.

Thus in this entire case every request satisfies

\[
u\le{3z+1\over2}\le{27w+13\over32}<w. \tag{9}
\]

#### The upper noncanonical case and the only possible expansion

If `3z` is noncanonical, `6z+1` is complementary canonical and equals 1
modulo 3. Its first requested index is

\[
u_*=4z+1\in W_5. \tag{10}
\]

The remaining upper list is exactly `I_z`, because `nu(F(z))=nu(z)`.
Every remaining upper request is at most `(2z+1)/3`. The lower list has the
same bounds just proved: if `z` is canonical it is `I_z`; otherwise it is
bounded by `(8z+5)/9` at `k=0` or `(4z+3)/3` at `k>=1`.

All these other indices are strictly less than both `w` and `u_*`. For
example `(4z+3)/3 <= (9w+11)/12 < w` for `w>=9`. Hence after exact signed
cancellation `u_*` remains with coefficient **+1**, and it cannot be canceled
by any lower or subsequent upper request. If `z` is canonical, the two
remaining lists cancel completely, leaving just `P(u_*)`.

For `k>=3`, (10) is also strictly smaller than `w`, since

\[
u_*<w\quad\Longleftrightarrow\quad
\bigl(2^{2k+4}-36\,3^k\bigr)C>8. \tag{11}
\]

At `k=3` the parenthesized integer is 52. It strictly increases thereafter:
the next value is four times the current value plus `36*3^k`. Since `C>=1`,
(11) follows for every `k>=3`.

The only possible nondecreasing request is therefore the following single
positive `W5` input, and it occurs precisely when `3z` is noncanonical:

| `d` | `k` | `z` | larger input `u_*` |
|---|---|---|---|
| 4 | 0 | `(9w-1)/16` | `(9w+3)/4` |
| 6 | 1 | `3(9w-1)/64` | `(27w+13)/16` |
| 8 | 2 | `9(9w-1)/256` | `(81w+55)/64` |

Each displayed `u_*` exceeds `w`; every other request is strictly smaller.
The rows apply to their exact valuation and canonical conditions, not every
integer in the displayed affine formula. The actual ternary unit is 2, so
these exceptions are outside R38's odd-`h` parameterization with ternary
unit 1. Reversing that parameterization cannot certify them.

## 4. Strong induction and an exact finite input bound

Equations (5) and (7) have the common form

\[
\operatorname{div}L_w=P(w)-\sum_{u\in W_5\cup W_9}b_w(u)P(u). \tag{12}
\]

Every `W9` child is smaller than `w`. Every child, including a possible
expanding `W5` child, is at most `(9w+3)/4`. Replace each `W9` child by its
own identity (12), multiplying **all** its rows and coefficients by the
signed parent coefficient. Each branch terminates by strict descent of a
positive integer `W9` parameter. Finite branching makes the expansion finite.
The bound on final `W5` inputs survives, since every recursively expanded
`W9` index is at most the original `w` and `(9w+3)/4` increases with `w`.
This proves (1), including exact multiplicities and signs.

This is not a claim that (12) decreases the full critical index on every
branch: the table contains the precise exceptions. Nor may a separate rule
for those `W5` inputs simply be appended to obtain termination without a new
rank proof. For example, the exact local formal request for `w=9` is

\[
P(9)=\operatorname{div}L_9+P(21)-P(5). \tag{13}
\]

The larger obligation `P(21)` is retained. A rule returning it to `P(9)`
would create a dependency loop; it would not prove either current exists.

Signed cancellations can also remove every premise in an individual case.
For example, recursively expanding the indices `1561,73,41,9` produces the
following nine-row current with divergence exactly `P(1561)`:

\[
e_{247}+e_{4683}+e_{5269}+e_{7025}
-e_{659}-e_{989}-e_{1171}-e_{1561}-e_{1757}. \tag{14}
\]

This finite certificate uses no supplied pair input. It illustrates why
signed coefficients must be combined exactly; it is not universal coverage.

## 5. Reproduction and saved evidence

`w9_closure.py` provides `local_plan(w)`, `five_plan(w)`, and
`compile_five_plan(data, supplied)`. Formal plans expose signed coefficients;
they never treat their missing leaves as actual currents. The compiler checks
every exact input divergence and rejects missing or malformed inputs.

Run:

```sh
python3 experiments/residual_progress/w9_closure/check_w9_closure.py
```

The checker records exact local identities, the child bounds, finite recursive
elimination, cap/input rejection, and a small separately capped set of actual
input substitutions. The latter are finite examples and are not used in the
universal written proof. The JSON receipt records the tested domains and
certificate hashes; the saved small current/input fixture allows an explicit
compiled identity to be inspected. No universal input-current construction
is supplied.
