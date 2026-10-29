#!/usr/bin/env python3
"""Program 1: print the knowledge base."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from logic.cli import build_parser  # noqa: E402
from logic.kb import format_kb, load_kb  # noqa: E402


def main() -> None:
    parser = build_parser("Show facts, rules, and query from a YAML knowledge base.")
    args = parser.parse_args()
    kb = load_kb(args.kb)
    print(format_kb(kb))
    print()
    print("Variables start with a lowercase letter (x). Constants start with uppercase (Tom).")
    print("Edit the YAML file, then rerun this program.")


if __name__ == "__main__":
    main()
