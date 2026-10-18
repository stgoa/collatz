# Framework scouting, memo 1

2026-10-18, sidekick lane. This memo is for finding a formulation in which Collatz could follow from structure rather than from rules applied class by class. It records the constraints any such formulation has to meet, and which candidates survive them. No proof is claimed. Every number below is reproducible from this branch.

## 1. Three constraints, all checked

**C1. Transfer.** Let `T_d(x) = (3x + d)/2^v2(3x + d)`. Then `T_d(d·y) = d·T_1(y)` on 2-adic integers. So 3x+d on the integers is 3x+1 on rationals with denominator `d`. Every identity built only from 2-adic data, 3-adic data and size is the same for every `d` with `gcd(d, 6) = 1` (feed, 01:0x; `sidekick/probes/transfer_3xd.py`).

**C2. Positive rational cycles.** Every periodic valuation word `(v_1..v_k)` with `2^m > 3^k`, where `m = Σv`, gives a positive cycle of 3x+1 on rationals with odd denominators. Its point is `x = B/(2^m − 3^k)`.

`frameworks/rational_cycles.py` lists all primitive such words with `k ≤ 9` and `m ≤ ⌈k log2 3⌉ + 2`:

- There are 3,889 cycles, and the only integral one is `{1}`.
- They reproduce known integer cycles of 3x+d, after multiplying by the denominator:

  | map | cycle minima |
  |---|---|
  | 3x+5 | 1, 19, 23 |
  | 3x+7 | 5 |
  | 3x+13 | 1, 211, 227, 251, 259, 283, 287, 319 |

- Cycle minima get large when `m/k` approximates `log2 3` well from above. The largest here is `319/13 ≈ 24.5`, at `(k, m) = (5, 8)`.

**C3. The two halves of the conjecture transfer differently.**

- **No nontrivial cycles.** This half depends on `d`, since 3x+5, 3x+13 and 3x+61 have extra cycles. Any proof of it must use integrality. The known tool does: Baker-type lower bounds on `|2^m − 3^k|` combined with computer verification exclude cycles up to very large lengths, but not all of them.
- **No divergence.** By C1, this is the `d = 1` slice of Lagarias's periodicity conjecture: no rational with an odd denominator has a divergent orbit. No such orbit is known for any `d`. So an argument for this half does not need to tell different `d` apart.

  What it does need is to turn the average contraction, a factor of about 3/4 per step, into a statement about every orbit. It must also fail for maps that expand on average, such as 5x+1, where divergence is expected.

## 2. What this says about the rule programme

**Its identities do not depend on `d` (C1).** For `d = 1`, a complete recursion would prove both halves, because its finite base check is true. The same recursion carried to 3x+d would reduce every obligation to that map's base, where false cases sit at its extra cycles. This is consistent; it is not a contradiction.

**Completeness is a stopping-time statement.** By the feed entry of 00:53, a complete recursion is equivalent to the quotient stopping-time statement for the critical images `ν(3w)`. Two families of shadows make that hard:

- Every cylinder contains shadows of negative rational cycles. These are growing patterns, and integer neighbours follow them for as long as their 2-adic agreement lasts.
- Every cylinder also contains shadows from below of positive rational cycles.

A complete recursion therefore has to control growing excursions of unbounded length. That is the divergence half, and no local identity supplies it.

## 3. One integrality fact, and why it does not reach divergence

**Contracting cycles can be followed only briefly.** Take a positive rational cycle point `c = a/d` with `d > 1` and multiplier `λ = 3^k/2^m < 1`. An integer orbit following its word from below satisfies `x' − c = λ(x − c)`. Since `|x − c| ≥ 1/d` for every integer `x`, it can follow for at most `log(d·|x₀ − c|)/log(1/λ)` cycles. Discreteness of the integers is what forces it off.

**Expanding cycles give nothing.** For the expanding negative cycles that drive growth, the same argument says nothing. The orbit moves away from `c`, which integers are free to do. The only limit is 2-adic agreement, and that budget grows with the orbit's bit length.

**Conclusion.** The divergence half cannot follow from archimedean discreteness, or from 2-adic data, on their own.

## 4. Candidates, ranked by what each would need

1. **Divergence half, the same for all `d`:**
   - **(a) Arithmetic of the parity-vector conjugacy** (Lagarias; Bernstein–Lagarias). Show that the conjugacy sends rationals to rationals. This needs structure in that map that forces eventual periodicity, such as a Mahler-type functional equation or automaton structure. Whether any such structure exists is unknown.
   - **(b) Quantitative ergodic route** (Tao, 2019: almost all orbits attain almost bounded values). Passing from "almost all" to "all" means ruling out a measure-zero set of conspiring orbits, and no current tool does that.
   - **(c) Growth-budget accounting.** A growing orbit has to keep renewing growing 2-adic patterns, each no longer than its current bit length. Find a cost per renewal that accumulates. A first look found no contradiction from counting or compression alone; this is open-ended.
2. **Cycle half, specific to `d`:** Baker-type bounds plus verification. The method is known and works partially, and the rule machinery is not needed for it.

## 5. Proposed next step for this lane

Take 1(a) and 1(c) one level deeper, each with a test that could fail:

- **1(a).** For rationals with small denominators, measure preperiod length against height. A uniform linear law would hint at structure; scattered outliers would argue against it.
- **1(c).** Measure how integer orbits renew growing patterns over long excursions, using records of slow orbits. Check whether renewal costs show an invariant that a proof could use.

Expectation: a sharper map of why this half is hard is the most likely outcome.
