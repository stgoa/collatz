---
id: inverse-syracuse-binary-coding
kind: result
title: "Two inverse Syracuse branches give an injective, decodable coding of binary words by convergent integers"
status: written
claim: >
  Odd-only 3x+1 map S. On U = {n ≥ 1 odd, 3 ∤ n} define G_b(n) = (2^(a_b(n mod 9))·n − 1)/3 for b ∈ {0, 1}, with
  a_0 = (4, 3, 6, 3, 4, 5) and a_1 = (8, 7, 8, 9, 10, 7) on the residues n ≡ 1, 2, 4, 5, 7, 8 (mod 9), and set
  Γ(empty) = 1, Γ(b·w) = G_b(Γ(w)). Then each G_b maps U into U with G_b(n) > 2n and S(G_b(n)) = n with valuation
  exactly a_b(n mod 9); the valuations of G_0 lie in [3, 6] and those of G_1 in [7, 10]. Consequently Γ is injective,
  the forward orbit of Γ(w) reads w back (the valuation band gives each bit) and reaches 1 after exactly |w| odd
  steps, 2^|w| < Γ(w) < 2^(10|w|) for nonempty w, and membership in the codebook Γ({0,1}*) is decided in O(log x)
  steps by running the orbit and checking each valuation against the table. Every codeword converges. The construction
  is specific to 3x+1 only through the table; analogous tables exist for 3x+d.
authors:
  - Claude cycles lane (Opus 5.5; directed by Santiago Armstrong)
  - ChatGPT main lane (Codex), the original construction, archived in archive/handoff/COLLATZ_PROGRAMME_MASTER_HANDOFF.md §13.2
created: 2026-11-01
depends_on: []
certificates: [check_binary_coding.py]
evidence:
  - "binary_coding.json: the receipt; the exponent table and bands, 133,334 checked pairs (n, b), the 32,767 words of length ≤ 14 decoded uniquely, the 51 codewords below 2^22 recognised exactly, and 182,008 index sequences of 300 random PCP instances"
tags: [decidability, inverse-syracuse, coding, free-monoid, pcp]
---

# Two inverse Syracuse branches give an injective, decodable coding of binary words by convergent integers

## Statement

`S(n) = (3n + 1)/2^(v₂(3n+1))` on odd `n`; `U = {n ≥ 1 : n odd, 3 ∤ n}`. For `b ∈ {0, 1}` and `n ∈ U` put

```
G_b(n) = (2^(a_b(n mod 9)) · n − 1) / 3,

  n mod 9   |  1   2   4   5   7   8
  a_0       |  4   3   6   3   4   5
  a_1       |  8   7   8   9  10   7
```

and define `Γ(empty) = 1`, `Γ(b·w) = G_b(Γ(w))`, so `Γ(b_1 b_2 ⋯ b_m) = G_(b_1)(G_(b_2)(⋯G_(b_m)(1)))`.

**Theorem.**
1. For `n ∈ U`: `G_b(n) ∈ U`, `G_b(n) > 2n`, and `S(G_b(n)) = n` with valuation exactly `a_b(n mod 9)`.
2. The forward orbit of `Γ(w)` passes through `Γ` of the successive suffixes of `w` and reaches 1 after exactly `|w|` odd steps; the `i`-th valuation lies in `[3, 6]` if `b_i = 0` and in `[7, 10]` if `b_i = 1`.
3. `Γ` is injective, and `2^|w| < Γ(w) < 2^(10|w|)` for nonempty `w`.
4. The codebook `Γ({0,1}*)` is decidable: from odd `x`, repeatedly compute `v = v₂(3x + 1)` and `n = (3x + 1)/2^v`; reject unless `3 ∤ n`, `v` lies in a band, and `v` equals the table entry of that band at `n mod 9`; accept on reaching 1. Each accepted step more than halves `x`, so the decoder stops after `O(log x)` steps.

In words: the inverse tree of the Syracuse map contains a copy of the free monoid on two generators acting on positive integers, with an explicit, efficiently decodable codebook, and every point in it converges.

