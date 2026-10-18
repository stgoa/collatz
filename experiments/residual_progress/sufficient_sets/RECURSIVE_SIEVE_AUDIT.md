# A failed set identity in a potentially relevant sieve proof

**Status: exact counterexample to one displayed proof step; no claim that
the paper's theorem is false.**

Ansari's [2025 paper](https://nntdm.net/papers/nntdm-31/NNTDM-31-3-471-480.pdf)
defines recursively sufficient sets and proposes a ternary-digit sieve.
We checked Lemma3.1 before importing that sieve. Its concluding equality
on printed page478, `F_(n+1)=F'_n\A'`, fails already at n=1:

| Set | Residues modulo36 |
|---|---|
| F2 | 3,7,15,19 |
| F'1 | 3,7,11,15,19,23,27,31,35 |
| A' | 35 |
| F'1 minus A' | 3,7,11,15,19,23,27,31 |

Thus11 belongs to the asserted right side but not the left. Removing
only the top-digit pair(2,2) does not restrict both digits to{0,1}.
The recursive sufficiency of the four additional removed classes needs
a separate argument. The displayed proof does not supply it.

We therefore do not use this lemma, the resulting sieve, or the reported
verification extension as premises. The elementary definition and
smaller-seed induction principle are unaffected. Our R37/R38 reductions
have their own explicit currents and input dependencies.

Reproduce the finite set arithmetic:

```sh
python3 experiments/residual_progress/sufficient_sets/check_recursive_sieve.py
```
