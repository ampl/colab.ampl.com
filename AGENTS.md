# Instructions for AI assistants

This repository holds the notebooks of the AMPL Model Colaboratory
(https://colab.ampl.com). The website is built from the notebooks' first
(header) cell, so keep that cell in the format below. The contribution guide is
in [README.md](README.md) and [docs/source/contribute.rst](docs/source/contribute.rst).

## Notebook header fields for search and filters

Every notebook's header cell has a hidden block, right after the `Tags:` line,
that feeds the notebook search and filters on the website:

```
Tags: educational, gurobi, energy, hydrogen, mp

<!--
Domain: Energy
Subdomain: Hydrogen Production
Model type: MILP
Level: Case Study
Algorithm: Rolling Horizon
Subject: Hydrogen Facility Operations
-->

Notebook author: Eduardo Salazar <<eduardo@ampl.com>>
```

When you create a notebook, or change what a notebook's model does, fill in or
update this block:

- `Domain`, `Model type` and `Level` are required. Use only values listed in
  [docs/finder-values.json](docs/finder-values.json), spelled exactly as there.
  Prefer an existing value even when it is not a perfect fit; add a new value to
  that file only when none fits, and say so in your summary of the change.
- `Subdomain`, `Algorithm` and `Subject` are optional free text. Reuse wording
  from other notebooks where possible (search the repository for `Subdomain:`).
  Leave a field out rather than writing it empty, `-` or `N/A`.
- Several values go on one line, separated by commas (`Domain: Retail, Sales`).
  Use one value per field unless the notebook really covers several.
- Keep the fields inside `<!--` and `-->`, one per line. They are not displayed
  in the notebook.

### Choosing the model type

Read the model (`%%ampl_eval` / `%%writefile` cells or `.mod` files), not only
the title:

1. `complements` in the model: `Complementarity`; a bilevel model reformulated
   with KKT conditions: `MPEC`.
2. Scenarios or uncertainty as part of the formulation (two-stage, Benders over
   scenarios): `Stochastic MILP`.
3. Cone constraints (second-order, exponential): `Conic`.
4. Otherwise, by the variables and expressions:
   - only continuous variables, everything linear: `LP`
   - `binary` or `integer` variables, everything linear (logical constraints
     such as `==>`, `or` and `alldiff` handled by MP count as linear): `MILP`
   - quadratic objective, linear constraints: `QP`, or `MIQP` with integer
     variables
   - other nonlinear terms (products of variables, `exp`, `log`, `sin`,
     powers): `NLP`, or `MINLP` with integer variables
5. A model solved with a constraint programming solver: `CP`.

### Choosing the level

- `Quick Start`: setup and first steps (installing amplpy, loading data).
- `Lecture`: teaching material, introductions, and tutorials on AMPL or amplpy
  features (e.g. infeasibility diagnosis, options, output handlers).
- `Case Study`: a worked optimization problem from start to finish.
- `Industry Prototype`: a realistic business model close to industrial use.

### Examples

```
<!--
Domain: Operations Research
Subdomain: Mathematical Programming
Model type: LP
Level: Lecture
Algorithm: Debugging Infeasibility
Subject: Debugging Infeasibility
-->
```

```
<!--
Domain: Operations Research
Subdomain: Bilevel Optimization
Model type: MPEC
Level: Lecture
Algorithm: KKT Reformulation
Subject: Stackelberg Game
-->
```

## Checking your changes

Run the header check from the repository root; it also runs in CI:

```
python scripts/check_headers.py
```

It reports missing required fields, values not in
[docs/finder-values.json](docs/finder-values.json), empty fields, repeated
fields and fields outside the `<!-- -->` block.

## Other rules

- Do not change the first two code cells ("Install dependencies" and "Google
  Colab & Kaggle integration") beyond the list of modules and the packages to
  install; `scripts/headers.py` regenerates them.
- Notebooks of an author go in `authors/<github_username>/`.
