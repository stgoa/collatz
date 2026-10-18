# S.1 — Fixed-factor stopping with explicit finite counts

**Batch P6-001. Proposed label: calibration. Status: written proof, with
separate executable checks.** This proves the stopping statement and W5
pullback named in [S.1](../../../ROUTE_MAP.md). It re-derives a fixed-half
corollary of a published density theorem. It does not prove convergence,
universal current supply, or a new dispatcher rule. Independent confirmation
of the programme label is recorded in the [Phase 6 ledger](../../../docs/PHASE6_LEDGER.md).

The batch read the independent lane at
`b1785fb2dcf121586e99be95c90b94afcf1e9733`. Its direction and feed entries
support using S.1 as a calibration; they are not premises of this proof.
The elementary quotient facts used in Section 6 are frozen repository
results, with their domains retained.

## 1. Maps, clocks, and the exact statement

Fix a positive odd integer `d` with `gcd(d,6)=1`. Define the **raw shortcut
map**, on positive integers, by

```
C_d(n) = n/2             if n is even,
         (3n+d)/2        if n is odd.
```

This raw map is used for parity counting even when its orbit reaches 1.
Define the raw odd map by removing every factor of 2 from `3n+d`, and let
`S_d` be that map **absorbed at 1**. Thus `S_d(1)=1` even when the raw map
would leave 1. The clocks of `C_d` and `S_d` are different. All conclusions
below state the `S_d` clock explicitly.

For integer `X>=1`, write

```
M(X) = ceil(X/2),
F_d(X,K) = #{positive odd n<=X:
             S_d^j(n)>n/2 for every integer 0<=j<=K}.
```

In particular, the seed 1 is a failure of half-descent; it is not silently
exempted from this count.

**Theorem.** For every rational `0<epsilon<=1` the following exact
construction terminates. It supplies positive integers `K(epsilon)` and
`X0(d,epsilon)` such that

```
F_d(X,K(epsilon)) <= epsilon*M(X)
```

for every integer `X>=X0(d,epsilon)`.

Set `r=16807/18432`. Choose the least integer `m>=9` satisfying

```
(8/7)*r^m <= epsilon/2.                                  (1)
```

Then define

```
k = K(epsilon) = 5m,
R = 2^(k-1),
B = sum_(j=3m)^(k-1) binom(k-1,j),
delta = B/R,
Z = ceil(4d*3^k/2^k),
E = B+ceil(Z/2),
M0 = ceil(2E/epsilon),
X0(d,epsilon) = 2M0-1.                                 (2)
```

Every ceiling in (2) is a ceiling of an exact rational number. No floating
logarithm or approximate binomial tail is needed. The search also has an
explicit rational upper limit. Put `a=1/r-1=1625/16807`. The binomial
theorem gives `r^(-m)=(1+a)^m>=1+ma`, and therefore

```
r^m <= 1/(1+ma).
```

It follows that the least m in (1) is at most

```
max(9,ceil((16/(7epsilon)-1)*16807/1625)).                (2a)
```

Indeed this bound makes `1+ma>=16/(7epsilon)`, and hence
`(8/7)*r^m<=epsilon/2`. This proves finite termination without a numerical
logarithm. The inequalities are deliberately conservative; their constants
are not claimed to be optimal. For example, tolerances `1/10` and `1/100`
give respectively `m=34,59` and odd-arrow horizons `170,295`.

The theorem for arbitrary rational `epsilon>0` follows by replacing it
with `min(epsilon,1)`. For a fixed `d`, letting epsilon tend to zero proves
that the odd seeds which eventually half-descend have relative natural
density one. The horizon varies with epsilon. This is not a claim of zero
exceptional density at one fixed horizon.

## 2. Complete raw parity words

For a positive integer `n`, let

```
b_i(n) = C_d^i(n) mod2,           0<=i<k,
p(n) = sum_(i=0)^(k-1) b_i(n).
```

**Parity lemma.** Length-k raw parity words are in bijection with the
residue classes modulo `2^k`. Restricting to odd starts fixes `b_0=1` and
leaves exactly `R=2^(k-1)` equally represented odd residue classes.

