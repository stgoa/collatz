---
id: evertse-1984-sums-of-s-units
kind: source
title: "Evertse: vanishing sums of integers with small parts outside a fixed set of primes"
status: cited
citation: >
  J.-H. Evertse, "On sums of S-units and linear recurrences", Compositio Mathematica 53 (1984), no. 2,
  225-244; Numdam item CM_1984__53_2_225_0; MR 766298; Zbl 0547.10008. Corollary 1, page 227, read in the
  Numdam scan.
url: https://www.numdam.org/item/CM_1984__53_2_225_0/
created: 2026-11-23
tags: [diophantine-approximation, s-units, subspace-theorem, ineffective]
---

# Evertse: vanishing sums of integers with small parts outside a fixed set of primes

## Citation

J.-H. Evertse, *On sums of S-units and linear recurrences*, Compositio Mathematica 53 (1984), no. 2, 225–244,
[Numdam item CM_1984__53_2_225_0](https://www.numdam.org/item/CM_1984__53_2_225_0/) (MR 766298, Zbl 0547.10008).
Pages 226 to 228 of the Numdam scan were read on 2026-11-23. The statement below is Corollary 1 on page 227,
transcribed into plain text. In the paper `||x||` is defined by its equation (2); for rational integers it is
`max |x_k|`. For a prime `p`, `|x|_p` is the `p`-adic absolute value.

**Corollary 1.** Let `c, d` be constants with `c > 0`, `0 <= d < 1`, let `S_0` be a finite set of prime
numbers and let `n` be a positive integer. Then there are only finitely many tuples `x = (x_0, x_1, ..., x_n)`
of rational integers such that

```
x_0 + x_1 + ... + x_n = 0;                                                    (9)
x_(i_0) + x_(i_1) + ... + x_(i_s) != 0                                        (10)
    for each proper, non-empty subset {i_0, i_1, ..., i_s} of {0, 1, ..., n};
gcd(x_0, x_1, ..., x_n) = 1;                                                  (11)
product over k = 0..n of ( |x_k| * product over p in S_0 of |x_k|_p )  <=  c * ||x||^d.      (12)
```

The paper derives it from its Theorem 1, the same statement for projective points over a number field, and
derives Theorem 1 from its Theorem 2, which it bases on "Schlickewei's p-adic version of the method of
Thue-Siegel-Roth-Schmidt" (introduction, page 225).

## What we use

`S_0 = {2, 3}` and `n = 2` or `n = 3`. The factor `|x_k| |x_k|_2 |x_k|_3` is the part of `|x_k|` that is
coprime to 6. So the corollary says: among the vanishing sums of three or four nonzero integers, with no
vanishing proper subsum and no common factor, only finitely many have the product of their parts coprime to 6
at most `c` times a fixed power `d < 1` of the largest term.

For three terms this is the situation treated with
[Ridout's theorem](ridout-1958-p-adic-roth.md) in
[`half-period-four-mismatch-finiteness`](../areas/cycles/results/half-period-four-mismatch-finiteness/README.md).
The four-term case is what
[`half-period-six-mismatch-finiteness`](../areas/cycles/results/half-period-six-mismatch-finiteness.md) needs.

**The corollary is ineffective as used here.** The paper gives no bound for the tuples, and its proof goes
through the p-adic Thue–Siegel–Roth–Schmidt theorem. Every result resting on it is a finiteness statement
without an explicit bound. The word "ineffective" is ours; it was not found in the pages read.

## How it is checked

`cited`. Not reproduced and not formalised. The statement was read in the scanned pages themselves, because the
text layer of the scan drops the displayed formulas. The proofs in the paper were not checked.
