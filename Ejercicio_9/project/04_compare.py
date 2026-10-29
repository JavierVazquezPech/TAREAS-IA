#!/usr/bin/env python3
"""Program 4: run both algorithms and contrast what each one visits."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from logic.backward import backward_chain  # noqa: E402
from logic.cli import build_parser, load_problem  # noqa: E402
from logic.forward import forward_chain  # noqa: E402
from logic.kb import format_kb  # noqa: E402


def main() -> None:
    parser = build_parser("Compare forward vs backward chaining on the same KB.")
    args = parser.parse_args()
    kb, query = load_problem(args)
    print(format_kb(kb))
    print()

    fc = forward_chain(kb, query)
    bc = backward_chain(kb, query)

    print("Forward chaining")
    print("-" * 50)
    for event in fc.events:
        print(event.message)
    print()
    print("Backward chaining")
    print("-" * 50)
    for event in bc.events:
        print(event.message)
    print()
    print("Contrast")
    print("-" * 50)
    print(f"Query {query}:  FC={'YES' if fc.proved else 'NO'}  BC={'YES' if bc.proved else 'NO'}")
    print("Facts FC inferred:  " + (", ".join(str(a) for a in fc.inferred) or "(none)"))
    print("Goals BC visited:   " + (", ".join(str(a) for a in bc.inferred) or "(none)"))
    extra = [a for a in fc.inferred if str(a) not in {str(g) for g in bc.inferred} and a != query]
    if extra:
        print("FC extra work (not needed by BC):  " + ", ".join(str(a) for a in extra))


if __name__ == "__main__":
    main()
