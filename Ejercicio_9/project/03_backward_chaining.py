#!/usr/bin/env python3
"""Program 3: backward chaining on a YAML knowledge base."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from logic.backward import backward_chain  # noqa: E402
from logic.cli import build_parser, load_problem, print_result  # noqa: E402


def main() -> None:
    parser = build_parser("Backward chaining: reduce the query until it hits facts.")
    args = parser.parse_args()
    kb, query = load_problem(args)
    result = backward_chain(kb, query)
    print_result("Backward chaining", result)


if __name__ == "__main__":
    main()
