"""Shared CLI helpers."""

from __future__ import annotations

import argparse
from pathlib import Path

from logic.atoms import Atom, parse_atom
from logic.forward import InferenceResult
from logic.kb import KnowledgeBase, load_kb

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_KB = ROOT / "kb" / "cats.yaml"


def build_parser(description: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--kb", type=Path, default=DEFAULT_KB, help="YAML knowledge base")
    parser.add_argument("--query", default=None, help="Override the query in the YAML file")
    return parser


def load_problem(args: argparse.Namespace) -> tuple[KnowledgeBase, Atom]:
    kb = load_kb(args.kb)
    if args.query:
        query = parse_atom(args.query)
    elif kb.query is not None:
        query = kb.query
    else:
        raise SystemExit("No query: set 'query:' in the YAML file or pass --query")
    return kb, query


def print_result(title: str, result: InferenceResult) -> None:
    print(title)
    print("-" * 50)
    for event in result.events:
        print(event.message)
    print("-" * 50)
    status = "YES" if result.proved else "NO"
    print(f"Proved: {status}")
    if result.inferred:
        label = "Inferred facts" if "Forward" in title else "Goals visited"
        print(f"{label}: " + ", ".join(str(a) for a in result.inferred))
