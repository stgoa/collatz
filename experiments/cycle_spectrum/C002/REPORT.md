# C002 — Two growing blocks and a uniform cycle exclusion

**2026-10-19. Written proofs, exact finite checks, novelty unclaimed.**
This batch tests the cancellation mechanism when both repeated blocks grow.
Its strongest elementary consequence is uniform over the blocks themselves:
two different blocks with the same length and total valuation cannot produce
an integer Collatz cycle when their repetition counts sum to at least three.
The [headline goal](../../../docs/CYCLE_SPECTRUM_BRIEF.md) remains open.

## 1. The uniform theorem

Let u and v be different nonempty positive valuation words, each of length
m and total A, with `U=2^A>V=3^m`. For arbitrary k,ell>=1 with k+ell>=3,

```
den(u^k v^ell) > 2^m * 2^A/3^m > 2^m > 1.
```

The [elementary proof](PROPORTIONAL.md) retains exact integer valuations
and uses the raw odd-only map, including its arrow at 1. There is no bound
on m, A, the two words, or either repetition count. The two blocks need
not themselves be primitive. Different cyclic phases count as different
words here, and are allowed by the theorem.

This is an exclusion of a specified structural class of cycles. An arbitrary
cycle word need not have this form. The hypotheses u!=v and k+ell>=3 are
essential to the stated proof; we do not silently apply the result to
identical blocks or the remaining k=ell=1 case.

There is also an effective finiteness statement across the entire class.
If the reduced denominator is at most d0, then

```
2^m < d0,                 2^(A+m) < d0*3^m.
```

Only finitely many totals and positive words remain. The proportional-slope
bound below then bounds both exponents for each pair. Thus finite bounded
denominator layers can be enumerated within this entire structural class;
the assertion is uniform over varying blocks, not only a fixed catalogue.

### Why the bound works

Write each block action as `(3^m*x+C_z)/2^A`. Exact suffix lengths give

```
0 < C_z <= 2^(A-m)*(3^m-2^m).
```

Different equal-total words have different C: otherwise the same positive
rational fixed point would have two different exact valuation histories
of the same length. Set J=C_v-C_u, n=k+ell and h=gcd(k,ell). Elimination
and strong divisibility give

```
den(u^k v^ell) > U^(n-h)/|J|.
```

Since n>=3 implies n-h>=2, and `|J|<UV/2^m`, the claimed uniform lower
bound follows. No prime-factor distribution assumption is used.

## 2. Complete fixed-pair picture

For arbitrary fixed u,v define

```
D_z=2^sum(z)-3^len(z),
G_z(t)=(2^(t*sum(z))-3^(t*len(z)))/D_z,
K=D_u*C_v-D_v*C_u.
```

For `w=u^k v^ell` with D_w>0, the two exact elimination identities imply

```
gcd(C_w,D_w) divides |K|*gcd(G_u(k),G_v(ell)),   K!=0.
```

The common geometric factor is indispensable. The two slope regimes have
different proofs and strengths.

| Block relation | Proved conclusion | Inputs and limits |
| --- | --- | --- |
| Equal valuation-to-length ratios, K!=0 | Explicit exponential lower bound, with at least half the common exponent retained | Elementary strong divisibility; all constants displayed in [the proof](PROPORTIONAL.md) |
| Unequal ratios | `log den(w) = sum(w)*log(2) - o(k+ell)` on the entire positive domain | Two published Corvaja–Zannier inputs; [application](INDEPENDENT_SLOPES.md) audits every local contribution and exceptional translate; no effective threshold |
| K=0 and D_w>0 | Both blocks repeat the same primitive rational cycle from the same phase; its denominator persists | Exact determinism; this exception includes actual generalized cycles and any hypothetical integer Collatz cycle |