**Proof.** Each branch has the form `(3^b*x+d*b)/2`. Inductively, if two
positive inputs differ by `t*2^j`, their first j branch bits agree and their
images after j steps differ by `3^p*t`, where p counts the odd branch bits
in that prefix. More explicitly, after i steps of their common prefix
the difference is `3^(p_i)*t*2^(j-i)`, which is even for `i<j`.

Suppose a length-j word specifies one residue modulo `2^j`. Its two lifts
modulo `2^(j+1)` can be represented by positive integers `n` and `n+2^j`.
Their j-th images differ by the odd integer `3^p`, so their next branch
bits are opposite. Each word therefore has exactly one lift with each
possible next bit. Starting with the empty word proves the bijection by
induction. Oddness of d makes the odd branch integral; the multiplier 3
is odd. No special value of d is used. This proves the lemma. □

The modulus here is `2^k` for a **shortcut parity word**, which includes
every even step. It is not the modulus of an exact odd-valuation cylinder.
An exact valuation word of total valuation A still requires `2^(A+1)`,
including its extra bit. The two encodings are not being identified.

Among the odd residue classes, `p` has the exact counting distribution

```
p = 1+Binomial(k-1,1/2).
```

This notation is a convenient uniform count on the finite residue set;
it asserts no stochastic independence along an individual infinite orbit.
Consequently exactly B classes have `p>3m` when `k=5m`, with B as in (2).

## 3. An exact exponential upper bound for the bad classes

Take `z=4/3`. Uniform averaging over the odd residue classes gives

```
average(z^p) = z*((1+z)/2)^(5m-1)
             = (4/3)*(7/6)^(5m-1).
```

On `p>3m` one has `z^p>=z^(3m)`. Averaging this inequality yields

```
delta <= (4/3)*(7/6)^(5m-1)/(4/3)^(3m)
       = (8/7)*((7/6)^5/(4/3)^3)^m
       = (8/7)*(16807/18432)^m.                         (3)
```

Using the integer threshold `p>=3m+1` could improve the prefactor to
`6/7`; the construction uses the valid weaker bound (3). In particular
(1) gives `delta<=epsilon/2` with no numerical rounding issue.

## 4. Affine intercept and conversion to odd arrows

For a fixed raw parity word, exact composition gives

```
C_d^k(n) = (3^p/2^k)*n+c,
0<=c<=d*((3/2)^k-1).                                  (4)
```

For completeness, each step has multiplier at most `3/2` and additive
term at most `d/2`. Starting at intercept zero therefore gives

```
c <= (d/2)*sum_(i=0)^(k-1) (3/2)^i
   = d*((3/2)^k-1).
```

If the word is good, meaning `p<=3m`, then

```
3^p/2^k <= (27/32)^m < 1/4,                            (5)
```

because `4*27^9<32^9` and `27/32<1`. If also `n>=Z`, then
`n/4>=d*(3/2)^k`. Equations (4) and (5) give

```
C_d^k(n) < n/4+d*(3/2)^k <= n/2.                      (6)
```

Now start from an odd n. The raw shortcut prefix contains p odd
operations. Complete any final divisions by 2 after its endpoint. This
adds no odd operation and reaches exactly the p-th raw odd-map iterate,
namely `oddpart(C_d^k(n))`, which is no larger than (6). Thus the raw
half-descent occurs within `p<=k` odd arrows.

If the raw odd orbit reached 1 earlier, the absorbed orbit follows that
prefix and then stays at 1. All n under consideration satisfy `n>=Z>1`,
so `1<=n/2` and that earlier arrival is already a successful half-descent.
Otherwise raw and absorbed odd iteration agree until the endpoint just
constructed. In both cases the good word and `n>=Z` imply half-descent
within k arrows of the absorbed map `S_d`. This argument does not assume
that the raw shortcut map is absorbed, and it does not count appended
halvings as odd arrows.

## 5. Count every cutoff, including its remainder

