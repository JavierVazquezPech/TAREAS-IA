# Forward and Backward Chaining

Practice definite-clause inference (Russell & Norvig, AIMA ch. 9) on a
**knowledge base you can edit**. The default KB is the lecture example:
`Mortal(Tom)?` with an extra cat (Felix) and an extra rule (`Maulla`) so
forward chaining does extra work that backward chaining skips.

## Setup

```bash
cd "Razonamiento lógico/project"
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows (PowerShell):

```powershell
cd "Razonamiento lógico/project"
python3 -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Later sessions: activate the venv again, then run the programs.
Deactivate with `deactivate`.

## Programs

| File | Role |
|---|---|
| `01_show_kb.py` | Print facts, rules, and the query |
| `02_forward_chaining.py` | Data-driven: fire every applicable rule |
| `03_backward_chaining.py` | Goal-driven: reduce the query to facts |
| `04_compare.py` | Run both and list extra facts FC inferred |

```bash
python 01_show_kb.py
python 02_forward_chaining.py
python 03_backward_chaining.py
python 04_compare.py
python 04_compare.py --kb kb/west.yaml
python 02_forward_chaining.py --query "Maulla(Felix)"
```

## Edit the knowledge base

Open `kb/cats.yaml` (or copy it). Syntax:

```yaml
facts:
  - Gato(Tom)

rules:
  - id: R1
    if: [Gato(x)]
    then: Animal(x)

query: Mortal(Tom)
```

- **Variables** start with a lowercase letter: `x`, `y`, `person`
- **Constants** start with an uppercase letter: `Tom`, `West`, `M1`
- Quote atoms that contain commas, e.g. `"Sells(x, y, z)"`, so YAML keeps them as one string.

A second example, the AIMA criminal KB, is in `kb/west.yaml`.

## What to expect (`kb/cats.yaml`, query `Mortal(Tom)`)

- **Forward chaining** infers `Animal(Tom)`, `Animal(Felix)`, `Maulla(Tom)`,
  `Maulla(Felix)`, `Mortal(Tom)`, and also `Mortal(Felix)`.
- **Backward chaining** only walks `Mortal(Tom)` ← `Animal(Tom)` ← `Gato(Tom)`.
  It never uses Felix or `Maulla`.
- Both answer **YES**. The difference is the *path* through the KB.
