# Papers

Typeset expositions, one folder per paper: `papers/<slug>/<slug>.tex`, with an optional `.bib`. A paper presents nodes in readable form and cites them by id. It adds no claims of its own: every claim in a paper is a node in `areas/`. Commit LaTeX sources only, never build output.

Build a paper locally, for example with `latexmk -pdf <slug>.tex`; `.gitignore` excludes the common build outputs.

| Paper | Presents |
|---|---|
| [`right-aligned-reduction/`](right-aligned-reduction/README.md) | The main lane's proof note of the packet-currents programme (R2 to about R94), kept byte-identical to its legacy version |