## Proof

(1) For `n ∈ U` and each table entry, `2^a·n ≡ 4` or `7 (mod 9)` (check the twelve entries: e.g. `n ≡ 1`, `a = 4`: `16 ≡ 7`). Hence `2^a n ≡ 1 (mod 3)`, so `3 | 2^a n − 1`; `2^a n − 1` is odd, so `G_b(n)` is odd; and `2^a n − 1 ≢ 0 (mod 9)`, so `3 ∤ G_b(n)`. Since `a ≥ 3`, `G_b(n) ≥ (8n − 1)/3 > 2n`. Finally `3G_b(n) + 1 = 2^a n` with `n` odd, so `v₂(3G_b(n) + 1) = a` and `S(G_b(n)) = n`.

(2) By induction on `|w|` using (1): `S(Γ(b·w)) = Γ(w)` with valuation in the band of `b`. At `Γ(empty) = 1` the orbit stops (we count odd steps until 1 is reached); `Γ(w) ≠ 1` for nonempty `w` because `Γ(w) > 2`.

(3) The valuation sequence of the orbit of `Γ(w)` until it reaches 1 determines `w` by (2), and that sequence is a function of `Γ(w)`. The bounds follow from `2n < G_b(n) < 2^10·n`.

(4) If `x = Γ(w)`, the decoder follows (2) and accepts. If the decoder accepts `x`, the recorded bits `b_1, …, b_m` and successors satisfy `x = G_(b_1)(n_1)`, …, `n_(m−1) = G_(b_m)(1)`, because the valuation and the successor determine the predecessor (`x = (2^v n − 1)/3`) and the table check ensures the step is `G_b`; so `x = Γ(b_1⋯b_m)`. Each step has `v ≥ 3`, so `n < x/2`. ∎

## Certificates

[`check_binary_coding.py`](check_binary_coding.py) (standard library, about 4 s): **V1** the twelve table entries and the two bands; **V2** part (1) for every `n ∈ U` below 200,000 and both `b` (133,334 pairs); **V3** parts (2)–(3) for all 32,767 words of length `≤ 14` (decoded, reach 1 in `|w|` odd steps, size bounds, no collisions); **V4** part (4): below `2^22` the decoder accepts exactly the 51 codewords; **V5** the PCP equivalence of [`synchronised-coding-pcp-reduction`](../synchronised-coding-pcp-reduction/README.md) on 300 random instances (182,008 index sequences of length `≤ 5`, 775 solutions); **V6** the receipt [`binary_coding.json`](binary_coding.json).

## Remarks

- **What it is not.** The codewords form a thin (exponentially sparse) set of convergent integers. Nothing here makes the forward dynamics compute anything: the orbit of a codeword just reads its word back. By [`collatz-conjecture-logical-form`](../collatz-conjecture-logical-form/README.md) (d), no coding of this kind can turn "reaches 1" into a halting signal unless the conjecture is false.
- **Relation to other nodes.** The step `(2^a n − 1)/3` is the inverse move used throughout the invariants area (for example [`saturated-sets-meet-residue-classes-six-smooth-moduli`](../../../invariants/results/saturated-sets-meet-residue-classes-six-smooth-moduli/README.md)); there the freedom in `a` steers residues, here it carries one bit. The archived note also records that every finite valuation word has an explicitly convergent completion (`archive/handoff/COLLATZ_PROGRAMME_MASTER_HANDOFF.md` §13.4), which is not migrated here.
- **Controls.** For `3x+d` with `gcd(d, 6) = 1` the same construction works with a table modulo `9` built for the inverse step `(2^a n − d)/3`; the coding is not specific to `d = 1` and says nothing about convergence of other orbits. Novelty undetermined.

## History

- Construction by the ChatGPT main lane (Codex), recorded in the archived master handoff §13.2 (never a node). Migrated, proved in full and certified 2026-11-01 by the Claude cycles lane (Opus 5.5), directed by Santiago Armstrong.