The unequal-slope result permits one expanding block. Its power-gap argument
does not assume the two positive powers remain a fixed relative distance
apart. The [primary source](https://arxiv.org/pdf/math/0311030) supplies the
S-unit estimates; their specialization is a written argument in this batch,
not an independent formal replay of that publication.

For equal ratios, write the totals as (ar,br) and (as,bs), put
`U=2^a`, `V=3^b`, `H_j=U^j-V^j`, `E=H_gcd(r,s)`, and let J0 be the
part of `|K/E|` coprime to 6. Then

```
den(u^k v^ell) > U^(rk+s*ell-gcd(rk,s*ell))/J0.
```

Every fixed nondegenerate pair therefore has only finitely many exponent
pairs in any bounded denominator layer. This fixed-pair theorem alone
does not bound a family in which the blocks vary; Section 1 supplies that
extra uniformity for equal totals.

## 3. The failed stronger bound and its exact obstruction

C001's constant cancellation bound cannot survive two growing blocks.
For `u=(1,1,3)`, `v=(1,2,2)` and k=ell=t,

```
K=20,
gcd(C_w,D_w)=(32^t-27^t)/5,
den(w)=5*(32^t+27^t).
```

At t=2 the cancellation is 59, larger than 20. It grows exponentially,
while the reduced denominator still grows. The different sharpness family
`u=(1,3)`, `v=(3,1)` has

```
den(u^t v^t)=7*(16^t+9^t).
```

Its unique cyclic 33 proves primitivity. Its exponential rate shows why
the half-exponent lower bound cannot be strengthened uniformly in this
class. The [finite receipt](two_blocks_audit.json) also preserves all thirteen
constant-bound failures found in actual stored cycle decompositions (six
distinct words across twelve parameters, including scaled repeats). One is the d59 cycle
starting at 221, with u=(1), k=2, v=(2), ell=4: C=1105, D=295, g=5>|K|=2.
Even unequal slopes do not justify a constant bound.

## 4. Unbounded heights and both cycle clocks

Let m>=13, `A=ceil(m log_2 3)`, u_m be the lower mechanical valuation word
with these totals, and v_m its one-letter left rotation. For all k,ell>=1,
the rational cycle of `u_m^k v_m^ell` has every state greater than m/12.
For k+ell>=3 the uniform theorem excludes denominator 1.

The [full proof](PROPORTIONAL.md) compares each block's affine prefixes with
the corresponding pure cycle. It needs no additional exponent separation.
There is one cyclic 222 and one cyclic 11; the word is primitive and its
shortcut parity word is not balanced. With n=k+ell, its local minima number

| Clock | Count |
| --- | ---: |
| Odd-only Syracuse | `n*(2m-A)-1` |
| Shortcut Collatz | `n*(A-m)` |

Both counts and the rational minimum can grow without bound. This preserves
the scope distinction established in the [C001 literature audit](../C001/LITERATURE.md):
the family exceeds any fixed local-minimum-count cutoff and is outside the
direct balanced/Christoffel hypotheses examined there. It does not improve
a general published record for all cycles, and no novelty claim is made.

## 5. Actual-cycle tests and verification

The [independent checker](check_two_blocks.py) recomputes the full declared
finite grid and compares every receipt field by default. Its input is the
unchanged C001 census; this batch replays its actual arrows and tests the
new identities, rather than presenting the census as newly discovered.

| Check | Scope |
| --- | ---: |
| Stored actual cycles replayed | 2,459 across 333 parameters |
| Historical cycle fixtures retained | All 11 |
| Canonical two-block power decompositions | 37,271 |
| Actual decompositions with both repetitions at least 2 | 56 |
| Ordered generated block pairs | 7,056 |
| Generated exponent/word cases | 451,584 |
| Positive integer-cycle realizations | 433,074 |
| Distinct parameters of those realizations | 5,003 |
| Exact generated odd arrows | 10,623,694 |
| Positive common-fixed-point controls | 6,016 |
| Generated equal-total uniform bounds | 33,768 |
| Generated proportional-slope bounds | 44,544 |
| Rotating-mechanical examples | 590, including block lengths 256 and 512 |

Generated blocks have lengths 1–3, valuations 1–4 and both repetition
counts 1–8. Expanding blocks are included. Realizations can repeat the
same primitive cycle: 427,028 cases have primitive displayed words and
6,046 have proper-power words. These are case counts, not distinct cycles.
The actual decompositions use only the canonical minimum-state orientation.
No all-rotation decomposition census or exhaustive fixed-d classification
is claimed. There are **zero eligible equal-total k+ell>=3 decompositions**
in the canonical actual-cycle sample: the uniform inequality is exercised
by the generated integer cycles and the rotating examples. The actual
sample exercises 459 proportional bounds and the general elimination
identity. The finite tests do not verify the imported asymptotic theorem.

Proof review is in [INDEPENDENT_REVIEW.md](INDEPENDENT_REVIEW.md) and
[ROOT_REVIEW.md](ROOT_REVIEW.md).
The side-lane assessment is in [SIDE_REVIEW.md](SIDE_REVIEW.md). Final
delivery checks and the historical finite gate are recorded in
[delivery_checks.json](delivery_checks.json) and [full_gate.json](full_gate.json).
The root's fresh default C002 replay passed, matching the saved receipt.
The full historical `verify_all.py --cpp --transfer-controls` gate also
passed with 119 reported fields. Neither test formalizes these proofs.

## 6. Interpretation and next decision

The previous C001 turn was progress: it delivered a fixed-perturbation
theorem, exact counterexample and cycle tests. C002 is progress through a
uniform structural exclusion, the two-slope classification for fixed pairs,
and an exact obstruction to keeping cancellation bounded.

| Required field | This batch |
| --- | --- |
| Objects | Exact denominator layers of positive rational cycles and their valuation words |
| Structural gain | Uniform exclusion and effective bounded-denominator finiteness for distinct equal-total two-block words with at least three block occurrences |
| Translated gap | Arbitrary primitive words need not have this repeated-block structure; the remaining two-occurrence case and unrelated block totals remain outside the uniform theorem |
| Worked example | Exponential cancellation in `(1,1,3)^t(1,2,2)^t` still leaves denominator `5*(32^t+27^t)` |
| Known-cycle controls | Actual certificates exercise the general/proportional identities; generated cycles exercise the uniform equal-total inequality; identical-block repetitions preserve d1/5/7/13 cycles |
| Cheapest meaningful next test | Test whether removing the equal-total hypothesis preserves an explicit uniform obstruction, with both fixed-denominator examples and exact word identities |
| Intermediate milestone | A structural denominator restriction uniform over varying blocks, with an explicitly stated class; Section 1 now meets one such milestone |

The next investigation should seek a restriction on how genuine cycle words
can be assembled while their constituent blocks vary. Merely fixing a new
catalogue and increasing its repetition cutoff would not address the
remaining uniformity problem. No new goal is activated by this recommendation;
the accepted all-cycle headline stays active, and divergence is separate.
