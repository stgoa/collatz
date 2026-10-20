---
id: ansari-2025-recursive-sieve
kind: source
title: "Ansari (2025): recursively sufficient sets and a ternary-digit sieve"
status: cited
citation: >
  Ansari, 2025 paper defining recursively sufficient sets for the 3x+1 problem and proposing a ternary-digit
  sieve, PDF at https://nntdm.net/papers/nntdm-31/NNTDM-31-3-471-480.pdf; Lemma 3.1, printed page 478. Only
  the author's surname, the year, the URL and the lemma and page are recorded in the legacy text; the full
  title, the author's given name and the venue details were not recorded and were not verified at the
  migration (the file name suggests volume 31, issue 3, pages 471–480 of the series hosted at nntdm.net).
url: https://nntdm.net/papers/nntdm-31/NNTDM-31-3-471-480.pdf
created: 2026-10-17
tags: [sufficient-sets, sieve, external-check]
---

# Ansari (2025): recursively sufficient sets and a ternary-digit sieve

## Citation

Ansari (2025), the paper at [nntdm.net](https://nntdm.net/papers/nntdm-31/NNTDM-31-3-471-480.pdf); Lemma 3.1 and the concluding equality `F_(n+1) = F'_n \ A'` of its proof on printed page 478. The repository's legacy text records only this much: author surname, year, URL, lemma and page. The full bibliographic data (title, given name, journal volume and pages) are not recorded here and must be checked against the PDF before being added.

## What we use

Nothing as a premise. The paper defines recursively sufficient sets and proposes a sieve that removes ternary-digit classes; the repository checked one displayed step before importing it, found it false ([`ansari-sieve-step-counterexample`](../areas/convergence/results/ansari-sieve-step-counterexample/README.md)), and therefore uses neither the lemma, nor the sieve, nor the paper's reported verification extension. The elementary definition of a recursively sufficient set and the smaller-seed induction principle are standard and unaffected.

## How it is checked

`cited`. The main lane read the primary PDF on 2026-10-17 and checked the finite set arithmetic of the one displayed identity; the paper's theorem itself was not checked and is not claimed false.
