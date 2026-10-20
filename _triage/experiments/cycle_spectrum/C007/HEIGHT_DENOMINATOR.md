# C007 — Height versus reduced denominator in ordered cycles

**Status:** open candidate with exact arithmetic obstructions. The modular
lemma and the min–top inequality below have elementary written proofs. No
proof or counterexample to the proposed bound is claimed. This note uses the
raw positive odd-only map, without absorbing at 1. A primitive rational
`S_1` cycle is written as a primitive positive odd numerator cycle

```
3n_i+q=2^a_i n_(i+1),       a_i>=1,
gcd(n_0,...,n_(m−1))=1,
```

with reduced odd denominator `q` coprime to 6. Set `L=min n_i`, assume
`q<=L`, and use the normalized heights `h_i=floor(log_2(n_i/L))`,
`B=max h_i`, `z_i=n_i/2^h_i`, and `F_i=3z_i+q2^(−h_i)` of
[C006](../C006/ORDER_RIGIDITY.md). “Ordered” means `F` increases strictly
with sorted `z`; it is equivalent here to a circular rank-shift successor.

## 1. The proposed bound and its exact missing step

The C007 candidate is

```
B <= q−1                                             (H)
```

for every primitive positive ordered cycle in the declared `q<=L` domain.
At `q=1`, (H) forces `B=0`, hence `H=max n_i<2L`; the C004 narrow-cycle
classification then leaves only the fixed point 1. Thus (H) would exclude
every nontrivial **ordered** integer cycle. It would not by itself address
unordered integer cycles or divergent orbits.

The known ordered interface yields a canonical lower mechanical normalized
word `c_i=a_i+h_(i+1)−h_i` with prefix sums `P_j`, total `(A,m)`, and
`D=2^A−3^m>0`. Its weighted intercept is

```
C_h = sum_(j=0)^(m−1) 3^(m−1−j) 2^(P_j−h_j),
D L = q C_h,                q = D/gcd(C_h,D).         (1)
```

The last equality uses the reduced numerator realization. Period primitivity
and reduction of the common denominator are separate conditions. If every height
is zero, `C_h=C_c` is the primitive mechanical intercept, whose gcd with
`D` is 1. For a wide profile the loss `C_c−C_h` can create a large gcd: the
ordered one-height `q=233` control in C006 has `D=1631`, `C_c=14501`,
`C_h=13349`, and `gcd(C_h,D)=7`. A denominator proof must control the full
height-dependent congruence in (1). Rewriting (H) as
`gcd(C_h,D)<=D/(B+1)` is equivalent to the candidate, not progress on it.

## 2. Exact modular lemma: normalization erases heights modulo `q`

**Lemma (written proof).** Every numerator `n_i` is coprime to `6q`.
Moreover, in the ring `Z/qZ` (for `q>1`) every normalized mantissa satisfies

```
z_i = 2^(−h_i)n_i ≡ L 3^i 2^(−P_i)  (mod q),          (2)
```

where the chronological cycle starts at `n_0=L` and all powers of 2 are
units modulo `q`. Thus the complete normalized residue orbit depends on
`c`, `L mod q`, and `i`, but **not** on the height profile.

**Proof.** The numerator is odd by construction. Reducing any predecessor
equation modulo 3 gives `2^a_i n_(i+1)≡q (mod 3)`, so `3` divides no
numerator. If a prime `p|q` divides one numerator, its successor is also
divisible by `p`, because `2` is invertible modulo `p`. Forward propagation
around the cycle would make every numerator divisible by `p`, contrary to
the reduced numerator condition. Finally the normalized arrow is
`2^c_i z_(i+1)=3z_i+q2^(−h_i)`. Reduce modulo `q` and iterate from
`z_0=L`. This proves (2). QED.

Equation (2) exposes a limit of a simple residue argument: the full sets of
unit residues occupied at different height levels need not be disjoint. In
the exact ordered
`q=5`, period-17 cycle beginning

```
(187,283,427,643,967,1453,1091,1639,2461,1847,2773,
 2081,781,587,883,1327,1993),
```

the height-residue sets `n_i mod 5` are

```
height 0: {2,3};  height 1: {2,3};
height 2: {1,2,3};  height 3: {1,2,3,4}.
```

Residue 2 occurs at every level, refuting any assertion that states in
different height bands always have different residues. This example still
allows a matching that selects one distinct residue from each band:
`0→2, 1→3, 2→1, 3→4`. It therefore does **not** refute every possible
residue-counting or matching proof of (H). Such a proof would need a new
reason why the selected residues are distinct; the normalized recurrence
(2) by itself supplies no such reason. This control has `B=3<q=5`, so it
does not refute (H).

## 3. The exact min–top order constraint is too weak alone

Let `B>=1`, and choose any cycle numerator `N` in height band `B`.
Write `N=2^B L+r`, where `r` is a positive odd integer. Comparing its
normalized image with that of the minimum gives

```
F(N)−F(L) = [3r−q(2^B−1)]/2^B.
```

Because `L<N/2^B<2L` and the cycle is ordered, this yields the exact
necessary inequality

```
3r > q(2^B−1),              0<r<2^B L, r odd.       (3)
```

For `B>=q`, (3) is still compatible with `q<=L`; taking `r` of order
`q2^B/3` satisfies the lower bound while the upper bound permits values
of order `L2^B`. Therefore this pairwise order test does not establish
(H). The C006 adjacent-gap system retains more information, but its
zero-forcing estimate has exponent `ceil(m/J)−1−B`; when the number `J` of
height-change forcing sites is large, that estimate also gives no bound of
the form `B<q`.

## 4. Seven-field decision record

| Field | C007 assessment |
|---|---|
| Objects | Primitive positive raw odd-only `S_q` cycles with `q<=L` and circular normalized successor order; reduced denominator `q`, dyadic span `B`. |
| Structural gain | Exact unit-coprimality and height-free normalized residue law (2); exact ordered min–top inequality (3). Both preserve the actual odd-cycle equations. |
| Translated unresolved gap | Prove or refute the height-sensitive divisibility bound in (1), while respecting integer heights, all arrows, and sorted order. Modulo-`q` normalized dynamics alone loses the height information needed for this. |
| Worked example | Ordered `q=5` period-17 cycle above has `B=3` and repeated residues across all height levels; the one-height `q=233` cycle has genuine gcd cancellation. |
| Known-cycle controls | C004 narrow classification, C006 exact `q=5`, `q=13`, `q=233` cycles, and the C006 nonordered `q=11` inversion remain in their stated domains. None refutes (H). |
| Cheapest meaningful next test | Analyze the full integer gap or weighted-intercept congruence for an ordered profile with `B>=q`, beginning with the smallest possible `q=1,B=1`; retain the rank inequalities and exact odd outputs. A finite absence report alone is insufficient. |
| Genuinely intermediate milestone | Exclude ordered denominator-one cycles in the single band `B=1`, leaving all `B>=2` cases open. This is strictly weaker than excluding all ordered integer cycles. |

**Decision:** retain (H) as an open candidate. The elementary arithmetic above
identifies the information that a proof must add, but does not establish a
new denominator exclusion. No novelty or finite completeness claim is made.
