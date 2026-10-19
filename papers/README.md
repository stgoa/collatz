# Papers

Typeset write-ups (LaTeX). Each paper is one folder `papers/<slug>/` containing `<slug>.tex` and an optional `.bib`.

Build it locally, for example with `latexmk -pdf <slug>.tex`. Do **not** commit PDFs or build artifacts; `.gitignore` excludes the common ones.

| Paper | Contents | Status |
|---|---|---|
| [`right_aligned_reduction/`](right_aligned_reduction/right_aligned_reduction.tex) | The proof note of the packet-currents programme: the right-aligned reduction and the rounds up to about R94 (9,027 lines). Its finite checks are in [`collatz_research_20261017/`](../collatz_research_20261017/). | frozen; byte-identical to its last version on `main` |

A new paper should cite the result folders it is based on. Its claims must match the status labels of those results.
