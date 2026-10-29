#!/usr/bin/env python3
"""Program 2: forward chaining on a YAML knowledge base."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from logic.cli import build_parser, load_problem, print_result  # noqa: E402
from logic.forward import forward_chain  # noqa: E402


def main() -> None:
    parser = build_parser("Forward chaining: fire every applicable rule from the facts.")
    args = parser.parse_args()
    kb, query = load_problem(args)
    result = forward_chain(kb, query)
    print_result("Forward chaining", result)


if __name__ == "__main__":
    main()