The positive odd integers through X form `M=M(X)` consecutive positions
in the odd-integer lattice. Each odd class modulo `2^k` occupies one
class modulo R in those positions. It therefore occurs at most
`floor(M/R)+1<=M/R+1` times. The number of starts in the B bad classes is
at most

```
B*(M/R+1) = delta*M+B.                                 (7)
```

Every failure is either in a bad class or is an odd seed below Z.
There are `floor(Z/2)` positive odd integers below Z; the chosen bound
`ceil(Z/2)` is safe, including either parity of Z. Counting possible
overlap twice only enlarges the upper bound. Thus for **every** integer
`X>=1`, without a divisibility or dyadic-cutoff condition,

```
F_d(X,k) <= delta*M(X)+B+ceil(Z/2)
          = delta*M(X)+E.                              (8)
```

For `X>=X0=2M0-1`, one has `M(X)>=M0>=2E/epsilon`.
Combining (1), (3), and (8) proves

```
F_d(X,k) <= (epsilon/2)*M(X)+E <= epsilon*M(X).
```

This proves the theorem with every cutoff error retained. The term B is
the finite residue-counting error. It cannot be omitted merely because
the binomial proportion is small or because one later wants to let the
modulus vary with X.

## 6. The W5 pullback and the exact quotient target

This section uses **d=1 only**. Let

```
W5={positive w: w=5 mod8},
q=rho(w)=nu(3w),
W(X)=#(W5 intersect [1,X])=floor((X+3)/8).
```

The frozen [R37 critical-domain theorem](../../residual_progress/tripling_equivalence/TRIPLING_EQUIVALENCE.md)
and [R43 rank interface](../../residual_progress/critical_rank/CRITICAL_IMAGE_RANK.md)
give, on W5,

```
q = 3w             when 3w is canonical,
q = (3w-1)/2       when 3w is selected,
w<q<=3w,           q>=7.                              (9)
```

The map `w -> q` is injective on W5. It is injective within each affine
branch, while the first image is 0 modulo 3 and the second is 1 modulo 3,
so the branches cannot collide. This is a statement about this critical
map, not a general density-preservation property of nu.

The frozen [R25 quotient theorem](../../residual_progress/bridge_normal_form/BRIDGE_NORMAL_FORM.md)
gives `T^j(q)=nu(S_1^j(q))` and `nu(x)<=x`. Whenever the ordinary odd
orbit of q half-descends within j arrows,

```
9*T^j(q)+5 <= 9q/2+5 < 8q,                            (10)
```

because `q>=7`. Thus such a q passes the exact R.2 stopping threshold,
using the same number j of quotient arrows. The finite quotient current
lifts retain their own signed rows; (10) does not identify their row
counts with this clock.

For rational `0<epsilon<=1`, put `eta=epsilon/18` and use Sections 1–5
with d=1 and tolerance eta. Define

```
K_W(epsilon)=K(eta),
X_W(epsilon)=max(5,ceil(X0(1,eta)/3)).                  (11)
```

For any integer `X>=5`, put `t=W(X)>=1`. Since `X<=8t+4`,

```
M(3X)=ceil(3X/2)<=12t+6<=18t=18W(X).                  (12)
```

For `X>=X_W`, the half-descent theorem applies at the integer cutoff 3X.
By injectivity in (9), every W5 input through X which fails R.2 through
time `K_W` gives a distinct half-descent failure q through 3X. Equations
(10)–(12) therefore prove

```
#{w in W5, w<=X:
  9*T^j(rho(w))+5>=8*rho(w) for every 0<=j<=K_W}
 <= F_1(3X,K_W)
 <= eta*M(3X)
 <= epsilon*W(X).                                    (13)
```

In particular, R.2 holds for relative-natural-density-one W5 inputs.
All finite cutoff and normal-form issues in this pullback are covered
by (9)–(13); no distribution of general normal-form fibres is assumed.
The exceptional set has not been removed. A supplied forward prefix
passing (10) supplies only the existing conditional smaller-rank plan;
the present counting theorem supplies no missing input currents.

## 7. Published calibration, transfer, and limits

The closest finite-horizon statement is
[Borovkov–Pfeifer, Corollary 2, equation (11)](https://doi.org/10.1137/S0040585X97978245),
checked in its author-uploaded text linked in L1. For k>=2, the density of
`{n:C_1^k(n)<n/2}` is `2^(-k) sum_(0<=j<(k-1)/log_2(3)) binom(k,j)`;
these densities tend to1. This supplies the precise finite-horizon benchmark.
Here we re-derive its density-one limit with explicit conservative cutoff
errors, rather than asserting all of its exact fixed-k densities.

[Korec, *A density estimate for the 3x+1 problem* (1994), Theorem 1,
page 85](https://dml.cz/bitstream/handle/10338.dmlcz/133225/MathSlov_44-1994-1_8.pdf)
proves natural-density-one descent below `n^c` for every `c>log_4(3)` in
the shortcut clock. Taking `c=4/5` is allowed because `3^5<4^4`.
For `n>=32`, `n^(4/5)<=n/2`. Restriction to odd starts preserves a
zero-density exceptional set, and completing final halvings gives the
odd-only fixed-half statement. This identifies the precise published
corollary being calibrated.

Sections 1–5 independently prove that corollary with explicit finite
horizons and all integer cutoff errors. They do **not** re-prove Korec's
stronger power-descent theorem or claim his power exponent for this fixed
horizon. The primary paper's parity lemma concerns the shortcut clock;
its power-descent iteration count is not bounded independently of the
starting value. The [literature audit](../../../docs/PHASE6_LITERATURE.md)
records the distinction from the Terras/Everett benchmarks and Tao's
different logarithmic-density statement. No novelty is asserted for the
elementary counting argument or its deliberately loose constants.

**Transfer status:** Sections 1–5 hold for each fixed d in the declared
domain, with the same K but d-dependent Z and X0. They even use only the
oddness and positivity of d. The W5/nu/T pullback is specific to the
frozen d=1 interfaces; this note defines no generalized quotient. The
ordinary statement coexists with the exact nonprincipal cycles in the
[transfer controls](../README.md). A cycle minimum can remain forever
exceptional without contradicting density one. Hence the proposed label
is **calibration**, not a proved non-transfer step.

No conclusion here asserts arrival at 1 for all or almost all starts,
an upper bound on total absorption time, C.2's power bound for unabsorbed
seeds, or a contraction of signed annular mass. Repeatedly applying a
density statement to its own endpoints would require an additional
argument controlling concentration in the exceptional set. The frozen
R1–R94 proofs and seventeen-family dispatcher are unchanged.

## 8. Verification boundary

The universal assertions above follow from the written argument, not from
finite trajectory samples. [calibration.py](calibration.py) constructs the
constants with exact rational arithmetic and a proved finite search limit.
An optional smaller computation cap returns an error when exhausted.
[check_calibration.py](check_calibration.py) compares its complete output
with [calibration_audit.json](calibration_audit.json):

```
python3 -B experiments/phase6/stopping_calibration/check_calibration.py
```

The persisted replay covers 24,570 complete parity words, 49,140 lifted
words, 504 cutoff comparisons, and exact binomial bounds for m from 1 to
200. It also checks 18 complete parameter examples and 72 cutoff
boundaries, 4,608 raw-clock identities, 1,102 half-descent conversions,
and five retained exceptional seeds. The W5 audit checks 1,024 inputs,
47,104 semiconjugacy identities, 32,395 threshold implications, 8,188
integer cutoffs, and three complete pullback parameter examples. Twelve
invalid-domain or exhausted-cap cases are rejected. The two frozen
R25/R37 source inputs have pinned hashes.

These finite checks preserve the distinction between raw and absorbed
maps, all cutoff ceilings, and the original W5 rank formula. They do not
test a putative universal convergence mechanism. Missing receipts,
incorrect arithmetic, or exhausted exploratory caps must not become a
claim that every exceptional seed is resolved.
